---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/73586rwunderaunion.html
---

## Stream: [general](index.html)
### Topic: [rw under a union](73586rwunderaunion.html)

---

#### [Kevin Buzzard (May 14 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126553772):
```lean
import data.set 
example (α γ : Type)  (F G : γ → set α)
  (H : ∀ (i : γ), F i = G i) : (⋃ (i : γ), F i)  = ⋃ (i : γ), G i :=
begin
  refine set.subset.antisymm _ _,
  { apply set.Union_subset_Union,
    intro i,rw (H i),
  },
  { apply set.Union_subset_Union,
    intro i,rw (H i),
  },
end 
```

#### [Kevin Buzzard (May 14 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126553840):
Is there a more sensible method to prove that if `F i = G i` for all `i` then the union of the `F i` equals the union of the `G i`? I couldn't figure out how to rewrite within the union.

#### [Kevin Buzzard (May 14 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126553854):
Sorry, the Union.

#### [Chris Hughes (May 14 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126553895):
```lean
example (α γ : Type)  (F G : γ → set α)
  (H : ∀ (i : γ), F i = G i) : (⋃ (i : γ), F i)  = ⋃ (i : γ), G i :=
by rw funext H
```

#### [Kevin Buzzard (May 14 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126553981):
ha ha that's clever :-)

#### [Patrick Massot (May 14 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554007):
```lean
example (α γ : Type)  (F G : γ → set α)
  (H : ∀ (i : γ), F i = G i) : (⋃ (i : γ), F i)  = ⋃ (i : γ), G i :=
by finish
```

#### [Patrick Massot (May 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554017):
Use automation Luke

#### [Kevin Buzzard (May 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554071):
What does `finish` do?

#### [Patrick Massot (May 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554073):
It finishes the proof

#### [Kevin Buzzard (May 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554074):
every time??

#### [Patrick Massot (May 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554079):
Yes, nobody told you?

#### [Patrick Massot (May 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554083):
You could also use `congr` here

#### [Kevin Buzzard (May 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554095):
I've seen `congr` do rewrites I couldn't do before, I should have tried this

#### [Kevin Buzzard (May 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554101):
I tried `conv` but I couldn't get that to work either

#### [Kevin Buzzard (May 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554103):
and it was the last line of a 250 line proof :-)

#### [Kevin Buzzard (May 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554104):
so I cheated and asked here.

#### [Kevin Buzzard (May 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554107):
I should be marking Chris' exam script!

#### [Kevin Buzzard (May 14 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554147):
But I am sick of affine schemes not being schemes

#### [Patrick Massot (May 14 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554151):
Recently I got to this situation where the goal is `a = a` (but not if `pp.all`) and `congr` alone finished the proof

#### [Patrick Massot (May 14 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554164):
You should have made that formalization the exam

#### [Kevin Buzzard (May 14 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554192):
next year

#### [Kevin Buzzard (May 14 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554243):
What would I do without this chat. Things would go so much more slowly.

#### [Patrick Massot (May 14 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554551):
I'm always fighting the temptation to post every lemma I need here

#### [Patrick Massot (May 14 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554597):
I hope to reduce my dependence a bit

#### [Patrick Massot (May 14 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554609):
But I'm still interested in learning better ways. Here are two lemmas I proved tonight. Usual questions: are there already there? What is the proof from the book?

#### [Patrick Massot (May 14 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554618):
```lean
lemma foldr_ext {α : Type*} {β : Type*} {l : list α} (f f' : α → β → β) (s : β)
  (H : ∀ a ∈ l, ∀ b : β, f a b = f' a b) : foldr f s l = foldr f' s l :=
begin
  induction l with h t IH,
  { simp },
  { have H' := H h (by simp),
    suffices : foldr f s t = foldr f' s t, by simp [H', this],
    apply IH,
    intros a a_t,
    exact H a (by simp[a_t]) }
end
```

