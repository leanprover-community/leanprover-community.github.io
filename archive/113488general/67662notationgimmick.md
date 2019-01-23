---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67662notationgimmick.html
---

## Stream: [general](index.html)
### Topic: [notation gimmick](67662notationgimmick.html)

---


{% raw %}
#### [ Kevin Buzzard (Jun 02 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447537):
If I have a family of rings `{gamma : Type} (R : gamma -> Type) [forall i, ring (R i)]`

#### [ Kevin Buzzard (Jun 02 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447541):
For a mathematician it would look clearer if I could write `forall i, ring R_i`

#### [ Kevin Buzzard (Jun 02 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447585):
can i make R an instance of some notation typeclass or use some other notation gimmick to do this?

#### [ Kenny Lau (Jun 02 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447591):
madness

#### [ Kevin Buzzard (Jun 02 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447595):
you're such a pessimist

#### [ Kevin Buzzard (Jun 02 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447597):
just because it could be another valid variable name

#### [ Kevin Buzzard (Jun 02 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447606):
what about some weird unicode underline that's not valid

#### [ Mario Carneiro (Jun 02 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447664):
This was a proposal on core lean a while back

#### [ Simon Hudon (Jun 02 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447665):
That's a terrible idea.

#### [ Mario Carneiro (Jun 02 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447666):
oh wait I misunderstood

#### [ Mario Carneiro (Jun 02 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447670):
I thought you wanted to avoid the `gamma` and `R` decls

#### [ Kevin Buzzard (Jun 02 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447712):
it's the underscore I want

#### [ Kevin Buzzard (Jun 02 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447715):
sorry

#### [ Mario Carneiro (Jun 02 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447716):
`R_i` parsed as nonatomic is a terrible idea, underscores are used *gratuitously* in lean as spaces that don't break the identifier

#### [ Kevin Buzzard (Jun 02 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447718):
We would always talk about a family $$R_i$$ of rings

#### [ Kevin Buzzard (Jun 02 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447722):
how about subscript i?

#### [ Mario Carneiro (Jun 02 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447728):
That's actually been discussed before too

#### [ Kevin Buzzard (Jun 02 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447730):
proper subscript would be brilliant

#### [ Mario Carneiro (Jun 02 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447731):
Did you know there is a subscript for every letter except q?

#### [ Kevin Buzzard (Jun 02 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447734):
sometimes I know that

#### [ Kevin Buzzard (Jun 02 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447776):
I have been browsing that file

#### [ Kevin Buzzard (Jun 02 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447778):
I was looking for cool curly sheaf notation :-)

#### [ Mario Carneiro (Jun 02 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447796):
Anyway I suggest you don't try too hard to perfectly replicate all the inconsistencies in math notation

#### [ Simon Hudon (Jun 02 2018 at 03:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127447893):
As an additional note, I believe an identifier followed by a subscript (like `fooₐ`) is treated as one big identifier, not as `foo` followed by `ₐ`

#### [ Kevin Buzzard (Jun 02 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127448374):
Yes I'm sure you're right. It would just look less nerdy

#### [ Simon Hudon (Jun 02 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20gimmick/near/127448450):
Hmmm, a mathematician complaining about looking too nerdy ...


{% endraw %}
