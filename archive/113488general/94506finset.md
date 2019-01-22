---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/94506finset.html
---

## [general](index.html)
### [finset](94506finset.html)

#### [Floris van Doorn (Nov 20 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148072219):
Is the following result somewhere in mathlib? If not, are there results which make it less painful than proving it from scratch using lists?
```
def exists_of_subset_image {α : Type u} {β : Type v} {f : α → β} {s : finset β} {t : set α}
  (h : ↑s ⊆ f '' t) : ∃s' : finset α, ↑s' ⊆ t ∧ s'.image f = s
```

#### [Kenny Lau (Nov 20 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148074485):
```lean
import data.finset

universes u v

theorem exists_of_subset_image {α : Type u} {β : Type v} [decidable_eq α] [decidable_eq β]
  {f : α → β} {s : finset β} {t : set α} (h : ↑s ⊆ f '' t) :
  ∃s' : finset α, ↑s' ⊆ t ∧ s'.image f = s :=
begin
  induction s using finset.induction with a s has ih h,
  { exact ⟨∅, set.empty_subset _, finset.image_empty _⟩ },
  rw [finset.coe_insert, set.insert_subset] at h,
  rcases ih h.2 with ⟨s', hst, hsi⟩,
  rcases h.1 with ⟨x, hxt, rfl⟩,
  refine ⟨insert x s', _, _⟩,
  { rw [finset.coe_insert, set.insert_subset], exact ⟨hxt, hst⟩ },
  rw [finset.image_insert, hsi]
end
```

#### [Kenny Lau (Nov 20 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148074490):
a simple induction

#### [Floris van Doorn (Nov 20 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148074765):
Thanks! `finset.induction` makes this indeed quite easy to prove.

#### [Kenny Lau (Nov 20 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148074832):
can we call this finite_choice... >?<

#### [Floris van Doorn (Nov 21 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148078119):
Different question: should `finset.singleton` be protected? There are two `singleton`s if you open `finset`.
```
import data.finset
open finset
#print singleton
```

#### [Kenny Lau (Nov 21 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148081655):
so... don't open `finset`? /s

#### [Mario Carneiro (Nov 21 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148082475):
or use `finset.singleton` anyway

#### [Mario Carneiro (Nov 21 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148082487):
maybe it should be renamed to `single` or something, it's already far longer than it should be, namely `{x}`

#### [Mario Carneiro (Nov 21 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148082509):
in finset it has a prefix notation `ι`, you could use that

#### [Scott Morrison (Nov 22 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198016):
Hi, possibly a range of `finset` questions coming up... :-)

#### [Scott Morrison (Nov 22 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198018):
Why is `theorem insert.comm (a b : α) (s : finset α) : insert a (insert b s) = insert b (insert a s) := ...` marked as `@[simp]`?

#### [Scott Morrison (Nov 22 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198064):
This seems like a terrible idea, and is responsible for bad simplifications like:
`range (n + 1 + 1)` simplifying to `insert n (insert (n + 1) (range n))`.

#### [Reid Barton (Nov 22 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198073):
how does that not loop?

#### [Scott Morrison (Nov 22 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198074):
That too. :-)

#### [Scott Morrison (Nov 22 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198245):
Does mathlib have something to the effect of `finset.iota n m`, giving the finset of natural numbers `n, n+1, ..., m-1`?

#### [Scott Morrison (Nov 23 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198417):
Oops, `iota` is the wrong name. I guess `finset.interval n m`?

#### [Scott Morrison (Nov 23 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198511):
Hmm.. `data.list.basic` has a peculiarly named `range' s n`, giving the list `[s, s+1, ..., s+n-1]`.

#### [Scott Morrison (Nov 23 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198612):
Okay, removing `@[simp]` on `finset.insert.comm` doesn't break anything, so if there are no complaints I'll PR it later.

#### [Kevin Buzzard (Nov 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198721):
IIRC Chris and Mario had a long discussion about the best way to do the bounds, when Chris was proving things about finite sums a while back

