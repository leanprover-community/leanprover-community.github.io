---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/24026Categorytheory.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Category theory](https://leanprover-community.github.io/archive/116395maths/24026Categorytheory.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Apr 01 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124502143):
<p><a href="https://github.com/kckennylau/category-theory/blob/master/src/adjunction_examples.lean" target="_blank" title="https://github.com/kckennylau/category-theory/blob/master/src/adjunction_examples.lean">https://github.com/kckennylau/category-theory/blob/master/src/adjunction_examples.lean</a></p>

#### [ Kenny Lau (Apr 02 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124520998):
<div class="codehilite"><pre><span></span>@[reducible] def Set.Prod_Hom (B : Type u) : adjunction examples.Set examples.Set :=
adjunction.make _ _
  (examples.Set.product_functor B)
  (examples.Set.Hom_functor_right B)
  (λ A C f x, f x.1 x.2)
  (λ A C f x y, f (x, y))
  (λ A₁ A₂ C₁ C₂ f g t, rfl)
  (λ A₁ A₂ C₁ C₂ f g t, rfl)
  (λ A C f, funext $ λ ⟨t₁, t₂⟩, rfl)
  (λ A C f, rfl)
</pre></div>

#### [ Kenny Lau (Apr 02 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124520999):
<p>so natural</p>

#### [ Kenny Lau (Apr 02 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124521485):
<div class="codehilite"><pre><span></span>@[reducible] def Top_Set : adjunction examples.Top examples.Set :=
adjunction.free_forgetful _
  examples.Top.discrete
  examples.Top.forgetful
  (λ S T f, ⟨f, continuous_top⟩)
  (λ S T f, f.1)
  (λ T₁ T₂ S₁ S₂ f g t z, rfl)
  (λ T₁ T₂ S₁ S₂ f g t, subtype.eq rfl)
  (λ S T f, subtype.eq rfl)
  (λ S T f, rfl)

@[reducible] def Set_Top : adjunction examples.Set examples.Top :=
adjunction.make _ _
  examples.Top.forgetful
  examples.Top.indiscrete
  (λ S T f, f.1)
  (λ S T f, ⟨f, continuous_bot⟩)
  (λ T₁ T₂ S₁ S₂ f g t, subtype.eq rfl)
  (λ T₁ T₂ S₁ S₂ f g t, rfl)
  (λ S T f, rfl)
  (λ S T f, subtype.eq rfl)
</pre></div>

#### [ Kenny Lau (Apr 02 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124521487):
<p>that moment when they're adjoint to each other</p>

#### [ Kenny Lau (Apr 07 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124769998):
<p>for a set S, denoting by L(S) the transitive closure of S, we see that for any transitive set T with S ⊆ T, then L(S) ⊆ T</p>

#### [ Kenny Lau (Apr 07 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124769999):
<p>I wonder if this is the left adjoint of some forgetful functor</p>

#### [ Kenny Lau (Apr 07 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124770041):
<p>well, working in the category of sets with inclusion as morphism, we see that Hom_Trans(L(S),T) = Hom_Set(S,R(T)), where Trans is the category of transitive sets</p>

#### [ Kevin Buzzard (Apr 07 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124771927):
<p>What does this even mean? What is a transitive set?</p>

#### [ Kenny Lau (Apr 07 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124771967):
<p>A set X is transitive if for every x and y such that x∈y∈X, we have x∈X</p>

#### [ Kenny Lau (Apr 07 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124771978):
<p>if the transitive closure is indeed a left adjoint, then we get right-exactness for free</p>

#### [ Kevin Buzzard (Apr 07 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772086):
<p>Eew. I think I saw that notion in undergraduate set theory nearly 30 years ago, and I'm not sure I've seen it since. Maybe I saw it in the context of ordinals, which is something else I've not seen since.</p>

#### [ Kevin Buzzard (Apr 07 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772191):
<p>Are you making an assertion here? What is R(T)?</p>

#### [ Kenny Lau (Apr 07 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772193):
<p>the forgetful functor that forgets the fact that T is transitive</p>

#### [ Kevin Buzzard (Apr 07 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772194):
<p>Is what you write true?</p>

#### [ Kenny Lau (Apr 07 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772195):
<p>I believe so</p>

#### [ Kevin Buzzard (Apr 07 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772234):
<p>If S and T are both transitive, then you're asserting that the transitive maps from S to T are the same as the maps from S to T then?</p>

#### [ Kenny Lau (Apr 07 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772235):
<p>yes, since here the morphisms are just inclusions, so there is only one morphism per pair of sets</p>

#### [ Kevin Buzzard (Apr 07 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772241):
<p>What does Hom_Set mean then?</p>

#### [ Kenny Lau (Apr 07 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772243):
<p>oh, inclusion</p>

#### [ Kevin Buzzard (Apr 07 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772287):
<p>Do you have a question?</p>

#### [ Kenny Lau (Apr 07 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772288):
<p>is my belief right</p>

#### [ Kevin Buzzard (Apr 07 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772327):
<p>What does Hom_Trans mean?</p>

#### [ Kenny Lau (Apr 07 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772328):
<p>subcategory</p>

#### [ Kevin Buzzard (Apr 07 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772329):
<p>I don't know what anything means. It feels like you have made these categories up.</p>

#### [ Kevin Buzzard (Apr 07 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772331):
<p>It also seems that you are just as capable of writing down a proof of your assertion as I am. Why not check it in Lean? ;-)</p>

#### [ Kenny Lau (Apr 07 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772336):
<p>because to hell with the category of sets in Lean</p>

#### [ Kevin Buzzard (Apr 07 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772338):
<p>What does Hom_Trans mean?</p>

#### [ Kenny Lau (Apr 07 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772339):
<p>the inclusion in the category of transitive sets</p>

#### [ Kevin Buzzard (Apr 07 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772340):
<p>So at most one map between two sets?</p>

#### [ Kenny Lau (Apr 07 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772378):
<p>yes</p>

#### [ Kevin Buzzard (Apr 07 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772387):
<p>" we see that for any transitive set T with S ⊆ T, then L(S) ⊆ T ". Is that your question?</p>

#### [ Kenny Lau (Apr 07 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772388):
<p>well that's the UMP of transitive closure</p>

#### [ Kenny Lau (Apr 07 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772389):
<p>which should be right</p>

#### [ Kevin Buzzard (Apr 07 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772398):
<p>But what is your question if it is not precisely that statement?</p>

#### [ Kenny Lau (Apr 07 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772399):
<p>no idea</p>

#### [ Kevin Buzzard (Apr 07 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772400):
<p>We might be done then :-)</p>

#### [ Kenny Lau (Apr 07 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772437):
<p>interesting</p>

#### [ Reid Barton (Sep 01 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/133190899):
<p>Scott I guess I'll keep you updated on what I'm doing by sending pastebin links for now.</p>

#### [ Reid Barton (Sep 01 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/133190905):
<p><a href="https://pastebin.com/WmdNgPdx" target="_blank" title="https://pastebin.com/WmdNgPdx">https://pastebin.com/WmdNgPdx</a> is limits and colimits in types (nice and easy) and small and filtered categories (also easy).</p>

#### [ Reid Barton (Sep 01 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/133190955):
<p>Next I plan to try to show that small limits commute with filtered colimits</p>

#### [ Reid Barton (Sep 01 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/133190963):
<p>Probably I won't finish that in the next few days.</p>

#### [ Scott Morrison (Sep 02 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/133193621):
<p>Thanks, Reid, that patch has been applied!</p>

#### [ Reid Barton (Sep 02 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/133219652):
<p>I defined the limit functor but the proofs aren't as concise as they should be, especially map_id'.<br>
<a href="https://pastebin.com/QDM9H7TX" target="_blank" title="https://pastebin.com/QDM9H7TX">https://pastebin.com/QDM9H7TX</a></p>

#### [ Reid Barton (Sep 02 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/133219672):
<p>Scott -- maybe the simp lemmas could be set up so that map_id' can be proved by obviously?<br>
map_comp' is more complicated, since you have to use associativity (backwards)</p>

#### [ Scott Morrison (Sep 03 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/133230162):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>, in fact I already had this, obscurely hidden in <code>universal/complete/default.lean</code>, with slightly different proofs. I've incorporated some changes from yours, but left my proofs for now. Curiously, <code>obviously</code> does just fine for <code>map_comp'</code>, but fails on <code>map_id'</code> because for some reason <code>simp</code> won't apply <code>limit.lift_π</code>.</p>

#### [ Scott Morrison (Sep 03 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/133230214):
<p>I guess it was hiding in that directory because I wrote it for the sake of <a href="https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/universal/complete/functor_category.lean" target="_blank" title="https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/universal/complete/functor_category.lean">https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/universal/complete/functor_category.lean</a>, a still incomplete proof that C \lea D has limits if D does.</p>

#### [ Kenny Lau (Oct 20 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136174097):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Will you change some of the mathlib files to use category theory?</p>

#### [ Kenny Lau (Oct 20 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136174143):
<p>what's the plan for category theory?</p>

#### [ Scott Morrison (Oct 20 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136174176):
<p>I think at first, not much. Things like <code>has_products CommRing</code> can first live under <code>category_theory/</code>, as we get used to them.</p>

#### [ Kenny Lau (Oct 20 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136174189):
<p>will they gradually assimilate into the main mathlib library?</p>

#### [ Scott Morrison (Oct 20 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136174190):
<p>Eventually such facts should move out to their natural homes, immediately following where the underlying lemmas are actually proved.</p>

#### [ Kenny Lau (Oct 20 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136174193):
<p>nice</p>

#### [ Scott Morrison (Oct 20 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136174205):
<p>I suspect in the long run a lot of files will want to import <code>category_theory.isomorphism</code>, to avoid having to define their own custom version of <code>equiv</code> for the structure at hand.</p>

#### [ Kenny Lau (Nov 02 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136987135):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> The new module will be:</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">module</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">out_param</span> <span class="err">$</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">[</span><span class="n">out_param</span> <span class="err">$</span> <span class="n">ring</span> <span class="n">α</span><span class="o">]</span>
  <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">β</span><span class="o">]</span> <span class="kn">extends</span> <span class="n">semimodule</span> <span class="n">α</span> <span class="n">β</span>
</pre></div>


<p>How will your category theory library deal with this?</p>

#### [ Scott Morrison (Nov 02 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136992913):
<p>Mostly users will just want the category of R-modules for some fixed R. After you've fixed the ring this is no more or less scary than bundling any other algebraic typeclass, I think.</p>

#### [ Kenny Lau (Nov 02 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136994837):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I don't see how <code>bundle</code> can solve this</p>

#### [ Scott Morrison (Nov 02 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136994962):
<p>Oh, I didn't imply that we should use <code>bundled</code>. It's only intended for the simplest cases.</p>

#### [ Scott Morrison (Nov 02 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136995172):
<p>But <code>structure Module (a : Type) [ring a] := (b : Type) (m : module a b)</code>, is presumably fine.</p>

#### [ Scott Morrison (Nov 02 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136995228):
<p>Maybe you haven't actually said what you're concerned about?</p>

#### [ Kenny Lau (Nov 02 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136995271):
<p>well you forgot the add_comm_group</p>

#### [ Kenny Lau (Nov 02 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136995293):
<p>and actually that's all I'm concerned about</p>

#### [ Scott Morrison (Nov 02 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136995418):
<p>So <code>structure Module (a : Type) [ring a] := (b : Type) (g : add_comm_group b) (m : module a b)</code>...?</p>

#### [ Kenny Lau (Nov 02 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136995910):
<p>I'm not really sure how all of this works, because last time in my own category repo, I was wrestling with sigma</p>

#### [ Scott Morrison (Nov 02 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136996578):
<p>Yeah, I think just building custom structures, and then a few lemmas that peel back out the typeclasses as needed, is easiest.</p>

