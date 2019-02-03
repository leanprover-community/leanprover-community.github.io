---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/74274Basicfinitegroups.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Basic finite groups](https://leanprover-community.github.io/archive/116395maths/74274Basicfinitegroups.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Jul 27 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130387854):
<p>Do we have the symmetry group of order n!?</p>

#### [ Mario Carneiro (Jul 27 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130389188):
<p>There is <code>perm (fin n)</code>, and you should be able to prove it is finite with the right cardinality using <code>list.length_permutations</code></p>

#### [ Kenny Lau (Jul 27 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130389202):
<p><code>equiv.perm (fin n)</code></p>

#### [ Kenny Lau (Jul 27 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130389504):
<p>Do we have C_2 and in general C_n?</p>

#### [ Kenny Lau (Jul 27 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130389505):
<p>i.e. the cyclic group of order 2 and n</p>

#### [ Kenny Lau (Jul 27 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130389653):
<p>hmm, Lean doesn't know that <code>equiv.perm</code> and <code>list.perm</code> are the same thing, so it might be hard to use <code>list.length_permutations</code>...</p>

#### [ Mario Carneiro (Jul 27 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130389875):
<p>hm, I'll put that on the todo list</p>

#### [ Johan Commelin (Jul 27 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130393507):
<p>We have <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Z</mi></mrow><mi mathvariant="normal">/</mi><mi>n</mi><mrow><mi mathvariant="double-struck">Z</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{Z}/n\mathbb{Z}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Z</span></span><span class="mord mathrm">/</span><span class="mord mathit">n</span><span class="mord"><span class="mord mathbb">Z</span></span></span></span></span>, right?</p>

#### [ Kenny Lau (Jul 27 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130393508):
<p>oh right that's in the not-mathlib</p>

#### [ Kenny Lau (Jul 27 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130393522):
<p>I don't think they proved that it is a group</p>

#### [ Johan Commelin (Jul 27 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130393533):
<p>Aaah, I didn't keep track of what exactly ended up in mathlib.</p>

#### [ Kenny Lau (Jul 27 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130393536):
<p>by "not-mathlib" I mean the initial library</p>

#### [ Johan Commelin (Jul 27 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130393537):
<p>I assumed it was a ring by now.</p>

#### [ Kenny Lau (Jul 27 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130393583):
<p>no, there's no algebraic structure of <code>fin n</code> proven</p>

#### [ Johan Commelin (Jul 27 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130393593):
<p>But Chris did a lot of stuff mod <code>n</code>, right?</p>

#### [ Kenny Lau (Jul 27 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130393594):
<p>ah</p>

#### [ Johan Commelin (Jul 27 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130393597):
<p>Anyway, got to run... some talk on K-theory and motives is calling me.</p>

#### [ Kevin Buzzard (Jul 27 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130395310):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> The problem with fin n (the subtype of N) is that addition and subtraction are defined in core Lean in...umm...not really the way that a mathematician would expect. Chris Hughes did a bunch of stuff mod n yes, but not with fin n.</p>

#### [ Kenny Lau (Jul 27 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130395382):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I don't really understand the problem with <code>fin n</code> though</p>

#### [ Kevin Buzzard (Jul 27 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130395464):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">two</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">4</span> <span class="o">:=</span> <span class="mi">2</span>
<span class="kn">definition</span> <span class="n">three</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">4</span> <span class="o">:=</span> <span class="mi">3</span>
<span class="bp">#</span><span class="n">reduce</span> <span class="o">(</span><span class="n">two</span><span class="bp">-</span><span class="n">three</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span> <span class="c1">-- 0</span>
<span class="bp">#</span><span class="n">reduce</span> <span class="o">(</span><span class="n">two</span><span class="bp">+</span><span class="n">three</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span> <span class="c1">-- 1</span>
</pre></div>


<p>Addition rolls over, subtraction stops at 0. It's in core so can never be fixed. But of course one couls just define Zmodn n to be fin n and start again.</p>

#### [ Kenny Lau (Jul 27 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130395470):
<p>oh, the definition in core is wrong</p>

#### [ Kevin Buzzard (Jul 27 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130395471):
<p>right</p>

#### [ Kenny Lau (Jul 27 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130400454):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fintype</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">namespace</span> <span class="n">list</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">length_attach</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">L</span><span class="bp">.</span><span class="n">attach</span><span class="bp">.</span><span class="n">length</span> <span class="bp">=</span> <span class="n">L</span><span class="bp">.</span><span class="n">length</span> <span class="o">:=</span>
<span class="n">length_pmap</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">nth_le_attach</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">i</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">i</span> <span class="bp">&lt;</span> <span class="n">L</span><span class="bp">.</span><span class="n">attach</span><span class="bp">.</span><span class="n">length</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="n">L</span><span class="bp">.</span><span class="n">attach</span><span class="bp">.</span><span class="n">nth_le</span> <span class="n">i</span> <span class="n">H</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">=</span> <span class="n">L</span><span class="bp">.</span><span class="n">nth_le</span> <span class="n">i</span> <span class="o">(</span><span class="n">length_attach</span> <span class="n">L</span> <span class="bp">▸</span> <span class="n">H</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">calc</span>  <span class="o">(</span><span class="n">L</span><span class="bp">.</span><span class="n">attach</span><span class="bp">.</span><span class="n">nth_le</span> <span class="n">i</span> <span class="n">H</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span>
    <span class="bp">=</span> <span class="o">(</span><span class="n">L</span><span class="bp">.</span><span class="n">attach</span><span class="bp">.</span><span class="n">map</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span><span class="bp">.</span><span class="n">nth_le</span> <span class="n">i</span> <span class="o">(</span><span class="k">by</span> <span class="n">simpa</span> <span class="kn">using</span> <span class="n">H</span><span class="o">)</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">nth_le_map&#39;</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">L</span><span class="bp">.</span><span class="n">nth_le</span> <span class="n">i</span> <span class="bp">_</span> <span class="o">:</span> <span class="k">by</span> <span class="n">congr</span><span class="bp">;</span> <span class="n">apply</span> <span class="n">attach_map_val</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">nth_le_range</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">(</span><span class="n">i</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">i</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">length</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">nth_le</span> <span class="o">(</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span> <span class="n">i</span> <span class="n">H</span> <span class="bp">=</span> <span class="n">i</span> <span class="o">:=</span>
<span class="n">option</span><span class="bp">.</span><span class="n">some</span><span class="bp">.</span><span class="n">inj</span> <span class="err">$</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">nth_le_nth</span> <span class="bp">_</span><span class="o">,</span> <span class="n">nth_range</span> <span class="o">(</span><span class="k">by</span> <span class="n">simpa</span> <span class="kn">using</span> <span class="n">H</span><span class="o">)]</span>

<span class="n">attribute</span> <span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="n">length_of_fn</span>
<span class="n">attribute</span> <span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="n">nth_le_of_fn</span>

<span class="c1">-- Congratulations, I proved that two things which have</span>
<span class="c1">-- equally few lemmas are equal.</span>
<span class="kn">theorem</span> <span class="n">of_fn_eq_pmap</span> <span class="o">{</span><span class="n">α</span> <span class="n">n</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span>
  <span class="n">of_fn</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">pmap</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span> <span class="n">hi</span><span class="o">,</span> <span class="n">f</span> <span class="bp">⟨</span><span class="n">i</span><span class="o">,</span> <span class="n">hi</span><span class="bp">⟩</span><span class="o">)</span> <span class="o">(</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">mem_range</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">pmap_eq_map_attach</span><span class="o">]</span><span class="bp">;</span> <span class="k">from</span> <span class="n">ext_le</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span> <span class="n">hi1</span> <span class="n">hi2</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="n">at</span> <span class="n">hi1</span><span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="n">nth_le_of_fn</span> <span class="n">f</span> <span class="bp">⟨</span><span class="n">i</span><span class="o">,</span> <span class="n">hi1</span><span class="bp">⟩</span><span class="o">])</span>

<span class="kn">theorem</span> <span class="n">nodup_of_fn</span> <span class="o">{</span><span class="n">α</span> <span class="n">n</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">injective</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">nodup</span> <span class="o">(</span><span class="n">of_fn</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="n">of_fn_eq_pmap</span><span class="bp">;</span> <span class="k">from</span> <span class="n">nodup_pmap</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span><span class="o">,</span> <span class="n">fin</span><span class="bp">.</span><span class="n">veq_of_eq</span> <span class="err">$</span> <span class="n">hf</span> <span class="n">H</span><span class="o">)</span> <span class="o">(</span><span class="n">nodup_range</span> <span class="n">n</span><span class="o">)</span>

<span class="kn">end</span> <span class="n">list</span>



<span class="kn">variable</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>

<span class="n">def</span> <span class="n">Sym</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">:=</span>
<span class="n">equiv</span><span class="bp">.</span><span class="n">perm</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_coe_to_fun</span> <span class="o">(</span><span class="n">Sym</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">equiv</span><span class="bp">.</span><span class="n">has_coe_to_fun</span>

<span class="bp">@</span><span class="o">[</span><span class="n">extensionality</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">Sym</span><span class="bp">.</span><span class="n">ext</span> <span class="o">(</span><span class="n">σ</span> <span class="n">τ</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">σ</span> <span class="n">i</span> <span class="bp">=</span> <span class="n">τ</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="n">σ</span> <span class="bp">=</span> <span class="n">τ</span> <span class="o">:=</span>
<span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">group</span> <span class="o">(</span><span class="n">Sym</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">equiv</span><span class="bp">.</span><span class="n">perm_group</span>

<span class="kn">section</span> <span class="n">perm</span>

<span class="kn">variable</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span>

<span class="n">def</span> <span class="n">Sym</span><span class="bp">.</span><span class="n">to_list</span> <span class="o">(</span><span class="n">σ</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">list</span><span class="bp">.</span><span class="n">of_fn</span> <span class="n">σ</span>

<span class="kn">theorem</span> <span class="n">Sym</span><span class="bp">.</span><span class="n">to_list_perm</span> <span class="o">(</span><span class="n">σ</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">σ</span><span class="bp">.</span><span class="n">to_list</span> <span class="bp">~</span> <span class="n">list</span><span class="bp">.</span><span class="n">of_fn</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">perm_ext</span>
  <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">nodup_of_fn</span> <span class="err">$</span> <span class="n">σ</span><span class="bp">.</span><span class="n">bijective</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span>
  <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">nodup_of_fn</span> <span class="err">$</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">bijective</span><span class="bp">.</span><span class="mi">1</span><span class="o">))</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">list</span><span class="bp">.</span><span class="n">of_fn_eq_pmap</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">of_fn_eq_pmap</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">mem_pmap</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">mem_pmap</span><span class="o">]</span><span class="bp">;</span> <span class="k">from</span>
<span class="bp">⟨λ</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">f</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">f</span><span class="bp">.</span><span class="mi">2</span><span class="o">],</span> <span class="n">fin</span><span class="bp">.</span><span class="n">eq_of_veq</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span>
<span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">⟨</span><span class="o">(</span><span class="n">σ</span><span class="bp">⁻¹</span> <span class="n">f</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[(</span><span class="n">σ</span><span class="bp">⁻¹</span> <span class="n">f</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span><span class="o">],</span> <span class="k">by</span> <span class="n">convert</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">apply_inverse_apply</span> <span class="n">σ</span> <span class="n">f</span><span class="bp">;</span>
  <span class="k">from</span> <span class="n">congr_arg</span> <span class="bp">_</span> <span class="o">(</span><span class="n">fin</span><span class="bp">.</span><span class="n">eq_of_veq</span> <span class="n">rfl</span><span class="o">)</span><span class="bp">⟩⟩</span>

<span class="n">def</span> <span class="n">list</span><span class="bp">.</span><span class="n">to_sym</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">))</span>
  <span class="o">(</span><span class="n">HL</span> <span class="o">:</span> <span class="n">L</span> <span class="bp">~</span> <span class="n">list</span><span class="bp">.</span><span class="n">of_fn</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span><span class="o">))</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">to_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">nth_le</span> <span class="n">L</span> <span class="n">f</span><span class="bp">.</span><span class="mi">1</span> <span class="err">$</span>
    <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">list</span><span class="bp">.</span><span class="n">perm_length</span> <span class="n">HL</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">length_of_fn</span><span class="o">]</span><span class="bp">;</span> <span class="k">from</span> <span class="n">f</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
  <span class="n">inv_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">list</span><span class="bp">.</span><span class="n">index_of</span> <span class="n">f</span> <span class="n">L</span><span class="o">,</span>
    <span class="k">begin</span>
      <span class="n">convert</span> <span class="n">list</span><span class="bp">.</span><span class="n">index_of_lt_length</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">_</span><span class="o">,</span>
      <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="n">list</span><span class="bp">.</span><span class="n">perm_length</span> <span class="n">HL</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">length_of_fn</span><span class="o">]</span> <span class="o">},</span>
      <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="n">list</span><span class="bp">.</span><span class="n">mem_of_perm</span> <span class="n">HL</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">mem_iff_nth_le</span><span class="o">],</span>
        <span class="n">refine</span> <span class="bp">⟨</span><span class="n">f</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">_⟩</span><span class="o">,</span>
        <span class="o">{</span> <span class="n">rw</span> <span class="n">list</span><span class="bp">.</span><span class="n">length_of_fn</span><span class="o">,</span>
          <span class="n">exact</span> <span class="n">f</span><span class="bp">.</span><span class="mi">2</span> <span class="o">},</span>
        <span class="o">{</span> <span class="n">apply</span> <span class="n">list</span><span class="bp">.</span><span class="n">nth_le_of_fn</span> <span class="o">}</span> <span class="o">}</span>
    <span class="kn">end</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">left_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">fin</span><span class="bp">.</span><span class="n">eq_of_veq</span> <span class="err">$</span> <span class="n">list</span><span class="bp">.</span><span class="n">nth_le_index_of</span>
    <span class="o">((</span><span class="n">list</span><span class="bp">.</span><span class="n">perm_nodup</span> <span class="n">HL</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="n">list</span><span class="bp">.</span><span class="n">nodup_of_fn</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">id</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">right_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">index_of_nth_le</span> <span class="err">$</span> <span class="n">list</span><span class="bp">.</span><span class="n">index_of_lt_length</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span>
    <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">mem_of_perm</span> <span class="n">HL</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="n">list</span><span class="bp">.</span><span class="n">mem_iff_nth_le</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span>
    <span class="bp">⟨</span><span class="n">f</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">list</span><span class="bp">.</span><span class="n">length_of_fn</span><span class="bp">;</span> <span class="k">from</span> <span class="n">f</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
      <span class="n">list</span><span class="bp">.</span><span class="n">nth_le_of_fn</span> <span class="bp">_</span> <span class="bp">_⟩</span> <span class="o">}</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">list</span><span class="bp">.</span><span class="n">to_sym_apply</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">))</span>
  <span class="o">(</span><span class="n">HL</span> <span class="o">:</span> <span class="n">L</span> <span class="bp">~</span> <span class="n">list</span><span class="bp">.</span><span class="n">of_fn</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span><span class="o">))</span> <span class="o">(</span><span class="n">i</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="n">L</span><span class="bp">.</span><span class="n">to_sym</span> <span class="n">HL</span><span class="o">)</span> <span class="n">i</span> <span class="bp">=</span> <span class="n">L</span><span class="bp">.</span><span class="n">nth_le</span> <span class="n">i</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">list</span><span class="bp">.</span><span class="n">perm_length</span> <span class="n">HL</span><span class="o">,</span> <span class="n">i</span><span class="bp">.</span><span class="mi">2</span><span class="o">])</span> <span class="o">:=</span>
<span class="n">rfl</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">Sym</span><span class="bp">.</span><span class="n">to_list_to_sym</span> <span class="o">(</span><span class="n">σ</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">σ</span><span class="bp">.</span><span class="n">to_list</span><span class="bp">.</span><span class="n">to_sym</span> <span class="n">σ</span><span class="bp">.</span><span class="n">to_list_perm</span> <span class="bp">=</span> <span class="n">σ</span> <span class="o">:=</span>
<span class="n">Sym</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="n">fin</span><span class="bp">.</span><span class="n">eq_of_veq</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">Sym</span><span class="bp">.</span><span class="n">to_list</span><span class="o">]</span>

<span class="kn">end</span> <span class="n">perm</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="o">(</span><span class="n">Sym</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">function</span><span class="bp">.</span><span class="n">injective</span><span class="bp">.</span><span class="n">decidable_eq</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">Sym</span><span class="bp">.</span><span class="n">to_list</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">σ</span> <span class="n">τ</span> <span class="n">h</span><span class="o">,</span>
<span class="n">Sym</span><span class="bp">.</span><span class="n">ext</span> <span class="n">n</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span>
<span class="k">have</span> <span class="n">H1</span> <span class="o">:</span> <span class="n">σ</span><span class="bp">.</span><span class="n">to_list</span><span class="bp">.</span><span class="n">nth_le</span> <span class="n">i</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">_</span> <span class="bp">=</span> <span class="bp">_</span><span class="o">,</span>
  <span class="k">from</span> <span class="n">list</span><span class="bp">.</span><span class="n">nth_le_of_fn</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
<span class="k">have</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">τ</span><span class="bp">.</span><span class="n">to_list</span><span class="bp">.</span><span class="n">nth_le</span> <span class="n">i</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">_</span> <span class="bp">=</span> <span class="bp">_</span><span class="o">,</span>
  <span class="k">from</span> <span class="n">list</span><span class="bp">.</span><span class="n">nth_le_of_fn</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">H1</span><span class="o">,</span> <span class="err">←</span> <span class="n">H2</span><span class="o">]</span><span class="bp">;</span> <span class="n">congr</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">h</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">fintype</span> <span class="o">(</span><span class="n">Sym</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">fintype</span><span class="bp">.</span><span class="n">of_list</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">pmap</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">L</span> <span class="n">HL</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">to_sym</span> <span class="n">L</span> <span class="n">HL</span><span class="o">)</span>
  <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">permutations</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">of_fn</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span><span class="o">)))</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">mem_permutations</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span><span class="o">))</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">σ</span><span class="o">,</span>
