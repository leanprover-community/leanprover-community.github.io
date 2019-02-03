---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58529prettyprintingunderscores.html
---

## Stream: [general](index.html)
### Topic: [pretty printing underscores](58529prettyprintingunderscores.html)

---


{% raw %}
#### [ Scott Morrison (Nov 27 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148406464):
<p>Is there a good way to pretty print expressions, so metavariables get replaced by <code>_</code> characters?</p>

#### [ Scott Morrison (Nov 27 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148406530):
<p>I see there is <code>pp.use_holes</code> which prints metavariables as <code>{! !}</code>.</p>

#### [ Scott Morrison (Nov 27 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148406776):
<p>or perhaps more simply --- does anyone know how I do substring replacement? (e.g. <code>{! !}</code> to <code>_</code>)</p>

#### [ Rob Lewis (Nov 27 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148406884):
<p>It might be easier to replace the metavars with <code>pexpr.mk_placeholder</code> before printing.</p>

#### [ Scott Morrison (Nov 27 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407075):
<p>I see. Any suggestions on how to do the replacement? I tried just folding, but I need to turn <code>expr</code>s back into <code>pexpr</code>s.</p>

#### [ Scott Morrison (Nov 27 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407086):
<p>of, pexpr.of_expr</p>

#### [ Rob Lewis (Nov 27 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407113):
<p>No promises that this works beyond the two little examples I just tried, but give it a shot.</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">replace_mvars</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:</span> <span class="n">expr</span> <span class="o">:=</span>
<span class="n">e</span><span class="bp">.</span><span class="n">replace</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">e&#39;</span> <span class="bp">_</span><span class="o">,</span> <span class="k">if</span> <span class="n">e&#39;</span><span class="bp">.</span><span class="n">is_meta_var</span> <span class="k">then</span> <span class="n">some</span> <span class="o">(</span><span class="n">unchecked_cast</span> <span class="n">pexpr</span><span class="bp">.</span><span class="n">mk_placeholder</span><span class="o">)</span> <span class="k">else</span> <span class="n">none</span><span class="o">)</span>
</pre></div>

#### [ Scott Morrison (Nov 27 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407167):
<p>Looking good!!</p>

#### [ Scott Morrison (Nov 27 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407267):
<p>I still need to learn how to do string munging in Lean, I'm flailing about trying to decide is a string contains a given character... :-(</p>

#### [ Scott Morrison (Nov 27 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407316):
<p><code>'_' ∈ s.to_list</code>?</p>

#### [ Scott Morrison (Nov 27 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407320):
<p>Seems to work, but presumably there's something more natural.</p>

#### [ Keeley Hoek (Nov 27 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148408767):
<p>Just on the strings scott<br>
Resist the temptation to use <code>string.iterator</code>s<br>
I thought they were the future (they are VM implemented), and changed the <code>expr</code> deserialiser to use them<br>
About a 5% slowdown</p>


{% endraw %}
