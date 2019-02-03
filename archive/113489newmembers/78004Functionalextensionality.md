---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/78004Functionalextensionality.html
---

## Stream: [new members](index.html)
### Topic: [Functional extensionality](78004Functionalextensionality.html)

---


{% raw %}
#### [ Ken Roe (Jul 24 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Functional%20extensionality/near/130240450):
<p>Is there a functionality extensionality theorem like the one shown below in one of the libraries:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">fun_ext</span> <span class="o">{</span><span class="n">t</span><span class="o">}</span> <span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="o">:</span>
    <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span><span class="o">:</span><span class="n">t</span><span class="bp">→</span><span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span><span class="o">:</span><span class="n">t</span><span class="bp">→</span><span class="n">u</span><span class="o">),</span> <span class="n">a</span><span class="bp">=</span><span class="n">b</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">t</span><span class="o">),</span> <span class="n">a</span><span class="o">)</span><span class="bp">=</span><span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">t</span><span class="o">),</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span><span class="bp">.</span>
</pre></div>

#### [ Chris Hughes (Jul 24 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Functional%20extensionality/near/130240630):
<p>There's <code>funext</code>, but that's not the same as what you stated. The proof of the theorem you stated is <code>assume a b h, by rw  h</code></p>

#### [ Ken Roe (Jul 25 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Functional%20extensionality/near/130242691):
<p>Thanks.  I'm running into another issue.  It seems I cannot rewrite if meta variables are involved.  How is the following theorem completed (ignore the "admit"--I'd like to get the "rw h" to work.</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">dd</span> <span class="o">:</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">x</span><span class="bp">*</span><span class="mi">2</span><span class="o">)</span><span class="bp">=</span><span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">x</span><span class="bp">+</span><span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="k">begin</span>
    <span class="k">have</span> <span class="n">h</span><span class="o">:</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="bp">*</span><span class="mi">2</span><span class="bp">=</span><span class="n">x</span><span class="bp">+</span><span class="n">x</span><span class="o">,</span> <span class="n">intro</span><span class="o">,</span> <span class="n">admit</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">h</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Jul 25 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Functional%20extensionality/near/130242967):
<p>You can't rewrite bound variables. Use <code>simp only [h]</code> instead</p>

#### [ Simon Hudon (Jul 25 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Functional%20extensionality/near/130243044):
<blockquote>
<p>Is there a functionality extensionality theorem like the one shown below in one of the libraries:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">fun_ext</span> <span class="o">{</span><span class="n">t</span><span class="o">}</span> <span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="o">:</span>
    <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span><span class="o">:</span><span class="n">t</span><span class="bp">→</span><span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span><span class="o">:</span><span class="n">t</span><span class="bp">→</span><span class="n">u</span><span class="o">),</span> <span class="n">a</span><span class="bp">=</span><span class="n">b</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">t</span><span class="o">),</span> <span class="n">a</span><span class="o">)</span><span class="bp">=</span><span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">t</span><span class="o">),</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


</blockquote>
<p>Isn't that normal rewriting?</p>


{% endraw %}