<span class="n">list</span><span class="bp">.</span><span class="n">mem_pmap</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">σ</span><span class="bp">.</span><span class="n">to_list</span><span class="o">,</span>
  <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">mem_permutations</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="n">σ</span><span class="bp">.</span><span class="n">to_list_perm</span><span class="o">,</span>
  <span class="k">by</span> <span class="n">simp</span><span class="bp">⟩</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">theorem Sym.card : fintype.card (Sym n) = nat.fact n :=</span>
<span class="cm">calc  fintype.card (Sym n)</span>
<span class="cm">    = _ : _</span>
<span class="cm">... = (list.of_fn ((1 : Sym n) : fin n → fin n)).permutations.length : list.to_finset_card_of_nodup sorry</span>
<span class="cm">... = nat.fact (list.of_fn ((1 : Sym n) : fin n → fin n)).length : list.length_permutations _</span>
<span class="cm">... = nat.fact n : by simp</span>
<span class="cm">-/</span>
</pre></div>

#### [ Kenny Lau (Jul 27 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130400457):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I think this all can go to mathlib</p>

#### [ Kenny Lau (Jul 27 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130401051):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">Cayley</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">group</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span>
  <span class="bp">∃</span> <span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sym</span> <span class="o">(</span><span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="n">α</span><span class="o">),</span> <span class="n">function</span><span class="bp">.</span><span class="n">injective</span> <span class="n">f</span> <span class="bp">∧</span> <span class="n">is_group_hom</span> <span class="n">f</span> <span class="o">:=</span>
<span class="n">nonempty</span><span class="bp">.</span><span class="n">rec_on</span> <span class="o">(</span><span class="n">fintype</span><span class="bp">.</span><span class="n">card_eq</span><span class="bp">.</span><span class="mi">1</span> <span class="err">$</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card_fin</span> <span class="err">$</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="n">α</span><span class="o">)</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">φ</span><span class="o">,</span>
<span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="n">i</span><span class="o">,</span> <span class="n">φ</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">x</span> <span class="bp">*</span> <span class="n">φ</span> <span class="n">i</span><span class="o">),</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="n">φ</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">x</span><span class="bp">⁻¹</span> <span class="bp">*</span> <span class="n">φ</span> <span class="n">i</span><span class="o">),</span>
  <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">⟩</span><span class="o">,</span>
<span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">H</span><span class="o">,</span> <span class="k">have</span> <span class="n">H1</span> <span class="o">:</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">congr_fun</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">mk</span><span class="bp">.</span><span class="n">inj</span> <span class="n">H</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">φ</span><span class="bp">.</span><span class="n">symm</span> <span class="mi">1</span><span class="o">),</span> <span class="k">by</span> <span class="n">simpa</span> <span class="kn">using</span> <span class="n">H1</span><span class="o">,</span>
<span class="bp">⟨λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">Sym</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">mul_assoc</span><span class="o">]</span><span class="bp">⟩⟩</span>
</pre></div>

#### [ Kenny Lau (Jul 27 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130401056):
<p>Cayley's theorem :P</p>

#### [ Kenny Lau (Jul 27 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130401160):
<p>TODO: prove that your list of permutations has no duplicates</p>

#### [ Kevin Buzzard (Jul 27 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130401457):
<p>I think <span class="user-mention" data-user-id="110044">@Chris Hughes</span> and <span class="user-mention" data-user-id="120276">@Morenikeji Neri</span> were thinking about this sort of thing last week (they were interested in proving that the size of S_n was n!). Chris also defined the signature of a permutation --  it was interesting to think of a workable definition. Eventually we settled on <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>s</mi><mi>g</mi><mi>n</mi><mo>(</mo><mi>σ</mi><mo>)</mo><mo>=</mo><mo>(</mo><mo>−</mo><mn>1</mn><msup><mo>)</mo><mrow><mi>N</mi><mo>(</mo><mi>σ</mi><mo>)</mo></mrow></msup></mrow><annotation encoding="application/x-tex">sgn(\sigma)=(-1)^{N(\sigma)}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8879999999999999em;"></span><span class="strut bottom" style="height:1.138em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">s</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mord mathit">n</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">σ</span><span class="mclose">)</span><span class="mrel">=</span><span class="mopen">(</span><span class="mord">−</span><span class="mord mathrm">1</span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8879999999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.10903em;">N</span><span class="mopen mtight">(</span><span class="mord mathit mtight" style="margin-right:0.03588em;">σ</span><span class="mclose mtight">)</span></span></span></span></span></span></span></span></span></span></span></span> where <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>N</mi><mo>(</mo><mi>σ</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">N(\sigma)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">N</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">σ</span><span class="mclose">)</span></span></span></span> is the number of pairs <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>i</mi><mo separator="true">,</mo><mi>j</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">(i,j)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit">i</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.05724em;">j</span><span class="mclose">)</span></span></span></span> with <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>i</mi><mo>&lt;</mo><mi>j</mi></mrow><annotation encoding="application/x-tex">i&lt;j</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.65952em;"></span><span class="strut bottom" style="height:0.85396em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">i</span><span class="mrel">&lt;</span><span class="mord mathit" style="margin-right:0.05724em;">j</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>σ</mi><mo>(</mo><mi>i</mi><mo>)</mo><mo>&gt;</mo><mi>σ</mi><mo>(</mo><mi>j</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\sigma(i)&gt;\sigma(j)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">σ</span><span class="mopen">(</span><span class="mord mathit">i</span><span class="mclose">)</span><span class="mrel">&gt;</span><span class="mord mathit" style="margin-right:0.03588em;">σ</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.05724em;">j</span><span class="mclose">)</span></span></span></span>.</p>

#### [ Kenny Lau (Jul 27 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130401462):
<p>did they prove that it is a homomorphism?</p>

#### [ Johan Commelin (Jul 27 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130401479):
<blockquote>
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> The problem with fin n (the subtype of N) is that addition and subtraction are defined in core Lean in...umm...not really the way that a mathematician would expect. Chris Hughes did a bunch of stuff mod n yes, but not with fin n.</p>
</blockquote>
<p>Right, but no-one said that C_n needed to have <code>fin n</code> as carrier type. I don't know what Chris used as carrier type, but I suppose one could use that. Or, like you suggest, just define C_n to be <code>fin n</code>, use that the definition is not reducible, and put new algebraic structures on it that behave properly.</p>

