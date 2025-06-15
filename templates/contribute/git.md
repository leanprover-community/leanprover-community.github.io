# Git Guide for Mathlib4 Contributors

This guide is designed for mathematicians who are new to git but want to contribute to mathlib4. We'll walk through the essential git workflows step by step.

## Prerequisites

Before starting, make sure you have:
- Git installed on your computer
- A GitHub account
- (Optional but recommended) The GitHub CLI tool (`gh`) installed

## Step 1: Fork the Repository on GitHub

First, you need to create your own copy (fork) of the mathlib4 repository:

1. Go to https://github.com/leanprover-community/mathlib4
2. Click the "Fork" button in the top right corner
3. Choose your GitHub account as the destination
4. Wait for GitHub to create your fork

You only ever need to do this step once. You can reuse your fork for many different branches and pull requests.

## Step 2: Get a Local Copy of the Repository

You have two options depending on whether you already have a clone of mathlib4:

### Option A: If you don't have mathlib4 cloned yet

Clone your fork (not the original repository):

```bash
# Replace YOUR_USERNAME with your GitHub username
git clone https://github.com/YOUR_USERNAME/mathlib4.git
cd mathlib4
```

This automatically sets up your fork as the `origin` remote, which is what we want.

### Option B: If you already have mathlib4 cloned

If you already have a clone from the original repository, you can reuse it. Just navigate to your existing mathlib4 directory:

```bash
cd path/to/your/existing/mathlib4
```

## Step 3: Set Up Remotes Correctly

The remote setup depends on which option you chose above:

### If you cloned your fork (Option A)

You need to add the original repository as `upstream`:

```bash
# Add the original repository as 'upstream'
git remote add upstream https://github.com/leanprover-community/mathlib4.git
```

### If you used an existing clone (Option B)

You need to rename the existing remote and add your fork:

```bash
# Rename the existing remote to 'upstream'
git remote rename origin upstream

# Add your fork as 'origin' (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/mathlib4.git
```

### Verify Your Remotes

Regardless of which option you chose, verify your remotes are set correctly:

```bash
git remote -v
```

You should see:
```
origin    https://github.com/YOUR_USERNAME/mathlib4.git (fetch)
origin    https://github.com/YOUR_USERNAME/mathlib4.git (push)
upstream  https://github.com/leanprover-community/mathlib4.git (fetch)
upstream  https://github.com/leanprover-community/mathlib4.git (push)
```

## Step 4: Configure the Master Branch

Make sure your `master` branch tracks `upstream/master`:

```bash
git branch --set-upstream-to=upstream/master master
```

## Step 5: Keep Your Master Branch Up to Date

Always keep your `master` branch synchronized with upstream:

```bash
git checkout master
git pull
```

Run these commands regularly, especially before creating new branches.

## Step 6: Prevent Accidental Commits to Master

To avoid accidentally committing directly to `master`, you can set up a pre-commit hook:

```bash
# Create the hook file
mkdir -p .git/hooks
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/sh
branch="$(git rev-parse --abbrev-ref HEAD)"
if [ "$branch" = "master" ]; then
  echo "You can't commit directly to master branch"
  exit 1
fi
EOF

# Make it executable
chmod +x .git/hooks/pre-commit
```

## Step 7: Create and Configure New Branches

### Set Default Push Behavior

Configure git to push new branches to `origin` by default:

```bash
git config push.default current
git config push.autoSetupRemote true
```

### Create a New Branch

Always create new branches from an up-to-date `master`:

```bash
# Make sure master is up to date
git checkout master
git pull

# Create and switch to a new branch
git checkout -b my-feature-branch
```

The branch will automatically track `origin/my-feature-branch` when you first push it.

## Step 8: Push Your Branch and Open a PR

### Push Your Branch

After making your changes and commits:

```bash
git push origin my-feature-branch
```

### Open a Pull Request

1. Go to your fork on GitHub: `https://github.com/YOUR_USERNAME/mathlib4`
2. You should see a banner suggesting to open a PR for your recent push
3. Click "Compare & pull request"
4. Fill in the PR title and description
5. Click "Create pull request"

Alternatively, if you have the GitHub CLI installed:

```bash
gh pr create --title "Your PR Title" --body "Description of your changes"
```

## Step 9: Working with Others' PRs

### Method 1: Manual Checkout

To check out someone else's PR manually:

```bash
# Add their fork as a remote (replace USERNAME with their GitHub username)
git remote add contributor-name https://github.com/USERNAME/mathlib4.git

# Fetch their branches
git fetch contributor-name

# Checkout their branch
git checkout contributor-name/their-branch-name
```

### Method 2: Using GitHub CLI (Recommended)

This is much simpler:

```bash
# Checkout PR #1234
gh pr checkout 1234
```

This automatically handles the remote setup and branch checkout.

## Step 10: Giving Collaborator Access

If you want to allow others to push directly to your PR branch:

1. Go to your fork: `https://github.com/YOUR_USERNAME/mathlib4`
2. Click "Settings" tab
4. Click "Collaborators" (you may have to reauthenticate)
5. Enter their GitHub username
6. Choose "Write" permission level
7. Send the invitation

Once they accept, they can push directly to your PR branches.

## ⚠️ Security Warning

**Important**: When you give someone collaborator access to your fork, or when you checkout and run someone else's code, you are potentially running unreviewed code on your computer. Only collaborate with people you trust, as they could potentially include malicious code that runs during the build process.

## Getting Help

If you encounter issues or have questions about git workflows, please ask in the `#new users` stream on the [Lean Zulip chat](https://leanprover.zulipchat.com). The community is very helpful and welcomes questions from newcomers!

## Quick Reference

Here's a summary of the most common commands you'll use:

```bash
# Update master and push to your fork
git checkout master
git pull

# Create a new branch
git checkout -b new-branch-name

# Push your branch and set up tracking
git push origin new-branch-name

# Check out someone else's PR
gh pr checkout PR_NUMBER

# Check remote configuration
git remote -v

# Check which branch you're on
git branch
```

## Common Troubleshooting

**Problem**: "Your branch is behind 'upstream/master'"
**Solution**: 
```bash
git checkout master
git pull
```

**Problem**: "fatal: The current branch has no upstream branch"
**Solution**: 
```bash
git push --set-upstream origin branch-name
```

**Problem**: Accidentally committed to your copy of the master branch
**Solution**: 
```bash
# Move the commits to a new branch
git branch new-branch-name
git checkout master
git reset --hard upstream/master
git checkout new-branch-name
```
