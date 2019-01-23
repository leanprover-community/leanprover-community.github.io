---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/81128DeMorgans.html
---

## Stream: [general](index.html)
### Topic: [De Morgan's](81128DeMorgans.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Lee (Oct 23 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136299566):
Just proved $$\neg (P \lor Q ) \iff \neg P \land \neg Q$$ and $$\neg P \lor \neg Q \to \neg (P \land Q)$$ in Lean. I don't see why the converse would require classical logic though. Can someone please explain?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Lee (Oct 23 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136299609):
```quote
Just proved $$\not (P \and Q ) \iff \not P \and \not Q$$ and $$\not P \or \not Q \to \not (P \and Q)$$ in Lean. I don't see why the converse would require classical logic though. Can someone please explain?
```
Oh no. It didn't format the inline maths.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136299662):
$$\neg (P \land Q ) \iff \neg P \land \neg Q$$ and $$\neg P \lor \neg Q \to \neg (P \land Q)$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136299665):
`\neg (P \land Q ) \iff \neg P \land \neg Q$$ and $$\neg P \lor \neg Q \to \neg (P \land Q)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Lee (Oct 23 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136299713):
```quote
$$\neg (P \land Q ) \iff \neg P \land \neg Q$$ and $$\neg P \lor \neg Q \to \neg (P \land Q)$$
```
Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jean Lo (Oct 23 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301162):
related question: more generally, how does one go about determining whether a proof can be done constructively?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 23 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301256):
If it implies excluded middle then it can't be done constructively. There's an exercise somewhere proving a whole load of things imply excluded middle.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301345):
but that is not necessary.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301420):
you can't check every Kripke model though... is there some finite subset that we can check

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301599):
there is a completeness result that says any intuitionistically invalid statement is false on a finite kripke model

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301662):
that makes set of intuitionstically valid theorems a Π1 set, thus a Δ1 set?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301672):
yes, so it is decidable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 23 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301676):
@**Jean Lo**  Here is a basic strategy for checking that various simple things can't be done constructively. First observe that all the rules of constructive logic apply when "truth values" are...something like...open sets in a topological space (I hope I remembered this right). You model "not" as "interior of the complement" and "implies" as "is a subset of". Then some stuff like "P or not P" simply isn't true in this interpretation, because the union of an open set and the interior of its complement might not be the whole space.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301727):
does this together with the 14-theorem give you a fast(er) way of determining stuff?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301729):
https://en.wikipedia.org/wiki/Kuratowski%27s_closure-complement_problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301731):
It's not complete, unfortunately

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301735):
at least not unless you consider all topologies

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 23 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301744):
I don't know, but I don't know what a Kripke model is and yet I've used this way of thinking about things to convince myself that certain propositions can't be proved in classical logic and basically it's the only way I know to do such a thing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301745):
just consider the Kuratowski algebra?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301848):
A Kripke model is based on a kind of epistemological interpretation of the formulas. There are a bunch of points called "worlds", and at each point there are things that are known to be true at that world, but the things that are not known to be true are just unknowns. There is a "in the future" accessibility relation to other worlds where more things may be known (but previously known things are still known), and things are known to be false only if they are never known in the future

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301894):
I don't think Kevin cares

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136301904):
For example, suppose we have time 0 and time 1, and at time 0 nothing is known and at time 1 $$p$$ is known. Then at time 0 neither $$p$$ or $$\neg p$$ is known

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302025):
This semantics generalizes nicely to modal logic as well, where $$\Box A$$ means A is known now and henceforth in the future

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302083):
$$\square$$ `\square`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Olson (Oct 23 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302094):
My intuition regarding `¬(p ∧ q) → ¬p ∨ ¬q` is that, as my assumption, I know "`p` and `q` aren't *both* true", but I don't know *which one* is false, and the conclusion requires me to pick one of the two and prove it's false, which I cannot do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302122):
ah, is that the program interpretation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Olson (Oct 23 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302208):
yeah, interpreting `∧` as a pair type and `∨` as a sum type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302213):
I think the corresponding model is where at time 0 nothing is known, at time 1a we know q, and at time 1b we know p.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302267):
The kripke model for this one has three points, with time 0 where nothing is known and a branching future. In world 1, p is known, and in world 2 q is known. Then since $$p\land q$$ is true in no world, $$\neg(p\land q)$$ is true in every world, but neither $$\neg p$$ nor $$\neg q$$ is true in world 0

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302274):
:)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Olson (Oct 23 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302330):
Interesting, I've never heard of that stuff but it lines up really well with what I did in my head

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302335):
I think you can consider the more general `((p ∧ q) → r) → (p → r) ∨ (q → r)` and use the same model

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302374):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302405):
cool

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302409):
There is no single finite model complete for intuitionistic logic though, or equivalently there is an infinite family of truth values over one proposition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302427):
or maybe "truth values" just don't make sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Olson (Oct 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302429):
```
h : (p ∧ q) → false
⊢ (p → false) ∨ (q → false)
```

(expanding the \not to the function to false)

I can either assume `p` or assume `q` (the two worlds) and then prove `false`, but I can't apply the function `h` with just one of them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302449):
https://upload.wikimedia.org/wikipedia/commons/5/5c/Rieger-Nishimura.svg

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302461):
what is thsi

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 23 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302472):
I saw this image for the first time like three days ago and I was very confused about how I had never seen it before

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302478):
it is the lattice of propositions over one variable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302485):
up to equivalence

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302539):
in classical logic it is much less interesting, $$\bot < p,\neg p < \top$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302543):
interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302586):
the program interpretation is to let `p` to mean `X contains 1` and `q` to mean `X contains no 1` where `X` is an arbitrary (computable) binary sequence, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302662):
that's one way to do it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302766):
But if you like the program (aka BHK) formulation of intuitionistic semantics, then you might like the computational interpretation of peirce's law as call with continuation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302777):
I never understood what call/cc means

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136302993):
The type is `callcc : ((p -> q) -> p) -> p`. Suppose we are building something of type N, say, and in the course of it we want to do double negation elimination on some proposition `p`, like say "this TM halts". Then that means we are going to do something with this value of type `p`, so that's a function `p -> N`, and so callcc steals this "continuation" and passes it to the enclosed function of type `(p -> N) -> p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136303945):
For example, consider the following implementation of `em`:
```lean
constant callcc {p q : Type} : ((p -> q) -> p) -> p

def em (p : Type) : p ⊕ (p → empty) :=
@callcc _ empty $ λ H,
show p ⊕ (p → empty), from sum.inr $ λ hp, H $
show p ⊕ (p → empty), from sum.inl hp
```
This function looks like magic when you see it for the first time. It's a computational interpretation of EM! So we can just put in our favorite nondecidable proposition to this oracle, like the Riemann hypothesis, and find out the answer. It calls `callcc` at this point, which remembers our position in the code, and then calls the `sum.inr` constructor. So the oracle says: RH is false! We are happy until we find out maybe that RH is actually true, and in justified anger return to our function to prove a contradiction. When we call the function though, it calls `H` with `sum.inl hp`. What happened? The function `H` remembers when we called callcc the first time, and "rewinds time" with our proof of RH in hand. So the oracle says: RH is true! and it stole our proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304147):
> our favorite nondecidable proposition to this oracle, like the Riemann hypothesis

