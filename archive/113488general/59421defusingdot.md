---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59421defusingdot.html
---

## Stream: [general](index.html)
### Topic: [def using dot](59421defusingdot.html)

---

#### [Chris Hughes (Apr 05 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124678478):
How does this definition work? 
```lean
def  empty.elim {C : Sort*} : empty → C.
```
What does the dot at the end do? I haven't seen that before.

#### [Kenny Lau (Apr 05 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124678484):
"it's too obvious I don't even wanna write "rfl""

#### [Simon Hudon (Apr 05 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124680675):
I don't think that's it. I think it's a definition by pattern matching and `empty` has no constructors. I haven't seen `.` used that way before but it looks to me like it signals that we're done with the pattern matching.

#### [Chris Hughes (Apr 05 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124680900):
How does this notation work in general, for things with constructors?

#### [Simon Hudon (Apr 05 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124680970):
You mean with the dot or just pattern matching definitions?

#### [Chris Hughes (Apr 05 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124680993):
With the dot

#### [Simon Hudon (Apr 05 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124681319):
I haven't seen many more examples but I found these:

```lean
lemma not_succ_le_zero : ∀ (n : ℕ), succ n ≤ 0 → false
.
lemma bool.ff_ne_tt : ff = tt → false
.
```

I think you just put it in instead of a pattern matching to signal that there are no constructors.

#### [Gabriel Ebner (Apr 05 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124681520):
In general the dot is an optional command delimiter, you can always use it if you want:
```lean
def foo : ℕ → ℕ | x := x+1.
```

#### [Gabriel Ebner (Apr 05 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124681558):
If you want to write a definition using pattern matching and you have zero equations, then the dot is mandatory.  The examples above have zero equations.

#### [Gabriel Ebner (Apr 05 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124681664):
In case you didn't know, this definition syntax is essentially just sugar for a nested match.  Here it is maybe clearer that there are zero equations:
```lean
example {C : Sort*} (h : ff = tt) : C :=
match h with end
```

#### [Gabriel Ebner (Apr 05 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124681854):
To give you an intuition for when this zero-equation magic works, recall that the equation compiler is (ignoring lots and lots of details) a wrapper around the `cases` tactic.  Whenever iterated `cases` would yield zero subgoals, then you can use this magic.
```lean
example : ¬ (∃ n, n < 0).
```

