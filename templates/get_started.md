# Get started with Lean

There are many options if you want to start using Lean, depending on how
seriously you want to try.

## <a name="web"></a>Just a quick glance

Lean can run in a web browser thanks to
[WebAssembly](https://en.wikipedia.org/wiki/WebAssembly). Of course,
the performance is nowhere near that of a regular install.
This is still a good option if you want to know what Lean looks
like, and have only 10 minutes to spare. For instance, you can read
your
[first proofs](https://leanprover-community.github.io/lean-web-editor/#url=https%3A%2F%2Fraw.githubusercontent.com%2Fleanprover-community%2Ftutorials%2Fmaster%2Fsrc%2Ffirst_proofs.lean).
You need to wait for the orange bar at the top to turn green and say
"Lean is ready!". Then you can click anywhere inside `begin` and `end`
pairs to see the state of proofs evolving.

If this is too passive for you, and you have a bit more time, you can start playing
[The Natural Number Game](http://wwwf.imperial.ac.uk/~buzzard/xena/natural_number_game/),
which also relies on Lean running in your web browser. Beware that some
Lean commands are voluntarily rendered less efficient in this game for
pedagogical purposes.

You can also use Lean on [CoCalc](https://cocalc.com/).

## <a name="bundle"></a>Maybe a couple of nights

If you are more serious about trying Lean, or can't stand waiting for
your web browser, but don't want to start installing too many things,
then you can try one of our autonomous bundles for:
- [Linux](http://oleanstorage.azureedge.net/releases/bundles/trylean_linux.tar.gz),
- [MacOS](http://oleanstorage.azureedge.net/releases/bundles/trylean_darwin.tar.gz), or
- [Windows](http://oleanstorage.azureedge.net/releases/bundles/trylean_windows.zip).

Each of these bundles contains a folder `trylean` from which you can run
the program `trylean` without installing anything anywhere else on your
computer (although MacOS users will need to tell their system
they really want to run it). These bundles contain Lean itself,
[VScodium](https://vscodium.com/)
which is a distributable version of the VS Code editor, the Lean VS Code extension,
the mathlib library, and a couple of Lean files to play with.

The downside is you won't be able to create your own projects or easily
upgrade Lean and mathlib. You'll need a regular install for this.

## <a name="install"></a>Regular install

In order to enjoy the full Lean experience, you need to install a couple
of dependencies, including a python package providing user-friendly
supporting tools. This is not much longer that installing an autonomous
bundle, but it does spread a bit more in your computer. You can read explanations
about [how the various parts fit together](toolchain.html) if you are
curious. But this is not necessary. You can head straight to
installation instructions for your OS:
[Debian/Ubuntu](install/debian.html),
[Other linux](install/linux.html),
[MacOS](install/macos.html) or
[Windows](install/windows.html).

After this installation procedure, it is crucial to read how to start or
get a [Lean project](install/project.html). And of course you'll
probably want to [learn Lean](learn.html)!
