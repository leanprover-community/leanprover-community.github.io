---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/44395sheavesandsites.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [sheaves and sites](https://leanprover-community.github.io/archive/116395maths/44395sheavesandsites.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Nov 08 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147299236):
<p>Lol, I'm quite sure that the definition of <code>coverage</code> is wrong. I should demand that the collection of covers contains the singletons <code>{id : U ⟶ U}</code> for every <code>U : X</code>.</p>

#### [ Johan Commelin (Nov 08 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147299259):
<p>If I'm right, this is also missing on nLab.</p>

#### [ Johan Commelin (Nov 12 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147532006):
<p>I retract this. There is a comment on nLab pointing out that you don't need to demand that identity morphisms cover. It doesn't change your category of sheaves.</p>

#### [ Kenny Lau (Nov 12 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147532080):
<p>did you say nlab...</p>

#### [ Kenny Lau (Nov 12 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147532144):
<p>man you've gone too far...</p>

#### [ Johan Commelin (Nov 12 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147545193):
<p><code>opens X</code> is now a site!<br>
<a href="https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheaf.lean#L245" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheaf.lean#L245">https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheaf.lean#L245</a></p>

#### [ Johan Commelin (Nov 12 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147545202):
<p>This is one of the ugliest proofs I've written in a long time.</p>

#### [ Johan Commelin (Nov 12 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147545468):
<p>Also, I would like to get some feedback on the definition of the <code>covers</code> for <code>opens X</code>. This is the actual data that goes into a <code>site</code>. The rest doesn't matter, because it's only proofs. (They should of course be faster then what I have now.)<br>
Basically, there are at least three (equivalent) ways to specify the data of <code>covers</code>:<br>
1) <code>covers := λ U Us, U.val = ⨆u∈Us, (u:over _).left.val</code> — take the union in <code>set X</code><br>
2) <code>covers := λ U Us, U = ⨆u∈Us, (u:over _).left</code> — take the "union" in <code>opens X</code><br>
3) <code>covers := λ U Us, U = limits.sigma (λ u∈Us, (u:over _))</code> — take the "union" as a colimit in the category <code>over U</code><br>
Do people already see reasons to choose/discard one of these options?</p>

#### [ Johan Commelin (Nov 12 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147545537):
<p>I currently have option (2). But maybe option (3) is actually better, even though it is high-brow; because it would tie in better to all the facts that we (will) have about functors/limits/etc...</p>

#### [ Reid Barton (Nov 12 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147547765):
<p>I wonder whether using actual families (instead of <code>set</code> everywhere) would make your life easier</p>

#### [ Reid Barton (Nov 12 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147547907):
<p>Maybe this isn't actually causing any difficulty</p>

#### [ Johan Commelin (Nov 12 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147548610):
<p>Hmm, I had that before, and it actually became harder... also, you run into more universe issues, I think.</p>

#### [ Johan Commelin (Nov 13 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147576521):
<p><code>sheaf.lean</code> is now <code>sorry</code>-free. In particular, I have defined the site on a basis of a topology.</p>

#### [ Kevin Buzzard (Nov 13 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147576576):
<p><span class="user-mention" data-user-id="132858">@Ramon Fernandez Mir</span> you might be interested in this. <span class="user-mention" data-user-id="112680">@Johan Commelin</span> where is this work? Is it on github?</p>

#### [ Johan Commelin (Nov 13 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147576586):
<p>My todo-list:</p>
<ul>
<li>Clean up the proofs</li>
<li>Prove that continuous functions to some space <code>T</code> form a sheaf on <code>X</code></li>
<li>Generalise to sheaves with values in <code>C</code> (e.g., <code>C = CommRing</code> or <code>Ab</code>)</li>
<li>Define stalks</li>
<li>Build an API around everything</li>
</ul>

#### [ Johan Commelin (Nov 13 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147576593):
<p><a href="https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheaf.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheaf.lean">https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheaf.lean</a></p>

#### [ Johan Commelin (Nov 13 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147576745):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Would you mind testing your most powerful version of <code>obviously</code> on (parts) of the proofs at the bottom of <code>sheaf.lean</code>? As you can see I'm mostly doing what <code>tidy</code> would do, except that I sprinkle an occasional <code>rw</code> into the mix.</p>

#### [ Johan Commelin (Nov 13 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147576748):
<p>(If you have time for this...)</p>

#### [ Scott Morrison (Nov 13 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147576890):
<p>Hi <span class="user-mention" data-user-id="112680">@Johan Commelin</span> , we should combine/adapt the stuff I wrote on bundled presheaves at some point, with a category structure based on:</p>
<div class="codehilite"><pre><span></span>structure Presheaf :=
(X : Top.{v})
(𝒪 : (opens X)ᵒᵖ ⥤ C)

structure Presheaf_hom (F G : Presheaf.{u v} C) :=
(f : F.X ⟶ G.X)
(c : G.𝒪 ⟹ ((opens.map f).op ⋙ F.𝒪))
</pre></div>

#### [ Scott Morrison (Nov 13 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147576895):
<p>Am I right that you haven't got this yet?</p>

#### [ Scott Morrison (Nov 13 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147576897):
<p>I think most of the other stuff I'd done previously on sheaves is all obsolete by your recent progress.</p>

