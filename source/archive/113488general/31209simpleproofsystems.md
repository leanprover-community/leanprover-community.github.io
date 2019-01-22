---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31209simpleproofsystems.html
---

## [general](index.html)
### [simple proof systems](31209simpleproofsystems.html)

#### [Reid Barton (Oct 14 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758238):
Sorry in advance for a rather vague question, hopefully I can make it clear what I'm looking for.
Suppose I wanted to "compile" Lean formulas and proof terms to some other logical system. How "simple" could the target logical system be?

#### [Mario Carneiro (Oct 14 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758249):
hm, it is a bit vague

#### [Reid Barton (Oct 14 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758299):
I want a human-verifiable procedure for taking a theorem statement and turning it into a formula in some other system, and also a procedure for turning the Lean proof into a valid proof in the other system

#### [Mario Carneiro (Oct 14 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758300):
you can go pretty simple for almost any system, by appropriate encoding in the language of PA

#### [Reid Barton (Oct 14 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758308):
So one kind of simplicity which I would like is if the formulas of the target system could be described by an inductive type, and provability could be described by an inductive proposition

#### [Reid Barton (Oct 14 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758325):
Is the encoding you have in mind sort of how like I could simulate a checker for any language by a universal Turing machine?

#### [Mario Carneiro (Oct 14 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758366):
yes

#### [Mario Carneiro (Oct 14 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758372):
I get the sense that misses your point though

#### [Reid Barton (Oct 14 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758373):
I see.

#### [Reid Barton (Oct 14 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758390):
I was hoping for a system more like: if I have a proof of P and a proof of P -> Q, then I get a proof of Q. Plus a bunch of axioms. I'm pretty sure that I need additional rules to deal with quantifiers though.

#### [Mario Carneiro (Oct 14 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758395):
like ZFC style?

#### [Mario Carneiro (Oct 14 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758404):
$$ $$ + FOL

#### [Reid Barton (Oct 14 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758465):
I think so but then I think I have to deal with substitution and that seems a little bit more complicated than I would like

#### [Reid Barton (Oct 14 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758479):
Is metamath based on something like this?

#### [Mario Carneiro (Oct 14 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758487):
I was about to suggest metamath indeed

#### [Mario Carneiro (Oct 14 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758494):
it doesn't have proper substitution

#### [Mario Carneiro (Oct 14 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758500):
just direct substitution

#### [Reid Barton (Oct 14 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758502):
I guess another way to frame the question is: Suppose you wanted to be as sure as possible that you had correctly implemented a proof checker which only accepts theorems provable in ZFC+U (or whatever).

#### [Reid Barton (Oct 14 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758544):
The universal turing machine idea doesn't help you here, because you still need to write the "actual machine" (it is just part of the specification of what constitutes a proof, rather than being the checker itself)

#### [Mario Carneiro (Oct 14 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758553):
I think you can avoid proper substitution in the axioms and what not by having it be an explicit judgment in the system

#### [Reid Barton (Oct 14 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758554):
what's not "proper" about direct substitution? Something about not renaming bound variables?

#### [Mario Carneiro (Oct 14 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758555):
yes

#### [Mario Carneiro (Oct 14 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758557):
metamath has a notion of text substitution a la grep

#### [Reid Barton (Oct 14 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758558):
I think I've heard phrases like "proof calculus with explicit substitution", is that relevant?

#### [Mario Carneiro (Oct 14 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758598):
that's about having terms in the language that are a sort of "deferred substitution"

#### [Mario Carneiro (Oct 14 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758603):
but you still have to do the substitution at some point

#### [Mario Carneiro (Oct 14 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758608):
although you can build it into the steps of actual proof, which is basically what metamath does

#### [Reid Barton (Oct 14 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758616):
but does that mean I can push the work of substitution into the proof itself

#### [Mario Carneiro (Oct 14 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758617):
yes

#### [Mario Carneiro (Oct 14 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758619):
that way all your substitutions are direct

#### [Reid Barton (Oct 14 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758662):
and if I were to target one of these systems then is there some kind of bound on how large the proofs would become in terms of the size of the original Lean proof term?

