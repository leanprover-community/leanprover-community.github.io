---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/92013LEANPATH.html
---

## Stream: [general](index.html)
### Topic: [LEAN_PATH](92013LEANPATH.html)

---

#### [Patrick Massot (Aug 14 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/LEAN_PATH/near/132139199):
I'm trying to use Lean from outside a project folder, using the `LEAN_PATH` environment variable. But it looks like it doesn't use the olean in this case (at least it starts eating up 380% CPU). I tried typing: `LEAN_PATH="/home/pmassot/.elan/toolchains/3.4.1/lib/lean/library/:/home/pmassot/lean/perfectoid-spaces/_target/deps/mathlib/:." lean t2.lean` in order to use the (compiled) mathlib that I have in the perfectoid project to execute `t2.lean` (which is a tiny test file).

