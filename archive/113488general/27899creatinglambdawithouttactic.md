---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27899creatinglambdawithouttactic.html
---

## Stream: [general](index.html)
### Topic: [creating lambda without tactic](27899creatinglambdawithouttactic.html)

---


{% raw %}
#### [ Zesen Qian (Jul 30 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130588564):
meta programming problem: So I have a function body represented as `expr -> expr`, which receives a reference to the argument, and return the body. Is it possible to abstract the argument away(that is, wrap it with a lambda) and get the anonymous function back as `expr`?

#### [ Zesen Qian (Jul 30 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130588588):
I might have been blur about `expr` and `pexpr`, but I hope that won't cause too much confusion.

#### [ Jeremy Avigad (Jul 30 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130599168):
Look in `init/meta/expr.lean`. The trick is to create an `expr` with a local constant, use `abstract_local` to replace it by an index, and then bind it.

My experiments follow. In the first example, I used a local variable in the context. For some reason, `bind_lambda` didn't work in that case (the abstracted variable did not get the right type), so I did it by hand. In the second example, I made a fresh local variable.

```lean
open tactic

example (f : nat → nat) (x : nat) : nat → nat := by do 
f' ← get_local `f,
x' ← get_local `x,
let e := expr.app f' x',
trace e,  -- e is the expression f x
-- let e' := expr.bind_lambda e x', -- this didn't work
nt ← to_expr ``(nat),
let e' := expr.lam `x binder_info.default nt (e.abstract_local x'.local_uniq_name),
trace e',  -- e' is the expression λ (x : ℕ), f x
exact e'

example (f : nat → nat) : nat → nat := by do 
f' ← get_local `f,
nt ← to_expr ``(nat),
x' ← mk_local' `x binder_info.default nt,
e ← to_expr ``(%%f' %%x'),
trace e,  -- e is the expression f x
let e' := expr.bind_lambda e x',
trace e',  -- e' is the expression λ (x : ℕ), f x
exact e'
```

#### [ Zesen Qian (Jul 30 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130599995):
Thank you jeremy. But it seems `tactic` is still used in both cases? Specifically, you used `mk_local`. It seems quite hard to do this without tactic monad?

#### [ Zesen Qian (Jul 30 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130600130):
yeah I think I shouldn't be bother by using `tactic`.

#### [ Zesen Qian (Jul 30 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130600142):
I looked in the definition of `mk_local` and really, `mk_fresh_name` is all I need from the `tactic`.

#### [ Simon Hudon (Jul 30 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130600826):
Why is it important to not have the tactic monad?

#### [ Zesen Qian (Jul 30 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130600984):
because this is a proof that in principle can be exclusively derived from a data structure, without looking at the environment.

#### [ Zesen Qian (Jul 30 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130601087):
but anyway, the current solution is good enough, I only need a fresh name from the `tactic`monad, so that's minimal side effect.

#### [ Jeremy Avigad (Jul 31 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130608722):
If you are building expressions entirely from scratch, you can make up your own unique name if you want. But `expr` is `meta`, so if you want to stay entirely within the logic, you have to define your own type of expressions.

#### [ Zesen Qian (Jul 31 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130608796):
I'm actually thinking about using `pexpr.var : nat -> pexpr` which is de-bruijn index. So I don't have to worry about all the details of `local_const`.  I plan to construct the `pexpr` as a pure function of the LSEC proof, and elaborate the huge proof altogether.

#### [ Zesen Qian (Jul 31 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130609160):
@**Jeremy Avigad** yeah but if I do that we still need a conversion from my custom expr to the lean `expr`.

#### [ Jeremy Avigad (Jul 31 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20lambda%20without%20tactic/near/130609351):
If you are building Lean expressions, don't hesitate to use the tactic framework. You will probably need constants from the environment anyway, and your code will be easier to debug if you elaborate expressions piece by piece.


{% endraw %}
