---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/93453nonexhaustiveformeta.html
---

## Stream: [general](index.html)
### Topic: [non-exhaustive for meta](93453nonexhaustiveformeta.html)

---


{% raw %}
#### [ Zesen Qian (Jul 09 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129371844):
If we allow non-termination at meta level, shouldn't we also allow non-exhaustive match?

#### [ Simon Hudon (Jul 09 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129372015):
There are a lot of possibilities. While mandatory termination is very restrictive, exhaustiveness is not and it has great benefits. It allows Lean to tell you when you're messing up

#### [ Simon Hudon (Jul 09 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129372069):
Whenever you would leave some cases out, it is a good practice to write an error message instead

#### [ Simon Hudon (Jul 09 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129372151):
You're making clear to any reader that you don't accept every input

#### [ Zesen Qian (Jul 09 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129373623):
@**Simon Hudon** by error message you mean type level error? or is there some backdoor at meta-level that I can just halt the program in case of non-exhaustion?

#### [ Zesen Qian (Jul 09 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129373691):
because I'm pretty sure the rest case is not going to happen(and if it happens, that means problem in my meta-code).

#### [ Simon Hudon (Jul 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129373788):
If you're in `tactic`, you can use `fail my_error_message` to report the error ... it might actually a good enough reason to write code in `tactic`

#### [ Simon Hudon (Jul 09 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129373814):
But that's not a backdoor, you can write trusted code in a similar way (but with different monads than `tactic` because `tactic` is `meta`)

#### [ Zesen Qian (Jul 09 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129373829):
hmm, what about a meta-program that simply returns a proof? 
```
prog : hint -> pexpr
```

#### [ Zesen Qian (Jul 09 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129373904):
because the generation of the proof doesn't depends on inspection of the prover's environment, but only on the hint.

#### [ Simon Hudon (Jul 09 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129373988):
You can return a default value like ``` ``(Type) ```

#### [ Gabriel Ebner (Jul 09 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129374000):
There is also `undefined_core "my error message"`

#### [ Zesen Qian (Jul 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129374011):
@**Gabriel Ebner** I think that's what I wanted.


{% endraw %}
