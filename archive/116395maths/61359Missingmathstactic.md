---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/61359Missingmathstactic.html
---

## Stream: [maths](index.html)
### Topic: [Missing maths tactic?](61359Missingmathstactic.html)

---

#### [Kevin Buzzard (Nov 23 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148250605):
`example (a b c d : ℤ) (H : a - b = c * d) : b - a = c * (-d) := by simp [H] -- fails`.

Is this one of those instances when someone familiar with Coq says "oh, it would work if you had <insert name of tactic which I don't know what it does, but it turns out it does this>"? I'm teaching equivalence relations shortly, and this stuff comes up with congruences; I want to give Lean a big push if possible but I want to make it look slick, ideally.

I remark that `example (a b c d : ℤ) (H : a - b = c * d) : b - a = c * (-d) := by simp [H.symm]` works! But I am stuck with having it this way round because it's how `has_dvd.dvd` unfolds on int :-( [I'm trying to prove congruence mod c is symmetric in a completely transparent way]

#### [Kevin Buzzard (Nov 23 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251400):
heh:

```lean
example (a b c : ℤ) : a - c = a - b + (b - c) := by simp -- fails
```

```lean
import tactic.ring

example (a b c : ℤ) : a - c = a - b + (b - c) := by ring -- works (of course)
```
but the surprise is

```lean
import tactic.ring

example (a b c : ℤ) : a - c = a - b + (b - c) := by simp -- works!
```

For this one I knew the tactic, but then I realised I didn't need it.

#### [Patrick Massot (Nov 23 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251450):
I think last year we had an extended discussion about how to define this equivalence relation in order to get an easy proof

#### [Kevin Buzzard (Nov 23 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251456):
But I really want a one-liner for this if possible:

```lean
example (m a b c j k : ℤ) (Hj : a - b = m * j) (Hk : b - c = m * k) :
a - c = m * (j + k) :=
begin
  rw [mul_add],
  rw [←Hj,←Hk],
  -- ⊢ a - c = a - b + (b - c)
  simp, -- works if tactic.ring imported
end
```

I want to do ring [Hj,Hk] or something, but I'm well aware that life isn't so easy.

#### [Kevin Buzzard (Nov 23 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251513):
```quote
I think last year we had an extended discussion about how to define this equivalence relation in order to get an easy proof
```
 Yes, the trick is to define congruence mod m (it was mod 37 last time) in a different way -- the order matters. But unfortunately in my lectures I defined congruence mod m to mean `m | (a - b)` so now I'm stuck with it and it unfolds to something which is not in the optimal order.

#### [Kevin Buzzard (Nov 23 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251525):
Is this one of those things which is done by omega or cooper or something -- these tactics that I have no idea what they are?

#### [Andrew Ashworth (Nov 23 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251577):
Omega only handles presburger arithmetic, ie no multiplication.

#### [Kevin Buzzard (Nov 23 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251584):
Hmm. I suspect `by Groebner_basis` might do it.

#### [Andrew Ashworth (Nov 23 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251585):
Cooper might do it, but I don't have lean in front of me to try it

#### [Kevin Buzzard (Nov 23 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251588):
I have Lean in front of me -- how do I get cooper working?

#### [Reid Barton (Nov 23 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251643):
Maybe you can add https://github.com/skbaek/qe as a dependency now

#### [Kenny Lau (Nov 23 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251707):
```lean
example (m a b c j k : ℤ) (Hj : a - b = m * j) (Hk : b - c = m * k) :
  a - c = m * (j + k) :=
by rw [mul_add, ← Hj, ← Hk, sub_add, sub_sub_self]
```

