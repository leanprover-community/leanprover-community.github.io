---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/71999generalizeproofs.html
---

## Stream: [general](index.html)
### Topic: [generalize_proofs](71999generalizeproofs.html)

---


{% raw %}
#### [ Reid Barton (Dec 01 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148900772):
<p>Does <code>generalize_proofs</code> ever work?</p>

#### [ Reid Barton (Dec 01 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148900782):
<p>I get this error <code>unknown declaration '1'</code></p>

#### [ Simon Hudon (Dec 01 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148901101):
<p>What did you write?</p>

#### [ Simon Hudon (Dec 01 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148901129):
<p>I think <code>generalize_proofs</code> is obsolete. I remember <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> saying that <code>h_generalize</code> does the work <code>generalize_proofs</code> was intended to do</p>

#### [ Reid Barton (Dec 01 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148901289):
<p>something very complicated</p>

#### [ Reid Barton (Dec 01 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148901307):
<p>ah, let me try that</p>

#### [ Reid Barton (Dec 01 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148901538):
<p>hmm, I realized I need to also generalize the type that it is being converted to, and that seems tricky</p>

#### [ Reid Barton (Dec 01 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148901543):
<p>I'll just go back to my interim solution</p>

#### [ Simon Hudon (Dec 01 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148901761):
<p>Try <code>h_generalize! h : my_var == new_name</code> then you can generalize the type of the new variable</p>

