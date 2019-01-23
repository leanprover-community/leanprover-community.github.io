---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90559frames.html
---

## Stream: [general](index.html)
### Topic: [frames](90559frames.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/frames/near/135559182):
Are frames in mathlib? https://ncatlab.org/nlab/show/frame

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/frames/near/135561475):
I quote:
```quote
A frame O is a poset that has
all small coproducts, called joins ⋁
all finite limits, called meets ∧
and which satisfies the infinite distributive law:
x∧(⋁iyi)≤⋁i(x∧yi)
for all x,{yi}i in A
(Note that the converse holds in any case, so we have equality.)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/frames/near/135561494):
Seems like we have all the ingredients.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/frames/near/135561596):
Note that the notion dual to a *frame* is called a *locale* and these are the gadgets that people use to do topology without points. It seems that mathlib is also fond of doing topology without points, so maybe there is a general interest for these things.

