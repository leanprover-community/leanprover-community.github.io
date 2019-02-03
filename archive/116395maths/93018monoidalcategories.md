---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/93018monoidalcategories.html
---

## Stream: [maths](index.html)
### Topic: [monoidal categories](93018monoidalcategories.html)

---


{% raw %}
#### [ Scott Morrison (Nov 07 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915123):
<p><span class="user-mention" data-user-id="128547">@Michael Jendrusch</span> has recently started work on monoidal categories again. (Yay!)</p>

#### [ Scott Morrison (Nov 07 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915139):
<p>I've been looking at what he's written, and I want to resume my rant about how terrible coercions are, as a result.</p>

#### [ Scott Morrison (Nov 07 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915148):
<p>He's defined monoidal categories, and I think these are uncontroversial.</p>

#### [ Scott Morrison (Nov 07 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915151):
<p><a href="https://github.com/mjendrusch/monoidal-categories-reboot/blob/master/src/monoidal_categories_reboot/monoidal_category.lean" target="_blank" title="https://github.com/mjendrusch/monoidal-categories-reboot/blob/master/src/monoidal_categories_reboot/monoidal_category.lean">https://github.com/mjendrusch/monoidal-categories-reboot/blob/master/src/monoidal_categories_reboot/monoidal_category.lean</a></p>

#### [ Mario Carneiro (Nov 07 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915158):
<p>so many axioms...</p>

#### [ Scott Morrison (Nov 07 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915160):
<p>However when he gets to monoidal functors the horrors caused by coercions start to creep out...</p>

#### [ Scott Morrison (Nov 07 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915162):
<p>Ah -- maybe I should address that first.</p>

#### [ Scott Morrison (Nov 07 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915165):
<p>You might have said:</p>

#### [ Scott Morrison (Nov 07 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915211):
<p>surely a monoidal category should be described as a category <code>C</code> equipped with a functor <code>C \times C \func C</code>, satisfying ...</p>

#### [ Scott Morrison (Nov 07 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915216):
<p>(this will certainly reduce the number of axioms, at least slightly, because various things are wrapped up in functoriality)</p>

#### [ Scott Morrison (Nov 07 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915225):
<p>However... implementation details forced on us by Lean make this a bad idea (as I discovered when I did monoidal categories previously)</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915228):
<p>hopefully you prove the equivalence though?</p>

#### [ Scott Morrison (Nov 07 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915274):
<p>Yes, it's easy (and Michael started doing it) to show afterwards that these things assemble into functors, and natural transformations, and so on.</p>

#### [ Scott Morrison (Nov 07 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915297):
<p>The problem with making tensor product a functor first of all is that it becomes really painful to implement notation <code>X \otimes Y</code> and <code>f \otimes' g</code>.</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915307):
<p>what's the issue?</p>

#### [ Scott Morrison (Nov 07 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915348):
<p>You end up having to define as auxiliary lemmas curried versions of the functor of objects, but even then the elaborator often really struggles.</p>

#### [ Scott Morrison (Nov 07 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915363):
<p>(Sorry, it's been a year or so since I last fought with this issue... give me a moment.)</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915369):
<p>Can you make it a curried functor instead?</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915376):
<p>cat being a CCC and all</p>

#### [ Scott Morrison (Nov 07 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915434):
<p>You could make it a curried functor, but I don't think it would help. If T was your tensor product functor, you still couldn't write <code>T X Y</code> and have the elaborator successfully introduce both coercions.</p>

#### [ Scott Morrison (Nov 07 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915471):
<p>Neither <code>T (X, Y)</code>, if <code>T : C \times C \func C</code>, or <code>T X Y</code>, if <code>T : C \func (C \func C)</code> will elaborate reliably. (In fact, I think they won't ever elaborate.)</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915479):
<p>that's sad...</p>

#### [ Scott Morrison (Nov 07 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915532):
<p>You can see examples of this all over my (no-longer-compiling) earlier attempt at monoidal categories.</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915535):
<p>What about an infix functor application operator?</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915540):
<p>like <code>&lt;$&gt;</code> for <code>functor</code></p>