#### [Patrick Massot (May 14 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554683):
```lean
lemma filter_ext {α : Type*} {r: list α} (P P') [decidable_pred P] [decidable_pred P'] 
  (HP : ∀ i ∈ r, P i = P' i) : filter P r = filter P' r :=
begin
  induction r with h t IH,
  { simp },
  { have HPh : P h = P' h := HP h (by simp),
    have : ∀ (i : α), i ∈ t → P i = P' i,
    { intros i i_t,
      exact (HP i $ by simp [i_t]) },
    by_cases H : P h, 
    { have H' : P' h := HPh ▸ H,
      simp [H, H', IH this] },
    { have H' : ¬ P' h := HPh ▸ H, 
      simp [H, H', IH this] } }
end
```

#### [Patrick Massot (May 14 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554698):
I haven't tried to obfuscate the proofs

#### [Kevin Buzzard (May 14 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554707):
ha ha can you do the first one with Chris' trick?

#### [Patrick Massot (May 14 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554754):
But I'm sure two lines are enough

#### [Patrick Massot (May 14 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554775):
I don't think so, you must not forget we have informations only on elements of the list

#### [Kevin Buzzard (May 14 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554779):
oh yes

#### [Patrick Massot (May 14 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554780):
This condition seems a bit too specific

#### [Patrick Massot (May 14 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554786):
For instance, start with `congr` and you loose

#### [Kevin Buzzard (May 14 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554788):
Do I need an import for these? I just this minute upgraded mathlib in my project and I'm re-building it

#### [Kevin Buzzard (May 14 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554829):
so maybe I just have to wait

#### [Kevin Buzzard (May 14 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554831):
but I have complaints about foldr currently

#### [Patrick Massot (May 14 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554836):
`import data.list.basic`

#### [Patrick Massot (May 14 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554837):
sorry

#### [Kevin Buzzard (May 14 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555316):
`list.foldr_hom` is too strong

#### [Patrick Massot (May 14 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555384):
Too strong?

#### [Kevin Buzzard (May 14 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555393):
For your application

#### [Kevin Buzzard (May 14 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555398):
like Chris' idea

#### [Kevin Buzzard (May 14 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555403):
Same problem

#### [Patrick Massot (May 14 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555410):
right

#### [Chris Hughes (May 14 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555898):
```lean
lemma foldr_ext {α : Type*} {β : Type*} {l : list α} (f f' : α → β → β) (s : β)
  (H : ∀ a ∈ l, ∀ b : β, f a b = f' a b) : foldr f s l = foldr f' s l :=
by induction l; simp * {contextual := tt}
```

#### [Patrick Massot (May 14 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555909):
:open_mouth:

#### [Kenny Lau (May 14 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555923):
@**Chris Hughes** can you derive normal and curvature for r=xi+f(x)j?

#### [Patrick Massot (May 14 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555943):
@**Kenny Lau** is this the mechanics exam running joke again?

#### [Kenny Lau (May 14 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555948):
is it a joke when the exam is tomorrow?

#### [Patrick Massot (May 14 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556102):
Thank you Chris for not revising mechanics

#### [Patrick Massot (May 14 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556105):
I disapprove of course

#### [Patrick Massot (May 14 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556108):
But I still take your proof

#### [Chris Hughes (May 14 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556116):
I can as of today. @**Kenny Lau**

#### [Kenny Lau (May 14 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556133):
ok you win

#### [Chris Hughes (May 14 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556183):
curvature is dn / ds, where s is arc length I think.

#### [Chris Hughes (May 14 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556192):
and n is normal

#### [Patrick Massot (May 14 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556199):
He can golf *and* compute curvature. What a man!

#### [Kevin Buzzard (May 14 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556397):
So what is going on with Chris' proof? I feel like I can learn something important here

#### [Kevin Buzzard (May 14 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556399):
Induction -- sure. Simp does the base case

#### [Kevin Buzzard (May 14 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556403):
simp doesn't do the inductive step.

#### [Kevin Buzzard (May 14 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556405):
by itself.

#### [Kenny Lau (May 14 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556407):
it's a semicolon

#### [Kenny Lau (May 14 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556450):
`simp` is simultaneously applied to both goals

#### [Kenny Lau (May 14 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556451):
the base case and the inductive step

#### [Patrick Massot (May 14 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556453):
`contextual` seems to do the magic trick

#### [Kenny Lau (May 14 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556457):
what does `contextual` do?

#### [Patrick Massot (May 14 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556461):
uses context

#### [Kenny Lau (May 14 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556465):
isn't that `simp *`?

