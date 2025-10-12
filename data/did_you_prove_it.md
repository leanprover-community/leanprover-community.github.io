# Did you prove it?

[Lean](https://lean-lang.org/) is a computer program
which is capable of verifying
mathematical proofs at a superhuman level. But Lean is
a complex program. A claim from someone that they
have proved a theorem cannot simply be accompanied
by a block of Lean code; this code has to conform to some
basic guidelines. We briefly list the guidelines below,
and then go through them in more detail.

## Guidelines for a verified Lean proof

* Is your code in a correctly-formatted Lean repository? A standalone Lean file is not enough.
* Does the repository compile? In other words, does `lake build` return without errors?
* Is the proof being checked? In other words, is the file
  where the main theorem is proved being compiled by the build process?
* Does the proof use nothing more than Lean's standard axioms?
  In other words, does `#print axioms my_proof` return a subset of `[propext, Classical.choice, Quot.sound]`?
* Does your work prove what you claims it proved?

We now go through these guidelines in more detail.

## Is your code in a repository?

Lean is a fast-moving piece of software, with new
releases every month. Lean's mathematics library `mathlib`
typically merges many commits every day. At this point
in time, the software is still in a ``move fast'' phase,
with little guarantee of backward compatibility. This means
in practice that a standalone piece of code in a Lean
file in a random directory on your computer may compile
on your machine, but not on somebody else's (or even on yours
at a later date) --- because a different version of Lean
or `mathlib` is being used.

To solve this problem, Lean code needs to be part of
a *repository*, also known as a *project*. For example,
[mathlib](https://github.com/leanprover-community/mathlib4)
is a Lean project stored on GitHub. A Lean project comes
with various system files which determine precisely the
version of Lean (and of other dependent libraries such as Mathlib)
which your code uses, meaning that other people can
independently compile your code.

If you are using Lean within VS Code, the simplest way
to create a new Lean project is to click on the `∀` symbol
supplied by the Lean extension and to select "New Project".

Alternatively you can create a new Lean project on the
command line. The command
```lean 
lake new my_project math
```
creates a new project called `my_project`, with a dependency
on Lean's mathematics library.

## Does the repository compile? Is the proof being checked?

The typical set-up for a project called `Foobar` is
that it will have a file `Foobar.lean` in the root
directory of the project, which imports all the relevant
files in the project. If the actual proof of your
theorem is in `Foobar/MainResult.lean` then the file
`Foobar.lean` should have a line in it saying
`import Foobar.MainResult`. Under normal circumstances,
`lake build` will then build `Foobar/MainResult.lean`,
and this command needs to compile without errors.

There are other more advanced ways to set up a repository,
but if you are aware of such things then you will also
be well-aware of what it means for the build process to
be checking your proof.

## Does the proof use only the axioms of matheamtics?

Lean is a flexible piece of software. It is possible
to add new axioms to the system (including false ones)
with the `axiom` command, or to skip proofs with the `sorry` tactic.
There are also other ways that the system can be abused.
The bottom line is that after `#print axioms my_proof`
the system should return `[propext, Classical.choice, Quot.sound]`
(or some subset of these axioms). User-defined axioms,
or `sorryAx` (indicating a proof which was omitted)
indicate that your proof is incomplete.

## Does your work prove what you claim it proves?

This is an important point, and more complex than it seems.
Lean's syntax is incredibly flexible. It is very easy to
define a statement `TheRiemannHypothesis` which, despite the
name, is not actually a statement of the Riemann Hypothesis.
A proof of this statement is then, of course, not a proof
of the actual Riemann Hypothesis. It is even possible to
override Lean's standard definitions of the naturals or
of basic operations on them and then claim that you have
proved a statement which *looks* like Fermat's Last Theorem,
but which is nothing of the kind. Lean's mathematics library
`Mathlib` provides statements of several famous mathematical
theorems and conjectures such as [Fermat's Last Theorem](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/FLT/Basic.html#FermatLastTheorem)
and the [Riemann Hypothesis](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/RiemannZeta.html#RiemannHypothesis).
These statements have been checked by Mathlib's maintainer team
to be correct translations into Lean's type theory of the
corresponding mathematical statements. If you are claiming
to have proved a theorem which is not stated in `Mathlib` then
a necessary part of the verification process is that a Lean
expert is able to confirm that the *statement* of what you
have proved corresponds to the mathematical claim which
you are making.
