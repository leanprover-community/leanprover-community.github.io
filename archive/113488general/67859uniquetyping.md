---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67859uniquetyping.html
---

## Stream: [general](index.html)
### Topic: [unique typing](67859uniquetyping.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 15 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123746502):
Success! I managed to finally show that Lean's full type system has unique typing (which implies stuff like it is impossible to prove `Type 0 : Type 0`), even if you use "full" definitional equality, i.e. the transitive and undecidable ideal version of what lean checks. Since it uses a reduction that is guaranteed to run forever on subsingleton eliminators like `acc`, it yields an alternative semi-decision procedure for testing definitional equality.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 15 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123747869):
Any chance it's a Lean proof?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 15 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123747919):
Good one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 15 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123748037):
No, it's still in the informal stage, although the proof is sufficiently subtle that it might be a good idea to formalize it just to make sure it all actually works as advertised.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 15 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123748094):
Wouldn't a Lean formalization be self-referential?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 15 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123748257):
Sure, but it wouldn't be the first time a proof assistant has proven parts of itself. Also unique typing is weaker than soundness - even if the type system is inconsistent there are many things that can't be defeq. I did not need to assume any inaccessible cardinals in the proof, it's a purely syntactic proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 15 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123748490):
I guess even if self-referential, it might be a good way to find errors. You might want to write it in Isabelle (or something else) if you want to avoid the self-referential criticism but even Lean would help get the details right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 15 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123752285):
Does your work shed any light on whether it is possible to make Lean's definitional equality "better" whilst still remaining decidable? Actually here is an even dumber question. Is the transitive closure of Lean's definitional equality still decidable? One's first thought is "of course not, if you want to prove `x=y` by finding `z` such that `x=z` and `z=y` then where do you start?", but if transitivity somehow only fails in some controlled way then perhaps there is some algorithm which spits out sensible choices for `z`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Mar 15 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123752298):
> Is the transitive closure of Lean's definitional equality still decidable?

No.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 15 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123752351):
This doesn't surprise me at all. How does one go about proving this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Mar 15 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123752355):
It's the standard interaction between subsingleton elimination (in particular `acc.rec`) and proof irrelevancy.  See also https://leanprover.github.io/reference/expressions.html#computation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Mar 15 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123752490):
The trick is that 1) you can encode functions with unbounded recursion using well-founded recursion (where the proof is e.g. exfalso), 2) you can evaluate such functions as many steps as you have nested `acc.intro`s, 3) by proof irrelevancy all such `acc.intro` terms are definitionally equal.  You can for example now ask whether the original function returns `0` when given `0` using a definitional equality test, and this problem is undecidable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 15 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123752623):
Thanks for the added information. This will greatly decrease the amount of time it will take to me to understand your previous comment :-) I'm sure this is standard DTT stuff but I am still a beginner. Thanks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 15 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123752686):
Aah so in fact this seems to be exactly the trick used to show that defeq isn't transitive in the reference manual. I have never taken the time to understand that proof before -- I just verified that it worked and moved on. I think that at the time I knew so little Lean that it just looked too daunting to get to the bottom of.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 15 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123767735):
> Does your work shed any light on whether it is possible to make Lean's definitional equality "better" whilst still remaining decidable?

The proof does a good job of pointing the finger squarely at subsingleton eliminators. That is, if there were no inductive types such that:
* The inductive type is a Prop family
* The inductive type has one constructor
* The constructor has at least one non-prop argument
* The constructor has at least one recursive argument
* All non-prop arguments appear in the output type

