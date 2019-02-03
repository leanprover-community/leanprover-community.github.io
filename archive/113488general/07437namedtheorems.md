---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/07437namedtheorems.html
---

## Stream: [general](index.html)
### Topic: [named theorems](07437namedtheorems.html)

---


{% raw %}
#### [ Patrick Massot (Mar 12 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/named%20theorems/near/123598899):
<p>We had endless conversation about lemmas which don't have names in maths and need a name in a proof assistant. But what about theorems that do have a name? Now in mathlib we have the squeeze theorem, that some mathematicians call the sandwich theorem and French mathematicians call the "théorème des gendarmes" (gendarme is a military version of policeman) but <a href="https://github.com/leanprover/mathlib/blob/fe0f2a34b2bc71d480c5fc7766d889e0a4de3ccd/analysis/topology/topological_structures.lean#L346" target="_blank" title="https://github.com/leanprover/mathlib/blob/fe0f2a34b2bc71d480c5fc7766d889e0a4de3ccd/analysis/topology/topological_structures.lean#L346">mathlib</a> calls it: <code>tendsto_of_tendsto_of_tendsto_of_le_of_le</code> and we have Lagrange's theorem on the order of subgroups called <a href="https://github.com/leanprover/mathlib/blob/b97b7c38416d4f6f258882f807458d4f980976ef/group_theory/subgroup.lean#L88" target="_blank" title="https://github.com/leanprover/mathlib/blob/b97b7c38416d4f6f258882f807458d4f980976ef/group_theory/subgroup.lean#L88">in mathlib</a> <code>group_equiv_cosets_times_subgroup</code>. Isn't it slightly problematic?</p>

#### [ Patrick Massot (Mar 12 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/named%20theorems/near/123598900):
<p>At least the squeeze theorem can be found by docstring grep</p>

#### [ Simon Hudon (Mar 12 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/named%20theorems/near/123599118):
<p>I always thought that those names made it harder to learn a subject. For instance, I came across Abelian groups multiple times not remembering what it was about while  if it was referred to as a commutative group, I wouldn't even pause</p>

#### [ Patrick Massot (Mar 12 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/named%20theorems/near/123599119):
<p>Now I need to go to work (need do to stuff before that Gowers colloquium this afternoon)</p>

#### [ Mario Carneiro (Mar 12 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/named%20theorems/near/123599221):
<p>Personally, I prefer to relax the name-by-symbols approach for really famous or already named theorems. I would not have called it that tendsto tendsto tendsto thing, maybe some hybrid like <code>tendsto_squeeze</code>. For the second one, we could call it <code>lagrange_theorem</code> but the bigger issue is which of the possible slight variants on that theorem are to be <em>the</em> lagrange theorem</p>

#### [ Mario Carneiro (Mar 12 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/named%20theorems/near/123599234):
<p>I think I've mentioned this before, but I dislike theorems whose name has more than around 30 characters</p>

#### [ Andrew Ashworth (Mar 12 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/named%20theorems/near/123599292):
<p>i foresee for mathlib search by function name is going to become a big problem sooner rather than later</p>

#### [ Mario Carneiro (Mar 12 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/named%20theorems/near/123599406):
<p>To locate a result in mathlib, it is more effective to just go to the place where similar theorems are defined and look around. And topic organization is the relevant criterion for making this work, it is a much easier problem than good naming of all the theorems</p>

#### [ Johannes Hölzl (Mar 12 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/named%20theorems/near/123600532):
<p>I prefer to stay with the current system, as long as there is no proper search available. I also don't mind long theorem names as long as they are not used to often. For example the sandwich theorem is only used 15x in Isabelle's analysis. And usually at the beginning of a proof.</p>

#### [ Mario Carneiro (Mar 12 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/named%20theorems/near/123601262):
<p>Once you've disambiguated a theorem from all other theorems in the database, there's no further need to extend the name though. I honestly cannot imagine actually looking up the squeeze/sandwich theorem according to the symbols in its statement, especially since there is possible variation in that statement and a more high level description that indicates which variables are less than which is necessary for indicating the meaning anyway. In such a situation the conventional name is far more effective. (Plus, the whole reason for these naming conventions is because mathematicians never stepped up and named them themselves. When they do, I think it's better to defer to them.)</p>

#### [ Kevin Buzzard (Mar 12 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/named%20theorems/near/123601823):
<p>Maybe the simplest solution is just good docstrings, which mention all of the common names of a theorem. The fact that different cultures use the same ideas has always resulted in different naming conventions. I noticed when I lived in Paris that many results had some generic name in English but were called &lt;French person&gt;'s Theorem in French, for example (e.g. Bezout's Lemma, I had never heard it called that in the UK in the 90s).</p>


{% endraw %}
