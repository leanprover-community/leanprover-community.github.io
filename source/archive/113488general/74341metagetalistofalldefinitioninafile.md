---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74341metagetalistofalldefinitioninafile.html
---

## [general](index.html)
### [(meta) get a list of all definition in a file](74341metagetalistofalldefinitioninafile.html)

#### [Zesen Qian (Aug 14 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28meta%29%20get%20a%20list%20of%20all%20definition%20in%20a%20file/near/132130403):
Hi, is it possible in meta-programming to get a list of all (non-meta) definitions in a file?

#### [Simon Hudon (Aug 14 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28meta%29%20get%20a%20list%20of%20all%20definition%20in%20a%20file/near/132130541):
Yes. There are three parts to this: listing (or folding over) the visible definitions, determining that they are from the current file and determining whether they are definitions.

#### [Zesen Qian (Aug 14 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28meta%29%20get%20a%20list%20of%20all%20definition%20in%20a%20file/near/132130754):
I guess the hard part is the first then. I browsed thorough tactic.lean and didn't find anything interesting.

#### [Simon Hudon (Aug 14 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28meta%29%20get%20a%20list%20of%20all%20definition%20in%20a%20file/near/132130776):
In `init.meta.environment`, you can find `environment.fold`. It doesn't give you a list but it lets you iterate over all the definitions of a file and accumulate them. `get_env` gives you the current environment and `in_current_file'` tells you if a given name is defined / declared in the current file and finally, you can look at the `declaration` data structure and see the `trusted` bit for `definition` and `constant`.

#### [Zesen Qian (Aug 14 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28meta%29%20get%20a%20list%20of%20all%20definition%20in%20a%20file/near/132130792):
that is very helpful. Thanks!

#### [Simon Hudon (Aug 14 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28meta%29%20get%20a%20list%20of%20all%20definition%20in%20a%20file/near/132131037):
You're welcome!

