# Papers

### Papers about Lean
* Daniel Selsam, Simon Hudon, and Leonardo de Moura. [*Sealing Pointer-Based Optimizations Behind Pure Functions.*](https://arxiv.org/abs/2003.01685) arXiv 2020.
* Sebastian Ullrich and Leonardo de Moura. [*Beyond Notations: Hygienic Macro Expansion for Theorem Proving Languages.*](https://arxiv.org/abs/2001.10490) arXiv 2020. 
* Daniel Selsam, Sebastian Ullrich, and Leonardo de Moura. [*Tabled Typeclass Resolution.*](https://arxiv.org/pdf/2001.04301.pdf) arXiv 2020.
  * The new type class resolution procedure in Lean 4.
* Mario Carneiro. [*The Type Theory of Lean.*](https://github.com/digama0/lean-type-theory/releases) Master thesis, 2019.
  * Meta-theoretic properties of Lean 3, including soundness.
* Sebastian Ullrich, Leonardo de Moura. [*Counting Immutable Beans: Reference Counting Optimized for Purely Functional Programming.*](https://arxiv.org/abs/1908.05647) preprint 2019.
  * Reference counting in Lean 4 ([appendix](https://leanprover.github.io/papers/beans_appendix.pdf), [partial formalization](https://github.com/mhuisi/rc-correctness), [bachelor thesis about partial formalization](https://pp.ipd.kit.edu/uploads/publikationen/huisinga19bachelorarbeit.pdf)).
* Gabriel Ebner, Sebastian Ullrich, Jared Roesch, Jeremy Avigad, and Leonardo de Moura. [*A metaprogramming framework for formal verification.*](https://dl.acm.org/citation.cfm?id=3110278) ICFP 2017.
  * Metaprogramming in Lean 3.
* Daniel Selsam and Leonardo de Moura. [*Congruence Closure in Intensional Type Theory.*](https://leanprover.github.io/papers/congr.pdf) IJCAR 2016.
  * Congruence closure in Lean 3.
* Leonardo de Moura, Soonho Kong, Jeremy Avigad, Floris van Doorn, Jakob von Raumer. [*The Lean Theorem Prover (System Description).*](https://kilthub.cmu.edu/articles/The_Lean_Theorem_Prover_system_description_/6492815/files/11937416.pdf) CADE 2015.
  * System description of Lean 2
* Leonardo de Moura, Jeremy Avigad, Soonho Kong, Cody Roux. [*Elaboration in Dependent Type Theory.*](https://arxiv.org/abs/1505.04324) 2015 (unpublished).
  * Elaboration in Lean 2.

### Papers using Lean
* Anne Baanen. [*A Lean tactic for normalising ring expressions with exponents*](https://lean-forward.github.io/ring_exp/paper.pdf) IJCAR 2020.
* Floris van Doorn, Gabriel Ebner, and Robert Y. Lewis. [*Maintaining a Library of Formal Mathematics.*](https://lean-forward.github.io/mathlib-maintenance/paper.pdf)
* Robert Y. Lewis and Paul-Nicolas Madelaine. [*Normalizing Casts and Coercions.*](https://arxiv.org/abs/2001.10594) arXiv 2020.
* The mathlib Community. [*The Lean mathematical library.*](https://arxiv.org/abs/1910.09336) CPP 2020.
  * [mathlib](https://github.com/leanprover-community/mathlib)
* Kevin Buzzard, Johan Commelin, Patrick Massot. [*Formalising perfectoid spaces.*](https://arxiv.org/abs/1910.12320) CPP 2020.
  * [Formalization](https://github.com/leanprover-community/lean-perfectoid-spaces)
* Jesse Michael Han and Floris van Doorn. [*A Formal Proof of the Independence of the Continuum Hypothesis.*](https://github.com/flypitch/flypitch-cpp-2020/releases/tag/1.0) CPP 2020.
  * [Formalization](https://github.com/flypitch/flypitch) / [Website](https://flypitch.github.io/)
* Sander R. Dahmen, Johannes Hölzl, Robert Y. Lewis. [Formalizing the Solution to the Cap Set Problem.](https://arxiv.org/abs/1907.01449) ITP 2019.
  * [Formalization](https://github.com/lean-forward/cap_set_problem)
* Minchao Wu and Rajeev Goré. [*Verified decision procedures for modal logics.*](http://drops.dagstuhl.de/opus/volltexte/2019/11086/pdf/LIPIcs-ITP-2019-31.pdf) ITP 2019.
  * [Formalization](https://github.com/minchaowu/ModalTab)
* Mario Carneiro. [*Formalizing computability theory via partial recursive functions.*](https://arxiv.org/abs/1810.08380) ITP 2019.
  * Formalization in [mathlib/computability](https://github.com/leanprover-community/mathlib/tree/master/src/computability)
* Jesse Michael Han and Floris van Doorn. [*A formalization of forcing and the unprovability of the continuum hypothesis.*](https://arxiv.org/pdf/1904.10570.pdf) ITP 2019.
  * [Formalization](https://github.com/flypitch/flypitch) / [Website](https://flypitch.github.io/)
* Jeremy Avigad, Mario Carneiro, and Simon Hudon. [*Data types as quotients of polynomial functors.*](https://www.andrew.cmu.edu/user/avigad/Papers/qpf.pdf) ITP 2019.
  * [Formalization](https://github.com/avigad/qpf)
* Juneyoung Lee, Chung-Kil Hur, and Nuno P. Lopes [*AliveInLean: A Verified LLVM Peephole Optimization Verifier.*](https://sf.snu.ac.kr/publications/aliveinlean.pdf) CAV 2019.
  * [Formalization](https://github.com/microsoft/aliveinlean) / [Website](https://sf.snu.ac.kr/aliveinlean/)
* Robert Y. Lewis. [*A formal proof of Hensel's lemma over the p-adic integers.*](https://robertylewis.com/padics/padics.pdf) CPP 2019.
  * The [formalization](https://github.com/leanprover-community/mathlib/tree/master/src/data/padics) is part of mathlib. [Website](https://robertylewis.com/padics/).
* Daniel Selsam, Percy Liang, David L. Dill [*Developing Bug-Free Machine Learning Systems With Formal Mathematics.*](https://arxiv.org/abs/1706.08605) ICML 2017.
  * [Formalization](https://github.com/dselsam/certigrad)
* Robert Y. Lewis. [*A bi-directional extensible ad hoc interface between Lean and Mathematica.*](https://robertylewis.com/leanmm/lean_mm.pdf) PxTP 2017.
  * [Formalization](https://github.com/robertylewis/mathematica) / [Website](https://robertylewis.com/leanmm/)

### Unpublished works using Lean
* Paul-Nicolas Madelaine. [*Arithmetic and Casting in Lean.*](https://lean-forward.github.io/norm_cast/norm_cast.pdf). 
  * A description of the [`norm_cast` tactic](https://github.com/leanprover-community/mathlib/blob/master/src/tactic/norm_cast.lean) in mathlib.
  * [Internship report](https://lean-forward.github.io/internships/arithmetic_and_casting_in_lean.pdf), 2019.
* Neil Strickland, Nicola Bellumat [*Iterated chromatic localisation.*](https://arxiv.org/abs/1907.07801) arXiv 2019.
  * [Formalization](https://github.com/NeilStrickland/itloc)
* Marc Huisinga. [*Formally Verified Insertion of Reference Counting Instructions.*](https://pp.ipd.kit.edu/uploads/publikationen/huisinga19bachelorarbeit.pdf) Bachelor thesis, 2019.
  * [Formalization](https://github.com/mhuisi/rc-correctness)
* Ramon Fernández Mir. [*Schemes in Lean.*](https://www.imperial.ac.uk/media/imperial-college/faculty-of-engineering/computing/public/1819-ug-projects/Fernandez-I-MirR-Schemes-in-Lean.pdf) Project report, 2019.
  * [Formalization](https://github.com/ramonfmir/lean-scheme)
* More reports/theses are listed on the [Lean Forward project page](https://lean-forward.github.io/#papers).
