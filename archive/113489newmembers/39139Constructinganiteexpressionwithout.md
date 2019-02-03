---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/39139Constructinganiteexpressionwithout.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Constructing an ite expression without %%](https://leanprover-community.github.io/archive/113489newmembers/39139Constructinganiteexpressionwithout.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Ken Roe (Jul 24 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Constructing%20an%20ite%20expression%20without%20%25%25/near/130183355):
<p>I entered the following code to construct an ite expression in a meta def:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">xeval</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">if</span> <span class="n">a</span><span class="bp">=</span><span class="mi">0</span> <span class="k">then</span> <span class="mi">0</span> <span class="k">else</span> <span class="n">b</span><span class="bp">.</span>

<span class="n">def</span> <span class="n">beq_nat</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">tt</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">beq_nat</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">ff</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">ff</span>


<span class="n">meta</span> <span class="n">def</span> <span class="n">evaluate_xeval_helper</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span>
<span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="n">xeval</span> <span class="err">%%</span><span class="n">x</span> <span class="err">%%</span><span class="n">y</span><span class="o">)</span> <span class="o">:=</span>
      <span class="o">(</span><span class="n">app</span> <span class="o">(</span><span class="n">app</span> <span class="o">(</span><span class="n">app</span> <span class="bp">`</span><span class="o">(</span><span class="n">ite</span><span class="o">)</span>
                     <span class="o">(</span><span class="n">app</span> <span class="o">(</span><span class="n">app</span> <span class="bp">`</span><span class="o">(</span><span class="n">beq_nat</span><span class="o">)))</span> <span class="n">x</span> <span class="bp">`</span><span class="o">(</span><span class="mi">0</span><span class="o">))</span>
                     <span class="bp">`</span><span class="o">(</span><span class="mi">0</span><span class="o">))</span>
                     <span class="n">y</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">x</span>
</pre></div>


<p>The word "ite" gets the error</p>
<div class="codehilite"><pre><span></span><span class="n">failed</span> <span class="n">to</span> <span class="n">synthesize</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">for</span>
<span class="n">evaluate_xeval_helper</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span><span class="o">,</span>
<span class="bp">_</span><span class="n">x</span> <span class="o">:</span> <span class="n">list</span> <span class="n">level</span><span class="o">,</span>
<span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">expr</span>
<span class="err">⊢</span> <span class="n">reflected</span> <span class="n">ite</span>
</pre></div>


<p>How do I fix this error?</p>

#### [ Sebastian Ullrich (Jul 25 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Constructing%20an%20ite%20expression%20without%20%25%25/near/130244278):
<p>The error is because the universe parameter of <code>ite</code> could not be inferred. If you use the full quotation</p>
<div class="codehilite"><pre><span></span>`(if beq_nat %%x 0 then (0 : nat) else %%y)
</pre></div>


<p>it should work</p>


{% endraw %}
