---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/47376freegroup.html
---

## Stream: [general](index.html)
### Topic: [free group](47376freegroup.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124469539):
I have constructed the free group of a set here: https://github.com/kckennylau/Lean/blob/master/free_group.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124469545):
@**Mario Carneiro** @**Kevin Buzzard** what do you think of it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124480775):
@**Mario Carneiro** I'm onto something. My construction of the *real* free group is almost done.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124481322):
https://github.com/kckennylau/Lean/blob/master/free_group.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124481323):
https://github.com/leanprover/mathlib/pull/89

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124493682):
Why not prove the adjoint functor theorem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124493728):
that construction was my first construction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124493731):
see https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making.20isomorphism.20class.20a.20group for why it fails

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124493781):
unfortunately I rewrote my second construction over my first

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124493783):
so see commit history for the construction from adjoint functor theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Peter Jipsen (Apr 01 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124499636):
Nice construction! Would it be possible to construct the free group directly on an inductive type of the group signature and then quotient by the group axioms (i.e. without using the inverse monoid)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124499786):
I find the divide-and-conquer approach more psychologically comfortable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Peter Jipsen (Apr 01 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124500101):
Sure, I agree with that. Was just wondering how a direct (minimal) construction would compare -- I may try that as an exercise

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124500103):
do let me know afterwards! :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124500203):
I agree that separating the construction into steps makes it clearer what is happening. Is it possible to use just the second stage to construct the free monoid as well?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124500247):
hmm, I don't know

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124500398):
free commutative ring = polynomial ring $$\mathbb{Z}[S]$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124500404):
might be a nice way to think about it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124500405):
feel free to construct it ^^

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124500408):
did you prove the adjoint functor theorem yet? ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124500452):
heh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187323):
```lean
universe u

variables (α : Type u)

inductive rel : list (α × bool) → list (α × bool) → Prop
| refl {L} : rel L L
| symm {L₁ L₂} : rel L₁ L₂ → rel L₂ L₁
| trans {L₁ L₂ L₃} : rel L₁ L₂ → rel L₂ L₃ → rel L₁ L₃
| append {L₁ L₂ L₃ L₄} : rel L₁ L₃ → rel L₂ L₄ → rel (L₁ ++ L₂) (L₃ ++ L₄)
| bnot {x b} : rel [(x, b), (x, bnot b)] []

example (x y : α) (H : rel α [(x, tt)] [(y, tt)]) : x = y :=
sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187324):
How might I prove this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187326):
looks simple but somehow I can't do it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 17 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187372):
You need to generalize `[(x, tt)]` and `[(y, tt)]` then you can use induction on it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 17 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187383):
Like
```lean
example (x y : α) : rel α [(x, tt)] [(y, tt)] -> x = y :=
begin
  generalize h1 : [(x, tt)] = x1,
  generalize h2 : [(y, tt)] = x2,
  intro h,
  induction h generalizing x y,
 ...
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187391):
can I not do inversion (pattern matching)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187452):
your code doesn't work, and after I removed `intro h`, I get an impossible goal:
```lean
case rel.refl
α : Type u,
x1 x2 H : list (α × bool),
h1 : H = x1,
h2 : H = x2,
x y : α
⊢ x = y
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 17 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187453):
`match` doesn't work, but `cases` could work. But I guess you need induction to finally proof it, as the `x` and `y` could come from the recursive call.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187468):
never mind, ignore what I said about your code not working

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187534):
```lean
case rel.symm
α : Type u,
x y : α,
X Y L1 L2 : list (α × bool),
H1 : rel α L1 L2,
ih1 : [(x, tt)] = L1 → [(y, tt)] = L2 → x = y,
hx : [(x, tt)] = L2,
hy : [(y, tt)] = L1
⊢ x = y
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187535):
I ran to an impossible goal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 17 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187539):
did you use `induction h generalizing x y`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 17 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187581):
```lean
case rel.symm
α : Type u_1,
x1 x2 h_L₁ h_L₂ : list (α × bool),
h_a : rel α h_L₁ h_L₂,
h_ih : ∀ (x y : α), [(x, tt)] = h_L₁ → [(y, tt)] = h_L₂ → x = y,
x y : α,
h1 : [(x, tt)] = h_L₂,
h2 : [(y, tt)] = h_L₁
⊢ x = y
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187582):
you're right, there's something wrong with me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 17 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187682):
If you are working on free groups: you don't need the `refl`, `symm` and `trans` rules. For example I did a experiment a while back:
https://gist.github.com/johoelzl/7e73916f39e3acef8796bfb6c089a9c9
There I used `quot`, which doesn't require a `setoid`. Then lifting functions requires less proofs. Other things get a little bit more difficult.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187727):
I, uh... prefer using setoid :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187734):
```lean
case free_group.rel.trans
α : Type u,
X Y L1 L2 L3 : list (α × bool),
H1 : rel α L1 L2,
H2 : rel α L2 L3,
ih1 : ∀ (x y : α), [(x, tt)] = L1 → [(y, tt)] = L2 → x = y,
ih2 : ∀ (x y : α), [(x, tt)] = L2 → [(y, tt)] = L3 → x = y,
x y : α,
hx : [(x, tt)] = L1,
hy : [(y, tt)] = L3
⊢ x = y

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187735):
an impossible goal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187776):
that's not impossible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187783):
it's just transitivity on the two ih

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187787):
but I can't use the assumption `[(y, tt)] = L2`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187788):
this can't be proved

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187802):
Ah, I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187809):
is there really no way to use the equation compiler?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187810):
Didn't I show you how to solve this with a different representation?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187815):
because that compiler is smarter than induction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 17 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187817):
You first need to prove a stronger inversion rule: `rel [x] as -> \exists y, as = [y]` (ups, this doesn't hold...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187820):
You want to focus on one-directional reduction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188017):
```
inductive red : list (α × bool) → list (α × bool) → Prop
| refl {L} : red L L
| trans {L₁ L₂ L₃} : red L₁ L₂ → red L₂ L₃ → red L₁ L₃
| cons {L₁ L₂} (a) : red L₁ L₂ → red (a :: L₁) (a :: L₂)
| bnot {x b L} : red ((x, b) :: (x, bnot b) :: L) L

theorem church_rosser : ∀ L₁ L₂, rel α L₁ L₂ → ∃ L₃, red α L₁ L₃ ∧ red α L₂ L₃ := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188022):
You could prove (easily by induction, I imagine) that for every function from alpha to Z/2Z (the additive group) the induced map from list (alpha x bool) to Z/2Z sending (x,b) to x and sending ++ to + has the property that two things related to each other go to the same place, and deduce it from that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188035):
seeing the word "church rosser" excites me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188036):
but x is in alpha, not Z/2Z

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188038):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188041):
so if x wasn't y you just write down a function sending x to 1 and y to 0

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188042):
so how is that a map from list (alpha x bool) to Z/2Z ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188083):
that's a map from alpha to Z/2Z

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188086):
@**Kevin Buzzard** "if x wasn't y"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188099):
@**Mario Carneiro** how would I prove symm?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188100):
To finish the proof given `church_rosser`, note that `red A L1 L2` implies `length L1 >= length L2`, and they are the same length mod 2 so if one is a singleton so is the other

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188101):
I'm telling you how a mathematician would answer the original question

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188102):
symm is trivial, since the target property is symmetric

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188142):
the hard one is trans

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188143):
I don't get what you mean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188144):
`bnot` is clearly not symmetric

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188146):
I'm a bit confused about why a proof of what Mario calls Church Rosser can't just be "let L3 be L2"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188149):
note that `rel` becomes `red` in the result

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188153):
oh wait what

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188154):
`red` has no symmetry rule

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188155):
I thought you were telling me to rewrite rel to red lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188157):
oh, I didn't spot rel wasn't red

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188158):
high five

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188265):
You will need this lemma for the trans case:
```
theorem church_rosser2 : ∀ L₁ L₂ L₃,
  red α L₁ L₂ → red α L₁ L₃ → ∃ L₄, red α L₂ L₄ ∧ red α L₃ L₄ := sorry
