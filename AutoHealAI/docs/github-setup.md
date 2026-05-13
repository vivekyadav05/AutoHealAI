# Add AutoHealAI to GitHub

## 1. Create an empty repository on GitHub

1. Open [https://github.com/new](https://github.com/new).
2. Name it (for example `AutoHealAI`).
3. Do **not** add a README, `.gitignore`, or license (this repo already has them).
4. Click **Create repository**.

## 2. Push this folder from your PC

In PowerShell (replace `YOUR_USER` with your GitHub username):

```powershell
cd "C:\Users\Charl\OneDrive\Documents\GitHub\AutoHealAI"
git remote add origin https://github.com/YOUR_USER/AutoHealAI.git
git branch -M main
git push -u origin main
```

If Git asks you to log in, use a [Personal Access Token](https://github.com/settings/tokens) as the password (HTTPS), or set up SSH and use `git@github.com:YOUR_USER/AutoHealAI.git`.

## 3. Why README “links” might not open on GitHub

URLs like `http://localhost:5173` only work **on your computer** while Docker or `npm run dev` is running. GitHub cannot open your localhost. Clone the repo, run the stack locally, then use those URLs in your browser.
