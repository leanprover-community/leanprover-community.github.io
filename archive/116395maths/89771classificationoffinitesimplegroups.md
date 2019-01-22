---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/89771classificationoffinitesimplegroups.html
---

## [maths](index.html)
### [classification of finite simple groups](89771classificationoffinitesimplegroups.html)

#### [Scott Morrison (Sep 22 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/134424165):
I made a very preliminary start on the statement of the classification of finite simple groups.

#### [Scott Morrison (Sep 22 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/134424166):
https://github.com/leanprover-community/mathlib/blob/cfsg/group_theory/classification_of_finite_simple_groups.lean

#### [Scott Morrison (Sep 22 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/134424167):
It contains a statement, but most of the branches quickly devolve in `sorry`.

#### [Scott Morrison (Sep 22 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/134424208):
So far it just has the cyclic, alternating, and Mathieu groups.

#### [Scott Morrison (Sep 22 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/134424210):
Please feel very free, anyone, to push directly to the `cfsg` branch on lean-prover community if you feel like adding some groups. :-)

#### [Mario Carneiro (Sep 22 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/134424219):
by the way, you can use `pprod` in place of `psigma` in the place you asked about earlier

#### [Mario Carneiro (Sep 22 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/134424221):
or better yet, just use a structure :)

#### [Mario Carneiro (Sep 22 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/134424354):
I think this would make a nice target for fabstracts

#### [Mario Carneiro (Sep 22 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/134424724):
Actually, you don't even need to know `nodup` for your `perm.of_cycles` definition. Just take the product of a bunch of swaps. You only need nodup to ensure that the cycles of the result are indeed what you claimed.

#### [Mario Carneiro (Sep 22 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/134424780):
Do you (or anyone else) have any insight in the infinite families part? "Classical Lie groups" is surprisingly hard to define precisely

#### [Scott Morrison (Sep 22 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/134425039):
Yeah, there's a reason I started on the sporadics. :-)

#### [Scott Morrison (Sep 22 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/134425090):
I'm worried that there's nothing much better than defining the 4 two parameter familes of classical groups, and the 10 one parameter families of exceptional/twisted groups...

#### [Mario Carneiro (Sep 22 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/134426871):
The main theorem in Robert Wilson "The Finite Simple Groups" is proving that all these groups are in fact simple. How do you rate that for hardness? :)

#### [Scott Morrison (Sep 22 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/134431025):
I was definitely considering that far out of scope. :-)

#### [Chris Hughes (Sep 22 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/134431821):
I while ago I did start writing a `list_to_cycle` definition, but it was much harder than expected. Now that I've proved some other stuff about cyclic permutations it will probably be much easier. Is this something people care about?

#### [Thales (Jan 14 2019 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/155122187):
Thanks to everyone at Lean Together, who helped me get back on track with Formal Abstracts.

This post is to get the statement of the classification of finite simple groups started in a big way.  Here is a blog post of my non-expert understanding of the classification as it relates to Lean: https://formalabstracts.wordpress.com/2019/01/14/the-journey-begins/   

My suggestion is to do the classification statement as a formal abstract.  What that means concretely is that it should be entirely compatible with Lean3 and mathlib, but with the "cheat" of  `axiom proof_omitted {A : Prop} : A` wherever needed, and where people stake reputation points on the correctness of props asserted by `proof_omitted`.  

Some questions that would be helped by discussion before getting too far into it.
- Is the best path to affine varieties (over an algebraically closed field) through Kevin's general construction of schemes?  It is overkill, but perhaps the simplest way forward.
- Is there agreement about the approach sketched for the groups of Lie type?  In particular, about the choice of using Lie structure theory rather than concrete implementations of the groups through their faithful representations as matrix groups.  My preference is for a Lie structural approach.
- What counts as an acceptable specification of a finite simple group.  For instance, for the pariahs, can we say that they are specified by their order?
- What sanity checks can we produce that the definitions are correct?

#### [Patrick Massot (Jan 15 2019 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/155152958):
@**Assia Mahboubi**

#### [Kevin Buzzard (Jan 15 2019 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/155153007):
@**Scott Morrison|110087**

#### [Patrick Massot (Jan 15 2019 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/155153233):
In my daily arXiv email this morning: https://arxiv.org/abs/1901.04223: 
> The proof of Theorem 1.6 is based on Theorem 1.4 (whose proof on its turn is based on [34], which uses the CFSG), and hence is very different from that in [39], which is based on the classification of compact complex surfaces.

I think CFSG stands for the title of this thread

#### [Kevin Buzzard (Jan 15 2019 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/155154160):
I didn't even define k-points of a scheme, for k a field (or a ring), but this will not be hard once we've refactored schemes and done them "properly" via locally ringed spaces etc (I took shortcuts in my formalisation -- what I have is provably equivalent to a scheme, but I used that Spec(A) was a locally ringed space without proving it). I'm meeting Ramon today and we will be working on this project seriously this term (both of us were busy with other things last term). The scheme route would lead to schemes called things like $$SL_n$$ whose $$k$$-points for $$k$$ a finite field would be the familiar $$SL_n(k)$$; I think you then have to leave the world of schemes and take the quotient group to make $$PSL_n(k)$$. I think that I had better read the statement of the classification myself actually!

#### [Thales (Jan 16 2019 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/155220783):
We will definitely need products and morphisms to define affine algebraic groups.  Have products and morphisms of schemes been defined?  Or is that something we need to do?

I think it is best to define the quotient PSL(n,k) of SL(n,k) as a quotient of k-points rather than as the k-points of a quotient of varieties.

Today, I have been adding more details to the sporadic group constructions at the url posted yesterday.

#### [Johan Commelin (Jan 16 2019 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/155232891):
As far as I know, neither morphisms nor products are defined.

#### [Kevin Buzzard (Jan 16 2019 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/155238230):
To define these things we need to take a more mature approach to schemes, which I did not do initially (it was just a race to the definition because I was having fun and learning). I did not even define locally ringed spaces, I cheated. My student Ramon Fernandez Mir has now defined locally ringed spaces in a private repo, and things are slowly but surely proceeding. When we met yesterday I urged him to make his work public. I think that the definition of binary products of schemes would be very interesting to do in Lean, not least because I remember well skipping over the details of the 7 point process in Hartshorne as a graduate student!

As for PSL(n,k), yes,  I think you have to define it as a quotient of points, the quotient scheme PSL equals PGL and PGL(n,k) is not in general simple, indeed it usually contains PSL(n,k) as an index 2 subgroup. The map from SL_n to PGL_n is surjective as fppf sheaves but not on k-points.

#### [Thales (Jan 18 2019 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/classification of finite simple groups/near/156327271):
It makes me wonder if the algebraic geometry will become the largest part of this project.

The url above now has informal description of all sporadic groups that I think should be sufficient for this project, except that a few conjugacy classes in the monster should be better specified.  (It states a few claims that are not completely backed by sources yet.)  

In describing the sporadic groups, it became apparent that there are numerous constructions from the Feit-Thompson theorem that should be useful.  That project presumably has libraries with topics such as semidirect products, covers, central extensions, extraspecial p-groups, quadratic forms, basic facts about orbits and stabilizers that would be useful here.

