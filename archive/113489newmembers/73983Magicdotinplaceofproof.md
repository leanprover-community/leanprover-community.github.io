---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/73983Magicdotinplaceofproof.html
---

## Stream: [new members](index.html)
### Topic: [Magic dot in place of proof?](73983Magicdotinplaceofproof.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mark Dickinson (Nov 05 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146826913):
Looking through the standard library, I see this in `basic.lean`:
```lean
lemma not_succ_le_zero : ∀ (n : ℕ), succ n ≤ 0 → false
.
```
What's the magic dot on the second line? Is this syntactic sugar for a particular tactic or set of tactics?

Source : https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/library/init/data/nat/basic.lean#L84-L85

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 05 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146826965):
no, it just says "this is the end of the definition", and causes lean to realise that there are no cases to prove!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 05 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146826976):
magic. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 05 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146827317):
See also https://leanprover.zulipchat.com/#narrow/stream/113489-new-members/topic/what.20does.20.2E.20mean.20here.3F

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mark Dickinson (Nov 05 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146827412):
Ah, thank you! I did try searching the archives, but it's not easy to figure out how to search for a single period.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 05 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146827436):
I searched for the name of this lemma, because I was pretty sure it was already discussed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mark Dickinson (Nov 05 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146827446):
Yep, I should have thought to use `not_succ_le_zero` as a search term ..

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 05 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146827451):
And there are very few opportunities to use this trick

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 05 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146827459):
No problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 06 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146832913):
I've sometimes found it useful when rewriting a proof,  e.g. instead of temporarily commenting out the rest of a proof, I just insert a `.`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 06 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146833077):
I usually insert a `#exit`

