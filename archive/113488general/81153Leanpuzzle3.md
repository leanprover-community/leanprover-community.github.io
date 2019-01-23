---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/81153Leanpuzzle3.html
---

## Stream: [general](index.html)
### Topic: [Lean puzzle #3](81153Leanpuzzle3.html)

---

#### [Keeley Hoek (Nov 27 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20puzzle%20%233/near/148625272):
Next up in my series of lean puzzles, consider the following code snippet:
````lean
universe u

meta def do_some_nonsense {α : Type u} (t : tactic α) : tactic α :=
  tactic.down (tactic.up (tactic.trace "ELLO1") >> tactic.up t)

meta def do_some_nonsense' {α : Type u} (t : tactic α) : tactic α :=
  (tactic.up (tactic.trace "ELLO2") >> t)

meta def tactic_bind_override {α β : Type u} (t₁ : tactic α) (t₂ : α → tactic β) : tactic β :=
-- do_some_nonsense (t₁ >>= (λ a, t₂ a))
do_some_nonsense' (t₁ >>= (λ a, t₂ a))

@[inline, instance, priority 2000] meta def bind_override : has_bind tactic :=
⟨@tactic_bind_override⟩

meta def go : tactic unit :=
tactic.trace "A"

run_cmd go
````

#### [Keeley Hoek (Nov 27 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20puzzle%20%233/near/148625276):
We are just stealing control of the `bind` function associated to the tactic monad, to prepend every single bind with a trace statement by calling `do_some_nonesense` (possibly the primed version). If you run the code as I have given it, the expected
````
ELLO2
A
````
will be printed. On the other hand, try uncommenting the commented line and commenting the line below it. This calls a slightly different version of `do_some_nonsense`, but no longer prints `ELLO1` before the `A`. Indeed, if you use `set_option trace.compiler.optimize_bytecode true` to inspect the code emitted for the `go` function, you will see that no call to `tactic_bind_override` is even being made anymore and lean is resorting to the builtin `interaction_monad_bind`.

#### [Keeley Hoek (Nov 27 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20puzzle%20%233/near/148625320):
The puzzle: determine why this is. (Spoiler, I have no idea)

#### [Keeley Hoek (Nov 27 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20puzzle%20%233/near/148625471):
Serious hint but still what the: replacing `tactic.down` with `tactic.down.{0}` makes it work

#### [Sebastian Ullrich (Nov 27 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20puzzle%20%233/near/148625601):
what the

#### [Gabriel Ebner (Nov 27 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20puzzle%20%233/near/148626504):
This is interesting!  You might want to look at the universe parameters of the declarations:
```lean
#eval do
env ← get_env,
[``tactic_bind_override, ``do_some_nonsense, ``do_some_nonsense']
  .for_each $ λ n, do
    decl ← returnex $ env.get n,
    trace (n, decl.univ_params)
/-
scratch20181127.lean:18:0: information trace output
(tactic_bind_override, [u])
(do_some_nonsense, [u, u_1])
(do_some_nonsense', [u])
-/
```

#### [Sebastian Ullrich (Nov 27 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20puzzle%20%233/near/148626617):
There really should be a linter for non-inferable instances :)