#### [ Kevin Buzzard (Jul 27 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130401652):
<blockquote>
<p>did they prove that it is a homomorphism?</p>
</blockquote>
<p>You need both that, and the fact that the signature of a transposition is -1. Neither are too hard ("in maths") and I would imagine that Chris could manage them in Lean, but I don't know if he did it.</p>

#### [ Chris Hughes (Jul 27 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130402534):
<p>I</p>
<blockquote>
<blockquote>
<p>did they prove that it is a homomorphism?</p>
</blockquote>
<p>You need both that, and the fact that the signature of a transposition is -1. Neither are too hard ("in maths") and I would imagine that Chris could manage them in Lean, but I don't know if he did it.</p>
</blockquote>
<p>I'm working on it now. After that I plan to find the product of disjoint cycles representation computably.</p>

#### [ Kevin Buzzard (Jul 27 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130402699):
<p>I know that this disjoint cycles result is presented to the first years as one of the highlights of the group theory course, but is it actually useful? I think the only reason they do this is that they have to do something group-ish and for some unknown reason they do not define homomorphisms of groups until the 2nd year at Imperial! All this will change with the new syllabus. This disjoint cycle stuff feels to me to be very much a product of a bygone era, when the classification was an active area of research (I suspect the course was written by one of the old school finite group theorists that used to work here).</p>

#### [ Kevin Buzzard (Jul 27 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130402702):
<p>OTOH maybe the philosophy is "do everything"</p>

#### [ Chris Hughes (Jul 27 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130415994):
<p>Maybe I won't do that then. I thought it would be cool to do a <code>has_repr</code>, for <code>perm</code> with disjoint cycle notation. I've proved sign is a hom, but not surjectivity yet.</p>

#### [ Kevin Buzzard (Jul 27 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130419142):
<blockquote>
<p>I thought it would be cool to do a <code>has_repr</code>, for <code>perm</code> with disjoint cycle notation.</p>
</blockquote>
<p>That is a good point! The other possibility for <code>has_repr</code> is just listing <code>(sigma(1),sigma(2),...,sigma(n))</code>but that is (a) unnecessarily big and (b) hard to interpret, so I'm not sure it's of much use. Go with disjoint cycles if you can face it -- making stuff look nice is important!</p>

#### [ Kenny Lau (Jul 28 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130462095):
<p><a href="https://github.com/kckennylau/Lean/blob/master/Sym.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/Sym.lean">https://github.com/kckennylau/Lean/blob/master/Sym.lean</a></p>

#### [ Kenny Lau (Jul 28 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130462099):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Sym</span><span class="bp">.</span><span class="n">equiv</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span> <span class="err">≃</span> <span class="n">fin</span> <span class="n">n</span><span class="bp">.</span><span class="n">fact</span> <span class="o">:=</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">n</span> <span class="n">Sym</span><span class="bp">.</span><span class="n">equiv_0</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">n</span> <span class="n">ih</span><span class="o">,</span>
<span class="k">calc</span>  <span class="n">Sym</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span>
    <span class="err">≃</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="bp">×</span> <span class="n">fin</span> <span class="n">n</span><span class="bp">.</span><span class="n">fact</span><span class="o">)</span> <span class="o">:</span> <span class="n">Sym</span><span class="bp">.</span><span class="n">equiv_succ</span> <span class="n">ih</span>
<span class="bp">...</span> <span class="err">≃</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span><span class="bp">.</span><span class="n">fact</span> <span class="o">:</span> <span class="n">fin_prod</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="o">(</span><span class="n">Sym</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">equiv</span><span class="bp">.</span><span class="n">decidable_eq_of_equiv</span> <span class="n">Sym</span><span class="bp">.</span><span class="n">equiv</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">fintype</span> <span class="o">(</span><span class="n">Sym</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">fintype</span><span class="bp">.</span><span class="n">of_equiv</span> <span class="bp">_</span> <span class="n">Sym</span><span class="bp">.</span><span class="n">equiv</span><span class="bp">.</span><span class="n">symm</span>

<span class="kn">theorem</span> <span class="n">Sym</span><span class="bp">.</span><span class="n">card</span> <span class="o">:</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="o">(</span><span class="n">Sym</span> <span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">fact</span> <span class="n">n</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">fintype</span><span class="bp">.</span><span class="n">of_equiv_card</span> <span class="n">Sym</span><span class="bp">.</span><span class="n">equiv</span><span class="bp">.</span><span class="n">symm</span><span class="o">)</span><span class="bp">.</span><span class="n">trans</span> <span class="err">$</span>
<span class="n">fintype</span><span class="bp">.</span><span class="n">card_fin</span> <span class="bp">_</span>
</pre></div>

#### [ Kenny Lau (Jul 28 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130462918):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> into which files should the content of my file go?</p>

#### [ Kevin Buzzard (Jul 28 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130463370):
<p>Mathematicians do a huge amount of work under various finiteness hypotheses. It's very easy to write down the definition of a vector space in Lean, but nobody ever proves theorems about vector spaces other than the most trivial things. The vector spaces that people care about have extra structure on, for example they're finite-dimensional, or they're separable Hilbert spares or whatever -- some extra finiteness assumptions. As a simple example, my students seem to need "order of the element divides the order of the group" a lot at the minute, and this is a theorem about finite groups. As a more complex example, a commutative ring is <em>Noetherian</em> if all its ideals are finitely-generated. I have a several-hundred-page-long book about etale cohomology which on page 1, when explaining assumptions and notation, says "all rings are assumed Noetherian". [and they're also all commutative]. </p>
<p>This makes me wonder whether "finite group" should be promoted in the heierarchy, to be a class of its own, extending <code>group</code>, and that theorems about finite groups like "order of the element divides order of the group" and "Sym n is a finite group" could go in there.</p>

#### [ Chris Hughes (Jul 28 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130464126):
<p>What's the advantage of <code>[finite_group G]</code> over <code>[fintype G]</code> and <code>[group G]</code>? Bundling classes only really makes sense when there are fields that depend on both  structures, like <code>left_distrib</code> depending on both <code>monoid</code> and <code>add_monoid</code></p>

#### [ Kevin Buzzard (Jul 28 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130464301):
<p>Well I guess that's what I wanted to discuss. Could one not also ask what the advantage of <code>[group G]</code> was over <code>[monoid G]</code> and <code>[has_inv G]</code> and <code>[has_mul_left_inv G]</code> or some such question?</p>

#### [ Kevin Buzzard (Jul 28 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130464392):
<p>We decide that <code>group</code> is important somehow, important enough to have its own typeclass. I am suggesting that finite-dimensional vector spaces, finite groups and Noetherian rings are also important enough to have their own typeclasses because these are the things that people study in practice. A group is a basic foundational concept in mathematics but there are only a few theorems that you can prove about all groups without any hypotheses because a general group is extremely general.</p>

#### [ Kevin Buzzard (Jul 28 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130464489):
<p>I see. You are arguing that <code>finite_group G</code> should be interpreted as "group for which the underlying type is finite" because in some sense these are completely unrelated concepts. But a <em>theorem</em> like "order of the element divides the order of the group" depends on both structures. This is not a field though, it's a theorem. So is that the design principle? If you have 100 theorems about finite groups then that's not enough -- the user is expected to say "a group, for which the underlying set is finite" 100 times?</p>
<p>And of course there are 100 theorems about finite groups -- Sylow's theorems are just the tip of the iceberg Chris :-) The 3rd year group theory course (at least the one I took as an UG) was just 24 lectures of definitions and theorems about finite groups. Maybe that's changed now the landscape has changed, I'm not sure, but all our definitions of solvable, nilpotent etc were almost immediately implied to the finite group case, and only applied to that case.</p>

#### [ Mario Carneiro (Jul 28 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130465381):
<p>maybe <code>group_theory</code>? It's pretty basic, but I'm not sure about the restriction to <code>fin n</code> entailed here. Anything that doesn't mention <code>Sym</code> can go in its respective files</p>

#### [ Kenny Lau (Jul 28 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130470650):
<p>Let's say we want to define the signature/parity of the permutation. In which type should the signature/parity live?</p>

#### [ Kevin Buzzard (Jul 28 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130470896):
<p>That's an interesting question. I am not sure anyone ever adds signatures together. I would argue that mathematically it lives in an abstract group with two elements called +1 and -1. However the CS people might want to choose a concrete implementation of this group rather than building it from scratch I guess.</p>

#### [ Kevin Buzzard (Jul 28 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130470938):
<p>I will remark that the people defining quadratic residues / non-residues in my summer project just defined the values of the Legendre symbol to be integers.</p>

#### [ Chris Hughes (Jul 28 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471146):
<p>I defined it to be an integer mod 2.</p>

#### [ Chris Hughes (Jul 28 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471196):
<p>I imagine you probably want a group structure on the image, so you can prove it's a group_hom, and it's kernel is a subgroup etc.</p>

#### [ Kenny Lau (Jul 28 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471198):
<p>right</p>

#### [ Chris Hughes (Jul 28 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471244):
<p>Unfortunately, the add groups not being groups issue comes into play here.</p>

#### [ Chris Hughes (Jul 28 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471291):
<p>And it would be nice if all tactics like <code>finish</code> also worked on anything isomorphic to <code>Prop</code></p>

#### [ Kenny Lau (Jul 28 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471364):
<p>then which group should i define it on?</p>

#### [ Kevin Buzzard (Jul 28 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471481):
<p>the subtype of Z consisting of things which square to 1?</p>

#### [ Kenny Lau (Jul 28 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471483):
<p>is that the best group?</p>

#### [ Kevin Buzzard (Jul 28 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471484):
<p>What about an abstract group of order 2 equipped with a coercion to Z?</p>

#### [ Kenny Lau (Jul 28 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471485):
<p>or maybe I should just create an inductive type</p>

#### [ Kevin Buzzard (Jul 28 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471486):
<p>right</p>

#### [ Kevin Buzzard (Jul 28 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471496):
<p>Maybe forget about the coercion to Z and see how long it takes people to complain.</p>

#### [ Kenny Lau (Jul 28 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471500):
<p>why do we need coercion to Z?</p>

#### [ Chris Hughes (Jul 28 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471545):
<p>It seems like the best thing is to choose a canonical group of order 2, and always use that for anything that requires a group of order 2. That group should be called either C2, or integers mod 2,</p>

#### [ Kenny Lau (Jul 28 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471548):
<p>but we would also need Cn</p>

#### [ Chris Hughes (Jul 28 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471551):
<p>Exactly.</p>

#### [ Kenny Lau (Jul 28 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471596):
<p>and how would we build that?</p>

#### [ Chris Hughes (Jul 28 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471760):
<p>But there's no point having C2 and some other group of order 2 with a different name</p>

#### [ Kevin Buzzard (Jul 28 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130472238):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">mu2</span>
<span class="bp">|</span> <span class="n">plus_one</span> <span class="o">:</span> <span class="n">mu2</span>
<span class="bp">|</span> <span class="n">minus_one</span> <span class="o">:</span> <span class="n">mu2</span>

<span class="kn">open</span> <span class="n">mu2</span>

<span class="kn">definition</span> <span class="n">neg</span> <span class="o">:</span> <span class="n">mu2</span> <span class="bp">→</span> <span class="n">mu2</span>
<span class="bp">|</span> <span class="n">plus_one</span> <span class="o">:=</span> <span class="n">minus_one</span>
<span class="bp">|</span> <span class="n">minus_one</span> <span class="o">:=</span> <span class="n">plus_one</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_one</span> <span class="n">mu2</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">plus_one</span><span class="bp">⟩</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_neg</span> <span class="n">mu2</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">neg</span><span class="bp">⟩</span>

<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span><span class="bp">-</span><span class="mi">1</span> <span class="o">:</span> <span class="n">mu2</span><span class="o">)</span>
<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="n">mu2</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Jul 28 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130472246):
<p>ok</p>

#### [ Kevin Buzzard (Jul 28 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130472247):
<p>I think the group law for the target of the signature map is traditionally multiplication</p>

