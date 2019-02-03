---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/11881overlappingcasesandwellfoundedness.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [overlapping cases and well-foundedness](https://leanprover-community.github.io/archive/113489newmembers/11881overlappingcasesandwellfoundedness.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mark Dickinson (Oct 21 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/overlapping%20cases%20and%20well-foundedness/near/136220983):
<p>I'm trying to define a simple <code>ℕ → ℕ → ℕ</code> function using well-founded recursion. At top-level, I'm splitting on cases, and those cases overlap:</p>

#### [ Mark Dickinson (Oct 21 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/overlapping%20cases%20and%20well-foundedness/near/136221041):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">isqrt_inner</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="bp">_</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="mi">1</span> <span class="bp">_</span> <span class="o">:=</span> <span class="mi">1</span>
<span class="bp">|</span> <span class="n">b</span> <span class="n">n</span> <span class="o">:=</span>
    <span class="k">let</span> <span class="n">k</span> <span class="o">:=</span> <span class="n">shiftr</span> <span class="n">b</span> <span class="mi">1</span> <span class="k">in</span>
    <span class="k">let</span> <span class="n">a</span> <span class="o">:=</span> <span class="k">have</span> <span class="n">b</span> <span class="bp">-</span> <span class="n">k</span> <span class="bp">&lt;</span> <span class="n">b</span><span class="o">,</span> <span class="k">from</span> <span class="n">sorry</span><span class="o">,</span>
                    <span class="n">isqrt_inner</span> <span class="o">(</span><span class="n">b</span> <span class="bp">-</span> <span class="n">k</span><span class="o">)</span> <span class="o">(</span><span class="n">shiftr</span> <span class="n">n</span> <span class="o">(</span><span class="mi">2</span><span class="bp">*</span><span class="n">k</span><span class="o">))</span> <span class="k">in</span>
    <span class="n">shiftl</span> <span class="n">a</span> <span class="o">(</span><span class="n">k</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">shiftr</span> <span class="n">n</span> <span class="o">(</span><span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="bp">/</span> <span class="n">a</span>
</pre></div>


<p>Question: how would I go about replacing the <code>sorry</code> here? I need to be able to use the hypotheses that <code>b</code> is neither <code>0</code> nor <code>1</code>, but I'm not sure how to get at those.</p>

#### [ Kenny Lau (Oct 21 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/overlapping%20cases%20and%20well-foundedness/near/136221179):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">isqrt_inner</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="bp">_</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="mi">1</span> <span class="bp">_</span> <span class="o">:=</span> <span class="mi">1</span>
<span class="bp">|</span> <span class="n">b</span><span class="bp">@</span><span class="o">(</span><span class="n">p</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span> <span class="n">n</span> <span class="o">:=</span>
    <span class="k">let</span> <span class="n">k</span> <span class="o">:=</span> <span class="n">shiftr</span> <span class="n">b</span> <span class="mi">1</span> <span class="k">in</span>
    <span class="k">let</span> <span class="n">a</span> <span class="o">:=</span> <span class="k">have</span> <span class="n">b</span> <span class="bp">-</span> <span class="n">k</span> <span class="bp">&lt;</span> <span class="n">b</span><span class="o">,</span> <span class="k">from</span> <span class="bp">_</span><span class="o">,</span>
                    <span class="n">isqrt_inner</span> <span class="o">(</span><span class="n">b</span> <span class="bp">-</span> <span class="n">k</span><span class="o">)</span> <span class="o">(</span><span class="n">shiftr</span> <span class="n">n</span> <span class="o">(</span><span class="mi">2</span><span class="bp">*</span><span class="n">k</span><span class="o">))</span> <span class="k">in</span>
    <span class="n">shiftl</span> <span class="n">a</span> <span class="o">(</span><span class="n">k</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">shiftr</span> <span class="n">n</span> <span class="o">(</span><span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="bp">/</span> <span class="n">a</span>
</pre></div>

#### [ Mark Dickinson (Oct 21 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/overlapping%20cases%20and%20well-foundedness/near/136221244):
<p>Beautiful! Thank you.</p>


{% endraw %}
