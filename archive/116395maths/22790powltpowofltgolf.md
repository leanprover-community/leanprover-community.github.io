---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/22790powltpowofltgolf.html
---

## Stream: [maths](index.html)
### Topic: [pow_lt_pow_of_lt golf](22790powltpowofltgolf.html)

---


{% raw %}
#### [ Kevin Buzzard (Nov 14 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147671439):
<div class="codehilite"><pre><span></span><span class="kn">variable</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="c1">-- or [linear_ordered_field]</span>
<span class="kn">theorem</span> <span class="n">pow_lt_pow_of_lt</span> <span class="o">{</span><span class="n">i</span> <span class="n">j</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">&gt;</span> <span class="mi">1</span> <span class="bp">→</span> <span class="n">i</span> <span class="bp">&lt;</span> <span class="n">j</span> <span class="bp">→</span> <span class="n">x</span><span class="err">^</span><span class="n">i</span> <span class="bp">&lt;</span> <span class="n">x</span><span class="err">^</span><span class="n">j</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>Is this in mathlib?</p>

#### [ Mario Carneiro (Nov 14 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147671985):
<p>all the other versions of this are in <code>group_power.lean</code>, but it looks like this one was missed</p>

#### [ Kevin Buzzard (Nov 14 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147671989):
<p><code>nat.pow_lt_pow_of_lt_right : ∀ {x : ℕ}, x &gt; 1 → ∀ {i j : ℕ}, i &lt; j → x ^ i &lt; x ^ j</code></p>
<p>This should be a theorem about partially ordered semirings or something, right?</p>

#### [ Mario Carneiro (Nov 14 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147672028):
<p>linear_ordered_semiring</p>

#### [ Mario Carneiro (Nov 14 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147672039):
<p>because we don't have partially ordered semirings</p>

#### [ Kevin Buzzard (Nov 14 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147672170):
<p>I spotted this hole this time last year, when I didn't understand the purpose of the mathlib library. At the time, I just figured this was the sort of thing you had to prove yourself, because I had no concept of what "should be there already" (so I proved it in the case I needed it). I understand this concept much better now.</p>

#### [ Mario Carneiro (Nov 14 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147672449):
<p>here's my proof:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">pow_lt_pow</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">n</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">a</span> <span class="err">^</span> <span class="n">m</span> <span class="o">:=</span>
<span class="n">lt_of_lt_of_le</span>
  <span class="o">((</span><span class="n">lt_mul_iff_one_lt_left</span> <span class="o">(</span><span class="n">pow_pos</span> <span class="o">(</span><span class="n">lt_trans</span> <span class="n">zero_lt_one</span> <span class="n">ha</span><span class="o">)</span> <span class="bp">_</span><span class="o">))</span><span class="bp">.</span><span class="mi">2</span> <span class="n">ha</span><span class="o">)</span>
  <span class="o">(</span><span class="n">pow_le_pow</span> <span class="o">(</span><span class="n">le_of_lt</span> <span class="n">ha</span><span class="o">)</span> <span class="n">h</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Nov 14 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147672553):
<p>I'm doing all my own example sheet questions again after last year's attempts. Some of the code I wrote a year ago was absolutely terrible.</p>
<p>Here's the library I wrote this year, to do a question on my problem sheet about n'th roots (n a positive integer)</p>
<p><a href="https://github.com/ImperialCollegeLondon/M1F_example_sheets/blob/master/src/xenalib/real_nth_root.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/M1F_example_sheets/blob/master/src/xenalib/real_nth_root.lean">https://github.com/ImperialCollegeLondon/M1F_example_sheets/blob/master/src/xenalib/real_nth_root.lean</a></p>
<p>Any stylistic comments or anything would be welcome. I only care about the reals but really that's for stylistic reasons -- I am trying to write a library with a lot of tactic mode proofs so maths students can follow them more easily, and I wanted to make it as simple as possible. Maybe some of this stuff is in mathlib but I understand my own proofs better -- I find them much more readable.</p>

#### [ Mario Carneiro (Nov 14 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147672666):
<p>My proof differs from yours in the proof strategy, which is most of why it is shorter</p>

#### [ Mario Carneiro (Nov 14 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147672690):
<p><code>lt_of_pow_lt</code> also has a very short proof using <code>pow_le_pow</code></p>

#### [ Mario Carneiro (Nov 14 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147672716):
<p>The lesson is "use lemmas"</p>

#### [ Mario Carneiro (Nov 14 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147672825):
<p>And I don't just mean use theorems that have already been proven, I mean arrange the proofs of similar facts to make the best use of commonality</p>

#### [ Mario Carneiro (Nov 14 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147673012):
<p>your assumptions to <code>lt_of_pow_lt</code> are also stronger than they need to be - it's nice when you can learn this by attempting the proof itself</p>

#### [ Mario Carneiro (Nov 14 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147673104):
<p><code>nth_root_unique</code> is reducible in the sense that it has an equality hypothesis - I would prove a lemma which doesn't have that hypothesis first</p>

#### [ Mario Carneiro (Nov 14 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147673417):
<p>it also factors into <code>x ^ n = y ^ n -&gt; x = y</code>, which should also be in <code>group_power</code> in some generality</p>

#### [ Kevin Buzzard (Nov 14 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147676410):
<blockquote>
<p>here's my proof:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">pow_lt_pow</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">n</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">a</span> <span class="err">^</span> <span class="n">m</span> <span class="o">:=</span>
<span class="n">lt_of_lt_of_le</span>
  <span class="o">((</span><span class="n">lt_mul_iff_one_lt_left</span> <span class="o">(</span><span class="n">pow_pos</span> <span class="o">(</span><span class="n">lt_trans</span> <span class="n">zero_lt_one</span> <span class="n">ha</span><span class="o">)</span> <span class="bp">_</span><span class="o">))</span><span class="bp">.</span><span class="mi">2</span> <span class="n">ha</span><span class="o">)</span>
  <span class="o">(</span><span class="n">pow_le_pow</span> <span class="o">(</span><span class="n">le_of_lt</span> <span class="n">ha</span><span class="o">)</span> <span class="n">h</span><span class="o">)</span>
</pre></div>


</blockquote>
<p><code>pow_le_pow (le_of_lt ha) h</code> is a dirty trick, isn't it?</p>

#### [ Kevin Buzzard (Nov 14 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147676673):
<p>So the reason I have noticed that <code>pow_le_pow</code> trick is because I manually completely unfolded your proof:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">pow_lt_pow&#39;</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">n</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">a</span> <span class="err">^</span> <span class="n">m</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">lt_of_lt_of_le</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="o">((</span><span class="n">lt_mul_iff_one_lt_left</span> <span class="o">(</span><span class="n">pow_pos</span> <span class="o">(</span><span class="n">lt_trans</span> <span class="n">zero_lt_one</span> <span class="n">ha</span><span class="o">)</span> <span class="bp">_</span><span class="o">))</span><span class="bp">.</span><span class="mi">2</span> <span class="n">ha</span><span class="o">)},</span>
  <span class="n">exact</span> <span class="o">(</span><span class="n">pow_le_pow</span> <span class="o">(</span><span class="n">le_of_lt</span> <span class="n">ha</span><span class="o">)</span> <span class="n">h</span><span class="o">)</span>
