---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/05461subtypesvsets.html
---

## [general](index.html)
### [subtypes v sets](05461subtypesvsets.html)

#### [Kevin Buzzard (Mar 04 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123245378):
I have `U : set alpha` and I want to make a Pi type which morally is `\Pi P : U, (some function of P)`

#### [Kevin Buzzard (Mar 04 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123245429):
I went for `\Pi P : {u : alpha // U u}, ...`

#### [Kevin Buzzard (Mar 04 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123245440):
and now I am constantly running into `v \in U` which I want to do my Pi
 stuff to

#### [Kevin Buzzard (Mar 04 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123245535):
meh I guess I just shouldn't be considering "elements of U" I should just be avoiding the set notation completely now

#### [Andrew Ashworth (Mar 04 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123246309):
if you want to stay with sets, you could use the set image lemmas

#### [Andrew Ashworth (Mar 04 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123246397):
but definitely type theory notation is more natural to work in

#### [Mario Carneiro (Mar 04 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123253942):
```quote
I have `U : set alpha` and I want to make a Pi type which morally is `\Pi P : U, (some function of P)`
```
Did you actually try `\Pi P : U, (some function of P)`? That should work because of coercions

#### [Kevin Buzzard (Mar 04 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123261361):
No I didn't :-) I know that if I'd tried this, I would have ended up not knowing what the type of P actually was, at least initially. Probably what you're saying is that if I'd tried it, it would have unfolded into what I actually used. More and more I am deciding not to use coercions or type classes because I realise that rather than using them and then struggling later it is easier for me to just do all the work myself. I guess what I'm saying is that initially things like coercions and the type class system were complete mysteries to me and I could see them working in simple cases and failing in more complex ones and didn't really understand enough to know how to make them work for me. Now I've decided to do all coercions myself, and of course now I understand what's going on much better. The next phrase will be me attempting to use these tools again, but this time knowing how to use them properly.

#### [Chris Hughes (Mar 04 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123264655):
@**Kevin Buzzard** I just wrote some docs about this, which I PRed to your WIP docs.

#### [Patrick Massot (Mar 04 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123268965):
@**Chris Hughes** your doc on set-like stuff is awesome. I added some comments (but I guess Kevin needs to allow them before you can see them). Then I think this should go straight to mathlib in the theories folder (with a link in https://github.com/leanprover/mathlib/blob/master/docs/theories.md)

#### [Chris Hughes (Mar 04 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123271485):
The main downside I can see to the Pi version, is if you ever wanted to prove the function is injective or has an inverse. No idea if you'd ever want to do that.

#### [Kevin Buzzard (Mar 04 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtypes%20v%20sets/near/123273900):
In my context I don't think I'll ever want to do this.

