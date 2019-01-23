---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/70927homology.html
---

## Stream: [maths](index.html)
### Topic: [homology](70927homology.html)

---


{% raw %}
#### [ Kenny Lau (Aug 21 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homology/near/132522372):
what is the progress of simplicial/singular homology?

#### [ Kevin Buzzard (Aug 21 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homology/near/132529629):
I guess Luca Gerolla is doing fundamental groups and that's all I know.

#### [ Reid Barton (Aug 21 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homology/near/132530694):
I think Johan Commelin has been refactoring the construction of singular homology (https://github.com/leanprover/mathlib/pull/144) in `category`-theoretic terms, but he's currently on vacation AFAIK.

#### [ Reid Barton (Aug 21 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homology/near/132531611):
Obvious goals would be to prove that simplicial homology satisfies the Eilenberg-Steenrod axioms (homotopy invariance, additivity, dimension axiom etc.) I don't think anyone has taken a crack at this. I'm not even sure of the best way to organize the theory here--this is one question I'm very interested in.

#### [ Reid Barton (Aug 21 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homology/near/132531710):
My feeling is that typing Hatcher into Lean is probably not the best approach.

#### [ Johan Commelin (Aug 21 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homology/near/132531986):
Right, I haven't been doing much Lean the last two weeks. This should change, next week in Orsay (-;

#### [ Johan Commelin (Aug 21 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homology/near/132532041):
Also, I've been looking into too many different directions in Lean. I should get back to the homology project (-;

#### [ Johan Commelin (Aug 21 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homology/near/132534122):
@**Kenny Lau** Was there something specific you were looking for or aiming at?

#### [ Kenny Lau (Aug 21 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homology/near/132534124):
not really

#### [ Patrick Massot (Aug 21 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homology/near/132540359):
```quote
My feeling is that typing Hatcher into Lean is probably not the best approach.
```
From a fun project perspective, typing parts of Hatcher could be nice, but this is certainly not the way to go for mathlib. Hatcher is too pedagogical. We certainly need something more abstract and systematic. What Johan did is already more abstract, since it's based on simplicial sets. But clearly we also need abstract homological algebra for lots of other stuff.


{% endraw %}
