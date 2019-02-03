---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/84538intmod.html
---

## Stream: [new members](index.html)
### Topic: [int.mod](84538intmod.html)

---


{% raw %}
#### [ petercommand (Nov 01 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136906477):
<p>Trying to prove <code>int.mod (int.of_nat a_1) ↑p &lt; ↑p</code> in lean, but I wasn't able to unfold int.mod.</p>

#### [ Mario Carneiro (Nov 01 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136906517):
<p>there should be a theorem called <code>int.mod_lt</code> for this</p>

#### [ Mario Carneiro (Nov 01 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136906523):
<p>it is <code>int.mod_lt_of_pos</code> and it isn't true when <code>a_1 = 0</code></p>

#### [ petercommand (Nov 01 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136906589):
<p>I can't find int.mod_lt in C-c C-d</p>

#### [ petercommand (Nov 01 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136906637):
<p>There is nat.mod_lt though</p>

#### [ Johan Commelin (Nov 01 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136906692):
<p><span class="user-mention" data-user-id="127883">@petercommand</span> Welcome! Can you tell if Mario's suggestion works?</p>

#### [ petercommand (Nov 01 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136906699):
<p>no</p>

#### [ Johan Commelin (Nov 01 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136906705):
<p>Ok, can you give a more detailed version of what you want to prove? A "minimal working example" (MWE)</p>

#### [ Johan Commelin (Nov 01 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136906750):
<p>So something of the form</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">foobar</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="err">??</span><span class="o">)</span> <span class="o">(</span><span class="n">a_1</span> <span class="o">:</span> <span class="n">int</span><span class="o">)</span> <span class="o">:</span> <span class="n">int</span><span class="bp">.</span><span class="n">mod</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">of_nat</span> <span class="n">a_1</span><span class="o">)</span> <span class="err">↑</span><span class="n">p</span> <span class="bp">&lt;</span> <span class="err">↑</span><span class="n">p</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ petercommand (Nov 01 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136906810):
<p><code>def test : Π (a b : ℤ) (p : ℕ), (a + b) % p &lt; p := sorry </code></p>

#### [ Johan Commelin (Nov 01 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136906902):
<p>That isn't true if <code>p = 0</code>, right?</p>

#### [ Mario Carneiro (Nov 01 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136906960):
<p>Do you have mathlib? <code>int.mod_lt_of_pos</code> is in <code>data.int.basic</code></p>

#### [ petercommand (Nov 01 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136906989):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>  ah, it should be <code>def test : Π (a b : ℤ) (p : ℕ) (p &gt;= 2), (a + b) % p &lt; p := sorry</code></p>

#### [ petercommand (Nov 01 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907038):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>  Ah..Thanks! I didn't set up mathlib</p>

#### [ petercommand (Nov 01 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907099):
<p>why wasn't I able to unfold <code>int.mod</code> though</p>

#### [ Johan Commelin (Nov 01 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907272):
<p>I guess it is some sort of inductive definition</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907273):
<p><code>int</code> is an inductive type with two constructors. <code>int.mod</code> eats an <code>int</code>, and how it unfolds depends on which constructor you use -- <code>int.mod</code> can't unfold unless it knows which it is.</p>

#### [ petercommand (Nov 01 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907290):
<p>Which, in <code>int.of_nat a_1</code>, is <code>of_nat</code></p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907291):
<p>But on the other hand you probably don't want to be unfolding <code>int.mod</code>. The devs will have made all the infrastructure you need, at least that's the philosophy.</p>

#### [ petercommand (Nov 01 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907296):
<p>True</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907297):
<p>If you post a MWE I can try to help.</p>

#### [ petercommand (Nov 01 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907354):
<p><code>def test : Π (a p : ℕ) (p &gt; 0) , int.mod (int.of_nat a) ↑p &lt; ↑p := sorry </code> something like this</p>

#### [ petercommand (Nov 01 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907408):
<p>Thanks</p>

#### [ petercommand (Nov 01 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907429):
<p>My first MWE wasn't clear, this one should be a bit better</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907479):
<p>the answer appears to be that the exact definition of <code>int.mod</code> uses <code>↑a</code> instead of <code>int.of_nat a</code></p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907498):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">test</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">,</span> <span class="n">int</span><span class="bp">.</span><span class="n">mod</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">of_nat</span> <span class="n">a</span><span class="o">)</span> <span class="err">↑</span><span class="n">p</span> <span class="bp">&lt;</span> <span class="err">↑</span><span class="n">p</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="c1">--  unfold int.mod, -- fails</span>
  <span class="n">change</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">),</span> <span class="n">int</span><span class="bp">.</span><span class="n">mod</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="err">↑</span><span class="n">p</span> <span class="bp">&lt;</span> <span class="err">↑</span><span class="n">p</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">int</span><span class="bp">.</span><span class="n">mod</span><span class="o">,</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Nov 01 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907500):