```
You can prove this by induction on one of the `red` assumptions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188437):
which one?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188441):
it doesn't matter by symmetry

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188443):
but which one would you expand?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188445):
?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188452):
never mind

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188612):
```lean
case free_group.red.trans
α : Type u,
L₂ L₁ L₃ L1 L2 L3 : list (α × bool),
H1 : red α L1 L2,
H2 : red α L2 L3,
ih1 : red α L1 L₂ → (∃ (L₄ : list (α × bool)), red α L₂ L₄ ∧ red α L2 L₄),
ih2 : red α L2 L₂ → (∃ (L₄ : list (α × bool)), red α L₂ L₄ ∧ red α L3 L₄),
H1 : red α L1 L₂
⊢ ∃ (L₄ : list (α × bool)), red α L₂ L₄ ∧ red α L3 L₄
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188613):
@**Mario Carneiro**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188681):
that's where `church_rosser2` comes in (also don't forget to generalize L₂)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188683):
that's church_rosser2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188805):
Actually on second thought I think you want to separate the transitivity part from the one-step reduction. That leads to the following proof skeleton:
```
inductive rel : list (α × bool) → list (α × bool) → Prop
| refl {L} : rel L L
| symm {L₁ L₂} : rel L₁ L₂ → rel L₂ L₁
| trans {L₁ L₂ L₃} : rel L₁ L₂ → rel L₂ L₃ → rel L₁ L₃
| append {L₁ L₂ L₃ L₄} : rel L₁ L₃ → rel L₂ L₄ → rel (L₁ ++ L₂) (L₃ ++ L₄)
| bnot {x b} : rel [(x, b), (x, bnot b)] []

inductive trans_gen {α} (R : α → α → Prop) (x : α) : α → Prop
| refl : trans_gen x
| trans {y z} : R y z → trans_gen y → trans_gen z

inductive red : list (α × bool) → list (α × bool) → Prop
| cons {L₁ L₂} (a) : red L₁ L₂ → red (a :: L₁) (a :: L₂)
| bnot {x b L} : red ((x, b) :: (x, bnot b) :: L) L

theorem church_rosser_1 : ∀ L₁ L₂ L₃,
  red α L₁ L₂ → red α L₁ L₃ → ∃ L₄, red α L₂ L₄ ∧ red α L₃ L₄ := sorry

theorem church_rosser_t1 : ∀ L₁ L₂ L₃,
  red α L₁ L₂ → trans_gen (red α) L₁ L₃ → ∃ L₄, trans_gen (red α) L₂ L₄ ∧ red α L₃ L₄ := sorry

theorem church_rosser_t : ∀ L₁ L₂ L₃,
  trans_gen (red α) L₁ L₂ → trans_gen (red α) L₁ L₃ → ∃ L₄, trans_gen (red α) L₂ L₄ ∧ trans_gen (red α) L₃ L₄ := sorry

theorem church_rosser : ∀ L₁ L₂, rel α L₁ L₂ →
  ∃ L₃, trans_gen (red α) L₁ L₃ ∧ trans_gen (red α) L₂ L₃ := sorry
```
This is important for the core of the proof, knowing that the one-step diamond property `church_rosser_1` holds is what allows you to do induction to get to `church_rosser_t`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125189880):
@**Mario Carneiro** I'm stuck on church_rosser_1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125189895):
You need to do induction on both arguments for that one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125189899):
even so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125189902):
```lean
case free_group.red.cons
α : Type u,
L₁ L₃ L1 L2 : list (α × bool),
x1 : α × bool,
H3 : red α L1 L2,
ih1 :
  ∀ (L₂ : list (α × bool)),
    red α L1 L₂ → (∃ (L₄ : list (α × bool)), red α L₂ L₄ ∧ red α L2 L₄),
L₂ L3 L4 : list (α × bool),
x2 : α × bool,
H4 : red α L3 L4,
ih2 : ∃ (L₄ : list (α × bool)), red α L4 L₄ ∧ red α (x1 :: L2) L₄
⊢ ∃ (L₄ : list (α × bool)), red α (x2 :: L4) L₄ ∧ red α (x1 :: L2) L₄
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125189947):
apply ih1?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125189953):
and then destruct the exists's

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125189962):
but I need the same list to clear the goal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125189966):
but x1 and x2 are different

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125189992):
I'm just suggesting to apply `ih1` to `H3`, and then open up the assumptions `ih1` and `ih2`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190021):
once you have done that you do inversion on `red α (x1 :: L2) L₄` and there are a few different cases

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190027):
this is the tricky part, since you have to show that the rewriting is confluent meaning different contractions result in the same thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190128):
```lean
α : Type u,
L₁ L₃ L1 L2 : list (α × bool),
x1 : α × bool,
H3 : red α L1 L2,
L₂ L3 L4 : list (α × bool),
x2 : α × bool,
H4 : red α L3 L4,
ih2 : ∃ (L₄ : list (α × bool)), red α L4 L₄ ∧ red α (x1 :: L2) L₄,
ih1 : ∃ (L₄ : list (α × bool)), red α L2 L₄ ∧ red α L2 L₄
⊢ ∃ (L₄ : list (α × bool)), red α (x2 :: L4) L₄ ∧ red α (x1 :: L2) L₄
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190129):
I don't think this is possible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190132):
It is, do cases on `ih1` and `ih2` now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190176):
but I know nothing about `x2`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190257):
hm, you seem to have forgotten something

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190266):
I think you need to generalize one of the parameters before the secondary induction, or you will lose the relation with x2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190843):
@**Mario Carneiro** forgive me, but which parameter?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190849):
the one that has `x2` in it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190857):
this is the state before the second induction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190858):
```lean
α : Type u,
L₁ L₃ L1 L2 : list (α × bool),
x1 : α × bool,
H3 : red α L1 L2,
ih1 :
  ∀ (L₂ : list (α × bool)),
    red α L1 L₂ → (∃ (L₄ : list (α × bool)), red α L₂ L₄ ∧ red α L2 L₄),
L₂ : list (α × bool),
H1 : red α (x1 :: L1) L₂
⊢ ∃ (L₄ : list (α × bool)), red α L₂ L₄ ∧ red α (x1 :: L2) L₄
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190859):
you want to get an equality constraint in the context so you can do injection on it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190863):
`generalize h : x1 :: L1 = xL`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190906):
and then `generalizing` who?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190959):
I don't think you need any generalizing here, but you know what to change if the IH isn't strong enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190968):
actually you might not even need induction here; see if `cases H1` works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125191726):
My way would be so much easier ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195531):
@**Kevin Buzzard** except it doesn't even work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195584):
Oh rotten luck :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195585):
It works in maths :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195606):
first three properties are that = is an equiv relation, fourth is that the map is a group hom, fifth that Z/2 has exponent 2, and bob's your uncle

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195660):
oh wait, I misunderstood

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195661):
what's your method?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195696):
you're using finsupp aren't you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195733):
that's noncomputable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195843):
if you form (Z/2Z)^S as a group, your set-theoretic function will be non-computable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 17 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195924):
since a couple of weeks finsupp is computable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195973):
right, but this instance is still not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195992):
in particular, `single` still needs decidable equality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125196116):
I said it works in maths ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 17 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125196117):
well, then you need to use `classical.prop_decidable`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125196156):
I thought you were talking about the adjoint functor theorem when I said it doesn't even work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125196159):
@**Johannes Hölzl** oh I forgot, we aren't on the same side

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 17 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125196231):
ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197470):
I think the main reason why this is hard is that reduction isn't straightforward

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197471):
if your list is [a,b,c,d]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197476):
you can eliminate [b,c] or you can eliminate [c,d]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197517):
then somehow you need to prove that [a,d] = [a,b]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197521):
on the outside we know that to be true intuitively, but that doesn't mean this translates well on the inside

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197599):
https://gist.github.com/johoelzl/7e73916f39e3acef8796bfb6c089a9c9

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197603):
@**Johannes Hölzl** oh and why don't you just put this onto mathlib lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 17 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197789):
Yours is slightly more general. I thought you want to fix your pull request and still try to get it into mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197801):
actually I've written another free_group today, before this thread even started

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 17 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197803):
But as it looks it will take a little bit longer, so I can add my stuff first.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197804):
(I live in GMT+8, so "today" started like 10 hours ago)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197809):
and all this fuss is about I can't prove that the set-theoretic function is injective

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197865):
https://gist.github.com/kckennylau/cda1c6c6bc781fe669692b8d725f43d0

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197868):
this is what the working part of my file looks like

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197873):
I think your file is slightly more general lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197947):
anyway, [a,d] and [a,b] aren't definitionally equal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197950):
it just so happens that d=b

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197952):
but how am I supposed to know that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197963):
I doubt church-rosser can be proved by me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 17 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197970):
So you don't want to follow the approach from stack overvlow anymore?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125198007):
nope

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125198018):
I don't see any point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125198021):
I was overwhelmed by fear

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125198027):
that I couldn't ever possibly define free group in one step

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 17 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125198125):
don't worry, while theorem proving is a steep learning curve, it is a continuous curve after all

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125198145):
you won't believe me if I told you that I prove limit commutes with multiplication in three steps

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125198146):
divide and conquer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199051):
if `[(x,tt)]` is related to `[(y,tt)]`, part of the reason why it is so hard to prove `x=y` is that the reason they are related can be complicated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199070):
since one can have `[(x,tt)] ~ [(x,tt), (x,ff), (x,tt)] ~ [(x,tt)]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199077):
where the two `~`s deal with different pairs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199099):
so this is hardly well-founded

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199108):
@**Johannes Hölzl** what do you think?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 17 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199232):
it is not well-founded. but the non-symmetric reduction is well founded. as Mario mentioned the hard part is to proof the existence of diamonds

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199240):
would you have insights for the diamond?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199339):
@**Johannes Hölzl** maybe give me more time to prove the diamonds?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199382):
I'll see if I can incorporate other theorems you proved

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199384):
i.e. free_group of empty is unit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199385):
free_group of unit is int

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199467):
```lean
| bnot {x b L₁ L₂} : red (L₁ ++ (x, b) :: (x, bnot b) :: L₂) (L₁ ++ L₂)

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199478):
(I know this is essentially what you did, but I hadn't looked at your file when I came up with this, somehow)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199483):
it's hard proving diamond even for one step bnot

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199492):
i.e. if L1 bnot L2, L1 bnot L3, then there is L4 such that L2 bnot L4 and L3 bnot L4

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199555):
@**Johannes Hölzl** what do you think?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 17 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199581):
I didn't look into this, yet. I will see if I find some time to understand it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199632):
I mean, don't put your freegroup into mathlib yet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 17 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199694):
okay. but mathlib seams to be broken anyway currently (EDIT: sorry, mathlib is not broken)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199706):
@**Johannes Hölzl** which one would you use? `n+n`, `n*2`, `2*n`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199708):
for usability

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199711):
I think` 2*n` is maximum usability

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 17 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199714):
yes, looks good

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199742):
I just answered my own question

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125204798):
I changed anew the definition:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125204801):
```lean
inductive red : list (α × bool) → list (α × bool) → Prop
| refl {L} : red L L
| trans_bnot {L₁ L₂ L₃ x b} : red (L₁ ++ L₂) L₃ → red (L₁ ++ (x, b) :: (x, bnot b) :: L₂) L₃

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125204804):
hopefully this will be more usable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125204805):
I still can't prove church-rosser though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125204811):
I suspect I shouldn't do church-rosser in one step

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205016):
[church-rosser-1.png](/user_uploads/3121/SwM98KnlFnJesSDVnNnSYJK1/church-rosser-1.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205188):
and induction on the rightmost solid arrow amounts to doing this:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205234):
[church-rosser-1.png](/user_uploads/3121/HY4gl0SQ4kObK_7zXbz_B1e3/church-rosser-1.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205244):
where `wordIH` is the word given by induction hypothesis

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205252):
my new definition makes sure that it is decomposed into steps

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205254):
whereas the old definition splits the arrow randomly in half

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205260):
my new definition guarantees that it is split at the tail

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205266):
oh no, my new definition splits it at the head

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205268):
brb

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205402):
I mean, even if I corrected the definition, I still don't know how to build `word4` from `wordIH`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205405):
@**Kevin Buzzard** any insight?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205454):
I told you how I'd do it ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205456):
I've not thought about the constructive approach

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205458):
I've not been following the conversation here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205466):
My daughter is sick so I've not had much time today, and what little time I did have I spent thinking about Spec(R) being compact

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205520):
you just need to look at my latest picture

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205521):
"step" means a one-step reduction, i.e. reducing `w1++[a,a^-1]++w2` to `w1++w2`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205528):
`wordIH` is given, and I would like to construct `word4`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205531):
I might have to destruct the bottom right solid arrow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205601):
@**Kevin Buzzard** I'm astonished by the fact that I'm drawing a diagram to represent induction and that I'm drawing a diagram (the same diagram) to deal with free groups

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205605):
I've never looked into free group this deeply

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205629):
I'll destruct the arrow I mentioned and see what comes up

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206778):
The construction of many step CR from one step CR is like building a checkerboard of diamonds

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206830):
oh and I've changed to the "correct" definition now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206833):
did you look at my picture?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206835):
You do induction on one of the `trans_rel` arguments to reduce to a line of diamonds, and then the other one to get one step out, one step back together

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206861):
You want to use the IH to move the base point of the bottom diamond to wordIH

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206878):
base point?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206917):
You have word1''' -> word3 and word1''' -> wordIH, so wordIH -> word4 <- word3 for some word4

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206925):
right, that's what I intend to do also

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206933):
I proved transitivity independently

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206942):
so I only need to focus on that diamond

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206947):
and destruct the bottom right solid arrow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206953):
right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206968):
I'm not sure I follod

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206978):
Do you still have the three theorems `church_rosser_(1,t1,t)` or something similar?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207035):
oh I am not using your definition now...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207049):
but do you have the thing with transitive closure of one step reduction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207067):
```lean
inductive red : list (α × bool) → list (α × bool) → Prop
| refl {L} : red L L
| trans_bnot {L₁ L₂ L₃ x b} : red L₁ (L₂ ++ (x, b) :: (x, bnot b) :: L₃) → red L₁ (L₂ ++ L₃)

lemma red.trans {L₁ L₂ L₃} (H12 : red α L₁ L₂) (H23 : red α L₂ L₃) : red α L₁ L₃ :=
begin
  induction H23 with L1 L1 L2 L3 x b H ih generalizing L₁,
  case red.refl
  { assumption },
  case red.trans_bnot
  { exact red.trans_bnot (ih H12) }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207071):
this is what i'm using

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207086):
and unfinished church rosser:
```lean
lemma church_rosser {L₁ L₂ L₃} (H12 : red α L₁ L₂) (H13: red α L₁ L₃) :
  ∃ L₄, red α L₂ L₄ ∧ red α L₃ L₄ :=
