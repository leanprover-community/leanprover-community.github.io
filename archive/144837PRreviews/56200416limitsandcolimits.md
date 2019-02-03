---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/56200416limitsandcolimits.html
---

## Stream: [PR reviews](index.html)
### Topic: [#416 limits and colimits](56200416limitsandcolimits.html)

---


{% raw %}
#### [ Scott Morrison (Oct 12 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135665324):
<p>Okay, here is limits and colimits (just for general shapes, not all the useful special cases yet), with no dependency on new-fangled tactics.</p>
<p><a href="https://github.com/leanprover/mathlib/pull/416" target="_blank" title="https://github.com/leanprover/mathlib/pull/416">https://github.com/leanprover/mathlib/pull/416</a></p>

#### [ Scott Morrison (Oct 12 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135665397):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>, <span class="user-mention" data-user-id="112680">@Johan Commelin</span> hopefully this will give you the parts you need for playing with presheaves.</p>

#### [ Johan Commelin (Oct 12 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135667107):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Hurray! Thank you so much!</p>

#### [ Scott Morrison (Oct 13 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741575):
<p>I've now added all the special shapes (although equalizers and pullbacks are less developed than everything else).</p>

#### [ Scott Morrison (Oct 13 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741583):
<p>I also added instances for (co)limits in <code>Type u</code>, and appropriate simp lemmas.</p>

#### [ Scott Morrison (Oct 13 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741588):
<p>I'm happy for this to be reviewed/merged at this point, I don't have immediate plans to add more.</p>

#### [ Scott Morrison (Oct 13 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741667):
<p>A few missing bits if anyone wants to fill them in:</p>
<ul>
<li>lemmas describing how equalizers and pullbacks (and the dual notions) transform, similar to all the <code>pre</code>, <code>post</code>, and <code>map</code> lemmas in the other files</li>
<li>the final three lemmas describing how colimits behave in <code>Type u</code>. (<span class="user-mention" data-user-id="110032">@Reid Barton</span>?)</li>
</ul>

#### [ Johan Commelin (Oct 13 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741727):
<p>One thing that I noticed while working on sheaves was that Lean couldn't figure out that if a category has limits then it also has products.</p>

#### [ Johan Commelin (Oct 13 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741730):
<p>I guess this means we need to add some instances.</p>

#### [ Scott Morrison (Oct 13 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741731):
<p>Other stuff that should be done in other PRs later, and of which I have prototypes (but someone should feel free to do themselves):</p>
<ul>
<li>functors into a complete category are complete</li>
<li>all the gadgets getting between different shapes of limits (equalizers and products imply all limits, etc)</li>
<li>filtered limits, finite limits, finite products</li>
</ul>

#### [ Johan Commelin (Oct 13 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741741):
<p>But maybe "limits implies products" should also be part of other PRs?</p>

#### [ Scott Morrison (Oct 13 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741743):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> , let me see if I have that one.</p>

#### [ Scott Morrison (Oct 13 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741853):
<p>Yes, I've got it. It relies on <code>discrete_category.lean</code>, which I think never got PR'd yet.</p>

#### [ Johan Commelin (Oct 13 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741862):
<p>Ok, well it can of course wait till another PR (-;</p>

#### [ Scott Morrison (Oct 14 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759817):
<p>I have a notational problem in the (co)limits PR. At first I'd introduced </p>
<div class="codehilite"><pre><span></span>def sigma {C : Type u} [𝒞 : category.{u v} C][has_coproducts.{u v} C] {β : Type v} (f : β → C) : C
def pi {C : Type u} [𝒞 : category.{u v} C][has_products.{u v} C] {β : Type v} (f : β → C) : C
</pre></div>

#### [ Scott Morrison (Oct 14 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759832):
<p>but then realised <code>sigma</code> is a terrible idea, because it overloads the built-in sigma.</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759834):
<p><code>protected</code>?</p>

#### [ Scott Morrison (Oct 14 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759877):
<p>I thought to change <code>sigma</code> to <code>Sigma</code> and <code>pi</code> to <code>Pi</code>, but <code>Pi</code> is of course already taken for pi-types.</p>

#### [ Scott Morrison (Oct 14 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759879):
<p>Is <code>protected</code> the best solution?</p>

#### [ Scott Morrison (Oct 14 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759880):
<p>I'm a bit unclear on what happens when we use it.</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759882):
<p>it means you have to prefix the namespace</p>

#### [ Scott Morrison (Oct 14 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759890):
<p>Hmm. I guess that's okay.</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759892):
<p>there are a few examples of things in the library named <code>sigma</code> and <code>pi</code> and protected</p>