#### [ Chris Hughes (Jul 28 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130472373):
<p>But I think it's worth breaking with that tradition for the sake of only having one group of order 2 in lean to deal with.</p>

#### [ Kenny Lau (Jul 28 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130472489):
<div class="codehilite"><pre><span></span><span class="kn">section</span> <span class="n">mu2</span>

<span class="bp">@</span><span class="o">[</span><span class="n">derive</span> <span class="n">decidable_eq</span><span class="o">]</span>
<span class="kn">inductive</span> <span class="n">mu2</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">plus_one</span> <span class="o">:</span> <span class="n">mu2</span>
<span class="bp">|</span> <span class="n">minus_one</span> <span class="o">:</span> <span class="n">mu2</span>

<span class="kn">open</span> <span class="n">mu2</span>

<span class="kn">definition</span> <span class="n">neg</span> <span class="o">:</span> <span class="n">mu2</span> <span class="bp">→</span> <span class="n">mu2</span>
<span class="bp">|</span> <span class="n">plus_one</span> <span class="o">:=</span> <span class="n">minus_one</span>
<span class="bp">|</span> <span class="n">minus_one</span> <span class="o">:=</span> <span class="n">plus_one</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_one</span> <span class="n">mu2</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">plus_one</span><span class="bp">⟩</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_neg</span> <span class="n">mu2</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">neg</span><span class="bp">⟩</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">comm_group</span> <span class="n">mu2</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">mu2</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">x</span> <span class="o">(</span><span class="n">mu2</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">y</span> <span class="mi">1</span> <span class="o">(</span><span class="bp">-</span><span class="mi">1</span><span class="o">))</span> <span class="o">(</span><span class="n">mu2</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">y</span> <span class="o">(</span><span class="bp">-</span><span class="mi">1</span><span class="o">)</span> <span class="mi">1</span><span class="o">),</span>
  <span class="n">mul_assoc</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">x</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">y</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">z</span><span class="bp">;</span> <span class="n">refl</span><span class="o">,</span>
  <span class="n">mul_one</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">x</span><span class="bp">;</span> <span class="n">refl</span><span class="o">,</span>
  <span class="n">one_mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">x</span><span class="bp">;</span> <span class="n">refl</span><span class="o">,</span>
  <span class="n">inv</span> <span class="o">:=</span> <span class="n">id</span><span class="o">,</span>
  <span class="n">mul_left_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">x</span><span class="bp">;</span> <span class="n">refl</span><span class="o">,</span>
  <span class="n">mul_comm</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">x</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">y</span><span class="bp">;</span> <span class="n">refl</span><span class="o">,</span>
  <span class="bp">..</span> <span class="n">mu2</span><span class="bp">.</span><span class="n">has_one</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">mu2</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">elems</span> <span class="o">:=</span> <span class="o">{</span><span class="mi">1</span><span class="o">,</span> <span class="bp">-</span><span class="mi">1</span><span class="o">},</span>
  <span class="n">complete</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">mu2</span><span class="bp">.</span><span class="n">cases_on</span> <span class="n">x</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="err">$</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">rfl</span><span class="o">)</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">rfl</span><span class="o">)</span> <span class="o">}</span>

<span class="kn">theorem</span> <span class="n">mu2</span><span class="bp">.</span><span class="n">card</span> <span class="o">:</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="n">mu2</span> <span class="bp">=</span> <span class="mi">2</span> <span class="o">:=</span>
<span class="n">rfl</span>

<span class="kn">end</span> <span class="n">mu2</span>
</pre></div>

#### [ Kenny Lau (Jul 28 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130472494):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">mu2</span><span class="bp">.</span><span class="n">card</span> <span class="o">:</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="n">mu2</span> <span class="bp">=</span> <span class="mi">2</span> <span class="o">:=</span>
<span class="n">rfl</span>
</pre></div>

#### [ Kenny Lau (Jul 28 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130473038):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">decidable_linear_order</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">le_refl</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">i</span><span class="o">,</span> <span class="n">hi</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">le_refl</span> <span class="n">i</span><span class="o">,</span>
  <span class="n">le_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">i</span><span class="o">,</span> <span class="n">hi</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">j</span><span class="o">,</span> <span class="n">hj</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">k</span><span class="o">,</span> <span class="n">hk</span><span class="bp">⟩</span> <span class="n">hij</span> <span class="n">hjk</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">le_trans</span> <span class="n">hij</span> <span class="n">hjk</span><span class="o">,</span>
  <span class="n">le_antisymm</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">i</span><span class="o">,</span> <span class="n">hi</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">j</span><span class="o">,</span> <span class="n">hj</span><span class="bp">⟩</span> <span class="n">hij</span> <span class="n">hji</span><span class="o">,</span> <span class="n">fin</span><span class="bp">.</span><span class="n">eq_of_veq</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">le_antisymm</span> <span class="n">hij</span> <span class="n">hji</span><span class="o">,</span>
  <span class="n">le_total</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">i</span><span class="o">,</span> <span class="n">hi</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">j</span><span class="o">,</span> <span class="n">hj</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">cases_on</span> <span class="o">(</span><span class="bp">@</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_total</span> <span class="n">i</span> <span class="n">j</span><span class="o">)</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span><span class="o">,</span>
  <span class="n">decidable_le</span> <span class="o">:=</span> <span class="n">fin</span><span class="bp">.</span><span class="n">decidable_le</span><span class="o">,</span>
  <span class="bp">..</span> <span class="n">fin</span><span class="bp">.</span><span class="n">has_le</span><span class="o">,</span> <span class="bp">..</span> <span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Jul 28 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130478700):
<p>We want 2 cyclic groups of order n, one multiplicative, the other additive.</p>

#### [ Johan Commelin (Jul 28 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130478772):
<p>The mu_n example by Kevin will pop up a lot in number theory.</p>

#### [ Johan Commelin (Jul 28 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130478783):
<p>I suppose that Lean Forward is going to do quite a bit of number theory pretty soon.</p>

#### [ Johan Commelin (Jul 28 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130478789):
<p>And then additive cyclic groups also show up everywhere (e.g. integers mod n).</p>

#### [ Johan Commelin (Jul 28 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130478861):
<p>If R is a ring, do we already know that <code>units R</code> is a group? If R is in fact a field, then every finite subgroup of <code>units R</code> is a cyclic group. This is a cute theorem about (finite!) groups. And those cyclic groups are pretty multiplicative.</p>

#### [ Kenny Lau (Jul 28 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482261):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Sym</span><span class="bp">.</span><span class="n">is_valid</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">Sym</span> <span class="n">n</span><span class="o">))</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="bp">∀</span> <span class="n">τ</span> <span class="err">∈</span> <span class="n">L</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">i</span> <span class="n">j</span><span class="o">,</span> <span class="n">i</span> <span class="bp">≠</span> <span class="n">j</span> <span class="bp">∧</span> <span class="n">τ</span> <span class="bp">=</span> <span class="n">Sym</span><span class="bp">.</span><span class="n">swap</span> <span class="n">i</span> <span class="n">j</span>

<span class="n">Sym</span><span class="bp">.</span><span class="n">list_swap_valid</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">σ</span> <span class="o">:</span> <span class="n">Sym</span> <span class="err">?</span><span class="n">M_1</span><span class="o">),</span> <span class="n">Sym</span><span class="bp">.</span><span class="n">is_valid</span> <span class="o">(</span><span class="n">Sym</span><span class="bp">.</span><span class="n">list_swap</span> <span class="n">σ</span><span class="o">)</span>

<span class="n">Sym</span><span class="bp">.</span><span class="n">list_swap_prod</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">σ</span> <span class="o">:</span> <span class="n">Sym</span> <span class="err">?</span><span class="n">M_1</span><span class="o">),</span> <span class="n">list</span><span class="bp">.</span><span class="n">prod</span> <span class="o">(</span><span class="n">Sym</span><span class="bp">.</span><span class="n">list_swap</span> <span class="n">σ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">σ</span>
</pre></div>

#### [ Kenny Lau (Jul 28 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482264):
<p>I proved constructively that every permutation can be written as the product of transpositions</p>

#### [ Kenny Lau (Jul 28 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482266):
<p>I actually didn't know that it is possible with at most n transpositions</p>

#### [ Kenny Lau (Jul 28 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482267):
<p>so I actually learnt (discovered) something new</p>

#### [ Kenny Lau (Jul 28 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482280):
<p>I also learnt how to use <code>well_founded.fix</code> and <code>well_founded.induction</code></p>

#### [ Johan Commelin (Jul 28 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482411):
<p>You can do it with <code>\le (n-1)</code> transpositions, right?</p>

#### [ Kenny Lau (Jul 28 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482414):
<p>yes</p>

#### [ Kenny Lau (Jul 28 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482428):
<p><a href="https://github.com/kckennylau/Lean/blob/master/Sym.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/Sym.lean">https://github.com/kckennylau/Lean/blob/master/Sym.lean</a></p>

#### [ Johan Commelin (Jul 28 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482430):
<p>So now we only need disjoint cycle representation.</p>

#### [ Kenny Lau (Jul 28 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482431):
<p>although I didn't prove the bound</p>

#### [ Kenny Lau (Jul 28 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482435):
<p>no, we don't need DCR</p>

#### [ Kenny Lau (Jul 28 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482436):
<p>it is way overrated</p>

#### [ Johan Commelin (Jul 28 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482441):
<p>It is nice for printing stuff.</p>

#### [ Kenny Lau (Jul 28 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482618):
<p>we should prove the homomorphism first</p>

#### [ Johan Commelin (Jul 28 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482714):
<p>That shouldn't be too hard anymore, right?</p>

#### [ Kenny Lau (Jul 28 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482715):
<p>no, that's a whole nother business</p>

#### [ Kenny Lau (Jul 28 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482716):
<p>they involve completely different skills</p>

#### [ Johan Commelin (Jul 28 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482731):
<p>What, the homomorphism?</p>

#### [ Kenny Lau (Jul 28 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482732):
<p>yes</p>

#### [ Johan Commelin (Jul 28 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482737):
<p>Hmmm, does it help if you change the definition of sgn?</p>

#### [ Johan Commelin (Jul 28 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482777):
<p>Maybe not</p>

#### [ Kenny Lau (Jul 28 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482782):
<p>you need to prove that if a bunch of transpositions multiply to 1, then you have an even number of transpositions</p>

#### [ Kenny Lau (Jul 28 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482784):
<p>that involves somehow traversing the whole list</p>

#### [ Johan Commelin (Jul 28 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482797):
<p>Fair enough</p>

#### [ Kenny Lau (Jul 28 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482858):
<p>which I'm not exactly comfortable with doing in Lean</p>

#### [ Kevin Buzzard (Jul 28 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482998):
<blockquote>
<p>you need to prove that if a bunch of transpositions multiply to 1, then you have an even number of transpositions</p>
</blockquote>
<p>AFAIK the best way to do this is to compute with signatures via the definition Chris used -- signature of sigma is (-1) ^ (the number of pairs (i,j) with i &lt; j and sigma(i) &gt; sigma(j) )</p>

#### [ Kenny Lau (Jul 28 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130483008):
<p>hmm, maybe</p>

#### [ Kevin Buzzard (Jul 28 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130484672):
<p>It's not so hard to prove that this is multiplicative. You can say that an <em>un</em>ordered pair is "switched" if their order is switched -- this is well-defined. if sigma switches a pair and tau switches them back then the composite scores 0 and each of sigma and tau scores 1.</p>

#### [ Chris Hughes (Jul 28 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130484741):
<p>I have proved it's multiplicative, and that transpositions are odd. My proof that transpositions are conjugate was brilliant, I did <code>split_ifs</code> and then solved 84 goals at once with <code>cc</code></p>

#### [ Patrick Massot (Jul 28 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130484843):
<p>I have a challenge for all the permutation experts. From a permutation of <code>fin n</code> (or any version) define a map from a product of  n topological space to the permuted product and prove it's continuous. When n=2, this is <code>continuous_id</code> and <code>continuous_swap</code>. Part of the challenge is that <code>A × B × C</code> is not the type of triple <code>(x.1, x.2, x.3)</code>, it's secretely  <code>A × (B × C)</code> with elements <code>(x.1, (x.2.1, x.2.2))</code></p>

