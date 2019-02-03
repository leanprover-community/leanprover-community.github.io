---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/32676heqhellagain.html
---

## Stream: [general](index.html)
### Topic: [heq hell again](32676heqhellagain.html)

---


{% raw %}
#### [ Patrick Massot (Oct 09 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135479776):
<p>My current goal looks like <code>eq.mpr comm_ring._proof_2 (quotient_ring.comm_ring (closure (is_ideal.trivial α))) == quotient_ring.comm_ring (closure (is_ideal.trivial α))</code> I'm ready to believe this is a rightful punishment for an earlier sin, but I'd like to know whether there is any hope to escape, or I should go back and think about what I'm doing</p>

#### [ Chris Hughes (Oct 09 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135480240):
<p>Does this lemma help?</p>
<div class="codehilite"><pre><span></span><span class="kn">universe</span> <span class="n">u</span>
<span class="kn">lemma</span> <span class="n">for_patrick</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">=</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">eq</span><span class="bp">.</span><span class="n">mpr</span> <span class="n">h</span> <span class="n">x</span> <span class="bp">==</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">subst</span> <span class="n">h</span><span class="bp">;</span> <span class="n">refl</span>
</pre></div>

#### [ Patrick Massot (Oct 09 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135480267):
<p>YES!</p>

#### [ Patrick Massot (Oct 09 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135480471):
<p>Can you explain what's going on here?</p>

#### [ Patrick Massot (Oct 09 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135480493):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> should this be added as a simp lemma in mathlib?</p>

