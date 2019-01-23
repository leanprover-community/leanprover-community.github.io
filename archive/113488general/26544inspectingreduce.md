---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26544inspectingreduce.html
---

## Stream: [general](index.html)
### Topic: [inspecting #reduce](26544inspectingreduce.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Jun 07 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127709156):
Is there a `set_option` of sorts to see what steps `#reduce` is going through to debug a *(deterministic) timeout*?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 07 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127712838):
I have no idea, but I did this:

```
$ cd lean/tests; git grep set_option
```

Looking around, I found these possible options:

```
set_option profiler true
set_option trace.elaborator_detail true
set_option trace.compiler.code_gen true
```

Perhaps one of those will help, or perhaps looking at `lean/tests` will.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Jun 08 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127760106):
Thank you Sean. It seems that `profiler` and `compiler.*` pertain to `#eval` only. There's a little bit of information from `elaborator.*` in this regard, but it somewhat unsurprisingly doesn't provide much beyond how parsing transpired and how it typed the AST *before* sending it for reduction. Going through `lean/tests` doesn't yield much either. There's a secret `import tools.debugger` but even there are no options to look into reduce. I'll just go through the implementation, can't be that bad :P.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 08 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127760302):
Good luck!

```cpp
library/init/meta/tactic.lean:1204:    memory allocations (in thousands) performed by 'tac'. This is a deterministic way of interrupting
library/init/util.lean:34:  This is a deterministic way of interrupting long running tasks. -/
src/shell/lean.cpp:200:    std::cout << "                     this is a deterministic way of interrupting long running tasks\n";
src/util/exception.cpp:29:    return "(deterministic) timeout";
src/util/json.hpp:7760:        deterministic finite automaton (DFA) by the tool
src/util/sexpr/options.cpp:29:    register_unsigned_option(*g_timeout, 0, "the (deterministic) timeout is measured as the maximum of memory allocations (in thousands) per task, the default is unbounded");
tests/lean/induction_generalize_premise_args.lean:8:  lemma deterministic_aux (c σ c'₁ c'₂ σ'₁ σ'₂) (h₁ : smallstep ⟨c, σ⟩ ⟨c'₁, σ'₁⟩)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Jun 08 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127760487):
It is somewhat mysterious to me why `#eval` works just fine and `#reduce` gets stuck, even though I've been told that `#reduce` can get stuck on axioms such as `propext` - however everything I have should be perfectly computable as witnessed by `#eval`. Getting `#reduce` to work should mean that I can also use defeq to compute `rfl` proofs for me, which is the ultimate goal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jun 08 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127761349):
Just to confirm: there are no tools to trace the computation of `#reduce` (at least that I know of).  Your best bet is to probably to run lean in a debugger and set a breakpoint on `normalize_fn::normalize` (or add a `tout() << e << "\n"` there).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jun 08 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127761361):
> however everything I have should be perfectly computable as witnessed by #eval

That's the point.  `#eval` (VM computation) can evaluate more things than `#reduce` (definitional reduction).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Jun 08 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127762471):
How does that conceptually make sense in pure settings? Does it have something to do with non-transitive defeq? Isn't pure computation technically just definitional reduction?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jun 08 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127762817):
Can you clarify the term "pure setting"?  The main area where definitional reduction can get stuck where VM computation succeeds is on terms with axioms---VM computation erases all Props and proofs, and hence does not care whether you use axioms or not.  Practically speaking, there is also a big performance difference.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Jun 08 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127764272):
I just wanted to avoid having to think about side-effects that can possibly influence computation as it is being executed, that's why I said "pure setting". However, VM computation erasing Props/proofs is interesting in my scenario - I think I know where it's getting stuck. I have a structure that has both `x` and a proof of `P x` - what I end up asking for is the `x` only. The interesting part is that if proof of `P x` is sorry, it reduces just fine - but I think that also makes sense.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Jun 08 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127764406):
I'll fix it by using less dependent typing, thank you so much, I think I've got this :).


{% endraw %}
