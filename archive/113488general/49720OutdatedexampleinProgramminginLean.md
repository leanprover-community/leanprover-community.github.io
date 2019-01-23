---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49720OutdatedexampleinProgramminginLean.html
---

## Stream: [general](index.html)
### Topic: [Outdated example in Programming in Lean](49720OutdatedexampleinProgramminginLean.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Miko de Amsterdamo (May 01 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Outdated%20example%20in%20Programming%20in%20Lean/near/125939264):
The example didn't work with my lean 3.3.0. It seems that ``for`` has become ``map``

```lean
meta def destruct_conjunctions : tactic unit :=
repeat (do
  l ← local_context,
  first $ l.map (λ h, do
    ht ← infer_type h >>= whnf,
    match ht with
    | `(and %%a %%b) := do
      n ← mk_fresh_name,
      mk_mapp ``and.left [none, none, some h] >>= assertv n a,
      n ← mk_fresh_name,
      mk_mapp ``and.right [none, none, some h] >>= assertv n b,
      clear h
    | _ := failed
    end))
```

