---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/13755existsatmostone.html
---

## Stream: [new members](index.html)
### Topic: [exists at most one](13755existsatmostone.html)

---


{% raw %}
#### [ Ali Sever (Jul 25 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists%20at%20most%20one/near/130274521):
<p>I want to state <code>p a b → ∃ (at most one) c, q c</code>, and if such <code>c</code> exists, I want <code>f a b = c</code>.  Is there a smart/efficient way to do this?</p>

#### [ Kevin Buzzard (Jul 25 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists%20at%20most%20one/near/130275258):
<p>you'll need the axiom of choice, because you're constructing data from a proof :-)</p>

#### [ Simon Hudon (Jul 25 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists%20at%20most%20one/near/130275840):
<p>Are you trying to build such a <code>f</code>?</p>
<p>The assertion I think could be made as <code>p a b -&gt; ∀ c₀ c₁, q c₀ → q c₁ → c₀ = c₁</code></p>

#### [ Simon Hudon (Jul 25 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists%20at%20most%20one/near/130276240):
<p>If you're defining <code>f</code>, you can do it in two ways:</p>
<div class="codehilite"><pre><span></span><span class="n">noncomputable</span> <span class="n">def</span> <span class="n">f</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">p</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">epsilon</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">c</span><span class="o">,</span> <span class="n">q</span> <span class="n">c</span><span class="o">)</span>
</pre></div>


<p>If a proper <code>c</code> exists (and your type is nonempty), the above <code>f</code> will return it (but you can't evaluate it). If such a <code>c</code> doesn't exist, we don't know what value <code>f</code> has.</p>
<p>We can be more defensive and write:</p>
<div class="codehilite"><pre><span></span><span class="n">noncomputable</span> <span class="n">def</span> <span class="n">f</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">p</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h&#39;</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">c</span><span class="o">,</span> <span class="n">q</span> <span class="n">c</span><span class="o">)</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="n">h&#39;</span>
</pre></div>


<p>This <code>f</code> can only used with a proof that a proper <code>c</code> exists and it will return that <code>c</code> (non-constructively, again).</p>


{% endraw %}
