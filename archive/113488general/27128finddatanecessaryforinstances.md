---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27128finddatanecessaryforinstances.html
---

## [general](index.html)
### [find data necessary for instances](27128finddatanecessaryforinstances.html)

#### [Joey van Langen (Jan 09 2019 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find data necessary for instances/near/154708830):
Is there an easy way to find which fields should be provided when defining an instance?
For example making an instance of a ring requires you to fill in a lot of data from different classes and manually going through each class in the hierarchy and finding the names of the respective data is quite some work

#### [Rob Lewis (Jan 09 2019 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find data necessary for instances/near/154708917):
One method is a hole command, as seen briefly in Mario's coding session yesterday:
```lean
variable α : Type
example : ring α :=
{! !}
```
In VSCode, click on the lightbulb and choose "generate a skeleton for the structure."

#### [Rob Lewis (Jan 09 2019 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find data necessary for instances/near/154708931):
(You'll need the right import, probably mathlib's `tactic.interactive`, I don't remember.)

#### [Kevin Buzzard (Jan 09 2019 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find data necessary for instances/near/154708988):
If I type

```lean
example (R : Type) : ring R :=
{
  
}
```

then (in VS Code) in the "problems" window (which I sometimes need to create by "pulling up" near the bottom of VS Code) then I see 15 problems, one for each field I need to create. Does this help?

#### [Rob Lewis (Jan 09 2019 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find data necessary for instances/near/154708993):
Alternatively, you can just write an empty structure {} and look at the error messages. (What Kevin said.)

#### [Kevin Buzzard (Jan 09 2019 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find data necessary for instances/near/154709008):
Within the `{ }` Lean is expecting me to write `add := blah` etc, and I get a problem for each missing field.

#### [Kevin Buzzard (Jan 09 2019 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find data necessary for instances/near/154709107):
Rob's import is correct -- I just tried it.

#### [Joey van Langen (Jan 09 2019 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find data necessary for instances/near/154709132):
Thanks! Is there also a generate skeleton for emacs?

#### [Reid Barton (Jan 09 2019 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find data necessary for instances/near/154709175):
Yes, move the cursor inside the `{! !}` and press C-c SPC

#### [Joey van Langen (Jan 09 2019 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find data necessary for instances/near/154709342):
Not having much succes with the C-c SPC. What should I enter when asked for a hole command?

#### [Reid Barton (Jan 09 2019 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find data necessary for instances/near/154709443):
If you press tab, one of the options should be "Instance Stub — Generate a skeleton for the structure under construction."

#### [Reid Barton (Jan 09 2019 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find data necessary for instances/near/154709450):
It requires importing the mathlib module that Rob mentioned