#### [ Johan Commelin (Nov 13 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147577022):
<p>(I don't have stalks yet <span class="emoji emoji-1f606" title="lol">:lol:</span>)</p>

#### [ Johan Commelin (Nov 13 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147577025):
<p>Why would you want the bundled presheaves?</p>

#### [ Johan Commelin (Nov 13 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147577047):
<p>To define morphisms of ringed spaces?</p>

#### [ Johan Commelin (Nov 13 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147577051):
<p>I think I would first do that unbundled.</p>

#### [ Johan Commelin (Nov 13 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147577899):
<p>Hmmm, I just realised that I don't even know what it means to be a sheaf with values in <code>C</code> when working on an arbitrary site.<br>
I can make sense of it</p>
<ul>
<li>if the site has pullbacks, or</li>
<li>if <code>C</code> is <em>concrete</em> in the sense that it comes with a forgetful functor to <code>Type</code>.</li>
</ul>

#### [ Johan Commelin (Nov 13 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147578584):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Do you have any tips on what the right "go-for-it" route would be in this case?</p>

#### [ Johan Commelin (Nov 13 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147578592):
<p>We want sheaves of rings.<br>
There are 23 definitions that are all math-equivalent.</p>

#### [ Harry Gindi (Nov 13 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580288):
<p>There's no way to do it as a ring object in sheaves?</p>

#### [ Johan Commelin (Nov 13 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580305):
<p>That is one of the 23 possibilities (-;</p>

#### [ Johan Commelin (Nov 13 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580313):
<p>But then you need to connect it to all the useful things that we know already about rings.</p>

#### [ Johan Commelin (Nov 13 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580320):
<p>This is math-trivial, of course</p>

#### [ Harry Gindi (Nov 13 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580363):
<p>A lot of them aren't true for sheafy rings</p>

#### [ Johan Commelin (Nov 13 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580367):
<p>But now you actually need to justify it to a computer.</p>

#### [ Johan Commelin (Nov 13 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580381):
<p>Sure, but there is an extremely large bunch of trivialities that are true</p>

#### [ Harry Gindi (Nov 13 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580399):
<p>Is there any way to work with sheaves directly as nonclassical types?</p>

#### [ Harry Gindi (Nov 13 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580463):
<p>so that all of the theorems for rings that don't use classical assertions hold?</p>

#### [ Johan Commelin (Nov 13 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580575):
<p>What exactly do you mean?</p>

#### [ Johan Commelin (Nov 13 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580580):
<p>Working internally in some topos?</p>

#### [ Johan Commelin (Nov 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580598):
<p>Or you want to lift all constructive results into every topos?</p>

#### [ Johan Commelin (Nov 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580615):
<p>Nothing like that currently exists. And pulling it off would be quite a non-trivial project.</p>

#### [ Harry Gindi (Nov 13 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580710):
<p>Yeah, I agree</p>

#### [ Johan Commelin (Nov 13 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580756):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Do you think the current definition of <code>sheaf</code> is ok?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">sheaf</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="err">𝒳</span> <span class="o">:</span> <span class="n">site</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="n">X</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">F</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">X</span> <span class="o">(</span><span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="bp">//</span> <span class="n">nonempty</span> <span class="o">(</span><span class="n">site</span><span class="bp">.</span><span class="n">sheaf_condition</span> <span class="n">F</span><span class="o">)</span> <span class="o">}</span>
</pre></div>


<p>I need the ugly <code>nonempty</code> because <code>is.iso</code> is not a <code>Prop</code>. What is the correct Lean-idiom for this?</p>

#### [ Scott Morrison (Nov 13 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580770):
<p>Why not just use a sigma type?</p>

#### [ Scott Morrison (Nov 13 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580779):
<p>The category of presheaves will not care about the evidence you provide</p>

#### [ Johan Commelin (Nov 13 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580780):
<p>I want to use <code>full_subcategory</code></p>

#### [ Johan Commelin (Nov 13 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580787):
<p>But maybe I shouldn't?</p>

#### [ Scott Morrison (Nov 13 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580792):
<p>so use <code>sigma_category</code>, which I think hasn't landed in mathlib</p>

#### [ Scott Morrison (Nov 13 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580795):
<p>but is the same idea, it just ignores the extra data</p>

#### [ Scott Morrison (Nov 13 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580839):
<p>If you think about it, this is a perfectly sensible thing to do categorically:</p>

#### [ Johan Commelin (Nov 13 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580842):
<p>Ok... I see. Which branch do I need to merge into <code>sheaf</code> to do that?</p>

#### [ Johan Commelin (Nov 13 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580848):
<p>Yeah, the idea is obvious. I just didn't want to roll my own tooling.</p>

#### [ Scott Morrison (Nov 13 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580850):
<p>you can have something that acts as a full subcategory, but actually makes many copies of the objects that you're keeping, according to the different ways to witness that you want them ...</p>

#### [ Johan Commelin (Nov 13 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580854):
<p>/me is lazy...</p>

#### [ Scott Morrison (Nov 13 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580860):
<p>I think it's only in <code>lean-category-theory</code></p>

#### [ Scott Morrison (Nov 13 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580862):
<p>so it's not just merging a branch</p>

#### [ Johan Commelin (Nov 13 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580876):
<p>Aaah, then I'll leave a TODO above the current definition.</p>

#### [ Harry Gindi (Nov 13 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580886):
<p>Is there documentation for what a sigma-category is?</p>

#### [ Scott Morrison (Nov 13 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580896):
<p>Copy and paste</p>
<div class="codehilite"><pre><span></span>instance sigma_category (Z : C → Type w₁) : category.{(max u₁ w₁) v₁} (Σ X : C, Z X) :=
{ hom  := λ X Y, X.1 ⟶ Y.1,
  id   := λ X, 𝟙 X.1,
  comp := λ _ _ _ f g, f ≫ g }

def sigma_category_inclusion (Z : C → Type u₁) : (Σ X : C, Z X) ⥤ C :=
{ obj := λ X, X.1,
  map&#39; := λ _ _ f, f }

instance full_σ        (Z : C → Type u₁) : full    (sigma_category_inclusion Z)    := by obviously
instance faithful_σ    (Z : C → Type u₁) : faithful (sigma_category_inclusion Z)   := by obviously
</pre></div>

#### [ Scott Morrison (Nov 13 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580925):
<p>into full_subcategory.lean?</p>

#### [ Harry Gindi (Nov 13 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580958):
<p>does it have a non-type-theoretic analogue?</p>

#### [ Johan Commelin (Nov 13 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581050):
<p>Sure, but I don't know if it actually occurs.</p>

#### [ Scott Morrison (Nov 13 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581091):
<p>Sure. Say you have a set of objects C, and a function f : C \to Set. Make a new category with objects (X, Y), where Y is in f(X), and whose morphisms (X, Y) to (X', Y') are just the C-morphisms from X to X'.</p>

#### [ Johan Commelin (Nov 13 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581094):
<p>It would be like taking the category of groups with all functions as morphisms</p>

#### [ Scott Morrison (Nov 13 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581095):
<p>Does it have a name?</p>

#### [ Scott Morrison (Nov 13 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581105):
<p>It just makes f(X) many copies of the object X.</p>

#### [ Harry Gindi (Nov 13 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581171):
<p>it looks like it's related to the 'anafunctor' version of a subcategory?</p>

#### [ Johan Commelin (Nov 13 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581204):
<p><span class="user-mention" data-user-id="137844">@Harry Gindi</span> Here is a math question that I don't know the answer to. In what generality do people speak of sheaves on a site <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>X</mi></mrow><annotation encoding="application/x-tex">X</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">X</span></span></span></span> with values in a category <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>C</mi></mrow><annotation encoding="application/x-tex">C</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07153em;">C</span></span></span></span>?<br>
What assumptions do I need to make on <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>X</mi></mrow><annotation encoding="application/x-tex">X</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">X</span></span></span></span> and/or <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>C</mi></mrow><annotation encoding="application/x-tex">C</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07153em;">C</span></span></span></span>? Is there some grand theory that unifies everything?</p>

#### [ Harry Gindi (Nov 13 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581290):
<p>people sometimes say "sheaves of X" in all kinds of cases, but it only makes sense when X is a subcategory of algebras for some algebraic theory rel set</p>

#### [ Johan Commelin (Nov 13 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581304):
<p>Well, if the site <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>X</mi></mrow><annotation encoding="application/x-tex">X</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">X</span></span></span></span> has pullbacks, then I guess the sheaf condition makes sense in every category <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>C</mi></mrow><annotation encoding="application/x-tex">C</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07153em;">C</span></span></span></span> with equalizers, right?</p>

#### [ Harry Gindi (Nov 13 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581351):
<p>yes, but it is usually the wrong thing</p>

#### [ Johan Commelin (Nov 13 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581356):
<p>Ok, so it works but is useless.</p>

#### [ Harry Gindi (Nov 13 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581368):
<p>I think so, yes</p>

#### [ Johan Commelin (Nov 13 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581438):
<p>Ok, I'll have to think a bit about how to move this forward. I'm not sure if I'm ready for defining all the stuff related to algebraic theories.</p>

#### [ Harry Gindi (Nov 13 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581522):
<p>It might make more sense if you could relativize algebraic stuff to like parameterized types?</p>

#### [ Harry Gindi (Nov 13 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581530):
<p>I don't know, it's really alien to me</p>

#### [ Harry Gindi (Nov 13 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581550):
<p>probably the easiest way is as you said</p>

#### [ Harry Gindi (Nov 13 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581604):
<p>when the category is concrete, being a sheaf with values in C is the same thing as asking that the underlying sheaf of sets is a sheaf</p>

#### [ Harry Gindi (Nov 13 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581646):
<p>I don't know how well that works with e.g. a sheaf of complexes</p>

#### [ Harry Gindi (Nov 13 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581741):
<p>which is like the most important application of sheafy stuff in alg. geom, I think</p>

#### [ Scott Morrison (Nov 13 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581744):
<p>You have to be pretty careful with this statement. It's not just "concrete" (e.g. topological rings have a faithful functor to Set) You also need that the forgetful functor is continuous and reflects isos.</p>

#### [ Scott Morrison (Nov 13 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581830):
<p>At some point I wrote down the statement, but never attempted to prove it:</p>
<div class="codehilite"><pre><span></span>variables {V : Type (u+1)} [𝒱 : large_category V] [has_products.{u+1 u} V] (ℱ : V ⥤ (Type u))
          [faithful ℱ] [category_theory.limits.preserves_limits ℱ] [reflects_isos ℱ]
include 𝒱

-- This is a good project!
def sheaf.of_sheaf_of_types
  (presheaf : (opens X)ᵒᵖ ⥤ V)
  (underlying_is_sheaf : is_sheaf (presheaf ⋙ ℱ)) : is_sheaf presheaf := sorry
</pre></div>

#### [ Scott Morrison (Nov 13 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581858):
<p>(This won't be compatible with Johan's version of presheaves and sheaves, of course.)</p>

#### [ Harry Gindi (Nov 13 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581877):
<p>I wonder if a good way to do this is with internal objects in a topos after all</p>

#### [ Harry Gindi (Nov 13 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581886):
<p>then you could try to follow Hakim's thesis</p>

#### [ Johan Commelin (Nov 13 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581986):
<p>I challenge you to try it <span class="emoji emoji-1f603" title="smiley">:smiley:</span></p>

#### [ Harry Gindi (Nov 13 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581991):
<p>I don't understand how you can say something like categories of nonclassical types satisfyinf Giraud's axioms are categories of sheaves on a site</p>

#### [ Johan Commelin (Nov 13 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582038):
<p>What do you mean?</p>

#### [ Harry Gindi (Nov 13 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582050):
<p>like, we might want to work internally to some Grothendieck topos</p>

#### [ Harry Gindi (Nov 13 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582065):
<p>and the objects there would hopefully be of type "type"</p>

#### [ Johan Commelin (Nov 13 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582066):
<p>Sure. And <code>Type</code> is equivalent to sheaves on <code>unit</code></p>

#### [ Johan Commelin (Nov 13 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582076):
<p>No, for an arbitrary topos the type of the objects wouldn't be <code>Type</code></p>

#### [ Johan Commelin (Nov 13 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582123):
<p>They would be of type <code>X</code>, where <code>X</code> is your topos.</p>

#### [ Harry Gindi (Nov 13 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582126):
<p>then how can you transfer results from type type to type sheafy type</p>

#### [ Johan Commelin (Nov 13 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582129):
<p>And so you have to develop all of type theory internal to topoi. And this hasn't been done yet in Lean. And I don't think it has been done in any theorem prover.</p>

#### [ Johan Commelin (Nov 13 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582142):
<p>To do that "transfer" you would have to build quite a bit of machinery.</p>

#### [ Harry Gindi (Nov 13 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582145):
<p>exactly, it looks daunting</p>

#### [ Johan Commelin (Nov 13 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582151):
<p>Very daunting</p>

#### [ Johan Commelin (Nov 13 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582160):
<p>It would take Mario a whole summer, I'm afraid.</p>

#### [ Harry Gindi (Nov 13 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582218):
<p>one way to do it, maybe, would be to try to prove that any nonclassical theorem in type type holds when you substitute type X for type type when X is a topos?</p>

#### [ Harry Gindi (Nov 13 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582233):
<p>it's not easy</p>

#### [ Harry Gindi (Nov 13 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582320):
<p>It would probably be highly rewarding in terms of work saved</p>

#### [ Harry Gindi (Nov 13 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582598):
<p>I should probably look in e.g. the elephant to see if there is a statement of such a theorem</p>

#### [ Mario Carneiro (Nov 13 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147583484):
<p>I'm afraid I have no idea about the math in this area</p>

#### [ Mario Carneiro (Nov 13 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147583499):
<p>I'm not sure how much of it is important to the modeling question</p>

#### [ Mario Carneiro (Nov 13 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147583644):
<blockquote>
<p>Hmmm, I just realised that I don't even know what it means to be a sheaf with values in <code>C</code> when working on an arbitrary site.<br>
I can make sense of it<br>
* if the site has pullbacks, or<br>
* if <code>C</code> is <em>concrete</em> in the sense that it comes with a forgetful functor to <code>Type</code>.</p>
</blockquote>
<p>Are these two definitions related to each other? Harry says this is not the right notion in some categories?</p>

#### [ Mario Carneiro (Nov 13 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147583678):
<p>If there is a reasonable categorical interpretation of the sheaf operations or what not then that seems like a good place to start</p>

#### [ Mario Carneiro (Nov 13 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147583745):
<p>but it sounds like a "sheaf of rings" is not a sheaf over <code>Ring</code> as I would hope, but rather a ring object in sheaves... unfortunately I don't know any way of relating rings and ring objects in a suitably algorithmic way</p>

#### [ Mario Carneiro (Nov 13 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147583842):
<p>that is, you can define a group object, ring object etc but nothing about these definitions will connect them to the usual algebraic classes, and there won't be a general procedure for inputting a universal algebra and getting a predicate in category theory language</p>

#### [ Mario Carneiro (Nov 13 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147583872):
<p>and "internalization" is not something we can currently do in a nice way, although maybe a tactic could do it in the future</p>

#### [ Johan Commelin (Nov 13 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147585448):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Thanks for your input. I think Harry is saying that it would be best to go for the option with <em>concrete</em> categories, and Scott already gave a mockup of the statement.</p>

#### [ Johan Commelin (Nov 13 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147585465):
<p>You are right that a sheaf of rings is a ring object in sheaves. (At least that is one way to define it.)</p>

#### [ Harry Gindi (Nov 13 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147585780):
<p>I asked a colleague of mine who specializes in topos theory (and has lots of experience with Lean, but the HOTT branch)</p>

#### [ Harry Gindi (Nov 13 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147585838):
<p>oh yeah, he's here, Jonas</p>

#### [ Harry Gindi (Nov 13 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147585865):
<p><span class="user-mention" data-user-id="114636">@Jonas Frey</span></p>

#### [ Johan Commelin (Nov 13 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147586499):
<p>I imagine that a bunch of these problems would go away when using HoTT + univalence</p>

#### [ Harry Gindi (Nov 13 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589162):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I was saying that the notion of a sheaf with values in a category that isn't 'algebraic' in some sense is bad</p>

#### [ Mario Carneiro (Nov 13 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589170):
<p>so what does "algebraic" mean here?</p>

#### [ Harry Gindi (Nov 13 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589185):
<p>admits a finite limit sketch over set, I believe</p>

#### [ Mario Carneiro (Nov 13 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589194):
<p>like what are some simple examples?</p>

#### [ Harry Gindi (Nov 13 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589196):
<p>sheaves of categories are bad, for example</p>

#### [ Mario Carneiro (Nov 13 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589202):
<p>I'm not really sure what the applications are here, what kinds of sheaves are good?</p>

#### [ Harry Gindi (Nov 13 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589247):
<p>the right notion for a sheaf of categories has additional coherence conditions (cocycle conditions) that make them stacks</p>

#### [ Mario Carneiro (Nov 13 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589258):
<p>but I presume these don't come up in the usual cases for some reason?</p>

#### [ Harry Gindi (Nov 13 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589259):
<p>good categories for sheaves: groups, rings, abgroups, things of that nature</p>

#### [ Harry Gindi (Nov 13 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589270):
<p>yeah, basically</p>

#### [ Mario Carneiro (Nov 13 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589330):
<p>So is the "data" of a sheaf all present in an arbitrary category?</p>

#### [ Mario Carneiro (Nov 13 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589340):
<p>or does pullbacks suffice?</p>

#### [ Mario Carneiro (Nov 13 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589364):
<p>and somehow in a "good" category these operations have additional properties that make it work</p>

#### [ Harry Gindi (Nov 13 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589374):
<p>(deleted)</p>

#### [ Harry Gindi (Nov 13 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589430):
<p>sorry, all products</p>

#### [ Harry Gindi (Nov 13 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589438):
<p>because you can have infinite covering families</p>

#### [ Mario Carneiro (Nov 13 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589448):
<p>I think the easy route would be to define what a sheaf is in an arbitrary category with the constructions needed in the definition itself, and then add appropriate regularity conditions for the theorems (or just prove the theorems in particular categories when needed)</p>

#### [ Mario Carneiro (Nov 13 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589497):
<p>I would imagine that it will be easy to retrofit the theorems with more generality as needed</p>

#### [ Harry Gindi (Nov 13 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589498):
<p>Scott's version works better than that</p>

#### [ Harry Gindi (Nov 13 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589514):
<p>it hits all of the ones we care about</p>

#### [ Mario Carneiro (Nov 13 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589516):
<p>I'm not sure how well "concrete categories" in the literal sense of functors to Type work in lean</p>

#### [ Mario Carneiro (Nov 13 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589536):
<p>Scott can say better than me</p>

#### [ Harry Gindi (Nov 13 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589604):
<p>the key feature of sheaves and presheaves is exactly that they are set-valued and the sheaf condition says something about sets</p>

#### [ Harry Gindi (Nov 13 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589691):
<p>having a continuous conservative functor to sets is always satisfied when the category is monadic over sets</p>

#### [ Kevin Buzzard (Nov 13 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589726):
<p>In the perfectoid project we need sheaves of topological rings</p>

#### [ Harry Gindi (Nov 13 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589741):
<p>hmm, how are those even defined?</p>

#### [ Harry Gindi (Nov 13 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589793):
<p>that was exactly the example Scott said would be problematic (topological groups)</p>

#### [ Kevin Buzzard (Nov 13 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589800):
<p>well we only need them on topological spaces, so I think there are no technical issues...</p>

#### [ Harry Gindi (Nov 13 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589829):
<p>Are they pro-rings like completions?</p>

#### [ Harry Gindi (Nov 13 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589933):
<p>Can I see where these are defined in ordinary mathematical language?</p>

#### [ Kevin Buzzard (Nov 13 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589942):
<p>Actually there might be some topological issue. Wait a minute, I'll dig up a reference</p>

#### [ Kevin Buzzard (Nov 13 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590004):
<p><a href="https://www2.math.uni-paderborn.de/fileadmin/Mathematik/People/wedhorn/Lehre/AdicSpaces.pdf" target="_blank" title="https://www2.math.uni-paderborn.de/fileadmin/Mathematik/People/wedhorn/Lehre/AdicSpaces.pdf">https://www2.math.uni-paderborn.de/fileadmin/Mathematik/People/wedhorn/Lehre/AdicSpaces.pdf</a>  remark 8.19 on p80</p>

#### [ Kevin Buzzard (Nov 13 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590030):
<p>The map from F(U) to the stuff in prod_i F(U_i) which agree on overlaps needs to be a homeo rather than just continuous</p>

#### [ Kevin Buzzard (Nov 13 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590087):
<p>I think that this is probably exactly the sheaf axiom for top rings</p>

#### [ Harry Gindi (Nov 13 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590088):
<p>Yeah, I think you could get away with this because they're adic rings</p>

#### [ Kevin Buzzard (Nov 13 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590092):
<p>I am not sure this has anything to do with it</p>

#### [ Kevin Buzzard (Nov 13 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590112):
<p>I think that the point is that to check that a presheaf of top rings is a sheaf, it does not suffice to check that the underlying presheaf of rings is a sheaf</p>

#### [ Kevin Buzzard (Nov 13 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590123):
<p>there is epsilon more to it than this.</p>

#### [ Harry Gindi (Nov 13 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590125):
<p>well, continuous maps between adic rings are the natural transformations between pro-objects</p>

#### [ Kevin Buzzard (Nov 13 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590130):
<p>These rings are not adic rings in general</p>

#### [ Harry Gindi (Nov 13 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590170):
<p>ah</p>

#### [ Kevin Buzzard (Nov 13 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590189):
<p>They are what used to be called "f-adic", which is _not_ "adic + ...", it's "has a subring which is adic + ..."</p>

#### [ Harry Gindi (Nov 13 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590197):
<p>mhm</p>

#### [ Kevin Buzzard (Nov 13 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590202):
<p>They're now called Huber rings</p>

#### [ Kevin Buzzard (Nov 13 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590220):
<p>(terminology due to Scholze)</p>

#### [ Mario Carneiro (Nov 13 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590238):
<p>When I said concrete categories in the literal sense I was comparing to categories that are built on actual sets and functions</p>

#### [ Harry Gindi (Nov 13 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590242):
<p>yeah, this looks like a special situation that isn't usually covered in the classical theory, I think</p>

#### [ Mario Carneiro (Nov 13 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590282):
<p>in which case the forgetful functor is implicit</p>

#### [ Mario Carneiro (Nov 13 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590317):
<p>there is quite a lot you can do with concrete categories built like this</p>

#### [ Harry Gindi (Nov 13 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590355):
<p>in that case, Kevin, maybe the answer is to do a common generalization that covers the usual situation and the one for perfectoid spaces.</p>

#### [ Harry Gindi (Nov 13 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590421):
<p>There are also simplicial sheaves, which have a separate homotopy-theoretic component</p>

#### [ Harry Gindi (Nov 13 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590456):
<p>but that way lies madness</p>

#### [ Harry Gindi (Nov 13 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590545):
<p>and you'd end up trying to do everything in this article: <a href="https://ncatlab.org/nlab/show/model+structure+on+simplicial+presheaves#injectiveprojective__localglobal__presheavessheaves" target="_blank" title="https://ncatlab.org/nlab/show/model+structure+on+simplicial+presheaves#injectiveprojective__localglobal__presheavessheaves">https://ncatlab.org/nlab/show/model+structure+on+simplicial+presheaves#injectiveprojective__localglobal__presheavessheaves</a></p>

#### [ Johan Commelin (Nov 13 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147591580):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I hope the following code is parseable</p>
<div class="codehilite"><pre><span></span><span class="n">T</span> <span class="o">:</span> <span class="n">Top</span><span class="o">,</span>
<span class="n">U</span> <span class="o">:</span> <span class="n">opens</span> <span class="n">X</span><span class="o">,</span>
<span class="n">Us</span> <span class="o">:</span> <span class="n">covering_family</span> <span class="n">U</span><span class="o">,</span>
<span class="n">this</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">over</span> <span class="n">U</span><span class="o">),</span> <span class="n">u</span> <span class="err">∈</span> <span class="n">Us</span> <span class="bp">→</span> <span class="o">(</span><span class="n">opens</span><span class="bp">.</span><span class="n">to_Top</span><span class="bp">.</span><span class="n">obj</span> <span class="o">(</span><span class="n">u</span><span class="bp">.</span><span class="n">left</span><span class="o">)</span> <span class="err">⟶</span> <span class="n">T</span><span class="o">)</span>
<span class="err">⊢</span> <span class="n">opens</span><span class="bp">.</span><span class="n">to_Top</span><span class="bp">.</span><span class="n">obj</span> <span class="o">(</span><span class="err">⨆</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">over</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">u</span> <span class="err">∈</span> <span class="n">Us</span><span class="o">),</span> <span class="n">u</span><span class="bp">.</span><span class="n">left</span><span class="o">)</span> <span class="err">⟶</span> <span class="n">T</span>
</pre></div>


<p>Do you know if we have any stuff in topology that would help here?</p>

#### [ Johan Commelin (Nov 13 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147591673):
<p>What this is saying is: I have a bunch of functions to <code>T</code> defined on <code>u</code>s that cover <code>U</code>. Now I want to build a function <code>U</code> to <code>T</code>.</p>

#### [ Johan Commelin (Nov 13 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147591691):
<p>Of course we need that they agree on overlaps. This is hidden in my context, but it looks ugly, so I didn't paste it.</p>

#### [ Johan Commelin (Nov 13 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147591712):
<p>Ok, so here is a more precise question: how do I check continuity locally?</p>

#### [ Mario Carneiro (Nov 13 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147591776):
<p>as with opens, I think you want a covering_family U to be a type</p>

#### [ Harry Gindi (Nov 13 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147591791):
<p>Can sieves make life easier?</p>

#### [ Harry Gindi (Nov 13 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147591847):
<p>because then you might just prove that every covering family determines a sieve</p>

#### [ Mario Carneiro (Nov 13 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147591941):
<p>why do sheaf and sieve and stack and site all sound so similar? the alliteration is killing me</p>

#### [ Johan Commelin (Nov 13 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147591998):
<blockquote>
<p>because then you might just prove that every covering family determines a sieve</p>
</blockquote>
<p>I am already using sieves.</p>

#### [ Harry Gindi (Nov 13 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592041):
<p>ah, I see, that's good. Much easier to state the sheaf condition that way!</p>

#### [ Johan Commelin (Nov 13 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592046):
<p>Mario, I was quite happy with <code>covering_family</code> being a set. But maybe it should be a type.</p>

#### [ Johan Commelin (Nov 13 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592069):
<blockquote>
<p>ah, I see, that's good. Much easier to state the sheaf condition that way!</p>
</blockquote>
<p>Sure, but now I need to actually prove that something is a sheaf <span class="emoji emoji-1f631" title="scream">:scream:</span></p>

#### [ Mario Carneiro (Nov 13 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592196):
<p>that statement parses, but it isn't provable without stuff about compatibility</p>

#### [ Harry Gindi (Nov 13 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592207):
<p>test case: Every representable is a sheaf wrt the topology generated by universal epimorphic families?</p>

#### [ Johan Commelin (Nov 13 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592302):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Hence my more precise question...</p>

#### [ Johan Commelin (Nov 13 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592369):
<p><span class="user-mention" data-user-id="137844">@Harry Gindi</span> Indeed. I'm proving that continuous functions <code>X → T</code> form a sheaf on <code>X</code>, for a given <code>T</code>.</p>

#### [ Johan Commelin (Nov 13 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592388):
<p>So it is not as general as your test case.</p>

#### [ Harry Gindi (Nov 13 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592452):
<p>I guess then you'd first have to define universal epimorphic families <span class="emoji emoji-1f61b" title="mischievous">:mischievous:</span></p>

#### [ Johan Commelin (Nov 13 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592469):
<p>Feel free to join in <span class="emoji emoji-1f639" title="joy cat">:joy_cat:</span></p>

#### [ Harry Gindi (Nov 13 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592486):
<p>Talk is cheap, that's why I do it so often</p>

#### [ Kenny Lau (Nov 13 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592586):
<p>let's just define the spectrum of a ring fist</p>

#### [ Kenny Lau (Nov 13 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592590):
<p>(sorry, I'm a more concrete guy)</p>

#### [ Johan Commelin (Nov 13 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592607):
<p>I'm working on it Kenny. I'm trying to define ringed spaces.</p>

#### [ Harry Gindi (Nov 13 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592667):
<p>Hom_CRing(R, -): Ring-&gt;Set; where's my big novelty check</p>

#### [ Johan Commelin (Nov 13 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592724):
<p>Harry, one of the first things you learn when working with provers is that there are lots of definitions that are math-trivially equivalent. But proving that they are equivalent in Lean is often very hard.</p>

#### [ Johan Commelin (Nov 13 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592742):
<p>I'm quite sure that there is value in defining a functor from <code>Ring^op</code> to <code>LRS</code>.</p>

#### [ Harry Gindi (Nov 13 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592797):
<p>I know, I'm being silly. This definition I just gave is meaningless even outside a theorem prover</p>

#### [ Harry Gindi (Nov 13 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147593491):
<p>Just saw this on MathOverflow, could be a useful guide: <a href="https://rawgit.com/iblech/internal-methods/master/notes.pdf" target="_blank" title="https://rawgit.com/iblech/internal-methods/master/notes.pdf">https://rawgit.com/iblech/internal-methods/master/notes.pdf</a></p>

#### [ Harry Gindi (Nov 13 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147593526):
<p>especially if you decide to go down the internal logic route</p>

#### [ Reid Barton (Nov 13 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594050):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>, not sure how much progress you made on your gluing continuous functions question, but step 1 is to just construct the glued function even as a function, i.e., disregarding the topology of X, and then check that the glued function actually restricts to the original guys</p>

#### [ Reid Barton (Nov 13 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594103):
<p>then step 2 would be to check continuity, possibly you can use <code>continuous_subtype_nhds_cover</code> for this</p>

#### [ Reid Barton (Nov 13 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594119):
<p>You might find <a href="https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/homotopy_theory/topological_spaces/inter_union.lean" target="_blank" title="https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/homotopy_theory/topological_spaces/inter_union.lean">https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/homotopy_theory/topological_spaces/inter_union.lean</a> a useful guide though there I was only interested in the case of two (closed) subsets</p>

#### [ Johan Commelin (Nov 13 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594216):
<p>Ok, thanks for the tips.</p>

#### [ Reid Barton (Nov 13 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594217):
<p>Step 1 will require <code>choice</code></p>

#### [ Johan Commelin (Nov 13 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594225):
<p>I'm currently trying to build a function.</p>

#### [ Johan Commelin (Nov 13 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594238):
<p>And I haven't come to the point yet where I need choice. But I think I'm close</p>

#### [ Patrick Massot (Nov 13 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594245):
<p>I think this was already discussed here, with a student of Kevin</p>

#### [ Patrick Massot (Nov 13 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594486):
<p><a href="#narrow/stream/116395-maths/subject/Topology.20-.20Beginner/near/130051069" title="#narrow/stream/116395-maths/subject/Topology.20-.20Beginner/near/130051069">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/Topology.20-.20Beginner/near/130051069</a></p>

#### [ Kevin Buzzard (Nov 13 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594545):
<p><span class="user-mention" data-user-id="120726">@Luca Gerolla</span>  wanted to define a continuous function on a closed interval [0,1] by glueing continuous functions on [0,1/2] and [1/2,1]</p>

#### [ Patrick Massot (Nov 13 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594557):
<p>exactly</p>

#### [ Patrick Massot (Nov 13 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594564):
<p>hopefully this is what I linked to</p>

#### [ Harry Gindi (Nov 13 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594583):
<p>I can't get that link to work on mobile</p>

#### [ Johan Commelin (Nov 13 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594681):
<p>Thanks <span class="user-mention" data-user-id="110031">@Patrick Massot</span>, your memory is better than mine.</p>

#### [ Reid Barton (Nov 13 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594772):
<p>I realize that maybe it's not very obvious what the module I linked to is doing--it's showing that for <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>A</mi><mn>0</mn></msub></mrow><annotation encoding="application/x-tex">A_0</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>, <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>A</mi><mn>1</mn></msub></mrow><annotation encoding="application/x-tex">A_1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> closed subsets of a space X, there is a pushout square in Top involving <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>A</mi><mn>0</mn></msub><mo>∩</mo><msub><mi>A</mi><mn>1</mn></msub></mrow><annotation encoding="application/x-tex">A_0 \cap A_1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mbin">∩</span><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>, <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>A</mi><mn>0</mn></msub></mrow><annotation encoding="application/x-tex">A_0</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>, <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>A</mi><mn>1</mn></msub></mrow><annotation encoding="application/x-tex">A_1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>, <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>A</mi><mn>0</mn></msub><mo>∪</mo><msub><mi>A</mi><mn>1</mn></msub></mrow><annotation encoding="application/x-tex">A_0 \cup A_1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mbin">∪</span><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>. For open subsets you would use the other lemma from topology I mentioned, and then it's the same as checking the sheaf condition I guess.</p>

#### [ Harry Gindi (Nov 13 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594850):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> you have to use AC to construct glued maps?</p>

#### [ Harry Gindi (Nov 13 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594873):
<p>that's surprising to me</p>

#### [ Harry Gindi (Nov 13 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594918):
<p>or is this "choice" different from the axiom of choice?</p>

#### [ Reid Barton (Nov 13 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594921):
<p>You could construct a glued map on the quotient type (the disjoint union of the subsets) modulo (points with the same image in X) without choice</p>

#### [ Reid Barton (Nov 13 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594980):
<p>Ah, it is a bit different from the axiom of choice</p>

#### [ Reid Barton (Nov 13 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594988):
<p>In Lean, basically, <code>choice</code> = nonconstructive</p>

#### [ Harry Gindi (Nov 13 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595010):
<p>so how do intuitionists glue maps?</p>

#### [ Reid Barton (Nov 13 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595116):
<p>You need <code>choice</code> to go from "for each x there exists a y such that ..." to a function mapping x to the corresponding y, even if you know that the corresponding y is also unique. So in that sense it's not exactly analogous to the axiom of choice in ZFC</p>

#### [ Reid Barton (Nov 13 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595178):
<p>I don't know. I guess you could try to replace "subset of X" by "map to X whose fibers are subsingletons", but I don't know how far you would get with that.</p>

#### [ Johan Commelin (Nov 13 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595313):
<p>I think I want my covers to be defined as <code>U = colimit u \in Us</code>. Then this sort of problems would go away.</p>

#### [ Reid Barton (Nov 13 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595319):
<p>I have this picture in my mind of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>A</mi><mn>0</mn></msub><mo>×</mo><mo>{</mo><mn>0</mn><mo>}</mo><mo>∪</mo><mo>(</mo><msub><mi>A</mi><mn>0</mn></msub><mo>∩</mo><msub><mi>A</mi><mn>1</mn></msub><mo>)</mo><mo>×</mo><mo>[</mo><mn>0</mn><mo separator="true">,</mo><mn>1</mn><mo>]</mo><mo>∪</mo><msub><mi>A</mi><mn>1</mn></msub><mo>×</mo><mo>{</mo><mn>1</mn><mo>}</mo></mrow><annotation encoding="application/x-tex">A_0 \times \{0\} \cup (A_0 \cap A_1) \times [0, 1] \cup A_1 \times \{1\}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mbin">×</span><span class="mopen">{</span><span class="mord mathrm">0</span><span class="mclose">}</span><span class="mbin">∪</span><span class="mopen">(</span><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mbin">∩</span><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mclose">)</span><span class="mbin">×</span><span class="mopen">[</span><span class="mord mathrm">0</span><span class="mpunct">,</span><span class="mord mathrm">1</span><span class="mclose">]</span><span class="mbin">∪</span><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mbin">×</span><span class="mopen">{</span><span class="mord mathrm">1</span><span class="mclose">}</span></span></span></span> projecting to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>A</mi><mn>0</mn></msub><mo>∪</mo><msub><mi>A</mi><mn>1</mn></msub><mo>⊂</mo><mi>X</mi></mrow><annotation encoding="application/x-tex">A_0 \cup A_1 \subset X</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mbin">∪</span><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mrel">⊂</span><span class="mord mathit" style="margin-right:0.07847em;">X</span></span></span></span>, and not admitting a continuous section over <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>A</mi><mn>0</mn></msub><mo>∪</mo><msub><mi>A</mi><mn>1</mn></msub></mrow><annotation encoding="application/x-tex">A_0 \cup A_1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mbin">∪</span><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>. Don't know if it means anything though.</p>

#### [ Mario Carneiro (Nov 13 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595430):
<p>I think I gave a proof that gluing in arbitrary topological spaces requires choice using roughly that example</p>

#### [ Reid Barton (Nov 13 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595436):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> had a nice example arguing that you really need something noncomputable to glue functions which is ... right.</p>

#### [ Mario Carneiro (Nov 13 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595494):
<p>where by "choice" I mean unique choice</p>

#### [ Mario Carneiro (Nov 13 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595558):
<p>lean doesn't really distinguish between AC, unique choice and LEM</p>

#### [ Mario Carneiro (Nov 13 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595575):
<p>they all follow from the same axiom</p>

#### [ Harry Gindi (Nov 13 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595737):
<p>Can you glue maps of locales without choice?</p>

#### [ Ramon Fernandez Mir (Nov 13 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596063):
<p>I've actually been looking into it. It's in the sheaf branch on the community mathlib.</p>

#### [ Johan Commelin (Nov 13 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596097):
<p>So now I have this goal:</p>
<div class="codehilite"><pre><span></span><span class="o">(</span><span class="err">⨆</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">Us</span><span class="o">}),</span> <span class="o">(</span><span class="n">u</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span><span class="bp">.</span><span class="n">left</span><span class="o">)</span> <span class="bp">=</span> <span class="err">⨆</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">over</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">u</span> <span class="err">∈</span> <span class="n">Us</span><span class="o">),</span> <span class="n">u</span><span class="bp">.</span><span class="n">left</span>
</pre></div>


<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> will say: "I told you that <code>covering_family U</code> should be a type." But it's not (at the moment). How do I solve silly goals like this?</p>

#### [ Johan Commelin (Nov 13 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596117):
<p><span class="user-mention" data-user-id="132858">@Ramon Fernandez Mir</span> Good to see you!</p>

#### [ Mario Carneiro (Nov 13 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596119):
<p>There is a rewrite rule for this</p>

#### [ Johan Commelin (Nov 13 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596132):
<p>I want <code>rewrite_search</code>...</p>

#### [ Mario Carneiro (Nov 13 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596236):
<p><code>supr_subtype</code></p>

#### [ Luca Gerolla (Nov 13 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596268):
<blockquote>
<p><span class="user-mention" data-user-id="120726">@Luca Gerolla</span>  wanted to define a continuous function on a closed interval [0,1] by glueing continuous functions on [0,1/2] and [1/2,1]</p>
</blockquote>
<p>Indeed, I was dealing with continuous functions on two closed sets <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>V</mi><mo separator="true">,</mo><mi>U</mi></mrow><annotation encoding="application/x-tex"> V, U</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.22222em;">V</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.10903em;">U</span></span></span></span> (where <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>U</mi><mo separator="true">,</mo><mi>V</mi></mrow><annotation encoding="application/x-tex">U, V</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.22222em;">V</span></span></span></span> cover the overall domain <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>X</mi></mrow><annotation encoding="application/x-tex">X</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">X</span></span></span></span>) agreeing on their intersection <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>U</mi><mo>∩</mo><mi>V</mi></mrow><annotation encoding="application/x-tex"> U \cap  V</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="mbin">∩</span><span class="mord mathit" style="margin-right:0.22222em;">V</span></span></span></span>  and I needed to construct a continuous function <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>X</mi><mo>→</mo><mi>Y</mi></mrow><annotation encoding="application/x-tex"> X \to Y </annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.22222em;">Y</span></span></span></span>. The code (mainly done by Mario and Kevin) is at <a href="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Topology/Material/pasting_lemma.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Topology/Material/pasting_lemma.lean">https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Topology/Material/pasting_lemma.lean</a>. <br>
Although dealing with a general covering I don't know if it can be of any help.</p>

#### [ Kenny Lau (Nov 13 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596340):
<p><span class="user-mention" data-user-id="120726">@Luca Gerolla</span> wrong thread?</p>

#### [ Mario Carneiro (Nov 13 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596355):
<p>I don't think so</p>

#### [ Kenny Lau (Nov 13 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596373):
<p>what's Luca doing on an nlab thread...</p>

#### [ Johan Commelin (Nov 13 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596381):
<p>He's on a thread about gluing functions.</p>

#### [ Kenny Lau (Nov 13 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596382):
<p><code>\cap</code> <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>∩</mo></mrow><annotation encoding="application/x-tex">\cap</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.55556em;"></span><span class="strut bottom" style="height:0.55556em;vertical-align:0em;"></span><span class="base"><span class="mord">∩</span></span></span></span></p>

#### [ Johan Commelin (Nov 13 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596387):
<p>His post is about gluing functions.</p>

#### [ Luca Gerolla (Nov 13 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596829):
<p>Also continous_if (from mathlib - topology.continuity) turned out  very useful when I had just and ite function. <br>
Look forward to seeing the solution to this more general pasting :)</p>

#### [ Johan Commelin (Nov 13 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147598973):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Here is something that I find a bit annoying to do. I'm trying to prove that the following functor preserves colimits:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">to_Top</span> <span class="o">:</span> <span class="n">opens</span> <span class="n">X</span> <span class="err">⥤</span> <span class="n">Top</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">obj</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span><span class="o">,</span>
          <span class="o">{</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">U</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span>
            <span class="n">str</span> <span class="o">:=</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">topological_space</span> <span class="o">},</span>
  <span class="n">map</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span> <span class="n">V</span> <span class="n">i</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="o">(</span><span class="n">plift</span><span class="bp">.</span><span class="n">down</span> <span class="o">(</span><span class="n">ulift</span><span class="bp">.</span><span class="n">down</span> <span class="n">i</span><span class="o">))</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="o">(</span><span class="n">embedding</span><span class="bp">.</span><span class="n">continuous_iff</span> <span class="n">embedding_subtype_val</span><span class="o">)</span><span class="bp">.</span><span class="n">mpr</span> <span class="n">continuous_subtype_val</span> <span class="bp">⟩</span> <span class="o">}</span>
</pre></div>


<p>Here is what I have so far:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">to_Top</span><span class="bp">.</span><span class="n">preserves_colimits</span> <span class="o">:</span> <span class="n">preserves_colimits</span> <span class="o">(</span><span class="bp">@</span><span class="n">to_Top</span> <span class="n">X</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">preserves</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">J</span> <span class="bp">_</span> <span class="n">K</span> <span class="n">c</span> <span class="n">hc</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">desc</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">s</span><span class="o">,</span> <span class="bp">_</span> <span class="o">}</span> <span class="o">}</span>
</pre></div>


<p>The local context is now:</p>
<div class="codehilite"><pre><span></span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">X</span><span class="o">,</span>
<span class="n">J</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="bp">_</span><span class="n">x</span> <span class="o">:</span> <span class="n">small_category</span> <span class="n">J</span><span class="o">,</span>
<span class="n">K</span> <span class="o">:</span> <span class="n">J</span> <span class="err">⥤</span> <span class="n">opens</span> <span class="n">X</span><span class="o">,</span>
<span class="n">c</span> <span class="o">:</span> <span class="n">limits</span><span class="bp">.</span><span class="n">cocone</span> <span class="n">K</span><span class="o">,</span>
<span class="n">hc</span> <span class="o">:</span> <span class="n">limits</span><span class="bp">.</span><span class="n">is_colimit</span> <span class="n">c</span><span class="o">,</span>
<span class="n">s</span> <span class="o">:</span> <span class="n">limits</span><span class="bp">.</span><span class="n">cocone</span> <span class="o">(</span><span class="n">K</span> <span class="err">⋙</span> <span class="n">to_Top</span><span class="o">)</span>
<span class="err">⊢</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">map_cocone</span> <span class="n">to_Top</span> <span class="n">c</span><span class="o">)</span><span class="bp">.</span><span class="n">X</span> <span class="err">⟶</span> <span class="n">s</span><span class="bp">.</span><span class="n">X</span>
</pre></div>


<p>The annoying thing is the pair <code>c, hc</code>. I would much rather work with <code>hc : has_colimit K</code> and <code>c : colimit K</code>. Because then I can use facts about how this colimit is defined. Of course I can build a unique isomorphism between the <code>c</code> that I got from Lean and the one that I'm interested in. But I wonder if it would make sense to change the setup a bit...</p>

#### [ Johan Commelin (Nov 13 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147599173):
<p>I've pushed all that I have so far. Now I need to start packing to catch a train.</p>

#### [ Johan Commelin (Nov 13 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147599192):
<p>If anyone has good ideas, or wants to refactor this, please go ahead!</p>

#### [ Johan Commelin (Nov 13 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147599215):
<p>I'm just trying to push this category stuff to the limit (no pun intended)</p>

#### [ Reid Barton (Nov 13 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147599555):
<p>I think we can just add a lemma for that.<br>
You're saying you want to prove: if F : C -&gt; D and C already <code>has_colimits</code>, then to prove F preserves colimits it suffices to consider the ones provided by the <code>has_colimits</code> instance.</p>

#### [ Johan Commelin (Nov 13 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147599626):
<p>Yes, but why not just always condider the one provided by <code>has_colimit K</code>, where <code>K</code> is a diagram.</p>

#### [ Patrick Massot (Nov 13 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147599634):
<blockquote>
<p>I'm just trying to push this category stuff to the limit (no pun intended)</p>
</blockquote>
<p>When we'll have that <code>to_dual</code> tactic, you'll be able to pull this category stuff to the colimit without any extra effort!</p>

#### [ Reid Barton (Nov 13 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147599670):
<p>Because the concept of preserving colimits doesn't depend on a choice of colimits</p>

#### [ Johan Commelin (Nov 13 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147599690):
<p>I see... you're probably right. I don't yet fully grasp the details of the API</p>

#### [ Johan Commelin (Nov 13 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147599771):
<p>But your suggested lemma would also fix this problem.</p>

#### [ Kevin Buzzard (Nov 13 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147601888):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> <span class="user-mention" data-user-id="110064">@Kenny Lau</span> -- <span class="user-mention" data-user-id="132858">@Ramon Fernandez Mir</span> asks me exactly what you are going to be doing regarding Spec of a ring. Ramon is supposed to be completely refactoring the scheme project as part of his MSc thesis; I got him to look at locally ringed spaces but now these are done modulo the assertion that the category of rings has all colimits. Then Kenny mentioned Spec -- I think it would just be less nervy for us if we knew exactly what you guys were planning on doing and what Ramon can do (he has written thousands of lines of Coq code but is new to Lean). Currently we need that colimits exist in the category of commutative rings, and that the spectrum of a ring is a locally ringed space (which of course is a lot of work, even though it's in some sense done already). The first step towards this is that the spectrum of a ring has a presheaf of rings on the basis of open sets <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>D</mi><mo>(</mo><mi>f</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">D(f)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.02778em;">D</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">)</span></span></span></span>. Shall I tell him to do this or will someone else do it by the weekend? It would be good if we could work together on this (although of course there is plenty plenty to do -- e.g. this Gamma Spec adjointness is a goal I have in mind for Ramon, something Johan suggested months ago -- and products of schemes is another thing).</p>

#### [ Kevin Buzzard (Nov 13 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147602049):
<p>Of course I know all of this is already done in the schemes project -- the point is that we want to do it as a test of the category theory stuff; in the past we did it all "by hand".</p>

#### [ Kevin Buzzard (Nov 13 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147604152):
<p>I think I know how to prove that colimits exist in the category of commutative rings -- can I get Ramon to do this or <span class="user-mention" data-user-id="110064">@Kenny Lau</span> are you likely do just randomly do this at some point in the next few days?</p>

#### [ Kevin Buzzard (Nov 13 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147604211):
<p>It will be quite a good stress test of Johannes' multivariable polynomial work I think.</p>

#### [ Johan Commelin (Nov 13 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611121):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Yes, collaboration is good. I have no intention to "mow away the grass" before Ramon's feet.<br>
Here is a question for you: do you intend to make things mathlib-ready? Is the endgoal a PR to mathlib?</p>
<p>My goal is to get a theory of sheaves that is ready for the perfectoid project.</p>

#### [ Johan Commelin (Nov 13 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611202):
<p>Concerning colimits in CommRing: do all of them exist? Or only the directed ones?</p>

#### [ Kevin Buzzard (Nov 13 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611234):
<p>I convinced myself this afternoon that they all existed</p>

#### [ Johan Commelin (Nov 13 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611284):
<p>Sheaves of rings seems to be a bit of an issue. I'm not yet sure how to define them. Once we have those, I'll leave it up to Ramon to define LRS. I will not touch <code>Spec</code> or anything close to it (-;</p>

#### [ Reid Barton (Nov 13 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611297):
<p>They do all exist</p>

#### [ Johan Commelin (Nov 13 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611305):
<p>I do intend to define stalks. So I might get close to LRS...</p>

#### [ Kevin Buzzard (Nov 13 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611313):
<p>via some big standard universal construction -- given a diagram in CommRing, let T0 be the polynomial ring over Z with variables the disjoint union of all the rings in the diagram, and then quotient out by the relations making all of the canonical maps ring homs</p>

#### [ Johan Commelin (Nov 13 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611342):
<p>I would not mind at all if Ramon works on a branch of community mathlib and regularly pull and pushes to the <code>sheaf</code> branch.</p>

#### [ Kevin Buzzard (Nov 13 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611388):
<p>The "bad" news is that this all seems to be some special case of some big theory due to Lawvere and we could spend forever formalising that instead</p>

#### [ Kevin Buzzard (Nov 13 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611425):
<p>(existence of limits and colimits in some big gneerality for some algebraic categories or something)</p>

#### [ Johan Commelin (Nov 13 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611521):
<p>Right. So we just do rings by hand first. Like you did schemes by hand first. This seems to be what Mario would tell us to do anyway.</p>

#### [ Kevin Buzzard (Nov 13 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611540):
<p>Right -- so <span class="user-mention" data-user-id="110064">@Kenny Lau</span> are you happy if <span class="user-mention" data-user-id="132858">@Ramon Fernandez Mir</span> proves existence of colimits in the category of commutative rings?</p>

#### [ Kevin Buzzard (Nov 13 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611550):
<p>In a relatively "hands-on" way, not using Lawvere anything</p>

#### [ Johan Commelin (Nov 13 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611586):
<p>Be aware that Scott already has some general machinery in this direction. I guess you only need coproducts and coequalisers.</p>

#### [ Kevin Buzzard (Nov 13 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611712):
<p>I am not 100% sure whether this makes life any easier in this case</p>

#### [ Kevin Buzzard (Nov 13 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611817):
<p>in the sense that now instead of making one gigantic commutative polynomial ring in a huge set of variables and quotienting out by an ideal generated by terms of two types and then proving something about it, you'll have to build two such rings and prove something about each of them.</p>

#### [ Johan Commelin (Nov 13 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611967):
<p>It would be useful to know that coproducts are defeq to tensor products, I assume...</p>

#### [ Kevin Buzzard (Nov 13 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147612367):
<p>funny isn't it. For products and subobjects you feel like you've made progress. But colimits are quotients so it's always going to be a pain I think. I don't even really understand what the coproduct of an arbitrary set of rings looks like -- it seems to be some sort of direct limit of finite tensor products -- but of course we haven't built direct limits yet so there's a danger of going round in circles here.</p>

#### [ Kevin Buzzard (Nov 13 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147612491):
<blockquote>
<p>Here is a question for you: do you intend to make things mathlib-ready? Is the endgoal a PR to mathlib?</p>
</blockquote>
<p>I don't even know if Mario would be interested in hosting schemes (and I've not asked) -- my goal is to take the crappy code which I wrote so I could learn how to write Lean code, and replace it with code which is sufficiently respectable to get a publication. I've not thought about mathlib at all.</p>

#### [ Johan Commelin (Nov 13 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147613037):
<p>I think there are two options:</p>
<ul>
<li>either stuff like this goes into mathlib,</li>
<li>or the Lean community comes up with a good strategy to have decentralised libraries that work together nicely as dependencies of other projects.</li>
</ul>

#### [ Mario Carneiro (Nov 13 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147613059):
<p>The construction you sketched is clearly a composition of two constructions, why not formalize that?</p>

#### [ Johan Commelin (Nov 13 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147613110):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Do you want schemes in mathlib?</p>

#### [ Mario Carneiro (Nov 13 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147613114):
<p>I want polished code in mathlib</p>

#### [ Johan Commelin (Nov 13 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147613127):
<p>Do you want polished schemes in mathlib?</p>

#### [ Mario Carneiro (Nov 13 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147613141):
<p>sure, if that interests yous</p>

#### [ Mario Carneiro (Nov 13 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147613160):
<p>there seem to be a lot of intermediate steps though</p>

#### [ Johan Commelin (Nov 13 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147613162):
<p>It interests mes and about 65% of all Field medalists.</p>

#### [ Johan Commelin (Nov 13 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147613239):
<p>There's a lot of intermediate steps because I'm trying to write reusable code.</p>

#### [ Reid Barton (Nov 13 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147613596):
<p>I'm not sure which construction Mario is referring to</p>

#### [ Mario Carneiro (Nov 13 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147615817):
<blockquote>
<p>via some big standard universal construction -- given a diagram in CommRing, let T0 be the polynomial ring over Z with variables the disjoint union of all the rings in the diagram, and then quotient out by the relations making all of the canonical maps ring homs</p>
</blockquote>

#### [ Mario Carneiro (Nov 13 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147615855):
<p>we already have the first part, and the second part should generalize to "given a bunch of functions(?) make them all ring homs"</p>

#### [ Scott Morrison (Nov 13 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147624123):
<p>I think, unfortunately, that eventually we will want to do all the varieties of colimits in CommRing separately.</p>

#### [ Scott Morrison (Nov 13 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147624194):
<p>We should do the general colimit, we should also do the filtered colimit (which is much easier), we should do coproducts, we should do binary coproducts. General nonsense says you don't need to prove any comparison theorems relating these, happily.</p>

#### [ Scott Morrison (Nov 13 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147624227):
<p>Later, various bits of general machinery about algebraic categories will give us the filtered colimits "for free"</p>

#### [ Scott Morrison (Nov 13 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147624240):
<p>but someone should do the construction in CommRing first as a warmup.</p>

#### [ Scott Morrison (Nov 13 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147624259):
<p>I don't know the Lawvere stuff; maybe later there's some generality that gives us all colimits in CommRing too?</p>

#### [ Kevin Buzzard (Nov 13 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147625299):
<p>Ok so Ramon and I will take on the task of general colimits. I'm a bit unsure about whether working in this generality will actually cause problems when we want to prove that the stalks for an affine scheme are local, but let's wait and see!</p>

#### [ Scott Morrison (Nov 13 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147629404):
<p>Are you sure you don't want to do filtered colimits first, <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>? They are both easier to construct, and more useful! (Because they're all that's needed for stalks, and will make arguments about stalks easier.)</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630367):
<p>The way Johan or you had set up locally ringed spaces relied on the fact that CommRing had colimits</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630421):
<p>I don't know what a filtered colimit is. I know what a directed set is. Is it sort-of the same thing?</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630462):
<p>aah I now know that a filtered colimit is a categorification of a directed set</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630538):
<p>So I guess I don't know where to stop here. Why not just do colimits over a directed partial order? They are both easier to construct, and more useful! (Because they're all that's needed for stalks, and will make arguments about stalks easier.)</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630555):
<p>And Kenny did them already :P</p>

#### [ Reid Barton (Nov 13 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630640):
<p>Well, filtered is the right level of generality for the fact that you can compute the colimit in Set</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630661):
<p>but colimits in Set are completely different to colimits in CommRing</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630669):
<p>or am I misunderstanding? (presumably)</p>

