---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66336dependentargumenthell.html
---

## Stream: [general](index.html)
### Topic: [dependent argument hell](66336dependentargumenthell.html)

---


{% raw %}
#### [ Scott Morrison (Sep 12 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133771753):
<p>I seem to have backed myself into a corner, and I don't understand how to escape. I would really appreciate some help, as it feels like this problem is an instance of one that will become more and more severe as we do more advanced maths.</p>

#### [ Scott Morrison (Sep 12 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133771756):
<p>I've been working on morphisms of presheaves.</p>

#### [ Scott Morrison (Sep 12 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133771768):
<p>These are "bundled" presheaves, so they consist of a topological space, along with a functor from the category of open sets (morphisms are subsets) to some other category.</p>

#### [ Scott Morrison (Sep 12 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133771812):
<p>A morphism of presheaves <code>(X, O_X) \hom (Y, O_Y)</code> consists of a pair: a function <code>f : X \hom Y</code>, which is just a continuous map, and</p>

#### [ Scott Morrison (Sep 12 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133771817):
<p>a "comorphism", which is a natural transformation from <code>O_Y \to f_* O_X</code>.</p>

#### [ Scott Morrison (Sep 12 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133771858):
<p>The point here is that you can push forward a presheaf on X to presheaf on Y, along a continuous map (take an open set of Y, pull it back via f, then evaluate the presheaf on it).</p>

#### [ Scott Morrison (Sep 12 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133771924):
<p>Now, I want to define the identity presheaf morphism, and I want to define compositions of presheaf morphisms, and check they satisfy the right properties.</p>

#### [ Scott Morrison (Sep 12 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133771965):
<p>Yesterday I managed to do this, but both the constructions and the proofs were very ugly.</p>

#### [ Scott Morrison (Sep 12 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133771976):
<p>Today I've made another attempt, where the constructions are quite a bit better, and the proofs look like they should be easy but get stuck at the last hurdle, when we should just be cancelling off identity morphisms and saying we're done.</p>

#### [ Scott Morrison (Sep 12 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772022):
<p>The code is at &lt;<a href="https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/V_pre.lean" target="_blank" title="https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/V_pre.lean">https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/V_pre.lean</a>&gt;.</p>

#### [ Scott Morrison (Sep 12 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772037):
<p>The particular problem I reach is the proof of <code>comp_id'</code> in constructing <code>instance : category (Presheaf.{u v} C) := ...</code>.</p>

#### [ Scott Morrison (Sep 12 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772085):
<p>Just before the <code>sorry</code>, the goal is</p>
<div class="codehilite"><pre><span></span>C : Type u,
𝒞 : category C,
X Y : Presheaf C,
f : Presheaf_hom X Y,
X_1 : open_set ((Y.X).α)
⊢ functor.map (Y.𝒪) (𝟙 X_1) ≫
      ⇑(f.c) (⇑(map_open_set (𝟙 (Y.X))) X_1) ≫
        functor.map (X.𝒪) (functor.map (map_open_set (f.f)) (𝟙 (⇑(map_open_set (𝟙 (Y.X))) X_1))) =
    ⇑(f.c) X_1
</pre></div>

#### [ Scott Morrison (Sep 12 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772095):
<p>And this should be perfectly manageable. The left hand side is a composition of three morphisms, and we should begin by observing the first and third are actually identity morphisms, since they are explicitly some functor applied to some identity morphism.</p>

#### [ Scott Morrison (Sep 12 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772100):
<p>In particular we should be able to rewrite <code>functor.map (Y.𝒪) (𝟙 X_1) </code> into <code>𝟙 (Y.𝒪 X_1) </code></p>

#### [ Scott Morrison (Sep 12 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772102):
<p>However <code>simp</code> fails.</p>

#### [ Reid Barton (Sep 12 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772147):
<p>Yeah I've had this happen too. In that case the problem was some implicit argument was not <code>X_1</code> but only something defeq to it, and <code>simp</code> didn't like that.</p>

#### [ Reid Barton (Sep 12 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772150):
<p>In my case <code>dsimp, simp</code> worked, but it doesn't look like that will help you judging from the two preceding lines</p>

#### [ Scott Morrison (Sep 12 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772154):
<p>Trying the rewrite by hand, with increasing desperation:</p>
<div class="codehilite"><pre><span></span>rw [category_theory.functor.map_id]
rw [category_theory.functor.map_id Y.𝒪 X_1]
</pre></div>

#### [ Scott Morrison (Sep 12 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772161):
<p><code>rw [category_theory.functor.map_id Y.𝒪 X_1] {md:=semireducible}</code></p>

#### [ Scott Morrison (Sep 12 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772164):
<p>all fail.</p>

#### [ Reid Barton (Sep 12 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772165):
<p><code>erw</code>?</p>

#### [ Scott Morrison (Sep 12 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772166):
<p><code>erw</code> is just the same as <code>{md:=semireducible}</code></p>

