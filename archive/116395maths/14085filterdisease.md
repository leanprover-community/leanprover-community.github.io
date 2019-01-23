---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/14085filterdisease.html
---

## Stream: [maths](index.html)
### Topic: [filter disease](14085filterdisease.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131057798):
This feels really strange: I just caught  myself writing a long string of manipulations involving filters pull-backed, push-forwarded, multiplied and compared, because it felt easier than thinking in terms of compositions of limits and such things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131058064):
The key point is how filters allow to talk about limits when x tends to x' while staying in the image of a dense embedding.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131059184):
It's on my to-do list to understand if and when filters can be pulled back and pushed forward

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131059283):
filters live on bare sets, hence can be pulled back and pushed forward by bare set morphisms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131059294):
aka any map

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131059431):
both operation are order preserving. And f_*F \le G iff F \le f^*G

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131059536):
Now let's do composition of limits. f goes to G along F (I don't know how to pronounce this) if, by definition, f_*F \le G. Now it's an exercise for you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131059574):
of course f_* is covariantly functorial

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131059776):
Are they adjoint functors? @**Kenny Lau** you'd like this stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131059802):
You'll soon be complaining that they teach limits wrong at Imperial. Did you see my  filter blog post? Maybe you know all this stuff already

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131060103):
What would be Hom between two filters?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131060239):
sorry

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131060254):
you mean for the poset structure?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131060330):
Yes, we have f_*f^*G \le G  and F \le f^*f_*F  for all F and G

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131060390):
I must be careful not to be carried away, or else I'll be tempted to teach this to innocent students

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131060872):
where are adjoint functors in mathlib now that we got a category PR accepted?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131062286):
You're right, I guess it must be like the opens in a top space, the inclusions are the only morphisms, and the one equation you mentioned above is I guess precisely the affirmative answer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131070762):
I managed to abstract the lemma I was using three times in my proof.
```lean
import analysis.topology.continuity

open set filter

variables {α : Type*} [topological_space α] 
variables {β : Type*} [topological_space β]
variables {γ : Type*}
variables {δ : Type*} [topological_space δ]

variables {e : α → β} {f : γ → α} {g : γ → δ} {h : δ → β}
/-
 γ -f→ α
g↓     ↓e
 δ -h→ β 
-/

lemma key  {d : δ} {a : α} (H : tendsto h (nhds d) (nhds (e a))) (comm : h ∘ g = e ∘ f)
  (de : dense_embedding e) :  tendsto f (vmap g (nhds d)) (nhds a) :=
begin
  have lim1 : map g (vmap g (nhds d)) ≤ nhds d := map_vmap_le,
  replace lim1 : map h (map g (vmap g (nhds d))) ≤ map h (nhds d) := map_mono lim1,
  rw [filter.map_map, comm, ← filter.map_map, map_le_iff_le_vmap] at lim1,
  have lim2 :  vmap e (map h (nhds d)) ≤  vmap e  (nhds (e a)) := vmap_mono H,
  rw de.induced at lim2,
  exact le_trans lim1 lim2,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131070803):
@**Johannes Hölzl** I hope you're proud of me. But I'd still be interested if there is a smarter proof (or if it's already in mathlib).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131070879):
By the way, why isn't `dense_embedding` a class?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131070901):
Also, I find it a bit painful that the map is an implicit argument in `map_mono` and `vmap_mono`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131070985):
Now I'll go sleeping, feeling I've learned some nice stuff today.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131071488):
+1 for the commutative diagram!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 08 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131079718):
> where are adjoint functors in mathlib now that we got a category PR accepted?

Sorry to disappoint, @**Patrick Massot**, but only the first epsilon of category theory has been PR'd. It's a ways to go before you have adjoint functors.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 08 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131084690):
However, adjoint functors between posets are Galois connections, and they are in mathlib (`order/galois_connection.lean`).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Aug 08 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131089180):
```quote
@**Johannes Hölzl** I hope you're proud of me. But I'd still be interested if there is a smarter proof (or if it's already in mathlib).
```
 
Looks good to me. I don't think there is a related proof in mathlib. I'm on a bike trip this week, I can check out next Monday.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 08 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131100297):
@**Scott Morrison** Sorry about this joke. I know it's only the beginning, I did look at your PR.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 08 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131101008):
There is no hurry at all. The more difficult question is: how should we name that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 08 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131101650):
And also I'm a bit confused by the relation between `dense_embedding` and `embedding` in mathlib. My lemma actually doesn't use the dense part, but it uses the way the `induced` axiom is stated. But I guess it could be stated that way for embeddings too, right?


{% endraw %}
