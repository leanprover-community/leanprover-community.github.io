---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01261CoqsAbortinLean.html
---

## Stream: [general](index.html)
### Topic: [Coq's Abort in Lean](01261CoqsAbortinLean.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Sullivan (Oct 08 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135406580):
What is Lean's equivalent of Abort in Coq?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135406598):
what does it do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Sullivan (Oct 08 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135406720):
@**Mario Carneiro** Abort terminates (gives up on) a failing or incomplete proof (whereas Coq's "Admitted" gives up and accepts the proposition being proved as an axiom, like sorry in Lean).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135406812):
Lean doesn't have this. I guess it makes more sense with the line-based input approach to coq

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135406836):
but in lean once you have written `def` you are committed to either finishing it or getting an error or warning

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Sullivan (Oct 08 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135407728):
For pedagogical purposes in any case it'd be good to have, as one can then exhibit proof strategies that don't work out. Students can see how the tactic state evolves until one gets stuck and gives up.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135407747):
Usually we use `sorry` for that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Sullivan (Oct 08 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135418308):
Yes but sorry accepts the proposition axiomatically, which in general is not what one wants to do. E.g., when showing why P \or \not P isn't provable without em.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 08 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135418336):
You can use `run_cmd`: it allows you to run tactics and failing to prove the goal has no consequences

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Oct 08 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135418499):
`example` may be more appropriate in that case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 08 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135418627):
`example` has the down side that, if you use `sorry`, it still produces warnings.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135418882):
There is always the trick used in the tests: use `sorry` in a `have` subproof that doesn't get used

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Sullivan (Oct 09 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135478380):
```quote
There is always the trick used in the tests: use `sorry` in a `have` subproof that doesn't get used
```
There are work-arounds, albeit with some compromises, but wouldn't it be cleaner to just provide an "abort" tactic. The context for this suggestion is not expert use of Lean but rather early undergraduate education, where every inelegant complexity causes additional pain and suffering amongst students.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Oct 09 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479771):
Note that `Abort` is not a tactic but a built-in command in Coq. We would need to change the `begin...end` syntax and parts of the elaborator for something similar.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 09 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479775):
From what (little) I know about Coq, `Abort` isn't a tactic, it's a top-level command. I don't think there's a way to implement it as a tactic in Lean 3, at least not in a way that mimics the usage of the Coq command. This seems like the kind of thing you might be able to do in Lean 4.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Oct 09 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479780):
Nice timing :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 09 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479782):
Haha, good timing!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Oct 09 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479784):
:D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 09 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479789):
Amazing duo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 09 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479859):
To keep repeating Sebastian, I agree that using `example` is the Lean-style way to do this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 09 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479876):
To show a failing proof attempt, start an example and don't finish it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 09 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479889):
No, the Lean way is to finish the proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 09 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479907):
There's no problem leaving an attempt unfinished like there is in Coq, it doesn't stop the processing of future declarations.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 09 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479921):
Even if `==` suddenly appear in the proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 09 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135494007):
What if we treated `abort` like `sorry` except that, when it appears in an example, it doesn't produce warnings?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Sullivan (Oct 10 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135516025):
```quote
What if we treated `abort` like `sorry` except that, when it appears in an example, it doesn't produce warnings?
```
It would need both (1) to not produce warnings, and (2) to not accept the goal axiomatically.

And, yes,  to Rob L. Abort is a command, not a tactic, in Coq.

By the way, Coq's command, analogous to Lean's sorry, is Admitted. It gives up on the current proof and accepts the goal axiomatically. By contrast, Abort gives up on the current proof but discards rather than accepts the current goal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 10 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135516089):
I think examples can't be invoked from other proofs so that part is already there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 10 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135528161):
I've only used Coq for  simple things. Specifically, I don't know how `Abort` works in nested proofs like they describe in the manual. Here's something that very roughly approximates its behavior in the top-level case. If you use `example`, the environment will be the same before and after processing this, and there are no warnings. 
```lean
constant {u} abort {α : Sort u} : α

open tactic 
meta def tactic.interactive.abort : tactic unit :=
all_goals `[exact abort]

example : 0 < 0 ∧ 0 > 0 := 
begin 
  split,
  abort
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 10 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135528193):
But I still think the Lean-style way to do this is to just leave the example unfinished.


{% endraw %}