begin
  induction H12 with L1 L1 L2 L3 x1 b1 H1 ih1 generalizing L₃,
  case red.refl
  { exact ⟨L₃, H13, red.refl _⟩ },
  case red.trans_bnot
  { specialize ih1 H13,
    rcases ih1 with ⟨L₄, H24, H34⟩,
    revert H24,
    generalize HL23 : L2 ++ (x1, b1) :: (x1, bnot b1) :: L3 = L23,
    intro H24,
    induction H24 with L4 L4 L5 L6 x2 b2 H2 ih2,
    case red.refl
    { subst HL23,
      exact ⟨_, red.refl _, red.trans_bnot H34⟩ },
    case red.trans_bnot
    { subst HL23,
      admit } }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207167):
I think that trying to do it all at once will be harder, because then you have to commute a whole sequence of reductions past another

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207318):
With one step reduction, the core of the proof is this: Suppose L -> L1 and L -> L2. Then L = A1 ++ [(x,b), (x, !b)] ++ A2 = B1 ++ [(y,c),(y,!c)] ++ B2 and L1 = A1 ++ A2, L2 = B1 ++ B2. There are three cases depending on whether |A1| = |B1|, |A1| = |B1| +- 1, or | |A1| - |B1| | >= 2, but in each case the results are either equal or can be put together with a single step on each side.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207342):
that's the hardest part of the theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207348):
So I guess you want `red` to be reflexive but not transitive, and then take its transitive closure to put the diamonds together

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207393):
I don't think I need to change my definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207524):
One word of warning: the confluence property B <- A -> C implies \ex D s.t. B ->* D <-* C does *not* imply church rosser in general. It does if you have strong normalization, but that's a harder proof. That's why I'm wary of building transitivity into the -> relation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207545):
isn't that church rosser?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207550):
Note the location of the stars

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207554):
what are those?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207557):
one step out, many steps back in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207595):
that's notation for transitive closure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207598):
hmm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224401):
```quote
With one step reduction, the core of the proof is this: Suppose L -> L1 and L -> L2. Then L = A1 ++ [(x,b), (x, !b)] ++ A2 = B1 ++ [(y,c),(y,!c)] ++ B2 and L1 = A1 ++ A2, L2 = B1 ++ B2. There are three cases depending on whether |A1| = |B1|, |A1| = |B1| +- 1, or | |A1| - |B1| | >= 2, but in each case the results are either equal or can be put together with a single step on each side.
```
@**Mario Carneiro** what is the best way to prove that there are three cases?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224462):
`wlog` length A1 <= length B1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224549):
aha, i never tried wlog before

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224592):
me neither, but this looks like a good use case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224731):
```lean
lemma partition {L1 L2 L3 L4 : list (α × bool)} {x1 b1 x2 b2}
  (H : L1 ++ (x1, b1) :: (x1, bnot b1) :: L2 = L3 ++ (x2, b2) :: (x2, bnot b2) :: L4) :
  (L1 = L3 ∧ x1 = x2 ∧ b1 = b2 ∧ L2 = L4) ∨
  (L1 = L3 ++ [(x2, b2)] ∧ x1 = x2 ∧ b1 = bnot b2 ∧ (x1, bnot b1) :: L2 = L4) ∨
  (L1 ++ [(x1, b1)] = L3 ∧ x1 = x2 ∧ b1 = bnot b2 ∧ L2 = (x2, bnot b2) :: L4) ∨
  (∃ L5 L6, L1 = L3 ++ (x2, b2) :: (x2, bnot b2) :: L5 ∧ (x1, b1) :: (x1, bnot b1) :: L2 = L6) ∨
  (∃ L5 L6, L1 ++ (x1, b1) :: (x1, bnot b1) :: L5 = L3 ∧ L2 = (x2, b2) :: (x2, bnot b2) :: L6) :=
begin
  admit
end

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224732):
how is this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224734):
I don't think `length` is very usable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224774):
it's obvious to mathematicians, but Lean doesn't really know how to count well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224776):
it's just translating one inductive type into another

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224834):
You can simplify this by assuming `length L1 <= length L3`, and then two of the cases can be proven impossible (it's not hard to show that if L1 = L3 ++ [(x2, b2)] then length L3 < length L1, and that's all you need)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224847):
are you saying I don't need induction?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224850):
induction on what? To prove partition?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224851):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224856):
on the lists

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224895):
You can use `append_inj` to use length information to get the decomposition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224905):
But you can also prove it by induction on one of the lists (generalizing everything else)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224956):
I think I would need more lemmas than `append_inj` if I want to avoid induction completely

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224961):
`append_inj` doesn't seem to help in the case where `|A.length - B.length| >= 2`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225016):
hm, you could use `take_drop` but I agree it is probably messier than induction on the list

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225031):
I think a useful lemma if I want to avoid length and induction completely is `A++B=C++D -> (exists F, A=C++F) or (exists F, A++F=C)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225036):
I think you can get that by using `prefix` appropriately

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225079):
I have never heard of prefix before. I've just learnt something new lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225146):
@**Mario Carneiro** I'm not seeing anything useful from the prefix lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225157):
Here's what I'm thinking:
```
theorem prefix_of_prefix_length_le {l₁ l₂ l₃ : list α} : l₁ <+: l₃ → l₂ <+: l₃ → length l₁ ≤ length l₂ → l₁ <+: l₂ :=
sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225161):
let's just focus on my lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225163):
and from that you get the version with the or

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225164):
aha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225204):
totality of prefix descends from totality of natural numbers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225207):
exactly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225210):
that's a very convoluted way of doing stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225213):
I would rather use induction to prove my lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225271):
disregarding this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225274):
how would you prove your lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225622):
working on it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225623):
me too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225624):
I think I can do that, thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225729):
```
theorem prefix_of_prefix_length_le : ∀ {l₁ l₂ l₃ : list α},
 l₁ <+: l₃ → l₂ <+: l₃ → length l₁ ≤ length l₂ → l₁ <+: l₂
