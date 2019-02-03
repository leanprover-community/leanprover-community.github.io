---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/73693groupone.html
---

## Stream: [general](index.html)
### Topic: [group.one?](73693groupone.html)

---


{% raw %}
#### [ Kenny Lau (Sep 02 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group.one%3F/near/133204605):
<p>This is the definition of <code>group</code>:</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">group</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">monoid</span> <span class="n">α</span><span class="o">,</span> <span class="n">has_inv</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">mul_left_inv</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">a</span><span class="bp">⁻¹</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span>
</pre></div>


<p>then how does this produce <code>group.one</code>?</p>

#### [ Reid Barton (Sep 02 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group.one%3F/near/133205871):
<p>Probably <code>monoid</code> extends <code>has_one</code>?</p>

#### [ Simon Hudon (Sep 02 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group.one%3F/near/133205875):
<p>Yes it does and <code>group</code> is an <code>old_structure</code></p>


{% endraw %}
