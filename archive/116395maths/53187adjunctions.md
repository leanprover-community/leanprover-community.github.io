---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/53187adjunctions.html
---

## Stream: [maths](index.html)
### Topic: [adjunctions](53187adjunctions.html)

---


{% raw %}
#### [ Johan Commelin (Nov 07 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146960106):
<p>I feel like it is time we get adjoint functors. We now have <code>map</code> and <code>comap</code> for over-categories. They form an adjoint pair, and this would allow us to prove useful stuff. Has anyone given thought to implementing adjunctions in Lean? Are there any traps that should be avoided?</p>

#### [ Kenny Lau (Nov 07 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146964831):
<p>and then refactor galois connection :p</p>

#### [ Johan Commelin (Nov 07 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146964958):
<p>Right. Are you interested in taking a look at the bottom of <code>sheaf.lean</code> on the <code>sheaf</code> branch? It is getting a big mess. As soon as we want to apply category theory to concrete stuff thing become rather unpleasant...</p>

#### [ Patrick Massot (Nov 07 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146965246):
<p>I don't like reading "As soon as we want to apply category theory to concrete stuff thing become rather unpleasant..." <span class="emoji emoji-2639" title="sad">:sad:</span></p>

#### [ Johan Commelin (Nov 07 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146965311):
<p>I agree... and it is probably just that I'm not skilled enough in Lean.</p>

#### [ Johan Commelin (Nov 07 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146967027):
<p>It feels like <code>category_theory</code> is a monad: You can bind yourself into it. But you really shouldn't try to crawl out of it.</p>

#### [ Johan Commelin (Nov 07 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146967111):
<p>I think it is hopeless that we will be able to rewrite along equivalences of categories, right?</p>

#### [ Johan Commelin (Nov 07 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146967150):
<p>If <code>X</code> is a topological space, and <code>U</code> is an open subset of <code>X</code>, then <code>over U</code> is canonically equivalent to <code>opens U</code>. Is there any hope at all that I can teach Lean how to use this fact?</p>

#### [ Johan Commelin (Nov 07 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146967222):
<p>(Without 100 lines of scaffolding to show that I can transfer everything I want along my canonical equivalence.)</p>

#### [ Johan Commelin (Nov 07 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146967920):
<p>In this case it is even an isomorphism of categories. I'm not sure if that helps.</p>

#### [ Kevin Buzzard (Nov 07 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146970541):
<blockquote>
<p>I think it is hopeless that we will be able to rewrite along equivalences of categories, right?</p>
</blockquote>
<p>rofl how about we rewrite along isomorphisms of groups first!</p>

#### [ Scott Morrison (Nov 07 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147252668):
<p><span class="emoji emoji-2b06" title="up">:up:</span></p>

#### [ Reid Barton (Nov 08 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147322759):
<blockquote>
<p>I feel like it is time we get adjoint functors. We now have <code>map</code> and <code>comap</code> for over-categories. They form an adjoint pair, and this would allow us to prove useful stuff. Has anyone given thought to implementing adjunctions in Lean? Are there any traps that should be avoided?</p>
</blockquote>
<p>I have defined adjunctions a couple of times, including at <a href="https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/category_theory/adjunctions.lean" target="_blank" title="https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/category_theory/adjunctions.lean">https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/category_theory/adjunctions.lean</a> (see also <a href="https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/category_theory/preserves_colimits.lean" target="_blank" title="https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/category_theory/preserves_colimits.lean">https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/category_theory/preserves_colimits.lean</a>). But I haven't needed to push the theory very far yet, so I'm not sure about traps.</p>

#### [ Reid Barton (Nov 08 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147322876):
<p>One thing which is a bit annoying is to state the naturality of the isomorphism Hom(FX, Y) = Hom(X, GY) for an adjunction F : C -&gt; D, G : D -&gt; C.<br>
If C and D have different morphism universes then where is this isomorphism happening...?</p>

#### [ Johan Commelin (Nov 08 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147328898):
<p>Probably in <code>max v_1 v_2</code>...</p>

#### [ Johan Commelin (Nov 08 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147328931):
<p>Maybe we can have an <code>adjunctions</code> branch where you push your stuff and we (Scott, you, me, maybe others) can play around with it till we think something is ready for merging.</p>

#### [ Johan Commelin (Nov 08 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147328996):
<p>For example, we could then merge that branch into the <code>sheaf</code> branch, and stress test it on that example.</p>

#### [ Scott Morrison (Nov 08 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147333368):
<p>When I've played with adjunctions I've settled on just putting everything in the same universe level.</p>

#### [ Scott Morrison (Nov 08 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147333380):
<p>Would this make us sad?</p>

#### [ Reid Barton (Nov 08 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147335341):
<p>I'm not sure. It might be fine, especially if we have a good interface for lifting a category to a bigger universe.</p>