| []      l₂ l₃ h₁ h₂ _ := nil_prefix _
| (a::l₁) (b::l₂) _ ⟨r₁, rfl⟩ ⟨r₂, e⟩ ll := begin
  injection e with _ e', subst b,
  rcases prefix_of_prefix_length_le ⟨_, rfl⟩ ⟨_, e'⟩
    (le_of_succ_le_succ ll) with ⟨r₃, rfl⟩,
  exact ⟨r₃, rfl⟩
end

theorem prefix_or_prefix_of_prefix {l₁ l₂ l₃ : list α}
 (h₁ : l₁ <+: l₃) (h₂ : l₂ <+: l₃) : l₁ <+: l₂ ∨ l₂ <+: l₁ :=
(le_total (length l₁) (length l₂)).imp
  (prefix_of_prefix_length_le h₁ h₂)
  (prefix_of_prefix_length_le h₂ h₁)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225731):
oh nice thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225737):
who is `nil_prefix`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225740):
```
theorem nil_prefix (l : list α) : [] <+: l := ⟨l, rfl⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225742):
did you just make it up?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225772):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225787):
thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225936):
does `A++B=A++C -> B=C` have a name?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226008):
`append_right_cancel`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226009):
oh, didn't think of cancel

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226011):
oh, and do you know that the lists form a monoid?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226013):
by "you" I of course mean "Lean"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226137):
No, although all the lemmas are there, because I don't think we want `*` to mean append on lists

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226138):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226191):
That was one of the main motivations Leo had for introducing the whole "notation free" algebraic hierarchy like `is_associative`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226198):
I'm not aware of what you're talking about

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226205):
look at `is_associative` and friends

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226208):
where is it used?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226250):
that's probably what lean 4 algebraic hierarchy will look like

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226258):
I'm not sold on it yet, and I don't think the tool support is there yet, so I'm sticking to "old style" structures like `monoid`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226264):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226267):
but it gets used in some core lean stuff like `rb_map`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226269):
another thing I've never heard of :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226857):
what's the fastest way to destruct `L5 ++ L6 = [(x1, bnot b1)]`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226907):
cases L5, lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125228253):
I proved church rosser!!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125228296):
thanks for your help all along @**Mario Carneiro**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125228390):
That theorem can of course also be used to show the existence and uniqueness of reduced words

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125228394):
right, since I proved that red is decreasing in length

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125228481):
You need decidable equality for it to be constructive, but you can just remove matching pairs until you can't find any more, and that will be the unique representative of its equivalence class by church rosser

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125228558):
Here's a fun trick showing that the converse also holds: assuming [(x,tt), (y,ff)] has a reduced word representative, if it has length zero then x=y, and if it has length 2 then x != y

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125228564):
aha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125228567):
nice trick

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125231206):
```
inductive red : list (α × bool) → list (α × bool) → Prop
| refl {L} : red L L
| trans_bnot {L₁ L₂ L₃ x b} : red L₁ (L₂ ++ (x, b) :: (x, bnot b) :: L₃) → red L₁ (L₂ ++ L₃)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125231212):
how do I use the equation compiler to destruct this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232619):
```
theorem T : ∀ L₁ L₂, red α L₁ L₂ → true
| L _ (red.refl _) := trivial
| _ _ (@red.trans_bnot _ L₁ L₂ L₃ x b IH) := trivial
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232627):
oh, I get error because I didn't type `L`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232629):
no, without the L you just get a placeholder name

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232669):
You can also use `(@red.refl _ L)` to name the parameters

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232671):
then why do I always get error lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232674):
oh and I can't use recursion because this is a Prop, right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232675):
You can use recursion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232681):
but I would have to provide custom well-founded proof?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232682):
but you can't generate a data type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232684):
maybe that's what you meant

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232743):
it doesn't work for wellfounded either because the inductive type has two constructors, so there are multiple ways to prove a `red` statement

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232802):
https://gist.github.com/johoelzl/7e73916f39e3acef8796bfb6c089a9c9

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232806):
this is interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232811):
"map" and "prod" together give the UMP

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232812):
but I can also prove "map" and "prod" using UMP

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232813):
@**Mario Carneiro** what would you prefer? or should I prove all three?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233054):
I think you should state the UMP just for "completeness", but I expect `map` and `prod` and their lemmas are the more useful version

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233057):
not just for completeness

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233058):
I'll actually prove map and prod from UMP

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233061):
then I don't need any induction again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233064):
The definitions of map and prod are constructive and done reasonably, I wouldn't want to make it more complicated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233072):
everything in my file is constructive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233089):
but you're right, I shouldn't use UMP to define map

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233094):
I mean, you can compute with `map` there. Don't make the program slower

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233097):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233344):
```
instance is_group_hom.id [group α] : is_group_hom (@id α) :=
λ _ _, rfl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233383):
@**Mario Carneiro** could you add this to mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233403):
K

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233430):
obrigad

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235275):
@**Mario Carneiro** `prod` is really a specialization of the UMP though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235287):
I mean, the definition would be identical

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235290):
defining `prod` using the UMP won't make anything slower

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235342):
what is your def of ump?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235346):
```lean
def to_group.aux : list (α × bool) → β :=
λ L, list.prod $ L.map $ λ x, bool.rec_on x.2 (f x.1)⁻¹ (f x.1)

def to_group : free_group α → β :=
quotient.lift (to_group.aux f) $ λ L₁ L₂ ⟨L₃, H13, H23⟩,
(red.to_group H13).trans (red.to_group H23).symm

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235388):
looks good

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235392):
update:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235393):
```lean
def to_group.aux : list (α × bool) → β :=
λ L, list.prod $ L.map $ λ x, cond x.2 (f x.1) (f x.1)⁻¹

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235401):
I guess `prod` is this specialized to id?\

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235403):
correct

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235446):
ok, seems reasonable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235447):
orbigad

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235449):
the spelling keeps getting weirder :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235450):
sim

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235518):
```lean
@[simp] lemma prod.eq_to_group : prod x = to_group id x :=
rfl

@[simp] lemma prod.mk : prod ⟦L⟧ = list.prod (L.map $ λ x, cond x.2 x.1 x.1⁻¹) :=
rfl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235519):
which one should I keep?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235583):
`prod.eq_to_group ` can be the definition, the other one should still be refl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235630):
it is the definition, but I still want a simp lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235633):
it shouldnt be a simp lemma though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235634):
prod.eq_to_group  that is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235638):
why not?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235654):
because it has its own lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235661):
https://gist.github.com/johoelzl/7e73916f39e3acef8796bfb6c089a9c9#file-free_group-lean-L119

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235662):
why isn't this an instance?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235705):
it can be

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 18 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235720):
Yup, I wrote this before `is_group_hom` was a class.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235724):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235766):
anyway, @**Johannes Hölzl** I proved of.inj constructively :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235773):
@**Mario Carneiro** oh, do you know that for any type `X`, `set X` is a group?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 18 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235774):
you  mean with out assuming decidability of α?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235775):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235819):
```lean
#print of
#check @of.inj
#print axioms of.inj

def free_group.of : Π {α : Type u}, α → free_group α :=
λ {α : Type u} (x : α), ⟦[(x, tt)]⟧

of.inj : ∀ {α : Type u_1} {x y : α}, of x = of y → x = y

propext
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 18 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235848):
as long as the proof isn't longer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235859):
aha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235860):
our different values are reflected in as short as two lines

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235903):
the only lengthy part of my file is church rosser

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235905):
which your file doesn't even have

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235912):
a group? With what, symmetric difference and complement?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235913):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235914):
it even forms a ring with multiplication being intersection

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235969):
that seems more like bool -> X

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235970):
X -> bool

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235972):
yeah that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235980):
it's the indexed ring product of Z/2Z

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236022):
is there any easy way to prove that an add_group is a group?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236024):
`multiplicative`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236025):
should I use it to define sum?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236026):
https://gist.github.com/johoelzl/7e73916f39e3acef8796bfb6c089a9c9#file-free_group-lean-L168

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236027):
sure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236029):
wonderful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236035):
I am currently using it to define add_group.smul

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236036):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236040):
it makes it easy to transfer theorems from additive to multiplicative and vice versa using `additive`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236082):
this method is in contrast with `transport_to_additive`, which translates the whole theorem to additive land

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236083):
rather than just applying the theorem with a funny instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236102):
how does it know to transfer list.prod to list.sum :o

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236153):
LOTS of definitional unfolding

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236154):
but not 1 to 0

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236156):
I was surprised by the same thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236158):
1 should go to 0

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236200):
```lean
@[simp] lemma sum.sum : sum (x * y) = sum x + sum y :=
to_group.mul

@[simp] lemma sum.one : sum (1:free_group α) = 0 :=
to_group.one

@[simp] lemma sum.inv : sum x⁻¹ = -sum x :=
to_group.inv

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236202):
the middle one errors

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236204):
you may need to specify the type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236205):
nvm, this worked

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236218):
```lean
@[simp] lemma sum.of {x : α} : sum (of x) = x :=
prod.of

instance sum.is_group_hom : is_group_hom (@sum α _) :=
prod.is_group_hom

