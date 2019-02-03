---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26974Substructuraltypesystems.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Substructural type systems](https://leanprover-community.github.io/archive/113488general/26974Substructuraltypesystems.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Wojciech Nawrocki (Oct 31 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Substructural%20type%20systems/near/136882886):
<p>Has anyone looked at or is familiar with Lean formalisations of substructural type systems (like linear types whose instances have to be used exactly once)?</p>

#### [ Wojciech Nawrocki (Nov 20 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Substructural%20type%20systems/near/148018930):
<p>If not that, perhaps someone has tried at least the base stuff like progress and preservation for simply-typed lambda calculus? I'm trying to follow <a href="https://softwarefoundations.cis.upenn.edu/current/plf-current/index.html" target="_blank" title="https://softwarefoundations.cis.upenn.edu/current/plf-current/index.html">Programming Language Foundations</a>, except using de Brujin indices, but struggling a bit with the different Coq vs. Lean tactics.</p>

#### [ Andrew Ashworth (Nov 20 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Substructural%20type%20systems/near/148019057):
<p>Ah, I know a contributor to Rust posted here once asking about linear types, but unfortunately I don't think they are an active member of this chat room</p>

#### [ Andrew Ashworth (Nov 20 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Substructural%20type%20systems/near/148019058):
<p>if you have tactic questions feel free to ask, though</p>

#### [ Andrew Ashworth (Nov 20 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Substructural%20type%20systems/near/148019171):
<p>although, looking over PLF, I don't know a good replacement for <code>eapply</code> and friends</p>

#### [ Wojciech Nawrocki (Nov 20 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Substructural%20type%20systems/near/148019190):
<p>Hm, how about <code>inversion</code>?</p>

#### [ Andrew Ashworth (Nov 20 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Substructural%20type%20systems/near/148019203):
<p><code>cases</code> will do it</p>

#### [ Mario Carneiro (Nov 20 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Substructural%20type%20systems/near/148023886):
<p>I think <span class="user-mention" data-user-id="111080">@Floris van Doorn</span> did some work with PTSs in lean, and he is currently working on model theory for first order logic using de bruijn indices. I don't know how much of his stuff is available or applicable to you though</p>

#### [ Floris van Doorn (Nov 20 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Substructural%20type%20systems/near/148050772):
<p>I have not done PTSs in Lean, but in Coq only: <a href="http://florisvandoorn.com/ptsf/index.html" target="_blank" title="http://florisvandoorn.com/ptsf/index.html">http://florisvandoorn.com/ptsf/index.html</a><br>
I'm now indeed working on first-order logic in Lean also using de Bruijn variables: <a href="https://github.com/flypitch/flypitch/blob/master/src/fol.lean" target="_blank" title="https://github.com/flypitch/flypitch/blob/master/src/fol.lean">https://github.com/flypitch/flypitch/blob/master/src/fol.lean</a><br>
First-order logic is a bit simpler than lambda calculus, but the bookkeeping with de Bruijn variables is the same (search for <code>lift_term_at</code>, <code>lift_formula_at</code>, <code>subst_term</code> and <code>subst_formula</code> and their properties).</p>


{% endraw %}