#### [ Scott Morrison (Sep 12 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772167):
<p>(I'd usually use <code>erw</code> but didn't want to scare anyone. :-)</p>

#### [ Scott Morrison (Sep 12 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772210):
<p>Reid is exactly right that the problem is an implicit argument.</p>

#### [ Scott Morrison (Sep 12 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772211):
<p>Let's look at that, turning on <code>set_option pp.implict true</code> and inspecting the goal again.</p>

#### [ Scott Morrison (Sep 12 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772226):
<p>The whole thing is a bit long, but the bit that corresponds to <code>functor.map (Y.𝒪) (𝟙 X_1)</code> is</p>
<div class="codehilite"><pre><span></span>@functor.map
        (@open_set (@bundled.α topological_space (@Presheaf.X C 𝒞 Y))
           (examples.topological_space (@Presheaf.X C 𝒞 Y)))
        (@open_set.open_sets (@bundled.α topological_space (@Presheaf.X C 𝒞 Y))
           (examples.topological_space (@Presheaf.X C 𝒞 Y)))
        C
        𝒞
        (@Presheaf.𝒪 C 𝒞 Y)
        X_1
        (⇑(@map_open_set (@Presheaf.X C 𝒞 Y) (@Presheaf.X C 𝒞 Y) (𝟙 (@Presheaf.X C 𝒞 Y))) X_1)
        (𝟙 X_1)
</pre></div>

#### [ Scott Morrison (Sep 12 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772266):
<p>We can see the problem at the end there: the last three arguments are meant to consist of two objects, and a hom between them.</p>

#### [ Scott Morrison (Sep 12 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772271):
<p>However we've got <code>X_1</code>,  <code>(⇑(@map_open_set (@Presheaf.X C 𝒞 Y) (@Presheaf.X C 𝒞 Y) (𝟙 (@Presheaf.X C 𝒞 Y))) X_1)</code>, and <code>(𝟙 X_1)</code>.</p>

#### [ Reid Barton (Sep 12 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772280):
<p>Something like <code>id ⁻¹' X_1</code>, I guess?</p>

#### [ Scott Morrison (Sep 12 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772281):
<p>We really want that second object to just be <code>X_1</code> again.</p>

#### [ Reid Barton (Sep 12 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772283):
<p>is what that long thing is</p>

#### [ Scott Morrison (Sep 12 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772285):
<p>If we <code>dsimp  [map_open_set]</code> we see:</p>

#### [ Scott Morrison (Sep 12 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772329):
<p><code>(@open_set.mk (@bundled.α topological_space (@Presheaf.X C 𝒞 Y))
           (examples.topological_space (@Presheaf.X C 𝒞 Y))
           (@subtype.val
                (@bundled.α topological_space (@Presheaf.X C 𝒞 Y) →
                 @bundled.α topological_space (@Presheaf.X C 𝒞 Y))
                (@continuous (@bundled.α topological_space (@Presheaf.X C 𝒞 Y))
                   (@bundled.α topological_space (@Presheaf.X C 𝒞 Y))
                   (@bundled.str topological_space (@Presheaf.X C 𝒞 Y))
                   (@bundled.str topological_space (@Presheaf.X C 𝒞 Y)))
                (𝟙 (@Presheaf.X C 𝒞 Y)) ⁻¹'
              @open_set.s (@bundled.α topological_space (@Presheaf.X C 𝒞 Y))
                (examples.topological_space (@Presheaf.X C 𝒞 Y))
                X_1)
           _)</code></p>

#### [ Scott Morrison (Sep 12 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772338):
<p>Which sadly is not definitely equal to <code>X_1</code>, although we can prove it is equal.</p>

#### [ Reid Barton (Sep 12 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772385):
<p>oh no</p>

#### [ Scott Morrison (Sep 12 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772386):
<p>In fact, we have a lemma prepared just for this!</p>

#### [ Reid Barton (Sep 12 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772390):
<p>wait then</p>

#### [ Scott Morrison (Sep 12 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772394):
<div class="codehilite"><pre><span></span>@[simp] def map_open_set_id_obj (X : Top) (U : open_set X.α) : map_open_set (𝟙 X) U = U :=
begin dsimp [map_open_set], cases U, congr, end
</pre></div>

#### [ Scott Morrison (Sep 12 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772412):
<p>And <code>rw [map_open_set_id_obj]</code> says ...</p>

#### [ Scott Morrison (Sep 12 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772414):
<p><code>failed</code></p>

#### [ Reid Barton (Sep 12 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772417):
<p>I'm confused</p>

#### [ Reid Barton (Sep 12 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772420):
<p>Doesn't this mean your goal is ill-typed?</p>

#### [ Scott Morrison (Sep 12 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772421):
<p>(And <code>erw</code> is no better, nor does it seem that using <code>conv</code> to zoom in on it helps.)</p>

