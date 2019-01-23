---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79339profiling.html
---

## Stream: [general](index.html)
### Topic: [profiling](79339profiling.html)

---


{% raw %}
#### [ Simon Hudon (Mar 25 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124196289):
Am I correct to believe that `lean --make` and `lean --profile` are not meant to be used together? 

When I use them together, I get this error:

```
libc++abi.dylib: terminating with uncaught exception of type std::length_error: vector
```

Do people use `--profile` one file at a time?

#### [ Sebastian Ullrich (Mar 25 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124200802):
I constantly use both flags together. The error message sure sounds bad.

#### [ Simon Hudon (Mar 25 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124200863):
I'm on Mac. What about you?

#### [ Sebastian Ullrich (Mar 25 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124200866):
Linux. I was about to ask.

#### [ Simon Hudon (Mar 25 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124200916):
I'm wondering if the C++ runtime on Mac allocates less memory than on Linux. Does that sound sensible?

#### [ Simon Hudon (Mar 25 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124200957):
(now I'm getting around that limitation with a Makefile)

#### [ Simon Hudon (Mar 25 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124200959):
(... which profiles one file at a time)

#### [ Sebastian Ullrich (Mar 25 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124200966):
You can also use `--profile --recursive`

#### [ Simon Hudon (Mar 25 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124201067):
What's the difference with `--make`?

#### [ Sebastian Ullrich (Mar 25 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124201114):
It doesn't actually save .olean files, but I'll assume that's not that part you want to profile :)

#### [ Simon Hudon (Mar 25 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124201118):
I believe you're right :)

#### [ Simon Hudon (Mar 25 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124201121):
The bad news is that I get the same error

#### [ Sebastian Ullrich (Mar 25 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124201331):
Well that's not good

#### [ Moses Schönfinkel (Mar 26 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124201382):
About as good as the broken link to Nightly Lean Windows build :P.

#### [ Simon Hudon (Mar 29 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124348839):
I've been using `lean --profile` on Mac and Linux and they seem to produce different information. On Mac, I get information like:

```
elaboration: tactic compilation took 8.2ms
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
```

while on Linux, I do not. Otherwise, the information looks the same

#### [ Simon Hudon (Mar 29 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124348841):
Is that normal?

#### [ Sebastian Ullrich (Mar 29 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124361454):
@**Simon Hudon** No, it should work on Linux as well

#### [ Sebastian Ullrich (Mar 29 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124361455):
Btw, you can use `-D profiler.threshold=0.5` to suppress output < 0.5s for example

#### [ Simon Hudon (Mar 29 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124363084):
thanks! Thanks should be useful! I'll try that. Any list of those fun constants?

#### [ Sebastian Ullrich (Mar 29 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124363129):
Same constants as after `set_option`

#### [ Simon Hudon (Mar 29 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124363483):
thanks! What does `profiler.freq` do?

#### [ Sebastian Ullrich (Mar 29 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/profiling/near/124363782):
The tactic execution profile as above is computed by sampling the top-most stack frame at that frequency


{% endraw %}