#### [Patrick Massot (May 14 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556496):
I hate natural number arithmetic, so I'm cheating for this one. Who could prove me `b < a` implies `b + 1 - a = 0`?

#### [Kevin Buzzard (May 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556576):
maybe b < a -> (b + 1) <= a

#### [Kenny Lau (May 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556581):
they are equivalent

#### [Kenny Lau (May 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556584):
definitionally

#### [Patrick Massot (May 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556587):
That could be a step yes

#### [Kevin Buzzard (May 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556590):
oh they are defeq right? ;-)

#### [Kenny Lau (May 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556596):
so something like `sub_le_zero_of_le`?

#### [Kenny Lau (May 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556601):
(deleted)

#### [Kenny Lau (May 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556649):
oh wait nothing

#### [Kenny Lau (May 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556657):
maybe you want `nat.eq_zero_of_le_zero` if it exists

#### [Kevin Buzzard (May 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556661):
```lean
import data.list.basic
open list
lemma foldr_ext {α : Type*} {β : Type*} {l : list α} (f f' : α → β → β) (s : β)
  (H : ∀ a ∈ l, ∀ b : β, f a b = f' a b) : foldr f s l = foldr f' s l :=
begin
  induction l with h t IH,
  { simp },
  simp * {contextual := tt},
end
```

#### [Kevin Buzzard (May 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556663):
The semicolon isn't important

#### [Kenny Lau (May 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556664):
it is, because it allows you to apply `simp` to both goals

#### [Kevin Buzzard (May 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556669):
but the contextual is

#### [Kenny Lau (May 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556671):
without the semicolon you need to write it twice

#### [Kevin Buzzard (May 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556674):
sure

#### [Kevin Buzzard (May 14 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556684):
Oh I see what you're saying -- what I am saying is trivial.

#### [Kevin Buzzard (May 14 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556688):
I'm just unravelling the semicolon

#### [Kevin Buzzard (May 14 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556692):
the contextual isn't important for the base case but for the inductive step we have an inductive hypothesis which needs to be used

#### [Kenny Lau (May 14 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556700):
does `simp [*]` work?

#### [Gabriel Ebner (May 14 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556778):
Contextual does not refer to context as in "induction hypothesis" but to the left-hand side of implications: in `a = b -> P a`, contextual allows simp to use the equation `a=b` to simplify `P a`.

#### [Kenny Lau (May 14 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556780):
oh

#### [Kevin Buzzard (May 14 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556790):
`nat.sub_eq_zero_iff_le`

#### [Kevin Buzzard (May 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556860):
`example (a b : ℕ) : b < a → b + 1 - a = 0 := nat.sub_eq_zero_of_le`

#### [Kenny Lau (May 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556865):
aha

#### [Kevin Buzzard (May 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556867):
using the trick that b < a is by definition b+1 <= a

#### [Kevin Buzzard (May 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556869):
as Kenny pointed out

#### [Kevin Buzzard (May 14 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556916):
(see `#print nat.lt`)

#### [Patrick Massot (May 14 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556928):
Thank you very much