#### [ Scott Morrison (Nov 02 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136996598):
<p>I'll make a few more examples.</p>

#### [ Kenny Lau (Nov 02 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137000581):
<p>thanks</p>

#### [ Kenny Lau (Nov 02 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137066926):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> is <code>bundled category</code> a category? If not, what's the proper name?</p>

#### [ Johan Commelin (Nov 02 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137078410):
<p>I have a natural transformation <code>a</code> from <code>F</code> to <code>G</code>, and Lean is looking for a natural transformation from <code>G.op</code> to <code>F.op</code>. So I would like to provide <code>a.op</code> but this is not defined yet. What is the natural place to add this definition? In <code>opposites.lean</code> or in <code>natural_transformation.lean</code>?</p>

#### [ Reid Barton (Nov 02 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137078733):
<p>I think it makes sense to keep <code>category</code>/<code>functor</code>/<code>natural_transformation</code> "at the bottom" and so put <code>a.op</code> in <code>opposites</code> like <code>F.op</code></p>

#### [ Johan Commelin (Nov 02 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137079047):
<p>Ok... fine with me. I could also imagine <code>opposites</code> being pretty "fundamental".</p>

#### [ Kenny Lau (Nov 02 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137079230):
<p>It would be quite interesting if we know that functors form a category but not that categories form a category...</p>

#### [ Kenny Lau (Nov 02 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137079231):
<p>I've searched all the files</p>

#### [ Mario Carneiro (Nov 02 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137079297):
<p>the problem is that categories form a 2-category</p>

#### [ Mario Carneiro (Nov 02 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137079305):
<p>so "categories form a category" is true but mostly useless</p>

#### [ Reid Barton (Nov 02 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137079310):
<p>Categories also form a perfectly good category, we just don't have it yet</p>

#### [ Johan Commelin (Nov 02 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137079773):
<p>Ok, I'm testing out a heresy:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">cocone</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">J</span> <span class="err">⥤</span> <span class="n">C</span><span class="o">)</span> <span class="o">:=</span> <span class="n">cone</span> <span class="n">F</span><span class="bp">.</span><span class="n">op</span>
</pre></div>


<p>The first problem I hit is that for <code>c : cocone F</code> the tip of the cocone <code>c.X</code> is now an object of <code>C\op</code> instead of <code>C</code>. Can this somehow be fixed? I would rather just write <code>f : c.X \hom X</code> instead of</p>
<div class="codehilite"><pre><span></span><span class="n">f</span> <span class="o">:</span> <span class="bp">@</span><span class="n">category</span><span class="bp">.</span><span class="n">hom</span> <span class="n">C</span> <span class="bp">_</span> <span class="n">c</span><span class="bp">.</span><span class="n">X</span> <span class="n">X</span>
</pre></div>

#### [ Reid Barton (Nov 02 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137080246):
<p>I actually have this problem in ordinary informal math as well: it's hard to talk about both C and C^op at the same time.<br>
Sometimes I write things like <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mover accent="true"><mrow><mi>A</mi></mrow><mo stretchy="true">‾</mo></mover></mrow><annotation encoding="application/x-tex">\overline{A}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8833300000000001em;"></span><span class="strut bottom" style="height:0.8833300000000001em;vertical-align:0em;"></span><span class="base"><span class="mord overline"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8833300000000001em;"><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathit">A</span></span></span><span style="top:-3.80333em;"><span class="pstrut" style="height:3em;"></span><span class="overline-line" style="border-bottom-width:0.04em;"></span></span></span></span></span></span></span></span></span> for the object of C^op corresponding to the object <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">A</span></span></span></span> of C, but I'm not really fond of it.</p>

#### [ Kenny Lau (Nov 02 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137080336):
<p>"ordinary informal math" = category</p>

#### [ Johan Commelin (Nov 02 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137080436):
<p>Sure, so we could write <code>X.op</code> for such objects. But this problem is different. With my definition <code>c.X</code> lives in <code>C^op</code> by definition. But I'dd rather have it live in <code>C</code>... And somehow just writing <code>f : (c.X : C) \hom X</code> doesn't cut it....</p>

#### [ Johan Commelin (Nov 02 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137080457):
<p>Hmmm... I have to run. See y'all later.</p>

#### [ Reid Barton (Nov 02 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137081858):
<p>Perhaps we could have <code>unop : C\op \to C</code>?</p>

#### [ Kenny Lau (Nov 02 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137082098):
<p>or maybe an equivalence of categories <code>C\op\op \cong C</code>?</p>

#### [ Kenny Lau (Nov 02 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137083573):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">module</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">examples</span><span class="bp">.</span><span class="n">rings</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">opposites</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span> <span class="n">w</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span>

<span class="n">class</span> <span class="n">Module</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">add_comm_group</span> <span class="n">M</span><span class="o">,</span> <span class="n">module</span> <span class="n">R</span> <span class="n">M</span>

