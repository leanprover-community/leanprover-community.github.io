---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/32934Prooftermsize2200.html
---

## [general](index.html)
### [Proof term size * 2^200](32934Prooftermsize2200.html)

#### [Seul Baek (Jan 10 2019 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof term size * 2^200/near/154864164):
I became curious how sizes of proof terms affect speed, so I ran a quick experiment: 

```
def foo : nat → Prop 
| 0 := true 
| (n+1) := (foo n) ∧ (foo n)

meta def mk_foo_expr : nat → expr 
| 0 := `(trivial)
| (n+1) := 
  expr.app 
    (expr.app 
      (reflected.to_expr `(@and.intro (foo n) (foo n))) 
      (mk_foo_expr n)) 
    (mk_foo_expr n)

open tactic

meta def show_foo : tactic unit :=
do `(foo %%nx) ← target, 
   n ← eval_expr nat nx, 
   exact (mk_foo_expr n)

set_option profiler true

lemma foo_200 : foo 200 := 
by show_foo

#print foo_200
```

To my surprise Lean handles it with ease, in roughly 50ms. I don' t think Lean is constructing and checking a gigantic proof term that has 2^200 occurrences of `trivial`. What's going on here?

#### [Gabriel Ebner (Jan 10 2019 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof term size * 2^200/near/154868623):
To a certain degree, Lean can handle terms with dag-like sharing (your term is very small when viewed as a dag).  This happens e.g. because type inference and whnf and unifiability are cached, i.e., only evaluated once for every subterm (there are only few subterms).

#### [Gabriel Ebner (Jan 10 2019 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof term size * 2^200/near/154868637):
See also https://github.com/leanprover/tc/issues/8

#### [Seul Baek (Jan 10 2019 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof term size * 2^200/near/154876865):
I see. Thanks!