#### [ Reid Barton (Nov 13 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630680):
<p>General ones are, but filtered ones are not</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630685):
<p>Oh I see!</p>

#### [ Scott Morrison (Nov 13 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630803):
<p>I will add filtered colimits (in the simplest sense, not Reid's kappa-filtered ones) to the limits branch shortly. (Just the definition!)</p>

#### [ Scott Morrison (Nov 13 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630858):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>, Johannes asked me to rebase the limits branch; prepare for trouble. :-)</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630866):
<p>So <span class="user-mention" data-user-id="132858">@Ramon Fernandez Mir</span> would be interested in this. People seem to be suggesting that the definition here <a href="https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/presheaves/locally_ringed.lean" target="_blank" title="https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/presheaves/locally_ringed.lean">https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/presheaves/locally_ringed.lean</a> which uses arbitrary colimits is not wise?</p>

#### [ Scott Morrison (Nov 13 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630872):
<p>Yes</p>

#### [ Scott Morrison (Nov 13 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630878):
<p>That isn't wise. :-)</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630892):
<p>and instead of <code>stalk_at</code> one should use something else?</p>

#### [ Scott Morrison (Nov 13 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630907):
<p>I think <code>stalk_at</code> will be exactly the same</p>

#### [ Scott Morrison (Nov 13 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630960):
<p>We'll just change the typeclass provided, from <code>has_colimits</code> to <code>has_filtered_colimits</code></p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630966):
<p>I see. And that doesn't break anything else?</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630973):
<p>When teaching is finished I'm going to be cloning this repo finally</p>

#### [ Scott Morrison (Nov 13 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630980):
<p>Magic will then notice that the category of open sets containing x is filtered, and so use the <code>has_filtered_colimits</code> instance,</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630984):
<p>at the minute cloning it would lead me astray</p>

