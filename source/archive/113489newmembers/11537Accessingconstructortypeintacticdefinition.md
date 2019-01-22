---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/11537Accessingconstructortypeintacticdefinition.html
---

## [new members](index.html)
### [Accessing constructor type in tactic definition](11537Accessingconstructortypeintacticdefinition.html)

#### [Jesse Michael Han (Oct 18 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136019547):
Hello everyone,

I'm trying to write the following function:

```lean
inductive hewwo : Type
| foo : nat → hewwo
| bar : nat → hewwo

def g : hewwo → ℕ :=
begin
intro hello,
cases hello,
sorry --help! intended behavior is g foo k = 0, g bar k = 1
end
```
where the goal state at the `sorry` is

```lean
2 goals
case hewwo.foo
hello : nat
⊢ nat

case hewwo.bar
hello : nat
⊢ nat
```

I know the sane way to do this is to just use the equation compiler, but I want to know: in this situation, how can I introduce new hypotheses which have the type of the constructors `foo` and `bar` into context?

If I furthermore write something like
```lean
def g : hewwo → ℕ :=
begin
intro hello,
cases hello,
{cases hewwo.foo,}
end
```
the error message gives something tantalizing close:
```lean
219:2: cases tactic failed, it is not applicable to the given hypothesis
state:
hello : nat,
_x : nat → hewwo
⊢ nat
```

but I don't know how to access this `_x` normally.

#### [Johan Commelin (Oct 18 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136019612):
@**Jesse Michael Han** Your to goals are tagged with a descriptive name. It contains "foo" and "bar".

#### [Johan Commelin (Oct 18 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136019652):
Your actual "foo" and "bar" is still called `hello`.

#### [Johan Commelin (Oct 18 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136019660):
Hmmm, that is not exactly correct. Sorry. So you have a `hello : nat` in those contexts. And that is the one you want to provide. (Your goal is also a `nat`.)

#### [Johan Commelin (Oct 18 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136019661):
My point is, you can close the goal with ~~`exact hello`~~ (see below).

#### [Mario Carneiro (Oct 18 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136019707):
well, I think he wants `exact 0, exact 1`

#### [Bryan Gin-ge Chen (Oct 18 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136019709):
Is this what you want?
```lean
inductive hewwo : Type
| foo : nat → hewwo
| bar : nat → hewwo

def g : hewwo → ℕ :=
begin
intro hello,
cases hello,
{ exact 0 },
{ exact 1 }
end

#eval g (hewwo.foo 40)
#eval g (hewwo.bar 4)
```

#### [Jesse Michael Han (Oct 18 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136020216):
Thanks for the prompt responses, guys! You're right, I should have chosen a less trivial toy intended behavior.

@**Johan Commelin** Okay, I see. So, to introduce that `_x`, I can just use `have := hewwo.foo` (resp. `bar`).

#### [Bryan Gin-ge Chen (Oct 18 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136020333):
What's the actual thing you're trying to do? `have := hewwo.foo` only gives you a hypothesis `this : ℕ → hewwo`.

#### [Bryan Gin-ge Chen (Oct 18 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136020477):
Oh, I misread your first message. I guess that's what you wanted after all.

#### [Jesse Michael Han (Oct 18 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136020878):
Right, I was just wondering where the data on the left hand side (if you write this using the equation compiler):
```lean
def HEWWO : hewwo → ℕ
| (foo i) := 0
| (bar i) := 1
```
goes if you try to write it with tactics instead. As Johan pointed out (and as I failed to notice :^)), once inside the case environment, Lean introduces `hello : nat` corresponding to `i`, and we can retrieve `foo` with `have :=`.

#### [Bryan Gin-ge Chen (Oct 18 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136021621):
When you're using `cases` to define a function, you don't need to worry about retrieving `foo` or `bar` anymore. `cases` takes care of all of that automatically. All you have to do is provide terms of the output type `nat` when it asks you to. 

Note that `have := hewwo.foo` doesn't depend on anything the `cases` statement introduces. You can write it before or after the `cases` statement with exactly the same effect. All the `have` tactic does is introduce a new term into the tactic state.  Furthermore, all that lean remembers from `have` is the type of the term after `:=`, so it's mostly useful for introducing proof terms and not data. In particular, you can check that the tactic state is the same whether you write `have := hewwo.foo` or `have := hewwo.bar`. 

Sometimes it can be useful to introduce local definitions, e.g. notation for a function or some other piece of "data", but to do that, one uses `let` instead.

#### [Jesse Michael Han (Oct 18 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136022027):
> Note that have := hewwo.foo doesn't depend on anything the cases statement introduces. You can write it before or after the cases statement with exactly the same effect. All the have tactic does is introduce a new term into the tactic state. Furthermore, all that lean remembers from have is the type of the term after :=, so it's mostly useful for introducing proof terms and not data. In particular, you can check that the tactic state is the same whether you write have := hewwo.foo or have := hewwo.bar. 

I see---thanks!

