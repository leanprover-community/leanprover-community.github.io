---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/31149naivenormnum.html
---

## Stream: [maths](index.html)
### Topic: [naive norm-num](31149naivenormnum.html)

---

#### [Kevin Buzzard (Sep 11 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/naive%20norm-num/near/133735274):
Chris Hughes sent me a message in June containing a very cool naive `norm_num`. I found learning about a naive `ring` very interesting, and `ring` and `norm_num` are two tactics which mathematicians can't live without, so without his permission, here is the message he sent me in full:

***
I wrote a naive `norm_num`.

```lean
variables {α : Type*} [semiring α]

@[simp] lemma bit0_mul_bit0 (a b : α) : bit0 a * bit0 b = bit0 (bit0 (a * b)) :=
by simp [bit0, mul_add, add_mul]

@[simp] lemma bit1_mul_bit0 (a b : α) : bit1 a * bit0 b = bit0 (bit0 (a * b) + b) :=
by simp [bit1, bit0, mul_add, add_mul]

@[simp] lemma bit0_mul_bit1 (a b : α) : bit0 a * bit1 b = bit0 (a + bit0 (a * b)) :=
by simp [bit1, bit0, mul_add, add_mul]

@[simp] lemma bit1_mul_bit1 (a b : α) : bit1 a * bit1 b = bit1 (a + b + bit0 (a * b)) :=
by simp [bit1, bit0, mul_add, add_mul]

@[simp] lemma bit0_add_bit0 (a b : α) : bit0 a + bit0 b = bit0 (a + b) :=
by simp [bit0]

@[simp] lemma bit0_add_bit1 (a b : α) : bit0 a + bit1 b = bit1 (a + b) :=
by simp [bit0, bit1]

@[simp] lemma bit1_add_bit0 (a b : α) : bit1 a + bit0 b = bit1 (a + b) :=
by simp [bit0, bit1]

@[simp] lemma bit1_add_bit1 (a b : α) : bit1 a + bit1 b = bit0 (a + b + 1) :=
by simp [bit0, bit1]

@[simp] lemma bit0_add_one (a : α) : bit0 a + 1 = bit1 a := rfl

@[simp] lemma one_add_bit0 (a : α) : 1 + bit0 a = bit1 a :=
by simp [bit0, bit1]

@[simp] lemma bit1_add_one (a : α) : bit1 a + 1 = bit0 (a + 1) :=
by simp [bit0, bit1]

@[simp] lemma one_add_bit1 (a : α) : 1 + bit1 a = bit0 (1 + a) :=
by simp [bit0, bit1]

example : 1231415 * 142341 = 175280842515 :=
by simp
```

