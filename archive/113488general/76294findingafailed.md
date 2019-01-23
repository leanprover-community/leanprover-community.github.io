---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/76294findingafailed.html
---

## Stream: [general](index.html)
### Topic: [finding a failed](76294findingafailed.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 10 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finding%20a%20failed/near/133643406):
What's the easiest way to find where a "failed" was generated? I've been resorting to inserting trace statements in multiple files and now its just getting out of hand

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 10 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finding%20a%20failed/near/133643997):
also, in the tactic monad, is there a way to get a stacktrace?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 10 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finding%20a%20failed/near/133644045):
There is the `vm` monad, which purports to be a debugger, but I don't know anyone who knows how to use it except possibly @**Sebastian Ullrich**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 10 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finding%20a%20failed/near/133671919):
What I usually do is that, if I have a function with three lines I add the following until I find the error:

```lean
meta def my_fn : tactic unit :=
do stmt1 <|> fail "line A",
   stmt2 <|> fail "line B",
   stmt3 <|> fail "line C"
```

When I have found the function that fails, I repeat in that function.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Sep 10 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finding%20a%20failed/near/133673961):
I've never used `vm` :sweat_smile: . I suppose it should be possible to write a `vm_monitor` that prints the stack trace whenever `failed` is called.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 10 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finding%20a%20failed/near/133674025):
who wrote it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 10 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finding%20a%20failed/near/133683100):
I had never used `vm_monitor and I gave it a try. Here's what I did:

```lean
set_option debugger true

@[vm_monitor]
meta def my_mon : vm_monitor unit := 
{ init := (),
  step := λ _, 
  do vm.curr_fn >>= vm.trace }

run_cmd my_tactic

set_option debugger false
```

It sets up a monitor that, before each instruction, prints the name of the enclosing function. It does not seem to be aware of failures but at least, you can figure out where the problem is by looking at the last printout

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 10 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finding%20a%20failed/near/133684138):
If you use the following instead, you can get an overview of the call nesting structure:

```lean
@[vm_monitor]
meta def my_mon : vm_monitor (nat × option name) := 
{ init := (0, none),
  step := λ fn, 
  do fn' ← vm.curr_fn, 
     n' ← vm.call_stack_size,
     when (fn ≠ (n',some fn')) $ vm.trace $ (string.join $ list.repeat "| " n') ++ to_string fn',
     pure (n',fn') }
```


{% endraw %}
