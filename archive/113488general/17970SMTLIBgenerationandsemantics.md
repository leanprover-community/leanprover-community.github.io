---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/17970SMTLIBgenerationandsemantics.html
---

## Stream: [general](index.html)
### Topic: [SMTLIB generation and semantics](17970SMTLIBgenerationandsemantics.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joe Hendrix (Sep 14 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/SMTLIB%20generation%20and%20semantics/near/133980967):
Is there a library for representing and rendering SMTLIB 2 expressions that is compatible with Lean 3?  I'd like to have a library where I can generate SMTLIB (specifically the uninterpreted functions/sorts, bitvectors, and arrays), and express semantically what it means for a set of SMTLIB assertions to be satisfiable from a model-theoretic definition.  I can start one, but don't want to duplicate existing work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Sep 14 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/SMTLIB%20generation%20and%20semantics/near/133981366):
We have https://github.com/leanprover/smt2_interface. It should still work, hopefully

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joe Hendrix (Sep 15 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/SMTLIB%20generation%20and%20semantics/near/133983348):
Thanks, it looks like this has most of what I'd want.  Is this intended to be ported to be compatible with Lean4?  I'd like to also define a model theory for SMTLIB.  Is that something that you think would be welcome in this repo?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Sep 15 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/SMTLIB%20generation%20and%20semantics/near/133983745):
I don't think we have any specific plans for this package, but hopefully it should be quick to port. I don't have any specific thoughts about what should go in the package either, but perhaps it could be a separate package on top of smt2_interface?