#### [ Scott Morrison (Sep 12 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772464):
<p>That's what appears to be happening, I agree.</p>

#### [ Scott Morrison (Sep 12 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772467):
<p>So how did Lean let me get this far?</p>

#### [ Reid Barton (Sep 12 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772468):
<p>I had that happen too once, but I didn't understand how it happened, but it's almost certainly unrelated.</p>

#### [ Scott Morrison (Sep 12 2018 at 03:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772479):
<p>I do have a note a few lines earlier in my code <code>It's hard to believe this typechecks!</code></p>

#### [ Scott Morrison (Sep 12 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772519):
<div class="codehilite"><pre><span></span>structure Presheaf_hom (F G : Presheaf.{u v} C) :=
(f : F.X ⟶ G.X)
(c : G.𝒪 ⟹ ((map_open_set f) ⋙ F.𝒪))

namespace Presheaf_hom
def id (F : Presheaf.{u v} C) : Presheaf_hom F F :=
{ f := 𝟙 F.X,
  c := begin apply nat_trans.vcomp, swap, apply whisker_on_right (map_open_set_id _).inv, apply (functor.id_comp _ _ _).inv end
}

def comp {F G H : Presheaf.{u v} C} (α : Presheaf_hom F G) (β : Presheaf_hom G H) : Presheaf_hom F H :=
{ f := α.f ≫ β.f,
  c := β.c ⊟ (whisker_on_left (map_open_set β.f) α.c), -- It&#39;s hard to believe this typechecks!
}
end Presheaf_hom
</pre></div>

#### [ Scott Morrison (Sep 12 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772525):
<p>In particular, I have to jump through some hoops to construct the natural transformation for <code>id</code>.</p>

#### [ Scott Morrison (Sep 12 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772531):
<p>But Lean appears to be happy with me just writing the "obvious" answer for <code>comp</code>.</p>

#### [ Reid Barton (Sep 12 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772542):
<p>I found composition/associativity things are often easier than identity/unitality things</p>

#### [ Scott Morrison (Sep 12 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772591):
<p>(... in real life as well as Lean, for me!)</p>

#### [ Scott Morrison (Sep 12 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772599):
<p>(identities are strange and confusing in higher dimensions!)</p>

#### [ Reid Barton (Sep 12 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772671):
<p>how hard would it be to find the first place the goal becomes ill-typed?<br>
Is the goal before the last <code>simp</code> comprehensible?</p>

#### [ Scott Morrison (Sep 12 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772673):
<p>The only avenues I can work out are:<br>
1) Go back and work out where this "ill-typed, or at least hard-to-see-its-well-typed" expression first appears, and then "do something different".<br>
2) Work out how to "fix" implicit arguments.</p>

#### [ Scott Morrison (Sep 12 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772717):
<p>(This is an example, by the way, of a situation it would be nice to have a good term inspector, where you can toggle on and off implicit arguments for subtrees.)</p>

#### [ Reid Barton (Sep 12 2018 at 03:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772767):
<p>Given that the implicit argument is not even defeq to the right thing, I think 2 isn't applicable in this case.<br>
It looks to me like you hit a bug in Lean (which is probably not in the kernel, since it is only the goal which is ill-typed, but still very frustrating).</p>

#### [ Scott Morrison (Sep 12 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772769):
<p>Oooh, I maybe found a way around it.</p>

#### [ Scott Morrison (Sep 12 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772777):
<p>It's just a matter of <code>dsimp</code>ing expressions in a different order, so somehow it's not at all a principled solution.</p>

#### [ Scott Morrison (Sep 12 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772821):
<p>Oh, no, the problem is there a step or two later. I was just doing something by hand that <code>simp</code> was doing anyway.</p>

#### [ Scott Morrison (Sep 12 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772822):
<p>:-(</p>

#### [ Reid Barton (Sep 12 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772935):
<p>I'm kind of surprised that the result of the tactic passes typechecking, even with <code>sorry</code> there</p>

#### [ Scott Morrison (Sep 12 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772995):
<p>Shall I try for a proof of false? :-)</p>

#### [ Reid Barton (Sep 12 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773004):
<p>Unfortunately I doubt you can prove false from a term which is ill-typed but only in that one of the type arguments is definitionally wrong (but propositionally correct)</p>

#### [ Scott Morrison (Sep 12 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773005):
<p>Okay... this is bizarre, but <code>cases X_1</code> seems to break the impasse.</p>

#### [ Reid Barton (Sep 12 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773006):
<p>that's not surprising</p>

#### [ Scott Morrison (Sep 12 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773008):
<p>Why is that?</p>

#### [ Reid Barton (Sep 12 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773051):
<p>same reason why you used <code>cases U</code> to prove <code>map_open_set_id_obj</code></p>

#### [ Reid Barton (Sep 12 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773055):
<p>basically you have an equality that looks like &lt;x.1, _&gt; = x</p>

