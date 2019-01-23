---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/31330mathlibconstructivity.html
---

## Stream: [new members](index.html)
### Topic: [mathlib & constructivity](31330mathlibconstructivity.html)

---


{% raw %}
#### [ Scott Olson (Sep 25 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134574550):
is there a standard library structure for isomorphisms, like this type in Idris? https://github.com/idris-lang/Idris-dev/blob/bae730a7ffaeae09a835a35bac132c141f3b50b3/libs/base/Control/Isomorphism.idr#L10-L16

i'm not sure what name to search for

#### [ Simon Hudon (Sep 25 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134574597):
In mathlib, you may want `data.equiv.basic`

#### [ Simon Hudon (Sep 25 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134574603):
https://github.com/leanprover/mathlib/blob/master/data/equiv/basic.lean

#### [ Scott Olson (Sep 25 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134575168):
thanks, that looks like what i want

that brings me to another question, though... should i be using mathlib, in general? is it basically just expected that most people will be using it?

#### [ Simon Hudon (Sep 25 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134575317):
Most people use mathlib because it's the largest repository of definitions and theorems in Lean and it keeps growing. Most importantly it has a lot of useful stuff

#### [ Mario Carneiro (Sep 25 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134575318):
That is certainly the intent... it is like the standard library of most programming languages

#### [ Scott Olson (Sep 25 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134578662):
is mathlib generally constructive or classical? or at least, does it clearly delimit which things depend on classical axioms? curious if i'll have to "wary" and check with `#print axioms`

#### [ Simon Hudon (Sep 25 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134578810):
You'll have to be wary. An effort is made to label classical theorems but people still use them pretty loosely

#### [ Mario Carneiro (Sep 25 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134578812):
mathlib is mostly classical. In particular, we only worry about constructivity in so far as it avoids the `noncomputable` marking. In any props or theorems we use AC freely

#### [ Mario Carneiro (Sep 25 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134578903):
There really isn't any point in being "wary" with `#print axioms`, because all you will achieve by doing that is get yourself in a tizzy about the many unnecessary uses of AC. Suffice it to say it is used in many difficult to avoid places in the foundation, some of which are in lean core and so are not even accessible to mathlib

#### [ Scott Olson (Sep 25 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134578908):
is there a discussion somewhere on the pros and cons of being classical for something like mathlib or just Props in general?

#### [ Scott Olson (Sep 25 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134578921):
the mathlib docs i've found so far just don't mention it

#### [ Mario Carneiro (Sep 25 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134578929):
We've had the discussion off and on for a while. Lean 2 made a concerted effort to be both constructive and classical

#### [ Mario Carneiro (Sep 25 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134578977):
At the beginning I held out hope that we could avoid AC when unnecessary, but at this point it's clear this isn't going to happen

#### [ Simon Hudon (Sep 25 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579016):
I wonder if that's part of why mathlib was able to move quickly too

#### [ Scott Olson (Sep 25 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579079):
i don't have much understanding of the implications of using such axioms in a system like Lean. i understand `noncomputable` prevents even bytecode, but any axioms at all prevent the term from evaluating to a normal form, and i'm curious if that can cause problems in practice

#### [ Mario Carneiro (Sep 25 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579097):
We don't evaluate proofs at all in practice

#### [ Mario Carneiro (Sep 25 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579099):
it doesn't matter if they are classical or not because they aren't programs

#### [ Scott Olson (Sep 25 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579154):
that was my thinking for Prop, but i haven't been able to find much documentation talking about this point

#### [ Mario Carneiro (Sep 25 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579155):
The only mechanism we have for evaluating proofs is `#reduce` and it falls over on all but the most trivial examples

#### [ Mario Carneiro (Sep 25 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579169):
I guess there isn't much docs on this

#### [ Mario Carneiro (Sep 25 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579187):
The VM evaluates anything that is not a Prop and is not `noncomputable`

#### [ Simon Hudon (Sep 25 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579193):
When computation is involved, you really need to look at defs that are in `Type 0` and over. Then an effort is often made to be efficient

#### [ Scott Olson (Sep 25 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579239):
that makes sense, thanks for all the responses

#### [ Simon Hudon (Sep 25 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579246):
:+1:

#### [ Scott Olson (Sep 25 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579260):
i realized while talking to a friend just now that an interesting argument in favor of using fewer axioms is that it makes the proof potentially more "portable" to different formalisms, but that's somewhat aspirational and lacking it doesn't block anything in mathlib in the meantime

#### [ Mario Carneiro (Sep 25 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579308):
Unfortunately, the axioms that really prevent portability of lean proofs aren't turn-off-able

#### [ Mario Carneiro (Sep 25 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579319):
Most systems have some equivalent of the axiom of choice, but few have inductive types and a hierarchy of universes

#### [ Kevin Buzzard (Sep 25 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579850):
```quote
i realized while talking to a friend just now that an interesting argument in favor of using fewer axioms is that it makes the proof potentially more "portable" to different formalisms, but that's somewhat aspirational and lacking it doesn't block anything in mathlib in the meantime
```
I'm a pure mathematician (as are several other people here) and one of the things that attracted me to Lean is precisely the attitude that "we will do maths like regular pure mathematicians do" (i.e. assume things like the axiom of choice, which in my circles is regarded as "just another axiom, with no particular reason to fuss about it".)

#### [ Sean Leather (Sep 25 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579993):
```quote
I'm a pure mathematician (as are several other people here) and one of the things that attracted me to Lean is precisely the attitude that "we will do maths like regular pure mathematicians do" (i.e. assume things like the axiom of choice, which in my circles is regarded as "just another axiom, with no particular reason to fuss about it".)
```
On the other hand, some of the things that attracted me to Lean included the ability to do constructive mathematics, the nice syntax, a fast theorem prover, and a comprehensive library. :slight_smile:

#### [ Scott Olson (Sep 25 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580185):
i figured some of what i said might have given away my friend's and my bias towards constructive type theories :P

i can see why Lean attracted pure mathematicians who might have otherwise used Coq or similar, though. the experience out of the box with Lean in VSCode is the best i've seen from any theorem prover

#### [ Mario Carneiro (Sep 25 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580336):
I am also attracted to constructive mathematics generally, but the pure mathematicians have worn me down. :) I realize now that lean is not remotely geared towards limiting its axiom strength, and if you want a system for playing with axioms you should look elsewhere. "Having few axioms" only means having few interesting subsystems, and none of the available subsystems are recognizable to traditional mathematicians except possibly intuitionistic type theory

#### [ Simon Hudon (Sep 25 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580385):
@**Sean Leather** how inconvenient is it for you that mathlib makes such liberal use of classical axioms?

#### [ Mario Carneiro (Sep 25 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580400):
Instead, it seems much more likely that lean will be able to support doing logic at the meta level, which is something that few systems can currently do well. This approach is much more flexible, of course, with regards to its axioms and with the permissible methods of proof

#### [ Sean Leather (Sep 25 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580402):
I haven't had any issues so far. I'm not even sure where I would run into any.

#### [ Scott Olson (Sep 25 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580417):
i figure i'll just adjust my expectations of what exactly i will play with in lean, but it will still be suitable for a lot of the stuff i want to experiment with

#### [ Sean Leather (Sep 25 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580423):
The only thing is this output:

```lean
#print axioms  
```

```lean
quot.sound : ∀ {α : Sort u} {r : α → α → Prop} {a b : α}, r a b → quot.mk r a = quot.mk r b
classical.choice : Π {α : Sort u}, nonempty α → α
propext : ∀ {a b : Prop}, (a ↔ b) → a = b
```

#### [ Simon Hudon (Sep 25 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580424):
Is your requirement that functions be computable or actually to avoid the axioms?

#### [ Sean Leather (Sep 25 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580482):
Computable, I suppose. I don't do anything actively to avoid axioms, but I don't think I use anything that does use the axiom of choice.

#### [ Scott Olson (Sep 25 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580506):
`#print axioms <name>` will list the axioms used (transitively) for the given thing

#### [ Scott Olson (Sep 25 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580515):
but as we discussed, this shouldn't be a problem in the bodies of proofs that will never need to be evaluated or examined by other proofs

#### [ Sean Leather (Sep 25 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580569):
```quote
`#print axioms <name>` will list the axioms used (transitively) for the given thing
```
When I create an empty file, `#print axioms` shows what I wrote above. :smile:

#### [ Scott Olson (Sep 25 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580583):
yeah, `#print axioms` just prints the axioms that are currently in scope

#### [ Mario Carneiro (Sep 25 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580592):
Can anyone come up with a reasonable (not completely contrived) example of a computable function that uses AC/LEM in its definition?

#### [ Mario Carneiro (Sep 25 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580884):
I will amend "not completely contrived" to not eliminable, in the sense that there isn't a way to write the same function without the axiom, or at least it's not easy to do so

#### [ Kevin Buzzard (Sep 25 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580946):
on nat?

#### [ Mario Carneiro (Sep 25 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580963):
sure, I doubt it makes a difference but `nat -> nat` is a fine target

#### [ Kevin Buzzard (Sep 25 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580976):
I'm sure you're right but I'm such a noob at this sort of thing. A year ago I wouldn't even have been able to formalise the question rigorously.

#### [ Mario Carneiro (Sep 25 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581031):
To give a hint on why it's even possible: `nat.find` will calculate the smallest value satisfying a predicate, given only a proof that there is such a value (in Prop). This proof can rely on any axioms, and the function will still be computable

#### [ Kevin Buzzard (Sep 25 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581033):
What about f(n)=1 if Fermat's Last Theorem is true and 0 otherwise? It's completely contrived but I'm trying to get the hang of the question. All known proofs of FLT use AC.

#### [ Mario Carneiro (Sep 25 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581117):
That won't work because `f` is just the constant function `1`, it doesn't need any axioms for its definition

#### [ Mario Carneiro (Sep 25 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581166):
But I think you are on the right track. Can you think of any forall exists theorem on nat that relies on AC?

#### [ Simon Hudon (Sep 25 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581211):
I don't know how to formalize that statement but it seems like a computable function like you described cannot be constructed

#### [ Mario Carneiro (Sep 25 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581378):
Here is an example that relies on the input being in a nonoptimal form: if the input is a function `f : nat -> nat` which is not the constant zero function, then you can computably find a nonzero `nat` in the range of `f`

#### [ Simon Hudon (Sep 25 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581503):
That's true. I stand corrected

#### [ Kevin Buzzard (Sep 25 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581579):
```quote
What about f(n)=1 if Fermat's Last Theorem is true and 0 otherwise? It's completely contrived but I'm trying to get the hang of the question. All known proofs of FLT use AC.
```
So by "computable" you mean "externally provable to be equal to a certain given fixed computable function", rather than "provable in Lean with/without AC to be equal to a certain given fixed computable function"

#### [ Kevin Buzzard (Sep 25 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581594):
What about f(n)=1 if RH is true and 0 otherwise? Don't I need LEM to define this?

#### [ Kevin Buzzard (Sep 25 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581599):
I'm still struggling to move away from the "contrived" part, as you can see ;-)

#### [ Mario Carneiro (Sep 25 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581758):
If you pick something which is definitely not decidable, or not known to be decidable like RH, then the function won't be computable either. By "computable" I mean "passes lean's `noncomputable` check"; you can't write `def f := if RH then 1 else 0` because `RH` is not decidable

#### [ Scott Olson (Sep 25 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581831):
yeah, that would specifically require the classical instance for `decidable` that uses LEM internally, which is `noncomputable`, which forces `f` to be `noncomputable`

#### [ Kevin Buzzard (Sep 25 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581840):
Here is something much less contrived but I am much less clear about whether it fits into the scope of this question. Let's say a pure mathematician proves that for every g>=2 there is a computable upper bound $$B(g)$$ for the number of rational points on a smooth projective curve of genus g over the rationals, and their proof uses a bunch of algebraic geometry and AC / LEM everywhere. I suspect I could find arithmetic geometers who were prepared to conjecture that this mathematical statement was true. If this result got proved, and it turned out that a deep theorem implied that $$B(g)=10000*g$$, this would *not* be an example, right? :-/

#### [ Mario Carneiro (Sep 25 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581848):
You can write `def f := if FLT then 1 else 0` only if you have already provided a computable proof of `decidable FLT`, which will involve a proof of FLT. This falls afoul of the second restriction because then you could just replace the definition of `f` with `1`