#### [Reid Barton (Oct 14 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758665):
like, a useful bound

#### [Mario Carneiro (Oct 14 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758681):
no, but the problem in that case is not substitution

#### [Mario Carneiro (Oct 14 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758682):
it is reduction

#### [Reid Barton (Oct 14 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758684):
oh right

#### [Mario Carneiro (Oct 14 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758687):
you can prove ridiculous theorems by `rfl` in lean

#### [Mario Carneiro (Oct 14 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758714):
If you deduplicate the proof I think substitution is a "modest" overhead, maybe linear in the proof

#### [Reid Barton (Oct 14 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758715):
how about something like linear in the size of the term plus the total number of reduction steps Lean has to do (if that makes sense)

#### [Mario Carneiro (Oct 14 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758756):
My favorite characterization is "linear in the run time of the lean checker"

#### [Reid Barton (Oct 14 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758757):
Sure

#### [Mario Carneiro (Oct 14 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758815):
You need substitution of some kind built in to your system so that you can express a proof schema like "|- P and |- P -> Q implies |- Q`

#### [Mario Carneiro (Oct 14 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758818):
but direct substitution is good enough

#### [Reid Barton (Oct 14 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758819):
Okay this was going to be exactly my next question: do I need some kind of substitution

#### [Mario Carneiro (Oct 14 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758823):
Actually metamath also has a primitive notion of "disjoint variables" used in substitution

#### [Reid Barton (Oct 14 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758824):
Well

#### [Mario Carneiro (Oct 14 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758829):
meaning that you can say "P can be substituted for any expression not containing x"

#### [Mario Carneiro (Oct 14 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758872):
again, this is grep style, so no provisos like "no free x", just "no x at all"

#### [Mario Carneiro (Oct 14 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758875):
but that is good enough since you can build the rest into the proof system

#### [Reid Barton (Oct 14 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758885):
this particular example though is substituting into a fixed formula, right? I could imagine representing it by a constructor of an inductive type
```lean
| mp (P Q : formula) (p : proof P) (pq : proof (formula.imp P Q)) : proof Q
```

#### [Mario Carneiro (Oct 14 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758910):
yes, here you have lifted the substitution to the beta rule of the metatheory (which is lean, I guess)

#### [Reid Barton (Oct 14 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758912):
which is just a built-in part of the syntax of proofs

#### [Reid Barton (Oct 14 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758952):
But then, I don't know how to deal with "forall elim" without invoking substitution in a more serious way

#### [Mario Carneiro (Oct 14 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758958):
right, you need a true substitution there... but you can get around it with some different axiomatizations

#### [Mario Carneiro (Oct 14 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758967):
I think the safest/easiest way to do this while still being transparent about it is to have a judgment `P(x |-> y) is Q`

#### [Mario Carneiro (Oct 14 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759010):
although when you get to the bottom you have to deal with `z(x |-> y)` which depends on a disjointness requirement

#### [Mario Carneiro (Oct 14 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759014):
which can be equality if you have decidable equality on the variables

#### [Mario Carneiro (Oct 14 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759020):
metamath takes a more abstract approach and just axiomatizes what this "disjointness" should satisfy

#### [Reid Barton (Oct 14 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759023):
Yes that's fine. This looks interesting.

#### [Reid Barton (Oct 14 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759034):
So I have a rule of inference that takes `forall x, P x` and `y` and `P(x |-> y) is Q` and concludes `Q`

#### [Mario Carneiro (Oct 14 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759039):
right

#### [Reid Barton (Oct 14 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759082):
and `P(x |-> y) is Q` is also defined by some other induction

#### [Mario Carneiro (Oct 14 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759085):
right

#### [Reid Barton (Oct 14 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759092):
I like this.
Is this likely to mess up the "size of proof is linear in the Lean kernel runtime" property?

#### [Mario Carneiro (Oct 14 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759094):
no

#### [Mario Carneiro (Oct 14 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759096):
because lean has to do this too

