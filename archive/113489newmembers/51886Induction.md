---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/51886Induction.html
---

## Stream: [new members](index.html)
### Topic: [Induction](51886Induction.html)

---


{% raw %}
#### [ Alistair Tucker (Sep 25 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/134579977):
<p>Hello again! I'm still having a little trouble with my induction. In the example below the second dite gives me</p>
<div class="codehilite"><pre><span></span><span class="n">term</span>
  <span class="bp">λ</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">≠</span> <span class="n">n</span><span class="o">),</span> <span class="n">sol</span><span class="bp">.</span><span class="n">v</span> <span class="n">s</span> <span class="bp">_</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="bp">Π</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">≠</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">sol</span><span class="bp">.</span><span class="n">V</span> <span class="n">s</span> <span class="bp">_</span> <span class="bp">→</span> <span class="n">β</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="bp">¬</span><span class="n">card</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">→</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">V</span> <span class="n">s</span> <span class="n">hs</span> <span class="bp">→</span> <span class="n">β</span>
</pre></div>


<p>But by the definition, V s hs should be the same as sol.V s (lt_of_ne s hs h)?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finset</span>
<span class="kn">open</span> <span class="n">nat</span> <span class="n">finset</span>

<span class="n">def</span> <span class="n">names</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">string</span> <span class="o">:=</span> <span class="o">{</span><span class="s2">&quot;BARC&quot;</span><span class="o">,</span> <span class="s2">&quot;HSBC&quot;</span><span class="o">,</span> <span class="s2">&quot;LLOY&quot;</span><span class="o">,</span> <span class="s2">&quot;NATW&quot;</span><span class="o">,</span> <span class="s2">&quot;RBSG&quot;</span><span class="o">,</span> <span class="s2">&quot;SANT&quot;</span><span class="o">,</span> <span class="s2">&quot;STDCH&quot;</span><span class="o">}</span>
<span class="n">def</span> <span class="n">B</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">:=</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">string</span> <span class="bp">//</span> <span class="n">s</span> <span class="err">∈</span> <span class="n">names</span><span class="o">}</span>