#### [ Mario Carneiro (Sep 25 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581943):
You are right, this is an interesting situation. If we know a bound on the function then we can skip the clever maths and just use the bound

#### [ Mario Carneiro (Sep 25 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581957):
Somehow it has to be an existence theorem with no bound

#### [ Edward Ayers (Sep 25 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582212):
How about `f(n)` is 1 if the nth turing machine halts and 0 otherwise? If I'm not mistaken the proof that `f` is total requires LEM.

#### [ Mario Carneiro (Sep 25 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582251):
I have been thinking about examples like that, but again it needs to be computable

#### [ Edward Ayers (Sep 25 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582254):
But that might be because I've never seen a constructive proof of halting problem

#### [ Mario Carneiro (Sep 25 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582319):
To define that function you have to know whether the nth turing machine halts

#### [ Edward Ayers (Sep 25 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582433):
Ah in that case I think that it's impossible.

#### [ Edward Ayers (Sep 25 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582569):
As in you can always rewrite the function to not use AC

#### [ Mario Carneiro (Sep 25 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582624):
Here's another way to put it: Find computable predicates `p(n), q(m,n)` such that if `p(n)` is true then there exists an `m` such that `q(m,n)`, but there is no computable upper bound on the least satisfying instance

#### [ Scott Olson (Sep 25 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582743):
so with `nat.find` we could find the least `nat` satisfying some predicate while only proving this search will actually terminate with, for example, a proof by contradiction (the kind that requires classical double negation elimination)?

#### [ Edward Ayers (Sep 25 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582749):
I can just run the `q` machine on each value of `m = 0,1,2,...` in turn. Since there exists an `m` where `q(m,n)` works, that program will halt. Right?

#### [ Mario Carneiro (Sep 25 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582818):
yes, that's the idea

#### [ Edward Ayers (Sep 25 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582819):
So it's impossible (to find such computable predicates)

#### [ Mario Carneiro (Sep 25 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582821):
that's the computable function

#### [ Mario Carneiro (Sep 25 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582980):
hm, you may be right. The very constraint that makes it lean-computable will also produce a computable upper bound, namely this function

#### [ Mario Carneiro (Sep 25 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583041):
but I think maybe "computable upper bound" isn't what I want either; it needs to be an upper bound that you can't prove using lean without AC

#### [ Mario Carneiro (Sep 25 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583046):
you can't use this function as a proof because it requires a proof that it will halt to run

#### [ Mario Carneiro (Sep 25 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583092):
If we use something weaker than DTT, it should be possible to use some Ackermann-like function here

#### [ Edward Ayers (Sep 25 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583167):
Ok I think I see what you mean now. You want a pair `p(n), q(m,n)` where the existence of  a satisfying `m`is proved using AC or LEM.

#### [ Mario Carneiro (Sep 25 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583218):
exactly

#### [ Johan Commelin (Sep 25 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583321):
Can you prove that such a function exists using AC?

#### [ Mario Carneiro (Sep 25 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583382):
You can use whatever methods you like to prove the existence of such p and q, but they have to be computable functions

