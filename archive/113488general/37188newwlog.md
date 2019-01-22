---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37188newwlog.html
---

## [general](index.html)
### [new wlog](37188newwlog.html)

#### [Patrick Massot (May 28 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127197261):
Johannes, I'm sorry I didn't properly follow the new wlog discussion, I've been caught by real world. But I really think like it's less powerful than Simon's version. Today I noticed that it doesn't  even try `assumption` to discharge auxiliary goals.

#### [Patrick Massot (May 28 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127197327):
for instance (I know this is already proven much more efficiently in mathlib, but I was testing stuff):
```lean
open set
example (X : Type) (A B C : set X) : A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) :=
begin
  ext x,
  split,
  { intro hyp,
    cases hyp,
    wlog x_in : x ∈ B using B C,
    { assumption },
    { exact or.inl ⟨hyp_left, x_in⟩ },
    { simpa [union_comm] using this } },
  { intro hyp,
    wlog x_in : x ∈ A ∩ B using B C,
    { assumption },
    { exact ⟨x_in.left, or.inl x_in.right⟩ },   
    { simpa [union_comm] using this } }
end
```

#### [Johannes Hölzl (May 28 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127197530):
Instead of using `assumption` to solve it you can use the new `:=` syntax:
```lean
wlog x_in := hyp using B C
```
did you try this?

#### [Patrick Massot (May 28 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127197635):
It doesn't seem to do anything

#### [Johannes Hölzl (May 28 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127198551):
My current assumption is that the hypothesis has syntactically the shape `p x ∨ q x`. I guess I need to unfold the type of the hypothesis.

#### [Patrick Massot (May 28 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127200877):
I don't know if unfolding is always a good move here, but it could attempted if discharging fails without unfolding (backtracking if unfolding also fails)

#### [Johannes Hölzl (May 28 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127203639):
The discharger is only used for the permuation cases, i.e. all `p x y z -> p y z x` etc (in your case this is the 3rd goal).
`wlog` now assumes that you eithr explicitly state the disjunction, or your proof it afterwards.

#### [Patrick Massot (May 28 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127203890):
I still don't understand how to use the `:=` syntax of `wlog`

#### [Patrick Massot (May 28 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127203996):
And I still haven't met a case where I'm not using the `wlog` as `wlog ... with ..., { finish }, { actual work }, { finish }`

#### [Johannes Hölzl (May 28 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127204823):
The `wlog n := H` syntax tells `wlog` that `H` is a proof of `p x y \or p y x` (the disjunction which tells us that we only need to look at these two cases). What are your cases you do `wlog` on?

#### [Patrick Massot (May 28 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127204999):
Can you do the set theoretic example above for instance?

#### [Johannes Hölzl (May 28 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205163):
I added them to the test cases in mathlib:
```lean
example (X : Type) (A B C : set X) : A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) :=
begin
  ext x,
  split,
  { intro hyp,
    cases hyp,
    wlog x_in : x ∈ B := hyp_right using B C,
    { exact or.inl ⟨hyp_left, x_in⟩ }, },
  { intro hyp,
    wlog x_in : x ∈ A ∩ B := hyp using B C,
    { exact ⟨x_in.left, or.inl x_in.right⟩ } }
end
```
The permutation proof is now done using the SMT framework, which seams to work better on these examples.  But sometimes they don't work and I'm not sure yet why not.

#### [Johannes Hölzl (May 28 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205187):
You can also write
```lean
example (X : Type) (A B C : set X) : A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) :=
begin
  ext x,
  split,
  { intro hyp,
    wlog x_in : x ∈ B := hyp.2 using B C,
    { exact or.inl ⟨hyp.1, x_in⟩ }, },
  { intro hyp,
    wlog x_in : x ∈ A ∩ B := hyp using B C,
    { exact ⟨x_in.left, or.inl x_in.right⟩ } }
end
```
It's not necessary that you perform the `cases hyp` in the first case.

#### [Patrick Massot (May 28 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205270):
Thanks! Is this meant to work with current mathlib?

#### [Patrick Massot (May 28 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205298):
Lean complains `Cases contains variables not declared in `using x y z` `

#### [Johannes Hölzl (May 28 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205315):
Just a second I fixed some problems with supporting `_ ∪ _ `

#### [Patrick Massot (May 28 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205324):
There is no hurry

#### [Johannes Hölzl (May 28 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205382):
There is still a strange bug: sometimes the SMT framework solves the permutation problem, in other, nearly equivalent cases it doesn't...

#### [Patrick Massot (May 28 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205452):
Isn't part of the reason why this SMT stuff is dying?

