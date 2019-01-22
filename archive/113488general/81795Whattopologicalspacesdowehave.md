---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/81795Whattopologicalspacesdowehave.html
---

## [general](index.html)
### [What topological spaces do we have?](81795Whattopologicalspacesdowehave.html)

#### [Kenny Lau (Mar 28 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124293562):
I'm aware that this place does not value examples, just abstract theorems, but do we have R^n? C^n? S^n? D^n?

#### [Kenny Lau (Mar 28 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124293573):
by "this place" I mean Mario

#### [Mario Carneiro (Mar 28 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124295797):
I like examples when they are abstract constructions :)

#### [Mario Carneiro (Mar 28 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124295837):
In this case you're talking about making a topological space out of K^n where K is a topological field or vector space

#### [Kenny Lau (Mar 28 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296128):
that's only the first two cases :)

#### [Mario Carneiro (Mar 28 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296187):
For S^n and D^n, I would just define them as the appropriate subspaces. There are loads of more abstract definitions of S^n of course, but I would suggest sticking to actual spheres for the definition

#### [Kenny Lau (Mar 28 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296200):
agreed, but do you have norm?

#### [Mario Carneiro (Mar 28 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296205):
Patrick had a working definition

#### [Kenny Lau (Mar 28 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296208):
in R^n?

#### [Mario Carneiro (Mar 28 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296255):
Hm, it occurs to me that "the unit sphere" is well defined in any normed vector space

#### [Kenny Lau (Mar 28 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296260):
for god's sake

#### [Mario Carneiro (Mar 28 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296266):
Patrick's definition gives a norm on any normed space

#### [Mario Carneiro (Mar 28 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296269):
of course R^n will be a normed space

#### [Mario Carneiro (Mar 28 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296316):
but there is some concern about whether to use the 2-norm vs some other p-norm

#### [Mario Carneiro (Mar 28 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296340):
If you just need something quick and dirty for some application, go ahead and define it however you like

#### [Kenny Lau (Mar 28 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296396):
I don’t need it now

#### [Mario Carneiro (Mar 28 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296402):
The simplest abstract definition if you only need the topological structure is by iterating the suspension operation on `bool`

#### [Kenny Lau (Mar 28 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296415):
good luck proving that S^n \ {pt} ~ R^n

#### [Kenny Lau (Mar 28 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296461):
good luck finding a single point inside

#### [Mario Carneiro (Mar 28 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296486):
I guess it's not obvious that S^n is homogeneous as the suspension, but it's easy to show S^n \ {north pole} ~ R^n

#### [Kenny Lau (Mar 28 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296533):
hmm

#### [Kenny Lau (Mar 28 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296554):
and R^n \ {0} def retracts to S^(n-1)?

#### [Mario Carneiro (Mar 28 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296606):
That's dead easy with the suspension, since R^n\{0} maps to S^(n-1) x (0,1)

#### [Kenny Lau (Mar 28 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296616):
tu ganhas

#### [Mario Carneiro (Mar 28 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296627):
I agree that homogeneity is easier with the geometric representation, since then you can use orthogonal transformations

#### [Kenny Lau (Mar 28 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296666):
next time someone asks me what S^n is, I’m gonna say “repeated suspension of bool” 😛

#### [Kenny Lau (Mar 28 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296681):
they be like “entao o que e bool?”

#### [Mario Carneiro (Mar 28 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296689):
I think that's the definition the HoTT people use, more or less

#### [Mario Carneiro (Mar 28 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296702):
Also, if you do repeated suspension on `unit` you get D^n

#### [Mario Carneiro (Mar 28 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296746):
or just take [0,1]^n

#### [Mario Carneiro (Mar 28 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124296762):
But for a mathlib definition, I would imagine it will be used in many contexts, not just topological, i.e. you might care about manifold structure in which case "corners" are not appreciated

#### [Patrick Massot (Mar 28 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124309189):
I almost have $$\mathbb{R}^n$$ as a topological space. I only need to find one day without a million urgent things to do. I have normed spaces and Pi instances for many things. But indeed the norm we'll have on $$\mathbb{R}^n$$ will have box balls, which is not good if you want to get a smooth $$\mathbb{S}^{n-1}$$.

#### [Kenny Lau (Mar 29 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124355085):
https://math.stackexchange.com/a/2712786/328173

#### [Kenny Lau (Mar 29 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124355086):
@**Mario Carneiro** this is part of the reason I asked that question

#### [Kenny Lau (Mar 29 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What topological spaces do we have?/near/124355089):
if we have enough lemmas we might be able to formalize that

