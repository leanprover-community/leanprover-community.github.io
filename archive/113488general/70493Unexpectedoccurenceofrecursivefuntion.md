---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/70493Unexpectedoccurenceofrecursivefuntion.html
---

## Stream: [general](index.html)
### Topic: [Unexpected occurence of recursive funtion](70493Unexpectedoccurenceofrecursivefuntion.html)

---


{% raw %}
#### [ Minchao Wu (Jul 08 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20occurence%20of%20recursive%20funtion/near/129302165):
<p>Hi friends, I'm wondering what's the right way to let Lean accept recursive calls with list.map?<br>
For example:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">bar</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="mi">0</span>     <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">list</span><span class="bp">.</span><span class="n">length</span> <span class="err">$</span> <span class="n">list</span><span class="bp">.</span><span class="n">map</span> <span class="n">bar</span> <span class="o">[</span><span class="n">n</span><span class="o">,</span> <span class="n">n</span><span class="o">,</span> <span class="n">n</span><span class="o">]</span>
</pre></div>


<p>Lean is not happy with the above one.</p>

#### [ Chris Hughes (Jul 08 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20occurence%20of%20recursive%20funtion/near/129306754):
<p>This works for this example. In general I think you pretty cannot do recursive calls with <code>list.map</code> and you have to find some different way of defining the function.</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">bar</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="mi">0</span>     <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">list</span><span class="bp">.</span><span class="n">length</span> <span class="err">$</span> <span class="o">[</span><span class="n">bar</span> <span class="n">n</span><span class="o">,</span> <span class="n">bar</span> <span class="n">n</span><span class="o">,</span> <span class="n">bar</span> <span class="n">n</span><span class="o">]</span>
</pre></div>

#### [ Minchao Wu (Jul 08 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20occurence%20of%20recursive%20funtion/near/129307191):
<p>Yes, your solution definitely works. But I am curious about why it cannot be done with maps.</p>

#### [ Chris Hughes (Jul 08 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20occurence%20of%20recursive%20funtion/near/129307283):
<p>It might be possible, but it's not easy. The equation compiler knows your function is well-founded if the recursive call applies it to a nat less than <code>n + 1</code>. Here your function <code>bar</code> is not actually applied to anything, so it cannot prove it is well founded.</p>

#### [ Minchao Wu (Jul 08 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20occurence%20of%20recursive%20funtion/near/129307398):
<p>That's true. Usually if Lean cannot prove well-foundedness then it throws a different error asking me for a proof, but for this one it just gives up. I guess the reason is exactly that <code>bar</code> is not applied to anything as you said.</p>

#### [ Chris Hughes (Jul 08 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20occurence%20of%20recursive%20funtion/near/129307555):
<p>I found a way </p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span><span class="bp">.</span><span class="n">basic</span>
<span class="n">def</span> <span class="n">bar</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="mi">0</span>     <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">list</span><span class="bp">.</span><span class="n">length</span>
  <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">pmap</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span> <span class="o">(</span><span class="n">hm</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">),</span> <span class="n">bar</span> <span class="n">m</span><span class="o">)</span> <span class="o">[</span><span class="n">n</span><span class="o">,</span> <span class="n">n</span><span class="o">,</span> <span class="n">n</span><span class="o">]</span>
  <span class="o">(</span><span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">lt_succ_self</span><span class="o">]))</span>
</pre></div>

#### [ Minchao Wu (Jul 08 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20occurence%20of%20recursive%20funtion/near/129307790):
<p>Great, this looks like a general solution. Thanks!</p>


{% endraw %}
