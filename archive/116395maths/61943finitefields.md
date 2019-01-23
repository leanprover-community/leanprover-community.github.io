---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/61943finitefields.html
---

## Stream: [maths](index.html)
### Topic: [finite fields](61943finitefields.html)

---


{% raw %}
#### [ Joey van Langen (Jan 09 2019 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154730425):
I'm going to do some works concerning finite fields. (number of elements, existence and uniqueness)
Can anyone tell me if the following things exist for lean in mathlib or somewhere else and where I can find them?
Integers modulo a prime, prime subfields, ring isomorphisms?

#### [ Rob Lewis (Jan 09 2019 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154730801):
Integers mod a prime are at least instantiated as a field: https://github.com/leanprover/mathlib/blob/master/data/zmod/basic.lean#L313

#### [ Rob Lewis (Jan 09 2019 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154730956):
Others will probably know more about your other questions. (@**Kenny Lau** ?)

#### [ Kenny Lau (Jan 09 2019 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154731006):
ik ben aan het bezoeken in de stedelijk museum :p

#### [ Joey van Langen (Jan 09 2019 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154731019):
Integers modulo p is a nice start

#### [ Rob Lewis (Jan 09 2019 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154731107):
I'm glad someone is taking my suggestion to relax this afternoon!

#### [ Joey van Langen (Jan 09 2019 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154731112):
Do isomorphisms exist in any context? I can only find them for types

#### [ Kenny Lau (Jan 09 2019 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154731465):
use hott!

#### [ Joey van Langen (Jan 09 2019 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154731624):
what do you mean by use hott?

#### [ Kevin Buzzard (Jan 09 2019 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154732681):
he's just trolling. He says "use something other than Lean"

#### [ Kevin Buzzard (Jan 09 2019 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154732787):
But I guess the answer to your question is that in general most objects don't have isomorphism between those objects already defined in Lean.

#### [ Kevin Buzzard (Jan 09 2019 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154732821):
You are more likely to find morphisms though, so you can define isomorphisms without too much pain. I guess morphisms of rings will be there somewhere.

#### [ Kevin Buzzard (Jan 09 2019 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154732935):
Some students at Imperial have done some work on splitting fields, but I don't know if it's public. What is your proposal for defining a finite field? Usually the definition I give is "splitting field of $$X^{p^n}-X$$ over $$\mathbb{F}_p$$, but I don't think Lean has splitting fields, at least not publically.

#### [ Joey van Langen (Jan 09 2019 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154733013):
I'm going to use the definition as a splitting field, by using the splitting field stuff currently in the community repo

#### [ Joey van Langen (Jan 09 2019 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154733317):
I will also use the material there concerning algebras as it will give me the tools to realize any finite field as a vector space over $$\mathbb{F}_p$$

#### [ Joey van Langen (Jan 09 2019 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154733332):
How do you put latex in these messages?

#### [ Kevin Buzzard (Jan 09 2019 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154733420):
`$$\mathbb{F}_p$$`

#### [ Kevin Buzzard (Jan 09 2019 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154733467):
Doesn't always work, for example \sqrt doesn't seem to work

#### [ Joey van Langen (Jan 11 2019 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154923261):
So I have been doing some work on the finite fields with the help of @**Casper Putz**  for the past couple of days.
We are now close to proving that every finite field has p^n elements with p a prime number.
Most effort was spent proving some simple results which we couldn't find anywhere,
such as the specification of the prime ideals and maximal ideals of $$\mathbb{Z}$$ and proving that the zero ideal in a field is in fact maximal.
Would people be interested in seeing these results added to mathlib separately? They seem quite useful

#### [ Chris Hughes (Jan 11 2019 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154924258):
Yes

#### [ Joey van Langen (Jan 11 2019 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154924456):
Any suggestions of where to put that stuff?

#### [ Johan Commelin (Jan 11 2019 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154924479):
Do you guys have push access to https://github.com/leanprover-community/mathlib/ ?

#### [ Joey van Langen (Jan 11 2019 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154924488):
For example should the explicit specification of the prime ideals of the integers be put with ideals, with the integers or a separate file entirely

#### [ Johan Commelin (Jan 11 2019 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154924492):
If so, put it on a branch `finite_fields` in that repo.

#### [ Johan Commelin (Jan 11 2019 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154924550):
Aaah, I'm always bad at deciding what should go in which file.

#### [ Joey van Langen (Jan 11 2019 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154924557):
```quote
Do you guys have push access to https://github.com/leanprover-community/mathlib/ ?
```
 We don't have access to the leanprover-community yet. Would be nice to have

#### [ Joey van Langen (Jan 11 2019 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154924578):
We're still working on it on my github, but after some cleanup that would probably be the best place to put it

#### [ Chris Hughes (Jan 11 2019 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154924590):
It basically depends on imports. Probably ideals imports everything you need, so it should probably go there.

#### [ Johan Commelin (Jan 11 2019 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finite%20fields/near/154926308):
@**Mario Carneiro** Could you please give @**Joey van Langen** push access on community mathlib? He's a PhD student of Sander Dahmen.


{% endraw %}
