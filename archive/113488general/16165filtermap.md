---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16165filtermap.html
---

## [general](index.html)
### [filter map](16165filtermap.html)

#### [Patrick Massot (May 10 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126378246):
Is this already somewhere in core or mathlib?
```lean
lemma filter_map_comm {I : Type*} {J : Type*} (f : I → J) (P : J → Prop) (r: list I) [decidable_pred P] :
  filter P (map f r) = map f (filter (P ∘ f) r) :=
begin
  induction r with h _ IH,
  { simp },
  { by_cases H : P (f h) ; simp [filter_cons_of_pos, filter_cons_of_neg, H, IH] }
end
```

#### [Simon Hudon (May 10 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126379540):
try:

```
theorem filter_map_eq_map (f : α → β) : filter_map (some ∘ f) = map f :=
theorem filter_map_eq_filter (p : α → Prop) [decidable_pred p] :
  filter_map (option.guard p) = filter p :=
theorem filter_map_filter_map (f : α → option β) (g : β → option γ) (l : list α) :
  filter_map g (filter_map f l) = filter_map (λ x, (f x).bind g) l :=
```

from `data.list.basic`

#### [Patrick Massot (May 10 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126379629):
What do you mean? The lemma is not there but there may be a shorter proof using those results?

#### [Simon Hudon (May 10 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126379663):
Yes exactly. Sorry, I was overly concise

#### [Patrick Massot (May 10 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126379737):
It looks at least as complicated as what I already have

#### [Patrick Massot (May 10 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126379748):
And I don't want to frustrate Kenny by stealing a golfing challenge from him

#### [Simon Hudon (May 10 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126379819):
That's very considerate :)

#### [Patrick Massot (May 10 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126379852):
Actually I'd rather use Kenny (or anyone else) to help me fighting nat substraction

#### [Patrick Massot (May 10 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126379859):
For instance:

#### [Simon Hudon (May 10 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126379865):
I like the resulting proof because it avoids induction

#### [Patrick Massot (May 10 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126379880):
`example (a b k : ℕ) : b + k - (a + k) = b - a `

#### [Patrick Massot (May 10 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126379934):
What do you mean avoid induction? `map` and `filter` are defined inductively

#### [Patrick Massot (May 10 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126379939):
You can at best hide induction

#### [Patrick Massot (May 10 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126379947):
Note that both sides are zero is b is larger than a

#### [Patrick Massot (May 10 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126379959):
So it looks like a "false" result but this one is actually true

#### [Patrick Massot (May 10 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126379962):
I think

#### [Patrick Massot (May 10 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126380041):
Do you have a solution with `filter_map`? Actually it could be useful to learn what `filter_map` is good for

#### [Simon Hudon (May 10 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126380170):
```quote
What do you mean avoid induction? `map` and `filter` are defined inductively
```
They're recursively defined. But yeah, you can never get around using induction / recursion directly or indirectly but I feel hiding induction produces nicer interfaces. The laws about `filter_map` seem like you can prove a lot about `filter` and `map` without induction.

#### [Simon Hudon (May 10 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126380179):
It's a generalization of both `map` and `filter`.

#### [Patrick Massot (May 10 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126380248):
I still don't see how it could help me here

#### [Reid Barton (May 10 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126380518):
```quote
`example (a b k : ℕ) : b + k - (a + k) = b - a `
```
```lean
example (a b k : ℕ) : b + k - (a + k) = b - a :=
nat.add_sub_add_right b k a
```

#### [Patrick Massot (May 10 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126380569):
:astonished:

#### [Simon Hudon (May 10 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126380590):
I think I overlooked a detail. I thought just doing a `rw` would work but here is what I get:

```lean
  rw [← filter_map_eq_map
     ,← filter_map_eq_filter
     ,← filter_map_eq_filter
     ,filter_map_filter_map
     ,filter_map_filter_map],
  congr, funext,
-- ⊢ option.bind ((some ∘ f) x) (option.guard P) = option.bind (option.guard (P ∘ f) x) (some ∘ f)
```

