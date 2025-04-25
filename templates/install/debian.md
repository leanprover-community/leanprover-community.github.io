# How to install Lean 4 on Debian/Ubuntu

Note that these are legacy instructions provided by the community. The recommended
way to install Lean and to create a project is to follow the instructions in
[the official Lean documentation](https://docs.lean-lang.org/lean4/doc/quickstart.html).

## Legacy instructions

This document explains how to get started with Lean and mathlib if you
are using a Linux distribution derived from Debian (Debian itself,
Ubuntu, LMDE,...).

If you get stuck, please come to [the chat room](https://leanprover.zulipchat.com/) to ask for assistance.

Here we will discuss the fast way, assuming a lot of trust from you. It
will install Lean, with supporting tools `elan` and `lake`, as well as the 
code editor VS Code and its Lean plugin, and
other dependencies you probably already have, like `curl` and `git`. 
If you don't like this method, there is a
[detailed webpage](debian_details.html) which will decompose the
process into described stages, and won't ask for a blind `sudo`.

The fast way is: open a terminal and type:
```bash
wget -q https://raw.githubusercontent.com/leanprover-community/mathlib4/master/scripts/install_debian.sh && bash install_debian.sh ; rm -f install_debian.sh && source ~/.profile
```

## Lean Projects

You can now read instructions about creating and working on [Lean projects](project.html)
