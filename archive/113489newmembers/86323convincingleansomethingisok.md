---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/86323convincingleansomethingisok.html
---

## Stream: [new members](index.html)
### Topic: [convincing lean something is ok](86323convincingleansomethingisok.html)

---

#### [Ned Summers (Aug 20 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/convincing%20lean%20something%20is%20ok/near/132461786):
I'm trying to construct a function `f :  a → b` (as part of an instance of a structure) with two types a and b and non-trivially I have that for some type c defined differently in fact `b=c` (and I can prove that if needed).  

How can I let lean know that in fact, what might appear to be of type `a → c` (being given by `λ x , y`, for some `y : c`) is in fact totally fine and fulfils the requirement for being of type `a → b`?

#### [Simon Hudon (Aug 20 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/convincing%20lean%20something%20is%20ok/near/132461983):
One way do it is to use `cast`. It does get in the way when trying to reason about the function but it does what you said. You could do it as `cast (by subst c) f`

#### [Simon Hudon (Aug 20 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/convincing%20lean%20something%20is%20ok/near/132462161):
I sometimes define local notations for this kind of cast: 

```lean
local prefix `♯`:0 := cast (by cc <|> solve_by_elim)
```

#### [Ned Summers (Aug 21 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/convincing%20lean%20something%20is%20ok/near/132508506):
Ah ok, thanks. I'm not familiar with using subst, how would I include a proof that b = c in this? Currently, I'm being told "subst tactic failed, given expression is not a local constant". Apologies, I am very much a beginning.

#### [Ned Summers (Aug 21 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/convincing%20lean%20something%20is%20ok/near/132509682):
Never mind, managed to get that sorted!

#### [Ned Summers (Aug 21 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/convincing%20lean%20something%20is%20ok/near/132510322):
I'm not sure if this is what you originally meant, Simon, but I ended up solving this with `λ x , cast( ... ) y`, using my proof in the brackets. However, if I also had properties previously expressed about y, how do I go about using these for the cast version?

For example (fairly close to what I'm doing), if y were in the center of a group, is it possible to prove that for some other member x, cast _ y * x = x * cast _ y? Or do we lose this information in casting?

#### [Kevin Buzzard (Aug 21 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/convincing%20lean%20something%20is%20ok/near/132517275):
Maybe you should take a look at https://leanprover.github.io/theorem_proving_in_lean/tactics.html#rewriting

