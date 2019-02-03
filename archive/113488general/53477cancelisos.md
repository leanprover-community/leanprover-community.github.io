---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53477cancelisos.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [cancel isos](https://leanprover-community.github.io/archive/113488general/53477cancelisos.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Aug 23 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cancel%20isos/near/132617646):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Somehow, <code>cancel_epi</code> with <code>f = ↑i</code> (<code>i : x ≅ y</code>) doesn't work any more.<br>
I managed to track this down far enough to find that adding the line (which used to be in <code>tidy.tidy</code>)</p>
<div class="codehilite"><pre><span></span><span class="n">attribute</span> <span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="n">lift_t</span> <span class="n">coe_t</span> <span class="n">coe_b</span>
</pre></div>


<p>makes it work again. But I don't really understand what is going on.</p>

#### [ Scott Morrison (Aug 23 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cancel%20isos/near/132620408):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>, thanks for all these requests. I am giving a demo in a few hours of parts of <code>obviously</code> and my category theory library, and right after that I will address these three issues!</p>

#### [ Scott Morrison (Aug 23 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cancel%20isos/near/132620460):
<p>The last one is a bit interesting: I'm now very careful to have my automation _not_ unfold too much, and <code>cancel_epi</code> is having trouble seeing through a coercion that formerly someone else was unfolding.  I'll have to find another solution. If you have a MWE showing the cancel_epi issue that would be great.</p>

#### [ Reid Barton (Aug 23 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cancel%20isos/near/132645544):
<p>Yes, I think the situation with <code>cancel_epi</code> makes sense to me now. Probably the right thing to do is just to add a second instance which matches <code>↑i</code> (in addition to the existing instance which matches <code>i.hom</code>).</p>

#### [ Scott Morrison (Aug 25 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cancel%20isos/near/132751886):
<p>Okay, this issue should be fixed in <a href="https://github.com/leanprover/mathlib/pull/278/commits/ccb1adf8a0fba114c5cbcad0169212d4775517d7" target="_blank" title="https://github.com/leanprover/mathlib/pull/278/commits/ccb1adf8a0fba114c5cbcad0169212d4775517d7">https://github.com/leanprover/mathlib/pull/278/commits/ccb1adf8a0fba114c5cbcad0169212d4775517d7</a>, which is part of <a href="https://github.com/leanprover/mathlib/pull/278" target="_blank" title="https://github.com/leanprover/mathlib/pull/278">https://github.com/leanprover/mathlib/pull/278</a>.</p>

#### [ Patrick Massot (Aug 25 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cancel%20isos/near/132751892):
<p>I'm happy to see you are enjoying your Paris sightseeing</p>

#### [ Scott Morrison (Aug 25 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cancel%20isos/near/132751968):
<p>:-)</p>

#### [ Scott Morrison (Aug 25 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cancel%20isos/near/132751971):
<p>I went out and ate lots of pastries and cheese this morning. :-)</p>

#### [ Scott Morrison (Aug 25 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cancel%20isos/near/132752029):
<p>Also I can see the Notre Dame from where I'm sitting.</p>

#### [ Patrick Massot (Aug 25 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cancel%20isos/near/132753363):
<p>Cheese, Notre-Dame and Lean seems to be a good combination</p>


{% endraw %}
