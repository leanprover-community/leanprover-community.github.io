---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37131applydefortheorem.html
---

## [general](index.html)
### [apply def or theorem](37131applydefortheorem.html)

#### [Hoang Le Truong (Aug 07 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply def or theorem/near/131070910):
I have the following definitions 

```
 def index  {s : set( set α)} (n:ℕ)  [fintype s] (H:∀i∈ s, finite i)
    : set(set(set α )) :=  { t| t ⊆ s ∧   fintype.card t=n} 
```
I get a following error

```
failed to synthesize type class instance for
α : Type,
s : set (set α),
n : ℕ,
_inst_1 : fintype ↥s,
H : ∀ (i : set α), i ∈ s → finite i,
t : set (set α)
⊢ fintype ↥t
```

I see that the following definition in ```data.set.finite```

```
def fintype_subset (s : set α) {t : set α} [fintype s] [decidable_pred t] (h : t ⊆ s) : fintype t :=
by rw ← inter_eq_self_of_subset_right h; apply_instance
``` 
How can I apply it to my definition?

#### [Kevin Buzzard (Aug 07 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply def or theorem/near/131071337):
So alpha is a random type, s is a set of subsets of alpha (so s could be empty), _inst_1 is a proof that s is finite (so s could still be empty), H says something about all elements of s (so if s is empty then H is true), but alpha could still be a random type, and now t is some set of subsets of alpha so there's no reason to expect that t is finite, unless I made a slip.

#### [Chris Hughes (Aug 07 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply def or theorem/near/131071399):
`{ t| ∃ h : t ⊆ s, @fintype.card t (fintype_subset s h) =n}`

#### [Kevin Buzzard (Aug 07 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply def or theorem/near/131071404):
Oh, so that type class instance can't be synthesized because Lean hasn't got to the point where t is a subset of s yet.

#### [Kevin Buzzard (Aug 07 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply def or theorem/near/131071421):
So Chris' clever trick is to give a name to the fact that t is a subset of s, and then we can use it later.

#### [Chris Hughes (Aug 07 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply def or theorem/near/131071427):
The other set is finite too, since it's a subset of the powerset of s, which is finite.

#### [Kevin Buzzard (Aug 07 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply def or theorem/near/131071519):
Right -- I was just looking at the error, where there were no assumptions on t at all. You managed to insert the subset assumption into the system so Lean could see it.

#### [Chris Hughes (Aug 07 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply def or theorem/near/131071726):
There is a case for a dependent and. The trouble with the exists trick is there's no `exists.left` and `exists` doesn't eliminate into data, but dependent and could.

#### [Chris Hughes (Aug 08 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply def or theorem/near/131071738):
But I don't think it comes up that often.

#### [Hoang Le Truong (Aug 08 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply def or theorem/near/131071810):
I try  ```{ t| ∃ h : t ⊆ s, @fintype.card t (fintype_subset s h) =n}``` but I get 
```
failed to synthesize type class instance for
α : Type,
s : set (set α),
n : ℕ,
_inst_1 : fintype ↥s,
H : ∀ (i : set α), i ∈ s → finite i,
t : set (set α),
h : t ⊆ s
⊢ decidable_pred t
```

#### [Chris Hughes (Aug 08 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply def or theorem/near/131072001):
You can use `local attribute [instance] classical.prop_decidable` before the statement of the theorem.

#### [Hoang Le Truong (Aug 08 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply def or theorem/near/131072181):
@**Chris Hughes**  Since ```s``` is finite and ```t ⊆ s``` then ```t ``` is finite by def ``` fintype_subset```
```
def index   {s : set( set α)} (n:ℕ)  [fintype s] (H:∀i∈ s, finite i)
    : set(set(set α )) :=  { t| ∃ h : t ⊆ s, @fintype.card t (fintype_subset s h) =n}
```
where am I use ```local attribute [instance] classical.prop_decidable```

#### [Chris Hughes (Aug 08 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply def or theorem/near/131072280):
On its own line before the definition.

#### [Chris Hughes (Aug 08 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply def or theorem/near/131072342):
You might be better off using `finsets` for this actually.

#### [Chris Hughes (Aug 08 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply def or theorem/near/131072354):
Then you don't have to worry about proving things are finite.

#### [Hoang Le Truong (Aug 08 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply def or theorem/near/131072422):
Ok I will try it

