---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/80075choosingfromdifferenceoffinsets.html
---

## Stream: [new members](index.html)
### Topic: [choosing from difference of finsets](80075choosingfromdifferenceoffinsets.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 09 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133619465):
Here's my "Tactic State":
```lean
α : Type u_1,
_inst_1 : decidable_eq α,
x y S : finset α,
hx : x ⊆ S,
hy : y ⊆ S,
hcard : finset.card x < finset.card y
⊢ ∃ (e : α), e ∈ y \ x
```
I've been digging through `finset` and am not sure what I need to do to kill this goal. Any pointers? It looks like I need to invoke `classical.choice`, but does that mean I need to turn things into `fintype`s?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133619814):
You could prove that `finset.card (y \ x) != 0`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 09 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133620757):
Oops, I should have showed that `S` is nonempty before this point. But I'm still not seeing how to easily work with `finset.card`. Perhaps I should be working with `multiset.card` instead?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133622733):
The interface should all be there, although it might require reading `finset.lean`...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133622824):
So my algorithm for doing questions like this is to type `import finset`, see what auto-complete suggests, find that `finset.lean` is in `data/`, then open finset.lean and search the file for `card` to see what's there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133622922):
`theorem eq_of_subset_of_card_le {s t : finset α} (h : s ⊆ t) (h₂ : card t ≤ card s) : s = t := ...`. Can I work classically?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133622924):
Yes!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133622930):
(didn't read the code part)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133622931):
You should have decidable whatever in this context

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623442):
```lean
import data.finset
import logic.basic

local attribute [instance, priority 0] classical.prop_decidable

example (α) [decidable_eq α] (x y : finset α) (hcard : finset.card x < finset.card y)
: ∃ (e : α), e ∈ y \ x :=
begin
  have hnsub : ¬ (y ⊆ x),
    intro hsub,
    have Heq := finset.eq_of_subset_of_card_le hsub (le_of_lt hcard),
    rw Heq at hcard,
    revert hcard,simp,
  by_contra hnotex,
  have h2 := forall_not_of_not_exists hnotex,
  apply hnsub,
  intros b Hb,
  have h3 := h2 b,
  revert Hb,
  revert h3,
  simp, 
end
```

Amateurish approach. I don't know if I need decidability.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623456):
does removing the local instance break the proof?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 09 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623508):
I think the `by_contra` will break.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623509):
`by_contra hnotex` breaks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 09 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623511):
I tried to do the following as a warmup for the above:
```lean
import data.fintype
variable {α : Type*}
variable [decidable_eq α]

noncomputable def chosen {S : finset α} (h : ¬(S = ∅)) : α := begin
rw [←ne] at h,
have SS : fintype (↑S : set α) := finset_coe.fintype S,
have hSS : nonempty (↑S : set α) := set.nonempty_iff_univ_ne_empty.mpr _,
exact (↑(classical.choice hSS) : α)
end
```
I'm having trouble turning `h : S ≠ ∅` into `⊢ @set.univ ↥↑S ≠ ∅`. Probably I'm just scared by the `↥↑` since I'm not too comfortable with coercions. 

I've also been following something like your algorithm @**Kevin Buzzard** but I wanted to check in and make sure I wasn't missing some obscure lemma elsewhere. Thanks for your solution, I'll study it carefully now!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 09 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623556):
if you make the statement bounded then by_contra will not break

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623557):
`chosen` is definitely noncomputable, but you can use `finset.exists_mem_of_ne_empty` to prove that easily

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 09 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623565):
`classical.sone (exists_mem_of_ne_empty h)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623568):
@**Bryan Gin-ge Chen** you should try and understand Kenny's golfed solution :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 09 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623615):
Thanks Mario and Chris!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623627):
I'm having trouble getting your warm-up to compile. What are the imports and variables?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 09 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623705):
Sorry about that, see the edit.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623756):
My Lean has never heard of `set.nonempty_iff_univ_ne_empty.mpr`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623769):
```
example (α) [decidable_eq α] (x y : finset α) (hcard : finset.card x < finset.card y) : ∃ (e : α), e ∈ y \ x :=
classical.by_contradiction $ λ h,
not_le_of_lt hcard (finset.card_le_of_subset $ by simpa using h)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623814):
Oh sorry, I meant Mario's golfed solution.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623821):
there is a way to prove it without classical stuff, but I will let kenny do that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 09 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623824):
it's in data.set.basic; I guess it was added quite recently https://github.com/leanprover/mathlib/pull/295

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623831):
Oh yes, I have an old project open. Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133624004):
I guess `↥↑S` means the subtype corresponding to the set corresponding to `S`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 09 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133624012):
```quote
there is a way to prove it without classical stuff, but I will let kenny do that
```
roger that
```lean
example (α) [decidable_eq α] (x y : finset α) (hcard : finset.card x < finset.card y) : ∃ (e : α), e ∈ y \ x :=
suffices ∃ e ∈ y, e ∉ x, by simpa,
by_contradiction $ λ H, not_le_of_lt hcard (finset.card_le_of_subset $ by simpa using H)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133624124):
lol, that was easy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133624311):
```lean
noncomputable def chosen {S : finset α} (h : ¬(S = ∅)) : α := begin
  rw [←ne] at h,
  rw ←finset.card_pos at h,
  change 0 < multiset.card S.val at h, -- switching to multisets
  rw multiset.card_pos_iff_exists_mem at h, -- there's now a one-liner that I forgot
  have hinhabited := classical.inhabited_of_exists h,
  cases hinhabited with a,
  exact a
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133624321):
```quote
lol, that was easy
```
oh come on, he just copied your answer ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133624505):
the last three lines can be abbreviated to `exact (classical.inhabited_of_exists h).default`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133624762):
```lean
noncomputable def chosen {α} {S : finset α} (h : ¬(S = ∅)) : α :=
classical.some $ classical.not_forall.1 $
mt finset.eq_empty_of_forall_not_mem h
```


{% endraw %}
