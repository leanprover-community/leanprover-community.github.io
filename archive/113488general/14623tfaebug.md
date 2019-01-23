---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/14623tfaebug.html
---

## Stream: [general](index.html)
### Topic: [tfae bug](14623tfaebug.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238104):
Minimized from the open maps thread:
```lean
example (α : Type) (P Q R : α → Prop) : tfae [∀ x, P x, ∀ x, Q x, ∀ x, R x] :=
begin
  tfae_have : 1 → 3, by sorry,
  tfae_have : 3 → 1, by sorry, 
  tfae_have : 3 ↔ 2, by sorry,
  tfae_finish,
end
```
fails with: `exact tactic failed, type mismatch, given expression has type
  (∀ (x : α), Q x) ↔ ∀ (x : α), R x
but is expected to have type
  (∀ (x : α), Q x) ↔ ∀ (x : α), P x`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 05 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238243):
I'm on it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238244):
Note that removing the forall hides the issue

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 05 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238255):
Does it? That's odd

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238366):
maybe not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238370):
I changed many times what I tried

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238381):
And also, undo in VScode vim extension is completely crazy, you never know how many steps you will go back

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238463):
Wow, I see completely random behavior

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238466):
I have a series of test cases, restarting Lean server changes the set of failing tests randomly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238471):
Heisenbugs!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238534):
A Heisenbug in a theorem prover — the irony

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238543):
My test file is 
```lean
import tactic.tfae

example (P Q R : Prop) : tfae [P, Q, R] :=
begin
  tfae_have : 1 → 2, by sorry,
  tfae_have : 2 → 1, by sorry, 
  tfae_have : 3 ↔ 1, by sorry,
  tfae_finish,
end
example (P Q R : Prop) : tfae [P, Q, R] :=
begin
  tfae_have : 1 → 2, by sorry,
  tfae_have : 2 → 1, by sorry, 
  tfae_have : 1 ↔ 3, by sorry,
  tfae_finish,
end 
example (α : Type) (P Q R : α → Prop) : tfae [∀ x, P x, ∀ x, Q x, ∀ x, R x] :=
begin
  tfae_have : 1 → 2, by sorry,
  tfae_have : 2 → 1, by sorry, 
  tfae_have : 1 ↔ 3, by sorry,
  tfae_finish,
end
example (α : Type) (P Q R : α → Prop) : tfae [∀ x, P x, ∀ x, Q x, ∀ x, R x] :=
begin
  tfae_have : 1 → 2, by sorry,
  tfae_have : 2 → 1, by sorry, 
  tfae_have : 3 ↔ 1, by sorry,
  tfae_finish,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238549):
Creating and deleting a line between two examples also changes what works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238607):
Can anyone see that, or is it only my computer going crazy?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238615):
I can reproduce

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238624):
Creating and deleting lines changes what works *nondeterministically*.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238683):
I guess meta-land allows non-deterministic algorithms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 05 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238704):
I don't get non-deterministic behavior with that code. I'm in emacs.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238712):
Right... we need a tactic that will first toss a coin to decide if it will actually help you :upside_down:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 05 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238720):
I have such tactics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238739):
we see that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238742):
@**Simon Hudon** Do you get any errors at all with that code (apart from the sorries)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 05 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238744):
Yes, it fails deterministically

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 05 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238787):
@**Patrick Massot** I'll remember that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 05 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238799):
```quote
And also, undo in VScode vim extension is completely crazy, you never know how many steps you will go back
```
This annoys me to no end as well. However it seems that VS code's built-in undo (cmd+z on mac, ctrl+z on other systems) works independently and seems to function properly.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 05 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135239970):
Ok now I see the non deterministic behavior. That looks weird. I think it's because some vertices are being ignored and because they are stored in a hash table and their hash code probably depends on the memory address of the expressions which changes from run to run.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240044):
is this because of `ref`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 05 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240047):
I don't think so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 05 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240076):
I'm only using `expr` as a key in hash tables

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240138):
In the mean time, I'd like to sorry this `tfae` and move on. How to you actually use a `tfae` statement? I don't see anything in the docs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 05 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240208):
That's a correct use of tfae.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 05 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240212):
`tfae.out` is probably what you want. It's mentioned obliquely in the docs: "In `data/list/basic.lean`there are propositions of the form..."

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240221):
you state follow up equivalences you are interested in and refer to the elements of the list by their index

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240260):
and use those numbers in `tfae.out`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 05 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240283):
With one added oddity: the indices are `1 ≤ i ≤ xs.length` rather than `0 ≤ i < xs.length`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240585):
I can't use it, probably because of parameters. Compare:
```lean
import tactic.tfae
open list
constants (α : Type) (P Q R : α → Prop)

