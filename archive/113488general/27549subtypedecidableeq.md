---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27549subtypedecidableeq.html
---

## Stream: [general](index.html)
### Topic: [subtype.decidable_eq](27549subtypedecidableeq.html)

---


{% raw %}
#### [ Chris Hughes (Jan 04 2019 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype.decidable_eq/near/154417392):
<p><code>subtype.decidable_eq</code> sometimes fails to reduce in the kernel. Not sure why this is, it doesn't use <code>propext</code> or anything. The <code>instance</code> <code>foo</code> that I wrote in this code does work for some reason.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">group_theory</span><span class="bp">.</span><span class="n">perm</span> <span class="n">group_theory</span><span class="bp">.</span><span class="n">coset</span>

<span class="kn">open</span> <span class="n">equiv</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="bp">⟨</span><span class="mi">1</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">perm</span> <span class="n">bool</span> <span class="bp">//</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">})</span> <span class="bp">=</span> <span class="bp">⟨</span><span class="n">swap</span> <span class="n">ff</span> <span class="n">tt</span> <span class="bp">*</span> <span class="n">swap</span> <span class="n">ff</span> <span class="n">tt</span><span class="o">,</span> <span class="n">dec_trivial</span><span class="bp">⟩</span> <span class="o">:=</span>
<span class="n">dec_trivial</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="bp">⟨</span><span class="mi">1</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">perm</span> <span class="n">bool</span> <span class="bp">//</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">})</span> <span class="bp">=</span> <span class="bp">⟨</span><span class="n">swap</span> <span class="n">ff</span> <span class="n">tt</span> <span class="bp">*</span> <span class="n">swap</span> <span class="n">ff</span> <span class="n">tt</span><span class="o">,</span> <span class="n">dec_trivial</span><span class="bp">⟩</span> <span class="o">:=</span>
<span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="n">dec_trivial</span>