#### [Reid Barton (Oct 14 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759101):
oh, I see!

#### [Mario Carneiro (Oct 14 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759173):
You can have a similar induction rule for deducing `x is free in P` for the elim rules

#### [Mario Carneiro (Oct 14 2018 at 05:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759369):
By the way metamath [doesn't do it this way](http://us.metamath.org/mpeuni/mmset.html#pcaxioms), instead it uses a slightly tricky axiom system for pred calc that allows us to deduce these judgments without building them in directly, and lets the forall rule be the simple `|- (forall x, P) -> P`

#### [Mario Carneiro (Oct 14 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759489):
But I think this is something like the difference between listing 20 obvious axioms for boolean algebras vs listing 3 incomprehensible ones and proving they are equivalent

#### [Reid Barton (Oct 14 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759619):
So here is one reason why I have this question.
Cryptography people tell me (not in this language of course, and I hope I am not mistranslating anything) that if I have some fancy indexed inductive type `proof P`, I can design some functions f, g and h with the following properties.
* f is a predicate on short strings (~300 bytes) which can be evaluated quickly (~20ms).
* g is some even cheaper function on such strings, and h(P) is just a recursive hash of the contents of P.
* Given a term of type `proof P` I can calculate a string x with f(x) = true and g(x) = h(P).
* (Subject to some trusted setup and cryptographic hardness assumptions,) the only way to construct such an x is as above: I have to really know a term of type `proof P`, though I can also use other pairs (Q, y) which have been published as certificates of other statements as inputs to my term.

The catch is that the third item is somewhat ridiculously expensive, though in the future it may become less ridiculously expensive.

#### [Reid Barton (Oct 14 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759630):
As a ballpark estimate for ridiculously expensive, assume 1 constructor costs 1 second to compute

#### [Mario Carneiro (Oct 14 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759688):
so I guess x is a "proof hash" of some sort, f means "this is a proof of something" and g means "this is the statement that is being proved"?

#### [Reid Barton (Oct 14 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759689):
Right

#### [Reid Barton (Oct 14 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759757):
Probably it is a bit better to think that the "proof hash" is a statement like "this is a proof of some statement which hashes to H"

#### [Mario Carneiro (Oct 14 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759809):
I'm surprised the function g is easy

#### [Mario Carneiro (Oct 14 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759818):
it's not even that easy to calculate the statement of a proof sometimes

#### [Reid Barton (Oct 14 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759821):
I think that g can just be extracting some of the bits from the string though I confess I have not thought much about this particular aspect yet

#### [Mario Carneiro (Oct 14 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759828):
I guess you can do something like that

#### [Reid Barton (Oct 14 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759830):
I think the idea is that it was the job of the person producing the proof to include the information of what is being proved

#### [Reid Barton (Oct 14 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759883):
This is really at a super early stage of "is it even conceivable that one could use this for theorem proving"--I'm trying to get a sense of what the minimal demands on the theorem proving side are

#### [Reid Barton (Oct 14 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759891):
What I find to be really remarkable about these setups is that the cost to verify a proof is independent of the size of the proof

#### [Mario Carneiro (Oct 14 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759944):
that's a good point. I wonder whether it can be used as a trusted alternative to caching

#### [Reid Barton (Oct 14 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759954):
So, ignoring some inconvenient details like the ~1000000x slowdown, you could use it as part of a "distributed theorem verification system", without requiring trusted provers

#### [Reid Barton (Oct 14 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760023):
(Concretely, you could imagine some kind of database to which anyone can upload proof certificates, with the amazing property that in order to verify the correctness of any proof, you only need to check *that certificate* and not the proofs of any of the results which the proof relies on)

#### [Mario Carneiro (Oct 14 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760029):
Unless they decided to modify `logic.basic` :)

#### [Mario Carneiro (Oct 14 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760085):
In some sense we already have this, the difference is that you can do this check without even precomputing the proofs of earlier parts, or even knowing what the proofs are (e.g. proprietary proofs)

