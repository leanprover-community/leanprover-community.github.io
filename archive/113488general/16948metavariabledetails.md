---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16948metavariabledetails.html
---

## [general](index.html)
### [metavariable details](16948metavariabledetails.html)

#### [Edward Ayers (Aug 16 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metavariable details/near/132255464):
In `metavar_context.h`, the class`metavar_decl` keeps a `local_context` field called `m_context`, which is the local context in which the mvar was created. In the system description it says "since only closed terms can be assigned to metavariables, a metavariable that occurs in a context records the parameters that it depends on". Is this what `m_context` is doing? Does closed here mean no unbound de-bruijn variables? The system description seems to imply that the context is stored as a telescope of `pi`s on the type of the mvar rather than in a special field in the declaration which is confusing me. Thanks

#### [Gabriel Ebner (Aug 16 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metavariable details/near/132255709):
The system description describes an old version of Lean where metavariables are handled differently.  The metavariables in Lean 3 can have free variables in the form of local constants.

#### [Gabriel Ebner (Aug 16 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metavariable details/near/132255801):
This is also the reason for the delayed_abstraction macro, if you've seen it before.  If you want to build `λ x, ?m_1` where `?m_1` could contain `x` as a free variable, then we insert a delayed_abstraction macro that tells Lean to replace the local constant by a de Bruijn variable when instantiating the metavariable.

#### [Gabriel Ebner (Aug 16 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metavariable details/near/132255930):
Re: publications.  Many of the publications on the website describe old versions of Lean.  I think the ICFP paper from last year (metaprogramming framework for formal verification) and the IJCAR paper from 2016 (congruence closure) are the only two which are up-to-date as of Lean 3.