#### [ Patrick Massot (Jul 28 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130484853):
<p>Note that I don't need this, I only want to make sure you don't get bored</p>

#### [ Kenny Lau (Jul 28 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130484904):
<p>can you give us the inputs? i.e. how is the n topological space represented?</p>

#### [ Johan Commelin (Jul 28 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130485013):
<blockquote>
<p>I have proved it's multiplicative, and that transpositions are odd. My proof that transpositions are conjugate was brilliant, I did <code>split_ifs</code> and then solved <strong>84</strong> goals at once with <code>cc</code></p>
</blockquote>
<p>Hmm, that crazy number 84 really has some special place in mathematics... (<a href="https://en.wikipedia.org/wiki/Hurwitz%27s_automorphisms_theorem" target="_blank" title="https://en.wikipedia.org/wiki/Hurwitz%27s_automorphisms_theorem">https://en.wikipedia.org/wiki/Hurwitz%27s_automorphisms_theorem</a>)</p>

#### [ Kevin Buzzard (Jul 28 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130487017):
<p>That's great! Somehow I'm surprised it's quite so many. You have the transposition (a b) and then you're trying to figure out whether the pair (i j) got re-aranged. So you have cases depending on whether i&lt;a,i=a,a&lt;i&lt;b,i=b,i&gt;b and the same with j. The clever thing is to get it so that the goals are solvable afterwards I guess, rather than just counting.</p>

#### [ Chris Hughes (Jul 28 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130487184):
<p>The proof had nothing to do with sign. This was the proof</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">transpose_conj</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span>
  <span class="o">(</span><span class="n">hab</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">hxy</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span>
  <span class="bp">∃</span> <span class="n">f</span> <span class="o">:</span> <span class="n">perm</span> <span class="n">α</span><span class="o">,</span> <span class="n">f</span> <span class="bp">*</span> <span class="n">transpose</span> <span class="n">x</span> <span class="n">y</span> <span class="bp">*</span> <span class="n">f</span><span class="bp">⁻¹</span> <span class="bp">=</span> <span class="n">transpose</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="k">if</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">b</span> <span class="k">then</span> <span class="n">transpose</span> <span class="n">y</span> <span class="n">a</span>
<span class="k">else</span> <span class="k">if</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">a</span> <span class="k">then</span> <span class="n">transpose</span> <span class="n">x</span> <span class="n">b</span>
<span class="k">else</span> <span class="n">transpose</span> <span class="n">x</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">transpose</span> <span class="n">y</span> <span class="n">b</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span>
<span class="k">begin</span>
  <span class="n">unfold_coes</span><span class="o">,</span>
  <span class="n">dsimp</span> <span class="o">[</span><span class="n">transpose</span><span class="o">,</span> <span class="n">inv_def</span><span class="o">,</span> <span class="n">mul_def</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">trans</span><span class="o">,</span> <span class="n">function</span><span class="bp">.</span><span class="n">comp</span><span class="o">],</span>
  <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">ite_apply</span><span class="o">,</span> <span class="n">ite_inv_apply</span><span class="o">],</span>
  <span class="n">split_ifs</span><span class="bp">;</span> <span class="n">cc</span>
<span class="kn">end</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Jul 28 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130487194):
<p>TIL <code>unfold_coes</code></p>

#### [ Patrick Massot (Jul 28 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130487907):
<blockquote>
<p>can you give us the inputs? i.e. how is the n topological space represented?</p>
</blockquote>
<p>The example that I actually needed is at <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/652422a5e5dd00f07ef3dc768bc774784904cb00/src/for_mathlib/topological_structures.lean#L7-L19" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/652422a5e5dd00f07ef3dc768bc774784904cb00/src/for_mathlib/topological_structures.lean#L7-L19">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/652422a5e5dd00f07ef3dc768bc774784904cb00/src/for_mathlib/topological_structures.lean#L7-L19</a></p>

#### [ Kenny Lau (Jul 29 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130512068):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> unfortunately this theorem is not true: <code>sgn.inversion (σ * τ) i j = sgn.inversion τ i j * sgn.inversion σ (τ i) (τ j)</code></p>

#### [ Kenny Lau (Jul 29 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130512069):
<p>and it makes my life defining sign using inversion hard</p>

#### [ Kenny Lau (Jul 29 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130512075):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">sgn</span><span class="bp">.</span><span class="n">inversion</span> <span class="o">(</span><span class="n">σ</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">i</span> <span class="n">j</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">mu2</span> <span class="o">:=</span>
<span class="k">if</span> <span class="n">i</span> <span class="bp">&lt;</span> <span class="n">j</span> <span class="bp">∧</span> <span class="n">σ</span> <span class="n">i</span> <span class="bp">&gt;</span> <span class="n">σ</span> <span class="n">j</span> <span class="k">then</span> <span class="bp">-</span><span class="mi">1</span> <span class="k">else</span> <span class="mi">1</span>
</pre></div>

#### [ Kevin Buzzard (Jul 29 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518707):
<p>How about you define it on unordered pairs? Then it's ok</p>

#### [ Kenny Lau (Jul 29 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518711):
<p>how do you define unordered pairs?</p>

#### [ Chris Hughes (Jul 29 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518804):
<p>quotient</p>

#### [ Kenny Lau (Jul 29 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518807):
<p>did you use quotient?</p>

#### [ Chris Hughes (Jul 29 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518819):
<p>No. I used pairs such that x.2 &gt; x.1</p>

#### [ Kenny Lau (Jul 29 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518826):
<p>and you still managed to prove that it is multiplicative? :o</p>

#### [ Chris Hughes (Jul 29 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518834):
<p>A lot of <code>ite</code> faffing</p>

#### [ Kenny Lau (Jul 29 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518841):
<p>it's mainly the finset prod that I'm uncomfortable with</p>

#### [ Kevin Buzzard (Jul 29 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518916):
<p>Also allow the possibility that i&gt;j and sigma i &lt; sigma j</p>

#### [ Chris Hughes (Jul 29 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518919):
<p>I used <code>sum_bij</code> where the <code>bij</code> was one of the perms I was multiplying, subject to some <code>ite</code> faffing to get the order right.</p>

#### [ Kenny Lau (Jul 29 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518927):
<p>ok</p>

#### [ Chris Hughes (Jul 29 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518928):
<blockquote>
<p>Also allow the possibility that i&gt;j and sigma i &lt; sigma j</p>
</blockquote>
<p>Won't you always get even if you do that?</p>

#### [ Kenny Lau (Jul 29 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518931):
<p>just prove that it is divisible by 2 and then divide by 2 :P</p>

#### [ Kevin Buzzard (Jul 29 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518983):
<p>Or just count over unordered pairs :-)</p>

#### [ Chris Hughes (Jul 29 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130534903):
<p>Done product of transpositions as well. Not sure there was any point making the very last definition computable or not, but it might have some usage. <a href="https://github.com/dorhinj/leanstuff/blob/master/signatures.lean" target="_blank" title="https://github.com/dorhinj/leanstuff/blob/master/signatures.lean">https://github.com/dorhinj/leanstuff/blob/master/signatures.lean</a></p>

#### [ Kenny Lau (Jul 29 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535153):
<p><a href="https://github.com/kckennylau/Lean/blob/master/Sym.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/Sym.lean">https://github.com/kckennylau/Lean/blob/master/Sym.lean</a></p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">sgn</span> <span class="o">(</span><span class="n">σ</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">mu2</span> <span class="o">:=</span>
<span class="o">(</span><span class="bp">-</span><span class="mi">1</span><span class="o">)</span> <span class="err">^</span> <span class="n">σ</span><span class="bp">.</span><span class="n">list_step</span><span class="bp">.</span><span class="n">length</span>

<span class="kn">instance</span> <span class="n">sgn</span><span class="bp">.</span><span class="n">is_group_hom</span> <span class="o">:</span> <span class="n">is_group_hom</span> <span class="o">(</span><span class="bp">@</span><span class="n">sgn</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">constructor</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">σ</span> <span class="n">τ</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">sgn</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">pow_add</span><span class="o">,</span> <span class="err">←</span> <span class="n">list</span><span class="bp">.</span><span class="n">length_append</span><span class="o">],</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">mu2</span><span class="bp">.</span><span class="n">neg_one_pow</span><span class="o">,</span> <span class="n">eq_comm</span><span class="o">,</span> <span class="n">mu2</span><span class="bp">.</span><span class="n">neg_one_pow</span><span class="o">],</span>
  <span class="n">refine</span> <span class="n">congr_arg</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">length_mod_two_eq</span><span class="o">,</span>
  <span class="n">simp</span>
<span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">sgn_step</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">step</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">sgn</span> <span class="n">s</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">=</span> <span class="bp">-</span><span class="mi">1</span> <span class="o">:=</span>
<span class="n">suffices</span> <span class="n">s</span><span class="bp">.</span><span class="kn">eval</span><span class="bp">.</span><span class="n">list_step</span><span class="bp">.</span><span class="n">length</span> <span class="err">%</span> <span class="mi">2</span> <span class="bp">=</span> <span class="o">[</span><span class="n">s</span><span class="o">]</span><span class="bp">.</span><span class="n">length</span> <span class="err">%</span> <span class="mi">2</span><span class="o">,</span>
  <span class="k">by</span> <span class="n">unfold</span> <span class="n">sgn</span><span class="bp">;</span> <span class="n">rw</span> <span class="o">[</span><span class="n">mu2</span><span class="bp">.</span><span class="n">neg_one_pow</span><span class="o">,</span> <span class="n">this</span><span class="o">]</span><span class="bp">;</span> <span class="n">refl</span><span class="o">,</span>
<span class="n">length_mod_two_eq</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simp</span>
</pre></div>

#### [ Kenny Lau (Jul 29 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535156):
<p>10 minutes behind you :-)</p>

#### [ Kevin Buzzard (Jul 29 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535197):
<p>So now you can both define determinant of an n x n matrix!</p>

#### [ Kenny Lau (Jul 29 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535205):
<p>oh no, we could already define determinant just fine, it's the multiplicative part that needs this result</p>

#### [ Chris Hughes (Jul 29 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535210):
<p>Is your sign defined using the list of transpositions?</p>

#### [ Kenny Lau (Jul 29 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535211):
<p>yes</p>

#### [ Kenny Lau (Jul 29 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535212):
<p>oh, and trust me, do not look at Lines 720 - 831</p>

#### [ Kenny Lau (Jul 29 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535252):
<p><a href="https://github.com/kckennylau/Lean/blob/master/Sym.lean#L720" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/Sym.lean#L720">https://github.com/kckennylau/Lean/blob/master/Sym.lean#L720</a></p>

#### [ Kenny Lau (Jul 29 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535259):
<blockquote>
<p>Is your sign defined using the list of transpositions?</p>
</blockquote>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">sgn</span> <span class="o">(</span><span class="n">σ</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">mu2</span> <span class="o">:=</span>
<span class="o">(</span><span class="bp">-</span><span class="mi">1</span><span class="o">)</span> <span class="err">^</span> <span class="n">σ</span><span class="bp">.</span><span class="n">list_step</span><span class="bp">.</span><span class="n">length</span>
</pre></div>

#### [ Kenny Lau (Jul 29 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535261):
<p>and <code>list_step</code> is a computable (!) function</p>

