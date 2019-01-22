---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85476updatingthenthelementofalist.html
---

## [general](index.html)
### [updating the nth element of a list](85476updatingthenthelementofalist.html)

#### [Scott Morrison (Nov 30 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148832961):
Do we have something equivalent to
```
def patch_nth {α : Type} (f : α → α) : ℕ → list α → list α
| _ []           := []
| 0 (h :: t)     := f h :: t
| (n+1) (h :: t) := h :: patch_nth n t
```
in mathlib?

#### [Scott Morrison (Nov 30 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148832974):
I've found a few times that it's really painful for update the nth element, because you have to deal with `nth` returning an option, even when you know it's there.

#### [Scott Morrison (Nov 30 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148833022):
A slight variation that is even more useful:
```
def opatch_nth {α : Type} (f : α → option α) : ℕ → list α → list α
| _ []           := []
| 0 (h :: t)     := match f h with
                    | (some e) := e :: t
                    | none     := t
                    end
| (n+1) (h :: t) := h :: opatch_nth n t
```

#### [Kenny Lau (Nov 30 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148833045):
```quote
I've found a few times that it's really painful for update the nth element, because you have to deal with `nth` returning an option, even when you know it's there.
```
 ... did you say it's painful to ***update*** the ***nth*** element?

#### [Scott Morrison (Nov 30 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148833052):
Of course there is `update_nth`

#### [Kenny Lau (Nov 30 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148833091):
also what is it with your `meta`?

#### [Scott Morrison (Nov 30 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148833099):
Oh, yeah, those `meta`s are completely unnecessary :-) Just habit, as I was in a whole file where most things were meta.

#### [Scott Morrison (Nov 30 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148833150):
But  to use `update_nth`, you need to use `nth` earlier to get out the existing element to modify.

#### [Scott Morrison (Nov 30 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148833154):
The typical example here is that I have a list of some structure, and I want to modify a single field of the nth element.

#### [Scott Morrison (Nov 30 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148833205):
In this case the function `f` can be `λ s, { f := x, .. s}`.

#### [Mario Carneiro (Nov 30 2018 at 04:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148837711):
did you say you want to ***modify*** the ***nth*** element?

#### [Reid Barton (Nov 30 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148838352):
Did somebody say "lens"?

#### [Scott Morrison (Nov 30 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148844167):
Thanks. And yes, let's have more lens. :-)

#### [Keeley Hoek (Dec 01 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/150230501):
Wait, isn't the syntax to declare functions in lean `meta def ....`? ;)

