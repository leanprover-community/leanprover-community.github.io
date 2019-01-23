---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/97741troublerunningleanonmac.html
---

## Stream: [new members](index.html)
### Topic: [trouble running lean on mac](97741troublerunningleanonmac.html)

---


{% raw %}
#### [ Yuhan Du (Aug 13 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132038880):
```
dyn3218-19:bin apple$ ls
lean		leanchecker	leanpkg
dyn3218-19:bin apple$ ./lean
dyld: Library not loaded: /usr/local/opt/gmp/lib/libgmp.10.dylib
  Referenced from: /Users/apple/Desktop/lean-3.4.2-nightly-2018-06-21-darwin/bin/./lean
  Reason: image not found
Abort trap: 6
```

can someone help with this

#### [ Mario Carneiro (Aug 13 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132038910):
I think if you are compiling it yourself there is some line to install `libgmp` in the readme?

#### [ Kevin Buzzard (Aug 13 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132038915):
This is the current nightly

#### [ Kevin Buzzard (Aug 13 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132038956):
I just don't know how to install gmp on a mac

#### [ Kevin Buzzard (Aug 13 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132038958):
(or indeed how to do anything on a mac)

#### [ Yulia Zaplatina (Aug 13 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132038960):
Homebrew solves the problem

#### [ Yulia Zaplatina (Aug 13 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132038964):
https://brew.sh

#### [ Kevin Buzzard (Aug 13 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132038971):
I think Homebrew solved a problem like this before. I should write this in the docs

#### [ Kevin Buzzard (Aug 13 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132039153):
Can one install Lean through homebrew? I'm guessing no

#### [ Sean Leather (Aug 13 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132039278):
I used to do it with Lean 2. I don't know if it's been kept up to date, though.

#### [ Sean Leather (Aug 13 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132039866):
I just read the rest of the thread before Kevin's message. I believe Yulia is referring to installing `libgmp` via `brew install gmp`, which will probably fix Yuhan's problem.

#### [ Patrick Massot (Aug 13 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132040275):
Since Lean is currently frozen, it seems like a very good time to update that brew thing

#### [ Kevin Buzzard (Aug 13 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132040340):
FWIW we have everything up and running now. On MacOS High Sierra we installed brew, and then `brew install gmp` (to get `lean` running) and `brew install coreutils` (to get `leanpkg` running).

#### [ Kevin Buzzard (Aug 13 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132040348):
Yuhan also installed git somehow, or had git already, but that was before I arrived.

#### [ Sean Leather (Aug 13 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132040849):
IIRC, `git` comes with the Xcode command line tools.


{% endraw %}
