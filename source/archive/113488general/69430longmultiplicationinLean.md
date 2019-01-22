---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/69430longmultiplicationinLean.html
---

## [general](index.html)
### [long multiplication in Lean](69430longmultiplicationinLean.html)

#### [Kevin Buzzard (Jan 12 2019 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/long%20multiplication%20in%20Lean/near/154983199):
`nat` is great for proving things, but is computationally inefficient because it uses O(n) memory to store the natural number n:

`#reduce 10000 * 10000 -- deep recursion error`

`pos_num` is a computationally efficient implementation of the positive integers in Lean.

```lean
inductive pos_num : Type
| one  : pos_num
| bit1 : pos_num → pos_num
| bit0 : pos_num → pos_num
```

Now we only need O(log n) memory to store n. But I must be using it incorrectly because I see performance issues:

```lean
import data.num.basic

-- takes a few seconds on my machine 
#reduce (10000 : pos_num) * 10000 -- binary repn of 10^8

-- (deterministic) timeout
#reduce (1000000 : pos_num) * 1000000
```

Why are these things not instantaneous, like they would be in a computer algebra system? Lean has clearly solved these problems somehow, because computationally efficient types are presumably at the root of why these proofs work:

```lean
import tactic.norm_num

-- all this is immediate
example : (10000 : ℕ) * 10000 = 100000000 := by norm_num
example : (1000000 : ℕ) * 1000000 = 1000000000000 := by norm_num
```

Oh! `tactic.norm_num` does not even seem to import `data.num.basic`! So it must be using something else. The `norm_num.lean` file looks much less scary to me than it did a year ago, but I still can't see how it is doing multiplication (maybe because there is no 50 line module docstring ;-) )

#### [Mario Carneiro (Jan 12 2019 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/long%20multiplication%20in%20Lean/near/154983632):
The norm_num interactive tactic actually delegates addition, subtraction and multiplication to `tactic.norm_num` in core

#### [Kevin Buzzard (Jan 12 2019 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/long%20multiplication%20in%20Lean/near/154983812):
Oh! And am I right in thinking that this is written in C++?

#### [Kevin Buzzard (Jan 12 2019 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/long%20multiplication%20in%20Lean/near/154983814):
`meta constant norm_num : expr → tactic (expr × expr)`

meta constants are in some sense invisible to me.

#### [Rob Lewis (Jan 12 2019 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/long%20multiplication%20in%20Lean/near/154984074):
Yes, the core `norm_num` is in C++. For addition and multiplication it works basically like a special purpose simplifier: `bit0 a + bit0 b` simplifies to `bit0 (a + b)`, etc. But it does this in the context of proving an equality, so it really changes `bit0 a + bit0 b = c` to `bit0 (a + b) = c` where `c` is in normal form. This makes it easy to reduce `-` and `/` to `+` and `*`.

#### [Mario Carneiro (Jan 12 2019 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/long%20multiplication%20in%20Lean/near/154986513):
The reason why `#reduce (10000 : pos_num)` is slow is because the parser produces `bit0` and `bit1` applications, which could be defined in terms of the constructors of the `pos_num` type but instead uses the fixed definition `_root_.bit0` which is defined using self-addition. As a result the `bit0` operation is linear time instead of O(1), and a full numeral should be O(n^2) to evaluate (rather than O(n)). But it is still much better than the exponential time implementation for `nat`. This could be solved if there was a typeclass like `has_bit` providing the bit operations directly

#### [Mario Carneiro (Jan 12 2019 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/long%20multiplication%20in%20Lean/near/154986619):
It looks like the equation compiler definitions of `pos_num.add` and `pos_num.succ` are also significant factors. If I define the functions using `pos_num.rec` or the induction tactic then it goes much faster

