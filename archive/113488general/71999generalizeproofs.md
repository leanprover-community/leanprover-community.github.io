---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/71999generalizeproofs.html
---

## Stream: [general](index.html)
### Topic: [generalize_proofs](71999generalizeproofs.html)

---


{% raw %}
#### [ Reid Barton (Dec 01 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148900772):
Does `generalize_proofs` ever work?

#### [ Reid Barton (Dec 01 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148900782):
I get this error `unknown declaration '1'`

#### [ Simon Hudon (Dec 01 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148901101):
What did you write?

#### [ Simon Hudon (Dec 01 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148901129):
I think `generalize_proofs` is obsolete. I remember @**Mario Carneiro** saying that `h_generalize` does the work `generalize_proofs` was intended to do

#### [ Reid Barton (Dec 01 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148901289):
something very complicated

#### [ Reid Barton (Dec 01 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148901307):
ah, let me try that

#### [ Reid Barton (Dec 01 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148901538):
hmm, I realized I need to also generalize the type that it is being converted to, and that seems tricky

#### [ Reid Barton (Dec 01 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148901543):
I'll just go back to my interim solution

#### [ Simon Hudon (Dec 01 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148901761):
Try `h_generalize! h : my_var == new_name` then you can generalize the type of the new variable

#### [ Chris Hughes (Dec 01 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148902893):
Does changing the definition of `collect_proofs_in` in `tactic.generalize_proofs` to this work?
```lean
private meta def collect_proofs_in :
  expr → list expr → list name × list expr → tactic (list name × list expr)
| e ctx (ns, hs) :=
let go (tac : list name × list expr → tactic (list name × list expr)) :
  tactic (list name × list expr) :=
(do t ← infer_type e,
   mcond (is_prop t) (do
     first (hs.map $ λ h, do
       t' ← infer_type h,
       is_def_eq t t',
       g ← target,
       change $ g.replace (λ a n, if a = e then some h else none),
       return (ns, hs)) <|>
     (let (n, ns) := (match ns with
        | [] := (`_x, [])
        | (n :: ns) := (n, ns)
        end : name × list name) in
      do generalize e n,
         h ← intro n,
         return (ns, h::hs)) <|> return (ns, hs)) (tac (ns, hs))) <|> return (ns, hs) in
match e with
| (expr.const _ _)   := go return
| (expr.local_const _ _ _ t) := collect_proofs_in t ctx (ns, hs)
| (expr.mvar _ _ t)  := collect_proofs_in t ctx (ns, hs)
| (expr.app f x)     :=
  go (λ nh, collect_proofs_in f ctx nh >>= collect_proofs_in x ctx)
| (expr.lam n b d e) :=
  go (λ nh, do
    nh ← collect_proofs_in d ctx nh,
    var ← mk_local' n b d,
    collect_proofs_in (expr.instantiate_var e var) (var::ctx) nh)
| (expr.pi n b d e) := do
  nh ← collect_proofs_in d ctx (ns, hs),
  var ← mk_local' n b d,
  collect_proofs_in (expr.instantiate_var e var) (var::ctx) nh
| (expr.elet n t d e) :=
  go (λ nh, do
    nh ← collect_proofs_in t ctx nh,
    nh ← collect_proofs_in d ctx nh,
    collect_proofs_in (expr.instantiate_var e d) ctx nh)
| (expr.macro m l) :=
  go (λ nh, mfoldl (λ x e, collect_proofs_in e ctx x) nh l)
| _                  := return (ns, hs)
end
```

#### [ Chris Hughes (Dec 01 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148903419):
I think the problem is that `infer_type` fails given a `sort`

#### [ Mario Carneiro (Dec 01 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148905988):
`generalize_proofs` is not so much obsolete as broken and abandoned

#### [ Mario Carneiro (Dec 01 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148905991):
I think it works as long as there are no binders in the goal


{% endraw %}
