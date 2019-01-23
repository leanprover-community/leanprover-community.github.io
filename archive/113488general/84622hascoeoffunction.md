---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/84622hascoeoffunction.html
---

## Stream: [general](index.html)
### Topic: [has_coe of function](84622hascoeoffunction.html)

---


{% raw %}
#### [ Sean Leather (Aug 08 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131112779):
Are there any problems with a coercion of a function?

```lean
instance : has_coe (∀ a, β₁ a → β₂ a) (embedding β₁ β₂)
```

where `embedding` is a structure.

#### [ Mario Carneiro (Aug 08 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131112953):
does it work?

#### [ Mario Carneiro (Aug 08 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131113020):
I don't see any obvious issues that it would cause, although it might not work

#### [ Sean Leather (Aug 08 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131113066):
In one place, `↑` worked. In another, I had to use `: sigma.embedding β₁ β₂`.

#### [ Mario Carneiro (Aug 08 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131113128):
If `B1` and `B2` are metavariables, it will have trouble

#### [ Mario Carneiro (Aug 08 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131113168):
I now recall seeing issues like this with the coercion from `order_iso` to `order_embedding`

#### [ Sean Leather (Aug 08 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131113221):
Hmm. If I have to use an annotation, it's not really worth it.

#### [ Gabriel Ebner (Aug 08 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131114775):
Yeah, function coercions only trigger if there are no metavariables at all.  This includes universe metavariables as well.

#### [ Simon Hudon (Aug 08 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131130618):
It might be worth defining your own up arrow instead (e.g. `⟰`)

#### [ Joe Hendrix (Aug 09 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131136017):
I'm actually working through a similar issue, but where I want coercions to trigger over. type with. a single parameter.  I have two types `reg : type -> Type` and `lhs : type -> Type`, and `\forall tp, has_coe (reg tp) (lhs tp)` that I want to trigger even when `tp` contains metavariables.

#### [ Joe Hendrix (Aug 09 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131136165):
I wish there was some way to control how defined a term had to be before searching for coercions.

#### [ Sebastian Ullrich (Aug 09 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131147896):
@**jhx** Yes, that is the biggest issue of using type class inference for coercions. We definitely want to fix this in the future, but we don't have a convincing alternative design yet https://github.com/leanprover/lean/issues/1402

#### [ Joe Hendrix (Aug 09 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131152344):
As a workaround, I've introduces a type class `has_coe1`, and explicitly tell the functions that expect an argument of the given type to use it.
```
class has_coe1 {α:Sort w} (f : α → Sort u) (g : α → Sort v) := (coe : Π{a : α}, f a → g a)

instance has_coe1_refl (α:Sort w) (f : α → Sort u) : has_coe1 f f := ⟨λa f, f⟩
instance all_reg_is_lhs   : has_coe1 reg lhs := sorry

...

section
parameter {f:type → Type}
parameter [has_coe1 f value]

def sext {w:ℕ} {f} [has_coe1 f value] (x:f (bv w)) (o:ℕ) : value (bv o) := ...
```

This approach might provide a more general solution to the monad special case mentioned in issue 1402, but still feels fairly special case.


{% endraw %}
