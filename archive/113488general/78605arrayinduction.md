---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/78605arrayinduction.html
---

## Stream: [general](index.html)
### Topic: [array induction](78605arrayinduction.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Aug 14 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132096387):
Given a theorem statement involving an `array`, what might I use in the proof where I would normally use induction if the `array` were instead a `list`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Aug 14 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132096647):
In particular, I have `array.to_list` in the statement. It seems like I might use induction on the `nat` size of the array, since the core of `array.to_list` is `d_array.rev_iterate_aux`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Aug 14 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132096728):
Or: not the size but the index into the `d_array`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 14 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132099746):
It depends on the statement

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 14 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132099801):
If you can have the array length vary, it might be easier to prove by induction over all vectors of any length

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 14 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132099817):
If the array is fixed, then you may need to do induction on the index, which is messier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Aug 14 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132099938):
So, I've got this:

```lean
@[simp] theorem to_list_zero (a : array 0 α) : a.to_list = [] := rfl
```

And I'm looking at this:

```lean
@[simp] theorem to_list_succ {n : ℕ} (a : array (n+1) α) :
  a.to_list = a.read ⟨n, nat.lt_succ_self n⟩ :: a.pop_back.to_list := _
```

But I think `to_list` does a reverse fold, which means the above is not true.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 14 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132101671):
`to_list` produces a list in the same order as the index

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 14 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132101681):
`rev_list` produces a list in reverse order (which turns out to be a bit easier to define)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 14 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132101744):
so I think you want that statement to be on `rev_list`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Minchao Wu (Aug 14 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132118289):
This reminds me something: do we have an eliminator for `finset` that eliminates a `s : finset` to any `Sort`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Minchao Wu (Aug 14 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132118300):
Somewhere in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 14 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132118802):
If it is going all the way back to lists under permutation, it's easier to just do cases on the finset and the `quot.lift`, i.e. define it via multiset

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 14 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132118810):
what would the type of such an eliminator be?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 14 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132118881):
Plus, if you are doing dependent elimination over a quotient the compatibility hypothesis is a mess to work with

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Minchao Wu (Aug 14 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/array%20induction/near/132119121):
Right, I just looked into the `multiset.lean` and saw your comments on the dependent recursor


{% endraw %}
