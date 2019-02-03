---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/75913Weirdbehaviorofrw.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Weird behavior of rw?](https://leanprover-community.github.io/archive/113489newmembers/75913Weirdbehaviorofrw.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sebastian Zimmer (Sep 29 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134890495):
<p>I'm trying to shorten the following proof:</p>
<div class="codehilite"><pre><span></span>lemma sqr_roots_one (x : ℝ) (p : x ^ 2 = 1) : x = 1 ∨ x = -1 := begin
cases le_total x 0,
right,
rw [neg_eq_iff_neg_eq.1],
rw [← sqrt_sqr (neg_le_neg h), pow_two, neg_mul_neg, ← pow_two, p, sqrt_one],
left, rw [← sqrt_sqr h, p, sqrt_one],
end
</pre></div>


<p>But when I try to combine the two adjacent rw tactics into one it doesn't work.</p>

#### [ Chris Hughes (Sep 29 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134890652):
<p>That's because <code>rw [neg_eq_iff_neg_eq.1],</code> solved your goal, but created a new one. <code>rw [eq_neg_iff_eq_neg],</code> should allow you to merge the goals.<br>
Incidentally, here's the shortest proof</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">sqr_roots_one</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="bp">-</span><span class="mi">1</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rwa</span> <span class="o">[</span><span class="n">pow_two</span><span class="o">,</span> <span class="n">mul_self_eq_one_iff</span><span class="o">]</span> <span class="n">at</span> <span class="n">p</span>
</pre></div>

#### [ Sebastian Zimmer (Sep 29 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134890698):
<p>Lol I feel like I searched for everything except mul_self <span class="emoji emoji-1f615" title="oh no">:oh_no:</span></p>

#### [ Johan Commelin (Sep 29 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134890804):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">sqr_roots_one</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="bp">-</span><span class="mi">1</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rwa</span> <span class="o">[</span><span class="err">←</span><span class="n">mul_self_eq_one_iff</span><span class="o">,</span> <span class="err">←</span><span class="n">pow_two</span><span class="o">]</span>
</pre></div>

#### [ Chris Hughes (Sep 29 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134890854):
<p>I think this is one area the library isn't entirely consistent. There's a mix of pow_two and mul_self.</p>

#### [ Scott Olson (Sep 29 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134890928):
<p>For the record I found this way that lets you write the original with a merged <code>rw</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">sqr_roots_one</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="bp">-</span><span class="mi">1</span> <span class="o">:=</span> <span class="k">begin</span>
<span class="n">cases</span> <span class="n">le_total</span> <span class="n">x</span> <span class="mi">0</span><span class="o">,</span>
<span class="n">right</span><span class="o">,</span>
<span class="n">symmetry</span><span class="o">,</span>
<span class="n">rw</span> <span class="o">[</span><span class="n">neg_eq_iff_neg_eq</span><span class="o">,</span> <span class="err">←</span> <span class="n">sqrt_sqr</span> <span class="o">(</span><span class="n">neg_le_neg</span> <span class="n">h</span><span class="o">),</span> <span class="n">pow_two</span><span class="o">,</span> <span class="n">neg_mul_neg</span><span class="o">,</span> <span class="err">←</span> <span class="n">pow_two</span><span class="o">,</span> <span class="n">p</span><span class="o">,</span> <span class="n">sqrt_one</span><span class="o">],</span>
<span class="n">left</span><span class="o">,</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">sqrt_sqr</span> <span class="n">h</span><span class="o">,</span> <span class="n">p</span><span class="o">,</span> <span class="n">sqrt_one</span><span class="o">],</span>
<span class="kn">end</span>
</pre></div>

#### [ Scott Olson (Sep 29 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134891047):
<p>(Didn't work without <code>symmetry</code> first because of the way <code>neg_eq_iff_neg_eq</code> is written)</p>

#### [ Sebastian Zimmer (Sep 29 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134892753):
<p>This is probably a stupid question but how do I prove 2 \neq 0 in \com ?</p>

#### [ Sebastian Zimmer (Sep 29 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134892763):
<p>I noticed there is a theorem <code>two_ne_zero</code> that sounded promising but doesn't seem to work</p>

#### [ Chris Hughes (Sep 29 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134892866):
<p>I think it's <code>two_ne_zero'</code>. Not a stupid question.</p>

#### [ Sebastian Zimmer (Sep 29 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134893098):
<p>Thanks that worked. What is the difference between <code>two_ne_zero</code>  and <code>two_ne_zero'</code>?</p>

#### [ Scott Olson (Sep 29 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134893823):
<p>Different typeclass requirements, I guess:</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">two_ne_zero</span>
<span class="c1">-- two_ne_zero : ∀ {α : Type u_1} [_inst_1 : linear_ordered_field α], 2 ≠ 0</span>

<span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">two_ne_zero&#39;</span>
<span class="c1">-- two_ne_zero&#39; : ∀ {α : Type u_1} [_inst_1 : add_monoid α] [_inst_2 : has_one α] [_inst_3 : char_zero α], 2 ≠ 0</span>
</pre></div>

#### [ Chris Hughes (Sep 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134893977):
<p>It's a core thing. Every linear ordered field has characteristic zero, but <code>two_ne_zero</code> is in core, so it can't be changed, and therefore we need a version for <code>char_zero</code> as well.</p>


{% endraw %}