<span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">pow_lt_pow&#39;&#39;</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">n</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">a</span> <span class="err">^</span> <span class="n">m</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">lt_of_lt_of_le</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">refine</span> <span class="o">(</span><span class="n">lt_mul_iff_one_lt_left</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="n">ha</span><span class="o">,</span>
    <span class="n">refine</span> <span class="n">pow_pos</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
    <span class="c1">-- got it</span>
    <span class="n">exact</span> <span class="n">lt_trans</span> <span class="n">zero_lt_one</span> <span class="n">ha</span>
  <span class="o">},</span>
  <span class="o">{</span> <span class="n">refine</span> <span class="n">pow_le_pow</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span> <span class="c1">-- dirty trick?</span>
    <span class="n">exact</span> <span class="n">le_of_lt</span> <span class="n">ha</span>
  <span class="o">}</span>
<span class="kn">end</span>
</pre></div>


<p>into a form which I can actually <em>read</em>. Could there be some code which helps me do this unravelling? It is so much easier for me to inspect nodes of the tree when in tactic mode. <span class="user-mention" data-user-id="110026">@Simon Hudon</span> can code do this? Break down some simple class of term mode functions into a tactic proof?</p>

#### [ Mario Carneiro (Nov 14 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147677006):
<p><code>explode</code> does this</p>

