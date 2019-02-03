---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/71280buildingmathlib.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [building mathlib](https://leanprover-community.github.io/archive/116395maths/71280buildingmathlib.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Apr 19 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/building%20mathlib/near/125292006):
<p>I'm trying to build the mathlib master with the Lean master. Should this work? I currently get this as the first error (followed by others):</p>
<div class="codehilite"><pre><span></span><span class="n">mathlib</span><span class="bp">/</span><span class="n">data</span><span class="bp">/</span><span class="n">finset</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">846</span><span class="o">:</span><span class="mi">12</span><span class="o">:</span> <span class="n">error</span><span class="o">:</span> <span class="n">rewrite</span> <span class="n">tactic</span> <span class="n">failed</span><span class="o">,</span> <span class="n">did</span> <span class="n">not</span> <span class="n">find</span> <span class="kn">instance</span> <span class="n">of</span> <span class="n">the</span> <span class="n">pattern</span> <span class="k">in</span> <span class="n">the</span> <span class="n">target</span> <span class="n">expression</span>
  <span class="err">?</span><span class="n">m_2</span> <span class="err">∈</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">to_finset</span> <span class="err">?</span><span class="n">m_4</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">,</span>
<span class="n">δ</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u_4</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="n">α</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_2</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">decidable_eq</span> <span class="o">(</span><span class="n">δ</span> <span class="n">a</span><span class="o">),</span>
<span class="n">t</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">finset</span> <span class="o">(</span><span class="n">δ</span> <span class="n">a</span><span class="o">),</span>
<span class="n">s_val</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">,</span>
<span class="n">s_nodup</span> <span class="o">:</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">nodup</span> <span class="n">s_val</span><span class="o">,</span>
<span class="n">f</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">a</span> <span class="err">∈</span> <span class="o">{</span><span class="n">val</span> <span class="o">:=</span> <span class="n">s_val</span><span class="o">,</span> <span class="n">nodup</span> <span class="o">:=</span> <span class="n">s_nodup</span><span class="o">}</span> <span class="bp">→</span> <span class="n">δ</span> <span class="n">a</span>
<span class="err">⊢</span> <span class="n">f</span> <span class="err">∈</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">to_finset</span> <span class="o">(</span><span class="n">multiset</span><span class="bp">.</span><span class="n">pi</span> <span class="o">({</span><span class="n">val</span> <span class="o">:=</span> <span class="n">s_val</span><span class="o">,</span> <span class="n">nodup</span> <span class="o">:=</span> <span class="n">s_nodup</span><span class="o">}</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="o">(</span><span class="n">t</span> <span class="n">a</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span><span class="o">))</span> <span class="bp">↔</span>
    <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="o">{</span><span class="n">val</span> <span class="o">:=</span> <span class="n">s_val</span><span class="o">,</span> <span class="n">nodup</span> <span class="o">:=</span> <span class="n">s_nodup</span><span class="o">}),</span> <span class="n">f</span> <span class="n">a</span> <span class="n">h</span> <span class="err">∈</span> <span class="n">t</span> <span class="n">a</span>
</pre></div>

#### [ Mario Carneiro (Apr 19 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/building%20mathlib/near/125292113):
<p>mathlib is currently building against nightly 04-06. I've been waiting for the 3.4.0 nightly to be released, which happened yesterday; I'll take a look at updating later.</p>

#### [ Sean Leather (Apr 25 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/building%20mathlib/near/125662029):
<p>Yay! I can build lean and mathlib. <span class="emoji emoji-1f938" title="person doing cartwheel">:person_doing_cartwheel:</span> Thanks, <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>!</p>

#### [ Sean Leather (Apr 26 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/building%20mathlib/near/125714983):
<p>Wow! I just upgraded my Lean and mathlib from February to the latest, and I didn't have to change a thing in my code. <span class="emoji emoji-1f632" title="astonished">:astonished:</span></p>

#### [ Mario Carneiro (Apr 26 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/building%20mathlib/near/125715047):
<p>that must be a record, two months without a backward incompatibility</p>


{% endraw %}