<span class="kn">structure</span> <span class="n">soln</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">V</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">B</span><span class="o">),</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span>
<span class="o">(</span><span class="n">v</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">hs</span> <span class="o">:</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">V</span> <span class="n">s</span> <span class="n">hs</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span>

<span class="kn">variable</span> <span class="o">{</span><span class="n">find_domain</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">B</span><span class="o">)</span> <span class="o">:</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">soln</span> <span class="n">α</span> <span class="n">β</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span>
<span class="kn">variable</span> <span class="o">{</span><span class="n">solve_pde</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">B</span><span class="o">)</span> <span class="o">:</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">soln</span> <span class="n">α</span> <span class="n">β</span> <span class="n">n</span> <span class="bp">→</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">V</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">V</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span>

<span class="n">def</span> <span class="n">solve_system</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">),</span> <span class="n">soln</span> <span class="n">α</span> <span class="n">β</span> <span class="n">n</span> <span class="o">:=</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">rec</span>
    <span class="o">(</span><span class="k">let</span> <span class="n">V</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">hs</span> <span class="o">:</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">&lt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span> <span class="o">(</span><span class="n">not_lt_zero</span> <span class="o">(</span><span class="n">card</span> <span class="n">s</span><span class="o">)</span> <span class="n">hs</span><span class="o">)</span> <span class="k">in</span>
        <span class="k">let</span> <span class="n">v</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">hs</span> <span class="o">:</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">&lt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">V</span> <span class="n">s</span> <span class="n">hs</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span> <span class="o">(</span><span class="n">not_lt_zero</span> <span class="o">(</span><span class="n">card</span> <span class="n">s</span><span class="o">)</span> <span class="n">hs</span><span class="o">)</span> <span class="k">in</span>
        <span class="bp">@</span><span class="n">soln</span><span class="bp">.</span><span class="n">mk</span> <span class="n">α</span> <span class="n">β</span> <span class="mi">0</span> <span class="n">V</span> <span class="n">v</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">(</span><span class="n">sol</span> <span class="o">:</span> <span class="n">soln</span> <span class="n">α</span> <span class="n">β</span> <span class="n">n</span><span class="o">),</span>
        <span class="k">let</span> <span class="n">lt_of_ne</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">hs</span> <span class="o">:</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">&lt;</span> <span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">≠</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="o">:=</span>
            <span class="k">have</span> <span class="n">h1</span> <span class="o">:</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">∨</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">n</span><span class="o">,</span> <span class="k">from</span> <span class="n">lt_succ_iff_lt_or_eq</span><span class="bp">.</span><span class="n">mp</span> <span class="n">hs</span><span class="o">,</span>
            <span class="k">assume</span> <span class="n">h2</span> <span class="o">:</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">≠</span> <span class="n">n</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">elim</span> <span class="n">h1</span> <span class="n">id</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">absurd</span> <span class="n">h</span> <span class="n">h2</span><span class="o">)</span> <span class="k">in</span>
        <span class="k">let</span> <span class="n">V</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">hs</span> <span class="o">:</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">&lt;</span> <span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="o">:=</span>
            <span class="n">dite</span> <span class="o">(</span><span class="n">card</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">n</span><span class="o">)</span>
                <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">n</span><span class="o">),</span> <span class="n">find_domain</span> <span class="n">α</span> <span class="n">β</span> <span class="n">n</span> <span class="n">s</span> <span class="n">h</span> <span class="n">sol</span><span class="o">)</span>
                <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">≠</span> <span class="n">n</span><span class="o">),</span> <span class="n">sol</span><span class="bp">.</span><span class="n">V</span> <span class="n">s</span> <span class="o">(</span><span class="n">lt_of_ne</span> <span class="n">s</span> <span class="n">hs</span> <span class="n">h</span><span class="o">))</span> <span class="k">in</span>
        <span class="k">let</span> <span class="n">v</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">hs</span> <span class="o">:</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">&lt;</span> <span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">V</span> <span class="n">s</span> <span class="n">hs</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span>
            <span class="n">dite</span> <span class="o">(</span><span class="n">card</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">n</span><span class="o">)</span>
                <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">n</span><span class="o">),</span> <span class="n">solve_pde</span> <span class="n">α</span> <span class="n">β</span> <span class="n">n</span> <span class="n">s</span> <span class="n">h</span> <span class="n">sol</span> <span class="o">(</span><span class="n">V</span> <span class="n">s</span> <span class="n">hs</span><span class="o">))</span>
                <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">≠</span> <span class="n">n</span><span class="o">),</span> <span class="n">sol</span><span class="bp">.</span><span class="n">v</span> <span class="n">s</span> <span class="o">(</span><span class="n">lt_of_ne</span> <span class="n">s</span> <span class="n">hs</span> <span class="n">h</span><span class="o">))</span> <span class="k">in</span>
        <span class="bp">@</span><span class="n">soln</span><span class="bp">.</span><span class="n">mk</span> <span class="n">α</span> <span class="n">β</span> <span class="o">(</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="n">V</span> <span class="n">v</span><span class="o">)</span>
</pre></div>

#### [ Alistair Tucker (Sep 25 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/134579994):
<p>As you can probably tell by the names, I am attempting some applied mathematics :)</p>

#### [ Reid Barton (Sep 25 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/134590793):
<p><code>V s hs</code> isn't equal to <code>sol.V s (lt_of_ne s hs h)</code> in general, only when you have the hypothesis <code>¬card s = n</code>, and even then it's not a definitional equality. You have to use <code>dif_neg</code> to simplify the <code>dite</code>.</p>

#### [ Reid Barton (Sep 25 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/134590965):
<p>I haven't looked carefully at what's going on here, but I wonder if there might be an easier way--it looks like you're constructing a "solution for all sets of size &lt; n" by induction on n, where we just pass to the inductive hypothesis if the set is not of the new size--then why not just define a "solution for all sets of size = n", and then if you want to reproduce the type of <code>soln</code>, just provide <code>n = card s</code></p>

#### [ Alistair Tucker (Sep 25 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/134592386):
<p>Thanks! I have applied dif_neg but the final step eludes me...</p>
<div class="codehilite"><pre><span></span><span class="k">let</span> <span class="n">v</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">hs</span> <span class="o">:</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">&lt;</span> <span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">V</span> <span class="n">s</span> <span class="n">hs</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span>
    <span class="n">dite</span> <span class="o">(</span><span class="n">card</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">n</span><span class="o">)</span>
        <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">n</span><span class="o">),</span> <span class="n">solve_pde</span> <span class="n">α</span> <span class="n">β</span> <span class="n">n</span> <span class="n">s</span> <span class="n">h</span> <span class="n">sol</span> <span class="o">(</span><span class="n">V</span> <span class="n">s</span> <span class="n">hs</span><span class="o">))</span>
        <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">≠</span> <span class="n">n</span><span class="o">),</span>
            <span class="k">have</span> <span class="n">V</span> <span class="n">s</span> <span class="n">hs</span> <span class="bp">=</span> <span class="n">sol</span><span class="bp">.</span><span class="n">V</span> <span class="n">s</span> <span class="o">(</span><span class="n">lt_of_ne</span> <span class="n">s</span> <span class="n">hs</span> <span class="n">h</span><span class="o">),</span> <span class="k">from</span> <span class="n">dif_neg</span> <span class="n">h</span><span class="o">,</span>
            <span class="n">sol</span><span class="bp">.</span><span class="n">v</span> <span class="n">s</span> <span class="o">(</span><span class="n">lt_of_ne</span> <span class="n">s</span> <span class="n">hs</span> <span class="n">h</span><span class="o">))</span> <span class="k">in</span>
</pre></div>

#### [ Alistair Tucker (Sep 25 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/134592520):
<p>Your description of my intended algorithm is spot on. The reason I am trying to accumulate the Vs and vs in each successive soln is so that I can prove certain relations between them.</p>

#### [ Reid Barton (Sep 25 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/134592759):
<p>Now there are two ways to proceed</p>

#### [ Reid Barton (Sep 25 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/134592811):
<p>The easier way is to change the last line to something like <code>by rw this; exact sol.v s (lt_of_ne s hs h)</code>, or the term-mode equivalent using <code>eq.rec</code></p>

#### [ Alistair Tucker (Sep 25 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/134593877):
<p>Got it! Thank you.</p>

#### [ Reid Barton (Sep 25 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/134594108):
<p>The slightly more complicated way is to instead use the equality <code>this</code> to turn the hypothesis <code>y ∈ V s hs</code> into a proof of <code>y ∈ sol.V s _</code>--this will probably make things easier later if you want to prove things about the values of <code>v</code>, because the actual <code>β</code> value won't be wrapped inside a <code>rw</code>/<code>eq.rec</code></p>

#### [ Patrick Thomas (Jan 03 2019 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154250457):
<p>Suppose I have the following:</p>
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">lambda</span>

<span class="kn">inductive</span> <span class="n">exp</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">var</span> <span class="o">:</span> <span class="n">string</span> <span class="bp">→</span> <span class="n">exp</span>
<span class="bp">|</span> <span class="n">app</span> <span class="o">:</span> <span class="n">exp</span> <span class="bp">→</span> <span class="n">exp</span> <span class="bp">→</span> <span class="n">exp</span>
<span class="bp">|</span> <span class="n">abs</span> <span class="o">:</span> <span class="n">string</span> <span class="bp">→</span> <span class="n">exp</span> <span class="bp">→</span> <span class="n">exp</span>

<span class="kn">inductive</span> <span class="n">is_subterm</span> <span class="o">:</span> <span class="n">exp</span> <span class="bp">→</span> <span class="n">exp</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="c1">-- x ∈ Sub (x)</span>
<span class="bp">|</span> <span class="n">var</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">string</span><span class="o">),</span> <span class="n">is_subterm</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">var</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">var</span> <span class="n">x</span><span class="o">)</span>

<span class="c1">-- e1 ∈ Sub ((e1 e2))</span>
<span class="bp">|</span> <span class="n">app_l</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">e1</span> <span class="o">:</span> <span class="n">exp</span><span class="o">)</span> <span class="o">(</span><span class="n">e2</span> <span class="o">:</span> <span class="n">exp</span><span class="o">),</span> <span class="n">is_subterm</span> <span class="n">e1</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">app</span> <span class="n">e1</span> <span class="n">e2</span><span class="o">)</span>

<span class="c1">-- e2 ∈ Sub ((e1 e2))</span>
<span class="bp">|</span> <span class="n">app_r</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">e1</span> <span class="o">:</span> <span class="n">exp</span><span class="o">)</span> <span class="o">(</span><span class="n">e2</span> <span class="o">:</span> <span class="n">exp</span><span class="o">),</span> <span class="n">is_subterm</span> <span class="n">e2</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">app</span> <span class="n">e1</span> <span class="n">e2</span><span class="o">)</span>

<span class="c1">-- (e1 e2) ∈ Sub ((e1 e2))</span>
<span class="bp">|</span> <span class="n">app_self</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">e1</span> <span class="o">:</span> <span class="n">exp</span><span class="o">)</span> <span class="o">(</span><span class="n">e2</span> <span class="o">:</span> <span class="n">exp</span><span class="o">),</span> <span class="n">is_subterm</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">app</span> <span class="n">e1</span> <span class="n">e2</span><span class="o">)</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">app</span> <span class="n">e1</span> <span class="n">e2</span><span class="o">)</span>

<span class="c1">-- e ∈ Sub ((λ x . e))</span>
<span class="bp">|</span> <span class="n">abs</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">string</span><span class="o">)</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">exp</span><span class="o">),</span> <span class="n">is_subterm</span> <span class="n">e</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">abs</span> <span class="n">x</span> <span class="n">e</span><span class="o">)</span>

<span class="c1">-- (λ x . e) ∈ Sub ((λ x . e))</span>
<span class="bp">|</span> <span class="n">abs_self</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">string</span><span class="o">)</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">exp</span><span class="o">),</span> <span class="n">is_subterm</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">abs</span> <span class="n">x</span> <span class="n">e</span><span class="o">)</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">abs</span> <span class="n">x</span> <span class="n">e</span><span class="o">)</span>
</pre></div>