#### [ Kevin Buzzard (Nov 14 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147677009):
<p>Even after this breaking-down I still lose information. For example after that first <code>lt_of_lt_of_le</code> -- when I do it in tactic mode I get an extra metavariable goal which Lean has solved in the term mode proof but has not solved in the tactic mode proof. I just want to inspect the metavariable-free goal which is actually proved at each function application I think. How does one do this?</p>

#### [ Kevin Buzzard (Nov 14 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147677072):
<p>How do I run <code>explode</code>?</p>

#### [ Kevin Buzzard (Nov 14 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147677126):
<p>found it</p>

#### [ Mario Carneiro (Nov 14 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147677334):
<p>ooh, <code>explode</code> actually works pretty well on that proof</p>

#### [ Kevin Buzzard (Nov 14 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147677383):
<p>Quick, we need an emoji</p>

#### [ Kevin Buzzard (Nov 14 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147677426):
<p>hey <code>#explode</code> is exactly the answer to my question!</p>

#### [ Kevin Buzzard (Nov 14 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147677441):
<p><span class="emoji emoji-1f600" title="grinning">:grinning:</span></p>

#### [ Kevin Buzzard (Nov 14 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147677664):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">explode</span>
<span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">group_power</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">linear_ordered_semiring</span> <span class="n">α</span><span class="o">]</span>
<span class="kn">theorem</span> <span class="n">pow_lt_pow</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">n</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">a</span> <span class="err">^</span> <span class="n">m</span> <span class="o">:=</span>
<span class="n">lt_of_lt_of_le</span>
  <span class="o">((</span><span class="n">lt_mul_iff_one_lt_left</span> <span class="o">(</span><span class="n">pow_pos</span> <span class="o">(</span><span class="n">lt_trans</span> <span class="n">zero_lt_one</span> <span class="n">ha</span><span class="o">)</span> <span class="bp">_</span><span class="o">))</span><span class="bp">.</span><span class="mi">2</span> <span class="n">ha</span><span class="o">)</span>
  <span class="o">(</span><span class="n">pow_le_pow</span> <span class="o">(</span><span class="n">le_of_lt</span> <span class="n">ha</span><span class="o">)</span> <span class="n">h</span><span class="o">)</span>

<span class="bp">#</span><span class="n">explode</span> <span class="n">pow_lt_pow</span>
</pre></div>


<p>MWE. Say kids! Understand Mario's proofs in seconds with <code>#explode</code>! Cool name, cool tactic.</p>

#### [ Kevin Buzzard (Nov 14 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147678779):
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">linear_ordered_semiring</span> <span class="n">α</span><span class="o">]</span>
<span class="kn">theorem</span> <span class="n">pow_lt_pow</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">n</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">a</span> <span class="err">^</span> <span class="n">m</span> <span class="o">:=</span>
<span class="n">lt_of_lt_of_le</span>
  <span class="o">(</span> <span class="n">iff</span><span class="bp">.</span><span class="n">mpr</span>
      <span class="o">(</span> <span class="n">lt_mul_iff_one_lt_left</span> <span class="err">$</span>
        <span class="n">pow_pos</span>
          <span class="o">(</span> <span class="n">lt_trans</span>
              <span class="n">zero_lt_one</span>
              <span class="n">ha</span>
          <span class="o">)</span>
          <span class="bp">_</span>
      <span class="o">)</span>
      <span class="n">ha</span>
  <span class="o">)</span>
  <span class="o">(</span> <span class="n">pow_le_pow</span>
      <span class="o">(</span> <span class="n">le_of_lt</span> <span class="err">$</span>
        <span class="n">ha</span>
      <span class="o">)</span>
      <span class="n">h</span>
  <span class="o">)</span>
