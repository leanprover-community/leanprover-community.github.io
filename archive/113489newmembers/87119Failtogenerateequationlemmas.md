---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/87119Failtogenerateequationlemmas.html
---

## Stream: [new members](index.html)
### Topic: [Fail to generate equation lemmas?](87119Failtogenerateequationlemmas.html)

---

#### [Andrew Tindall (Jan 12 2019 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fail%20to%20generate%20equation%20lemmas%3F/near/154958586):
I have [a function](https://github.com/flypitch/flypitch/blob/f73127c3ad36e6c2f074a26518dc333f07c1ab85/src/fol.lean#L2071-L2077) that I defined recursively by cases on an inductive type. If i `set_option eqn_compiler.lemmas false` it compiles, but `simp` cannot use it ( [simp debug](https://pastebin.com/Hv6Q2TGW) ). if I `set_option eqn_compiler.lemmas true` it does not compile ( [eqn_compiler debug](https://pastebin.com/fMhF8scv) ). I can't tell from either of these where the error is - is there some other `trace` option I can turn on, maybe? 

(@**Mario Carneiro** , I am also thinking this is a problem that might just disappear when Jesse OKs your pull request defining inductive `dfin`s instead of `fin`s)

