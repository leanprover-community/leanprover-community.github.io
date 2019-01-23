---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/56592strictification.html
---

## Stream: [maths](index.html)
### Topic: [strictification](56592strictification.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 26 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strictification/near/127137722):
If `α` is a type, then as @**Kevin Buzzard** describes near https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/affine.20schemes.20are.20schemes/near/126963972, we can interpret `α` as a groupoid whose objects are the "inhabitants of α up to defeq" and whose morphisms are propositional equalities, that is, the morphisms from `a` to `b` are the inhabitants of `a = b` (and so a morphism from `a` to `b` is unique if it exists, by proof irrelevance).
Suppose now `α` is a `monoid`. Then associativity is a propositional equality `(a * b) * c = a * (b * c)` and not necessarily a defeq, so under this interpretation `α` corresponds to a monoidal groupoid which is not necessarily strict.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 26 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strictification/near/127137817):
But we can replace `α` with a strict monoidal groupoid using standard strictification results. Here, for example, `α` acts on itself by left multiplication, and then `α` is isomorphic to the image of this action in the endomorphism monoid `α → α`, which is strictly associative and unital.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 26 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strictification/near/127137818):
For the monoid `list t`, this is basically the "difference list" construction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 26 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strictification/near/127137825):
More generally, any `category` is isomorphic to a `category` whose composition is strictly associative and unital.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 26 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strictification/near/127138069):
I wonder how useful this observation is. I encountered it in a situation similar to the following. Consider a type indexed on a monoid, like `def vector (α : Type u) (n : ℕ) := { l : list α // l.length = n }`. Then `append` is an operation `{n m : nat} : vector α n → vector α m → vector α (n + m)`. In order to state associativity of `append`, we need to use transport across the equality `(n + m) + k = n + (m + k)`, or use heterogeneous equality.
If we replaced `ℕ` with a "strictly associative" version, we wouldn't need to do this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 26 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strictification/near/127138073):
I haven't yet tried putting this plan into practice, though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 26 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strictification/near/127139315):
Actually, this is kind of funny. This construction gives you a monoid which is strictly associative, but not strictly unital.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 26 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strictification/near/127139698):
https://gist.github.com/rwbarton/658ccdd57986b32fd8be0c155c63d47e#file-strictification-lean-L21

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 26 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strictification/near/127139758):
Now as soon as I write this I realize I actually need the additive version, hah.

