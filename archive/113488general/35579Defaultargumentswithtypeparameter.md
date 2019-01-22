---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35579Defaultargumentswithtypeparameter.html
---

## [general](index.html)
### [Default arguments with type parameter](35579Defaultargumentswithtypeparameter.html)

#### [Keeley Hoek (Aug 18 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Default arguments with type parameter/near/132355082):
I've got a (honest, in-a-program) function
````
def do_some_stuff {α : Type} (cfg : config α) := xxx
````
In an ideal world, I'd like to be able to have a default `config`, with a fixed parameter `α` (obviously), so I could write `do_some_stuff` and everything would work great. I guess I want to be able to write (and compile)
````
def default_config : config string := xxx
def do_some_stuff {α : Type} (cfg : config α := default_config) := xxx
````
with that having the meaning that if `cfg` is omitted, the type `α` is forced to be `string`.

I see that I might be "fighting the system". What do you think is the best way to emulate this kind of option-passing interface?

#### [Mario Carneiro (Aug 18 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Default arguments with type parameter/near/132357334):
This comes up in core lean in some of the structures, where you have to give `A` such that `A = B`, and the proof of `A = B` is `rfl` but this only works if `A` is `B`. You can set this up using auto params instead of opt params:
```
def config : Type → Type := sorry
def default_config : config string := sorry
meta def default_config_tac : tactic unit := `[exact default_config]
def do_some_stuff {α : Type} (cfg : config α . default_config_tac) : α := sorry

example : string := do_some_stuff -- ok
example : nat := do_some_stuff (sorry : config ℕ) -- ok
example : nat := do_some_stuff -- error

```

#### [Keeley Hoek (Aug 18 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Default arguments with type parameter/near/132357505):
Thanks so much Mario. Do you know where I could read about the auto params "." period syntax?

#### [Mario Carneiro (Aug 18 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Default arguments with type parameter/near/132357514):
It might be in the reference manual? It's very simple. You can only put a name of a def of a `tactic unit` there, and it gets called when the argument is not supplied

#### [Mario Carneiro (Aug 18 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Default arguments with type parameter/near/132357522):
I wish it would accept an expression so you could write a tactic inline there, but alas

#### [Keeley Hoek (Aug 18 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Default arguments with type parameter/near/132357563):
ok sweet! cheers!

#### [Mario Carneiro (Aug 18 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Default arguments with type parameter/near/132357567):
(actually there is a good reason you can't write a tactic inline, since that would be `meta`)

