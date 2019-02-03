---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/12700scratchfiles.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [scratch files](https://leanprover-community.github.io/archive/113488general/12700scratchfiles.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Sep 15 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/scratch%20files/near/134015349):
<p>I'd like to have a few scratch files in my clone of community-mathlib, in e.g. a <code>scratch/</code> directory. Should I do this with some local trickery in .gitignore, should I change the github version of .gitignore, should I just use <code>_target</code>, should I load a second project in VS Code? I want VS Code to stop nagging me about files I just use to do tests or calculations.</p>

#### [ Bryan Gin-ge Chen (Sep 15 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/scratch%20files/near/134015591):
<p>Putting stuff in <code>_target/scratch/</code> seems safe enough, at least it doesn't seem to be overwritten when doing <code>leanpkg upgrade / build</code>.</p>

#### [ Scott Morrison (Sep 16 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/scratch%20files/near/134031737):
<p>I'd support adding /scratch/ to the official .gitignore. I've wanted the same thing previously.</p>

#### [ Mario Carneiro (Sep 16 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/scratch%20files/near/134039022):
<p>I have a <code>test.lean</code> file at the root of my repository, that I have added to my local gitignore (<code>.git/info/exclude</code>). I suggest doing this for whatever your local scratch setup is</p>

#### [ Kevin Buzzard (Sep 16 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/scratch%20files/near/134045518):
<p>Aah this is probably the canonical solution. The idea is that <code>.gitignore</code> is for files and directories which should be ignored by all users of the repo, like .olean files, but <code>.git/info/exclude</code> is a local .gitignore for your clone only and you won't be faced with VS Code nagging you that you've updated .gitignore if you edit this. Thanks for this tip Mario!</p>

#### [ Kevin Buzzard (Sep 16 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/scratch%20files/near/134046304):
<p>Gaargh <code>leanpkg build</code> builds my scratch files that don't build and then reports errors. Could this be fixed by moving all of mathlib into a <code>src/</code> directory?</p>

#### [ Scott Morrison (Sep 16 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/scratch%20files/near/134049356):
<p>Yes. :-)</p>


{% endraw %}