#### [ Kenny Lau (Jul 29 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535266):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">list_step</span> <span class="o">(</span><span class="n">σ</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">step</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">refine</span> <span class="n">well_founded</span><span class="bp">.</span><span class="n">fix</span> <span class="n">list_step</span><span class="bp">.</span><span class="n">aux</span><span class="bp">.</span><span class="n">wf</span> <span class="bp">_</span> <span class="n">σ</span><span class="bp">;</span> <span class="k">from</span>
<span class="bp">λ</span> <span class="n">σ</span> <span class="n">ih</span><span class="o">,</span> <span class="k">if</span> <span class="n">H</span> <span class="o">:</span> <span class="n">σ</span><span class="bp">.</span><span class="n">support</span> <span class="bp">=</span> <span class="err">∅</span> <span class="k">then</span> <span class="o">[]</span>
  <span class="k">else</span> <span class="k">let</span> <span class="bp">⟨</span><span class="n">i</span><span class="o">,</span> <span class="n">hi</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">σ</span><span class="bp">.</span><span class="n">support_choice</span> <span class="n">H</span> <span class="k">in</span>
    <span class="n">step</span><span class="bp">.</span><span class="n">mk&#39;</span> <span class="o">(</span><span class="n">σ</span> <span class="n">i</span><span class="o">)</span> <span class="n">i</span> <span class="o">(</span><span class="n">support_def</span><span class="bp">.</span><span class="mi">1</span> <span class="n">hi</span><span class="o">)</span>
    <span class="bp">::</span> <span class="n">ih</span> <span class="o">(</span><span class="n">swap</span> <span class="o">(</span><span class="n">σ</span> <span class="n">i</span><span class="o">)</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">σ</span><span class="o">)</span> <span class="o">(</span><span class="n">support_swap_mul</span> <span class="n">hi</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Jul 29 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535267):
<p>by induction (recursion) on the support</p>

#### [ Chris Hughes (Jul 29 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535268):
<p>What's it do?</p>

#### [ Kenny Lau (Jul 29 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535272):
<p>it expresses a permutation as a product of transpositions</p>

#### [ Kenny Lau (Jul 29 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535324):
<p>I just realized kernel of group hom is not in mathlib</p>

#### [ Kenny Lau (Jul 29 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535372):
<p>(btw if anyone is reading my code, all my "choice" functions are computable :P)</p>

#### [ Kevin Buzzard (Jul 29 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535806):
<p>I think kernel of a group hom is somewhere in mathlib...<code>is_group_hom.ker</code>?</p>

#### [ Kenny Lau (Jul 29 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535849):
<p>ah right</p>

#### [ Kenny Lau (Jul 29 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535903):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Alt</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">:=</span>
<span class="n">is_group_hom</span><span class="bp">.</span><span class="n">ker</span> <span class="o">(</span><span class="bp">@</span><span class="n">Sym</span><span class="bp">.</span><span class="n">sgn</span> <span class="n">n</span><span class="o">)</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">group</span> <span class="o">(</span><span class="n">Alt</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">unfold</span> <span class="n">Alt</span><span class="bp">;</span> <span class="n">apply_instance</span>
</pre></div>

#### [ Kevin Buzzard (Jul 29 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535921):
<p>You can now prove A_5 is simple by counting conjugacy classes.</p>

#### [ Kenny Lau (Jul 29 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535960):
<p>hmm, not the proof of simple that i know</p>

#### [ Kenny Lau (Jul 29 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535961):
<p>is there an easier proof?</p>

#### [ Kevin Buzzard (Jul 29 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535963):
<blockquote>
<p>oh no, we could already define determinant just fine, it's the multiplicative part that needs this result</p>
</blockquote>
<p>Yes, in fact Keji did it already, by expanding along the top row. He could prove nothing about it from this definition :-)</p>

#### [ Kenny Lau (Jul 29 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535974):
<p>how about Chris proving that any simple group must have order at least 60 lol</p>

#### [ Kevin Buzzard (Jul 29 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130536023):
<blockquote>
<p>is there an easier proof?</p>
</blockquote>
<p>You could use Sylow to prove that group of order strictly dividing 60 was solvable, and then there's some crappy trick with 3-cycles (which I used to set on the 2nd year group theory course) which shows that A_5 has no non-trivial cyclic quotients. The counting proof is pretty trivial! Any normal subgroup is a union of conjugacy classes but any non-trivial sum of conj class sizes doesn't even equal a divisor of 60.</p>

#### [ Kenny Lau (Jul 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130537317):
<p><a href="/user_uploads/3121/tJtctbAOJKrPMftkcpbbkPt3/2018-07-30.png" target="_blank" title="2018-07-30.png">2018-07-30.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/tJtctbAOJKrPMftkcpbbkPt3/2018-07-30.png" target="_blank" title="2018-07-30.png"><img src="/user_uploads/3121/tJtctbAOJKrPMftkcpbbkPt3/2018-07-30.png"></a></div>

#### [ Kenny Lau (Jul 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130537318):
<p>glorious</p>

#### [ Kenny Lau (Jul 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130537319):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">eq_sgn</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">mu2</span><span class="o">)</span> <span class="o">[</span><span class="n">is_group_hom</span> <span class="n">f</span><span class="o">]</span>
  <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">step</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">f</span> <span class="n">s</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">=</span> <span class="bp">-</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">σ</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">f</span> <span class="n">σ</span> <span class="bp">=</span> <span class="n">sgn</span> <span class="n">σ</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">H2</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">t</span> <span class="o">:</span> <span class="n">step</span> <span class="n">n</span><span class="o">,</span> <span class="n">f</span> <span class="n">t</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">=</span> <span class="bp">-</span><span class="mi">1</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">t</span><span class="o">,</span>
    <span class="n">by_cases</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">by_cases</span> <span class="n">H3</span> <span class="o">:</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
      <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">step</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H2</span> <span class="n">H3</span><span class="o">,</span> <span class="n">H1</span><span class="o">]</span> <span class="o">},</span>
      <span class="k">have</span> <span class="n">H4</span> <span class="o">:</span> <span class="n">t</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">=</span> <span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">s</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">*</span> <span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
      <span class="o">{</span> <span class="n">dsimp</span> <span class="o">[</span><span class="n">step</span><span class="bp">.</span><span class="kn">eval</span><span class="o">,</span> <span class="n">swap</span><span class="o">],</span> <span class="n">ext</span> <span class="n">k</span><span class="o">,</span> <span class="n">dsimp</span><span class="o">,</span>
        <span class="k">have</span> <span class="o">:=</span> <span class="n">ne_of_lt</span> <span class="n">s</span><span class="bp">.</span><span class="mi">3</span><span class="o">,</span> <span class="k">have</span> <span class="o">:=</span> <span class="n">ne_of_lt</span> <span class="n">t</span><span class="bp">.</span><span class="mi">3</span><span class="o">,</span>
        <span class="n">split_ifs</span><span class="bp">;</span> <span class="n">cc</span> <span class="o">},</span>
      <span class="n">simp</span> <span class="o">[</span><span class="n">H4</span><span class="o">,</span> <span class="n">is_group_hom</span><span class="bp">.</span><span class="n">mul</span> <span class="n">f</span><span class="o">,</span> <span class="n">H1</span><span class="o">]</span> <span class="o">},</span>
    <span class="n">by_cases</span> <span class="n">H3</span> <span class="o">:</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
    <span class="o">{</span> <span class="k">have</span> <span class="n">H4</span> <span class="o">:</span> <span class="n">t</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">=</span> <span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">*</span> <span class="n">s</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">*</span> <span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
      <span class="o">{</span> <span class="n">dsimp</span> <span class="o">[</span><span class="n">step</span><span class="bp">.</span><span class="kn">eval</span><span class="o">,</span> <span class="n">swap</span><span class="o">],</span> <span class="n">ext</span> <span class="n">k</span><span class="o">,</span> <span class="n">dsimp</span><span class="o">,</span>
        <span class="k">have</span> <span class="o">:=</span> <span class="n">ne_of_lt</span> <span class="n">s</span><span class="bp">.</span><span class="mi">3</span><span class="o">,</span> <span class="k">have</span> <span class="o">:=</span> <span class="n">ne_of_lt</span> <span class="n">t</span><span class="bp">.</span><span class="mi">3</span><span class="o">,</span>
        <span class="n">split_ifs</span><span class="bp">;</span> <span class="n">cc</span> <span class="o">},</span>
      <span class="n">simp</span> <span class="o">[</span><span class="n">H4</span><span class="o">,</span> <span class="n">is_group_hom</span><span class="bp">.</span><span class="n">mul</span> <span class="n">f</span><span class="o">,</span> <span class="n">H1</span><span class="o">]</span> <span class="o">},</span>
    <span class="n">by_cases</span> <span class="n">H4</span> <span class="o">:</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
    <span class="o">{</span> <span class="k">have</span> <span class="n">H5</span> <span class="o">:</span> <span class="n">t</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">=</span> <span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">s</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">*</span> <span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
      <span class="o">{</span> <span class="n">dsimp</span> <span class="o">[</span><span class="n">step</span><span class="bp">.</span><span class="kn">eval</span><span class="o">,</span> <span class="n">swap</span><span class="o">],</span> <span class="n">ext</span> <span class="n">k</span><span class="o">,</span> <span class="n">dsimp</span><span class="o">,</span>
        <span class="k">have</span> <span class="o">:=</span> <span class="n">ne_of_lt</span> <span class="n">s</span><span class="bp">.</span><span class="mi">3</span><span class="o">,</span> <span class="k">have</span> <span class="o">:=</span> <span class="n">ne_of_lt</span> <span class="n">t</span><span class="bp">.</span><span class="mi">3</span><span class="o">,</span>
        <span class="n">split_ifs</span><span class="bp">;</span> <span class="n">cc</span> <span class="o">},</span>
      <span class="n">simp</span> <span class="o">[</span><span class="n">H5</span><span class="o">,</span> <span class="n">is_group_hom</span><span class="bp">.</span><span class="n">mul</span> <span class="n">f</span><span class="o">,</span> <span class="n">H1</span><span class="o">]</span> <span class="o">},</span>
    <span class="n">by_cases</span> <span class="n">H5</span> <span class="o">:</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
    <span class="o">{</span> <span class="k">have</span> <span class="n">H6</span> <span class="o">:</span> <span class="n">t</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">=</span> <span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">*</span> <span class="n">s</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">*</span> <span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
      <span class="o">{</span> <span class="n">dsimp</span> <span class="o">[</span><span class="n">step</span><span class="bp">.</span><span class="kn">eval</span><span class="o">,</span> <span class="n">swap</span><span class="o">],</span> <span class="n">ext</span> <span class="n">k</span><span class="o">,</span> <span class="n">dsimp</span><span class="o">,</span>
        <span class="k">have</span> <span class="o">:=</span> <span class="n">ne_of_lt</span> <span class="n">s</span><span class="bp">.</span><span class="mi">3</span><span class="o">,</span> <span class="k">have</span> <span class="o">:=</span> <span class="n">ne_of_lt</span> <span class="n">t</span><span class="bp">.</span><span class="mi">3</span><span class="o">,</span>
        <span class="n">split_ifs</span><span class="bp">;</span> <span class="n">cc</span> <span class="o">},</span>
      <span class="n">simp</span> <span class="o">[</span><span class="n">H6</span><span class="o">,</span> <span class="n">is_group_hom</span><span class="bp">.</span><span class="n">mul</span> <span class="n">f</span><span class="o">,</span> <span class="n">H1</span><span class="o">]</span> <span class="o">},</span>
    <span class="k">have</span> <span class="n">H6</span> <span class="o">:</span> <span class="n">t</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">=</span> <span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">*</span> <span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">s</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">*</span> <span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">dsimp</span> <span class="o">[</span><span class="n">step</span><span class="bp">.</span><span class="kn">eval</span><span class="o">,</span> <span class="n">swap</span><span class="o">],</span> <span class="n">ext</span> <span class="n">k</span><span class="o">,</span> <span class="n">dsimp</span><span class="o">,</span>
      <span class="k">have</span> <span class="o">:=</span> <span class="n">ne_of_lt</span> <span class="n">s</span><span class="bp">.</span><span class="mi">3</span><span class="o">,</span> <span class="k">have</span> <span class="o">:=</span> <span class="n">ne_of_lt</span> <span class="n">t</span><span class="bp">.</span><span class="mi">3</span><span class="o">,</span>
      <span class="n">split_ifs</span><span class="bp">;</span> <span class="n">cc</span> <span class="o">},</span>
    <span class="n">rw</span> <span class="n">H6</span><span class="o">,</span>
    <span class="n">repeat</span> <span class="o">{</span> <span class="n">rw</span> <span class="n">is_group_hom</span><span class="bp">.</span><span class="n">mul</span> <span class="n">f</span> <span class="o">},</span>
    <span class="n">rw</span> <span class="o">[</span><span class="n">H1</span><span class="o">,</span> <span class="n">mul_assoc</span> <span class="o">(</span><span class="n">f</span> <span class="o">(</span><span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span><span class="o">)),</span> <span class="n">mul_assoc</span> <span class="o">(</span><span class="n">f</span> <span class="o">(</span><span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span><span class="o">))],</span>
    <span class="n">rw</span> <span class="o">[</span><span class="n">mu2</span><span class="bp">.</span><span class="n">mul_neg_one</span><span class="o">,</span> <span class="n">mu2</span><span class="bp">.</span><span class="n">neg_mul_self</span><span class="o">],</span> <span class="n">simp</span> <span class="o">},</span>
  <span class="k">have</span> <span class="n">H3</span> <span class="o">:=</span> <span class="n">list_step_prod</span> <span class="n">σ</span><span class="o">,</span>
  <span class="n">revert</span> <span class="n">H3</span><span class="o">,</span> <span class="n">generalize</span> <span class="o">:</span> <span class="n">list_step</span> <span class="n">σ</span> <span class="bp">=</span> <span class="n">L</span><span class="o">,</span> <span class="n">intro</span> <span class="n">H3</span><span class="o">,</span> <span class="n">subst</span> <span class="n">H3</span><span class="o">,</span>
  <span class="n">induction</span> <span class="n">L</span> <span class="k">with</span> <span class="n">hd</span> <span class="n">tl</span> <span class="n">ih</span><span class="o">,</span> <span class="o">{</span> <span class="n">simp</span> <span class="o">[</span><span class="n">is_group_hom</span><span class="bp">.</span><span class="n">one</span> <span class="n">f</span><span class="o">]</span> <span class="o">},</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">is_group_hom</span><span class="bp">.</span><span class="n">mul</span> <span class="n">f</span><span class="o">,</span> <span class="n">ih</span><span class="o">,</span> <span class="n">H2</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Jul 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130537320):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> <span class="user-mention" data-user-id="110044">@Chris Hughes</span></p>