#### [ Scott Morrison (Nov 07 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915549):
<div class="codehilite"><pre><span></span>@[ematch] definition interchange (f : U ⟶ V) (g : V ⟶ W) (h : X ⟶ Y) (k : Y ⟶ Z) :
  (f ≫ g) ⊗ (h ≫ k) = (f ⊗ h) ≫ (g ⊗ k) :=
  @Functor.functoriality (C × C) _ C _ (tensor C) ⟨U, X⟩ ⟨V, Y⟩ ⟨W, Z⟩ ⟨f, h⟩ ⟨g, k⟩
</pre></div>


<p>should really just be proved by <code>(tensor  C).map_comp (f, h) (g,k)</code>, but instead we need to use @, and specify way too many implicit arguments.</p>

#### [ Scott Morrison (Nov 07 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915556):
<p>Yes --- so this is what I had long ago.</p>

#### [ Scott Morrison (Nov 07 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915560):
<p>I had <code>+&gt;</code> for obj, and <code>&amp;&gt;</code> for map, although I really don't care what the symbols are.</p>

#### [ Scott Morrison (Nov 07 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915564):
<p>I would _love_ to move back to this model, which would let us get rid of lots of coercions.</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915612):
<p>I've heard this story before, and I don't disagree with you</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915628):
<p>I really want coercions to work, and in principle they could, but lean's coercion model is not extensible enough</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915646):
<p>it should be a parser extension rather than being tied to <code>coe</code> in core</p>

#### [ Scott Morrison (Nov 07 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915652):
<p>If we were in a situation where modifying the coercion mechanism was on the table, I would absolutely support struggling on with coercions, essentially to gain data about what we really want.</p>

#### [ Scott Morrison (Nov 07 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915697):
<p>But I'm not sure whether <span class="emoji emoji-1f340" title="four leaf clover">:four_leaf_clover:</span> gives us this prospect, or not.</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915706):
<p>I think it might, at least it should not be far from the areas under development</p>

#### [ Scott Morrison (Nov 07 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915710):
<p>If my fighting with coercions is not significantly likely to result in better coercions later, I just want the suffering to go away. :-)</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915724):
<p>the fact that simp doesn't work under coercions is something we might be able to fix in lean 3</p>

#### [ Scott Morrison (Nov 07 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915727):
<p>I haven't even started explaining the difficulties coercions are causing in the design of <code>monoidal_functor</code>... :-)</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915773):
<p>right, sorry to derail your story. carry on</p>

#### [ Scott Morrison (Nov 07 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915790):
<p>Essentially: if we want <code>monoidal_functor</code> to extend <code>functor</code>, we need new coercions so we can still write <code>F X</code>, when <code>F</code> is a monoidal functor. Now however none of the lemmas involving <code>F X</code> will apply when <code>F</code> is a monoidal functor, because the coercion won't be the right one.</p>

#### [ Scott Morrison (Nov 07 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915792):
<p>So we'll have to reproduce all the lemmas...</p>

#### [ Scott Morrison (Nov 07 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915795):
<p>And we'll have to do this again for <code>braided_functor</code>, and then again for <code>additive_functor</code>, and then again for ...</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915834):
<p>wait, what's a monoidal functor now</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915847):
<p>oh <a href="https://github.com/mjendrusch/monoidal-categories-reboot/blob/master/src/monoidal_categories_reboot/monoidal_functor.lean" target="_blank" title="https://github.com/mjendrusch/monoidal-categories-reboot/blob/master/src/monoidal_categories_reboot/monoidal_functor.lean">https://github.com/mjendrusch/monoidal-categories-reboot/blob/master/src/monoidal_categories_reboot/monoidal_functor.lean</a></p>

#### [ Scott Morrison (Nov 07 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915848):
<p>monoidal functor doesn't exist yet, beyond Michael's first cut at <a href="https://github.com/mjendrusch/monoidal-categories-reboot/blob/master/src/monoidal_categories_reboot/monoidal_functor.lean" target="_blank" title="https://github.com/mjendrusch/monoidal-categories-reboot/blob/master/src/monoidal_categories_reboot/monoidal_functor.lean">https://github.com/mjendrusch/monoidal-categories-reboot/blob/master/src/monoidal_categories_reboot/monoidal_functor.lean</a></p>

