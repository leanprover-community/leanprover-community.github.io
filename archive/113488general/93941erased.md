---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/93941erased.html
---

## Stream: [general](index.html)
### Topic: [erased](93941erased.html)

---


{% raw %}
#### [ Mario Carneiro (Apr 05 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124681873):
@**Gabriel Ebner** What would be the best way to define the following type:
* `erased A` is a type with a computable function `A -> erased A` and a noncomputable function `erased A -> A`
* `A` and `erased A` are (noncomputably) equivalent with those functions
* `erased A` is VM-erased, meaning elements of this type are stored as the "proof object" / "neutral element"

#### [ Mario Carneiro (Apr 05 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124681928):
Attempt 1:
```
import data.set.basic data.equiv

def erased (α : Type*) : Type* := set.range (singleton : α → set α)

namespace erased

@[inline] def mk {α} (a : α) : erased α := ⟨_, a, rfl⟩

noncomputable def out {α} (a : erased α) : α :=
classical.some a.2

theorem mk_out {α} (a : α) : (mk a).out = a :=
eq.symm $ set.mem_singleton_iff.1 $
by unfold out; rw [classical.some_spec (mk a).2]; simp [mk]

theorem out_mk {α} (a : erased α) : mk (out a) = a :=
subtype.eq $ set.ext $ λ b,
by simp [out, mk, classical.some_spec a.2]

noncomputable def equiv (α) : erased α ≃ α :=
⟨out, mk, out_mk, mk_out⟩

end erased
```

#### [ Mario Carneiro (Apr 05 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124682307):
The problem with this encoding is that `erased A` is essentially a `set A`, which is a `A -> Prop`, which is stored as a closure returning a proof object. Thus it isn't fully erased, so it still causes its arguments to be evaluated:
```
#eval erased.mk (2+2) -- (erased.mk 4)
```
Do you know why type families aren't erased like types are?

#### [ Simon Hudon (Apr 05 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124682380):
Why not use `nonempty`?

#### [ Mario Carneiro (Apr 05 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124682407):
it's not noncomputably equivalent to `A`

#### [ Simon Hudon (Apr 05 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124682408):
I withdraw my question, I get it

#### [ Mario Carneiro (Apr 05 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124682469):
The goal is to have a piece of "data" that is actually erased but still exists from the lean modeling POV

#### [ Simon Hudon (Apr 05 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124682497):
I see

#### [ Gabriel Ebner (Apr 05 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124682565):
Wait, this no longer works?  Let me check.

#### [ Gabriel Ebner (Apr 05 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124682890):
Mmmh, I can't reproduce this here.  The 2+2 computation is completely erased.  Let me upgrade Lean.

#### [ Gabriel Ebner (Apr 05 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124683007):
Still can't reproduce.

#### [ Mario Carneiro (Apr 05 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124683060):
Actually that `#eval` doesn't work, lean complains about too few arguments since it's a closure which is waiting for an argument. This shows the closure creation:
```
set_option trace.compiler.code_gen true
def f := let x := erased.mk (2+2) in x
-- [compiler.code_gen]  f._lambda_1 1
-- 0: scnstr #0
-- 1: ret
-- [compiler.code_gen]  f 0
-- 0: closure f._lambda_1 0
-- 1: localinfo x @ 0
-- 2: push 0
-- 3: drop 1
-- 4: ret
```

#### [ Gabriel Ebner (Apr 05 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124683063):
What do you get with these changes (added `has_repr` and the `set_option`):
```lean
set_option trace.compiler.optimize_bytecode true

def erased (α : Type*) : Type* := set.range (singleton : α → set α)

namespace erased

@[inline] def mk {α} (a : α) : erased α := ⟨_, a, rfl⟩

noncomputable def out {α} (a : erased α) : α :=
classical.some a.2

theorem mk_out {α} (a : α) : (mk a).out = a :=
eq.symm $ (set.mem_singleton_iff _ _).1 $
by unfold out; rw [classical.some_spec (mk a).2]; simp [mk]

theorem out_mk {α} (a : erased α) : mk (out a) = a :=
subtype.eq $ set.ext $ λ b,
by simp [out, mk, classical.some_spec a.2]

noncomputable def equiv (α) : erased α ≃ α :=
⟨out, mk, out_mk, mk_out⟩

instance (α): has_repr (erased α) := ⟨λ _, "erased"⟩

end erased

#eval (erased.mk (2+2)) -- (erased.mk 4)

```

#### [ Gabriel Ebner (Apr 05 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124683113):
Hmm, as a workaround you can use `have ..., from ..., ...` instead of let.

#### [ Mario Carneiro (Apr 05 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124683168):
Well, the let was just to force the closure creation out of tail call position

#### [ Mario Carneiro (Apr 05 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124683177):
if you use `have` instead it just adds an additional argument to the main function

#### [ Gabriel Ebner (Apr 05 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124683278):
I think the problem is just that prop-erasure is not implemented for `let`, because nobody ever uses lets except for data.