#### [Kevin Buzzard (May 14 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556989):
This `contextual` thing is not documented in my simp docs -- I looked through the source or the docs (I don't remember, maybe the source), saw it was there and mentioned it but basically also said I didn't know what it di.

#### [Kevin Buzzard (May 14 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556990):
d

#### [Kevin Buzzard (May 14 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557009):
I don't quite understand Gabriel's explanation -- is `a = b -> P a` supposed to be a hypothesis or a goal?

#### [Kenny Lau (May 14 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557013):
goal

#### [Kenny Lau (May 14 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557022):
hmm, but the goal is not an implication

#### [Kevin Buzzard (May 14 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557030):
```quote
does `simp [*]` work?
```
no

#### [Kevin Buzzard (May 14 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557125):
right -- the implications are in the hypotheses

#### [Kevin Buzzard (May 14 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557127):
Maybe it's just magic

#### [Kevin Buzzard (May 14 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557131):
"Lean does not do magic" -- K. Lau, a couple of months ago

#### [Kevin Buzzard (May 14 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557175):
The comment inspired me to start really thinking about how some of the techniques I had picked up actually worked

#### [Mario Carneiro (May 14 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557393):
```
lemma filter_congr {p q : α → Prop} [decidable_pred p] [decidable_pred q]
  : ∀ {l : list α}, (∀ x ∈ l, p x ↔ q x) → filter p l = filter q l
| [] _     := rfl
| (a::l) h := by simp at h; by_cases pa : p a;
  [simp [pa, h.1.1 pa, filter_congr h.2],
   simp [pa, mt h.1.2 pa, filter_congr h.2]]
```

Regarding naming: A theorem of the form `a = b -> F a = F b` is a "congruence" theorem, named with `congr` at the end. An "extensionality" theorem has the form `F a = F b -> a = b` where `F` is some appropriate (collection of) projection-like operations

#### [Mario Carneiro (May 14 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557415):
`map_congr` exists in `list.basic` but not all list theorems have congr theorems stated for them

#### [Patrick Massot (May 14 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557583):
Thanks!

#### [Patrick Massot (May 14 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557592):
Is there any difference between my `p x = q x` and your `p x ↔ q x` here?

#### [Mario Carneiro (May 14 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557609):
No, given `propext`, but mathlib convention is to use `iff` instead of `eq` for equivalent propositions

#### [Mario Carneiro (May 14 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557632):
Otherwise you have to face weird theorems like `(a = b) = c = b`

#### [Chris Hughes (May 14 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557712):
It more or less does `intros; simp *` I think

#### [Chris Hughes (May 14 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557713):
But I just realise that can't be what it does, because my example didn't have anything to intro.

#### [Chris Hughes (May 14 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557714):
and `simp *` doesn't work

#### [Patrick Massot (May 14 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126558301):
Going from = to iff broke a magic `finish` success

#### [Patrick Massot (May 14 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126558311):
Probably by breaking a magic `cc` under the hood

#### [Patrick Massot (May 14 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126558380):
This natural number substraction is really a nightmare. Now I want `b + k + 1 - (a + k) = b + 1 - a`. It's almost the same I had a couple of days ago. But I'm stuck again...

#### [Patrick Massot (May 14 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126558463):
It seems like I really need `omega` in the end

#### [Patrick Massot (May 14 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126558972):
Is there any hope to use Coq to tell me a proof Lean could understand?

#### [Andrew Ashworth (May 14 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126559159):
No, in general the names of the lemmas used in Coq would be different

#### [Patrick Massot (May 14 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126559200):
But can you get the sequence of Coq lemmas used by omega?

#### [Andrew Ashworth (May 14 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126559219):
I do not have a Coq installation in front of me to look at the output of omega, so I don't know

#### [Andrew Ashworth (May 14 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126559407):
What I did when i had a lot of similar problems was write down a cheat sheet of relevant cancellation lemmas in my notebook... looking them all up was my biggest hurdle

#### [Patrick Massot (May 14 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126559611):
Now I need `H : a ≤ b ⊢ 2 * a + (b + 1 - a) - i - 1 = a - i + b`. I give up for today

#### [Patrick Massot (May 14 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126559664):
I have four proofs stuck because of such stupid goals

#### [Kenny Lau (May 14 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126559670):
I understand your feeling

#### [Kevin Buzzard (May 15 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126563181):
```quote
Going from = to iff broke a magic `finish` success
```
You can just deduce your old version from Mario's version of course...

#### [Kevin Buzzard (May 15 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126563201):
```quote
This natural number substraction is really a nightmare. Now I want `b + k + 1 - (a + k) = b + 1 - a`. It's almost the same I had a couple of days ago. But I'm stuck again...
```
I really like doing these. Patrick -- just type nat.sub and then ctrl-space escape ctrl-space to see what Lean has, you can just browse through stuff.

#### [Kevin Buzzard (May 15 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126563696):
Actually I don't understand how ctrl-space works at all. I just managed to type `nat.sub` and get it to display `nat.add_sub_add_left` (which is useful for you) and then after esc ctrl-space I don't see it any more

#### [Kevin Buzzard (May 15 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126563797):
```lean
example (a b k : ℕ) : b + k + 1 - (a + k) = b + 1 - a := calc 
b + k + 1 - (a + k) = k + (b + 1) - (k + a) : by simp [add_assoc,add_comm]
... = b + 1 - a : by rw nat.add_sub_add_left
```

#### [Kevin Buzzard (May 15 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126563842):
```lean
example (a b k : ℕ) : b + k + 1 - (a + k) = b + 1 - a := calc 
b + k + 1 - (a + k) = b + 1 + k - (a + k) : by simp
... = b + 1 - a : by rw nat.add_sub_add_right
```

#### [Kevin Buzzard (May 15 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126564406):
```quote
Now I need `H : a ≤ b ⊢ 2 * a + (b + 1 - a) - i - 1 = a - i + b`. I give up for today
```
If `i > a` but `i <= a + b` then this one won't be true, because `a - i + b` is `(a - i) + b`

#### [Kevin Buzzard (May 15 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126564613):
Here's some true version:

#### [Kevin Buzzard (May 15 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126564616):
```lean
example (a b i : ℕ) (H : a ≤ b) : 2 * a + (b + 1 - a) - i - 1 = a + b - i := 
calc 2 * a + (b + 1 - a) - i - 1 = a + (a + (b + 1 - a)) - i - 1 : by simp [two_mul]
... = a + (b + 1) - i - 1 : by rw nat.add_sub_of_le (le_trans H (nat.le_succ _))
... = (a + b) + 1 - (i + 1)  : by simp [add_assoc,nat.sub_sub]
... = a + b - i : by rw nat.add_sub_add_right
```

#### [Andrew Ashworth (May 15 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126564908):
```quote
```quote
This natural number substraction is really a nightmare. Now I want `b + k + 1 - (a + k) = b + 1 - a`. It's almost the same I had a couple of days ago. But I'm stuck again...
```
I really like doing these. Patrick -- just type nat.sub and then ctrl-space escape ctrl-space to see what Lean has, you can just browse through stuff.
```
Ctrl-T and typing sub brings up lemmas with sub inside

#### [Mario Carneiro (May 15 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126574769):
By the way patrick, your "stupid goals" are exactly why I wrote `range'` to take a start and length instead of start and end. Remember, the value of a good modeling decision is not in the beauty of the statements but in the beauty of the proofs. When things are done right, the proof is like everything is given to you just as you need it, but when you write things in a cumbersome way the proofs become orders of magnitude more cumbersome.

#### [Mario Carneiro (May 15 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126574827):
If your desire for clean statements overrides this concern, then just have two versions and write from the "porcelain" version (which looks nice but is hard to work with) to the "plumbing" version (optimized for proofs) before proving anything, and just translate back at the end.

#### [Mario Carneiro (May 15 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126575178):
But cumbersome is as cumbersome does, here's a proof:
```
example (a b k : ℕ) : b + k + 1 - (a + k) = b + 1 - a :=
by rw [add_comm a, ← nat.sub_sub, add_right_comm, nat.add_sub_cancel]
```
and a counterexample:
```
#eval do
  a ← list.range 3,
  b ← list.range 3,
  i ← list.range 3,
  return $ to_bool (∀ (_:a ≤ b), 2 * a + (b + 1 - a) - i - 1 = a - i + b)
 -- [tt, tt, tt, tt, ff, ff, tt, ff, ff, tt, tt, tt, tt, tt, ff, tt, tt, ff, tt, tt, tt, tt, tt, tt, tt, tt, tt]
```
That's my version of isabelle quickcheck - I just evaluated the theorem at some small numbers and it sometimes fails.

#### [Mario Carneiro (May 15 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126575374):
Assuming you don't want to learn the beautiful theory of monus on the naturals, but just want to pretend it's regular subtraction, I recommend you treat it like a partial function, in the sense that you never state a theorem about `-` unless the fact that the RHS is less or equal to the LHS is in the context or otherwise deducible. Your second theorem fails this, since it has a variable `i` being subtracted from stuff even though there is no upper bound on it.

#### [Mario Carneiro (May 15 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126575537):
hm, maybe this is a slightly nicer quickcheck:
```
#eval do
  a ← list.range 5,
  b ← list.range 5,
  i ← list.range 5,
  guardb (a ≤ b),
  guardb (2 * a + (b + 1 - a) - i - 1 ≠ a - i + b),
  return (a, b, i)
```
it returns a list of counterexample triples

#### [Chris Hughes (May 15 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579115):
```quote
hmm, but the goal is not an implication
```
I think it's because some of the hypotheses are an implication

#### [Gabriel Ebner (May 15 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579186):
Indeed, look at the (condition of the) induction hypothesis.

#### [Patrick Massot (May 15 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579580):
Sorry I messed up the last statement. What I really need is `2 * a + (b + 1 - a) - i - 1 = a+b-i` assuming `a ≤ b` and `i ∈ range' a (b + 1 - a)`

#### [Patrick Massot (May 15 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579628):
I do have all the right bounds, that's what my `foldr_congr` and `filter_ext` are made for

#### [Patrick Massot (May 15 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579681):
But I should probably think about first proving stuff with cumbersome statements and then try to deduce the natural statements from their twisted versions

#### [Kevin Buzzard (May 15 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579683):
Patrick I proved what you wanted, right?

#### [Patrick Massot (May 15 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579684):
This is all about summing for n from a to b, instead of n from a to a+k

#### [Patrick Massot (May 15 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579691):
You proved one of the things I wanted, thank you very much to you and Mario, but this is another one

#### [Kevin Buzzard (May 15 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579692):
The "true version" above

#### [Kevin Buzzard (May 15 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579695):
I thought I'd done everything for oyu

#### [Kevin Buzzard (May 15 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579696):
what is missing?

#### [Patrick Massot (May 15 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579697):
Oh sorry

#### [Kevin Buzzard (May 15 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579699):
:-)

