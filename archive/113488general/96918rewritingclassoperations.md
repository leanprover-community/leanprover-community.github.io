---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/96918rewritingclassoperations.html
---

## Stream: [general](index.html)
### Topic: [rewriting class operations](96918rewritingclassoperations.html)

---


{% raw %}
#### [ Reid Barton (Jun 05 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20class%20operations/near/127602788):
<p>I have this instance:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">Xplus</span><span class="bp">.</span><span class="n">setoid</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">Xplus</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">Xplus_rel</span><span class="o">,</span> <span class="n">Xplus_rel</span><span class="bp">.</span><span class="n">refl</span><span class="o">,</span> <span class="n">Xplus_rel</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span> <span class="n">Xplus_rel</span><span class="bp">.</span><span class="n">trans</span><span class="bp">⟩</span>
</pre></div>


<p>How can I use a tactic to rewrite <code>a ≈ b</code> somewhere in the goal to <code>Xplus_rel a b</code>?</p>

#### [ Reid Barton (Jun 05 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20class%20operations/near/127602900):
<p>Is there some name I can pass to <code>rw</code> or <code>simp</code>?</p>

#### [ Kenny Lau (Jun 05 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20class%20operations/near/127602930):
<p><code>set_option pp.notations false</code></p>

#### [ Simon Hudon (Jun 05 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20class%20operations/near/127602986):
<p>Does <code>change Xplus_rel a b</code> do it for you?</p>

#### [ Sebastian Ullrich (Jun 05 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20class%20operations/near/127603021):
<p><code>simp [(≈)]</code> should do it</p>

#### [ Reid Barton (Jun 05 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20class%20operations/near/127603023):
<p><code>change</code> works if I write out the whole new goal (which isn't bad at all using copious <code>_</code>s)</p>

#### [ Reid Barton (Jun 05 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20class%20operations/near/127603087):
<p><code>simp [(≈)]</code> turned it into <code>setoid.r</code>, not <code>Xplus_rel</code></p>

#### [ Reid Barton (Jun 05 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20class%20operations/near/127603093):
<p>Oh, but <code>[(≈), setoid.r]</code> worked</p>

#### [ Kenny Lau (Jun 05 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20class%20operations/near/127603099):
<p><code>≈</code> is literally <code>setoid.r</code></p>

#### [ Reid Barton (Jun 05 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20class%20operations/near/127603112):
<p>No, it's literally <code>has_equiv.equiv</code></p>

#### [ Kenny Lau (Jun 05 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20class%20operations/near/127603118):
<p>oh</p>

#### [ Reid Barton (Jun 05 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20class%20operations/near/127603181):
<p>Great, this is better than what I had before. I feel like I run into this a lot</p>

#### [ Chris Hughes (Jun 05 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20class%20operations/near/127604658):
<p>I often use <code>show Xplus_rel a b</code> in these situtations.</p>

#### [ Simon Hudon (Jun 05 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20class%20operations/near/127604971):
<p>That's similar to <code>change</code> but <span class="user-mention" data-user-id="110032">@Reid Barton</span> pointed out that that only works if there's nothing else in your goal.</p>

#### [ Chris Hughes (Jun 05 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20class%20operations/near/127605892):
<p><code>show Xplus_rel _ _</code></p>

#### [ Simon Hudon (Jun 05 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20class%20operations/near/127606006):
<p>That doesn't work if the goal is <code>p ∧ Xplus_rel a b</code></p>

#### [ Kenny Lau (Jun 05 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20class%20operations/near/127606012):
<p><code>split</code></p>

#### [ Simon Hudon (Jun 05 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20class%20operations/near/127606149):
<p>This is an ad hoc response to it. <span class="user-mention" data-user-id="110032">@Reid Barton</span> Is looking for one solution that will work for a variety of goals</p>

#### [ Reid Barton (Jun 05 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20class%20operations/near/127606159):
<p>And won't get longer the longer my goal is</p>


{% endraw %}
