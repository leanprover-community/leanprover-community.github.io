---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88707subsetorsubtype.html
---

## Stream: [general](index.html)
### Topic: [subset or subtype?](88707subsetorsubtype.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 04 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268484):
I wrote presheaves of types twice in my life and I see now that my definitions differ.

#### [ Kevin Buzzard (Mar 04 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268485):
First is

#### [ Kevin Buzzard (Mar 04 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268528):
`(F : Π U : set α, T.is_open U → Type*) `

#### [ Kevin Buzzard (Mar 04 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268536):
Second is

#### [ Kevin Buzzard (Mar 04 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268537):
`(F : {U // topological_space.is_open T U} → Type*)`

#### [ Kevin Buzzard (Mar 04 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268539):
Which is "better"?

#### [ Kevin Buzzard (Mar 04 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268544):
I seem to be able to work with either

#### [ Kevin Buzzard (Mar 04 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268647):
Is the only difference that with the first I have two different names U and HU, and with the second I have V.val and V.property?

#### [ Gabriel Ebner (Mar 04 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268652):
Yes, it is analogous to the difference between `A → B → C` and `A ∧ B → C`.

#### [ Kevin Buzzard (Mar 04 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268694):
But with those two choices, functional program people prefer the first, right?

#### [ Patrick Massot (Mar 04 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268696):
Proof assistant people seem to always prefer `A → B → C`, so which is better for presheaves?

#### [ Kevin Buzzard (Mar 04 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268697):
which is which ;-)

#### [ Kevin Buzzard (Mar 04 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268698):
Presumably H.1 and H.2 is V.val and V.property so this is the one I should perhaps avoid

#### [ Reid Barton (Mar 04 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268699):
The second one also gives you the name "V", which for doing abstract sheaf theory things (that don't care about the particular site) seems like it would be more convenient.

#### [ Kevin Buzzard (Mar 04 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268704):
oh but here's a difference: A and B is a type

#### [ Kevin Buzzard (Mar 04 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268705):
so it can be used more easily as a target

#### [ Kevin Buzzard (Mar 04 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123268797):
This doesn't seem to matter in practice. I am going for set because it seems to be analogous to the "more functional" `A -> B -> C`

#### [ Reid Barton (Mar 04 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123269074):
If you imagine defining a sheaf of sets on a general site, then the first way seems really unnatural (what would be the analogue of `is_open`?) So from a "math" perspective, the second way looks better.
I don't know what the practical implications are, though.

#### [ Reid Barton (Mar 04 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20or%20subtype%3F/near/123269187):
(I would also set it up so that I can write `U : T.open_set`, and use $$\cap$$ and $$\cup$$ and $$\subset$$ directly on open sets, etc.)


{% endraw %}