<p>Is it possible to prove that is_subterm does not hold for something? For example, could one prove that if <code>x</code> is a lambda variable, then the only subterm of <code>x</code> is <code>x</code> itself?</p>

#### [ Patrick Massot (Jan 03 2019 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154250562):
<p>Doesn't it contradict <code>is_subterm.abs</code>?</p>

#### [ Patrick Thomas (Jan 03 2019 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154250752):
<p>Are you saying that the statement "if <code>x</code> is a lambda variable, then the only subterm of <code>x</code> is <code>x</code> itself", does not hold because of <code>is_subterm.abs</code>? I'm not sure I see why that would be the case?</p>

#### [ Gabriel Ebner (Jan 03 2019 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154250754):
<p>This is provable (hint: try the <code>cases</code> tactic):</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">y</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_subterm</span> <span class="n">y</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">var</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">exp</span><span class="bp">.</span><span class="n">var</span> <span class="n">x</span>
</pre></div>

#### [ Rob Lewis (Jan 03 2019 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154250765):
<p>You may need to be a little careful about how you state it, but this is a good place to take advantage of the equation compiler. It will discharge the structurally impossible cases for you.</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">string</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">exp</span><span class="o">),</span> <span class="n">is_subterm</span> <span class="n">e</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">var</span> <span class="n">s</span><span class="o">)</span> <span class="bp">→</span> <span class="n">e</span> <span class="bp">=</span> <span class="n">exp</span><span class="bp">.</span><span class="n">var</span> <span class="n">s</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">(</span><span class="n">is_subterm</span><span class="bp">.</span><span class="n">var</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>


<p>(As Gabriel points out, <code>cases</code> will do the same thing.)</p>

#### [ Patrick Massot (Jan 03 2019 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154250796):
<p>oh I missed "variable" in "lambda variable", it's on the next line here</p>

#### [ Patrick Thomas (Jan 03 2019 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154251107):
<p>Thank you. I will have to do some reading on tactics and the equation compiler.</p>

#### [ Patrick Thomas (Jan 03 2019 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154251985):
<p>I'm still learning how induction is handled in Lean. Does the inductive definition create theorems related to what is not an object of the defined type?</p>

#### [ Rob Lewis (Jan 03 2019 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154252289):
<p>The only objects of the defined type are the ones that can be defined using the constructors. This is a "theorem" that's captured by the type's induction principle. In your case, look at <code>#check is_subterm.cases_on </code>.</p>

#### [ Kenny Lau (Jan 03 2019 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154253410):
<p>should we use <code>nat</code> instead of <code>string</code>?</p>

#### [ Patrick Thomas (Jan 03 2019 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154254942):
<p>Is the following what Gabriel means by the <code>cases</code> tactic?</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">exp</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">string</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_subterm</span> <span class="n">e</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">var</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="n">e</span> <span class="bp">=</span> <span class="n">exp</span><span class="bp">.</span><span class="n">var</span> <span class="n">x</span> <span class="o">:=</span>
    <span class="n">exp</span><span class="bp">.</span><span class="n">cases_on</span> <span class="n">e</span>
    <span class="o">(</span><span class="k">show</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">string</span><span class="o">),</span> <span class="n">is_subterm</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">var</span> <span class="n">y</span><span class="o">)</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">var</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">var</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">var</span> <span class="n">x</span><span class="o">),</span> <span class="k">from</span>
    <span class="k">assume</span> <span class="n">y</span> <span class="o">:</span> <span class="n">string</span><span class="o">,</span>
</pre></div>


<p>I'm not sure how to proceed from here.</p>

#### [ Kenny Lau (Jan 03 2019 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154254968):
<p>well by the <code>cases</code> tactic he means <code>by cases e</code></p>

#### [ Kenny Lau (Jan 03 2019 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154254973):
<p>but I don't know if you're familiar with using tactics</p>

#### [ Patrick Thomas (Jan 03 2019 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154255034):
<p>Oh. No, I'm not.</p>

#### [ Gabriel Ebner (Jan 03 2019 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154255194):
<p>Actually I mean by cases on the <code>is_subterm</code> proof:<br>
<code>begin intro h, cases h, end</code>  (you can easily solve the remaining goal)</p>

#### [ Kenny Lau (Jan 03 2019 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154265785):
<p>why bother making <code>is_subterm</code> inductive</p>

#### [ Patrick Thomas (Jan 03 2019 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154265902):
<p>I thought it would have to be. What is the alternative?</p>

#### [ Kenny Lau (Jan 03 2019 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154266764):
<p>well it isn't inductive (i.e. recursive) so maybe just make it a def or something</p>

#### [ Patrick Thomas (Jan 03 2019 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154267466):
<p>Hmm. I was trying to formalize the recursive definition of the set of all subterms of a lambda expression given by definition 1.3.5 here: <a href="https://play.google.com/books/reader?id=orsrBQAAQBAJ&amp;hl=en_US&amp;pg=GBS.PA5.w.4.0.36" target="_blank" title="https://play.google.com/books/reader?id=orsrBQAAQBAJ&amp;hl=en_US&amp;pg=GBS.PA5.w.4.0.36">https://play.google.com/books/reader?id=orsrBQAAQBAJ&amp;hl=en_US&amp;pg=GBS.PA5.w.4.0.36</a><br>
Did I do this wrong?</p>

#### [ Rob Lewis (Jan 03 2019 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154267703):
<p>You're missing the recursive calls. The set of subterms of (M N) is the union of the subterms of M, the subterms of N, and the singleton set {(M N)}.</p>

#### [ Rob Lewis (Jan 03 2019 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154267747):
<p>In your definition, (M N) only has three subterms: M, N, and (M N).</p>

#### [ Rob Lewis (Jan 03 2019 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154267858):
<p>This is a perfectly good situation to use an inductive predicate, but the one you wrote isn't the one you wanted.</p>

#### [ Patrick Thomas (Jan 03 2019 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154269430):
<p>Does adding the following fix it?</p>
<div class="codehilite"><pre><span></span><span class="bp">|</span> <span class="n">app_l&#39;</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">exp</span><span class="o">)</span> <span class="o">(</span><span class="n">e1</span> <span class="o">:</span> <span class="n">exp</span><span class="o">)</span> <span class="o">(</span><span class="n">e2</span> <span class="o">:</span> <span class="n">exp</span><span class="o">),</span> <span class="o">(</span><span class="n">is_subterm</span> <span class="n">e</span> <span class="n">e1</span><span class="o">)</span> <span class="bp">→</span> <span class="n">is_subterm</span> <span class="n">e</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">app</span> <span class="n">e1</span> <span class="n">e2</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">app_r&#39;</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">exp</span><span class="o">)</span> <span class="o">(</span><span class="n">e1</span> <span class="o">:</span> <span class="n">exp</span><span class="o">)</span> <span class="o">(</span><span class="n">e2</span> <span class="o">:</span> <span class="n">exp</span><span class="o">),</span> <span class="o">(</span><span class="n">is_subterm</span> <span class="n">e</span> <span class="n">e2</span><span class="o">)</span> <span class="bp">→</span> <span class="n">is_subterm</span> <span class="n">e</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">app</span> <span class="n">e1</span> <span class="n">e2</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">abs&#39;</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">exp</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">string</span><span class="o">)</span> <span class="o">(</span><span class="n">e1</span> <span class="o">:</span> <span class="n">exp</span><span class="o">),</span> <span class="o">(</span><span class="n">is_subterm</span> <span class="n">e</span> <span class="n">e1</span><span class="o">)</span> <span class="bp">→</span> <span class="n">is_subterm</span> <span class="n">e</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">abs</span> <span class="n">x</span> <span class="n">e1</span><span class="o">)</span>
</pre></div>


<p>Also, is there a way to formalize this as a set, similar to the definition in the book?</p>

#### [ Gabriel Ebner (Jan 03 2019 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154269672):
<p>Sure, you can just write a recursive function:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">subterms</span> <span class="o">:</span> <span class="n">exp</span> <span class="bp">→</span> <span class="n">multiset</span> <span class="n">exp</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">var</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{</span><span class="n">exp</span><span class="bp">.</span><span class="n">var</span> <span class="n">x</span><span class="o">}</span>
<span class="c1">-- ...</span>
</pre></div>


<p>I'm not sure why they use multisets instead of sets though.</p>

#### [ Rob Lewis (Jan 03 2019 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154269810):
<p>You could add those, and you can also reduce some of the others into one case.</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">is_subterm</span> <span class="o">:</span> <span class="n">exp</span> <span class="bp">→</span> <span class="n">exp</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">self</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">is_subterm</span> <span class="n">x</span> <span class="n">x</span>
<span class="bp">|</span> <span class="n">app_l</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">e₁</span> <span class="n">e₂</span> <span class="n">x</span><span class="o">,</span> <span class="n">is_subterm</span> <span class="n">x</span> <span class="n">e₁</span> <span class="bp">→</span> <span class="n">is_subterm</span> <span class="n">x</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">app</span> <span class="n">e₁</span> <span class="n">e₂</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">app_r</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">e₁</span> <span class="n">e₂</span> <span class="n">x</span><span class="o">,</span> <span class="n">is_subterm</span> <span class="n">x</span> <span class="n">e₂</span> <span class="bp">→</span> <span class="n">is_subterm</span> <span class="n">x</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">app</span> <span class="n">e₁</span> <span class="n">e₂</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">abs</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">e</span> <span class="n">s</span> <span class="n">x</span><span class="o">,</span> <span class="n">is_subterm</span> <span class="n">x</span> <span class="n">e</span> <span class="bp">→</span> <span class="n">is_subterm</span> <span class="n">x</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">abs</span> <span class="n">s</span> <span class="n">e</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Jan 03 2019 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154270313):
<p>and rename <code>self</code> into <code>refl</code>...</p>