#### [ Chris Hughes (Dec 01 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148902893):
<p>Does changing the definition of <code>collect_proofs_in</code> in <code>tactic.generalize_proofs</code> to this work?</p>
<div class="codehilite"><pre><span></span><span class="kn">private</span> <span class="n">meta</span> <span class="n">def</span> <span class="n">collect_proofs_in</span> <span class="o">:</span>
  <span class="n">expr</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">name</span> <span class="bp">×</span> <span class="n">list</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="o">(</span><span class="n">list</span> <span class="n">name</span> <span class="bp">×</span> <span class="n">list</span> <span class="n">expr</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">e</span> <span class="n">ctx</span> <span class="o">(</span><span class="n">ns</span><span class="o">,</span> <span class="n">hs</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">let</span> <span class="n">go</span> <span class="o">(</span><span class="n">tac</span> <span class="o">:</span> <span class="n">list</span> <span class="n">name</span> <span class="bp">×</span> <span class="n">list</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="o">(</span><span class="n">list</span> <span class="n">name</span> <span class="bp">×</span> <span class="n">list</span> <span class="n">expr</span><span class="o">))</span> <span class="o">:</span>
  <span class="n">tactic</span> <span class="o">(</span><span class="n">list</span> <span class="n">name</span> <span class="bp">×</span> <span class="n">list</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">do</span> <span class="n">t</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">e</span><span class="o">,</span>
   <span class="n">mcond</span> <span class="o">(</span><span class="n">is_prop</span> <span class="n">t</span><span class="o">)</span> <span class="o">(</span><span class="n">do</span>
     <span class="n">first</span> <span class="o">(</span><span class="n">hs</span><span class="bp">.</span><span class="n">map</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">do</span>
       <span class="n">t&#39;</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">h</span><span class="o">,</span>
       <span class="n">is_def_eq</span> <span class="n">t</span> <span class="n">t&#39;</span><span class="o">,</span>
       <span class="n">g</span> <span class="err">←</span> <span class="n">target</span><span class="o">,</span>
       <span class="n">change</span> <span class="err">$</span> <span class="n">g</span><span class="bp">.</span><span class="n">replace</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">n</span><span class="o">,</span> <span class="k">if</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">e</span> <span class="k">then</span> <span class="n">some</span> <span class="n">h</span> <span class="k">else</span> <span class="n">none</span><span class="o">),</span>
       <span class="n">return</span> <span class="o">(</span><span class="n">ns</span><span class="o">,</span> <span class="n">hs</span><span class="o">))</span> <span class="bp">&lt;|&gt;</span>
     <span class="o">(</span><span class="k">let</span> <span class="o">(</span><span class="n">n</span><span class="o">,</span> <span class="n">ns</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="k">match</span> <span class="n">ns</span> <span class="k">with</span>
        <span class="bp">|</span> <span class="o">[]</span> <span class="o">:=</span> <span class="o">(</span><span class="bp">`_</span><span class="n">x</span><span class="o">,</span> <span class="o">[])</span>
        <span class="bp">|</span> <span class="o">(</span><span class="n">n</span> <span class="bp">::</span> <span class="n">ns</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">n</span><span class="o">,</span> <span class="n">ns</span><span class="o">)</span>
        <span class="kn">end</span> <span class="o">:</span> <span class="n">name</span> <span class="bp">×</span> <span class="n">list</span> <span class="n">name</span><span class="o">)</span> <span class="k">in</span>
      <span class="n">do</span> <span class="n">generalize</span> <span class="n">e</span> <span class="n">n</span><span class="o">,</span>
         <span class="n">h</span> <span class="err">←</span> <span class="n">intro</span> <span class="n">n</span><span class="o">,</span>
         <span class="n">return</span> <span class="o">(</span><span class="n">ns</span><span class="o">,</span> <span class="n">h</span><span class="bp">::</span><span class="n">hs</span><span class="o">))</span> <span class="bp">&lt;|&gt;</span> <span class="n">return</span> <span class="o">(</span><span class="n">ns</span><span class="o">,</span> <span class="n">hs</span><span class="o">))</span> <span class="o">(</span><span class="n">tac</span> <span class="o">(</span><span class="n">ns</span><span class="o">,</span> <span class="n">hs</span><span class="o">)))</span> <span class="bp">&lt;|&gt;</span> <span class="n">return</span> <span class="o">(</span><span class="n">ns</span><span class="o">,</span> <span class="n">hs</span><span class="o">)</span> <span class="k">in</span>
<span class="k">match</span> <span class="n">e</span> <span class="k">with</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">const</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>   <span class="o">:=</span> <span class="n">go</span> <span class="n">return</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">local_const</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">t</span><span class="o">)</span> <span class="o">:=</span> <span class="n">collect_proofs_in</span> <span class="n">t</span> <span class="n">ctx</span> <span class="o">(</span><span class="n">ns</span><span class="o">,</span> <span class="n">hs</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">mvar</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">t</span><span class="o">)</span>  <span class="o">:=</span> <span class="n">collect_proofs_in</span> <span class="n">t</span> <span class="n">ctx</span> <span class="o">(</span><span class="n">ns</span><span class="o">,</span> <span class="n">hs</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span>     <span class="o">:=</span>
  <span class="n">go</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">nh</span><span class="o">,</span> <span class="n">collect_proofs_in</span> <span class="n">f</span> <span class="n">ctx</span> <span class="n">nh</span> <span class="bp">&gt;&gt;=</span> <span class="n">collect_proofs_in</span> <span class="n">x</span> <span class="n">ctx</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">lam</span> <span class="n">n</span> <span class="n">b</span> <span class="n">d</span> <span class="n">e</span><span class="o">)</span> <span class="o">:=</span>
  <span class="n">go</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">nh</span><span class="o">,</span> <span class="n">do</span>
    <span class="n">nh</span> <span class="err">←</span> <span class="n">collect_proofs_in</span> <span class="n">d</span> <span class="n">ctx</span> <span class="n">nh</span><span class="o">,</span>
    <span class="n">var</span> <span class="err">←</span> <span class="n">mk_local&#39;</span> <span class="n">n</span> <span class="n">b</span> <span class="n">d</span><span class="o">,</span>
    <span class="n">collect_proofs_in</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">instantiate_var</span> <span class="n">e</span> <span class="n">var</span><span class="o">)</span> <span class="o">(</span><span class="n">var</span><span class="bp">::</span><span class="n">ctx</span><span class="o">)</span> <span class="n">nh</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">pi</span> <span class="n">n</span> <span class="n">b</span> <span class="n">d</span> <span class="n">e</span><span class="o">)</span> <span class="o">:=</span> <span class="n">do</span>
  <span class="n">nh</span> <span class="err">←</span> <span class="n">collect_proofs_in</span> <span class="n">d</span> <span class="n">ctx</span> <span class="o">(</span><span class="n">ns</span><span class="o">,</span> <span class="n">hs</span><span class="o">),</span>
  <span class="n">var</span> <span class="err">←</span> <span class="n">mk_local&#39;</span> <span class="n">n</span> <span class="n">b</span> <span class="n">d</span><span class="o">,</span>
  <span class="n">collect_proofs_in</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">instantiate_var</span> <span class="n">e</span> <span class="n">var</span><span class="o">)</span> <span class="o">(</span><span class="n">var</span><span class="bp">::</span><span class="n">ctx</span><span class="o">)</span> <span class="n">nh</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">elet</span> <span class="n">n</span> <span class="n">t</span> <span class="n">d</span> <span class="n">e</span><span class="o">)</span> <span class="o">:=</span>
  <span class="n">go</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">nh</span><span class="o">,</span> <span class="n">do</span>
    <span class="n">nh</span> <span class="err">←</span> <span class="n">collect_proofs_in</span> <span class="n">t</span> <span class="n">ctx</span> <span class="n">nh</span><span class="o">,</span>
    <span class="n">nh</span> <span class="err">←</span> <span class="n">collect_proofs_in</span> <span class="n">d</span> <span class="n">ctx</span> <span class="n">nh</span><span class="o">,</span>
    <span class="n">collect_proofs_in</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">instantiate_var</span> <span class="n">e</span> <span class="n">d</span><span class="o">)</span> <span class="n">ctx</span> <span class="n">nh</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">macro</span> <span class="n">m</span> <span class="n">l</span><span class="o">)</span> <span class="o">:=</span>
  <span class="n">go</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">nh</span><span class="o">,</span> <span class="n">mfoldl</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">e</span><span class="o">,</span> <span class="n">collect_proofs_in</span> <span class="n">e</span> <span class="n">ctx</span> <span class="n">x</span><span class="o">)</span> <span class="n">nh</span> <span class="n">l</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span>                  <span class="o">:=</span> <span class="n">return</span> <span class="o">(</span><span class="n">ns</span><span class="o">,</span> <span class="n">hs</span><span class="o">)</span>
<span class="kn">end</span>
</pre></div>

#### [ Chris Hughes (Dec 01 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148903419):
<p>I think the problem is that <code>infer_type</code> fails given a <code>sort</code></p>

#### [ Mario Carneiro (Dec 01 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148905988):
<p><code>generalize_proofs</code> is not so much obsolete as broken and abandoned</p>

#### [ Mario Carneiro (Dec 01 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize_proofs/near/148905991):
<p>I think it works as long as there are no binders in the goal</p>


{% endraw %}