<span class="n">def</span> <span class="n">Module</span><span class="bp">.</span><span class="n">is_linear_map</span> <span class="o">{</span><span class="n">M</span> <span class="n">N</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">Module</span> <span class="n">R</span> <span class="n">M</span><span class="o">]</span> <span class="o">[</span><span class="n">Module</span> <span class="n">R</span> <span class="n">N</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">M</span> <span class="bp">→</span> <span class="n">N</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="n">is_linear_map</span> <span class="n">f</span>

<span class="kn">open</span> <span class="n">category_theory</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">examples</span>

<span class="kn">instance</span> <span class="n">Module</span><span class="bp">.</span><span class="n">concrete_category</span> <span class="o">:</span> <span class="n">concrete_category</span> <span class="o">(</span><span class="bp">@</span><span class="n">Module</span><span class="bp">.</span><span class="n">is_linear_map</span> <span class="n">R</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="k">by</span> <span class="n">constructor</span><span class="bp">;</span> <span class="n">intros</span><span class="bp">;</span> <span class="n">refl</span><span class="o">,</span>
<span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">hf</span> <span class="n">hg</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">hf</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">hg</span><span class="bp">;</span> <span class="n">constructor</span><span class="bp">;</span> <span class="n">intros</span><span class="bp">;</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[(</span><span class="err">∘</span><span class="o">),</span> <span class="bp">*</span><span class="o">]</span><span class="bp">⟩</span>

<span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="n">def</span> <span class="n">Mod</span> <span class="o">:=</span> <span class="n">bundled</span> <span class="o">(</span><span class="n">Module</span> <span class="n">R</span><span class="o">)</span>

<span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="n">def</span> <span class="n">Cat</span> <span class="o">:=</span> <span class="n">bundled</span> <span class="n">category</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">category</span> <span class="n">Cat</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">hom</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">C</span> <span class="n">D</span><span class="o">,</span> <span class="bp">@</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">functor</span> <span class="n">C</span><span class="bp">.</span><span class="mi">1</span> <span class="n">C</span><span class="bp">.</span><span class="mi">2</span> <span class="n">D</span><span class="bp">.</span><span class="mi">1</span> <span class="n">D</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
  <span class="n">id</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">C</span><span class="o">,</span> <span class="bp">@</span><span class="n">functor</span><span class="bp">.</span><span class="n">id</span> <span class="n">C</span><span class="bp">.</span><span class="mi">1</span> <span class="n">C</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
  <span class="n">comp</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">C</span> <span class="n">D</span> <span class="n">E</span><span class="o">,</span> <span class="bp">@</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">functor</span><span class="bp">.</span><span class="n">comp</span> <span class="n">C</span><span class="bp">.</span><span class="mi">1</span> <span class="n">C</span><span class="bp">.</span><span class="mi">2</span> <span class="n">D</span><span class="bp">.</span><span class="mi">1</span> <span class="n">D</span><span class="bp">.</span><span class="mi">2</span> <span class="n">E</span><span class="bp">.</span><span class="mi">1</span> <span class="n">E</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
  <span class="n">id_comp&#39;</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">C</span> <span class="n">D</span> <span class="n">f</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">f</span><span class="bp">;</span> <span class="n">refl</span><span class="o">,</span>
  <span class="n">comp_id&#39;</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">C</span> <span class="n">D</span> <span class="n">f</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">f</span><span class="bp">;</span> <span class="n">refl</span> <span class="o">}</span>

<span class="n">def</span> <span class="n">Mod</span> <span class="o">:</span> <span class="n">Ring</span><span class="err">ᵒᵖ</span> <span class="err">⥤</span> <span class="n">Cat</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">obj</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">R</span><span class="o">,</span> <span class="n">bundled</span><span class="bp">.</span><span class="n">mk</span> <span class="bp">_</span> <span class="o">(</span><span class="n">Mod</span> <span class="n">R</span><span class="bp">.</span><span class="mi">1</span><span class="o">),</span>
  <span class="n">map&#39;</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">R</span> <span class="n">S</span> <span class="n">φ</span><span class="o">,</span> <span class="n">concrete_functor</span> <span class="o">(</span><span class="k">begin</span> <span class="kn">end</span><span class="o">)</span> <span class="o">(</span><span class="k">begin</span> <span class="kn">end</span><span class="o">)</span> <span class="o">}</span>
</pre></div>

#### [ Reid Barton (Nov 02 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137084172):
<p>This looks good, but then the real test is whether it's convenient to use objects of <code>Mod R</code> as modules and vice versa, and the same for <code>Cat</code></p>

#### [ Reid Barton (Nov 02 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137084272):
<p>At a minimum you want the instance that gets you the <code>Module</code> back out from <code>x : Mod R</code></p>

#### [ Reid Barton (Nov 02 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137084280):
<p>analogous to <code>instance (x : Ring) : ring x := x.str</code></p>

#### [ Kenny Lau (Nov 02 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137084285):
<p>that's just interface</p>

#### [ Kenny Lau (Nov 02 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137084287):
<p>anyone can write an interface</p>

#### [ Reid Barton (Nov 02 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137084348):
<p>anyone can define <code>Cat</code>, too</p>

#### [ Reid Barton (Nov 02 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137084357):
<p>Finding a good interface is the important thing</p>

#### [ Chris Hughes (Nov 02 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137084372):
<p>Interfaces are hard.</p>

#### [ Kenny Lau (Nov 02 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137084448):
<p>I think <code>opposite</code> can have a better interface</p>

#### [ Kenny Lau (Nov 02 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087104):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> how should we define an additive category?</p>

#### [ Scott Morrison (Nov 02 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087138):
<p>ugh, yeah, defining enriched categories may take a lot of work to do in general. :-(</p>

#### [ Scott Morrison (Nov 02 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087180):
<p>If you _just_ want additive categories (which is very reasonable, later we can retrofit them as special cases of enriched categories)</p>

#### [ Scott Morrison (Nov 02 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087225):
<p>then I don't think it's too bad</p>

#### [ Kenny Lau (Nov 02 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087236):
<p>ok, then how?</p>

#### [ Scott Morrison (Nov 02 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087237):
<p>Just have a new typeclass <code>[additive_category C]</code>, with fields <code>hom_abelian : add_comm_group (X \hom Y)</code> and <code>comp_bilinear : ...</code></p>

#### [ Scott Morrison (Nov 02 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087239):
<p>and then some <code>defs</code> that create instances from these fields</p>

#### [ Kenny Lau (Nov 02 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087261):
<p>can we instead declare it as a functor from the Hom category to the Ab category</p>

#### [ Kenny Lau (Nov 02 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087302):
<p>such that some triangle commutes</p>

#### [ Kenny Lau (Nov 02 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087316):
<p>I guess Hom isn't a category</p>

#### [ Scott Morrison (Nov 02 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087321):
<p>yeah, I'm not sure what you mean</p>

#### [ Kenny Lau (Nov 02 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087339):
<p>there must be a way to do this category-theoretically...</p>

#### [ Scott Morrison (Nov 02 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087358):
<p>Well... I think often it's better to have the definitions "explicit" and then have lemmas saying "you can interpret this in categorical terms"</p>

#### [ Kenny Lau (Nov 02 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087367):
<p>sure</p>

#### [ Scott Morrison (Nov 02 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087368):
<p>In particular, for monoidal categories (or 2-categories), which I really want to get back to,</p>

#### [ Scott Morrison (Nov 02 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087421):
<p>it turns out to be a really bad idea to say that a monoidal category is a category equipped with a functor (C x C) \func C, such that ...</p>

#### [ Kenny Lau (Nov 02 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087436):
<p>why isn't Lean ready for a category theory library?</p>

#### [ Scott Morrison (Nov 02 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087445):
<p>and instead you should do everything grossly: a function <code>tensorObjects</code>, a function <code>tensorMorphisms</code>, and then have a lemma saying these form that functor</p>

#### [ Scott Morrison (Nov 02 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087481):
<p>This sounds like a really bad idea, but the way lean's notation system and elaborator work, you run into endless misery making the functor the "primary" description of the tensor product.</p>

#### [ Scott Morrison (Nov 02 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087484):
<p>It's very unfortunate. :-(</p>

#### [ Scott Morrison (Nov 02 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087555):
<blockquote>
<p>why isn't Lean ready for a category theory library?</p>
</blockquote>
<p>Speaking to mathematicians, Lean, like every other ITP system, is not ready to do mathematics in. :-)</p>
<p>Lean is terrible, just less terrible than all the others!</p>

#### [ Reid Barton (Nov 03 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137088959):
<p>I don't know whether this would be easier or harder, but you don't actually need monoidal categories to do enriched categories; you could enrich in a multicategory instead</p>

#### [ Kevin Buzzard (Nov 03 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137089207):
<p>I've found it quite good fun doing abstract maths in Lean. I've not used categories though. But stuff like commutative algebra seems to come out nicely.</p>

#### [ Kenny Lau (Nov 03 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137089255):
<p>right, until the module thing came along</p>

#### [ Chris Hughes (Nov 03 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137089369):
<p>Lean is often good at abstract stuff. I think maybe abstract usually means it has to be done on paper more formally, because there's less real world intuition.</p>

#### [ Scott Morrison (Nov 03 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137103458):
<blockquote>
<p>But stuff like commutative algebra seems to come out nicely.</p>
</blockquote>
<p>Stockholm syndrome. :-)</p>

#### [ Reid Barton (Nov 05 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137177771):
<p>Scott, are you attached to the name <code>category_theory.embedding</code>?<br>
How about <code>fully_faithful</code>?</p>

#### [ Reid Barton (Nov 05 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137177843):
<p><code>embedding</code> is ambiguous, I feel. Someone may think it implies "injective on objects" for example. The nlab gives a variety of definitions.</p>

#### [ Reid Barton (Nov 05 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137177890):
<p>(Also it collides with the top-level <code>embedding</code> of topological spaces, which is not <code>category_theory</code>'s fault but it did cause some extremely confusing behavior during one of my lean-homotopy-theory mathlib version bumps.)</p>

#### [ Scott Morrison (Nov 05 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137179986):
<p>Yes, we should definitely change this.</p>

#### [ Johan Commelin (Nov 05 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815330):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Do you have any idea why this would fail?</p>
<div class="codehilite"><pre><span></span><span class="n">failed</span> <span class="n">to</span> <span class="n">synthesize</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">for</span>
<span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">,</span>
<span class="err">𝒳</span> <span class="o">:</span> <span class="n">category</span> <span class="n">X</span><span class="o">,</span>
<span class="n">U</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span>
<span class="n">f</span> <span class="o">:</span> <span class="n">covering_family</span> <span class="n">U</span><span class="o">,</span>
<span class="n">p</span> <span class="o">:</span> <span class="n">f</span><span class="bp">.</span><span class="n">index</span> <span class="bp">×</span> <span class="n">f</span><span class="bp">.</span><span class="n">index</span>
<span class="err">⊢</span> <span class="n">category</span> <span class="o">(</span><span class="n">X</span><span class="err">ᵒᵖ</span> <span class="err">⥤</span> <span class="kt">Type</span> <span class="n">v₁</span><span class="o">)</span>
</pre></div>

#### [ Scott Morrison (Nov 05 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815457):
<p>either you're missing the import, or something is weird with universe levels?</p>

#### [ Johan Commelin (Nov 05 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815502):
<p>I have</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">presheaf</span> <span class="o">:=</span> <span class="n">X</span><span class="err">ᵒᵖ</span> <span class="err">⥤</span> <span class="n">C</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span><span class="o">}</span> <span class="o">{</span><span class="n">C</span><span class="o">}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">category</span> <span class="o">(</span><span class="n">presheaf</span> <span class="n">X</span> <span class="n">C</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">unfold</span> <span class="n">presheaf</span><span class="bp">;</span> <span class="n">apply_instance</span>
</pre></div>


<p>in the same file.</p>

#### [ Scott Morrison (Nov 05 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815626):
<p>Turn on pp.universes?</p>

#### [ Johan Commelin (Nov 05 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815660):
<p>I'll try that. I also see</p>
<div class="codehilite"><pre><span></span>[class_instances] (0) ?x_0 : category (Xᵒᵖ ⥤ Type v₁) := @functor.category ?x_40 ?x_41 ?x_42 ?x_43
failed is_def_eq
</pre></div>


<p>in the trace.</p>

#### [ Johan Commelin (Nov 05 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815837):
<p>Ok, that gave me</p>
<div class="codehilite"><pre><span></span><span class="n">failed</span> <span class="n">to</span> <span class="n">synthesize</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">for</span>
<span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">,</span>
<span class="err">𝒳</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">v₁</span><span class="o">}</span> <span class="n">X</span><span class="o">,</span>
<span class="n">U</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span>
<span class="n">f</span> <span class="o">:</span> <span class="n">covering_family</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">v₁</span><span class="o">}</span> <span class="n">U</span><span class="o">,</span>
<span class="n">p</span> <span class="o">:</span> <span class="n">f</span><span class="bp">.</span><span class="n">index</span> <span class="bp">×</span> <span class="n">f</span><span class="bp">.</span><span class="n">index</span>
<span class="err">⊢</span> <span class="n">category</span><span class="bp">.</span><span class="o">{(</span><span class="n">max</span> <span class="n">u₁</span> <span class="o">(</span><span class="n">v₁</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">v₁</span><span class="o">}</span> <span class="o">(</span><span class="n">X</span><span class="err">ᵒᵖ</span> <span class="err">⥤</span> <span class="kt">Type</span> <span class="n">v₁</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (Nov 05 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815842):
<p>Maybe I don't understand universes well enough...</p>

#### [ Johan Commelin (Nov 05 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815850):
<p>Should that last <code>v_1</code> be a <code>v_1 + 1</code>?</p>

#### [ Reid Barton (Nov 05 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815950):
<p>I think it should be <code>max u_1 v_1</code>, if I calculated right</p>

#### [ Reid Barton (Nov 05 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815980):
<p>Ah, Scott was kind enough to write out the universe parameters in <code>instance functor.category</code>.</p>

#### [ Reid Barton (Nov 05 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815996):
<p>My guess: perhaps you are doing something where you actually need <code>X</code> to be a small category?</p>

#### [ Reid Barton (Nov 05 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816055):
<p>it's hard to say what to do without knowing where that goal is coming from</p>

#### [ Johan Commelin (Nov 05 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816060):
<p>But in <code>yoneda</code> Scott is doing the same thing as I'm doing. Now I'm really confused.</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">)</span> <span class="o">[</span><span class="err">𝒞</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u₁</span> <span class="n">v₁</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span>
<span class="n">include</span> <span class="err">𝒞</span>

<span class="n">def</span> <span class="n">yoneda</span> <span class="o">:</span> <span class="n">C</span> <span class="err">⥤</span> <span class="o">((</span><span class="n">C</span><span class="err">ᵒᵖ</span><span class="o">)</span> <span class="err">⥤</span> <span class="o">(</span><span class="kt">Type</span> <span class="n">v₁</span><span class="o">))</span> <span class="o">:=</span>
</pre></div>

#### [ Reid Barton (Nov 05 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816089):
<p>Sure you can write down <code>X\op \func Type v_1</code>, but it might not have <code>v_1</code>-small hom sets.</p>

#### [ Reid Barton (Nov 05 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816155):
<p>Which is what your goal is asking for</p>

#### [ Mario Carneiro (Nov 05 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816217):
<p>how big are the homsets of the functor category?</p>

#### [ Scott Morrison (Nov 05 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816296):
<div class="codehilite"><pre><span></span>variables (C : Type u₁) [𝒞 : category.{u₁ v₁} C] (D : Type u₂) [𝒟 : category.{u₂ v₂} D]
include 𝒞 𝒟

instance functor.category :
  category.{(max u₁ v₁ u₂ v₂) (max u₁ v₂)} (C ⥤ D) :=
</pre></div>

#### [ Scott Morrison (Nov 05 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816308):
<p>I wrote the universe levels explicitly in the definition, as documentation for just these moments. :-)</p>

#### [ Johan Commelin (Nov 05 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816354):
<p>Thanks! I'm probably dense, but I'm still confused why Scott could write what he wrote for <code>yoneda</code>, and now I want to apply it and Lean complains...</p>

#### [ Scott Morrison (Nov 05 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816417):
<p>The danger is always the <code>u1</code> appearing the morphism universe level.</p>

#### [ Reid Barton (Nov 05 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816437):
<p>Apply what how? What is the actual math?</p>

#### [ Scott Morrison (Nov 05 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816449):
<p>So in Yoneda, we don't care about the universe level of the morphisms in the resulting category.</p>

#### [ Scott Morrison (Nov 05 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816456):
<p>But you _do_ care.</p>

#### [ Scott Morrison (Nov 05 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816472):
<p>You need a category  <code>category.{(max u₁ (v₁+1)) v₁} (Xᵒᵖ ⥤ Type v₁)</code></p>

#### [ Johan Commelin (Nov 05 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816490):
<p>Ooops... I crashed the machine I was logged into...</p>

#### [ Johan Commelin (Nov 05 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816497):
<p>I was working on the <code>sheaf</code> branch.</p>

#### [ Johan Commelin (Nov 05 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816561):
<p><a href="https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheaf.lean#L41" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheaf.lean#L41">https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheaf.lean#L41</a></p>

#### [ Scott Morrison (Nov 05 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816588):
<p>But with <code>category.{u1 v1} X</code>, you're going to find <code>Xop \func Type v1</code> only has a category structure with</p>

#### [ Scott Morrison (Nov 05 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816603):
<p>objects in universe <code>max u1 (v1+1)</code> (which is fine)</p>

#### [ Scott Morrison (Nov 05 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816619):
<p>and morphisms in universe <code>max u1 v1</code></p>

#### [ Scott Morrison (Nov 05 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816623):
<p>which breaks your constraint</p>

#### [ Johan Commelin (Nov 05 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816683):
<p>I see. So now I should convince Lean that it should be looking for a more relaxed constraint...</p>

#### [ Johan Commelin (Nov 05 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816844):
<p>First need to build mathlib on a new machine. (What is the emoji for compiling?)</p>

#### [ Johan Commelin (Nov 05 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817011):
<p>I propose <span class="emoji emoji-1f93a" title="fencing">:fencing:</span> for compiling because of <a href="https://www.xkcd.com/303/" target="_blank" title="https://www.xkcd.com/303/">https://www.xkcd.com/303/</a></p>

#### [ Reid Barton (Nov 05 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817352):
<p>I guess this is one of the points where one uses universes in a more serious way</p>

#### [ Mario Carneiro (Nov 05 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817488):
<p>is this what representable functors are for?</p>

#### [ Reid Barton (Nov 05 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817526):
<p>In math one could just pass to a universe in which X is a small category</p>

#### [ Kevin Buzzard (Nov 05 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817571):
<blockquote>
<p>is this what representable functors are for?</p>
</blockquote>
<p>They're used in the Fermat's Last Theorem proof to produce rings out of thin air.</p>

#### [ Reid Barton (Nov 05 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817863):
<p>I think your options are</p>
<ul>
<li>Assume <code>X</code> is a <code>small_category.{v_1}</code></li>
<li>Have <code>sieve</code> take values in presheaves valued in <code>Type (max u_1 v_1)</code></li>
<li>Redesign limits so that you can talk about the limit of a <code>w</code>-sized diagram in a <code>category.{u v}</code> (but I don't think this sounds like a good idea)</li>
</ul>

#### [ Reid Barton (Nov 05 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817945):
<p>The first two are both versions of the math "just pick a universe in which X looks small", and it's a matter of where you want to put that shift of universe</p>

#### [ Kevin Buzzard (Nov 05 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817951):
<p>The fpqc topology has some issues with large limits. <span class="user-mention" data-user-id="112680">@Johan Commelin</span> are you planning on writing something sufficently general to deal with the fpqc topology?</p>

#### [ Johan Commelin (Nov 05 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817961):
<p>Yes.</p>

#### [ Johan Commelin (Nov 05 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817974):
<p>I want to do sheaves in the biggest generality possible.</p>

#### [ Kevin Buzzard (Nov 05 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817983):
<p>Conrad would argue that the fpqc topology "does not exist"</p>

#### [ Johan Commelin (Nov 05 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817984):
<p>I think I'll go for option 2.</p>

#### [ Reid Barton (Nov 05 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817988):
<p>Are they actual issues or just issues for people who don't believe in universes?</p>

#### [ Kevin Buzzard (Nov 05 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818048):
<p>I don't fully understand the issues</p>

#### [ Johan Commelin (Nov 05 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818056):
<p>I think a little bit of both. You need to do resizing at some point. Like we were discussing <code>kappa</code>-small stuff a while ago.</p>

#### [ Reid Barton (Nov 05 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818087):
<p>I think if you express any topology other than the Zariski one naturally in Lean it will have the same issues as the fpqc topology--otherwise you will need to manually replace your category with an essentially equivalent small one</p>

#### [ Kevin Buzzard (Nov 05 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818088):
<p>I do understand that the issue with an fpqc cover is that you can't make a set of all fpqc covers</p>

#### [ Kevin Buzzard (Nov 05 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818107):
<p>I'm not sure this is accurate Reid</p>

#### [ Kevin Buzzard (Nov 05 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818172):
<p>With the etale topology there is in some formal sense not a set of etale covers</p>

#### [ Kevin Buzzard (Nov 05 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818174):
<p>but there is a set of etale covers such that every etale cover is isomorphic to a cover in your set</p>

#### [ Kevin Buzzard (Nov 05 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818187):
<p>with fpqc the problem is genuinely worse</p>

#### [ Kevin Buzzard (Nov 05 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818188):
<p>because an arbitrary morphism of fields is fpqc</p>

#### [ Kevin Buzzard (Nov 05 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818203):
<p>so there is not even a set of isomorphism classes of etale covers of spec(field)</p>

#### [ Kevin Buzzard (Nov 05 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818256):
<p>I don't know whether thinking about things in a more universey way makes these two problems become the same</p>

#### [ Kevin Buzzard (Nov 05 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818305):
<p>but in ZFC I've always had the impression that they were not the same</p>

#### [ Reid Barton (Nov 05 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818326):
<p>Right, that is what I mean--you would not be able to define etale covers as just "a scheme with an etale map to X", because that will live in a too large universe--you need to manually replace the category with an equivalent small one with some kind of cardinality argument</p>

#### [ Kevin Buzzard (Nov 05 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818343):
<p>right</p>

#### [ Kevin Buzzard (Nov 05 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818352):
<p>but you can't do that for fpqc</p>

#### [ Reid Barton (Nov 05 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818363):
<p>right</p>

#### [ Reid Barton (Nov 05 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818411):
<p>so there are two kinds of issues which could arise then</p>

#### [ Reid Barton (Nov 05 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818486):
<p>one is if you don't accept the universe axiom, then you can't talk about such large collections like the category of sheaves for the fpqc topology on X at all</p>

#### [ Kevin Buzzard (Nov 05 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818510):
<p>I believe Conrad is strictly ZFC so rejects the fpqc topology</p>

#### [ Reid Barton (Nov 05 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818514):
<p>but that's not an issue if you do accept universes</p>

#### [ Scott Morrison (Nov 05 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818575):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> I pushed my (inconclusive) changes to the sheaf branch. Now my dog insists on a walk (in the rain).</p>

#### [ Reid Barton (Nov 05 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818580):
<p>but then a second issue which might come up is: you need to take a limit of sets or something, but because the indexing diagram of the limit is large it could take you outside the category you called Set. And that is a real issue even if you believe in universes</p>

#### [ Johan Commelin (Nov 05 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146819009):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Thanks! I'll take a look!</p>

#### [ Kevin Buzzard (Nov 05 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146819201):
<p>Looking through old emails I've exchanged with Conrad on the fpqc matter, he basically says "fppf is enough for everything, and anyone who wants to work with fpqc -- well, that's their problem, and they can work out the details for themselves"</p>

#### [ Reid Barton (Nov 05 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146819571):
<p>Another possible approach is <a href="https://ncatlab.org/nlab/show/small+presheaf" target="_blank" title="https://ncatlab.org/nlab/show/small+presheaf">https://ncatlab.org/nlab/show/small+presheaf</a></p>

#### [ Reid Barton (Nov 05 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146819792):
<p>I think you can also think of this as like Ind, but with no restriction on the indexing diagrams you allow</p>

#### [ Reid Barton (Nov 05 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146819837):
<p>However I don't know whether this is useful for applications in algebraic geometry</p>

#### [ Reid Barton (Nov 05 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146819848):
<p><a href="https://ncatlab.org/nlab/show/large+site" target="_blank" title="https://ncatlab.org/nlab/show/large+site">https://ncatlab.org/nlab/show/large+site</a> is a not particularly encouraging page</p>

#### [ Johan Commelin (Nov 05 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146820504):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Hmmzz, I'm not really making any progress...</p>

#### [ Reid Barton (Nov 05 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146820515):
<p>I expect you will have other problems, too <span class="emoji emoji-1f642" title="slight smile">:slight_smile:</span></p>

#### [ Johan Commelin (Nov 05 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146820521):
<p>/me is not designed to think about universe issues...</p>

#### [ Johan Commelin (Nov 05 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146820597):
<p>What do you think is the best solution for now? Making <code>X</code> small?</p>

#### [ Reid Barton (Nov 05 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146820648):
<p>certainly easiest for the time being</p>

#### [ Reid Barton (Nov 05 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146820668):
<p>and you don't really lose any generality</p>

#### [ Johan Commelin (Nov 05 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146820672):
<p>Ok, then I'll leave the headaches for the sheaves refactor that Mario will work on next summer (-;</p>

#### [ Reid Barton (Nov 05 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146820747):
<p>I think your next problem was going to be: you have some coproducts indexed on a <code>Type v_1</code>, but now the morphism size is <code>max u_1 v_1</code></p>

#### [ Reid Barton (Nov 05 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146820750):
<p>so you would need to add some <code>ulift</code> to align them</p>

#### [ Johan Commelin (Nov 05 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146821056):
<p>You're completely right.</p>

#### [ Johan Commelin (Nov 05 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146821111):
<p>So I want my indexing type to be <em>small</em> small</p>

#### [ Johan Commelin (Nov 05 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146821132):
<p>In which universe should the indexing type of a covering family live?</p>

#### [ Johan Commelin (Nov 05 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146821143):
<p><code>max u_1 v_1</code>?</p>

#### [ Reid Barton (Nov 05 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146821152):
<p>I thought you were going to make X small instead</p>

#### [ Reid Barton (Nov 05 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146821157):
<p>so u_1 = v_1</p>

#### [ Reid Barton (Nov 05 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146821163):
<p>if not, then I'm not sure</p>

#### [ Johan Commelin (Nov 05 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146821344):
<p>Yes, I am going to do that. So then I should just take <code>u_1</code>, right?</p>

#### [ Reid Barton (Nov 05 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146821455):
<p>Whatever the universe level of X is. It seems we tend to call it <code>v</code> in <code>category_theory</code></p>

#### [ Reid Barton (Nov 05 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146821697):
<p>Well, or <code>u</code></p>

#### [ Johan Commelin (Nov 05 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146823630):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Wouldn't it be useful to have <code>has_pullbacks_of_has_limits</code> be an instance in general?</p>

#### [ Scott Morrison (Nov 05 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146823698):
<p>I'm afraid of doing that before we know that the pullbacks thus produced are "nice enough".</p>

#### [ Johan Commelin (Nov 05 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146823713):
<p>Ok, I see.</p>

#### [ Scott Morrison (Nov 05 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146823719):
<p>I suspect that you'll only want that instance "in desperation", when you don't have access to a construction of pullbacks that is defeq to something easier to work with than the general limit.</p>

#### [ Johan Commelin (Nov 05 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146823743):
<p>Hmmm, ok</p>

#### [ Johan Commelin (Nov 05 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146823759):
<p>So now I've made two small edits to <code>sheaf</code>.</p>

#### [ Johan Commelin (Nov 05 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146823819):
<p>Do you have a minute to look at the errors that remain? I'm very bad at fighting these universe issues.</p>

#### [ Scott Morrison (Nov 05 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824066):
<p>hah, we've been duplicating effort :-)</p>

#### [ Johan Commelin (Nov 05 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824201):
<p>Well, I didn't do much...</p>

#### [ Johan Commelin (Nov 05 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824312):
<p>Do you think the library is ready for this? Or am I making too big a jump?</p>

#### [ Scott Morrison (Nov 05 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824367):
<p>We're almost there. :-)</p>

#### [ Scott Morrison (Nov 05 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824419):
<p>And this is exactly the sort of stress testing of limits that we need.</p>

#### [ Scott Morrison (Nov 05 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824431):
<p>I committed a little, but it's still badly broken, and I have to get the kids to school/me to work.</p>

#### [ Johan Commelin (Nov 05 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824449):
<p>Sure, those are more important than silly sheaves (-;</p>

#### [ Johan Commelin (Nov 05 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824459):
<p>See you later</p>

#### [ Kevin Buzzard (Nov 05 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824782):
<p>I've just been reading SGA4 in the bath</p>

#### [ Kevin Buzzard (Nov 05 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824788):
<p>As you do</p>

#### [ Kevin Buzzard (Nov 05 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824860):
<p>And very early on when talking about limits and colimits</p>

#### [ Kevin Buzzard (Nov 05 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824888):
<p>They assume that the diagram is u-small</p>

#### [ Kevin Buzzard (Nov 05 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824928):
<p>ie isomorphic to an element of the universe u</p>

#### [ Kevin Buzzard (Nov 05 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824964):
<p>Their categories are u-categories</p>

#### [ Kevin Buzzard (Nov 05 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824981):
<p>Ie hom sets are all in u</p>

#### [ Kevin Buzzard (Nov 05 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146825039):
<p>But the limits are over u-small diagrams consistently</p>

#### [ Kevin Buzzard (Nov 05 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146825391):
<p>Example theorem : the category of u-abelian groups has u-limits. This <em>means</em> that you take the category  whose objects are abelian groups in some universe, and then take a limit but only over a category which is itself an <em>element</em> of u</p>

#### [ Reid Barton (Nov 05 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146825626):
<p>That's essentially our setup too, see <a href="https://github.com/leanprover-community/mathlib/blob/limits-others-new/category_theory/limits/limits.lean#L21-L22" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/limits-others-new/category_theory/limits/limits.lean#L21-L22">https://github.com/leanprover-community/mathlib/blob/limits-others-new/category_theory/limits/limits.lean#L21-L22</a></p>

#### [ Johan Commelin (Nov 05 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146826137):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> In things like <code>coequalizer.desc</code> should the argument <code>w</code> get an auto_param <code>obviously</code>?</p>

#### [ Scott Morrison (Nov 05 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146826530):
<p>Yes, that seems plausible.</p>

#### [ Johan Commelin (Nov 05 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146826939):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I just pushed some more silly stuff. Didn't make fundamental progress.</p>

#### [ Johan Commelin (Nov 06 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146850316):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I don't think <code>functor.const</code> should be in <code>cones</code>. It is more fundamental. Should this be moved to <code>functor</code> or something?</p>

#### [ Scott Morrison (Nov 06 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146851045):
<p>Sounds good.</p>

#### [ Reid Barton (Nov 10 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147440403):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> did you ever find a setup for typing the functor arrow in emacs?</p>

#### [ Johan Commelin (Nov 10 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147442348):
<p>Nah, haven't looked into it yet. Sorry. Maybe some other emacs user can tell us how to fix this. <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> ?</p>

#### [ Gabriel Ebner (Nov 10 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147442884):
<p>The input abbreviations for emacs are defined here: <a href="https://github.com/leanprover/lean-mode/blob/9d6b8471e2044310b4cd7cd3213b1fc8f78ec499/lean-input.el#L407" target="_blank" title="https://github.com/leanprover/lean-mode/blob/9d6b8471e2044310b4cd7cd3213b1fc8f78ec499/lean-input.el#L407">https://github.com/leanprover/lean-mode/blob/9d6b8471e2044310b4cd7cd3213b1fc8f78ec499/lean-input.el#L407</a>  It should be straightforward to submit a PR adding the new arrows (you might also want to add Scott's calligraphic symbols).</p>

#### [ Gabriel Ebner (Nov 10 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147443005):
<p>These are the relevant changes in the vscode extension:<br>
<code>\McB</code>, etc. <a href="https://github.com/leanprover/vscode-lean/commit/46ef6b277f4b90ef440730e3b2f73f9381aa08b0#diff-7c2385f0b8db521fe81e3d20489e5f12" target="_blank" title="https://github.com/leanprover/vscode-lean/commit/46ef6b277f4b90ef440730e3b2f73f9381aa08b0#diff-7c2385f0b8db521fe81e3d20489e5f12">https://github.com/leanprover/vscode-lean/commit/46ef6b277f4b90ef440730e3b2f73f9381aa08b0#diff-7c2385f0b8db521fe81e3d20489e5f12</a><br>
<code>\bbA</code>, etc. <a href="https://github.com/leanprover/vscode-lean/commit/0080ed0f7c80b199abf31212a7eb9356d3cbc896#diff-7c2385f0b8db521fe81e3d20489e5f12" target="_blank" title="https://github.com/leanprover/vscode-lean/commit/0080ed0f7c80b199abf31212a7eb9356d3cbc896#diff-7c2385f0b8db521fe81e3d20489e5f12">https://github.com/leanprover/vscode-lean/commit/0080ed0f7c80b199abf31212a7eb9356d3cbc896#diff-7c2385f0b8db521fe81e3d20489e5f12</a><br>
<code>\functor</code> <a href="https://github.com/leanprover/vscode-lean/commit/d3988d9fae1ab4a7e4785486a08c5eddcd33c575#diff-7c2385f0b8db521fe81e3d20489e5f12" target="_blank" title="https://github.com/leanprover/vscode-lean/commit/d3988d9fae1ab4a7e4785486a08c5eddcd33c575#diff-7c2385f0b8db521fe81e3d20489e5f12">https://github.com/leanprover/vscode-lean/commit/d3988d9fae1ab4a7e4785486a08c5eddcd33c575#diff-7c2385f0b8db521fe81e3d20489e5f12</a></p>

#### [ Gabriel Ebner (Nov 10 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147443017):
<p>In the long term, we might want to have a common source for these abbreviations that is shared by the editor extensions.</p>

#### [ Johan Commelin (Nov 10 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147443021):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> Thanks a lot for the links! Once I find some time, I hope to add a PR.</p>

#### [ Johan Commelin (Nov 15 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147739528):
<p>Do we know that composition of functors is associative? I can't find it...</p>

#### [ Reid Barton (Nov 15 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147739654):
<p>I don't think so, but it is true by defeq at least</p>

#### [ Johan Commelin (Nov 15 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147739865):
<p>I see. So I guess this should be added sooner rather than later.</p>

#### [ Scott Morrison (Nov 15 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147768822):
<p>It's in <code>lean-category-theory</code>, under <code>functor_categories/isomorphisms.lean</code>.</p>

#### [ Scott Morrison (Nov 15 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147768830):
<p>At least -- it constructs the equality as a natural isomorphism.</p>

#### [ Scott Morrison (Nov 15 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147768858):
<p>I thought it would be good to also prove the the unitors and associator for functors satisfy the triangles and pentagon equations, but didn't do that.</p>

#### [ Scott Morrison (Nov 15 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147772079):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>, it turned out this was easy to do, so there's a new PR adding unitors and associators for functors, as well as checking the pentagon and triangle. (These will be necessary one day when we want an example of a 2-category!)</p>

#### [ Johan Commelin (Nov 16 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147797409):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> <span class="user-mention" data-user-id="110032">@Reid Barton</span>  I have a question about yoneda. I find the <code>yoneda.lean</code> file a bit confusing. Is there an easy way to extract that <code>F.obj U</code> is canonically the same as <code>yoneda.obj  ⟹ F</code>, where <code>U : X</code> and <code>F : presheaf X</code>? Or is this something that we have to add to this file?</p>

#### [ Reid Barton (Nov 16 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147797624):
<p>In the adjunctions branch I just sort of ignored most of the contents of <code>yoneda.lean</code> and added an <code>equiv</code> which I could actually understand</p>

#### [ Reid Barton (Nov 16 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147797631):
<p>though I feel this approach isn't ideal either</p>

#### [ Johan Commelin (Nov 16 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147802724):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I don't think this is in your Yoneda file in an equivalent form, is it?</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">yoneda_sections</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="n">yoneda</span><span class="bp">.</span><span class="n">obj</span> <span class="n">U</span> <span class="err">⟹</span> <span class="n">F</span><span class="o">)</span> <span class="err">≅</span> <span class="n">F</span><span class="bp">.</span><span class="n">obj</span> <span class="n">U</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">hom</span> <span class="o">:=</span> <span class="k">show</span> <span class="o">(</span><span class="n">yoneda</span><span class="bp">.</span><span class="n">obj</span> <span class="n">U</span> <span class="err">⟹</span> <span class="n">F</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">F</span><span class="bp">.</span><span class="n">obj</span> <span class="n">U</span><span class="o">),</span> <span class="k">from</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="n">α</span><span class="bp">.</span><span class="n">app</span> <span class="n">U</span> <span class="o">(</span><span class="mi">𝟙</span> <span class="n">U</span><span class="o">),</span>
  <span class="n">inv</span> <span class="o">:=</span> <span class="k">show</span> <span class="n">F</span><span class="bp">.</span><span class="n">obj</span> <span class="n">U</span> <span class="bp">→</span> <span class="n">yoneda</span><span class="bp">.</span><span class="n">obj</span> <span class="n">U</span> <span class="err">⟹</span> <span class="n">F</span><span class="o">,</span> <span class="k">from</span> <span class="bp">λ</span> <span class="n">s</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">app</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">V</span><span class="o">,</span> <span class="k">show</span> <span class="bp">_</span> <span class="bp">→</span> <span class="n">F</span><span class="bp">.</span><span class="n">obj</span> <span class="n">V</span><span class="o">,</span> <span class="k">from</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="n">F</span><span class="bp">.</span><span class="n">map</span> <span class="n">i</span> <span class="n">s</span><span class="o">,</span>
    <span class="n">naturality&#39;</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">V₁</span> <span class="n">V₂</span> <span class="n">i</span><span class="o">,</span> <span class="k">by</span> <span class="n">tidy</span><span class="bp">;</span> <span class="n">erw</span> <span class="n">F</span><span class="bp">.</span><span class="n">map_comp</span><span class="bp">;</span> <span class="n">tidy</span> <span class="o">},</span>
  <span class="n">hom_inv_id&#39;</span> <span class="o">:=</span>
  <span class="k">begin</span>
    <span class="n">ext</span> <span class="n">α</span> <span class="n">V</span> <span class="n">i</span><span class="o">,</span>
    <span class="n">tidy</span> <span class="o">{</span><span class="n">trace_result</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">},</span>
    <span class="k">have</span> <span class="o">:=</span> <span class="n">congr</span> <span class="o">(</span><span class="n">α</span><span class="bp">.</span><span class="n">naturality</span> <span class="n">i</span><span class="o">),</span>
    <span class="n">dsimp</span> <span class="n">at</span> <span class="n">this</span><span class="o">,</span>
    <span class="n">erw</span> <span class="err">←</span><span class="o">(</span><span class="n">this</span> <span class="n">rfl</span><span class="o">),</span>
    <span class="n">simp</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">inv_hom_id&#39;</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">tidy</span><span class="bp">;</span> <span class="n">erw</span> <span class="n">F</span><span class="bp">.</span><span class="n">map_id</span><span class="bp">;</span> <span class="n">tidy</span> <span class="o">}</span>
</pre></div>


<p>That <code>hom_inv_id'</code> is particularly nasty. Would <code>tidy</code> + <code>rewrite_search</code> be able to deal with that?</p>

#### [ Scott Morrison (Nov 16 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147803013):
<p>No, we've already got this. This iso is just a component of the natural isomorphism produced in <code>yoneda_lemma</code>.</p>

#### [ Scott Morrison (Nov 16 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147803015):
<div class="codehilite"><pre><span></span>@[simp] lemma yoneda_sections (X : C) (F : Cᵒᵖ ⥤ Type v₁) : (yoneda.obj X ⟹ F) ≅ ulift.{u₁} (F.obj X) :=
nat_iso.app (yoneda_lemma C) (X, F)
</pre></div>

#### [ Scott Morrison (Nov 16 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147803018):
<p>should do it.</p>

#### [ Scott Morrison (Nov 16 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147803027):
<p>If you're already working in a small category you can remove the <code>ulift</code>.</p>

#### [ Scott Morrison (Nov 16 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147803088):
<p><code>yoneda_lemma</code> is the natural isomorphism between the two functors starting with <code>(X, F)</code>. You can either embed <code>X</code> into presheafs, via the yoneda embedding, and then take hom, or you can just evaluate <code>F</code> on <code>X</code>.</p>

#### [ Scott Morrison (Nov 16 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147803312):
<p>And</p>
<div class="codehilite"><pre><span></span>omit 𝒞
def ulift_trivial (V : Type u₁) : ulift.{u₁} V ≅ V := by tidy

@[simp] def yoneda_sections_small {C : Type u₁} [small_category C] (X : C) (F : Cᵒᵖ ⥤ Type u₁) : (yoneda.obj X ⟹ F) ≅ F.obj X :=
nat_iso.app (yoneda_lemma C) (X, F) ≪≫ ulift_trivial _
</pre></div>


<p>gives you the version you want, for small categories.</p>

#### [ Scott Morrison (Nov 16 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147803314):
<p>Shall I just push this as a separate PR?</p>

#### [ Scott Morrison (Nov 16 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147803361):
<p>Sorry, it was an obvious omission in writing <code>yoneda.lean</code>, just writing out the main result in components.</p>

#### [ Scott Morrison (Nov 16 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147804444):
<p>This is available at <a href="https://github.com/leanprover/mathlib/pull/480" target="_blank" title="https://github.com/leanprover/mathlib/pull/480">https://github.com/leanprover/mathlib/pull/480</a>.</p>

#### [ Scott Morrison (Nov 16 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147804449):
<p>It depends on the limits PR, because it's not worth backporting, but you're welcome to merge into the <code>sheaf</code> branch.</p>

#### [ Johan Commelin (Nov 16 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147827210):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Ok cool! I kept on struggling with that product category. But this looks really nice!</p>

#### [ Johan Commelin (Nov 17 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147868545):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Is <code>iso_of_is_iso</code> missing in the library?</p>

#### [ Scott Morrison (Nov 17 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147868567):
<p>Yes, lots of iso stuff is missing, that I've just been discovering now. :-)</p>

#### [ Scott Morrison (Nov 17 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147868569):
<p>I've been filling it in the monoidal categories repository, which is where I need it immediately.</p>

#### [ Scott Morrison (Nov 17 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147868576):
<p>Is it holding you up? I can make yet another PR to mathlib with some improvements to the <code>iso</code> and <code>is_iso</code> interface.</p>

#### [ Johan Commelin (Nov 17 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147868625):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">iso_of_is_iso</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">C</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="err">⟶</span> <span class="n">Y</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">is_iso</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">X</span> <span class="err">≅</span> <span class="n">Y</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">hom</span> <span class="o">:=</span> <span class="n">f</span><span class="o">,</span>
  <span class="bp">..</span><span class="n">h</span><span class="o">}</span>
</pre></div>


<p>That's whay I have at the top of my file now.</p>

#### [ Scott Morrison (Nov 17 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147868668):
<p>Ok, if that's keeping you afloat for now, I'll finish up a few things before making a "fixing isos" PR. It turns out there are at least a dozen other things missing too. :-)</p>

#### [ Scott Morrison (Nov 17 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147868676):
<p>As I'm sure Mario has told us many times before, you actually have to use this stuff!</p>

#### [ Johan Commelin (Nov 17 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147869737):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I just pushed a whole bunch of stuff to the <code>sheaf</code> branch. If you want more data points for how stuff is used...</p>

#### [ Johan Commelin (Nov 17 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147869739):
<p>I'm gathering stuff that should move elsewhere at the top of the file. If it fits into PRs that you are preparing, please take it.</p>

#### [ David Michael Roberts (Nov 21 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148077160):
<blockquote>
<p>I do understand that the issue with an fpqc cover is that you can't make a set of all fpqc covers</p>
</blockquote>
<p>The issue is that there is not even a set of fpqc covers whose elements refine all possible fpqc covers, whereas for fppf and coarser this is true, even when there's not a set of isomorphism classes of covers. This is a genuine problem, and there is a model of ZF whose category of sets forms a large site with this 'feature' (with covers=surjective functions).</p>

#### [ David Michael Roberts (Nov 21 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148077261):
<p>One can of course consider whether a given presheaf is a fpqc sheaf or not, but forget trying to fpcq-sheafify in general. The hypotheses of the general adjoint functor theorem are not satisfied, so one cannot construct the left adjoint to Sh_fpqc(Aff) --&gt; PreSh(Aff).</p>

#### [ Johan Commelin (Nov 27 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148639830):
<p>I currently have</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">map_left_id</span> <span class="o">:</span> <span class="n">map_left</span> <span class="n">R</span> <span class="o">(</span><span class="n">nat_trans</span><span class="bp">.</span><span class="n">id</span> <span class="n">L</span><span class="o">)</span> <span class="err">≅</span> <span class="n">functor</span><span class="bp">.</span><span class="n">id</span> <span class="bp">_</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">hom</span> <span class="o">:=</span>
  <span class="o">{</span> <span class="n">app</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span><span class="o">,</span> <span class="o">{</span> <span class="n">left</span> <span class="o">:=</span> <span class="mi">𝟙</span> <span class="bp">_</span><span class="o">,</span> <span class="n">right</span> <span class="o">:=</span> <span class="mi">𝟙</span> <span class="bp">_</span> <span class="o">}</span> <span class="o">},</span>
  <span class="n">inv</span> <span class="o">:=</span>
  <span class="o">{</span> <span class="n">app</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span><span class="o">,</span> <span class="o">{</span> <span class="n">left</span> <span class="o">:=</span> <span class="mi">𝟙</span> <span class="bp">_</span><span class="o">,</span> <span class="n">right</span> <span class="o">:=</span> <span class="mi">𝟙</span> <span class="bp">_</span> <span class="o">}</span> <span class="o">}</span> <span class="o">}</span>
</pre></div>


<p>but that is a worthless simp-lemma because of <code>≅</code>. I think that in fact equality should hold:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">map_left_id&#39;</span> <span class="o">:</span> <span class="n">map_left</span> <span class="n">R</span> <span class="o">(</span><span class="n">nat_trans</span><span class="bp">.</span><span class="n">id</span> <span class="n">L</span><span class="o">)</span> <span class="bp">=</span> <span class="n">functor</span><span class="bp">.</span><span class="n">id</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>But I have no idea how to prove that two terms of a structure are equal. Is it true that they are equal if all their fields are equal? Is this somewhere in mathlib?</p>

#### [ Reid Barton (Nov 27 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148640013):
<p>This is generally what extensionality lemmas do... but you're probably going to have a bad time working with equality of functors</p>

#### [ Reid Barton (Nov 27 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148640081):
<p>what's <code>map_left</code>?</p>

#### [ Reid Barton (Nov 27 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148640129):
<p>Never mind, I figured it out from one of your other messages</p>

#### [ Patrick Massot (Nov 27 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148640189):
<p>Not sure it will help, but your question looks like the classic:</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">johan</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="o">(</span><span class="n">aone</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">johan</span><span class="bp">.</span><span class="n">ext</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">johan</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">X</span><span class="bp">.</span><span class="n">a</span> <span class="bp">=</span> <span class="n">Y</span><span class="bp">.</span><span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">=</span> <span class="n">Y</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">X</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">Y</span><span class="o">,</span>
  <span class="n">congr</span> <span class="bp">;</span> <span class="n">assumption</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Nov 27 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148640204):
<p>sorry about the silly example, but I wanted a structure including at least one data and one proof field</p>

#### [ Johan Commelin (Nov 27 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148640336):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Thanks, I should have thought about <code>cases</code>.</p>

#### [ Reid Barton (Nov 27 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148640349):
<p>I think what you have now is the best way</p>

#### [ Johan Commelin (Nov 27 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148640352):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Well, but working with natural isomorphisms is also a massive pain atm.</p>

#### [ Reid Barton (Nov 27 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148640456):
<p>I guarantee it is not as bad as rewriting morphisms across equalities of objects and then trying to reason about the result</p>

#### [ Patrick Massot (Nov 27 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148640556):
<p>We should really setup a FAQ somewhere</p>

#### [ Johan Commelin (Nov 27 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148662831):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I have no idea if this makes any sense, but I regularly get errors like these:</p>
<div class="codehilite"><pre><span></span><span class="n">type</span> <span class="n">mismatch</span> <span class="n">at</span> <span class="n">application</span>
  <span class="n">colimit</span><span class="bp">.</span><span class="n">pre_map</span> <span class="o">(</span><span class="n">comma</span><span class="bp">.</span><span class="n">fst</span> <span class="n">yoneda</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_obj</span> <span class="n">X</span><span class="o">)</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">)</span> <span class="o">((</span><span class="n">comma</span><span class="bp">.</span><span class="n">map_right_id&#39;</span> <span class="n">yoneda</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_obj</span> <span class="n">X</span><span class="o">))</span><span class="bp">.</span><span class="n">hom</span><span class="o">)</span>
<span class="n">term</span>
  <span class="o">(</span><span class="n">comma</span><span class="bp">.</span><span class="n">map_right_id&#39;</span> <span class="n">yoneda</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_obj</span> <span class="n">X</span><span class="o">))</span><span class="bp">.</span><span class="n">hom</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="n">comma</span><span class="bp">.</span><span class="n">map_right</span> <span class="n">yoneda</span> <span class="o">(</span><span class="mi">𝟙</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_obj</span> <span class="n">X</span><span class="o">))</span> <span class="err">⟶</span> <span class="n">functor</span><span class="bp">.</span><span class="n">id</span> <span class="o">(</span><span class="n">comma</span> <span class="n">yoneda</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_obj</span> <span class="n">X</span><span class="o">))</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span>
        <span class="o">(</span><span class="n">max</span> <span class="err">?</span> <span class="n">v</span><span class="o">)</span>
        <span class="n">v</span>
        <span class="err">?</span><span class="o">)</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="err">?</span><span class="n">m_3</span> <span class="err">⟹</span> <span class="err">?</span><span class="n">m_4</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span>
</pre></div>


<p>Would it help to just get rid of the notation <code>⟹</code>, and always speak of natural transformations as homs in the functor category?</p>

#### [ Johan Commelin (Nov 27 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148662863):
<p>Or is this a stupid universe issue again? (I just realise there are annoying <code>?</code> in the error...)</p>

#### [ Johan Commelin (Nov 27 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148662980):
<p>Ok, never mind. It's a universe issue.</p>

#### [ Kenny Lau (Nov 27 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148664964):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> how do you get that many colours</p>

#### [ Johan Commelin (Nov 27 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148665094):
<p>I had <code>less</code> syntax, instead of <code>lean</code> <span class="emoji emoji-1f643" title="upside down">:upside_down:</span> <span class="user-mention" data-user-id="110064">@Kenny Lau</span></p>

#### [ Scott Morrison (Nov 27 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148666324):
<blockquote>
<p>I guarantee it is not as bad as rewriting morphisms across equalities of objects and then trying to reason about the result</p>
</blockquote>
<p>Yes. This. Please don't prove equalities between functors, you are just setting yourself up for suffering.</p>

#### [ Reid Barton (Nov 27 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148670683):
<blockquote>
<p>Would it help to just get rid of the notation <code>⟹</code>, and always speak of natural transformations as homs in the functor category?</p>
</blockquote>
<p>I have actually wondered about this too, after a few minor annoyances involving the difference between <code>nat_trans.vcomp</code> and <code>category.comp</code>.</p>

#### [ Reid Barton (Nov 27 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148670713):
<p>It's hard to predict which one you will get once you start talking about colimits in categories of presheaves, as Johan has probably also experienced.</p>

#### [ Reid Barton (Nov 27 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148671054):
<p>It might be a rather invasive change though, or even not workable for some reason</p>

#### [ Scott Morrison (Nov 27 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148673378):
<p>I've experienced the same pain, but haven't tried removing <code>⟹</code>. It seems a reasonable experiment, however.</p>

#### [ Johan Commelin (Nov 28 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148696347):
<p>I don't like the idea of setting myself up for suffering.</p>

#### [ Johan Commelin (Nov 28 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148696378):
<p>But I'm suffering hard at the moment.</p>

#### [ Johan Commelin (Nov 28 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148696393):
<p>After all <code>functor.id ⋙ F</code> is not defeq to <code>F</code>, and so we need some natural isomorphisms, and I just get the general feeling that we are walking headfirst into nasty 2-categorical territory.</p>

#### [ Johan Commelin (Nov 28 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148696399):
<p>Because, say what you like, but Lean isn't very good at working with the canonical natural isomorphism between <code>functor.id ⋙ F</code> and <code>F</code>.</p>

#### [ Johan Commelin (Nov 28 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148696451):
<p>I've got the following context:</p>
<div class="codehilite"><pre><span></span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">,</span>
<span class="err">𝒞</span> <span class="o">:</span> <span class="n">small_category</span> <span class="n">C</span><span class="o">,</span>
<span class="n">D</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="err">𝒟</span> <span class="o">:</span> <span class="n">category</span> <span class="n">D</span><span class="o">,</span>
<span class="n">F</span> <span class="o">:</span> <span class="n">C</span> <span class="err">⥤</span> <span class="n">D</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">has_colimits</span> <span class="n">D</span><span class="o">,</span>
<span class="n">X</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">C</span>
<span class="err">⊢</span> <span class="n">colimit</span><span class="bp">.</span><span class="n">pre</span> <span class="o">(</span><span class="n">comma</span><span class="bp">.</span><span class="n">fst</span> <span class="n">yoneda</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_obj</span> <span class="n">X</span><span class="o">)</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">)</span> <span class="o">(</span><span class="n">comma</span><span class="bp">.</span><span class="n">map_right</span> <span class="n">yoneda</span> <span class="o">(</span><span class="mi">𝟙</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_obj</span> <span class="n">X</span><span class="o">)))</span> <span class="bp">=</span>
    <span class="mi">𝟙</span> <span class="o">(</span><span class="n">colimit</span> <span class="o">(</span><span class="n">comma</span><span class="bp">.</span><span class="n">fst</span> <span class="n">yoneda</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_obj</span> <span class="n">X</span><span class="o">)</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">))</span>
</pre></div>


<p>This might look a bit daunting, but <code>(comma.map_right yoneda (𝟙 (functor.of_obj X)))</code> is naturally isomorphic to <code>functor.id _</code></p>

#### [ Johan Commelin (Nov 28 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148696511):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I'm really lost here. The maths is trivial. But Lean is fighting back hard.</p>

#### [ Scott Morrison (Nov 28 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148696896):
<p>Want to point me to a file and a commit?</p>

#### [ Johan Commelin (Nov 28 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697034):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> <a href="https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/presheaf.lean#L69" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/presheaf.lean#L69">https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/presheaf.lean#L69</a></p>

#### [ Johan Commelin (Nov 28 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697048):
<p>Maybe I still don't know how to let the library do the heavy lifting for me...</p>

#### [ Scott Morrison (Nov 28 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697316):
<p>woah, checking out that branch is like stepping into the future. adjunctions, cocompletions, groupoids, oh my.</p>

#### [ Johan Commelin (Nov 28 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697393):
<p>Well, most of that is by Reid.</p>

#### [ Johan Commelin (Nov 28 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697415):
<p>Or I should say: all of <em>that</em> is by Reid.</p>

#### [ Scott Morrison (Nov 28 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697497):
<p>Can we not call functors <code>f</code>, when they could perfectly well be <code>F</code>?</p>

#### [ Scott Morrison (Nov 28 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697542):
<p>Also, I feel you're slightly overusing variables. Things like <code>map</code> and <code>map'</code> should have the variable <code>F : C \func D</code> visible right there at the definition.</p>

#### [ Scott Morrison (Nov 28 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697554):
<p>variables are great for implicit arguments, or even the primary argument if they are the sole primary argument for 20 definitions in a row...</p>

#### [ Johan Commelin (Nov 28 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697568):
<p>Sure. I was using <code>F</code> for presheaves, but I decided that maybe I shouldn't yet do that.</p>

#### [ Johan Commelin (Nov 28 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697647):
<p>Anyway, you shouldn't look too much at the <code>sheaf.lean</code> file. It will need a major rewrite once I have working presheaves.</p>

#### [ Scott Morrison (Nov 28 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697740):
<p>Lots of stuff doesn't compile?</p>

#### [ Scott Morrison (Nov 28 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697742):
<p>In the imports of presheaf.lean</p>

#### [ Johan Commelin (Nov 28 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697786):
<p>Hmmm... I thought those were fine... but maybe stuff broke.</p>

#### [ Scott Morrison (Nov 28 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697789):
<p>e.g. limits/limits.lean and adjunctions.lean</p>

#### [ Johan Commelin (Nov 28 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697815):
<p>adjunctions probably don't compile</p>

#### [ Johan Commelin (Nov 28 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697822):
<p>limits should work, but maybe it broke after I merged in Reid's branch</p>

#### [ Scott Morrison (Nov 28 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697824):
<p>Ok, I see the thing you probably need, which is naturality in the second argument of colimit.pre</p>

#### [ Scott Morrison (Nov 28 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697831):
<p>I can try to provide you that, and you can try to get stuff to compile :-)</p>

#### [ Johan Commelin (Nov 28 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697896):
<p>Ok, so I have <code>colimit.pre_map</code></p>

#### [ Scott Morrison (Nov 28 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697904):
<p>yes, but that's naturality in the first argument, which isn't what you need</p>

#### [ Johan Commelin (Nov 28 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697907):
<p>But I guess we need to upgrade <code>pre</code> into a functor?</p>

#### [ Scott Morrison (Nov 28 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697911):
<p>unfortunately I think that might need to wait for 2-categories, I'm not sure. :-)</p>

#### [ Johan Commelin (Nov 28 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697919):
<p>Right... but it is where this stuff is sucking us into, not?</p>

#### [ Scott Morrison (Nov 28 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697960):
<p>I'm actually not sure where I should do this work. The main <code>limits</code> branch is now a bit stranded, as Reid has been pulling stuff out into separate PRs.</p>

#### [ Scott Morrison (Nov 28 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697966):
<p>Doing work on the limits branch now may get orphaned, I'm not sure.</p>

#### [ Johan Commelin (Nov 28 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697980):
<p>Maybe dump it into <code>sheafy_preamble</code></p>

#### [ Johan Commelin (Nov 28 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697995):
<p>I've been using that file to collect all sorts of facts that I need.</p>

#### [ Scott Morrison (Nov 28 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698006):
<p>Yeah, I'm worried about that getting orphaned too. :-)</p>

#### [ Scott Morrison (Nov 28 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698050):
<p>We're playing a bit fast and loose with our branches at the moment.</p>

#### [ Johan Commelin (Nov 28 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698056):
<p>Very much.</p>

#### [ Johan Commelin (Nov 28 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698093):
<p>So what exactly is the statement that you are trying to prove?</p>

#### [ Scott Morrison (Nov 28 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698100):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>, I'd really like to straighten out the limits branches a bit. What is the best way to "rebase" (possibly by hand) everything remaining on top of <code>limits-2</code>? Is this a bad thing to want to do?</p>

#### [ Scott Morrison (Nov 28 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698145):
<p>No idea :-) I hadn't even started.</p>

#### [ Scott Morrison (Nov 28 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698181):
<p>Say we have a natural transformation a : E \natt E'.</p>

#### [ Scott Morrison (Nov 28 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698235):
<p>colim.map (a &gt;&gt;&gt; F) gives a map from colim (E &gt;&gt;&gt; F) to colim (E' &gt;&gt;&gt; F)</p>

#### [ Scott Morrison (Nov 28 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698250):
<p>presumably the triangle, obtained by mapping both of those to colim F via colim.pre, commutes?</p>

#### [ Scott Morrison (Nov 28 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698274):
<p>So then if a is invertible, we have <code>colim.pre F E = colim.map (a^{-1} &gt;&gt;&gt; F) &gt;&gt; colim.pre F E' &gt;&gt; colim.map (a &gt;&gt;&gt; F)</code>.</p>

#### [ Scott Morrison (Nov 28 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698318):
<p>and hopefully now if E' is the identity, as in your case, everything quickly simplifies from there</p>

#### [ Johan Commelin (Nov 28 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698343):
<p>So <code>pre_map</code> is saying that this triangle commutes.</p>

#### [ Scott Morrison (Nov 28 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698410):
<p>No. <code>pre_map</code> is about changing the functor <code>F</code>, not the functor <code>E</code>.</p>

#### [ Johan Commelin (Nov 28 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698416):
<p>But if <code>E' = functor.id _</code> it still doesn't simplify, because <code>functor.id _ &gt;&gt;&gt; F</code> is not <code>F</code>. For example <code>colimit.pre F (functor.id _) = \b1 (colimit F)</code> does not typecheck <span class="emoji emoji-2639" title="sad">:sad:</span></p>

#### [ Scott Morrison (Nov 28 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698417):
<p>I've just been looking at the history of the <code>sheaf</code> branch.</p>

#### [ Johan Commelin (Nov 28 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698433):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I think you are confusing <code>map_pre</code> and <code>pre_map</code>.</p>

#### [ Scott Morrison (Nov 28 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698437):
<p>And ... you're up shit creek without a paddle. :-)</p>

#### [ Johan Commelin (Nov 28 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698441):
<p><code>pre_map</code> is something I added. It is in <code>sheafy_preamble.lean</code></p>

#### [ Scott Morrison (Nov 28 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698445):
<p>Getting <code>sheaf</code> back on top of master after <code>limits-2</code> is merged is going to suck.</p>

#### [ Johan Commelin (Nov 28 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698488):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I will probably just copy-paste stuff into a new branch...</p>

#### [ Scott Morrison (Nov 28 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698489):
<p>I'm looking at</p>
<div class="codehilite"><pre><span></span>lemma colimit.pre_map {K : Type v} [small_category K] [has_colimits_of_shape K C] (E : K ⥤ J) :
  colimit.pre F E ≫ colim.map α = colim.map (whisker_left E α) ≫ colimit.pre G E :=
by ext; rw [←assoc, colimit.ι_pre, colim.ι_map, ←assoc, colim.ι_map, assoc, colimit.ι_pre]; refl
</pre></div>


<p>in <code>limits-2</code>.</p>

#### [ Scott Morrison (Nov 28 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698507):
<p>I see. But yes, your <code>pre_map</code> is what we need. :-)</p>

#### [ Johan Commelin (Nov 28 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698523):
<p>Aaahrg... so the names have changed...</p>

#### [ Johan Commelin (Nov 28 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698565):
<p>What is called <code>pre_map</code> in <code>limits-2</code> used to be <code>map_pre</code> on your old limits branch.</p>

#### [ Johan Commelin (Nov 28 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698572):
<p>Ok, so in <code>presheaf.lean</code> you can see that I already <code>erw</code>d the <code>pre_map</code>-thingy.</p>

#### [ Scott Morrison (Nov 28 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698574):
<p>I see. :-) Reid must have fixed it. :-) As I said, up a creek! :-)</p>

