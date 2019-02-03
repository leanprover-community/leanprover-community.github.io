---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91772mypolynomialperformance.html
---

## Stream: [general](index.html)
### Topic: [my_polynomial performance](91772mypolynomialperformance.html)

---


{% raw %}
#### [ Reid Barton (Nov 17 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147887874):
<p>I tried proving that the polynomial ring functor is left adjoint to the forgetful functor CommRing -&gt; Set but I gave up because doing anything with <code>mv_polynomial</code> was so slow. <span class="user-mention" data-user-id="110064">@Kenny Lau</span> you were having similar problems with <code>mv_polynomial</code> right?<br>
I think something is wrong there, but I couldn't figure out what.</p>

#### [ Kenny Lau (Nov 17 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147887984):
<p>yes, something is wrong</p>

#### [ Kenny Lau (Nov 17 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147887985):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what do you think?</p>

#### [ Mario Carneiro (Nov 18 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147895390):
<p>I think something is wrong</p>

#### [ Kenny Lau (Nov 18 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147895486):
<p>...</p>

#### [ Mario Carneiro (Nov 18 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147895501):
<p>my impression is that lean is having to solve enormous typeclass problems, I'm not sure if that's the whole problem</p>

#### [ Kenny Lau (Nov 18 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147895542):
<p>would you know specifically what is the problem with mv_polynomial and polynomial?</p>

#### [ Mario Carneiro (Nov 18 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147895552):
<p>if you look at the pp.all versions of any of the theorem statements, what looks like five tokens fills several pages</p>

#### [ Kenny Lau (Nov 18 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147895597):
<p>I don't think <code>pp.all</code> tells us <em>all</em> about the situation</p>

#### [ Kenny Lau (Nov 18 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147895603):
<p>but sure it tells us a lot</p>

#### [ Mario Carneiro (Nov 18 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147895604):
<p>yeah it doesn't know when to shut up</p>


{% endraw %}
