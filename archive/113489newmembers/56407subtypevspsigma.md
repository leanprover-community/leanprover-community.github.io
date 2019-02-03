---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/56407subtypevspsigma.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [subtype vs psigma](https://leanprover-community.github.io/archive/113489newmembers/56407subtypevspsigma.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sebastian Zimmer (Oct 14 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/subtype%20vs%20psigma/near/135787450):
<p>What is the difference between <code>{a:α // p a}</code> and <code>Σ' a, P a</code>?<br>
It seems like they are both a dependent pair.</p>

#### [ Chris Hughes (Oct 14 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/subtype%20vs%20psigma/near/135787505):
<p><code>psigma</code> is a less restrictive definition than <code>subtype</code>, because the second element does not have to be a proof, but for subtypes it does.</p>

#### [ Sebastian Zimmer (Oct 14 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/subtype%20vs%20psigma/near/135787529):
<p>So in the case where the second element is a proof, which one would you recommend using?</p>

#### [ Chris Hughes (Oct 14 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/subtype%20vs%20psigma/near/135787578):
<p>Definitely <code>subtype</code>. Subtypes have the extensionality rule, that two elements are equal iff the first of the pair is equal, which is very handy.</p>


{% endraw %}
