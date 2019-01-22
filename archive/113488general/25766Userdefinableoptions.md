---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/25766Userdefinableoptions.html
---

## [general](index.html)
### [User definable options](25766Userdefinableoptions.html)

#### [Joe Hendrix (Jan 12 2019 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/User definable options/near/154955190):
Is there a way that I can set user definable options that can be parsed by tactics?  I have some proofs that take a while to run, and I'd like to be able to have an option at the file or lean package level that let me configure whether they ran or not.  e.g., during interactive development I disable proofs I'm not actually working on, but in a regression test they are enabled.
I noticed within a single run of the tactic monad, I can set custom option names (e.g., `set_options (opt.set_bool "enable_unsafe_tac" tt)`), but the value doesn't appear to show up in tactics farther down the file.  The set_option command also doesn't allow custom options.

#### [Sebastian Ullrich (Jan 12 2019 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/User definable options/near/154982882):
`set_option` accepts only built-in options, but using the `set_options` primitive should work. Did you execute that code in a `run_command`?

