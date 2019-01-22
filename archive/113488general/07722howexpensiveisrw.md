---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/07722howexpensiveisrw.html
---

## [general](index.html)
### [how expensive is rw?](07722howexpensiveisrw.html)

#### [Kenny Lau (May 31 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how expensive is rw?/near/127334288):
a profiler for a long proof I just typed:
```
elaboration: tactic execution took 6.66s
num. allocated objects:  20027
num. allocated closures: 20050
 6658ms   100.0%   tactic.istep._lambda_1
 6658ms   100.0%   _interaction._lambda_2
 6658ms   100.0%   tactic.istep
 6658ms   100.0%   tactic.step
 6658ms   100.0%   scope_trace
 6548ms    98.3%   tactic.solve1
 4617ms    69.3%   interaction_monad.monad._lambda_9
 4612ms    69.3%   tactic.interactive.propagate_tags
 4131ms    62.0%   rw_core
 4093ms    61.5%   _private.3132620493.rw_goal._lambda_4
 4093ms    61.5%   interactive.loc.apply
 4092ms    61.5%   interaction_monad.orelse'
 4092ms    61.5%   _private.3132620493.rw_goal._lambda_2
 4069ms    61.1%   tactic.rewrite_target
 4009ms    60.2%   tactic.rewrite
 3972ms    59.7%   tactic.rewrite_core
 1494ms    22.4%   tactic.ac_refl
 1489ms    22.4%   cc_state.internalize
  524ms     7.9%   tactic.interactive.apply._lambda_1

#### [Kenny Lau (May 31 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how expensive is rw?/near/127334311):
Highlight:
```
 3972ms    59.7%   tactic.rewrite_core
 1494ms    22.4%   tactic.ac_refl

#### [Mario Carneiro (May 31 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how expensive is rw?/near/127334696):
what was the rewrite

#### [Kenny Lau (May 31 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how expensive is rw?/near/127334699):
it was 100 rewrites

#### [Kenny Lau (May 31 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how expensive is rw?/near/127335262):
another highlight:

#### [Kenny Lau (May 31 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how expensive is rw?/near/127335263):
```
 6548ms    98.3%   tactic.solve1
 4617ms    69.3%   interaction_monad.monad._lambda_9

#### [Kenny Lau (May 31 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how expensive is rw?/near/127335266):
what is so expensive about focussing on a goal?

#### [Kenny Lau (May 31 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how expensive is rw?/near/127335275):
```
 1489ms    22.4%   cc_state.internalize
  524ms     7.9%   tactic.interactive.apply._lambda_1

#### [Kenny Lau (May 31 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how expensive is rw?/near/127341050):
After some optimizations (heavily cutting down the workload of `rw`):
```
elaboration: tactic execution took 3.65s
num. allocated objects:  9569
num. allocated closures: 7495
 3653ms   100.0%   tactic.istep
 3653ms   100.0%   scope_trace
 3653ms   100.0%   tactic.step
 3653ms   100.0%   _interaction._lambda_2
 3653ms   100.0%   tactic.istep._lambda_1
 3554ms    97.3%   tactic.solve1
 2271ms    62.2%   interaction_monad.monad._lambda_9
 1792ms    49.1%   interaction_monad_orelse
 1584ms    43.4%   tactic.interactive.convert
 1581ms    43.3%   tactic.interactive.congr'
 1581ms    43.3%   tactic.focus1
 1579ms    43.2%   tactic.interactive.congr'._main._lambda_1
 1548ms    42.4%   tactic.all_goals
 1548ms    42.4%   _private.3864167971.all_goals_core._main._lambda_2
 1548ms    42.4%   all_goals_core
 1241ms    34.0%   tactic.interactive.propagate_tags
 1127ms    30.9%   tactic.apply_core

#### [Kenny Lau (May 31 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how expensive is rw?/near/127341051):
I'm still surprised that `solve1` took the most time

#### [Kenny Lau (May 31 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how expensive is rw?/near/127341052):
I thought `solve1` is the most inexpensive tactic

#### [Sebastian Ullrich (May 31 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how expensive is rw?/near/127348788):
This doesn't have to mean that `solve1` is slow, more probably it means that you have multiple calls to it, and not all of them call `_lambda_9` next.

#### [Sebastian Ullrich (May 31 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how expensive is rw?/near/127348798):
Basically, the profile trace isn't all that useful right now

#### [Gabriel Ebner (May 31 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how expensive is rw?/near/127349707):
The reason for the comparatively large runtime of `solve1` is not that it is called often, but that it calls the tactic you give it as an argument.  That is, when you have `begin { my_tactic } end`, then `my_tactic` is executed by `solve1` and hence the cumulative runtime of `solve1` includes the runtime of `my_tactic`.

