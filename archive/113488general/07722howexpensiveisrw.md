---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/07722howexpensiveisrw.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [how expensive is rw?](https://leanprover-community.github.io/archive/113488general/07722howexpensiveisrw.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (May 31 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20expensive%20is%20rw%3F/near/127334288):
<p>a profiler for a long proof I just typed:</p>
<div class="codehilite"><pre><span></span>elaboration: tactic execution took 6.66s
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
 4092ms    61.5%   interaction_monad.orelse&#39;
 4092ms    61.5%   _private.3132620493.rw_goal._lambda_2
 4069ms    61.1%   tactic.rewrite_target
 4009ms    60.2%   tactic.rewrite
 3972ms    59.7%   tactic.rewrite_core
 1494ms    22.4%   tactic.ac_refl
 1489ms    22.4%   cc_state.internalize
  524ms     7.9%   tactic.interactive.apply._lambda_1
</pre></div>

#### [ Kenny Lau (May 31 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20expensive%20is%20rw%3F/near/127334311):
<p>Highlight:</p>
<div class="codehilite"><pre><span></span> 3972ms    59.7%   tactic.rewrite_core
 1494ms    22.4%   tactic.ac_refl
</pre></div>

#### [ Mario Carneiro (May 31 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20expensive%20is%20rw%3F/near/127334696):
<p>what was the rewrite</p>

#### [ Kenny Lau (May 31 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20expensive%20is%20rw%3F/near/127334699):
<p>it was 100 rewrites</p>

#### [ Kenny Lau (May 31 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20expensive%20is%20rw%3F/near/127335262):
<p>another highlight:</p>

#### [ Kenny Lau (May 31 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20expensive%20is%20rw%3F/near/127335263):
<div class="codehilite"><pre><span></span> 6548ms    98.3%   tactic.solve1
 4617ms    69.3%   interaction_monad.monad._lambda_9
</pre></div>

#### [ Kenny Lau (May 31 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20expensive%20is%20rw%3F/near/127335266):
<p>what is so expensive about focussing on a goal?</p>

#### [ Kenny Lau (May 31 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20expensive%20is%20rw%3F/near/127335275):
<div class="codehilite"><pre><span></span> 1489ms    22.4%   cc_state.internalize
  524ms     7.9%   tactic.interactive.apply._lambda_1
</pre></div>

#### [ Kenny Lau (May 31 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20expensive%20is%20rw%3F/near/127341050):
<p>After some optimizations (heavily cutting down the workload of <code>rw</code>):</p>
<div class="codehilite"><pre><span></span>elaboration: tactic execution took 3.65s
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
 1581ms    43.3%   tactic.interactive.congr&#39;
 1581ms    43.3%   tactic.focus1
 1579ms    43.2%   tactic.interactive.congr&#39;._main._lambda_1
 1548ms    42.4%   tactic.all_goals
 1548ms    42.4%   _private.3864167971.all_goals_core._main._lambda_2
 1548ms    42.4%   all_goals_core
 1241ms    34.0%   tactic.interactive.propagate_tags
 1127ms    30.9%   tactic.apply_core
</pre></div>

#### [ Kenny Lau (May 31 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20expensive%20is%20rw%3F/near/127341051):
<p>I'm still surprised that <code>solve1</code> took the most time</p>

#### [ Kenny Lau (May 31 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20expensive%20is%20rw%3F/near/127341052):
<p>I thought <code>solve1</code> is the most inexpensive tactic</p>

#### [ Sebastian Ullrich (May 31 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20expensive%20is%20rw%3F/near/127348788):
<p>This doesn't have to mean that <code>solve1</code> is slow, more probably it means that you have multiple calls to it, and not all of them call <code>_lambda_9</code> next.</p>

#### [ Sebastian Ullrich (May 31 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20expensive%20is%20rw%3F/near/127348798):
<p>Basically, the profile trace isn't all that useful right now</p>

#### [ Gabriel Ebner (May 31 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20expensive%20is%20rw%3F/near/127349707):
<p>The reason for the comparatively large runtime of <code>solve1</code> is not that it is called often, but that it calls the tactic you give it as an argument.  That is, when you have <code>begin { my_tactic } end</code>, then <code>my_tactic</code> is executed by <code>solve1</code> and hence the cumulative runtime of <code>solve1</code> includes the runtime of <code>my_tactic</code>.</p>


{% endraw %}