That should be hard either, but it makes the proof longer than expected

#### [Patrick Massot (May 10 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126380594):
That's crazy

#### [Patrick Massot (May 10 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126380596):
That's also crazy

#### [Patrick Massot (May 10 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126380599):
Thanks Reid

#### [Patrick Massot (May 10 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126380617):
I wasn't hoping for this to be in Lean core...

#### [Patrick Massot (May 10 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126381158):
I'm becoming better and better at proof obfuscation. If I ever need to read those proofs, I'll hate myself.

#### [Reid Barton (May 10 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126381226):
it's too hard to resist the golf

#### [Patrick Massot (May 10 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126381282):
Right now I'm staring at line saying `congr_n 1 ; funext ; simp only [nat.add_sub_cancel, nat.add_sub_add_right]`

#### [Patrick Massot (May 10 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126381295):
I wrote two minutes ago

#### [Patrick Massot (May 10 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126381297):
And I already have no clue what it does

#### [Patrick Massot (May 10 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126381299):
Mario and Johannes will be so proud

#### [Patrick Massot (May 10 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126381363):
Because it's half the proof of some trivial statement, and trivial statement must have obfuscated proof according to mathlib style guide

#### [Patrick Massot (May 10 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126381371):
```lean
lemma big.shift (P : ℕ → Prop) [decidable_pred P] (F : ℕ → R) (a b k : ℕ) : 
  (big[(◆)/nil]_(i=a..b | (P i)) (F i)) = (big[(◆)/nil]_(i=(a+k)..(b+k) | (P (i-k))) (F (i-k))) :=
begin
  rw [range'_add_map, big.map],
  congr_n 1 ; funext ; simp only [nat.add_sub_cancel, nat.add_sub_add_right]
end
```

#### [Patrick Massot (May 10 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126381380):
(for instance `big[(◆)/nil]` could be a `\Sum` operator

#### [Kevin Buzzard (May 10 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126381460):
This is just the sort of stuff which I really needed last November and wasn't there

#### [Kevin Buzzard (May 10 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126381471):
I remember having to give up on a 1st year problem sheet question because I couldn't prove that sum from 1 to n was equal to sum from n to 1 :-)

#### [Kevin Buzzard (May 10 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126381475):
[at the time]

#### [Reid Barton (May 10 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126381521):
imagine where we'd be if Gauss had had a computer

#### [Kevin Buzzard (May 10 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126381527):
I don't even want to think about that

#### [Kevin Buzzard (May 10 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126381534):
how much time did Gauss and Euler waste working out examples etc

#### [Patrick Massot (May 10 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126381541):
They would have had computer aided waste of time instead

#### [Kevin Buzzard (May 10 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126381556):
Maybe they would have just played minecraft all day

#### [Kevin Buzzard (May 10 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126381559):
and we'd be worse off

#### [Patrick Massot (May 10 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126381562):
yep

#### [Patrick Massot (May 10 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126381571):
or watched lol cats on youtube

#### [Sean Leather (May 11 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126402529):
If they were functional programmers (esp. in Haskell), I think they would have enjoyed [Lambdacats](https://spl.smugmug.com/Humor/Lambdacats/).

#### [Moses Schönfinkel (May 11 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126404033):
Hehe, we're slowly eroding formality of this forum :).

#### [Patrick Massot (May 11 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126404169):
I think it was already pretty badly eroded

#### [Moses Schönfinkel (May 11 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126404210):
I believe cat pictures are new tho.

#### [Moses Schönfinkel (May 11 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126404214):
Dank memes next.

#### [Sean Leather (May 11 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter map/near/126405008):
```quote
Hehe, we're slowly eroding formality of this forum :).
```
Given that theorem proving is a formal method, what does an eroded formal method look like? :thinking_face:

Ah ha! :light_bulb: This must be why the name “lean” was chosen: the methodological mountain was so eroded, it couldn't stand up straight.

