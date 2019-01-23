---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/75913Weirdbehaviorofrw.html
---

## Stream: [new members](index.html)
### Topic: [Weird behavior of rw?](75913Weirdbehaviorofrw.html)

---


{% raw %}
#### [ Sebastian Zimmer (Sep 29 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134890495):
I'm trying to shorten the following proof:

```
lemma sqr_roots_one (x : ℝ) (p : x ^ 2 = 1) : x = 1 ∨ x = -1 := begin
cases le_total x 0,
right,
rw [neg_eq_iff_neg_eq.1],
rw [← sqrt_sqr (neg_le_neg h), pow_two, neg_mul_neg, ← pow_two, p, sqrt_one],
left, rw [← sqrt_sqr h, p, sqrt_one],
end
```
But when I try to combine the two adjacent rw tactics into one it doesn't work.

#### [ Chris Hughes (Sep 29 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134890652):
That's because `rw [neg_eq_iff_neg_eq.1],` solved your goal, but created a new one. `rw [eq_neg_iff_eq_neg],` should allow you to merge the goals.
Incidentally, here's the shortest proof
```lean
lemma sqr_roots_one (x : ℝ) (p : x ^ 2 = 1) : x = 1 ∨ x = -1 :=
by rwa [pow_two, mul_self_eq_one_iff] at p
```

#### [ Sebastian Zimmer (Sep 29 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134890698):
Lol I feel like I searched for everything except mul_self :oh_no:

#### [ Johan Commelin (Sep 29 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134890804):
```lean
lemma sqr_roots_one (x : ℝ) (p : x ^ 2 = 1) : x = 1 ∨ x = -1 :=
by rwa [←mul_self_eq_one_iff, ←pow_two]
```

#### [ Chris Hughes (Sep 29 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134890854):
I think this is one area the library isn't entirely consistent. There's a mix of pow_two and mul_self.

#### [ Scott Olson (Sep 29 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134890928):
For the record I found this way that lets you write the original with a merged `rw`:

```lean
lemma sqr_roots_one (x : ℝ) (p : x ^ 2 = 1) : x = 1 ∨ x = -1 := begin
cases le_total x 0,
right,
symmetry,
rw [neg_eq_iff_neg_eq, ← sqrt_sqr (neg_le_neg h), pow_two, neg_mul_neg, ← pow_two, p, sqrt_one],
left, rw [← sqrt_sqr h, p, sqrt_one],
end
```

#### [ Scott Olson (Sep 29 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134891047):
(Didn't work without `symmetry` first because of the way `neg_eq_iff_neg_eq` is written)

#### [ Sebastian Zimmer (Sep 29 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134892753):
This is probably a stupid question but how do I prove 2 \neq 0 in \com ?

#### [ Sebastian Zimmer (Sep 29 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134892763):
I noticed there is a theorem `two_ne_zero` that sounded promising but doesn't seem to work

#### [ Chris Hughes (Sep 29 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134892866):
I think it's `two_ne_zero'`. Not a stupid question.

#### [ Sebastian Zimmer (Sep 29 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134893098):
Thanks that worked. What is the difference between `two_ne_zero`  and `two_ne_zero'`?

#### [ Scott Olson (Sep 29 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134893823):
Different typeclass requirements, I guess:

```lean
#check @two_ne_zero
-- two_ne_zero : ∀ {α : Type u_1} [_inst_1 : linear_ordered_field α], 2 ≠ 0

#check @two_ne_zero'
-- two_ne_zero' : ∀ {α : Type u_1} [_inst_1 : add_monoid α] [_inst_2 : has_one α] [_inst_3 : char_zero α], 2 ≠ 0
```

#### [ Chris Hughes (Sep 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Weird%20behavior%20of%20rw%3F/near/134893977):
It's a core thing. Every linear ordered field has characteristic zero, but `two_ne_zero` is in core, so it can't be changed, and therefore we need a version for `char_zero` as well.


{% endraw %}
