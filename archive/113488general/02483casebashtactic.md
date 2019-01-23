---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02483casebashtactic.html
---

## Stream: [general](index.html)
### Topic: [case bash tactic](02483casebashtactic.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 19 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/case%20bash%20tactic/near/136128666):
@**Scott Morrison|110087** I incorrectly assumed that your `case_bash` tactic was related to the `fin`-bashing tactic. Nevertheless I wonder if there is place for a mechanism as follows:
* `case_bash` goes into `tactics/`
* `tidy` takes an optional list of tactics to apply (besides the `local [attribute]` thing that we use nowadays)
* So we can prove thing with `tidy [case_bash]` or something like that.

Does that make sense?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 19 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/case%20bash%20tactic/near/136139714):
I think you can already override the list of tactics: `tidy { tactics := tactic.tidy.default_tactics ++ [foo] }`, although `foo` has to be a `tactic string` for this to work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 19 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/case%20bash%20tactic/near/136139744):
Certainly that can be given nicer syntax, and use some reflection to allow passing more complicated things than just a `tactic string`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 19 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/case%20bash%20tactic/near/136139757):
(e.g. a `tactic A` for any A, a function with arguments that have default values, etc.)