#### [ Scott Morrison (Nov 13 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631004):
<p>which will provide an nice construction of the colimit (as a quotient of a disjoint union, just like in Set), rather than the huge one in terms of tensor products.</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631007):
<p>Would magic work for sheaves on a basis? For sheaves on a site?</p>

#### [ Scott Morrison (Nov 13 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631014):
<p>That I don't know.</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631032):
<p>I had never seen the construction of a colimit in CommRing until today, when I figured it out for myself. I did not use tensor products. What trick did I miss?</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631053):
<p>I just made a polynomial ring over Z with variables the disjoint union of all the rings in the diagram</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631056):
<p>and then quotiented</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631112):
<p>I understand that for two rings a coproduct is the tensor product</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631119):
<p>but I couldn't see how this generalised to infinitely many rings</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631132):
<p>it seemed to be a direct limit of tensor produts, but to make direct limits you  want to take coproducts again</p>

#### [ Scott Morrison (Nov 13 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631157):
<p>oh, okay, maybe I didn't think very hard about the infinite diagram case, either :-)</p>

#### [ Scott Morrison (Nov 13 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631173):
<p>(I had never thought about any of this (nor knew what a site was, etc) until Lean came along. :-)</p>

#### [ Reid Barton (Nov 13 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631237):
<p>Well... it's the filtered colimit of all the ways to take a coproduct of finitely many of the rings</p>

#### [ Reid Barton (Nov 13 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631238):
<p>and filtered colimits are easy</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631245):
<p>Is there a general story?</p>

#### [ Reid Barton (Nov 13 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631246):
<p>That said, the construction you gave is the simplest one and it has essentially nothing to do with rings in particular</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631256):
<p>Reducing a general colimit to a filtered colimit?</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631348):
<p>I still don't know whether we should just stick to filtered (0,1)-categories</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631363):
<p>i.e. directed sets (I should stop looking at nlab)</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631372):
<p>Oh, Reid's argument perhaps resolves this -- if it works over set then take it</p>

#### [ Reid Barton (Nov 13 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631433):
<p>Directed colimits will be somewhat easier notationally and you don't need them unless you want stalks for some site which is not itself a poset. I think.</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631440):
<p>I think the etale site is the simplest example of this that I know</p>

#### [ Reid Barton (Nov 13 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631441):
<p>Er, don't need filtered colimits unless ..., of course.</p>

#### [ Kevin Buzzard (Nov 13 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631458):
<p>and next year when we're doing etale cohomology we'll need etale sites</p>

#### [ Reid Barton (Nov 13 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631469):
<p>I think it is safe to assume that by the time we want to do etale cohomology we will have filtered colimits of rings</p>

#### [ Reid Barton (Nov 13 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631531):
<p>You can actually build filtered colimits from directed ones, so it doesn't lose any great generality to work with directed ones for some purposes</p>

#### [ Kevin Buzzard (Nov 14 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147633659):
<blockquote>
<p>Magic will then notice that the category of open sets containing x is filtered, and so use the <code>has_filtered_colimits</code> instance,</p>
</blockquote>
<p>There's something I can't get to add up here. Say there's a <code>has_colimits</code> instance and also a simpler <code>has_filtered_colimits</code> instance. Now let's say I'm trying to take a colimit and it happens to be filtered. If Lean uses the <code>has_colimits</code> instance then the colimit will be constructed in one way, but if Magic notices that the colimit is filtered then it could construct it using the simpler filtered colimit construction. The two constructions will give canonically isomorphic, but probably not defeq, objects, and doesn't this give rise to a diamond?</p>

#### [ Scott Morrison (Nov 14 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147638007):
<p>I have to admit I don't know how bad a problem this is going to be!</p>

#### [ Reid Barton (Nov 14 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147638987):
<p>You also don't necessarily <em>have</em> to put your filtered colimits into the type class system. You can just define and use them directly.</p>

#### [ Harry Gindi (Nov 14 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147640447):
<p>the general statement comes from the theory of locally presentable categories</p>

#### [ Harry Gindi (Nov 14 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147640571):
<p>every object can be given as a filtered colimit of finite pushouts of compact (i.e. finitely (resp Kappa)-presentable) objects, iirc the statement correctly</p>

#### [ Harry Gindi (Nov 14 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147640591):
<p>and iirc CRing has only a single generator, Z[x]</p>

#### [ Harry Gindi (Nov 14 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147640677):
<p>You don't need to work with Lawvere theories to do this stuff, you might be fine doing the locPres machinery and then proving algebraic categories you care about are LocPres</p>

#### [ Harry Gindi (Nov 14 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147640684):
<p>standard reference is Adamek-Rosicky</p>

#### [ Harry Gindi (Nov 14 2018 at 03:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147640760):
<p>It seems a lot less complicated than doing Lawvere theories generally</p>

#### [ Harry Gindi (Nov 14 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147640896):
<p>The general argument is useful in other places, iirc. Grothendieck first used this style of argument in the Tohoku paper</p>

#### [ Harry Gindi (Nov 14 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147640956):
<p>proving that the category of abelian sheaves has enough injectives, but I forget the details</p>

#### [ Johan Commelin (Nov 14 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147649975):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Maybe we should change the definition of <code>stalk</code> a tiny little bit, and write <code>filtered_colimit</code> instead of <code>colimit</code>. That would take care of your issue, I think.</p>

#### [ Kevin Buzzard (Nov 14 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147650968):
<p>This is a diamond-like issue but one level up. With diamonds you might end up with two objects which are equal but the proof isn't rfl. Here the objects are not even equal, merely canonically isomorphic</p>

#### [ Johan Commelin (Nov 14 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147652970):
<p>I see what you mean. And I think this is showing that the current type class system might not be a good fit for categorical stuff (wait till we want to do higher-categorical stuff...). But maybe we can just ignore the issue for now, and hope  that Lean 4 will solve this issue before we hit serious problems.</p>

#### [ Johan Commelin (Nov 15 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147739873):
<p>This is pretty ugly:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">extend</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">X</span> <span class="n">C</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">obj</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span><span class="o">,</span> <span class="n">limit</span> <span class="o">((</span><span class="n">comma</span><span class="bp">.</span><span class="n">fst</span> <span class="o">(</span><span class="n">full_subcategory_inclusion</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_obj</span> <span class="n">U</span><span class="o">))</span><span class="bp">.</span><span class="n">op</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">),</span>
  <span class="n">map</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span> <span class="n">V</span> <span class="n">i</span><span class="o">,</span>
    <span class="k">show</span> <span class="o">(</span><span class="n">limits</span><span class="bp">.</span><span class="n">limit</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">op</span> <span class="o">(</span><span class="n">comma</span><span class="bp">.</span><span class="n">fst</span> <span class="o">(</span><span class="n">full_subcategory_inclusion</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_obj</span> <span class="n">U</span><span class="o">))</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">)</span> <span class="err">⟶</span>
        <span class="n">limits</span><span class="bp">.</span><span class="n">limit</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">op</span> <span class="o">(</span><span class="n">comma</span><span class="bp">.</span><span class="n">fst</span> <span class="o">(</span><span class="n">full_subcategory_inclusion</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_obj</span> <span class="n">V</span><span class="o">))</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">)),</span>
    <span class="k">begin</span>
      <span class="k">have</span> <span class="n">foo</span> <span class="o">:=</span> <span class="n">limit</span><span class="bp">.</span><span class="n">pre</span> <span class="o">((</span><span class="n">comma</span><span class="bp">.</span><span class="n">fst</span> <span class="o">(</span><span class="n">full_subcategory_inclusion</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_obj</span> <span class="n">U</span><span class="o">))</span><span class="bp">.</span><span class="n">op</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">)</span> <span class="o">(</span><span class="n">extend</span><span class="bp">.</span><span class="n">aux</span> <span class="n">i</span><span class="o">),</span>
      <span class="n">dsimp</span> <span class="o">[</span><span class="n">extend</span><span class="bp">.</span><span class="n">aux</span><span class="o">]</span> <span class="n">at</span> <span class="n">foo</span><span class="o">,</span>
      <span class="n">convert</span> <span class="n">foo</span><span class="o">,</span>
      <span class="n">swap</span> <span class="mi">3</span><span class="o">,</span> <span class="n">assumption</span>
    <span class="kn">end</span> <span class="o">}</span>
</pre></div>

#### [ Reid Barton (Nov 15 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147740652):
<p>Why isn't the <code>map</code> field just an application of <code>limit.pre</code>?</p>

#### [ Reid Barton (Nov 15 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147740706):
<p>what goal is the last line solving?</p>

#### [ Reid Barton (Nov 15 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147741081):
<p>My guess is that representing slice categories as comma categories is actually not a good idea in Lean, because the isomorphism (punit -&gt; a) = a is not enough of an equality</p>

#### [ Reid Barton (Nov 15 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147741481):
<p>Did you actually manage to prove the map_id and map_comp fields?</p>

#### [ Johan Commelin (Nov 15 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147741721):
<p>Not yet, still working on it.</p>

#### [ Johan Commelin (Nov 15 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147741761):
<p>Note that I'm not taking a slice category, although it almost is.</p>

#### [ Johan Commelin (Nov 15 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147741857):
<p>This is opens in <code>B</code> that are contained in <code>U</code>, but <code>U</code> is not in <code>B</code>.</p>

#### [ Reid Barton (Nov 15 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742182):
<p>Oh, I see</p>

#### [ Reid Barton (Nov 15 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742355):
<p>If these are presheaves of sets, then there's an easier way to write the formula</p>

#### [ Reid Barton (Nov 15 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742375):
<p>it's the same as the right Kan extension, right?</p>

#### [ Johan Commelin (Nov 15 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742424):
<p>Hmmm... I think so.</p>

#### [ Johan Commelin (Nov 15 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742430):
<p>If you want to help, please do so.</p>

#### [ Johan Commelin (Nov 15 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742437):
<p>Lean is fighting back hard (-;</p>

#### [ Johan Commelin (Nov 15 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742454):
<p>Maybe we should do it for a general map between sites, in that case.</p>

#### [ Reid Barton (Nov 15 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742530):
<p>If E is the extended presheaf then we should have E(U) = Hom(yU, E) = Hom(R(yU), F) where R is the restriction of a presheaf on C to a presheaf on B</p>

#### [ Reid Barton (Nov 15 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742547):
<p>so E is the composition y, then R, then Hom(-, F)</p>

#### [ Reid Barton (Nov 15 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742567):
<p>Yes, that might help as well... at least for clarity</p>

#### [ Johan Commelin (Nov 15 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742652):
<p>Ok, I think this is a nice way to do it!</p>

#### [ Johan Commelin (Nov 15 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742680):
<p>I don't yet see why it is the same thing as in my special case</p>

#### [ Johan Commelin (Nov 15 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742806):
<p>Aah, <code>U</code> is the colimit of all the <code>Ui ∈ B</code> that are contained in <code>U</code>. Now pull this through <code>Hom(_, F)</code> and you get a limit.</p>

#### [ Reid Barton (Nov 15 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743096):
<p>You might find it useful to borrow <a href="https://github.com/leanprover-community/mathlib/blob/adjunctions/category_theory/presheaf.lean#L85" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/adjunctions/category_theory/presheaf.lean#L85">https://github.com/leanprover-community/mathlib/blob/adjunctions/category_theory/presheaf.lean#L85</a></p>

#### [ Reid Barton (Nov 15 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743119):
<p>I think you will want to apply it twice</p>

#### [ Reid Barton (Nov 15 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743129):
<p>In your setup you have a functor B -&gt; C, right?</p>

#### [ Johan Commelin (Nov 15 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743202):
<p>What do you mean?</p>

#### [ Johan Commelin (Nov 15 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743262):
<p><code>B</code> is a basis, and it has an inclusion into <code>opens X</code>.</p>

#### [ Johan Commelin (Nov 15 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743276):
<p>I have a presheaf on <code>B</code></p>

#### [ Reid Barton (Nov 15 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743300):
<p>Okay so let's call <code>opens X</code> <code>C</code> for now</p>

#### [ Johan Commelin (Nov 15 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743339):
<p>Aaah, <code>C</code> was my category of coefficients so far</p>

#### [ Reid Barton (Nov 15 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743342):
<p>ah</p>

#### [ Johan Commelin (Nov 15 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743355):
<p>But maybe I should stop worrying about coefficients, and only focus on <code>Type</code>.</p>

#### [ Reid Barton (Nov 15 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743373):
<p>Well this formula won't work unless the values are in Type</p>

#### [ Johan Commelin (Nov 15 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743496):
<p>Right, so I should forget about <code>C</code></p>

#### [ Johan Commelin (Nov 15 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743523):
<p>And sheaves of rings will require some extra thought</p>

#### [ Reid Barton (Nov 15 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743525):
<p>Okay, in that case let me just use the names from the thing I linked above, so you have a functor C -&gt; D</p>

#### [ Reid Barton (Nov 15 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743544):
<p>If you apply <code>restricted_yoneda</code> to it, you get a functor D -&gt; Set^C^op</p>

#### [ Reid Barton (Nov 15 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743555):
<p>and if you apply <code>restricted_yoneda</code> to that, you get a functor Set^C^op -&gt; Set^D^op</p>

#### [ Reid Barton (Nov 15 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743559):
<p>and that should be the right Kan extension along the original functor</p>

#### [ Reid Barton (Nov 15 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743982):
<p>the thing I called "Ry" earlier is another, possibly better way to write <code>restricted_yoneda</code></p>

#### [ Johan Commelin (Nov 15 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743992):
<p>Sorry, as student entered my office. So I have to wait a while with this thing.</p>

#### [ Johan Commelin (Nov 15 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147746533):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Hmmm... morphisms of sites seem to be non-trivial. I don't think I want to do them now, unless you want to join in. We would need to explain Lean this definition <a href="https://ncatlab.org/nlab/show/flat+functor#SiteValuedFunctors" target="_blank" title="https://ncatlab.org/nlab/show/flat+functor#SiteValuedFunctors">https://ncatlab.org/nlab/show/flat+functor#SiteValuedFunctors</a></p>

#### [ Reid Barton (Nov 15 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147747568):
<p>Right... so concretely I guess your actual goal is to show that the extended presheaf is actually a sheaf?</p>

#### [ Reid Barton (Nov 15 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147747732):
<p>You might want to pick a fact to prove, and work backwards from there</p>

#### [ Reid Barton (Nov 15 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147747750):
<p>Otherwise you can enter a swamp of things you could formalize and choices of definitions you could make</p>

#### [ Johan Commelin (Nov 15 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147751358):
<p>Right. I want to get an equivalence of categories between <code>sheaf B</code> and <code>sheaf X</code>. That is a concrete goal that I definitely want to reach.</p>

#### [ Johan Commelin (Nov 15 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147753284):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> So which approach would you suggest now? Maybe the one with Kan extensions is best? Because it will generalise later on?</p>

#### [ Johan Commelin (Nov 15 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147753315):
<p>Hmmm, I'm being called for an early dinner. See you later.</p>

#### [ Johan Commelin (Nov 15 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147762987):
<p><span class="emoji emoji-1f923" title="rolling on the floor laughing">:rolling_on_the_floor_laughing:</span> This error is hilarious:</p>
<div class="codehilite"><pre><span></span><span class="n">type</span> <span class="n">mismatch</span> <span class="n">at</span> <span class="n">application</span>
  <span class="n">set</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">over</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">u</span><span class="o">}</span> <span class="n">U</span><span class="o">)</span>