#### [ Kevin Buzzard (Nov 09 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147356768):
<p>I know that the philosophy is to be maximally universe polymorphic. But when I wrote schemes originally I spent almost my entire time working in one universe, just to see what happened, and I never ran into any problems (other than Mario telling me I should stop -- I mean I didn't run into any mathematical problems). Reading SGA the other day I see that Grothendieck also was happy with just one universe for a lot of the time. If being maximally universe polymorphic is causing problems then I might venture to suggest that being maximally universe polymorphic might simply not be that good an idea when working with categories.</p>

#### [ Johan Commelin (Nov 09 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147357592):
<p>I do think that a lot of our universe annotations could then go away. And the errors related to universe issues are also quite nasty and annoying. I agree with <span class="user-mention" data-user-id="110032">@Reid Barton</span> that we would need a good way to turn lift a category to a higher universe, and I have no idea how hard this is.<br>
<span class="user-mention" data-user-id="110087">@Scott Morrison</span> What do you think? How much of the universe issues are maths-problems, and how much of it is just <em>users fighting Lean</em>?</p>

#### [ Scott Morrison (Nov 10 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147411657):
<p>I don't think we've had any universe problem in a long while in the category_theory development. I think the current setup, where you often have to say <code>XXX.{u v}</code>, so Lean knows which morphism universe level you intend, is mildly annoying. The current setup is a minimal envelope around supporting <code>category.{v v}</code> and <code>category.{v+1 v}</code>, which is all that ever turns up in practice. Any time more than one category is involved, and there is a potential problem with mismatching universe levels, my instinct is to put everything at the same universe level. (i.e., just like Grothendieck, we work in a single universe, called <code>v</code>, except that we also have <code>u</code>, which we think of as either being <code>v</code> or <code>v+1</code> for small or large categories).</p>

#### [ Scott Morrison (Nov 10 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147411706):
<p>If that ever causes problems, then we'll announce we've learnt something, and deal with it, but for now I see no need to deal with mixed-universe level adjunctions, etc.</p>

#### [ Kevin Buzzard (Nov 10 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147411924):
<p>I guess Grothendieck fixed one universe u, and then talked about u-categories and u-small categories, which are these two cases.</p>

#### [ Scott Morrison (Nov 10 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147412697):
<p>We would suffer quite a bit by specialising to only u-categories and u-small categories, because we'd have to duplicate lots of theorems. Having <code>category.{u v}</code> lets us state theorems in both cases uniformly with not-that-much suffering, and we just remember that all the other values of <code>u</code> are not particularly relevant.</p>

#### [ Kevin Buzzard (Nov 10 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147425039):
<p>Yes, I'm now starting to understand the philosophy much better</p>

#### [ Reid Barton (Nov 12 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147503855):
<p>Status update on adjunctions: I managed to get as far as proving that right adjoints preserve limits and that any functor C -&gt; D with C small and D cocomplete induces an adjunction (like the geometric realization/Sing adjunction).</p>

#### [ Reid Barton (Nov 12 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147503862):
<p>The code still needs some cleaning up, but I'll try to push it to community tomorrow</p>

#### [ Johan Commelin (Nov 12 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147509015):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> That sounds fantastic! I'm looking forward to seeing the code.</p>

#### [ Reid Barton (Nov 12 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147548648):
<p><a href="https://github.com/leanprover-community/mathlib/tree/adjunctions" target="_blank" title="https://github.com/leanprover-community/mathlib/tree/adjunctions">https://github.com/leanprover-community/mathlib/tree/adjunctions</a></p>

#### [ Johan Commelin (Nov 12 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147548937):
<p>Cool!</p>

#### [ Reid Barton (Nov 12 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147549367):
<p>I'm still not sure about the best way to deal with natural isomorphisms. Sometimes I want to compose natural isomorphisms together, in which case I want to view the isomorphism and its naturality as a single object, but often I also want to just work objectwise, and check naturality as needed later</p>

#### [ Reid Barton (Nov 12 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147549474):
<p>I'm looking at this proof on paper: "<span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="normal">H</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">m</mi></mrow><mo>(</mo><mover accent="true"><mi>F</mi><mo>~</mo></mover><mo>(</mo><mi>y</mi><mi>c</mi><mo>)</mo><mo separator="true">,</mo><mi>d</mi><mo>)</mo><mo>=</mo><mrow><mi mathvariant="normal">H</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">m</mi></mrow><mo>(</mo><mi>y</mi><mi>c</mi><mo separator="true">,</mo><msup><mi>F</mi><mo>∗</mo></msup><mi>d</mi><mo>)</mo><mo>=</mo><msup><mi>F</mi><mo>∗</mo></msup><mi>d</mi><mo>(</mo><mi>c</mi><mo>)</mo><mo>=</mo><mrow><mi mathvariant="normal">H</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">m</mi></mrow><mo>(</mo><mi>F</mi><mi>c</mi><mo separator="true">,</mo><mi>d</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\mathrm{Hom}(\tilde F (y c), d) = \mathrm{Hom}(y c, F^* d) = F^* d(c) = \mathrm{Hom}(F c, d)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.9201899999999998em;"></span><span class="strut bottom" style="height:1.1701899999999998em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathrm">H</span><span class="mord mathrm">o</span><span class="mord mathrm">m</span></span><span class="mopen">(</span><span class="mord accent"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.9201899999999998em;"><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="mord mathit" style="margin-right:0.13889em;">F</span></span><span style="top:-3.6023300000000003em;"><span class="pstrut" style="height:3em;"></span><span class="accent-body" style="margin-left:0.16668em;"><span>~</span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mord mathit">c</span><span class="mclose">)</span><span class="mpunct">,</span><span class="mord mathit">d</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord"><span class="mord mathrm">H</span><span class="mord mathrm">o</span><span class="mord mathrm">m</span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mord mathit">c</span><span class="mpunct">,</span><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.688696em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mbin mtight">∗</span></span></span></span></span></span></span></span><span class="mord mathit">d</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.688696em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mbin mtight">∗</span></span></span></span></span></span></span></span><span class="mord mathit">d</span><span class="mopen">(</span><span class="mord mathit">c</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord"><span class="mord mathrm">H</span><span class="mord mathrm">o</span><span class="mord mathrm">m</span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mord mathit">c</span><span class="mpunct">,</span><span class="mord mathit">d</span><span class="mclose">)</span></span></span></span> and so there is a natural isomorphism <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>F</mi><mi>c</mi><mo>→</mo><mover accent="true"><mi>F</mi><mo>~</mo></mover><mo>(</mo><mi>y</mi><mi>c</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">F c \to \tilde F (y c)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.9201899999999998em;"></span><span class="strut bottom" style="height:1.1701899999999998em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mord mathit">c</span><span class="mrel">→</span><span class="mord accent"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.9201899999999998em;"><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="mord mathit" style="margin-right:0.13889em;">F</span></span><span style="top:-3.6023300000000003em;"><span class="pstrut" style="height:3em;"></span><span class="accent-body" style="margin-left:0.16668em;"><span>~</span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mord mathit">c</span><span class="mclose">)</span></span></span></span>"</p>

#### [ Reid Barton (Nov 12 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147549477):
<p>and trying to figure out how to explain it to Lean</p>

#### [ Johan Commelin (Nov 12 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147549682):
<p><code>apply yoneda_lemma; obviously</code> ??? <span class="emoji emoji-1f606" title="lol">:lol:</span></p>

#### [ Reid Barton (Nov 12 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147553765):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I left a bit of a mess in <code>limits.lean</code> regarding <code>is_limit.equiv</code>/<code>is_limit.of_equiv</code> and the colimit versions. I found it's often easier to just work with the <code>equiv</code> type, rather than <code>iso</code> and especially <code>iso</code> between natural transformations. In particular, <code>is_limit.of_equiv</code> is nontrivially (at least in Lean) harder to use than <code>is_colimit.of_equiv</code>--for <code>is_limit.of_equiv</code> you have to produce an inverse as a natural transformation, while the fact that it's natural is actually automatic.</p>

#### [ Reid Barton (Nov 12 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147553773):
<p>This should get sorted out somehow--maybe having both <code>equiv</code> and <code>iso</code> versions</p>

#### [ Scott Morrison (Nov 12 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147554813):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>, isn't this what <code>nat_iso.of_components</code> is for?</p>

#### [ Scott Morrison (Nov 12 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147554871):
<p>You specify an iso in each component, and check naturality in just one direction.</p>

#### [ Scott Morrison (Nov 12 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147554885):
<p>Perhaps there should be a companion that let's you check naturality in the other direction instead.</p>

#### [ Reid Barton (Nov 12 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147554886):
<p>oh, I didn't see that</p>

#### [ Scott Morrison (Nov 12 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147554900):
<p>Sorry, I really should write some docs. :-(</p>

#### [ Reid Barton (Nov 12 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147554902):
<p>but anyways, I shouldn't need to check naturality in either direction</p>

#### [ Scott Morrison (Nov 12 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147554907):
<p>Ah, why is that?</p>

#### [ Reid Barton (Nov 12 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147554951):
<p>Well, because... I actually want to use something like <code>is_limit.of_extensions_iso</code></p>

#### [ Reid Barton (Nov 12 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147554969):
<p>but <code>nat_iso.of_components</code> doesn't produce an <code>is_iso</code></p>

#### [ Reid Barton (Nov 12 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555016):
<p>The point is just that the thing which is supposed to be <code>is_iso</code> is already known to be natural</p>

#### [ Scott Morrison (Nov 12 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555021):
<p>ah!</p>

#### [ Scott Morrison (Nov 12 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555026):
<p>okay, sorry, I missed that</p>

#### [ Scott Morrison (Nov 12 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555051):
<p>so we need is_iso.of_nat_trans, which takes an input an <code>F \natt G</code>,  and and is_iso for each component?</p>

#### [ Scott Morrison (Nov 12 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555185):
<p>Regarding your</p>
<blockquote>
<p>I'm looking at this proof on paper: "<span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="normal">H</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">m</mi></mrow><mo>(</mo><mover accent="true"><mi>F</mi><mo>~</mo></mover><mo>(</mo><mi>y</mi><mi>c</mi><mo>)</mo><mo separator="true">,</mo><mi>d</mi><mo>)</mo><mo>=</mo><mrow><mi mathvariant="normal">H</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">m</mi></mrow><mo>(</mo><mi>y</mi><mi>c</mi><mo separator="true">,</mo><msup><mi>F</mi><mo>∗</mo></msup><mi>d</mi><mo>)</mo><mo>=</mo><msup><mi>F</mi><mo>∗</mo></msup><mi>d</mi><mo>(</mo><mi>c</mi><mo>)</mo><mo>=</mo><mrow><mi mathvariant="normal">H</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">m</mi></mrow><mo>(</mo><mi>F</mi><mi>c</mi><mo separator="true">,</mo><mi>d</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\mathrm{Hom}(\tilde F (y c), d) = \mathrm{Hom}(y c, F^* d) = F^* d(c) = \mathrm{Hom}(F c, d)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.9201899999999998em;"></span><span class="strut bottom" style="height:1.1701899999999998em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathrm">H</span><span class="mord mathrm">o</span><span class="mord mathrm">m</span></span><span class="mopen">(</span><span class="mord accent"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.9201899999999998em;"><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="mord mathit" style="margin-right:0.13889em;">F</span></span><span style="top:-3.6023300000000003em;"><span class="pstrut" style="height:3em;"></span><span class="accent-body" style="margin-left:0.16668em;"><span>~</span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mord mathit">c</span><span class="mclose">)</span><span class="mpunct">,</span><span class="mord mathit">d</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord"><span class="mord mathrm">H</span><span class="mord mathrm">o</span><span class="mord mathrm">m</span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mord mathit">c</span><span class="mpunct">,</span><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.688696em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mbin mtight">∗</span></span></span></span></span></span></span></span><span class="mord mathit">d</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.688696em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mbin mtight">∗</span></span></span></span></span></span></span></span><span class="mord mathit">d</span><span class="mopen">(</span><span class="mord mathit">c</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord"><span class="mord mathrm">H</span><span class="mord mathrm">o</span><span class="mord mathrm">m</span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mord mathit">c</span><span class="mpunct">,</span><span class="mord mathit">d</span><span class="mclose">)</span></span></span></span> and so there is a natural isomorphism <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>F</mi><mi>c</mi><mo>→</mo><mover accent="true"><mi>F</mi><mo>~</mo></mover><mo>(</mo><mi>y</mi><mi>c</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">F c \to \tilde F (y c)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.9201899999999998em;"></span><span class="strut bottom" style="height:1.1701899999999998em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mord mathit">c</span><span class="mrel">→</span><span class="mord accent"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.9201899999999998em;"><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="mord mathit" style="margin-right:0.13889em;">F</span></span><span style="top:-3.6023300000000003em;"><span class="pstrut" style="height:3em;"></span><span class="accent-body" style="margin-left:0.16668em;"><span>~</span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mord mathit">c</span><span class="mclose">)</span></span></span></span>"</p>
</blockquote>
<p>It seems we'd want to write:</p>
<div class="codehilite"><pre><span></span>apply nat_iso.of_components, -- giving us two goals; an iso in each component, and naturality of the forward direction,
{ intro X,
  apply yoneda.ext,
  &lt;&lt;&lt;calc block goes here, doing the Hom set calculation&gt;&gt;&gt; },
obviously -- to deal with naturality
</pre></div>

#### [ Scott Morrison (Nov 12 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555241):
<p>I think a calc block should work fine with a string of isos.</p>

#### [ Scott Morrison (Nov 12 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555247):
<p>Because there compositions of isos is marked with <code>[trans]</code>.</p>

#### [ Reid Barton (Nov 12 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555262):
<p>There are actually two naturalities(?) involved: in c and in d</p>

#### [ Reid Barton (Nov 12 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555280):
<p>One of them gets consumed by <code>yoneda.ext</code>, the other to show the resulting transformation is natural in <code>c</code></p>

#### [ Scott Morrison (Nov 12 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555303):
<p>oh, of course</p>

#### [ Scott Morrison (Nov 12 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555361):
<p>so after the <code>calc</code> block we'd have another <code>obviously</code> to discharge the naturality goal that <code>yoneda.ext</code> creates?</p>

#### [ Scott Morrison (Nov 12 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555382):
<p>I guess <code>yoneda.ext</code> and <code>nat_iso.of_components</code> could both have <code>obviously</code> as an autoparam...</p>

#### [ Reid Barton (Nov 12 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555473):
<p>Gotta run for a bit <span class="emoji emoji-1f3c3" title="running">:running:</span></p>

#### [ Scott Morrison (Nov 12 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555483):
<p>but that probably makes no sense; auto_param in a open argument of an applied function isn't going to help, because it should run until later...</p>

#### [ Reid Barton (Nov 13 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147566939):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> We need that Globular integration already <a href="https://github.com/leanprover-community/mathlib/blob/adjunctions/category_theory/adjunction.lean#L156" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/adjunctions/category_theory/adjunction.lean#L156">https://github.com/leanprover-community/mathlib/blob/adjunctions/category_theory/adjunction.lean#L156</a></p>

#### [ Scott Morrison (Nov 13 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147568567):
<p>Yeah, I was wishing for globular yesterday as well. I ended up writing a page long rewrite proof, corresponding to a commutative diagram built out of two hexagons and two squares (but interminable rewriting along category.assoc to actually use it), corresponding to a string diagram in which you just had to pull some cups and caps past each other. (This was for composition of monoidal functors.)</p>

#### [ Reid Barton (Nov 15 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147715738):
<p>I can't believe this resulted in a statement I could actually prove</p>
<div class="codehilite"><pre><span></span>    <span class="n">dsimp</span> <span class="o">[</span><span class="n">canonical_diagram</span><span class="bp">.</span><span class="n">cocone</span><span class="o">,</span> <span class="n">canonical_diagram</span><span class="bp">.</span><span class="n">to_original</span><span class="o">,</span> <span class="n">canonical_diagram</span><span class="o">,</span>
      <span class="n">canonical_diagram</span><span class="bp">.</span><span class="n">colimit_cocone</span><span class="o">,</span> <span class="n">id_iso_yoneda_extension_yoneda</span><span class="o">,</span>
      <span class="n">adjunction</span><span class="bp">.</span><span class="n">nat_iso_equiv</span><span class="o">,</span> <span class="n">adjunction</span><span class="bp">.</span><span class="n">nat_trans_equiv</span><span class="o">,</span>
      <span class="n">equiv</span><span class="bp">.</span><span class="n">refl</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">trans</span><span class="o">,</span> <span class="n">iso</span><span class="bp">.</span><span class="n">hom_equiv_of_isos</span><span class="o">,</span>
      <span class="n">adjunction</span><span class="bp">.</span><span class="n">mate</span><span class="o">,</span> <span class="n">adjunction</span><span class="bp">.</span><span class="n">nat_equiv</span><span class="o">,</span> <span class="n">adjunction</span><span class="bp">.</span><span class="n">nat_equiv&#39;</span><span class="o">,</span>
      <span class="n">adjunction</span><span class="bp">.</span><span class="n">hom_equiv</span><span class="o">,</span> <span class="n">adjunction</span><span class="bp">.</span><span class="n">id</span><span class="o">,</span> <span class="n">adjunction</span><span class="bp">.</span><span class="n">adjunction_of_equiv_left</span><span class="o">,</span>
      <span class="n">adjunction</span><span class="bp">.</span><span class="n">adjunction_of_equiv</span><span class="o">,</span> <span class="n">adjunction</span><span class="bp">.</span><span class="n">left_adjoint_of_equiv</span><span class="o">,</span>
      <span class="n">yoneda_extension_adj</span><span class="o">,</span> <span class="n">yoneda_extension_e</span><span class="o">,</span>
      <span class="n">equiv</span><span class="bp">.</span><span class="n">subtype_equiv_subtype</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">subtype_equiv_of_subtype</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">Pi_congr_right</span><span class="o">,</span>
      <span class="n">equiv</span><span class="bp">.</span><span class="n">arrow_congr</span><span class="o">,</span>
      <span class="n">is_colimit</span><span class="bp">.</span><span class="n">equiv</span><span class="o">,</span>
      <span class="n">restricted_yoneda</span><span class="o">,</span> <span class="n">yoneda_extension</span><span class="o">,</span> <span class="n">yoneda_extension_obj</span><span class="o">,</span>
      <span class="n">restricted_yoneda_yoneda_iso_id</span><span class="o">,</span>
      <span class="n">nat_iso</span><span class="bp">.</span><span class="n">of_components</span><span class="o">,</span> <span class="n">iso_of_equiv</span><span class="o">,</span> <span class="n">yoneda_equiv</span><span class="o">],</span>
</pre></div>

#### [ Kevin Buzzard (Nov 15 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147715886):
<p>I look at that and I can see why category theory has a reputation in some quarters of just being a bunch of trivialities...</p>

#### [ Scott Morrison (Nov 15 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147716433):
<p>Sounds like more rfl lemmas were needed.</p>

#### [ Reid Barton (Nov 17 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147853440):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> did you do a second force push to the adjunctions branch, or am I imagining things?</p>

#### [ Scott Morrison (Nov 17 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147853442):
<p>Oh, maybe I did. Sorry, did I mess things up? :-(</p>

#### [ Reid Barton (Nov 17 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147853526):
<p>No not really, but give me a heads up if you do a force push in the future, as it's easier to deal with if I know about it earlier</p>

#### [ Reid Barton (Nov 17 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147853596):
<p>I managed to prove that the category of colimit-preserving functors Set^C^op -&gt; D is equivalent to the category of functors C -&gt; D</p>

#### [ Reid Barton (Nov 17 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147853606):
<p>for D cocomplete of course</p>

#### [ Reid Barton (Nov 17 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147853610):
<p>though I'm not particularly happy with the proof yet</p>

#### [ Reid Barton (Nov 17 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147853633):
<p>It turns out there are a lot of statements to check there...</p>

#### [ Reid Barton (Nov 17 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147853740):
<p>I guess I also proved the "adjoint functor theorem" for such functors, along the way</p>

#### [ Johan Commelin (Nov 26 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/148386153):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Shouldn't the <code>left_triangle</code> and <code>right_triangle</code> fields in adjunction get <code>obviously</code> auto_param? (I can testify that <code>obviously</code> will prove them in the case of <code>comap f</code> and <code>map f</code> between <code>presheaf X</code> and <code>presheaf Y</code>.</p>

#### [ Johan Commelin (Nov 26 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/148386577):
<p>This is really slick:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">adj</span> <span class="o">:</span> <span class="n">adjunction</span> <span class="o">(</span><span class="n">comap</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">map</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">unit</span>   <span class="o">:=</span> <span class="n">unit</span> <span class="n">f</span><span class="o">,</span>
  <span class="n">counit</span> <span class="o">:=</span> <span class="n">counit</span> <span class="n">f</span><span class="o">,</span>
  <span class="n">left_triangle</span>  <span class="o">:=</span> <span class="k">by</span> <span class="n">tidy</span><span class="o">,</span>
  <span class="n">right_triangle</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">tidy</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="n">comap</span><span class="bp">.</span><span class="n">preserves_colimits</span> <span class="o">:</span> <span class="n">preserves_colimits</span> <span class="o">(</span><span class="n">comap</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">adjunction</span><span class="bp">.</span><span class="n">left_adjoint_preserves_colimits</span> <span class="o">(</span><span class="n">adj</span> <span class="n">f</span><span class="o">)</span>
</pre></div>

#### [ Reid Barton (Nov 26 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/148386603):
<p>I suppose, though I think that defining adjunctions in terms of the unit and counit was actually the wrong idea in the first place</p>

#### [ Johan Commelin (Nov 26 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/148389931):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>  Does that mean that I shouldn't try to apply this on my sheaf branch?</p>

#### [ Reid Barton (Nov 26 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/148394873):
<p>Using the adjunctions branch as-is should be fine for now--I don't expect you will need to make major changes later. And more users of the code is good for trying out different designs.</p>

#### [ Johan Commelin (Jan 17 2019 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/155331480):
<p>I've been experimenting a bit with adjunctions. Here is a little teaser:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">discrete</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="err">⥤</span> <span class="n">Top</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">obj</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">X</span><span class="o">,</span> <span class="err">⊤</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">map</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span> <span class="n">Y</span> <span class="n">f</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">f</span><span class="o">,</span> <span class="n">continuous_top</span><span class="bp">⟩</span> <span class="o">}</span>

<span class="n">def</span> <span class="n">trivial</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="err">⥤</span> <span class="n">Top</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">obj</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">X</span><span class="o">,</span> <span class="err">⊥</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">map</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span> <span class="n">Y</span> <span class="n">f</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">f</span><span class="o">,</span> <span class="n">continuous_bot</span><span class="bp">⟩</span> <span class="o">}</span>

<span class="n">def</span> <span class="n">adj₁</span> <span class="o">:</span> <span class="n">adjunction</span> <span class="n">discrete</span> <span class="n">forget</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">hom_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span> <span class="n">Y</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">to_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">f</span><span class="o">,</span>
    <span class="n">inv_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">f</span><span class="o">,</span> <span class="n">continuous_top</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">left_inv</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">tidy</span><span class="o">,</span>
    <span class="n">right_inv</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">tidy</span> <span class="o">},</span>
  <span class="n">unit</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">app</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span><span class="o">,</span> <span class="n">id</span> <span class="o">},</span>
  <span class="n">counit</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">app</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">id</span><span class="o">,</span> <span class="n">continuous_top</span><span class="bp">⟩</span> <span class="o">}</span> <span class="o">}</span>

