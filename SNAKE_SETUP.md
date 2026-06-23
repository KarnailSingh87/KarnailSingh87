# 🐍 GitHub Snake Animation Setup Guide - Complete Step-by-Step

## What is Snake Animation?

The snake animation is a visual representation of your GitHub contributions displayed as a moving snake that "eats" your contribution squares. It creates an animated graph that shows on your GitHub profile README.

**Visual Result**: 
- Every day your snake grows based on your contributions
- It's a fun, animated version of your contribution graph
- Shows your activity in real-time on your profile

---

## ⚙️ COMPLETE SETUP INSTRUCTIONS

### **STEP 1: Create Profile Repository (If Not Exists)**

1. Go to: https://github.com/new
2. Fill in:
   - **Repository name**: `KarnailSingh87` (Must match your GitHub username EXACTLY)
   - **Description**: "Full Stack MERN Developer Portfolio"
   - **Public**: ✅ (Required for snake to work)
3. **Check**: "Add a README file"
4. Click **Create Repository**

---

### **STEP 2: Create GitHub Actions Workflow File**

1. Go to your profile repository: https://github.com/KarnailSingh87/KarnailSingh87
2. Click **"Add file"** → **"Create new file"**
3. In the filename field, type:
   ```
   .github/workflows/generate-snake.yml
   ```
   (GitHub will create the folders automatically)

4. **Copy and paste the entire content below** into the file:

```yaml
name: Generate Snake Animation

on:
  schedule:
    # Runs every day at 00:00 UTC (you can change the time)
    - cron: "0 0 * * *"
  
  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    
    permissions:
      contents: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Generate Snake SVG
        uses: Platane/snk@v3
        with:
          # GitHub username to generate snake for
          github_user_name: KarnailSingh87
          
          # Output locations for the SVGs
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark

      - name: Push changes to output branch
        uses: crazy-max/ghaction-github-pages@v3
        with:
          # Where to push the generated files
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

5. Click **Commit new file**
   - Commit message: `ci: Add snake animation workflow`
   - Click **Commit directly to the main branch**

✅ **Workflow file is now created!**

---

### **STEP 3: Manually Trigger the Workflow**

1. Go to **Actions** tab in your repository
2. Click on **"Generate Snake Animation"** workflow (left sidebar)
3. Click **"Run workflow"** → **"Run workflow"** (blue button)
4. Wait for it to complete (usually 2-3 minutes)

You should see a ✅ checkmark when it's done.

---

### **STEP 4: Verify Output Branch Was Created**

1. Go back to your repository main page
2. Click the **"main"** branch dropdown (near top-left)
3. Look for **"output"** branch
4. Click on it to verify the snake SVG files are there:
   - `github-contribution-grid-snake.svg`
   - `github-contribution-grid-snake-dark.svg`

✅ **If you see these files, the snake is working!**

---

### **STEP 5: Add Snake to Your Profile README**

1. Go to your **README.md** file in the main branch
2. Find a good spot (usually after your GitHub stats section)
3. **Add this code**:

```markdown
## 🐍 My Contribution Snake