#### [ Kevin Buzzard (Jul 29 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130537326):
<p>Ouch</p>

#### [ Kenny Lau (Jul 29 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539514):
<p>I think I just discovered a uniform definition of a permutation that can conjugate (ab) to become (cd)</p>

#### [ Kenny Lau (Jul 29 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539519):
<p>uniform as in doesn't rely on casing</p>

#### [ Chris Hughes (Jul 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539530):
<p>How would you manage that?</p>

#### [ Kenny Lau (Jul 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539531):
<p>exercise to the reader :P</p>

#### [ Kenny Lau (Jul 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539533):
<p>to be fair, I did use <code>swap</code>, which relies on casing</p>

#### [ Kenny Lau (Jul 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539536):
<p><code>swap a b</code> swaps <code>a</code> and <code>b</code> regardless of whether they are distinct</p>

#### [ Chris Hughes (Jul 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539573):
<p>That's easy then.</p>

#### [ Chris Hughes (Jul 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539578):
<p>Probably</p>

#### [ Kenny Lau (Jul 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539579):
<p>what's your answer?</p>

#### [ Kenny Lau (Jul 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539585):
<p>oh btw a and b are distinct; and c and d are distinct</p>

#### [ Chris Hughes (Jul 29 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539659):
<p>I give up</p>

#### [ Chris Hughes (Jul 29 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539660):
<p>I can shorten a proof by a few lines if I work it out.</p>

#### [ Kenny Lau (Jul 29 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539661):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">eq_sgn_aux4</span> <span class="o">(</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">step</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span> <span class="o">:=</span>
<span class="n">swap</span> <span class="o">(</span><span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span>

<span class="kn">theorem</span> <span class="n">eq_sgn_aux3</span> <span class="o">(</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">step</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">eq_sgn_aux4</span> <span class="n">s</span> <span class="n">t</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">dsimp</span> <span class="o">[</span><span class="n">eq_sgn_aux4</span><span class="o">,</span> <span class="n">swap</span><span class="o">],</span>
  <span class="k">have</span> <span class="o">:=</span> <span class="n">ne_of_lt</span> <span class="n">s</span><span class="bp">.</span><span class="mi">3</span><span class="o">,</span>
  <span class="k">have</span> <span class="o">:=</span> <span class="n">ne_of_lt</span> <span class="n">t</span><span class="bp">.</span><span class="mi">3</span><span class="o">,</span>
  <span class="n">simp</span><span class="o">,</span> <span class="n">split_ifs</span><span class="bp">;</span> <span class="n">cc</span>
<span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">eq_sgn_aux2</span> <span class="o">(</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">step</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">eq_sgn_aux4</span> <span class="n">s</span> <span class="n">t</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">dsimp</span> <span class="o">[</span><span class="n">eq_sgn_aux4</span><span class="o">,</span> <span class="n">swap</span><span class="o">],</span>
  <span class="n">simp</span>
<span class="kn">end</span>
</pre></div>

#### [ Chris Hughes (Jul 29 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539698):
<p>But also probably massively slow down cimpilation time</p>

#### [ Kenny Lau (Jul 29 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539702):
<p>looks like I'm finally useful :P</p>

#### [ Kevin Buzzard (Jul 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539708):
<p>(ac)(bd) conjugates (ab) into (cd). In general conjugating by g sends (abc) to (ga gb gc) and the same for products of cycles</p>

#### [ Kenny Lau (Jul 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539710):
<p>your thing only works when we have more separation axioms</p>

#### [ Kenny Lau (Jul 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539711):
<p>here we only know that <code>a != b</code> and <code>c != d</code></p>

#### [ Kevin Buzzard (Jul 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539712):
<p>No</p>

#### [ Kenny Lau (Jul 29 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539758):
<p>wait what</p>

#### [ Kenny Lau (Jul 29 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539769):
<p>ok now I'm shocked</p>

#### [ Kenny Lau (Jul 29 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539770):
<p>I don't believe it</p>

#### [ Kenny Lau (Jul 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539816):
<p>ah</p>

#### [ Kenny Lau (Jul 29 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539942):
<p>/me finds a hole to hide from his embarrassment</p>

#### [ Kenny Lau (Jul 29 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540157):
<p>in my defense, my definition is easier to work with</p>

#### [ Kenny Lau (Jul 29 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540186):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">eq_sgn_aux4</span> <span class="o">(</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">step</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span> <span class="o">:=</span>
<span class="n">swap</span> <span class="o">(</span><span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span>

<span class="kn">theorem</span> <span class="n">eq_sgn_aux3</span> <span class="o">(</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">step</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">eq_sgn_aux4</span> <span class="n">s</span> <span class="n">t</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">dsimp</span> <span class="o">[</span><span class="n">eq_sgn_aux4</span><span class="o">,</span> <span class="n">swap</span><span class="o">],</span>
  <span class="k">have</span> <span class="o">:=</span> <span class="n">ne_of_lt</span> <span class="n">s</span><span class="bp">.</span><span class="mi">3</span><span class="o">,</span>
  <span class="k">have</span> <span class="o">:=</span> <span class="n">ne_of_lt</span> <span class="n">t</span><span class="bp">.</span><span class="mi">3</span><span class="o">,</span>
  <span class="n">simp</span><span class="o">,</span> <span class="n">split_ifs</span><span class="bp">;</span> <span class="n">cc</span>
<span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">eq_sgn_aux2</span> <span class="o">(</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">step</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">eq_sgn_aux4</span> <span class="n">s</span> <span class="n">t</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">dsimp</span> <span class="o">[</span><span class="n">eq_sgn_aux4</span><span class="o">,</span> <span class="n">swap</span><span class="o">],</span>
  <span class="n">simp</span>
<span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">eq_sgn_aux</span> <span class="o">(</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">step</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">eq_sgn_aux4</span> <span class="n">s</span> <span class="n">t</span> <span class="bp">*</span> <span class="n">s</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">*</span> <span class="o">(</span><span class="n">eq_sgn_aux4</span> <span class="n">s</span> <span class="n">t</span><span class="o">)</span><span class="bp">⁻¹</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="kn">eval</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">ext</span> <span class="n">k</span><span class="o">,</span>
  <span class="n">by_cases</span> <span class="n">H1</span> <span class="o">:</span> <span class="n">k</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">subst</span> <span class="n">H1</span><span class="o">,</span>
    <span class="n">dsimp</span> <span class="o">[</span><span class="n">step</span><span class="bp">.</span><span class="kn">eval</span><span class="o">],</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">equiv</span><span class="bp">.</span><span class="n">symm_apply_eq</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">eq_sgn_aux3</span> <span class="n">s</span> <span class="n">t</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span> <span class="n">eq_sgn_aux2</span><span class="o">]</span> <span class="o">},</span>
  <span class="n">by_cases</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">k</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">subst</span> <span class="n">H2</span><span class="o">,</span>
    <span class="n">dsimp</span> <span class="o">[</span><span class="n">step</span><span class="bp">.</span><span class="kn">eval</span><span class="o">],</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">equiv</span><span class="bp">.</span><span class="n">symm_apply_eq</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">eq_sgn_aux2</span> <span class="n">s</span> <span class="n">t</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span> <span class="n">eq_sgn_aux3</span><span class="o">]</span> <span class="o">},</span>
  <span class="n">dsimp</span> <span class="o">[</span><span class="n">step</span><span class="bp">.</span><span class="kn">eval</span><span class="o">,</span> <span class="n">swap</span><span class="o">],</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">H1</span><span class="o">,</span> <span class="n">H2</span><span class="o">,</span> <span class="n">eq_sgn_aux2</span><span class="o">,</span> <span class="n">eq_sgn_aux3</span><span class="o">]</span>
<span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">eq_sgn</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">mu2</span><span class="o">)</span> <span class="o">[</span><span class="n">is_group_hom</span> <span class="n">f</span><span class="o">]</span>
  <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">step</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">f</span> <span class="n">s</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">=</span> <span class="bp">-</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">σ</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">f</span> <span class="n">σ</span> <span class="bp">=</span> <span class="n">sgn</span> <span class="n">σ</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">H2</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">t</span> <span class="o">:</span> <span class="n">step</span> <span class="n">n</span><span class="o">,</span> <span class="n">f</span> <span class="n">t</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">=</span> <span class="bp">-</span><span class="mi">1</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">t</span><span class="o">,</span>
    <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">eq_sgn_aux</span> <span class="n">s</span> <span class="n">t</span><span class="o">],</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">is_group_hom</span><span class="bp">.</span><span class="n">mul</span> <span class="n">f</span><span class="o">,</span> <span class="n">is_group_hom</span><span class="bp">.</span><span class="n">inv</span> <span class="n">f</span><span class="o">,</span> <span class="n">H1</span><span class="o">]</span> <span class="o">},</span>
  <span class="k">have</span> <span class="n">H3</span> <span class="o">:=</span> <span class="n">list_step_prod</span> <span class="n">σ</span><span class="o">,</span>
  <span class="n">revert</span> <span class="n">H3</span><span class="o">,</span> <span class="n">generalize</span> <span class="o">:</span> <span class="n">list_step</span> <span class="n">σ</span> <span class="bp">=</span> <span class="n">L</span><span class="o">,</span> <span class="n">intro</span> <span class="n">H3</span><span class="o">,</span> <span class="n">subst</span> <span class="n">H3</span><span class="o">,</span>
  <span class="n">induction</span> <span class="n">L</span> <span class="k">with</span> <span class="n">hd</span> <span class="n">tl</span> <span class="n">ih</span><span class="o">,</span> <span class="o">{</span> <span class="n">simp</span> <span class="o">[</span><span class="n">is_group_hom</span><span class="bp">.</span><span class="n">one</span> <span class="n">f</span><span class="o">]</span> <span class="o">},</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">is_group_hom</span><span class="bp">.</span><span class="n">mul</span> <span class="n">f</span><span class="o">,</span> <span class="n">ih</span><span class="o">,</span> <span class="n">H2</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Jul 29 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540187):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> did it help you?</p>

#### [ Chris Hughes (Jul 29 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540227):
<p>If a = d then (ac)(bd)(ab)(bd)(ac) a = (ac)(ba)(ab)(ba)(ac) a = a != c = (cd) a. What's my mistake? I'm probably being an idiot.</p>

#### [ Kenny Lau (Jul 29 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540231):
<p>hmm...</p>

#### [ Kenny Lau (Jul 29 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540884):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> how did you find that counter-example?</p>

#### [ Kevin Buzzard (Jul 29 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540885):
<p>(cd)a=a.</p>

