---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/28310dectrivialfails.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [dec_trivial fails](https://leanprover-community.github.io/archive/113489newmembers/28310dectrivialfails.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Oct 30 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136806175):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">rat</span>

<span class="n">def</span> <span class="n">rat</span><span class="bp">.</span><span class="n">sqrt</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℚ</span> <span class="o">:=</span>
<span class="n">rat</span><span class="bp">.</span><span class="n">mk</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">sqrt</span> <span class="err">$</span> <span class="n">int</span><span class="bp">.</span><span class="n">to_nat</span> <span class="n">q</span><span class="bp">.</span><span class="n">num</span><span class="o">)</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">sqrt</span> <span class="n">q</span><span class="bp">.</span><span class="n">denom</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">rat</span><span class="bp">.</span><span class="n">sqrt</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">dec_trivial</span> <span class="c1">-- fails</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">rat</span><span class="bp">.</span><span class="n">sqrt</span> <span class="mi">2</span> <span class="c1">-- 1</span>
</pre></div>

#### [ Kenny Lau (Oct 30 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136806191):
<p>Why does <code>dec_trivial</code> fail?</p>

#### [ Kenny Lau (Oct 30 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136806337):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span></p>

#### [ Kenny Lau (Oct 30 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136807285):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sqrt</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">to_nat</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">dec_trivial</span> <span class="c1">-- fails</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sqrt</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">dec_trivial</span> <span class="c1">-- fails</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">rat</span><span class="bp">.</span><span class="n">mk</span> <span class="mi">1</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">dec_trivial</span> <span class="c1">-- succeeds</span>
</pre></div>

#### [ Kenny Lau (Oct 30 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136807385):
<p>ok so the problem boils down to this</p>

#### [ Kenny Lau (Oct 30 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136807389):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">sqrt</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sqrt</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">dec_trivial</span> <span class="c1">-- fails</span>
</pre></div>

#### [ Scott Olson (Oct 30 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136807651):
<p>Looks like it goes <code>nat.sqrt -&gt; nat.size -&gt; nat.binary_rec</code> and <code>binary_rec</code> reduces very slowly, so <code>dec_trivial</code> gives up</p>

#### [ Kevin Buzzard (Oct 30 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136807739):
<p>From <code>data.nat.sqrt</code>:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">sqrt</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="k">match</span> <span class="n">size</span> <span class="n">n</span> <span class="k">with</span>
<span class="bp">|</span> <span class="mi">0</span>      <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="n">succ</span> <span class="n">s</span> <span class="o">:=</span> <span class="n">sqrt_aux</span> <span class="o">(</span><span class="n">shiftl</span> <span class="mi">1</span> <span class="o">(</span><span class="n">bit0</span> <span class="o">(</span><span class="n">div2</span> <span class="n">s</span><span class="o">)))</span> <span class="mi">0</span> <span class="n">n</span>
<span class="kn">end</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">sqrt</span>

<span class="kn">open</span> <span class="n">nat</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">size</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="c1">-- 1</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">size</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="c1">-- ℕ</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sqrt</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">dec_trivial</span> <span class="c1">-- fails</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">sqrt_aux</span> <span class="o">(</span><span class="n">shiftl</span> <span class="mi">1</span> <span class="o">(</span><span class="n">bit0</span> <span class="o">(</span><span class="n">div2</span> <span class="mi">0</span><span class="o">)))</span> <span class="mi">0</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">dec_trivial</span> <span class="c1">-- works?</span>
</pre></div>

#### [ Kevin Buzzard (Oct 30 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136807780):
<p>Yes Scott has seen the right path -- <code>example : size 1 = 1 := dec_trivial</code> fails</p>

#### [ Scott Olson (Oct 30 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136807877):
<p>I get failure for the <code>sqrt_aux</code> line</p>

#### [ Kevin Buzzard (Oct 30 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136807887):
<p>Did you open nat?</p>

#### [ Scott Olson (Oct 30 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136807888):
<p>Yes</p>

#### [ Kenny Lau (Oct 30 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808002):
<p>hmm</p>

#### [ Kenny Lau (Oct 30 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808015):
<p>this is troublesome</p>

#### [ Kenny Lau (Oct 30 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808032):
<p>because we can't change <code>nat.binary_rec</code></p>

#### [ Kenny Lau (Oct 30 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808036):
<p>well maybe we can write <code>nat.binary_rec'</code> just like we do other functions</p>

#### [ Kevin Buzzard (Oct 30 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808291):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">binary_rec</span> <span class="mi">0</span> <span class="o">(</span><span class="bp">λ_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">succ</span><span class="o">)</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span> <span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">binary_rec</span><span class="o">,</span>
  <span class="n">split_ifs</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">refl</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>Maybe you can add some sort of decidability instance for <code>size</code>?</p>

#### [ Kevin Buzzard (Oct 30 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808370):
<p>I don't think you need to go down as far as <code>binary_rec</code>.</p>

#### [ Kenny Lau (Oct 30 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808446):
<p>I don't see how we can just add decidability instance.</p>

#### [ Kevin Buzzard (Oct 30 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808451):
<p>You know more about decidability than me.</p>

#### [ Kevin Buzzard (Oct 30 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808459):
<p><code>decidable (size a = b)</code>?</p>

#### [ Kenny Lau (Oct 30 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808465):
<p>that wouldn't be useful</p>

#### [ Kenny Lau (Oct 30 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808470):
<p>because I can have another function that calls <code>size</code></p>

#### [ Kevin Buzzard (Oct 30 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808471):
<p>Or "computability" or something? I have no idea how these things work.</p>

#### [ Kenny Lau (Oct 30 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808498):
<p>I don't see any other solution than rewriting some functions in the chain, but maybe <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> would have some idea</p>

#### [ Kevin Buzzard (Oct 30 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808581):
<p>So what's going on here? You need to make sure that the...kernel? VM? can compute <code>size a</code>?</p>

#### [ Kevin Buzzard (Oct 30 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808629):
<p>I don't really understand how <code>a = b</code> can fail to be proved by <code>dec_trivial</code> (if a and b are explicit computable nats). Equality on nat is decidable, so whatever runs <code>dec_trivial</code> just has to work out what <code>a</code> and <code>b</code> are and then check that they're equal.</p>

#### [ Kevin Buzzard (Oct 30 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808676):
<p>and any nat in Lean is reducible to succ succ ... succ zero</p>

#### [ Kevin Buzzard (Oct 30 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808918):
<p>Aah I understand more about the problem now. <code>#reduce size 1</code> is a deterministic timeout.</p>

#### [ Kevin Buzzard (Oct 30 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136808927):
<p>and then a segfault ;-)</p>

