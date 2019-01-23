---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/42891termination.html
---

## Stream: [general](index.html)
### Topic: [termination](42891termination.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) petercommand (Nov 23 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148203856):
https://gist.github.com/petercommand/91e72613af95bde16baadf484abd1368
lean fails to prove that this code terminates, but this code is structurally recursive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) petercommand (Nov 23 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148204024):
and if I change ```Prop``` to ```Type```, termination check succeeds

#### [![Click to go to Zulip](../../assets/img/zulip2.png) petercommand (Nov 23 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148204028):
looks like a bug

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 23 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148204092):
well if you change `Prop` to `Type` then I suspect Lean is doing induction on `tup_order`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 23 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148204093):
which is not what you want

#### [![Click to go to Zulip](../../assets/img/zulip2.png) petercommand (Nov 23 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148204141):
wasn't I doing induction on ```tup_order``` when I use ```Prop```?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 23 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148204162):
when you use `Prop`, the `tup_order` has no size, so there's no well-founded relation on it that Lean is using

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 23 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148204165):
if you see the error, you can see `⊢ prod.lex has_lt.lt has_lt.lt (p, q) (p, q)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 23 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148204168):
Lean is trying to decrease the arguments of `tup_order` instead of the constructors of `tup_order`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 23 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148204221):
I'm still surprised it doesn't work. Shouldn't it be using `tup_order.rec` instead?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) petercommand (Nov 23 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148204333):
```quote
if you see the error, you can see ```⊢ prod.lex has_lt.lt has_lt.lt (p, q) (p, q)```
```
what you do mean? the prod.lex in wf.lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 23 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148204344):
I'm surprised this still doesn't work:
```lean
inductive tup_order : (ℕ × ℕ) → (ℕ × ℕ) → Prop
| base_snd : ∀ a b, tup_order (a, b) (a, nat.succ b)
| base_fst : ∀ a b c, tup_order (a, b) (nat.succ a, c)
| succ_fst : ∀ a b c d e, tup_order (a, b) (c, d) → tup_order (a, b) (nat.succ c, e)
| succ_snd : ∀ a b c d, tup_order (a, b) (c, d) → tup_order (a, b) (c, nat.succ d)

namespace tup_order

protected theorem trans : ∀ {p : (ℕ × ℕ) × (ℕ × ℕ) × (ℕ × ℕ)},
  tup_order p.1 p.2.1 → tup_order p.2.1 p.2.2 → tup_order p.1 p.2.2
| ((_,_), (_,_), (_,_)) ord1 (base_snd a b) := succ_snd _ _ _ _ ord1
| ((_,_), (_,_), (_,_)) ord1 (base_fst h i j) := succ_fst _ _ _ _ _ ord1
| ((p,q), (_,_), (_,_)) ord1 (succ_fst a b c d e t1) := succ_fst _ _ _ d _ (@trans ((p,q),(a,b),(c,d)) ord1 t1)
| ((p,q), (_,_), (_,_)) ord1 (succ_snd a b c d t) := succ_snd _ _ _ _ (@trans ((p,q),(a,b),(c,d)) ord1 t)

end tup_order
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 23 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148204346):
```lean
⊢ prod.lex (prod.lex has_lt.lt has_lt.lt) (prod.lex (prod.lex has_lt.lt has_lt.lt) (prod.lex has_lt.lt has_lt.lt))
    ((p, q), (a, b), c, d)
    ((p, q), (a, b), nat.succ c, e)

⊢ prod.lex (prod.lex has_lt.lt has_lt.lt) (prod.lex (prod.lex has_lt.lt has_lt.lt) (prod.lex has_lt.lt has_lt.lt))
    ((p, q), (a, b), c, d)
    ((p, q), (a, b), c, nat.succ d)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 23 2018 at 03:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148204433):
and I'm astonished that this doesn't work (swapping the order):
```lean
inductive tup_order : (ℕ × ℕ) → (ℕ × ℕ) → Prop
| base_snd : ∀ a b, tup_order (a, b) (a, nat.succ b)
| base_fst : ∀ a b c, tup_order (a, b) (nat.succ a, c)
| succ_fst : ∀ a b c d e, tup_order (a, b) (c, d) → tup_order (a, b) (nat.succ c, e)
| succ_snd : ∀ a b c d, tup_order (a, b) (c, d) → tup_order (a, b) (c, nat.succ d)

namespace tup_order

protected theorem trans : ∀ {c a b : ℕ × ℕ},
  tup_order a b → tup_order b c → tup_order a c