then definitional equality would be decidable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 15 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123767813):
Probably the same can be said about proof irrelevance, but that's baked in a bit more thoroughly, so it's less obvious how it would change the proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 15 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123768875):
i was searching "subsingleton elimination" and one of the top results was this: https://www.cs.cmu.edu/~cangiuli/sigbovik/unintentional.pdf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 15 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123768881):
not totally related but possibly humorous

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 15 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123768927):
Oh, I was wrong about needing at least one non-prop argument. Here's an extremely simple type, simpler than `acc`, that also causes the same problems (non-transitivity, undecidability)
```
inductive T : Prop
| mk : T → T

variables (x : T) {α : Sort*} (f : α → α)
def fix : α := T.rec (λ _, f) x
example : fix x f = f (fix x f) :=
show fix (T.mk x) f = f (fix x f), from rfl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 15 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123770686):
You have a variable of type `T` but I am not sure it's possible to construct anything of type T. 
```
variable y : false
example : false := y
```
This has caused a lot more trouble than undecidability. I don't really understand what you're saying yet but I am still optimistic it's within my grasp. You seem to have proved that every function has a fixed point, given a variable of type `T`, a type for which there are no instances. What does this have to do with non-transitivity and undecidability? Sorry if this is all standard.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 15 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771207):
That's correct - I didn't mention it but `(x : T)` is an inconsistent context. `fix` is also inconsistent, but from a soundness perspective that's no surprise, inconsistent in, inconsistent out. The point is that this is a fixpoint operation that works definitionally, so I can execute unbounded computations exactly as one might use `fix` in haskell. For example, let `f : (nat -> unit) -> (nat -> unit)` such that `f g n := if TM halts at n then () else g (n+1)`, then `fix f 0` evaluates all the steps of a turing machine, resulting in `()` if and only if the TM halts, so `fix x f 0 =?= ()` is undecidable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 15 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771287):
Note that the other known examples of undecidable definitional equality problems also occur in inconsistent contexts. I'm not certain if it suffices to assume the context is consistent, but if "consistent" is replaced by "inhabited" (i.e. there is a concrete sequence of terms which satisfies the context) then it is equivalent to asking if reduction terminates in the empty context, which is also known as strong normalization. This is believed to be true, but I guess that will be another big chapter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 15 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771484):
Strong Normalization is an open problem -- is that correct? I read it in the reference manual I guess. It feels to me a bit like the 3n+1 problem :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 16 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771545):
I don't think it is, although you have to pull out the big guns to prove it, since it implies that lean is consistent

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771552):
Hmm let me dig out the quote.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771569):
section 3.7

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771570):
"The reduction relation is believed to be strongly normalizing, which is to say, every sequence of reductions applied to a term will eventually terminate."

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 16 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771572):
These definitional equality problems are a little counter intuitive, because you want to reason that in an inconsistent context anything goes, but that's actually not the case. Even if you prove `0 = 1`, you still cannot prove that `0 == 1` definitionally

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 16 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771612):
"Believed to be" is code for "no one's done the work". That's my job :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771614):
Oh I see!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771617):
Is that your thesis problem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 16 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771626):
It's one of the nearby problems, I'm not quite sure what my thesis will be exactly but something along these lines

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 16 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771632):
I guess it depends on what I get done, but unique typing is a major step forward

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 16 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771675):
soundness is the next step, by modeling everything in ZFC + omega inaccessibles

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 16 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771689):
then strong normalization, where you use the rank of a term's ZFC interpretation as the wellfounded decreasing measure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771691):
I think that modeling Lean in ZFC + omega inaccessibles is how I initially tried to understand type theoy.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771739):
Assuming that inductive structures don't add a bunch of axioms I wasn't expecting, this sounds straightforward to me and is probably all well-known. Is that right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 16 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771741):
That's actually the easiest part, it's quite straightforward. But there are some places where I need to know that if a term is a Prop then it's not a Type, and unique typing was necessary for that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771755):
Oh so you use all this to prove strong normalization??

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771757):
I thought you were just going to argue by induction on number of unicode characters in the term :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 16 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771760):
Like I said, big guns

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 16 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771807):
remember from Godel that anything that implies Con(lean) is going to require some advanced mathematics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771810):
I know people who would say that anything that implies Con(lean) is going to require something that is strictly stronger than mathematics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 16 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771814):
If mathematics = lean, sure :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771817):
beyond mathematics, rather than advanced mathematics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771818):
Oh, mathematics is ZFC :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771819):
Of this there is little doubt

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 16 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771826):
You don't believe in the existence of grothendieck universes?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771866):
in the sense that 90% of mathematicians don't have a clue what mathematics is but know how to use it, 9.9% know what ZFC is and use that, and then the other 0.1% worry about other possibilities.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771875):
Didn't I share that link from a recent Scholze paper recently?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771876):
And there's also some section in the stacks project

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771877):
Real, serious, mathematicians actually occasionally go out of their way to justify to the rest of the world that what they are doing can be done in ZFC

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 16 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771883):
I always get the sense from regular mathematicians that if large cardinals come up they just assume them and move on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771884):
Those are just the amateurs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 16 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771885):
like Wiles, I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771888):
Yup

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771890):
He doesn't know how to remove it, but he knows who to ask

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771931):
This is how mathematics is actually done in 2018.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771932):
It's farcical.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771933):
We all believe we're working in ZFC

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771941):
and occasionally someone writes a chapter in a paper saying "I know section 5 was full of categories of rings, but actually we could look at the category of rings which live in V_kappa for kappa=2^2^2^2^2^2^aleph_0 and it all still works, so it's OK we're doing ZFC"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771943):
and then all of us amateurs go "oh that's a relief, it's still holding out"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123772003):
http://www.math.uni-bonn.de/people/scholze/EtCohDiamonds.pdf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123772004):
one of the best living mathematicians, 2017 paper, check out section 4

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123772063):
Algebraic geometry genius Johan de Jong's stacks project: https://stacks.math.columbia.edu/tag/000F and https://stacks.math.columbia.edu/tag/000H

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123772066):
All of that crap just so we can say "it's OK, we're still in ZFC"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123772150):
What's happening is that large cardinals come up (99% of the time in the form "this functor from the category of rings to the category of sets is representable") and people either say nothing (the normal situation) or they note that functors are a bit problematic in ZFC but they read somewhere in the stacks project that it was all OK, or maybe Brian Conrad told them once. There is no formal reference that "everything is OK", but people know who to ask if they're worried

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 16 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123772206):
Over the last year I have come to regard this position as farcical. What are the point of foundations? They're to make your life easier! Not so Scholze has to take time out from being a father of 2 small kids and generating a pile of amazing arithmetic algebraic geometry so he can write down some crap about cardinals just to prove that his latest theory fits into ZFC.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 16 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123772285):
As far as Con(lean) is concerned, the easy/lazy approach (that I will take, at least at first) is to assume omega inaccessibles and prove it. You can be more refined though, since for a specific proof you only need n inaccessibles for some n < omega. It might be possible to even trim down the universes themselves so that they aren't quite grothendieck universes, and then maybe you can fit it all in ZFC, but this probably fails in some extreme cases (like when constructing a model of ZFC in lean)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 16 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123772972):
By the way, https://www.fing.edu.uy/~amiquel/publis/types02.pdf "The not so simple proof-irrelevant model of CC" is my competition in the soundness part; I contend that it is exactly as simple as it looks, and they made some poor modeling decisions in there that made things complicated