@[simp] lemma sum.sum : sum (x * y) = sum x + sum y :=
prod.mul

@[simp] lemma sum.one : sum (1:free_group α) = 0 :=
prod.one

@[simp] lemma sum.inv : sum x⁻¹ = -sum x :=
prod.inv
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236221):
shortwiring everything to prod

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236222):
did I say short wiring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236223):
I mean short-circuiting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236224):
I had to google for this one. my english.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125237946):
```lean
def group.gen [group α] (s : set α) : set α :=
set.range $ @free_group.to_group s _ _ subtype.val
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125237947):
completely pointless usage

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125237949):
(I know we have `group.closure` already)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238075):
maybe you should prove this as a theorem about `group.closure` then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238076):
fazendo :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238144):
what is the idiomatic way to use the fact that 1 is in a subgroup?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238197):
isn't that a theorem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238199):
what is the name?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238200):
presumably `is_subgroup.ome_mem` or similar

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238201):
it isn't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238208):
it should be a field of `is_submonoid`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238209):
it is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238249):
so `is_submonoid.one_mem s` then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238251):
but it doesn't look idiomatic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238255):
the group files seem to open `is_submonoid` to clean it up a bit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238305):
I guess it could go in the root namespace, but `one_mem` sounds a bit generic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 18 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238364):
I never used `export`, but maybe it works to `export is_submonoid`in `is_subgroup`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238453):
`export` is like permanent `open`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238454):
for example, `option.some` is `export`ed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238468):
I don't think it's namespaced, but I could be wrong

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238509):
```lean
theorem useless [group α] (s : set α) :
  set.range (@free_group.to_group s _ _ subtype.val) = group.closure s :=
begin
  apply set.ext,
  intro z,
  split,
  { intro h,
    rcases h with ⟨x, H⟩,
    subst H,
    apply quotient.induction_on x, clear x,
    intro L,
    induction L with hd tl ih,
    case list.nil
    { simp [is_submonoid.one_mem] },
    case list.cons
    { simp at ih ⊢,
      apply is_submonoid.mul_mem,
      { rcases hd with ⟨x, _ | _⟩,
        { simp [is_subgroup.inv_mem (group.subset_closure x.2)] },
        { simp [group.subset_closure x.2] } },
      { assumption } } },
  { intro H,
    induction H with x H x H ih x1 x2 H1 H2 ih1 ih2,
    case group.in_closure.basic
    { existsi (of (⟨x, H⟩ : s)),
      simp },
    case group.in_closure.one
    { existsi (1 : free_group s),
      simp },
    case group.in_closure.inv
    { cases ih with y h,
      existsi y⁻¹,
      simp [h] },
    case group.in_closure.mul
    { cases ih1 with y1 h1,
      cases ih2 with y2 h2,
      existsi y1 * y2,
      simp [h1, h2] } }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238562):
