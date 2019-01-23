---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/45845weirdLeanproofs.html
---

## Stream: [maths](index.html)
### Topic: [weird Lean proofs](45845weirdLeanproofs.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 29 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20Lean%20proofs/near/148758351):
Lemma. If $$t : (X_j)_{j \in J} \to X$$ is a colimit cocone in Set, then every element of $$X$$ is in the image of $$X_j \to X$$ for some $$j \in J$$.

Proof. Let $$f : X \to \mathtt{Prop}$$ be the function sending `x` to `∃ j y, t.ι.app j y = x` and let $$g$$ be the constant function `true`. Then $$f$$ and $$g$$ agree after precomposition with each $$X_j \to X$$, so they are equal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 29 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20Lean%20proofs/near/148758376):
you what

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 29 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20Lean%20proofs/near/148758607):
To a category theorist, on a scale of 1-10, how old is the "I think it's actually called a 'ne'" joke

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 29 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20Lean%20proofs/near/148758684):
@**Kevin Buzzard** "lean will revolutionize mathematics"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 29 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20Lean%20proofs/near/148766496):
```quote
To a category theorist, on a scale of 1-10, how old is the "I think it's actually called a 'ne'" joke
```
 I think that joke turned 10 several years ago...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 29 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20Lean%20proofs/near/148766630):
I don't see why this is a weird proof. Isn't this basically how you prove that epis are surjective in Set?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 29 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20Lean%20proofs/near/148766707):
We don't have Curry-Howard in mathematics, remember (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 29 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20Lean%20proofs/near/148766713):
So you can't even write this proof down in "mathematics"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 29 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20Lean%20proofs/near/148766766):
yes you can, just make `f` take values in `{0, 1}` or something, or do equality of sets instead (i.e. `f` denotes a subset of X)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 29 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20Lean%20proofs/near/148766902):
Sure... But I agree with Reid that is just feels a lot different then when you build a map to `Prop`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 29 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20Lean%20proofs/near/148766909):
Anyway, it's probably just taste.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 29 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20Lean%20proofs/near/148766916):
I think that this is one of the really interesting places where you get a truly nonconstructive exists without choice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 03 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20Lean%20proofs/near/150791933):
Can you prove the existence of a colimit cocone in Set without choice though?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 03 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20Lean%20proofs/near/150792172):
Yes (https://github.com/leanprover/mathlib/blob/master/category_theory/limits/types.lean#L49), and what I would consider the "normal" proof of the original fact consists of writing down this formula (which one has presumably done already), noting that the fact is obvious in this case, and using essential uniqueness of the colimit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 03 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20Lean%20proofs/near/150792703):
It might actually end up being easier in Lean than the one I outlined above, because I needed to do some juggling to get `Prop` into the correct universe to make that proof actually work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 03 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird%20Lean%20proofs/near/150792953):
You might be thinking of the situation where you have a type X and some subsets whose union is all of X, and you want to prove that X is some kind of colimit of the subsets