<span class="n">term</span>
  <span class="n">over</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">u</span><span class="o">}</span> <span class="n">U</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="kt">Type</span> <span class="n">u</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="kt">Type</span> <span class="n">u</span>
</pre></div>

#### [ Johan Commelin (Nov 15 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147767061):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> How does this look?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">restrict</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">X</span> <span class="err">⥤</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">presheaf</span> <span class="n">B</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">obj</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">F</span><span class="o">,</span> <span class="o">(</span><span class="n">full_subcategory_inclusion</span> <span class="n">B</span><span class="o">)</span><span class="bp">.</span><span class="n">op</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">,</span>
  <span class="n">map</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">f</span><span class="o">,</span> <span class="n">whisker_left</span> <span class="bp">_</span> <span class="n">f</span> <span class="o">}</span>

<span class="n">def</span> <span class="n">extend</span> <span class="o">:</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">presheaf</span> <span class="n">B</span> <span class="err">⥤</span> <span class="n">presheaf</span> <span class="n">X</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">obj</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">F</span><span class="o">,</span> <span class="n">yoneda</span><span class="bp">.</span><span class="n">op</span> <span class="err">⋙</span> <span class="n">restrict</span><span class="bp">.</span><span class="n">op</span> <span class="err">⋙</span> <span class="n">yoneda</span><span class="bp">.</span><span class="n">obj</span> <span class="n">F</span><span class="o">,</span>
  <span class="n">map</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">F</span> <span class="n">G</span> <span class="n">f</span><span class="o">,</span> <span class="n">whisker_left</span> <span class="bp">_</span> <span class="err">$</span> <span class="n">whisker_left</span> <span class="bp">_</span> <span class="err">$</span> <span class="n">yoneda</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span> <span class="o">}</span>
</pre></div>


<p>I think you gave a very good suggestion!</p>

#### [ Johan Commelin (Nov 15 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147767734):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> I think it makes sense to merge your <code>presheaf.lean</code> with parts of my <code>sheaf.lean</code>. What would be the best approach? Should I merge your branch into mine?</p>

#### [ Johan Commelin (Nov 15 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147767788):
<p>I would like to prove that <code>restrict</code> and <code>extend</code> form an adjunction anyway.</p>

#### [ Reid Barton (Nov 16 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147783569):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> Feel free to merge my branch into yours of course, though I will note that I intend to try out a redesign of adjunctions at some point</p>

#### [ Johan Commelin (Nov 20 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024110):
<p>I'm not sure if I'm using things in the right way. I'm trying to write</p>
<div class="codehilite"><pre><span></span><span class="k">let</span> <span class="n">G1</span> <span class="o">:=</span> <span class="o">(</span><span class="n">equiv_of_iso</span> <span class="n">D</span><span class="o">)</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">subtype_equiv_of_subtype</span><span class="bp">.</span><span class="o">{(</span><span class="n">u</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">u</span><span class="bp">+</span><span class="mi">1</span><span class="o">)}</span> <span class="n">Eeq</span><span class="o">),</span>
</pre></div>


<p>where <code>D : F.obj ≅ {p // horrible p}</code> is isomorphisms between a type and a subtype in the category <code>Type u</code> which I turn into an equiv.<br>
I then want to replace the horrible right hand side with a subtype of something else, so I thought, lets use transitivity of <code>equiv</code> and feed it <code>Eeq</code>, which is:</p>
<div class="codehilite"><pre><span></span><span class="n">Eeq</span> <span class="o">:</span> <span class="o">(</span><span class="n">limits</span><span class="bp">.</span><span class="n">sigma</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="bp">+</span><span class="mi">1</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">Ui</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">c</span><span class="o">}),</span> <span class="n">yoneda</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">u</span><span class="o">}</span><span class="bp">.</span><span class="n">obj</span> <span class="o">((</span><span class="n">Ui</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span><span class="bp">.</span><span class="n">left</span><span class="o">))</span> <span class="err">⟶</span> <span class="n">F</span><span class="o">)</span> <span class="err">≃</span>
  <span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">c</span><span class="o">}),</span> <span class="n">F</span><span class="bp">.</span><span class="n">obj</span> <span class="o">((</span><span class="n">a</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span><span class="bp">.</span><span class="n">left</span><span class="o">)</span> <span class="o">:=</span>
  <span class="n">equiv</span><span class="bp">.</span><span class="n">trans</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="bp">+</span><span class="mi">1</span> <span class="n">u</span><span class="bp">+</span><span class="mi">1</span> <span class="n">u</span><span class="bp">+</span><span class="mi">1</span><span class="o">}</span> <span class="o">(</span><span class="n">equiv_of_iso</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="n">E</span><span class="o">)</span>
    <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">Pi_congr_right</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">u</span><span class="bp">+</span><span class="mi">1</span> <span class="n">u</span><span class="bp">+</span><span class="mi">1</span><span class="o">}</span>
       <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">Ui</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">c</span><span class="o">}),</span>
          <span class="n">equiv_of_iso</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span>
            <span class="o">(</span><span class="n">nat_iso</span><span class="bp">.</span><span class="n">app</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="bp">+</span><span class="mi">1</span> <span class="n">u</span><span class="bp">+</span><span class="mi">1</span> <span class="n">u</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">yoneda_lemma</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">u</span><span class="o">}</span> <span class="n">X</span><span class="o">)</span> <span class="o">((</span><span class="n">Ui</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span><span class="bp">.</span><span class="n">left</span><span class="o">,</span> <span class="n">F</span><span class="o">)</span> <span class="err">≪≫</span>
               <span class="n">ulift_trivial</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="o">((</span><span class="n">evaluation_uncurried</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">u</span> <span class="n">u</span><span class="bp">+</span><span class="mi">1</span> <span class="n">u</span><span class="o">}</span> <span class="n">X</span><span class="err">ᵒᵖ</span> <span class="o">(</span><span class="kt">Type</span> <span class="n">u</span><span class="o">))</span><span class="bp">.</span><span class="n">obj</span> <span class="o">((</span><span class="n">Ui</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span><span class="bp">.</span><span class="n">left</span><span class="o">,</span> <span class="n">F</span><span class="o">))))),</span>
</pre></div>


<p>The left hand side of <code>Eeq</code> should be exactly the type of the <code>p</code> in <code>{p // horrible p}</code>.</p>
<p>I get the following error:</p>
<div class="codehilite"><pre><span></span><span class="n">type</span> <span class="n">mismatch</span> <span class="n">at</span> <span class="n">application</span>
  <span class="n">equiv</span><span class="bp">.</span><span class="n">subtype_equiv_of_subtype</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="bp">+</span><span class="mi">1</span> <span class="n">u</span><span class="bp">+</span><span class="mi">1</span><span class="o">}</span> <span class="n">Eeq</span>
<span class="n">term</span>
  <span class="n">Eeq</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="o">(</span><span class="n">limits</span><span class="bp">.</span><span class="n">sigma</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="bp">+</span><span class="mi">1</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">Ui</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">c</span><span class="o">}),</span> <span class="n">yoneda</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">u</span><span class="o">}</span><span class="bp">.</span><span class="n">obj</span> <span class="o">((</span><span class="n">Ui</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span><span class="bp">.</span><span class="n">left</span><span class="o">))</span> <span class="err">⟶</span> <span class="n">F</span><span class="o">)</span> <span class="err">≃</span>
    <span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">c</span><span class="o">}),</span> <span class="n">F</span><span class="bp">.</span><span class="n">obj</span> <span class="o">((</span><span class="n">a</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span><span class="bp">.</span><span class="n">left</span><span class="o">)</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="o">(</span><span class="n">limits</span><span class="bp">.</span><span class="n">sigma</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="bp">+</span><span class="mi">1</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">Ui</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">c</span><span class="o">}),</span> <span class="n">yoneda</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">u</span><span class="o">}</span><span class="bp">.</span><span class="n">obj</span> <span class="o">((</span><span class="n">Ui</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span><span class="bp">.</span><span class="n">left</span><span class="o">))</span> <span class="err">⟶</span> <span class="n">F</span><span class="o">)</span> <span class="err">≃</span> <span class="err">?</span><span class="n">m_1</span>
</pre></div>


<p>I have tried looking at universes. I have enable <code>pp.all</code>. And I'm clueless. Any suggestions?</p>

#### [ Kevin Buzzard (Nov 20 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024274):
<p>Is it a typeclass issue? That sometimes causes errors that look like that. Lean can't infer a typeclass and so gives up and prints an unhelpful error message</p>

#### [ Kevin Buzzard (Nov 20 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024298):
<p>I mean equiv.subtype_equiv_of_subtype -- does it have some secret inputs that it can't find?</p>

