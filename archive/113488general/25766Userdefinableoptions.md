---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/25766Userdefinableoptions.html
---

## Stream: [general](index.html)
### Topic: [User definable options](25766Userdefinableoptions.html)

---

#### [Joe Hendrix (Jan 12 2019 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/User%20definable%20options/near/154955190):
Is there a way that I can set user definable options that can be parsed by tactics?  I have some proofs that take a while to run, and I'd like to be able to have an option at the file or lean package level that let me configure whether they ran or not.  e.g., during interactive development I disable proofs I'm not actually working on, but in a regression test they are enabled.
I noticed within a single run of the tactic monad, I can set custom option names (e.g., `set_options (opt.set_bool "enable_unsafe_tac" tt)`), but the value doesn't appear to show up in tactics farther down the file.  The set_option command also doesn't allow custom options.

#### [Sebastian Ullrich (Jan 12 2019 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/User%20definable%20options/near/154982882):
`set_option` accepts only built-in options, but using the `set_options` primitive should work. Did you execute that code in a `run_command`?

#### [Joe Hendrix (Jan 22 2019 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/User%20definable%20options/near/156639542):
Sorry for the delay; I didn't see this until today.  Here's a sample script:
```
open tactic

meta
def get_my_opt : tactic unit := do
  o ← get_options,
  trace (repr (o.get_bool "foo" ff))

meta
def set_my_opt : tactic unit := do
  o ← get_options,
  set_options (o.set_bool "foo" tt),
  get_my_opt

run_cmd get_my_opt
run_cmd set_my_opt
run_cmd get_my_opt
```

The output I get is:
```
ff
tt
ff
```

So `set_options` works in the current command, but the option is forgotten in subsequent commands.

#### [Sebastian Ullrich (Jan 22 2019 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/User%20definable%20options/near/156642096):
Ah, that's too bad. You may want to fake the option with a custom attribute (which can be set globally or locally, but unset only locally). I'm not aware of a better solution.

#### [Joe Hendrix (Jan 22 2019 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/User%20definable%20options/near/156643580):
Thanks, that seems to work well.

#### [Mario Carneiro (Jan 22 2019 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/User%20definable%20options/near/156644445):
Is this improving in lean 4? More generally, it would be nice if there was a way to persist arbitrary data across different commands. Does everything have to go via adding defs to the environment?

#### [Joe Hendrix (Jan 23 2019 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/User%20definable%20options/near/156665743):
I could see use cases for persisting data, but I also think it's important that tactics could be run concurrently, and the results cached.  Given that goal, `set_options` behavior  doesn't seem to surprising.
In Haskell, you can define package level options and use them to define constants that can be checked at compile time (via CPP).  That's what I was hoping for here, so I could pass a flag to build or configure that controlled whether an axiom was allowed to be used.  The attribute trick doesn't seem too bad though.

