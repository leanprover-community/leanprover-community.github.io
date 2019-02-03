---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/74041categorytheorynotations.html
---

## Stream: [maths](index.html)
### Topic: [category theory notations](74041categorytheorynotations.html)

---


{% raw %}
#### [ Scott Morrison (Apr 28 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125808846):
<p>I am very-nearly-just-about ready with my category theory PR. I would like some help with notations, however.</p>

#### [ Scott Morrison (Apr 28 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125808889):
<p>Perhaps I will write up a short document explaining my current choices, and hopefully some of the mathematicians (/computer scientists who like category theory) here can complain about them. :-)</p>

#### [ Kenny Lau (Apr 28 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125808941):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> fancy incorporating my examples?</p>

#### [ Scott Morrison (Apr 28 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125809059):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> which examples?</p>

#### [ Scott Morrison (Apr 28 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125809060):
<p>I'll look, but it may just be best to do a later PR.</p>

#### [ Scott Morrison (Apr 28 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125809097):
<p>My first category theory PR is going to be a tiny subset of the whole existing library.</p>

#### [ Kenny Lau (Apr 28 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125809100):
<blockquote>
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> which examples?</p>
</blockquote>
<p>I have many examples in my repo :P</p>

#### [ Kenny Lau (Apr 28 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125809101):
<p><a href="https://github.com/kckennylau/category-theory" target="_blank" title="https://github.com/kckennylau/category-theory">https://github.com/kckennylau/category-theory</a></p>

#### [ Scott Morrison (Apr 28 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125809359):
<p>okay --- let's wait until we have the basics in mathlib, and then we can start importing!</p>

#### [ Reid Barton (Apr 28 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125809663):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span>, I should have mentioned this earlier, but I noticed that your <code>Complete C</code> class doesn't quite correspond to the usual notion of completeness, since one ordinarily only requires the indexing category <code>J</code> for a limit to be small (w.r.t. the same universe in which the hom sets of <code>C</code> are small), but your definition further requires the hom sets of <code>J</code> to belong to an even smaller universe.</p>

#### [ Reid Barton (Apr 28 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125809669):
<p>More concretely, in a complete category one may always form the equalizer of all the morphisms between a given pair of objects, but that's not possible with the <code>Complete</code> class.</p>

#### [ Reid Barton (Apr 28 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125809788):
<p>And generally speaking it is useful to have a notion of "small category" where the objects and morphisms are sets that live in the same universe. I mention this because one possible way to address this (though maybe not the best way) would be to add a second universe parameter to the <code>category</code> class, which would probably involve many other changes.</p>

#### [ Reid Barton (Apr 28 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125810026):
<p>Another option might be to define a small category as a category with object type of the form <code>ulift.{i (i+1)} a</code></p>

#### [ Scott Morrison (Apr 28 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125810972):
<p>(deleted)</p>

#### [ Scott Morrison (Apr 28 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125810978):
<p>(deleted)</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817480):
<p>It seems to me that doing category theory in Lean brings up some extremely delicate issues.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817520):
<p>I am an end user and I do not care about universes or these subtleties, at least when I have my algebraic geometry hat on</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817523):
<p>I just want to write down a functor from "the" category of open sets on a topological space to "the" category of groups, without caring at all about which universe all these things live in.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817572):
<p>On the other hand, I have seen intelligent people occasionally pausing to say "by the way, when I say category of _all_ schemes, it might be best if you interpret this as the category of all schemes which show up at some level in a set-theoretical hierarchy, and here is a calculation indicating that certain basic operations will never take us out of that category"</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817619):
<p>Here, for example, is Johan de Jong being very careful about what he means by the category of schemes, as formalised within ZFC.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817620):
<p><a href="https://stacks.math.columbia.edu/tag/000H" target="_blank" title="https://stacks.math.columbia.edu/tag/000H">https://stacks.math.columbia.edu/tag/000H</a></p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817627):
<p>It seems to me that when you are doing calculations such as these, you are making a <em>promise</em> to your reader.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817674):
<p>You are saying "isn't maths great, look at all the things we can do. Here is one thing we can do which is quite sensible -- we can sometimes take certain limits of schemes. And look, if my schemes are all "small" and the diagram is "small" then the limit of the diagram is "small" too."</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817677):
<p>And now you make the promise that throughout the 6000 pages which are about to follow</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817680):
<p>you promise you don't do anything pathological</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817681):
<p>which forces a universe change</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817682):
<p>Now that is a really big promise.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817714):
<p>But some mathematicians are absolutely alive to that promise.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817728):
<p>and it's those kinds of mathematicians, like Brian Conrad, who, when you mention the fpqc topology on a scheme, points out that in that situation you have not kept your promise.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817730):
<p>because an arbitrary map between fields is quasi-compact</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817736):
<p>and there are a lot of fields</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817743):
<p>What I am pretty convinced about is that one day in the future when we have formalised schemes, and their etale cohomology, their fppf cohomology and their fpqc cohomology</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817792):
<p>then at some point there will be an issue with fpqc</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817797):
<p>which will manifest itself in some constructions having to be worked out slightly differently</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817798):
<p>because of universe issues</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817799):
<p>I believe that mathematicians hide that thought away</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817805):
<p>because it hopefully doesn't affect anything they do</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817843):
<p>Scott -- if you could just give me some working definition of a category and a site and a topos</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817846):
<p>then there is nothing stopping people from formalising definitions of these fancy cohomology theories in Lean</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817847):
<p>Proving anything non-trivial about these fancy cohomology theories would almost certainly be extemely difficult</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817848):
<p>however _defining_ them is another kettle of fish</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817855):
<p>I defined schemes over a month ago and am still yet to produce a single example because I have been caught up in notions of canonical isomorphism</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817856):
<p>but the definition is there</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817861):
<p>So let me know when you want to define some fancy cohomology theories on the category of schemes</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817863):
<p>and not prove anything about them</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817903):
<p>because this would be an extremely good stress test for your category theory library</p>

#### [ Kevin Buzzard (Apr 28 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817905):
<p>and I believe it is within reach</p>


{% endraw %}
