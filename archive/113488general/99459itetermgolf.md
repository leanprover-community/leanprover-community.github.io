---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99459itetermgolf.html
---

## Stream: [general](index.html)
### Topic: [ite term golf](99459itetermgolf.html)

---


{% raw %}
#### [ Andrew Ashworth (May 27 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ite%20term%20golf/near/127155648):
<p>Suppose I need to prove <code>ite (x = y) tt ff = tt → x = y</code> and <code>x = y → ite (x = y) tt ff = tt</code>. Is there a succint way to do this in term mode? (I know <code>simp</code> and <code>split_ifs</code> is amazing here, but I'd like to do inversion by hand if possible)</p>

#### [ Nicholas Scheel (May 27 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ite%20term%20golf/near/127156020):
<p>this should take care of the second part: <a href="https://github.com/leanprover/lean/blob/master/library/init/logic.lean#L839" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/logic.lean#L839">https://github.com/leanprover/lean/blob/master/library/init/logic.lean#L839</a></p>

#### [ Nicholas Scheel (May 27 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ite%20term%20golf/near/127156150):
<p>for the first part I wonder if something like the following would work (untested):</p>
<div class="codehilite"><pre><span></span>λ h,
if p : (x = y) then p else
  bool.no_confusion (eq.trans (eq.symm h) (if_neg p))
</pre></div>


<p>basically you decide the proposition (equivalent to the by_cases tactic) and then return the true case, or prove the false case is absurd</p>

#### [ Nicholas Scheel (May 27 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ite%20term%20golf/near/127156160):
<p>maybe this is easier than no_confusion: <a href="https://github.com/leanprover/lean/blob/master/library/init/logic.lean" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/logic.lean">https://github.com/leanprover/lean/blob/master/library/init/logic.lean</a></p>

#### [ Nicholas Scheel (May 27 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ite%20term%20golf/near/127156203):
<p><code>absurd (eq.symm (eq.trans .....)) bool.ff_ne_tt</code></p>

#### [ Nicholas Scheel (May 27 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ite%20term%20golf/near/127156220):
<p>btw I think this is just <code>if p then tt else ff</code>: <a href="https://github.com/leanprover/lean/blob/master/library/init/logic.lean#L590" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/logic.lean#L590">https://github.com/leanprover/lean/blob/master/library/init/logic.lean#L590</a></p>

#### [ Mario Carneiro (May 27 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ite%20term%20golf/near/127164043):
<p>use <code>to_bool</code>, it has lots of lemmas for this</p>

#### [ Andrew Ashworth (May 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ite%20term%20golf/near/127165905):
<p>thanks Nicholas / Mario for the pointers</p>


{% endraw %}
