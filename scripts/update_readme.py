#!/usr/bin/env python3
import json
import os
import re
import urllib.request
from datetime import datetime, timezone


def fetch_github_data(username):
    """Fetch user and repository data from GitHub API."""
    token = os.environ.get("GITHUB_TOKEN", "")
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"token {token}"

    user_url = f"https://api.github.com/users/{username}"
    repos_url = f"https://api.github.com/users/{username}/repos?per_page=100&type=owner"

    req = urllib.request.Request(user_url, headers=headers)
    with urllib.request.urlopen(req) as response:
        user_data = json.loads(response.read().decode())

    req = urllib.request.Request(repos_url, headers=headers)
    with urllib.request.urlopen(req) as response:
        repos_data = json.loads(response.read().decode())

    return user_data, repos_data


def fetch_language_stats(username, repos):
    """Aggregate language statistics across all repositories."""
    token = os.environ.get("GITHUB_TOKEN", "")
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"token {token}"

    language_bytes = {}

    for repo in repos:
        if repo.get("fork") or repo.get("private"):
            continue
        lang_url = repo["languages_url"]
        try:
            req = urllib.request.Request(lang_url, headers=headers)
            with urllib.request.urlopen(req) as response:
                langs = json.loads(response.read().decode())
                for lang, bytes_count in langs.items():
                    language_bytes[lang] = language_bytes.get(lang, 0) + bytes_count
        except Exception as e:
            print(f"Error fetching languages for {repo['name']}: {e}")

    return language_bytes


def compute_language_bars(language_bytes, top_n=7, bar_width=20):
    """Generate ASCII progress bars for top languages."""
    if not language_bytes:
        return "No language data available yet"

    total_bytes = sum(language_bytes.values())
    sorted_langs = sorted(language_bytes.items(), key=lambda x: x[1], reverse=True)[:top_n]

    lines = []
    for lang, bytes_count in sorted_langs:
        percentage = (bytes_count / total_bytes) * 100
        filled = int((percentage / 100) * bar_width)
        empty = bar_width - filled
        bar = "█" * filled + "░" * empty
        lines.append(f"{lang:<16}{bar}  {percentage:>4.1f}%")

    return "\n".join(lines)


def update_readme(username):
    """Update README.md with fresh GitHub data."""
    print(f"Fetching data for {username}...")
    
    try:
        user_data, repos_data = fetch_github_data(username)
        language_bytes = fetch_language_stats(username, repos_data)

        print(f"Fetched {len(repos_data)} repos, computing language stats...")
        language_section = compute_language_bars(language_bytes)

        readme_path = "README.md"
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Update language section
        langs_pattern = r"(<!-- LANGS_START -->).*?(<!-- LANGS_END -->)"
        langs_replacement = f"\\1\n{language_section}\n\\2"
        content = re.sub(langs_pattern, langs_replacement, content, flags=re.DOTALL)

        # Update timestamp
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        timestamp_pattern = r"<!-- LAST_UPDATED -->"
        timestamp_replacement = f"<!-- LAST_UPDATED {timestamp} -->"
        content = re.sub(timestamp_pattern, timestamp_replacement, content)

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"README updated at {timestamp}")
        
    except Exception as e:
        print(f"Error updating README: {e}")
        raise


if __name__ == "__main__":
    username = "Abhiroop-24"
    update_readme(username)
