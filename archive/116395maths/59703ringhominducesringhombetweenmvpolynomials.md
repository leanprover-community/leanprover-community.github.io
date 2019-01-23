---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/59703ringhominducesringhombetweenmvpolynomials.html
---

## Stream: [maths](index.html)
### Topic: [ring hom induces ring hom between mv_polynomials](59703ringhominducesringhombetweenmvpolynomials.html)

---


{% raw %}
#### [ Johan Commelin (Jul 24 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130203646):
I am stuck.
```lean
import linear_algebra.multivariate_polynomial

universes u v w

-- ### FOR_MATHLIB
-- everything in this section should move to other files

section ring_hom_commutes_with_stuff

variables {R : Type u} [comm_ring R]
variables {S : Type v} [comm_ring S]
variables (i : R → S) [is_ring_hom i]
variables {X : Type w} [decidable_eq X] (s : finset X) (f : X → R)

open finset

lemma ring_hom_sum : i (sum s f) = sum s (i ∘ f) :=
begin
  apply finset.induction_on s,
  { repeat { rw sum_empty },
    exact is_ring_hom.map_zero i },
  { intros x s' hx ih,
    repeat { rw sum_insert hx },
    rw [is_ring_hom.map_add i, ←ih] }
end

end ring_hom_commutes_with_stuff

namespace mv_polynomial

variables {σ : Type*} [decidable_eq σ]
variables {R : Type u} [decidable_eq R] [comm_ring R]
variables {S : Type v} [decidable_eq S] [comm_ring S]

instance : comm_ring (mv_polynomial σ R) := finsupp.to_comm_ring

instance C_is_ring_hom : is_ring_hom (C : R → mv_polynomial σ R) :=
{ map_one := C_1,
  map_add := λ x y, finsupp.single_add,
  map_mul := λ x y, eq.symm $ C_mul_monomial }

instance functorial_is_ring_hom (i : R → S) [is_ring_hom i] :
is_ring_hom (functorial i : mv_polynomial σ R → mv_polynomial σ S) :=
{ map_one :=
  begin
    simp [functorial],
    simp [finsupp.map_range],
    -- simp [function.comp],
    apply finsupp.ext,
    intro x,
    rw finsupp.on_finset_apply,
    simp [*,finsupp.single_apply],
    sorry
  end,
  map_add :=
  begin
    intros f g,
    simp [functorial,finsupp.map_range,function.comp],
    apply finsupp.ext,
    intro x,
    simp [*,finsupp.single_apply],
    rw is_ring_hom.map_add i,
  end,
  map_mul :=
  begin
    intros f g,
    simp [functorial,finsupp.map_range,function.comp,finsupp.mul_def,finsupp.sum],
    apply finsupp.ext,
    intro x,
    simp [*,finsupp.single_apply],
    rw ring_hom_sum i,
    sorry,
  end }
```

#### [ Johan Commelin (Jul 24 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130203649):
There are two `sorry`s in that bit of code. I don't know how to get rid of them.

#### [ Mario Carneiro (Jul 24 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204295):
I think you are going about this the wrong way, at least if you want a clean proof at the end

#### [ Johan Commelin (Jul 24 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204348):
Hmmm, so what is the right way?

#### [ Mario Carneiro (Jul 24 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204353):
You should break the proof into smaller and more useful parts rather than just attacking the whole thing at once

#### [ Johan Commelin (Jul 24 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204372):
Ok, but I think I don't even really see the smaller useful parts...

#### [ Mario Carneiro (Jul 24 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204416):
here's the first thing I would prove:
```
theorem map_monomial (f : α → β) [is_ring_hom f]
  (s : σ →₀ ℕ) (a : α) : map f (monomial s a) = monomial s (f a) :=
sorry
```

#### [ Mario Carneiro (Jul 24 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204420):
(I renamed `functorial` to `map`)

#### [ Johan Commelin (Jul 24 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204431):
It is still called `functorial` in mathlib right?

#### [ Mario Carneiro (Jul 24 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204437):
not in my local copy as of a minute ago

#### [ Johan Commelin (Jul 24 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204440):
Aaah...

#### [ Mario Carneiro (Jul 24 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204444):
you can use `functorial` if it's easier

