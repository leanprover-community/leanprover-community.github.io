---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/01043isthereanybetterway.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [is there any better way?](https://leanprover-community.github.io/archive/116395maths/01043isthereanybetterway.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Truong Nguyen (Sep 03 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271618):
<p>Hi Everybody,<br>
I this this way of proving 1 &lt; 4 is not a smart way. Do you have any better way for doing this. Thanks</p>
<p>theorem oiooo : 1 &lt; 4 :=<br>
begin<br>
have thh: 1 &lt; nat.succ 1, from nat.lt_succ_self 1,<br>
have hht6: nat.succ 1 &lt; 3, from nat.lt_succ_self 2,<br>
have ht5: 3 &lt; 4, from nat.lt_succ_self 3,<br>
have tg: 1 &lt; 3, from nat.lt_trans thh hht6,<br>
show 1 &lt; 4, from nat.lt_trans tg ht5<br>
end</p>

#### [ Johan Commelin (Sep 03 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271642):
<p>You can format code by putting three backticks before and after it:</p>
<div class="codehilite"><pre><span></span>```lean
Your code goes here
```
</pre></div>

#### [ Kenny Lau (Sep 03 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271717):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">oiooo</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">&lt;</span> <span class="mi">4</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
</pre></div>

#### [ Kenny Lau (Sep 03 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271728):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">oiooo</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">&lt;</span> <span class="mi">4</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">repeat</span> <span class="o">{</span><span class="n">constructor</span><span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Sep 03 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271729):
<p>rofl</p>

#### [ Kevin Buzzard (Sep 03 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271731):
<p>that's some obscure proof</p>

#### [ Kevin Buzzard (Sep 03 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271750):
<p><span class="user-mention" data-user-id="125610">@Truong Nguyen</span> the correct proof is <code>dec_trivial</code> -- inequalities are decidable on the naturals</p>

#### [ Kevin Buzzard (Sep 03 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271800):
<p>Unfortunately the reals do not have decidable equality, so for them you have to prove stuff like 1 &lt; 4 using <code>norm_num</code></p>

#### [ Johan Commelin (Sep 03 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271865):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">tidy</span>

<span class="kn">theorem</span> <span class="n">oiooo</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">&lt;</span> <span class="mi">4</span> <span class="o">:=</span> <span class="o">{</span><span class="bp">!</span> <span class="bp">_</span> <span class="bp">!</span><span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Sep 03 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271869):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">oiooo</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">&lt;</span> <span class="mi">4</span> <span class="o">:=</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">one_lt_bit0</span> <span class="err">$</span> <span class="n">ne</span><span class="bp">.</span><span class="n">symm</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero_ne_bit0</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">one_ne_zero</span>
</pre></div>

#### [ Johan Commelin (Sep 03 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271880):
<p>The <code>{! _ !}</code> is called a goal. You can fill it in in two ways: (1) Click the light bulb. (2) Put your cursor in the goal and hit <code>Ctrl-.</code></p>

#### [ Johan Commelin (Sep 03 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271887):
<p>Choose the option "Use <code>tidy</code> to fill in the goal."</p>

#### [ Johan Commelin (Sep 03 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133271898):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">oiooo</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">&lt;</span> <span class="mi">4</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">tidy</span>
</pre></div>


<p>will also work.</p>

#### [ Truong Nguyen (Sep 03 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133273683):
<p>Oh, Thank you.<br>
How about this one: </p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">tyyy</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span><span class="o">:</span> <span class="bp">ℕ</span> <span class="o">):</span>
<span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="err">%</span> <span class="mi">4</span> <span class="bp">=</span> <span class="o">(</span><span class="n">a</span> <span class="err">%</span> <span class="mi">4</span> <span class="bp">+</span> <span class="n">b</span> <span class="err">%</span> <span class="mi">4</span><span class="o">)</span> <span class="err">%</span> <span class="mi">4</span> <span class="o">:=</span>
<span class="n">sorry</span>
</pre></div>

#### [ Bryan Gin-ge Chen (Sep 03 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133274209):
<p>This is part of the way there:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">zmod</span><span class="o">,</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>

<span class="kn">theorem</span> <span class="n">tyyy0</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span><span class="o">:</span> <span class="bp">ℕ</span> <span class="o">):</span>
<span class="o">((</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">zmod</span> <span class="mi">4</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">zmod</span> <span class="mi">4</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">zmod</span> <span class="mi">4</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">ring</span>
</pre></div>


<p>There should be some way to use <code>zmod.cast_mod_nat</code> but I'm stuck.</p>

#### [ Truong Nguyen (Sep 03 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133274358):
<p>I am stuck too.</p>

#### [ Reid Barton (Sep 03 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133274407):
<p>I think the original tyyy is a lemma somewhere in mathlib</p>

#### [ Reid Barton (Sep 03 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133274562):
<p>There's <code>int.add_mod_mod</code> and <code>int.mod_add_mod</code></p>

#### [ Reid Barton (Sep 03 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133274692):
<p>Which you can combine to get what you want</p>

#### [ Chris Hughes (Sep 03 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20there%20any%20better%20way%3F/near/133274701):
<p>I think this should work</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">tyyy</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span><span class="o">:</span> <span class="bp">ℕ</span> <span class="o">):</span>
<span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="err">%</span> <span class="mi">4</span> <span class="bp">=</span> <span class="o">(</span><span class="n">a</span> <span class="err">%</span> <span class="mi">4</span> <span class="bp">+</span> <span class="n">b</span> <span class="err">%</span> <span class="mi">4</span><span class="o">)</span> <span class="err">%</span> <span class="mi">4</span> <span class="o">:=</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">modeq_add</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">mod_mod</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">))</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">mod_mod</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">))</span>
</pre></div>


{% endraw %}
