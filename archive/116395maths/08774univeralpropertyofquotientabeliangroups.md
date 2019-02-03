---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/08774univeralpropertyofquotientabeliangroups.html
---

## Stream: [maths](index.html)
### Topic: [univeral property of quotient abelian groups](08774univeralpropertyofquotientabeliangroups.html)

---


{% raw %}
#### [ Kevin Buzzard (Jul 19 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953243):
<p>I have a <code>comm_group G</code> and a subgroup <code>N</code>, which is the kernel of an <code>is_group_hom f : G -&gt; H</code>. I'd like a quotient group <code>G/N</code>, and an injective group homomorphism from <code>G/N</code> to <code>H</code>. The quotient has been made for general groups (in <code>group_theory.coset</code>) but not the injective hom as far as I can see, and also for modules over an arbitrary ring (with the injective hom), so I can either build the injection for general groups or I can persuade Lean that an abelian group is the same as a Z-module. Have either of these been done? Neither should be hard, but which to do?</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953396):
<p>Should there be an instance <code>(add_comm_group G) -&gt; module ℤ G</code>? What about <code>comm_group G -&gt; module ℤ G</code>? Do either of these cause problems?</p>

#### [ Johan Commelin (Jul 19 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953422):
<p>Modules cause problems, in general. I would stay away of them for now.</p>

#### [ Johan Commelin (Jul 19 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953456):
<p>I think it is best to prove a bit about the universal property of group quotients.</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953616):
<p>I'm trying to define perfectoid spaces, I've just spent an hour worrying about constructing an object isomorphic to an object I already have but in a different universe, and now I'm doing quotient groups :-) Some things are just slow going, I guess!</p>

#### [ Patrick Massot (Jul 19 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953639):
<p>I'm also having universe issues and type class inference issues at the moment</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953691):
<p>It's good for the soul I guess...</p>

#### [ Patrick Massot (Jul 19 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953783):
<p>I'm discovering new error messages</p>

#### [ Patrick Massot (Jul 19 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953784):
<p><code>synthesized type class instance is not definitionally equal to expression inferred by typing rules</code></p>

#### [ Mario Carneiro (Jul 19 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953797):
<p>I think an instance for <code>add_comm_group G -&gt; module ℤ G</code> will not go awry</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953799):
<p>Does that say "you have a diamond"?</p>

#### [ Mario Carneiro (Jul 19 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953812):
<p><code>comm_group G -&gt; module ℤ G</code> doesn't make any sense</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953831):
<blockquote>
<p>I think an instance for <code>add_comm_group G -&gt; module ℤ G</code> will not go awry</p>
</blockquote>
<p><code>module</code> might extend <code>add_comm_group</code> -- will there be an instance the other way?</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953882):
<blockquote>
<p><code>comm_group G -&gt; module ℤ G</code> doesn't make any sense</p>
</blockquote>
<p>well that's a pain because my group laws are all <code>*</code> :-/</p>

#### [ Mario Carneiro (Jul 19 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953884):
<p>ah, actually I think you are right</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953931):
<p>I'm sticking to groups.</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129953995):
<p>I think it's about time we had a mathlib issue about modules, the chat about the problems is dispersed here and there in Zulip, I don't understand the problems myself, and they're stopping Patrick from doing stuff.</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129954121):
<p><code>instance [group α] (s : set α) [normal_subgroup s] : group (left_cosets s) := ...</code>. That's in <code>section quotient_group</code>. How do I find out the name of that instance?</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129954166):
<p>[all in <code>group_theory/coset.lean</code>]</p>

#### [ Chris Hughes (Jul 19 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129954201):
<p><code>left_cosets.group</code></p>

#### [ Chris Hughes (Jul 19 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129954207):
<p>Clue is in the statement.</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129954251):
<p>I remembered there was an algorithm but couldn't remember what it was. Thanks Chris.</p>

#### [ Patrick Massot (Jul 19 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129954312):
<p>you could also use that <code>print_names</code> command we did recently</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129954363):
<p>That's the other type of answer to this question. All that was way over my head, but I cut and pasted some stuff and it was pretty cool :-)</p>

#### [ Chris Hughes (Jul 19 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129954396):
<blockquote>
<p>you could also use that <code>print_names</code> command we did recently</p>
</blockquote>
<p>Is that in mathlib?</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129954475):
<p><a href="#narrow/stream/113488-general/topic/full.20names" title="#narrow/stream/113488-general/topic/full.20names">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full.20names</a></p>

#### [ Johan Commelin (Jul 20 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129989346):
<blockquote>
<p>I think it's about time we had a mathlib issue about modules, the chat about the problems is dispersed here and there in Zulip, I don't understand the problems myself, and they're stopping Patrick from doing stuff.</p>
</blockquote>
<p>I completely agree. They are also stopping me from doing stuff. (Both with simplicial homology and with Lie algebras...)</p>

#### [ Patrick Massot (Jul 20 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129989432):
<p>My hope here is that someone will fix my issue in the norms PR, and this will explain how to handle modules</p>

#### [ Kevin Buzzard (Jul 20 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129989535):
<p>But you've been hoping that someone will fix modules for a long time now, and what I find I'm doing is: occasionally asking "what is the problem with modules again?", and someone answers, in some random thread, and I go "oh", and then the discussion degenerates into <code>out_param</code> stuff, and peters out, and then I forget everything, and it was a waste of everyone's time even talking about it. Making it an issue will at least give me a place where I can read about what the problem is and exactly what it is stopping people from doing.</p>

#### [ Patrick Massot (Jul 20 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129989565):
<p>The difference this time is I opened a PR for normed spaces. But feel free to open an issue</p>

#### [ Kevin Buzzard (Jul 20 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129989631):
<p>If I open the issue it will just be a one-liner saying "something is wrong with modules and this issue is a place where we can talk about what it is and how to fix it".</p>

#### [ Kevin Buzzard (Jul 20 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129989638):
<p>But I'm happy to do this.</p>

#### [ Patrick Massot (Jul 20 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129989649):
<p>The only ones who could write a much better description are Mario, Johannes and Sebastian</p>

#### [ Kevin Buzzard (Jul 20 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/univeral%20property%20of%20quotient%20abelian%20groups/near/129989701):
<p>Not you?</p>


{% endraw %}