#### [Patrick Massot (May 15 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579701):
I missed that one

#### [Kevin Buzzard (May 15 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579739):
I can believe that these things are not to everyone's tastes. I only did it because I quite like them.

#### [Patrick Massot (May 15 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579742):
I'm glad you're such a pervert

#### [Patrick Massot (May 15 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579744):
Thank you very much

#### [Kevin Buzzard (May 15 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579746):
What I especially like is that Mario's proof is only about 30% shorter :-)

#### [Kevin Buzzard (May 15 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579755):
[and that I was aware that something like this would probably work after I finished mine...]

#### [Kevin Buzzard (May 15 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579799):
```quote
Indeed, look at the (condition of the) induction hypothesis.
```
Right -- that's what I'm unclear about. Explicitly -- `simp * {contextual := tt}` does something different to `simp` in a situation where there is a _hypothesis_ of the form `X -> Y`, in which case it does...what?

#### [Kevin Buzzard (May 15 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579815):
Oh -- maybe I do understand.

#### [Chris Hughes (May 15 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579858):
It's hard to tell because trace.simplify doesn't show you where the rewrites are happening.

#### [Kenny Lau (May 15 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579860):
@**Chris Hughes** can you derive Kepler's laws?

#### [Kevin Buzzard (May 15 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579865):
Where are the mods? Honestly, this place is going down the pan