#### [ Scott Morrison (Oct 14 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759894):
<p>Ok, I'll try that.</p>

#### [ Scott Morrison (Oct 14 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759936):
<p>I better sleep, spent a long time on <span class="emoji emoji-1f6eb" title="airplane departure">:airplane_departure:</span> today.</p>

#### [ Scott Morrison (Oct 14 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759953):
<p>In other news, there's a second PR, containing the constructions limits =&gt; equalizers, limits =&gt; products, products + equalizer =&gt; limits, and functors into complete categories form a complete category, ready to go.</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135760013):
<p>By the way, in response to an earlier suggestion of inferring has_products from has_limits or something like this, I suggest that all these be regular defs, and you make them instances in particular categories</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135760020):
<p>that way you get to decide which ones imply which others</p>

#### [ Scott Morrison (Oct 14 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135788644):
<p>Great, these have just appeared as <a href="https://github.com/leanprover/mathlib/issues/420" target="_blank" title="https://github.com/leanprover/mathlib/issues/420">#420</a>.</p>

#### [ Patrick Massot (Oct 14 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135788813):
<p>Are there any examples of actual limits (in mathlib or in your repo)?</p>

#### [ Kenny Lau (Oct 14 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135788825):
<p>so how close are we to direct limits?</p>

#### [ Patrick Massot (Oct 14 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135788830):
<p>Direct limits of what?</p>

#### [ Kenny Lau (Oct 14 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135788833):
<p>rings</p>

#### [ Patrick Massot (Oct 14 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135788883):
<p>This was my question: we have abstract notion of limits and colimits, but I think there is no example yet</p>

#### [ Patrick Massot (Oct 14 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135788884):
<p>Limits in Ring would be an example</p>

#### [ Patrick Massot (Oct 14 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135788999):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> maybe you could do one example, in order to demonstrate the interface, and then we could try to have another one.</p>

#### [ Scott Morrison (Oct 14 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135789055):
<p>The examples so far are just are the (co)limits in <code>Type u</code>. <a href="https://github.com/leanprover/mathlib/pull/416/files#diff-e57d73facf90a0010edf5b1dcece8ac1" target="_blank" title="https://github.com/leanprover/mathlib/pull/416/files#diff-e57d73facf90a0010edf5b1dcece8ac1">https://github.com/leanprover/mathlib/pull/416/files#diff-e57d73facf90a0010edf5b1dcece8ac1</a></p>

#### [ Scott Morrison (Oct 14 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135789059):
<p>I'm a bit indecisive about how to do rings. We can do it directly, or we can build machinery to do it quickly. :-)</p>

#### [ Patrick Massot (Oct 14 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135789101):
<p>What would be the machinery?</p>

#### [ Scott Morrison (Oct 14 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135789305):
<p>reflective subcategories (to get from Ring to CommRing) and monadic adjunctions (to get from Type to Ring)</p>

#### [ Scott Morrison (Oct 14 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135789312):
<p>But I don't know this stuff well; I'd need to talk to Reid again to get it all straight.</p>

#### [ Scott Morrison (Oct 14 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135789324):
<p>I guess that is an indication that doing things directly on the first pass is a good idea. :-)</p>

#### [ Scott Morrison (Oct 14 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135789364):
<p>Also, my PRs don't include filtered colimits yet, so the direct limits Kenny wants require another intermediate step.</p>

#### [ Patrick Massot (Oct 14 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135789424):
<p>I'd love to get this fancy stuff, but it would probably be better to first do it by hand for rings, and then check we get the same result using fancy stuff (I mean the same usability, hopefully the abstract result should be the same anyway)</p>

#### [ Patrick Massot (Oct 14 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135789431):
<p>Maybe topological spaces are an easier target for beginners</p>

#### [ Scott Morrison (Oct 14 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135789949):
<p>Ok... I will do products for rings in a moment.</p>

#### [ Kenny Lau (Oct 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135790430):
<p>As I mentioned in another thread, the perfect closure of F can be constructed as a direct limit of a bunch of copies of F.</p>

#### [ Kenny Lau (Oct 14 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135790433):
<p>So I would really like to have direct limit. However it's fine if you don't feel like doing it.</p>

#### [ Scott Morrison (Oct 14 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135790486):
<p>No, I would like to do it (the general definition, that is). Next time I see Reid around I'm going to ask him about how to do it without too much duplication.</p>

#### [ Kenny Lau (Oct 14 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135790554):
<p>in the meantime, maybe I can revive my <a href="https://github.com/leanprover/mathlib/pull/118" target="_blank" title="https://github.com/leanprover/mathlib/pull/118">direct limit PR</a>...</p>

