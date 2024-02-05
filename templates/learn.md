# Learning Lean 4

There are many ways to start learning Lean, depending on your background and
taste. They are all fun and rewarding, but also difficult and
occasionally frustrating. Proof assistants are still difficult to use,
and you cannot expect to become proficient after one afternoon of
learning. Note that all resources listed on that page are about Lean 4. 
There is no point learning Lean 3 at this stage.

## Hands-on approaches

* Whatever your background, if you want to dive right away, you can play the
  [Natural Number Game](https://adam.math.hhu.de/#/g/hhu-adam/NNG4). 
  This is an online interactive tutorial to Lean
  focused on proving properties of the elementary operations on natural numbers.

* For a faster paced and broader dive, you can get the
  [Glimpse of Lean tutorial](https://github.com/PatrickMassot/GlimpseOfLean).
  This contains four basic files covering some fundamental aspects of proving
  using Lean, and then independent topic files about elementary analysis,
  abstract topology and mathematical logic.

## Documents

* [Mathematics in Lean](https://leanprover-community.github.io/mathematics_in_lean/) by Jeremy Avigad and 
  Patrick Massot is the standard
  reference on formalizing mathematics in Lean. You can download it 
  [as a pdf](https://leanprover-community.github.io/mathematics_in_lean/mathematics_in_lean.pdf),
  but it can also be used within VSCode, in which case  you can do the exercises without copying them from
  the document to the editor (see the
  [instructions](https://leanprover-community.github.io/mathematics_in_lean/C01_Introduction.html#getting-started)).

* [The Mechanics of Proof](https://hrmacbeth.github.io/math2001/) by Heather Macbeth is an undergraduate textbook that    
  uses Lean to teach methods of proof in mathematics.

* [How To Prove It With Lean](https://djvelleman.github.io/HTPIwL/) by Daniel Velleman is a Lean supplement to the
  author's undergraduate textbook (*How To Prove It: Third Edition*, Cambridge, University Press, 2019)  for teaching methods of proof in mathematics.

* [A Gentle Introduction to Lean](https://github.com/motib/gentle-lean) by Moti Ben-Ari is a tutorial on the Lean proof 
  assistant for novices that introduces the proof tactics step-by-step.

* [Theorem Proving in Lean](https://leanprover.github.io/theorem_proving_in_lean4/) by Jeremy Avigad, 
  Leonardo de Moura, Soonho Kong and Sebastian Ullrich is a formal description of the Lean proof assistant.
  Unlike *Mathematics in Lean* which focuses on the *use* of Lean to prove mathematical theorems, this document
  explains the meaning and the rationale of the Lean constructs. 
  You will want to study this after achieving some familiarity with the use of Lean. 
  
* [Lean Manual](https://leanprover.github.io/lean4/doc/) is the Lean reference manual.

## (Meta)-programming and tactic writing

* If you are interested in Lean as a programming language then you should read
  [Functional programming in Lean](https://leanprover.github.io/functional_programming_in_lean/).

* If you specifically want to do meta-programming and write tactics then you can read
  [Metaprogramming in Lean 4](https://github.com/arthurpaulino/lean4-metaprogramming-book)
  (after at least checking you are comfortable with the monad chapters of Functional programming in Lean).

## More on foundations

If you are interested in foundations of Lean, you can first read a
very rough sketch
[here](https://leanprover-community.github.io/lean-perfectoid-spaces/type_theory.html).
If you want a bit more detail, you can read the first chapter
of the [HoTT book](https://homotopytypetheory.org/book/), ignoring
anything where univalence is mentioned.

If you're interested in the nuts and bolts of Lean's kernel, writing your own external type checker for Lean, or exporting proofs, you can read more in [Type Checking in Lean 4](https://ammkrn.github.io/type_checking_in_lean4/).

Another potentially useful resource is
[this page](https://coq.github.io/doc/master/refman/language/cic.html)
from Coq's documentation. The foundations of Coq are very very close to
those of Lean. The most relevant differences to keep in mind are:
* Lean's `Prop` is proof-irrelevant, so it is closer to `SProp` from the
  page above.
* Universes in Lean are *not* cumulative. However, any type can be lifted
  to higher universes.
* Lean natively supports quotient types and their associated reduction
  rule (see [this
  section](https://leanprover.github.io/theorem_proving_in_lean4/axioms_and_computation.html#quotients)
  of *Theorem proving in Lean*).

If you can read the above Coq documentation then you are ready for
[this paper](https://github.com/digama0/lean-type-theory/releases) by
Mario Carneiro which precisely describes the type theory of Lean.

Note that understanding type theoretic foundations is not at all necessary
to use Lean.

## Meetings

A number of meetings have helped welcome newcomers to the Lean community.
The following have links to online talks and other material that may
be of interest. Note that all items until year 2022 used Lean 3 but may still contain relevant information.
* [Lean for the Curious Mathematician 2023](https://lftcm2023.github.io/tutorial/index.html)
* [Formalization of mathematics 2023](https://www.msri.org/summer_schools/1021)
* [Lean for the Curious Mathematician 2022](https://icerm.brown.edu/topical_workshops/tw-22-lean/)
* [Lean Together 2021](https://leanprover-community.github.io/lt2021/)
* [Lean for the Curious Mathematician 2020](https://leanprover-community.github.io/lftcm2020/)
* [Formal Methods in Mathematics / Lean Together 2020](https://www.andrew.cmu.edu/user/avigad/meetings/fomm2020/)
* [Lean Together 2019](https://lean-forward.github.io/lean-together/2019/)

We also have a [YouTube channel](https://www.youtube.com/channel/UCWe5B7Ikr0AI9727doEUxPg/playlists)
which includes playlists of videos from the above conferences, and also other conferences with Lean-relevant content.