</pre></div>


<p>Here is another way of taking your proof apart Mario. I have tried to have some sort of a system when unravelling. Is there some sort of name for a form like this? Again I feel like I applied an algorithm. I used $ for functions of one variable and indented for two or more.</p>
<p>How do I tell which term fills the underscore in that proof, by the way? What's the easiest way?</p>

#### [ Reid Barton (Nov 14 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147678945):
<p>I discovered recently if you replace a <code>_</code> by a hole <code>{! !}</code> then Lean will give you an error saying there's only one way to fill the hole and tell you what it should be</p>

#### [ Bryan Gin-ge Chen (Nov 14 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147678962):
<p>I was just about to say that ^</p>

#### [ Bryan Gin-ge Chen (Nov 14 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147678971):
<p>In this case it's <code>n</code></p>

#### [ Kevin Buzzard (Nov 14 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147679302):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">pow_lt_pow&#39;</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">n</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span>
<span class="n">a</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">a</span> <span class="err">^</span> <span class="n">m</span> <span class="o">:=</span>
<span class="n">lt_of_lt_of_le</span> <span class="c1">-- 14</span>
  <span class="o">(</span> <span class="n">iff</span><span class="bp">.</span><span class="n">mpr</span> <span class="c1">-- 11</span>
      <span class="o">(</span> <span class="n">lt_mul_iff_one_lt_left</span> <span class="err">$</span> <span class="c1">-- 10</span>
        <span class="n">pow_pos</span> <span class="c1">-- 9 -- takes two inputs</span>
          <span class="o">(</span> <span class="n">lt_trans</span> <span class="c1">-- 8</span>
              <span class="n">zero_lt_one</span> <span class="c1">-- 7</span>
              <span class="n">ha</span> <span class="c1">-- 5</span>
          <span class="o">)</span>
          <span class="bp">_</span> <span class="c1">-- gaargh explode doesn&#39;t tell me</span>
      <span class="o">)</span>
      <span class="n">ha</span> <span class="c1">-- 5</span>
  <span class="o">)</span>
  <span class="o">(</span> <span class="n">pow_le_pow</span> <span class="c1">-- 13</span>
      <span class="o">(</span> <span class="n">le_of_lt</span> <span class="err">$</span> <span class="c1">-- 12</span>
        <span class="n">ha</span> <span class="c1">-- 5</span>
      <span class="o">)</span>
      <span class="n">h</span> <span class="c1">-- 6</span>
  <span class="o">)</span>
</pre></div>


<p>I can't immediately see how to fill in that hole using the output of <code>#explode</code> though</p>

#### [ Kevin Buzzard (Nov 14 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147679309):
<p>Funky numbering by the way.</p>

#### [ Bryan Gin-ge Chen (Nov 14 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147679900):
<p>This is post-hoc and probably not immediate enough, but first note that the underscore is the second argument to <code>pow_pos</code> (easy to see right away with the bracket colorizer extension), and then compare with the corresponding line of <code>#explode</code>, which says <code>0 &lt; a ^ n</code>.</p>

#### [ Kevin Buzzard (Nov 14 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147679928):
<p>Maybe this indentation is better:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">explode</span>
<span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">group_power</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">linear_ordered_semiring</span> <span class="n">α</span><span class="o">]</span>
<span class="kn">theorem</span> <span class="n">pow_lt_pow&#39;</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">n</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span>
<span class="n">a</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">a</span> <span class="err">^</span> <span class="n">m</span> <span class="o">:=</span>
<span class="n">lt_of_lt_of_le</span> <span class="c1">-- 14</span>
  <span class="o">(</span> <span class="n">iff</span><span class="bp">.</span><span class="n">mpr</span> <span class="c1">-- 11</span>
      <span class="o">(</span> <span class="n">lt_mul_iff_one_lt_left</span>  <span class="c1">-- 10</span>
        <span class="o">(</span> <span class="n">pow_pos</span> <span class="c1">-- 9 -- takes two inputs</span>
          <span class="o">(</span> <span class="n">lt_trans</span> <span class="c1">-- 8</span>
              <span class="n">zero_lt_one</span> <span class="c1">-- 7</span>
            <span class="n">ha</span> <span class="c1">-- 5</span>
          <span class="o">)</span>
        <span class="bp">_</span> <span class="c1">-- gaargh explode doesn&#39;t tell me</span>
        <span class="o">)</span>
      <span class="o">)</span>
    <span class="n">ha</span> <span class="c1">-- 5</span>
  <span class="o">)</span>
  <span class="o">(</span> <span class="n">pow_le_pow</span> <span class="c1">-- 13</span>
      <span class="o">(</span> <span class="n">le_of_lt</span> <span class="c1">-- 12</span>
        <span class="n">ha</span> <span class="c1">-- 5</span>
      <span class="o">)</span>
    <span class="n">h</span> <span class="c1">-- 6</span>
  <span class="o">)</span>