#### [Scott Morrison (Nov 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198726):
So what happened to Chris's work on finite sums?

#### [Scott Morrison (Nov 23 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198734):
Faced with talking to students again, I really want to make `finset.sum` more fun. :-)

#### [Scott Morrison (Nov 23 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148200245):
I'm wondering how people would feel about removing the `@[simp]` from 
```
theorem range_succ : range (succ n) = insert n (range n) := ...
```
I feel like this is often unhelpful. (In fact, in `quadratic_reciprocity.lean` Chris has to write `- range_succ` many times to avoid it firing. Similarly in `order_of_element.lean`.)

This would require either explicitly adding `range_succ` to the simp set in a few places, but not too many. (Three places across mathlib, and it saves many `simp [-range_succ]`s in `quadratic_reciprocity.lean`.)

#### [Scott Morrison (Nov 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148200257):
But in particular as soon as you have a sum of `range (n+1)`, this simp lemma may unhelpfully fire, which is confusing.

#### [Kenny Lau (Nov 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148200291):
Is Scott Morrison talking about `simp`? :P

#### [Scott Morrison (Nov 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148200293):
I love `simp`. I want to use it as much as possible.

#### [Scott Morrison (Nov 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148200294):
Hence I want to remove bad `@[simp]` lemmas that get the maths wrong.

#### [Kenny Lau (Nov 23 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148200300):
I see

#### [Chris Hughes (Nov 23 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148200457):
I don't recall that conversation. I think it was Mario and Patrick. There's definitely a need to make finest.sum nicer, particularly with natural numbers. Also a need for a nice non commutative sum interface.

#### [Scott Morrison (Nov 23 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148201138):
@**Chris Hughes** , if we were going to introduce an `interval n m : finset nat`, and try to make doing sums over natural numbers work nicely with it, would you prefer `interval n m` includes `m`, or not?

#### [Scott Morrison (Nov 23 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148201725):
Does anyone know if
```
lemma finset_sum_split [add_comm_monoid β] (s : finset α) (f : α → β) (P : α → Prop) [decidable_pred P] :
s.sum f = (s.filter P).sum f + (s.filter (λ a, ¬ P a)).sum f := sorry
```
exists in mathlib?

#### [Kenny Lau (Nov 23 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148201736):
yes

#### [Kenny Lau (Nov 23 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148201749):
```lean
import data.finsupp

#check @finsupp.filter_pos_add_filter_neg

/-
finsupp.filter_pos_add_filter_neg :
  ∀ {α : Type u_1} {β : Type u_2} [_inst_1 : decidable_eq α] [_inst_2 : decidable_eq β] [_inst_3 : add_monoid β]
  (f : α →₀ β) (p : α → Prop) [_inst_4 : decidable_pred p] [_inst_5 : decidable_pred (λ (a : α), ¬p a)],
    finsupp.filter p f + finsupp.filter (λ (a : α), ¬p a) f = f
-/
```

#### [Kenny Lau (Nov 23 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148201752):
oh wait

#### [Kenny Lau (Nov 23 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148201753):
they are not exactly the same

#### [Scott Morrison (Nov 23 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148201796):
I see. They're clearly related, but it's not obvious you could even prove mine from this, because of the `decidable_eq` hypotheses.

#### [Scott Morrison (Nov 23 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148201859):
While on the subject, the `[_inst_5 : decidable_pred (λ (a : α), ¬p a)]` argument of `finsupp.filter_pos_add_filter_neg` is unnecessary.

#### [Kenny Lau (Nov 23 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148201968):
```lean
import data.finsupp

lemma finset_sum_split {α β : Type*} [add_comm_monoid β] (s : finset α) (f : α → β) (P : α → Prop) [decidable_pred P] :
s.sum f = (s.filter P).sum f + (s.filter (λ a, ¬ P a)).sum f :=
by haveI := classical.dec_eq α; rw [← finset.sum_union (finset.filter_inter_filter_neg_eq s), finset.filter_union_filter_neg_eq]
```

#### [Scott Morrison (Nov 23 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148202012):
awesome, thank you!

