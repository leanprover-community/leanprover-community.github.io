---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35408existsiissodumb.html
---

## Stream: [general](index.html)
### Topic: [`existsi` is so dumb](35408existsiissodumb.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 19 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962582):
I often really feel like the `existsi` tactic is slacking off. It is always moaning that it doesn't know the type of what I suggest, even though it knows exactly the type it is expecting to get. And now this!
```lean
import tactic.interactive


theorem existsi_is_so_dumb (α : Type) : ∃ S : set α, S = S :=
begin
  have this : has_emptyc (set α) := by apply_instance,
  existsi ∅,
  -- new goal `⊢ has_emptyc (set α)` appears
  -- I mean -- what did you even try??
  { refl},
  { by apply_instance},
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962659):
It's not my favorite tactic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962674):
it's more or less completely superceded by `refine`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962760):
I can see why:
```
meta def existsi : parse pexpr_list_or_texpr → tactic unit
| []      := return ()
| (p::ps) := i_to_expr p >>= tactic.existsi >> existsi ps
```
The type of `p` is elaborated with no other information from the target type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962824):
The underlying `existsi` tactic is a bit more sophisticated, and it could have elaborated in the appropriate context

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 19 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962852):
Is this in core?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962854):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962858):
still it's all just a long winded way of doing the same thing as `refine <e1, e2, _>`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 19 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962914):
Hmm, we could define a tactic `use e1 e2 ...` that is a wrapper around `refine`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 19 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962919):
It is both shorter and more readable than `existsi`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962928):
the point is that the extra flexibility in where to put the underscores is actually useful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 19 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962953):
Of course, so `use` is for when you don't need that flexibility and you want some sort of beginner-friendly readable proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 19 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147963409):
`existsi` is a rubbish name anyway. No mathematician knows what it means, it's not even a word. How about `use x := refine x _ _ _ _ ... _`. Can we do that? Beginner mathematicans would like it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 19 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147963515):
or however it would work, is it just `use x := refine \< x,_\>`?, I don't know exactly how to make it work, all I know is that it would be better than existsi

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 19 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147963708):
I don't know how to define `use x := refine \<x, _\>` in Lean. This involves making a tactic that takes an input, and I only ever write tactics by just writing them in tactic mode and then sticking a load of backticks and square brackets everywhere.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 20 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148044440):
So, what's the conclusion of that thread? Who is writing that `use` tactic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 20 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148044510):
How about `meta def use := refine`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Nov 20 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148045273):
I think this is approximately right.
```lean
meta def tactic.interactive.use (l : interactive.parse interactive.types.pexpr_list_or_texpr) : tactic unit :=
tactic.refine $ l.foldr (λ t p, ``(⟨%%t, %%p⟩)) pexpr.mk_placeholder

example : ∃ a b c : ℕ, a + b + c = 6 :=
begin 
  use [1, 2, 3], refl
end 

theorem existsi_is_so_dumb (α : Type) : ∃ S : set α, S = S :=
begin
  use ∅, refl
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 20 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148048724):
how about we PR core

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 21 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148110505):
How about PRing 
```lean
meta def tactic.interactive.use (l : interactive.parse interactive.types.pexpr_list_or_texpr) : tactic unit :=
do tactic.refine $ l.foldr (λ t p, ``(⟨%%t, %%p⟩)) pexpr.mk_placeholder, tactic.try tactic.interactive.refl
```
to mathlib? I only added trying refl, just in case (I hope it's not too time consuming)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 21 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148110636):
Does it also solve the issue where `existsi` does not know the expected type. So if I type `existsi ⟨x, y⟩`, it fails because it doesn't know what type `⟨x, y⟩` is even though this should be inferrable from the goal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 21 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148110648):
It's meant to solve this issue, yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 21 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148110650):
And it does on Kevin's examples

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 21 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148110655):
Could you provide more examples?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 21 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148110725):
I never use it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 21 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148111034):
Here are my test cases so far:
```lean
meta def tactic.interactive.use (l : interactive.parse interactive.types.pexpr_list_or_texpr) : tactic unit :=
do tactic.refine $ l.foldr (λ t p, ``(⟨%%t, %%p⟩)) pexpr.mk_placeholder, tactic.try tactic.interactive.refl

example : ∃ a b c : ℕ, a + b + c = 6 :=
by use [1, 2, 3]

example (α : Type) : ∃ S : set α, S = S :=
by use ∅ 

example : ∃ x : ℤ, x = x :=
by use 42

example : ∃ p : ℤ × ℤ, p.1 = 1 :=
by use ⟨1, 42⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Nov 21 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148111139):
The first example is more interesting with `int` instead of `nat` since `existsi` fails in that case.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 21 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148111142):
Only the first one works with `existsi`, even if you end the line with `; refl`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 21 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148111157):
Right, replace nat by int in the first example

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 21 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148111210):
Rob, would you mind PRing this? I can do it of course, but I don't want to claim any credit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Nov 21 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148111239):
Yeah, I'll do it. It's a little hackish, but I couldn't think of a nicer one line solution off the top of my head. So, good enough!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 21 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148111607):
Of course the real test would be to replace every use of `existsi` in mathlib, but that's more work, and probably not worth the trouble

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Nov 21 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148112078):
PRed. That's definitely not worth the trouble.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 21 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148112151):
Thanks Rob! This looks much much better pedagogically

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 21 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148112259):
And thanks Patrick too for helping to make it happen

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Nov 21 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148114826):
[if-you-give-a-mouse-a-cookie-HarperCollins.jpeg](/user_uploads/3121/lVNrNYy6wJQaiT7sCVQo4wsi/if-you-give-a-mouse-a-cookie-HarperCollins.jpeg)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Nov 21 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148114844):
(https://github.com/leanprover/mathlib/pull/486)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jeremy Avigad (Nov 21 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148117611):
I don't see a big win over `exists` and `refine`:
```lean
example : ∃ a b c : ℕ, a + b + c = 6 :=
by exact ⟨1, 2, 3, rfl⟩ 

example (α : Type) : ∃ S : set α, S = S :=
by exact ⟨∅, rfl⟩ 

example : ∃ x : ℤ, x = x :=
by exact ⟨1, rfl⟩ 

example : ∃ p : ℤ × ℤ, p.1 = 1 :=
by exact ⟨⟨1, 42⟩, rfl⟩
```
`exists` and `refine` with the corner brackets is more flexible, since the corner brackets can handle structures with multiple arguments and nested structures. If you use `exact` with placeholders, squiggly lines well tell you what you need to fill in. You can use whatever tactics you want to discharge the final goal. Are there any advantages to `use`? Doesn't it just clutter the language?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Nov 21 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148119422):
When you're proving `∃ x, P x` in tactic mode, and the proof of `P a` is long, you don't want to write `exact <a, begin end>`. You can write `refine <a, _>` and keep going. This tactic is exactly an abbreviation for that, that looks more natural. `use` is really a replacement for `existsi`,  except we can't change that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 21 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148119507):
Jeremy, the comparison is not with `exact` and `refine`. `use` is meant as a better behaved drop-in replacement of `existsi`

