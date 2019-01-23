---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/46824Usehaveonorhypothesis.html
---

## Stream: [new members](index.html)
### Topic: [Use "have" on "or" hypothesis](46824Usehaveonorhypothesis.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135318782):
If we had a hypothesis "HX: ∀x : nat, x ^ 2 - 3 * x + 2 = 0" and wanted to prove "false", we could do so by writing "have H3 := HX 3," and then revert and do norm_num.

But "∀x : nat, x ^ 2 - 3 * x + 2 = 0" is just a way of writing "x = 0 ∨ x = 1 ∨ x = 2 ∨ ... → x ^ 2 - 3 * x + 2 = 0". If instead you had "x = 1 ∨ x = 2 ∨ x = 3 → x ^ 2 - 3 * x + 2 = 0", what is the equivalent of the "have" command?

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135319310):
This works:
```lean
example (x : ℕ) : x = 1 ∨ x = 2 ∨ x = 3 → x ^ 2 - 3 * x + 2 = 0 → false :=
begin
  intros hx H,
  exact or.elim hx (by { intro h, simp [h] at H, contradiction }) 
    (by { intro h', 
      exact or.elim h' (by { intro h, simp [h] at H, contradiction }) 
        (by { intro h, simp [h] at H, contradiction }) })
end
```
There's probably a cleaner way to do it involving pattern-matching / better use of tactics though.

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135319743):
Oh this is weird. If I import `tactic.norm_num`, the second `contradiction` above fails because after `simp [h] at H` we have `H : 2 = 0 ∧ 2 ^ 2 - 3 * 2 = 0` instead of `H : 2 + (2 ^ 2 - 3 * 2) = 0`. That's scary.

And the following gives me `no goals` by the end, but also a strange error under `example`:
```lean
import tactic.norm_num
example (x : ℕ) : x = 1 ∨ x = 2 ∨ x = 3 → x ^ 2 - 3 * x + 2 = 0 → false :=
begin
  intros hx H,
  exact or.elim hx (by { revert H, norm_num }) 
    (by { intro h', 
      exact or.elim h' (by { revert H, norm_num }) 
        (by { revert H, norm_num }) })
end
/- type mismatch at application
  eq.trans (nat.pow_eq_pow x 2) (norm_num.pow_bit0_helper x x 1 (pow_one x))
term
  norm_num.pow_bit0_helper x x 1 (pow_one x)
has type
  @eq nat (@has_pow.pow nat nat (@monoid.has_pow nat nat.monoid) x 2)
    (@has_mul.mul nat (@semigroup.to_has_mul nat (@monoid.to_semigroup nat nat.monoid)) x x)
but is expected to have type
  @eq nat (@has_pow.pow nat nat nat.has_pow x 2)
    (@has_mul.mul nat (@semigroup.to_has_mul nat (@monoid.to_semigroup nat nat.monoid)) x x) -/
```

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135319963):
```quote
This works:
```lean
example (x : ℕ) : x = 1 ∨ x = 2 ∨ x = 3 → x ^ 2 - 3 * x + 2 = 0 → false :=
begin
  intros hx H,
  exact or.elim hx (by { intro h, simp [h] at H, contradiction }) 
    (by { intro h', 
      exact or.elim h' (by { intro h, simp [h] at H, contradiction }) 
        (by { intro h, simp [h] at H, contradiction }) })
