# How to install Lean and mathlib on MacOS

This document explains how to get started with Lean and mathlib if you
are using MacOS.

If you get stuck, please come to [the chat room](https://leanprover.zulipchat.com/) to ask for assistance.

There is a [video walkthrough](https://www.youtube.com/watch?v=NOGWsCNm_FY) of these instructions on YouTube.

## Installing Lean and mathlib

### Intel Macs

Here we will discuss the fast way, assuming a lot of trust from you. It
will install Lean, with supporting tools `elan` and `leanpkg`,
the supporting tool `leanproject` for Lean's mathematical
library, as well as the code editor VS Code and its Lean plugin.
If you don't like this method, there is a
[detailed webpage](macos_details.html) which will decompose the
process into described stages, and won't ask for a blind `sudo`.

The fast way is: open a terminal and type:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/leanprover-community/mathlib-tools/master/scripts/install_macos.sh)" && source ~/.profile
```

### M1 Macs / Apple Silicon

Given that GitHub Actions does [not yet support builds on Apple
ARM](https://github.com/actions/virtual-environments/issues/2187), installation
of Lean is for the moment a bit more complex.

Specifically, `elan` – which is installed
as part of the above instructions – will not be able to fetch Lean binaries on
these devices if installed the normal way.

The following instructions are adapted from [Fedor Pavutnitskiy](https://leanprover.zulipchat.com/#narrow/stream/113489-new-members/topic/M1.20Macs.3A.20Installing.20the.20Lean.203.20toolchain/near/262832039), and allow you to install elan through [Rosetta](https://developer.apple.com/documentation/apple-silicon/about-the-rosetta-translation-environment).

1. Open a new terminal window and install XCode Command Line Tools and Rosetta 2 using `xcode-select --install` and `softwareupdate --install-rosetta`.

2. We will install a second, separate x86 installation of Homebrew, which is easiest done by running a shell entirely using Rosetta 2. Do so by running `arch -x86_64 zsh`. The remainder of the commands below should be run from within this `x86`-running window, though once the steps have been completed, the installed tools will work in any future shell.

3. Install a second installation of Homebrew for `x86` with `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`. It will automatically install itself into a second location (`/usr/local`, rather than `/opt/`).

4. Follow the same steps described in [Controlled Installation for macOS](https://leanprover-community.github.io/install/macos_details.html) using the `brew` you just installed:

```
/usr/local/bin/brew install elan mathlibtools
elan toolchain install stable 
elan default stable  
```

5. Use ```leanproject get``` to get the repositories needed.

6. Install vs-code from the website and set it up as usual.

There is a [Zulip thread](https://leanprover.zulipchat.com/#narrow/stream/113489-new-members/topic/M1.20macs)
with some interim further details and advice. If you have trouble, feel free to ask for help.

## Lean Projects

You can now read instructions about creating and working on [Lean projects](project.html)

If you encounter any `command not found` errors when opening a new terminal,
logging out from MacOS and logging in again should fix it.