isn't there a more "universal" kind of proof?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238569):
you're right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238570):
both `group.closure` and `free_group.to_group` have universal properties

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239184):
```lean
inductive red : list (α × bool) → list (α × bool) → Prop
| refl {L} : red L L
| trans_bnot {L₁ L₂ L₃ x b} : red L₁ (L₂ ++ (x, b) :: (x, bnot b) :: L₃) → red L₁ (L₂ ++ L₃)

def reduce : list (α × bool) → list (α × bool)
| ((x1,b1)::(x2,b2)::tl) := cond b1
    (cond b2
      ((x1,b1)::(reduce $ (x2,b2)::tl))
      (if x1 = x2 then reduce tl else (x1,b1)::(x2,b2)::(reduce tl)))
    (cond b2
      (if x1 = x2 then reduce tl else (x1,b1)::(x2,b2)::(reduce tl))
      ((x1,b1)::(reduce $ (x2,b2)::tl)))
| L := L

theorem reduce.eq_of_red (H : red L₁ L₂) : reduce L₁ = reduce L₂ := sorry

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239185):
would you have some insights?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239187):
on how to prove the theorem at the bottom?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239239):
oh nvm I'll just use induction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239247):
you could use `b1 = b2` instead of four cases there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239306):
I don't like unfolding `ite`s

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 18 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239308):
I also played around with free_groups: https://gist.github.com/johoelzl/4238422b0810a9d04bb41cfdb682e8ff#file-free_groups-lean-L426 
Now it includes `normalize`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239309):
you win

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 18 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239310):
Using `if _ then _ else _ ` makes `normalize.step` much smaller.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239333):
aha, I like your approach

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239336):
you use `list.sizeof`? Why?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239337):
do it one step first, and then the whole thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239343):
now I'm confused as to what I should do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239400):
```quote
you use `list.sizeof`? Why?
```
to justify that the recursion is well-founded?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 18 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239403):
I never used well founded recursion before. `list.sizeof` was what the equation compiler proposed. Is there an easier way?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239431):
You (Johannes) didn't prove that `normalize` is related to the original input though, or that the result is unique in the equivalence class (it can be defined as a function on the free group itself)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239434):
so there's that if you want it kenny

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 18 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239435):
well its not finished yet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239437):
this is not good

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239439):
You can use `list.length` instead of `sizeof`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239440):
we are writing our own free groups separately

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239443):
this is not good

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239445):
they seem pretty similar

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239514):
they're different enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 18 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239515):
I'm sure we ca merge them later

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239518):
I don't believe in hope

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239525):
Oh, I see Johannes also proved church rosser

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 18 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239587):
Yeah, the question was how to prove it. And then I couldn't sleep and remembered Tobias book on Term Rewriting and All That.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239601):
this is not good

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239603):
you should see how it compares to Kenny's proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239607):
I'm ashamed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239609):
I need to work very hard to shorten my proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 18 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239678):
@**Kenny Lau** why not incorporate both proofs? I think merging both would be helpful.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239686):
our proofs are different enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239688):
our definitions are different enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239689):
this will be a disaster

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239696):
they aren't that different, if I'm following the discussion well enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239698):
you haven't even seen my file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239701):
I am reading it from your posts

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239702):
I can see that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239749):
Why don't you post what you have and then we can compare and see what parts are better in each file?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239752):
lemme finish my `reduce` first

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239810):
here's what I use to do induction on `length`:
```
using_well_founded {
  rel_tac := λ_ _, `[exact ⟨_, inv_image.wf length nat.lt_wf⟩],
  dec_tac := tactic.assumption }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 18 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239813):
Ah! that's perfect

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 18 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239886):
I guess what we also want: a induction method which generalizes all indices of the major hypotheses. I often needed to write something like this:
```lean
revert h,
generalize eq_t : (a :: xs) = t,
intro h,
induction h,
...
```
Or is there a better variant already available?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239899):
same here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239965):
I recall discussing this with Sebastian. The problem with this is that it often cripples the inductive hypothesis (since the index can't get smaller or whatever), and it's hard to say what to generalize to recover it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239973):
which makes it unclear how to proceed in general

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 18 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240027):
I see. We surely don't want to do it in all cases. But something along the lines `induction h generalizing (t_eq : (a :: xs) = t)`. At least would be shorter to write.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240082):
hm, I guess there's no point in the `t` there since it will disappear after the induction. The form of the index is also unnecessary, unless you only want to generalize some indices and leave other index expressions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240093):
So it would suffice to just say `generalizing indices` or something

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240158):
 or equivalently, just have a `induction_g` command (name TBD) with the same syntax as `induction` that does this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240172):
how do you destruct ite in equation compiler?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 18 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240255):
@**Mario Carneiro** I'm fine with `induction_g` or `generalizing indices`. I will take a look into this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240296):
how do you destruct ite in term mode at all?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240297):
I recall asking this a long time ago

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240298):
I can only destruct it in tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240305):
because it is `decidable.rec_on` something obscure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240307):
i.e. a proof that the condition is decidable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240308):
it's easier in tactic mode to be sure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 18 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240310):
@**Kenny Lau** do you mean rewriting with "destruct"? This is surely one thing where tactic mode is prefered.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240327):
that's why I don't like using `ite`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240330):
but you can `match (by apply_instance : decidable p) with ...` and then just use `show` to get rid of the ite in the branches

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240342):
hmm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240394):
this is what I used to do before `by_cases` got good

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240545):
I've got myself into certain trouble

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240549):
```lean
def reduce : list (α × bool) → list (α × bool)
| ((x1,b1)::(x2,b2)::tl) := cond b1
    (cond b2
      ((x1,b1)::(reduce $ (x2,b2)::tl))
      (if x1 = x2 then reduce tl else (x1,b1)::(x2,b2)::(reduce tl)))
    (cond b2
      (if x1 = x2 then reduce tl else (x1,b1)::(x2,b2)::(reduce tl))
      ((x1,b1)::(reduce $ (x2,b2)::tl)))
| L := L

⊢ reduce (L2 ++ (x, b) :: (x, bnot b) :: L3) = reduce (L2 ++ L3)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240590):
do you still have that church rosser proof?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240601):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240602):
```lean
church_rosser : red ?M_2 ?M_3 → red ?M_2 ?M_4 → (∃ (L₄ : list (?M_1 × bool)), red ?M_3 L₄ ∧ red ?M_4 L₄)

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240603):
It suffices to show that reduce is following *some* reduction sequence

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240609):
and that when it gets to the end there is no other possible reduction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240611):
I've shown the former

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240657):
```lean
theorem reduce.min : red (reduce L₁) L₂ → reduce L₁ = L₂ :=

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240658):
issue?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240660):
Then if A ~ B then reduce A ~ A ~ B ~ reduce B, so by C-R there exists C such that reduce A -> C <- reduce B; but reduce A is minimal so reduce A = C = reduce B

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240670):
nice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240723):
@**Mario Carneiro** which list should I destruct?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240725):
where

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240727):
common sense would say the former, but I'm asking if I need to destruct the latter as well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240730):
```lean
theorem reduce.min : red (reduce L₁) L₂ → reduce L₁ = L₂ :=
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240741):
`red` means that you have some representation as append of stuff, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240744):
not sure what you mean; don't think it's right anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240785):
```lean
inductive red : list (α × bool) → list (α × bool) → Prop
| refl {L} : red L L
| trans_bnot {L₁ L₂ L₃ x b} : red L₁ (L₂ ++ (x, b) :: (x, bnot b) :: L₃) → red L₁ (L₂ ++ L₃)

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240786):
I think you want to do induction on L1, along the same lines as the definition of `reduce`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240787):
right, but I'm asking if I need to destruct L2 as well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240793):
no, generalize it in the induction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240796):
why shouldn't I do it in term mode?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240797):
you can

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125241458):
I give up using term mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125241867):
Here's a proof strategy: if `red (reduce L1) L2`, then by cases either `reduce L1 = L2` or `reduce L1 = L3 ++ (x, b) :: (x, bnot b) :: L4` and `L2 = L3 ++ L4`; so it suffices to prove the second case is impossible. Prove `\forall L3 L4 x b, reduce L1 != L3 ++ (x, b) :: (x, bnot b) :: L4` by induction on L1, which you can do in term mode so that the equation compiler sets up the weird induction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125241913):
aha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125241914):
muit obrigad

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125241923):
that will be the first "not" I'm using in a while

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125241976):
are you sure I can do that by induction on L1 alone?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243339):
my function is wrong

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243343):
hmm...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243417):
reducing a word is more difficult than it seems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243624):
I don't think there's an online algorithm to reduce a word

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243629):
so my function is bound to fail

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243632):
I'm using the CS usage of "online"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243809):
just use greedy?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243849):
is your greedy algorithm online?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243850):
and remember to backtrack slightly when you kill $$x * x^{-1}$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243851):
right, that's my new plan now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243852):
how am I writing program in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243854):
...when you should be revising?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243856):
well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243857):
;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244111):
```quote
this will be a disaster
```
No, it's great! Two smart people doing the same thing means that you can take the union of their ideas at the end -- either that, or you get two different ways of doing the same thing, each with their own benefits. Either way it's a win.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244117):
there will be only one version in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244165):
If the two approaches are sufficiently different and both have their uses, then they might both end up in there. If they are sufficiently similar then we end up with the best of both pieces of code. It's just a collaborative open source situation. I ask 200 people to do the same question when I'm teaching them and I don't worry about this at all. Every year I see an answer I haven't seen before, e.g. Chris' modal logic proof of the islanders question this year.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244170):
there can't be two definitions of a free group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244173):
There is generate and span

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244175):
two definitions of the submodule generated/spanned by a subset

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244176):
in my files

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244181):
only span is in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244346):
```lean
def reduce.core : list (α × bool) → list (α × bool) → list (α × bool)
| L [] := L
| [] (h::t) := reduce.core [h] t
| ((x1,tt)::tl1) ((x2,tt)::tl2) :=
    reduce.core ((x2,tt)::(x1,tt)::tl1) tl2
| ((x1,tt)::tl1) ((x2,ff)::tl2) :=
    if x1 = x2
    then reduce.core tl1 tl2
    else reduce.core ((x2,ff)::(x1,tt)::tl1) tl2
| ((x1,ff)::tl1) ((x2,tt)::tl2) :=
    if x1 = x2
    then reduce.core tl1 tl2
    else reduce.core ((x2,tt)::(x1,ff)::tl1) tl2
| ((x1,ff)::tl1) ((x2,ff)::tl2) :=
    reduce.core ((x2,ff)::(x1,ff)::tl1) tl2

def reduce (L : list (α × bool)) : list (α × bool) :=
(reduce.core [] L).reverse
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244347):
this should be correct

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244461):
but it would be difficult to prove anything about it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125254855):
heh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125254858):
```lean
instance is_comm_ring_hom.id {α : Type} [comm_ring α] : is_ring_hom (@id α) :=
{map_add := λ _ _,rfl,map_mul := λ _ _,rfl,map_one := rfl}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125254868):
@**Mario Carneiro** could you add this to mathlib? ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125254923):
Or tell me where to put it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125254943):
in ring.lean, just after definition of is_ring_hom?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125254960):
Is there a better proof? Some "meta-rfl" tactic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255008):
Sounds like a job for Scott's `obviously` tactic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255033):
but it's not yet in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255041):
Patrick, this is what the world has come to. Kenny has defined localization maps and of course there are equivalence classes everywhere, and I'm not very experienced with using them. But Kenny has written a sufficiently good interface (universal properties of localization, basically guided by the needs I had for schemes) that I can work with localizations without ever needing to think about quotient types.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255053):
So I need to prove that the canonical map R[1/S] -> R[1/S] is the identity map

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255113):
and I can either attempt to do this by unravelling the definition and getting my hands dirty

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255123):
or I can do it by observing that the identity map is an R-algebra homomorphism R[1/S] -> R[1/S] and hence it's the canonical map, by some universal property :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255126):
one could also take this as an exercise in tactic writing: write a tactic doing that kind of proof that `id` is a morphism of anything (this should be easy after reading @**Simon Hudon** 's tutorial about how he wrote the pi instance tactic)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255147):
and because I don't like quotient types I will use the universal property.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255155):
Nice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255159):
And I think this shows exactly the point that Mario was explaining to me the other day.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255176):
About interfaces?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255179):
Yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255182):
If the interface (which he did actually describe as "a bunch of universal properties" at the time) is good enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255185):
then you don't ever need to worry about the details

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255226):
of how it is implemented

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255247):
and indeed I can believe that any direct proof that it's the identity might break if some underlying way of implementing equivalence relations changed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255255):
but my universal property definition will never break

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255257):
That is crazy.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255279):
yes, it's great

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255306):
tactic tutorial did you say??

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255358):
I think maths papers should also be written like this. Many math papers lack encapsulation of technical details

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255370):
I don't know if we are the mad ones or the sane ones

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255385):
Yes, Simon is writing some tutorial

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255395):
Or at least he intends to do it, and I remind him from time to time.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255407):
Which is really unfair because I lack time for all my Lean projects

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255426):
But in three weeks I'll be done with teaching and I hope I'll be able to work more seriously on Lean stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 18 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255520):
```quote
If the interface (which he did actually describe as "a bunch of universal properties" at the time) is good enough
then you don't ever need to worry about the details
of how it is implemented
```

@**Kevin Buzzard** I think I agree with this. But, just for my education, what is the definition of “universal” here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255607):
I'm giving a graduate course and tomorrow and next lecture are about https://arxiv.org/abs/1201.2245 And a new version came out on arXiv on Monday, after five years without moving. Since then I've been reading like crazy to understand why she changed so many things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255629):
Good news is the new version contains something which is much closer to an actual proof of the main theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255687):
But that doesn't leave much time for Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255757):
Sean: https://en.wikipedia.org/wiki/Universal_property

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255801):
Sean -- I asked Kenny to type up some basic constructions of localization of rings at multiplicative sets in Lean. Kenny read a book on commutative algebra and did it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255811):
I then realised I couldn't use his constructions at all because to access any element of the localized ring I needed to start playing around with quotient types

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255845):
so I asked him if he could also prove various results of the form "if some situation is true, then there's a map from some ring to a localized ring"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255848):
or "if some situation is true, then there's a map from a localized ring to some ring"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255849):
and he did this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255853):
and then I realised that I still couldn't prove half the things I wanted to prove

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255911):
so I asked him if he could prove various results of the form "if some situation is true, then there's a map from some ring to some localized ring and furthermore it is the unique map with some property"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255915):
and similarly the other way around

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255920):
and then I could prove everything I needed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255922):
but then to my surprise

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255938):
I realised that statements of the form "this map that Kenny defined is the identity map"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255941):
which I needed to prove

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255953):
even such statements as that, which my gut instinct said "this proof should be refl"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256011):
I realised I was proving by showing that the identity map had the property required of Kenny's map, and hence was Kenny's map

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256017):
and this has had the joyous consequence

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256020):
that I never once have to write an equivalence class

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256021):
which is great

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256023):
because I don't know if it's just me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256029):
but whenever I type `\[[` it doesn't work properly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256036):
I get `\[[]]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256042):
so you manually delete the extra closing brackets and press space to enter it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256053):
instead of `⟦`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256058):
aah, you are an equivalence relation expert

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256064):
instead of doing that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256068):
I get you to write me an interface ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 18 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256142):
@**Kevin Buzzard** So, am I right in that you are describing a sort of minimum set of properties for a given definition that allow you to prove something without having to unfold the given definition?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256146):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256204):
but somehow in the past I knew that this sort of thing was sometimes possible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 18 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256208):
That's what I thought. Is that the same thing as https://en.wikipedia.org/wiki/Universal_property as @**Patrick Massot** referred to? I didn't think so.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256211):
but when it came to the identity map, I didn't care

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256219):
because "one can easily check that this map is the identity map from the construction"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256226):
at least, I would not be scared to write that in a maths paper

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256230):
but in this situation I am so scared to prove anything directly from the construction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256240):
Kevin, that's also the same idea in https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/.60_.60.20style.20and.20order.20of.20goals/near/125119384

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256243):
that it has only now dawned on me that even trivial things which I would usually prove directly from the construction can be done via the interface

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256246):
Oh is it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256248):
I didn't understand that comment

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256256):
I guessed so, that's why I'm referring to it now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256297):
That comment is starred for "come back to this when your daughter is not off school sick"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256299):
I'm talking about the first bullet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256318):
I kind of think/hope that the general technique I picked up when working on those proofs was the thing Mario was trying to explain to me there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256330):
but I've not had time to internalise it yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256336):
I can really see the light at the end of the tunnel for affine schemes now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256346):
Great!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256348):
Chris did the ghastly ring theory multinomial theorem lemma which I was putting off

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256394):
and what is left, I believe, is the kind of mathematics which is really good fun to type into Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256403):
i.e. it's just universal property after universal property

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256425):
The last 5 theorems I proved had proofs of the form `name_of_universal_property_theorem _ _ _ _`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256441):
i.e. exactly what one would write in mathematics:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256446):
"this follows from the universal property"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 18 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256456):
except that one failed because Lean didn't know the identity was a ring hom ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 18 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256511):
Have I already published the tutorial?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256532):
Not yet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 18 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256533):
You are about to do it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 18 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256542):
Oh! Thanks for keeping me up-to-date!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125267684):
Done!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125267686):
https://github.com/kckennylau/Lean/blob/master/free_group.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125267689):
@**Mario Carneiro** do you see how to shorten my proofs?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 18 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125267750):
@**Johannes Hölzl**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 18 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125267882):
What helped in my approach: not using `setoid` and `quotient` but `quot`. Also I introduced a `refl_trans` and `refl_cl` to handle the relations and a general version of Church-Rosser. I guess using `append_eq_append_iff`, together with `case_matching*` was useful automation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 18 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125268207):
I don't combine the transitive closure and the reduction relation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125290928):
@**Johannes Hölzl** @**Mario Carneiro** do we mind reversing the direction of `red` to conform with wf conventions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 19 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125290929):
no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125290933):
I'm disinclined to because it would break reduction conventions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125290939):
i.e. church rosser is completely different the other way around

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125290943):
the automater doesn’t work well though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125290944):
(it's called something like noetherian in this case)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125290988):
If you use `tactic.assumption` as the discharger, it should reduce the `swap`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125290990):
you could also state your hypothesis with `swap`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125291017):
this is the problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125291018):
```lean
inductive red.step : list (α × bool) → list (α × bool) → Prop
| bnot {L₁ L₂ x b} : red.step (L₁ ++ (x, b) :: (x, bnot b) :: L₂) (L₁ ++ L₂)