#### [ Scott Morrison (Sep 12 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773056):
<p>Okay, and there's a (horrible) proof:</p>
<div class="codehilite"><pre><span></span>  comp_id&#39; := λ X Y f, --sorry,
    begin
      ext,
      -- we check the functions first
      dsimp [Presheaf_hom.id, Presheaf_hom.comp],
      simp,
      -- and now the comorphisms
      dsimp [Presheaf_hom.id, Presheaf_hom.comp],
      simp,
      ext,
      dsimp [whisker_on_right, whiskering_on_right, whisker_on_left, whiskering_on_left],
      dsimp [map_open_set],
      simp,
      erw [category_theory.functor.map_id],
      simp,
      cases X_1,
      simp,
      apply congr_fun,
      simp,
    end,
</pre></div>

#### [ Reid Barton (Sep 12 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773062):
<p>where x is a variable, and so they can never be definitionally equal. Buf after <code>cases x</code>, it's okay</p>

#### [ Scott Morrison (Sep 12 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773063):
<p>I see.</p>

#### [ Reid Barton (Sep 12 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773064):
<p>when you do comp, both sides look like &lt;_, _&gt;</p>

#### [ Reid Barton (Sep 12 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773065):
<p>and that's why comp is easier</p>

#### [ Reid Barton (Sep 12 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773107):
<p>This still feels weird to me, but I've seen it a few times</p>

#### [ Scott Morrison (Sep 12 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773113):
<p>So maybe the summary from today is:</p>
<blockquote>
<p>avoid <code>cases</code> when constructing stuff, because then you'll have horrible <code>X.rec</code> expressions to deal with later, but<br>
remember to try <code>cases</code> when an implicit argument looks wrong!</p>
</blockquote>

#### [ Reid Barton (Sep 12 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773166):
<p>Well, in general when you need to prove <code>(blah.mk _ _) = X</code>, it will require doing cases on X</p>

#### [ Reid Barton (Sep 12 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773170):
<p>I still think something very fishy is going on with your original code</p>

#### [ Scott Morrison (Sep 12 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773173):
<p>Sure. The problem here was that it wasn't at all obvious to me that this was what was going on.</p>

#### [ Mario Carneiro (Sep 12 2018 at 04:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773227):
<p>The file you linked references <code>category_theory.examples.topological_spaces</code> but I can't find it in the repo</p>

#### [ Scott Morrison (Sep 12 2018 at 04:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773228):
<p>That's in mathlib</p>

#### [ Scott Morrison (Sep 12 2018 at 04:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773229):
<p>:-)</p>

#### [ Reid Barton (Sep 12 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773271):
<p>I just finished building your repo locally so I can take a look</p>

#### [ Scott Morrison (Sep 12 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773278):
<p>And just to confound you, Mario, lean-category-theory is currently pointing at a branch of mathlib on <code>community</code>, in which that file has been modified. :-)</p>

#### [ Reid Barton (Sep 12 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773287):
<p>Anyways the situation you were in ought to have been impossible. If <code>x : t</code> and <code>x : t'</code> then <code>t</code> and <code>t'</code> should be definitionally equal. Not just propositionally equal.</p>

#### [ Reid Barton (Sep 12 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773288):
<p>At least, as far as I understand.</p>

#### [ Scott Morrison (Sep 12 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773290):
<p>yes.</p>

#### [ Mario Carneiro (Sep 12 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773291):
<p>oh wow, mathlib category theory has grown quite a bit since I last checked</p>

#### [ Mario Carneiro (Sep 12 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773444):
<div class="codehilite"><pre><span></span>-- Do I dare define `open_set` as a functor from Top to CAT? I don&#39;t like CAT.

def map_open_set
  {X Y : Top} (f : X ⟶ Y) : open_set Y.α ⥤ open_set X.α :=
</pre></div>


<p>Why is it a functor to CAT? It looks like <code>open_set</code> should be a (contravariant) functor from <code>Top</code> to <code>Type</code></p>

#### [ Scott Morrison (Sep 12 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773453):
<p>For each topological space X, we get the category of open sets and inclusions.</p>

#### [ Reid Barton (Sep 12 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773493):
<p>The ill-typed goal I encountered involved Lean getting confused about the difference between <code>quot</code> and <code>quotient</code>, and so I had a goal involving some types of the form <code>quot s a</code> where <code>s</code> was a setoid, which I had trouble producing</p>

#### [ Mario Carneiro (Sep 12 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773568):
<p>Okay, I think I'm starting to piece this together. There is an unnamed function <code>comap f U</code> (where <code>f</code> is a bundled continuous function and <code>U</code> is an <code>open_set</code>) which is the object part of <code>map_open_set</code></p>

#### [ Mario Carneiro (Sep 12 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773575):
<p>And what is true is that <code>map_open_set (𝟙 X) U = comap (𝟙 X) U</code>, which is isomorphic to <code>U</code></p>