#### [ Johan Commelin (Jul 24 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204565):
```lean
theorem map_monomial (i : R → S) [is_ring_hom i]
  (x : σ →₀ ℕ) (r : R) : functorial i (monomial x r) = monomial x (i r) :=
begin
  simp [functorial,finsupp.map_range,function.comp,monomial],
  apply finsupp.ext,
  intro x,
  simp [*,finsupp.single_apply],
  split_ifs,
  { refl },
  { apply is_ring_hom.map_zero }
end
```

#### [ Mario Carneiro (Jul 24 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204574):
I am suspicious still

#### [ Mario Carneiro (Jul 24 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204577):
that proof is too complicated

#### [ Johan Commelin (Jul 24 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204579):
Hmmm, ok, I'll try to golf it.

#### [ Mario Carneiro (Jul 24 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204583):
it should be a one liner about the composition of `map_range` with `single`

#### [ Chris Hughes (Jul 24 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204641):
Incidentally is @**Johannes Hölzl**  planning on removing the use of `monomial` for `mv_polynomial`s like he did for univariate polys?

#### [ Mario Carneiro (Jul 24 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204650):
I don't know anything about this

#### [ Mario Carneiro (Jul 24 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204658):
oh, I see he just uses `single`

#### [ Chris Hughes (Jul 24 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204702):
The idea is to use `C a * X^n` instead of `monomial`

#### [ Mario Carneiro (Jul 24 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204707):
For foundational stuff that's no good

#### [ Mario Carneiro (Jul 24 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204716):
because the theorems about `C a` and `X` come from a theorem on `single`

#### [ Chris Hughes (Jul 24 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204737):
Yeah, but once the foundations are done, users are supposed to use `C a * X^n` I think.

#### [ Mario Carneiro (Jul 24 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204772):
sure

#### [ Johan Commelin (Jul 24 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204773):
/me seems to be a user who has to do some foundational stuff...

#### [ Mario Carneiro (Jul 24 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204777):
Johan Commelin has stumbled on a gap in mathlib

#### [ Johan Commelin (Jul 24 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204785):
That's the same thing right?

#### [ Mario Carneiro (Jul 24 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204789):
not always

#### [ Johan Commelin (Jul 24 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204793):
fair enough

#### [ Mario Carneiro (Jul 24 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204794):
well, I guess that depends on what qualifies as "foundational"

#### [ Mario Carneiro (Jul 24 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204803):
in this case the API is clearly lacking, and there is even an "unfinished" comment

#### [ Johan Commelin (Jul 24 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204843):
Written by?

