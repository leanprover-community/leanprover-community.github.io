---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/70927homology.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [homology](https://leanprover-community.github.io/archive/116395maths/70927homology.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Aug 21 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homology/near/132522372):
<p>what is the progress of simplicial/singular homology?</p>

#### [ Kevin Buzzard (Aug 21 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homology/near/132529629):
<p>I guess Luca Gerolla is doing fundamental groups and that's all I know.</p>

#### [ Reid Barton (Aug 21 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homology/near/132530694):
<p>I think Johan Commelin has been refactoring the construction of singular homology (<a href="https://github.com/leanprover/mathlib/pull/144" target="_blank" title="https://github.com/leanprover/mathlib/pull/144">https://github.com/leanprover/mathlib/pull/144</a>) in <code>category</code>-theoretic terms, but he's currently on vacation AFAIK.</p>

#### [ Reid Barton (Aug 21 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homology/near/132531611):
<p>Obvious goals would be to prove that simplicial homology satisfies the Eilenberg-Steenrod axioms (homotopy invariance, additivity, dimension axiom etc.) I don't think anyone has taken a crack at this. I'm not even sure of the best way to organize the theory here--this is one question I'm very interested in.</p>

#### [ Reid Barton (Aug 21 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homology/near/132531710):
<p>My feeling is that typing Hatcher into Lean is probably not the best approach.</p>

#### [ Johan Commelin (Aug 21 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homology/near/132531986):
<p>Right, I haven't been doing much Lean the last two weeks. This should change, next week in Orsay (-;</p>

#### [ Johan Commelin (Aug 21 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homology/near/132532041):
<p>Also, I've been looking into too many different directions in Lean. I should get back to the homology project (-;</p>

#### [ Johan Commelin (Aug 21 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homology/near/132534122):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Was there something specific you were looking for or aiming at?</p>

#### [ Kenny Lau (Aug 21 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homology/near/132534124):
<p>not really</p>

#### [ Patrick Massot (Aug 21 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homology/near/132540359):
<blockquote>
<p>My feeling is that typing Hatcher into Lean is probably not the best approach.</p>
</blockquote>
<p>From a fun project perspective, typing parts of Hatcher could be nice, but this is certainly not the way to go for mathlib. Hatcher is too pedagogical. We certainly need something more abstract and systematic. What Johan did is already more abstract, since it's based on simplicial sets. But clearly we also need abstract homological algebra for lots of other stuff.</p>


{% endraw %}