<p>All the more reason why you shouldn't be unfolding it ;-)</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907578):
<p>I just wrote <code>#check int.mod</code> and then right clicked on <code>int.mod</code> and peeked the actual definition.</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907650):
<p>Of course the two things are definitionally equal: <code>example (a : ℕ) : int.of_nat a = ↑a := rfl </code></p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907654):
<p>But under the hood <code>unfold</code> is using <code>simp</code>, and I think <code>simp</code> can be fussy about not changing things to definitionally equal things.</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907658):
<p>Well, that's my amateur diagnosis anyway.</p>

#### [ Kenny Lau (Nov 01 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907777):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">test</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hp</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">≥</span> <span class="mi">2</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="err">%</span> <span class="n">p</span> <span class="bp">&lt;</span> <span class="n">p</span> <span class="o">:=</span>
<span class="k">match</span> <span class="n">a</span><span class="bp">+</span><span class="n">b</span> <span class="k">with</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">show</span> <span class="err">↑</span><span class="o">(</span><span class="n">n</span><span class="err">%</span><span class="n">p</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">),</span> <span class="k">from</span> <span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_lt_coe_nat_of_lt</span>
    <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">mod_lt</span> <span class="bp">_</span> <span class="o">(</span><span class="n">lt_of_le_of_lt</span> <span class="n">dec_trivial</span> <span class="n">Hp</span><span class="o">))</span>
<span class="bp">|</span> <span class="bp">-</span><span class="o">[</span><span class="mi">1</span><span class="bp">+</span> <span class="n">n</span><span class="o">]</span> <span class="o">:=</span> <span class="k">show</span> <span class="err">↑</span><span class="n">p</span> <span class="bp">+</span> <span class="bp">-</span><span class="o">[</span><span class="mi">1</span><span class="bp">+</span> <span class="n">n</span><span class="err">%</span><span class="n">p</span><span class="o">]</span> <span class="bp">&lt;</span> <span class="err">↑</span><span class="n">p</span><span class="o">,</span> <span class="k">from</span> <span class="n">add_lt_of_le_of_neg</span>
    <span class="o">(</span><span class="n">le_refl</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">neg_succ_lt_zero</span> <span class="o">(</span><span class="n">n</span><span class="err">%</span><span class="n">p</span><span class="o">))</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Nov 01 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907786):
<p>A side comment -- I think <code>test</code> is not quite what you want to prove (AFK)</p>

#### [ Kenny Lau (Nov 01 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907800):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">test</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hp</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="err">%</span> <span class="n">p</span> <span class="bp">&lt;</span> <span class="n">p</span> <span class="o">:=</span>
<span class="k">match</span> <span class="n">a</span><span class="bp">+</span><span class="n">b</span> <span class="k">with</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">show</span> <span class="err">↑</span><span class="o">(</span><span class="n">n</span><span class="err">%</span><span class="n">p</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">),</span> <span class="k">from</span> <span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_lt_coe_nat_of_lt</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">mod_lt</span> <span class="bp">_</span> <span class="n">Hp</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">-</span><span class="o">[</span><span class="mi">1</span><span class="bp">+</span> <span class="n">n</span><span class="o">]</span> <span class="o">:=</span> <span class="k">show</span> <span class="err">↑</span><span class="n">p</span> <span class="bp">+</span> <span class="bp">-</span><span class="o">[</span><span class="mi">1</span><span class="bp">+</span> <span class="n">n</span><span class="err">%</span><span class="n">p</span><span class="o">]</span> <span class="bp">&lt;</span> <span class="err">↑</span><span class="n">p</span><span class="o">,</span> <span class="k">from</span> <span class="n">add_lt_of_le_of_neg</span>
    <span class="o">(</span><span class="n">le_refl</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">neg_succ_lt_zero</span> <span class="o">(</span><span class="n">n</span><span class="err">%</span><span class="n">p</span><span class="o">))</span>
<span class="kn">end</span>
</pre></div>


<p>(I just noticed that you changed the condition again)</p>

#### [ petercommand (Nov 01 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907877):
<p>hmm, this is quite annoying..I thought <code>int.mod</code> was directly matching on the constructor</p>

#### [ petercommand (Nov 01 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907942):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> thanks</p>

#### [ Kenny Lau (Nov 01 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907960):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">test</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hp</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="err">%</span> <span class="n">p</span> <span class="bp">&lt;</span> <span class="n">p</span> <span class="o">:=</span>
<span class="k">match</span> <span class="n">a</span><span class="bp">+</span><span class="n">b</span> <span class="k">with</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">show</span> <span class="err">↑</span><span class="o">(</span><span class="n">n</span><span class="err">%</span><span class="n">p</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">),</span> <span class="k">from</span> <span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_lt_coe_nat_of_lt</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">mod_lt</span> <span class="bp">_</span> <span class="n">Hp</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">-</span><span class="o">[</span><span class="mi">1</span><span class="bp">+</span> <span class="n">n</span><span class="o">]</span> <span class="o">:=</span> <span class="k">show</span> <span class="err">↑</span><span class="n">p</span> <span class="bp">+</span> <span class="bp">-</span><span class="o">[</span><span class="mi">1</span><span class="bp">+</span> <span class="n">n</span><span class="err">%</span><span class="n">p</span><span class="o">]</span> <span class="bp">&lt;</span> <span class="err">↑</span><span class="n">p</span><span class="o">,</span> <span class="k">from</span> <span class="n">int</span><span class="bp">.</span><span class="n">lt</span><span class="bp">.</span><span class="n">intro</span> <span class="o">(</span><span class="n">neg_add_cancel_right</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span><span class="err">%</span><span class="n">p</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Nov 01 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907961):
<p>it is</p>

