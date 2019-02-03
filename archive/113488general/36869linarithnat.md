---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/36869linarithnat.html
---

## Stream: [general](index.html)
### Topic: [linarith & nat](36869linarithnat.html)

---


{% raw %}
#### [ Reid Barton (Sep 30 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134918920):
<p><span class="user-mention" data-user-id="110596">@Rob Lewis</span> I started remembering to use <code>linarith</code> to solve some easy goals like <code>f &lt; g -&gt; -f - -g &lt;= 0 -&gt; false</code>.<br>
Do you have a sense of how hard it would be to support <code>-</code> on nat? I guess at least in simple cases there should be a translation to a new linear system (maybe involving adding an extra variable).</p>

#### [ Rob Lewis (Sep 30 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919195):
<p>Yeah, there's a translation that can be done. My instinct: it would take more work to go from the current state to supporting <code>-</code> than it took to go from no <code>nat</code> support to here. The bigger worry is that these are all just stopgaps, ultimately we want <code>omega</code> or <code>cooper</code> or something nat/int specific. <code>linarith</code> will never work completely right on <code>nat</code>.</p>

#### [ Mario Carneiro (Sep 30 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919295):
<p>does linarith support <code>max</code> and <code>min</code>?</p>

#### [ Mario Carneiro (Sep 30 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919307):
<p>Maybe focus effort on that, and then you can get nat.sub easy by rewriting it to a <code>max</code></p>

#### [ Rob Lewis (Sep 30 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919411):
<p>Not natively. You can unfold them, <code>split_ifs</code>, and then call <code>linarith</code> a bunch of times. That's exactly how the translation would go, and it's not efficient, you get an explosion of <code>linarith</code> calls.</p>

#### [ Mario Carneiro (Sep 30 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919422):
<p>So <code>linarith</code> only handles convex regions?</p>

#### [ Mario Carneiro (Sep 30 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919468):
<p>You can interpret a <code>max</code> or <code>min</code> as a conjunction sometimes, and then there is no case split</p>

#### [ Mario Carneiro (Sep 30 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919470):
<p>but when the inequality is the wrong way you get a disjunction and have to case split</p>

#### [ Mario Carneiro (Sep 30 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919471):
<p>I don't see any way to avoid exponential blowup</p>

#### [ Reid Barton (Sep 30 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919525):
<p>Right, that makes sense.</p>

#### [ Rob Lewis (Sep 30 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919571):
<p>Yeah. <code>linarith</code> has no fancy logic handling at all, and again, I'm not sure how much it's worth bundling more and more into the current tactic. Eventually you just end up approximating an SMT solver.</p>

#### [ Reid Barton (Sep 30 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919572):
<p>On the other hand, sometimes the problems we want to solve are quite small. Like I had this one: define <code>def I (j : ℕ) : ℕ := if j ≤ e then e - j else j</code>, and then prove <code>lemma II {j : ℕ} : I (I j) = j</code>. (<code>e</code> is some constant nat.)</p>

#### [ Reid Barton (Sep 30 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134919620):
<p>Haha, that's the trick isn't it. Once you write the tactic to do X, then everything will start to look like "almost X, if only..."</p>

#### [ Kevin Buzzard (Sep 30 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134920648):
<p>With <code>ring</code> I started to learn how to use what we had to get what I wanted in two lines rather than one. For example if the goal is <code>(x+1)^2 &lt; x^2+2*x+2</code>then instead of thinking "a souped-up <code>ring</code> should make progress here" you prove <code>h : x^2+2*x+2=(x+1)^2+1 := by ring</code> and then rewrite. For <code>ring</code> in particular, having a very clear idea of exactly what it can and can't do is of great help to me, and I am beginning to understand <code>simp</code> and <code>dec_trivial</code> in the same way. I only wish I had a better grasp on what things like <code>cc</code>, <code>linarith</code> and <code>finish</code> did -- these are still tactics which I apply "randomly" in some sense (like how I used to apply <code>simp</code> when I was a beginner).</p>

#### [ Tobias Grosser (Sep 30 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134926271):
<p>We use (outside of the theorem proover world) a simplification and decision procedure for Presburger arithmetic based on linear programming / dual simplex.</p>

#### [ Tobias Grosser (Sep 30 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134926325):
<p>While probably the easiest is to implement omega / cooper / or Leo's extensions to cooper as used in Z3, I am interested in exploring an approach based on the mathematics implemented in a constraint based math library such as isl, visible e.g. at nhttp://playground.pollylabs.org/.</p>

#### [ Tobias Grosser (Sep 30 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20%26%20nat/near/134926332):
<p>I am interested to discuss this topic in more depth (and will also be in Freiburg).</p>


{% endraw %}