#### [Mario Carneiro (May 15 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579919):
Hi there, it's your friendly neighborhood mod

#### [Patrick Massot (May 15 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579927):
Are we still rewriting under a union?

#### [Mario Carneiro (May 15 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579932):
It's all connected, I'm sure

#### [Patrick Massot (May 15 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579933):
What about this one: `lemma reverse_range' (a b : ℕ) : reverse (range' a b) = map (λ i, 2*a+b-i-1) (range' a b) `?

#### [Mario Carneiro (May 15 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579935):
even Kepler's laws get involved in some rewrites

#### [Patrick Massot (May 15 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579936):
I need a topic "I hate natural numbers"

#### [Mario Carneiro (May 15 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579979):
That statement reminds me a lot of Kevin's theorem on reversing sums

#### [Patrick Massot (May 15 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579982):
Of course this is what I'm doing

#### [Patrick Massot (May 15 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579985):
I'm working on my big_op project

#### [Patrick Massot (May 15 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579992):
And this statement is partly what motivated my `nth_le_map` question

#### [Patrick Massot (May 15 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579997):
I wanted to use `ext_le` on that one

#### [Mario Carneiro (May 15 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580039):
suggestion: don't use `2*a+b-i-1`, use `a-(b+1-a)-i`

#### [Mario Carneiro (May 15 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580049):
otherwise you will spend the whole proof showing that the first thing rewrites to the second

#### [Patrick Massot (May 15 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580050):
That's part of the nightmare: each time I change my mind on something like this, I must redo all the natural numbers computations lemmas