#### [ Kenny Lau (Nov 01 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907966):
<p>oh, and it isn't <code>def</code></p>

#### [ Kenny Lau (Nov 01 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136907967):
<p>it's <code>theorem</code></p>

#### [ Kenny Lau (Nov 01 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908008):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hp</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="err">%</span> <span class="n">p</span> <span class="bp">&lt;</span> <span class="n">p</span> <span class="o">:=</span>
<span class="k">match</span> <span class="n">a</span><span class="bp">+</span><span class="n">b</span> <span class="k">with</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">show</span> <span class="err">↑</span><span class="o">(</span><span class="n">n</span><span class="err">%</span><span class="n">p</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">),</span> <span class="k">from</span> <span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_lt_coe_nat_of_lt</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">mod_lt</span> <span class="bp">_</span> <span class="n">Hp</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">-</span><span class="o">[</span><span class="mi">1</span><span class="bp">+</span> <span class="n">n</span><span class="o">]</span> <span class="o">:=</span> <span class="k">show</span> <span class="err">↑</span><span class="n">p</span> <span class="bp">+</span> <span class="bp">-</span><span class="o">[</span><span class="mi">1</span><span class="bp">+</span> <span class="n">n</span><span class="err">%</span><span class="n">p</span><span class="o">]</span> <span class="bp">&lt;</span> <span class="err">↑</span><span class="n">p</span><span class="o">,</span> <span class="k">from</span> <span class="n">int</span><span class="bp">.</span><span class="n">lt</span><span class="bp">.</span><span class="n">intro</span> <span class="o">(</span><span class="n">neg_add_cancel_right</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span><span class="err">%</span><span class="n">p</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span>
<span class="kn">end</span>
</pre></div>

#### [ petercommand (Nov 01 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908019):
<p>aren't they synonyms?</p>

#### [ Kenny Lau (Nov 01 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908020):
<p>no</p>

#### [ petercommand (Nov 01 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908028):
<p>what's different between def and thoerem?</p>

#### [ Kenny Lau (Nov 01 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908031):
<p>def is data</p>

#### [ Kenny Lau (Nov 01 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908032):
<p>theorem is proof</p>

#### [ petercommand (Nov 01 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908082):
<p>I mean, semantically, are they different?</p>

#### [ Kenny Lau (Nov 01 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908095):
<p>yes</p>

#### [ petercommand (Nov 01 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908114):
<p>proof irrelevance?</p>

#### [ petercommand (Nov 01 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908179):
<p><a href="https://leanprover.github.io/theorem_proving_in_lean/propositions_and_proofs.html" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/propositions_and_proofs.html">https://leanprover.github.io/theorem_proving_in_lean/propositions_and_proofs.html</a><br>
Ah, it says that <br>
<code>by proof irrelevance, any two proofs of that theorem are definitionally equal.</code></p>

#### [ Kenny Lau (Nov 01 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908184):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">x</span> <span class="o">:</span> <span class="n">nat</span> <span class="o">:=</span> <span class="mi">5</span>
<span class="n">def</span> <span class="n">test</span> <span class="o">:</span> <span class="n">x</span><span class="bp">=</span><span class="mi">5</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kenny Lau (Nov 01 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908186):
<blockquote>
<p><a href="https://leanprover.github.io/theorem_proving_in_lean/propositions_and_proofs.html" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/propositions_and_proofs.html">https://leanprover.github.io/theorem_proving_in_lean/propositions_and_proofs.html</a><br>
Ah, it says that <br>
<code>by proof irrelevance, any two proofs of that theorem are definitionally equal.</code></p>
</blockquote>
<p>that's irrelevant</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908209):
<p>Kenny, independent of that def/theorem business, what's happening below? <span class="user-mention" data-user-id="127883">@petercommand</span> 's original formulation of the MWE has something wrong with it I think:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">test</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">,</span> <span class="n">int</span><span class="bp">.</span><span class="n">mod</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">of_nat</span> <span class="n">a</span><span class="o">)</span> <span class="err">↑</span><span class="n">p</span> <span class="bp">&lt;</span> <span class="err">↑</span><span class="n">p</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">b</span><span class="o">,</span> <span class="c1">-- ??</span>
  <span class="n">intro</span> <span class="n">p</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">HP</span><span class="o">,</span>
  <span class="c1">-- ⊢ int.mod (int.of_nat a) ↑p &lt; ↑p</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Nov 01 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908253):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">test</span> <span class="o">:</span> <span class="mi">5</span><span class="bp">=</span><span class="mi">5</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">#</span><span class="kn">print</span> <span class="kn">prefix</span> <span class="n">test</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">test : 5 = 5</span>
