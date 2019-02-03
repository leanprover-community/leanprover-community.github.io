---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/76453Sorryofwrongtype.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Sorry of wrong type!](https://leanprover-community.github.io/archive/113488general/76453Sorryofwrongtype.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Moses Schönfinkel (Mar 21 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124004577):
<p>Heh...</p>
<div class="codehilite"><pre><span></span><span class="n">type</span> <span class="n">mismatch</span> <span class="n">at</span> <span class="n">field</span> <span class="err">&#39;</span><span class="n">le_refl&#39;</span>
  <span class="n">sorry</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="err">?</span><span class="n">m_1</span> <span class="n">a</span> <span class="n">a</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">a</span>
</pre></div>

#### [ Mario Carneiro (Mar 21 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124004587):
<p>did you put <code>sorry</code> for the definition of <code>le</code> as well?</p>

#### [ Mario Carneiro (Mar 21 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124004627):
<p><code>le := _, le_refl := sorry</code> will error</p>

#### [ Moses Schönfinkel (Mar 21 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124004630):
<p>Yes :). I just sorried everything to build it incrementally, I know I don' goof'd, it's just amusing that sorry can actually fail to typecheck.</p>

#### [ Moses Schönfinkel (Mar 21 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124004634):
<p>Indeed! :)</p>

#### [ Moses Schönfinkel (Mar 21 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124004641):
<p>It's the first time I've seen <code>sorry</code> being red-squiggled in Lean</p>

#### [ Mario Carneiro (Mar 21 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124004706):
<p>I think it is having difficulty unifying the types, this would happen also if you tried to use something of type <code>\forall {x : Type*}. x</code></p>

#### [ Moses Schönfinkel (Mar 21 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124004853):
<p>So I guess  sorry first needs to know the type and then gives you a bogus term thereof, rather than just "closing the goal" as if by magic? Would the latter behaviour lead to weirdness in scenarios where something depends on a (presumably temporary) sorry?</p>

#### [ Mario Carneiro (Mar 21 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124004895):
<p>I think the problem has to do with unresolved metavariables in the type</p>

#### [ Mario Carneiro (Mar 21 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124004947):
<p>You should always be able to sorry everything, but you have to work from the beginning, from the nondependent <code>sorry</code>s to the dependent ones</p>

#### [ Moses Schönfinkel (Mar 21 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124005016):
<p>Right. It's just interesting that sorry cares about anything at all :)! So for example, <code>{ le := sorry, le_refl := sorry ... }</code> would work but <code>{ le := _, le_refl := sorry ... }</code> would not.</p>

#### [ Kevin Buzzard (Mar 21 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124005487):
<p>I got sorry red-squiggled about 2 weeks ago, for probably the first time. I awarded myself an achievement.</p>

#### [ Mario Carneiro (Mar 21 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124005556):
<p>It's like the dual problem of proving an inconsistency :)</p>

#### [ Kevin Buzzard (Mar 21 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124006030):
<p><a href="#narrow/stream/113488-general/subject/too.20many.20axioms.20in.20comm_ring.20class/near/123391025" title="#narrow/stream/113488-general/subject/too.20many.20axioms.20in.20comm_ring.20class/near/123391025">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/too.20many.20axioms.20in.20comm_ring.20class/near/123391025</a></p>


{% endraw %}