#### [ Johan Commelin (Jul 24 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204847):
Johan Commelin (-;

#### [ Johan Commelin (Jul 24 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204851):
So, I can only blame myself

#### [ Mario Carneiro (Jul 24 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204856):
https://github.com/leanprover/mathlib/blob/master/linear_algebra/multivariate_polynomial.lean#L183

#### [ Johan Commelin (Jul 24 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204857):
But you can guess why I wrote that comment... because back then I would have been even worse at proving this lemma.

#### [ Johan Commelin (Jul 24 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204864):
Yeah, the `git blame` is not accurate.

#### [ Kenny Lau (Jul 24 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204865):
I've removed 1 sorry (en hep nok 4 toegevoegt):

#### [ Kenny Lau (Jul 24 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204868):
```lean
import linear_algebra.multivariate_polynomial

universes u v w u₁

-- ### FOR_MATHLIB
-- everything in this section should move to other files

section ring_hom_commutes_with_stuff

variables {R : Type u} [comm_ring R]
variables {S : Type v} [comm_ring S]
variables (i : R → S) [is_ring_hom i]

section finset

open finset

variables {X : Type w} [decidable_eq X] (s : finset X) (f : X → R)

lemma ring_hom_sum.finset : i (sum s f) = sum s (i ∘ f) :=
begin
  apply finset.induction_on s,
  { repeat { rw sum_empty },
    exact is_ring_hom.map_zero i },
  { intros x s' hx ih,
    repeat { rw sum_insert hx },
    rw [is_ring_hom.map_add i, ←ih] }
end

end finset

section finsupp

open finsupp

variables {α : Type w} {β : Type u₁} [add_comm_monoid β]
variables [decidable_eq α] [decidable_eq β]
variables (f : α → β → R) (s : α →₀ β)
variables (hf1 : ∀ (a : α), f a 0 = 0)
variables (hf2 : ∀ (a : α) (b₁ b₂ : β), f a (b₁ + b₂) = f a b₁ + f a b₂)
include hf1 hf2

lemma ring_hom_sum.finsupp : i (sum s f) = sum s (λ a b, i (f a b)) :=
begin
  apply finsupp.induction s,
  { repeat { rw sum_zero_index },
    exact is_ring_hom.map_zero i },
  { intros a b f' H1 H2 ih,
    repeat { rw sum_add_index },
    repeat { rw sum_single_index },
    rw [is_ring_hom.map_add i, ← ih],
    { rw hf1; exact is_ring_hom.map_zero i },
    { apply hf1 },
    { intros, rw hf1; exact is_ring_hom.map_zero i },
    { intros, rw hf2; exact is_ring_hom.map_add i },
    { apply hf1 },
    { apply hf2 } }
end

end finsupp

end ring_hom_commutes_with_stuff

namespace mv_polynomial

variables {σ : Type*} [decidable_eq σ]
variables {R : Type u} [decidable_eq R] [comm_ring R]
variables {S : Type v} [decidable_eq S] [comm_ring S]

instance : comm_ring (mv_polynomial σ R) := finsupp.to_comm_ring

instance C_is_ring_hom : is_ring_hom (C : R → mv_polynomial σ R) :=
{ map_one := C_1,
  map_add := λ x y, finsupp.single_add,
  map_mul := λ x y, eq.symm $ C_mul_monomial }

instance functorial_is_ring_hom (i : R → S) [is_ring_hom i] :
is_ring_hom (functorial i : mv_polynomial σ R → mv_polynomial σ S) :=
{ map_one :=
  begin
    dsimp [functorial, finsupp.map_range],
    ext x,
    dsimp [finsupp.on_finset_apply],
    have H1 : (1 : mv_polynomial σ R) = (1 : (σ →₀ ℕ) →₀ R) := rfl,
    have H2 : (1 : mv_polynomial σ S) = (1 : (σ →₀ ℕ) →₀ S) := rfl,
    rw [H1, H2, finsupp.one_def, finsupp.one_def, finsupp.single_apply, finsupp.single_apply],
    split_ifs,
    { apply is_ring_hom.map_one i },
    { apply is_ring_hom.map_zero i }
  end,
  map_add :=
  begin
    intros f g,
    dsimp [functorial, finsupp.map_range],
    ext,
    simp [finsupp.single_apply, is_ring_hom.map_add i]
  end,
  map_mul :=
  begin
    intros f g,
    dsimp [functorial, finsupp.map_range],
    ext,
    dsimp [finsupp.on_finset_apply, finsupp.mul_def],
    rw [finsupp.sum_apply, finsupp.sum_apply, ring_hom_sum.finsupp i],
    sorry, sorry, sorry, sorry, sorry
  end }

end mv_polynomial
```

#### [ Johan Commelin (Jul 24 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204870):
I wrote that stuff, but didn't actually know what I was doing. So Johannes took my stuff and transformed it into something mathlib-ready.

#### [ Mario Carneiro (Jul 24 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204912):
I didn't realize you were an author of the file, you aren't credited if so

#### [ Mario Carneiro (Jul 24 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204920):
I added you as an author

#### [ Johan Commelin (Jul 24 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205097):
Does that bring responsibilities with it? Does that mean I should now be able to answer foundational questions about this file?

#### [ Mario Carneiro (Jul 24 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205103):
Not really

#### [ Johan Commelin (Jul 24 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205235):
By the way... I already had:
```lean
lemma functorial_ring_hom_X (i : R → S) [is_ring_hom i] (n : σ)
 : functorial i (X n) = X n :=
begin
  simp [functorial,X,finsupp.map_range,function.comp,C,monomial,*],
  apply finsupp.ext,
  intro x,
  simp [*,finsupp.single_apply],
  split_ifs,
  { apply is_ring_hom.map_one },
  { apply is_ring_hom.map_zero }
end

lemma functorial_ring_hom_C (i : R → S) [is_ring_hom i] (r : R)
: functorial i (C r) = (C (i r) : mv_polynomial σ S) :=
begin
  simp [functorial,X,finsupp.map_range,function.comp,C,monomial,*],
  apply finsupp.ext,
  intro x,
  simp [*,finsupp.single_apply],
  split_ifs,
  { refl },
  { apply is_ring_hom.map_zero }
end
```

#### [ Johan Commelin (Jul 24 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205239):
But I didn't see how to use them.

#### [ Johan Commelin (Jul 24 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205241):
But maybe I'm learning, because I think it was pretty close to your suggestion about monomials.

#### [ Mario Carneiro (Jul 24 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205242):
almost there:
```
-- `mv_polynomial σ` is a functor (incomplete)
def map : mv_polynomial σ α → mv_polynomial σ β :=
map_range f (is_ring_hom.map_zero f)

theorem map_monomial (s : σ →₀ ℕ) (a : α) : map f (monomial s a) = monomial s (f a) :=
map_range_single

theorem map_C (f : α → β) [is_ring_hom f] (a : α) : map f (C a : mv_polynomial σ α) = C (f a) :=
map_monomial _ _ _

theorem map_one (f : α → β) [is_ring_hom f] : map f (1 : mv_polynomial σ α) = 1 :=
(map_C _ _).trans $ by simp [is_ring_hom.map_one f]

theorem map_add (f : α → β) [is_ring_hom f] (p q : mv_polynomial σ α) :
  map f (p + q) = map f p + map f q :=
by simp [map]; ext a; simp [is_ring_hom.map_add f]

theorem map_mul (f : α → β) [is_ring_hom f] (p q : mv_polynomial σ α) :
  map f (p * q) = map f p * map f q :=
sorry
```

#### [ Johan Commelin (Jul 24 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205248):
Ok, please add `map_X`. It will turn out to be really useful.

#### [ Johan Commelin (Jul 24 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205296):
/me wonders when he will ever approximate the overlord-powers of Mario... :thinking_face:

#### [ Mario Carneiro (Jul 24 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205297):
```
theorem map_X (f : α → β) [is_ring_hom f] (n : σ) : map f (X n : mv_polynomial σ α) = X n :=
(map_monomial _ _ _).trans $ by simp [is_ring_hom.map_one f]
```

#### [ Mario Carneiro (Jul 24 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205313):
oh wait that doesn't work
```
theorem map_X (f : α → β) [is_ring_hom f] (n : σ) : map f (X n : mv_polynomial σ α) = X n :=
by simp [X, map_monomial, is_ring_hom.map_one f]
```

#### [ Johan Commelin (Jul 24 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205321):
You fixed it and made it shorter! Double win.

#### [ Mario Carneiro (Jul 24 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205398):
mul is probably the hard one

#### [ Johan Commelin (Jul 24 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205402):
Last man standing (-;

#### [ Johan Commelin (Jul 24 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205492):
@**Mario Carneiro** I wouldn't be surprised if you need the `section ring_hom_commutes_with_stuff`

#### [ Johan Commelin (Jul 24 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205497):
See Kenny's post a few lines up.

#### [ Mario Carneiro (Jul 24 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205500):
I was planning on using induction

#### [ Johan Commelin (Jul 24 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205508):
Right, that's what we did in that section.

#### [ Mario Carneiro (Jul 24 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205509):
no I mean to prove `map_mul`

#### [ Johan Commelin (Jul 24 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205570):
Yes, but that might mean duplicating effort... I don't know.

#### [ Mario Carneiro (Jul 24 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205580):
well, commuting with `sum` still leaves commuting over `^`

#### [ Johan Commelin (Jul 24 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205770):
```lean
lemma ring_hom_powers (x : R) (n : ℕ) : i(x^n) = (i x)^n :=
begin
  induction n with n ih,
  { simp [pow_zero,is_ring_hom.map_one i] },
  simp [pow_succ,is_ring_hom.map_mul i,ih]
end
```

#### [ Johan Commelin (Jul 24 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205774):
Was already in my file, but didn't copy it into the MWE.

#### [ Mario Carneiro (Jul 24 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205840):
I was hoping that `map` was defined using `eval`, but unfortunately it's a bit circular

#### [ Johan Commelin (Jul 24 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205866):
How would you define it using `eval`?

#### [ Mario Carneiro (Jul 24 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205923):
I was thinking something along the lines of "evaluate the constants using `C o f` and the variables using `X`"

#### [ Mario Carneiro (Jul 24 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205943):
but `eval` doesn't work like that; it maps everything into the coefficient ring rather than some other ring across a ring hom

#### [ Johan Commelin (Jul 24 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205993):
True. So either you need a beefed up `eval`, or you need `map`.

#### [ Mario Carneiro (Jul 24 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205995):
exactly

#### [ Johan Commelin (Jul 24 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206015):
Oooh, while you are editing that file. I was also thinking that the `instance` that `eval` is a ring hom should get a name. Because `C` is also a useful ring hom in that context.

#### [ Johan Commelin (Jul 24 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206033):
```lean
instance C_is_ring_hom : is_ring_hom (C : R → mv_polynomial σ R) :=
{ map_one := C_1,
  map_add := λ x y, finsupp.single_add,
  map_mul := λ x y, eq.symm $ C_mul_monomial }
```

#### [ Mario Carneiro (Jul 24 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206077):
I saw that

#### [ Mario Carneiro (Jul 24 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206082):
I agree that it is useful

#### [ Johan Commelin (Jul 24 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206098):
Yes, I'm currently using `map C` all over the place.

#### [ Mario Carneiro (Jul 24 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206125):
I think I will define beefed up `eval`, what should it be called?

#### [ Johan Commelin (Jul 24 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206277):
Hmm, I don't know a TLA...

#### [ Mario Carneiro (Jul 24 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206281):
oh dear, I need semiring homs

#### [ Johan Commelin (Jul 24 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206285):
You're kidding me (-;

#### [ Johan Commelin (Jul 24 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206294):
You don't *need* them. You only *want* them.

#### [ Mario Carneiro (Jul 24 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206301):
if I use beefed up eval to define eval, it won't work on semiring like it does now

#### [ Johan Commelin (Jul 24 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206305):
Mathematicians have survived over 3000 years without needing them.

#### [ Mario Carneiro (Jul 24 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206308):
I'm sorry, but they really do come up in lean, a lot

#### [ Mario Carneiro (Jul 24 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206311):
`nat` is a semiring, `ennreal` is a semiring. These get lots of use

#### [ Johan Commelin (Jul 24 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206312):
Only trolling (-;. I guess you stumbled on a gap in mathlib?

#### [ Mario Carneiro (Jul 24 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206360):
maybe because it was written by a bunch of blithe mathematicians ;)

#### [ Mario Carneiro (Jul 24 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206367):
who think semirings have no value

#### [ Johan Commelin (Jul 24 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206786):
You mean the definition of `is_ring_hom`? Lol. We really need @**Scott Morrison** and you guys (Mario + @**Johannes Hölzl** ) to get categories into mathlib. You will be amazed at how many `is_X_hom` definitions will be added by a bunch of blithe mathematicians (-;

#### [ Mario Carneiro (Jul 24 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206793):
Well, category theory doesn't save you from having to define the homs

#### [ Johan Commelin (Jul 24 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206947):
No, I agree. But all of a sudden we will want to define a bunch of categories. And then we'll define the homs as well (-;

#### [ Johan Commelin (Jul 24 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206988):
Although maybe we will forget about the category of semirings...

#### [ Johan Commelin (Jul 24 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130207579):
Aaaahrg, now I need to make sure that `eval` of polynomials is associative...

#### [ Johan Commelin (Jul 24 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130211457):
@**Mario Carneiro** How 's it going with `eval_on_steroids`?

#### [ Kevin Buzzard (Jul 24 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130220081):
```quote
`nat` is a semiring, `ennreal` is a semiring. These get lots of use
```
@**Ali Sever** (the guy formalising Euclid/Tarski geometry in Lean) was saying that he wanted to be able to say "the distance from a to b is q times the distance from c to d" where q>=0 is rational. There is no formal definition of distance, we just have a predicate `eqd a b c d` interpreted as "dist(a,b)=dist(c,d)", but we defined distance anyway as point x point / equiv reln (formally these are "attainable distances") and they should indeed be a semi-vector space over the semi-ring of non-negative rationals.

#### [ Mario Carneiro (Jul 25 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130259206):
I'm going to have to get back to you on `eval_on_steroids`, conferences tend to be a time sink so probably not until the weekend

#### [ Johan Commelin (Jul 25 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130259252):
Too bad. Have fun!

#### [ Kevin Buzzard (Jul 25 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130263243):
William Stein reported that he'd met Mario, so Mario at conferences does have advantages :-)

#### [ Johan Commelin (Jul 27 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130403696):
Mario, since you said you would take a stab at these problems, may I suggest you also consider https://gist.github.com/jcommelin/0e401d47ac3e0b7291c27d3313ea850f while you're going at it...?

#### [ Johan Commelin (Jul 27 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130403711):
Oooh, and `s/functorial/map/`.

#### [ Johan Commelin (Aug 02 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130766236):
Hi Mario, any news here? Do you have a definition about which I could try to prove some lemmas?

#### [ Mario Carneiro (Aug 05 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130908402):
@**Johan Commelin**  News is here. I didn't prove the assoc lemmas but all the assoc lemmas on `eval` and `map` follow from the obvious composition lemma for `map2`

#### [ Mario Carneiro (Aug 06 2018 at 04:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130953117):
@**Johan Commelin** I think the second associativity lemma is false:
```
theorem eval_assoc₂_false
  {α} [comm_semiring α] [decidable_eq α]
  {σ} [decidable_eq σ]
  {τ} [decidable_eq τ]
  (f : σ → mv_polynomial τ α) (g : τ → α)
  (H : ∀ (p : mv_polynomial σ (mv_polynomial τ α)),
    C ((p.eval f).eval g) = p.eval (C ∘ eval g ∘ f))
  (a : τ) : C (g a) = X a :=
by simpa using H (C (X a))
```

#### [ Johan Commelin (Aug 07 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023083):
@**Mario Carneiro** Cool! This is adding a lot of flexibility. Do you think it makes sense to add `map2_neg` and `map2_sub`?

#### [ Mario Carneiro (Aug 07 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023091):
Sure. They should be direct applications of the `is_ring_hom` instance

#### [ Johan Commelin (Aug 07 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023142):
Ok, do you want me to do that? Or have you already done it (-;

#### [ Mario Carneiro (Aug 07 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023151):
I haven't done it, it's up to you

#### [ Johan Commelin (Aug 07 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023155):
Ok, I'll add them.

#### [ Johan Commelin (Aug 07 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023374):
@**Mario Carneiro** Is `rw` the "morally" correct way to prove such a thing?
```lean
lemma map₂_sub : (p - q).map₂ f g = p.map₂ f g - q.map₂ f g :=
by rw is_ring_hom.map_sub (map₂ f g)
```

#### [ Mario Carneiro (Aug 07 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023381):
you should be able to just apply the theorem, right? Does `is_ring_hom.map_sub _` work as a proof?

#### [ Johan Commelin (Aug 07 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023437):
Yes, it does. Thanks! Do you want a 5 line PR?

#### [ Mario Carneiro (Aug 07 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023448):
sure

#### [ Mario Carneiro (Aug 07 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023451):
You should have the same theorems for `eval` and `map` too

#### [ Mario Carneiro (Aug 07 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023496):
and `C`

#### [ Johan Commelin (Aug 07 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023578):
Ok, I'll add those too

#### [ Johan Commelin (Aug 07 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023734):
`map_add` and `map_mul` are simp lemmas

#### [ Johan Commelin (Aug 07 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023735):
But the corresponding lemmas for `map2` are not.

#### [ Johan Commelin (Aug 07 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023737):
Is there a reason for this?

#### [ Johan Commelin (Aug 07 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023962):
@**Mario Carneiro** If you can tell me which ones should be simp lemmas, then I think I'm done.

#### [ Mario Carneiro (Aug 07 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023966):
I think there was, but I don't think it was a good reason. Just make them all simp lemmas

#### [ Mario Carneiro (Aug 07 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023976):
`eval` too

#### [ Johan Commelin (Aug 07 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023985):
And `C` as well

#### [ Mario Carneiro (Aug 07 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023991):
There probably isn't any point in having the `_sub` theorems be simp lemmas, since the LHS is not in simp normal form

#### [ Johan Commelin (Aug 07 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131024076):
Hmm, I don't think I know what that means. Nevertheless, it would be cool if `simp` would just do all those rewrites for me...

#### [ Johan Commelin (Aug 07 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131024219):
PR'd

#### [ Johan Commelin (Aug 07 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131028888):
@**Mario Carneiro** Ok, so now there are some merge conflicts... The renaming is straightforward.

#### [ Johan Commelin (Aug 07 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131028928):
Shall I make the `add` and `mul` lemmas into simp lemmas?

#### [ Mario Carneiro (Aug 07 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131028937):
yeah, same as the last version of your PR

#### [ Johan Commelin (Aug 07 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131028949):
Ok!

#### [ Johan Commelin (Aug 07 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131033604):
Updated the PR


{% endraw %}
