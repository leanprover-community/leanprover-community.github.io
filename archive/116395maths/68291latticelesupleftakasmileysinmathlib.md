---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/68291latticelesupleftakasmileysinmathlib.html
---

## Stream: [maths](index.html)
### Topic: [lattice.le_sup_left' a.k.a. smileys in mathlib](68291latticelesupleftakasmileysinmathlib.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 05 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130925919):
I thought it was time to learn about uniform spaces, and then I realised I had to learn about filters before that, and then I realised I had to learn about lattices before that.

```lean
import data.set.lattice

#check @lattice.le_sup_left
--  lattice.le_sup_left : ∀ {α : Type u_1} [_inst_1 : lattice.semilattice_sup α] {a b : α}, a ≤ a ⊔ b
#check @lattice.le_sup_left'
-- lattice.le_sup_left' : ∀ {α : Type u_1} [_inst_1 : lattice.semilattice_sup α] {a b : α}, a ≤ (:a ⊔ b:)

```

What's with the smileys? This is one of those times when `#print notation (:` is useless -- it doesn't direct the user to what they actually want to know.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 05 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130926055):
PS this is as far as I've got:

https://xenaproject.wordpress.com/2018/08/04/what-is-a-filter-how-some-computer-scientists-think-about-limits/

https://xenaproject.wordpress.com/2018/08/05/what-is-a-uniform-space-how-some-computer-scientists-think-about-completions/

and I'm now thinking of doing one on lattices because I still look at some filter code and see random bits of notation like `⊥` and `⨅` and I've not yet internalised what the lattice structure on filters is; I'm currently going about learning things the long way around by just reading some of this basic filter stuff -- I'm sure it can't be hard, but not knowing these basic things is holding me back a bit. I think Patrick went through the same thought process recently and now he's written a bunch of code for the perfectoid project about completions, and a desire to understand that has turned into a wider desire to understand some of these basic mathematical objects like filters and lattices which they don't actually seem to teach mathematicians.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 05 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130926161):
I'm guessing it has something to do with the `ematch` attribute.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 05 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130926232):
Oh yes they were talking about `ematch` earlier in the `order/lattice.lean` file; I'd not made the connection.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 05 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130926281):
Exhibit A:

```lean
section
  variable {α : Type u}

  -- TODO: this seems crazy, but it also seems to work reasonably well
  @[ematch] theorem le_antisymm' [partial_order α] : ∀ {a b : α}, (: a ≤ b :) → b ≤ a → a = b :=
  @le_antisymm _ _
end
```

It's antiymmetry of <= with some crazy smilies

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 05 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130926344):
I think `ematch` might have something to do with the equation compiler's automation for solving inequalities.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 05 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130926868):
Check this out (from the top of `order/lattice.lean`)

```lean
theorem sup_of_le_left (h : b ≤ a) : a ⊔ b = a :=
by apply le_antisymm; finish

theorem sup_of_le_right (h : a ≤ b) : a ⊔ b = b :=
by apply le_antisymm; finish

theorem sup_le_sup (h₁ : a ≤ b) (h₂ : c ≤ d) : a ⊔ c ≤ b ⊔ d :=
by finish

theorem sup_le_sup_left (h₁ : a ≤ b) (c) : c ⊔ a ≤ c ⊔ b :=
by finish

theorem sup_le_sup_right (h₁ : a ≤ b) (c) : a ⊔ c ≤ b ⊔ c :=
by finish

theorem le_of_sup_eq (h : a ⊔ b = b) : a ≤ b :=
by finish

@[simp] theorem sup_idem : a ⊔ a = a :=
by apply le_antisymm; finish

instance sup_is_idempotent : is_idempotent α (⊔) := ⟨@sup_idem _ _⟩

theorem sup_comm : a ⊔ b = b ⊔ a :=
by apply le_antisymm; finish
```

Very slick automated proofs! Now write `set_option profiler true` at the top:

```
elaboration of sup_of_le_left took 264ms
elaboration of sup_of_le_right took 281ms
elaboration of sup_le_sup took 781ms
elaboration of sup_le_sup_left took 519ms
elaboration of sup_le_sup_right took 396ms
elaboration of le_of_sup_eq took 199ms
elaboration of sup_idem took 203ms
elaboration of sup_comm took 132ms
```

and compare with 

```lean
theorem sup_of_le_left' (h : b ≤ a) : a ⊔ b = a :=
le_antisymm (sup_le (le_refl _) h) le_sup_left
```

```
elaboration of sup_of_le_left' took 7.54ms
```

etc. It saved the author of that file 30 seconds using automation instead of writing down the low-level proof, and now everyone who ever compiles mathlib has to pay an extra 250ms every time. Are the mathlib authors OK with that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 05 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130927184):
I think we should rather hope for optimized recompilation and available mathlib builds rather than avoiding automatization

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 05 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130927534):
I see. So in the long term these proofs are fine. Kenny would also point out that they use all three of Lean's spare axioms, but as far as I can see this is irrelevant in practice -- what we need to keep if possible is computation, because it makes proofs easier, and that's a different matter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 05 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130927594):
does it use `quot.sound`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 05 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130927673):
I think a lot of people need to download mathlib before 250ms of their laptop's time is more expensive than 30 seconds of a person's time.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 05 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130927730):
Finish does

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 05 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130927754):
I guess we need to start worrying when computers start writing mathlib then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 05 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130930180):
```quote
PS this is as far as I've got:

https://xenaproject.wordpress.com/2018/08/04/what-is-a-filter-how-some-computer-scientists-think-about-limits/

https://xenaproject.wordpress.com/2018/08/05/what-is-a-uniform-space-how-some-computer-scientists-think-about-completions/
```
Nice posts! But I think the titles are a bit unfair to Bourbaki, and especially to André Weil. Actually this is a story I keep telling people when I try to explain proof assistants. Boubaki invented filters because they were facing the exact same issue that proof assistants are facing. They wanted to prove everything without repeating statements and proofs again and again. It really makes sense that we are using the solution those very clever guys invented for that purpose.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 05 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130930237):
Actually your first post may fail to convey the combinatorial explosion here. Filters also handle functions converging at a point or at infinity in  a topological space, or at plus or minus infinity in R, or limits from the left or from the right at some real number.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 05 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130930238):
I mention Weil briefly, and Bourbaki not at all, despite being well aware that this is where this sort of stuff started to appear. I can add some comments.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 05 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130930286):
I just sat down and wrote something -- I don't really know what a filter is at all apart from what I read on Wikipedia the other day and what I worked out as a consequence. Patrick do you know how to pronounce `tendsto f F_X F_Y`? Is it "f of filter F_X tends to F_Y" or what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 05 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130930300):
Also don't forget that filters kill all the epsilon/4 nonsense.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 05 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130930344):
I don't know how to pronounce anything here, I never used filters before using Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 05 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130930400):
I realised when I was writing the filter post that I didn't even know how to say the concepts I was trying to explain.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 05 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130930448):
Maybe the uniform space post could include a brief description of the separatedness issue, since you describe completeness and then mention a Hausdorff completion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 05 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130930698):
Another random comment: about uniform structure, it may be worth pointing out the analogy with distances coming from norms. A norm N measures distance to 0, and one get a distance d(x, y) = N(y-x). In a (commutative) topological group the topology gives a way to say "close to zero" and the same trick applies, giving a uniform structure. I think uniting this case with the metric space case was Weil's motivation.