#### [Johannes Hölzl (May 28 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205637):
In Lean 3 SMT is still alive :-) We will see what happens in Lean 4. At some point we might want to have a specialized permutation prover which applies symmetry and AC laws.

#### [Patrick Massot (May 28 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205777):
Maybe we should use Assia's return here. @**Assia Mahboubi** did you notice https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/without.20loss.20of.20advertisement/near/125491146, https://github.com/leanprover/mathlib/pull/135 and the curren thread?

#### [Patrick Massot (May 28 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205786):
Does it look like what you use in Coq?

#### [Johannes Hölzl (May 28 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127206160):
I just pushed a couple of fixes w.r.t. to the discharger and the handling of `_ ∪ _`.

#### [Johannes Hölzl (May 28 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127206255):
the `wlog` tactic in ssreflect is quiet different from Lean's. In ssreflect the `wlog` tactic introduces  cut, and can be used to generalize some terms. While in Lean it is used to handle do permutations of variables.

#### [Assia Mahboubi (May 28 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127207476):
Hi @**Patrick Massot** , I was not able to find a precise documentation of the wlog tactic following the links you gave, did I miss something? I must confess that I am starting to have trouble reading Lean code without executing it so it's harder to answer... But from what I could see, @**Johannes Hölzl** is right, Lean's ``wlog`` seems a bit different from Coq's ``wlog``.  Can you describe the behaviour of it? Doesn't it generate a cut in the proof (even if not exposed to the user)? Apologize  in advance if I missed the doc.
Incidentally, there is an even older (2009 I think) paper by John Harrison on ``wlog`` reasoning in proof assistants: https://www.cl.cam.ac.uk/~jrh13/papers/wlog.pdf

#### [Patrick Massot (May 28 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127207495):
Johannes's version is documented at https://github.com/leanprover/mathlib/blob/fe7d5738417aeaf835790af2101b98d1758ad8fe/tactic/wlog.lean#L107

#### [Assia Mahboubi (May 28 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127207504):
But I liked the layout of the script of ``fundamental``,  I agree that it should not be longer than that.

#### [Patrick Massot (May 28 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127207508):
I think the first messages of https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without.20loss.20of.20advertisement should also be a rather good documentation

#### [Assia Mahboubi (May 28 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127207594):
Hmm, this is what I read first and it wasn't enough in my case.

#### [Patrick Massot (May 28 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127207654):
I have no idea how it works. It's like in the mathematician dream: we think in our way and the computer understands without us needing to understand how the computer understands

#### [Patrick Massot (May 28 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127207663):
Of course when it fails you get frustration crises like with Kevin has today

#### [Assia Mahboubi (May 28 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127208541):
Ok so now I have read @**Johannes Hölzl** , very clear description. So my understanding is that Coq's version is a more general, lower-level building block, and what Johannes describes is a special case, well suited to symmetry arguments and with a nicer syntax. Then Simon seems to bring a very useful layer of automation on top of it. To use the same example as Johannes', in Coq writing
``wlog hnm : n m / n <= m => [h | ]``
when the current state of the proof is (n m : N)  |- p n m
makes the situation become:
(n m : N) (hnm : n <= m) |- p n m  (i)
and 
(n m : N) (h : forall k l, k <= l -> p k l) |- p n m (ii)

(i) is probably the main part of your proof and (ii) should be quite straightforward. But Johannes' version hard-codes the assumption that (ii) will be proved from the fact that (n <= m) \/ (m <= n), when Coq does not.

#### [Johannes Hölzl (May 28 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127208979):
My idea of `wlog` was to have a generalized version  of John Harrisons `wlog` to an arbitrary list of variables and cases. But ssreflect's version is a nice building block! @**Assia Mahboubi** how do you handle the case when your permutation has more than two cases? For example `a < b < c \/ a < c < b \/ b < a < c \/ b < c < a \/ c < a < b \/ c < b < a` do you need to iterate `wlog`?

#### [Assia Mahboubi (May 28 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127209436):
Hi @**Johannes Hölzl**. Correct me if I misunderstand your question. But if I am correct, then no, there is a single ``wlog``, and the main branch of the proof is (1). Then in order to proof (ii), you will need to prove first that your big disjunction holds, and then proceed by case analysis on this big disjunction and used hypothesis ``h`` in each case. The only difference I see here is that you have a nice syntax to generate the big disjunction, which is a cut in the proof (ii). This is why I described your implementation as a specialization of Coq's ``wlog``, which on the other hand deals with ``wlog`` arguments that may not rely on this kind of properties of the relation.

#### [Johannes Hölzl (May 28 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127209700):
Ah, thanks for the clarification! And I agree that Coq's `wlog` is more general.