| (_,_) (_,_) (_,_) ord1 (base_snd a b) := succ_snd _ _ _ _ ord1
| (_,_) (_,_) (_,_) ord1 (base_fst h i j) := succ_fst _ _ _ _ _ ord1
| (_,_) (_,_) (_,_) ord1 (succ_fst a b c d e t1) := succ_fst _ _ _ _ _ (trans ord1 t1)
-- ⊢ prod.lex has_lt.lt has_lt.lt (c, d) (nat.succ c, e)
| (_,_) (_,_) (_,_) ord1 (succ_snd a b c d t) := succ_snd _ _ _ _ (trans ord1 t)
-- ⊢ prod.lex has_lt.lt has_lt.lt (c, d) (c, nat.succ d)

end tup_order
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 23 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148204488):
and what is it with this:
```lean
inductive tup_order : (ℕ × ℕ) → (ℕ × ℕ) → Prop
| base_snd : ∀ a b, tup_order (a, b) (a, nat.succ b)
| base_fst : ∀ a b c, tup_order (a, b) (nat.succ a, c)
| succ_fst : ∀ a b c d e, tup_order (a, b) (c, d) → tup_order (a, b) (nat.succ c, e)
| succ_snd : ∀ a b c d, tup_order (a, b) (c, d) → tup_order (a, b) (c, nat.succ d)

namespace tup_order

protected theorem trans : ∀ {c a b : ℕ × ℕ},
  tup_order a b → tup_order b c → tup_order a c
| (_,_) (_,_) (_,_) ord1 (base_snd a b) := succ_snd _ _ _ _ ord1
| (_,_) (_,_) (_,_) ord1 (base_fst h i j) := succ_fst _ _ _ _ _ ord1
| (_,_) (_,_) (_,_) ord1 (succ_fst a b c d e t1) :=
    have _ := prod.lex.left (<) d e (nat.lt_succ_self c),
    succ_fst _ _ _ _ _ (trans ord1 t1)
-- this : prod.lex has_lt.lt has_lt.lt (c, d) (nat.succ c, e)
-- ⊢ prod.lex has_lt.lt has_lt.lt (c, d) (nat.succ c, e)
| (_,_) (_,_) (_,_) ord1 (succ_snd a b c d t) := succ_snd _ _ _ _ (trans ord1 t)
-- ⊢ prod.lex has_lt.lt has_lt.lt (c, d) (c, nat.succ d)

end tup_order
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Nov 23 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148217775):
If you want to do induction on recursively-defined propositions, you should use `induction`:
```lean
lemma tup_order_trans {a b c} : tup_order a b → tup_order b c → tup_order a c :=
begin
intros h₁ h₂, induction h₂ generalizing a,
case base_snd { cases a, apply succ_snd, assumption },
-- ...
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Nov 23 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148217895):
The equation compiler does not use `rec`: https://github.com/leanprover/lean/issues/1611
In this case, it tries to do well-founded induction on the size of the tuples `a`, `b`, and `c`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Nov 23 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148218019):
This strategy does not allow you to do recursion on proofs (since they have a constant size).  Another gotcha is that you can't recursion on propositions defined via nested induction.  One possible workaround is to change the universe of `tup_order` to `Type`, then there is a more sensible `sizeof`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 23 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148247683):
```lean
inductive tup_order : (ℕ × ℕ) → (ℕ × ℕ) → Prop
| base_snd : ∀ {a b}, tup_order (a, b) (a, nat.succ b)
| base_fst : ∀ {a b c}, tup_order (a, b) (nat.succ a, c)
| succ_fst : ∀ {a b c d e}, tup_order (a, b) (c, d) → tup_order (a, b) (nat.succ c, e)
| succ_snd : ∀ {a b c d}, tup_order (a, b) (c, d) → tup_order (a, b) (c, nat.succ d)

namespace tup_order

protected theorem trans {a b c : ℕ × ℕ}
  (Hab : tup_order a b) (Hbc : tup_order b c) : tup_order a c :=
begin
  cases a, cases b, cases c, induction Hbc,
  case tup_order.base_snd { exact succ_snd Hab },
  case tup_order.base_fst { exact succ_fst Hab },
  case tup_order.succ_fst { exact succ_fst (Hbc_ih Hab) },
  case tup_order.succ_snd { exact succ_snd (Hbc_ih Hab) }
end

end tup_order
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 23 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148247827):
So can you never use the equation compiler to consume an inductive Prop?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 23 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148247840):
you're asking the wrong person...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 23 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148247915):
Can Mario never use the equation compiler to consume an inductive Prop?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 23 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148248002):
@**Mario Carneiro** Reid wants to know if Kenny can never use the equation compiler to consume an inductive Prop.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 23 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148248022):
great

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Nov 23 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/termination/near/148250530):
> So can you never use the equation compiler to consume an inductive Prop?

It works just fine as long as you don't need recursion; pattern-matching is no problem.

