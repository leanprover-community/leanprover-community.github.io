---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01274unfoldingnotationintheoremvsdefinstance.html
---

## Stream: [general](index.html)
### Topic: [unfolding notation in theorem vs def/instance](01274unfoldingnotationintheoremvsdefinstance.html)

---


{% raw %}
#### [ Kenny Lau (May 31 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/127341302):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">pi</span><span class="bp">.</span><span class="n">comm_ring_i</span> <span class="o">{</span><span class="n">I</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">I</span> <span class="bp">→</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">semigroup</span> <span class="err">$</span> <span class="n">f</span> <span class="n">i</span><span class="o">]</span> <span class="o">:</span> <span class="n">semigroup</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span> <span class="o">:</span> <span class="n">I</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">i</span><span class="o">,</span> <span class="n">x</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">y</span> <span class="n">i</span><span class="o">,</span>
  <span class="n">mul_assoc</span> <span class="o">:=</span> <span class="bp">_</span><span class="o">,</span> <span class="o">}</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">⊢ ∀ (a b c : Π (i : I), f i),</span>
<span class="cm">    (λ (x y : Π (i : I), f i) (i : I), semigroup.mul (x i) (y i))</span>
<span class="cm">        ((λ (x y : Π (i : I), f i) (i : I), semigroup.mul (x i) (y i)) a b)</span>
<span class="cm">        c =</span>
<span class="cm">      (λ (x y : Π (i : I), f i) (i : I), semigroup.mul (x i) (y i)) a</span>
<span class="cm">        ((λ (x y : Π (i : I), f i) (i : I), semigroup.mul (x i) (y i)) b c)</span>
<span class="cm">-/</span>

<span class="kn">theorem</span> <span class="n">pi</span><span class="bp">.</span><span class="n">comm_ring_t</span> <span class="o">{</span><span class="n">I</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">I</span> <span class="bp">→</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">semigroup</span> <span class="err">$</span> <span class="n">f</span> <span class="n">i</span><span class="o">]</span> <span class="o">:</span> <span class="n">semigroup</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span> <span class="o">:</span> <span class="n">I</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">i</span><span class="o">,</span> <span class="n">x</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">y</span> <span class="n">i</span><span class="o">,</span>
  <span class="n">mul_assoc</span> <span class="o">:=</span> <span class="bp">_</span><span class="o">,</span> <span class="o">}</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">⊢ ∀ (a b c : Π (i : I), f i), a * b * c = a * (b * c)</span>
<span class="cm">-/</span>
</pre></div>

#### [ Kenny Lau (May 31 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/127341307):
<p>The extra unfolding in <code>def</code> and <code>instance</code> is making things harder (I did not include example of <code>def</code>)</p>

#### [ Kenny Lau (May 31 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/127341309):
<p>i.e. the <code>*</code> becoming <code>semigroup.mul</code></p>

#### [ Kenny Lau (May 31 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/127341354):
<p>how can I avoid this? is this a bug?</p>

#### [ Kenny Lau (May 31 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/127341357):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Mario Carneiro (May 31 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/127341402):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span></p>

#### [ Kenny Lau (May 31 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/127341404):
<p>thanks</p>

#### [ Kenny Lau (May 31 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/127341411):
<p>temporary workaround: change it to <code>theorem</code> where it doesn't unfold, copy the goal, use <code>change</code>/<code>show</code>, and then switch back to <code>def</code></p>

#### [ Sebastian Ullrich (May 31 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/127348395):
<p>I'm not sure what is happening just by looking at it... but I'll leave for a short trip until Sunday soon</p>

#### [ Patrick Massot (May 31 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/127348933):
<p>I see that all the time. It's indeed a bit annoying</p>

#### [ Kenny Lau (Jun 13 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128009463):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span></p>

#### [ Kenny Lau (Jun 15 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128094754):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Sebastian Ullrich (Jun 15 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128110837):
<p>I'd have to go back to a debug build of Lean 3 to diagnose this, but it won't be fixed for Lean 3 anyway...</p>

#### [ Kevin Buzzard (Jun 15 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128111464):
<p>So just to be clear -- there is no point noting this down as an issue anywhere on github, because we all know it won't be fixed in Lean 3, and because Lean 4 is a complete rewrite it's very unlikely that the issue will remain in Lean 4? Or could it be the case that when Lean 4 comes, exactly the same issue will be there because chunks of code were basically copied from Lean 3, and then this issue should be marked as something which should be fixed in the future. What I'm trying to establish is whether this trickle of minor Lean 3 points which will not be fixed in Lean 3 should be recorded somewhere anyway, just to check Lean 4 does not suffer from the same problems. If the chances of Lean 4 suffering from the same problem is 0% then in this case there is no point recording anything formally.</p>

