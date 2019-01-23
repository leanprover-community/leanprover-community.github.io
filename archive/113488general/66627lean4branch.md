---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66627lean4branch.html
---

## Stream: [general](index.html)
### Topic: [lean 4 branch](66627lean4branch.html)

---

#### [Mario Carneiro (Apr 11 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124913759):
For those who are interested: Leo just added a bunch of commits to a new lean 4 branch, primarily just removing lean 3 cruft, and you can see a taste of what it means for the size of corelib.
* He's already taken a hatchet to most of the math in the corelib library, leaving only definitions of stuff like `int.mul` without proving it's a comm_ring, etc.
* `norm_num` (the core tactic) is also removed, which eliminates the other main dependency on the algebraic hierarchy.
* `coinductive` and `transfer` were removed, but that's not much of a surprise since they were pure lean anyway.
* I'm a bit surprised `mk_has_sizeof_instance` got the axe, unless `sizeof` itself is going away. But again, it's pure lean so easily replaceable.
* unification hints were removed? I'm not sure what's going on here, but it's true that these got essentially no use since they were introduced, and I think the API was not well thought out. But maybe this is a concern for Tom Hales, who has been planning to use unification hints to resolve some typeclass problems. I'll wait to see what's Leo's plan for algebra before making a judgment on this.
* SMT is gone, we knew that was coming. Maybe we'll get something better later, but I think it's fair to say that the next thing will be significantly different.

I've mentioned this before, but the removal of most of these things from core lib is good news from my point of view, because they can just be reinstated in mathlib, in a place where PRs are not unwelcome. Bad news here would involve things that essentially require lean C support being removed, which can't just be coded up in lean itself, like the SMT stuff. But as Jeremy points out to me, Leo is a world expert when it comes to doing automated theorem proving with equations, and furthermore this is one of the major things that MS will want from any internal uses of Lean, so I'm not unduly worried about this.

#### [Simon Hudon (Apr 11 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124913812):
Thanks for the cliff notes

#### [Patrick Massot (Apr 11 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124920412):
Thank you very much for taking the time to report on this in a way everybody can understand at least vaguely.

#### [Sebastian Ullrich (Apr 11 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124922587):
> I'm a bit surprised mk_has_sizeof_instance got the axe, unless sizeof itself is going away. But again, it's pure lean so easily replaceable.

There _is_ a pretty big surprise hidden here: Lean 4 will support nested and mutual inductives in the kernel, exactly to get rid of the mess that is `sizeof` etc

#### [Mario Carneiro (Apr 11 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124922656):
If you have any say in it, is there any chance of getting structural recursion in definitions? I want my inductive predicates

#### [Sebastian Ullrich (Apr 11 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124922808):
You mean like induction-recursion or...?

#### [Mario Carneiro (Apr 11 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124922814):
No, just plain structural induction, you know, the one that lean does natively?

#### [Mario Carneiro (Apr 11 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124922818):
For some reason that's the one kind of induction you *can't* do using the equation compiler

#### [Mario Carneiro (Apr 11 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124922831):
It's not as big a problem here, but this is the same reason why `nat.add`, defined in the current "obvious way", compiles to a 30-line monster

#### [Sebastian Ullrich (Apr 11 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124922991):
Okay, I was confused about the connection to ginductives. But yes, the equation compiler would have to be touched anyway, so... maybe? I don't know why it's not implemented right now, or if it would be hard to do so.

#### [Mario Carneiro (Apr 11 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124923057):
Cool, just wanted to make sure you are aware of this

#### [Gabriel Ebner (Apr 11 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124924647):
> Lean 4 will support nested and mutual inductives in the kernel

Wow, it would be awesome if nested inductives worked nicely.  Will Lean 4 still use recursors?  It's probably obvious, but how would the recursor for `term` look like?
```lean
inductive term
| fn (args : list term)
```

#### [Sebastian Ullrich (Apr 11 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124924696):
Heh, good question. We've only talked about how to implement mutual inductives so far, to be honest.

#### [Sebastian Ullrich (Apr 11 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124924746):
Well, if you interpret it as a mutual definition of `term` and `list term`, I suppose you should get three motives? Would that work?

#### [Gabriel Ebner (Apr 11 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124925368):
Two motives, but it would work.  So no recursing through `map`, apparently. :disappointed:

#### [Sebastian Ullrich (Apr 30 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/125884409):
@**Gabriel Ebner** I talked with Leo about nested recursion again yesterday and we want to keep using well-founded recursion for this for now. I.e. you should be able to recursive through a dependently-typed `pmap` variant of `map`, which hopefully the default `dec_tac` should make easy to do. Perhaps a future equation compiler, probably written in Lean, will do cleverer things like transforming `map` automatically.

