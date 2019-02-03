---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30658automation.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [automation](https://leanprover-community.github.io/archive/113488general/30658automation.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Jun 05 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automation/near/127574167):
<p>I was just having a look at <span class="user-mention" data-user-id="110044">@Chris Hughes</span>'s nice PR for quotient groups.</p>

#### [ Scott Morrison (Jun 05 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automation/near/127574170):
<p>I golfed it a bit, using my "obviously" and "tidy" tactics, and would like to see how people feel about the result.</p>

#### [ Scott Morrison (Jun 05 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automation/near/127574180):
<p>Chris's  proof is at &lt;<a href="https://github.com/leanprover/mathlib/pull/154/commits/b7edcbdd1f783da5f17dcd840057352157afdac0" target="_blank" title="https://github.com/leanprover/mathlib/pull/154/commits/b7edcbdd1f783da5f17dcd840057352157afdac0">https://github.com/leanprover/mathlib/pull/154/commits/b7edcbdd1f783da5f17dcd840057352157afdac0</a>&gt;.</p>

#### [ Scott Morrison (Jun 05 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automation/near/127574222):
<p>I factored this into essentially three bits: 2 lemmas about elements in normal subgroups, a few "hints" for my automation, and then the following proof:</p>

#### [ Scott Morrison (Jun 05 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automation/near/127574225):
<div class="codehilite"><pre><span></span>instance quotient_group&#39; [group α] (s : set α) [normal_subgroup s] : group (left_cosets s) :=
by refine
{ one := ⟦1⟧,
  mul := λ a b, quotient.lift_on₂ a b (λ a b, ⟦a * b⟧) (by obviously),
  inv := λ a&#39;,  quotient.lift_on  a&#39;  (λ a, ⟦a⁻¹⟧)     (by obviously),
  .. }; obviously
</pre></div>

#### [ Scott Morrison (Jun 05 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automation/near/127574227):
<p>which is about as easy on the eye as I think one can hope for.</p>

#### [ Scott Morrison (Jun 05 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automation/near/127574235):
<p>The lemmas are:</p>
<div class="codehilite"><pre><span></span>lemma quotient_group_aux  [group α] (s : set α) [normal_subgroup s] (a b : α) (h : a⁻¹ * b ∈ s) : a * b⁻¹ ∈ s :=
begin
  rw [← inv_inv a, ← mul_inv_rev],
  exact is_subgroup.inv_mem (is_subgroup.mem_norm_comm h),
end

lemma quotient_group_aux&#39; [group α] (s : set α) [normal_subgroup s] (a b c d : α) (h₁ : a * b ∈ s) (h₂ : c * d ∈ s) : c * (a * (b * d)) ∈ s :=
begin
  apply is_subgroup.mem_norm_comm,
  rw [← mul_assoc, mul_assoc],
  apply (is_subgroup.mul_mem_cancel_right s h₁).2,
  exact is_subgroup.mem_norm_comm h₂
end
</pre></div>

#### [ Scott Morrison (Jun 05 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automation/near/127574311):
<p>which are dull variants on what Chris had done, just extracted out. I made no attempt to automate those, but I think it's not too much a stretch to hope that one could explain to a computer how to do these.</p>

#### [ Scott Morrison (Jun 05 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automation/near/127574316):
<p>The ugly part of my "obviously-golfed" version is the "hints": before the nice instance proof I need to say:</p>
<div class="codehilite"><pre><span></span>-- Some &#39;hint&#39; attributes for obviously.
local attribute [reducible] setoid_has_equiv left_rel
local attribute [applicable] is_submonoid.one_mem  -- `applicable` means the lemma should be applied whenever relevant
local attribute [semiapplicable] quotient_group_aux quotient_group_aux&#39; -- `semiapplicable` means the lemma should be applied if all its hypotheses can be satisfied from the context
local attribute [simp] mul_assoc
</pre></div>

#### [ Scott Morrison (Jun 05 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automation/near/127574324):
<p>The whole thing is available at &lt;<a href="https://github.com/semorrison/lean-tidy/blob/master/examples/quotient_group.lean" target="_blank" title="https://github.com/semorrison/lean-tidy/blob/master/examples/quotient_group.lean">https://github.com/semorrison/lean-tidy/blob/master/examples/quotient_group.lean</a>&gt;.</p>

#### [ Scott Morrison (Jun 05 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automation/near/127574427):
<p>(Regarding the hints: <code>attribute [applicable] is_submonoid.one_mem</code> would become a global attribute in my dream world --- whenever the goal is to prove <code>1 ∈ s</code>, for <code>s</code> a monoid, you should let the computer do that for you. :-) With another simple lemma about normal subgroups, one could do without the <code>attribute [simp] mul_assoc</code> hint, which is pretty fragile.)</p>

#### [ Scott Morrison (Jun 05 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automation/near/127576401):
<p>(On the subject of the two lemmas, once we have PIDs and Smith normal form, we can write a general purpose tactic which shows whether a given word lies in the normal subgroup generated by some collection of words, and hence prove goals of the form <code>w \mem s</code>, given one or more hypotheses of the same form.)</p>

#### [ Scott Morrison (Jun 05 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automation/near/127576415):
<p>(Such a tactic would remove the need for both the <code>semiapplicable</code> and <code>simp</code> hints above.)</p>

#### [ Johan Commelin (Jun 05 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automation/near/127583599):
<p>Wow! That's some nice golfing. And golfing where you increase readability, instead of obfuscating!</p>

#### [ Johan Commelin (Jun 05 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automation/near/127583641):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Don't you think these tactics would help a lot with the perfectoid project?</p>

#### [ Johan Commelin (Jun 05 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automation/near/127583645):
<p>If we want to produce code that is somewhat legible to mathematicians.</p>

#### [ Kevin Buzzard (Jun 05 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automation/near/127585727):
<p>I am pretty sure that these tactics will make life much easier for mathematicians. Goodness knows if I will be able to use them. I have no idea of the problems I'll face with perfectoid spaces.</p>

#### [ Patrick Massot (Jun 05 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automation/near/127586790):
<p>Automation is clearly the key. Proof assistants can become useful tools for mathematicians only if every stupid proof eventually gets automatic</p>


{% endraw %}
