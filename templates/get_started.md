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

# Get started with Lean

<div class="alert alert-info">
This webpage is about the current stable version of Lean, which is Lean 3, although
the community is currently switching to Lean 4.
See the <a href="https://leanprover.github.io/lean4/doc/">Lean 4 manual</a> for information about installing Lean 4.
</div>

You have several options for installing Lean 3, described below:

* a regular install (recommended)
* using Lean in a web browser
* use a stand-alone bundle (which runs out of a single directory, with no system-wide installation)

## Regular install

* [Debian/Ubuntu](install/debian.html)
* [Other linux](install/linux.html)
* [MacOS](install/macos.html)
* [Windows](install/windows.html)

After this installation procedure, it is crucial to read how to start or
get a [Lean project](install/project.html). And of course you'll
probably want to [learn Lean](learn.html)!

A regular install following these instructions installs a few pieces of supporting software.
You can read about [this infrastructure](toolchain.html) if you are
curious, but it is not necessary in order to use Lean.

## Just a quick glance

Lean can run in a web browser, although the performance is worse than a regular install.
Nevertheless it is good for taking a quick look, for example at some
[first proofs in Lean](https://leanprover-community.github.io/lean-web-editor/#url=https%3A%2F%2Fraw.githubusercontent.com%2Fleanprover-community%2Ftutorials%2Fmaster%2Fsrc%2Fexercises%2F00_first_proofs.lean).
You need to wait for the orange bar at the top to turn green and say
"Lean is ready!". Then you can click anywhere inside `begin` and `end`
pairs to see the state of proofs evolving.

With a bit more time, you can play
[The Natural Number Game](https://www.ma.imperial.ac.uk/~buzzard/xena/natural_number_game/),
in your browser.

You can also use Lean on [CoCalc](https://cocalc.com/).

## Maybe a couple of nights

If you are more serious about trying Lean, or can't stand waiting for
your web browser, but don't want to start installing too many things,
then you can try one of our autonomous bundles for:
- [Linux](https://oleanstorage.azureedge.net/releases/bundles/trylean_linux.tar.gz),
- [MacOS](https://oleanstorage.azureedge.net/releases/bundles/trylean_darwin.tar.gz), or
- [Windows](https://oleanstorage.azureedge.net/releases/bundles/trylean_windows.zip).

Each of these bundles contains a folder `trylean` from which you can run
the program `trylean` without installing anything anywhere else on your
computer (although MacOS users will need to tell their system
they really want to run it). On Windows this is a batch file, and there will be a Microsoft
Defender warning when running it. To allow the batch file to execute, click on "More Info"
then "Run anyway". These bundles contain Lean itself,
[VScodium](https://vscodium.com/)
which is a distributable version of the VS Code editor, the Lean VS Code extension,
the mathlib library, and a couple of Lean files to play with.

The downside is you won't be able to create your own projects or easily
upgrade Lean and mathlib. You'll need a regular install for this.