#### [ Kenny Lau (Jan 03 2019 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154270442):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">is_subterm</span> <span class="o">:</span> <span class="n">exp</span> <span class="bp">→</span> <span class="n">exp</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="n">e</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">var</span> <span class="n">s</span><span class="o">)</span> <span class="o">:=</span> <span class="n">e</span> <span class="bp">=</span> <span class="n">exp</span><span class="bp">.</span><span class="n">var</span> <span class="n">s</span>
<span class="bp">|</span> <span class="n">e</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">app</span> <span class="n">e₁</span> <span class="n">e₂</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">e</span> <span class="bp">=</span> <span class="n">exp</span><span class="bp">.</span><span class="n">app</span> <span class="n">e₁</span> <span class="n">e₂</span><span class="o">)</span> <span class="bp">||</span> <span class="n">is_subterm</span> <span class="n">e</span> <span class="n">e₁</span> <span class="bp">||</span> <span class="n">is_subterm</span> <span class="n">e</span> <span class="n">e₂</span>
<span class="bp">|</span> <span class="n">e</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">abs</span> <span class="n">s</span> <span class="n">e&#39;</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">e</span> <span class="bp">=</span> <span class="n">exp</span><span class="bp">.</span><span class="n">abs</span> <span class="n">s</span> <span class="n">e&#39;</span><span class="o">)</span> <span class="bp">||</span> <span class="n">is_subterm</span> <span class="n">e</span> <span class="n">e&#39;</span>
</pre></div>