#### [ Johan Commelin (Nov 20 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024334):
<p>Also, why is <code>p</code> not an explicit argument in</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">subtype_equiv_of_subtype</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="n">β</span><span class="o">),</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">a</span><span class="o">}</span> <span class="err">≃</span> <span class="o">{</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">//</span> <span class="n">p</span> <span class="o">(</span><span class="n">e</span><span class="bp">.</span><span class="n">symm</span> <span class="n">b</span><span class="o">)}</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="n">f</span><span class="o">,</span> <span class="n">g</span><span class="o">,</span> <span class="n">l</span><span class="o">,</span> <span class="n">r</span><span class="bp">⟩</span> <span class="o">:=</span>
  <span class="bp">⟨</span><span class="n">subtype</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span> <span class="err">$</span> <span class="k">assume</span> <span class="n">a</span> <span class="n">ha</span><span class="o">,</span> <span class="k">show</span> <span class="n">p</span> <span class="o">(</span><span class="n">g</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">)),</span> <span class="k">by</span> <span class="n">rwa</span> <span class="o">[</span><span class="n">l</span><span class="o">],</span>
   <span class="n">subtype</span><span class="bp">.</span><span class="n">map</span> <span class="n">g</span> <span class="err">$</span> <span class="k">assume</span> <span class="n">a</span> <span class="n">ha</span><span class="o">,</span> <span class="n">ha</span><span class="o">,</span>
   <span class="k">assume</span> <span class="n">p</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">map_comp</span><span class="o">,</span> <span class="n">l</span><span class="bp">.</span><span class="n">comp_eq_id</span><span class="o">]</span><span class="bp">;</span> <span class="n">rw</span> <span class="o">[</span><span class="n">map_id</span><span class="o">]</span><span class="bp">;</span> <span class="n">refl</span><span class="o">,</span>
   <span class="k">assume</span> <span class="n">p</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">map_comp</span><span class="o">,</span> <span class="n">r</span><span class="bp">.</span><span class="n">comp_eq_id</span><span class="o">]</span><span class="bp">;</span> <span class="n">rw</span> <span class="o">[</span><span class="n">map_id</span><span class="o">]</span><span class="bp">;</span> <span class="n">refl</span><span class="bp">⟩</span>
</pre></div>

#### [ Johan Commelin (Nov 20 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024344):
<p>Well, in general it can't infer that <code>p</code>.</p>

#### [ Kevin Buzzard (Nov 20 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024349):
<p>I'm explicitly talking about typeclasses</p>

#### [ Chris Hughes (Nov 20 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024351):
<p>What universe is <code>?m_1</code> expected to be in?</p>

#### [ Johan Commelin (Nov 20 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024354):
<p><code>Type u</code></p>

#### [ Mario Carneiro (Nov 20 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024361):
<p>I think Johannes has a bad habit of making lots of things implicit that can't be inferred when used directly</p>

#### [ Mario Carneiro (Nov 20 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024384):
<p>I guess that <code>p</code> is inferrable if you use it as a rewrite, or apply it to something</p>

#### [ Johan Commelin (Nov 20 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024389):
<p>But in my case a smart elaborator should even be able to infer it, because I'm composing with another equiv.</p>

#### [ Johan Commelin (Nov 20 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024429):
<p>Can I rewrite along <code>equiv</code>s?</p>

#### [ Mario Carneiro (Nov 20 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024432):
<p>I think? <code>calc</code> for sure</p>

#### [ Chris Hughes (Nov 20 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024442):
<p>Isn't <code>Π (a : {x // x ∈ c}), F.obj ((a.val).left)</code> Type (u + 1). If I'm not mistaken?</p>

#### [ Johan Commelin (Nov 20 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024445):
<p>Hmmm, it says <code>rewrite tactic failed, lemma is not an equality nor a iff</code></p>

#### [ Mario Carneiro (Nov 20 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024474):
<p>hm, I guess that is probably a <code>// TODO(Leo)</code> somewhere</p>

#### [ Mario Carneiro (Nov 20 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024531):
<p>obviously it's not high on the list of priorities</p>

#### [ Johan Commelin (Nov 20 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024534):
<p>The <code>F.obj ((a.val).left)</code> is <code>Type u</code>, and the product is over <code>c : set (over U)</code> where <code>U : X</code> and <code>X : Type u</code></p>

#### [ Johan Commelin (Nov 20 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024540):
<p>I hope that doesn't bump up universes...</p>

#### [ Mario Carneiro (Nov 20 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024545):
<p>that sounds fine</p>

#### [ Mario Carneiro (Nov 20 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024550):
<p>you can just check, of course</p>

#### [ Chris Hughes (Nov 20 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024567):
<p>If <code>F.obj ((a.val).left</code> is Type u, then <code>Π (a : {x // x ∈ c}), F.obj ((a.val).left)</code> is Type (u + 1) right?</p>

#### [ Chris Hughes (Nov 20 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024608):
<p>No it isn't</p>

#### [ Mario Carneiro (Nov 20 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024687):
<p>another trick you can try is <code>by convert</code> at the type mismatch</p>

#### [ Mario Carneiro (Nov 20 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024697):
<p>it should home in on the mismatched part</p>

#### [ Johan Commelin (Nov 20 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024711):
<p>How exactly should I do that?</p>

#### [ Mario Carneiro (Nov 20 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024771):
<p>something like <code>subtype_equiv_of_subtype (by convert Eeq)</code> or <code>refine subtype_equiv_of_subtype _, convert Eeq</code></p>

#### [ Johan Commelin (Nov 20 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024839):
<p>Cool! That finds the following unsolved goal:</p>
<div class="codehilite"><pre><span></span><span class="err">⊢</span> <span class="n">presheaf</span><span class="bp">.</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span><span class="bp">.</span><span class="n">has_coproducts</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="bp">=</span> <span class="n">limits</span><span class="bp">.</span><span class="n">functor_category_has_coproducts</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="bp">+</span><span class="mi">1</span> <span class="n">u</span><span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Nov 20 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024841):
<p>That's progress at least.</p>

#### [ Kevin Buzzard (Nov 20 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024861):
<p>I am loving <code>convert</code>. I use it a lot when doing basic UG maths -- "this is basically the answer, now let's see what pieces we have to pick up"</p>

#### [ Johannes Hölzl (Nov 20 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148027986):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>  <code>rw</code> only work with <code>=</code> (maybe also <code>==</code>, and <code>&lt;-&gt;</code> only works due to <code>propext</code>). Rewriting with <code>equiv</code> is hard, one needs to prove that the motive (i.e. context in which the right-hand side appears) can be transported along the <code>equiv</code>. Even ignoring dependencies, parametricity is necessary as it shows that there is no <code>choice</code> involved.</p>

#### [ Johan Commelin (Nov 20 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148028093):
<p>Right. That is about what I expected.</p>

#### [ Johannes Hölzl (Nov 20 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148028181):
<p>To rewrite along a <code>equiv</code> we could use the <code>param</code>-branch <a href="https://github.com/leanprover-community/mathlib/commits/param" target="_blank" title="https://github.com/leanprover-community/mathlib/commits/param">https://github.com/leanprover-community/mathlib/commits/param</a> and <code>transfer</code>.</p>

#### [ Johannes Hölzl (Nov 20 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148028325):
<p>One example why it is a problem is:</p>
<p>We want to rewrite <code>e : α ≃ β</code> in <code>{a : α // p a}</code>, but what would be the goal? We get something like<code>{b : β // p (f⁻¹ b)}</code>. But in many cases <code>p</code> itself is also parametric, i.e. we have actually <code>{b : β // @p α (f⁻¹ b)}</code> (not really, as <code>p</code> is describing a term and not a constant, but I hope you get the idea) Now when we can try to adopt the structure of <code>p</code> s.t. <code>α</code> is completely replaced by <code>β</code>, and then <code>f</code> isn't occurring anymore</p>

#### [ Johannes Hölzl (Nov 20 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148028348):
<p>This adoption mechanism is the kind of rewrite <code>transfer</code> is intended to do</p>

#### [ Johannes Hölzl (Nov 20 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148028353):
<p>and <code>param</code> provides us with the necessary relations</p>

#### [ Johan Commelin (Nov 20 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148028487):
<p>I see. But I suspect that <code>param</code> isn't yet ready for prime time.</p>

#### [ Patrick Massot (Nov 20 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148028596):
<p>You need to ask <span class="user-mention" data-user-id="110193">@Cyril Cohen</span> about this</p>

#### [ Cyril Cohen (Nov 20 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148028937):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> <span class="user-mention" data-user-id="112680">@Johan Commelin</span> <span class="user-mention" data-user-id="110031">@Patrick Massot</span> <code>param</code> is not ready yet, the translation of recursors was not as straightforward as I thought.</p>

#### [ Johan Commelin (Nov 20 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148039894):
<p>What do you do when Lean doesn't want to plug a morphism in the category <code>C</code> into your contravariant functor <code>F : Cᵒᵖ  ⥤ Type u</code>?<br>
You use <code>convert</code>, and let <code>tidy</code> clean up the mess! <span class="emoji emoji-1f389" title="tada">:tada:</span></p>
<div class="codehilite"><pre><span></span><span class="n">functor</span><span class="bp">.</span><span class="n">map</span> <span class="n">F</span> <span class="o">(</span><span class="k">by</span> <span class="n">convert</span> <span class="n">Ui</span><span class="bp">.</span><span class="n">val</span><span class="bp">.</span><span class="n">hom</span><span class="bp">;</span> <span class="n">tidy</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (Nov 20 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148041125):
<p>What's up, <span class="user-mention" data-user-id="110064">@Kenny Lau</span>?</p>

#### [ Reid Barton (Nov 20 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046156):
<blockquote>
<p>Cool! That finds the following unsolved goal:</p>
<div class="codehilite"><pre><span></span><span class="err">⊢</span> <span class="n">presheaf</span><span class="bp">.</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span><span class="bp">.</span><span class="n">has_coproducts</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="bp">=</span> <span class="n">limits</span><span class="bp">.</span><span class="n">functor_category_has_coproducts</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="bp">+</span><span class="mi">1</span> <span class="n">u</span><span class="o">}</span>
</pre></div>


</blockquote>
<p>This is probably true by <code>refl</code></p>

#### [ Johan Commelin (Nov 20 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046302):
<div class="codehilite"><pre><span></span><span class="n">invalid</span> <span class="n">apply</span> <span class="n">tactic</span><span class="o">,</span> <span class="n">failed</span> <span class="n">to</span> <span class="n">unify</span>
  <span class="n">presheaf</span><span class="bp">.</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span><span class="bp">.</span><span class="n">has_coproducts</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="bp">=</span> <span class="n">limits</span><span class="bp">.</span><span class="n">functor_category_has_coproducts</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="bp">+</span><span class="mi">1</span> <span class="n">u</span><span class="o">}</span>
<span class="k">with</span>
  <span class="err">?</span><span class="n">m_3</span> <span class="bp">=</span> <span class="err">?</span><span class="n">m_3</span>
</pre></div>

#### [ Johan Commelin (Nov 20 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046325):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_coproducts</span><span class="bp">.</span><span class="o">{(</span><span class="n">u</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">presheaf</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span> <span class="n">limits</span><span class="bp">.</span><span class="n">has_coproducts_of_has_colimits</span>
</pre></div>

#### [ Johan Commelin (Nov 20 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046374):
<p>So, I changed that instance, and now I get</p>
<div class="codehilite"><pre><span></span><span class="n">tactic</span> <span class="n">failed</span><span class="o">,</span> <span class="n">there</span> <span class="n">are</span> <span class="n">no</span> <span class="n">goals</span> <span class="n">to</span> <span class="n">be</span> <span class="n">solved</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">no</span> <span class="n">goals</span>
</pre></div>

#### [ Johan Commelin (Nov 20 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046438):
<p>Aaah, lol, that is because I should now remove the <code>refl</code>.</p>

#### [ Reid Barton (Nov 20 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046447):
<p>Oh, I didn't notice "coproducts" rather than "colimits". Still I'm confused. What are the two instances which are not defeq, but equal by tidy?</p>

#### [ Johan Commelin (Nov 20 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046463):
<p>No, they aren't equal by <code>tidy</code> either</p>

#### [ Reid Barton (Nov 20 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046499):
<p>Or rather, what did you change that instance to?</p>

#### [ Reid Barton (Nov 20 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046576):
<p>well, the right hand side of that goal I guess</p>

#### [ Johan Commelin (Nov 20 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046590):
<p>Exactly</p>

#### [ Reid Barton (Nov 20 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046604):
<p>But I see</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">functor_category_has_coproducts</span> <span class="o">[</span><span class="n">has_coproducts</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span> <span class="o">:</span> <span class="n">has_coproducts</span><span class="bp">.</span><span class="o">{(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="n">v</span><span class="o">}</span> <span class="o">(</span><span class="n">K</span> <span class="err">⥤</span> <span class="n">C</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">limits</span><span class="bp">.</span><span class="n">has_coproducts_of_has_colimits</span>
</pre></div>

#### [ Reid Barton (Nov 20 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046754):
<p>... I'm really confused now</p>

#### [ Reid Barton (Nov 20 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046922):
<p>Ohh, maybe I get what is going on. I think all this duplication between colimit classes is biting you</p>

#### [ Reid Barton (Nov 20 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047035):
<p>Well, I'm still not sure why that would be a problem either really</p>

#### [ Reid Barton (Nov 20 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047048):
<p>But I still think the duplication is silly anyways</p>

#### [ Johan Commelin (Nov 20 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047066):
<p>Which duplication do you mean exactly?</p>

#### [ Reid Barton (Nov 20 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047140):
<p>Good question</p>

#### [ Reid Barton (Nov 20 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047155):
<p>I was thinking of <code>has_colimits_of_shape</code> and <code>has_colimits</code> being unrelated</p>

#### [ Reid Barton (Nov 20 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047165):
<p>But now I see there's also <code>has_colimits</code> which is also unrelated</p>

#### [ Reid Barton (Nov 20 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047176):
<p>Gah, <code>has_coproducts</code></p>

#### [ Reid Barton (Nov 20 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047441):
<p>Anyways, I'm still confused by the original fact that you replaced an instance by, as far as I can tell, its definition and it changed the behavior of <code>refl</code></p>

#### [ Johan Commelin (Nov 20 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047568):
<p>Well, I didn't even need <code>refl</code> anymore. <code>convert</code> now took care of everything.</p>

#### [ Reid Barton (Nov 20 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047657):
<p>because <code>congr</code>, which <code>convert</code> uses, will try closing goals with <code>refl</code> for you</p>

#### [ Johan Commelin (Nov 20 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047663):
<p>Currently I'm trying to prove the equivalence of different formulations of the sheaf condition. Math-proof: apply Yoneda; QED. Lean-proof: <span class="emoji emoji-1f631" title="scream">:scream:</span> <span class="emoji emoji-1f631" title="scream">:scream:</span> <span class="emoji emoji-1f4a5" title="boom">:boom:</span></p>

#### [ Reid Barton (Nov 20 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047717):
<p><code>by convert x</code> should be the same as <code>by exact x</code></p>

#### [ Johan Commelin (Nov 20 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047745):
<p>which apparently is not the same as <code>x</code></p>

#### [ Reid Barton (Nov 20 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148055915):
<p>OK, I got to the same place where you were before changing the instance.</p>

#### [ Reid Barton (Nov 20 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148055953):
<p>It's kind of hard to understand what's going on because all the <code>has_blah</code> things are classes, which means they aren't printed except with <code>pp.implicit</code>, which also prints a bunch of other stuff I don't care about...</p>

#### [ Reid Barton (Nov 20 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148056108):
<p>I wish you could jump from names in the goal window to their definitions...</p>

#### [ Johan Commelin (Nov 20 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148056614):
<p>Right, we should but the "interactive" back in the goal window <span class="emoji emoji-1f600" title="grinning">:grinning:</span></p>

#### [ Reid Barton (Nov 20 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148056956):
<p>My conclusion is that I don't know what is wrong exactly, but all these different <code>has_*</code> need to be rethought (probably there should be far fewer of them)</p>

#### [ Reid Barton (Nov 20 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148057011):
<p>Apparently your instances which were not the same reduce to something like the following</p>

#### [ Reid Barton (Nov 20 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148057077):
<p>On one side, we have the colimit of a functor on a discrete category defined using the instance that says the category of types has colimits</p>

#### [ Reid Barton (Nov 20 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148057109):
<p>On the other side, we're doing something like building a colimit cone from a coproduct thing, which in turn is built from the original colimit somehow</p>

#### [ Reid Barton (Nov 20 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148057118):
<p>both of these constructions being nontrivial</p>

#### [ Reid Barton (Nov 20 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148057189):
<p>so that they don't just cancel out</p>

#### [ Reid Barton (Nov 20 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148057227):
<p>I haven't even seen this file <code>limits/products.lean</code> before</p>

#### [ Johan Commelin (Nov 20 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148065294):
<p>Thanks for looking into this! Apparently it's trickier than I thought...</p>

#### [ Reid Barton (Nov 20 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148065317):
<p>There are so many instances and it's hard to tell which ones are used where.</p>

#### [ Reid Barton (Nov 20 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148065430):
<p>for example, <code>functor_category_has_coproducts</code> uses <code>limits.has_coproducts_of_has_colimits</code> which needs a <code>limits.has_colimits_of_shape.{u v} (discrete β)</code> instance. Does it come from <code>has_colimits_of_shape_of_has_coproducts_of_shape</code> or <code>functor_category_has_colimits_of_shape</code>?</p>

#### [ Reid Barton (Nov 20 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148065635):
<p>either way, it will eventually end up at <code>has_coproducts_of_shape</code> for the original category which comes from <code>has_coproducts_of_shape_of_has_coproducts</code> which uses <code>has_coproducts</code> which comes from an unnamed instance with definition <code>has_coproducts_of_has_colimits</code> which finally comes from the one true <code>has_colimits</code> instance for Type. I think.</p>

#### [ Reid Barton (Nov 20 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148065696):
<p>So that's how you end up with the <code>has_colimits</code> -&gt; <code>has_coproducts</code> -&gt; <code>has_colimits</code> double translation, which is not <code>refl</code></p>

#### [ Johan Commelin (Nov 27 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640522):
<p>It's really quite stupid, but I only realised yesterday that all the time I've been working with the wrong <code>map f : presheaf X \functor presheaf Y</code>.</p>

#### [ Johan Commelin (Nov 27 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640569):
<p>We want something like this:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">map&#39;</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">X</span> <span class="err">⥤</span> <span class="n">presheaf</span> <span class="n">Y</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">obj</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">F</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">obj</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">V</span><span class="o">,</span> <span class="n">colimit</span> <span class="o">((</span><span class="n">comma</span><span class="bp">.</span><span class="n">snd</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">u</span> <span class="n">u</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_obj</span> <span class="n">V</span><span class="o">)</span> <span class="n">f</span><span class="o">)</span><span class="bp">.</span><span class="n">op</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">),</span>
    <span class="n">map</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">V₁</span> <span class="n">V₂</span> <span class="n">j</span><span class="o">,</span> <span class="n">colimit</span><span class="bp">.</span><span class="n">pre</span> <span class="o">((</span><span class="n">comma</span><span class="bp">.</span><span class="n">snd</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">u</span> <span class="n">u</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_obj</span> <span class="n">V₂</span><span class="o">)</span> <span class="n">f</span><span class="o">)</span><span class="bp">.</span><span class="n">op</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">)</span> <span class="o">(</span><span class="n">comma</span><span class="bp">.</span><span class="n">map_left</span> <span class="n">f</span> <span class="err">$</span> <span class="n">functor</span><span class="bp">.</span><span class="n">of_map</span> <span class="n">j</span><span class="o">)</span><span class="bp">.</span><span class="n">op</span><span class="o">,</span>
    <span class="n">map_id&#39;</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">V</span><span class="o">,</span>
    <span class="k">begin</span>
      <span class="n">erw</span> <span class="n">functor</span><span class="bp">.</span><span class="n">of_map_id</span><span class="o">,</span>
      <span class="n">erw</span> <span class="n">colimit</span><span class="bp">.</span><span class="n">pre_map</span><span class="o">,</span>
      <span class="n">tidy</span><span class="o">,</span>
    <span class="kn">end</span> <span class="o">},</span>
  <span class="n">map</span> <span class="o">:=</span> <span class="bp">_</span> <span class="o">}</span>
</pre></div>


<p>but I find it impossible to get this sorry-free.</p>

#### [ Reid Barton (Nov 27 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640594):
<p>This is what I implemented in the <code>adjunctions</code> branch, I think?</p>

#### [ Johan Commelin (Nov 27 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640600):
<p>This is what will give us the pullback of (pre)sheaves.</p>

#### [ Johan Commelin (Nov 27 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640608):
<p>Aaah, did you?</p>

#### [ Johan Commelin (Nov 27 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640664):
<p>I didn't look far enough, I'm afraid.</p>

#### [ Reid Barton (Nov 27 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640670):
<p>I think it is <code>yoneda_extension (F.comp yoneda)</code>?</p>

#### [ Reid Barton (Nov 27 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640698):
<p>at least, it seems to involve many of the same ingredients :)</p>

#### [ Johan Commelin (Nov 27 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640743):
<p>In which file?</p>

#### [ Reid Barton (Nov 27 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640747):
<p>another construction which I am not very happy about, though...</p>

#### [ Reid Barton (Nov 27 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640751):
<p><code>presheaf.lean</code></p>

#### [ Johan Commelin (Nov 27 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640850):
<p>Aaah, I see. Seems pretty non-trivial...</p>

#### [ Johan Commelin (Nov 27 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640875):
<p>Also, why do you work with <code>≃</code> instead of <code>≅</code>. Isn't that just as "bad"?</p>

#### [ Reid Barton (Nov 27 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640886):
<p>Yeah, I did it in a round-about way, in retrospect</p>

#### [ Reid Barton (Nov 27 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640953):
<p>In general I use <code>equiv</code> because it actually has useful lemmas and also it can relate different universes</p>

#### [ Reid Barton (Nov 27 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640961):
<p>though I added a couple more lemmas for <code>iso</code> in the limits PR</p>

#### [ Johan Commelin (Nov 27 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640996):
<p>Hmm, I feel like we should merge your <code>presheaf.lean</code> and my <code>sheaf.lean</code>. Or at least deduplicate.</p>

#### [ Reid Barton (Nov 27 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148641237):
<p>I intend to take a second stab at all the adjunctions and presheaf stuff at some point, but I'm not actively working on it at the moment</p>

#### [ Johan Commelin (Nov 27 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148641294):
<p>Ok, I'll move some stuff from my file to yours. So that <code>sheaf.lean</code> is only about sheaves.</p>

#### [ Johan Commelin (Nov 27 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148641306):
<p>If you start working on it again, please make sure to take a look at the <code>sheaf</code> branch version of your file.</p>

#### [ Reid Barton (Nov 27 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148641624):
<p>FWIW, my conclusion from my first attempt was that it's probably better to do all the constructions in a manifestly natural way, like Scott did in <code>yoneda.lean</code> for example, even though the result is probably pretty unreadable. Then you can add a simp lemma that explains what is actually happening on the level of objects</p>

#### [ Reid Barton (Nov 27 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148642150):
<p>Or at least, don't have a bunch of isomorphisms with the naturality conditions stated separately. That was a big mess</p>

#### [ Johan Commelin (Nov 27 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148642474):
<p>I see. That's what I've been trying to do. But I also got stuck.</p>

#### [ Johan Commelin (Nov 27 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148642576):
<p>The problem with doing things in a "manifestly natural way" is that you get sucked into ever deeper/wider/higher abstractions...</p>

#### [ Reid Barton (Nov 27 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148642695):
<p>it's true</p>

#### [ Reid Barton (Nov 27 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148643278):
<p>And that's sort of why I backed off from my previous comment. It's not obvious how to do this "category of elements" construction functorially</p>

#### [ Reid Barton (Nov 27 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148643384):
<p>The key is to somehow give these things usable and complete instances, so that the way to prove things about them is not to <code>dsimp</code> 100 things</p>

#### [ Reid Barton (Nov 27 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148643417):
<p>and that's where my current version of <code>presheaf.lean</code> sort of fell apart</p>

#### [ Reid Barton (Nov 27 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148643508):
<p><a href="https://github.com/leanprover-community/mathlib/blob/adjunctions/category_theory/presheaf.lean#L310" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/adjunctions/category_theory/presheaf.lean#L310">https://github.com/leanprover-community/mathlib/blob/adjunctions/category_theory/presheaf.lean#L310</a></p>

#### [ Johan Commelin (Nov 27 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148644814):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Does this mean that you think we should avoid <code>adjunction.left_adjoint_of_equiv</code>?</p>

#### [ Johan Commelin (Nov 29 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148766980):
<p>Yuchai! This is now sorry-free: <a href="https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/presheaf.lean#L59" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/presheaf.lean#L59">https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/presheaf.lean#L59</a><br>
But it is slower than slow! Not sure how to speed it up though. I'm chaining a bunch of rewrites. Are there strategies for speeding this up?</p>

#### [ Scott Morrison (Nov 29 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148767231):
<p>One thing that I find often works is to work out why the <code>erw</code> are necessary. This is sometimes unrewarding, but often it is because hidden inside implicit arguments there are things that should <code>dsimp</code>, but you forgot to write the appropriate <code>rfl</code> lemmas.  Sometimes you get really lucky, and after diagnosing a problem like this you can not only change the <code>erw</code> to <code>rw</code>, but even to <code>dsimp</code>!</p>

#### [ Johan Commelin (Nov 29 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148767295):
<p>I see. (I've stopped using <code>rw</code>, because <code>erw</code> has more powerful magic (-;)</p>

#### [ Johan Commelin (Nov 29 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148767296):
<p>Is <code>dsimp</code> faster than <code>erw</code>?</p>

#### [ Scott Morrison (Nov 29 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148767299):
<p>Yes.</p>

#### [ Scott Morrison (Nov 29 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148767305):
<p>And <code>erw</code> can be slower than <code>rw</code>, in places where either work. (I think?)</p>

#### [ Scott Morrison (Nov 29 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148767352):
<p>Well, <code>dsimp</code> can be either faster or slower than <code>erw</code>. :-) But _usually_ it seems to be faster to avoid using <code>erw</code>.</p>

#### [ Johan Commelin (Nov 29 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148767491):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Do you think we could have a <code>[derive rfl-lemmas]</code>?</p>