#### [ Patrick Massot (Oct 09 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135480728):
<p>Let's see how bad things are. What I wanted to write was:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">uniform_add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span>
  <span class="n">topological_ring</span> <span class="o">(</span><span class="n">quotient</span> <span class="o">(</span><span class="n">separation_setoid</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span>
<span class="k">by</span>  <span class="n">rw</span> <span class="n">ring_sep_rel</span> <span class="bp">;</span> <span class="n">apply_instance</span>
</pre></div>


<p>What I actually wrote (after adding Chris's simp lemma):</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">uniform_add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span>
  <span class="n">topological_ring</span> <span class="o">(</span><span class="n">quotient</span> <span class="o">(</span><span class="n">separation_setoid</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">convert</span> <span class="n">topological_ring_quotient</span> <span class="o">(</span><span class="n">closure</span> <span class="o">(</span><span class="n">is_ideal</span><span class="bp">.</span><span class="n">trivial</span> <span class="n">α</span><span class="o">)),</span>
  <span class="o">{</span> <span class="n">apply</span> <span class="n">ring_sep_rel</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">dsimp</span> <span class="o">[</span><span class="n">topological_ring_quotient_topology</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">topological_space</span><span class="o">,</span> <span class="n">to_topological_space</span><span class="o">],</span>
    <span class="n">congr</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">ring_sep_rel</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">ring_sep_rel</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">apply</span> <span class="n">ring_sep_rel</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">simp</span> <span class="o">[</span><span class="n">uniform_space</span><span class="bp">.</span><span class="n">comm_ring</span><span class="o">]</span> <span class="o">},</span>
<span class="kn">end</span>
</pre></div>


<p>Like: <em>come one Lean: apply ring_sep_rel!</em></p>

#### [ Patrick Massot (Oct 09 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135480782):
<p>where <code>lemma ring_sep_rel (α) [comm_ring α] [uniform_space α] [uniform_add_group α] [topological_ring α] :
  separation_setoid α = quotient_ring.quotient_rel (closure $ is_ideal.trivial α)</code></p>

#### [ Chris Hughes (Oct 09 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135480982):
<p><code>subst</code> is a better version of <code>rw</code>, that can <code>rw</code> the types of proofs as well. before <code>subst h</code> the goal is <code>@eq.mpr β α h x == x</code>, after <code>subst h</code>the goal is <code>@eq.mpr β β (@eq.refl (Sort u) β) x == x</code>, and now the types are the same on each sude of the equality, and <code>eq.mpr</code> can iota-reduce, since <code>eq.refl</code> is a constructor, so it's just <code>refl</code>. </p>
<p>The trouble with <code>subst</code> is it only works with local constants, so these proofs often require you to turn your goal into a lemma where you can use <code>subst</code> on local constants. A good version of <code>subst</code> that handles things other than local constants is something that needs to be written I think.</p>

#### [ Chris Hughes (Oct 09 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135481256):
<p><code>eq_rec_heq</code> is exactly the same as the lemma I wrote by the way.</p>

#### [ Patrick Massot (Oct 09 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135481343):
<p>not quite</p>

#### [ Patrick Massot (Oct 09 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135482297):
<p>Chris, do you know if there is some more documentation about this magic <code>subst</code>? It sounds like it could be very useful. Lately I've been fighting that kind of <code>rw</code> issues a lot</p>

#### [ Chris Hughes (Oct 09 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135487819):
<p>I don't think there's any documentation. The strategy to use it is to make sure that the expression you're substituting is a local constant, and if it isn't, then make an intermediate lemma. In the example I gave, only <code>α</code> had to be a local constant.</p>

#### [ Reid Barton (Oct 09 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135488280):
<p>I always assumed <code>subst</code> was just induction on <code>eq</code>, is it actually something different?</p>

#### [ Simon Hudon (Oct 09 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135488614):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> That's a useful way to see it. The thing is that by doing induction on eq, you're substitution everywhere at once so when your variable is used as a parameter for a function with a dependent type, it can help do the substitution in every term and type at once so that the goal remains type correct</p>

#### [ Chris Hughes (Oct 09 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135488646):
<p>Looking at the definition it appears to not be based on the induction tactic. <code>cases</code> also works in this example, but basically <code>subst</code> is for when the motive is hard to compute due to dependent arguments. The proof terms use <code>eq.drec</code> instead of <code>eq.rec</code></p>

#### [ Patrick Massot (Oct 09 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135488654):
<p>It sounds exactly like what I've needed for one week</p>

#### [ Patrick Massot (Oct 09 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135488934):
<p>What is a local constant?</p>

#### [ Simon Hudon (Oct 09 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135489147):
<p>It's a free variable in your goal, not a definition and not a bound variable.</p>

#### [ Chris Hughes (Oct 09 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135489169):
<p>I think it's basically a variable in your local context, so <code>α</code> is, but not <code>ℕ</code> or <code>f α</code></p>

#### [ Reid Barton (Oct 09 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135489182):
<p>"something you could substitute something else for"</p>

#### [ Patrick Massot (Oct 09 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135489247):
<p>It's hard to see how such a restrictive condition can be satisfied</p>

#### [ Mario Carneiro (Oct 09 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135489445):
<p>Only one side has to be a variable. e.g. <code>x = 1 |- P x</code> reduces to <code>P 1</code></p>

#### [ Chris Hughes (Oct 09 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135489455):
<p>You turn your goal into a lemma about local constants, and then substitute your expression into that lemma, like I did with <code>for_patrick</code> A bit messy, but reliable.</p>

#### [ Mario Carneiro (Oct 09 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135489480):
<p>Also, <code>rcases e with rfl</code> will do subst on terms</p>

#### [ Patrick Massot (Oct 09 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135489504):
<p>What?!</p>

#### [ Mario Carneiro (Oct 09 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135489507):
<p>and <code>rcases e with &lt;&gt;</code> will do cases instead, which has slightly different effects wrt unfolding</p>

#### [ Patrick Massot (Oct 09 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135489516):
<p>All this becomes more and more obscure to me</p>

#### [ Mario Carneiro (Oct 09 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135489532):
<p>it's super useful to use <code>rfl</code> in rcases patterns</p>

#### [ Mario Carneiro (Oct 09 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135489628):
<p>If your assumption is <code>f x = g y</code> then it's difficult to eliminate the equality once and for all, it could make lots of things equal to other things in an unpredictable way (see: word problem)</p>

#### [ Mario Carneiro (Oct 09 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135489659):
<p>but when one side is a fresh variable, like <code>x = g y</code>, then we can just replace <code>x</code> with <code>g y</code> everywhere in the context to eliminate <code>x</code></p>

#### [ Mario Carneiro (Oct 09 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135489743):
<p>The nice thing is that this works <em>regardless of any dependencies</em>, which is a big plus compared to <code>rw</code> with this equality everywhere</p>

#### [ Mario Carneiro (Oct 09 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135489786):
<p>Basically all facts about <code>eq</code> and <code>heq</code> are proved using this trick</p>

#### [ Patrick Massot (Oct 09 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135489943):
<p>I think I need to see examples to understand this</p>

#### [ Patrick Massot (Oct 09 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135491213):
<p>I have no idea where to start</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135491595):
<p>Patrick I have heard Chris moaning about this <code>heq</code> stuff. But I have never once had to use it? Why is that? Am I avoiding a certain kind of mathematics? Why do you need it?</p>

#### [ Reid Barton (Oct 09 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135491658):
<p>When you didn't use the identity map as a map from <code>F (id '' U)</code> to <code>F U</code>, this is the kind of thing you avoided.</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135492132):
<p>Yes I just went back to that thread.</p>

#### [ Andrew Ashworth (Oct 09 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135492200):
<p>I found a pretty good summary of all the different types of equality here: <a href="https://jozefg.bitbucket.io/posts/2014-08-06-equality.html" target="_blank" title="https://jozefg.bitbucket.io/posts/2014-08-06-equality.html">https://jozefg.bitbucket.io/posts/2014-08-06-equality.html</a></p>

#### [ Patrick Massot (Oct 09 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20hell%20again/near/135492206):
<p>I have no idea what heq is. I can only tell you that when arguments of a term depend on other arguments then <code>rw</code> and <code>simp</code> often don't work. <code>convert</code> works but spawns <code>heq</code> goals. I understand nothing about Mario's explanations unfortunately</p>


{% endraw %}
