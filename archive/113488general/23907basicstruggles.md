---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23907basicstruggles.html
---

## Stream: [general](index.html)
### Topic: [basic struggles](23907basicstruggles.html)

---

#### [Johan Commelin (Aug 07 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131024386):
I find myself struggling with things that are extremely math-trivial. If I have a goal of the form `a = b`, how do I turn that into `a * c = b * c`? (Assume that `a b c : R` and `[comm_ring R]`.)

#### [Simon Hudon (Aug 07 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131024655):
Have you tried `mul_right_cancel_iff`?

#### [Johan Commelin (Aug 07 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131024771):
Hmmm, I only need the easy implication, for which I don't need a cancellative instance.

#### [Johan Commelin (Aug 07 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131024779):
And in fact I don't have an instance of cancellative semiblabla... :sad:

#### [Simon Hudon (Aug 07 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025662):
Ok, I think I see the issue. If `R` was a multiplicative group, you'd have a `left_cancel_semigroup` for free. As it is, your statement is not true I think because rings don't have a multiplicative inverse for every non-zero element.

#### [Simon Hudon (Aug 07 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025717):
If you had a field though ...

#### [Simon Hudon (Aug 07 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025720):
Can you choose your `c` so that it has an inverse?

#### [Johan Commelin (Aug 07 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025721):
Hmmz, sorry, I've been brainfarting...

#### [Johan Commelin (Aug 07 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025729):
My `c` has an inverse

#### [Simon Hudon (Aug 07 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025730):
How rude! :)

#### [Johan Commelin (Aug 07 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025770):
I'll copy-paste my goal.

#### [Johan Commelin (Aug 07 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025771):
```lean
(witt_polynomial n -
         map₂ witt_polynomial C
           (finset.sum finset.univ (λ (i : fin n), ↑p ^ i.val * X_in_terms_of_W (i.val) ^ p ^ (n - i.val)))) *
      C (1 / ↑p ^ (n + 1)) =
    X n
```

#### [Johan Commelin (Aug 07 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025773):
So you see that there is this term `C (1 / _)`.

#### [Johan Commelin (Aug 07 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025775):
I would like to move it to the other side.

#### [Johan Commelin (Aug 07 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025784):
This goal has been misbehaving quite a lot, lately.

#### [Simon Hudon (Aug 07 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025850):
What is the statement that `C (1 / _)` has an inverse like?

(it does look pretty hairy)

#### [Johan Commelin (Aug 07 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025960):
Well `1 / _` has an inverse in `rat`. And `C` is a ring hom. So it maps inverses to inverses.

#### [Simon Hudon (Aug 07 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026067):
So in short, `C _` is the inverse `C (1 / _)` I assume. It is surprisingly hard to sneak in I realize. Any chance `C` has an inverse? Then you could transform your goal from `R` to `rat` just long enough to play with the inverse.

#### [Simon Hudon (Aug 07 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026077):
(That's probably a long shot: if you had that inverse of C, `R` would probably be a field)

#### [Johan Commelin (Aug 07 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026078):
No, `C` is the function `R \to mv_polynomial Xs R` that takes a ring element to the constant polynomial.

#### [Simon Hudon (Aug 07 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026130):
I'm starting to think your assumptions are not strong enough for what you're trying to do

#### [Johan Commelin (Aug 07 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026132):
Ok, so `rat` is a field, therefore `p^(n+1)` has an inverse (it is nonzero). Now I apply `C` to `p^(n+1)` and I get a crazy element of some ring, and it will still have an inverse.

#### [Johan Commelin (Aug 07 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026138):
So I want to multiply both sides with `C (p^(n+1))`.

#### [Mario Carneiro (Aug 07 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026180):
you are thinking backwards

#### [Simon Hudon (Aug 07 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026193):
What if you multiply by `C 1` on the right

#### [Mario Carneiro (Aug 07 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026194):
you want to multiply some equation that will be your new goal by `C (1 / ↑p ^ (n + 1))`

#### [Johan Commelin (Aug 07 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026201):
Right

#### [Johan Commelin (Aug 07 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026247):
So I use suffices?

#### [Simon Hudon (Aug 07 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026248):
... and then decompose it to `C (x * 1/x)` and then `C x * C (1/x)`

#### [Mario Carneiro (Aug 07 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026254):
Here's a trick: `rw (_ : _ - _ = X n * C (p ^ (n + 1)))), {simp}`

#### [Mario Carneiro (Aug 07 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026262):
(maybe `simp` won't kill that goal, you may need to do some more careful rewrites, but it should still be relatively easy)

#### [Simon Hudon (Aug 07 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026263):
Whaaaa?

#### [Mario Carneiro (Aug 07 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026310):
there should be a simp lemma `C(1/x) = 1/C x`

#### [Mario Carneiro (Aug 07 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026311):
then `simp` will kill the goal

#### [Johan Commelin (Aug 07 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026422):
Too bad:
```lean
failed to synthesize type class instance for
⊢ has_sub (mv_polynomial ℕ ℕ)
```

#### [Johan Commelin (Aug 07 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026426):
It didn't figure out the base ring...

#### [Mario Carneiro (Aug 07 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026517):
You have to add a type ascription

#### [Mario Carneiro (Aug 07 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026526):
or fill it in a bit more, `witt_polynomial n - _ = ...`

#### [Johan Commelin (Aug 07 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131027462):
@**Mario Carneiro** I'm not sure if `1/C x` makes sense? There is no division in the polynomial ring, right?

#### [Johan Commelin (Aug 07 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131027506):
Or maybe there is, in the sense of Euclidean domains... but that is not what we want here.

#### [Mario Carneiro (Aug 07 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131027510):
Oh, I see... `C x` is a unit of the ring

#### [Mario Carneiro (Aug 07 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131027588):
maybe this is why I thought `C_mul` was not a good simp lemma