#### [ Scott Morrison (Nov 28 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698581):
<p>Well, I can't see that, because nothing compiles. :-)</p>

#### [ Scott Morrison (Nov 28 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698603):
<p>So, you need to keep the <code>colim.map</code> in there for the unitor.</p>

#### [ Johan Commelin (Nov 28 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698613):
<p>Sorry, I need to run to a seminar...</p>

#### [ Johan Commelin (Nov 28 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698663):
<p>And I'm sorry that stuff doens't compile. I still have some sort of interactive VScode when I work on this...</p>

#### [ Johan Commelin (Nov 28 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698669):
<p>Maybe I should just wait till limits are merged, and then start from scratch.</p>

#### [ Scott Morrison (Nov 28 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698678):
<p>You just want to know that</p>
<div class="codehilite"><pre><span></span>colimit.pre F (functor.id _) = colimit.map (left_unitor F)
</pre></div>


<p>(that's not meant to be real code).</p>

#### [ Scott Morrison (Nov 28 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698746):
<p>Okay, in any case, keep bugging me about this. I'd both like to help, and like to see the resolution. I think it's going to be fine. :-)</p>

#### [ Johan Commelin (Nov 28 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148704306):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Thanks for all your comments. I'll see if I can make any progress.</p>

#### [ Reid Barton (Nov 28 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148708825):
<p>Oh yeah, I noticed all the <code>limit.</code> lemmas had names of the form <code>limit.foo_bar</code> if the left-hand side looked like <code>limit.foo ... &gt;&gt; limit.bar ...</code>, and so I reversed the components of all the names of the corresponding <code>colimit</code> lemmas because they have the composition on the left-hand side in the other order.</p>

