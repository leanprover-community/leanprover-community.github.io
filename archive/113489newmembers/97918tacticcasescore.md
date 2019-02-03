---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/97918tacticcasescore.html
---

## Stream: [new members](index.html)
### Topic: [tactic.cases_core](97918tacticcasescore.html)

---


{% raw %}
#### [ Kenny Lau (Nov 24 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/tactic.cases_core/near/148270993):
<p>What is the output of <code>tactic.cases_core</code>?</p>

#### [ Mario Carneiro (Nov 24 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/tactic.cases_core/near/148271269):
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm">- Apply `cases_on` recursor, names for the new hypotheses are retrieved from `ns`.</span>
<span class="cm">   `h` must be a local constant. It returns for each new goal the name of the constructor, a list of new hypotheses, and a list of</span>
<span class="cm">   substitutions for hypotheses depending on `h`. The number of new goals may be smaller than the</span>
<span class="cm">   number of constructors. Some goals may be discarded when the indices to not match.</span>
<span class="cm">   See `induction` for information on the list of substitutions.</span>

<span class="cm">   The `cases` tactic is implemented using this one, and it relaxes the restriction of `h`. -/</span>
</pre></div>

#### [ Kenny Lau (Nov 24 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/tactic.cases_core/near/148286948):
<p>I don't really understand <code>a list of substitutions for hypotheses</code> and the fact that sometimes I get duplicates in that particular list</p>


{% endraw %}
