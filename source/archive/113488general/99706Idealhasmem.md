---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99706Idealhasmem.html
---

## [general](index.html)
### [Ideal has_mem](99706Idealhasmem.html)

#### [AHan (Nov 30 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148853358):
I don't get why `test₁` type checked but `test₂` will result in deterministic timeout...?

```lean
variables {α : Type*}
variables [discrete_field α]
variables [decidable_eq α] [decidable_linear_order α]
variables [comm_ring (mv_polynomial ℕ α)]

lemma test₁ (a : α) : a ∈ (ideal.span ({a} : set α)) := sorry

lemma test₂ (a : mv_polynomial ℕ α) : a ∈ (ideal.span ({a} : set (mv_polynomial ℕ α))) := sorry
```

#### [Johan Commelin (Nov 30 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148854580):
@**AHan** What happens if you remove the `[comm_ring ...]` instance? It should derive it automatically, I hope.

#### [Patrick Massot (Nov 30 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148854942):
And also the proof is only one `rw` long

#### [Patrick Massot (Nov 30 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855036):
If order to find out the relevant lemma, you start by writing `ideal.mem_span` because you want something about ideals saying something belongs to a span, then you pause to inspect what autocompletions are suggested, and choose the relevant one.

#### [Kevin Buzzard (Nov 30 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855180):
@AHan if you pasted minimal _working_ examples (i.e. with all the imports needed to run the example) then my life would be slightly easier -- I'd just be able to cut and paste.

```lean
import linear_algebra.multivariate_polynomial
import ring_theory.ideals

variables {α : Type*}
variables [discrete_field α]
variables [decidable_eq α] [decidable_linear_order α]
--variables [comm_ring (mv_polynomial ℕ α)]

example : comm_ring (mv_polynomial ℕ α) := by apply_instance -- this works

lemma test₁ (a : α) : a ∈ (ideal.span ({a} : set α)) := sorry

lemma test₂ (a : mv_polynomial ℕ α) :
a ∈ (ideal.span ({a} : set (mv_polynomial ℕ α))) := sorry -- no timeout any more
```

#### [Patrick Massot (Nov 30 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855293):
you second import is probably unnecessary

#### [Kevin Buzzard (Nov 30 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855406):
So your problem is what Johan suggested. If alpha is a field then Lean *already knows* that the multivariate polynomial ring over alpha is a commutative ring. This fact is already in the "type class inference system" because Lean spotted that it was true, and put it there automatically. My `example` above shows that the fact that the polynomial ring is a commutative ring can be proved using the `apply_instance` tactic -- which means that Lean already internally has a term of type `comm_ring (mv_polynomial ℕ α)`. The line you wrote and I commented out makes a second term of that type. Now Lean's type class system works under the assumption that for typeclasses like `comm_ring`, there should be at most one term of each type, and if Lean has more than one term of a given typeclass then Lean can get confused. I don't know why this leads to a timeout in your case (some of the CS people here would be able to explain it I'm sure) but I can see the rule you broke, and breaking rules like this can lead to all sorts of random problems.

#### [Patrick Massot (Nov 30 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855565):
What is slightly more mysterious is why `lemma test₂ (a : mv_polynomial ℕ α) : a ∈ (ideal.span ({a} : set (mv_polynomial ℕ α))) := 
by rw ideal.mem_span_singleton` works without any extra step

#### [Patrick Massot (Nov 30 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855576):
The trick is https://github.com/leanprover/mathlib/blob/master/algebra/ring.lean#L73

#### [Patrick Massot (Nov 30 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855635):
Although `dvd_refl` is not definitionaly true, it is marked as `refl`, and it seems `rw` tries (all?) such lemmas to close goals

#### [Mario Carneiro (Nov 30 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855654):
it calls `refl`

#### [Patrick Massot (Nov 30 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855734):
How do you ask lean whether a particular lemma has been marked as `refl` and, if yes, where? I found the above line using grep

#### [Mario Carneiro (Nov 30 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855777):
if you print the lemma you can see any attributes

#### [Patrick Massot (Nov 30 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855782):
good

#### [Patrick Massot (Nov 30 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855789):
what about finding the line attaching the attribute?

#### [Mario Carneiro (Nov 30 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855798):
no luck

#### [Patrick Massot (Nov 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855824):
In `@[refl, simp, priority 100] theorem dvd_refl` what has priority 100?

#### [Patrick Massot (Nov 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855903):
priority in which process? simp?

#### [Kevin Buzzard (Nov 30 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855990):
Oh +1 to that question! I thought priority was just for type classes.

#### [Mario Carneiro (Nov 30 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855993):
I don't know why that's there. It's only for typeclasses

#### [Kevin Buzzard (Nov 30 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855997):
oh cool, I'm going back to mathlib and I'm going to give all the lemmas I proved priority 20000

#### [Johan Commelin (Nov 30 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856047):
You should give them priority 37. Just to make a point.

#### [Mario Carneiro (Nov 30 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856049):
maybe @**Keeley Hoek** can go code diving to ascertain if this is the case

#### [Mario Carneiro (Nov 30 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856057):
is it explicitly set by some line?

#### [Mario Carneiro (Nov 30 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856059):
or did lean do it

#### [Kevin Buzzard (Nov 30 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856061):
When Lean gets sponsored by Coca Cola and the user gets a little Coca Cola ad each time your lemma is used, every dev will want to make sure their lemmas are being used as much as possible.

#### [Mario Carneiro (Nov 30 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856126):
"This factorization was brought to you by the refreshing taste of... Coca Cola"

#### [Johan Commelin (Nov 30 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856150):
If (not when) that day arrives, I'll go back to pen and paper proofs.

#### [Edward Ayers (Nov 30 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856208):
Just install adblock on vscode

#### [Johan Commelin (Nov 30 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856284):
And waste precious CPU cycles. The real world is so debased. (And pure math is an ivory tower, yes I know.)

#### [Kevin Buzzard (Nov 30 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856305):
So if you write `#print dvd_refl` directly after the definition in core Lean in `init/algebra/ring.lean`, already the priority is 100. If you remove the `simp` tag then the priority also disappears.

#### [Kevin Buzzard (Nov 30 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856318):
Aah!

#### [Kevin Buzzard (Nov 30 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856373):
https://github.com/leanprover/lean/blob/master/library/init/algebra/ring.lean#L11

#### [Kevin Buzzard (Nov 30 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856392):
```
/- Make sure instances defined in this file have lower priority than the ones
   defined for concrete structures -/
```

And simp lemmas too :-)