#### [ Kenny Lau (Jul 29 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540886):
<p>(cd)a = (ca)a = c</p>

#### [ Kevin Buzzard (Jul 29 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540927):
<p>It's certainly true that if sigma sends x to y, then g sigma g^{-1} sends gx to gy.</p>

#### [ Kenny Lau (Jul 29 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540928):
<p>yes, that is true</p>

#### [ Chris Hughes (Jul 29 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540929):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">x</span> <span class="n">y</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">3</span><span class="o">,</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">y</span> <span class="bp">∧</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">b</span> <span class="bp">∧</span>
  <span class="n">transpose</span> <span class="n">x</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">transpose</span> <span class="n">y</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">transpose</span> <span class="n">x</span> <span class="n">y</span> <span class="bp">*</span> <span class="o">(</span><span class="n">transpose</span> <span class="n">x</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">transpose</span> <span class="n">y</span> <span class="n">a</span><span class="o">)</span><span class="bp">⁻¹</span> <span class="bp">≠</span>
  <span class="n">transpose</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
</pre></div>

#### [ Kenny Lau (Jul 29 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540930):
<p>ah</p>

#### [ Kenny Lau (Jul 29 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540933):
<p>relying on the automation</p>

#### [ Kevin Buzzard (Jul 29 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540940):
<p>Oh ha ha (ac)(bd) is not the map sending a to c and b to d</p>

#### [ Kevin Buzzard (Jul 29 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540981):
<p>The map that conjugates (ab) into (cd) is "anything sending a to c and b to d"</p>

#### [ Kevin Buzzard (Jul 29 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540985):
<p>In fact the general solution is "either send a to c and b to d, or send a to d and b to c -- and do anything you like with everything else"</p>

#### [ Chris Hughes (Jul 29 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541149):
<p>How briefly can you write down such a function?</p>

#### [ Kenny Lau (Jul 29 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541150):
<p>I just did</p>

#### [ Kenny Lau (Jul 29 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541151):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">eq_sgn_aux4</span> <span class="o">(</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">step</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span> <span class="o">:=</span>
<span class="n">swap</span> <span class="o">(</span><span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span>

<span class="kn">theorem</span> <span class="n">eq_sgn_aux3</span> <span class="o">(</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">step</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">eq_sgn_aux4</span> <span class="n">s</span> <span class="n">t</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">dsimp</span> <span class="o">[</span><span class="n">eq_sgn_aux4</span><span class="o">,</span> <span class="n">swap</span><span class="o">],</span>
  <span class="k">have</span> <span class="o">:=</span> <span class="n">ne_of_lt</span> <span class="n">s</span><span class="bp">.</span><span class="mi">3</span><span class="o">,</span>
  <span class="k">have</span> <span class="o">:=</span> <span class="n">ne_of_lt</span> <span class="n">t</span><span class="bp">.</span><span class="mi">3</span><span class="o">,</span>
  <span class="n">simp</span><span class="o">,</span> <span class="n">split_ifs</span><span class="bp">;</span> <span class="n">cc</span>
<span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">eq_sgn_aux2</span> <span class="o">(</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">step</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">eq_sgn_aux4</span> <span class="n">s</span> <span class="n">t</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">dsimp</span> <span class="o">[</span><span class="n">eq_sgn_aux4</span><span class="o">,</span> <span class="n">swap</span><span class="o">],</span>
  <span class="n">simp</span>
<span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">eq_sgn_aux</span> <span class="o">(</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">step</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">eq_sgn_aux4</span> <span class="n">s</span> <span class="n">t</span> <span class="bp">*</span> <span class="n">s</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">*</span> <span class="o">(</span><span class="n">eq_sgn_aux4</span> <span class="n">s</span> <span class="n">t</span><span class="o">)</span><span class="bp">⁻¹</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="kn">eval</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">ext</span> <span class="n">k</span><span class="o">,</span>
  <span class="n">by_cases</span> <span class="n">H1</span> <span class="o">:</span> <span class="n">k</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">subst</span> <span class="n">H1</span><span class="o">,</span>
    <span class="n">dsimp</span> <span class="o">[</span><span class="n">step</span><span class="bp">.</span><span class="kn">eval</span><span class="o">],</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">equiv</span><span class="bp">.</span><span class="n">symm_apply_eq</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">eq_sgn_aux3</span> <span class="n">s</span> <span class="n">t</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span> <span class="n">eq_sgn_aux2</span><span class="o">]</span> <span class="o">},</span>
  <span class="n">by_cases</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">k</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">subst</span> <span class="n">H2</span><span class="o">,</span>
    <span class="n">dsimp</span> <span class="o">[</span><span class="n">step</span><span class="bp">.</span><span class="kn">eval</span><span class="o">],</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">equiv</span><span class="bp">.</span><span class="n">symm_apply_eq</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">eq_sgn_aux2</span> <span class="n">s</span> <span class="n">t</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span> <span class="n">eq_sgn_aux3</span><span class="o">]</span> <span class="o">},</span>
  <span class="n">dsimp</span> <span class="o">[</span><span class="n">step</span><span class="bp">.</span><span class="kn">eval</span><span class="o">,</span> <span class="n">swap</span><span class="o">],</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">H1</span><span class="o">,</span> <span class="n">H2</span><span class="o">,</span> <span class="n">eq_sgn_aux2</span><span class="o">,</span> <span class="n">eq_sgn_aux3</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>

#### [ Chris Hughes (Jul 29 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541190):
<p>Why does swap have 3 arguments?</p>

#### [ Chris Hughes (Jul 29 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541192):
<p>I see</p>

#### [ Kenny Lau (Jul 29 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541193):
<p>it only has 2, then it is coerced to become a function</p>

#### [ Kenny Lau (Jul 29 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541360):
<p>I finally proved that my <code>step</code> is a fintype</p>

#### [ Kenny Lau (Jul 29 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541361):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">step</span> <span class="mi">3</span><span class="o">,</span>
  <span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">*</span> <span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">s</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">*</span> <span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">swap</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span>
  <span class="bp">≠</span> <span class="n">t</span><span class="bp">.</span><span class="kn">eval</span> <span class="o">:=</span>
<span class="n">dec_trivial</span>
</pre></div>

#### [ Chris Hughes (Jul 29 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541420):
<p>What is step?</p>

#### [ Kenny Lau (Jul 29 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541422):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">derive</span> <span class="n">decidable_eq</span><span class="o">]</span>
<span class="kn">structure</span> <span class="n">step</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">fst</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">)</span>
<span class="o">(</span><span class="n">snd</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">)</span>
<span class="o">(</span><span class="n">lt</span>  <span class="o">:</span> <span class="n">fst</span> <span class="bp">&lt;</span> <span class="n">snd</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Jul 29 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541462):
<p>it represents a transposition</p>

#### [ Kenny Lau (Jul 29 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541465):
<p><a href="https://github.com/kckennylau/Lean/blob/master/Sym.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/Sym.lean">https://github.com/kckennylau/Lean/blob/master/Sym.lean</a></p>

#### [ Chris Hughes (Jul 29 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541473):
<p>I used something similar </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">fin_pairs_lt</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="err">Σ</span> <span class="n">a</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">,</span> <span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">univ</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">))</span><span class="bp">.</span><span class="n">sigma</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="o">(</span><span class="n">range</span> <span class="n">a</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span><span class="bp">.</span><span class="n">attach_fin</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span> <span class="n">hm</span><span class="o">,</span> <span class="n">lt_trans</span> <span class="o">(</span><span class="n">mem_range</span><span class="bp">.</span><span class="mi">1</span> <span class="n">hm</span><span class="o">)</span> <span class="n">a</span><span class="bp">.</span><span class="mi">2</span><span class="o">))</span>
</pre></div>

#### [ Kevin Buzzard (Jul 29 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541533):
<p>The fact that if sigma sends x to y then g sigma g^{-1} sends gx to gy is a special case of "transport de structure". It's more easily seen if you generalise. If sigma is a permutation of a set X, and if g is a bijection between X and another set Y, then g identifies X and Y, so sigma transports over to a permutation of Y. The explicit formula for the permutation of Y is g sigma g^{-1}. If you think of g as a dictionary identifying X and Y, then a in X gets identified with ga in Y, and b in X gets identified with gb in Y. If sigma sends a to b, then the transported sigma sends ga to gb. The counterintuitive idea now is to imagine that X = Y and that g is not the identity map but perhaps some other bijection. If you think about things this way then the fact that e.g. conjugate permutations have the same cycle type becomes trivial.</p>

#### [ Chris Hughes (Jul 30 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130542126):
<p>I had to think about it like that when I defined <code>sign</code> on an arbitrary <code>fintype</code>, and not just <code>fin</code>. I used <code>equiv_fin</code> to define the <code>sign</code>, but I had to prove that <code>sign</code> did not depend on which <code>equiv_fin</code> I chose, which i used the conjugation property for by combining my two different <code>equiv_fins</code> together to make a <code>perm</code> and conjugating by that <code>perm</code></p>

#### [ Kenny Lau (Jul 30 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130562395):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">inversions_eq_sgn</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">σ</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span><span class="o">,</span> <span class="n">inversions</span> <span class="n">σ</span> <span class="bp">=</span> <span class="n">sgn</span> <span class="n">σ</span> <span class="o">:=</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">cases_on</span> <span class="n">n</span> <span class="n">dec_trivial</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">cases_on</span> <span class="n">n</span> <span class="n">dec_trivial</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">n</span> <span class="n">σ</span><span class="o">,</span>
<span class="n">eq_sgn</span> <span class="n">inversions</span> <span class="o">(</span><span class="n">step01</span> <span class="n">n</span><span class="o">)</span> <span class="n">inversions_step01</span> <span class="n">σ</span>
</pre></div>

#### [ Kevin Buzzard (Jul 30 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130562545):
<blockquote>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">x</span> <span class="n">y</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">3</span><span class="o">,</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">y</span> <span class="bp">∧</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">b</span> <span class="bp">∧</span>
  <span class="n">transpose</span> <span class="n">x</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">transpose</span> <span class="n">y</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">transpose</span> <span class="n">x</span> <span class="n">y</span> <span class="bp">*</span> <span class="o">(</span><span class="n">transpose</span> <span class="n">x</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">transpose</span> <span class="n">y</span> <span class="n">a</span><span class="o">)</span><span class="bp">⁻¹</span> <span class="bp">≠</span>
  <span class="n">transpose</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
</pre></div>


</blockquote>
<p>Did this work out of the box? I was going to use it in my talk today! But</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">A</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">3</span><span class="o">,</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
</pre></div>


<p>doesn't work for me. Do I need an import?</p>

#### [ Kenny Lau (Jul 30 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130562550):
<p>maybe import fintype</p>

#### [ Kenny Lau (Jul 30 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130562722):
<p>this is interesting. <code>fintype.decidable_exists_fintype</code> isn't in the online Lean</p>

#### [ Kenny Lau (Jul 30 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130562763):
<p>it was added <a href="https://github.com/leanprover/mathlib/commit/21b918b3083ce42c495ab48b7ea19e486e3eae6b#diff-de2c770e28fdceb296e807697c00ad8a" target="_blank" title="https://github.com/leanprover/mathlib/commit/21b918b3083ce42c495ab48b7ea19e486e3eae6b#diff-de2c770e28fdceb296e807697c00ad8a">18 days ago</a></p>

#### [ Kevin Buzzard (Jul 30 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130562986):
<p>Oh I think that might have been because of some other problem I had, which Chris fixed. Oh I remember -- it was for Ellen's dots and boxes project. She wanted to write basic definitions like "if the number of times this multiset contains 3 is at most 1, and if ..., then blah" and Lean was demanding decidability proofs. I asked why and Chris and Simon just fixed everything up so it worked.</p>

#### [ Kenny Lau (Jul 30 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130562995):
<p>'tis a small world</p>

#### [ Kevin Buzzard (Jul 30 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130563038):
<p>rofl I had a scratch file open with the "not working" theorem A, and I just imported analysis.topology.continuity to think about Patrick's comment about continuous being a class and it fixed my proof :-)</p>

#### [ Kenny Lau (Jul 30 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130563041):
<p>lol</p>


{% endraw %}