#### [Reid Barton (Nov 23 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251708):
(but I don't know how to actually *use* it)

#### [Andrew Ashworth (Nov 23 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251711):
I think the examples in https://github.com/skbaek/qe/blob/master/src/examples.lean are self explanatory

#### [Kevin Buzzard (Nov 23 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251716):
```lean
definition cong_mod_37 (a b : ℤ) := ∃ k : ℤ, 37 * k = a - b

example (a : ℤ) : cong_mod_37 a a :=
begin
  use 0,
  simp,
end

example (a b : ℤ) (H : cong_mod_37 a b) : cong_mod_37 b a :=
begin
  cases H with k Hk,
  use -k,
  simp [Hk],
end

example (a b c : ℤ) (H1 : cong_mod_37 a b) (H2 : cong_mod_37 b c) : cong_mod_37 a c :=
begin
  cases H1 with j Hj,
  cases H2 with k Hk,
  use (j+k),
  simp [mul_add,Hj,Hk],
end
```

#### [Kevin Buzzard (Nov 23 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251753):
@**Kenny Lau** I know how to do it, but the problem is that your proof is a great example of how to put first year undergraduates off Lean.

#### [Kevin Buzzard (Nov 23 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148251754):
Compare with my 37 proofs, where everything is just simp.

#### [Patrick Massot (Nov 23 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252152):
@**Kevin Buzzard** about `example (m a b c j k : ℤ) (Hj : a - b = m * j) (Hk : b - c = m * k) : a - c = m * (j + k)`. For students I think a two-liner is good enough. The proof you would tell them is: "add equations Hj and Hk, then compute". Having a tactic `add_eq Hk Hj` is clearly within reach (actually we should both know how to do that by now). It would replace the first line in:
```lean
example (m a b c j k : ℤ) (Hj : a - b = m * j) (Hk : b - c = m * k) :
a - c = m * (j + k) :=
begin
  have : (a - b) + (b - c) = (m * j) + (m * k) := congr (congr_arg int.add Hj) Hk,
  ring at *,
  assumption
end
```

#### [Kenny Lau (Nov 23 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252226):
... can someone teach me how to write tactics

#### [Patrick Massot (Nov 23 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252241):
Yes

#### [Patrick Massot (Nov 23 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252248):
Johannes, Mario, Simon, Rob, Scott...

#### [Andrew Ashworth (Nov 23 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252389):
The textbook everyone recommends is Handbook of Practical Logic and Automated Reasoning

#### [Andrew Ashworth (Nov 23 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252503):
Term rewriting and all that is good too, so is Modern Computer Algebra, depending on what you want your tactics to do

#### [Patrick Massot (Nov 23 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252856):
Andrew, our problem stops us before needing anything from these books. It's about Lean meta programming (especially parsing arguments in our case).

#### [Patrick Massot (Nov 23 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252902):
Our only immediate hope is @**Simon Hudon** will pity us, and we'll wake up with a `add_eq` tactic PR'ed to mathlib.

#### [Simon Hudon (Nov 23 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252955):
How can you be sure that he heard you?

#### [Patrick Massot (Nov 23 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252971):
That's the magic of Zulip's notification

#### [Patrick Massot (Nov 23 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252974):
And it's midnight here, so I'm allowed to dream

#### [Simon Hudon (Nov 23 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148252975):
You sure are

#### [Simon Hudon (Nov 23 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253023):
What's the gist of this `add_eq` that you're looking for?

#### [Patrick Massot (Nov 23 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253036):
It replaces
```lean
example (m a b c j k : ℤ) (Hj : a - b = m * j) (Hk : b - c = m * k) :
a - c = m * (j + k) :=
begin
  have : (a - b) + (b - c) = (m * j) + (m * k) := congr (congr_arg int.add Hj) Hk,
  ring at *,
  assumption
end
```
by
```lean
example (m a b c j k : ℤ) (Hj : a - b = m * j) (Hk : b - c = m * k) :
a - c = m * (j + k) :=
begin
  add_eq Hj Hk,
  ring at *,
  assumption
end
```

#### [Patrick Massot (Nov 24 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253099):
It's similar in spirit to the `mul_left` tactic that we never finished writing

#### [Simon Hudon (Nov 24 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253117):
Wouldn't a lemma work just as well?

#### [Patrick Massot (Nov 24 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253233):
I don't understand how you can miss such opportunities to save the world with a new tactic

#### [Patrick Massot (Nov 24 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253234):
```lean
lemma add_eq {α : Type*} [has_add α] {b c d e : α} (H : b = c) (H' : d = e) : 
  b + d = c + e := congr (congr_arg has_add.add H) H'

example (m a b c j k : ℤ) (Hj : a - b = m * j) (Hk : b - c = m * k) :
a - c = m * (j + k) :=
begin
  have := add_eq Hj Hk,
  ring at *,
  assumption,
end
```

#### [Simon Hudon (Nov 24 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253274):
My favorite tactics are those I don't have to write :P

#### [Simon Hudon (Nov 24 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253283):
(btw, you type faster than I do, I was about to write that!)

#### [Patrick Massot (Nov 24 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253285):
I wonder whether this lemma is already in mathlib, the hypothesis `has_add α` is really weak

#### [Reid Barton (Nov 24 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253331):
Maybe a two-argument `congr_arg₂` would be nice?

#### [Patrick Massot (Nov 24 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253333):
Yes, I also thought about that when writing the first version of the proof

#### [Kenny Lau (Nov 24 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253445):
```quote
Maybe a two-argument `congr_arg₂` would be nice?
```
 https://github.com/leanprover/mathlib/pull/118#discussion_r183841541

#### [Patrick Massot (Nov 24 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253449):
But for students I would still prefer to have the `add_eq` lemma and its friends that the abstract version

#### [Patrick Massot (Nov 24 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253515):
Same story as ever: an impressive proof from Kenny
```lean
theorem congr_arg₂ {α β γ : Type*} (f : α → β → γ) {x₁ x₂ : α} {y₁ y₂ : β}
  (Hx : x₁ = x₂) (Hy : y₁ = y₂) : f x₁ y₁ = f x₂ y₂ :=
eq.drec (eq.drec rfl Hy) Hx

lemma add_eq {α : Type*} [has_add α] {b c d e : α} (H : b = c) (H' : d = e) : 
  b + d = c + e := congr_arg₂ has_add.add H H'
```
and then Mario wins:
```lean
lemma add_eq {α : Type*} [has_add α] {b c d e : α} (H : b = c) (H' : d = e) : 
  b + d = c + e := by congr'
```

#### [Patrick Massot (Nov 24 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253565):
I still think all versions deserve to be in mathlib: `congr_arg₂` and `add_eq` with its one-word proof

#### [Patrick Massot (Nov 24 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148253595):
And now, I really go to sleep

#### [Kenny Lau (Nov 24 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148256302):
man these 10 lines took me 1.5 hours to write:
```lean
import tactic.ring

namespace tactic.interactive
open lean.parser tactic interactive
meta def add_eq (h1 : parse ident) (h2 : parse ident)
  (h : parse (optional (tk "with" *> ident))) : tactic unit :=
do
e1 ← get_local h1, e2 ← get_local h2,
e ← to_expr ```(_root_.congr (congr_arg has_add.add %%e1) %%e2),
tactic.note (h.get_or_else `this) none e
>> skip
end tactic.interactive

example (m a b c j k : ℤ) (Hj : a - b = m * j) (Hk : b - c = m * k) :
  a - c = m * (j + k) :=
begin
  add_eq Hj Hk,
  ring at *,
  assumption
end
```

#### [Kenny Lau (Nov 24 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148256304):
@**Kevin Buzzard** I wrote my first tactic just by browsing through core / mathlib

#### [Kenny Lau (Nov 24 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148256360):
@**Mario Carneiro** are you going to replace my 5-line tactic with 1 line now?

#### [Kenny Lau (Nov 24 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148256569):
golfed:
```lean
import tactic.ring

namespace tactic.interactive
open lean.parser tactic interactive
meta def add_eq (h1 : parse ident) (h2 : parse ident)
  (h : parse (optional (tk "with" *> ident))) : tactic unit :=
do e1 ← get_local h1, e2 ← get_local h2,
   «have» h none ```(_root_.congr (congr_arg has_add.add %%e1) %%e2)
end tactic.interactive

example (m a b c j k : ℤ) (Hj : a - b = m * j) (Hk : b - c = m * k) :
  a - c = m * (j + k) :=
begin
  add_eq Hj Hk,
  ring at *,
  assumption
end
```

#### [Scott Morrison (Nov 24 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148256983):
@**Kenny Lau**, why not reuse the lemma, and save yourself constructing the expression by hand:
```
import tactic.ring

lemma add_eq {α : Type*} [has_add α] {b c d e : α} (H : b = c) (H' : d = e) :
  b + d = c + e := by congr'

namespace tactic.interactive
open lean.parser tactic interactive
meta def add_eq (h1 : parse ident) (h2 : parse ident)
  (h : parse (optional (tk "with" *> ident))) : tactic unit :=
do e1 ← get_local h1,
   e2 ← get_local h2,
   «have» h none ```(add_eq %%e1 %%e2)
end tactic.interactive

example (m a b c j k : ℤ) (Hj : a - b = m * j) (Hk : b - c = m * k) :
  a - c = m * (j + k) :=
begin
  add_eq Hj Hk,
  ring at *,
  assumption
end
```

#### [Kenny Lau (Nov 24 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148256990):
fair enough

#### [Scott Morrison (Nov 24 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148257035):
Quotations are your friend, both for constructing `expr` instances and pattern matching on them.

#### [Johan Commelin (Nov 24 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148265264):
Doesn't this mean that we should provide `instance {A : Type*} [has_add A] : has_add (eq A)`? And then prove that it is associative and commutative in the appropriate cases...

#### [Johan Commelin (Nov 24 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148265271):
@**Mario Carneiro** Is it possible to do `ring at * using [foo,bar]`?

#### [Kevin Buzzard (Nov 24 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148267312):
This sounds unlikely as it sounds like you're asking Lean to figure out if an element of a ring is in the ideal generated by the inputs, which is surely well beyond the ring tactic

#### [Mario Carneiro (Nov 24 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148268834):
Right. As you have identified this needs groebner bases, which could be a future generalization of `ring` but is a completely different algorithm

#### [Mario Carneiro (Nov 24 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148268884):
@**Kenny Lau** , be careful golfing tactic code. Because we don't have the same assurances on correctness of meta code, it's much more like conventional programming, and it is important to be clear rather than compact, for maintainability

#### [Rob Lewis (Nov 24 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148271134):
FYI, a student of ours who just started his BS thesis project is interested in Grobner basis algorithms. I'm not sure exactly which direction his project will go. Hopefully we'll get the core of an algorithm for this kind of thing, and then either he or we will turn it into a tactic.

#### [Johan Commelin (Nov 24 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148280564):
Wouldn't it be faster (both  development, and user experience) to piggyback on some other CAS? You already have the Mathematica interface. I guess a pari or sage interface would also be helpful. And we would get grobner basis tactics "for free"...

#### [Kevin Buzzard (Nov 24 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148281161):
Oh! It's just like the matrix inverse isn't it! You ask magma or whatever for a proof that the element is in the ideal, it supplies an explicit linear combination claiming to prove this but which hasn't been formally verified, and then you formally verify it in Lean with the `ring` tactic.

#### [Rob Lewis (Nov 24 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148281219):
Sure, but there are upsides to implementing the algorithm natively too. Our student will learn how it works, of course. And it would be portable, so the tactic would be usable in mathlib without external dependencies. There's also theoretical interest in implementing the algorithm in non-meta Lean and proving it correct, even if it can't be efficiently executed in the kernel. And any tactic built on this should be modular enough to use an external oracle too.

#### [Johan Commelin (Nov 24 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148284554):
By the way, I think my question about `ring using [foo,bar]` was misunderstood. I didn't want it to find relations on its own. I wanted to be able to type something like
```lean
ring using [add_eq H1 H2]
```

#### [Johan Commelin (Nov 24 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148284566):
And using notation, that might be improved to `ring using [H1 + H2]`

#### [Mario Carneiro (Nov 25 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Missing%20maths%20tactic%3F/near/148296295):
that seems more reasonable. You give some linear combination of hypotheses, like `a * h1 + x^2 * h2`, and it checks that `goal - (a*h1 + x^2 * h2)` is an equality of ring expressions

