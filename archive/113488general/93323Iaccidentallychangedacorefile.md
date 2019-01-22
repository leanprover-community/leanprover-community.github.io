---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/93323Iaccidentallychangedacorefile.html
---

## [general](index.html)
### [I accidentally changed a core file](93323Iaccidentallychangedacorefile.html)

#### [Kenny Lau (Sep 06 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444111):
I accidentally changed a core file and everything is now shit. I honestly don't know what to do.

#### [Kenny Lau (Sep 06 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444149):
Do I need to rebuild Lean?

#### [Keeley Hoek (Sep 06 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444331):
do you use elan

#### [Kenny Lau (Sep 06 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444344):
I don't

#### [Kevin Buzzard (Sep 06 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444360):
why not just download the binary again?

#### [Keeley Hoek (Sep 06 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444361):
tears
did you build it from source? download a zip distribution?

#### [Kenny Lau (Sep 06 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444469):
oh nvm I did the standard trick and it worked again

#### [Kenny Lau (Sep 06 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444475):
(standard trick = turning it off and on again)

#### [Kenny Lau (Sep 06 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444645):
I still think something has changed

#### [Kenny Lau (Sep 06 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444710):
This is what I do:
```
cd /c/
git clone https://github.com/leanprover/lean
cd lean
mkdir -p build/release
cd build/release
cmake -DCMAKE_BUILD_TYPE=RELEASE -G Ninja ../../src
ninja
cd /c/
git clone https://github.com/leanprover/mathlib
cd mathlib
/c/lean/bin/leanpkg build
```

#### [Kenny Lau (Sep 06 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444915):
I think it's alright

#### [Kevin Buzzard (Sep 06 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133445045):
I think that script looks OK, I mean, it will just download a reasonable version of everything

#### [Keeley Hoek (Sep 06 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133445409):
sure. if you mess up the standard library again, it is enough to just cd into the "lean" folder you already have sitting around and `git reset --hard HEAD` (and avoid the waiting)

#### [Kenny Lau (Sep 06 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133446802):
do I need to restart Lean after that? @**Keeley Hoek**

#### [Keeley Hoek (Sep 06 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133446886):
yes definitely

#### [Keeley Hoek (Sep 06 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133447053):
and I guess it is best to cd into build/release and run ninja again, but not obligatory (and ninja should be very fast compared to normal)

#### [Kenny Lau (Sep 06 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133447150):
oh ok

