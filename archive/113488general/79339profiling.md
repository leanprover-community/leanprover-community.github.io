---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79339profiling.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [profiling](https://leanprover-community.github.io/archive/113488general/79339profiling.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Simon Hudon (Mar 25 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124196289):
<p>Am I correct to believe that <code>lean --make</code> and <code>lean --profile</code> are not meant to be used together? </p>
<p>When I use them together, I get this error:</p>
<div class="codehilite"><pre><span></span>libc++abi.dylib: terminating with uncaught exception of type std::length_error: vector
</pre></div>


<p>Do people use <code>--profile</code> one file at a time?</p>

#### [ Sebastian Ullrich (Mar 25 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124200802):
<p>I constantly use both flags together. The error message sure sounds bad.</p>

#### [ Simon Hudon (Mar 25 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124200863):
<p>I'm on Mac. What about you?</p>

#### [ Sebastian Ullrich (Mar 25 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124200866):
<p>Linux. I was about to ask.</p>

#### [ Simon Hudon (Mar 25 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124200916):
<p>I'm wondering if the C++ runtime on Mac allocates less memory than on Linux. Does that sound sensible?</p>

#### [ Simon Hudon (Mar 25 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124200957):
<p>(now I'm getting around that limitation with a Makefile)</p>

#### [ Simon Hudon (Mar 25 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124200959):
<p>(... which profiles one file at a time)</p>

#### [ Sebastian Ullrich (Mar 25 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124200966):
<p>You can also use <code>--profile --recursive</code></p>

#### [ Simon Hudon (Mar 25 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124201067):
<p>What's the difference with <code>--make</code>?</p>

#### [ Sebastian Ullrich (Mar 25 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124201114):
<p>It doesn't actually save .olean files, but I'll assume that's not that part you want to profile :)</p>

#### [ Simon Hudon (Mar 25 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124201118):
<p>I believe you're right :)</p>

#### [ Simon Hudon (Mar 25 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124201121):
<p>The bad news is that I get the same error</p>

#### [ Sebastian Ullrich (Mar 25 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124201331):
<p>Well that's not good</p>

#### [ Moses Schönfinkel (Mar 26 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124201382):
<p>About as good as the broken link to Nightly Lean Windows build :P.</p>

#### [ Simon Hudon (Mar 29 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124348839):
<p>I've been using <code>lean --profile</code> on Mac and Linux and they seem to produce different information. On Mac, I get information like:</p>
<div class="codehilite"><pre><span></span>elaboration: tactic compilation took 8.2ms
elaboration: tactic execution took 221ms
num. allocated objects:  1407
num. allocated closures: 366
  221ms   100.0%   _interaction._lambda_2
  221ms   100.0%   scope_trace
  221ms   100.0%   tactic.istep._lambda_1
  221ms   100.0%   tactic.solve1
  221ms   100.0%   tactic.step
  221ms   100.0%   tactic.istep
  220ms    99.5%   tactic.interactive.simp_core
  220ms    99.5%   tactic.interactive.propagate_tags
  218ms    98.6%   tactic.mk_simp_set_core
  218ms    98.6%   tactic.mk_simp_set
  217ms    98.2%   tactic.get_user_simp_lemmas
  217ms    98.2%   get_attribute_cache_dyn._lambda_1
  217ms    98.2%   user_attribute.get_cache
  217ms    98.2%   simp_attr.tl_simp._lambda_3
  217ms    98.2%   tactic.to_simp_lemmas
  217ms    98.2%   tactic.join_user_simp_lemmas_core
  217ms    98.2%   tactic.join_user_simp_lemmas
  215ms    97.3%   simp_lemmas.add_simp
  202ms    91.4%   interaction_monad.monad._lambda_9
  201ms    91.0%   simp_attr.tl_simp._lambda_2
</pre></div>


<p>while on Linux, I do not. Otherwise, the information looks the same</p>

#### [ Simon Hudon (Mar 29 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124348841):
<p>Is that normal?</p>

#### [ Sebastian Ullrich (Mar 29 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124361454):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> No, it should work on Linux as well</p>

#### [ Sebastian Ullrich (Mar 29 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124361455):
<p>Btw, you can use <code>-D profiler.threshold=0.5</code> to suppress output &lt; 0.5s for example</p>

#### [ Simon Hudon (Mar 29 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124363084):
<p>thanks! Thanks should be useful! I'll try that. Any list of those fun constants?</p>

#### [ Sebastian Ullrich (Mar 29 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124363129):
<p>Same constants as after <code>set_option</code></p>

#### [ Simon Hudon (Mar 29 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124363483):
<p>thanks! What does <code>profiler.freq</code> do?</p>

#### [ Sebastian Ullrich (Mar 29 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124363782):
<p>The tactic execution profile as above is computed by sampling the top-most stack frame at that frequency</p>


{% endraw %}
