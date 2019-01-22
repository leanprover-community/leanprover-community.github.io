---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54961reflectedalpha.html
---

## [general](index.html)
### [reflected \alpha](54961reflectedalpha.html)

#### [Keeley Hoek (Nov 21 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected \alpha/near/148091917):
This probably counts as a newbie question, sorry:

What is the purpose of the typeclass instance `[reflected \alpha]` which `eval_expr` takes? Why can the typeclass system work out what it is most of the time, but sometimes when you pass a custom structure withh few boring nested structures it freaks out?

#### [Mario Carneiro (Nov 21 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected \alpha/near/148092166):
it needs to know how to produce expressions from a VM value

#### [Mario Carneiro (Nov 21 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected \alpha/near/148092175):
I don't know what the freakout problem is

#### [Keeley Hoek (Nov 21 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected \alpha/near/148093813):
Ok
I will try to concoct

#### [Keeley Hoek (Nov 21 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected \alpha/near/148097478):
Consider this little snippet:
````
structure a_struct (α : Type) :=
(val : α)

def make_struct : a_struct unit := ⟨()⟩

meta def go (tv : Type) : tactic unit := do
  e ← tactic.mk_app `make_struct [],
  tactic.eval_expr (a_struct tv) e,                 /-  failed to synthesize type class instance for ⊢ reflected (a_struct tv) -/
  tactic.skip

#eval (go unit)

````

#### [Sebastian Ullrich (Nov 21 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected \alpha/near/148097603):
`reflected` can only be synthesized for closed (parts of) expressions, so `go` needs a `[reflected tv]` parameter

#### [Keeley Hoek (Nov 21 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected \alpha/near/148106110):
In principle, is there any way to make something like this:
````
set_option trace.app_builder true

structure signature :=
(α : Type)

structure container_struct :=
(c : signature)
(val : c.α)

meta def go : tactic unit := tactic.down $ do
  e ← tactic.up $ tactic.mk_app `container_struct.mk [`({signature . α := nat}), `(2)],
  tactic.eval_expr container_struct e.down,
  tactic.up $ tactic.skip

run_cmd go

-- [app_builder] failed to create an 'container_struct.mk'-application,
-- failed to solve unification constraint for #2 argument (?x_0.α =?= ℕ)

````
work? I'd really like to be able to persuade lean to be able to solve that constraint (why can't it? :'()

(Please mind the `tactic.up` and `tactic.down`s, which are just dealing with the fact that `container_struct` is `Type 1`.)

#### [Sebastian Ullrich (Nov 21 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected \alpha/near/148106771):
That might be an issue with `tactic.mk_app`, can you try with the full `tactic.to_expr`?

#### [Keeley Hoek (Nov 21 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected \alpha/near/148107099):
@**Sebastian Ullrich** Brilliant! Thanks so much, lots of time of potentially lost work saved

#### [Keeley Hoek (Nov 22 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected \alpha/near/148159497):
Here's another mini-problem. I'm just going to store a variable `a` of arbitrary type `α` in a structure in two different ways:
````
structure struct_v1 (α : Type) :=
(a : α)

structure struct_v2 :=
(α : Type)
(a : α)

def v1_def : struct_v1 nat := ⟨3⟩

def v2_def : struct_v2 := ⟨nat, 3⟩
````


Now I'll try to dynamically fetch these structures, first for version 1, and second for version 2:
````
meta def go_1 (t : Type) : tactic unit :=
  let n := `v1_def in do
  e ← tactic.resolve_name n >>= tactic.to_expr,

-- failed to synthesize type class instance for
-- ⊢ reflected (struct_v1 t)
  tactic.eval_expr (struct_v1 t) e,

  return ()

run_cmd go_1 nat

meta def go_2 : tactic unit := tactic.down $
  let n := `v2_def in do
  e ← tactic.up $ tactic.resolve_name n >>= tactic.to_expr,
  tactic.eval_expr struct_v2 e.down,
  tactic.up $ return ()

run_cmd go_2
````
I get a reflection error in only the first way, even though the type could be arbitrary in either case. What's the difference between these constructions?

#### [Sebastian Ullrich (Nov 22 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected \alpha/near/148162400):
In both versions, you need a reflected term of the type. In version 2, that is already part of `v2_def`(defs are stored as `expr`s after all). In version 1, you need an explicit `[reflected t]`. That is the difference.

