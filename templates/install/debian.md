<div class="alert alert-info">
<p>
We are currently updating the Lean community website to describe working with Lean 4,
but most of the information you will find here today still describes Lean 3.
</p>
<p>
Pull requests updating this page for Lean 4 are very welcome.
There is a link at the bottom of this page.
</p>
<p>
Please visit <a href="https://leanprover.zulipchat.com">the leanprover zulip</a>
and ask for whatever help you need during this transitional period!
</p>
<p>
The website for Lean 3 has been <a href="https://leanprover-community.github.io/lean3/">archived</a>.
If you need to link to Lean 3 specific resources please link there.
</p>
</div>

# How to install Lean and mathlib on Debian/Ubuntu

This document explains how to get started with Lean and mathlib if you
are using a Linux distribution derived from Debian (Debian itself,
Ubuntu, LMDE,...).

If you get stuck, please come to [the chat room](https://leanprover.zulipchat.com/) to ask for assistance.

There is a [video walkthrough](https://www.youtube.com/watch?v=02ff4WrW0FU) of these instructions on YouTube.

## Installing Lean and mathlib

Here we will discuss the fast way, assuming a lot of trust from you. It
will install Lean, with supporting tools `elan` and `leanpkg`,
the supporting tool `leanproject` for Lean's mathematical
library, as well as the code editor VS Code and its Lean plugin, and
other dependencies you probably already have, like `curl`, `git`,
`python3`, and `pip3`. If you don't like this method, there is a
[detailed webpage](debian_details.html) which will decompose the
process into described stages, and won't ask for a blind `sudo`.

The fast way is: open a terminal and type:
```bash
wget -q https://raw.githubusercontent.com/leanprover-community/mathlib-tools/master/scripts/install_debian.sh && bash install_debian.sh ; rm -f install_debian.sh && source ~/.profile
```

## Lean Projects

You can now read instructions about creating and working on [Lean projects](project.html)
