# Controlled installation of Lean and mathlib on Debian/Ubuntu

This document explains a more controlled installation procedure
for Lean and mathlib on Linux distributions derived from Debian (Debian itself,
Ubuntu, LMDE,...). There is a quicker way described in the main
[install page](debian.html) but it requires more trust.
Of course you can get even more details about what is going on by
reading the bash script that will be downloaded below:
[elan_init](https://github.com/Kha/elan/blob/master/elan-init.sh).

* Lean itself doesn't depend on much infrastructure, but supporting tools
  needed by most users require `git`, `curl`, and `python`. So the first step is:
  ```bash
  sudo apt install git curl python3 python3-pip
  ```

* The next step installs a small tool called `elan` which will handle
  updating Lean according to the needs of your current project (hit Enter
  when a question is asked). It will live in `$HOME/.elan` and adds a
  line to `$HOME/.profile`.
  ```bash
  curl https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh -sSf | sh
  ```

* There are two editors you can use with Lean, VS Code and emacs. The
  recommended choice is [Visual Studio Code](https://code.visualstudio.com/).
  ```bash
  wget -O code.deb https://go.microsoft.com/fwlink/?LinkID=760868
  sudo apt install ./code.deb
  rm code.deb
  code --install-extension jroesch.lean
  ```

  Now open VS Code, and verify Lean is working, for example by saving a file `test.lean` and entering `#eval 1+1`.
   A green line should appear underneath `#eval 1+1`, and hovering the mouse over it you should see `2`
   displayed.

  The alternative is to use Emacs, and its [lean-mode](https://github.com/leanprover/lean-mode).

* Then we install a small tool called `leanproject` that which will handle
  updating mathlib according to the needs of your current project.
  Follow the recommended Python way (look, no `sudo`) and install things into
  your `$HOME` by doing
  ```bash
  pip3 install mathlibtools --user
  ```
  and make sure that `$HOME/.local/bin`, where scripts, such as `leanproject`, are installed, is in your `PATH`. If it is not there, do
  ```bash
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.profile
  . ~/.profile
  ```
  to have you all set. Alternatively, if you have root/sudo access, you can do (a more dangerous)
  ```bash
  sudo pip3 install mathlibtools
  ```
  This, in particular, will install scripts such as `leanproject` into `/usr/local/bin`, which should
  be in your `$PATH`. If it is not there, do
  ```bash
  echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.profile
  . ~/.profile
  ```

   
You can now read instructions about creating and working on [Lean projects](project.html)
