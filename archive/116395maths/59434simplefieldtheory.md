---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/59434simplefieldtheory.html
---

## Stream: [maths](index.html)
### Topic: [simple field theory](59434simplefieldtheory.html)

---


{% raw %}
#### [ Joey van Langen (Dec 04 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150851783):
<p>I would like to work on some simple results about fields to contribute to the math library. Results that seem achievable are: field extensions and their degree, splitting fields, the existence and uniqueness of finite fields, maybe some galois theory. Is anyone working in this direction? If so, what has already been done?</p>

#### [ Johan Commelin (Dec 04 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150852014):
<p>There is a branch <code>splitting_fields</code> on the community repo.</p>

#### [ Johan Commelin (Dec 04 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150852027):
<p>Also: welcome!</p>

#### [ Johan Commelin (Dec 04 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150852057):
<p>I think that branch has a definition of the splitting field, but not yet the proofs of the interesting properties.</p>

#### [ Johan Commelin (Dec 04 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150852105):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Defined the perfect closure of a field.</p>

#### [ Johan Commelin (Dec 04 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150852152):
<p>See <code>field_theory/perfect_closure.lean</code>.</p>

#### [ Johan Commelin (Dec 04 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150852231):
<p>In general, Kenny and <span class="user-mention" data-user-id="110044">@Chris Hughes</span> have been doing some stuff. So it would be good to check with them before you start big projects.</p>

#### [ Johan Commelin (Dec 04 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150852242):
<p>I think Kenny has most of the definition of algebraic closure.</p>

#### [ Johan Commelin (Dec 04 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150852280):
<p>Uniqueness of finite fields isn't there, as far as I know. Galois theory is completely missing. But I'dd love to see it there, so please work on it <span class="emoji emoji-1f603" title="smiley">:smiley:</span></p>

#### [ Joey van Langen (Dec 04 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150852444):
<p>Thanks for all the information. Looking at the sources you mentioned now</p>

#### [ Johan Commelin (Dec 04 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150852528):
<p>If you decide to work on splitting fields, it shouldn't be hard to give you access to the community repo, so that you can push your contributions</p>

#### [ Chris Hughes (Dec 04 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150853364):
<blockquote>
<p>In general, Kenny and <span class="user-mention" data-user-id="110044">@Chris Hughes</span> have been doing some stuff. So it would be good to check with them before you start big projects.</p>
</blockquote>
<p>I haven't done anything that hasn't been merged.</p>

#### [ Johan Commelin (Dec 04 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150853530):
<p>Right, but it would also be a pity if people redid stuff that you did that isn't merged.</p>

#### [ Kenny Lau (Dec 04 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150853615):
<p>I wrote a roadmap once</p>

#### [ Kenny Lau (Dec 04 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150853674):
<p><a href="https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md">https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md</a><br>
<a href="https://github.com/kckennylau/Lean/blob/master/Galois-theory-roadmap.md" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/Galois-theory-roadmap.md">https://github.com/kckennylau/Lean/blob/master/Galois-theory-roadmap.md</a><br>
<a href="https://github.com/semorrison/lean-category-theory/blob/master/schemes_roadmap.md" target="_blank" title="https://github.com/semorrison/lean-category-theory/blob/master/schemes_roadmap.md">https://github.com/semorrison/lean-category-theory/blob/master/schemes_roadmap.md</a></p>

#### [ Kevin Buzzard (Dec 04 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150854972):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> why not make your roadmaps into mathlib issues? They'd be easier to find.</p>

#### [ Scott Morrison (Dec 04 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150869896):
<p>My student <span class="user-mention" data-user-id="137449">@Aditya Agarwal</span> has expressed some interest in doing some Galois theory over the summer. He's at a conference at the moment, so I'm not sure if he's started on anything yet.</p>

#### [ Kevin Buzzard (Dec 04 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150875160):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> you presumably mean Aussie summer i.e. right now?</p>

#### [ Chris Hughes (Dec 12 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/151553124):
<p>I've started work on splitting fields <a href="#narrow/stream/116395-maths/topic/Splitting.20fields" title="#narrow/stream/116395-maths/topic/Splitting.20fields">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting.20fields</a></p>


{% endraw %}