#### [ Mario Carneiro (Sep 12 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773613):
<p>so you have a classic two-category problem</p>

#### [ Scott Morrison (Sep 12 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773625):
<p>I don't know this classic. :-)</p>

#### [ Reid Barton (Sep 12 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773626):
<p>I think Mario means 2-category?</p>

#### [ Mario Carneiro (Sep 12 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773628):
<p>You have to worry about coherences since it's not an equality</p>

#### [ Scott Morrison (Sep 12 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773629):
<p>Oh, okay! :-)</p>

#### [ Scott Morrison (Sep 12 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773666):
<p>Yes.</p>

#### [ Reid Barton (Sep 12 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773667):
<p>Like, the Top -&gt; Cat thing could be only a pseudofunctor</p>

#### [ Mario Carneiro (Sep 12 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773672):
<p>As Kevin learned a while ago, a propositional equality should not ever be treated as equality in a category, only isomorphism</p>

#### [ Mario Carneiro (Sep 12 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773673):
<p>objects are either defeq or isomorphic</p>

#### [ Scott Morrison (Sep 12 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773674):
<p>but where am I abusing that here?</p>

#### [ Mario Carneiro (Sep 12 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773684):
<div class="codehilite"><pre><span></span>-- These next two are desperate attempts to solve problems below.
@[simp] def map_open_set_id_obj (X : Top) (U : open_set X.α) : map_open_set (𝟙 X) U = U :=
begin dsimp [map_open_set], cases U, congr, end
@[simp] def map_open_set_id (X : Top) : map_open_set (𝟙 X) ≅ functor.id (open_set X.α) :=
</pre></div>


<p>this is bad news</p>

#### [ Mario Carneiro (Sep 12 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773691):
<p>this equality should be turned into an iso, given a name, and explicitly reasoned with</p>

#### [ Scott Morrison (Sep 12 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773692):
<p>It's the first one that is evil</p>

#### [ Scott Morrison (Sep 12 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773694):
<p>and I don't use it</p>

#### [ Scott Morrison (Sep 12 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773736):
<p>the second one is fine, isn't it?</p>

#### [ Reid Barton (Sep 12 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773743):
<p>the type looks fine, but now I am confused about the implementation</p>

#### [ Mario Carneiro (Sep 12 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773744):
<p>I think? I can't parse it</p>

#### [ Scott Morrison (Sep 12 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773745):
<p>I just pushed an update</p>

#### [ Mario Carneiro (Sep 12 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773746):
<p><code>map_open_set (𝟙 X)</code> is a functor, so what does <code>≅</code> mean here?</p>

#### [ Scott Morrison (Sep 12 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773748):
<p>that has the working proof, and doesn't have the evil <code>map_open_set_id_obj</code></p>

#### [ Scott Morrison (Sep 12 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773786):
<p>iso is automatically natural isomorphism</p>

#### [ Scott Morrison (Sep 12 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773791):
<p>sweet sweet typeclass magic finds the category of functors between two fixed categories</p>

#### [ Reid Barton (Sep 12 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773792):
<p>isomorphism in the functor category</p>

#### [ Scott Morrison (Sep 12 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773793):
<p>and correctly interprets iso</p>

#### [ Mario Carneiro (Sep 12 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773796):
<p>and that doesn't have any 2-category mess in it?</p>

#### [ Scott Morrison (Sep 12 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773799):
<p>no -- for a fixed pair of categories C and D</p>

#### [ Scott Morrison (Sep 12 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773804):
<p>functors and natural transformations between them are a perfectly honest 1-category</p>

#### [ Scott Morrison (Sep 12 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773806):
<p>(indeed, the prototypical example)</p>

#### [ Reid Barton (Sep 12 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773899):
<p>Oh man this is confusing.</p>

#### [ Mario Carneiro (Sep 12 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773901):
<p>so where did you get that bad application from? <code>functor.map (Y.𝒪) (𝟙 X_1)</code></p>