end
```
There's probably a cleaner way to do it involving pattern-matching / better use of tactics though.
```
Wait a minute -- that's not the correct goal, though. The order of associativity is wrong.

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320003):
Oops, you're right! Let me take another look.

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320004):
I'm actually confused as to how you managed to prove that statement at all -- it's not true that for *any* x, x^2 - 3x + 2 = 0 is false.

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320065):
(deleted)

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320281):
It's true that the goal `(x = 1 ∨ x = 2 ∨ x = 3 → x ^ 2 - 3 * x + 2 = 0) → false` can't be proved (I just spent an embarrassingly long time attempting it nonetheless), but as you say, that's quite different from the one I proved above, which is `x = 1 ∨ x = 2 ∨ x = 3 → (x ^ 2 - 3 * x + 2 = 0 → false)`.

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320384):
Anyways, returning to your original question, my instinct when I want to use hypotheses of the form `H : h1 ∨ h2` is to immediately start writing `exact or.elim H (by {}) (by {})` and then start filling in the curly braces. I'd be curious if more experienced members have better advice.

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320389):
You must've made a typo -- the two statements you've written are identical.

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320414):
Yes, sorry about that. I've fixed it above.

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320483):
That can't be right -- (P → Q) → false just means that P → Q is false, which is exactly right, since indeed Q is not always true when P is true. (...I'm letting P: x = 1 ∨ x = 2 ∨ x = 3 and Q : x ^ 2 - 3 * x + 2 = 0)

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320532):
On the other hand P → (Q → false) (which you proved, although I have no clue how it worked) can't be right, since that implies Q is *always* false when P is true. But this isn't right, since you can have x = 1 or x = 2, for which P is true and Q is true.

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320554):
I must be confused on something basic here, as Lean couldn't possibly accept a proof of a false statement.

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320611):
I think we should be careful with the quantifiers here. There's a (x : nat) before the statement, which is \forall x in front of everything.

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320669):
But how does that make a difference?

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320781):
You're right. That doesn't. I think I'm getting confused now too. :) Give me a minute.

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135321000):
haha, OK. I see the issue. Remember that subtraction over the nats won't do what you expect, in particular n - m when n < m gives you zero!

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135321004):
That explains the second part. Let me now put together a proof of the first part.

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135321011):
(deleted)

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135321061):
Ah, ok, I see. Changing nat to int does break things.

#### [ Kevin Buzzard (Oct 06 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135322325):
It's still true that `3 ^ 2 - 3 * 3 + 2 = 0` is false in `nat`, even though subtraction is not the mathematics subtraction on nat.

#### [ Chris Hughes (Oct 06 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135322374):
(deleted)

#### [ Kevin Buzzard (Oct 06 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135322375):
I guess you should be proving `example : ¬ (∀ x, x = 1 ∨ x = 2 ∨ x = 3 → x ^ 2 - 3 * x + 2 = 0) := sorry`

#### [ Kevin Buzzard (Oct 06 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135322383):
The way to think about it is that if something is directly before the colon, you can move it to the right but you then have to add a universal quantifier. I agree that these things are confusing!

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135323812):
Consider the following:
```lean
example (x : ℕ) : (x = 1 ∨ x = 2 ∨ x = 3 → x ^ 2 - 3 * x + 2 = 0) := sorry
example (x : ℕ) : (x = 1 ∨ x = 2 ∨ x = 3 → x ^ 2 - 3 * x + 2 = 0) → false := sorry
```
As Kevin says, the stuff to the left of the colon corresponds to a forall quantifier. One thing to keep in mind is that with the forall quantifiers there, these expressions are closely related to certain Prop-valued functions (predicates) over the nats. The first predicate (λ x, x = 1 ∨ x = 2 ∨ x = 3 → x ^ 2 - 3 * x + 2 = 0) happens to be false for every nat, so we have finally:
```lean
example : (∀ x, x = 1 ∨ x = 2 ∨ x = 3 → x ^ 2 - 3 * x + 2 = 0) → false := 
begin
  intro h,
  replace h := h 1 (or.inl rfl), 
  contradiction
end
```
The predicate corresponding to the second one (λ x, (x = 1 ∨ x = 2 ∨ x = 3 → x ^ 2 - 3 * x + 2 = 0) → false) is sometimes true and sometimes false. In particular it's true when x=1, x=2, x=3 but false everywhere else. The Prop version of this (∀x, (x = 1 ∨ x = 2 ∨ x = 3 → x ^ 2 - 3 * x + 2 = 0) → false) then should be false, so 
```lean
example : (∀ x, (x = 1 ∨ x = 2 ∨ x = 3 → x ^ 2 - 3 * x + 2 = 0) → false) → false:=
begin
  intro H,
  replace H := H 0,
  simp at H,
  exact H (by { intro h, exact or.elim h (by contradiction) (by contradiction) })
end
```

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135324682):
Thanks -- that makes sense. And although the notation you gave (`replace h := h 1 (or.inl rfl),`) doesn't seem to be working, I guess just adding the forall x allows one to use the `have` command normally, i.e. as `have h3 := h 3,`

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135324850):
Sorry for all the edits! Thinking about this definitely cleared up a lot of confusion on my end. Hopefully it's all right now.

`replace` only works in tactic mode, so if you're using term mode, you'll have to do what you did with `have`.

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325128):
Tactic mode just means enclosed by `begin` and `end`, right? `replace` doesn't seem to be working for me in tactic mode either. I'm using the web editor, does that affect things?

#### [ Kenny Lau (Oct 06 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325137):
you need to `import tactic.interactive`