#### [ Kevin Buzzard (Oct 30 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136809025):
<p>[ten seconds later]</p>

#### [ Scott Olson (Oct 30 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136809162):
<p>Yeah, my understanding is <code>dec_trivial</code> should never fail on closed terms, but it gives up when reduction takes too long</p>

#### [ Kevin Buzzard (Oct 30 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136809269):
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">nat</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">binary_rec</span> <span class="mi">0</span> <span class="o">(</span><span class="bp">λ_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">succ</span><span class="o">)</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">binary_rec</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">dec_trivial</span>
<span class="kn">end</span> <span class="c1">-- works</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">binary_rec</span> <span class="mi">0</span> <span class="o">(</span><span class="bp">λ_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">succ</span><span class="o">)</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">exact</span> <span class="n">dec_trivial</span>
<span class="kn">end</span> <span class="c1">-- fails</span>
</pre></div>

#### [ Scott Olson (Oct 30 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136809462):
<p>That does seem a bit... artificial. I wish I knew more about how the reductions worked</p>

#### [ Scott Olson (Oct 30 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136809536):
<p>But I can confirm <code>#reduce binary_rec 0 (λ_ _, succ) 1</code> times out but <code>#reduce</code> on the goal after <code>unfold binary_rec</code> (copy/pasted out with <code>set_option pp.proofs true</code> and <code>set_option pp.implicit true</code>) does give you <code>1</code></p>

#### [ Mario Carneiro (Oct 31 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136814397):
<p>This is because proofs are irreducible by default. I think there is an option for this, I forget the name</p>

#### [ Mario Carneiro (Oct 31 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136814432):
<p>It is almost never necessary to reduce a proof during evaluation, but well founded definitions require recursion on proofs of wellfoundedness</p>

#### [ Kenny Lau (Oct 31 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136814666):
<p>then what should we do?</p>

#### [ Mario Carneiro (Oct 31 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136815767):
<p>give up? This definition is not intended for kernel reduction</p>

#### [ Mario Carneiro (Oct 31 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dec_trivial%20fails/near/136815862):
<p>If you need to calculate these things, you can either use the definition, or if we need larger scale computation we can add another <code>norm_num</code> add-on for this (I really need to make it extensible via annotation...)</p>


{% endraw %}
