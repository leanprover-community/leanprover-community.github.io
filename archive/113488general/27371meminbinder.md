---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27371meminbinder.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [mem in binder](https://leanprover-community.github.io/archive/113488general/27371meminbinder.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jun 16 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem%20in%20binder/near/128145487):
<p>I wrote the code <code>⨅ U ∈ nhd_zero R, principal {p : R×R | p.2 - p.1 ∈ U}</code> but now I realize I don't quite understand what's going on under the hood. The inf notation is defined by:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">infi</span> <span class="o">[</span><span class="n">complete_lattice</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">ι</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">Inf</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">|</span> <span class="bp">∃</span><span class="n">i</span> <span class="o">:</span> <span class="n">ι</span><span class="o">,</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">s</span> <span class="n">i</span><span class="o">}</span>
<span class="kn">notation</span> <span class="bp">`</span><span class="err">⨅</span><span class="bp">`</span> <span class="n">binders</span> <span class="bp">`</span><span class="o">,</span> <span class="bp">`</span> <span class="n">r</span><span class="o">:(</span><span class="n">scoped</span> <span class="n">f</span><span class="o">,</span> <span class="n">infi</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span> <span class="n">r</span>
</pre></div>


<p>What is <code>ι</code> in my case? <code>{U : set R // U ∈ nhd_zero R}</code>?</p>

#### [ Patrick Massot (Jun 16 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem%20in%20binder/near/128145505):
<p>or is it some kind of Pi type?</p>

#### [ Reid Barton (Jun 16 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem%20in%20binder/near/128145510):
<p>It magically becomes <code>⨅ U, ⨅ (H : U ∈ nhd_zero R), principal {p : R×R | p.2 - p.1 ∈ U}</code></p>

#### [ Patrick Massot (Jun 16 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem%20in%20binder/near/128145564):
<p>ok, this is consistent with stuff I saw</p>

#### [ Reid Barton (Jun 16 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem%20in%20binder/near/128145649):
<p>You can even refer to <code>H</code> after the comma, though this seems like a bad idea to me</p>

#### [ Patrick Massot (Jun 16 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem%20in%20binder/near/128145811):
<p>Thank you</p>

#### [ Patrick Massot (Jun 16 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem%20in%20binder/near/128145812):
<p>I'm writing really strange looking code</p>

#### [ Patrick Massot (Jun 16 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem%20in%20binder/near/128145817):
<p>I hope Johannes will help me clean it up</p>

#### [ Patrick Massot (Jun 16 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem%20in%20binder/near/128146158):
<p>It's getting really late here. I'll give up for today. If someone else wants to play with filters while I sleep, I think the lemma I need next is:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">filter</span><span class="bp">.</span><span class="n">mem_sets_of_mem_infi</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">ι</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">ι</span> <span class="bp">→</span> <span class="n">filter</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span>
<span class="n">A</span> <span class="err">∈</span> <span class="o">(</span><span class="err">⨅</span> <span class="n">i</span><span class="o">,</span><span class="n">f</span> <span class="n">i</span><span class="o">)</span><span class="bp">.</span><span class="n">sets</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">i</span><span class="o">,</span> <span class="n">A</span> <span class="err">∈</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">)</span><span class="bp">.</span><span class="n">sets</span>
</pre></div>


{% endraw %}