#### [Reid Barton (Oct 14 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760134):
I think what we have is like a non-distributed version of this, where I trust the Lean kernel on my machine to only record as theorems the facts which it has checked. Or do you mean something else?

#### [Reid Barton (Oct 14 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760191):
Solving the recompilation problem is somehow close to but not exactly the same as the problem this solves, I think.

#### [Mario Carneiro (Oct 14 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760192):
That's true, but I'm pointing out that if you have mathlib, say, fully compiled, then you are currently in the state of trusting all the results in it, and if a new proof comes along that depends on these facts you only have to check *that proof* and not the rest of the library

#### [Mario Carneiro (Oct 14 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760197):
In this crypto setup compilation is being replaced by certificate generation

#### [Mario Carneiro (Oct 14 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760251):
where the difference is that if I send you a certificate you can have the same trust as if you created it yourself, while if I send you my compiled files then you don't know that I haven't tampered with them

#### [Reid Barton (Oct 14 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760254):
Yes exactly

#### [Reid Barton (Oct 14 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760271):
And if we had some massive proof of say FLT, then maybe it would be quite expensive for everyone to verify the whole proof, whether or not they do it incrementally over time. If the certificates can be computed by someone just once, then you can save total work (assuming there are > 1000000 people who want to verify the proof)

#### [Mario Carneiro (Oct 14 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760330):
I think this isn't a realistic threat model though

#### [Reid Barton (Oct 14 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760331):
Anyways, I think that today we're not really anywhere close to wanting something like this, and the technology is also not really that feasible yet

#### [Reid Barton (Oct 14 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760372):
Which part is not realistic?

#### [Mario Carneiro (Oct 14 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760373):
I think when people get mathlib they usually don't do it because they want additional assurance that the theorems in it are true

#### [Reid Barton (Oct 14 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760374):
Well not for mathlib

#### [Mario Carneiro (Oct 14 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760385):
I am pretty sure that feit thompson is true because Gonthier checked it, and my running it on my machine did not increase my confidence in the theorem as much as it increased my confidence that I had installed Coq correctly

#### [Reid Barton (Oct 14 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760427):
In some distant future world, you could imagine that instead of posting papers to arXiv, we publish formal proofs to some other service. I guess your claim is that in that scenario, you are not too worried about people claiming to publish proofs which are in fact bogus.

#### [Reid Barton (Oct 14 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760434):
Especially given that anyone *could* verify the proof and everything underneath it, it would just be quite expensive for everybody to do so.

#### [Mario Carneiro (Oct 14 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760438):
I would want the service to be spending effort on checking for bogus proofs

#### [Mario Carneiro (Oct 14 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760443):
that's not my responsibility

#### [Reid Barton (Oct 14 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760447):
Right, you could delegate to the service to check correctness which seems quite reasonable

#### [Mario Carneiro (Oct 14 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760487):
I would be responsible for convincing myself that the service is doing its job to my satisfaction

#### [Mario Carneiro (Oct 14 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760492):
meaning that this service should be easily checkable (i.e. small trusted kernel)

#### [Reid Barton (Oct 14 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760508):
Plus you have to trust the people who operate the service to actually verify the proofs

#### [Mario Carneiro (Oct 14 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760567):
I think there is room for some crypto cross checks at this point

#### [Mario Carneiro (Oct 14 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760577):
i.e. the process of verification by the service also produces a certificate that I can check quickly

#### [Reid Barton (Oct 14 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760625):
In general the way to produce a certificate that a computation was done correctly is the same process that I am talking about for generating proof certificates.

#### [Mario Carneiro (Oct 14 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760636):
Although nowadays this check is replaced with me being able to download and check the proof myself if I want

#### [Reid Barton (Oct 14 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760637):
(Namely, SNARKs and applications like TinyRAM)

#### [Reid Barton (Oct 14 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760645):
Right so in actual crypto applications, there is the far more important property that the person producing the certificate doesn't have to give you the proof.

#### [Reid Barton (Oct 14 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760711):
As I mentioned, this stuff is currently quite impractical for large applications.
Probably a far more practical question would be: could Lean have a mode where it checks a given olean file against lean source, and is this faster than trying to recompute the proof from scratch.