inductive red : list (α × bool) → list (α × bool) → Prop
| refl {L} : red L L
| trans_step {L₁ L₂ L₃} (H : free_group.red.step L₂ L₃) :
    red L₁ L₂ → red L₁ L₃
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125291019):
so I defined things like this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125291060):
now I'm in this stage:
```lean
H1 : red.step L2 L₂,
H2 : red L₁ L2
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125291064):
so if I want to prove something with `L₁` and `L₂`, then I would recursion on `H2` right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125291073):
then somehow the automater wants me to prove this:
```lean
⊢ function.swap red.step L₁ L₁
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125291111):
What is the setup of your induction?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125291122):
I want to prove that red L1 L2 -> red (inv L1) (inv L2)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125291130):
I’m starting to believe that my approach won’t work because it’s in the wrong direction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125291252):
I’ll just define red differently then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125304550):
I have renamed this thread to "free group"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125304556):
in other news, I shortened the file a bit more: https://github.com/kckennylau/Lean/blob/master/free_group.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125304562):
@**Mario Carneiro** could you have a look?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125304769):
not a single negation in my file :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 19 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306426):
Just looking at the proof: it looks like `red.step.church_rosser` could be made smaller by wlog after the case `list.prefix_or_prefix_of_append_eq_append `? At least the proof structure looks very similar.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306474):
@**Johannes Hölzl** I just shortened red.step.church_rosser by 10 lines

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306477):
now it spans 34 lines and does not depend on `list.prefix_or_prefix_of_append_eq_append`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306478):
I feel good

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 19 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306483):
nice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306484):
this means I can now convert it to equation compiler and save more lines

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306553):
```quote
Just looking at the proof: it looks like `red.step.church_rosser` could be made smaller by wlog after the case `list.prefix_or_prefix_of_append_eq_append `? At least the proof structure looks very similar.
```
right, but I just can't find a way for wlog to work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306564):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog.20example

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306566):
nobody replied

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 19 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306654):
I didn't mean to use directly the `wlog` tactic. I meant to do the following: state the theorem, and use it to proof one direction, and then the second one by the corresponding application of symmetry and AC (associativity and commutativity of append, and etc)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306704):
that's disgusting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306709):
I would rather wait for them to fix wlog

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306788):
```lean
{ injections, subst_vars, simp }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306791):
I used this so much, this should be a tactic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 19 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306820):
What? Why is it **disgusting**? That's how you do it. You can work on changing wlog yourself!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306844):
anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125308690):
13 lines lost!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125308693):
```lean
theorem red.step.church_rosser.aux2 : ∀ {L₁ L₂ L₃ L₄ : list (α × bool)} {x1 b1 x2 b2},
  L₁ ++ (x1, b1) :: (x1, bnot b1) :: L₂ = L₃ ++ (x2, b2) :: (x2, bnot b2) :: L₄ →
  L₁ ++ L₂ = L₃ ++ L₄ ∨ ∃ L₅, red.step (L₁ ++ L₂) L₅ ∧ red.step (L₃ ++ L₄) L₅
| [] _ [] _ _ _ _ _ H  :=
  by injections; subst_vars; simp
| [] _ [(x3,b3)] _ _ _ _ _ H :=
  by injections; subst_vars; simp
| [(x3,b3)] _ [] _ _ _ _ _ H :=
  by injections; subst_vars; simp
| [] _ ((x3,b3)::(x4,b4)::tl) _ _ _ _ _ H :=
  by injections; subst_vars; simp; right; exact ⟨_, red.step.bnot, red.step.cons_bnot⟩
| ((x3,b3)::(x4,b4)::tl) _ [] _ _ _ _ _ H :=
  by injections; subst_vars; simp; right; exact ⟨_, red.step.cons_bnot, red.step.bnot⟩
| ((x3,b3)::tl) _ ((x4,b4)::tl2) _ _ _ _ _ H :=
  let ⟨H1, H2⟩ := list.cons.inj H in
  match red.step.church_rosser.aux2 H2 with
    | or.inl H3 := or.inl $ by simp [H1, H3]
    | or.inr ⟨L₅, H3, H4⟩ := or.inr ⟨_, red.step.cons H3, by simpa [H1] using red.step.cons H4⟩
  end

theorem red.step.church_rosser.aux : ∀ {L₁ L₂ L₃ L₄ : list (α × bool)},
  red.step L₁ L₃ → red.step L₂ L₄ → L₁ = L₂ →
  L₃ = L₄ ∨ ∃ L₅, red.step L₃ L₅ ∧ red.step L₄ L₅
| _ _ _ _ red.step.bnot red.step.bnot H := red.step.church_rosser.aux2 H

theorem red.step.church_rosser (H12 : red.step L₁ L₂) (H13 : red.step L₁ L₃) :
  L₂ = L₃ ∨ ∃ L₄, red.step L₂ L₄ ∧ red.step L₃ L₄ :=
red.step.church_rosser.aux H12 H13 rfl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 19 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125308696):
Be careful not to drop to zero

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125308698):
probably can delete some newlines

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 19 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125308713):
That's what my PhD advisor used to say

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125340029):
https://github.com/kckennylau/Lean/blob/master/free_group.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125340064):
now it is 531 lines

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125340072):
Johannes's file is 486 lines

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125340073):
only 45 lines to go :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 20 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342476):
But my file is not finished! There are a couple of proofs missing... So i guess 531 lines are good enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342482):
Could I insist to use `quotient`? @**Johannes Hölzl**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342490):
you seem to have developed some theories of the transitive and reflexive closure of general reduction propositions though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342492):
maybe you could put that theories in another file and I can use it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 20 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342550):
Yes, I will put `refl_trans` and `refl_cl` somewhere in mathlib. I'm not sure yet about the naming.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342551):
I would love it if you could prove that the result is a setoid ^^

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342553):
```lean
instance : setoid (list (α × bool)) :=
⟨λ L₁ L₂, ∃ L₃, red L₁ L₃ ∧ red L₂ L₃,
 λ L, ⟨L, red.refl, red.refl⟩,
 λ L₁ L₂ ⟨L₃, H13, H23⟩, ⟨L₃, H23, H13⟩,
 λ L₁ L₂ L₃ ⟨L₄, H14, H24⟩ ⟨L₅, H25, H35⟩,
   let ⟨L₆, H46, H56⟩ := church_rosser H24 H25 in
   ⟨L₆, red.trans H14 H46, red.trans H35 H56⟩⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342590):
the relation being "there is a common reduction"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 20 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342703):
yep, makes sense.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342710):
and I think this is better than the refl-symm-trans closure, because things are easier to prove

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342711):
the symm makes everything work no well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477808):
@**Mario Carneiro** I just proved that `red` is a partial order

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477809):
Should I be using `\le`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477851):
No, it's not really a less-than kind of thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477852):
should I remove the proof?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477853):
I would prefer ~>* if you want notation for red

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477859):
is there unicode?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477860):
also, it kinda looks like something not nice, so you might want to think twice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477862):
That's a right squiggle arrow with a star

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477863):
the right squiggle arrow is `red.step`, and the star is its reflexive transitive closure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477904):
eh, is that an answer to any of my two questions...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477953):
there is unicode for the right squig arrow, pretty sure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477955):
I was explaining the notation in response to "not so nice" comment

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477956):
so you're saying I should define reflexive transitive closure?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477959):
you sort of did

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477967):
I mean define `~>` and `*` separately

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477969):
You could do like Johannes did and prove C-R generically over r.t. closure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478010):
would the notations work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478017):
I doubt it, but you could locally define ~>* to mean `rt_closure red.step` or something

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478165):
I found this in unicode: ⇝ , but it's a bit hard to distinguish from the regular arrow in my font on vscode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478168):
let's just stick with `red`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478173):
should I remove the proof?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478175):
are you using it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478176):
not really, as you said we don't want to use `\le`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478177):
I have the other theorems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478217):
my proof is literally
```lean
instance : partial_order (list (α × bool)) :=
{ le := red,
  le_refl := λ _, red.refl,
  le_trans := λ _ _ _, red.trans,
  le_antisymm := λ _ _, red.antisymm }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478218):
