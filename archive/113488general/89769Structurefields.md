---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89769Structurefields.html
---

## Stream: [general](index.html)
### Topic: [Structure fields](89769Structurefields.html)

---

#### [Sebastien Gouezel (Nov 07 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Structure%20fields/near/146965379):
Is there a quick way to unfold something defined in a class? Let me be more specific. The product of metric spaces starts with
```lean
instance prod.metric_space_max [metric_space β] : metric_space (α × β) :=
{ dist := λ x y, max (dist x.1 y.1) (dist x.2 y.2),
......}
```
Now, in a proof, I have `dist x y` where `x` and `y` are in a product metric space, and I would like to unfold it to `max (dist x.1 y.1) (dist x.2 y.2)`. 
I can `change` it, or use `show`, or prove a lemma giving the formula for the distance (with `rfl`) and then unfold this lemma. But I am wondering if I am missing something and if there is something I can just unfold, like `prod.metric_space_max._secret_access_to_dist_` or something like that.

#### [Johannes Hölzl (Nov 07 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Structure%20fields/near/146967395):
I don't think so. you can unfold `prod.metric_space_max`, and then call `dsimp` to unfold the projection. But this will not work in general. The best thing to do is to add the lemma as a `simp`-rule (which we should have anyway)

#### [Sebastian Ullrich (Nov 07 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Structure%20fields/near/146968934):
Does `simp [dist]` not work? Or do you want to unfold only this specific `dist`?

#### [Sebastien Gouezel (Nov 07 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Structure%20fields/near/146969406):
No, simp does not work here:
```lean
lemma prod.dist_eq {α : Type u} {β : Type v} [metric_space α] [metric_space β] {x y : α × β} :
  dist x y = max (dist x.1 y.1) (dist x.2 y.2) := by simp
```
fails with
```
simplify tactic failed to simplify
```
I have proved the lemma using `rfl`, and then used it explicitly later. This seems to be the canonical way to proceed. By the way, this is not the kind of thing I would want to unfold all the time, so I don't think it is a good simp lemma (but it is definitely useful to have it in explicit form like this)

#### [Sebastian Ullrich (Nov 07 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Structure%20fields/near/146969573):
You have to pass the projection explicitly: `simp [dist]`

#### [Sebastien Gouezel (Nov 07 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Structure%20fields/near/146969749):
Sorry, I should learn to read. Yes, `simp [dist]` works. Can you explain why?

#### [Sebastian Ullrich (Nov 07 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Structure%20fields/near/146969913):
`simp` accepts not just rewrite lemmas but also function and projection names, which tell it to unfold usages of them

#### [Sebastien Gouezel (Nov 07 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Structure%20fields/near/146970400):
OK, thanks (and this is very useful, I don't know why I never noticed this)

#### [Kevin Buzzard (Nov 07 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Structure%20fields/near/146970867):
Oh nice trick Sebastian! I thought that the philosophy was to always prove these lemmas and give them names. Wait -- maybe that is the philosophy anyway.

#### [Floris van Doorn (Nov 07 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Structure%20fields/near/146971122):
I also didn't know this. This is very useful!

