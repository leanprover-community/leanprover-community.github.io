---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/13495Simplifyingoutlogicaljunk.html
---

## Stream: [new members](index.html)
### Topic: [Simplifying out logical junk](13495Simplifyingoutlogicaljunk.html)

---


{% raw %}
#### [ Ken Roe (Jul 28 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Simplifying%20out%20logical%20junk/near/130445253):
<p>How can the following theorem be proven:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">junk</span> <span class="o">{</span> <span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">}</span> <span class="o">{</span> <span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="n">p</span> <span class="bp">∨</span> <span class="o">(</span><span class="n">q</span> <span class="bp">→</span> <span class="n">false</span><span class="o">))</span><span class="bp">=</span><span class="n">p</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Jul 28 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Simplifying%20out%20logical%20junk/near/130445495):
<p>I don't think the theorem hold. If <code>p</code> is false and <code>q</code> is false too, the left hand side is true and the right hand side is false</p>


{% endraw %}
