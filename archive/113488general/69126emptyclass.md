---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/69126emptyclass.html
---

## Stream: [general](index.html)
### Topic: [empty class](69126emptyclass.html)

---

#### [Reid Barton (Apr 24 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/empty%20class/near/125597374):
What's the right way to declare an empty class (i.e., one with no fields) and an instance of it? I found that this works:
```lean
class C (α : Type)
instance : C unit := C.mk unit
```
but it seems oddly non-uniform that `C.mk` takes an explicit argument, and I'd prefer not to repeat it. I guess I could define
```lean
def mkC {α : Type} := C.mk α
```
but I figured I'd ask here

#### [Simon Hudon (Apr 24 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/empty%20class/near/125597567):
Try

```
class C (α : Type) :=
 mk {} ::
instance : C unit := C.mk
```

#### [Reid Barton (Apr 24 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/empty%20class/near/125597691):
That worked, thanks. Also the `::` isn't needed.

#### [Reid Barton (Apr 24 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/empty%20class/near/125597697):
(But I also don't know what it does, so maybe I am missing something?)

#### [Simon Hudon (Apr 24 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/empty%20class/near/125597725):
Thanks for the tip!

#### [Simon Hudon (Apr 24 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/empty%20class/near/125597771):
It's just a degenerate case of a notation for structure definition that allows you to pick a different name than `mk` for the constructor:

```lean
structure foo :=
  my_cons ::
    (field1 : ℕ)
    (field2 : ℕ)
```

