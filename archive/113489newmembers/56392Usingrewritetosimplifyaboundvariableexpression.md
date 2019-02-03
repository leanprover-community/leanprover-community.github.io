---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/56392Usingrewritetosimplifyaboundvariableexpression.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Using rewrite to simplify a bound variable expression](https://leanprover-community.github.io/archive/113489newmembers/56392Usingrewritetosimplifyaboundvariableexpression.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Ken Roe (Aug 06 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950190):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">fsimp3</span> <span class="o">{</span> <span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">}</span> <span class="o">:</span> <span class="n">x</span><span class="bp">=</span><span class="mi">0</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intro</span><span class="o">,</span> <span class="n">unfold</span> <span class="n">f</span><span class="o">,</span> <span class="n">rw</span> <span class="n">a</span>
<span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">fsimp4</span> <span class="o">{</span><span class="n">e</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">}</span> <span class="o">:</span> <span class="n">e</span><span class="bp">=</span><span class="mi">0</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">x</span><span class="bp">+</span><span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span><span class="bp">=</span><span class="mi">1</span><span class="bp">+</span><span class="n">x</span><span class="o">)</span><span class="bp">=</span><span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="mi">1</span><span class="bp">=</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intro</span><span class="o">,</span>
    <span class="n">rewrite</span> <span class="n">fsimp3</span><span class="o">,</span> <span class="n">simp</span>
<span class="kn">end</span>
</pre></div>


<p>How do I get the "rewrite fsimp3" tactic to work in the "fsimp4" proof?</p>

#### [ Scott Morrison (Aug 06 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950208):
<p>Probably use <code>conv</code>. Do you want to post an MWE?</p>

#### [ Ken Roe (Aug 06 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950318):
<p>Go ahead and post</p>

#### [ Scott Morrison (Aug 06 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950372):
<p>No, I was suggesting that _you_ post a minimal example that shows the problem --- in particular you haven't included the definition of <code>f</code>!</p>

#### [ Scott Morrison (Aug 06 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950374):
<p>I think <code>def f (x : ℕ) := x + 1</code> probably serves your purpose.</p>

#### [ Mario Carneiro (Aug 06 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950425):
<p><code>rw</code> does not work under a binder. You can either use <code>simp</code> instead, or use <code>conv</code> or <code>funext</code> to enter the binder</p>

#### [ Reid Barton (Aug 06 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950432):
<p>For conv, see <a href="https://github.com/leanprover/mathlib/blob/master/docs/extras/conv.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/extras/conv.md">https://github.com/leanprover/mathlib/blob/master/docs/extras/conv.md</a></p>

#### [ Ken Roe (Aug 06 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950433):
<p>Oops--Missed that def</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">f</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span> <span class="n">x</span><span class="bp">+</span><span class="mi">1</span>

<span class="kn">theorem</span> <span class="n">fsimp3</span> <span class="o">{</span> <span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">}</span> <span class="o">:</span> <span class="n">x</span><span class="bp">=</span><span class="mi">0</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intro</span><span class="o">,</span> <span class="n">unfold</span> <span class="n">f</span><span class="o">,</span> <span class="n">rw</span> <span class="n">a</span>
<span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">fsimp4</span> <span class="o">{</span><span class="n">e</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">}</span> <span class="o">:</span> <span class="n">e</span><span class="bp">=</span><span class="mi">0</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">x</span><span class="bp">+</span><span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span><span class="bp">=</span><span class="mi">1</span><span class="bp">+</span><span class="n">x</span><span class="o">)</span><span class="bp">=</span><span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="mi">1</span><span class="bp">=</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intro</span><span class="o">,</span>
    <span class="n">rewrite</span> <span class="n">fsimp3</span><span class="o">,</span> <span class="n">simp</span>
<span class="kn">end</span>
</pre></div>

#### [ Scott Morrison (Aug 06 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950482):
<p>I'm pretty confused how you intend to do anything using <code>rw fsimp3</code>, even under the binder.</p>

#### [ Scott Morrison (Aug 06 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950491):
<p>You've only got <code>e=0</code>, but now want to say something about all <code>x</code>?</p>

#### [ Ken Roe (Aug 06 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950780):
<p>It looks like conv fails:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">fsimp4</span> <span class="o">{</span><span class="n">e</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">}</span> <span class="o">:</span> <span class="n">e</span><span class="bp">=</span><span class="mi">0</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">x</span><span class="bp">+</span><span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span><span class="bp">=</span><span class="mi">1</span><span class="bp">+</span><span class="n">x</span><span class="o">)</span><span class="bp">=</span><span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="mi">1</span><span class="bp">=</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intro</span><span class="o">,</span> <span class="n">simp</span><span class="o">,</span> <span class="n">conv</span>
    <span class="k">begin</span>
        <span class="n">to_lhs</span><span class="o">,</span>
        <span class="n">funext</span><span class="o">,</span>
        <span class="n">rw</span> <span class="n">fsimp3</span><span class="o">,</span> <span class="n">reflexivity</span><span class="o">,</span>
    <span class="kn">end</span>
<span class="kn">end</span>
</pre></div>


<p>I get the error:</p>
<div class="codehilite"><pre><span></span><span class="n">convert</span> <span class="n">tactic</span> <span class="n">failed</span><span class="o">,</span> <span class="n">there</span> <span class="n">are</span> <span class="n">unsolved</span> <span class="n">goals</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">e</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="n">a</span> <span class="o">:</span> <span class="n">e</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">,</span>
<span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span>
<span class="err">⊢</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span>
</pre></div>

#### [ Reid Barton (Aug 06 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950786):
<p>That's because, as Scott pointed out, what you're trying to prove is not true</p>

#### [ Ken Roe (Aug 06 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950908):
<p>Actually, I found the error:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">fsimp4</span> <span class="o">{</span><span class="n">e</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">}</span> <span class="o">:</span> <span class="n">e</span><span class="bp">=</span><span class="mi">0</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">x</span><span class="bp">+</span><span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span><span class="bp">=</span><span class="mi">1</span><span class="bp">+</span><span class="n">x</span><span class="o">)</span> <span class="n">e</span><span class="bp">=</span><span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="mi">1</span><span class="bp">=</span><span class="mi">1</span><span class="o">)</span> <span class="n">e</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intro</span><span class="o">,</span> <span class="n">conv</span>
    <span class="k">begin</span>
        <span class="n">to_lhs</span><span class="o">,</span>
        <span class="n">simp</span><span class="o">,</span> <span class="n">rw</span> <span class="n">a</span><span class="o">,</span>
        <span class="n">funext</span><span class="o">,</span>
        <span class="n">rw</span> <span class="n">fsimp3</span><span class="o">,</span> <span class="n">skip</span><span class="o">,</span> <span class="n">reflexivity</span>
    <span class="kn">end</span>
<span class="kn">end</span>
</pre></div>


<p>However, the error I got is confusing.  The "x=0" got changed to "x" on the screen in the message.</p>

#### [ Mario Carneiro (Aug 06 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130951440):
<p>this proof attempt is not valid for the same reason as before. You can't try to prove the functions are equal because they aren't. You can only prove that the functions <em>evaluated at <code>e</code></em> are equal, so you need to do beta reduction first (using <code>dsimp</code>) and then try to prove it</p>


{% endraw %}
