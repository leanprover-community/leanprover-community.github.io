---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04700examplex2x0sorry.html
---

## Stream: [general](index.html)
### Topic: [example (x : ℕ) : ¬ (2 + x = 0) := sorry](04700examplex2x0sorry.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 04 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124642055):
It is forever taking me 3 lines to prove stuff like this. What's a slick way of doing this quickly?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 04 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124642141):
`rw add_comm; apply succ_ne_zero`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644443):
```
example (x : ℕ) : ¬ (2 + x = 0) :=
by cases x; apply nat.no_confusion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644446):
So you (Mario) decided to do it in tactic mode. Looking at this example I realise I didn't really understand what `apply` actually does.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644490):
oh hey our solutions have exactly the same length

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644493):
he opened nat!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644496):
oh right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644498):
so i win

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644500):
in some sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644502):
He answered first

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644504):
well i was sleeping

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644512):
solutions aren't totally ordered

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644519):
you always win if you get to choose the ordering

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644528):
Let me think about Mario's solution.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644542):
`apply [xxx]`, where `[xxx] : A -> B -> C -> D` attempts to match `D` with the goal, and set `A`, `B`, `C` as three new goals if necessary

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644544):
`x + 2` unfolds to `x + bit0 1` which unfolds to `x + (1 + 1)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644550):
and I can't match this with nat.succ anything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644596):
oh I have to unfold more

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644602):
```
example (x : ℕ) : x + 2 = nat.succ (x + 1) := rfl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644603):
`x + succ 1, succ (x + 1)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644605):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644617):
but there's still more to do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644618):
how so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644624):
because apply is not exact

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644625):
and this is not exact

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644670):
the goal is `f(succ x)` and we solve it with `forall n, f(n)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644675):
```
example (x : ℕ) : ¬ (2 + x = 0) :=
by rw add_comm; exact nat.succ_ne_zero (x+1)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644676):
`apply` automatically fills out the arguments for you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644678):
I've seen it not automatically fill out the arguments for me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644681):
and I've had to use refine instead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644693):
well I can't say anything if you don't have an example

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644698):
yeah and I can't read the definition of apply because it's in meta land

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644739):
I guess I've sometimes tried to apply to partially close a goal and it's failed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644750):
I guess I just have to read the docstring more carefully.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644764):
```
/--
The `apply` tactic tries to match the current goal against the conclusion of the type of term. The argument term should be a term well-formed in the local context of the main goal. If it succeeds, then the tactic returns as many subgoals as the number of premises that have not been fixed by type inference or type class resolution. Non-dependent premises are added before dependent ones.

The `apply` tactic uses higher-order pattern matching, type class resolution, and first-order unification with dependent types.
-/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 05 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124650332):
I used `apply` in that example simply as a shorthand for `exact` (or `refine` nonterminally), it saves me a few underscores at the end. It doesn't always work, but I think it works here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (Apr 05 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124653601):
what about `rw add_comm; from dec_trivial`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124653603):
does it work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (Apr 05 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124653644):
https://leanprover.github.io/live/latest/#code=variable%20x%20:%20nat%0A%0Aexample%20:%20%C2%AC%20(2%20+%20x%20=%200)%20:=%20by%20rw%20add_comm;%20from%20dec_trivial

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124653651):
you win

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 05 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124653845):
`simp; from dec_trivial`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 05 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124653851):
ok you win

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 05 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124653852):
Or import lean-tidy and: `obviously`.


{% endraw %}
