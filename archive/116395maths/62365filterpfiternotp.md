---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/62365filterpfiternotp.html
---

## [maths](index.html)
### [filter p + fiter not p](62365filterpfiternotp.html)

#### [Kevin Buzzard (Aug 15 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132190025):
```lean
import data.multiset

open multiset

example (α : Type*) (M : multiset α) (p : α → Prop) [decidable_pred p]:
filter p M + filter (λ a, ¬ p a) M = M := sorry
```

I want this to be much easier than it's turning out to be! Should I be using `add_sub_of_le`?

#### [Kevin Buzzard (Aug 15 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132190288):
Aah Chris has given me a hint :-)

#### [Kevin Buzzard (Aug 15 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132195469):
I'm actually trying to prove this:

```lean
example (L : multiset ℕ) (H : ∀ l ∈ L, l = 4 ∨ l = 6 ∨ l ≥ 8) :
L = filter (λ l, l = 4) L + filter (λ l, l = 6) L + filter (λ l, l ≥ 8) L := sorry
```

and I had suspected I'd be done if I had the example above but now I realise I also need 

```lean
example {α : Type*} (L : multiset α) (p : α → Prop) (q : α → Prop)
[decidable_pred p] [decidable_pred q] : 
filter p (filter q L) = filter (λ a, p a ∧ q a) L
```

which I'd assumed would be there. 

Am I not thinking about this in the right way?

#### [Mario Carneiro (Aug 15 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132195624):
I recently discovered that omission as well

#### [Mario Carneiro (Aug 15 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132195642):
I could have sworn there was a theorem like that already

#### [Kevin Buzzard (Aug 15 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132196310):
For the filter filter thing I've just discovered `filter_map`

#### [Kevin Buzzard (Aug 15 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132196408):
There's `filter_map_filter_map`, `filter_filter_map` and `filter_map_eq_filter` and it might be a case of putting these things together.

#### [Kevin Buzzard (Aug 15 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132196580):
Another thing I need is 
```lean
example (α : Type*) (p q : α → Prop) (L : multiset α) (H : ∀ l ∈ L, p l ↔ q l)
[decidable_pred p] [decidable_pred q] : 
filter p L = filter q L := sorry
```

which I suspect I can get with judicious application of `filter_le`

#### [Mario Carneiro (Aug 15 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132197033):
that should definitely be there, it should be called `filter_congr`

#### [Kevin Buzzard (Aug 15 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132197419):
It seems that it's there for lists but not multisets. Would you try and deduce it for multisets from the list result or use `le_filter`?

#### [Kevin Buzzard (Aug 15 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132198058):
```lean
theorem filter_congr (α : Type*) (p q : α → Prop) (L : multiset α) (H : ∀ l ∈ L, p l ↔ q l)
[decidable_pred p] [decidable_pred q] :
filter p L = filter q L := 
le_antisymm 
  (le_filter.2 ⟨filter_le _,λ a Ha, by rw mem_filter at Ha;exact (H a Ha.1).1 Ha.2⟩) 
  (le_filter.2 ⟨filter_le _,λ a Ha, by rw mem_filter at Ha;exact (H a Ha.1).2 Ha.2⟩)
```

I'm now at the stage where I can usually prove these things, but am wondering whether I should be trying to prove them or just asking one of the experts to prove it in half the time. I guess a few months ago I had a Mario factor of 10, but maybe he'd have a job making that proof ten times smaller.

#### [Kevin Buzzard (Aug 15 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132198230):
@**Kenny Lau** when you wake up you might like these

#### [Mario Carneiro (Aug 15 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132198236):
```
lemma filter_congr {p q : α → Prop} [decidable_pred p] [decidable_pred q]
  {s : multiset α} : (∀ x ∈ s, p x ↔ q x) → filter p s = filter q s :=
quot.induction_on s $ λ l h, congr_arg coe $ filter_congr h
```

#### [Mario Carneiro (Aug 15 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132198257):
that's like a mario factor of 2.5 or so

#### [Mario Carneiro (Aug 15 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132198259):
so definite improvement :)

#### [Kevin Buzzard (Aug 15 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132198264):
so you did go for the list approach. Quotients still scare me :-/

#### [Mario Carneiro (Aug 15 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132198307):
the theorem was already there...

#### [Mario Carneiro (Aug 15 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132198316):
quot.induction_on is great, since everything is suddenly defeq to the equivalent list definition

