---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/47494deletingvariables.html
---

## Stream: [general](index.html)
### Topic: [deleting variables](47494deletingvariables.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485299):
Is it possible to delete something that has been declared using `variables`? (I want to "upgrade" an instance variable to a class which extends the original one.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 03 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485300):
no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485309):
Can you show me concretely what you're going for?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485402):
My actual example involves my own classes, but something like
```lean
section
variables {α : Type} [monoid α]

/- other definitions that don't require the group structure... -/

variables [group α]

def g : α → α := λ x, x * x⁻¹
example (x : α) : g x = (1 : α) := by simp [g]
   
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485439):
I can just put the earlier definitions in their own section which has the `monoid` variable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485452):
but I was hoping for something more convenient

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485457):
Ah I see! Your best bet I think is to end your section and start it just before the `group` variable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485460):
What is the inconvenient in doing that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485469):
Not really very inconvenient, just a few extra lines of `section`/`end`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485519):
One downside I can see is if you have other variables declared in the first section that you want to keep in the rest of the section

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485562):
In that case, I would do this:

```
section
variables {α : Type} 
section
variables [monoid α]

/- other definitions that don't require the group structure... -/
end
variables [group α]
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485613):
Actually, if you don't do anything, what error do you get?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485719):
There I got an error which arose because `*` was using the monoid instance and `\-1` was using the group instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485732):
Ah, ok, I thought maybe it would go through the group by default

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485734):
well it's still a problem to have redundant typeclasses on a def

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485815):
Why?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485832):
in the theorem itself, it's a problem since they aren't the same structure, in uses it's a nuisance to have a redundant assumption

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485882):
Right in theorems I know the issues. With defs, I can't see it will be a nuisance down the line but not how that definition would be invalid

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127486403):
It won't be invalid. Often things like duplicate typeclass hypotheses will go unnoticed for a long time because they aren't really visibly different

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127486404):
unless you use `@thm` and notice two underscores in place of one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127486500):
It would be nice to have warnings for that kind of stuff. Actually, more warnings in general would be nice


{% endraw %}