#### [Patrick Massot (May 15 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580096):
With `2*a+b-i-1` I can use what Kevin proved last night down the road. Otherwise I return to having nothing

#### [Mario Carneiro (May 15 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580103):
We call that cruft

#### [Mario Carneiro (May 15 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580112):
Here's a suggestion: write the theorem so as to minimize the number of rewrites. That is, as soon as you get something technically the same as what you want (in this case, `range' a b = map ... (range' a b)`), go with it, even if it's written in a kind of weird way

#### [Mario Carneiro (May 15 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580116):
if you do that for two or three theorems the idioms will stand out

#### [Mario Carneiro (May 15 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580156):
like in this case keeping `b+1-a` together as a unit

#### [Kevin Buzzard (May 15 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580158):
```lean
import data.list.basic 
open list 
lemma foldr_ext {α : Type*} {β : Type*} {l : list α} (f f' : α → β → β) (s : β)
  (H : ∀ a ∈ l, ∀ b : β, f a b = f' a b) : foldr f s l = foldr f' s l :=
begin induction l with A B C, {simp}, -- base case}
  simp at H {contextual := tt},
  sorry,
end
```

#### [Kevin Buzzard (May 15 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580159):
I have isolated `contextual := tt` doing something

#### [Gabriel Ebner (May 15 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580165):
```quote
Right -- that's what I'm unclear about. Explicitly -- `simp * {contextual := tt}` does something different to `simp` in a situation where there is a _hypothesis_ of the form `X -> Y`, in which case it does...what?
```
Oh no, there is no difference in how simp treats implications in assumptions.  If you have a simp lemma/assumption `forall x, p x -> f x=g x`, then `simp` will try to prove `p a` before rewriting `f a` to `g a`.  And it proves this condition using `simp` itself!  Small demo:
```lean
example {n} {q : Prop} (h1 : n=1) (h2 : n*n=n → q) : q := by simp *
```
Here `simp` first proves the condition `n*n = n` (using `simp`) before rewriting `q` to `true`.

#### [Kevin Buzzard (May 15 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580167):
darn no I haven't

#### [Kevin Buzzard (May 15 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580178):
but Gabriel has. Thanks!

#### [Kevin Buzzard (May 15 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580221):
Wait -- there is no `contextual` here?

#### [Gabriel Ebner (May 15 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580229):
No, `simp` can use conditional simp lemmas without `contextual:=tt`.  It uses `simp` to prove the condition.

#### [Patrick Massot (May 15 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580233):
Mario, the trouble is I want to prove 
```lean
lemma big.range_anti_mph {φ : R → R} (P : ℕ → Prop) [decidable_pred P] (F : ℕ → R) (a b : ℕ)
  (Hop : ∀ a b : R, φ (a ◆ b) = φ b ◆ φ a) (Hnil : φ nil = nil) :
  φ (big[(◆)/nil]_(i=a..b | (P i)) F i) = big[(◆)/nil]_(i=a..b | (P (a+b-i))) φ (F (a+b-i))
```
I don't want the `a+b-i` in the conclusion to be some weird formula which is the same after a dozen rewrites

#### [Kevin Buzzard (May 15 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580245):
```lean
import data.list.basic 
open list 
lemma foldr_ext {α : Type*} {β : Type*} {l : list α} (f f' : α → β → β) (s : β)
  (H : ∀ a ∈ l, ∀ b : β, f a b = f' a b) : foldr f s l = foldr f' s l :=
begin induction l with A B C, {simp}, -- base case}
  simp at H,
  simp *,
  -- dammit simp, prove it without using contextual
  simp * {contextual := tt}, -- what just happened?
end
```

#### [Kevin Buzzard (May 15 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580277):
That's what I don't get

#### [Mario Carneiro (May 15 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580283):
I don't either. But I don't see that `2*a+whatever` anywhere in the statement either

#### [Kevin Buzzard (May 15 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580284):
Can I break that last line down into simpler steps?

#### [Patrick Massot (May 15 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580286):
Knowing of course that I proved
```lean
lemma big.anti_mph {φ : R → R} 
  (Hop : ∀ a b : R, φ (a ◆ b) = φ b ◆ φ a) (Hnil : φ nil = nil) :
  φ (big[(◆)/nil]_(i ∈ r | (P i)) F i) = big[(◆)/nil]_(i ∈ r.reverse | (P i)) φ (F i)
```
a long time ago

#### [Patrick Massot (May 15 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580300):
I'm only fighting the `range'` stuff

#### [Patrick Massot (May 15 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580345):
And I have 
```lean
lemma big.map {J : Type*} (f : I → J) (P : J → Prop) [decidable_pred P] (F : J → R) : 
  (big[(◆)/nil]_(j ∈ map f r | (P j)) (F j)) = (big[(◆)/nil]_(i ∈ r | (P (f i))) (F (f i))) 
```

#### [Patrick Massot (May 15 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580348):
So I wanted to write `reverse (range' ...)` as a `map ... (range' ...)`

#### [Mario Carneiro (May 15 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580357):
What are you going to do with the `map` once you have it?

#### [Gabriel Ebner (May 15 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580362):
@**Kevin Buzzard**  Look at the left-hand side of the implication in the induction hypothesis in foldr_ext.  Contextual simplification makes a difference here: simp then has the additional assumption `a ∈ l`, which it can use to apply `H`.

#### [Mario Carneiro (May 15 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580404):
Okay I think it is time to split this convo in two

#### [Patrick Massot (May 15 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580405):
Yes sorry

#### [Kevin Buzzard (May 15 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580428):
```quote
Okay I think it is time to split this convo in two
```
...given that neither thread is about the topic name ;-)

#### [Gabriel Ebner (May 15 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580490):
```lean
case list.cons
α : Type u_1,
β : Type u_2,
f f' : α → β → β,
s : β,
h : α,
t : list α,
IH : (∀ (a : α), a ∈ t → ∀ (b : β), f a b = f' a b) → foldr f s t = foldr f' s t,
H : ∀ (a : α), a ∈ h :: t → ∀ (b : β), f a b = f' a b
⊢ foldr f s (h :: t) = foldr f' s (h :: t)
```
This is the case for cons. ^^   In order to apply `IH`, you need to prove its left-hand side using `H`.  And to prove `a ∈ h :: t`, you need the `a ∈ t` from `IH`.

#### [Kevin Buzzard (May 15 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580729):
I am beginning to understand now. I'm writing out the proof in full, and I have to apply `IH` and then apply `H`.

#### [Kevin Buzzard (May 15 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580768):
So everything is there but somehow it's all in a bit of a tangle

#### [Kevin Buzzard (May 15 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580909):
I think I have it now

#### [Kevin Buzzard (May 15 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580911):
```lean
lemma got_it (P Q R S : Prop) (IH : (P → R) → S) (H0 : P → Q) (H' : Q → R) : S := 
begin
--simp *, -- fails
simp * {contextual := tt},
end 
```

#### [Kevin Buzzard (May 15 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580956):
I want to use `IH` to prove `S` but the hypothesis of `IH` isn't immediately true; however simp can prove it using other hypotheses.

#### [Kevin Buzzard (May 15 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580975):
Thanks Gabriel. To show your time isn't being wasted here I'll add it to the simp docs (once I've done another 8 hours of marking..)

#### [Kevin Buzzard (May 15 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126581149):
All of these conversations (threads about what simp does and doesn't do, threads about how to make type class inference work etc) -- it's in some sense sad that they just appear here and then disappear. The type class inference thread especially contains some really useful tips (in the sense that I was genuinely stuck about three times and then got unstucked by the contents of that thread). I will try to write some notes on that thread too, but I have so much marking at the minute and I have decided that it is time to prove an affine scheme is a scheme so I spend all my spare time on that. I am using the zulip "star" functionality a lot at the minute -- star meaning "get back to this later and write it up properly".

#### [Kevin Buzzard (May 15 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126581151):
Thanks to all as ever.

#### [Patrick Massot (May 15 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126581273):
Next year Lean will mark all this for you

#### [Kevin Buzzard (May 15 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126581275):
That's the plan!

#### [Patrick Massot (May 17 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126718080):
Because this `{contextual := true}` discussion I'm back to beginner level. Except that, instead of trying `simp` whatever the goal and hope for the best, I try `simp * at * { contextual := true}`

#### [Patrick Massot (May 17 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126718124):
And often it works!