#### [ Kevin Buzzard (Oct 06 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325174):
Yes, tactic mode is anything with in a `begin/.../end` or `by {...}`.

#### [ Kevin Buzzard (Oct 06 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325183):
Aah, `replace` is a mathlib tactic?

#### [ Kevin Buzzard (Oct 06 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325192):
If you have `norm_num` imported then these basic tactic imports will come too I guess.

#### [ Patrick Massot (Oct 06 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325199):
Congratulations to both of you: you went through a very important Lean initiatory ritual, where the initiate becomes utterly confused, loses all confidence in his or her most elementary mathematical skills. You met ℕ substraction!

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325204):
```quote
you need to `import tactic.interactive`
```
Oh, thanks, works.

#### [ Kevin Buzzard (Oct 06 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325208):
@**Abhimanyu Pallavi Sudhir** the lean web editor is horrible! Are you using Lean on a computer you own, or a computer at Imperial?

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325261):
```quote
@**Abhimanyu Pallavi Sudhir** the lean web editor is horrible! Are you using Lean on a computer you own, or a computer at Imperial?
```
My own computer. It (the web editor) seems to be okay for basic proofs, though.

#### [ Kevin Buzzard (Oct 06 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325271):
What OS?

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325275):
Windows.

#### [ Kevin Buzzard (Oct 06 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325281):
Patrick -- that logic stuff is super-confusing, and broken `-` makes things worse :-)

#### [ Kenny Lau (Oct 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325335):
```quote
Windows.
```
install a linux VM

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325337):
I do have a Linux VM (Ubuntu, if that still counts). It's just really slow.

#### [ Kevin Buzzard (Oct 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325338):
Win10 or 7?

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325339):
Win 10.

#### [ Kevin Buzzard (Oct 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325341):
OK I have a cheap way of installing Lean on your PC

#### [ Kenny Lau (Oct 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325346):
```quote
I do have a Linux VM. It's just really slow.
```
it was a joke

#### [ Kevin Buzzard (Oct 06 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325357):
For Sage they used to recommend that peolpe on Windows just ran it in a Linux VM

#### [ Kevin Buzzard (Oct 06 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325364):
(deleted)

#### [ Kevin Buzzard (Oct 06 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325366):
wait that won't work for you

#### [ Chris Hughes (Oct 06 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325368):
Scott's new method should work, provided there are no spaces in your username.

#### [ Kevin Buzzard (Oct 06 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325413):
https://xenaproject.wordpress.com/getting-lean-and-mathlib-running-in-the-mlc/

#### [ Kevin Buzzard (Oct 06 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325415):
That way is super-cheap and needs no git or command line.

#### [ Kevin Buzzard (Oct 06 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325419):
However Scott's method is much better, because it will enable you to upgrade properly.

#### [ Kenny Lau (Oct 06 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325428):
https://gist.github.com/kckennylau/611cc453c67df074ad492b4939ddd356

#### [ Kenny Lau (Oct 06 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325430):
this is the one that I use

#### [ Kenny Lau (Oct 06 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325433):
but they don't really recommend this

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325546):
Oh ok. I'll try the cheap way for now -- I'll just re-install the updated versions manually.

#### [ Kevin Buzzard (Oct 07 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135327522):
```quote
this is the one that I use
```
Kenny, that involves compiling Lean. What's the point of doing that now? Lean has been stable for ages, you can just take the binary.

#### [ Kenny Lau (Oct 07 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135327573):
I see

#### [ Kevin Buzzard (Oct 07 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135329837):
@**Abhimanyu Pallavi Sudhir** the way dependent type theory works is that it prefers  functions to be defined everywhere and just give junk values at places mathematicians would not normally evaluate them, and it also wants things like `-` to go from $$X\times X$$ to $$X$$, for varying $$X$$ (see around 300 lines in in `core.lean` in the core lean library -- `class has_sub      (α : Type u) := (sub : α → α → α)` and `class has_div      (α : Type u) := (div : α → α → α)` ). This means that subtraction on `nat` has to take two nats and give back a `nat` (hence `2 - 3 = 0`) and division on, say, the reals, has to take two reals and give back a real, hence `1 / 0 = 0`. This isn't a logical problem -- they have just artificially extended these functions to places where mathematicians would not normally use them; I think of `-` and `/` as being "computer science versions" of these operators, and in the statements of theorems I care about, if either of them are used then I have to do a little check to make sure that the results imply what I want them to say. Of course it doens't matter in the proofs -- you would not object if a mathematician defined a new function `f(x,y)` to be `x/y` if `y` was non-zero but `0` if `y` was zero and then used `f` in proofs; that's all that's happening here. Subtraction is particularly horrible because at least division gives the same weird answer in all cases; the behaviour of subtraction actually changes if you move from `nat` (where it's weird) to `int` (where it's normal).

