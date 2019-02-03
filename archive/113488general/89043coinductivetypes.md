---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89043coinductivetypes.html
---

## Stream: [general](index.html)
### Topic: [coinductive types](89043coinductivetypes.html)

---


{% raw %}
#### [ Kevin Buzzard (Feb 28 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123081684):
<p>Can someone (<span class="user-mention" data-user-email="simon.hudon@gmail.com" data-user-id="110026">@Simon Hudon</span> ?) explain what a coinductive type is and, more specifically, whether a mathematician would ever need them?</p>

#### [ Kevin Buzzard (Feb 28 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123081788):
<p>As to the comments about them made here and linked to here, this might be another of those "perfect is the enemy of good" situations where we could either have Simon's "does the job to a certain extent", or the observation that one could do this much better if only we could find a Lean C++ hacker that just sat down and wrote a bunch of complicated working code, I would vote for Simon any day of the week.</p>

#### [ Mario Carneiro (Feb 28 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123081900):
<p>We don't need a C++ hacker for this one. I hope to implement the next version of (co)inductive types in lean</p>

#### [ Sean Leather (Feb 28 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123081904):
<p><span class="user-mention" data-user-email="k.buzzard@imperial.ac.uk" data-user-id="110038">@Kevin Buzzard</span>: <a href="https://plato.stanford.edu/entries/nonwellfounded-set-theory/" target="_blank" title="https://plato.stanford.edu/entries/nonwellfounded-set-theory/">Non-wellfounded Set Theory</a> might help.</p>

#### [ Mario Carneiro (Feb 28 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123081913):
<p>Mathematically, the theory of coinductive types is very elegantly dual to the theory of inductive types. A simple example of a coinductive type is the type of "possibly infinite lists", which is defined with the same clauses as <code>list</code></p>

#### [ Mario Carneiro (Feb 28 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123081955):
<p>This is a type that contains the empty list, finite lists, as well as all infinite lists (a.k.a "streams")</p>

#### [ Mario Carneiro (Feb 28 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123082040):
<p>(These are often called <code>llist</code> or "lazy lists" for reasons to come.) The type <code>llist</code> has a <code>cases_on</code>, i.e. you can ask for any <code>llist</code> whether it is nil or a cons of an element and a <code>llist</code>, but there is no <code>rec</code>, because a <code>llist</code> is not well founded</p>

#### [ Simon Hudon (Feb 28 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123102878):
<p>There's also:<br>
<span class="user-mention" data-user-email="intoverflow@gmail.com" data-user-id="110028">@Tim Carstens</span> </p>
<blockquote>
<p>terminal co-algebra of an endofunctor, instead of initial algebra of an endofunctor</p>
</blockquote>
<p>if you want to look at them in terms of category theory</p>

#### [ Simon Hudon (Feb 28 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123103022):
<p><code>llist</code> are easy enough without <code>coinductive</code> types but I imagine if you care about (possibly) infinite objects such as trees, it will be hard to study them without coinductive types.</p>
<p>I personally care about them mostly for modelling programs that do not terminate such as operating systems, controllers for pacemakers or any internet protocol</p>

#### [ Tim Carstens (Feb 28 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123103123):
<p>maybe bass-serre theory, aka doing group theory by way of group actions on (infinite) trees</p>

#### [ Tim Carstens (Feb 28 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123103136):
<p>i'm struggling to think up examples from pure math where coinductives would be handy</p>

#### [ Tim Carstens (Feb 28 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123103143):
<p>it's a big world out there though</p>


{% endraw %}