<span class="bp">#</span><span class="n">explode</span> <span class="n">pow_lt_pow&#39;</span>
</pre></div>

#### [ Kevin Buzzard (Nov 14 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147679979):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">explode</span>
<span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">group_power</span>

<span class="kn">theorem</span> <span class="n">pow_lt_pow&#39;</span>
<span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="c1">-- 0</span>
<span class="o">[</span><span class="n">linear_ordered_semiring</span> <span class="n">α</span><span class="o">]</span> <span class="c1">-- 1</span>
<span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="c1">-- 2</span>
<span class="o">{</span><span class="n">n</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="c1">-- 3,4</span>
<span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span> <span class="c1">-- 5</span>
<span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="c1">-- 6</span>
<span class="n">a</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">a</span> <span class="err">^</span> <span class="n">m</span> <span class="o">:=</span> <span class="c1">-- proof starts</span>
<span class="n">lt_of_lt_of_le</span> <span class="c1">-- 14</span>
  <span class="o">(</span> <span class="n">iff</span><span class="bp">.</span><span class="n">mpr</span> <span class="c1">-- 11</span>
      <span class="o">(</span> <span class="n">lt_mul_iff_one_lt_left</span>  <span class="c1">-- 10</span>
        <span class="o">(</span> <span class="n">pow_pos</span> <span class="c1">-- 9</span>
          <span class="o">(</span> <span class="n">lt_trans</span> <span class="c1">-- 8</span>
              <span class="n">zero_lt_one</span> <span class="c1">-- 7</span>
            <span class="n">ha</span><span class="o">)</span> <span class="c1">-- 5</span>
        <span class="bp">_</span><span class="o">))</span> <span class="c1">-- gaargh explode doesn&#39;t tell me</span>
    <span class="n">ha</span><span class="o">)</span> <span class="c1">-- 5</span>
  <span class="o">(</span> <span class="n">pow_le_pow</span> <span class="c1">-- 13</span>
      <span class="o">(</span> <span class="n">le_of_lt</span> <span class="c1">-- 12</span>
        <span class="n">ha</span><span class="o">)</span> <span class="c1">-- 5</span>
    <span class="n">h</span><span class="o">)</span> <span class="c1">-- 6</span>

<span class="bp">#</span><span class="n">explode</span> <span class="n">pow_lt_pow&#39;</span>
</pre></div>


<p>explode covers basically every other line of code</p>

#### [ Kevin Buzzard (Nov 14 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680151):
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="n">explode</span> <span class="n">zmodp</span><span class="bp">.</span><span class="n">quadratic_reciprocity</span>
<span class="c1">-- (deterministic) timeout</span>
</pre></div>


<p>boo</p>

#### [ Bryan Gin-ge Chen (Nov 14 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680230):
<p>Hmm, so the line in the output of <code>#explode</code> corresponding to <code>pow_pos</code> is this:</p>
<div class="codehilite"><pre><span></span>9 │8    │ pow_pos                │ 0 &lt; a ^ n
</pre></div>


<p>Why doesn't the second column read <code>8,3</code> (<code>3</code> is the line corresponding to <code>n : nat</code>)? It's the same whether I put in <code>n</code> or <code>_</code>.</p>

#### [ Mario Carneiro (Nov 14 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680270):
<p>Non-propositional arguments are automatically suppressed, because they would otherwise dominate the output and they are inferrable from the (fully elaborated) types in the right column</p>

#### [ Jeremy Avigad (Nov 14 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680342):
<p>Wow, <code>explode</code> is really nice. It is great for teaching. I just tried</p>
<div class="codehilite"><pre><span></span>theorem foo (A B C : Prop) : (A → B → C) → (A ∧ B → C) :=
λ h hab, and.elim hab (λ ha hb, h ha hb)

#explode foo
</pre></div>


<p>It made me realize that the proof can be shortened:</p>
<div class="codehilite"><pre><span></span>theorem foo&#39; (A B C : Prop) : (A → B → C) → (A ∧ B → C) :=
λ h hab, and.elim hab h
</pre></div>


<p>The tactic doesn't behave well with <code>have</code>, though.</p>
<div class="codehilite"><pre><span></span>theorem bar  (A B C : Prop) : A ∧ (B ∨ C) → (A ∧ B) ∨ (A ∧ C) :=
assume h : A ∧ (B ∨ C),
have h₁ : A, from and.left h,
have h₂ : B ∨ C, from and.right h,
or.elim h₂
  (assume h₃ : B,
    or.inl (and.intro h₁ h₃))
  (assume h₃ : C,
    or.inr (and.intro h₁ h₃))

#explore bar
</pre></div>


<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Would it be hard to handle <code>have</code> nicely in the tactic?</p>

#### [ Mario Carneiro (Nov 14 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680687):
<p>hm, it's <code>explode</code> not <code>explore</code> but that is also an interesting name</p>

#### [ Jeremy Avigad (Nov 14 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680738):
<p>Oops, sorry, I forgot to cut-and-paste that part and added it manually. You are right, it is also a good name.</p>

#### [ Mario Carneiro (Nov 14 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680791):
<p><code>have</code> should be handled well since it will translate to a proof line that is referred to twice</p>

#### [ Mario Carneiro (Nov 14 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680818):
<p>what does it look like now? (on my phone)</p>

#### [ Mario Carneiro (Nov 14 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680925):
<p>indeed it is best suited to the basic dtt proofs used in intro logic</p>

#### [ Kevin Buzzard (Nov 14 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680929):
<p>In general, I think I'd rather read the output from the bottom up when trying to figure out what you're doing.</p>

#### [ Mario Carneiro (Nov 14 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680940):
<p>yes absolutely</p>

#### [ Kevin Buzzard (Nov 14 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680953):
<p>so...it's upside-down?</p>

#### [ Mario Carneiro (Nov 14 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680979):
<p>well no, it is meant to be read bottom up</p>

#### [ Mario Carneiro (Nov 14 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680988):
<p>but it follows the usual proof order</p>

#### [ Mario Carneiro (Nov 14 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147681053):
<p>it is a fitch style proof display</p>

#### [ Kevin Buzzard (Nov 14 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147681070):
<p>Thanks a lot for alerting me to it.</p>

#### [ Bryan Gin-ge Chen (Nov 14 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147681091):
<p><code>#explode bar</code> looks like this now:</p>
<div class="codehilite"><pre><span></span>bar : ∀ (A B C : Prop), A ∧ (B ∨ C) → A ∧ B ∨ A ∧ C
0│   │ A                                                                                                                     ├ Prop
1│   │ B                                                                                                                     ├ Prop
2│   │ C                                                                                                                     ├ Prop
3│   │ h                                                                                                                     ├ A ∧ (B ∨ C)
4│   │ λ (h₁ : A),
  have h₂ : B ∨ C, from h.right,
  or.elim h₂ (λ (h₃ : B), or.inl ⟨h₁, h₃⟩) (λ (h₃ : C), or.inr ⟨h₁, h₃⟩) │ A → A ∧ B ∨ A ∧ C
5│3  │ and.left                                                                                                              │ A
6│4,5│ ∀E                                                                                                                    │ A ∧ B ∨ A ∧ C
</pre></div>

#### [ Mario Carneiro (Nov 14 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147681164):
<p>also pp.beta helps sometimes</p>


{% endraw %}
