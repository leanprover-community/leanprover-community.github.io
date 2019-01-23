---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/85259databaseofgroups.html
---

## Stream: [maths](index.html)
### Topic: [database of groups](85259databaseofgroups.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 23 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148218899):
Looking at the second year group theory problem sheets, there seem to be just as many "prove this is false" questions as "prove this is true" ones. I want to deduce from this that mathematicians are interested in not only theorems about groups, but examples of groups (e.g. as a source of counterexamples). @**Amelia Livingston** would in particular be interested in these, and we've tentatively begun discussions on what should go in there -- cyclic groups, dihedral groups, C_2 x C_2, symmetric and alternating groups.

Got to go and give a lecture, but briefly: (1) does it matter what the underlying type is for these groups (2) does anyone know about whether the standard databases I've used in the past in GAP and magma have been formally verified?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 23 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148231934):
Semidirect products would let you construct a bunch of small groups and many other things of interest.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 23 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148232015):
Do we not already have some of these things in some form?
I guess mathematicians are in the habit of giving different names to the same thing in different settings ($$C_n$$, $$\mathbb{Z}/n\mathbb{Z}$$, $$\mathbb{F}_p$$ when $$n = p$$ is prime) but I don't know whether that is a good idea in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 23 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148233793):
Well, we will want $$\mathbb{F}_q$$ at some point... so then we will also get a $$\mathbb{F}_p$$...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 23 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148235984):
I guess I'm not sure exactly what a "database of groups" would look like in Lean... maybe that's part of the question

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 23 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148238581):
What I need them for is to be able to answer questions such as "true or false: if G is abelian then G is cyclic".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 24 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148253284):
@**Kevin Buzzard**, you might look at the abortive start I made on the (statement of the) classification of finite simple groups.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 24 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148253289):
Unfortunately, even constructing the sporadics is a big project.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 24 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148267459):
I think our questions are much more mundane. For example how should one define the dihedral groups? As a presentation? A subgroup of a permutation group? An explicit list of elements with a given multiplication? etc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 24 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148268002):
Oh, I forgot to put a link, sorry. https://github.com/leanprover/mathlib/compare/master...leanprover-community:cfsg

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 24 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148268060):
I was defining things as terms of `Grp`, a bundled group. This gives you some freedom to chose different ways to define different groups. You can see some examples in that diff. For example, I did the Mathieu 12 and 24 via generators in a permutation group, M23 and M22 as stabilisers,  but the alternating group as a subtype of `perm (fin n)`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 24 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148268109):
It would be nice to have `gap_db(n,m)` constructor that would give you a representative of the group with `n` elements that is listed as `m`th iso-class in the GAP database.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 24 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148268154):
ha ha, you could write an interface to gap which pulls off the group from the GAP database, lists all the elements, makes a new inductive type with a constructor for each object, and then just puts together the multiplication table manually and proves it's a group with dec_trivial :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 24 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148268612):
@**Kevin Buzzard** I think there might be quite some potential in such an interface...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 24 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148268628):
I don't know if it should be an inductive type or whatever, I guess GAP can also give you generators and relations etc... Anyway, this is just wishful thinking from my side atm.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 24 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148268782):
we could certainly have a way to define groups by their generators and relations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 24 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148268786):
of course lots of questions about finitely presented groups are very hard to solve

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 24 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148269104):
and some are impossible to solve!

