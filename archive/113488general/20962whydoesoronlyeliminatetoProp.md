---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20962whydoesoronlyeliminatetoProp.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [why does or only eliminate to Prop?](https://leanprover-community.github.io/archive/113488general/20962whydoesoronlyeliminatetoProp.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Mar 22 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124063589):
<p>I just noticed this. Chris Hughes wrote a proof for me, but in my application of his proof I have a function from <code>fin n</code> to <code>nat</code>, and he has implemented his proof using a function from <code>nat</code> to <code>nat</code> which he only ever evaluates at numbers less than <code>n</code>. Given my function from <code>fin n</code> to <code>nat</code> I hence need to come up with a function from <code>nat</code> to <code>nat</code> which extends it and I thought I'd just define it using <code>or.elim (decidable.em (i&lt;n))</code> but this won't work because the target can't be <code>nat</code>.</p>

#### [ Chris Hughes (Mar 22 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124063639):
<p>You can using choice, but ite is probably more natural</p>

#### [ Chris Hughes (Mar 22 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124063654):
<p><code>p or ¬p</code> is not as strong as <code>decidable p</code></p>

#### [ Kevin Buzzard (Mar 22 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124063729):
<p>I had trouble eliminating <code>dite</code> a couple of weeks ago because I couldn't remember <code>dif_pos</code>. Why isn't it called <code>dite.elim_true</code> or something?</p>

#### [ Mario Carneiro (Mar 22 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124064130):
<p>If you want to eliminate on a decidable proposition, <code>dite</code> is the standard way. You can't eliminate from an <code>or</code> to a type because the or doesn't contain information about which disjunct is true (it's been forgotten in proof irrelevance), and you can't recover the data once you drop it.</p>

#### [ Mario Carneiro (Mar 22 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124064215):
<p>Also, <code>simp</code> will simplify with <code>dif_pos</code> and its friends, I usually prefer that to using the names explicitly</p>

#### [ Kevin Buzzard (Mar 22 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124064628):
<p>I was preparing myself for the fact that <code>dite</code> will be removed from Lean 4 ;-)</p>

#### [ Chris Hughes (Mar 24 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124151668):
<p>The other reason, which only just occurred to me, is that if both sides of your <code>or</code> are true, then your function is defined to be two different things.</p>

#### [ Chris Hughes (Mar 24 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152040):
<p>I'm just trying to work out in general which inductive predicates can eliminate into Sort, and which only eliminate into Prop. It's not that obvious why something like acc doesn't have this problem, and can eliminate into Sort.</p>

#### [ Mario Carneiro (Mar 24 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152052):
<p>the basic idea is that there should only be one way to construct an element of an inductive prop if you want large elimination</p>

#### [ Mario Carneiro (Mar 24 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152093):
<p>that's why it is called subsingleton elimination</p>

#### [ Mario Carneiro (Mar 24 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152142):
<p>There are two proofs of <code>p \/ q</code>, which are equal by proof irrelevance, so inversion would be inconsistent</p>

#### [ Mario Carneiro (Mar 24 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152150):
<p>similarly there are multiple ways to prove <code>\ex x. p x</code> by giving different witnesses, so you can't extract the witness</p>

#### [ Mario Carneiro (Mar 24 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152201):
<p>The general rule is described in my paper, in the section "large elimination"</p>

#### [ Simon Hudon (Mar 24 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152304):
<p>Do you know the reason behind the choice of making universes non-cumulative?</p>

#### [ Mario Carneiro (Mar 24 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152533):
<p>It simplifies a lot of things</p>

#### [ Mario Carneiro (Mar 24 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152574):
<p>cumulativity would break unique typing, for one</p>

#### [ Mario Carneiro (Mar 24 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152580):
<p>you have to have a subtyping relation, which interacts with everything in the type theory in nontrivial ways</p>

#### [ Simon Hudon (Mar 24 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152622):
<p>Oh? I didn't think you'd need a subtype relation just because of the universes</p>

#### [ Mario Carneiro (Mar 24 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152623):
<p>I was thinking about extending my analysis to Coq, but it would not be a small modification</p>

#### [ Mario Carneiro (Mar 24 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152668):
<p>you have to also have stuff like <code>A -&gt; Sort 1 &lt;= A -&gt; Sort 2</code></p>

#### [ Simon Hudon (Mar 24 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20does%20or%20only%20eliminate%20to%20Prop%3F/near/124152723):
<p>... and now that I think of it, might get tricky for generic monadic code, if you want to allow<code>m α</code> <code>m β</code> even when <code>α</code>, <code>β</code> are in different universes. You might need covariance / contravariance hints in the type of <code>m</code></p>


{% endraw %}