#### [ Reid Barton (Sep 12 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773903):
<p>I noticed that both of these worked, and was confused.</p>
<div class="codehilite"><pre><span></span>  <span class="o">{</span> <span class="n">app</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span><span class="o">,</span> <span class="k">show</span> <span class="n">map_open_set</span> <span class="o">(</span><span class="mi">𝟙</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="err">⟶</span> <span class="n">U</span><span class="o">,</span> <span class="k">from</span> <span class="mi">𝟙</span> <span class="n">U</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">app</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span><span class="o">,</span> <span class="k">show</span> <span class="n">U</span> <span class="err">⟶</span> <span class="n">U</span><span class="o">,</span> <span class="k">from</span> <span class="mi">𝟙</span> <span class="n">U</span> <span class="o">},</span>
</pre></div>

#### [ Reid Barton (Sep 12 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773910):
<p>Even though we know <code>map_open_set (𝟙 X) U = U</code> is not a definitional equality</p>

#### [ Mario Carneiro (Sep 12 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773911):
<p>hah, it's because the hom destructs it</p>

#### [ Reid Barton (Sep 12 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773913):
<p>right</p>

#### [ Scott Morrison (Sep 12 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773916):
<p>Yeah, and I think this is where the "bad" application is coming from.</p>

#### [ Scott Morrison (Sep 12 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773956):
<p>Can you explain what "the hom destructs it" means?</p>

#### [ Reid Barton (Sep 12 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773962):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_subset</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">subset</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span> <span class="n">V</span><span class="o">,</span> <span class="n">U</span><span class="bp">.</span><span class="n">s</span> <span class="err">⊆</span> <span class="n">V</span><span class="bp">.</span><span class="n">s</span> <span class="o">}</span>
</pre></div>

#### [ Reid Barton (Sep 12 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773970):
<p>this is what defines the partial order, and therefore the hom types</p>

#### [ Scott Morrison (Sep 12 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773972):
<p>oh ...</p>

#### [ Reid Barton (Sep 12 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774013):
<p>it's not true that <code>map_open_set (𝟙 X) U = U</code> definitionally, but it is true that <code>(map_open_set (𝟙 X) U).s = U.s</code> because (contrary to my initial guess) <code>preimage id</code> is definitionally the identity</p>

#### [ Scott Morrison (Sep 12 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774014):
<p>I see.</p>

#### [ Reid Barton (Sep 12 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774017):
<p>Oh, wait...</p>

#### [ Reid Barton (Sep 12 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774022):
<p>So maybe that weird goal was correctly typed, after all</p>

#### [ Scott Morrison (Sep 12 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774023):
<p>Yeah.</p>

#### [ Scott Morrison (Sep 12 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774028):
<p>And I could have replaced my evil lemma with</p>

#### [ Scott Morrison (Sep 12 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774071):
<div class="codehilite"><pre><span></span>@[simp] def map_open_set_id_obj (X : Top) (U : open_set X.α) : (map_open_set (𝟙 X) U).s = U.s := rfl
</pre></div>

#### [ Scott Morrison (Sep 12 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774072):
<p>and perhaps had it work...</p>

#### [ Scott Morrison (Sep 12 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774082):
<p>Hmm,. you can indeed prove that via <code>rfl</code>, but I can't get it to help.</p>

#### [ Scott Morrison (Sep 12 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774124):
<p>ah, I have to remove the dsimp [map_open_set], perhaps</p>

#### [ Mario Carneiro (Sep 12 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774125):
<p>Scott, I'm trying to get your repo. How do you update everything with leanpkg?</p>

#### [ Scott Morrison (Sep 12 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774127):
<p><code>leanpkg build</code>?</p>

#### [ Scott Morrison (Sep 12 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774129):
<p>It should notice if you don't have the right dependencies already in <code>_target</code>.</p>

#### [ Mario Carneiro (Sep 12 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774130):
<p>I get version mismatch error</p>

#### [ Scott Morrison (Sep 12 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774136):
<p>ah... Is your lean provided by elan?</p>

#### [ Scott Morrison (Sep 12 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774137):
<p>This repo is set to use nightly-2018-06-21</p>

#### [ Scott Morrison (Sep 12 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774139):
<p>but I think it should be safe to change that in leanpkg.toml file</p>

#### [ Scott Morrison (Sep 12 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774140):
<p>What is the "official recommendation" these days?</p>

#### [ Mario Carneiro (Sep 12 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774179):
<p>I've been using 3.4.1 even though a few bugfixes have come in</p>

#### [ Scott Morrison (Sep 12 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774185):
<p>Since my student Keeley started forking Lean I've switched to using elan and don't notice these problems. :-)</p>

#### [ Mario Carneiro (Sep 12 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774188):
<p>that's good to hear. You should write a tutorial :)</p>

#### [ Reid Barton (Sep 12 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774233):
<p>for elan?</p>

#### [ Scott Morrison (Sep 12 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774234):
<p>I really should borrow a windows machine, and write a tutorial for running elan on windows.</p>

#### [ Scott Morrison (Sep 12 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774365):
<p>Ducking out for lunch. Thanks very much for the discussion today!</p>

#### [ Mario Carneiro (Sep 12 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774471):
<p>Aha, I found some 2-categoricity:</p>
<div class="codehilite"><pre><span></span>structure Presheaf_hom (F G : Presheaf.{u v} C) :=
(f : F.X ⟶ G.X)
(c : G.𝒪 ⟹ ((map_open_set f) ⋙ F.𝒪))
</pre></div>


<p>Since <code>Presheaf_hom</code> has a component which is a functor, proving equality of homs is going to involve equality of objects</p>

#### [ Mario Carneiro (Sep 12 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774631):
<p>I guess that can't really be avoided, but since <code>G.𝒪</code> is a functor out of a skeletal category (a partial order category), it suffices to prove isomorphism instead of equality</p>

#### [ Mario Carneiro (Sep 12 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774739):
<div class="codehilite"><pre><span></span>@[extensionality] lemma ext {F G : Presheaf.{u v} C} (α β : Presheaf_hom F G)
  (w : α.f = β.f) (h : α.c == β.c)
  : α = β :=
</pre></div>


<p>the <code>heq</code> here is evil. You should state some kind of composite equality here</p>

#### [ Scott Morrison (Sep 12 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133775001):
<p>Hi <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>, actually that component <code>Preasheaf_hom.c</code> is a natural transformation, not a functor, so equality is non-evil.</p>

#### [ Scott Morrison (Sep 12 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133775042):
<p>I agree that the <code>ext</code> lemma is evil. I will replace that.</p>

#### [ Mario Carneiro (Sep 12 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133775051):
<p>equality of natural transformations is not evil, equality of natural transformations in different categories is</p>

#### [ Scott Morrison (Sep 12 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133775062):
<p>Oh, so you're saying specifically the <code>heq</code> is evil.</p>

#### [ Scott Morrison (Sep 12 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133775075):
<p>I don't think we'll ever to to say anything about equalities of objects, however.</p>

#### [ Mario Carneiro (Sep 12 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133775136):
<p>I think I found the culprit. <code>map_open_sets</code> is a 2-categorical thing, since it takes homs to functors. This means that congruence says that equality of homs maps to natural iso of functors</p>

#### [ Mario Carneiro (Sep 12 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133775143):
<p>And this is the iso you should reference in the definition of <code>ext</code></p>

#### [ Scott Morrison (Sep 12 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133775147):
<p>I'm filling in </p>
<div class="codehilite"><pre><span></span>def map_open_set_iso {X Y : Top} (f g : X ⟶ Y) (h : f = g) : map_open_set f ≅ map_open_set g := {

}
</pre></div>

#### [ Scott Morrison (Sep 12 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133775148):
<p>right now</p>

#### [ Kevin Buzzard (Sep 12 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133781152):
<p>This is a terrifying thread to wake up to. It reminds me of when I couldn't prove anything about real numbers because there was no norm_num. But instead of a beginner struggling to prove math-trivial things because of a lack of tools, it's experts and tool-makers having problems with something that looks math-trivial</p>

#### [ Kevin Buzzard (Sep 12 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133781442):
<p>I actually stopped thinking about pushing the perfectoid repo forward towards the definition of an adic space because this funky category showed up, Patrick was doing completions (which were also needed) and I knew someone had to do integral closures (which were also needed) so I went back to those and thought I'd wait a bit to see what the category experts thought about this category V_pre which had shown up "in the wild". I want to argue that we don't <em>need</em> V_pre, it's just a convenient container and I thought it would be a good test case. I could instead just make a new structure modelling the objects and muddle on from there and it would no doubt be fine at least as far as the ultimate goal is concerned, which is a definition.</p>

#### [ Mario Carneiro (Sep 12 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133781575):
<p>I think this thread is Scott having an epiphany similar to the one that prompted that blog post <a href="https://mathematicswithoutapologies.wordpress.com/2018/09/11/guest-post-by-kevin-buzzard/" target="_blank" title="https://mathematicswithoutapologies.wordpress.com/2018/09/11/guest-post-by-kevin-buzzard/">https://mathematicswithoutapologies.wordpress.com/2018/09/11/guest-post-by-kevin-buzzard/</a></p>

#### [ Mario Carneiro (Sep 12 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133781606):
<p>I think it boils down to "equalities of types are evil"</p>

#### [ Kevin Buzzard (Sep 12 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133784114):
<p>As I'm sure you realise, that comment (it was only supposed to be a comment!) was very much informed by the comments you made when I was having that big meltdown about equality a few months ago ("Kevin, stop trolling!").</p>

#### [ Kevin Buzzard (Sep 12 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133784227):
<p>A summer student, Ned Summers, was doing some 4th year category theory example sheet questions (using Scott's library as a dependency) and ran into these sorts of problems, and this time I was better equipped. Chris (who freely admits he knows nothing about category theory) had suggested some casts which had caused trouble for Ned, and I diagnosed the problem as exactly the same sort of thing: Ned had two objects X and Y and a proof that they were equal, and was doing exactly what a mathematican would do -- treating Hom(X,Z) as equal to Hom(Y,Z) etc etc. Equality in type theory is more delicate than that. Of course this doesn't change the fact that we are right, and your definition is rubbish -- but it's what we've got to work with ;-)</p>

#### [ Kenny Lau (Sep 12 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133784234):
<blockquote>
<p>A summer student, Ned Summers</p>
</blockquote>

#### [ Kevin Buzzard (Sep 12 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133784295):
<p>They've almost all gone now. Ned stopped on Friday. Only about three left. I am going to spend all day writing documentation and basic questions. Yesterday I said "we want ten basic examples and ten basic questions about metaprogramming" -- today I'm (hopefully) going to write ten basic examples and ten basic questions about set membership.</p>

#### [ Kevin Buzzard (Sep 12 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133784364):
<p>I asked a question on this chat probably last Wed or Thurs about how to generate "the identity morphism" between two objects which were provably equal, and Reid answered very quickly with some function called something like <code>iso_of_eq</code> which generated the data from the proof; it was because of my schemes meltdown that I had understood that this was what was missing.</p>

#### [ Chris Hughes (Sep 12 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133786353):
<p>I didn't suggest the use of <code>eq.rec</code>. My instinct would be that <code>eq.rec</code> for data should be avoided if at all possible</p>

#### [ Kevin Buzzard (Sep 12 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133788910):
<p>Maybe I got the wrong impression from Ned :-)</p>