#### [ Andrew Ashworth (Oct 07 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135330196):
:grinning: Could be worse. With computers, `((0 : uint32_t) - 1) = 4294967295`.

#### [ Kevin Buzzard (Oct 07 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135330204):
so Lean's convention is actually closer in this case ;-)

#### [ Scott Olson (Oct 07 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135335803):
I'd argue it's quite natural to define versions of functions like `nat.sub` or division that restrict their domain (either by type or dependent hypothesis argument) rather than returning "junk" values, but it depends on the use case. For example, it's quite nice that `nat.sub` *precisely* matches the structure of `list.drop`, so you can prove things like `list.drop n (list.repeat a m) = list.repeat a (m - n)`.

But you could look at Idris for example where the total division function has type `Nat -> (y : Nat) -> Not (y = Z) -> Nat`, or look at `List.head : (l : List a) -> {auto ok : NonEmpty l} -> a` as opposed to Lean's `list.head : Π {α} [inhabited α], list α → α`.

On the other hand, both Lean and Idris have a `head' : list α → option α` alternative which is the preferred API in non-dependent modern programming languages, since you can chain convenient methods on the resulting `option` to deal with the error case in different ways.

#### [ Scott Olson (Oct 07 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135336120):
Though as @**Kevin Buzzard** pointed out, the interface the operator typeclasses have in Lean would get in the way of doing anything like this for the normal subtraction or division syntax.

#### [ Kevin Buzzard (Oct 07 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135342844):
I've long been convinced that Lean's approach is the simplest -- but Abhi is a new student at Imperial and I'd not mentioned this stuff to the students yet, and for a mathematician the convention is quite disconcerting and unexpected. As I pointed out recently, mathematicians expect to divide the integer 1 by the integer 2 and get the rational `1/2` because that's what happens with all the standard maths packages. I recently mentioned a possible typeclass trick which might let us emulate that here but it would need a lot of testing until we got it right.

#### [ Abhimanyu Pallavi Sudhir (Oct 07 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135345234):
```quote
@**Abhimanyu Pallavi Sudhir** the way dependent type theory works is that it prefers  functions to be defined everywhere and just give junk values at places mathematicians would not normally evaluate them... the behaviour of subtraction actually changes if you move from nat (where it's weird) to int (where it's normal).
```
Yeah, I get that -- although I'm not sure why this is better than just defining an object called "undefined" (as javascript does it with 1/0, for instance).

#### [ Kenny Lau (Oct 07 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135345376):
then the codomain wouldn't be N anymore

#### [ Kenny Lau (Oct 07 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135345377):
I'm not sure if javascript functions care about whether its codomain includes `undefined`

#### [ Scott Olson (Oct 07 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135345429):
In a typed setting, the equivalent of that approach is to return `option nat` as in one of my examples above. I've seen almost no one ever do this for division, though

#### [ Mario Carneiro (Oct 07 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135345683):
This is an option. I think there is actually a function `nat.psub` that implements this

#### [ Mario Carneiro (Oct 07 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135345726):
These sorts of functions often go by the name e.g. "safe division"

#### [ Scott Olson (Oct 07 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135345872):
I think part of the argument for just using a junk value is that proofs about division like `div_self : a ≠ 0 → a / a = 1` will need to include the precondition `a ≠ 0` regardless of which definition for division you choose, and so you might as well pick a simple one.

It would be more controversial to define nat/integer division the Lean way for general purpose programming, but even that has been done

#### [ Kevin Buzzard (Oct 07 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135346494):
The point simply seems to be that whilst there are several methods for "fixing the problem" (as mathematicians would interpret it), all the ones I've tried seem to result in the "problem being fixed", the functions now being more of a pain to use in practice, and then the dawning realisation that actually...was this ever really a problem? Or was it just a psychological issue? There is no foundational logical issue -- the computer scientists are just using  a different function from mathematician's division, and calling it the same name. Mathematicians just need to be aware that these are not the functions they're used to, that the function they're used to can easily be constructed, but do they really *need* the functions they're used to? I'm not convinced they do.

#### [ Kevin Buzzard (Oct 07 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135346514):
What they need instead is to be educated that the CS functions are different and to be aware of this.


{% endraw %}