hmm...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304242):
I guess this is like "innocent until proven guilty", we have "false until proven true"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304249):
I still don't understand what it does... thanks for your lengthy explanation though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304262):
The semantics is a bit tricky to explain without a notion of "continuation"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304322):
the idea is that every expression exists in a context, where you are evaluating an expression *in order to pass it to something else*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304335):
and this something else can be thought of as a function from the type of the expr to the "final output"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304340):
which can be whatever, it doesn't really matter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304349):
it's like an expression with a hole in it where our expr goes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304376):
and `callcc` saves this expr-with-hole that surrounds the `callcc f` expression itself, and calls `f` on it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304463):
This enables bizarre behavior like returning twice from a function or functions that call each other as coroutines, or exception handling

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304470):
lots of control flow can be expressed using continuations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304536):
what kind of thing is call/cc?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136304544):
is it a function that we can implement? is it a function that only exists in some alternate programming language?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136306080):
it isn't a function you can implement in lean, but it is a function that could conceivably be supported in the VM as a primitive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318157):
Could you write your RH thing in say `Scheme`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318356):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318362):
I think they are the pioneers of callcc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318441):
then what would it return?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318449):
like I said, "false" until you prove it wrong

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318453):
and then it goes back in time with your proof and says "true"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318501):
do you have actual Scheme code?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318508):
no, but you should just be able to use `callcc` in a term like I've shown

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318521):
the lean code should translate without issue to scheme

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318583):
there is also the matter of scheme not being a typed language

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318709):
if the time travel is the part that is surprising, a more pedestrian explanation is that it just saves the current state of the VM - the call stack and values of the variables, then we can later "reset" to this execution state

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318715):
how does the program "take" our proof?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318717):
you pass it to the function in an attempt to derive false

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318761):
and rather than producing a proof of false, it abandons the entire execution of the rest of the program and resets with this proof in hand

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318779):
does `callcc` have any equational lemmas?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318784):
yes, but they are a bit weird because they depend on the execution context

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136318985):
You have to set up the idea of a dynamic semantics. Let's say we want to evaluate `e1 + e2`, we can write this as `e1 + e2 < K`where `K` is the call stack. It is expecting a value of type `nat` say, here. So we first evaluate `e1`, that is, `e1 < _ + e2, K` where we have pushed `_ + e2` on the stack. We get to a value `v > _ + e2, K` (the arrow is reversed to indicate that the value is done computing) which steps to `e2 < v + _, K`. That is we are evaluating `e2` now. This finishes to `v2 > v + _, K` which steps to `v' > K` where `v'` is the actual result of adding numbers `v` and `v2`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319003):
I don't understand how you can pass the proof to the function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319008):
the function doesn't accept things of type `p` right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319009):
it wants a thing of type `(p -> q) -> p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319021):
In the `em` example I define a particular function of type `(p -> false) -> p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319037):
or rather `(p + not p -> false) -> p + not p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319085):
so when the callcc is called it evaluates this function giving it a kind of magic function which has type `p + not p -> false`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319152):
this function should not ever be called, because it "destroys the universe" rather than producing a proof of false

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319316):
Here's another example. If `f : (N -> false) -> N` is the constant function 42, then `callcc f` just returns 42. Nothing special happens as long as `f` never uses its argument

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319330):
But if `f = \lam g, false.elim (g 12)`, then `callcc f` returns 12

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319335):
how?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319377):
and if `f = \lam g, false.elim (g 12) + false.elim (g 13)`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319379):
returns 12

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319386):
the rest of the computation is abandoned once `g` is called

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 23 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319394):
hmm...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319395):
The function `g` given to `f` is actually the expr-with-hole that `callcc f` is situated in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319465):
it might make more sense if `g` is called `throw` instead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s/near/136319468):
and `callcc` is `catch`