#### [ Johan Commelin (Sep 25 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583448):
Ok, I should have put more emphasis on *you* in my last post (-;

#### [ Johan Commelin (Sep 25 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583453):
I have no clue at all about all this computability stuff.

#### [ Mario Carneiro (Sep 25 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583461):
I don't have a solution to this puzzle

#### [ Mario Carneiro (Sep 25 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583474):
but I believe it is possible

#### [ Edward Ayers (Sep 25 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583532):
I am still not satisfied that the question is well posed. If I found a `p` and `q` with that property. I could take the AC proof, throw it away and replace it with a machine that just tries all `m`. Eventually it would find the `m` (which I know but Lean doesn't) and Lean would use that. But then I guess my new program would have to run in unsafe mode.

#### [ Mario Carneiro (Sep 25 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583545):
For a fixed `n` you can do that, but I don't think you can do that for all `n`

#### [ Mario Carneiro (Sep 25 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583553):
i.e. if `p(5)` is true and it turns out that `q(100,5)` is the satisfying instance, then you can use an upper bound of 100 in the construction

#### [ Johan Commelin (Sep 25 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583554):
Mario, do you want a proof that can only prove the upper bound under the assumption of LEM/AC?

#### [ Mario Carneiro (Sep 25 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583555):
right

#### [ Johan Commelin (Sep 25 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583557):
Or is it enough that we know no such proof.

#### [ Mario Carneiro (Sep 25 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583599):
Even that would be nice

#### [ Mario Carneiro (Sep 25 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583615):
I'm worried that since no axioms lean has the same consistency strength as lean + AC, it will not be able to prove any new turing machines halt

#### [ Johan Commelin (Sep 25 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583617):
So, there are only finitely many abelian varieties of dimension `g` over `rat` with good reduction outside `{favourite finite list of primes}`.

#### [ Johan Commelin (Sep 25 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583631):
I don't think we know any upper bounds on this. The proof is a celebrated theorem of Faltings and uses classical maths all over the place.

#### [ Johan Commelin (Sep 25 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583668):
If your favourite finite list of primes is not empty, then this function is extremely hard to compute.

#### [ Johan Commelin (Sep 25 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583691):
(Otherwise it is `if g = 0 then 1 else 0`.)

#### [ Johan Commelin (Sep 25 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583717):
Does this mean that `f g = card (abelian varieties of dim g with good reduction outside blah)` is not computable?

#### [ Johan Commelin (Sep 25 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583767):
Hmmm.... I'm too much of a newbie when it comes to such questions.

#### [ Mario Carneiro (Sep 25 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583893):
hm, this theorem has AEA quantifier complexity, which is a bit hard to use

#### [ Johan Commelin (Sep 25 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583936):
AEA?

#### [ Johan Commelin (Sep 25 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583941):
`\forall \exists \forall`?

#### [ Mario Carneiro (Sep 25 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583954):
"for all g, there exists an n such that all variety things don't have good reduction above n"

#### [ Johan Commelin (Sep 25 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583971):
No, I don't think that's what it says.

#### [ Mario Carneiro (Sep 25 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583978):
I assume there is a way to enumerate abelian varieties?

#### [ Mario Carneiro (Sep 25 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584022):
and the theorem says this enumeration runs dry after a certain point

#### [ Johan Commelin (Sep 25 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584026):
For all `P : finset primes` and for all `g` there exists `n` such that `card { abvar of dim g and good reduction outside P }` is less than `n`.

#### [ Johan Commelin (Sep 25 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584031):
Well, an abelian variety is defined by a finite number of polynomials

#### [ Mario Carneiro (Sep 25 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584040):
right, so we enumerate all such things

#### [ Mario Carneiro (Sep 25 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584042):
and only a finite number of them will have good reduction

#### [ Johan Commelin (Sep 25 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584046):
Right (the polys are over Q), so we could do that.

#### [ Mario Carneiro (Sep 25 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584054):
so there is an upper bound on the last one with good reduction

#### [ Mario Carneiro (Sep 25 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584057):
thus AEA

#### [ Johan Commelin (Sep 25 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584061):
Right, but testing the good reduction has to happen at all primes outside `P`

#### [ Johan Commelin (Sep 25 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584107):
So you can't enumerate that.

#### [ Mario Carneiro (Sep 25 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584120):
oh, I see

#### [ Johan Commelin (Sep 25 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584123):
But I guess you can compute some discriminant in terms of the polynomials

#### [ Mario Carneiro (Sep 25 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584125):
the property of having good reduction depends on all p?

#### [ Johan Commelin (Sep 25 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584132):
and then bad reduction at `p` implies that `p` divides the discriminant.

#### [ Johan Commelin (Sep 25 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584139):
This works for elliptic curves (the case `g = 1`)

#### [ Mario Carneiro (Sep 25 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584145):
then it is AEAE

#### [ Johan Commelin (Sep 25 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584146):
Lol

#### [ Mario Carneiro (Sep 25 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584154):
for all g/P, there exists n, such that for all abvars above n, there is a p such that the var has bad reduction at p

#### [ Johan Commelin (Sep 25 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584195):
No, it isn't about abvars above `n`, I think.

#### [ Johan Commelin (Sep 25 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584196):
At least I can't parse that.

#### [ Johan Commelin (Sep 25 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584200):
Ooh, wait, you enumerated them

#### [ Mario Carneiro (Sep 25 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584204):
that is to exclude the finite number of things with good reduction

#### [ Johan Commelin (Sep 25 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584212):
Hmmm.... but we still need a decision procedure to determine if a bunch of polynomials defines an AV

#### [ Mario Carneiro (Sep 25 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584213):
that's surely decidable

#### [ Johan Commelin (Sep 25 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584220):
Ok, if you say so... I have no idea how to do that...

#### [ Mario Carneiro (Sep 25 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584232):
I have no idea what an AV is, so there

#### [ Mario Carneiro (Sep 25 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584277):
but it surely can't be more than AE complexity

#### [ Johan Commelin (Sep 25 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584296):
It means that there exists a group structure on the solution set defined by the polynomials, and the solution set must be compact (in the algebro-geometric sense of compact)

#### [ Johan Commelin (Sep 25 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584330):
Both seem hard to check at first sight.

#### [ Edward Ayers (Sep 25 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584389):
```quote
For a fixed `n` you can do that, but I don't think you can do that for all `n`
```
Is this argument on the right lines?
If `p` and `q` are computable and we know that  for all `n`, if `p(n)` then there exists a `m` such that `q(m,n)`. Then there exists a computable function `n -> m` using AC. So I can find the code which runs that function, and put that in Lean. So `n` doesn't have to be fixed.

#### [ Mario Carneiro (Sep 25 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584411):
but the code that runs that function uses AC

#### [ Mario Carneiro (Sep 25 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584419):
oh you mean the code of a computable function

#### [ Edward Ayers (Sep 25 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584420):
Right but I can find the code outside Lean and just put the code in

#### [ Mario Carneiro (Sep 25 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584427):
but then you need to know it codes a (total) computable function

#### [ Mario Carneiro (Sep 25 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584429):
and the proof of that uses AC

#### [ Mario Carneiro (Sep 25 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584479):
lean won't just let you run whatever function you like

#### [ Edward Ayers (Sep 25 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584498):
I can run the n->m in unsafe mode because it's not part of the proof. I just need to get the `m`

#### [ Mario Carneiro (Sep 25 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584554):
the idea with this reduction is to build a computable function in no axioms lean, right? You can't run in unsafe mode since then you don't have a well defined term

#### [ Mario Carneiro (Sep 25 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584582):
i.e. the `m` that you pick depends on `n`, so there is no closed term you can give for the function without unsafe lean stepping in to provide the `m`

#### [ Jared Corduan (Sep 25 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134618450):
how about this:
let `A(n)` be some computable predicate that requires either `AC` or `LEM` to show that either `{n | A(n)}` or `{n | ~A(n)}`is infinite.  (in other words, `A` witnesses the nonconstructive nature of the infinite pigeon hole principle).

then let `q1(m, n)` be the statement that there is an `n < x < m` such that `A(x)` holds. and similarly define `q2(m, n)` with `~A(x)`.  both of these are computable since `A` is computable.  since either `{n | A(n)}` or `{n | ~A(n)}`is infinite, then for at least one of `q1` or `q2`we can show the existence of such an `m` for any given `n`.  but we need `AC` or `LEM` for the existence of the `m`s.

#### [ Kenny Lau (Sep 25 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134618503):
is there a tl;dr for this thread?

#### [ Patrick Massot (Sep 25 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134618569):
Do you really want me to write it?

#### [ Kenny Lau (Sep 25 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134618618):
well this thread is way too long, a tl;dr would be good, I don't see why not

#### [ Patrick Massot (Sep 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134618657):
Ok, let me try: constructivity questions are pointless.

#### [ Kenny Lau (Sep 25 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134618804):
I don't think that's a very faithful summary, nor is it contributing to the discussion at hand

#### [ Patrick Massot (Sep 25 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134618832):
I'm sorry, but you explicitly asked for it!

#### [ Patrick Massot (Sep 25 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134618922):
Anyway, I should work instead of trolling

#### [ Mario Carneiro (Sep 25 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134618948):
I don't think that works, although it's so close I can taste it. What is the computable function that we are defining?

#### [ Mario Carneiro (Sep 25 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619027):
(Kenny, the gist is I posed a puzzle [here](https://leanprover.zulipchat.com/#narrow/stream/113489-new-members/subject/mathlib.20.26.20constructivity/near/134580592) and people are trying to solve it.)

#### [ Jared Corduan (Sep 25 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619086):
well, it's one of two functions.  either 1) it is `f(n)` is the least `m>n`such that `A(n)` or 2) it is `f(n)` is the least `m>n`such that `~A(n)`.

#### [ Jared Corduan (Sep 25 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619105):
but I punted on giving you an actual `A`...

#### [ Mario Carneiro (Sep 25 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619126):
But we can't define either of those functions unless we have a proof (possibly using AC) that A(n) is infinite (resp. co-infinite)

#### [ Jared Corduan (Sep 25 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619199):
you can prove the infinite pigeon hole with `AC` and `LEM`, so all I'm missing is a good `A`, right?

#### [ Mario Carneiro (Sep 25 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619312):
right, but if we assume `A` is something about which we can prove very little, then we can't prove `A(n)` is infinite, so 1) can't be defined, and we can't prove `~A(n)` is infinite either, so 2) can't be defined

#### [ Chris Hughes (Sep 25 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619345):
What's the constructive proof that there exists a natural such that a^n=1 in a finite group?

#### [ Mario Carneiro (Sep 25 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619367):
If it is finite, then there is an upper bound on the cardinality, enumerate them all and test for equality

#### [ Mario Carneiro (Sep 25 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619409):
(you need decidable equality)

#### [ Jared Corduan (Sep 25 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619454):
ok, I might have misunderstood the problem!  I thought we wanted an `f` that needed `AC` and/or `LEM` in order to be defined, though it was built from these computable predicates.

#### [ Mario Carneiro (Sep 25 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619495):
That is what we want, but it also needs to be a term that represents a lean-computable function

#### [ Mario Carneiro (Sep 25 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619527):
It is okay if the proof of existence of the term is nonconstructive, like you tried, but the term itself must contain a proof that it halts since lean expects as much

#### [ Jared Corduan (Sep 25 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619598):
ah ok, I'll have to think about that some more!

#### [ Reid Barton (Sep 25 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134620571):
Could we do something like this? Inside Lean, build a language for programs in STLC or another system which Lean can prove is strongly normalizing, but incorporating the type $$\hat \mathbb{N}$$ = nondecreasing functions nat -> bool. Then the input to our function is a code for a function `f` from $$\hat \mathbb{N}$$ to `bool` together with a proof that `f inf = tt` (where `inf` $$\in \hat \mathbb{N}$$ is the constant function `ff`); we can enumerate such programs because the system is strongly terminating. In Lean+LEM, we can prove that every such function satisfies `f n = tt` for some finite `n`, and we ask that our function return the smallest such `n`.

#### [ Reid Barton (Sep 25 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134620748):
Actually we don't even need the type $$\hat \mathbb{N}$$, we can just use the whole type `nat -> bool`, but with the same idea.

#### [ Reid Barton (Sep 25 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134620778):
If `f (const ff) = tt`, then there must be some finite `n` such that `f (\lam x, x > n) = tt`.

#### [ Reid Barton (Sep 25 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134620813):
Then we seek `g f = ` the least `n` for which the above holds, provided that `f (const ff) = tt`, otherwise 37

#### [ Reid Barton (Sep 25 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134620905):
(Compare http://math.andrej.com/2007/09/28/seemingly-impossible-functional-programs/)

#### [ Reid Barton (Sep 25 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134620946):
Maybe this is actually still computable without LEM though

#### [ Reid Barton (Sep 25 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134621676):
Yeah, I doubt this can be made to work. If you can constructively define a normalizer for your language, then you can presumably modify it to keep track of the invocations of the argument, and return the largest number on which it is invoked, then search up to there. If you can't constructively define a normalizer for your language, then you should just use a normalizer for your language as the function we're looking for.

#### [ Mario Carneiro (Sep 25 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134622225):
Note that one way to "cheat" here is to have as input a nondecidable proposition, which you then use in the construction. I did something similar with my example of a function that takes as input a function that is not constant zero and returns a value in the range

#### [ Mario Carneiro (Sep 25 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134622939):
Here again we seem to be stuck: if we use STLC or something provably normalizing, then we won't need LEM to prove the compactness property, and if we use DTT functions then even AC won't help since compactness isn't provable (though true)

#### [ Reid Barton (Sep 25 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623070):
Yes. We would need a language whose power is just right so that the proof of normalization requires LEM, which I have no idea how to go about (or whether it is even plausible that such a language could exist).

#### [ Reid Barton (Sep 25 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623309):
Can we prove that Lean-with-N-universes is normalizing inside Lean-with-N+1-universes? What do we know about the relative consistency of AC?

#### [ Reid Barton (Sep 25 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623359):
Any term of type `nat -> nat` is equal (in a meta sense) to one defined without using universe variables right?

#### [ Mario Carneiro (Sep 25 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623378):
I believe that Con(CIC+AC) = Con(CIC) for the same reasons as Con(ZF) = Con(ZFC)

#### [ Reid Barton (Sep 25 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623467):
I wonder whether we can just describe a meta-level procedure for taking a function defined in Lean+AC and producing an equal one defined in Lean (using one more universe) explicitly

#### [ Mario Carneiro (Sep 25 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623469):
I believe that lean-with-n-universes is normalizing in n+1 universes

#### [ Mario Carneiro (Sep 25 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623492):
I have to prove that lean is normalizing first though :)

#### [ Mario Carneiro (Sep 25 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623545):
any term of type nat -> nat may contain universe variables but is parametric in them, so you get the same result no matter what they are set to

#### [ Kenny Lau (Sep 25 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623572):
```quote
Any term of type `nat -> nat` is equal (in a meta sense) to one defined without using universe variables right?
```
I heard FLT uses universes

#### [ Kenny Lau (Sep 25 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623574):
Fermat's Last Theorem

#### [ Reid Barton (Sep 25 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623625):
by writing an evaluator for Lean+AC-in-N-universes in Lean-in-N+1-universes, and then at the meta level looking to see how many universes are actually used, picking N to be bigger than that and writing down a term in the model that corresponds to the given function

#### [ Mario Carneiro (Sep 25 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623652):
It may be that even without any universe variables you still need type 3 or something in the term

#### [ Mario Carneiro (Sep 25 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623655):
(re: kenny)

#### [ Kenny Lau (Sep 25 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623688):
but is it just because nobody has cleaned up the proof yet?

#### [ Kenny Lau (Sep 25 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623694):
do we really need type 3?

#### [ Reid Barton (Sep 25 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623702):
Kenny is taking over for Patrick on trolling duty

#### [ Kenny Lau (Sep 25 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623811):
i'm serious

#### [ Mario Carneiro (Sep 25 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623831):
We know that ZFC is equiconsistent with ZF, but I think that may include a double negation translation

#### [ Mario Carneiro (Sep 25 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623845):
(if you use IZF in place of ZF)

#### [ Reid Barton (Sep 25 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623878):
```quote
I believe that Con(CIC+AC) = Con(CIC) for the same reasons as Con(ZF) = Con(ZFC)
```
This is unclear to me because, in the case of ZF, we start from classical logic, at least in the version I know. But that's not to say that LEM is required for the relative consistency, only that I don't know whether it is.

#### [ Mario Carneiro (Sep 25 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623955):
I also know that classical prop calc is equiconsistent with intuitionistic

#### [ Reid Barton (Sep 25 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134624102):
@**Kenny Lau** https://mathoverflow.net/questions/35746/inaccessible-cardinals-and-andrew-wiless-proof (See the first few answers.)

#### [ Reid Barton (Sep 25 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134624631):
Mario, right, that seems plausible then.

#### [ Kevin Buzzard (Sep 26 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134652603):
```quote
What's the constructive proof that there exists a natural such that a^n=1 in a finite group?
```
Let n be the order of the group ;-)

#### [ Kevin Buzzard (Sep 26 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134652674):
```quote
```quote
Any term of type `nat -> nat` is equal (in a meta sense) to one defined without using universe variables right?
```
I heard FLT uses universes
```
Kenny that is fake news, but the rumour seems hard to kill. Some people might argue that "the proof is written using universes" (because at some point Wiles says the word "representable functor" and at some other point uses etale cohomology) but they can easily be expunged using standard tricks.


{% endraw %}