#### [Kevin Buzzard (Aug 15 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132199346):
So I look at it and think "crumbs, I'll end up having to prove that if L1 and L2 are lists which biject with each other then so do filter p L1 and filter p L2, I'm not sure I fancy that..."

#### [Chris Hughes (Aug 15 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132199458):
There's only one list.

#### [Kevin Buzzard (Aug 15 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132200798):
I just spent some time actually looking at Mario's proof, and somehow he doesn't have to do at all what I expected him to have to do. The work I imagined having to do is already done in the definition of `multiset.filter`. Hence the proof is much easier than I'd imagined.

#### [Kevin Buzzard (Aug 15 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132201117):
There are 45 instances of this `congr_arg coe` trick in `multiset.lean`

#### [Mario Carneiro (Aug 15 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132201380):
it's basically just saying that when two lists are equal then the multisets they generate are also equal

#### [Mario Carneiro (Aug 15 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132201440):
it's very common for multiset equalities after applying `quot.induction_on` since you might know that the lists are equal

#### [Mario Carneiro (Aug 15 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132201459):
for example, associativity of addition of multisets follows from associativity of append on lists, but since the goal is to show that the multisets are equal rather than the lists, we have to `congr_arg coe`

#### [Mario Carneiro (Aug 15 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132201474):
if instead, we knew not that the lists were equal but that they were permutations of each other, we would use `quot.sound` instead

#### [Kevin Buzzard (Aug 16 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132202271):
```lean
example {α : Type*} (L : multiset α) (p : α → Prop) (q : α → Prop)
[decidable_pred p] [decidable_pred q] :
filter p (filter q L) = filter (λ a, p a ∧ q a) L :=
begin
  rw ←filter_map_eq_filter q,
  rw filter_filter_map,
  rw ←filter_map_eq_filter,
  congr,
  funext,
  unfold option.filter,
  unfold option.guard,
  split_ifs;unfold option.bind; try {unfold option.guard;split_ifs},
  finish,cc,finish,refl,finish,
end
```

I kept wanting it to die but it wouldn't die. I'm not sure this one is mathlib-ready.

#### [Mario Carneiro (Aug 16 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132203124):
no worries, I killed it

#### [Mario Carneiro (Aug 16 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132203154):
> `finish,cc,finish,refl,finish`

lol, I'm imagining kevin stabbing the proof "die! die! you're finished!"

#### [Kevin Buzzard (Aug 16 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132206369):
I guess I can do the original question using `multiset.ext` if I had these:

```lean
theorem count_filter_eq_zero (α : Type*) (M : multiset α) (p : α → Prop)
(a : α) [decidable_eq α] [decidable_pred p]
(hnp : ¬ p a) : count a (filter p M) = 0 :=
begin
  rw count_eq_zero,
  intro Hin,
  rw mem_filter at Hin,
  apply hnp,
  exact Hin.right
end

theorem count_filter (α : Type*) (M : multiset α) (p : α → Prop) (a : α) [decidable_eq α] [decidable_pred p]
(hp : p a) : count a M = count a (filter p M) := sorry 
```

Straightforward for the first one and could easily be mathlibbed up; one could also define `count_filter` to mean `count a (filter p M) = if (p a) then count a M else 0`, perhaps that's the natural lemma?

#### [Mario Carneiro (Aug 16 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132206556):
I added the theorems fyi

#### [Kevin Buzzard (Aug 16 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132207003):
Oh thanks! I was checking email waiting for a push but I now realise that I only get emails for PR's.

#### [Kenny Lau (Aug 17 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132285416):
```lean
import data.multiset

open multiset

theorem filter_inclusion_exclusion (α : Type*) (p q : α → Prop)
  [decidable_pred p] [decidable_pred q] (L : multiset α) :
  filter p L + filter q L = filter (λ x, p x ∨ q x) L + filter (λ x, p x ∧ q x) L :=
multiset.induction_on L (by simp) $ λ hd tl ih,
by by_cases H1 : p hd; by_cases H2 : q hd; simpa [H1, H2] using ih

example (L : multiset ℕ) (H : ∀ l ∈ L, l = 4 ∨ l = 6 ∨ l ≥ 8) :
L = filter (λ l, l = 4) L + filter (λ l, l = 6) L + filter (λ l, l ≥ 8) L :=
have H1 : filter (λ (x : ℕ), x = 4 ∧ x = 6) L = 0,
  from filter_eq_nil.2 $ λ _ _ H, by cc,
have H2 : filter (λ (x : ℕ), (x = 4 ∨ x = 6) ∧ x ≥ 8) L = 0,
  from filter_eq_nil.2 $ λ _ _ H, by cases H.1; subst h;
  from absurd H.2 dec_trivial,
by rw [filter_inclusion_exclusion, H1, add_zero];
rw [filter_inclusion_exclusion, H2, add_zero];
symmetry; rw [filter_eq_self]; intros;
rw [or_assoc]; solve_by_elim
```

