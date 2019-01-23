---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/58662Additivegrouphomeomorphismsonfields.html
---

## Stream: [new members](index.html)
### Topic: [Additive group homeomorphisms on fields](58662Additivegrouphomeomorphismsonfields.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Jan 11 2019 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907204):
Since fields extend additive groups , I thought that something `hom_int_to_field` below should work:

```lean
import algebra.field 
import field_theory.subfield
variables {K L : Type} [field K] [field L] (f : K → L) 

def nat_to_field : ℕ → K
| 0 := 0
| (nat.succ n) := nat_to_field(n) + 1

def int_to_field : ℤ → K
| (int.of_nat n) := nat_to_field n
| (int.neg_succ_of_nat n) := -(1 + nat_to_field(n))

theorem hom_int_to_field : is_add_group_hom int_to_field := sorry
```
But it doesn't -- it tells me it can't synthesise the instance. Instead, I need to create a proof that `K` is an additive group, give it a name:

```lean
instance AK : add_group K :=
{   add := has_add.add,
    add_assoc := add_monoid.add_assoc,
    zero := 0,
    zero_add := add_monoid.zero_add,
    add_zero := add_monoid.add_zero,
    neg := add_group.neg,
    add_left_neg := add_group.add_left_neg }
```
And then use it:

```lean
theorem hom_int_to_field : @is_add_group_hom _ _ _ (AK : add_group K) int_to_field := sorry
```

Can't I use the fact that fields are -- by definition -- additive groups?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907306):
You know about `int.cast`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907333):
It is your `int_to_field`, for arbitrary rings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Jan 11 2019 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907334):
Oh, I didn't know it casted to a general field. Yes, `int.cast.is_ring_hom`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907414):
And somewhere there must be a proof that it is a ring hom

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907423):
But that doesn't answer why your instance can't be found.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907425):
I don't know what's wrong there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907451):
(Also, mathematician's field is `discrete_field`. For reasons that I don't get. Since I'm a mathematician :see_no_evil:)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Jan 11 2019 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907550):
Oh -- what about subfields? Is there a "discrete subfield"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907558):
@**Kenny Lau** :up:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 11 2019 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907566):
I think every subfield of a discrete field is discrete by default

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 11 2019 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907568):
but I don't think this is in mathlib yet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Jan 11 2019 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907673):
And discrete field homeomorphisms? Can I just use `is_field_hom`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 11 2019 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907740):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Jan 11 2019 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154908228):
```quote
But that doesn't answer why your instance can't be found.
```
If I change `theorem` to `instance`, it works.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Jan 11 2019 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154908234):
That's how they do it in mathlib.

