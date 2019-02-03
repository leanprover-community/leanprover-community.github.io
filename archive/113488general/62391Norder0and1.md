---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/62391Norder0and1.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [N, order, 0 and 1](https://leanprover-community.github.io/archive/113488general/62391Norder0and1.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Ned Summers (Aug 18 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/N%2C%20order%2C%200%20and%201/near/132369398):
<p>Hey, I'm trying to prove the seemingly very simple</p>
<div class="codehilite"><pre><span></span>example (n : ℕ) (h : n &lt; 1) : n = 0 := sorry
</pre></div>


<p>It's revealing a lot about what I don't know in lean (like getting stuck getting 1&gt;n from n&lt;1) and would welcome any advice/solutions. I'm not working very much at all with order or N at any other stage so, despite wading through theorems the past couple of days trying to find what I need, I'm giving up a bit. Thanks.</p>
<p>(Also, I'm using this to show that if you take any <code>(a : fin 1)</code> then <code>a = 0</code>. I suspect too that this is probably much simpler than what I'm doing.)</p>

#### [ Mario Carneiro (Aug 18 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/N%2C%20order%2C%200%20and%201/near/132369562):
<p>you should be able to do it by cases</p>

#### [ Mario Carneiro (Aug 18 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/N%2C%20order%2C%200%20and%201/near/132369628):
<p>not my favorite proof:</p>
<div class="codehilite"><pre><span></span>example (n : ℕ) (h : n &lt; 1) : n = 0 :=
by cases h with _ h; [refl, cases h]
</pre></div>

#### [ Mario Carneiro (Aug 18 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/N%2C%20order%2C%200%20and%201/near/132369681):
<div class="codehilite"><pre><span></span>example (n : fin 1) : n = 0 :=
fin.cases rfl (λ i, i.elim0) n
</pre></div>

#### [ Mario Carneiro (Aug 18 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/N%2C%20order%2C%200%20and%201/near/132370212):
<div class="codehilite"><pre><span></span>example : ∀ (n : fin 1), n = 0 := dec_trivial
</pre></div>

#### [ Patrick Massot (Aug 18 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/N%2C%20order%2C%200%20and%201/near/132371079):
<blockquote>
<p>It's revealing a lot about what I don't know in lean (like getting stuck getting 1&gt;n from n&lt;1) and would welcome any advice/solutions. </p>
</blockquote>
<p>This is literaly the same thing.</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">&gt;</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">h</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">&gt;</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">change</span> <span class="mi">1</span> <span class="bp">&gt;</span> <span class="n">n</span><span class="o">,</span>
<span class="n">assumption</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Aug 18 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/N%2C%20order%2C%200%20and%201/near/132371124):
<p>Note that the <code>change</code> is here so you see it in the interative message window, but it's useless</p>

#### [ Kenny Lau (Aug 18 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/N%2C%20order%2C%200%20and%201/near/132376851):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="mi">1</span> <span class="bp">→</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="n">dec_trivial</span>
</pre></div>

#### [ Ned Summers (Aug 20 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/N%2C%20order%2C%200%20and%201/near/132445610):
<p>Thanks everyone, dec_trivial is a nice thing to know about. Will be using this to ponder where my break in understanding was.</p>


{% endraw %}
