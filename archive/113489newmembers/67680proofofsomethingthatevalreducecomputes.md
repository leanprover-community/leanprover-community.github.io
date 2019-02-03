---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/67680proofofsomethingthatevalreducecomputes.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [proof of something that #eval / #reduce computes](https://leanprover-community.github.io/archive/113489newmembers/67680proofofsomethingthatevalreducecomputes.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Bryan Gin-ge Chen (Sep 21 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134343915):
<p>If I have:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finset</span>
<span class="kn">open</span> <span class="n">finset</span>
<span class="bp">#</span><span class="kn">eval</span> <span class="o">({</span><span class="mi">0</span><span class="o">,</span><span class="mi">1</span><span class="o">,</span><span class="mi">2</span><span class="o">}</span> <span class="err">⊆</span> <span class="n">range</span> <span class="mi">4</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span> <span class="c1">-- tt</span>
<span class="bp">#</span><span class="n">reduce</span> <span class="o">({</span><span class="mi">0</span><span class="o">,</span><span class="mi">1</span><span class="o">,</span><span class="mi">2</span><span class="o">}</span> <span class="err">⊆</span> <span class="n">range</span> <span class="mi">4</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span> <span class="c1">-- tt</span>
</pre></div>


<p>So lean clearly knows that this fact is true. How can I get lean to give me a proof of (something of the type) <code>{0,1,2}  ⊆ range 4</code> that I can then feed into some other function that takes that as a hypothesis? [Was this what <code>esimp</code> did in lean 2?]</p>

#### [ Kevin Buzzard (Sep 21 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134344507):
<p>My guess is that dec_trivial will work</p>

#### [ Kevin Buzzard (Sep 21 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134344516):
<p>you can't push a random Prop into bool, it has to be decidable. And if it's decidable then <code>dec_trivial</code> should decide it</p>

#### [ Kevin Buzzard (Sep 21 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134344547):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finset</span>
<span class="kn">open</span> <span class="n">finset</span>
<span class="kn">lemma</span> <span class="n">XYZ</span> <span class="o">:</span> <span class="o">{</span><span class="mi">0</span><span class="o">,</span><span class="mi">1</span><span class="o">,</span><span class="mi">2</span><span class="o">}</span> <span class="err">⊆</span> <span class="n">range</span> <span class="mi">4</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
</pre></div>

#### [ Kevin Buzzard (Sep 21 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134344589):
<p>1 year ago I would have just assumed it was magic</p>

#### [ Kevin Buzzard (Sep 21 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134344595):
<p>My eyes have been opened this year to how mathematics actually works</p>

#### [ Bryan Gin-ge Chen (Sep 21 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134344599):
<p>Great, that does make a lot of sense in hindsight. I've been using <code>dec_trivial</code> as a hammer for nat things without really thinking about what it does.</p>

#### [ Kevin Buzzard (Sep 21 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134344634):
<p>I also found a good explanation of why the reals don't have decidable equality</p>

#### [ Kevin Buzzard (Sep 21 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134344685):
<p><a href="https://mathoverflow.net/a/44933/1384" target="_blank" title="https://mathoverflow.net/a/44933/1384">https://mathoverflow.net/a/44933/1384</a></p>

#### [ Kevin Buzzard (Sep 21 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134344694):
<p>Those two real numbers have been verified to be equal to 20000 decimal places, but because there is no algorithm for checking equality of real numbers, you can't use <code>dec_trivial</code> to prove it</p>

#### [ Mario Carneiro (Sep 21 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134344904):
<p>Of course, from the way the claim is worded it's clear that everyone thinks it's true, like the RH is true. Physicists are happy with "equal to 100 decimals =&gt; equal"</p>

#### [ Chris Hughes (Sep 21 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134386256):
<p>Are they computable reals though? Is the limit of a real Cauchy sequence computable?</p>

#### [ Kenny Lau (Sep 21 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134386498):
<p>not every.</p>

#### [ Mario Carneiro (Sep 21 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134388931):
<p>Yes, both those expressions are computable. Basically anything you can write down with a formula composing the usual constructions on reals is computable. The main exception is if you are writing something self referential or making explicit references to turing machines or other turing complete notions, and most math doesn't touch this.</p>

#### [ Mario Carneiro (Sep 21 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proof%20of%20something%20that%20%23eval%20/%20%23reduce%20computes/near/134388942):
<p>But comparing computable numbers is also undecidable</p>


{% endraw %}
