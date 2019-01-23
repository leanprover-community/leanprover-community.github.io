---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22256coolpaperonreification.html
---

## Stream: [general](index.html)
### Topic: [cool paper on reification](22256coolpaperonreification.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 03 2018 at 04:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486086):
just in case anybody else is interested in proofs by reflection: https://people.csail.mit.edu/jgross/personal-website/papers/2018-reification-by-parametricity-itp-draft.pdf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 03 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486131):
it's my favorite topic right now since i'm trying to teach myself how to write reflective tactics in lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 03 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486177):
i wish i was in oxford so i could attend the workshops at ITP :|

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 03 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486552):
does lean have a `vm_compute` equivalent?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486600):
No. @**Jeremy Avigad** This paper relates to our discussion about proof by `#eval`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486602):
I had a conversation with @**Mario Carneiro** a while back on proofs by reflection. He was pointing out to me that they are not as beneficial in Lean as they are in Coq because of some details of computation in the kernel

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486604):
I don't remember which detail that was

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486617):
It's possible to do proof by reflection using the *kernel* for computation, but it's not very fast

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486658):
doing proof by reflection using the VM is not supported (directly)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486661):
but you can use tactics, computing in the VM, to craft appropriate theorems as certificates for the kernel

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 03 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486668):
is there an example of that in lean? I think the idea of verified decision procedures is very appealing theoretically

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486669):
`norm_num` and `ring` use this latter strategy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486708):
`cooper` uses kernel reflection, and `vm_cooper` uses "tactic reflection"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 03 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486709):
and in lean 4, i think we will be able to extract tactics and use them?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486711):
sure, that's one thing compilation should allow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 03 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486712):
not tactics, i mean regular function defs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 03 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486718):
so we could extract the `check_is_even` program as described in the paper and have it run in C++

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486719):
You can `#eval check_is_even` currently

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486756):
to run in the VM

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486764):
or you can `#reduce check_is_even` to run in the kernel

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 03 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127487123):
but, in a sense, we can't reason about vm evaluation, it's outside lean, is my current understanding

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 03 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127487175):
if there was a `#eval that produced exprs` we could though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127487290):
no but we can trust the results

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127487328):
like if we evaluate a `bool` expr and get `tt` we believe the same should hold true of reduce

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127487339):
The reasoning would go into the definition of the function being evaluated itself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 03 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127487721):
reasoning would go into the definition? do you have a concrete example? I don't quite follow. As I understand it the kernel is quite strict. If we use nat, it will reduce everything strictly using the zero / succ nat representation. However, vm evaluation might use a bignum library for speed. How can we say their behavior is equivalent?
(maybe I should just be reading more about reflection / I don't understand how Lean uses GMP)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127487986):
The assumption, the trust, goes into assuming that the VM respects the lean model. You verify the lean model

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 03 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127488045):
ah, gotcha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127488054):
But that's not much different from assuming the kernel is correctly implemented in C++. You expand your trust level a bit and get fast evaluation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 03 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127488200):
it's interesting to me that reflection is slow because generating the reified syntax and reducing the output of the interpretation function are such huge constant overheads. I would've guessed that the manipulations you might do on the AST you create would've been a bigger deal in practice for most problems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 03 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127495213):
well, you weren't kidding about kernel computation
```lean
inductive is_even : ℕ → Prop
| zero : is_even 0
| ssuc : ∀ n, is_even n → is_even (nat.succ (nat.succ n))

meta def prove_even : tactic unit := `[repeat {constructor}]

example : is_even 2000 := by do timetac "" prove_even

def check_is_even : ℕ → bool
| nat.zero := tt
| (nat.succ nat.zero) := ff
| (nat.succ (nat.succ n')) := check_is_even n'

local attribute [elab_as_eliminator] nat.case_strong_induction_on
theorem cie_sound : ∀ n, check_is_even n = tt → is_even n :=
λ n, nat.case_strong_induction_on n
  (λ h, is_even.zero)
  (λ n', nat.rec_on n' 
    (λ h₁ h₂, have h₃ : check_is_even 1 = ff, from rfl, by contradiction) 
    (λ m h₁ h₂ h₃, is_even.ssuc _ ((h₂ m) (nat.le_succ m) h₃)))

example : is_even 2000 := by do timetac "" `[exact cie_sound 2000 rfl]
```


{% endraw %}