#### [Reid Barton (Oct 14 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760762):
Or more generally, what information could Lean write out to an .olean or other external certificate file which would make verifying the validity of a theorem more efficient

#### [Mario Carneiro (Oct 14 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760873):
In principle lean should be able to check an olean file without reference to a lean file at all

#### [Mario Carneiro (Oct 14 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760883):
and if you wanted you could view this as a "compiled file" same as the compiled binaries of any other program

#### [Mario Carneiro (Oct 14 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760886):
in particular, it would be difficult to reverse engineer the sources from this

#### [Mario Carneiro (Oct 14 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760890):
... I think. I need to write an olean viewer to be sure

#### [Reid Barton (Oct 14 2018 at 05:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760994):
Do .olean files and the export textual format and what `#print foo` produces all contain roughly the same information?

#### [Reid Barton (Oct 14 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761081):
looking at the export format it seems not to include all information about notation, which must be in .olean files, but aside from minor details like that

#### [Mario Carneiro (Oct 14 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761088):
I think so

#### [Mario Carneiro (Oct 14 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761089):
It should have the information necessary to construct an `environment` object from the imported environments

#### [Reid Barton (Oct 14 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761091):
I wonder whether there is a way today to convince Lean to export an .olean file to textual format

#### [Mario Carneiro (Oct 14 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761139):
That would be nice... I probably wouldn't even write such an exporter in lean

#### [Mario Carneiro (Oct 14 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761151):
(that is, there is no particular advantage to writing it in lean)

#### [Reid Barton (Oct 14 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761215):
I guess you could import the module for which you had the .olean from a new module, and then run it through `lean --export`

#### [Reid Barton (Oct 14 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761310):
it seems to work

#### [Reid Barton (Oct 14 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761322):
though I wouldn't be 100% confident that lean importing an arbitrary .olean file and then exporting its contents and checking them in an external checker means lean is actually in a valid state after reading the .olean file

#### [Mario Carneiro (Oct 14 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761702):
why? The checker doesn't matter for that

#### [Mario Carneiro (Oct 14 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761703):
Lean itself will complain if the olean is bad

#### [Mario Carneiro (Oct 14 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761709):
although I'm not sure how you can induce that without writing the olean bits manually, since lean won't produce olean files for errored files

#### [Kevin Buzzard (Oct 14 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135771923):
```quote
I want a human-verifiable procedure for taking a theorem statement and turning it into a formula in some other system, and also a procedure for turning the Lean proof into a valid proof in the other system
```
My understanding (which may be wrong) is: Computer scientists want (and occasionally some claim that they have built) a procedure for translating code written in one common language to code written in another common language, and the reason none of these procedures are ever used in practice is that in practice they are typically not very good at all.


```quote
I am pretty sure that feit thompson is true because Gonthier checked it, and my running it on my machine did not increase my confidence in the theorem as much as it increased my confidence that I had installed Coq correctly
```

My understanding (which is much more likely to be correct this time) is that Feit Thompson is true because the pure mathematics community did an *extremely* good job of checking it in the 1960s, decided it was correct, and awarded Thompson the Fields Medal as a consequence. This is exactly why pure mathematicians are not excited by Gonthier et al's verification. Checking 400 pages of lemmas about finite groups and undergraduate/MSc level representation theory and number theoy is not difficult for a team of humans to do, it can be broken down into manageable sub-jobs etc.

#### [Mario Carneiro (Oct 14 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135772552):
Yeah, but I didn't understand what Thompson did at all, I at least have some idea of how Gonthier did it

#### [Mario Carneiro (Oct 14 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135772564):
I think you should not forget that one of the applications of formal mathematics is that at least in principle you can pick it up and read it from *zero* prior knowledge of the field

#### [Mario Carneiro (Oct 14 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135772607):
And I know several people who did exactly that, including myself

