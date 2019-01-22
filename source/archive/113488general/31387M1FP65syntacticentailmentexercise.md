---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31387M1FP65syntacticentailmentexercise.html
---

## [general](index.html)
### [(M1F/P65) syntactic entailment exercise](31387M1FP65syntacticentailmentexercise.html)

#### [Kevin Buzzard (Oct 22 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136257251):
At Imperial in the 3rd year logic course M3P65 they're doing first order propositional logic, soundness and completeness etc. In a guest M1F lecture (my course) John Britnell went through some of this stuff with the first years, and the last question on his problem sheet was a real stinker. @**Abhimanyu Pallavi Sudhir** [asked about it on math SE](https://math.stackexchange.com/questions/2962525/derive-simple-logical-laws-in-a-structure-with-not-and-implies) and got what looks like a couple of nice answers. I'd like the stufents to check those answers in Lean but I'd like to make it as easy as possible for them, by setting up the underlying infrastructure, so they have easy access to the axioms, and only the axioms. 

I can think of several ways that one could try to do this (make a new inductive type for propositions-in-the-sense-of-this-question and then input the axioms as axioms, or make a structure somehow with the axioms inbuilt as part of the structure). It would be nice to get some views on the best way to set up this sort of puzzle. The idea would be for the students to formalise the answers posted on MO within the framework (a skeleton lean file or an import) which I provide them, with them not having to worry about setting up notation or whatever (I am assuming that we can't using inbuilt not and arrow for our two inbuilt constructors).

#### [Kevin Buzzard (Oct 22 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136257538):
And here's a question which exposes my own ignorance on the subject: if we can check that `P → (¬ (¬ P))` using the "it's true if P is true and true if P is false so it's true" method (semantic entailment?) then does the completeness theorem actually construct a proof of this proposition from the three axioms in the question, or does the compactness argument render the entire thing necessarily nonconstructive (i.e. it only shows "there exists a term of this type" rather than "here is a term of this type")?

#### [Gabriel Ebner (Oct 22 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136258425):
The typical completeness proof is a proof by contradiction.  You can complete any set of (syntactically) consistent formulas into a maximally consistent set (for every formula `φ`, you iteratively add either `φ` or `¬ φ` so that the set stays consistent), which then gives you a model.  Your statement is then the contrapositive: there are no counterexamples, so the (singleton) set `{¬ (p → ¬ ¬ p)}` must be inconsistent.  I don't think that *this* proof gives you a proof.

#### [Gabriel Ebner (Oct 22 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136258577):
However it's not "necessarily" nonconstructive for a single propositional formula.  You can of course just produce a proof by case analysis (just do the "if p is true, then ..., if p is false, ...." in the proof).

#### [Kevin Buzzard (Oct 22 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136258683):
Thanks Gabriel! Now I realise that one can make it constructive by proving the proof exists and then just searching through all proofs to find it, knowing your search will terminate.

#### [Kevin Buzzard (Oct 22 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136258693):
So perhaps the interesting question is the best running time one can hope for, if I've understood all this correctly.

#### [Gabriel Ebner (Oct 22 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136258696):
Propositional validity is coNP-complete.

#### [Kevin Buzzard (Oct 22 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136259027):
Math is hard

#### [Gabriel Ebner (Oct 22 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136259350):
Regarding the original question, I think inductive type for formulas and proofs is the way to go.  For inspiration, there are at least 2 logical formalizations in lean that I know of: https://github.com/skbaek/fol/blob/master/frm.lean and https://github.com/avigad/formal_logic
Personally I'm not a big fan of writing concrete Hilbert-style proofs as exercises.  I've found it to be much more instructive to show how to derive rules that allow you to simulate saner proof systems; e.g. the deduction theorem or even simple rules such as `p → q → r ⇒ q → p → r`.

#### [Kevin Buzzard (Oct 22 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136259545):
Gabriel I am a complete novice coming to this stuff. I guess I have no idea what is instructive -- because these questions are in the air in the maths department at Imperial I just decided it was time to get to the bottom of how it all worked.

#### [Kevin Buzzard (Oct 22 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136259551):
Here's an approach based on axioms, which I thought might be promising but got scary at the end:

```lean
constant prop : Type

constant impl : prop → prop → prop

-- I am assuming overwriting → is not recommended
local infix `~>`:50 := impl 

constant pnot : prop → prop

local notation ¬ := pnot

constant entails : set (prop) → prop → Prop

local infix ⊢ := entails

axiom A1 : ∀ P Q : prop, entails {P,Q} (P ~> (Q ~> P))

-- plus two other axioms

-- and now I need modus ponens or something?

-- am I missing a trick?
```

#### [Gabriel Ebner (Oct 22 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136259786):
You probably want `∅ ⊢ (P ~> (Q ~> P))`.

#### [Kevin Buzzard (Oct 22 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136259808):
@**Kenny Lau** @**Chris Hughes**  is it possible to make a simple framework in Lean where first years could work on [the M1F question in the MSE post](https://math.stackexchange.com/questions/2962525/derive-simple-logical-laws-in-a-structure-with-not-and-implies)? I find the files in Gabriel's links a bit daunting.

#### [Kevin Buzzard (Oct 22 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136259887):
Or could I use those files without understanding them somehow?

#### [Gabriel Ebner (Oct 22 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136260159):
If you just want a Hilbert calculus for propositional logic, then it's only two inductive types:
```lean
inductive fml
| atom (i : ℕ)
| imp (a b : fml)
open fml

infixr ` →' `:50 := imp

inductive prf : fml → Type
| axk (p q) : prf (p →' q →' p)
| axs (p q r) : prf $ (p →' q →' r) →' (p →' q) →' (p →' r)
| mp (p q) : prf p → prf (p →' q) → prf q
```
You can add negation if you want, but there should be enough examples in the implication-only fragment.

#### [Kevin Buzzard (Oct 22 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136261299):
@**Abhimanyu Pallavi Sudhir**  I've got it up and running.

https://gist.github.com/kbuzzard/15a40e59ce815b69a0dcc983935abc83

I've proved P implies P :-)

#### [Kevin Buzzard (Oct 22 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136261336):
Thanks so much @**Gabriel Ebner** , I think I can take it from here.

#### [Abhimanyu Pallavi Sudhir (Oct 22 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136261394):
```quote
@**Abhimanyu Pallavi Sudhir**  I've got it up and running.

https://gist.github.com/kbuzzard/15a40e59ce815b69a0dcc983935abc83

I've proved P implies P :-)
```
Darn, I was trying to beat you to it.

#### [Abhimanyu Pallavi Sudhir (Oct 22 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136261397):
I'm almost done myself.

#### [Kevin Buzzard (Oct 22 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136261420):
:-)

#### [Kevin Buzzard (Oct 22 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136261429):
Well there's still a race on for P implies not not P :-)

#### [Kevin Buzzard (Oct 22 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136261510):
github being a bit unreliable at the minute -- I think they had a bit of a minor disaster earlier today. Here's the proof.

```lean
inductive fml
| atom (i : ℕ)
| imp (a b : fml)
| not (a : fml)

open fml

infixr ` →' `:50 := imp -- right associative
local notation ¬ := fml.not

inductive prf : fml → Type
| axk (p q) : prf (p →' q →' p)
| axs (p q r) : prf $ (p →' q →' r) →' (p →' q) →' (p →' r)
| axX (p q) : prf $ (¬q →' ¬p) →' p →' q
| mp (p q) : prf p → prf (p →' q) → prf q

open prf

lemma pqpp (p q : fml) : prf $ (p →' q) →' (p →' p) :=
begin
  apply mp (p →' q →' p) ((p →' q) →' p →' p) (axk p q),
  exact axs p q p
end

theorem p_implies_p (p : fml) : prf $ p →' p :=
begin
  exact mp (p →' p →' p) (p →' p) (axk p p) (pqpp p (p →' p)), 
end
```

#### [Kevin Buzzard (Oct 22 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136261545):
Gabriel called the axioms `axk` and `axs` but he left the negation one out (and indeed I never used it). I called it `axX` but I'm wondering where there is standard CS code for these axioms. `mp` I know is modus ponens.

#### [Abhimanyu Pallavi Sudhir (Oct 22 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136261975):
Mine is essentially the same too but with `have`s instead of lemmas.

```lean
theorem reflex (P : fml) : prf (P →' P) :=
    begin
        have R : fml, exact P,
        let Q : fml := R →' P,
        have HPQ : prf (P →' Q),
            change prf (P →' (R →' P)),
            apply prf.axk,
        have HPQP : prf (P →' (Q →' P)),
            apply prf.axk,
        have HPQPP : prf ((P →' Q) →' (P →' P)),
            apply prf.mp (P →' Q →' P),
            exact HPQP,
            apply prf.axs,
        apply prf.mp (P →' Q),
        exact HPQ,
        exact HPQPP,
    end
```

#### [Abhimanyu Pallavi Sudhir (Oct 22 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262078):
Btw is it a good idea to reuse `¬`? Shouldn't we use a variant like `¬'` as Gabriel Ebner did?

#### [Kevin Buzzard (Oct 22 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262110):
So this is a weird thing about computer scientists -- they like to do proofs backwards. Almost all tactics operate on the goal. If you have proofs of `A`, `A -> B`, `B -> C` and `C -> D` and your goal is `D`, a mathematician in a lecture might say "well first we can prove B, then we can deduce C, and then finally we can deduce D so done". If you write all of this in one theorem in Lean, in that order, you end up with a bunch of intermediate extra terms in your context which you only ever use once and then would really rather throw away because for big proofs all these extra junk terms just start getting in the way and making your goal scroll off the bottom of the screen.

#### [Kevin Buzzard (Oct 22 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262160):
So there are two other ways of doing things. Either prove B and C as lemmas before you embark on a proof of D, or just write the entire proof backwards and change the goal from D to C to B to A with `apply` and then use `assumption` at the end.

#### [Johan Commelin (Oct 22 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262192):
Well, there is `suffices`.

#### [Kevin Buzzard (Oct 22 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262196):
Because going backwards is not always intuitive, the "lots of lemmas" approach becomes more appealing. And for other reasons too it's preferable to break your proofs up into as small chunks as you can.

#### [Kevin Buzzard (Oct 22 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262250):
`suffices` is still going backwards, right?

#### [Johan Commelin (Oct 22 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262258):
Hmmm, yes, I guess it is.

#### [Kevin Buzzard (Oct 22 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262335):
```quote
Btw is it a good idea to reuse `¬`? Shouldn't we use a variant like `¬'` as Gabriel Ebner did?
```
I have no idea if it's a good idea to reuse `¬`. I was 100% convinced that it was a bad idea to reuse `→` and I like Gabriel's idea of the apostrophe -- I think this is a CS meme or something.

#### [Kevin Buzzard (Oct 22 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262435):
grr I wish github was working, I have everything locally in a git repo and am having trouble pushing.

#### [Kevin Buzzard (Oct 22 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262677):
@**Abhimanyu Pallavi Sudhir** https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/tree/master/src you could just edit that file (as could anyone else who wants to work on this)

#### [Kevin Buzzard (Oct 22 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262684):
@**Alexandru-Andrei Bosinta** There's my proof that P implies P

#### [Kevin Buzzard (Oct 22 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262985):
Meh still GH problems (also having trouble with gists). Current version of framework, with example proof, is here (I took Abhi's advice and changed not to not'):

```lean
inductive fml
| atom (i : ℕ)
| imp (a b : fml)
| not (a : fml)

open fml

infixr ` →' `:50 := imp -- right associative

notation `¬' ` := fml.not


inductive prf : fml → Type
| axk (p q) : prf (p →' q →' p)
| axs (p q r) : prf $ (p →' q →' r) →' (p →' q) →' (p →' r)
| axX (p q) : prf $ ((¬' q) →' (¬' p)) →' p →' q
| mp (p q) : prf p → prf (p →' q) → prf q

open prf

lemma p_of_p_of_p_of_q (p q : fml) : prf $ (p →' q) →' (p →' p) :=
begin
  apply mp (p →' q →' p) ((p →' q) →' p →' p) (axk p q),
  exact axs p q p
end

lemma p_of_p_of_p_of_q' (p q : fml) : prf $ (p →' q) →' (p →' p) :=
mp (p →' q →' p) ((p →' q) →' p →' p) (axk p q) (axs p q p)

theorem p_of_p (p : fml) : prf $ p →' p :=
begin
  exact mp (p →' p →' p) (p →' p) (axk p p) (p_of_p_of_p_of_q p (p →' p)), 
end
```

#### [Kevin Buzzard (Oct 22 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262996):
I also added a term proof for the first lemma

#### [Kevin Buzzard (Oct 22 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136263023):
Note : `$` is a clever CS trick which can be used in place of brackets sometimes (it's a clever trick to do with BIDMAS / operator precedence)

#### [Gabriel Ebner (Oct 22 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136264746):
I copied the apostrophe directly from Seul's formalization, but yeah indeed, apostrophe, tilde, hat, etc. are all common modifiers.

#### [Andrew Ashworth (Oct 22 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136265032):
```quote
So this is a weird thing about computer scientists -- they like to do proofs backwards. Almost all tactics operate on the goal. If you have proofs of `A`, `A -> B`, `B -> C` and `C -> D` and your goal is `D`, a mathematician in a lecture might say "well first we can prove B, then we can deduce C, and then finally we can deduce D so done". If you write all of this in one theorem in Lean, in that order, you end up with a bunch of intermediate extra terms in your context which you only ever use once and then would really rather throw away because for big proofs all these extra junk terms just start getting in the way and making your goal scroll off the bottom of the screen.
```
I know this isn't a good workaround, but you might try anonymous `have` statements.

#### [Gabriel Ebner (Oct 22 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136265228):
> Gabriel called the axioms axk and axs but he left the negation one out (and indeed I never used it). I called it  axX but I'm wondering where there is standard CS code for these axioms. mp I know is modus ponens.

This naming scheme is indeed rooted in a very fundamental observation in computer science, namely the Curry-Howard isomorphism.  This isomorphism maps formulas to types, and proofs to programs.  The Hilbert calculus for propositional logic that we consider here is mapped to the simply-typed [combinator calculus](https://en.wikipedia.org/wiki/SKI_combinator_calculus); and just as I hope that nobody is writing programs in combinator calculus, hopefully only hardcore freaks are writing proofs in Hilbert calculus.  To come back to the naming: as you might have noticed the propositions derived by these two axioms are exactly the types of the K and S combinators:
```lean
#check combinator.K
-- combinator.K : ?M_1 → ?M_2 → ?M_1
#check combinator.S
-- combinator.S : (?M_1 → ?M_2 → ?M_3) → (?M_1 → ?M_2) → ?M_1 → ?M_3
```

#### [Kevin Buzzard (Oct 22 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136265229):
They still pile up. I guess what a mathematician would like is a tactic which actually deletes hypotheses `HA : A` and `HAB : A -> B` from the context and adds a new hypothesis `HB : B`. That's very much how I'm thinking about these things. Of course there's the risk you'll need the hypotheses later but in my experience there are times you know for sure you won't.

#### [Kevin Buzzard (Oct 22 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136265369):
This combinator business is so cool. Thanks Gabriel. They don't teach any of this stuff in maths departments usually -- just a couple of lectures on the completeness theorem and then let's get on to proper stuff like ZFC.

#### [Rob Lewis (Oct 22 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136268664):
Kevin, are you aware of the `replace` tactic? It has some of the behavior you want.
```lean
import tactic.interactive

example (A B : Prop) (ha : A) (hab : A → B) : true :=
begin 
  replace ha := hab ha, -- now we have hab : B
end 

example (A B C : Prop) (ha : A) (hab : A → B) (hbc : B → C) : C :=
begin 
  have : A, from ha, -- this : A
  replace := hab this, -- this : B
  replace := hbc this, -- this : C
  exact this
end
```
But in general, I think of forward reasoning as a term mode thing. Unless you're using tactics that search for things in the local context, there's nothing wrong with having lots of hypotheses around, other than that they clutter the goal view. If you're working in term mode, you don't need the goal view, and your hypotheses are all visible all the time because they're part of your proof script.

#### [Rob Lewis (Oct 22 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136268701):
e.g. the proof that @**Abhimanyu Pallavi Sudhir** posted above is really a term mode proof until the very end.

#### [Kevin Buzzard (Oct 22 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136269931):
That's an interesting point. I teach mathematicians tactic mode from the very start because I think it's much easier for them to grasp than term mode. I always forget about the `replace` tactic -- I always remember it starts `re`something and then it always autocompletes in my brain to `rewrite`.

#### [Johan Commelin (Oct 22 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136270252):
Otoh in our minds we definitely don't think of it as `replace`ing an assumption.

#### [Johan Commelin (Oct 22 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136270296):
In our minds what is really going on is `have b : B := hab a, clear a hab,`

#### [Chris Hughes (Oct 22 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136271125):
Is this a proof?
```lean
import data.fintype
variables (imp : bool → bool → bool) (n : bool → bool) 
  (a1 : ∀ p q, imp p (imp p q) = tt) 
  (a2 : ∀ p q, imp (imp (n p) (n q)) (imp p q) = tt) 
  (a3 : ∀ p q r, imp (imp p (imp q r)) (imp (imp p q) (imp q r)) = tt)
include a1 a2 a3

set_option class.instance_max_depth 50

example : ∀ p, imp p (n (n p)) = tt :=
by revert imp n; exact dec_trivial
```

#### [Kevin Buzzard (Oct 22 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136271635):
No, that doesn't count.

#### [Kevin Buzzard (Oct 22 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136272090):
[IMG_20181019_134013644.jpg](/user_uploads/3121/RzZ8ETr6cUDU63MzUV9zWyXp/IMG_20181019_134013644.jpg) [IMG_20181019_134020093.jpg](/user_uploads/3121/j9yYOt0hVLqosT3niylQup03/IMG_20181019_134020093.jpg) Chris -- you are assuming the completeness theorem, namely that the stuff which the axioms prove is exactly the stuff which is true. In 3rd year logic they're proving this sort of thing right now.

#### [Chris Hughes (Oct 22 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136272377):
What's the definition of true?

#### [Kevin Buzzard (Oct 22 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136272981):
Whilst there are many here who can explain all of this better than me, my memory of what I was taught in undergraduate logic was this. You can _prove_ statements by deducing them from the axioms using modus ponens. Note that the axioms aren't constructive logic because we have that extra one about not Q implies not P which is I believe is equivalent to LEM in the presence of the other two axioms. A statement is _true_ if whenever you evaluate all your variables as booleans and interpret -> and not as following the truth tables, it evaluates to true. You have seen enough constructive mathematics to know that "always evaluates to true" a.k.a. "true in every model" is not the same as "being provable from a random set of axioms", especially if the axioms are those of constructive logic. The key thing here is that if we add that third axiom, then the true things and the provable things coincide. This is the completeness theorem.

#### [Chris Hughes (Oct 22 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136272996):
I know what provable means. What does true mean?

#### [Kevin Buzzard (Oct 22 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273011):
it means "always evaluates to true whenever we map the propositions to bools"

#### [Kevin Buzzard (Oct 22 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273085):
A _model_ of a bunch of statements involving propositions p q r etc is just an assignment of a boolean value to each of the variables p q retc so that all the statements become true.

#### [Kevin Buzzard (Oct 22 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273227):
A bunch of propositions involving a set of variables _semantically entails_ another proposition X if, for every model where the bunch of propositions all evaluate to true, the proposition X also evaluates to true.

A bunch of propositions _syntactially entails_ another proposition X if you can use the axioms and modus ponens to deduce X from the bunch of propositions. This depends on your axioms of course.

The theorem is that for the axioms on the poor photos I sent you, the two notions are the same. If I've remembered everything correctly...

#### [Chris Hughes (Oct 22 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273242):
By this definition, true + em -> provable, though right?

#### [Kevin Buzzard (Oct 22 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273257):
When you say "provable" you have to say which axioms we're using

#### [Kevin Buzzard (Oct 22 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273320):
"true" is an absolute thing, stuff like p -> p is true because T -> T and F -> F

#### [Kevin Buzzard (Oct 22 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273341):
This is the same as "provable using the axioms of classical logic" (the completeness theorem) but not the same as "provable using the axioms of constructive logic" (the law of the excluded middle being a counterexample)

#### [Kevin Buzzard (Oct 22 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273430):
I only have the most tenuous understanding of this stuff now, so please someone butt in if I'm talking nonsense.

#### [Rob Lewis (Oct 22 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273434):
```quote
"true" is an absolute thing, stuff like p -> p is true because T -> T and F -> F
```
To nitpick: to say "true" you have to say what semantics we're using. Excluded middle isn't true in Kripke semantics for propositional logic.

#### [Simon Cruanes (Oct 22 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273435):
When you move to higher-order logic and interpret function types as function spaces, then provability is always weaker than semantic truth, sadly.

#### [Rob Lewis (Oct 22 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273456):
But Chris, feel free to ignore me complicating the story for now. :)

#### [Kevin Buzzard (Oct 22 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273479):
```quote
To nitpick: to say "true" you have to say what semantics we're using.
```
What semantics am I using?

#### [Kevin Buzzard (Oct 22 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273546):
Are my semantics something like "bool is the set of values, and here's the truth table for ->, and here's the truth table for not"?

#### [Rob Lewis (Oct 22 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273554):
Boolean semantics? Truth table semantics? I'm blanking on a standard name.

#### [Rob Lewis (Oct 22 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273559):
Exactly.

#### [Kevin Buzzard (Oct 22 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273575):
I would have understood the logic course *much* better when I was an UG if I could have done the course in Lean.

#### [Rob Lewis (Oct 22 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273646):
Intuitionistic logic is sound but not complete for those semantics. So you end up with Kripke semantics, a different way of interpreting true/false under which the true formulas coincide with the intuitionistically provable ones.

#### [Kevin Buzzard (Oct 22 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273691):
I see. So you're saying there is a completeness theorem for constructive logic.

#### [Rob Lewis (Oct 22 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273888):
Yeah, but it's not as intuitive (ha ha) as for classical logic. https://plato.stanford.edu/entries/logic-intuitionistic/#BasSem

#### [Simon Cruanes (Oct 22 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273961):
I don't know much about constructive semantics, but there are things like "reducibility candidates" in this area I believe?
edit: ah neat, if there's an entry in the encyclopedia already, nevermind…

#### [Gabriel Ebner (Oct 22 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136275199):
```quote
To nitpick: to say "true" you have to say what semantics we're using. Excluded middle isn't true in Kripke semantics for propositional logic.
```
To nitpick even harder: usually truth refers to a single model, the concept we need here is validity---truth in all models.  For example `p ∨ ¬ p` is true in some Kripke models (e.g. any model with only one world); but is not *valid*, it is not true at all worlds in all Kripke models.

#### [Gabriel Ebner (Oct 22 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136275469):
```quote
"true" is an absolute thing, stuff like p -> p is true because T -> T and F -> F
```
This should be "valid".  `p → p` is *valid* because `p → p` is *true* (alt. satisfied) in all models.

#### [Gabriel Ebner (Oct 22 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136275669):
```quote
[...] then the true things and the provable things coincide. This is the completeness theorem.
```
Since we're already nitpicking, the completeness theorem only states one inclusion: namely that `valid ⊆ provable`.  The other direction, `provable ⊆ valid` is typically called soundness.

#### [Kevin Buzzard (Oct 22 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136278211):
Thanks a lot for fixing up my inaccuracies. Some kids here at Imperial are asking me about these things so I'm very pleased to be able to get it all straight for the first time in my life.

#### [Kenny Lau (Oct 22 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136284552):
there are quite some (equivalent) semantics for constructive logic

#### [Kevin Buzzard (Oct 22 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136287058):
@**Kenny Lau**  are you going to rise to my challenge?

#### [Kevin Buzzard (Oct 22 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136287089):
or rather, Dr Britnell's challenge. https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/c55d507918a8de1ec4c81953fe4dfcd696c46e82/src/gabriel_framework.lean#L33

#### [Kevin Buzzard (Oct 22 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136287285):
@**Rohan Mitta**  asked me why `prf` was taking values in Type and not Prop. Is there a reason for this? It gave Rohan some trouble (he couldn't use `or.elim`), so he made a new `Prop`-valued type to get around it. Does this mean that `or.elim` somehow should not be used? What's happening here?

#### [Kevin Buzzard (Oct 22 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136287518):
@**Abhimanyu Pallavi Sudhir** is making progress: https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/c55d507918a8de1ec4c81953fe4dfcd696c46e82/src/abhimanyu.lean#L39

#### [Kevin Buzzard (Oct 22 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136287752):
https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/master/src/rohan_enrico_success.lean @**Rohan Mitta** says he's done it! But he changed the question a bit...

#### [Kevin Buzzard (Oct 22 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136288400):
@**Kenny Lau** I tidied up the question. Here it is:

https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/master/src/gabriel_framework.lean

The proofs are really nice to write in term mode

#### [Kevin Buzzard (Oct 22 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136288447):
That's what Britnell asked the first years.

#### [Kenny Lau (Oct 22 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136288455):
I'm revising for my test tomorrow

#### [Kevin Buzzard (Oct 22 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136288465):
Probably a better use of your time, if you have a test tomorrow.

#### [Kevin Buzzard (Oct 22 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136288909):
https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/master/src/question6.lean There's the final version of the challenge. I tinkered with `mp` a bit. If anyone can suggest any other improvements I'd be all ears. Rohan, I stubbornly left it as `Type` but only because I don't understand if changing it to `Prop` is cheating or not.

#### [Kevin Buzzard (Oct 22 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136289685):
@**Rohan Mitta** what do you think of my changes to `mp`?

#### [Kevin Buzzard (Oct 22 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136289732):
I put p and q in `{}` and I changed the order of the next two inputs (first the function, then the input).

#### [Kevin Buzzard (Oct 22 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136289781):
Would that have made your code easier or harder to write?

#### [Rohan Mitta (Oct 22 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136289917):
Yeah your changes are great! In all my proofs I let lean infer what p and q were, and also often accidentally wrote the next two inputs in the order that you changed it to.

#### [Kevin Buzzard (Oct 22 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136290105):
Oh, here's something I just realised I didn't know: Modus Ponens says `prf (q →' r) → (prf q → prf r)` but is the converse true? Is there a map `(prf q → prf r) → prf (q →' r)` ?

#### [Kevin Buzzard (Oct 22 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136290243):
Regarding order of inputs for modus ponens, check out the analogy here:
```lean
axs (p q r) : prf $ (p →' q →' r) →' (p →' q) →' (p →' r)
mp {q r} : prf (q →' r) → prf q → prf r
```

#### [Kevin Buzzard (Oct 22 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136290622):
```quote
Oh, here's something I just realised I didn't know: Modus Ponens says `prf (q →' r) → (prf q → prf r)` but is the converse true? Is there a map `(prf q → prf r) → prf (q →' r)` ?
```
I see -- this is the deduction theorem.

#### [Abhimanyu Pallavi Sudhir (Oct 22 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136292121):
```quote
Oh, here's something I just realised I didn't know: Modus Ponens says `prf (q →' r) → (prf q → prf r)` but is the converse true? Is there a map `(prf q → prf r) → prf (q →' r)` ?
```
Is it okay to assume "internal modus ponens", i.e. `P →' (P →' Q) →' Q`? I can prove the other form, that `(P →' Q) →' P →' Q)` easily from `P →' P`, but not this form.

#### [Kevin Buzzard (Oct 22 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136292278):
Did you see what Rohan did? He set up a whole theory of what it means to be able to syntactically deduce a formula from a set of formulae

#### [Abhimanyu Pallavi Sudhir (Oct 22 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136292311):
```quote
Did you see what Rohan did?
```
I tried to.

#### [Kevin Buzzard (Oct 22 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136292322):
I don't understand this stuff too well; I had never realised the subtleties of the internal / external stuff.

#### [Abhimanyu Pallavi Sudhir (Oct 22 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136292397):
It's just that the standard Hilbertian formulation contains modus ponens as an axiom, so it seems like it should be ok to assume it.

#### [Kevin Buzzard (Oct 22 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136292460):
If you want to tinker with the framework then you'll need to talk to someone who knows what's going on better than me. I thought that it should be possible to prove what you want, because the term is valid.

#### [Kevin Buzzard (Oct 22 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136294136):
@**Rohan Mitta** maybe the whole Prop / Type thing is the Curry-Howard thing. If you were writing computer programs, e.g. if you thought that `P ->' P` was the identity function, then you should be using `Type`. But if you're regarding it as a theorem I guess you should be using `Prop`.  I don't know how well `Type` plays with the contrapositive axiom because that's precisely the axiom that the computer programmers don't have.

#### [Scott Morrison (Oct 23 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136303803):
```quote
In our minds what is really going on is `have b : B := hab a, clear a hab,`
```
There's no reason one couldn't write a tactic that does this; just parse the expression, looking for appearances and named hypotheses, and clear any that aren't used anymore. (e.g. just by attempting to clear them).

#### [Scott Morrison (Oct 23 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136303850):
You could call this `then`, rather than `have`, perhaps.

#### [Abhimanyu Pallavi Sudhir (Oct 23 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136322889):
I formalised the proof on MSE, but had to assume two additional axioms:
https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/master/src/abhimanyu.lean

#### [Abhimanyu Pallavi Sudhir (Oct 23 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136322908):
It's not as comprehensive as Rohan & Enrico's, of course.

#### [Gabriel Ebner (Oct 23 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136323186):
```quote
maybe the whole Prop / Type thing is the Curry-Howard thing. If you were writing computer programs, e.g. if you thought that P ->' P was the identity function, then you should be using Type
```
The choice of whether to use Type or Prop is not between programs and proofs, or between intuitionistic and classical logic, but between proofs and provability---each choice models *different objects* in mathematical logic.  A proof is traditionally a finite tree of inferences, and it should live in Type.  However if you use the exact same constructors and just change the universe to Prop then you get a completely different structure: namely the set of theorems, which is the same as the set of tautologies (= valid propositional formulas) and does not have any relationship to proofs.  There are lots of things you can do with proofs, but not with provability alone.  For example you can define the size of a proof as a function `size {p} : prf p → ℕ` (for Hilbert-style calculi you'd typically want to measure the size as a DAG though, i.e., not counting duplicate subproofs more than once), and ask the question whether there are formulas whose proofs are necessarily exponential in size (easy exercise: every tautology has a proof of exponential size).  (We don't know.)  Such questions about the sizes of proofs in various proof systems for propositional logic are considered in the field of proof complexity.
Many proof systems also admit interpolation: from a proof of `p → q` you can compute an interpolant (= formula `r` such that `p → r` and `r → q` such that `r` only contains the symbols occurring in both `p` and `q`).  This interpolant depends on the proof; i.e., different proofs give different interpolants.  Since the computation of the interpolant is typically polynomial-time, we get a relationship to proof size as well.
These are just two prominent examples from propositional logic, where you actually want to talk about proofs and not just provability.  Sure, I've seen workarounds: instead of defining a size function for proofs, you could define a predicate "provable in at most n steps".  But from my point of view this is an awkward workaround.  Fundamentally, proofs are *data* and should be modelled as such.

#### [Gabriel Ebner (Oct 23 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136323892):
>  Is there a map (prf q → prf r) → prf (q →' r) ?

It almost looks like the deduction theorem, but no, there cannot be such a map.  This is because the function `prf q → prf r` can do a case analysis on the `prf q`.  Concretely, there is a function `prf (atom 0) → prf r` for any `r` (by contradiction, because `atom 0` is not a tautology).  Hence you'd be able to obtain e.g. `prf (atom 0 →' atom 1)`, which is clearly not a tautology.  (This problem is related to the so-called "exotic terms" in HOAS, if you're interested.)

#### [Gabriel Ebner (Oct 23 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136324163):
If you want to prove the deduction theorem, my suggestion would be to add a parameter `Γ : set fml` so that `prf Γ p` are the proofs of `p` from assumptions `Γ`:
```lean
inductive prf (Γ : set fml) : fml → Type
| ass (p) : p ∈ Γ → prf p
| axk (p q) : prf (p →' q →' p)
| axs (p q r) : prf $ (p →' q →' r) →' (p →' q) →' (p →' r)
| axX (p q) : prf $ ((¬' q) →' (¬' p)) →' p →' q
| mp {p q} : prf (p →' q) → prf p → prf q -- bracket change

infix ` ⊢ `:30 := prf

def deduction_thm {Γ p} : ∀ {q}, Γ ∪ {p} ⊢ q → Γ ⊢ p →' q :=
sorry
```

#### [Kevin Buzzard (Oct 23 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136353019):
@**Rohan Mitta** (working with someone called Enrico) introduced a new `consequence` type https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/8df51accce766b8e33cae026203f85a8f87eed7e/src/rohan_enrico_success.lean#L34 which probably has the same effect. Rohan -- you see the trick Gabriel is suggesting? Instead of introducing the new type, modify the definition of the old one.

#### [Kevin Buzzard (Oct 23 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136358650):
@**Chris Hughes** examined Rohan's proof term and then came up with a really minimised answer https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/master/src/Chris_Hughes.lean

#### [Kevin Buzzard (Oct 23 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136358920):
@**Abhimanyu Pallavi Sudhir** was asking how Chris' term can work with so much information missing. I told him that Lean sees the missing `{ }` variables as a big logic puzzle and it must have proved that there was a unique solution.

#### [Kevin Buzzard (Oct 23 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136359692):
Abhi you could change the definition of `prf` back so that the variables are explicit, and then you could fill in everything in Chris' proof with `_`'s as required and then start adding and deleting hints for the elaborator.

#### [Kevin Buzzard (Oct 23 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136360475):
Here's something I don't understand.

```lean
inductive prf : fml → Type
| axk {p q} : prf (p →' q →' p)
| axs {p q r} : prf $ (p →' q →' r) →' (p →' q) →' (p →' r)
| axX {p q} : prf $ ((¬' q) →' (¬' p)) →' p →' q
| mp {p q} : prf p → prf (p →' q) → prf q

open prf

theorem not_not_p_of_p (p : fml) : prf (p →' (¬' (¬' p))) :=
mp (mp (mp (@axk (¬' p) (¬' p)) axk)
  (mp (mp (mp (mp (mp (@axk (¬' ¬' ¬' p) (¬' ¬' ¬' p)) (mp axk axs))
  (mp (mp axk axk) axs)) (mp (mp axX axk) axs)) (mp (mp axX axk) axs)) axs)) axX
```

I liked the analogy between `@mp q r` and `@axs p q r` when `mp` was written the other way around, however:
```lean
| mp' {p q} : prf (p →' q) → prf p → prf q
```
and I was in my mind using this to justify `mp'` over `mp`. I wondered what would happen to Chris' proof if I replaced `mp` with `mp'` though? He has all these rows of `mp (mp (mp (mp (...`. Is this an indication that he's doing it right, doing it wrong, or are these big strings just irrelevant? Is this even an important question, which way round these inputs go?

#### [Abhimanyu Pallavi Sudhir (Oct 23 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136360843):
```quote
Here's something I don't understand.

```lean
inductive prf : fml → Type
| axk {p q} : prf (p →' q →' p)
| axs {p q r} : prf $ (p →' q →' r) →' (p →' q) →' (p →' r)
| axX {p q} : prf $ ((¬' q) →' (¬' p)) →' p →' q
| mp {p q} : prf p → prf (p →' q) → prf q

open prf

theorem not_not_p_of_p (p : fml) : prf (p →' (¬' (¬' p))) :=
mp (mp (mp (@axk (¬' p) (¬' p)) axk)
  (mp (mp (mp (mp (mp (@axk (¬' ¬' ¬' p) (¬' ¬' ¬' p)) (mp axk axs))
  (mp (mp axk axk) axs)) (mp (mp axX axk) axs)) (mp (mp axX axk) axs)) axs)) axX
```

I liked the analogy between `@mp q r` and `@axs p q r` when `mp` was written the other way around, however:
```lean
| mp' {p q} : prf (p →' q) → prf p → prf q
```
and I was in my mind using this to justify `mp'` over `mp`. I wondered what would happen to Chris' proof if I replaced `mp` with `mp'` though? He has all these rows of `mp (mp (mp (mp (...`. Is this an indication that he's doing it right, doing it wrong, or are these big strings just irrelevant? Is this even an important question, which way round these inputs go?
```
Something interesting to note is that the internal counterpart of `mp'` (i.e. `prf ((p →' q) →' p →' q)`) is much easier to prove in our system (follows from `P →' P`) than `mp` (i.e. `prf (p →' (p →' q) →' q)`) -- at least, I wasn't able to prove the latter. Which gives an indication that in this system, where stuff like `intro` are not formalised, it does make a difference how you define `mp`.

#### [Alexandru-Andrei Bosinta (Oct 23 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136361087):
```quote
Here's something I don't understand.

```lean
inductive prf : fml → Type
| axk {p q} : prf (p →' q →' p)
| axs {p q r} : prf $ (p →' q →' r) →' (p →' q) →' (p →' r)
| axX {p q} : prf $ ((¬' q) →' (¬' p)) →' p →' q
| mp {p q} : prf p → prf (p →' q) → prf q

open prf

theorem not_not_p_of_p (p : fml) : prf (p →' (¬' (¬' p))) :=
mp (mp (mp (@axk (¬' p) (¬' p)) axk)
  (mp (mp (mp (mp (mp (@axk (¬' ¬' ¬' p) (¬' ¬' ¬' p)) (mp axk axs))
  (mp (mp axk axk) axs)) (mp (mp axX axk) axs)) (mp (mp axX axk) axs)) axs)) axX
```

I liked the analogy between `@mp q r` and `@axs p q r` when `mp` was written the other way around, however:
```lean
| mp' {p q} : prf (p →' q) → prf p → prf q
```
and I was in my mind using this to justify `mp'` over `mp`. I wondered what would happen to Chris' proof if I replaced `mp` with `mp'` though? He has all these rows of `mp (mp (mp (mp (...`. Is this an indication that he's doing it right, doing it wrong, or are these big strings just irrelevant? Is this even an important question, which way round these inputs go?
```
If you replace mp with mp' you would probably only have to switch all the arguments, but I don't think anything else has to be changed.

#### [Kevin Buzzard (Oct 23 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136361161):
Right -- but it would be really boring doing that by hand. I did all the other substitutions using emacs.

#### [Kevin Buzzard (Oct 23 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136361184):
this one is a more serious tree operation

#### [Kevin Buzzard (Oct 23 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136361186):
actually I think I can do it using emacs

#### [Kenny Lau (Oct 23 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136362986):
```lean
def fml.eval (f : ℕ → Prop) : fml → Prop
| (atom i) := f i
| (a →' b) := fml.eval a → fml.eval b
| (¬' a) := ¬fml.eval a

def prf.eval (f : ℕ → Prop) : Π p:fml, prf p → p.eval f
| _ (@axk p q) := λ hpq _, hpq
| _ (@axs p q r) := λ hpqr hpq hp, hpqr hp (hpq hp)
| _ (@axX p q) := λ hmt hp, classical.by_contradiction (λ hnq, hmt hnq hp)
| _ (@mp p q hp hpq) := prf.eval _ hpq (prf.eval _ hp)
```

#### [Kevin Buzzard (Oct 23 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136363138):
I think Chris did something clever with decidability?

#### [Rob Lewis (Oct 23 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136364666):
Kenny, that's a soundness proof. Now do completeness!

#### [Kenny Lau (Oct 23 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136364680):
heh

#### [Rob Lewis (Oct 23 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136364686):
Kevin, I think the strings of `mp (mp (mp...` are really just a sign of how awkward Hilbert systems are to use.

#### [Rob Lewis (Oct 23 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136364743):
Like, that's just what a proof in this calculus looks like.

#### [Rob Lewis (Oct 23 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136364757):
If for some reason you wanted to keep making these proofs, you'd design tools to assemble them from something more readable.

#### [Rob Lewis (Oct 23 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136364772):
i.e. natural deduction, or a tactic language.

#### [Kenny Lau (Oct 23 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136364796):
i.e. prove the deduction theorem

#### [Rob Lewis (Oct 23 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136364828):
Jeremy has a related example for the sequent calculus here: https://github.com/avigad/embed/blob/master/src/examples.lean

#### [Kevin Buzzard (Oct 23 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136365197):
```lean
theorem not_not_p_of_p (p : fml) : prf (p →' (¬' (¬' p))) :=
mp (mp (mp (@axk (¬' p) (¬' p)) 
           (axk _ _)
       )
       (mp (mp (mp (mp (mp (@axk (¬' ¬' ¬' p) (¬' ¬' ¬' p)) 
                           (mp (axk _ _)
                               (axs _ _ _)
                           )
                       )
                       (mp (mp (axk _ _) 
                               (axk _ _)
                           ) 
                           (axs _ _ _)
                       )
                   ) 
                   (mp (mp (axX _ _) 
                           (axk _ _)
                       ) 
                       (axs _ _ _)
                   )
               ) 
               (mp (mp (axX _ _) 
                       (axk _ _)
                   ) 
                   (axs _ _ _)
               )
           ) 
           (axs _ _ _)
       )
   ) 
   (axX _ _)
```

It's not very often I think about proof trees. I know it's all awful to you computer scientists, but I'm still on the basics :-)

#### [Mario Carneiro (Oct 24 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136381508):
by the way, I think this is actually a really good application of metamath. The whole logic is set up from these exact axioms of propositional calculus, by lucasiewicz. (Unfortunately I don't have any better naming suggestions - in metamath they are literally called ax-1, ax-2, ax-3 since that's what lucasiewicz called them)

#### [Mario Carneiro (Oct 24 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136381553):
You should look at the derivations of some basic theorems - this is where metamath is most readable. Your theorem is [notnot1](http://us.metamath.org/mpeuni/notnot1.html)

#### [Mario Carneiro (Oct 24 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136383658):
Here is a moderately inlined version of the metamath proof. The key to making this readable is to break it into bite sized pieces of no more than five steps. Almost all of the intermediate steps are independently useful, even more than I'm showing here. Hilbert style axiomatizations are not meant to be used directly; you should prove as lemmas all the basic facts and use them as scaffolding to manage the complexity.
```lean
inductive fml
| atom (i : ℕ)
| imp (a b : fml)
| not (a : fml)

open fml

infixr ` →' `:50 := imp -- right associative

prefix `¬' `:max := fml.not

inductive prf : fml → Type
| axk {p q} : prf (p →' q →' p)
| axs {p q r} : prf $ (p →' q →' r) →' (p →' q) →' (p →' r)
| axX {p q} : prf $ (¬' q →' ¬' p) →' p →' q
| mp {p q} : prf p → prf (p →' q) → prf q

namespace prf
prefix `⊢ `:30 := prf

def mp' {p q} (h1 : ⊢ p →' q) (h2 : ⊢ p) : ⊢ q := mp h2 h1
def a1i {p q} : ⊢ p → ⊢ q →' p := mp' axk
def a2i {p q r} : ⊢ p →' q →' r → ⊢ (p →' q) →' p →' r := mp' axs
def con4i {p q} : ⊢ ¬' p →' ¬' q → ⊢ q →' p := mp' axX
def mpd {p q r} (h : ⊢ p →' q →' r) : ⊢ p →' q → ⊢ p →' r := mp' (a2i h)
def syl {p q r} (h1 : ⊢ p →' q) (h2 : ⊢ q →' r) : ⊢ p →' r := mpd (a1i h2) h1
def id {p} : ⊢ p →' p := mpd axk (@axk p p)
def a1d {p q r} (h : ⊢ p →' q) : ⊢ p →' r →' q := syl h axk
def com12 {p q r} (h : ⊢ p →' q →' r) : ⊢ q →' p →' r := syl (a1d id) (a2i h)
def con4d {p q r} (h : ⊢ p →' ¬' q →' ¬' r) : ⊢ p →' r →' q := syl h axX
def absurd {p q} : ⊢ ¬' p →' p →' q := con4d axk
def imidm {p q} (h : ⊢ p →' p →' q) : ⊢ p →' q := mpd h id
def contra {p} : ⊢ (¬' p →' p) →' p := imidm (con4d (a2i absurd))
def notnot2 {p} : ⊢ ¬' ¬' p →' p := syl absurd contra
def mpdd {p q r s} (h : ⊢ p →' q →' r →' s) : ⊢ p →' q →' r → ⊢ p →' q →' s := mpd (syl h axs)
def syld {p q r s} (h1 : ⊢ p →' q →' r) (h2 : ⊢ p →' r →' s) : ⊢ p →' q →' s := mpdd (a1d h2) h1
def con2d {p q r} (h1 : ⊢ p →' q →' ¬' r) : ⊢ p →' r →' ¬' q := con4d (syld (a1i notnot2) h1)
def con2i {p q} (h1 : ⊢ p →' ¬' q) : ⊢ q →' ¬' p := con4i (syl notnot2 h1)
def notnot1 {p} : ⊢ p →' ¬' ¬' p := con2i id

end prf
```

#### [Mario Carneiro (Oct 24 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136383668):
If you are going for a direct from axioms proof, there is probably a faster way, but all you get from that is a big hideous proof term and no useful subparts

#### [Mario Carneiro (Oct 24 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136384232):
One of my first papers was a proof that Hilbert style axiomatizations result in an O(1) additive overhead over natural deduction proof rules (i.e. the bulk of the proof is 1-1 matched to lemmas), so I respectfully disagree that hilbert systems are innately harder to use - there is just a bit more "honest toil" in showing that and, or, implies all exist and have the appropriate theorems as in natural deduction

#### [Kevin Buzzard (Oct 24 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136391718):
Well I am very unimpressed that metamath starts so high up. What's wrong with just having Chris Barker's iota combinator and building everything from that? Guess you guys were just lazy

#### [Kevin Buzzard (Oct 24 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136391779):
I like the way everyone is calling that third axiom `axX`. That was supposed to be a placeholder until a computer scientist told us the proper name...

#### [Kevin Buzzard (Oct 24 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136391780):
Xcluded middle

#### [Kevin Buzzard (Oct 24 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136392655):
@**Abhimanyu Pallavi Sudhir** note proof of `syl`. Mario thanks a *lot* for this -- when I had time I was going to take Chris' proof apart and turn it into a bunch of lemmas like this, that's why I was unravelling all the brackets. I see you also have `mp` the "wrong way round"

#### [Mario Carneiro (Oct 24 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136429594):
@**Kevin Buzzard** It also wasn't meant to be intentionally obtuse, it is following a mishmash of logic and set theory textbooks where possible (everything is referenced too, so you can read along)

#### [Mario Carneiro (Oct 24 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136429649):
The Lucasiewicz axioms seem to be pretty popular for hilbert style axiomatizations

#### [Mario Carneiro (Oct 24 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136429705):
Metamath has `mp` the way you stated it, but it also has no notion of partial application. You will notice I make use of partially applied `mp'` a few times