#### [ Scott Morrison (Nov 07 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915853):
<p>and you can see at the bottom of that file the problems waiting for us as soon as we define composition of monoidal functors.</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915944):
<p>What's the alternative?</p>

#### [ Scott Morrison (Nov 07 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915954):
<p>well, if all the coercions were gone, our problems would mostly disappear.</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146915997):
<p>if the coercions were gone, it wouldn't typecheck. Are you writing explicit functions now?</p>

#### [ Scott Morrison (Nov 07 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916000):
<p>Instead of having <code>functor.map'</code>, the structure field, which doesn't use the coercion, and <code>functor.map</code>, the same, as a lemma written using the coercion, we'd just have the structure field.</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916006):
<p><code>F.to_functor.map f</code>?</p>

#### [ Scott Morrison (Nov 07 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916008):
<p>So we wouldn't have to define a new version of <code>map</code> for monoidal functors, so all the lemmas about <code>functor.map</code> would still apply</p>

#### [ Scott Morrison (Nov 07 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916009):
<p>Yes.</p>

#### [ Scott Morrison (Nov 07 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916020):
<p>But you wouldn't have to write the <code>.to_functor</code> explicitly.</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916022):
<p>?</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916025):
<p>what's the magic sauce you are using in place of coercions</p>

#### [ Scott Morrison (Nov 07 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916029):
<p>Am I wrong? I thought that's how the extension mechanism works -- you can refer directly to the fields of the parent structure.</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916074):
<p>It depends on whether you are using the old structures or new</p>

#### [ Scott Morrison (Nov 07 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916076):
<p>new</p>

#### [ Scott Morrison (Nov 07 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916082):
<p>but this certainly works, I just double checked :-)</p>

#### [ Mario Carneiro (Nov 07 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916094):
<p>Is the <code>to_functor</code> in the pp.all term?</p>

#### [ Scott Morrison (Nov 07 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916287):
<p>Yes</p>

#### [ Scott Morrison (Nov 07 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916297):
<p>The <code>to_functor</code> is in fact there even without <code>pp.all</code>. You just don't need to write it.</p>

#### [ Scott Morrison (Nov 07 2018 at 04:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916427):
<p>As far as I can see the parser is doing this. There's no <code>monoidal_functor.obj</code> field at all,  but you can nevertheless write <code>F.obj X</code> when <code>F</code> is a monoidal functor, and when you pp the resulting term it shows as <code>F.to_functor.obj X</code>.</p>

#### [ Scott Morrison (Nov 07 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916445):
<p>The essential problem is that because of coercions, we have all this duplication: <code>functor</code> has both <code>map'</code> and <code>map</code>, and <code>map_comp'</code> and <code>map_comp</code>, etc.</p>

#### [ Scott Morrison (Nov 07 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916452):
<p>Every time we extend functor (or anything similar), we will need to reproduce all this duplication again.</p>

#### [ Mario Carneiro (Nov 07 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916502):
<p>hm, this is parser magic we can't duplicate</p>

#### [ Reid Barton (Nov 07 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916655):
<p>Sorry, so to go back to the start, if we forgot about coercions entirely, is there still an issue with defining the tensor product to be a functor from C x C to C?</p>

#### [ Scott Morrison (Nov 07 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916709):
<p>I think there still is.</p>

#### [ Scott Morrison (Nov 07 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916711):
<p>The basic question is how to implement <code>X \otimes Y</code>.</p>

#### [ Reid Barton (Nov 07 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916717):
<p><code>T.app (X, Y)</code>?</p>

#### [ Scott Morrison (Nov 07 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916719):
<p>You mean <code>T.obj (X, Y)</code>?</p>

#### [ Reid Barton (Nov 07 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916720):
<p>er, <code>T.obj</code></p>

#### [ Reid Barton (Nov 07 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916765):
<p>I can see that writing down the functors which the associator is supposed to be a natural isomorphism between is going to be ugly</p>