#### [Reid Barton (Nov 23 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148202015):
in principle, it could be relevant at the use site... because decidability arguments are relevant

#### [Scott Morrison (Nov 23 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148202017):
oh, I see, you might want to give separate arguments that P and not P are decidable??

#### [Reid Barton (Nov 23 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148202022):
in principle...

#### [Reid Barton (Nov 23 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148202070):
though it's not very likely especially when the arguments are provided by type class inference and not looking at the expected type

#### [Reid Barton (Nov 23 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148202176):
actually it might not be that unlikely, if both instances come from `prop_decidable`

#### [Sebastien Gouezel (Nov 23 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148212877):
```quote
@**Chris Hughes** , if we were going to introduce an `interval n m : finset nat`, and try to make doing sums over natural numbers work nicely with it, would you prefer `interval n m` includes `m`, or not?
```
 The notation for real intervals is Icc a b for intervals which are closed on both ends, and Ico for closed-open ones, and so on. All this is in `/data/set/intervals`. Ideally, you would use the same syntax prefixed with `finset.`, or something like that. And by the way, the only good convention to do sums is closed on the left and open on the right, i.e., $S_n f = \sum_{i=0}^{n-1}  f(i)$.

#### [Sebastien Gouezel (Nov 23 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148213145):
Fancy Isabelle notation for these (I don't think this has been ported to Lean, or if there could be a parsing problem): `{a..b}` for the closed interval with endpoints `a` and `b`. And `{a<..b}` for the open/closed version. And `{..<b}` for the semiinfinite open one. And so on.

#### [Scott Morrison (Nov 23 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148213855):
I wonder if we could do the actual maths notations for these... `[a,b)`, etc.

#### [Patrick Massot (Nov 23 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214028):
Or the actual maths notations for these... `[a, b[,` etc.

#### [Mario Carneiro (Nov 23 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214030):
nonono

#### [Mario Carneiro (Nov 23 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214031):
that will kill your editor

#### [Mario Carneiro (Nov 23 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214075):
trust me it's not worth it

#### [Patrick Massot (Nov 23 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214076):
see also https://github.com/PatrickMassot/bigop/blob/master/src/tests.lean

#### [Patrick Massot (Nov 23 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214083):
Although Cyril convinced me that Sébastien is right and I should exclude the upper bound from the sum

#### [Mario Carneiro (Nov 23 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214091):
I'm okay with `{a..<b}` and friends. In metamath we used `(a ..^ b)` which is slightly less mnemonic

#### [Mario Carneiro (Nov 23 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214133):
there could be a parsing problem with `{a}`, but it might work as long as `...` doesn't mean anything else... oh

#### [Johan Commelin (Nov 23 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214140):
There is also unicode `…`

#### [Scott Morrison (Nov 23 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214207):
In any case, it sounds like everyone is on board with the "default" being to not include the upper point.

#### [Kevin Buzzard (Nov 23 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214252):
One million python users can't be wrong

#### [Patrick Massot (Nov 23 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214254):
What convinced be is that is avoids some nat substractions. *That* is a killing argument

#### [Scott Morrison (Nov 23 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214257):
I will try to fill in `interval n m` as a list/multiset/finset, and provide a good API for splitting these, into disjoint intervals or endpoint + other interval, for reindexing, etc.

#### [Johan Commelin (Nov 23 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214346):
@**Scott Morrison|110087** How does this tie in to "I'll stop working on maths in Lean for a while, to work a bit on infrastructure..." (just curious)

#### [Scott Morrison (Nov 24 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148253177):
:-)

#### [Scott Morrison (Nov 28 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148689585):
Is there any reason why we don't have `sUnion` on `finset`? This seems like an obvious omission.

#### [Kenny Lau (Nov 28 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148689646):
`finset.bind _ id`?

#### [Scott Morrison (Nov 28 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148689656):
Great, thank you!

#### [Scott Morrison (Nov 28 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148690310):
Is there no `preimage` for `finset`?

#### [Kenny Lau (Nov 28 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148690350):
you could use `finset.filter`

