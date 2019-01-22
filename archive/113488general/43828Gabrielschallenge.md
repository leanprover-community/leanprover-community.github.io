---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/43828Gabrielschallenge.html
---

## [general](index.html)
### [Gabriel's challenge](43828Gabrielschallenge.html)

#### [Kevin Buzzard (Apr 02 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504672):
Can you do Gabriel's exercise?

#### [Kevin Buzzard (Apr 02 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504673):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/elaborator

#### [Kevin Buzzard (Apr 02 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504678):
` theorem  very_easy : unit = unit :=
by  do exact $ ???`

#### [Kevin Buzzard (Apr 02 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504679):
Can you make an expr which corresponds to `eq.refl unit`?

#### [Kevin Buzzard (Apr 02 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504716):
Talking of tactics reminded me of this.

#### [Kevin Buzzard (Apr 02 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504720):
I could only make a `tactic expr`

#### [Simon Hudon (Apr 02 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504727):
Is that against the rules of the game?

#### [Kevin Buzzard (Apr 02 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504764):
I wasn't sure.

#### [Kevin Buzzard (Apr 02 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504768):
because I know absolutely nothing about exprs

#### [Kevin Buzzard (Apr 02 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504769):
or whether it's possible to make them

#### [Kevin Buzzard (Apr 02 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504770):
I thought that `eq.refl unit` was an expression in Lean

#### [Kevin Buzzard (Apr 02 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504776):
but I don't think it has type expr

#### [Simon Hudon (Apr 02 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504777):
For unit, you could do: `do exact $ expr.const ``unit.star []`

#### [Kevin Buzzard (Apr 02 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504819):
stop at that one

#### [Kevin Buzzard (Apr 02 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504820):
that one works

#### [Kevin Buzzard (Apr 02 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504824):
were you having a backtick nightmare? ;-)

#### [Simon Hudon (Apr 02 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504830):
Yeah and I don't have an anti-tick shampoo!

#### [Simon Hudon (Apr 02 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504832):
How do you escape ticks?

#### [Kevin Buzzard (Apr 02 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504833):
```
open tactic expr
definition  very_easy : unit :=
by  do exact $ expr.const ``unit.star []
```

#### [Kevin Buzzard (Apr 02 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504835):
result!

#### [Simon Hudon (Apr 02 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504875):
There should be only one tick before `unit.star` though

#### [Kevin Buzzard (Apr 02 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504876):
`expr.const` wants a `name`

#### [Kevin Buzzard (Apr 02 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504877):
oh we are doing the bad thing which Patrick complained about

#### [Kevin Buzzard (Apr 02 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504878):
he wants us to buzz off to another thread

#### [Simon Hudon (Apr 02 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504883):
Co-opting a channel?

#### [Kevin Buzzard (Apr 02 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504885):
topic

#### [Kevin Buzzard (Apr 02 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504929):
Oh that was clever. I didn't know you could change in the middle

#### [Kevin Buzzard (Apr 02 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504937):
So a constructor is a `const`?

#### [Simon Hudon (Apr 02 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504939):
:grin: There's an option to change the topic of everything that comes after a certain post

#### [Simon Hudon (Apr 02 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504940):
Yes, that's correct

#### [Kevin Buzzard (Apr 02 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504979):
so how to change something like eq.refl into an expr?

#### [Simon Hudon (Apr 02 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504980):
Lean compiles `inductive` types into constants and axioms

#### [Simon Hudon (Apr 02 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504989):
Same thing ``const `eq.refl [`u]`` ... with the exception of the universe level

#### [Kevin Buzzard (Apr 02 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124504991):
because then you could use `expr.app` to apply the function

#### [Simon Hudon (Apr 02 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505033):
Yes, you would first apply it to a `Sort u` and then to whatever term you want prove equal to itself

#### [Kevin Buzzard (Apr 02 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505039):
` infer type failed, incorrect number of universe levels`

#### [Kevin Buzzard (Apr 02 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505040):
woo, new error messages

#### [Simon Hudon (Apr 02 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505078):
That's curious! I'm pretty sure there should be only one

#### [Kevin Buzzard (Apr 02 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505083):
I honestly think that playing around with this sort of thing would be a good introduction to tactics.

#### [Kevin Buzzard (Apr 02 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505089):
because it gives you the idea of what an expr really is and begins to introduce stuff like the backtick hell before going meta

#### [Simon Hudon (Apr 02 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505090):
What you can do to see what's wrong is:

```lean
do c <- mk_const `eq.refl`,
   trace (c.to_raw_fmt)
```

#### [Simon Hudon (Apr 02 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505130):
Interesting! Thanks for the suggestion. I'll add some of that to my tutorial

#### [Kevin Buzzard (Apr 02 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505139):
Am I right in thinking that tactics could really be said to be acting on the exprs

#### [Kevin Buzzard (Apr 02 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505141):
and that you really have to have some sort of clear idea of what an expr is before moving on to tactics?

#### [Simon Hudon (Apr 02 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505142):
Yes, that's really the main data structure

#### [Kevin Buzzard (Apr 02 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505146):
so everyone has an informal idea of what one is

#### [Simon Hudon (Apr 02 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505147):
Completely

#### [Kevin Buzzard (Apr 02 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505148):
because they have written some Lean code

#### [Kevin Buzzard (Apr 02 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505189):
and they are told that they are constructing expressions of certain types

#### [Simon Hudon (Apr 02 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505190):
And maybe an explanation of what a proof goal is would also help

#### [Kevin Buzzard (Apr 02 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505191):
but actually they are not constructing the exprs themselves

#### [Kevin Buzzard (Apr 02 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505192):
What is a proof goal?