<span class="n">def</span> <span class="n">adj₂</span> <span class="o">:</span> <span class="n">adjunction</span> <span class="n">forget</span> <span class="n">trivial</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">hom_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span> <span class="n">Y</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">to_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">f</span><span class="o">,</span> <span class="n">continuous_bot</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">inv_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">f</span><span class="o">,</span>
    <span class="n">left_inv</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">tidy</span><span class="o">,</span>
    <span class="n">right_inv</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">tidy</span> <span class="o">},</span>
  <span class="n">unit</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">app</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">id</span><span class="o">,</span> <span class="n">continuous_bot</span><span class="bp">⟩</span> <span class="o">},</span>
  <span class="n">counit</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">app</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span><span class="o">,</span> <span class="n">id</span> <span class="o">}</span> <span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Jan 17 2019 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/155331490):
<p>Code can be found on the <code>adjunctions-2</code> branch.</p>

#### [ Johan Commelin (Jan 17 2019 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/155331619):
<p>Observations made by Reid:</p>
<ul>
<li>It is nice if we can have adjunctions between functors <code>F : C =&gt; D</code> and <code>G : D =&gt; C</code> where <code>C</code> and <code>D</code> don't need to live in the same universe.</li>
<li>We should learn from the <code>metric_space</code> hierarchy, and add redundant data in our definitions, with conditions that they are compatible.</li>
</ul>

