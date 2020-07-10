# How to install Lean and mathlib on MacOS

This document explains how to get started with Lean and mathlib if you
are using MacOS.

If you get stuck, please come to [the chat room](https://leanprover.zulipchat.com/) to ask for assistance.

## Installing Lean and mathlib

Here we will discuss the fast way, assuming a lot of trust from you. It
will install Lean, with supporting tools `elan` and `leanpkg`,
the supporting tool `leanproject` for Lean's mathematical
library, as well as the code editor VS Code and its Lean plugin, and
other dependencies you probably already have, like `curl`, `git`,
`python3`, and `pipx`. If you don't like this method, there is a
[detailed webpage](macos_details.html) which will decompose the
process into described stages, and won't ask for a blind `sudo`.

The fast way is: open a terminal and type:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/leanprover-community/mathlib-tools/master/scripts/install_macos.sh)" && source ~/.profile
```

You can now read instructions about creating and working on [Lean projects](project.html).
If you encounter any `command not found` errors when opening a new terminal,
logging out from MacOS and logging in again should fix it.
