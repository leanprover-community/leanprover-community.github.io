---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/09896isgrouphommul.html
---

## Stream: [general](index.html)
### Topic: [is_group_hom.mul](09896isgrouphommul.html)

---

#### [Kenny Lau (Apr 12 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970058):
This is what `is_group_hom.mul` looked like on [Apr 5](https://github.com/leanprover/mathlib/blob/22e671c5ed5fd1b891fb73aa10c9425d1c6cfd3d/algebra/group.lean#L493):
```
namespace is_group_hom
variables {f : α → β} (H : is_group_hom f)
include H

theorem mul : ∀ a b : α, f (a * b) = f a * f b := H
```
Now, the function variable became explicit, which broke some of my files. Are changes like this just going to happen randomly without any notice?

#### [Mario Carneiro (Apr 12 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970067):
short answer: yes

#### [Kenny Lau (Apr 12 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970068):
wonderful

#### [Mario Carneiro (Apr 12 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970106):
mathlib is not stable any more than lean itself is, be prepared for this sort of thing

#### [Kenny Lau (Apr 12 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970111):
https://github.com/leanprover/mathlib/commit/fa86d349527766c2d0fc3173fcda302cdd5673f3#diff-52b9e281e7667f88f8203fb617843d93L488

#### [Mario Carneiro (Apr 12 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970112):
It's not clear what kind of notice would be appropriate here in any case

#### [Kenny Lau (Apr 12 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970121):
so if i werent clever enough to know exactly that my files broke because they made this variable explicit, I'm just going to have to sit down for an hour?

#### [Kenny Lau (Apr 12 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970164):
also, this change broke `h.one` where `h` is the proof that some function is a group homomorphism

#### [Kenny Lau (Apr 12 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970165):
now I have to do `is_group_hom.one _ h`

#### [Mario Carneiro (Apr 12 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970166):
If you update and your files break, double check what changed in the update, should give you a hint at what to do

#### [Mario Carneiro (Apr 12 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970167):
or ask here, of coure

#### [Mario Carneiro (Apr 12 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970169):
Now you do `is_group_hom.one f` I think

#### [Kenny Lau (Apr 12 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970224):
right

#### [Kenny Lau (Apr 12 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970225):
suddenly `is_group_hom` became a class

#### [Kenny Lau (Apr 12 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970226):
and guess what

#### [Kenny Lau (Apr 12 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970227):
https://github.com/leanprover/mathlib/commit/fa86d349527766c2d0fc3173fcda302cdd5673f3#diff-52b9e281e7667f88f8203fb617843d93L515

#### [Mario Carneiro (Apr 12 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970228):
Complain to @**Scott Morrison** and @**Johannes Hölzl**, I think this change is still in its probationary period

#### [Kenny Lau (Apr 12 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970232):
before: `theorem inv (a : α) : (f a)⁻¹ = f a⁻¹`
after: `theorem inv (a : α) : f a⁻¹ = (f a)⁻¹`

#### [Kenny Lau (Apr 12 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970233):
really

#### [Mario Carneiro (Apr 12 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970240):
I agree with that change, it makes more sense the other way around to match with `one` and `mul`

#### [Mario Carneiro (Apr 12 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970294):
but one thing I will not do is avoid small consistency changes because of a worry of breaking things. Once you start doing that, it will only become more crufty as time goes on