yeah, skip it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478219):
ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478477):
```lean
inductive red.step : list (α × bool) → list (α × bool) → Prop
| bnot {L₁ L₂ x b} : red.step (L₁ ++ (x, b) :: (x, bnot b) :: L₂) (L₁ ++ L₂)

instance : fintype { L₂ // red.step L₁ L₂ } :=
_
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478481):
@**Mario Carneiro** @**Chris Hughes** would you have some insights as to how I would prove this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478522):
Even stronger, the set of all lists that are `red` related to the original is finite

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478523):
right, but this is the inductive step

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478528):
because if `red L1 L2` then `L2 <+ L1`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478530):
and then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478531):
use `sublists`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478557):
but it is not in mathlib that sublists are finite

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478572):
yes, that's `sublists`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478574):
it's literally a list of all sublists of another

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478575):
hence finite

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478577):
aha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478587):
then again it's probably not the most efficient enumeration strategy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478635):
have you proven that `red L1 L2` is decidable?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478636):
let's say I have

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478637):
(I have not, but I will)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478677):
it's easier to prove that the free group relation (including symmetry) Is decidable, since then you can use `reduce`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478681):
I don't understand, sorry

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478687):
how would I use reduce to prove that red L1 L2 is decidable?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478688):
you can decide if L1 ~ L2 by just reducing both sides and testing for equality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478691):
but that doesn't mean red is decidable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478693):
that doesn't give you decidability of `red` though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478788):
how would that help?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478797):
I'm not sure how important it is to know that red is decidable, but you need that to build a fintype using filter and sublists the way I described

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478798):
aha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478800):
you could also directly enumerate the red related lists

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478803):
which amounts to writing another reduce-like function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478840):
i.e. with a core

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478843):
```lean
def reduce.step : list (α × bool) → (α × bool) → list (α × bool)
| (hd::tl) x := if hd.1 = x.1 ∧ hd.2 = bnot x.2 then tl else x::hd::tl
| [] x := [x]

def reduce.core : list (α × bool) → list (α × bool) → list (α × bool)
| L []       := L
| L (hd::tl) := reduce.core (reduce.step L hd) tl

def reduce (L : list (α × bool)) : list (α × bool) :=
reduce.core [] L.reverse
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478845):
speaking of which, I don't understand why your definition is so convoluted

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478846):
why the reverse?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478848):
because it gets reversed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478849):
...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478850):
so I have a word `[a,b,c,d,e,f,g,h]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478852):
my pointer goes from left to right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478857):
and the left of the pointer gets reversed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478859):
because the heads are at `d` and `e` respectively

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478860):
you can output either reversed or not, depending on how you structure the recursive call

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478861):
after the traversal of the list, it will become `[h,g,f,c,b,a]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478863):
look at how `list.foldl` and `list.foldr` are defined

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478898):
basically

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478907):
I destructed the list once, so it has to get reversed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478908):
What's wrong with Johannes's definition of reduce?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478910):
it's less efficient

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478914):
my algorithm is O(n)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478916):
his algorithm is O(n^2)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478921):
[don't quote me on this]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479008):
To be clear, I'm talking about the following definition:
```
def reduce {α} [decidable_eq α] : list (α × bool) → list (α × bool)
| ((a₁, p) :: (a₂, n) :: xs) :=
  if a₁ = a₂ ∧ p ≠ n then reduce xs
  else (a₁, p) :: reduce ((a₂, n) :: xs)
| l := l
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479010):
that's wrong

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479011):
as I painfully realized two days ago

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479014):
because `[a,b,b^-1,a^-1]` becomes `[a,a^-1]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479112):
Fair enough. What about this then:
```
def reduce {α} [decidable_eq α] : list (α × bool) → list (α × bool)
| ((a₁, p) :: xs) :=
  match reduce xs with
  | (a₂, n) :: xs' :=
    if a₁ = a₂ ∧ p ≠ n then xs'
    else (a₁, p) :: (a₂, n) :: xs'
  | [] := [(a₁, p)]
  end
| l := l
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479117):
(deleted)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479119):
aha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479162):
somehow my gut says this is n^2 also

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479164):
it seems to work
```
#eval reduce [(0, tt), (1, tt), (1, ff), (0, ff), (0, tt), (0, ff)]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479165):
my gut might be wrong

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479166):
I don't think it is since it's one-pass

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479173):
this is what I mean by "depending on how you use the IH"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479174):
interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479175):
that's clever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479176):
you can either process and then call the IH, or call the IH and then process, or both

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479177):
that's how `foldl` and `foldr` get different results

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479265):
I have much more to learn

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481027):
@**Mario Carneiro** the lifting theorem is really a pain

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481028):
I need some guidance from you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481029):
it isn't really straightforward

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481070):
```lean
L₂ L4 L5 L6 : list (α × bool),
H45 : red.step L4 L5,
H56 : red L5 L6,
H26 : red.step L₂ L6,
H24 : L₂ <+ L4,
ih : L₂ <+ L5 → red L5 L₂
⊢ red L4 L₂
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481071):
wrong thread

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481077):
this is the hardest part of the proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481078):
the rest is just induction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481129):
wait, I'm confused. What's the statement and proof so far?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481132):
the thing I sent you just there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481133):
is the inductive step

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481135):
the rest is just induction that I can do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481137):
I know, but it doesn't make any sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481138):
oh, the lifting theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481139):
I don't understand what got you to this point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481178):
if reduce L1 = reduce L2 and L2 is a sublist of L1, then red L1 L2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481181):
ah, I was thinking about that but I'm not sure it's a theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481182):
aha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481183):
I thought it's true

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481184):
my gut tells me so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481190):
now to make it more like the lifting theorem, we restate it:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481191):
if red L1 L3 and red L2 L3, and that L2 is a sublist of L1, then red L1 L2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481233):
I can't really come up with a counter-example

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481234):
I can think of examples where the lift is not really trivial

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481761):
Okay, I'm still not on board with saying it's definitely true but we can try to prove it anyway. Let's show that if `red L1 L3` and `red L2 L3`, then `L2 <+ L1` implies `red L1 L2`. Proof by induction on `red L2 L3`, reducing to the following lemma: if `red L1 L3` and `red.step L2 L3` and `L2 <+ L1` then `red L1 L2`. Now you have some list details by comparing `red.step` with `<+`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481943):
aha, counterexample: `abb⁻¹a⁻¹` has a sublist `bb⁻¹` which reduces to `[]`, but `abb⁻¹a⁻¹` does not reduce to `bb⁻¹`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125482387):
aha!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125482389):
nice, thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125482394):
so, how might we prove that red is decidable?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125482941):
```
def is_red {α} [decidable_eq α] : list (α × bool) → list (α × bool) → bool
| [] [] := tt
| [] ((b, q) :: ys) := ff
| ((a, p) :: xs) [] := is_red xs [(a, bnot p)]
| ((a, p) :: xs) ((b, q) :: ys) :=
  if (a, p) = (b, q) then is_red xs ys else
  is_red xs ((a, bnot p) :: (b, q) :: ys)
```
replace `bool` with `decidable` and insert proofs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125482944):
aha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125484985):
@**Mario Carneiro** should I inject your name onto the top of the file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125485472):
If you want... I've got enough credits on mathlib already, I don't need to be stealing it from others ;)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125485519):
I guess the full combined file on free groups when it gets finished will be joint work of all three of us, there's been a lot of collaboration on it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125492272):
```lean
theorem red.of_cons {x} : red (x :: L₁) (x :: L₂) → red L₁ L₂ :=
begin
  generalize H1 : (x :: L₁ : list _) = L1,
  generalize H2 : (x :: L₂ : list _) = L2,
  intro H,
  induction H with L3 L3 L4 L5 H3 H4 ih generalizing x L₁ L₂,
  case red.refl
  { subst H1; injections; subst_vars },
  case red.step_trans
  { cases H3 with L6 L7 x1 b1,
    subst_vars,
    cases L6 with hd tl,
    case list.nil
    { injection H1 with H5 H6,
      substs H5 H6,
      clear H1 H3,
      transitivity,
      { exact red.cons H4 },
      { simp } },
    case list.cons
    { injection H1 with H5 H6,
      substs H5 H6,
      exact red.trans red.bnot (ih rfl rfl) } }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125492273):
why so long