<span class="cm">test.equations._eqn_1 : test = rfl</span>
<span class="cm">-/</span>

<span class="kn">theorem</span> <span class="n">test2</span> <span class="o">:</span> <span class="mi">5</span><span class="bp">=</span><span class="mi">5</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">#</span><span class="kn">print</span> <span class="kn">prefix</span> <span class="n">test2</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">test2 : 5 = 5</span>
<span class="cm">-/</span>
</pre></div>

#### [ Kenny Lau (Nov 01 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908274):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> lol the conditions keep changing</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908278):
<p>I think the <code>p</code> in <code>forall p</code> isn't the same as the <code>p</code> in <code>p &gt; 0</code>.</p>

#### [ Kenny Lau (Nov 01 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908282):
<p><span class="user-mention" data-user-id="127883">@petercommand</span> can you make up your mind?</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908284):
<p>I never changed anything, I just copied his MWE.</p>

#### [ Kenny Lau (Nov 01 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908289):
<blockquote>
<p>I think the <code>p</code> in <code>forall p</code> isn't the same as the <code>p</code> in <code>p &gt; 0</code>.</p>
</blockquote>
<p>I think it's the same</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908332):
<p>Did you look at my tactic mode post?</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908334):
<p>There's an extra nat</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908337):
<p><code>-- ??</code></p>

#### [ Kenny Lau (Nov 01 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908349):
<p>I don't know why you have 4 <code>intro</code>s</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908354):
<p>because Lean is asking for 4. That's the point I'm trying to make</p>

#### [ Kenny Lau (Nov 01 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908359):
<p>what do you mean Lean is asking for 4</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908366):
<p>What do you mean? The function wants 4 inputs</p>

#### [ Kenny Lau (Nov 01 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908367):
<p>that's spooky</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908369):
<p>Must be Halloween.</p>

#### [ Kenny Lau (Nov 01 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908412):
<p>oh!</p>

#### [ petercommand (Nov 01 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908413):
<p>o.o</p>

#### [ Kenny Lau (Nov 01 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908420):
<p>lol</p>

#### [ Kenny Lau (Nov 01 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908427):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">,</span> <span class="n">int</span><span class="bp">.</span><span class="n">mod</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">of_nat</span> <span class="n">a</span><span class="o">)</span> <span class="err">↑</span><span class="n">p</span> <span class="bp">&lt;</span> <span class="err">↑</span><span class="n">p</span> <span class="o">:=</span>
</pre></div>

#### [ Kenny Lau (Nov 01 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908428):
<p><code>&gt;</code> is a binder or something</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908432):
<p>right</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908489):
<p><span class="user-mention" data-user-id="127883">@petercommand</span> this is fine: <code>theorem test : ∀ (a p : ℕ), (p &gt; 0) → int.mod (int.of_nat a) ↑p &lt; ↑p :=</code></p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908504):
<p>but <code>(p &gt; 0)</code> before the comma gets interpreted as "and there's another variable p, different to the p you just mentioned"</p>

