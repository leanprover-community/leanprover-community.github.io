---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21691simpinsideexpressionswithcoetofunsometimesfails.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [simp inside expressions with coe_to_fun sometimes fails](https://leanprover-community.github.io/archive/113488general/21691simpinsideexpressionswithcoetofunsometimesfails.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Aug 06 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130948850):
<p>I've been trying to implement <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> request that in my baby PR for category theory I use coercions to allow applying a functor to an object, as <code>F X</code>, rather than having to either write explicitly <code>F.onObjects X</code>, or introduce some awkward notation, such as <code>F +&gt; X</code>.</p>

#### [ Scott Morrison (Aug 06 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130948858):
<p>I would very much like to do this, but I also want to be confident that this doesn't mess up the nice and easy automation I have throughout my category theory library.</p>

#### [ Scott Morrison (Aug 06 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130948897):
<p>Unfortunately, I seem to have run into a problem, which is a strange interaction between coercions and the simplifier.</p>

#### [ Scott Morrison (Aug 06 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130948901):
<p>Hopefully someone here will explain how to get around this! I fear that the fix would require tweaking the simplifier, which is out of bounds at the moment.</p>

#### [ Scott Morrison (Aug 06 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130948911):
<p>In any case, here is a self-contained piece of code, containing some very cut down definitions from the category theory library, that demonstrates the problem.</p>

#### [ Scott Morrison (Aug 06 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130948964):
<p>Essentially, it is that <code>simp</code> sometimes can't rewrite under a coercion, because it can't build the proof terms (in particular, it can't build some <code>congr_arg</code> terms, because of a type checking subtlety).</p>

#### [ Scott Morrison (Aug 06 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130948985):
<p>This has the result that in order to be able to use <code>simp</code> successfully, I'll have to provide two versions of many lemmas: one for use by humans, that refer to the coercions, and one for use by <code>simp</code> (after applying <code>unfold_coes</code> to unfold all the coercions), that don't refer to the coercions.</p>

#### [ Scott Morrison (Aug 06 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130948986):
<p>In my mind, that's worse than not having the coercions available in the first place.</p>

#### [ Scott Morrison (Aug 06 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949027):
<div class="codehilite"><pre><span></span>import tactic.interactive

universe u

class category (Obj : Type u) : Type (u+1) :=
(Hom : Obj → Obj → Type u)
(identity : Π X : Obj, Hom X X)

notation `𝟙` := category.identity     -- type as \b1
infixr ` ⟶ `:10  := category.Hom     -- type as \h

variable (C : Type u)
variable [𝒞 : category C]
variable (D : Type u)
variable [𝒟 : category D]
include 𝒞 𝒟

instance ProductCategory : category (C × D) :=
{ Hom            := λ X Y, ((X.1) ⟶ (Y.1)) × ((X.2) ⟶ (Y.2)),
  identity       := λ X, ⟨ 𝟙 (X.1), 𝟙 (X.2) ⟩ }

@[simp] lemma ProductCategory.identity (X : C) (Y : D) : 𝟙 (X, Y) = (𝟙 X, 𝟙 Y) := by refl

structure Functor  :=
(onObjects     : C → D)
(onMorphisms   : Π {X Y : C}, (X ⟶ Y) → ((onObjects X) ⟶ (onObjects Y)))
(identities    : ∀ (X : C), onMorphisms (𝟙 X) = 𝟙 (onObjects X))

attribute [simp] Functor.identities

infixr ` +&gt; `:70 := Functor.onObjects
infixr ` &amp;&gt; `:70 := Functor.onMorphisms
infixr ` ↝ `:70 := Functor -- type as \lea

variables {C} {D}

structure NaturalTransformation (F G : C ↝ D) : Type u :=
(components: Π X : C, (F +&gt; X) ⟶ (G +&gt; X))

infixr ` ⟹ `:50  := NaturalTransformation

instance {F G : C ↝ D} : has_coe_to_fun (F ⟹ G) :=
{ F   := λ α, Π X : C, (F +&gt; X) ⟶ (G +&gt; X),
  coe := λ α, α.components }

definition IdentityNaturalTransformation (F : C ↝ D) : F ⟹ F :=
{ components := λ X, 𝟙 (F +&gt; X) }

instance FunctorCategory : category (C ↝ D) :=
{ Hom            := λ F G, F ⟹ G,
  identity       := λ F, IdentityNaturalTransformation F }

@[simp] lemma FunctorCategory.identity.components (F : C ↝ D) (X : C) : (𝟙 F : F ⟹ F) X = 𝟙 (F +&gt; X) := by refl

lemma test (E : Type u) [ℰ : category E] (X : C) (Y : D) (F : C ↝ (D ↝ E)) : (F &amp;&gt; (prod.fst (𝟙 (X, Y)))) Y = 𝟙 ((F +&gt; X) +&gt; Y) :=
begin
  -- Really, `simp` should just work, finishing the goal.
  -- However this doesn&#39;t work:
  success_if_fail {simp},
  -- Notice that rewriting with that simp lemma succeeds:
  rw ProductCategory.identity,
  dsimp,
  -- Again, this `simp` fails:
  success_if_fail {simp},
  rw Functor.identities,
  -- Finally, at this stage `simp` manages to apply FunctorCategory.identity.components
  simp,
end

lemma test&#39; (E : Type u) [ℰ : category E] (X : C) (Y : D) (F : C ↝ (D ↝ E)) : (F &amp;&gt; (prod.fst (𝟙 (X, Y)))) Y = 𝟙 ((F +&gt; X) +&gt; Y) :=
begin
  -- If we unfold all the coercions first, at least `simp` gets started
  unfold_coes,
  simp,
  -- But doesn&#39;t finish, because with the coercions gone, FunctorCategory.identity.components doesn&#39;t apply anymore!
  admit
end

-- We can define an alternative version of that @[simp] lemma, with the coercion removed.
@[simp] lemma FunctorCategory.identity.components&#39; (F : C ↝ D) (X : C) : (𝟙 F : F ⟹ F).components X = 𝟙 (F +&gt; X) := by refl

lemma test&#39;&#39; (E : Type u) [ℰ : category E] (X : C) (Y : D) (F : C ↝ (D ↝ E)) : (F &amp;&gt; (prod.fst (𝟙 (X, Y)))) Y = 𝟙 ((F +&gt; X) +&gt; Y) :=
begin
  unfold_coes,
  simp,
  -- At this stage, we&#39;ve recovered reasonable automation, at the expense of having to
  -- state lemmas twice, once with the coercions (for the humans) and once without (for the simplifier).
end
</pre></div>

#### [ Mario Carneiro (Aug 06 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949286):
<p>I've seen this issue before. Unfortunately <code>simp</code> does not rewrite inside coercions because they are apparently dependent functions (the nondependency is only visible after you unfold the definition)</p>

#### [ Scott Morrison (Aug 06 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949293):
<p>Exactly!</p>

#### [ Scott Morrison (Aug 06 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949304):
<p>This is related to why I was writing a <code>mk_congr_arg_using_dsimp</code> tactic <a href="#narrow/stream/113488-general/subject/congr_arg.20and.20superficially.20dependent.20functions/near/130827909" title="#narrow/stream/113488-general/subject/congr_arg.20and.20superficially.20dependent.20functions/near/130827909">above</a>. (The idea being that if you <code>dsimp</code> the function first, sometimes you see that it's not actually a dependent function.)</p>

#### [ Mario Carneiro (Aug 06 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949367):
<p>I would look into fixing the congr lemma generation to use this</p>

#### [ Scott Morrison (Aug 06 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949411):
<p>Is that something which is fixable? Or is it frozen waiting for Lean 4?</p>

#### [ Mario Carneiro (Aug 06 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949414):
<p>there is always the option of making <code>simp'</code></p>

#### [ Scott Morrison (Aug 06 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949419):
<p>I see. But isn't much of <code>simp</code> written in C++?</p>

#### [ Scott Morrison (Aug 06 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949428):
<p>Could we make a patched <code>simp'</code> that had similar performance?</p>

#### [ Mario Carneiro (Aug 06 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949435):
<p>probably not, but if you use it only when necessary it should be palatable</p>

#### [ Mario Carneiro (Aug 06 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949483):
<p>I think you can use <code>ext_simplify_core</code> to hook into the traversal part without messing with the core of <code>simp</code></p>

#### [ Scott Morrison (Aug 06 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949485):
<p>eek... but my automation really relies on <code>simp</code> just doing its thing. As things are, I don't think there's any way to distinguish between the situations "simp failed to do anything" and "simp would have worked, but broke trying to construct a <code>congr_arg</code>"</p>

#### [ Scott Morrison (Aug 06 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949493):
<p>So it's not like I could just write a tactic that says "do <code>simp</code>, unless that breaks, in which case retry with <code>simp'</code>".</p>

#### [ Scott Morrison (Aug 06 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949495):
<p>Okay, I will investigate <code>ext_simplify_core</code> again. I once knew how that worked, but have forgotten.</p>

#### [ Mario Carneiro (Aug 06 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949551):
<p>By the way, <code>dsimp</code> works under dependent functions</p>

#### [ Mario Carneiro (Aug 06 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949557):
<p>so in particular it works in <code>test</code></p>

#### [ Sebastian Ullrich (Aug 06 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949606):
<p>Without having thought about it too hard, could a custom congr lemma for non-dependent coercions work?</p>

#### [ Mario Carneiro (Aug 06 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949607):
<p>Does <code>simp</code> use <code>@[congr]</code> lemmas?</p>

#### [ Scott Morrison (Aug 06 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949628):
<p>While I've got your attention on this, would you mind having a look at my <a href="#narrow/stream/113488-general/subject/congr_arg.20and.20superficially.20dependent.20functions/near/130827909" title="#narrow/stream/113488-general/subject/congr_arg.20and.20superficially.20dependent.20functions/near/130827909"><code>mk_congr_arg_using_dsimp</code></a> and see if there is a way to avoid polluting the goal with extra hypotheses as a side effect? I'm pretty unhappy about that hack.</p>

#### [ Scott Morrison (Aug 06 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949672):
<p>Yes; I know <code>dsimp</code> works fine, and indeed in my automation I always attempt <code>dsimp</code> before <code>simp</code>; sorry if this minimised example is too minimised, but I certainly have cases where <code>simp</code> is failing because of this effect.</p>

#### [ Scott Morrison (Aug 06 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949675):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>, sorry, I don't know what you mean by "Does <code>simp</code> use <code>@[congr]</code> lemmas?".</p>

#### [ Mario Carneiro (Aug 06 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949740):
<p>Simp works by using congruence lemmas generated by <code>mk_congr_lemma</code> for traversal. If it also accepts user lemmas marked <code>@{congr]</code>, then this would solve all our problems, because we could craft congr lemmas for looking through apparently dependent functions</p>

#### [ Scott Morrison (Aug 06 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949748):
<p>Ah, I see!</p>

#### [ Mario Carneiro (Aug 06 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949806):
<p>Also, looking at the coercion in your example, it is in fact a dependent function:</p>
<div class="codehilite"><pre><span></span>instance {F G : C ↝ D} : has_coe_to_fun (F ⟹ G) :=
{ F   := λ α, Π X : C, (F +&gt; X) ⟶ (G +&gt; X),
  coe := λ α, α.components }
</pre></div>


<p>so why is this legitimate in this case?</p>

#### [ Sebastian Ullrich (Aug 06 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949818):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I think so? <a href="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/library/tactic/simplify.cpp#L739-L740" target="_blank" title="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/library/tactic/simplify.cpp#L739-L740">https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/library/tactic/simplify.cpp#L739-L740</a> <code>simp</code> is the reason <code>[congr]</code> was introduced, afaik</p>

#### [ Scott Morrison (Aug 06 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949820):
<p>The problem is that for particular values of <code>α</code>, that dependent function might <code>dsimp</code> to a non-dependent function.</p>

#### [ Mario Carneiro (Aug 06 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130949862):
<p>I thought <code>[congr]</code> was used for <code>calc</code></p>

#### [ Sebastian Ullrich (Aug 06 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130950017):
<p>I'm not aware of <code>calc</code> using anything other than <code>[trans]</code></p>

#### [ Scott Morrison (Aug 06 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130950538):
<p>Are there any places I can look to find <code>@[congr]</code> used in conjunction with <code>simp</code>? I'm finding the C++ code pretty hard going.</p>

#### [ Scott Morrison (Aug 06 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130950675):
<p>I guess I just found <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span>'s example at <a href="https://github.com/leanprover/lean/commit/6bd3fe24493c1748c8cfd778f63a3b832c6e6ba7#diff-db6c06d0649a66f8bbfc76e59b15cef2" target="_blank" title="https://github.com/leanprover/lean/commit/6bd3fe24493c1748c8cfd778f63a3b832c6e6ba7#diff-db6c06d0649a66f8bbfc76e59b15cef2">https://github.com/leanprover/lean/commit/6bd3fe24493c1748c8cfd778f63a3b832c6e6ba7#diff-db6c06d0649a66f8bbfc76e59b15cef2</a>, but I'm still not sure what's going on. :-)</p>

#### [ Scott Morrison (Aug 06 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130951668):
<p>Okay, I am for now failing to work out how to use @[congr] to help <code>simp</code> work better, or to write my own <code>simp'</code> that uses <code>ext_simplify_core</code>. I'm happy to continue investigating both options, and very happy if someone else does this. :-)</p>

#### [ Scott Morrison (Aug 06 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130951718):
<p>In the meantime, could I propose, <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> and <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>, that in my category theory PR we defer the issue of adding coercions for functors acting on objects, and not consider that an obstacle for merging this PR?</p>
<p>If we can solve the issue here, of course I would love to add these coercions. In the meantime, it is not very expensive to write out the coercions, or have notations for them. I would really like to get this PR done, without breaking the possibility of good automation.</p>

#### [ Mario Carneiro (Aug 06 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130951764):
<p>Damn! I figured out what congr lemma to use, but lean doesn't accept it :/</p>
<div class="codehilite"><pre><span></span>@[congr] theorem NaturalTransformation.components_congr
  {F G : C ↝ D} {α β : F ⟹ G} (h : α = β) (X) : α.components X = β.components X :=
congr_fun (congr_arg coe_fn h) _
-- ok, generated automatically

@[congr] theorem NaturalTransformation.coe_congr
  {F G : C ↝ D} {α β : F ⟹ G} (h : α = β) (X) : α X = β X :=
congr_fun (congr_arg coe_fn h) _
-- invalid congruence lemma, &#39;NaturalTransformation.coe_congr&#39; the left-hand-side of the congruence
-- resulting type must be of the form (coe_fn x_1 ... x_n), where each x_i is a distinct variable or a sort
</pre></div>

#### [ Mario Carneiro (Aug 06 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130951827):
<p>even worse, the error is garbage because it didn't parse the statement correctly</p>

#### [ Mario Carneiro (Aug 06 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130951879):
<p>notice that <code>congr</code> fails on this proof for completely the wrong reason:</p>
<div class="codehilite"><pre><span></span>theorem NaturalTransformation.coe_congr
  {F G : C ↝ D} {α β : F ⟹ G} (h : α = β) (X) : α X = β X :=
by do {
  tgt ← target,
  (lhs, rhs) ← match_eq tgt,
  guard lhs.is_app,
  clemma ← mk_specialized_congr_lemma lhs,
  trace clemma.type,
  apply_eq_congr_core tgt }
-- invalid apply tactic, failed to unify
--   ⇑α X = ⇑β X
-- with
--   ⇑?m_2 = ⇑?m_2
</pre></div>

#### [ Mario Carneiro (Aug 06 2018 at 03:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130952264):
<p>For the purpose of this PR, how about adding the coercions, but add a simp lemma that unfolds the coercions and make simp lemmas that don't use the coercions. That way users can use the coercions but they won't interfere with <code>simp</code></p>

#### [ Mario Carneiro (Aug 06 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130952475):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> I think the coe_fn typeclass needs to be fixed so that lean knows it's a pi type:</p>
<div class="codehilite"><pre><span></span>class has_coe_to_fun (a : Sort u) : Sort (max u (v+1) (w+1)) :=
(dom : a → Sort v) (F : ∀ a, dom a → Sort w) (coe : Π x y, F x y)
</pre></div>


<p>I tried this modification in my local copy and it seems to work fine, but of course this requires a modification to core. Also related is an issue brought up by Floris a long time ago - <code>has_coe_to_sort</code> doesn't actually require that the target type is a sort. It should read:</p>
<div class="codehilite"><pre><span></span>class has_coe_to_sort (a : Sort u) : Type (max u v) :=
(coe : a → Sort v)
</pre></div>


<p>Any chance of at least getting these into lean 4?</p>

#### [ Scott Morrison (Aug 06 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130952782):
<p>Okay, I will try out that approach. You're right that it will probably work. The only downside is that <code>simp</code> will produce 'ugly' output that looks different from what the humans are used to.</p>

#### [ Mario Carneiro (Aug 06 2018 at 04:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130952921):
<p>of course it already does this enough that we have techniques like "use <code>simp</code> terminally" and "use <code>simpa</code>" to mitigate this problem</p>

#### [ Scott Morrison (Aug 06 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130953261):
<p>Okay. So now I'm left with the question of how much _I_ should use the coercion in the library development.</p>

#### [ Scott Morrison (Aug 06 2018 at 04:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130953269):
<p>I'm inclined to barely use it! That is, provide the coercion, and a simp lemma that unfolds it, but otherwise ignore it.</p>

#### [ Scott Morrison (Aug 06 2018 at 04:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130953275):
<p>Is that okay? Or is that making life unpleasant for a user?</p>

#### [ Scott Morrison (Aug 06 2018 at 04:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130953318):
<p>The alternative is to carefully go through, introducing use of the coercion everywhere except in simp lemmas, I guess.</p>

#### [ Mario Carneiro (Aug 06 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130953809):
<p>I think you should handle it like <code>sub</code>. Write lemmas using it, but also add simp lemma versions of the theorems when applicable</p>

#### [ Mario Carneiro (Aug 06 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130953855):
<p>these should be one liners or restatements</p>

#### [ Mario Carneiro (Aug 06 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130953858):
<p>the user will want to use coercions whenever possible, so there should be lemmas supporting this</p>

#### [ Mario Carneiro (Aug 06 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20inside%20expressions%20with%20coe_to_fun%20sometimes%20fails/near/130953864):
<p>besides, I haven't lost hope of an automation solution to this, we're talking about a workaround here</p>


{% endraw %}
