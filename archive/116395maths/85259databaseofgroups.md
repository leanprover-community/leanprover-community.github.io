---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/85259databaseofgroups.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [database of groups](https://leanprover-community.github.io/archive/116395maths/85259databaseofgroups.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Nov 23 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148218899):
<p>Looking at the second year group theory problem sheets, there seem to be just as many "prove this is false" questions as "prove this is true" ones. I want to deduce from this that mathematicians are interested in not only theorems about groups, but examples of groups (e.g. as a source of counterexamples). <span class="user-mention" data-user-id="118107">@Amelia Livingston</span> would in particular be interested in these, and we've tentatively begun discussions on what should go in there -- cyclic groups, dihedral groups, C_2 x C_2, symmetric and alternating groups.</p>
<p>Got to go and give a lecture, but briefly: (1) does it matter what the underlying type is for these groups (2) does anyone know about whether the standard databases I've used in the past in GAP and magma have been formally verified?</p>

#### [ Reid Barton (Nov 23 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148231934):
<p>Semidirect products would let you construct a bunch of small groups and many other things of interest.</p>

#### [ Reid Barton (Nov 23 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148232015):
<p>Do we not already have some of these things in some form?<br>
I guess mathematicians are in the habit of giving different names to the same thing in different settings (<span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>C</mi><mi>n</mi></msub></mrow><annotation encoding="application/x-tex">C_n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07153em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:-0.07153em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>, <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Z</mi></mrow><mi mathvariant="normal">/</mi><mi>n</mi><mrow><mi mathvariant="double-struck">Z</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{Z}/n\mathbb{Z}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Z</span></span><span class="mord mathrm">/</span><span class="mord mathit">n</span><span class="mord"><span class="mord mathbb">Z</span></span></span></span></span>, <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi mathvariant="double-struck">F</mi><mi>p</mi></msub></mrow><annotation encoding="application/x-tex">\mathbb{F}_p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.974998em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathbb">F</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span></span></span></span> when <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi><mo>=</mo><mi>p</mi></mrow><annotation encoding="application/x-tex">n = p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">n</span><span class="mrel">=</span><span class="mord mathit">p</span></span></span></span> is prime) but I don't know whether that is a good idea in Lean</p>

#### [ Johan Commelin (Nov 23 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148233793):
<p>Well, we will want <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi mathvariant="double-struck">F</mi><mi>q</mi></msub></mrow><annotation encoding="application/x-tex">\mathbb{F}_q</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.974998em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathbb">F</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.03588em;">q</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span></span></span></span> at some point... so then we will also get a <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi mathvariant="double-struck">F</mi><mi>p</mi></msub></mrow><annotation encoding="application/x-tex">\mathbb{F}_p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.974998em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathbb">F</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span></span></span></span>...</p>

#### [ Reid Barton (Nov 23 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148235984):
<p>I guess I'm not sure exactly what a "database of groups" would look like in Lean... maybe that's part of the question</p>

#### [ Kevin Buzzard (Nov 23 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148238581):
<p>What I need them for is to be able to answer questions such as "true or false: if G is abelian then G is cyclic".</p>

#### [ Scott Morrison (Nov 24 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148253284):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>, you might look at the abortive start I made on the (statement of the) classification of finite simple groups.</p>

#### [ Scott Morrison (Nov 24 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148253289):
<p>Unfortunately, even constructing the sporadics is a big project.</p>

#### [ Kevin Buzzard (Nov 24 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148267459):
<p>I think our questions are much more mundane. For example how should one define the dihedral groups? As a presentation? A subgroup of a permutation group? An explicit list of elements with a given multiplication? etc</p>

#### [ Scott Morrison (Nov 24 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148268002):
<p>Oh, I forgot to put a link, sorry. <a href="https://github.com/leanprover/mathlib/compare/master...leanprover-community:cfsg" target="_blank" title="https://github.com/leanprover/mathlib/compare/master...leanprover-community:cfsg">https://github.com/leanprover/mathlib/compare/master...leanprover-community:cfsg</a></p>

#### [ Scott Morrison (Nov 24 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148268060):
<p>I was defining things as terms of <code>Grp</code>, a bundled group. This gives you some freedom to chose different ways to define different groups. You can see some examples in that diff. For example, I did the Mathieu 12 and 24 via generators in a permutation group, M23 and M22 as stabilisers,  but the alternating group as a subtype of <code>perm (fin n)</code>.</p>

#### [ Johan Commelin (Nov 24 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148268109):
<p>It would be nice to have <code>gap_db(n,m)</code> constructor that would give you a representative of the group with <code>n</code> elements that is listed as <code>m</code>th iso-class in the GAP database.</p>

#### [ Kevin Buzzard (Nov 24 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148268154):
<p>ha ha, you could write an interface to gap which pulls off the group from the GAP database, lists all the elements, makes a new inductive type with a constructor for each object, and then just puts together the multiplication table manually and proves it's a group with dec_trivial :-)</p>

#### [ Johan Commelin (Nov 24 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148268612):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I think there might be quite some potential in such an interface...</p>

#### [ Johan Commelin (Nov 24 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148268628):
<p>I don't know if it should be an inductive type or whatever, I guess GAP can also give you generators and relations etc... Anyway, this is just wishful thinking from my side atm.</p>

#### [ Mario Carneiro (Nov 24 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148268782):
<p>we could certainly have a way to define groups by their generators and relations</p>

#### [ Mario Carneiro (Nov 24 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148268786):
<p>of course lots of questions about finitely presented groups are very hard to solve</p>

#### [ Kevin Buzzard (Nov 24 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/database%20of%20groups/near/148269104):
<p>and some are impossible to solve!</p>


{% endraw %}