#### [ Kenny Lau (Nov 01 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908516):
<p>I don't think <span class="user-mention" data-user-id="127883">@petercommand</span> has tested his "MWE" before posting</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908518):
<p><code>def test' : Π (a : ℕ) (p &gt; 0) , int.mod (int.of_nat a) ↑p &lt; ↑p := </code> is OK</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908521):
<p>I just made it a bit more minimal, that's all ;-)</p>

#### [ petercommand (Nov 01 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908569):
<blockquote>
<p>I don't think <span class="user-mention" data-user-id="127883">@petercommand</span> has tested his "MWE" before posting</p>
</blockquote>
<p>Yeah, I should've tested the MWEs o.o Thought that was simple enough</p>

#### [ Kenny Lau (Nov 01 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908575):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test&#39;</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="n">int</span><span class="bp">.</span><span class="n">mod</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">of_nat</span> <span class="n">a</span><span class="o">)</span> <span class="err">↑</span><span class="n">p</span> <span class="bp">&lt;</span> <span class="err">↑</span><span class="n">p</span> <span class="o">:=</span>
<span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_lt_coe_nat_of_lt</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">mod_lt</span> <span class="bp">_</span> <span class="n">H</span><span class="o">)</span>
</pre></div>

#### [ petercommand (Nov 01 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908636):
<p>Hmm, actually, I tested the MWEs, but didn't discover that I got one more variable</p>

#### [ petercommand (Nov 01 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908637):
<p>anyway</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908828):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">int</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">theorem</span> <span class="n">test&#39;</span> <span class="o">(</span><span class="n">a</span> <span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="n">int</span><span class="bp">.</span><span class="n">mod</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">of_nat</span> <span class="n">a</span><span class="o">)</span> <span class="err">↑</span><span class="n">p</span> <span class="bp">&lt;</span> <span class="err">↑</span><span class="n">p</span> <span class="o">:=</span>
<span class="n">int</span><span class="bp">.</span><span class="n">mod_lt_of_pos</span> <span class="n">a</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_lt_coe_nat_of_lt</span> <span class="n">H</span><span class="o">)</span>
</pre></div>

#### [ AHan (Nov 01 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908830):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span>  About the difference between "def" and "theorem", why is there test.eqations._eqn_1 appeared in your example<br>
<code>def test : 5=5 := rfl
#print prefix test</code></p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908835):
<p>because Kenny (intentionally) wrote bad code</p>

#### [ Kenny Lau (Nov 01 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908842):
<p>because <code>test</code> is now a definition so it has definitional equations</p>

#### [ Kenny Lau (Nov 01 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908844):
<p>just write any old definition</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908846):
<p>If you use def instead of theorem or theorem instead of def, expect random things</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908858):
<p>because they were not designed to be used in these circumstances</p>

#### [ Kenny Lau (Nov 01 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908901):
<p>undocumented behaviour... lul</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908906):
<p>I think "garbage in, garbage out" is well documented in the literature</p>

#### [ AHan (Nov 01 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136908975):
<p>What does the definitional equations refers to here?<br>
And how to use it in a normal def?</p>

#### [ Kenny Lau (Nov 01 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136909036):
<p>you don't really use it</p>

#### [ Kenny Lau (Nov 01 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136909041):
<p>it's internal mechanism</p>

#### [ Kevin Buzzard (Nov 01 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136909042):
<p>Every time you make a definition (especially a nice complicated one, maybe with pattern matching) Lean creates some secret "equation lemmas"</p>

#### [ Kevin Buzzard (Nov 01 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136909043):
<p>and when you try and unfold the definition, Lean uses these lemmas</p>

#### [ Kevin Buzzard (Nov 01 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136909058):
<p>As Kenny says, this is all done internally and the user is not supposed to have to worry about it. It's basically the trick which makes "unfold" work.</p>

#### [ Kevin Buzzard (Nov 01 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136909070):
<p><code>unfold X</code> is <code>simp only [equation lemmas for X]</code></p>

#### [ Kevin Buzzard (Nov 01 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136909131):
<p>(this is my slightly amateurish understanding of it -- I am a mathematician so shouldn't really be talking about implementation issues)</p>

#### [ AHan (Nov 01 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/int.mod/near/136909163):
<p>Are they the beta reduction rules?</p>


{% endraw %}
