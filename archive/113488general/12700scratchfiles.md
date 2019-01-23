---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/12700scratchfiles.html
---

## Stream: [general](index.html)
### Topic: [scratch files](12700scratchfiles.html)

---


{% raw %}
#### [ Kevin Buzzard (Sep 15 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/scratch%20files/near/134015349):
I'd like to have a few scratch files in my clone of community-mathlib, in e.g. a `scratch/` directory. Should I do this with some local trickery in .gitignore, should I change the github version of .gitignore, should I just use `_target`, should I load a second project in VS Code? I want VS Code to stop nagging me about files I just use to do tests or calculations.

#### [ Bryan Gin-ge Chen (Sep 15 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/scratch%20files/near/134015591):
Putting stuff in `_target/scratch/` seems safe enough, at least it doesn't seem to be overwritten when doing `leanpkg upgrade / build`.

#### [ Scott Morrison (Sep 16 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/scratch%20files/near/134031737):
I'd support adding /scratch/ to the official .gitignore. I've wanted the same thing previously.

#### [ Mario Carneiro (Sep 16 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/scratch%20files/near/134039022):
I have a `test.lean` file at the root of my repository, that I have added to my local gitignore (`.git/info/exclude`). I suggest doing this for whatever your local scratch setup is

#### [ Kevin Buzzard (Sep 16 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/scratch%20files/near/134045518):
Aah this is probably the canonical solution. The idea is that `.gitignore` is for files and directories which should be ignored by all users of the repo, like .olean files, but `.git/info/exclude` is a local .gitignore for your clone only and you won't be faced with VS Code nagging you that you've updated .gitignore if you edit this. Thanks for this tip Mario!

#### [ Kevin Buzzard (Sep 16 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/scratch%20files/near/134046304):
Gaargh `leanpkg build` builds my scratch files that don't build and then reports errors. Could this be fixed by moving all of mathlib into a `src/` directory?

#### [ Scott Morrison (Sep 16 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/scratch%20files/near/134049356):
Yes. :-)


{% endraw %}
