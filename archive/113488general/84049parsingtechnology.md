---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/84049parsingtechnology.html
---

## Stream: [general](index.html)
### Topic: [parsing technology](84049parsingtechnology.html)

---

#### [Assia Mahboubi (Jun 08 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parsing%20technology/near/127768347):
Hi there, can someone help me finding the code of Lean's parser and/or its documentation?

#### [Sebastian Ullrich (Jun 08 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parsing%20technology/near/127769028):
Hi Assia. There is basically no documentation - this should certainly change for Lean 4 where the parser will be rewritten in Lean to be user-accessible. The current one is implemented in C++ as a recursive-descent LL(1) Pratt parser - https://github.com/leanprover/lean/blob/master/src/frontends/lean/parser.h

#### [Assia Mahboubi (Jun 08 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parsing%20technology/near/127769336):
Thanks a lot @**Sebastian Ullrich** !