#### [Kevin Buzzard (Nov 30 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856457):
Yeah that's it -- my `dvd_refl` now has priority 37.

#### [Patrick Massot (Nov 30 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856531):
MWE
```lean
set_option default_priority 100
@[simp]
lemma pat : 1+1 = 2 := dec_trivial

#print pat
```

#### [Patrick Massot (Nov 30 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856583):
gives `@[simp, priority 100] theorem pat : 1 + 1 = 2 := of_as_true trivia`

#### [Patrick Massot (Nov 30 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856586):
Removing the `set_option` line remove any priority number

#### [Patrick Massot (Nov 30 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856595):
Is this a bug in `set_option` @**Sebastian Ullrich** ?

#### [Mario Carneiro (Nov 30 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856596):
so, does it affect simp?

#### [Patrick Massot (Nov 30 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856655):
Yes!

#### [Patrick Massot (Nov 30 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856671):
```lean
@[simp, priority 200]
lemma pat : 1+1 = 2 := dec_trivial

@[simp, priority 37]
theorem kevin : 1 + 1 = 2 :=
of_as_true trivial

set_option trace.simplify.rewrite true
example : 1 + 1 = 2 := by simp
```

#### [Patrick Massot (Nov 30 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856714):
Changing priorities does change which lemma is used, so it's not a bug in `set_option`, it's an undocumented feature

#### [Reid Barton (Nov 30 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856727):
whoa!

#### [Patrick Massot (Nov 30 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856729):
Or maybe we didn't read the documentation seriously enough

#### [Patrick Massot (Nov 30 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856737):
For instance, maybe we didn't read the source code...

#### [Sebastian Ullrich (Nov 30 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856747):
Yeah, it's clearly spelled out in line 11386

#### [Patrick Massot (Nov 30 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856927):
The documentation file https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/library/tactic/simp_lemmas.cpp mentions priority  all over the place

#### [AHan (Nov 30 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148857208):
@**Johan Commelin**  @**Kevin Buzzard**  Thanks for the suggestion and explanation!!

#### [Patrick Massot (Nov 30 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148857259):
I still wonder whether `set_option default_priority` setting both instance and simp priority is intended behavior. It would also be nice to know whether `simp` would be faster without this mechanism, which seems to be used nowhere

#### [Sebastian Ullrich (Nov 30 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148857918):
```quote
I still wonder whether `set_option default_priority` setting both instance and simp priority is intended behavior.
```
The real problem is the `priority` attribute itself. It doesn't make any sense that it's `[simp, priority 1000]` instead of something like `[simp:1000]` in the first place (and when `priority` is gone, `default_priority` without any extra qualifier doesn't make much sense either). I doubt this will still be the case in Lean 4.
```quote
It would also be nice to know whether `simp` would be faster without this mechanism, which seems to be used nowhere
```
 I don't think so, it's still using the head-symbol index.

#### [Patrick Massot (Nov 30 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148857993):
The printing thing seems easy enough to correct at https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/library/tactic/simp_lemmas.cpp#L175-L180

#### [Patrick Massot (Nov 30 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148858035):
but it's very probably not worth the trouble

