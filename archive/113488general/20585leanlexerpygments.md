---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20585leanlexerpygments.html
---

## Stream: [general](index.html)
### Topic: [lean lexer (pygments)](20585leanlexerpygments.html)

---

#### [Joseph Corneli (Jul 25 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20lexer%20%28pygments%29/near/130273767):
FYI I found and reported the following bug in the LeanLexer: [#1459: LeanLexer does not have a "^" operator](https://bitbucket.org/birkenfeld/pygments-main/issues/1459/leanlexer-does-not-have-a-operator).  The fix is simple, but my BitBucket account is locked so I can't submit the fix myself! (... Though I guess I could register another account there easily enough ...) Maybe it's worth setting up a stress-test for the Lexer to make sure that it has all the other required syntax?

#### [Gabriel Ebner (Jul 25 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20lexer%20%28pygments%29/near/130274242):
BTW, we're using a pygments fork for the reference manual, etc.: https://bitbucket.org/gebner/pygments-main/src/default/

#### [Gabriel Ebner (Jul 25 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20lexer%20%28pygments%29/near/130274253):
The upstream pygments project is unfortunately not very active.  The lean highlighting there is still from Lean 2.

#### [Patrick Massot (Jul 25 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20lexer%20%28pygments%29/near/130278694):
And we still need to bring this fork to use in Zulip...

#### [Joseph Corneli (Jul 25 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20lexer%20%28pygments%29/near/130280318):
```quote
The upstream pygments project is unfortunately not very active.  The lean highlighting there is still from Lean 2.
```
Thanks for the tip!  I installed the fork, and got a replacement version of sphinx set up with the correct requirement `'Pygments==2.1a0.dev20180725',` in `setup.py`.  No problems with this version of the LeanLexer.

