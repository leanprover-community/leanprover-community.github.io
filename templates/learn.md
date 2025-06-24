# Learning Lean 4

There are many ways to start learning Lean, depending on your background and
taste. They are all fun and rewarding, but also difficult and
occasionally frustrating. Proof assistants are still difficult to use,
and you cannot expect to become proficient after one afternoon of
learning.

All the resources listed on this page are about Lean 4.
Some have Lean 3 versions, but there is no point learning Lean 3 at this stage.

## Hands-on approaches

* Whatever your background, if you want to dive right away, you can play the
  [Natural Number Game](https://adam.math.hhu.de/#/g/hhu-adam/NNG4).
  This is an online interactive Lean tutorial
  focused on proving properties of the elementary operations on natural numbers.
  The [Lean Game Server](https://adam.math.hhu.de/#/) hosts various learning games including
  Set Theory, Logic, and Robo (a story about undergrad mathematics).

* For a faster-paced dive, you can get the
  [Glimpse of Lean tutorial](https://github.com/PatrickMassot/GlimpseOfLean).
  This contains four basic files covering some fundamental aspects of proving
  using Lean, and then independent topic files about elementary analysis,
  abstract topology and mathematical logic.

* You can download the [tactic cheatsheet (PDF)](https://leanprover-community.github.io/papers/lean-tactics.pdf) for a reference of most common tactics.

* If you wish to learn directly from source, the
  [Lean API documentation](https://leanprover-community.github.io/mathlib4_docs/)
  not only includes `Mathlib`, but also covers `Std`, `Batteries`, `Lake`, and the core compiler.
  As much of Lean is defined in terms of syntax extensions, this is the closest thing to a
  comprehensive reference manual that exists.

## Books

If you prefer reading a book (with exercises), there are a number of freely available Lean books
that have proven to be useful to beginners.
These are available as HTML or PDFs, but are usually meant to be read interactively in VSCode,
doing Lean exercises on the fly:

* The standard mathematics-oriented reference is
  [Mathematics in Lean](https://leanprover-community.github.io/mathematics_in_lean/).
  You can [download it as a PDF](https://leanprover-community.github.io/mathematics_in_lean/mathematics_in_lean.pdf),
  but see also the
  [VSCode instructions](https://leanprover-community.github.io/mathematics_in_lean/C01_Introduction.html#getting-started).

* [The Mechanics of Proof](https://hrmacbeth.github.io/math2001/) is also mathematics-oriented.
  It has a gentler pace than *Mathematics in Lean* and is aimed at readers with less mathematical
  experience.

* If you prefer something more about the foundations of type theory, the standard reference is
  [Theorem Proving in Lean](https://lean-lang.org/theorem_proving_in_lean4/).

* A computer-science/programming-oriented book is
  [The Hitchhiker's Guide to Logical Verification](https://raw.githubusercontent.com/blanchette/logical_verification_2023/main/hitchhikers_guide.pdf).
  It also has useful information about the type theory of Lean, and an associated VSCode project with exercises.

If you want something more focused on Lean itself than on using Lean, then you
can read the [reference manual](https://lean-lang.org/doc/reference/latest/) ([old manual](https://lean-lang.org/lean4/doc/)).

## (Meta)-programming and tactic writing

* If you are interested in Lean as a programming language then you should read
  [Functional programming in Lean](https://lean-lang.org/functional_programming_in_lean/).

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
  section](https://lean-lang.org/theorem_proving_in_lean4/axioms_and_computation.html#quotients)
  of *Theorem proving in Lean*).

If you can read the above Coq documentation then you are ready for
[this paper](https://github.com/digama0/lean-type-theory/releases) by
Mario Carneiro which precisely describes the type theory of Lean.

Note that understanding type-theoretic foundations is not at all necessary
to use Lean.

## Meetings

A number of meetings have helped welcome newcomers to the Lean community.
The following have links to online talks and other material that may
be of interest.
Note that all items until the year 2022 used Lean 3, but they may still contain relevant information.
* [Lean for the Curious Mathematician 2023](https://lftcm2023.github.io/tutorial/index.html)
* [Formalization of mathematics 2023](https://www.msri.org/summer_schools/1021)
* [Lean for the Curious Mathematician 2022](https://icerm.brown.edu/topical_workshops/tw-22-lean/)
* [Lean for the Curious Mathematician 2020](https://leanprover-community.github.io/lftcm2020/)

More events can be found on the [events](events.html) page.
We also have a [YouTube channel](https://www.youtube.com/channel/UCWe5B7Ikr0AI9727doEUxPg/playlists)
which includes playlists of videos from the above conferences, and also other conferences with Lean-relevant content.