#### [Kevin Buzzard (Apr 02 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505193):
There is some "interesting" comment in PIL

#### [Kevin Buzzard (Apr 02 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505236):
there it is, p38

#### [Kevin Buzzard (Apr 02 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505237):
`8.5 Metavariables and Unification
[This section is still under construction. It will discuss the notion of a metavariable and
its local context, with the interesting bit of information that goals in the tactic state are
nothing more than metavariables. So the goal list is really just a list of metavariables,
which can help us make sense of the get_goals and set_goals tactics. It will also discuss
the unify tactic.]`

#### [Simon Hudon (Apr 02 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505289):
A proof goal is basically an unassigned meta variable. It has no special status. You can think of a proof in tactic mode as creating one metavariable, saying that it's the proof of the main goal and then telling you to assign a value to that metavariable `v` by calling `set_goals [v]`

#### [Simon Hudon (Apr 02 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505326):
But you can set any list of unassigned metavariables as the goals in a proof even if they are not relevant.

#### [Simon Hudon (Apr 02 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505385):
Does that make sense?

#### [Kevin Buzzard (Apr 02 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505441):
set_goals doesn't make sense, but I can guess what it means.

#### [Kevin Buzzard (Apr 02 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505442):
so it makes some sort of sense

#### [Mario Carneiro (Apr 02 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505672):
@**Kevin Buzzard** To construct an expr, you can use the `` `(...)`` syntax

#### [Kevin Buzzard (Apr 02 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505679):
There is one backtick and two backticks and three backticks and none of them really make much sense to me

#### [Kevin Buzzard (Apr 02 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505680):
I can read the definitions but they don't stick yet

#### [Kevin Buzzard (Apr 02 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505681):
I am wondering if playing with exprs like this without thinking about tactics would be a better way to explain how all the backticks work

#### [Simon Hudon (Apr 02 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505728):
If you want to implement `have` for example, you could do it this way:

```lean
meta def my_have (h : name) (p : expr) : tactic unit :=
do (g :: gs) <- get_goals,
   prf <- mk_meta_var p, -- the side goal
   g' <- mk_mvar, -- not giving a type, we'll let `unify` guess it
   let prove_g := expr.app (expr.lam h binder_info.default p g') prf,
   unify prove_g g,
   set_goals (prf :: g' :: gs)
```

#### [Kevin Buzzard (Apr 02 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505766):
aah but now you're in tactic mode

#### [Kevin Buzzard (Apr 02 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505771):
I was wondering whether one could write something about creating raw exprs without ever mentioning the tactic monad

#### [Kevin Buzzard (Apr 02 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505772):
as an introduction to the backtick notation and to exprs

#### [Simon Hudon (Apr 02 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505774):
Yes, for two reasons: so that we can set and get the goals and so that we can create metavariables that are valid within the scope of the current proof

#### [Kevin Buzzard (Apr 02 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505775):
without having to introduce them at the same time as introducing all the tactic monad stuff

#### [Simon Hudon (Apr 02 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505783):
Oh ... and for unification. Since a meta variable is meaningful only in the context of a specific proof, you need the proof state when you assign a value to one.

#### [Mario Carneiro (Apr 02 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505822):
```
open tactic
theorem very_easy : unit = unit :=
by do exact `(eq.refl unit)

theorem very_easy₂ : unit = unit :=
by do mk_eq_refl `(unit) >>= exact

theorem very_easy₃ : unit = unit :=
by do exact $
  (expr.const ``eq.refl [level.of_nat 2] : expr)
  (expr.sort $ level.of_nat 1)
  (expr.const ``unit [])
```

#### [Simon Hudon (Apr 02 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505823):
But we're not discharging a goal completely here

#### [Kevin Buzzard (Apr 02 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505824):
it was `level.of_nat 1` I  was missing

#### [Kevin Buzzard (Apr 02 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505825):
Thanks Mario.

#### [Mario Carneiro (Apr 02 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505830):
you can also write `level.succ level.zero`

#### [Kevin Buzzard (Apr 02 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505832):
oh wow there is `mk_eq_refl`

#### [Simon Hudon (Apr 02 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505873):
Ah! That's the part I didn't think of! you were trying to prove `unit = unit`

#### [Kevin Buzzard (Apr 02 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505874):
I was trying to learn basic stuff about how to build exprs without going into tactic mode

#### [Kevin Buzzard (Apr 02 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505879):
no `expr.app` in version 3?

#### [Kevin Buzzard (Apr 02 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505880):
what's going on there?

#### [Mario Carneiro (Apr 02 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505881):
The last example is a bit artifical though, since usually you will not construct a complete expr by hand like that. Here's a half-tactic way to construct it:
```
theorem very_easy₄ : unit = unit :=
by do
  u ← mk_const ``unit,
  e ← mk_app ``eq.refl [u],
  exact e
```

#### [Kevin Buzzard (Apr 02 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505883):
I thought Lean was expecting one expr after the dollar sign and you passed three?

#### [Simon Hudon (Apr 02 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505924):
It's because of:

```
meta instance : has_coe_to_fun (expr elab) :=
{ F := λ e, expr elab → expr elab, coe := λ e, expr.app e }
```

#### [Mario Carneiro (Apr 02 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505925):
`expr` has a lovely coe_fn instance that allows you to write applications like that

#### [Mario Carneiro (Apr 02 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Gabriel%27s%20challenge/near/124505969):
```
theorem very_easy₃' : unit = unit :=
by do exact $
  expr.app (expr.app
    (expr.const ``eq.refl [level.of_nat 2])
    (expr.sort $ level.of_nat 1))
  (expr.const ``unit [])
```

