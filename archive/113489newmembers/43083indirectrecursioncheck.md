---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/43083indirectrecursioncheck.html
---

## [new members](index.html)
### [indirect recursion check](43083indirectrecursioncheck.html)

#### [Scott Olson (Sep 27 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/indirect recursion check/near/134713724):
A while ago I was porting some code from Coq to Lean and it was going very well, but there was one definition that reduces to something like this:

```lean
def foo (f : ℕ → bool) (n : ℕ) : bool := 
    f n

def bar : ℕ → bool
| 0     := true
| (n+1) := foo bar n
```

I get "unexpected occurrence of recursive function" on `bar`. Is there any way to make this kind of definition work, and prove termination? I'm actually kind of surprised it worked in Coq in the first place...

#### [Scott Olson (Sep 27 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/indirect recursion check/near/134713786):
Effectively, you need to prove that `foo` only calls `bar` with something smaller than `n+1`, which it does in this case. Maybe it's technically possible, but the equation compiler in particular doesn't support it?

#### [Simon Hudon (Sep 27 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/indirect recursion check/near/134717621):
It this example, you can inline `foo` but I assume that's not an option with what you're working on ...

#### [Simon Hudon (Sep 27 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/indirect recursion check/near/134717700):
Otherwise, you can make `foo` and `bar` into mutually recursive functions

#### [Scott Olson (Sep 27 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/indirect recursion check/near/134719571):
It is possible but inconvenient to inline `foo` in the real code. It turned out more convenient to use a different approach to defining `bar` entirely.

When I try a mutually recursive approach, I still get the same "unexpected occurrence of recursive function" error (which comes from the pattern compiler, I assume):

```lean
mutual def foo, bar
with foo : (ℕ → bool) → ℕ → bool
| f n := f n
with bar : ℕ → bool
| 0     := true
| (n+1) := foo bar n
```

#### [Scott Olson (Sep 27 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/indirect recursion check/near/134719682):
When I find the time, I'll look up the original Coq example again for comparison.

#### [Mario Carneiro (Sep 27 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/indirect recursion check/near/134719755):
the idea is to define `bar` and `foo bar` by mutual recursion

#### [Mario Carneiro (Sep 27 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/indirect recursion check/near/134719758):
so you wouldn't have that first parameter in `foo`

#### [Simon Hudon (Sep 27 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/indirect recursion check/near/134719838):
What Mario said

#### [Simon Hudon (Sep 27 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/indirect recursion check/near/134720141):
So that would look like:

```lean
mutual def foo, bar
with foo : ℕ → bool
| n := bar n -- this will be trouble because `n` doesn't decrease
with bar : ℕ → bool
| 0     := true
| (n+1) := foo n
```

#### [Scott Olson (Sep 27 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/indirect recursion check/near/134720156):
Hmm, I suspect I still haven't fully understood, but here's my latest attempt:

```lean
-- (To be clear this is elsewhere, can't be changed, inconvenient to inline.)
def foo (f : ℕ → bool) (n : ℕ) : bool := f n

mutual def foo_bar, bar
with foo_bar : ℕ → bool
| n := foo bar n
with bar : ℕ → bool
| 0     := true
| (n+1) := foo_bar n
```

Which has the same "unexpected occurrence of recursive function" message.

#### [Mario Carneiro (Sep 27 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/indirect recursion check/near/134720226):
that is trouble, because you need to know that `foo` doesn't look at future values of `bar`

#### [Scott Olson (Sep 27 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/indirect recursion check/near/134720245):
Yeah, it's definitely fair for Lean to reject it. I think I'll come back to this thread when I've found the Coq example to compare with

#### [Mario Carneiro (Sep 27 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/indirect recursion check/near/134720292):
One option, used with things like `list.map`, is to use a theorem like `map_congr` to acquire an assumption that is needed for the recursion, or use a partial function like `list.pmap`

#### [Scott Olson (Sep 27 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/indirect recursion check/near/134720313):
I *think* the difference is Coq allowed the code with an explicit termination proof, whereas Lean's equation compiler won't even touch it

#### [Scott Olson (Sep 27 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/indirect recursion check/near/134720318):
Unlike simpler examples where you just need to prove something is decreasing

#### [Mario Carneiro (Sep 27 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/indirect recursion check/near/134720321):
lean allows explicit termination proofs, but you have to thread the proof through in a kind of awkward way

#### [Mario Carneiro (Sep 27 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/indirect recursion check/near/134720365):
I would need a more concrete example to demonstrate

#### [Scott Olson (Sep 27 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/indirect recursion check/near/134720386):
I've got to head out for now but I'll come back to this with more details