#### [Mario Carneiro (Aug 17 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132286367):
`filter_inclusion_exclusion` is already in mathlib, I think I called it `filter_add_filter`

#### [Kevin Buzzard (Aug 17 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132288987):
@**Ellen Arlt** with this and the 468 lemma you can break up your multiset into those three multisets, and evaluate the sum for the fully controlled value on each one. This is how I would prove the second lemma you emailed me. I'm in a field right now with no laptop so can't do it, but everything you need is now there thanks to Mario and Kenny. If you've not done it by Tuesday I can help then.

#### [Kevin Buzzard (Aug 17 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132289276):
Are these holes in mathlib by the way? Here's a stupid question. Is there not yet some completely standard list of "all the things that should be proved about multisets" somewhere, and when people make new proof verifiers they just copy the list? I know `multiset.lean` is long but in some sense are we still "making it up as we go along" and adding things people need, or will this stop at some point, or is there a known list (eg whatever the analogous file is in coq or whatever) of facts which people will need and which haven't all been written up yet? I'm assuming not. I'm asking what multiset.lean will look like in 5 years' time basically

#### [Mario Carneiro (Aug 17 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132289497):
I think it is a process of continuous addition with a finite limit

#### [Sean Leather (Aug 17 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132289507):
I think there are a couple of things here:

1. It's hard to imagine all the theorems needed to make a theory (e.g. of multisets) complete.
2. Even if you can imagine them all, it will take time to implement them.
3. If you don't release before you implement them all, nobody else can use what you have in the meantime.

#### [Mario Carneiro (Aug 17 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132289524):
for example, `filter_inclusion_exclusion` is on that list, this 468 lemma is not

#### [Mario Carneiro (Aug 17 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132289586):
the criterion is basically to have maximally general theorems which combine at most two or three concepts together

#### [Mario Carneiro (Aug 17 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132289624):
i.e. `a + b + c = a + (b + c)` is a good lemma, `a + (a + b) + c + (d + e) = e + a + (a + c) + (d + b)` is not

#### [Mario Carneiro (Aug 17 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132289841):
Coq probably has a similar file, and they are going through a similar process, but since their file is older I'm sure they will be closer to convergence and we might find a few lemmas there that aren't in mathlib. But no one has the complete list, and like any convergent sequence of integers I'm not sure we would know that we have converged when we do

#### [Sean Leather (Aug 17 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132289918):
So we need a (meta) proof that the theory is complete...

#### [Mario Carneiro (Aug 17 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132290080):
I think that in principle you could write a program to generate these facts. The hart part would be picking only the true ones

#### [Mario Carneiro (Aug 17 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132290108):
But keep in mind that this generation process is also highly dependent on what definitions exist. The more definitions you have, the more ways there are to combine them

#### [Mario Carneiro (Aug 17 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132290159):
so a definition can make a previously arbitrary looking statement become a natural question

#### [Mario Carneiro (Aug 17 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132290182):
and this is why I take seriously the introduction of new definitions, since every definition comes with a cloud of associated theorems to prove

#### [Gabriel Ebner (Aug 17 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132290240):
```quote
I think that in principle you could write a program to generate these facts. The hart part would be picking only the true ones
```
Moa Johannson has done some work on theory exploration; [IsaHipster](https://github.com/moajohansson/IsaHipster) is pretty much such a tool for Isabelle.  Essentially, they enumerate statements up to a certain size and use random testing to filter out obviously wrong ones.  The rest are handed to sledgehammer.

#### [Scott Morrison (Aug 22 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter p + fiter not p/near/132559474):
Ugh... I'm not sure I want to be part of a tradition of mathematics that works that way. :-)