#### [ Scott Morrison (Sep 12 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133794864):
<p>Thanks to some help from Mario and Reid, it is well sorted out now!</p>

#### [ Scott Morrison (Sep 12 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133794955):
<p>While I agree that I was making mistakes (being "evil") when I shouldn't have been, and the code is nicer as a result of today's exorcism, the fundamental cause of being stuck was something a bit different. I really need to catch up on sleep now, so I won't explain it now. :-)</p>

#### [ Scott Morrison (Sep 12 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133794972):
<p>The upshot is that &lt;<a href="https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/presheaves.lean" target="_blank" title="https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/presheaves.lean">https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/presheaves.lean</a>&gt; contains the definition of bundled presheaves (i.e. a topological space and a presheaf on it), and the right notion of morphisms between these, and indeed the category structure.</p>

#### [ Scott Morrison (Sep 12 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133794979):
<p>It's certainly not all of <code>V_pre</code>, but it's the categorical theoretic core.</p>

#### [ Patrick Massot (Sep 12 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133794986):
<p>Yeah, "Lean does no magic" ™ but sometimes a good exorcism session is needed</p>

#### [ Scott Morrison (Sep 12 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133795036):
<p>Hopefully from this point on it is just adding bells and whistles (that stalk needs to be local, these valuations need to be jiggered by the whatsit).</p>