#### [ Kenny Lau (Oct 14 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135790703):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> would there be any problem if I do so?</p>

#### [ Patrick Massot (Oct 14 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135791871):
<p>I think it's pointless to try to do topological spaces before you do rings, there are too many definitions and notations to decipher. I started with</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_products</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="bp">+</span><span class="mi">1</span> <span class="n">u</span><span class="o">}</span> <span class="n">Top</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">prod</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span> <span class="n">f</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">X</span> <span class="o">:=</span> <span class="o">{</span><span class="n">α</span> <span class="o">:=</span> <span class="bp">Π</span> <span class="n">b</span><span class="o">,</span> <span class="n">f</span> <span class="n">b</span><span class="o">,</span> <span class="n">str</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="o">},</span>
    <span class="n">π</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">continuous_supr_dom</span> <span class="n">continuous_induced_dom</span><span class="bp">⟩</span> <span class="o">},</span>
  <span class="n">is_product</span> <span class="o">:=</span>
  <span class="k">begin</span>
    <span class="n">tidy</span><span class="o">,</span>
  <span class="kn">end</span> <span class="o">}</span><span class="bp">.</span>
</pre></div>


<p>but then I see goals like <code>is_open ((λ (a : ((s.to_shape).X).α) (b : β), (s.π b).val a) ⁻¹' s_1)</code> which is pretty hard to read</p>

#### [ Johan Commelin (Oct 15 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135797440):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> You will see something very similar if you do products of rings. The <code>to_shape</code> and the <code>s.pi ..).val</code> etc are all parts of the category theory.</p>

#### [ Scott Morrison (Oct 15 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135803776):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>, to parse that for you: <code>s_1</code> is presumably an open set. <code>s</code> is a cone (in this case called a "fan" because we're doing products, not general limits. It has a field <code>X</code>, which is the cone point. Unfortunately this is written as <code>(s.to_shape).X</code>; I wish the <code>to_shape</code> wasn't necessary; I'll investigate that further. I'd originally called <code>X</code> <code>cone_point</code>, but people's preference for brevity caused me to change it. In any case, <code>(s.to_shape).X</code> is now a <code>Top</code>, i.e. a bundled topological space. Then <code>((s.to_shape).X).α</code> is the underlying type of points of that topological space. <code>s.π b</code> is one of the projection maps of the cone, i.e. the continuous map from <code>((s.to_shape).X)</code> to <code>f b</code>. So the goal you reach is just saying: the preimage of an open set under the ... [oops, first attempt got this wrong]</p>

#### [ Scott Morrison (Oct 15 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135803885):
<p>under the product of all the projection maps (i.e. some subset of <code>\Pi b, (f b).α</code>) is open.</p>

#### [ Scott Morrison (Oct 15 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135803926):
<p>At this point we're actually going to need to look at the topology we gave on <code>Π b</code>, and see that this is true pretty much by definition, using the fact that all the <code>(s.π b).val</code> are continuous functions.</p>

#### [ Scott Morrison (Oct 15 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135803932):
<p>(assuming that's is the definition of the product topology we're using, I haven't looked)</p>

#### [ Scott Morrison (Oct 15 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135803936):
<p>If you have advice about renaming fields to make it easier to do that unpacking, please let me know!</p>

#### [ Mario Carneiro (Oct 15 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135804097):
<p>I would suggest casing a whole bunch on <code>s</code></p>

#### [ Mario Carneiro (Oct 15 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135804237):
<p>if possible</p>

#### [ Mario Carneiro (Oct 15 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135804244):
<p>I would prefer to see a theorem that assumes a topological space and some properties</p>

#### [ Scott Morrison (Oct 15 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135805031):
<p>I'll continue this in <a href="#narrow/stream/144837-PR-reviews/subject/.23422.20limits.20in.20CommRing" title="#narrow/stream/144837-PR-reviews/subject/.23422.20limits.20in.20CommRing">https://leanprover.zulipchat.com/#narrow/stream/144837-PR-reviews/subject/.23422.20limits.20in.20CommRing</a></p>

#### [ Johan Commelin (Oct 17 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135963625):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> wrote on the PR page:</p>
<blockquote>
<p>Another thing which doesn't work for me: duplication of duality.<br>
What about copying to_additive and adapting it to an duality method?</p>
</blockquote>
<p>We talked about that in Orsay. I think Mario and Scott came to the conclusion that it is a lot of hassle.</p>

#### [ Johan Commelin (Oct 17 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135963653):
<p>For example, a lot of names change.</p>


{% endraw %}