#### [ Scott Morrison (Nov 29 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148767960):
<p>I've just had a quick look at that proof, Johan, and I don't seem to be able to make much improvement. :-( There does seem to be a small problem changing between <code>colimit</code> and <code>colim.obj</code>.</p>

#### [ Johan Commelin (Nov 29 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148770849):
<p>So here is what I imagine <code>derive rflsimp</code> (or whatever) should do: it looks at the current definition, and (as far as I thought this through, which is not that far) it does two checks:</p>
<ul>
<li>the definition is an "abbreviation" (like <code>def presheaf C := C \functor Type v</code>. In this case it looks up all the rflsimp lemmas that it derived for <code>C \functor D</code> and defines copies in the <code>presheaf</code> namespace.</li>
<li>the definition <code>X</code> is a structure. In this case it looks up all the fields. For a field <code>foo</code> it checks whether this is a Pi-type (?) and how many arguments the Pi takes. So if <code>foo := λ a b c, bar(a,b,c)</code> then it will create the appropriate simp-lemma (proved by <code>rfl</code>) that</li>
</ul>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">X</span><span class="bp">.</span><span class="n">foo</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">some_type</span><span class="o">)</span> <span class="o">:</span>  <span class="n">x</span><span class="bp">.</span><span class="n">foo</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">bar</span><span class="o">(</span><span class="n">a</span><span class="o">,</span><span class="n">b</span><span class="o">,</span><span class="n">c</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>


<p>Of course I don't know how to write <code>meta</code>-code. And of course this is probably a very simplified picture. But I think something like this should be possible, and I think it would result in three things:</p>
<ul>
<li>less boilerplate (especially in the category library!)</li>
<li>less broken proofs, where <code>tidy</code> doesn't work, because somewhere someone forgot to state the obvious <code>rfl</code>-simp-lemma.</li>
<li>less wasted time in hunting down the brokenness of the preceding point.</li>
</ul>

#### [ Johan Commelin (Nov 29 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148771232):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Thanks for looking into speeding things up. I added a rflsimp-lemma for <code>colim.obj</code>. Do you have any clue why the first line in that proof (with the comment) didn't simplify?</p>

#### [ Scott Morrison (Nov 29 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148777570):
<p>Nope, I couldn't work it out. The next "usual suspect" for simp not working is that the thing that needs to be <code>simp</code>ed is inside a function that looks superficially dependent but actually isn't when you think about it a bit. <code>simp</code>, which needs to build congruence lemmas to do "rewriting", can't work out what do to, but <code>rw</code> can. This is a "known problem" with <code>simp</code>, apparently.</p>

#### [ Scott Morrison (Nov 29 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148777585):
<p>You know how to use <code>rewrite_search</code>, don't you? :-)</p>

#### [ Keeley Hoek (Nov 29 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148778422):
<p>At some point Johan I made a thing which did this<br>
It was a command called <code>rfl_lemma</code> I think. If you have access to rewrite_search you have access to it, too</p>

#### [ Keeley Hoek (Nov 29 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148778431):
<p>It only worked for structures though</p>

#### [ Johan Commelin (Nov 29 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148779294):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> <span class="user-mention" data-user-id="110111">@Keeley Hoek</span> I don't have <code>rewrite_search</code>. Do you think it is ready to be tested by others? If so, what do I need to do to get started?</p>

#### [ Keeley Hoek (Nov 29 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148782650):
<p>You could always try it out! My understanding is that all you should have to do is add</p>
<div class="codehilite"><pre><span></span>lean-tidy = {git = &quot;https://github.com/semorrison/lean-tidy&quot;, rev = &quot;3a69d6241207f0c0758468dce666858027c54909&quot;}
</pre></div>


<p>to your <code>leanpkg.toml</code> and run <code>leanpkg configure</code>. (I'm slightly worried though because <code>lean-tidy</code> obviously imports from <code>mathlib</code>, which you are working on... but I suspect it will work find (I think this is what Scott does to get his proofs using it).</p>

#### [ Keeley Hoek (Nov 29 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148782717):
<p>Then import <code>tactic.rewrite_search</code>. You can try to discharge goals with the <code>rewrite_search</code> tactic, but make sure you tag lemmas it is allowed to use with <code>@[search]</code>. There is much more complicated stuff you can do (including more specific tagging), but that's a start!</p>

#### [ Johan Commelin (Nov 29 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148783201):
<p>Thanks for the explanation!</p>

#### [ Scott Morrison (Nov 29 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148783722):
<p>I've actually never used it inside mathlib, I'm very curious if it works.</p>

#### [ Keeley Hoek (Nov 29 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148783729):
<p>ooh<br>
Maybe it won't then</p>

#### [ Keeley Hoek (Nov 29 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148783739):
<p>something about "ambiguous import xxxx"</p>

#### [ Johan Commelin (Nov 29 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148784745):
<p>How far are we from a merge request of a (preliminary) version of <code>rewrite_search</code>?</p>

#### [ Johan Commelin (Nov 29 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148785350):
<p><span class="user-mention" data-user-id="110111">@Keeley Hoek</span> <span class="user-mention" data-user-id="110087">@Scott Morrison</span> I followed the instructions and then ran <code>leanpkg build</code>. I'm getting tons of errors <span class="emoji emoji-1f61c" title="stuck out tongue wink">:stuck_out_tongue_wink:</span></p>

#### [ Keeley Hoek (Nov 29 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148785538):
<p>:D</p>

#### [ Keeley Hoek (Nov 29 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148785563):
<p>yeah, sorry<br>
I think what you actually have to do is copy paste the lean-tidy repo over mathlib<br>
but probably don't do that it will mess your history</p>

#### [ Johan Commelin (Nov 30 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148857277):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> <span class="user-mention" data-user-id="110111">@Keeley Hoek</span> I can report that adding that Lean <em>does not</em> outright refuse that repo as a dependency of mathlib. However... there's tons and tons of errors. So it's not really usable in a sense.</p>

#### [ Johan Commelin (Dec 28 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638060):
<p>After a long period of being distracted by other work, I've returned to the sheaves and sites project. Stuff is now happening on the <code>sheaf-2</code> branch, which has less dependencies than <code>sheaf</code>.<br>
I am currently struggling with defining a pretty non-constructive map. I have a gadget <code>s</code> which comes with a proof that I can perform a certain construction after some choice, and the result of the construction does not depend on the choice. But how do I actually do this?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">foo</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">covering_family</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="n">matching_sections</span> <span class="n">c</span> <span class="n">F</span><span class="o">)</span> <span class="err">⟶</span> <span class="o">(</span><span class="n">matching_sections</span> <span class="n">c</span><span class="bp">.</span><span class="n">generate_sieve</span><span class="bp">.</span><span class="n">val</span> <span class="n">F</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">s</span> <span class="o">:</span> <span class="n">matching_sections</span> <span class="n">c</span> <span class="n">F</span><span class="o">,</span> <span class="k">show</span> <span class="n">matching_sections</span> <span class="n">c</span><span class="bp">.</span><span class="n">generate_sieve</span><span class="bp">.</span><span class="n">val</span> <span class="n">F</span><span class="o">,</span> <span class="k">from</span>
<span class="o">{</span> <span class="n">val</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">V</span> <span class="n">H</span><span class="o">,</span>
  <span class="k">begin</span>
    <span class="n">delta</span> <span class="n">matching_sections</span> <span class="n">at</span> <span class="n">s</span><span class="o">,</span>
    <span class="n">choose</span> <span class="n">Ui</span> <span class="n">H</span> <span class="n">f</span> <span class="kn">using</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">refine</span> <span class="n">F</span><span class="bp">.</span><span class="n">map</span> <span class="bp">_</span> <span class="o">(</span><span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">_</span> <span class="n">H</span><span class="o">),</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">property</span> <span class="o">:=</span> <span class="bp">_</span> <span class="o">}</span>
</pre></div>


<p>Here is what my goal window looks like</p>
<div class="codehilite"><pre><span></span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">small_category</span> <span class="n">X</span><span class="o">,</span>
<span class="n">U</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span>
<span class="n">c</span> <span class="o">:</span> <span class="n">covering_family</span> <span class="n">U</span><span class="o">,</span>
<span class="n">F</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">X</span><span class="o">,</span>
<span class="n">V</span> <span class="o">:</span> <span class="n">over</span> <span class="n">U</span><span class="o">,</span>
<span class="n">s</span> <span class="o">:</span>
  <span class="o">{</span><span class="n">s</span> <span class="bp">//</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">Ui</span> <span class="o">:</span> <span class="n">over</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">Ui</span> <span class="err">∈</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">Uj</span> <span class="o">:</span> <span class="n">over</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">H_1</span> <span class="o">:</span> <span class="n">Uj</span> <span class="err">∈</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">V</span> <span class="o">:</span> <span class="n">over</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">V</span> <span class="err">⟶</span> <span class="n">Ui</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">V</span> <span class="err">⟶</span> <span class="n">Uj</span><span class="o">),</span>
     <span class="n">F</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">left</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="n">Ui</span> <span class="n">H</span><span class="o">)</span> <span class="bp">=</span> <span class="n">F</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="n">g</span><span class="bp">.</span><span class="n">left</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="n">Uj</span> <span class="n">H_1</span><span class="o">)},</span>
<span class="n">Ui</span> <span class="o">:</span> <span class="n">over</span> <span class="n">U</span><span class="o">,</span>
<span class="n">H</span> <span class="o">:</span> <span class="n">Ui</span> <span class="err">∈</span> <span class="n">c</span><span class="o">,</span>
<span class="n">f</span> <span class="o">:</span> <span class="n">nonempty</span> <span class="o">(</span><span class="n">V</span> <span class="err">⟶</span> <span class="n">Ui</span><span class="o">)</span>
<span class="err">⊢</span> <span class="n">Ui</span><span class="bp">.</span><span class="n">left</span> <span class="err">⟶</span> <span class="n">V</span><span class="bp">.</span><span class="n">left</span>
</pre></div>


<p>What I need to do is extract some hom <code>f</code> from <code>V</code> to <code>Ui</code> out of the current <code>f : nonempty (_)</code>. I should then be able to close the goal with <code>exact f.left</code>. But I can only eliminate into <code>Prop</code> from <code>nonempty</code>. So how should I set things up?<br>
All of this is at <a href="https://github.com/leanprover-community/mathlib/blob/sheaf-2/category_theory/sheaf.lean#L190-L199" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/sheaf-2/category_theory/sheaf.lean#L190-L199">https://github.com/leanprover-community/mathlib/blob/sheaf-2/category_theory/sheaf.lean#L190-L199</a></p>

#### [ Reid Barton (Dec 28 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638676):
<p>Are you going to need to prove the resulting construction is independent of the choice?</p>

#### [ Reid Barton (Dec 28 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638688):
<p>The simple answer is to use choice again, in the form of <code>classical.choice</code></p>

#### [ Reid Barton (Dec 28 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638738):
<p>maybe the <code>choose</code> tactic could do this when the final Prop is a <code>nonempty</code></p>

#### [ Reid Barton (Dec 28 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638740):
<p>or you could use that <code>\exists blah, blah, blah, true</code> encoding</p>

#### [ Johan Commelin (Dec 28 2018 at 07:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638796):
<p>So <code>nonempty blah</code> is not Lean-equivalent to the <code>\exists blah, blah, blah, true</code> encoding?</p>

#### [ Johan Commelin (Dec 28 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638804):
<p>The <code>choose</code> tactic doesn't help... <span class="emoji emoji-2639" title="sad">:sad:</span></p>

#### [ Reid Barton (Dec 28 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638807):
<p>it's not definitionally equivalent, much as <code>p /\ true</code> isn't definitionally equivalent to <code>p</code></p>

#### [ Johan Commelin (Dec 28 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638882):
<p><code>nonempty_of_exists</code> is not an iff...</p>

#### [ Reid Barton (Dec 28 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638940):
<p>You can just use <code>choice f</code></p>

#### [ Johan Commelin (Dec 28 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638952):
<p>Ok, I'll try that. Too bad that <code>choose f</code> does not work.</p>

#### [ Reid Barton (Dec 28 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638953):
<p>Sometimes when there is going to be a lot of "can only eliminate into Prop" nonsense in a proof, I just put an <code>apply choice</code> at the start</p>

#### [ Reid Barton (Dec 28 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152639001):
<p>or not necessarily at the start of the whole argument, but at the start of some subargument to satisfy some lemma which wants to take an actual map rather than just an existence statement</p>

#### [ Johan Commelin (Dec 28 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152642729):
<p>Ok, that worked. But I still wonder why <code>choose f</code> didn't work. <span class="user-mention" data-user-id="110031">@Patrick Massot</span> Any ideas why <code>choose</code> doesn't work on <code>nonempty</code>?<br>
Here's the proof that I have now</p>
<div class="codehilite"><pre><span></span><span class="n">noncomputable</span> <span class="n">def</span> <span class="n">foo</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">covering_family</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="n">matching_sections</span> <span class="n">c</span> <span class="n">F</span><span class="o">)</span> <span class="err">⟶</span> <span class="o">(</span><span class="n">matching_sections</span> <span class="n">c</span><span class="bp">.</span><span class="n">generate_sieve</span><span class="bp">.</span><span class="n">val</span> <span class="n">F</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">s</span> <span class="o">:</span> <span class="n">matching_sections</span> <span class="n">c</span> <span class="n">F</span><span class="o">,</span> <span class="k">show</span> <span class="n">matching_sections</span> <span class="n">c</span><span class="bp">.</span><span class="n">generate_sieve</span><span class="bp">.</span><span class="n">val</span> <span class="n">F</span><span class="o">,</span> <span class="k">from</span>
<span class="o">{</span> <span class="n">val</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">V</span> <span class="n">H</span><span class="o">,</span>
  <span class="k">begin</span>
    <span class="n">delta</span> <span class="n">matching_sections</span> <span class="n">at</span> <span class="n">s</span><span class="o">,</span>
    <span class="n">choose</span> <span class="n">Ui</span> <span class="n">H</span> <span class="n">f</span> <span class="kn">using</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">refine</span> <span class="n">F</span><span class="bp">.</span><span class="n">map</span> <span class="bp">_</span> <span class="o">(</span><span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">_</span> <span class="n">H</span><span class="o">),</span>
    <span class="n">exact</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">choice</span> <span class="n">f</span><span class="o">)</span><span class="bp">.</span><span class="n">left</span><span class="o">,</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">property</span> <span class="o">:=</span> <span class="bp">_</span> <span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Dec 28 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152642813):
<p>because <code>choose</code> is skolemization?</p>

#### [ Johan Commelin (Dec 28 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152643079):
<p>I don't know what that means.</p>

#### [ Johan Commelin (Dec 28 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152643597):
<p>I love the marvellous power of the underscore:</p>
<div class="codehilite"><pre><span></span><span class="n">noncomputable</span> <span class="n">def</span> <span class="n">foo</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">covering_family</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="n">matching_sections</span> <span class="n">c</span> <span class="n">F</span><span class="o">)</span> <span class="err">⟶</span> <span class="o">(</span><span class="n">matching_sections</span> <span class="n">c</span><span class="bp">.</span><span class="n">generate_sieve</span><span class="bp">.</span><span class="n">val</span> <span class="n">F</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">s</span> <span class="o">:</span> <span class="n">matching_sections</span> <span class="n">c</span> <span class="n">F</span><span class="o">,</span> <span class="k">show</span> <span class="n">matching_sections</span> <span class="n">c</span><span class="bp">.</span><span class="n">generate_sieve</span><span class="bp">.</span><span class="n">val</span> <span class="n">F</span><span class="o">,</span> <span class="k">from</span>
<span class="o">{</span> <span class="n">val</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">V</span> <span class="n">H</span><span class="o">,</span>
  <span class="k">begin</span>
    <span class="n">choose</span> <span class="n">Ui</span> <span class="n">H</span> <span class="n">f</span> <span class="kn">using</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">refine</span> <span class="n">F</span><span class="bp">.</span><span class="n">map</span> <span class="bp">_</span> <span class="o">(</span><span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">_</span> <span class="n">H</span><span class="o">),</span>
    <span class="n">exact</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">choice</span> <span class="n">f</span><span class="o">)</span><span class="bp">.</span><span class="n">left</span><span class="o">,</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">property</span> <span class="o">:=</span>
  <span class="k">begin</span>
    <span class="n">intros</span><span class="o">,</span>
    <span class="k">show</span> <span class="o">(</span><span class="n">F</span><span class="bp">.</span><span class="n">map</span> <span class="bp">_</span> <span class="err">≫</span> <span class="n">F</span><span class="bp">.</span><span class="n">map</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">=</span> <span class="o">(</span><span class="n">F</span><span class="bp">.</span><span class="n">map</span> <span class="bp">_</span> <span class="err">≫</span> <span class="n">F</span><span class="bp">.</span><span class="n">map</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">_</span><span class="o">,</span>
    <span class="n">repeat</span> <span class="o">{</span><span class="n">rw</span> <span class="err">←</span> <span class="n">F</span><span class="bp">.</span><span class="n">map_comp</span><span class="o">},</span>
    <span class="n">exact</span> <span class="n">s</span><span class="bp">.</span><span class="n">property</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">_</span> <span class="err">≫</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="bp">_</span> <span class="err">≫</span> <span class="bp">_</span><span class="o">)</span>
  <span class="kn">end</span> <span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Dec 28 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152667001):
<p>I'm hitting a nasty error again (probably I'm being bitten by <code>choice</code>).<br>
Here is the error (code follows below):</p>
<div class="codehilite"><pre><span></span><span class="n">type</span> <span class="n">mismatch</span> <span class="n">at</span> <span class="n">application</span>
  <span class="bp">⟨</span><span class="n">s_val</span><span class="o">,</span> <span class="n">s_property</span><span class="bp">⟩.</span><span class="n">val</span> <span class="n">Ui</span> <span class="n">H</span>
<span class="n">term</span>
  <span class="n">H</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="n">Ui_1</span> <span class="err">∈</span> <span class="n">c_1</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="n">Ui</span> <span class="err">∈</span> <span class="n">c</span>
<span class="n">types</span> <span class="n">contain</span> <span class="n">aliased</span> <span class="n">name</span><span class="o">(</span><span class="n">s</span><span class="o">):</span> <span class="n">Ui</span> <span class="n">U</span> <span class="n">c</span>
<span class="n">remark</span><span class="o">:</span> <span class="n">the</span> <span class="n">tactic</span> <span class="bp">`</span><span class="n">dedup</span><span class="bp">`</span> <span class="n">can</span> <span class="n">be</span> <span class="n">used</span> <span class="n">to</span> <span class="n">rename</span> <span class="n">aliases</span>
</pre></div>


<p>Code:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">quux</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">covering_family</span> <span class="n">U</span><span class="o">)</span> <span class="o">:</span>
<span class="n">c</span><span class="bp">.</span><span class="n">matching_sections</span> <span class="err">≅</span> <span class="n">c</span><span class="bp">.</span><span class="n">generate_sieve</span><span class="bp">.</span><span class="n">val</span><span class="bp">.</span><span class="n">matching_sections</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">hom</span> <span class="o">:=</span> <span class="n">foo</span> <span class="n">c</span><span class="o">,</span>
  <span class="n">inv</span> <span class="o">:=</span> <span class="n">bar</span> <span class="n">c</span><span class="o">,</span>
  <span class="n">hom_inv_id&#39;</span> <span class="o">:=</span>
  <span class="k">begin</span>
    <span class="n">ext1</span> <span class="n">F</span><span class="o">,</span>
    <span class="n">ext1</span> <span class="n">s</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">ext</span><span class="bp">.</span><span class="n">mpr</span><span class="o">,</span>
    <span class="n">funext</span><span class="o">,</span>
    <span class="n">convert</span> <span class="n">s</span><span class="bp">.</span><span class="n">property</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="mi">𝟙</span> <span class="bp">_</span><span class="o">),</span>
    <span class="n">tidy</span> <span class="o">{</span><span class="n">trace_result</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">}</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">inv_hom_id&#39;</span> <span class="o">:=</span>
  <span class="k">begin</span>
    <span class="n">ext1</span> <span class="n">F</span><span class="o">,</span>
    <span class="n">ext1</span> <span class="n">s</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">ext</span><span class="bp">.</span><span class="n">mpr</span><span class="o">,</span>
    <span class="n">funext</span><span class="o">,</span>
    <span class="n">dsimp</span> <span class="o">[</span><span class="n">foo</span><span class="o">,</span> <span class="n">bar</span><span class="o">],</span>
    <span class="n">convert</span> <span class="n">s</span><span class="bp">.</span><span class="n">property</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="mi">𝟙</span> <span class="bp">_</span><span class="o">),</span> <span class="c1">-- This line fails</span>
    <span class="n">tidy</span> <span class="o">{</span><span class="n">trace_result</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">},</span>
  <span class="kn">end</span> <span class="o">}</span>
