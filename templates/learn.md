# Learning Lean

There are many ways to start learning Lean, depending on your background and
taste. They are all fun and rewarding, but also difficult and
occasionally frustrating. Proof assistants are still difficult to use,
and you cannot expect to become proficient after one afternoon of
learning.

## Hands-on approaches

* Whatever your background, if you want to dive right away, you can play the
  [Natural Number Game](http://wwwf.imperial.ac.uk/~buzzard/xena/natural_number_game/)
  by Kevin Buzzard and Mohammad Pedramfar. This is a online interactive tutorial to Lean
  focused on proving properties of the elementary operations on natural numbers.

* For a faster paced and broader dive, you can get the
  [tutorials project](https://github.com/leanprover-community/tutorials).
  (You already have it if you installed an autonomous bundle or
  followed the instructions on [this page](install/project.html).)
  This tutorial is specifically geared towards mathematics rather than
  computer science. The last files of this project are easier if you have
  already encountered the definition of limits of sequences of real
  numbers.

* The [lfctm2020 exercises](https://github.com/leanprover-community/lftcm2020),
  developed for the July 2020 virtual meeting
  [Lean for the Curious Mathematician](https://leanprover-community.github.io/lftcm2020/),
  are another good resource. There are corresponding tutorial videos from the meeting.

* A brand new resource that is still under construction is
  *Mathematics in Lean*.
  It can be [read online](https://leanprover-community.github.io/mathematics_in_lean/),
  or downloaded [as a pdf](https://leanprover-community.github.io/mathematics_in_lean/mathematics_in_lean.pdf),
  but it is really meant to be used in VSCode, doing exercises
  on the fly (see the [instructions](https://leanprover-community.github.io/mathematics_in_lean/introduction.html#getting-started)).
  It currently covers roughly the same ground as the tutorials project.

* Once you know the basics, you can also learn by solving Lean puzzles
  on [Codewars](https://www.codewars.com/?language=lean).

Whatever resource you choose to use from the above list, it could
be useful to have a copy of our [tactic cheat sheet](img/lean-tactics.pdf)
at hand, for reference.

## Textbooks

* If you prefer reading a book (with exercises), the standard reference is
  [Theorem Proving in Lean](https://leanprover.github.io/theorem_proving_in_lean/).
  You almost certainly want to read it at some point anyway, since it
  explains foundational things much better than any hands-on tutorial
  could do.

* If you are very new to the concept of logic and proofs, you can read
  [Logic and Proof](https://leanprover.github.io/logic_and_proof/),
  a textbook that is a first rigorous proving course that teaches Lean at the same time.

* If you have a computer science background, and are primarily interested
  in software verification, then you can read
  [The Hitchhiker's Guide to Logical Verification (pdf)](https://github.com/blanchette/logical_verification_2020/raw/master/hitchhikers_guide.pdf) ([tablet edition optimized for on-screen viewing](https://github.com/blanchette/logical_verification_2020/raw/master/hitchhikers_guide_tablet.pdf)),
  course notes for an [MSc-level course](https://lean-forward.github.io/logical-verification/2020/index.html) at VU Amsterdam.

* If you want a systematic exposition of syntax and commands, then you
  can read the [reference manual](https://leanprover.github.io/reference/).

## Miscellaneous topics

In addition to the above sources, we have a number of small documents
covering specific topics:

* The [conversion tactic mode](extras/conv.html)
* The [simplifier](extras/simp.html)
* The [calc environment](extras/calc.html)
* [Well founded recursion](extras/well_founded_recursion.html)

## Metaprogramming and tactic writing

After using Lean for a while, you may want to learn how to write your
own tactics. This is less documented than proof writing, but you can
still have a look at the following resources.

* The [tactic writing tutorial](extras/tactic_writing.html)
  covers the basics and enables you to read more advanced sources, for instance
  the code of
  [existing tactics](https://leanprover-community.github.io/mathlib_docs/tactics.html).
* [The Hitchhiker's Guide to Logical Verification (pdf)](https://github.com/blanchette/logical_verification_2020/raw/master/hitchhikers_guide.pdf) also has a chapter on metaprogramming.
* The reference paper on
  [Lean metaprogramming](https://leanprover.github.io/papers/tactic.pdf).
* The [metaprogramming tutorial videos](https://www.youtube.com/watch?v=o6oUjcE6Nz4&list=PLlF-CfQhukNnq2kDCw2P_vI5AfXN7egP2) that Rob Lewis designed and recorderd for LftCM 2020.

## More on foundations

If you are interested in foundations of Lean, you can first read a
very rough sketch
[here](https://leanprover-community.github.io/lean-perfectoid-spaces/type_theory.html).
If you want a bit more detail, you can read the first chapter
of the [HoTT book](https://homotopytypetheory.org/book/), ignoring
anything where univalence is mentioned.

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
  section](https://leanprover.github.io/theorem_proving_in_lean/axioms_and_computation.html#quotients)
  of *Theorem proving in Lean*).

If you can read the above Coq documentation then you are ready for
[this paper](https://github.com/digama0/lean-type-theory/releases) by
Mario Carneiro which precisely describes the type theory of Lean.

Note that understanding type theoretic foundations is not at all necessary
to use Lean.

## Meetings

A number of meetings have helped welcome newcomers to the Lean community.
The following have links to online talks and other material that may
be of interest:
* [Lean for the Curious Mathematician 2020](https://leanprover-community.github.io/lftcm2020/)
* [Formal Methods in Mathematics / Lean Together 2020](https://www.andrew.cmu.edu/user/avigad/meetings/fomm2020/)
* [Lean Together 2019](https://lean-forward.github.io/lean-together/2019/)
