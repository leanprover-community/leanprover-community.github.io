---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/59016leancomplexnumber.html
---

## Stream: [new members](index.html)
### Topic: [#lean #complex number](59016leancomplexnumber.html)

---


{% raw %}
#### [ VeraZZ (Jul 10 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129414919):
<p>hey I intend to write a proof of an equation where the RHS is real and LHS is a sum of a pair of  complex conjugates but it keeps telling the error that the terms on RHS should have type \real . how am I supposed to fix it ? thanks</p>

#### [ Kenny Lau (Jul 10 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129415017):
<p>you need to make the real number complex</p>

#### [ Kenny Lau (Jul 10 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129415049):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">complex</span><span class="bp">.</span><span class="n">basic</span>

<span class="bp">#</span><span class="kn">check</span> <span class="bp">λ</span> <span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">,</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (Jul 10 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129415117):
<p>Isn't there automatic coercion?</p>

#### [ Johan Commelin (Jul 10 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129415139):
<p>If the LHS is complex, I would think that the RHS would be coerced automatically. (Otoh, if LHS is real and RHS is complex, then Lean will start complaining, or you have to coerce manually.)</p>

#### [ Kevin Buzzard (Jul 10 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129416182):
<p><span class="user-mention" data-user-id="120352">@VeraZZ</span> if <code>x</code> is a real number then <code>(x : ℂ)</code> is an attempt to force <code>x</code> to be a complex number.</p>

#### [ Kevin Buzzard (Jul 10 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129416642):
<p>but the complex number isn't <code>x</code>, it's written <code>↑x : ℂ</code></p>

#### [ Kevin Buzzard (Jul 10 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129416647):
<p>because you applied a secret function to x</p>

#### [ Kevin Buzzard (Jul 10 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129416650):
<p>which almost certainly has a name</p>

#### [ Kenny Lau (Jul 10 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129416653):
<p>but <code>(x : ℂ)</code> shows that the coercion is automatic</p>

#### [ Kevin Buzzard (Jul 10 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129416713):
<p>aha</p>

#### [ Kevin Buzzard (Jul 10 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129416733):
<p>it's <code>complex.of_real : ℝ → ℂ</code> of course. That's the name for the explicit injection from the reals to the complexes.</p>

#### [ VeraZZ (Jul 11 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129469902):
<p>the LHS is actually a function which gives the inner product of two complex variables (so it is real).Is there a way to make the output of the function complex ?</p>

#### [ Mario Carneiro (Jul 11 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129469962):
<p>this is what the coercion does</p>

#### [ Mario Carneiro (Jul 11 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129469980):
<p>just write <code>( ... : ℂ)</code> around your real term and then it will be "cast" to complex</p>

#### [ VeraZZ (Jul 11 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%23lean%20%23complex%20number/near/129470001):
<p>aha thanks !</p>


{% endraw %}
