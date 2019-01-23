---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26974Substructuraltypesystems.html
---

## Stream: [general](index.html)
### Topic: [Substructural type systems](26974Substructuraltypesystems.html)

---


{% raw %}
#### [ Wojciech Nawrocki (Oct 31 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Substructural%20type%20systems/near/136882886):
Has anyone looked at or is familiar with Lean formalisations of substructural type systems (like linear types whose instances have to be used exactly once)?

#### [ Wojciech Nawrocki (Nov 20 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Substructural%20type%20systems/near/148018930):
If not that, perhaps someone has tried at least the base stuff like progress and preservation for simply-typed lambda calculus? I'm trying to follow [Programming Language Foundations](https://softwarefoundations.cis.upenn.edu/current/plf-current/index.html), except using de Brujin indices, but struggling a bit with the different Coq vs. Lean tactics.

#### [ Andrew Ashworth (Nov 20 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Substructural%20type%20systems/near/148019057):
Ah, I know a contributor to Rust posted here once asking about linear types, but unfortunately I don't think they are an active member of this chat room

#### [ Andrew Ashworth (Nov 20 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Substructural%20type%20systems/near/148019058):
if you have tactic questions feel free to ask, though

#### [ Andrew Ashworth (Nov 20 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Substructural%20type%20systems/near/148019171):
although, looking over PLF, I don't know a good replacement for `eapply` and friends

#### [ Wojciech Nawrocki (Nov 20 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Substructural%20type%20systems/near/148019190):
Hm, how about `inversion`?

#### [ Andrew Ashworth (Nov 20 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Substructural%20type%20systems/near/148019203):
`cases` will do it

#### [ Mario Carneiro (Nov 20 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Substructural%20type%20systems/near/148023886):
I think @**Floris van Doorn** did some work with PTSs in lean, and he is currently working on model theory for first order logic using de bruijn indices. I don't know how much of his stuff is available or applicable to you though

#### [ Floris van Doorn (Nov 20 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Substructural%20type%20systems/near/148050772):
I have not done PTSs in Lean, but in Coq only: http://florisvandoorn.com/ptsf/index.html
I'm now indeed working on first-order logic in Lean also using de Bruijn variables: https://github.com/flypitch/flypitch/blob/master/src/fol.lean
First-order logic is a bit simpler than lambda calculus, but the bookkeeping with de Bruijn variables is the same (search for `lift_term_at`, `lift_formula_at`, `subst_term` and `subst_formula` and their properties).


{% endraw %}