</pre></div>


<p>Context, just before the <code>convert</code>:</p>
<div class="codehilite"><pre><span></span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">small_category</span> <span class="n">X</span><span class="o">,</span>
<span class="n">U</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span>
<span class="n">c</span> <span class="o">:</span> <span class="n">covering_family</span> <span class="n">U</span><span class="o">,</span>
<span class="n">F</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">X</span><span class="o">,</span>
<span class="n">s</span> <span class="o">:</span> <span class="o">(</span><span class="n">matching_sections</span> <span class="o">((</span><span class="n">generate_sieve</span> <span class="n">c</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span><span class="o">))</span><span class="bp">.</span><span class="n">obj</span> <span class="n">F</span><span class="o">,</span>
<span class="n">V</span> <span class="o">:</span> <span class="n">over</span> <span class="n">U</span><span class="o">,</span>
<span class="n">H</span> <span class="o">:</span> <span class="n">V</span> <span class="err">∈</span> <span class="o">(</span><span class="n">generate_sieve</span> <span class="n">c</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span>
<span class="err">⊢</span> <span class="n">F</span><span class="bp">.</span><span class="n">map</span> <span class="o">((</span><span class="n">classical</span><span class="bp">.</span><span class="n">choice</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">left</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span><span class="bp">.</span><span class="n">val</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="n">H</span><span class="o">)</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">=</span> <span class="n">s</span><span class="bp">.</span><span class="n">val</span> <span class="n">V</span> <span class="n">H</span>
</pre></div>

#### [ Johan Commelin (Jan 20 2019 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/156493474):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Replying to <a href="#narrow/stream/116395-maths/topic/What's.20new.20in.20Lean.20maths.3F/near/156491890" title="#narrow/stream/116395-maths/topic/What's.20new.20in.20Lean.20maths.3F/near/156491890">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What's.20new.20in.20Lean.20maths.3F/near/156491890</a> in this thread.<br>
To be precise: I have no trouble at all extending a presheaf from a basis to the whole space. The problem is checking that it sends sheaves to sheaves. The difficulty is probably due to the fact that I do not have a usable API around the sheaf condition.<br>
And I guess my sheaf condition is hard to work with right now because I'm trying to be quite general, doing sheaves on an arbitrary site.</p>

#### [ Kevin Buzzard (Jan 20 2019 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/156495585):
<p>Oh -- the proof involves some argument on stalks which for a general site is complicated? Are there universe issues or do you only work with small sites?</p>

#### [ Kevin Buzzard (Jan 29 2019 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/157127004):
<p>OK so I just spent 2 hours with Ramon going through this proof (sheaf on a basis extends to sheaf on site) again in the case of topological spaces. The ideas are all fresh in my mind at the minute so let me note them down in case there's anything helpful here.</p>
<p>Aah -- I now realise that actually I don't know how you're extending the presheaf at all. The way Ramon and I do it is that given a presheaf <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>F</mi></mrow><annotation encoding="application/x-tex">F</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">F</span></span></span></span> on a basis we can define the stalk <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>F</mi><mi>x</mi></msub></mrow><annotation encoding="application/x-tex">F_x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:-0.13889em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">x</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> at a point <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi></mrow><annotation encoding="application/x-tex">x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">x</span></span></span></span> via a direct limit construction, and then we define a presheaf <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>F</mi><mo>+</mo></msup></mrow><annotation encoding="application/x-tex">F^+</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.771331em;"></span><span class="strut bottom" style="height:0.771331em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.771331em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mbin mtight">+</span></span></span></span></span></span></span></span></span></span></span> on the space by saying that its values on an open <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>U</mi></mrow><annotation encoding="application/x-tex">U</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">U</span></span></span></span> are a subtype of a big Pi type sending <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mo>∈</mo><mi>U</mi></mrow><annotation encoding="application/x-tex">x\in U</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.72243em;vertical-align:-0.0391em;"></span><span class="base"><span class="mord mathit">x</span><span class="mrel">∈</span><span class="mord mathit" style="margin-right:0.10903em;">U</span></span></span></span> to an element of the stalk <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>F</mi><mi>x</mi></msub></mrow><annotation encoding="application/x-tex">F_x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:-0.13889em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">x</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>; it's the subtype consisting of functions which are locally a section of the presheaf-on-a-basis.</p>
<p>What both he and I did next was then immediately embarked on a proof that if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>F</mi></mrow><annotation encoding="application/x-tex">F</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">F</span></span></span></span> is a sheaf on a basis then this extension is a sheaf. This gets really hairy. Say I have a bunch of local sections <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>s</mi><mi>i</mi></msub></mrow><annotation encoding="application/x-tex">s_i</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.58056em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">s</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> on opens <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>U</mi><mi>i</mi></msub></mrow><annotation encoding="application/x-tex">U_i</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:-0.10903em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>, which agree on overlaps. I want to glue them together to get a section <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span> of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>F</mi><mo>+</mo></msup></mrow><annotation encoding="application/x-tex">F^+</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.771331em;"></span><span class="strut bottom" style="height:0.771331em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.771331em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mbin mtight">+</span></span></span></span></span></span></span></span></span></span></span>. Well, a section of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>F</mi><mo>+</mo></msup></mrow><annotation encoding="application/x-tex">F^+</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.771331em;"></span><span class="strut bottom" style="height:0.771331em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.771331em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mbin mtight">+</span></span></span></span></span></span></span></span></span></span></span> is just a subtype of a pi type, so we know how to define it. But the technicality is that to define this function <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span> we want to say <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msub><mi>s</mi><mi>i</mi></msub><mo>(</mo><mi>x</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">S(x)=s_i(x)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord"><span class="mord mathit">s</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span></span></span></span> where we choose some <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>i</mi></mrow><annotation encoding="application/x-tex">i</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.65952em;"></span><span class="strut bottom" style="height:0.65952em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">i</span></span></span></span> such that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mo>∈</mo><msub><mi>U</mi><mi>i</mi></msub></mrow><annotation encoding="application/x-tex">x\in U_i</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord mathit">x</span><span class="mrel">∈</span><span class="mord"><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:-0.10903em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>. As mathematicians we know that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">S(x)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span></span></span></span> is independent of the choice, but in computer science this is some <code>classical.indefinite_description</code> blah blah noncomputable crap and we're forced to deal with this. Ramon had written 0 API so at the end of it our goals had all these <code>classical.indefinite_description</code> terms in. He was able to battle past the first few, but checking that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span> restricted to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>s</mi><mi>i</mi></msub></mrow><annotation encoding="application/x-tex">s_i</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.58056em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">s</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> was really difficult, for a reason which I am only now beginning to understand properly. </p>
<p>The issue was that we didn't have the right API for this construction of extending a presheaf-on-a-basis to a presheaf on the space. A general presheaf on a space, when evaluated at some open <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>U</mi></mrow><annotation encoding="application/x-tex">U</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">U</span></span></span></span>, is just some random type. But for a presheaf coming from a presheaf-on-a-basis this is far from being true -- the sections are subtypes of pi types, and the restriction maps are literally restrictions. This is all wrapped up in the definition of the construction of a presheaf from a presheaf-on-a-basis. I realised that if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>F</mi><mo>+</mo></msup></mrow><annotation encoding="application/x-tex">F^+</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.771331em;"></span><span class="strut bottom" style="height:0.771331em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.771331em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mbin mtight">+</span></span></span></span></span></span></span></span></span></span></span> is a presheaf coming from a presheaf-on-a-basis then for <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mo>∈</mo><mi>U</mi><mo>⊆</mo><mi>X</mi></mrow><annotation encoding="application/x-tex">x\in U\subseteq X</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.8193em;vertical-align:-0.13597em;"></span><span class="base"><span class="mord mathit">x</span><span class="mrel">∈</span><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="mrel">⊆</span><span class="mord mathit" style="margin-right:0.07847em;">X</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>s</mi><mo>∈</mo><msup><mi>F</mi><mo>+</mo></msup><mo>(</mo><mi>X</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">s\in F^+(X)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.771331em;"></span><span class="strut bottom" style="height:1.021331em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">s</span><span class="mrel">∈</span><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.771331em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mbin mtight">+</span></span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mclose">)</span></span></span></span> a function, the fact that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>r</mi><mi>e</mi><msub><mi>s</mi><mi>U</mi></msub><mi>s</mi><mo>)</mo><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>s</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">(res_U s)(x)=s(x)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.02778em;">r</span><span class="mord mathit">e</span><span class="mord"><span class="mord mathit">s</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.10903em;">U</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord mathit">s</span><span class="mclose">)</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathit">s</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span></span></span></span> seemed to be true by definition, but Lean would not definitionally unfold the restriction map from <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>F</mi><mo>+</mo></msup><mo>(</mo><mi>X</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">F^+(X)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.771331em;"></span><span class="strut bottom" style="height:1.021331em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.771331em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mbin mtight">+</span></span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mclose">)</span></span></span></span> to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>F</mi><mo>+</mo></msup><mo>(</mo><mi>U</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">F^+(U)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.771331em;"></span><span class="strut bottom" style="height:1.021331em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.771331em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mbin mtight">+</span></span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="mclose">)</span></span></span></span> as a restriction of functions. I had to explicitly push Lean in the right direction with lines like <code>dunfold presheaf_on_basis_to_presheaf, dsimp</code>; I was really surprised that this could make progress when a simple <code>dsimp</code> could not.</p>
<p>But we shouldn't have been doing this anyway. It seems to me that the correct thing to do is:</p>
<p>1) Define the construction <code>presheaf_on_basis_to_presheaf</code><br>
2) Define also the actual noncomputable function space, i.e. given <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>F</mi></mrow><annotation encoding="application/x-tex">F</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">F</span></span></span></span> a presheaf on a basis, and an open set $$U$ (not necc in the basis), define the space of functions sending an element <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi></mrow><annotation encoding="application/x-tex">x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">x</span></span></span></span> of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>U</mi></mrow><annotation encoding="application/x-tex">U</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">U</span></span></span></span> to an element of the stalk <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>F</mi><mi>x</mi></msub></mrow><annotation encoding="application/x-tex">F_x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:-0.13889em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">x</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>, and have some coercion from <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>F</mi><mo>+</mo></msup><mo>(</mo><mi>U</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">F^+(U)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.771331em;"></span><span class="strut bottom" style="height:1.021331em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.771331em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mbin mtight">+</span></span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="mclose">)</span></span></span></span> to this space of functions.<br>
3) Crucially, prove (by rfl) that the restriction map on <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>F</mi><mo>+</mo></msup></mrow><annotation encoding="application/x-tex">F^+</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.771331em;"></span><span class="strut bottom" style="height:0.771331em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.771331em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mbin mtight">+</span></span></span></span></span></span></span></span></span></span></span> really is just restriction of functions. This is some key lemma which if you don't explicitly say it, can get buried. Prove it for values too -- prove that if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi><mo>∈</mo><msup><mi>F</mi><mo>+</mo></msup><mo>(</mo><mi>U</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">S\in F^+(U)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.771331em;"></span><span class="strut bottom" style="height:1.021331em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span><span class="mrel">∈</span><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.771331em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mbin mtight">+</span></span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="mclose">)</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>V</mi><mo>⊆</mo><mi>U</mi></mrow><annotation encoding="application/x-tex">V\subseteq U</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.8193em;vertical-align:-0.13597em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.22222em;">V</span><span class="mrel">⊆</span><span class="mord mathit" style="margin-right:0.10903em;">U</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mo>∈</mo><mi>V</mi></mrow><annotation encoding="application/x-tex">x\in V</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.72243em;vertical-align:-0.0391em;"></span><span class="base"><span class="mord mathit">x</span><span class="mrel">∈</span><span class="mord mathit" style="margin-right:0.22222em;">V</span></span></span></span> then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>r</mi><mi>e</mi><mi>s</mi><mo>(</mo><mi>S</mi><mo>)</mo><mo>(</mo><mi>x</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">S(x)=res(S)(x)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.02778em;">r</span><span class="mord mathit">e</span><span class="mord mathit">s</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.05764em;">S</span><span class="mclose">)</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span></span></span></span>. This is how you will eliminate <code>res</code> in practice. We were having to eliminate it using <code>dunfold</code> and then <code>dsimp</code>.<br>
4) Also crucially, you should hide the <code>classical.indefinite_description</code>s. Given local sections <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>s</mi><mi>i</mi></msub></mrow><annotation encoding="application/x-tex">s_i</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.58056em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">s</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> which agree on overlaps, there's a non-computable function on <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>U</mi></mrow><annotation encoding="application/x-tex">U</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">U</span></span></span></span> which agrees with each <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>s</mi><mi>i</mi></msub></mrow><annotation encoding="application/x-tex">s_i</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.58056em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">s</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>, but to define it at <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi></mrow><annotation encoding="application/x-tex">x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">x</span></span></span></span> you have to choose <br>
<span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>i</mi></mrow><annotation encoding="application/x-tex">i</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.65952em;"></span><span class="strut bottom" style="height:0.65952em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">i</span></span></span></span> with <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mo>∈</mo><msub><mi>U</mi><mi>i</mi></msub></mrow><annotation encoding="application/x-tex">x\in U_i</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord mathit">x</span><span class="mrel">∈</span><span class="mord"><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:-0.10903em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>. It's a theorem that the resulting function is independent of all choices. Define the noncomputable function and prove the theorem -- you will need it later!</p>
<p>We'd done none of this, and it was only when struggling through the proof that I began to understand what was missing. </p>
<p>I know you (Johan) are working in a far more complicated situation, but somehow these are the things which seem to me to be necessary to make things work smoothly. Ramon arrived in my office with a goal that had three <code>classical.indefinite_description</code>s on one side of an equality, and these are horrible to work with. The idea which Patrick showed so convincingly in his Nantes talk -- hide the nonconstructive stuff with a <code>choose</code> tactic and immediately go to the noncomputable function and the proof that it has the key property you want -- is a really important trick for getting things to run smoothly.</p>

#### [ Johan Commelin (Jan 29 2019 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/157127474):
<p>Thanks for these detailed comments! They will probably be helpful when I pick up my work on sheaves again in a couple of days!</p>

#### [ Kevin Buzzard (Jan 29 2019 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/157127497):
<p>How do you extend the presheaf on a basis in your generality?</p>

#### [ Kevin Buzzard (Jan 29 2019 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/157127506):
<p>Is it still a stalk-valued function?</p>

#### [ Johan Commelin (Jan 29 2019 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/157127610):
<p>You can take a limit over all basic opens contained in <code>U</code>.</p>

#### [ Kevin Buzzard (Jan 29 2019 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/157127633):
<p>Does that work for sites?</p>

#### [ Johan Commelin (Jan 29 2019 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/157127653):
<p>Yes, extending the presheaf is not too hard. What I'm missing is a good API for the sheaf condition.</p>

#### [ Kevin Buzzard (Jan 29 2019 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/157127736):
<p>What I learnt today was that there are special extra lemmas for presheaves which have come from a presheaf-on-a-basis, and those are what we needed to prove that sheaves go to sheaves.</p>

#### [ Johan Commelin (Jan 29 2019 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/157127754):
<p>Because it needs to work with abstract sites (where you don't know anything about the opens in your category) and then it should also work for concrete things like the open sets in a concrete topological space (and your presheaf has some concrete interpretation as functions)... somehow these two things don't play nicely together yet.</p>

#### [ Kevin Buzzard (Jan 29 2019 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/157127787):
<p>But your limit is different. You're taking a subset of a product perhaps.</p>

#### [ Kevin Buzzard (Jan 29 2019 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/157128038):
<p>Hmm. Maybe the ideas are still the same. I'm perhaps suggesting that you spend some time proving lemmas (by rfl) about the function sending an open U to the product of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>F</mi><mo>(</mo><msub><mi>U</mi><mi>i</mi></msub><mo>)</mo></mrow><annotation encoding="application/x-tex">F(U_i)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mopen">(</span><span class="mord"><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:-0.10903em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mclose">)</span></span></span></span> where the <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>U</mi><mi>i</mi></msub></mrow><annotation encoding="application/x-tex">U_i</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:-0.10903em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> range over the basis elements that are part of a cover. Then prove that if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>V</mi></mrow><annotation encoding="application/x-tex">V</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.22222em;">V</span></span></span></span> is a subset of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>U</mi></mrow><annotation encoding="application/x-tex">U</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">U</span></span></span></span> then the restriction map is something like "restrict to the <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>U</mi><mi>i</mi></msub></mrow><annotation encoding="application/x-tex">U_i</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:-0.10903em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> which map to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>V</mi></mrow><annotation encoding="application/x-tex">V</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.22222em;">V</span></span></span></span>". Or something.</p>

#### [ Johan Commelin (Jan 29 2019 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/157128445):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> <span class="user-mention" data-user-id="132858">@Ramon Fernandez Mir</span> Does this mean that you are now rapidly approaching a cleaned up version of schemes? When will there be code that we can look at?</p>

#### [ Mario Carneiro (Jan 29 2019 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/157129667):
<p>I would also like to see some code, I might be able to give some tips. I think you should define the glue construction  for functions, i.e. if you have a bunch of functions that agree on overlaps then you get a function on the union. You can put your choices here and never see them again</p>

#### [ Kevin Buzzard (Jan 29 2019 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/157134234):
<p><a href="https://github.com/ramonfmir/lean-scheme" target="_blank" title="https://github.com/ramonfmir/lean-scheme">https://github.com/ramonfmir/lean-scheme</a></p>

#### [ Kevin Buzzard (Jan 29 2019 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/157134245):
<p>We've only just started really, but we're moving along nicely.</p>


{% endraw %}
