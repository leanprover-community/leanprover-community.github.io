---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35032Whathappenednext.html
---

## Stream: [general](index.html)
### Topic: [What happened next?](35032Whathappenednext.html)

---


{% raw %}
#### [ Kevin Buzzard (Apr 04 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20happened%20next%3F/near/124638598):
<div class="codehilite"><pre><span></span>example (d : ℕ) (H : 1  =  2  * nat.succ d) : 1  =  2  * d +  2  :=
begin
rw H,
-- goal now?
admit,
end
</pre></div>

#### [ Kevin Buzzard (Apr 04 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20happened%20next%3F/near/124638609):
<p>Took me slightly by surprise at the time.</p>

#### [ Mario Carneiro (Apr 04 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20happened%20next%3F/near/124639398):
<p>heh, I assume <code>2</code> got rewritten?</p>

#### [ Kevin Buzzard (Apr 04 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20happened%20next%3F/near/124640156):
<p>That was part of it.</p>

#### [ Kevin Buzzard (Apr 04 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20happened%20next%3F/near/124640252):
<p>The other phenomenon shows itself here:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">=</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">=</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">rw</span> <span class="n">H</span><span class="o">,</span>
<span class="c1">-- goal now?</span>
<span class="n">admit</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 04 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20happened%20next%3F/near/124640326):
<p>Oh I have just realised what is going on.</p>

#### [ Kevin Buzzard (Apr 04 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20happened%20next%3F/near/124640331):
<p>So the goal becomes</p>

#### [ Kevin Buzzard (Apr 04 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20happened%20next%3F/near/124640335):
<p><code> bit0 x = y </code></p>

#### [ Kevin Buzzard (Apr 04 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20happened%20next%3F/near/124640345):
<p>but that's because <code>2</code> isn't defined to be <code>succ 1</code> here, it's defined to be <code>bit0 1</code></p>


{% endraw %}