#### [ Reid Barton (Nov 28 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148708855):
<p>Actually I just copied and pasted the limit lemmas to make colimit versions, I ignored whatever was there before (which I think was not a full set of matching lemmas)</p>

#### [ Johan Commelin (Nov 28 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148709058):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I fixed a bunch of compile issues, which we due to <code>functor.const</code> being picked from the wrong namespace (even though <code>category_theory</code> seems to be open). I really hope Lean 4 will kick a lot of these things out of the root namespace, because these conflicts are quite annoying.</p>

#### [ Reid Barton (Nov 28 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148709086):
<p>Yeah I encountered that same <code>functor.const</code> issue too, not sure what caused it to crop up suddenly</p>

#### [ Keeley Hoek (Nov 28 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148709263):
<p>Does @[priority] affect that kind of resolution?</p>

#### [ Reid Barton (Nov 28 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148710423):
<p>I can try to produce a rebased version of my <code>adjunctions</code> branch, that shouldn't take too long.</p>

#### [ Reid Barton (Nov 28 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148712087):
<p>It looks like Johan has mostly just been working on one file, so probably easiest to just copy the <code>sheaf</code> branch into a new branch indeed</p>

#### [ Reid Barton (Nov 28 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148712367):
<p>Oh, also the specific shape limit stuff isn't in <code>limits-2</code> yet. I do have a copy that at least builds on top of <code>limits-2</code> though, so I can push that somewhere as a temporary measure for you, Johan</p>

