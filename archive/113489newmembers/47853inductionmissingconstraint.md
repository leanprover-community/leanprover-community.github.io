---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/47853inductionmissingconstraint.html
---

## Stream: [new members](index.html)
### Topic: [induction missing constraint](47853inductionmissingconstraint.html)

---


{% raw %}
#### [ Etienne Laurin (Sep 01 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133180811):
<p>Given <code>(a b : ℕ) (h : a ≤ b)</code>, after doing <code>induction h</code>, the <code>case less_than_or_equal.refl</code> doesn't have any hypothesis allowing to conclude <code>a = b</code>. Why not? Is there another way to perform induction that does introduce <code>a = b</code> in that case?</p>

#### [ Mario Carneiro (Sep 01 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133180865):
<p>in the refl case, you should already have <code>b</code> replaced by <code>a</code> in the goal</p>

#### [ Mario Carneiro (Sep 01 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133180929):
<p>By the way, I don't recommend doing induction on an le hypothesis. Instead, do induction on <code>a</code> and/or <code>b</code> and use lemmas on le to satisfy the induction hypothesis</p>

#### [ Etienne Laurin (Sep 01 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133181092):
<p>What if a and b are expressions? In this example, the goal is still <code>a ≤ b</code></p>
<div class="codehilite"><pre><span></span>example (a b : ℕ) (h : nat.succ a ≤ nat.succ b) : a ≤ b := begin
  induction h,
  case nat.less_than_or_equal.refl { sorry }
end
</pre></div>

#### [ Mario Carneiro (Sep 01 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133181104):
<p>use cases instead for that</p>

#### [ Mario Carneiro (Sep 01 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133181150):
<p>If you need to combine induction with the parameter equalities, you should first use <code>generalize h : nat.succ a</code> with all the variables you are holding fixed in the induction, then use <code>induction</code></p>

#### [ Etienne Laurin (Sep 01 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133181412):
<p>Thanks, that seems to work</p>

#### [ Etienne Laurin (Sep 01 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133181414):
<p>I haven't used a lot of explicit lemmas so far, I often have trouble finding the right one. I usually get by with a lot of unfold/delta/induction/cases followed by simp</p>

#### [ Mario Carneiro (Sep 01 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133181437):
<p>That's not very sustainable. I suggest learning to browse the source files of core lib and/or mathlib</p>

#### [ Etienne Laurin (Sep 01 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133181486):
<p>I recently discovered M-. will jump to lean and mathlib sources, I'll start using it more</p>

#### [ Mario Carneiro (Sep 01 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133181487):
<p>autocompletion also helps for discoverability, once you learn the naming convention</p>

#### [ Etienne Laurin (Sep 01 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133181653):
<p>Oh nice. But I notice that doesn't work too well if I haven't imported the right theory. Is there a better way to find lemmas than grep?</p>

#### [ Kevin Buzzard (Sep 01 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133181720):
<p><code>#find</code> might be helpful for you. But I would definitely recommend (a) learning the rules of thumb for lemma names and (b) the ctrl-space dance for auto-completion. If you're trying to prove something about int then just import <code>data.int.basic</code></p>


{% endraw %}
