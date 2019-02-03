---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/60254eraseduplicates.html
---

## Stream: [new members](index.html)
### Topic: [erase_duplicates](60254eraseduplicates.html)

---


{% raw %}
#### [ Keeley Hoek (Nov 24 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148267520):
<p>Does mathlib have a function which erases list duplicates?</p>

#### [ Bryan Gin-ge Chen (Nov 24 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148267854):
<p>Maybe <code>list.pw_filter</code>?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span><span class="bp">.</span><span class="n">basic</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">list</span><span class="bp">.</span><span class="n">pw_filter</span> <span class="o">(</span><span class="bp">≠</span><span class="o">)</span> <span class="o">[</span><span class="mi">1</span><span class="o">,</span><span class="mi">2</span><span class="o">,</span><span class="mi">3</span><span class="o">,</span><span class="mi">5</span><span class="o">,</span><span class="mi">5</span><span class="o">,</span><span class="mi">5</span><span class="o">,</span><span class="mi">5</span><span class="o">,</span><span class="mi">2</span><span class="o">,</span><span class="mi">1</span><span class="o">,</span><span class="mi">4</span><span class="o">,</span><span class="mi">1</span><span class="o">]</span> <span class="c1">-- [3, 5, 2, 4, 1]</span>
</pre></div>

#### [ Bryan Gin-ge Chen (Nov 24 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148267993):
<p>Oh, <code>list.erase_dup</code> is defined to be <code>pw_filter (≠)</code>. But its docstring is wrong:</p>
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm"> `erase_dup l` removes duplicates from `l` (taking only the first occurrence).</span>

<span class="cm">     erase_dup [1, 2, 2, 0, 1] = [1, 2, 0] -/</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">list</span><span class="bp">.</span><span class="n">erase_dup</span> <span class="o">[</span><span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">,</span> <span class="mi">2</span><span class="o">,</span> <span class="mi">0</span><span class="o">,</span> <span class="mi">1</span><span class="o">]</span> <span class="c1">-- [2, 0, 1]</span>
</pre></div>

#### [ Kevin Buzzard (Nov 24 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148268163):
<p>It removed the first "1" and the first "2"</p>

#### [ Kevin Buzzard (Nov 24 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148268210):
<p>Should it say "...leaving only the last occurrence"?</p>

#### [ Mario Carneiro (Nov 24 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148268668):
<p>yeah, obviously I meant first from the right end ;)</p>

#### [ Bryan Gin-ge Chen (Nov 24 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148269503):
<p>I'm putting together a PR that fixes this and also improves the other docstrings in <code>data.list.basic</code>. I found that the example given for <code>list.sigma</code> is also wrong:</p>
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm"> `sigma l₁ l₂` is the list of dependent pairs `(a, b)` where `a ∈ l₁` and `b ∈ l₂ a`.</span>

<span class="cm">     sigma [1, 2] (λ_, [5, 6]) = [(1, 5), (1, 6), (2, 5), (2, 6)] -/</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">list</span><span class="bp">.</span><span class="n">sigma</span> <span class="o">[</span><span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">]</span> <span class="o">(</span><span class="bp">λ_</span><span class="o">,</span> <span class="o">[</span><span class="mi">5</span><span class="o">,</span> <span class="mi">6</span><span class="o">])</span>
<span class="c">/-</span><span class="cm"> don&#39;t know how to synthesize placeholder</span>
<span class="cm">context:</span>
<span class="cm">⊢ ℕ → Type ?</span>
<span class="cm">-/</span>
</pre></div>


<p>The following works, but I don't think this would make a good example:</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">eval</span> <span class="bp">@</span><span class="n">list</span><span class="bp">.</span><span class="n">sigma</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">λ_</span><span class="o">,</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">[</span><span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">]</span> <span class="o">(</span><span class="bp">λ_</span><span class="o">,</span> <span class="o">[</span><span class="mi">5</span><span class="o">,</span><span class="mi">6</span><span class="o">])</span> <span class="c1">--[(1, 5), (1, 6), (2, 5), (2, 6)]</span>
</pre></div>


<p>Any suggestions?</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148269615):
<p>hm, that's weird</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148269616):
<p>does a type ascription on <code>[5,6]</code> work?</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148269622):
<p>or even just on <code>5</code></p>

#### [ Bryan Gin-ge Chen (Nov 24 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148269665):
<p>Ah, yes, that works.</p>

#### [ Bryan Gin-ge Chen (Nov 24 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/erase_duplicates/near/148271040):
<p><a href="https://github.com/leanprover/mathlib/pull/493" target="_blank" title="https://github.com/leanprover/mathlib/pull/493">https://github.com/leanprover/mathlib/pull/493</a></p>


{% endraw %}
