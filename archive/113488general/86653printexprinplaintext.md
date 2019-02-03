---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86653printexprinplaintext.html
---

## Stream: [general](index.html)
### Topic: [print `expr` in plaintext](86653printexprinplaintext.html)

---


{% raw %}
#### [ Zesen Qian (Aug 12 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012147):
<p>How to print an <code>expr</code> in a plaintext way? That is, represented as all constructors <code>app</code> <code>lam</code> <code>var</code>, etc..</p>

#### [ Zesen Qian (Aug 12 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012314):
<p>Maybe I should provide a context: I'm parsing a <code>expr</code> which (in pretty print) read like \forall (a b : bool), (b -&gt; a). But somehow I encouter <code>var 2</code> at <code>b</code> 's position, which is not possible because there should be only <code>0</code>(refering to <code>b</code>) and <code>1</code>(refering to <code>a</code>).</p>

#### [ Simon Hudon (Aug 12 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012324):
<p>use <code>e.to_raw_fmt</code></p>

#### [ Zesen Qian (Aug 12 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012325):
<p>it's actually <code>      ∀ (a b : bool), ↥b → ↥a</code>, to be precise.</p>

#### [ Simon Hudon (Aug 12 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012338):
<p>Did you use <code>expr.lambdas</code> or <code>expr.pis</code>?</p>

#### [ Zesen Qian (Aug 12 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012398):
<p>thank you, I got this: </p>
<div class="codehilite"><pre><span></span>(pi a default (const bool []) (pi b default (const bool []) (pi a default (app (app (app (const coe_sort [1,
         1]) (const bool [])) (const coe_sort_bool [])) (var 0)) (app (app (app (const coe_sort [1,
         1]) (const bool [])) (const coe_sort_bool [])) (var 2)))))
</pre></div>

#### [ Simon Hudon (Aug 12 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012450):
<p><code>pis</code> and <code>lambdas</code> have a known bug which behaves like you showed and there's a fix in mathlib, in <code>meta.expr</code></p>

#### [ Simon Hudon (Aug 12 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012460):
<p>Oh, no, that's not what I thought</p>

#### [ Zesen Qian (Aug 12 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012463):
<p>I think I didn't use expr.lambdas/pis explicitly. I just wrote the formula in this form.</p>

#### [ Simon Hudon (Aug 12 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012467):
<p>You don't have only two bound variables, you have three because implication is also a pi-type</p>

#### [ Zesen Qian (Aug 12 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012512):
<p>Gee.. rookie mistake...</p>

#### [ Simon Hudon (Aug 12 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012515):
<p>I recommend you don't manipulate <code>var</code> directly, there's a better interface for it. What do you need with them?</p>

#### [ Zesen Qian (Aug 12 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012516):
<p>I need to parse a user-provided formula to generate a query to SMT solvers.</p>

#### [ Zesen Qian (Aug 12 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012523):
<p>these formulas are mostly like the one I said above.</p>

#### [ Zesen Qian (Aug 12 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012524):
<p>So first I need extract declarations, (a, b : bool), then the assertions (a -&gt; b), or something more complex.</p>

#### [ Simon Hudon (Aug 13 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012721):
<p>I see. So you're trying to use constants in your smt formulas rather than use quantifiers. What you can do is strip one quantifier at a time like this:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">unbind_vars</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">-&gt;</span> <span class="n">tactic</span> <span class="o">(</span><span class="n">list</span> <span class="n">expr</span> <span class="bp">×</span> <span class="n">expr</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">e</span> <span class="o">:=</span>
<span class="n">do</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">pi</span> <span class="n">n</span> <span class="n">bi</span> <span class="n">d</span> <span class="n">b</span><span class="o">)</span> <span class="err">←</span> <span class="n">return</span> <span class="n">e</span> <span class="bp">|</span> <span class="n">return</span> <span class="o">([],</span><span class="n">e</span><span class="o">),</span>
   <span class="n">v</span> <span class="err">←</span> <span class="n">mk_local&#39;</span> <span class="n">n</span> <span class="n">bi</span> <span class="n">d</span><span class="o">,</span>
   <span class="k">let</span> <span class="n">b&#39;</span> <span class="o">:=</span> <span class="n">b</span><span class="bp">.</span><span class="n">instantiate_var</span> <span class="n">v</span><span class="o">,</span>
   <span class="o">(</span><span class="n">vs</span><span class="o">,</span><span class="n">b&#39;&#39;</span><span class="o">)</span> <span class="err">←</span> <span class="n">unbind_vars</span> <span class="n">b&#39;</span><span class="o">,</span>
   <span class="n">return</span> <span class="o">(</span><span class="n">v</span> <span class="bp">::</span> <span class="n">vs</span><span class="o">,</span> <span class="n">b&#39;&#39;</span><span class="o">)</span>
</pre></div>

#### [ Simon Hudon (Aug 13 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012763):
<p>The only thing you do with <code>var</code> in this code is use <code>intantiate_var</code></p>

#### [ Zesen Qian (Aug 13 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012813):
<p>this is so much better than mine. Right now I have to keep track of the variable stack myself.</p>

#### [ Simon Hudon (Aug 13 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012925):
<p>The more you know ... <span class="emoji emoji-1f320" title="shooting star">:shooting_star:</span></p>

#### [ Zesen Qian (Aug 13 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012975):
<p>..the more I have to worry about?</p>

#### [ Zesen Qian (Aug 13 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132012978):
<p><span class="emoji emoji-1f600" title="grinning">:grinning:</span></p>

#### [ Simon Hudon (Aug 13 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20%60expr%60%20in%20plaintext/near/132013027):
<p>I'm hoping not in this case <span class="emoji emoji-1f606" title="laughing">:laughing:</span></p>


{% endraw %}
