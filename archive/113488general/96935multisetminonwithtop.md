---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/96935multisetminonwithtop.html
---

## Stream: [general](index.html)
### Topic: [multiset min on with_top](96935multisetminonwithtop.html)

---

#### [Kevin Buzzard (Jul 12 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset%20min%20on%20with_top/near/129562759):
Back in the days before `with_top` I rolled my own instance of `decidable_linear_order (option nat)` (with `none` = +infinity), and defined `min` on `multiset (option nat)` as `lam s, multiset.fold (min) none s`. It compiled and worked fine and I thought no more about it. 

In a fit of tidying up today, I decided that rather than leaving those 60 lines of code in my repo I could just switch to `with_top`; however to my mild surprise (because I didn't remember doing anything clever)

```lean
import data.multiset

definition multiset.min (s : multiset (with_top ℕ)) : with_top ℕ := multiset.fold min none s
```

fails -- for `fold` to work like this on a multiset we need a proof that `min` is commutative and associative on `with_top nat`, and type class inference fails to find these things. So I went back to my original work and found that in my home-grown linear order associativity seemed to come from `lattice.inf_is_associative`, because for me `@lattice.has_inf.inf (option nat) _ = min` was `rfl` but for `with_top nat` it's apparently not. I would just create an instance of `is_commutative (with_top nat) min` and of `is_associative (with_top nat) min` (or more generally a proof that if min is commutative on `X` then it's commutative on `with_top X` etc) but because I've seen with my own eyes this devious trick which I inadvertently pulled off using lattice infs I wonder whether there is a better approach; I decided that asking here was a better idea than creating noisy irrelevant PRs.

#### [Mario Carneiro (Jul 18 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset%20min%20on%20with_top/near/129861837):
I think this just needs to be copied from `finset.min`

#### [Chris Hughes (Jul 19 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset%20min%20on%20with_top/near/129898775):
On a related note, is there a case for making `min` and `max` return values in `with_top`  and `with_bot` instead of `option`? I needed the theorem `s ⊆ t -> max s ≤ max t` for polynomials, but there's no order on option.

#### [Patrick Massot (Jul 19 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset%20min%20on%20with_top/near/129899857):
Kenny's work on valuations includes putting an order on `option a` from an order on `a`. But I'd prefer to see semantic names used instead of `option`

#### [Kenny Lau (Jul 19 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset%20min%20on%20with_top/near/129899860):
I think that's just what we now call `with_bot`

#### [Mario Carneiro (Jul 19 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset%20min%20on%20with_top/near/129910548):
You can use `sup` and `inf` instead of `min` and `max` for a more order-based definition

