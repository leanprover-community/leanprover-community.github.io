---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66348natint.html
---

## Stream: [general](index.html)
### Topic: [nat = int](66348natint.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 09 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492419):
Is `nat = int` consistent with Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492660):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492670):
but it will make the VM not like you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 09 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492671):
good lord

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 09 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492701):
so how can a constructor of an inductive type construct itself...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492733):
Equality of types is terrifying. I just stick to equality of terms.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492747):
```
axiom nat_eq_int : nat = int

#eval cast nat_eq_int.symm (-5) -- 2147483643
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492754):
I am not sure I have a good feeling as to what equality of types means.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492774):
`equiv` of types -- that I understand.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492840):
Unfortunately, as a cast off from HoTT, univalence is consistent in some weak forms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135492856):
but the VM assumes something much stricter, in order for type erasure to be sound

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493250):
So an interesting thing happened in my lecture today. It was an interactive lecture and the students could vote on the questions I was asking, on their phones. And I asked them if "not P" was equal to "P implies false" and a lot of them said that these things were not equal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 09 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493310):
I'm not surprised

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 09 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493313):
Did you teach them the truth table definition of implies?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493317):
But they were all happy that these things were equivalent. I didn't tell them Lean's definition of "not P", I was doing basic propositional calculus, so the definition of "not" was "not false = true" and "not true = false" and that's it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 09 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493324):
Did you try on a room full of professional mathematicians next?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493335):
But this is somehow the same issue.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493352):
Two propositions can be equivalent, but it's a bit weird saying they are equal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493360):
Especially when I told them that 2+2=4 and Fermat's Last Theorem were both true, and asked them if they thought that they were hence equal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493365):
aha, here's an example of a lie proposition from that axiom:
```
axiom nat_eq_int : nat = int
def lie : bool := cast nat_eq_int.symm (-int.of_nat (2^31)) < 0
theorem not_lying : lie = ff := rfl
#eval lie -- tt
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493376):
This is bad because you can make the VM crash

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493426):
That's not bad -- that just means that you shouldn't rely on the VM

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493428):
If the kernel's happy, I'm happy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 09 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493435):
It means you shouldn't introduce axioms and then rely on the VM.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 09 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493446):
But you shouldn't introduce axioms and rely on the kernel either. So I don't think that's a problem.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493448):
it means that some axioms are consistent with the VM and others aren't, even if they are consistent with lean itself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493466):
Mario do you _know_ that nat = int is consistent with Lean (assuming maths is consistent etc)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493513):
I have strong evidence in the direction of a proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493517):
Fair enough.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493521):
the more general statement is that two types with the same cardinality are consistently equal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493532):
Aah I see equiv has popped up again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 09 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493547):
maybe we should add that as an axiom

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 09 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493553):
just like how we added propext as an axiom

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493557):
But type erasure, used in the VM, assumes that the only provable equalities are between objects with the same runtime representation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493564):
Is `forall X Y : Type, equiv X Y iff X = Y` consistent with Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493569):
which has to do with the other thread

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 09 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493573):
`Type u` even

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 09 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493577):
It doesn't type check

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493622):
oh yeah

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 09 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493633):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493636):
nonempty (equiv X Y) iff X = Y or whatever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 09 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493641):
use `\to`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493676):
You have to be careful not to run afoul of the counterexample to HoTT

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493788):
Consider the `bnot : bool -> bool` function, which swaps the two values. This is provably an equivalence in HoTT, so from univalence we get an equality `ua bnot : bool = bool`. It is provable in HoTT that `cast (ua bnot) tt = ff`, but `cast rfl tt = tt` and hence `ua bnot != rfl`, contradicting proof irrelevance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 09 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493870):
but you can't prove in lean that `cast (ua bnot) tt = ff` right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493930):
In HoTT, this is provable because we know `ua` is the inverse of the natural function `A = B -> A ~= B`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493990):
@**Patrick Massot** this should sort out your `heq` problems:

```lean
import data.equiv.basic
axiom for_patrick : ∀ (X Y : Type*), equiv X Y → X = Y
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135493999):
and apparently Mario thinks it's consistent, but just be careful with the VM OK?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494020):
I strongly recommend against any axioms that don't obey type erasure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 09 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494022):
I don't think it helps. Patrick knows his Types are equal, he just can't `rw` using that equality.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 09 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494056):
We all want the same tactic: `rw_that_just_works`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494119):
this is a difficult research question

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494128):
the problem is always type dependency

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 09 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494130):
What is type erasure?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494140):
```quote
this is a difficult research question
```
Mathematicians can do it in their heads!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 09 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494184):
Then do you have example where all those `subst` or `generalize` tricks works? I haven't been able to find any math example

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494327):
https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/Continuous.20Functions.20Preserve.20Limits/near/134675116

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494366):
Rohan wanted to prove that if $$x_0,x_1,x_2...$$ tended to $$x$$ then $$x_1,x_2,x_3,...$$ also tended to $$x$$. We formalised the change of variables using filters and then Kenny proved it using `subst`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494504):
the solution of course is extensional type theory but I might be contractually obligated to say that's silly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Oct 09 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494641):
was OTT (https://github.com/leanprover/lean/issues/654) no good?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 09 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135494975):
One thing I've wondered for a while is why does this work?
```lean
example : (0 : ℕ) = eq.rec 0 (classical.choice ⟨eq.refl ℕ⟩) := rfl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135495482):
there is a kernel reduction rule `eq.rec e h ~> e` when `h : a = a`. Intuitively this is justified by using proof irrelevance to replace `h` with `rfl` and then iota reducing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135495777):
Chris it looks like it's about time you learn C++

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135495803):
or type theory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 09 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135496147):
Kevin means learning type theory by reading C++ code of the Lean kernel

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 09 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135496158):
That's the proper way for brave men

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135496744):
I should note that I have written a paper on this topic and I still haven't fully understood the kernel of lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat%20%3D%20int/near/135496776):
it is much easier to read the reference typecheckers like trepplein


{% endraw %}
