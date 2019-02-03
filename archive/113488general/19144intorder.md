---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/19144intorder.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [int order](https://leanprover-community.github.io/archive/113488general/19144intorder.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Sep 13 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133888086):
<p>Why is most of <a href="https://github.com/leanprover/mathlib/blob/master/data/int/order.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/data/int/order.lean">https://github.com/leanprover/mathlib/blob/master/data/int/order.lean</a> commented out? Do we have these theorems elsewhere?</p>

#### [ Patrick Massot (Sep 13 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133888105):
<p>Do we usually keep commented code in mathlib?</p>

#### [ Patrick Massot (Sep 13 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133888255):
<p>Oh, it seems we have them in core <span class="emoji emoji-1f62e" title="open mouth">:open_mouth:</span></p>

#### [ Patrick Massot (Sep 13 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133888272):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what's this mess?</p>

#### [ Mario Carneiro (Sep 13 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889045):
<p>that is a <em>very</em> old file, ported from lean 2 I guess, and the theorems in it were either never updated or never needed, or appeared in other places (e.g. core) so they just stayed as is</p>

#### [ Mario Carneiro (Sep 13 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889074):
<p>I'm pretty sure the whole file can be deleted</p>

#### [ Mario Carneiro (Sep 13 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889152):
<p>on the plus side, it's good to see that the VSCode highlighting now understands that it is a comment; it used to try highlighting it since the nested comment at the start confused it</p>

#### [ Patrick Massot (Sep 13 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889165):
<p>github highlighting doesn't</p>

#### [ Mario Carneiro (Sep 13 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889226):
<div class="codehilite"><pre><span></span>theorem coe_nat_pos {n : ℕ} (Hpos : #nat n &gt; 0) : ↑n &gt; 0 :=
</pre></div>


<p>we haven't had that notation since lean 2</p>

#### [ Mario Carneiro (Sep 13 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889367):
<p>I wanted to make sure that all the theorems in the file have equivalents before deleting it</p>

#### [ Patrick Massot (Sep 13 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889457):
<p>Yeah, let's do that before Lean 4</p>

#### [ Mario Carneiro (Sep 13 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889497):
<p>is that an exercise I can outsource?</p>

#### [ Patrick Massot (Sep 13 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889539):
<p>It depends whether you're currently working on maths or the theory of computability of ordinal stuff :-p</p>

#### [ Mario Carneiro (Sep 13 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889914):
<p>does linear algebra count as maths?</p>

#### [ Patrick Massot (Sep 13 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889927):
<p>Is it over a semiring?</p>

#### [ Mario Carneiro (Sep 13 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889947):
<p>lattice of submodules</p>

#### [ Mario Carneiro (Sep 13 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889956):
<p>no semirings</p>

#### [ Patrick Massot (Sep 13 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889970):
<p>I'm sure there is a trick, but let's say yes</p>

#### [ Mario Carneiro (Sep 13 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133889984):
<p>Since I agree that semimodules have dubious worth, I plan to only generalize theorems from modules as needed</p>

#### [ Kevin Buzzard (Sep 13 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133890168):
<p>Chris asked me if semifields existed yesterday. I asked him if every semiring could be embedded into a ring and he said he didn't think so, so I told him I had no clue what a semifield was. He suggested that you take the field axioms and then remove all the ones mentioning <code>-</code>. I suppose that's one way of making new structures! I wasn't even sure if this gave a well-defined definition (in the sense that there might be more than one way of axiomatising fields)</p>

#### [ Bryan Gin-ge Chen (Sep 13 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133890191):
<blockquote>
<p>github highlighting doesn't</p>
</blockquote>
<p>There's <a href="https://github.com/leanprover/Lean.tmbundle/pull/7" target="_blank" title="https://github.com/leanprover/Lean.tmbundle/pull/7">an open PR</a> to fix the github highlighting; it probably needs to be updated for the most recent fixes to the VS code extension though.</p>

#### [ Johan Commelin (Sep 13 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133890291):
<p>Wow, this thread is degenerating quickly <span class="emoji emoji-1f606" title="lol">:lol:</span></p>

#### [ Chris Hughes (Sep 13 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133892163):
<p>PRed <a href="https://github.com/leanprover/mathlib/pull/348" target="_blank" title="https://github.com/leanprover/mathlib/pull/348">https://github.com/leanprover/mathlib/pull/348</a></p>

#### [ Kevin Buzzard (Sep 13 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133892911):
<p>me and Kenny are playing multiplayer lean</p>

#### [ Kevin Buzzard (Sep 13 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133892928):
<p>lots of things are there that weren't there last week. I should take this to the cocalc thread</p>

#### [ Patrick Massot (Sep 13 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133895614):
<p>Do we already have <code>{α : Type*} [linear_ordered_ring α] {a : α} (h : a ≠ 0) : a * a &gt; 0</code>. I can prove it but it should be there already</p>

#### [ Reid Barton (Sep 13 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133895853):
<p>I guess it should have a name like <code>mul_self_pos</code>, and I don't see it.</p>

#### [ Mario Carneiro (Sep 13 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133895951):
<p>I don't think it's there, and it's good to have</p>

#### [ Kevin Buzzard (Sep 13 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133895952):
<p>There's <code>mul_pos</code> and <code>mul_self_nonneg</code> but maybe you found a hole :-)</p>

#### [ Patrick Massot (Sep 13 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896064):
<p>Indeed I called it <code>mul_self_pos</code>.</p>

#### [ Mario Carneiro (Sep 13 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896078):
<p>approve</p>

#### [ Patrick Massot (Sep 13 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896082):
<p>Mario, do you want a PR or would it be quicker for you to add it yourself?</p>

#### [ Patrick Massot (Sep 13 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896851):
<p>A PR would contains something like:</p>
<div class="codehilite"><pre><span></span><span class="kn">section</span> <span class="n">linear_ordered_ring</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">linear_ordered_ring</span> <span class="n">α</span><span class="o">]</span>

<span class="kn">lemma</span> <span class="n">mul_self_eq_zero_iff</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span><span class="bp">*</span><span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">↔</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">split</span><span class="bp">;</span> <span class="n">intro</span> <span class="n">h</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">cases</span> <span class="n">linear_ordered_ring</span><span class="bp">.</span><span class="n">eq_zero_or_eq_zero_of_mul_eq_zero</span> <span class="n">h</span> <span class="k">with</span> <span class="n">H</span> <span class="n">H</span> <span class="bp">;</span> <span class="n">exact</span> <span class="n">H</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="n">h</span><span class="o">,</span> <span class="n">mul_zero</span><span class="o">]</span> <span class="o">}</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">mul_self_pos</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="n">lt_of_le_of_ne</span> <span class="o">(</span><span class="n">mul_self_nonneg</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">h</span> <span class="err">$</span> <span class="o">(</span><span class="n">mul_self_eq_zero_iff</span> <span class="n">a</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span> <span class="err">$</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="n">H</span><span class="o">)</span>
<span class="kn">end</span> <span class="n">linear_ordered_ring</span>
</pre></div>

#### [ Patrick Massot (Sep 13 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896882):
<p>Or even one more $</p>

#### [ Mario Carneiro (Sep 13 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896885):
<p>I didn't include that other lemma, but it's true in any domain</p>

#### [ Patrick Massot (Sep 13 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896957):
<p>do we have that <code>linear_ordered_ring</code> implies domain?</p>

#### [ Patrick Massot (Sep 13 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896964):
<p>I mean, as an instance</p>

#### [ Mario Carneiro (Sep 13 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896965):
<p>except for that pesky 0 != 1 thing</p>

#### [ Patrick Massot (Sep 13 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896981):
<p>OF course I see (and use) the lemma</p>

#### [ Mario Carneiro (Sep 13 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133896985):
<p>oh wait, 0 &lt; 1 in a linorder ring so it's okay</p>

#### [ Patrick Massot (Sep 13 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133897078):
<p><a href="https://github.com/leanprover/mathlib/commit/46502df9a61b131ee5e9265ec2593ab87b654b94" target="_blank" title="https://github.com/leanprover/mathlib/commit/46502df9a61b131ee5e9265ec2593ab87b654b94">https://github.com/leanprover/mathlib/commit/46502df9a61b131ee5e9265ec2593ab87b654b94</a> Sometimes diff tries to be too clever...</p>

#### [ Reid Barton (Sep 13 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133897207):
<p>I mean, both lemmas have a hypothesis <code>ha</code> about something named <code>a</code>, so they're basically the same lemma</p>

#### [ Patrick Massot (Sep 13 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133897219):
<p>I can hear my students saying that</p>

#### [ Kevin Buzzard (Sep 13 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133898099):
<p>you permuted two lemmas!</p>

#### [ Chris Hughes (Sep 13 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/int%20order/near/133900919):
<p>(deleted)</p>


{% endraw %}
