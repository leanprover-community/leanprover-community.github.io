---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/78098simplestructuralequality.html
---

## Stream: [new members](index.html)
### Topic: [simple structural equality](78098simplestructuralequality.html)

---


{% raw %}
#### [ Edward Ayers (Aug 08 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121507):
<p>How would I prove this?</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">mystr</span> <span class="o">:=</span>
    <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
    <span class="o">(</span><span class="n">B</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span>
    <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">&gt;</span> <span class="mi">10</span><span class="o">)</span>

<span class="n">def</span> <span class="n">mystr_eq</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">mystr</span><span class="o">)</span> <span class="o">(</span><span class="n">A_eq</span> <span class="o">:</span> <span class="n">x</span><span class="bp">.</span><span class="n">A</span> <span class="bp">=</span> <span class="n">y</span><span class="bp">.</span><span class="n">A</span><span class="o">)</span> <span class="o">(</span><span class="n">B_eq</span> <span class="o">:</span> <span class="n">x</span><span class="bp">.</span><span class="n">B</span> <span class="bp">=</span> <span class="n">y</span><span class="bp">.</span><span class="n">B</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span>
<span class="o">:=</span> <span class="k">by</span> <span class="n">sorry</span>
</pre></div>

#### [ Patrick Massot (Aug 08 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121866):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">mystr_eq</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">mystr</span><span class="o">)</span> <span class="o">(</span><span class="n">A_eq</span> <span class="o">:</span> <span class="n">x</span><span class="bp">.</span><span class="n">A</span> <span class="bp">=</span> <span class="n">y</span><span class="bp">.</span><span class="n">A</span><span class="o">)</span> <span class="o">(</span><span class="n">B_eq</span> <span class="o">:</span> <span class="n">x</span><span class="bp">.</span><span class="n">B</span> <span class="bp">=</span> <span class="n">y</span><span class="bp">.</span><span class="n">B</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span>
<span class="o">:=</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">x</span> <span class="bp">;</span> <span class="n">cases</span> <span class="n">y</span> <span class="bp">;</span> <span class="n">cc</span>
</pre></div>

#### [ Edward Ayers (Aug 08 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121909):
<p>thanks</p>

#### [ Mario Carneiro (Aug 08 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121919):
<p><code>congr</code>?</p>

#### [ Edward Ayers (Aug 08 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121937):
<p>next question: how to prove it without tactics? Just a proof term.</p>

#### [ Patrick Massot (Aug 08 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121944):
<p><code>congr ; assumption</code> instead of <code>cc</code> also works</p>

#### [ Mario Carneiro (Aug 08 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121952):
<p><code>congr'</code> too</p>

#### [ Johan Commelin (Aug 08 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121953):
<p>It's longer though</p>

#### [ Patrick Massot (Aug 08 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121955):
<p>but is much longer to type</p>

#### [ Patrick Massot (Aug 08 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121960):
<p>still longer</p>

#### [ Mario Carneiro (Aug 08 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121965):
<p><code>cc</code> is longer to run</p>

#### [ Johan Commelin (Aug 08 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121967):
<p>I suppose <code>congr; cc</code> works</p>

#### [ Johan Commelin (Aug 08 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121976):
<p>Can't we have <code>congra</code>?</p>

#### [ Edward Ayers (Aug 08 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121978):
<p><code>by congr ; assumption</code> fails on <code>congr</code> for me</p>

#### [ Mario Carneiro (Aug 08 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121980):
<p><code>congr'</code></p>

#### [ Mario Carneiro (Aug 08 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131121985):
<p>is <code>congra</code></p>

#### [ Mario Carneiro (Aug 08 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131122043):
<p>you have to do <code>cases</code> first</p>

#### [ Mario Carneiro (Aug 08 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131122165):
<p>term proof:</p>
<div class="codehilite"><pre><span></span>theorem mystr_eq : ∀ (x y : mystr) (A_eq : x.A = y.A) (B_eq : x.B = y.B), x = y
| ⟨xA, xB, xp⟩ ⟨_, _, _⟩ rfl rfl := rfl
</pre></div>

#### [ Kevin Buzzard (Aug 08 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simple%20structural%20equality/near/131122397):
<p>I was about to post that term proof but Mario just beat me to it. When I was a beginner I found those sorts of proofs miraculous; that's why I thought it was worth mentioning. The equation compiler is so clever.</p>


{% endraw %}
