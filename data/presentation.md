## Lean and its Mathematical Library

The [Lean theorem prover](https://leanprover.github.io)
is a proof assistant developed principally by Leonardo de Moura at Microsoft Research.

The Lean mathematical library, *mathlib*, is a community-driven effort
to build a unified library of mathematics formalized in the
Lean proof assistant. The library also contains definitions
useful for programming. This project is very active, with many
regular contributors and daily activity.

The contents, design, and community organization of mathlib are
described in the paper
[The Lean mathematical library](https://arxiv.org/abs/1910.09336), which appeared
at CPP 2020. You can get a bird's eye view of what is in the library by
reading [the library overview](mathlib-overview.html).
You can also have a look at our [repository statistics](mathlib_stats.html)
to see how it grows and who contributes to it.

## What is a proof assistant?

A *proof assistant* is a piece of software that provides a language
for defining objects, specifying properties of these objects, 
and proving that these specifications hold.
The system checks that these proofs are correct down to their logical foundation.

These tools are often used to verify the correctness of programs.
But they can also be used for abstract mathematics,
which is something of interest to the mathlib community.
In a formalization, all definitions are precisely specified
and all proofs are virtually guaranteed to be correct.