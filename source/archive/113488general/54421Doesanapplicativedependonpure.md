---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54421Doesanapplicativedependonpure.html
---

## [general](index.html)
### [Does an applicative depend on pure?](54421Doesanapplicativedependonpure.html)

#### [Mario Carneiro (Aug 10 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Does%20an%20applicative%20depend%20on%20pure%3F/near/131222242):
A surprisingly hard problem: Prove or construct a counterexample to the following claim: If two (lawful) applicative structures on `F` have the same `seq` function, then they are equal.

#### [Mario Carneiro (Aug 10 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Does%20an%20applicative%20depend%20on%20pure%3F/near/131222417):
Originally I thought it might be true, by analogue to the uniqueness of the identity of a monoid, but now I'm not so sure. Nevertheless there are no obvious ways to cook up an applicative with two different pures. Here is the equational theory of applicatives (with map eliminated):
$$p_1(f)\cdot p_1(x)=p_1(f \,x)$$
$$f\cdot p_1(x)=p_1(\lambda g.\, g\,x)\cdot f$$
$$p_1(\circ)\cdot h\cdot g\cdot x=h\cdot (g\cdot x)$$
$$p_1(id)\cdot x=x$$