#### [ Scott Morrison (Sep 12 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133795050):
<p>Happily, the category of presheaves is actually pretty easy to PR now. I only have one dependency, about whiskering, and that looks easy to clean up. So this may be in mathlib soon.</p>

#### [ Kenny Lau (Sep 12 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133837710):
<blockquote>
<p>to reduce an <code>eq.rec</code> you need the major premise to become <code>refl</code> somehow</p>
<p>that usually means finding the appropriate equality in the context and generalizing it until one side is a variable, and then <code>subst</code>, which is to say use <code>eq.rec</code> in the proof term</p>
</blockquote>
<p><a href="#narrow/stream/113488-general/subject/so.20what.20is.20eq.2Erec.3F/near/125134372" title="#narrow/stream/113488-general/subject/so.20what.20is.20eq.2Erec.3F/near/125134372">Mario Carneiro, 16/04/2018 04:39:04 (UTC)</a></p>

#### [ Kenny Lau (Sep 12 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133837740):
<p>underrated comment</p>

#### [ Kenny Lau (Sep 12 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133842645):
<p>wow I had an <code>eq.rec</code> in my goal and it took me nearly 2 hours to destruct it</p>

#### [ Reid Barton (Sep 12 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133845614):
<p>sounds about right</p>

#### [ Scott Morrison (Sep 13 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133856278):
<p>I feel like <code>eq.rec</code> is such a disaster that we need special VS Code plugin support: a little zulip box that pops up, with a message: "Help me, Mario!" ready to be sent...</p>

#### [ Kenny Lau (Sep 13 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133866974):
<p>ok so eq.rec isn't really the problem. The problem is sometimes you can't just rewrite something with an equality <code>a = b</code> because that something depends on <code>a</code> and <code>b</code> being those expressions. And the solution is to generalize <code>a</code> in all places in which that expression occurs, and then <code>subst</code> that equality</p>

#### [ Kenny Lau (Sep 13 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133866988):
<p>sometimes you can't just generalize <code>a</code>, but you have to generalize a lot of things</p>

#### [ Kenny Lau (Sep 13 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133866989):
<p>a strategy is to generalize all proofs first (<code>set_option pp.proofs true</code>), because that will always work because of proof irrelevance</p>

#### [ Scott Morrison (Sep 14 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133947991):
<p>Slowly making progress here. This now compiles:</p>
<div class="codehilite"><pre><span></span>def stalks_local (F : Presheaf.{u+1 u} TopRing) : Type u :=
Π x : F, local_ring (((TopRing.forget_to_CommRing).map_presheaf F).stalk_at x)

def V_pre_pre := Σ (F : Presheaf.{u+1 u} TopRing), stalks_local F

example : category.{u+1 u} V_pre_pre := by unfold V_pre_pre; apply_instance
</pre></div>


{% endraw %}
