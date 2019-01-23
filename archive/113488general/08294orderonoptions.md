---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08294orderonoptions.html
---

## Stream: [general](index.html)
### Topic: [order on options](08294orderonoptions.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 23 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134463860):
Is there an instance of `decidable_linear_order` on `option` in Mathlib or core? I can't find one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 23 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464059):
maybe `with_bot` has an order

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 23 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464253):
Yes, it does, thanks! Now I'm stuck for a new reason: I don't have a decidable linear order for `name` (from the tactics). I think I'll need to write some of those orders myself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 23 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464258):
There is an order on `name`, but it is `meta` and not an instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 23 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464261):
does it need to be meta?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 23 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464262):
no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 23 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464263):
Actually, I only need a decidable relation, not an order

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 23 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464264):
it has that already

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 23 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464301):
```
meta instance : decidable_rel name.lt :=
λ a b, ordering.decidable_eq _ _

meta instance : has_lt name :=
⟨name.lt⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 23 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464305):
also relevant
```
/- Both cmp and lex_cmp are total orders, but lex_cmp implements a lexicographical order. -/
meta constant name.cmp : name → name → ordering
meta constant name.lex_cmp : name → name → ordering
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 23 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464306):
The issue is that the order relation and its decidability for `has_bot` are wrapped up in order instances

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 23 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464312):
I guess we could generalize the definitions to `has_le` from `has_le` and `has_lt` from `has_lt`, without committing to any order properties

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 23 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464353):
Exactly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 23 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464354):
An easy fix is
```
meta instance : decidable_linear_order name :=
by refine {lt := (<), le := \lam a b, \neg b < a, ..}; exact undefined
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 23 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464400):
That's evil

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 23 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464401):
how exactly is `undefined` defined?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 23 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464402):
`undefined := undefined`, effectively

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 23 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464404):
then how does VM know what to do with `#eval unchecked_cast`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 23 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464405):
it's not really, because this causes loops instead of an error

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 23 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464406):
@**Mario Carneiro** you may have a different opinion if you knew that this is for a mathlib PR

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 23 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464412):
`name` is basically meta. If a proof gets in your way, kill it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 23 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464413):
As long as it's actually true

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 23 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464453):
or close enough to true that it doesn't matter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 23 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464462):
We could write `name.lt` non-meta, but I would want to see what is the performance hit first

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 23 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464579):
```quote
or close enough to true that it doesn't matter
```

I'm hesitant to agree because I see the type class constraint as a way the type system tells you to make sure you're satisfying assumptions and warning you when you break those assumptions. You write `undefined` and you lose all that information. Or rather, the type system tells you "all the assumptions are satisfied, no worries" when it might not be the case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 23 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464780):
This is true, but `meta` code doesn't have these guarantees anyway, except in a vague sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 23 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464784):
A proof in `meta` land means something between "nothing at all" and "probably true"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 23 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464828):
As a comparison, that used to be my opinion of software testing until I started grading software assignment of students who often didn't bother testing. Yes, tested software is still imperfect but untested is so much worse

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 23 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464829):
right, which is why a meta proof can mean "probably true": the user had to make a conscious choice to either prove it or stub it out

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 23 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464878):
I liken it to the "preconditions" requirements in programs in Haskell or Java. It says "don't fail this requirement or else" and no compile or run time checking

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 23 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464905):
If you pass an order that is not linear to a function expecting one in the type, it's your fault if it breaks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 23 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464920):
I think comparing it the a quickcheck property would be closer to the truth, when you decide to write them, they nudge you in the right direction


{% endraw %}