#### [ Mario Carneiro (Apr 05 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124683920):
Hm, you can still clearly tell the difference between these two pieces of code:
```
set_option trace.compiler.code_gen true
#eval let x := 2 + 2 = 4 in x
#eval let x := erased.mk (2+2) in x
```
I'm glad to see that `2+2` is not evaluated anywhere in the generated code, but it is still creating a closure returning `#0` rather than `#0` itself

#### [ Gabriel Ebner (Apr 05 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124684479):
Now I remember: we can't erase type families to `#0`.  We need to erase them to a function type, but I don't think such an erasure is implemented.  If `mk` is not inlined, then we actually compute `2+2` here.

#### [ Mario Carneiro (Apr 05 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124684551):
Here's attempt number 2, which tries to encode each element of erased A as a straight type:
```
import set_theory.ordinal

universe u
def erased (α : Type u) : Type (u+1) :=
{o // o < cardinal.ord (cardinal.mk α)}

namespace erased
open cardinal ordinal

noncomputable def wo' (α : Type u) :
  {r : α → α → Prop // ∃ [wo : is_well_order α r],
  ord (mk α) = @ordinal.type α r wo} :=
classical.choice $ let ⟨r, wo⟩ := cardinal.ord_eq α in ⟨⟨r, wo⟩⟩

def wo (α : Type u) (x y) := (wo' α).1 x y

instance {α} : is_well_order α (wo α) := (wo' α).2.fst

theorem wo_eq (α : Type u) : ord (mk α) = type (wo α) := (wo' α).2.snd

@[inline] def type {α} (r : α → α → Prop) [wo : is_well_order α r] : ordinal :=
quot.mk _ ⟨α, r, wo⟩

@[inline] def typein {α} (r : α → α → Prop) [is_well_order α r] (a : α) : ordinal :=
type (subrel r {b | r b a})

@[inline] def mk {α} (a : α) : erased α :=
⟨typein (wo α) a, (wo_eq α).symm ▸ typein_lt_type (wo α) a⟩

noncomputable def out {α} (a : erased α) : α :=
enum (wo α) a.1 (wo_eq α ▸ a.2)

theorem out_mk {α} (a : α) : (mk a).out = a := enum_typein _ _

theorem mk_out {α} (a : erased α) : mk (out a) = a := subtype.eq $ typein_enum _ _

noncomputable def equiv (α) : erased α ≃ α :=
⟨out, mk, mk_out, out_mk⟩

end erased
```

#### [ Mario Carneiro (Apr 05 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124684600):
Since you can't really (provably) distinguish types except by their cardinality, this approach is rather more involved

#### [ Mario Carneiro (Apr 05 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124684622):
It also requires a lot of inlining; I had to restate the definitions of `ordinal.type` and `ordinal.typein` so they would be inlined

#### [ Gabriel Ebner (Apr 05 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124684756):
Anything that relies on inlining will have the closure problem.

#### [ Mario Carneiro (Apr 05 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124684912):
Not true:
```
set_option trace.compiler.code_gen true
def f := @erased.mk ℕ
#eval let x := f (2+2) in x
```
Note that even though `f` is not inlined `2+2` is not evaluated

#### [ Gabriel Ebner (Apr 05 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124684913):
If you're okay with a bit of extra ugliness, you can define an `erase` function in both versions:
```lean
@[inline]
def erase {α} (a : erased α) : erased α :=
⟨λ x, a.1 x, a.2⟩

-- 👌
def f' := let x := erased.mk (2+2) in x.erase
```

#### [ Gabriel Ebner (Apr 05 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124684994):
Mmh, I still get a call to `erased.mk` and `2+2`, but no call to `f` since it is (of course) inlined.

#### [ Gabriel Ebner (Apr 05 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124685031):
You should set the `optimize_bytecode` option instead of `code_gen`, otherwise you miss out on all the optimizations.

#### [ Mario Carneiro (Apr 05 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124685258):
I'm confused: why does `erase` work? The argument count goes down, but it still returns `#0`. I thought you said type/proof lambdas can't be implemented as `#0`?

#### [ Mario Carneiro (Apr 05 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124685263):
```
set_option trace.compiler.optimize_bytecode true
def f1 : erased ℕ := (erased.mk (2+2))
def f2 : erased ℕ := (erased.mk (2+2)).erase
```

#### [ Gabriel Ebner (Apr 05 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124685972):
I'm a bit lost as well.  Apparently the `apply` operation is special-cased to also work on `#0`.

#### [ Mario Carneiro (Apr 05 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124686074):
That's why I would expect that type families should also compile as `#0` rather than `lam x, #0`

#### [ Gabriel Ebner (Apr 05 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/erased/near/124686214):
You know, type families are actually erased, it's just that subtypes aren't because they haven't been erased yet....:
```lean
def f (x : set ℕ) := x
def g (x : { s : set ℕ // true }) := x
```


{% endraw %}