#### [ Johan Commelin (Jan 17 2019 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/155331719):
<p>So now there are 3 ways to define an adjunction (with the help of <code>obviously</code> <span class="emoji emoji-1f603" title="smiley">:smiley:</span>).<br>
 1. Like I did above: you specify <code>hom_equiv</code>, <code>unit</code> and <code>counit</code>.<br>
 2. You only give <code>hom_equiv</code>.<br>
 3. You only give <code>unit</code> and <code>counit</code>.<br>
Here are two helper structures:</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">adjunction</span><span class="bp">.</span><span class="n">core_hom_equiv</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">C</span> <span class="err">⥤</span> <span class="n">D</span><span class="o">)</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="n">D</span> <span class="err">⥤</span> <span class="n">C</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">hom_equiv</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span><span class="o">),</span> <span class="o">(</span><span class="n">F</span><span class="bp">.</span><span class="n">obj</span> <span class="n">X</span> <span class="err">⟶</span> <span class="n">Y</span><span class="o">)</span> <span class="err">≃</span> <span class="o">(</span><span class="n">X</span> <span class="err">⟶</span> <span class="n">G</span><span class="bp">.</span><span class="n">obj</span> <span class="n">Y</span><span class="o">))</span>
<span class="o">(</span><span class="n">hom_equiv_naturality_left&#39;</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">X&#39;</span> <span class="n">X</span> <span class="n">Y</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X&#39;</span> <span class="err">⟶</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">F</span><span class="bp">.</span><span class="n">obj</span> <span class="n">X</span> <span class="err">⟶</span> <span class="n">Y</span><span class="o">),</span>
  <span class="o">(</span><span class="n">hom_equiv</span> <span class="n">X&#39;</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span> <span class="err">≫</span> <span class="n">g</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="err">≫</span> <span class="o">(</span><span class="n">hom_equiv</span> <span class="n">X</span> <span class="n">Y</span><span class="o">)</span> <span class="n">g</span> <span class="bp">.</span> <span class="n">obviously</span><span class="o">)</span>
<span class="o">(</span><span class="n">hom_equiv_naturality_right&#39;</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="n">Y&#39;</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">F</span><span class="bp">.</span><span class="n">obj</span> <span class="n">X</span> <span class="err">⟶</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">Y</span> <span class="err">⟶</span> <span class="n">Y&#39;</span><span class="o">),</span>
  <span class="o">(</span><span class="n">hom_equiv</span> <span class="n">X</span> <span class="n">Y&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="err">≫</span> <span class="n">g</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">hom_equiv</span> <span class="n">X</span> <span class="n">Y</span><span class="o">)</span> <span class="n">f</span> <span class="err">≫</span> <span class="n">G</span><span class="bp">.</span><span class="n">map</span> <span class="n">g</span> <span class="bp">.</span> <span class="n">obviously</span><span class="o">)</span>
</pre></div>


<p>and</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">adjunction</span><span class="bp">.</span><span class="n">core_unit_counit</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">C</span> <span class="err">⥤</span> <span class="n">D</span><span class="o">)</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="n">D</span> <span class="err">⥤</span> <span class="n">C</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">unit</span> <span class="o">:</span> <span class="n">functor</span><span class="bp">.</span><span class="n">id</span> <span class="n">C</span> <span class="err">⟹</span> <span class="n">F</span><span class="bp">.</span><span class="n">comp</span> <span class="n">G</span><span class="o">)</span>
<span class="o">(</span><span class="n">counit</span> <span class="o">:</span> <span class="n">G</span><span class="bp">.</span><span class="n">comp</span> <span class="n">F</span> <span class="err">⟹</span> <span class="n">functor</span><span class="bp">.</span><span class="n">id</span> <span class="n">D</span><span class="o">)</span>
<span class="o">(</span><span class="n">left_triangle&#39;</span> <span class="o">:</span> <span class="o">(</span><span class="n">whisker_right</span> <span class="n">unit</span> <span class="n">F</span><span class="o">)</span><span class="bp">.</span><span class="n">vcomp</span> <span class="o">(</span><span class="n">whisker_left</span> <span class="n">F</span> <span class="n">counit</span><span class="o">)</span> <span class="bp">=</span> <span class="n">nat_trans</span><span class="bp">.</span><span class="n">id</span> <span class="bp">_</span> <span class="bp">.</span> <span class="n">obviously</span><span class="o">)</span>
<span class="o">(</span><span class="n">right_triangle&#39;</span> <span class="o">:</span> <span class="o">(</span><span class="n">whisker_left</span> <span class="n">G</span> <span class="n">unit</span><span class="o">)</span><span class="bp">.</span><span class="n">vcomp</span> <span class="o">(</span><span class="n">whisker_right</span> <span class="n">counit</span> <span class="n">G</span><span class="o">)</span> <span class="bp">=</span> <span class="n">nat_trans</span><span class="bp">.</span><span class="n">id</span> <span class="bp">_</span> <span class="bp">.</span> <span class="n">obviously</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (Jan 17 2019 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/155331737):
<p>We then have</p>
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm">-</span>
<span class="cm">`adjunction F G` represents the data of an adjunction between two functors</span>
<span class="cm">`F : C ⥤ D` and `G : D ⥤ C`. `F` is the left adjoint and `G` is the right adjoint.</span>
<span class="cm">-/</span>
<span class="kn">structure</span> <span class="n">adjunction</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">C</span> <span class="err">⥤</span> <span class="n">D</span><span class="o">)</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="n">D</span> <span class="err">⥤</span> <span class="n">C</span><span class="o">)</span> <span class="kn">extends</span>
  <span class="o">(</span><span class="n">adjunction</span><span class="bp">.</span><span class="n">core_hom_equiv</span> <span class="n">F</span> <span class="n">G</span><span class="o">),</span> <span class="o">(</span><span class="n">adjunction</span><span class="bp">.</span><span class="n">core_unit_counit</span> <span class="n">F</span> <span class="n">G</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">unit_hom_equiv</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">X</span><span class="o">},</span> <span class="n">unit</span><span class="bp">.</span><span class="n">app</span> <span class="n">X</span> <span class="bp">=</span> <span class="o">(</span><span class="n">hom_equiv</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">to_fun</span> <span class="o">(</span><span class="mi">𝟙</span> <span class="o">(</span><span class="n">F</span><span class="bp">.</span><span class="n">obj</span> <span class="n">X</span><span class="o">))</span> <span class="bp">.</span> <span class="n">obviously</span><span class="o">)</span>
<span class="o">(</span><span class="n">counit_hom_equiv</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">Y</span><span class="o">},</span> <span class="n">counit</span><span class="bp">.</span><span class="n">app</span> <span class="n">Y</span> <span class="bp">=</span> <span class="o">(</span><span class="n">hom_equiv</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">inv_fun</span> <span class="o">(</span><span class="mi">𝟙</span> <span class="o">(</span><span class="n">G</span><span class="bp">.</span><span class="n">obj</span> <span class="n">Y</span><span class="o">))</span> <span class="bp">.</span> <span class="n">obviously</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (Jan 17 2019 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/155331794):
<p>And finally</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">of_core_hom_equiv</span> <span class="o">(</span><span class="n">adj</span> <span class="o">:</span> <span class="n">core_hom_equiv</span> <span class="n">F</span> <span class="n">G</span><span class="o">)</span> <span class="o">:</span> <span class="n">adjunction</span> <span class="n">F</span> <span class="n">G</span> <span class="o">:=</span> <span class="c1">-- see github for the code</span>
<span class="n">def</span> <span class="n">of_core_unit_counit</span> <span class="o">(</span><span class="n">adj</span> <span class="o">:</span> <span class="n">core_unit_counit</span> <span class="n">F</span> <span class="n">G</span><span class="o">)</span> <span class="o">:</span> <span class="n">adjunction</span> <span class="n">F</span> <span class="n">G</span> <span class="o">:=</span> <span class="c1">-- see github for the code</span>
</pre></div>

#### [ Patrick Massot (Jan 17 2019 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/155344034):
<p>It looks very nice, except that it could look much nicer. Did you miss <a href="https://github.com/leanprover/lean/commit/95fa4cfb0a8774570d67bb231c1ab088a94e12bb#diff-50f7eff1a2547545a820cbbeee3a0b6eL15" target="_blank" title="https://github.com/leanprover/lean/commit/95fa4cfb0a8774570d67bb231c1ab088a94e12bb#diff-50f7eff1a2547545a820cbbeee3a0b6eL15">https://github.com/leanprover/lean/commit/95fa4cfb0a8774570d67bb231c1ab088a94e12bb#diff-50f7eff1a2547545a820cbbeee3a0b6eL15</a> ?</p>

#### [ Johan Commelin (Jan 17 2019 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/155344144):
<p>Yes, I guess we should quickly make a PR that uses the correct functor symbol</p>

#### [ Johan Commelin (Jan 17 2019 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/155356649):
<p>There is one drawback that I currently see with my approach. If the categories <code>C</code> and <code>D</code> do live in the same universe, then we can extract an isomorphism between the two Hom-bifunctors from the adjunction. We can also define an adjunction given such a natural isomorphism <code>i</code>. But the extracted isomorphism will not be defeq to <code>i</code>.</p>

#### [ Johan Commelin (Jan 17 2019 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/155356679):
<p>I do not see how to fix this if we also want to keep the option of adjunctions for different universe levels.</p>

#### [ Johan Commelin (Jan 22 2019 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156608839):
<p>Here is a slightly non-trivial example of a Lean checked adjunction:</p>
<div class="codehilite"><pre><span></span><span class="kn">section</span>
<span class="kn">open</span> <span class="n">mv_polynomial</span>
<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">,</span> <span class="n">priority</span> <span class="mi">0</span><span class="o">]</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">fintype</span> <span class="n">set_fintype</span> <span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span>

<span class="n">noncomputable</span> <span class="n">def</span> <span class="n">polynomial</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="err">⥤</span> <span class="n">CommRing</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">obj</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">mv_polynomial</span> <span class="n">α</span> <span class="bp">ℤ</span><span class="o">,</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">map</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">f</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">eval₂</span> <span class="n">C</span> <span class="o">(</span><span class="n">X</span> <span class="err">∘</span> <span class="n">f</span><span class="o">),</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">map_id&#39;</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">ext</span><span class="bp">.</span><span class="n">mpr</span> <span class="err">$</span> <span class="n">funext</span> <span class="err">$</span> <span class="n">eval₂_eta</span><span class="o">,</span>
  <span class="n">map_comp&#39;</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">f</span> <span class="n">g</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">ext</span><span class="bp">.</span><span class="n">mpr</span> <span class="err">$</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">p</span><span class="o">,</span>
  <span class="k">by</span> <span class="n">apply</span> <span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">p</span><span class="bp">;</span> <span class="n">intros</span><span class="bp">;</span>
    <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="bp">*</span><span class="o">,</span> <span class="n">eval₂_add</span><span class="o">,</span> <span class="n">eval₂_mul</span><span class="o">,</span> <span class="n">eval₂_C</span><span class="o">,</span> <span class="n">eval₂_X</span><span class="o">,</span> <span class="n">comp_val</span><span class="o">,</span>
      <span class="n">eq_self_iff_true</span><span class="o">,</span> <span class="n">function</span><span class="bp">.</span><span class="n">comp_app</span><span class="o">,</span> <span class="n">types_comp</span><span class="o">]</span> <span class="n">at</span> <span class="bp">*</span> <span class="o">}</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">polynomial_obj_α</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">:</span>
  <span class="o">(</span><span class="n">polynomial</span><span class="bp">.</span><span class="n">obj</span> <span class="n">α</span><span class="o">)</span><span class="bp">.</span><span class="n">α</span> <span class="bp">=</span> <span class="n">mv_polynomial</span> <span class="n">α</span> <span class="bp">ℤ</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">polynomial_map_val</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">:</span>
  <span class="o">(</span><span class="n">polynomial</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span> <span class="bp">=</span> <span class="n">eval₂</span> <span class="n">C</span> <span class="o">(</span><span class="n">X</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="n">noncomputable</span> <span class="n">def</span> <span class="n">adj</span> <span class="o">:</span> <span class="n">adjunction</span> <span class="n">polynomial</span> <span class="o">(</span><span class="n">forget</span> <span class="o">:</span> <span class="n">CommRing</span> <span class="err">⥤</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">adjunction</span><span class="bp">.</span><span class="n">mk_of_hom_equiv</span> <span class="bp">_</span> <span class="bp">_</span>
<span class="o">{</span> <span class="n">hom_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">R</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">to_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">X</span><span class="o">,</span>
    <span class="n">inv_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">eval₂</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast</span> <span class="n">f</span><span class="o">,</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">left_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">ext</span><span class="bp">.</span><span class="n">mpr</span> <span class="err">$</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">p</span><span class="o">,</span>
    <span class="k">begin</span>
      <span class="k">have</span> <span class="n">H0</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span><span class="n">congr</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">eq_cast&#39;</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">val</span> <span class="err">∘</span> <span class="n">C</span><span class="o">))</span> <span class="o">(</span><span class="n">rfl</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">n</span><span class="o">))</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span>
      <span class="k">have</span> <span class="n">H1</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">p₁</span> <span class="n">p₂</span><span class="o">,</span> <span class="o">(</span><span class="bp">@</span><span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_add</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">f</span><span class="bp">.</span><span class="n">val</span> <span class="n">f</span><span class="bp">.</span><span class="mi">2</span> <span class="n">p₁</span> <span class="n">p₂</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span>
      <span class="k">have</span> <span class="n">H2</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">p₁</span> <span class="n">p₂</span><span class="o">,</span> <span class="o">(</span><span class="bp">@</span><span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_mul</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">f</span><span class="bp">.</span><span class="n">val</span> <span class="n">f</span><span class="bp">.</span><span class="mi">2</span> <span class="n">p₁</span> <span class="n">p₂</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span>
      <span class="n">apply</span> <span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">p</span><span class="bp">;</span> <span class="n">intros</span><span class="bp">;</span>
      <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="bp">*</span><span class="o">,</span> <span class="n">eval₂_add</span><span class="o">,</span> <span class="n">eval₂_mul</span><span class="o">,</span> <span class="n">eval₂_C</span><span class="o">,</span> <span class="n">eval₂_X</span><span class="o">,</span>
        <span class="n">eq_self_iff_true</span><span class="o">,</span> <span class="n">function</span><span class="bp">.</span><span class="n">comp_app</span><span class="o">,</span> <span class="n">hom_coe_app</span><span class="o">]</span> <span class="n">at</span> <span class="bp">*</span>
    <span class="kn">end</span><span class="o">,</span>
    <span class="n">right_inv</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">tidy</span> <span class="o">},</span>
  <span class="n">hom_equiv_naturality_left_symm&#39;</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X&#39;</span> <span class="n">X</span> <span class="n">Y</span> <span class="n">f</span> <span class="n">g</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">ext</span><span class="bp">.</span><span class="n">mpr</span> <span class="err">$</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">p</span><span class="o">,</span>
  <span class="k">begin</span>
    <span class="n">apply</span> <span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">p</span><span class="bp">;</span> <span class="n">intros</span><span class="bp">;</span>
    <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="bp">*</span><span class="o">,</span> <span class="n">eval₂_mul</span><span class="o">,</span> <span class="n">eval₂_add</span><span class="o">,</span> <span class="n">eval₂_C</span><span class="o">,</span> <span class="n">eval₂_X</span><span class="o">,</span>
      <span class="n">comp_val</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">coe_fn_symm_mk</span><span class="o">,</span> <span class="n">hom_coe_app</span><span class="o">,</span> <span class="n">polynomial_map_val</span><span class="o">,</span>
      <span class="n">eq_self_iff_true</span><span class="o">,</span> <span class="n">function</span><span class="bp">.</span><span class="n">comp_app</span><span class="o">,</span> <span class="n">add_right_inj</span><span class="o">,</span> <span class="n">types_comp</span><span class="o">]</span> <span class="n">at</span> <span class="bp">*</span>
  <span class="kn">end</span> <span class="o">}</span>

<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Jan 22 2019 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156608907):
<p>For some reason this code is slower than I would have hoped. And as you can see there is quite a bit of <code>mv_polynomial.induction_on p</code>, so I think there are some lemmas that could be factored out...</p>

#### [ Reid Barton (Jan 22 2019 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156608934):
<p>When I was working on adjunctions I gave up on precisely this because everything was so slow</p>

#### [ Johan Commelin (Jan 22 2019 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609025):
<p>Somehow that doesn't feel like a good sign.</p>

#### [ Reid Barton (Jan 22 2019 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609062):
<p><a href="#narrow/stream/113488-general/topic/my_polynomial.20performance/near/147887874" title="#narrow/stream/113488-general/topic/my_polynomial.20performance/near/147887874">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial.20performance/near/147887874</a></p>

#### [ Johan Commelin (Jan 22 2019 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609169):
<p>Aah, I see.</p>

#### [ Johan Commelin (Jan 22 2019 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609366):
<p>I just pushed.</p>

#### [ Patrick Massot (Jan 22 2019 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609404):
<p>Is this <code>obviously</code> being slow of <code>mv_polynomial</code>?</p>

#### [ Johan Commelin (Jan 22 2019 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609443):
<div class="codehilite"><pre><span></span>rings.lean:115:18: information

parsing took 41.6ms
rings.lean:115:18: information

elaboration of adj took 15.2s
rings.lean:115:18: information

type checking of adj took 18.7ms
rings.lean:115:18: information

decl post-processing of adj took 17.5ms
</pre></div>

#### [ Johan Commelin (Jan 22 2019 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609454):
<p>No, I think it's <code>mv_polynomial</code></p>

#### [ Johan Commelin (Jan 22 2019 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609524):
<p>Also:</p>
<div class="codehilite"><pre><span></span>rings.lean:100:18: information

parsing took 7.51ms
rings.lean:100:18: information

elaboration of polynomial took 4.11s
rings.lean:100:18: information

type checking of polynomial took 15.8ms
rings.lean:100:18: information

decl post-processing of polynomial took 15.3ms
</pre></div>

#### [ Johan Commelin (Jan 22 2019 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609545):
<p>And there is no <code>obviously</code> in</p>
<div class="codehilite"><pre><span></span><span class="n">noncomputable</span> <span class="n">def</span> <span class="n">polynomial</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="err">⥤</span> <span class="n">CommRing</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">obj</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">mv_polynomial</span> <span class="n">α</span> <span class="bp">ℤ</span><span class="o">,</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">map</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">f</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">eval₂</span> <span class="n">C</span> <span class="o">(</span><span class="n">X</span> <span class="err">∘</span> <span class="n">f</span><span class="o">),</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">map_id&#39;</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">ext</span><span class="bp">.</span><span class="n">mpr</span> <span class="err">$</span> <span class="n">funext</span> <span class="err">$</span> <span class="n">eval₂_eta</span><span class="o">,</span>
  <span class="n">map_comp&#39;</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">f</span> <span class="n">g</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">ext</span><span class="bp">.</span><span class="n">mpr</span> <span class="err">$</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">p</span><span class="o">,</span>
  <span class="k">by</span> <span class="n">apply</span> <span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">p</span><span class="bp">;</span> <span class="n">intros</span><span class="bp">;</span>
    <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="bp">*</span><span class="o">,</span> <span class="n">eval₂_add</span><span class="o">,</span> <span class="n">eval₂_mul</span><span class="o">,</span> <span class="n">eval₂_C</span><span class="o">,</span> <span class="n">eval₂_X</span><span class="o">,</span> <span class="n">comp_val</span><span class="o">,</span>
      <span class="n">eq_self_iff_true</span><span class="o">,</span> <span class="n">function</span><span class="bp">.</span><span class="n">comp_app</span><span class="o">,</span> <span class="n">types_comp</span><span class="o">]</span> <span class="n">at</span> <span class="bp">*</span> <span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Jan 22 2019 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609647):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> <span class="user-mention" data-user-id="110064">@Kenny Lau</span> <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Is there anything that can be done here? I guess lots of the stuff that we plan on doing will depend on <code>mv_polynomial</code>. All the number theory that Kevin and Sander are interested in will need it.</p>

#### [ Patrick Massot (Jan 22 2019 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609654):
<p>What happens if you sorry the last proof?</p>

#### [ Johan Commelin (Jan 22 2019 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609771):
<p>Then it drops from 4s to 1s.</p>

#### [ Kenny Lau (Jan 22 2019 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609780):
<p>Stuff involving mv_polynomial and polynomial have been known to be slow.</p>

#### [ Kenny Lau (Jan 22 2019 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609783):
<p>I don't think <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> knows how to fix it.</p>

#### [ Johan Commelin (Jan 22 2019 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609862):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> It spends 638ms in the second <code>by apply_instance</code>.</p>

#### [ Johan Commelin (Jan 22 2019 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156610033):
<p>The last <code>begin</code>-<code>end</code> block in <code>adj</code> takes 10 seconds <span class="emoji emoji-1f631" title="scream">:scream:</span></p>

#### [ Reid Barton (Jan 22 2019 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156610251):
<p>do you really need to <code>simp at *</code>?</p>

#### [ Johan Commelin (Jan 22 2019 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156610303):
<p>Yes, some of the goals need that.</p>

#### [ Reid Barton (Jan 22 2019 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156610418):
<p>I mean maybe you can do something more than <code>simp</code> but less than <code>at *</code></p>

#### [ Reid Barton (Jan 22 2019 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156610450):
<p>e.g. explicitly say where to simp</p>

#### [ Johan Commelin (Jan 22 2019 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156610592):
<p>Aah, ok. But the context is very small, and I guess <code>simp</code> will fail quickly on atomic hypotheses...</p>

#### [ Johan Commelin (Jan 22 2019 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156610713):
<p>Also, the places where I want to simplify are introduced by <code>intros</code>, and what gets intro'd depends on the goal.</p>

#### [ Johan Commelin (Jan 22 2019 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156610722):
<p>The induction step generates 3 goals.</p>

#### [ Johan Commelin (Jan 22 2019 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156610749):
<p>So if I want to be explicit in the <code>simp</code>-part, I need to tackle the 3 goals separately...</p>

#### [ Reid Barton (Jan 28 2019 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/157020948):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>, maybe <code>is_left_adjoint</code> should be a class, and <code>left_adjoint_preserves_colimits</code> an instance?</p>

#### [ Johan Commelin (Jan 28 2019 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/157052142):
<p>Probably yes... I wasn't sure yet when I wrote that code (and I had just experienced that it isn't always a good idea to make things classes, viz <code>unique</code>).</p>

#### [ Johan Commelin (Jan 28 2019 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/157052152):
<p>Feel free to upgrade it whenever you have code that comes close to it.</p>


{% endraw %}