#### [ Sebastian Ullrich (Jun 15 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128113301):
<p>It's hard to say in general. There seems to be some bug somewhere in the elaborator here, which may very well survive into Lean 4 if we don't fix it specifically. _However_, Kenny's example will likely work because Lean 4 will elaborate the type and body of a <code>def/instance</code> separately if the former is given explicitly - so just like for <code>theorem</code>.</p>

#### [ Kenny Lau (Jun 16 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128167974):
<p>holy mother I found a workaround</p>

#### [ Kenny Lau (Jun 16 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128167975):
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>

<span class="kn">instance</span> <span class="n">pi</span><span class="bp">.</span><span class="n">comm_ring_i</span> <span class="o">{</span><span class="n">I</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">I</span> <span class="bp">→</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">semigroup</span> <span class="err">$</span> <span class="n">f</span> <span class="n">i</span><span class="o">]</span> <span class="o">:</span> <span class="n">semigroup</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span> <span class="o">:</span> <span class="n">I</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">i</span><span class="o">,</span> <span class="n">x</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">y</span> <span class="n">i</span><span class="o">,</span>
  <span class="n">mul_assoc</span> <span class="o">:=</span> <span class="bp">_</span><span class="o">,</span> <span class="o">}</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">⊢ ∀ (a b c : Π (i : I), f i),</span>
<span class="cm">    (λ (x y : Π (i : I), f i) (i : I), semigroup.mul (x i) (y i))</span>
<span class="cm">        ((λ (x y : Π (i : I), f i) (i : I), semigroup.mul (x i) (y i)) a b)</span>
<span class="cm">        c =</span>
<span class="cm">      (λ (x y : Π (i : I), f i) (i : I), semigroup.mul (x i) (y i)) a</span>
<span class="cm">        ((λ (x y : Π (i : I), f i) (i : I), semigroup.mul (x i) (y i)) b c)</span>
<span class="cm">-/</span>

<span class="kn">instance</span> <span class="n">pi</span><span class="bp">.</span><span class="n">comm_ring_i_uv</span> <span class="o">{</span><span class="n">I</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">I</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">semigroup</span> <span class="err">$</span> <span class="n">f</span> <span class="n">i</span><span class="o">]</span> <span class="o">:</span> <span class="n">semigroup</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span> <span class="o">:</span> <span class="n">I</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">i</span><span class="o">,</span> <span class="n">x</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">y</span> <span class="n">i</span><span class="o">,</span>
  <span class="n">mul_assoc</span> <span class="o">:=</span> <span class="bp">_</span><span class="o">,</span> <span class="o">}</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">⊢ ∀ (a b c : Π (i : I), f i), a * b * c = a * (b * c)</span>
<span class="cm">-/</span>

<span class="kn">theorem</span> <span class="n">pi</span><span class="bp">.</span><span class="n">comm_ring_t</span> <span class="o">{</span><span class="n">I</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">I</span> <span class="bp">→</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">semigroup</span> <span class="err">$</span> <span class="n">f</span> <span class="n">i</span><span class="o">]</span> <span class="o">:</span> <span class="n">semigroup</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span> <span class="o">:</span> <span class="n">I</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">i</span><span class="o">,</span> <span class="n">x</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">y</span> <span class="n">i</span><span class="o">,</span>
  <span class="n">mul_assoc</span> <span class="o">:=</span> <span class="bp">_</span><span class="o">,</span> <span class="o">}</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">⊢ ∀ (a b c : Π (i : I), f i), a * b * c = a * (b * c)</span>
<span class="cm">-/</span>
</pre></div>

#### [ Kenny Lau (Jun 16 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128167978):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> it can be avoided by using universes instead of <code>Type*</code></p>

#### [ Sebastian Ullrich (Jun 16 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128168239):
<p>Wow, nice find. Then I can probably explain it - there is some tricky code in the structure notation elaborator that needs to unfold terms that contain metavariables - apparently it also does that for universe mvars, which it probably shouldn't do. As I said above, when you use <code>theorem</code>, the body is elaborated separately from the type, so the mvars have already been solved.</p>

#### [ Mario Carneiro (Jun 16 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128169386):
<p>well, that was unexpected</p>

#### [ Kenny Lau (Jun 16 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128169426):
<p>finally something unexpected :P</p>

#### [ Johan Commelin (Jun 16 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128171397):
<p>I'm going to check if this will also simplify my code, and if it removes some of the issues that I've been have lately.</p>

#### [ Johan Commelin (Jun 16 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128171404):
<p>But it will have to wait till Monday before I get back to Lean.</p>

#### [ Kevin Buzzard (Jun 16 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20notation%20in%20theorem%20vs%20def/instance/near/128178398):
<p>I write all my code just using Type. I believe in ZFC!</p>


{% endraw %}