#### [ Johan Commelin (Nov 28 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148712439):
<p>Ooh, don't worry too much about this</p>

#### [ Johan Commelin (Nov 28 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148712447):
<p>I think it's best to fix it after <code>limits-2</code> is merged.</p>

#### [ Reid Barton (Nov 28 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148712710):
<p>Ah, fair enough. I'll hold off on these things then</p>

#### [ Johan Commelin (Nov 28 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148720854):
<p>I'm very confused about <a href="https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/commas.lean#L155-L156" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/commas.lean#L155-L156">https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/commas.lean#L155-L156</a><br>
I thought I understood <code>rfl</code> by now. But apparently this is not <code>rfl</code>. If someone can explain this mystery, I would be very grateful.</p>

#### [ Gabriel Ebner (Nov 28 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148721486):
<p><code>map_right_id'</code> should be a <code>def</code>.  Theorems don't unfold (except for special circumstances / options).</p>

#### [ Johan Commelin (Nov 28 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148721547):
<p>Aaah, it should certainly be a <code>def</code>. Let me try again.</p>

#### [ Johan Commelin (Nov 28 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148721603):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> Cool! Now it works.</p>

#### [ Kevin Buzzard (Nov 28 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148727291):
<p>Computer scientists have such weird ideas about what a theorem is :-)</p>

