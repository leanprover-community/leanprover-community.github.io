---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/14331simpequalityandinstances.html
---

## Stream: [new members](index.html)
### Topic: [simp, equality, and instances](14331simpequalityandinstances.html)

---


{% raw %}
#### [ Simon Winwood (Sep 25 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%2C%20equality%2C%20and%20instances/near/134561065):
<p>Hi, I am trying to prove that list intersection with a singleton list is essentially a filter, and get this sub-goal:</p>
<div class="codehilite"><pre><span></span>lemma filter_mem_singleton_is_filter_eq {a} [decidable_eq a] {x : a} {xs : list a}:
  filter (λy, y ∈ [x]) xs = filter (λy, y = x) xs :=
</pre></div>


<p>this is more or less trivial, but for the implicite <code>decidable</code> term in the filter.  When I rewrite the mem term to be eq, the terms look like:</p>
<div class="codehilite"><pre><span></span>a : Type u_1,
_inst_1 : decidable_eq a,
x : a,
xs : list a
⊢ @filter a (λ (y : a), y = x)
      (@eq.rec (a → Prop) (λ (y : a), y ∈ [x]) (@decidable_pred a)
         (λ (a_1 : a), @list.decidable_mem a _inst_1 a_1 [x])
         (λ (y : a), y = x)
         _)
      xs =
    @filter a (λ (y : a), y = x) (λ (a : a), _inst_1 a x) xs
</pre></div>


<p>where the terms are equal but for the instance terms (after <code>simp, dsimp</code>).  I have run into this before, but managed to find a workaround.  My questions is: is this common, and what is the solution, or am I doing something that is very un-lean?</p>

#### [ Mario Carneiro (Sep 25 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%2C%20equality%2C%20and%20instances/near/134561362):
<p>When you get to that goal, use <code>congr</code> to simplify it</p>

#### [ Mario Carneiro (Sep 25 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%2C%20equality%2C%20and%20instances/near/134561367):
<p>before the rw</p>

#### [ Simon Winwood (Sep 25 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%2C%20equality%2C%20and%20instances/near/134561425):
<p>oh, nice, that works.</p>

#### [ Mario Carneiro (Sep 25 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%2C%20equality%2C%20and%20instances/near/134561432):
<p><code>congr</code> knows about subsingleton arguments and will automatically prove they are equal. In this case <code>decidable p</code> is a subsingleton</p>

#### [ Simon Winwood (Sep 25 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%2C%20equality%2C%20and%20instances/near/134561678):
<p>and a follow-on - is there somewhere I should be sending the lemmas I prove?  They look like they should be in the standard library, but I don't know the protocol for submitting them.  These are lemmas like the interaction between list.inter and const etc..</p>

#### [ Mario Carneiro (Sep 25 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%2C%20equality%2C%20and%20instances/near/134561916):
<p>This should probably be going into <a href="https://github.com/leanprover/mathlib" target="_blank" title="https://github.com/leanprover/mathlib">mathlib</a>. The core library is frozen and does not accept PRs</p>

#### [ Mario Carneiro (Sep 25 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%2C%20equality%2C%20and%20instances/near/134562029):
<p>Although I'm not sure I want this particular theorem, it seems a bit specialized... Both sides are equivalent to <code>list.repeat x (xs.count x)</code></p>

#### [ Simon Winwood (Sep 25 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%2C%20equality%2C%20and%20instances/near/134562143):
<p>This is a helper lemma, so maybe not.  It looks like mathlib has a bunch of lemmas which may do what I want, anyway.  Thanks!</p>


{% endraw %}
