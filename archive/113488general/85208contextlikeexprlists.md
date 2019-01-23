---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85208contextlikeexprlists.html
---

## Stream: [general](index.html)
### Topic: [context like expr lists?](85208contextlikeexprlists.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Mar 13 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654389):
How do I construct a list of expressions where later entries can depend on earlier ones? Like `(A : Sort u) (a : A)` as a minimal example... Do I have to use local constants?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 13 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654415):
when you say list of expressions, are you working in `meta` land?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Mar 13 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654423):
Yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 13 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654424):
it's just `list expr`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 13 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654473):
all that binding stuff is handled by you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Mar 13 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654481):
Yes, but how is the above example represented for example?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 13 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654502):
the first expr is ```(Sort u)``, the second is either `` `(A)`` or `#0` depending on whether `A` is in context

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Mar 13 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654671):
Well at the time I define the list, `A` is clearly not in context, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 13 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654676):
Maybe; perhaps you are planning for when it is. What's your use case?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Mar 13 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654723):
Just experimenting with the `add_inductive` API a bit... which is where it should be used as list of parameters or such

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Mar 13 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654735):
And `meta example : list expr := [\`(Sort 1), \`(A)]` immediately gives me "unknown identifier A"..

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Mar 13 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654737):
*sigh* How do I escape backticks here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 13 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654777):
`add_inductive` doesn't take a list of parameters, it takes `ty : expr` that specifies the whole type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 13 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654787):
Since it's a single expression, all the binding is done via `expr.pi`, and dependencies are done with `var` (de bruijn variables)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 13 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654810):
That is, `ty` should be a closed term

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 13 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654857):
escape backticks with more backticks ``` `` `escaped` `` ```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Mar 13 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654861):
But it takes a list of constructtors, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 13 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654865):
The constructor types are also closed terms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 13 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654868):
they repeat all the parameters, with the same types

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Mar 13 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654914):
Hm, I'd still like to have a data structure like that...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 13 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654915):
(this is done because constructors may change the binding type, like making things implicit)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 13 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654921):
Usually, we work in a context, and then it's a `list expr`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 13 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654928):
the whole tactic state is built around that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 13 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654931):
that's where local constants come in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Mar 13 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654988):
`expr` could use a bit more documentation somehow, it's really hard to figure out what local constants are

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 13 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123655582):
@**Jakob von Raumer** Write what you know and PR it to mathlib/docs/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 13 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123655583):
and then ask about what you don't know

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 13 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123655594):
we're trying to make some community-based docs in there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 13 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123655599):
informal and hopefully useful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Mar 13 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123655600):
I'll try :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 13 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123655643):
The rule I usually go for is "if it's not in the reference manual, and it's either not in TPIL/Programming In Lean or it's hard to find, then stick it in mathlib/docs"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Mar 13 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123655655):
I think it *should* be in PIL but it's noted as a TODO there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 13 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123655712):
Then I would urge you to create a short text file called expr.md and simply write some background and then what you're stuck on and PR it to that docs dir. You can assume people have read PIL.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Mar 14 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123705964):
What is the purpose of the second `name` argument to `expr.local_const`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Mar 14 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123706023):
Ah, got it, pretty printer name...


{% endraw %}
