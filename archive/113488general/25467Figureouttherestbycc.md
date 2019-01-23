---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/25467Figureouttherestbycc.html
---

## Stream: [general](index.html)
### Topic: [Figure out the rest by cc](25467Figureouttherestbycc.html)

---

#### [Johan Commelin (Aug 02 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130779658):
Can I tell Lean to work out the rest `by cc`:
```lean
import algebra.module

variables {R : Type} [ring R]

open punit

def zero_module : module R punit :=
  { smul := λ _ _, star,
    zero := star,
    add  := λ _ _, star,
    neg  := λ _, star,
    add_zero := by cc,
    zero_add := by cc,
    add_comm := by cc,
    add_left_neg := by cc,
    one_smul := by cc,
    mul_smul := by cc,
    add_smul := by cc,
    smul_add := by cc,
    add_assoc := by cc }

```

#### [Johan Commelin (Aug 02 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130779703):
I found that I was repeating myself, while trying to make a point to Lean.

#### [Scott Morrison (Aug 02 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130779783):
sure, something like: 
```
begin
  refine 
  { smul := λ _ _, star,
    zero := star,
    add  := λ _ _, star,
    neg  := λ _, star,
    .. } ; cc
end
```

#### [Johan Commelin (Aug 02 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130779915):
Aaah, I need to understand `refine`.

#### [Scott Morrison (Aug 02 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780063):
Curiously that doesn't actually work...

#### [Scott Morrison (Aug 02 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780069):
Of course, replacing `cc` with `obviously` does it. :-)

#### [Scott Morrison (Aug 02 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780103):
In fact just `by obviously` should work, except for some reason `split` doesn't work on modules, for some reason I can't see at the moment (type class inference throws an error?)

#### [Johan Commelin (Aug 02 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780108):
`finish` works instead of `cc`.

#### [Kenny Lau (Aug 02 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780164):
what is `obviously`? is it in mathlib?

#### [Johan Commelin (Aug 02 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780199):
No, it is Scott's Hammer.

#### [Johan Commelin (Aug 02 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780206):
Well, maybe `tidy` is his hammer.

#### [Sean Leather (Aug 02 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780270):
[`obviously`](https://github.com/semorrison/lean-tidy/blob/master/src/tidy/tidy.lean#L81)

#### [Johan Commelin (Aug 02 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780292):
So, the current golf record is:
```lean
def zero_module' : module R punit :=
by refine
{ add := λ x y, punit.star,
  zero := punit.star,
  neg := λ x, punit.star,
  smul := λ c x, punit.star,
  .. }; finish
```

#### [Kenny Lau (Aug 02 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780309):
gadvardammt finish

#### [Johan Commelin (Aug 02 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780310):
Let's assume we open `punit`.

#### [Scott Morrison (Aug 02 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780403):
If someone can explain to me why you can't `split` when the goal is a module, maybe I can golf the entire proof to `by tidy`.

#### [Kenny Lau (Aug 02 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780415):
isn't the right command `constructor`

#### [Kenny Lau (Aug 02 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780432):
`split` is for inductive types I think

#### [Johan Commelin (Aug 02 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780438):
`constructor` also fails...

