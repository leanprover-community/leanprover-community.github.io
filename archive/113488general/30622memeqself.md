---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30622memeqself.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [mem_eq_self](https://leanprover-community.github.io/archive/113488general/30622memeqself.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Dec 02 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem_eq_self/near/150731070):
<p>Harder than I expected!</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">mem_eq_self</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">a</span><span class="o">}</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Dec 02 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem_eq_self/near/150731071):
<p>Took me three attempts!</p>

#### [ Kenny Lau (Dec 02 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem_eq_self/near/150731079):
<p>ok too me two attempts</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">mem_eq_self</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">a</span><span class="o">}</span> <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="n">a</span>
</pre></div>

#### [ Kevin Buzzard (Dec 02 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem_eq_self/near/150731132):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">refl</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">mem_eq_self</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">a</span><span class="o">}</span> <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="n">a</span>

<span class="kn">example</span> <span class="o">:</span> <span class="mi">3</span> <span class="err">∈</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">3</span><span class="o">}</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refl</span>
</pre></div>


<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> is this your suggestion? To those that didn't follow the other thread, the point is that without tagging <code>mem_eq_self</code> as <code>refl</code>, <code>by refl</code> doesn't work for the example.</p>

#### [ Kevin Buzzard (Dec 02 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem_eq_self/near/150731148):
<p><code>example : 3 ∈ {x : ℕ | 3 = x} := by refl</code> now works too. I don't really understand what is going on here.</p>

#### [ Kenny Lau (Dec 02 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem_eq_self/near/150731199):
<div class="codehilite"><pre><span></span><span class="c1">-- all fail</span>
<span class="kn">example</span> <span class="o">:</span> <span class="mi">3</span> <span class="err">∈</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">3</span><span class="o">}</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refl</span>
<span class="kn">example</span> <span class="o">:</span> <span class="mi">3</span> <span class="err">∈</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">x</span><span class="o">}</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refl</span>
<span class="kn">example</span> <span class="o">:</span> <span class="mi">3</span> <span class="err">∈</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="mi">3</span> <span class="bp">=</span> <span class="mi">3</span><span class="o">}</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refl</span>
<span class="kn">example</span> <span class="o">:</span> <span class="mi">3</span> <span class="err">∈</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="mi">3</span> <span class="bp">=</span> <span class="n">x</span><span class="o">}</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refl</span>

<span class="bp">@</span><span class="o">[</span><span class="n">refl</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">mem_eq_self</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">a</span><span class="o">}</span> <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="n">a</span>

<span class="c1">-- all work</span>
<span class="kn">example</span> <span class="o">:</span> <span class="mi">3</span> <span class="err">∈</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">3</span><span class="o">}</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refl</span>
<span class="kn">example</span> <span class="o">:</span> <span class="mi">3</span> <span class="err">∈</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">x</span><span class="o">}</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refl</span>
<span class="kn">example</span> <span class="o">:</span> <span class="mi">3</span> <span class="err">∈</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="mi">3</span> <span class="bp">=</span> <span class="mi">3</span><span class="o">}</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refl</span>
<span class="kn">example</span> <span class="o">:</span> <span class="mi">3</span> <span class="err">∈</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="mi">3</span> <span class="bp">=</span> <span class="n">x</span><span class="o">}</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refl</span>
</pre></div>

#### [ Kevin Buzzard (Dec 02 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem_eq_self/near/150731247):
<p><code>example : 3 ∈ {x : ℕ | 3 = 3} := by refl</code> -- Doesn't that say <code>3 \in set.univ</code>? Why is that <code>by refl</code>?</p>

#### [ Kenny Lau (Dec 02 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem_eq_self/near/150731256):
<p>no, set.univ is true</p>

#### [ Kevin Buzzard (Dec 02 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem_eq_self/near/150731261):
<p>We're evaluating <code>lam x, 3 = 3</code> at <code>x=3</code> :-)</p>

#### [ Kevin Buzzard (Dec 02 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem_eq_self/near/150731300):
<p>so indeed it's refl</p>


{% endraw %}