#### [Mario Carneiro (Oct 14 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135772725):
(Note that that quote was about my subjective perception of the truth of the theorem, not the mathematics community at large.) The whole point of this crypto stuff is that just because *you* trust X body of knowledge / institution / person doesn't mean *I* do, and the problem is to figure out how to reliably transfer your trust to me

#### [Kevin Buzzard (Oct 14 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135776718):
Aah I see! So this is a perfect analogy. I say "I am a mathematician and my tribe can guarantee that Feit-Thompson is proved" and you reply "I am a computer scientist and I require a different kind of justification than just assurances from your tribe".

#### [Patrick Massot (Oct 14 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135776739):
```quote
I think you should not forget that one of the applications of formal mathematics is that at least in principle you can pick it up and read it from *zero* prior knowledge of the field
```
I thought mathlib didn't care about human readability?

#### [Mario Carneiro (Oct 14 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135776942):
I'm talking about formal proof in general. Certainly it's more true of metamath than mathlib, because there are fewer skipped steps

#### [Mario Carneiro (Oct 14 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135776974):
The point is that it doesn't matter if it's been written to be human readable in the mathematician's sense. In fact, it's better if it doesn't make too much use of tactics that do what Kevin wants (i.e. trivial for a mathematician steps omitted)

#### [Mario Carneiro (Oct 14 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135777021):
because that way you can follow what's happening even if you aren't a mathematician

#### [Mario Carneiro (Oct 14 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135777103):
the worst kind of proof for people who want to learn like this are the big complicated statement proven by some blasty tactic. It's like the movie ends just as it's setting up for the climax, you feel robbed

#### [Mario Carneiro (Oct 14 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135777177):
luckily lean doesn't have too many blasty tactics yet, so it is still feasible to read a proof and get the details

#### [Kevin Buzzard (Oct 14 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135777934):
I have been telling my maths students to never read any proofs in mathlib because they are all unreadable, and if they want to know why some theorem is true then to look it up on Wikipedia, which is written for humans. I am the anti-Paulson. I believe that proofs generated by computers in the future will inevitably be unreadable, and that anyone who attempts to make them readable will in some sense be holding the area back. I was always struck by something Johannes said to me months ago when I asked him why he'd changed my 10 line tactic proof into an incomprehensible two-line term proof, and he replied that he liked the challenge of finding a short efficient proof of something which was easy in maths. While he might not want to extrapolate this comment himself to longer proofs, I don't mind doing so.

#### [Mario Carneiro (Oct 14 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135778173):
My view is that there is a kind of readability that can't be harmed by "unreadable" proof style

#### [Mario Carneiro (Oct 14 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135778177):
because the information is still there to be given to the computer

#### [Mario Carneiro (Oct 14 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135778228):
and there are some enterprising kids that actually prefer this kind of exactitude to the "aimed for human level" style that is traditional in maths

#### [Mario Carneiro (Oct 14 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135778285):
This is where stuff like `#explode` is useful, when you just want to see EVERYTHING and make your own choices about what is important

#### [Mario Carneiro (Oct 14 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135778292):
rather than whatever the author thought was important or trivial

#### [Patrick Massot (Oct 14 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135780253):
```quote
I have been telling my maths students to never read any proofs in mathlib because they are all unreadable, and if they want to know why some theorem is true then to look it up on Wikipedia, which is written for humans.
```
I just did the exercise of reading the Wikipedia page on [topological rings](https://en.wikipedia.org/wiki/Topological_ring). It's full of plain wrong statements...

#### [Kevin Buzzard (Oct 14 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135786040):
You have a clear choice then :-) Human efforts with wrong statements, or `topological_structures.lean` written by Johannes and never meant to be read by a mathematician :-) Pure maths is two things and you are lucky enough to be able to choose which one you like best.

#### [Johan Commelin (Oct 15 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135797803):
@**Mario Carneiro** @**Reid Barton** I find this topic of cryptographic proof certificates really interesting! Do you know if anything like this has been implemented for some theorem prover? I've thought about this on and off (basically as an amateur) and I couldn't find anything written about it. Are there references that go beyond speculating how nice it would be to have this? From Reid's description it is still quite a leap to an actual (fast) implementation.

