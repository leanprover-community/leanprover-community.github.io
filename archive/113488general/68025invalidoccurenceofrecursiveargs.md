---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68025invalidoccurenceofrecursiveargs.html
---

## Stream: [general](index.html)
### Topic: [invalid occurence of recursive args](68025invalidoccurenceofrecursiveargs.html)

---

#### [Zesen Qian (Jun 20 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurence%20of%20recursive%20args/near/128381305):
Not sure if it's a place for routine trouble shooting, but I'm trying to do some theory inside lean, I defined a inductive family but lean is not happy with it. https://ptpb.pw/3O0a
The error is at the constructor satlem, "invalid occurence of recursive arg#5, the body of the functional type depends on it".

#### [Mario Carneiro (Jun 20 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurence%20of%20recursive%20args/near/128381813):
I don't think lean likes that you have placed the recursive argument before the variable `v`

#### [Mario Carneiro (Jun 20 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurence%20of%20recursive%20args/near/128381941):
you had:
```
| satlem (c : context) (cl cl' : clause) :
  proof c (type.holds cl) → 
  ∀ v : string, proof ((v, type.holds cl) :: c) (type.holds cl') →
  proof c (type.holds cl')
```
This works:
```
| satlem (c : context) (cl cl' : clause) :
  ∀ v : string, proof c (type.holds cl) → 
  proof ((v, type.holds cl) :: c) (type.holds cl') →
  proof c (type.holds cl')
```
Or maybe you got the parentheses wrong? This works too, but means something different:
```
| satlem (c : context) (cl cl' : clause) :
  proof c (type.holds cl) → 
  (∀ v : string, proof ((v, type.holds cl) :: c) (type.holds cl')) →
  proof c (type.holds cl')
```

#### [Zesen Qian (Jun 20 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurence%20of%20recursive%20args/near/128382752):
Thanks! this works. I also fixed similar issues in the code.
question tho: why is this required? intuitively I don't see how it's invalid.

#### [Mario Carneiro (Jun 20 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurence%20of%20recursive%20args/near/128383088):
There was a restriction along the lines that recursive arguments must come after non-recursive args, mostly for convenience of implementation, but last I checked that restriction had been lifted, so I'm not sure why you are getting the error still

#### [Zesen Qian (Jun 20 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurence%20of%20recursive%20args/near/128383377):
maybe because it's inductive family, so impl. could be harder.

#### [Gabriel Ebner (Jun 21 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurence%20of%20recursive%20args/near/128403732):
There is still a restriction on *dependent* arguments, none of the arguments after the first recursive argument may occur in other arguments.  In this case `v` comes after the first recursive argument and occurs in the second recursive argument.

