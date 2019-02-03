---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27699instanceobfuscation.html
---

## Stream: [general](index.html)
### Topic: [instance obfuscation](27699instanceobfuscation.html)

---


{% raw %}
#### [ Simon Hudon (Jan 30 2019 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20obfuscation/near/157203765):
<p>Every now and then, I use <code>rw</code> and I get a type class resolution problem as a side condition. If I work with <code>traversable</code>, I get <code>traversable (λ x, t x)</code> as a side condition while <code>traversable t</code> is in my context. Is there a way to avoid that? Also, is there a reason why type class resolution does not perform eta reduction first?</p>

#### [ Chris Hughes (Jan 30 2019 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20obfuscation/near/157204541):
<p>Usually giving the <code>rw</code> enough information to work out the type is good enough. So do <code>rw @lemma α</code> for example.</p>

#### [ Gabriel Ebner (Jan 30 2019 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20obfuscation/near/157205673):
<p>Is this a problem?  Instance search should transparently apply η:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">t</span><span class="o">}</span> <span class="o">[</span><span class="n">traversable</span> <span class="n">t</span><span class="o">]</span> <span class="o">:</span> <span class="n">traversable</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">t</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">infer_instance</span>
</pre></div>

#### [ Simon Hudon (Jan 30 2019 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20obfuscation/near/157211145):
<p>Oh, that's curious. Maybe <code>η</code> is not the problem then.</p>

#### [ Simon Hudon (Jan 30 2019 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20obfuscation/near/157211164):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> Thanks, I will do that. I was hoping it wouldn't come done to it though</p>


{% endraw %}