#### [ Kenny Lau (Jan 03 2019 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154270505):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">is_subterm</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">exp</span><span class="o">)</span> <span class="o">:</span> <span class="n">exp</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">var</span> <span class="n">s</span><span class="o">)</span> <span class="o">:=</span> <span class="n">e</span> <span class="bp">=</span> <span class="n">exp</span><span class="bp">.</span><span class="n">var</span> <span class="n">s</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">app</span> <span class="n">e₁</span> <span class="n">e₂</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">e</span> <span class="bp">=</span> <span class="n">exp</span><span class="bp">.</span><span class="n">app</span> <span class="n">e₁</span> <span class="n">e₂</span><span class="o">)</span> <span class="bp">||</span> <span class="n">is_subterm</span> <span class="n">e₁</span> <span class="bp">||</span> <span class="n">is_subterm</span> <span class="n">e₂</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">exp</span><span class="bp">.</span><span class="n">abs</span> <span class="n">s</span> <span class="n">e&#39;</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">e</span> <span class="bp">=</span> <span class="n">exp</span><span class="bp">.</span><span class="n">abs</span> <span class="n">s</span> <span class="n">e&#39;</span><span class="o">)</span> <span class="bp">||</span> <span class="n">is_subterm</span> <span class="n">e&#39;</span>
</pre></div>

#### [ Patrick Thomas (Jan 03 2019 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Induction/near/154270926):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> Cool. Could something similar be done for the set of all lambda terms?</p>


{% endraw %}
