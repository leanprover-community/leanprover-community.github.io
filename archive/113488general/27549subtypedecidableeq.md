---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27549subtypedecidableeq.html
---

## Stream: [general](index.html)
### Topic: [subtype.decidable_eq](27549subtypedecidableeq.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 04 2019 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype.decidable_eq/near/154417392):
`subtype.decidable_eq` sometimes fails to reduce in the kernel. Not sure why this is, it doesn't use `propext` or anything. The `instance` `foo` that I wrote in this code does work for some reason.
```lean
import group_theory.perm group_theory.coset

open equiv

example : (⟨1, rfl⟩ : {x : perm bool // x = 1}) = ⟨swap ff tt * swap ff tt, dec_trivial⟩ :=
dec_trivial

example : (⟨1, rfl⟩ : {x : perm bool // x = 1}) = ⟨swap ff tt * swap ff tt, dec_trivial⟩ :=
subtype.eq dec_trivial

@[instance, priority 1000] lemma foo {α : Type*} [decidable_eq α] {P : α → Prop} : 
  decidable_eq (subtype P) :=
λ a b, decidable_of_iff (a.1 = b.1) (by cases a; cases b; simp)

example : (⟨1, rfl⟩ : {x : perm bool // x = 1}) = ⟨swap ff tt * swap ff tt, dec_trivial⟩ :=
dec_trivial
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 04 2019 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype.decidable_eq/near/154422485):
Here's a little test of the decidable instance:
```lean
run_cmd do
  let t := `((⟨1, rfl⟩ : {x : perm bool // x = 1}) = ⟨swap ff tt * swap ff tt, dec_trivial⟩),
  inst ← mk_instance `(decidable %%t),
  e ← whnf inst, -- should be is_true _ but it's not
  trace e, -- eq.rec (λ (w_property : 1 = 1), is_true _) _ _
  [_,_,_,_,_,_,e] ← return $ expr.get_app_args e, -- get the major premise
  `(%%a = %%b) ← infer_type e, -- it is a proof of swap ff tt * swap ff tt = 1
  is_def_eq a b -- and they are not defeq
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 04 2019 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype.decidable_eq/near/154422613):
`whnf` gets stuck here because it does not unfold proofs, like the major premise of the `eq.rec`, and it can't ignore the proof because it's not equivalent to `rfl` (because the things being equated are not defeq)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 04 2019 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype.decidable_eq/near/154422993):
You should not cast types in order to prove a decidable instance. I know it's tempting but you should always use  `decidable_of_iff` which does a case on the target rather than a cast

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 04 2019 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype.decidable_eq/near/154423028):
Unfortunately, the blame here seems to lie in `mk_dec_eq_instance`, which is bad since it powers `@[derive decidable_eq]` which is used all over

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 04 2019 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype.decidable_eq/near/154423095):
Here's `subtype.decidable_eq`:
```lean
@[instance]
protected def subtype.decidable_eq : Π {α : Type u} {p : α → Prop} [_inst_1 : decidable_eq α], decidable_eq {x // p x} :=
λ {α : Type u} {p : α → Prop} [_inst_1 : decidable_eq α],
  id
    (λ (_v : {x // p x}),
       subtype.cases_on _v
         (λ (val : α) (property : p val) (w : {x // p x}),
            subtype.cases_on w
              (λ (w_val : α) (w_property : p w_val),
                 decidable.by_cases (λ (a : val = w_val), eq.rec (λ (w_property : p val), is_true _) a w_property)
                   (λ (a : ¬val = w_val), is_false _))))
```
Note the `eq.rec` in the true branch

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 04 2019 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype.decidable_eq/near/154423146):
if it said `is_true (eq.rec (λ (w_property : p val), _) a w_property)` there would be no problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 04 2019 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype.decidable_eq/near/154423514):
the culprit is the `subst` here -> https://github.com/leanprover/lean/blob/master/library/init/meta/mk_dec_eq_instance.lean#L76 . Unfortunately I'm not sure there is anything we can do about it from mathlib


{% endraw %}