#### [ Scott Morrison (Nov 07 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916767):
<p>The problem there is that for reasons I don't totally understand, even having the pair construction in there gums up the elaborator.</p>

#### [ Reid Barton (Nov 07 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916768):
<p>hm</p>

#### [ Scott Morrison (Nov 07 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916773):
<p>My old monoidal-categories repository didn't use any coercions.</p>

#### [ Scott Morrison (Nov 07 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916780):
<p>(unfortunately I don't have a compiling version of it anymore...)</p>

#### [ Scott Morrison (Nov 07 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916812):
<p>But I found myself having to use</p>
<div class="codehilite"><pre><span></span>-- Convenience methods which take two arguments, rather than a pair. (This seems to often help the elaborator avoid getting stuck on `prod.mk`.)
definition tensorObjects (X Y : C) : C := (tensor C) +&gt; (X, Y)

infixr ` ⊗ `:80 := tensorObjects -- type as \otimes
</pre></div>

#### [ Reid Barton (Nov 07 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916854):
<p>Another question: how about using isos for the associator/unitors instead of four fields each?</p>

#### [ Reid Barton (Nov 07 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916855):
<p>I imagine you thought of that already</p>

#### [ Scott Morrison (Nov 07 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916857):
<p>but then there's an extra layer of folding and unfolding <code>tensorObjects</code></p>

#### [ Scott Morrison (Nov 07 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916860):
<p>Actually, the question of using isos is a good one.</p>

#### [ Scott Morrison (Nov 07 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916862):
<p>and I'm not sure that I did think about it carefully.</p>

#### [ Scott Morrison (Nov 07 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916903):
<p>I suspect I wrote my initial monoidal categories library before I'd actually ironed out a usable implementation of isomorphisms....</p>

#### [ Scott Morrison (Nov 07 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916908):
<p><span class="user-mention" data-user-id="128547">@Michael Jendrusch</span>, next time you're around, how about we try this idea out: using isomorphisms as the fields for associators and unitors, rather than the four separate fields?</p>

#### [ Reid Barton (Nov 07 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146916961):
<p>Also: no bicategories?? <span class="emoji emoji-1f643" title="upside down">:upside_down:</span></p>

#### [ Reid Barton (Nov 07 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146917029):
<p>I kind of want to formalize (bi)limits in bicategories, since I feel the literature on them is kind of spotty.</p>

#### [ Reid Barton (Nov 07 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146918446):
<p>but, I might want to do it less if it is going to look like <a href="https://ncatlab.org/nlab/show/bicategory#detailedDefn" target="_blank" title="https://ncatlab.org/nlab/show/bicategory#detailedDefn">https://ncatlab.org/nlab/show/bicategory#detailedDefn</a>. How would I even know that I got the definition correct?</p>

#### [ Scott Morrison (Nov 07 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146922053):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>, I've been considering trying to talk <span class="user-mention" data-user-id="128547">@Michael Jendrusch</span> into doing bicategories. :-) I would like them, too.</p>

#### [ Scott Morrison (Nov 07 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146922071):
<p>But I think it makes sense to sort out the issues we're having here first, and if they are all solvable it might be a cheap rewrite to generalise...</p>

#### [ Scott Morrison (Nov 07 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146922130):
<p><span class="user-mention" data-user-id="128547">@Michael Jendrusch</span>, I just added two new commits that package associators, unitors, and tensorators as isos. I think it is nicer.</p>

#### [ Johan Commelin (Nov 07 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146924968):
<p>Yesterday one of my colleagues walked in to have a quick look at the workshop. He is working on derivators and such stuff. He explained how we might want to use multicategories for this. But I'm not sure how much work it would be to set up all the basics. He said it would help us get rid of the pentagon axiom in some sense. But I'm not sure if it means that the carpet won't fit in another corner... (is this an English idiom?).<br>
<span class="user-mention" data-user-id="110087">@Scott Morrison</span> Are you familiar with this multicategorical approach?</p>

#### [ Michael Jendrusch (Nov 07 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146925211):
<blockquote>
<p><span class="user-mention" data-user-id="128547">@Michael Jendrusch</span>, I just added two new commits that package associators, unitors, and tensorators as isos. I think it is nicer.</p>
</blockquote>
<p>It's merged! I would kind of like to have bicategories, too, but this looks painful (<a href="https://ncatlab.org/nlab/show/bicategory#detailedDefn" target="_blank" title="https://ncatlab.org/nlab/show/bicategory#detailedDefn">https://ncatlab.org/nlab/show/bicategory#detailedDefn</a>).</p>

#### [ Michael Jendrusch (Nov 07 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146925412):
<p>On another note, making <code>µ</code> an iso in the definition of a monoidal functor makes that a _strict_ monoidal functor according to nLab, where I would also want _lax_ monoidal functors. Maybe we can define a _lax_ monoidal functor and then extend it to a _strict_ monoidal functor?</p>

#### [ Scott Morrison (Nov 07 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146926349):
<p>Ah, it's  a little subtle. If you want lax monoidal functors, then I want oplax ones (this is a serious request, actually: &lt;<a href="https://arxiv.org/abs/1701.00567" target="_blank" title="https://arxiv.org/abs/1701.00567">https://arxiv.org/abs/1701.00567</a>&gt;. So if we want to do it via inheritance we'll be dealing with a diamond.</p>

#### [ Scott Morrison (Nov 07 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146926350):
<p>But I agree it's desirable.</p>

#### [ Scott Morrison (Nov 07 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146926357):
<p>(But you certainly can't use the name monoidal functor if you mean a lax one. :-)</p>

#### [ Scott Morrison (Nov 07 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146926559):
<p>Regarding multicategories --- I'm not opposed to someone also introducing these, but I'm pretty confident it's all blind men describing an elephant. Now if we want to talk about disklike categories &lt;<a href="https://arxiv.org/pdf/1108.5386.pdf" target="_blank" title="https://arxiv.org/pdf/1108.5386.pdf">https://arxiv.org/pdf/1108.5386.pdf</a>&gt;, then we'd be cooking with gas.</p>

#### [ Reid Barton (Nov 07 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/146964187):
<p>Actually, maybe bicategories won't be that bad at all. Shouldn't it just be a matter of asking for <code>Pi a b. category (C a b)</code>, then adding a bunch of type indices everywhere in the definition of monoidal category?</p>

#### [ Scott Morrison (Nov 07 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/147252547):
<p>Yes, that sounds right. It's a pity you can't mix <code>variables</code> syntax with structures; you could almost leave out all those extra type indices!</p>

#### [ Michael Jendrusch (Nov 08 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/147289125):
<blockquote>
<p>Ah, it's  a little subtle. If you want lax monoidal functors, then I want oplax ones (this is a serious request, actually: &lt;<a href="https://arxiv.org/abs/1701.00567" target="_blank" title="https://arxiv.org/abs/1701.00567">https://arxiv.org/abs/1701.00567</a>&gt;. So if we want to do it via inheritance we'll be dealing with a diamond.</p>
</blockquote>
<p>It seems that a lot of things in category theory result in diamonds when using inheritance (e.g. with strict monoidal categories). Is there another standard way of treating this without inheritance, and what are the actual problems one gets with diamonds in Lean?</p>

#### [ Michael Jendrusch (Nov 08 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/147297174):
<p>would it make sense to try and work around inheritance (and thus diamonds) by not having a classes <code>lax_monoidal_functor</code>, <code>oplax_monoidal_functor</code> both inheriting from functor (and getting a diamond from defining <code>monoidal_functor</code> as inheriting from both), instead opting to have <code>functor_is_lax_monoidal</code>, <code>functor_is_oplax_monoidal</code> together with an instance <code>functor_is_monoidal</code> for every functor which is both lax and oplax, like this?</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">functor_is_lax_monoidal</span>
  <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">monoidal_category</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span>
  <span class="o">(</span><span class="n">D</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u&#39;</span><span class="o">)</span> <span class="o">[</span><span class="n">monoidal_category</span><span class="bp">.</span><span class="o">{</span><span class="n">u&#39;</span> <span class="n">v&#39;</span><span class="o">}</span> <span class="n">D</span><span class="o">]</span>
  <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">C</span> <span class="err">⥤</span> <span class="n">D</span><span class="o">)</span> <span class="o">:=</span>
<span class="c1">-- definition of lax monoidal functor here.</span>

<span class="n">class</span> <span class="n">functor_is_oplax_monoidal</span>
  <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">monoidal_category</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span>
  <span class="o">(</span><span class="n">D</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u&#39;</span><span class="o">)</span> <span class="o">[</span><span class="n">monoidal_category</span><span class="bp">.</span><span class="o">{</span><span class="n">u&#39;</span> <span class="n">v&#39;</span><span class="o">}</span> <span class="n">D</span><span class="o">]</span>
  <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">C</span> <span class="err">⥤</span> <span class="n">D</span><span class="o">)</span> <span class="o">:=</span>
<span class="c1">-- definition of oplax monoidal functor here.</span>

<span class="n">class</span> <span class="n">functor_is_monoidal</span>
  <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">monoidal_category</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span>
  <span class="o">(</span><span class="n">D</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u&#39;</span><span class="o">)</span> <span class="o">[</span><span class="n">monoidal_category</span><span class="bp">.</span><span class="o">{</span><span class="n">u&#39;</span> <span class="n">v&#39;</span><span class="o">}</span> <span class="n">D</span><span class="o">]</span>
  <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">C</span> <span class="err">⥤</span> <span class="n">D</span><span class="o">)</span> <span class="o">:=</span>
<span class="c1">-- definition of monoidal functor here.</span>

<span class="kn">instance</span> <span class="n">lax_and_oplax</span>
  <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">monoidal_category</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span>
  <span class="o">(</span><span class="n">D</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u&#39;</span><span class="o">)</span> <span class="o">[</span><span class="n">monoidal_category</span><span class="bp">.</span><span class="o">{</span><span class="n">u&#39;</span> <span class="n">v&#39;</span><span class="o">}</span> <span class="n">D</span><span class="o">]</span>
  <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">C</span> <span class="err">⥤</span> <span class="n">D</span><span class="o">)</span> <span class="o">[</span><span class="n">functor_is_lax_monoidal</span> <span class="n">C</span> <span class="n">D</span> <span class="n">F</span><span class="o">]</span> <span class="o">[</span><span class="n">functor_is_oplax_monoidal</span> <span class="n">C</span> <span class="n">D</span> <span class="n">F</span><span class="o">]</span> <span class="o">:</span>
  <span class="n">functor_is_monoidal</span> <span class="n">C</span> <span class="n">D</span> <span class="n">F</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">obviously</span>
</pre></div>

#### [ Scott Morrison (Nov 08 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/147333122):
<p>This is an interesting approach; I wonder if we should re-explore making <code>functor</code> a typeclass right from the beginning.</p>

#### [ Scott Morrison (Nov 08 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/147333145):
<p>My concern is that <code>functor_is_monoidal</code> carries data (the tensorator), so it's a little scary making it a typeclass.</p>

#### [ Scott Morrison (Nov 08 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/147333211):
<p>However in my experience it's extremely rare that one considers two different tensorators for the same functor. (Although not _never_)</p>

#### [ Scott Morrison (Nov 08 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/147333229):
<p>But if we're going to carry this data in a typeclass, why aren't we carrying the data of <code>functor.map</code> in a typeclass?</p>

#### [ Scott Morrison (Nov 08 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/147333256):
<p>I have tried this, ..., but it was a long time ago and I don't really remember why I didn't like it then.</p>

#### [ Scott Morrison (Nov 10 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal%20categories/near/147448765):
<p><span class="user-mention" data-user-id="128547">@Michael Jendrusch</span>, I started adding the monoidal structure on any category with products, that should subsume your initial example of <code>Type u</code>. It's not there yet, but I think it's a fun test of our limits library to make sure this is doable with no more effort than in the <code>Type u</code> case.</p>


{% endraw %}
