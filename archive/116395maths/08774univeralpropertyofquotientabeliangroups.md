---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/08774univeralpropertyofquotientabeliangroups.html
---

## Stream: [maths](index.html)
### Topic: [univeral property of quotient abelian groups](08774univeralpropertyofquotientabeliangroups.html)

---

#### [Kevin Buzzard (Jul 19 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953243):
I have a `comm_group G` and a subgroup `N`, which is the kernel of an `is_group_hom f : G -> H`. I'd like a quotient group `G/N`, and an injective group homomorphism from `G/N` to `H`. The quotient has been made for general groups (in `group_theory.coset`) but not the injective hom as far as I can see, and also for modules over an arbitrary ring (with the injective hom), so I can either build the injection for general groups or I can persuade Lean that an abelian group is the same as a Z-module. Have either of these been done? Neither should be hard, but which to do?

#### [Kevin Buzzard (Jul 19 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953396):
Should there be an instance `(add_comm_group G) -> module ℤ G`? What about `comm_group G -> module ℤ G`? Do either of these cause problems?

#### [Johan Commelin (Jul 19 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953422):
Modules cause problems, in general. I would stay away of them for now.

#### [Johan Commelin (Jul 19 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953456):
I think it is best to prove a bit about the universal property of group quotients.

#### [Kevin Buzzard (Jul 19 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953616):
I'm trying to define perfectoid spaces, I've just spent an hour worrying about constructing an object isomorphic to an object I already have but in a different universe, and now I'm doing quotient groups :-) Some things are just slow going, I guess!

#### [Patrick Massot (Jul 19 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953639):
I'm also having universe issues and type class inference issues at the moment

#### [Kevin Buzzard (Jul 19 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953691):
It's good for the soul I guess...

#### [Patrick Massot (Jul 19 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953783):
I'm discovering new error messages

#### [Patrick Massot (Jul 19 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953784):
`synthesized type class instance is not definitionally equal to expression inferred by typing rules`

#### [Mario Carneiro (Jul 19 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953797):
I think an instance for `add_comm_group G -> module ℤ G` will not go awry

#### [Kevin Buzzard (Jul 19 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953799):
Does that say "you have a diamond"?

#### [Mario Carneiro (Jul 19 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953812):
`comm_group G -> module ℤ G` doesn't make any sense

#### [Kevin Buzzard (Jul 19 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953831):
```quote
I think an instance for `add_comm_group G -> module ℤ G` will not go awry
```
`module` might extend `add_comm_group` -- will there be an instance the other way?

#### [Kevin Buzzard (Jul 19 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953882):
```quote
`comm_group G -> module ℤ G` doesn't make any sense
```
well that's a pain because my group laws are all `*` :-/

#### [Mario Carneiro (Jul 19 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953884):
ah, actually I think you are right

#### [Kevin Buzzard (Jul 19 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953931):
I'm sticking to groups.

#### [Kevin Buzzard (Jul 19 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953995):
I think it's about time we had a mathlib issue about modules, the chat about the problems is dispersed here and there in Zulip, I don't understand the problems myself, and they're stopping Patrick from doing stuff.

#### [Kevin Buzzard (Jul 19 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129954121):
`instance [group α] (s : set α) [normal_subgroup s] : group (left_cosets s) := ...`. That's in `section quotient_group`. How do I find out the name of that instance?

#### [Kevin Buzzard (Jul 19 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129954166):
[all in `group_theory/coset.lean`]

#### [Chris Hughes (Jul 19 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129954201):
`left_cosets.group`

#### [Chris Hughes (Jul 19 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129954207):
Clue is in the statement.

#### [Kevin Buzzard (Jul 19 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129954251):
I remembered there was an algorithm but couldn't remember what it was. Thanks Chris.

#### [Patrick Massot (Jul 19 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129954312):
you could also use that `print_names` command we did recently

#### [Kevin Buzzard (Jul 19 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129954363):
That's the other type of answer to this question. All that was way over my head, but I cut and pasted some stuff and it was pretty cool :-)

#### [Chris Hughes (Jul 19 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129954396):
```quote
you could also use that `print_names` command we did recently
```
Is that in mathlib?

#### [Kevin Buzzard (Jul 19 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129954475):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full.20names

#### [Johan Commelin (Jul 20 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129989346):
```quote
I think it's about time we had a mathlib issue about modules, the chat about the problems is dispersed here and there in Zulip, I don't understand the problems myself, and they're stopping Patrick from doing stuff.
```
I completely agree. They are also stopping me from doing stuff. (Both with simplicial homology and with Lie algebras...)

#### [Patrick Massot (Jul 20 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129989432):
My hope here is that someone will fix my issue in the norms PR, and this will explain how to handle modules

#### [Kevin Buzzard (Jul 20 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129989535):
But you've been hoping that someone will fix modules for a long time now, and what I find I'm doing is: occasionally asking "what is the problem with modules again?", and someone answers, in some random thread, and I go "oh", and then the discussion degenerates into `out_param` stuff, and peters out, and then I forget everything, and it was a waste of everyone's time even talking about it. Making it an issue will at least give me a place where I can read about what the problem is and exactly what it is stopping people from doing.

#### [Patrick Massot (Jul 20 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129989565):
The difference this time is I opened a PR for normed spaces. But feel free to open an issue

#### [Kevin Buzzard (Jul 20 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129989631):
If I open the issue it will just be a one-liner saying "something is wrong with modules and this issue is a place where we can talk about what it is and how to fix it".

#### [Kevin Buzzard (Jul 20 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129989638):
But I'm happy to do this.

#### [Patrick Massot (Jul 20 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129989649):
The only ones who could write a much better description are Mario, Johannes and Sebastian

#### [Kevin Buzzard (Jul 20 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129989701):
Not you?

