# GitHub Profile README Setup Guide

This profile README includes advanced features and auto-updating components.

## Features

### 1. **ASCII Art Header**
- Custom ASCII art name display
- Monochrome design for professional look

### 2. **Typing Animation**
- Rotating text showing expertise areas
- Uses readme-typing-svg for dynamic effect

### 3. **Python Class Bio**
- Code-style personal information
- Clean, developer-focused presentation

### 4. **Expertise Matrix**
- Five core domains with detailed capabilities
- Terminal-style formatting

### 5. **GitHub Metrics**
- Stats card with contribution counts
- Streak statistics
- Top languages chart
- Productive time analysis
- Profile activity graph

### 6. **Auto-Updating Language Stats**
- Real language distribution from your repos
- ASCII progress bars
- Updates every 6 hours via GitHub Actions

### 7. **Tech Stack Icons**
- Pure icon display (no labels)
- 24+ technology icons
- Organized by domain

### 8. **Contribution Snake**
- Animated snake eating your contributions
- Dark theme matching profile
- Updates every 12 hours

### 9. **Recent Activity**
- Last 5 GitHub activities
- Auto-updates every 6 hours

### 10. **Profile Views Counter**
- Tracks profile visits
- Monochrome badge

## Automation

### Workflows

1. **update-readme.yml** - Updates language statistics every 6 hours
2. **snake.yml** - Generates contribution snake animation every 12 hours
3. **activity.yml** - Updates recent activity section every 6 hours

### Manual Triggers

All workflows can be manually triggered from the Actions tab:
- Go to Actions
- Select workflow
- Click "Run workflow"

## Customization

### Change Colors

All components use monochrome theme:
- Background: `0d1117`
- Primary text: `ffffff`
- Secondary text: `888888`
- Accent: `555555`

### Add More Icons

Visit [devicons](https://devicons.github.io/devicon/) to find more technology icons.

Format:
```html
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/TECH/TECH-original.svg" width="40" height="40"/>
```

### Modify Update Frequency

Edit the cron schedule in workflow files:
- `0 */6 * * *` = every 6 hours
- `0 */12 * * *` = every 12 hours
- `0 0 * * *` = daily at midnight

## Troubleshooting

### Snake not showing
- Wait for first workflow run
- Check Actions tab for errors
- Ensure `output` branch exists

### Stats not loading
- Vercel services may be slow
- Try refreshing after a few minutes
- Check if username is correct

### Language stats not updating
- Verify GITHUB_TOKEN has repo access
- Check workflow logs in Actions tab
- Ensure markers exist in README

## Credits

- [github-readme-stats](https://github.com/anuraghazra/github-readme-stats)
- [github-readme-streak-stats](https://github.com/DenverCoder1/github-readme-streak-stats)
- [readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg)
- [snk](https://github.com/Platane/snk)
- [github-activity-readme](https://github.com/jamesgeorge007/github-activity-readme)
- [devicons](https://devicons.github.io/devicon/)
