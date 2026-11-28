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
* Does your work prove what you claim it proved?
* Does the proof pass `lake comparator`? This command, included with Lean since version 4.35.0,
  is the recommended way to check a proof against a fixed statement.

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

## Does the proof use only the axioms of mathematics?

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

* It is possible for users to confuse the *statement* of a result
and its *proof*. It is easy in Lean to define and name the
*statement* that `2+2=5`; this does not constitute a *proof*
that `2+2=5`!

* It is very easy to define a complicated-looking statement and call it
`TheRiemannHypothesis` which, despite the
name, is not actually a statement of the Riemann Hypothesis.
A proof of this statement is then, of course, not a proof
of the actual Riemann Hypothesis. 

* Lean's syntax is incredibly flexible. It is possible to
override Lean's standard definitions of the naturals or
of basic operations on them and then claim that you have
proved a statement which *looks* like Fermat's Last Theorem,
but which is nothing of the kind. 

Lean's mathematics library
`Mathlib` provides statements of several famous mathematical
theorems and conjectures such as [Fermat's Last Theorem](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/FLT/Basic.html#FermatLastTheorem)
and the [Riemann Hypothesis](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/RiemannZeta.html#RiemannHypothesis).
These statements have been checked by Mathlib's maintainer team
to be correct translations into Lean's language of the
corresponding mathematical statements. 

If you are claiming
to have proved a theorem which is not stated in `Mathlib` then
a necessary part of the verification process is that a Lean
expert is able to confirm that the *statement* of what you
have proved corresponds to the mathematical claim which
you are making, and that you have *proved* the statement as well
as stating it.

## Does the proof pass `lake comparator`?

`lake comparator`, which is included with Lean since version 4.35.0,
is the community gold standard for judging whether a Lean proof
actually proves what it claims to prove. We recommend it
whenever you claim a proof or assess someone else's claim,
and especially when the proof was generated by an AI.

Lean is a powerful programming language as well as a theorem prover.
Users can modify everything from the meaning of definitions and notations
to the declarations in the Lean environment itself, through metaprogramming.
The checks above can therefore be fooled by code which is deliberately misleading,
and since building a Lean project runs the code in it,
`lake build` on an untrusted project is not safe either.

### How it works

`lake comparator` compares two modules:

* a *challenge*, containing the claimed theorems with `sorry` in place of the proofs,
  and containing or importing the definitions needed to state them;
* a *solution*, containing or importing the same theorems with the same names
  (this is important), this time with proofs.

The command builds and exports both modules in a sandbox.
It accepts the solution only if every theorem named in its configuration
has the same statement as in the challenge, down to every declaration
which the statement depends on, uses no axioms outside a permitted list,
and is accepted by Lean's kernel.
A definition, notation or other trick in the solution cannot influence the challenge,
so using one to change the meaning of a statement leads to a mismatch.

### How to set it up

To let other people check your project with `lake comparator`:

1. Decide what the end statements of your project are.
2. Create a file `Challenge.lean` containing a copy of these statements,
   and of the definitions from your project which appear in them.
3. Create a file `Solution.lean` containing or importing the proofs.
   It can simply import your whole project.
4. Create a file `comparator.json` in the root directory of your project containing
```text
{
  "challenge_module": "Challenge",
  "solution_module": "Solution",
  "theorem_names": ["your_theorem_name_here", "your_second_theorem_name_here"],
  "permitted_axioms": ["propext", "Quot.sound", "Classical.choice"]
}
```

Your project also has to contain a `lake-manifest.json` file, which is written
when you build it. Running `lake comparator` in the root directory
then prints `Your solution is okay!` if the solution is accepted.

The challenge should import as few files and contain as few new definitions as possible,
because other people have to trust all of them. Consider upstreaming your definitions
to a community-maintained library such as Mathlib.
The solution can import any amount of Lean code without decreasing trust.

The challenge and solution can be anywhere in your project, under any names,
and their module names in `comparator.json` should match.
We recommend making them default build targets, and not claiming generic library names
such as `Challenge` or `Solution`.
A project can have several challenges, with one configuration file for each:
use `lake comparator --config=<file>` to choose one.

### What it does not check

Here are the known ways that a result from `lake comparator` can still mislead,
and how to guard against them.

* It does not check that the definitions used in the challenge agree with their
  informal descriptions. You should know enough Lean to read them,
  or trust the libraries which provide them.
* It does not check that the theorem statements in the challenge correspond to
  their informal descriptions, so a Lean expert still has to confirm this,
  as described in the previous section.
  The [Palomar registry](https://palomar-registry.org/) also publishes
  the exact statements of the results it records, along with comments from its review.
* A challenge can leave a definition for the solution to fill in, using
  `definition_names` in the configuration. Many such challenges can be gamed:
  given `def ChallengeSolution : Prop := sorry` and
  `theorem challenge : RiemannHypothesis ↔ ChallengeSolution := sorry`,
  a solution can define `ChallengeSolution` to be `RiemannHypothesis`.
  A definition filled in this way always has to be reviewed.
* The result relies on some assumptions about how the command is run:
    * Everything imported by the challenge, the files `lakefile.toml` or `lakefile.lean`
      and `lake-manifest.json`, and all the dependencies they require, are trusted.
    * There is no existing `.lake` directory.
    * The command is run on Linux, with [`bubblewrap`](https://github.com/containers/bubblewrap)
      installed for the sandbox, and not by a privileged user.
    * Lean's kernel has no soundness bug which affects the proof.
      With `--paranoid`, the solution must also be accepted by the other
      checkers distributed with Lean, so this assumption only has to hold for one of them.

### Further documentation

The [Lean reference manual](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/#lake-comparator)
and `lake help comparator` describe the command and its options,
and the manual explains [what the check does and does not protect against](https://lean-lang.org/doc/reference/latest/ValidatingProofs/#validating-comparator).
These replace the instructions in the [standalone `comparator` repository](https://github.com/leanprover/comparator),
which is now archived.
