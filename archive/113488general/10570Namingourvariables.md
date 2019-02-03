---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/10570Namingourvariables.html
---

## Stream: [general](index.html)
### Topic: [Naming our variables](10570Namingourvariables.html)

---


{% raw %}
#### [ Kenny Lau (Apr 07 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124741274):
<blockquote>
<p>For consistency, please change your upper case type names to <code>α, β, γ</code> etc.</p>
</blockquote>
<p><a href="https://github.com/leanprover/mathlib/pull/89#discussion_r179398893" target="_blank" title="https://github.com/leanprover/mathlib/pull/89#discussion_r179398893">https://github.com/leanprover/mathlib/pull/89#discussion_r179398893</a></p>

#### [ Kenny Lau (Apr 07 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124741277):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> :)</p>

#### [ Kevin Buzzard (Apr 07 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124742233):
<p>I am skeptical about this approach being always the best idea. Rings are called R in mathematics, groups are called G and so on. Schemes are called S and their structure sheaves are called <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi mathvariant="script">O</mi><mi>S</mi></msub></mrow><annotation encoding="application/x-tex">\mathcal{O}_S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathcal" style="margin-right:0.02778em;">O</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.05764em;">S</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>. They're all types.</p>

#### [ Kevin Buzzard (Apr 07 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124742238):
<p>That was supposed to be a calliagraphic O</p>

#### [ Kenny Lau (Apr 07 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124742239):
<p>I triggered the right person :P</p>

#### [ Kevin Buzzard (Apr 07 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124742289):
<p>My index sets are called things like alpha, beta, because they are just random types so I stick to the conventions.</p>

#### [ Kenny Lau (Apr 07 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124742292):
<p>what happened to iota</p>

#### [ Kevin Buzzard (Apr 07 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124742297):
<p>But for readability isn't it better to have math objects called what mathematicians call them?</p>

#### [ Kevin Buzzard (Apr 07 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124742298):
<p>i.e. depends on the typeclass</p>

#### [ Simon Hudon (Apr 07 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124743335):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I'd be tempted to agree with you on groups and rings but I'm also hesitant to add any exception to style rules. The more exceptions there are, the harder they are to understand, enforce and agree to. I guess the next question is: what would be a good reason to create an exception?</p>

#### [ Simon Hudon (Apr 07 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124743443):
<p>Not answering my own question yet ... I can think of good reasons to not call type variables <code>R</code> or <code>G</code>. Being a ring or a group is not necessarily all that they are. If they conform to independent structures, which one should dictate the name?</p>

#### [ Simon Hudon (Apr 07 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124743518):
<p>I think the reason for naming them <code>R</code> or <code>G</code> is somewhat undermined by the fact that the information is already conveyed by <code>[group α]</code></p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124756586):
<p>I want to argue that mathematicians have solved these problems. I am currently writing a bunch of stuff about topological spaces and I call my topological spaces X and Y, because this is what mathematicians tend to call them, but if I had a topological ring I would call it R, because this is what mathematicians tend to call them. I would definitely never call any of them alpha.</p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124756627):
<p>Given that many mathematical objects are types, it seems like a very strange rule to demand that they're all called alpha etc. Isn't this analogous to someone saying "OK so in this code, everything that is a variable needs to be called standard variable names like x,y,z etc"? [regardless of what they're doing]</p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124756629):
<p>If we weren't using type class inference and things like groups, rings etc were their own specialised types then nobody would bat an eyelid if groups were all called G</p>

#### [ Mario Carneiro (Apr 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124756678):
<p>I think it is just like that though. For me, when writing lean code the "sort of thing" the type represents seems less important since it's not being directly associated to the notations and such like it is in math. (Instead, the typeclass parameters do all the heavy lifting here.) From what I can tell, the current convention is to use <code>G H</code> etc for <code>Group</code>s, but still to use greek letters for unbundled group-types.</p>

#### [ Mario Carneiro (Apr 07 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124756679):
<p>It's just that <code>Group</code> hasn't needed to play a big role (yet) in mathlib, so you don't see it much</p>

#### [ Kenny Lau (Apr 07 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758522):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> what will happen if I call a group alpha and a ring beta in the m1p2 test?</p>

#### [ Kenny Lau (Apr 07 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758523):
<p>I mean, alpha[beta] doesn’t look so bad as a group ring does it</p>

#### [ Kevin Buzzard (Apr 07 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758560):
<p>Just don't get me started.</p>

#### [ Kevin Buzzard (Apr 07 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758563):
<p>I'm trying to prove an affine scheme is a scheme</p>

#### [ Kevin Buzzard (Apr 07 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758564):
<p>Lean has notational irrelevance</p>

#### [ Kevin Buzzard (Apr 07 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758565):
<p>so notation is irrelevant</p>

#### [ Kenny Lau (Apr 07 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758613):
<p>it’s my PR; of course i will get you started</p>

#### [ Kenny Lau (Apr 07 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758621):
<p>let alpha be a real number... let beta be a sequence with limit to gamma</p>

#### [ Mario Carneiro (Apr 07 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758622):
<p>now <em>that's</em> a bridge too far</p>

#### [ Mario Carneiro (Apr 07 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758661):
<p>I kid, but in the lean convention only things of type <code>Type</code> are greek letters</p>

#### [ Kevin Buzzard (Apr 07 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758940):
<p>My gut instinct is to be completely happy with _restrictions_ of this form -- "we use alpha to be something of type Type so don't use it to be anything else"</p>

#### [ Kevin Buzzard (Apr 07 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758942):
<p>because mathematicians typically have more than one notation for things</p>

#### [ Kevin Buzzard (Apr 07 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758943):
<p>e.g. if you told me I couldn't use G for groups because mathlib conventions were that G was always for rings</p>

#### [ Kevin Buzzard (Apr 07 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758945):
<p>then I would just use H for groups</p>

#### [ Kevin Buzzard (Apr 07 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758948):
<p>so that sort of rule is easy to abide by</p>


{% endraw %}