#### [ Johan Commelin (Nov 28 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148728262):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> <span class="user-mention" data-user-id="110032">@Reid Barton</span> I suggest we replace <code>of_obj</code> with <code>of.obj</code> after defining</p>
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">functor</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="err">𝒞</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span>
<span class="n">include</span> <span class="err">𝒞</span>

<span class="n">def</span> <span class="n">of</span> <span class="o">:</span> <span class="n">C</span> <span class="err">⥤</span> <span class="o">(</span><span class="n">punit</span> <span class="err">⥤</span> <span class="n">C</span><span class="o">)</span> <span class="o">:=</span> <span class="n">const</span> <span class="n">punit</span>

<span class="kn">namespace</span> <span class="n">of</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">obj_obj</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">C</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">of</span><span class="bp">.</span><span class="n">obj</span> <span class="n">X</span><span class="o">)</span><span class="bp">.</span><span class="n">obj</span> <span class="bp">=</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">X</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">obj_map</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">C</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">of</span><span class="bp">.</span><span class="n">obj</span> <span class="n">X</span><span class="o">)</span><span class="bp">.</span><span class="n">map</span> <span class="bp">=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="mi">𝟙</span> <span class="n">X</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">map_app</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">C</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="err">⟶</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">of</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span><span class="o">)</span><span class="bp">.</span><span class="n">app</span> <span class="bp">=</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="kn">end</span> <span class="n">of</span>

