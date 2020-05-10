# Learning Lean

There are ways to start learning Lean, depending on your background and
taste. There are all fun and rewarding, but also difficult and
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

* Once you know the basics, you can also learn by solving Lean puzzles
  on [Codewars](https://www.codewars.com/?language=lean).

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
  [The Hitchhiker's Guide to Logical Verification (pdf)](https://github.com/blanchette/logical_verification_2020/raw/master/hitchhikers_guide.pdf),
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

* The [tactic writing tutorial](https://github.com/leanprover-community/mathlib/blob/master/docs/extras/tactic_writing.md)
  covers the basics and enables you to read more advanced sources, for instance
  the code of
  [existing tactics](https://leanprover-community.github.io/mathlib_docs/tactics.html).
* The reference paper on
  [Lean metaprogramming](https://leanprover.github.io/papers/tactic.pdf).

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