<span class="bp">@</span><span class="o">[</span><span class="kn">instance</span><span class="o">,</span> <span class="n">priority</span> <span class="mi">1000</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">foo</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">P</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span>
  <span class="n">decidable_eq</span> <span class="o">(</span><span class="n">subtype</span> <span class="n">P</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">decidable_of_iff</span> <span class="o">(</span><span class="n">a</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">=</span> <span class="n">b</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="k">by</span> <span class="n">cases</span> <span class="n">a</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">b</span><span class="bp">;</span> <span class="n">simp</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="bp">⟨</span><span class="mi">1</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">perm</span> <span class="n">bool</span> <span class="bp">//</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">})</span> <span class="bp">=</span> <span class="bp">⟨</span><span class="n">swap</span> <span class="n">ff</span> <span class="n">tt</span> <span class="bp">*</span> <span class="n">swap</span> <span class="n">ff</span> <span class="n">tt</span><span class="o">,</span> <span class="n">dec_trivial</span><span class="bp">⟩</span> <span class="o">:=</span>
<span class="n">dec_trivial</span>
</pre></div>

#### [ Mario Carneiro (Jan 04 2019 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype.decidable_eq/near/154422485):
<p>Here's a little test of the decidable instance:</p>
<div class="codehilite"><pre><span></span><span class="n">run_cmd</span> <span class="n">do</span>
  <span class="k">let</span> <span class="n">t</span> <span class="o">:=</span> <span class="bp">`</span><span class="o">((</span><span class="bp">⟨</span><span class="mi">1</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">perm</span> <span class="n">bool</span> <span class="bp">//</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">})</span> <span class="bp">=</span> <span class="bp">⟨</span><span class="n">swap</span> <span class="n">ff</span> <span class="n">tt</span> <span class="bp">*</span> <span class="n">swap</span> <span class="n">ff</span> <span class="n">tt</span><span class="o">,</span> <span class="n">dec_trivial</span><span class="bp">⟩</span><span class="o">),</span>
  <span class="n">inst</span> <span class="err">←</span> <span class="n">mk_instance</span> <span class="bp">`</span><span class="o">(</span><span class="n">decidable</span> <span class="err">%%</span><span class="n">t</span><span class="o">),</span>
  <span class="n">e</span> <span class="err">←</span> <span class="n">whnf</span> <span class="n">inst</span><span class="o">,</span> <span class="c1">-- should be is_true _ but it&#39;s not</span>
  <span class="n">trace</span> <span class="n">e</span><span class="o">,</span> <span class="c1">-- eq.rec (λ (w_property : 1 = 1), is_true _) _ _</span>
  <span class="o">[</span><span class="bp">_</span><span class="o">,</span><span class="bp">_</span><span class="o">,</span><span class="bp">_</span><span class="o">,</span><span class="bp">_</span><span class="o">,</span><span class="bp">_</span><span class="o">,</span><span class="bp">_</span><span class="o">,</span><span class="n">e</span><span class="o">]</span> <span class="err">←</span> <span class="n">return</span> <span class="err">$</span> <span class="n">expr</span><span class="bp">.</span><span class="n">get_app_args</span> <span class="n">e</span><span class="o">,</span> <span class="c1">-- get the major premise</span>
  <span class="bp">`</span><span class="o">(</span><span class="err">%%</span><span class="n">a</span> <span class="bp">=</span> <span class="err">%%</span><span class="n">b</span><span class="o">)</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">e</span><span class="o">,</span> <span class="c1">-- it is a proof of swap ff tt * swap ff tt = 1</span>
  <span class="n">is_def_eq</span> <span class="n">a</span> <span class="n">b</span> <span class="c1">-- and they are not defeq</span>
</pre></div>

#### [ Mario Carneiro (Jan 04 2019 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype.decidable_eq/near/154422613):
<p><code>whnf</code> gets stuck here because it does not unfold proofs, like the major premise of the <code>eq.rec</code>, and it can't ignore the proof because it's not equivalent to <code>rfl</code> (because the things being equated are not defeq)</p>

#### [ Mario Carneiro (Jan 04 2019 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype.decidable_eq/near/154422993):
<p>You should not cast types in order to prove a decidable instance. I know it's tempting but you should always use  <code>decidable_of_iff</code> which does a case on the target rather than a cast</p>

#### [ Mario Carneiro (Jan 04 2019 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype.decidable_eq/near/154423028):
<p>Unfortunately, the blame here seems to lie in <code>mk_dec_eq_instance</code>, which is bad since it powers <code>@[derive decidable_eq]</code> which is used all over</p>

#### [ Mario Carneiro (Jan 04 2019 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype.decidable_eq/near/154423095):
<p>Here's <code>subtype.decidable_eq</code>:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="kn">instance</span><span class="o">]</span>
<span class="kn">protected</span> <span class="n">def</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">decidable_eq</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="n">α</span><span class="o">],</span> <span class="n">decidable_eq</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span><span class="o">}</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="n">α</span><span class="o">],</span>
  <span class="n">id</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="bp">_</span><span class="n">v</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span><span class="o">}),</span>
       <span class="n">subtype</span><span class="bp">.</span><span class="n">cases_on</span> <span class="bp">_</span><span class="n">v</span>
         <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">val</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">property</span> <span class="o">:</span> <span class="n">p</span> <span class="n">val</span><span class="o">)</span> <span class="o">(</span><span class="n">w</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span><span class="o">}),</span>
            <span class="n">subtype</span><span class="bp">.</span><span class="n">cases_on</span> <span class="n">w</span>
              <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">w_val</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">w_property</span> <span class="o">:</span> <span class="n">p</span> <span class="n">w_val</span><span class="o">),</span>
                 <span class="n">decidable</span><span class="bp">.</span><span class="n">by_cases</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">val</span> <span class="bp">=</span> <span class="n">w_val</span><span class="o">),</span> <span class="n">eq</span><span class="bp">.</span><span class="n">rec</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">w_property</span> <span class="o">:</span> <span class="n">p</span> <span class="n">val</span><span class="o">),</span> <span class="n">is_true</span> <span class="bp">_</span><span class="o">)</span> <span class="n">a</span> <span class="n">w_property</span><span class="o">)</span>
                   <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">val</span> <span class="bp">=</span> <span class="n">w_val</span><span class="o">),</span> <span class="n">is_false</span> <span class="bp">_</span><span class="o">))))</span>
</pre></div>


<p>Note the <code>eq.rec</code> in the true branch</p>

#### [ Mario Carneiro (Jan 04 2019 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype.decidable_eq/near/154423146):
<p>if it said <code>is_true (eq.rec (λ (w_property : p val), _) a w_property)</code> there would be no problem</p>

#### [ Mario Carneiro (Jan 04 2019 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype.decidable_eq/near/154423514):
<p>the culprit is the <code>subst</code> here -&gt; <a href="https://github.com/leanprover/lean/blob/master/library/init/meta/mk_dec_eq_instance.lean#L76" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/meta/mk_dec_eq_instance.lean#L76">https://github.com/leanprover/lean/blob/master/library/init/meta/mk_dec_eq_instance.lean#L76</a> . Unfortunately I'm not sure there is anything we can do about it from mathlib</p>


{% endraw %}