lemma eqv (x : α) : P x ↔ Q x :=
sorry

example (x : α) (h : P x) : P x :=
begin
  rw eqv at *, 
  assumption
end

lemma eqvs (x : α): tfae [P x, Q x, R x] :=
sorry

example (x : α) (h : P x) : P x :=
begin
  rw tfae.out (eqvs ) 1 2, 
  assumption
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 05 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240708):
Sorry, my comment was misleading: the indices start at 1 in the proof, not when you use the theorem.

Now that I'm saying, I think we should remove that oddity.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240728):
Can you fix my example above?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 05 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240741):
` rw tfae.out (eqvs ) 0 1,`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240789):
doesn't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 05 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240802):
What error do you get?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241134):
Sorry I wasn't clear. You can't use it directly as a rewrite rule, you have to restate the theorem and prove it by `tfae.out`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 05 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241156):
```
theorem eqvs_PQ (x : α) : P x ↔ Q x := (eqvs x).out 0 1
theorem eqvs_PR (x : α) : P x ↔ R x := (eqvs x).out 0 2
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241387):
Thanks. It's somehow disappointing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241396):
Arg, I'm super late

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241466):
Oooh, that's disappointing indeed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241610):
Would something like `erw` be able to deal with this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 05 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241679):
What if you could do: `from_tfae h : eqvs 0 1` first to add an assumption `h` with the right equivalence?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241704):
We need a `rw` on steroids. One that will use more power to do the job. Like `simp` it should dive into binders etc, so that we no longer need to do the `conv` dance. And it should also unpack this stuff from `tfae.out` so that it can just use it to `rw`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241728):
@**Simon Hudon** Yes, you could just do `have : P → Q := tfae.out 0 1` and then `rw this`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241732):
But it is too verbose.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241794):
Yes. It's confusing... mathematicians keep complaining that proofs are too compact and unreadable in term mode. Otoh we love the brevity of informal maths...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 06 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135317699):
```quote
```quote
And also, undo in VScode vim extension is completely crazy, you never know how many steps you will go back
```
This annoys me to no end as well. However it seems that VS code's built-in undo (cmd+z on mac, ctrl+z on other systems) works independently and seems to function properly.
```
@**Bryan Gin-ge Chen**  Gabriel just told me to use the trick described in https://github.com/VSCodeVim/Vim/issues/1490#issuecomment-352167221

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 18 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/147925497):
@**Simon Hudon** How are things going with `tfae`? Is there something blocking progress? I'm currently stating 5 equivalent conditions for a presheaf to be a sheaf. I think `tfae` could increase the user experience :smiley:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Nov 18 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/147925626):
I haven't fixed the bug yet, I was under the impression that it didn't always manifest and tfae has been merged so you should be able to use it and cross your fingers.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 19 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/147998398):
I can still see the bug using the latest mathlib.
```lean
import tactic.tfae

example (P Q R : Prop) : tfae [P, Q, R] :=
begin
  tfae_have : 1 → 2, by sorry,
  tfae_have : 2 → 1, by sorry,
  tfae_have : 3 ↔ 1, by sorry,
  tfae_finish,
end
```
doesn't work here

