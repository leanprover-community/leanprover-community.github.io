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

Specifically, `elan` – which is otherwise recommended (and installed)
as part of the above instructions – will not be able to fetch Lean binaries on
these devices.

Until [a separate M1 installation is
automated](https://github.com/leanprover-community/mathlib-tools/issues/107),
manual compilation of Lean is required on Apple ARM hardware.

There is a [Zulip thread](https://leanprover.zulipchat.com/#narrow/stream/113489-new-members/topic/M1.20macs)
with some interim further details and advice. If you have trouble, feel free to ask for help.

## Lean Projects

You can now read instructions about creating and working on [Lean projects](project.html)

If you encounter any `command not found` errors when opening a new terminal,
logging out from MacOS and logging in again should fix it.