<span class="kn">end</span> <span class="n">functor</span>
</pre></div>


<p>Is that ok?</p>

#### [ Reid Barton (Nov 28 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148728479):
<p>Yes, that seems sensible</p>

#### [ Reid Barton (Nov 28 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148748886):
<blockquote>
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I fixed a bunch of compile issues, which we due to <code>functor.const</code> being picked from the wrong namespace (even though <code>category_theory</code> seems to be open). I really hope Lean 4 will kick a lot of these things out of the root namespace, because these conflicts are quite annoying.</p>
</blockquote>
<p>If someone could track this down, it would be super helpful. I'm not sure what changed here.</p>

#### [ Johan Commelin (Nov 30 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148861225):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> <span class="user-mention" data-user-id="110087">@Scott Morrison</span> Do you think we need something like this? I find it extremely annoying that Lean refuses some of my morphisms because the come from an opposite category. I understand why Lean complains, but getting it to accept the arrow is extremely annoying. This might help...</p>
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">category</span><span class="bp">.</span><span class="n">hom</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="err">𝒞</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span>
<span class="n">include</span> <span class="err">𝒞</span>

<span class="n">def</span> <span class="n">op</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">C</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="err">⟶</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span> <span class="bp">@</span><span class="n">category</span><span class="bp">.</span><span class="n">hom</span> <span class="bp">_</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">opposite</span> <span class="n">Y</span> <span class="n">X</span> <span class="o">:=</span> <span class="n">f</span>
<span class="n">def</span> <span class="n">deop</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">C</span><span class="err">ᵒᵖ</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="err">⟶</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span> <span class="bp">@</span><span class="n">category</span><span class="bp">.</span><span class="n">hom</span> <span class="bp">_</span> <span class="err">𝒞</span> <span class="n">Y</span> <span class="n">X</span> <span class="o">:=</span> <span class="n">f</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">op_deop</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">C</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="err">⟶</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span><span class="bp">.</span><span class="n">op</span><span class="bp">.</span><span class="n">deop</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">deop_op</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">C</span><span class="err">ᵒᵖ</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="err">⟶</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span><span class="bp">.</span><span class="n">deop</span><span class="bp">.</span><span class="n">op</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="kn">end</span> <span class="n">category</span><span class="bp">.</span><span class="n">hom</span>
</pre></div>

#### [ Scott Morrison (Dec 01 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148898413):
<p>This sounds fine to me. I agree dealing with opposites is gross. :-(</p>

#### [ Johan Commelin (Dec 03 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/150778353):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Have you had similar experiences? What is your opinion on my proposed solution?</p>

#### [ Scott Morrison (Dec 04 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/150835179):
<p>Hi <span class="user-mention" data-user-id="112680">@Johan Commelin</span>, I am experimenting with making <code>op</code> irreducible, and thus _requiring_ the use of <code>op</code> or <code>deop</code> (and corresponding <code>op_obj</code> and <code>deop_obj</code> on objects).</p>

#### [ Scott Morrison (Dec 04 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/150835194):
<p>It is slightly grosser, but I think we've all discovered that too much can go mysteriously wrong with the current implementation of opposites.</p>

#### [ Johan Commelin (Dec 04 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/150835467):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Aah, that sounds like a good idea!</p>

#### [ Johan Commelin (Dec 04 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/150835496):
<p>I hadn't thought about making it irreducible. Those boundaries are useful, but I'm not yet aware of how to make the system help us.</p>

#### [ Johan Commelin (Dec 04 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/150835503):
<p>So yes, I think it is very good if we have to be explicit about <code>op</code>ing and <code>deop</code>ing.</p>

#### [ Scott Morrison (Dec 04 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/150840492):
<p><a href="https://github.com/leanprover/mathlib/issues/510" target="_blank" title="https://github.com/leanprover/mathlib/issues/510">#510</a></p>

#### [ Johan Commelin (Dec 04 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/150841470):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Looks good to me. I do wonder if we can remove the <code>_obj</code> suffix to make things a bit shorter. We could rename the existing <code>op</code> to <code>op_cat</code>.</p>

#### [ Johan Commelin (Dec 04 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/150841491):
<p>I think this is a good PR, but I regret that a lot of stuff is also becoming somewhat uglier.</p>

#### [ Kevin Buzzard (Dec 11 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151459647):
<p><span class="user-mention" data-user-id="132858">@Ramon Fernandez Mir</span> is making me engage with the category theory stuff! Is there a name for this map: <code>(λ f r, f r : (FF.obj x ⟶ FF.obj y) → (FF.obj x → FF.obj y)) </code>? I'm changing a long arrow to a short one. The target of the functor FF is the category <code>CommRing</code>, so I want to take an abstract element of the hom set and actually produce the ring hom. There's a coercion that does it magically, but I actually have a set of abstract homs and want a set of concrete homs and I have to feed <code>set.image</code> something.</p>

#### [ Johan Commelin (Dec 11 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151461302):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Could you provide slightly more context? I typically get away without doing anything.</p>

#### [ Kevin Buzzard (Dec 11 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151461833):
<p>We had a functor <code>FF</code> from a small category <code>J</code> to <code>CommRing</code> and two objects <code>x</code> and <code>y</code> of <code>J</code>, and we wanted the set of maps from <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>F</mi><mi>F</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">FF(x)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span></span></span></span> to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>F</mi><mi>F</mi><mo>(</mo><mi>y</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">FF(y)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mclose">)</span></span></span></span> coming from <code>J</code>.</p>

#### [ Johan Commelin (Dec 11 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151461946):
<p>I see, and <code>FF.obj x \hom FF.obj y</code> is a subtype, but you want a set?</p>

#### [ Johan Commelin (Dec 11 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151461981):
<p>Is that correct? If so, I think <code>subtype.val</code> would be the function you are looking for.</p>

#### [ Johan Commelin (Dec 11 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151461995):
<p>I don't know by heart how <code>CommRing</code> is defined.</p>

#### [ Kevin Buzzard (Dec 11 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151462204):
<p>I'm trying to get from <code>category_theory.category.hom R S</code> to <code>R -&gt; S</code></p>

#### [ Kevin Buzzard (Dec 11 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151462333):
<p>I can just evaluate a term of type <code>category_theory.category.hom R S</code> at <code>r</code> and get <code>s : S</code></p>

#### [ Kevin Buzzard (Dec 11 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151462431):
<p>but I was wondering what the name of the coercion was, because I needed to refer to the map itself when doing something else.</p>

#### [ Johan Commelin (Dec 11 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151465278):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> On line 90 of <code>category.lean</code> you can find</p>
<div class="codehilite"><pre><span></span><span class="o">{</span> <span class="n">hom</span>   <span class="o">:=</span> <span class="bp">λ</span><span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">subtype</span> <span class="o">(</span><span class="n">hom</span> <span class="n">a</span><span class="bp">.</span><span class="mi">2</span> <span class="n">b</span><span class="bp">.</span><span class="mi">2</span><span class="o">),</span>
</pre></div>


<p>(This is in the instance of <code>concrete_category</code> --&gt; <code>category</code>.) So the map you want is called <code>subtype.val</code>.</p>

#### [ Reid Barton (Dec 11 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151467554):
<p>I think there is (or should be?) some more high-level name for this, like <code>forget</code></p>

#### [ Johan Commelin (Dec 11 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151469130):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> That's right. As Reid mentioned, there is a <code>forget</code>ful functor. You will have to</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">types</span>
</pre></div>

#### [ Reid Barton (Dec 11 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151469476):
<p>Ah that's where it is</p>

#### [ Reid Barton (Dec 14 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151755507):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> did you end up using <code>forget</code>? I'm inclined to make its "C" argument implicit, would that help or hurt you?</p>

#### [ Kevin Buzzard (Dec 14 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151758445):
<p>I didn't do anything. I was talking about it with Ramon at our last meeting and haven't thought about it since</p>

#### [ Kevin Buzzard (Dec 14 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151758486):
<p>I am completely snowed under with teaching and reference writing</p>

#### [ Ramon Fernandez Mir (Dec 23 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/152438280):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> sorry I just saw this. I was playing with that code a few days ago and I didn't manage to make it work with forget. What is the "C" argument meant to be?</p>


{% endraw %}