![Snake animation](https://raw.githubusercontent.com/KarnailSingh87/KarnailSingh87/output/github-contribution-grid-snake.svg)
```

**OR for Light/Dark mode support**, add:

```markdown
## 🐍 My Contribution Activity

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/KarnailSingh87/KarnailSingh87/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/KarnailSingh87/KarnailSingh87/output/github-contribution-grid-snake.svg">
  <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/KarnailSingh87/KarnailSingh87/output/github-contribution-grid-snake.svg">
</picture>
```

4. **Commit the changes**

✅ **You should now see the snake animation on your profile!**

---

## 🎯 How to Verify It's Working

### **Immediate Check:**
1. Go to your GitHub profile: https://github.com/KarnailSingh87
2. Scroll to the section with the snake animation
3. You should see an animated SVG showing your contributions

### **If Snake Doesn't Appear:**

**Check 1: Actions Tab**
- Go to Actions → "Generate Snake Animation"
- Look for a ✅ or ❌ status
- If ❌, click and view the logs to see what failed

**Check 2: Output Branch**
- Make sure the `output` branch exists
- Make sure SVG files are in it
- Visit the SVG URL directly in browser:
  `https://raw.githubusercontent.com/KarnailSingh87/KarnailSingh87/output/github-contribution-grid-snake.svg`

**Check 3: README Link**
- Make sure the markdown link matches your username
- It should be: `KarnailSingh87/KarnailSingh87` (appears twice)

**Check 4: Repository is Public**
- Go to Settings → Security → Visibility
- Make sure it's set to **Public**
- Private repositories don't work with this method

---

## 🔧 Customization Options

### **Change Update Frequency**

Edit the `cron` schedule in `.github/workflows/generate-snake.yml`

Current: `"0 0 * * *"` (Daily at midnight UTC)

**Examples:**
```yaml
# Every 6 hours
- cron: "0 */6 * * *"

# Every 12 hours  
- cron: "0 0,12 * * *"

# Every day at 3 PM UTC
- cron: "0 15 * * *"

# Every Sunday at midnight
- cron: "0 0 * * 0"
```

### **Change Colors**

The snake animation uses your GitHub contribution colors. You can customize by adding palette options:

```yaml
outputs: |
  dist/github-contribution-grid-snake.svg
  dist/github-contribution-grid-snake-dark.svg?palette=github-dark
  dist/github-contribution-grid-snake-alt.svg?palette=github-light
```

Available palettes: `github-light`, `github-dark`, `haukas`, `chartreuse-dark`, `chartreuse-light`

---

## 📱 Mobile & Desktop Preview

### **How it looks:**
- **Desktop**: Appears as a smooth animated grid pattern
- **Mobile**: Auto-scales to fit screen
- **Both**: Updates daily based on your contributions

---

## 🚀 Advanced: Alternative Methods

### **Method 2: Using Readme Stats with Snake**
Add to README:
```markdown
![snake gif](https://github.com/KarnailSingh87/KarnailSingh87/blob/output/github-contribution-grid-snake.gif)
```

### **Method 3: Animated GIF (Instead of SVG)**
Modify the workflow to generate GIF:
```yaml
outputs: |
  dist/github-contribution-grid-snake.gif?palette=github-dark
```

---

## ⚠️ Troubleshooting

### **Problem: Action Failed**
**Solution**: 
- Check the Actions tab logs
- Make sure username is correct: `KarnailSingh87`
- Make sure repository is public
- Try manually triggering again

### **Problem: SVG Not Loading**
**Solution**:
- Wait 5-10 minutes after workflow completes
- GitHub needs time to update the raw content
- Clear browser cache or open in incognito
- Check if `output` branch exists

### **Problem: Wrong Branch Name**
**Solution**:
- The files must go to `output` branch (not `main`)
- Check workflow file has `target_branch: output`
- Don't manually create the output branch

### **Problem: Snake Looks Strange**
**Solution**:
- Make sure you have contributions in the last 52 weeks
- If account is very new, snake will be small
- Snake grows with more contributions
- Don't worry, it will fill up over time!

---

## 📊 Understanding Your Snake

**What the snake shows:**
- 🟥 **Red/colored squares** = Days with contributions
- ⬜ **White/empty squares** = Days with no contributions
- 🐍 **The snake** = Visual representation of your contribution patterns
- 📈 **Direction** = Snake moves based on contribution density

**More contributions** = **Longer/Fatter Snake** 🐍

---

## 🎁 Bonus: Combine with Other Animations

You can add multiple animations to your README:

```markdown
## 📊 GitHub Activity

### Contribution Snake
![snake gif](https://raw.githubusercontent.com/KarnailSingh87/KarnailSingh87/output/github-contribution-grid-snake.svg)

### GitHub Stats
![stats](https://github-readme-stats.vercel.app/api?username=KarnailSingh87)

### Contribution Streak
[![streak stats](https://streak-stats.demolab.com/?user=KarnailSingh87)](https://git.io/streak-stats)
```

---

## ✅ Final Checklist

- [ ] Created profile repository named `KarnailSingh87`
- [ ] Repository is PUBLIC
- [ ] Created `.github/workflows/generate-snake.yml` file
- [ ] Workflow ran successfully (check Actions tab)
- [ ] `output` branch was created
- [ ] SVG files exist in `output` branch
- [ ] Added snake animation link to README.md
- [ ] Snake appears on your profile
- [ ] Snake updates daily

---

## 🎉 Success Indicators

✅ You'll know it's working when:
1. You see the workflow ✅ in Actions
2. The `output` branch appears in your repo
3. SVG files are in that branch
4. The snake animation displays on your README
5. It updates every day automatically

---

## 📞 Still Having Issues?

1. **Check official repo**: https://github.com/Platane/snk
2. **GitHub Actions status**: Check your Actions tab for logs
3. **Clear cache**: Use Ctrl+Shift+Del in browser
4. **Try incognito mode**: Open profile in private browsing
5. **Wait longer**: Sometimes takes 10-15 minutes to display

---

## 🌟 Pro Tips

- 💡 Keep making contributions to make your snake longer!
- 💡 The snake is most impressive when you have consistent contributions
- 💡 Combine with other GitHub stats widgets for a complete profile
- 💡 Share your profile on LinkedIn to showcase your activity
- 💡 The animation automatically updates every day - no manual work needed!

---

**You're all set! Your snake animation will now run automatically every day! 🐍✨**
