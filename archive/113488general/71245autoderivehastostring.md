---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/71245autoderivehastostring.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [auto derive has_to_string](https://leanprover-community.github.io/archive/113488general/71245autoderivehastostring.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Zesen Qian (Jul 21 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20derive%20has_to_string/near/130069413):
<p>RT, something like this in lean?</p>

#### [ Mario Carneiro (Jul 21 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20derive%20has_to_string/near/130069676):
<p>No, I don't think this one has a derive handler, although you could totally write one</p>

#### [ Simon Hudon (Jul 21 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20derive%20has_to_string/near/130069770):
<p>If you don't mind going into <code>meta</code>-land, you can derive <code>has_reflect</code> for your type and use the following to just pretty-print the Lean expression that corresponds to a value of your type:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">to_string&#39;</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">has_reflect</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">string</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">to_fmt</span> <span class="o">(</span><span class="n">reflect</span> <span class="n">x</span><span class="o">))</span><span class="bp">.</span><span class="n">to_string</span>
</pre></div>

#### [ Zesen Qian (Jul 21 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20derive%20has_to_string/near/130070006):
<p><code>has_reflect</code> asks me to provide a <code>expr</code> for every value? Not sure how to do it for my type.</p>

#### [ Zesen Qian (Jul 21 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20derive%20has_to_string/near/130070023):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> yeah, it's just a very long type.</p>

#### [ Simon Hudon (Jul 21 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20derive%20has_to_string/near/130070026):
<p>You write <code>@[derive has_reflect]</code> above your type definition</p>

#### [ Mario Carneiro (Jul 21 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20derive%20has_to_string/near/130070074):
<p>I meant write a derive handler</p>

#### [ Zesen Qian (Jul 21 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20derive%20has_to_string/near/130070106):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> very cool, thanks.</p>

#### [ Simon Hudon (Jul 21 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20derive%20has_to_string/near/130070171):
<p>You're welcome</p>

#### [ Simon Hudon (Jul 21 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20derive%20has_to_string/near/130070237):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Such a derive handler seems like a lot of work but I'm wondering if piggy backing on top of <code>has_reflect</code> might help us be extra lazy</p>


{% endraw %}
