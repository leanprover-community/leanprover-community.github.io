---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49748categorytheorydesign.html
---

## Stream: [general](index.html)
### Topic: [category theory design](49748categorytheorydesign.html)

---


{% raw %}
#### [ Scott Morrison (Aug 12 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997040):
<p>I spent some time this afternoon trying out three different implementations of products/equalizers/pullbacks. If anyone has a moment to have a look at them, I'd very much appreciate it. It's all in &lt;<a href="https://github.com/semorrison/lean-category-theory-pr/blob/limits/src/categories/universal/default.lean" target="_blank" title="https://github.com/semorrison/lean-category-theory-pr/blob/limits/src/categories/universal/default.lean">https://github.com/semorrison/lean-category-theory-pr/blob/limits/src/categories/universal/default.lean</a>&gt;.</p>

#### [ Scott Morrison (Aug 12 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997093):
<p>To try them out, I proved that the category of types has equalizers, pullbacks, and binary products.<br>
Rather beautifully, using <code>obviously</code> you can write exactly the same proof for all three versions:<br>
you just specify the shape, and <code>obviously</code> deals with the variations in what's required to check the universal<br>
properties.</p>

#### [ Scott Morrison (Aug 12 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997103):
<p>e.g. </p>
<div class="codehilite"><pre><span></span>instance : has_equalizers (Type u) :=
{ equalizer := λ Y Z f g, { X := { y : Y // f y = g y }, ι := subtype.val, w := by obviously, h := by obviously } }
</pre></div>

#### [ Kevin Buzzard (Aug 12 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997163):
<p>I feel out of my depth commenting on your work Scott. For me the proof of the pudding will be in the eating. Are we still a long way from me defining a presheaf on the adic space <code>Spa A</code> to be a functor from some category of open sets to the category whose objects are pairs consisting of a topological ring and some open subring with some properties?</p>

#### [ Scott Morrison (Aug 12 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997218):
<p>We're ... getting there.</p>

#### [ Scott Morrison (Aug 12 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997222):
<p>For me the eating is all about the fact that I don't need to write any proofs of boring statements, and _that_ I'm feeling pretty happy about.</p>

#### [ Mario Carneiro (Aug 12 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997234):
<p>Could we have a coercion from <code>span</code> and friends to the object?</p>

#### [ Scott Morrison (Aug 12 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997235):
<p>The big unknown step in getting to what you want is that we'll need to do enriched categories, and I haven't even started thinking about that.</p>

#### [ Scott Morrison (Aug 12 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997239):
<p>Sure, those coercions would be nice.</p>

#### [ Scott Morrison (Aug 12 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997278):
<p>I went with very short, nondescript field names for these structures, but attempted to be very uniform. To me the naming looks terrible, so if anyone has comments there I'm all ears. :-)</p>

#### [ Mario Carneiro (Aug 12 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997291):
<p>it didn't cry out to me as much as previous commits, so I guess that's a step forward?</p>

#### [ Scott Morrison (Aug 12 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997330):
<p>:-)</p>

#### [ Mario Carneiro (Aug 12 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997331):
<p>uniform naming is good</p>

#### [ Scott Morrison (Aug 12 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997340):
<p>I really love <span class="user-mention" data-user-id="110032">@Reid Barton</span>'s approach, which I implemented as <code>version_2</code> in that file. The fact that <code>obviously</code> just worked out the box to prove the category of types has all these things in Reid's approach made me very happy.</p>

#### [ Mario Carneiro (Aug 12 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997387):
<p>what is <code>is_equiv</code>?</p>

#### [ Scott Morrison (Aug 12 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997389):
<p>Having <code>obviously</code> handle <code>version_1</code> (essentially what <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> and I discussed earlier today) took a bit of tweaking, and in the end requires two hints.</p>

#### [ Scott Morrison (Aug 12 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997396):
<p>It's defined at the top of the file, as <code>is_iso</code> in the category of types: an explicit inverse function</p>

#### [ Scott Morrison (Aug 12 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997399):
<p>I can change it to something <code>equiv</code>, of course. :-)</p>

#### [ Mario Carneiro (Aug 12 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997402):
<p>I'm not sold on maximum compactification of statements. We did a lot of this in the filter/topology section, and it often made proofs longer</p>

#### [ Scott Morrison (Aug 12 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997445):
<p>Ok. Well, for now it's easy for me to continue experimenting with all three versions. They have very similar interface, except for how the universal properties are packaged.</p>

#### [ Scott Morrison (Aug 12 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997457):
<p>And for the first thing I tried to prove, all three versions admitted (the same) "shortest possible proofs".</p>

#### [ Scott Morrison (Aug 12 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997506):
<p>Just as an example, in <code>version_2</code> the proof of the field <code>h</code> in <code>has_equalizers</code> that <code>obviously</code> finds is:</p>
<div class="codehilite"><pre><span></span>/- obviously says: -/
intros X&#39;,
dsimp at *,
fsplit,
work_on_goal 0 {
  intros a a_1,
  cases a,
  have congr_fun_a_property_a_1 := congr_fun a_property a_1,
  fsplit,
  work_on_goal 0 {
  solve_by_elim
},
  work_on_goal 0 {
  simp at *,
  solve_by_elim
}
}, work_on_goal 0 {
  ext1,
  ext1,
  ext1,
  refl
}, work_on_goal 0 {
  ext1,
  ext1,
  ext1,
  cases x,
  refl
}
</pre></div>

#### [ Scott Morrison (Aug 12 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997530):
<p>where in <code>version_0</code> <code>obviously</code> finds</p>
<div class="codehilite"><pre><span></span>/- obviously says: -/
fsplit,
work_on_goal 0 {
  intros X&#39; k w a,
  have congr_fun_w_a := congr_fun w a,
  dsimp at *,
  fsplit,
  work_on_goal 0 {
  solve_by_elim
},
  work_on_goal 0 {
  simp at *,
  solve_by_elim
}
}, work_on_goal 0 {
  intros X&#39; k w,
  refl
}, work_on_goal 0 {
  dsimp at *,
  fsplit,
  intros Z_1 g_1 h w,
  ext1,
  have congr_fun_w_x := congr_fun w x,
  ext1,
  solve_by_elim
}
</pre></div>

#### [ Mario Carneiro (Aug 12 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997582):
<p>where is unfolding of the definitions happening?</p>

#### [ Mario Carneiro (Aug 12 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997584):
<p>what is <code>fsplit</code></p>

#### [ Scott Morrison (Aug 12 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997587):
<p><code>fsplit</code> is just <code>split</code>, but not reordering the new goals</p>

#### [ Scott Morrison (Aug 12 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997590):
<p>sorry, needs a better name</p>

#### [ Scott Morrison (Aug 12 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997607):
<p>(i.e. the goals for <code>fsplit</code> on a structure are the fields in order, whereas for <code>split</code> the dependent ones come first.)</p>

#### [ Mario Carneiro (Aug 12 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997736):
<p>Another version of <code>version_1</code> is to use <code>Σ!</code></p>

#### [ Mario Carneiro (Aug 12 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997775):
<p>which was once created but doesn't seem to exist anymore</p>

#### [ Mario Carneiro (Aug 12 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997776):
<p>but you can guess what the definition was given <code>∃!</code></p>

#### [ Mario Carneiro (Aug 12 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997825):
<p>one thing I like about <code>version_0.is_binary_product</code> is that the uniqueness is equational</p>

#### [ Mario Carneiro (Aug 12 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997834):
<p>Do you know if there is an equational expression for the others?</p>

#### [ Mario Carneiro (Aug 12 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997882):
<p>I don't really understand <code>version_0.is_equalizer.uniq</code></p>

#### [ Scott Morrison (Aug 12 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997956):
<p>Hmm... maybe I got that one wrong. Let's see. Uniqueness is meant to say if you have a function <code>h : X' -&gt; Y</code> so <code>h then f = h then g</code>, and two different factorisations of <code>h</code> as <code>h_1 then i</code> and <code>h_2 then i</code>, then <code>h_1 = h_2</code>.</p>

#### [ Mario Carneiro (Aug 12 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131997966):
<p>I think for mathlib, I'll vote for version_0 with the others proved as lemmas</p>

#### [ Mario Carneiro (Aug 12 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131998023):
<p>I know it's wordy, but it's also perspicuous</p>

#### [ Mario Carneiro (Aug 12 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131998042):
<p>we should save the slick version for a theorem</p>

#### [ Mario Carneiro (Aug 12 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131998097):
<p>you will notice that <a href="https://en.wikipedia.org/wiki/Product_(category_theory)" target="_blank" title="https://en.wikipedia.org/wiki/Product_(category_theory)">https://en.wikipedia.org/wiki/Product_(category_theory)</a> gives essentially version_0 as its definition</p>

#### [ Scott Morrison (Aug 12 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131998239):
<p>I think what I said for <code>version_0.is_equalizer.uniq</code> is correct, but absolutely that should be a lemma, not the official statement.</p>

#### [ Scott Morrison (Aug 12 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/131998367):
<p>Hopefully <span class="user-mention" data-user-id="110032">@Reid Barton</span> will have a look later, and comment too. He's already implemented quite a lot using something very close to <code>version_2</code>.</p>

#### [ Reid Barton (Aug 14 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132125040):
<p>Hi, I've been traveling recently (and also dealing with a broken laptop power supply) but I should be able to take a look within a couple of days.</p>

#### [ Reid Barton (Aug 20 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132473102):
<p>Returning to this topic. I have a few general comments.</p>

#### [ Reid Barton (Aug 20 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132473442):
<ul>
<li>
<p>I think it's rather important to include the <code>is_*</code> structures (like <code>is_pullback</code>, etc.) and to define the structures like <code>pullback</code> in terms of them. The <code>is_pullback</code> type is useful to express concepts like "the functor G : D -&gt; C preserves pullbacks", that is, "the image under G of a pullback diagram is again a pullback", especially in the absence of completeness assumptions on D and C. In terms of just <code>pullback</code>, the conclusion would have to include an existential and a bunch of equalities.</p>
<p>All of Scott's versions in the file linked above follow this form. I only mention point because I think Scott's library used to define <code>pullback</code> without <code>is_pullback</code>, and I've become convinced of the importance of the <code>is_*</code> structures from experience with applications.</p>
</li>
</ul>

#### [ Reid Barton (Aug 20 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132474260):
<ul>
<li>
<p>In the end, I don't think it's terribly important for applications which definition is adopted as the official definition, especially since projection notation makes it pretty easy for a structure to behave as though it has an entirely different set of fields. The biggest effect will be when constructing <code>is_pullback</code> values, since as far as I know the record <code>{ ... }</code> notation can only be used with the actual fields of the structure. For this reason alone, maybe taking the "explicit" version as the definition would be preferable, as it has the most fields (there's not much pain in using an explicit function as an "alternative constructor", when that function has just one or two arguments).</p>
<p>I did find both the "explicit" and "bijective" styles useful in different situations. I'm slightly surprised that <code>obviously</code> was able to provide all the limit constructions for the category of sets, I mean, types, using any of the definition styles. I guess <code>tauto</code> is pretty good at guessing how to do product-type constructions. I suspect if you tried to build colimits, you'd need to do more hand-holding. At any rate, when I proved that topological spaces have coproducts and coequalizers, I found it easier to do the construction using the "explicit" style; when I thought about what I would need to do in the "bijective" style, it amounted to checking the "explicit" style conditions first anyways. On the other hand, for proving facts about colimits, I made use of the "bijective" style using some <code>bij_on</code> machinery. This wasn't that easy to set up, but I'm reasonably happy with how the proofs turned out. They seem preferable to endless diagram chases--unless possibly the computer can just do the entire diagram chasing argument, in which case I won't complain about how long it is!</p>
</li>
</ul>

#### [ Reid Barton (Aug 20 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132474513):
<ul>
<li>About constructive vs classical universal properties--I've been assuming that the constructive notions are preferable, but I haven't actually experimented with the alternative, that is, making the <code>is_*</code> structures into Props rather than subsingletons. All I can report here is that using the constructive notions hasn't presented me with any major obstacles.</li>
</ul>

#### [ Reid Barton (Aug 20 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132474628):
<p>I find it a bit curious that Mario thinks the wikipedia definition is essentially Scott's "explicit" definition. To me, it's not even obvious that the "explicit" <code>is_product</code> structure is a subsingleton, but wikipedia definitely defines a proposition!</p>

#### [ Reid Barton (Aug 20 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132474662):
<p>The "explicit" definition looks like someone took the wikipedia definition and ran it through a compiler, and what came out is this structure with four fields.<br>
In math we don't even really have a specific name for the function which takes a map into X and a map into Y and produces a map into X x Y, besides the "induced" map or something.</p>

#### [ Reid Barton (Aug 20 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132474906):
<p>But in any case, the order is different. First we require a property of the (potential) product diagram, "for all ..., there exists a unique ... such that blah blah", and then call the diagram a product. Then, optionally, we could name the function that is determined by this relationship, but mostly we don't bother.</p>

#### [ Reid Barton (Aug 20 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132474943):
<p>With a constructive unique existential quantifier, you could just translate the definition word-for-word into Lean.<br>
But in any case, like I said above, I don't think the exact choice of definition is that important.</p>

#### [ Reid Barton (Aug 20 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132475609):
<p>Here's a very simple example of using the "bijective" style to prove a fact about products: namely that products are associative up to isomorphism. Suppose I have (X x Y) x Z and X x (Y x Z). Then for any object A, I get, on the one hand, a bijection between Hom(A, (X x Y) x Z) and (Hom(A, X) x Hom(A, Y)) x Hom(A, Z), and on the other hand a bijection between Hom(A, X x (Y x Z)) and Hom(A, X) x (Hom(A, Y) x Hom(A, Z)). Composing these together with the associativity isomorphism for products of sets, I get an isomorphism Hom(A, (X x Y) x Z) ~= Hom(A, X x (Y x Z)), which means that I have an isomorphism between (X x Y) x Z and X x (Y x Z), by Yoneda.</p>

#### [ Johan Commelin (Aug 20 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132475710):
<p>Is Yoneda already in Lean?</p>

#### [ Reid Barton (Aug 20 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132475783):
<p>If I were to use the explicit/first-order definition of products directly, I would need to manually build the comparison map by pairing the maps (X x Y) x Z -&gt; X and (X x Y) x Z -&gt; Y x Z given by, respectively, projection on the first component twice and (the pairing of the maps (X x Y) -&gt; Y and ...), and then construct the inverse map in the same fashion, and then finally check that the compositions are the identity, which means checking that each projection is the identity, which is going to involve a whole lot of applications of the axioms of a product object.</p>

#### [ Reid Barton (Aug 20 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132475837):
<p>Similarly, I would prefer to show that right adjoints preserve products by a calculation along the lines of<br>
Hom(A, G(X x Y)) = Hom(FA, X x Y) = Hom(FA, X) x Hom(FA, Y) = Hom(A, GX) x Hom(A, GY)<br>
although I think that in this case, the first-order approach is also not so difficult</p>

#### [ Reid Barton (Aug 20 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132476073):
<p>I think Scott's library has some version of Yoneda. The version I used is just a couple lines to prove, although I did sweep some questions of naturality in A under the rug.</p>

#### [ Reid Barton (Aug 20 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132476207):
<p>(For reference, I proved that left adjoints preserve pushouts in <a href="https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/categories/preserves_colimits.lean#L44-L82" target="_blank" title="https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/categories/preserves_colimits.lean#L44-L82">https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/categories/preserves_colimits.lean#L44-L82</a>, although the proof is still not as polished as I'd like. The basic structure is analogous to what I wrote above though.)</p>

#### [ Johan Commelin (Aug 20 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132476804):
<p>I would like to first have a proof that left adjoints preserve arbitrary colimits, and then deduce the fact about push-outs by specialisation. How hard do you think that will be?</p>

#### [ Reid Barton (Aug 20 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132477332):
<p>I had a hard time when I tried to deduce existence of pullbacks from completeness quite some time ago, but now I think I know how to go about it.</p>

#### [ Reid Barton (Aug 20 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132477463):
<p>One should describe the indexing category for the pullback in terms of generators and relations (of course, there are no relations in this case) because one needs to describe functors from the indexing category in terms of concrete data</p>

#### [ Scott Morrison (Aug 21 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132536953):
<p>Thanks, <span class="user-mention" data-user-id="110032">@Reid Barton</span>, for all the remarks. I'm rewriting my file about limits again now, and I think what I'm doing is compatible with everything you've said. The "explicit" version comes first, and the other two viewpoints are available as lemmas and alternative constructors.</p>

#### [ Scott Morrison (Aug 21 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132537150):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> I have Yoneda at &lt;<a href="https://github.com/semorrison/lean-category-theory/blob/master/src/categories/yoneda.lean" target="_blank" title="https://github.com/semorrison/lean-category-theory/blob/master/src/categories/yoneda.lean">https://github.com/semorrison/lean-category-theory/blob/master/src/categories/yoneda.lean</a>&gt;. <code>obviously</code> just plows through all the boring bits.</p>

#### [ Johan Commelin (Aug 22 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132559544):
<p>I'm also interested in what the plans are for the limit/colimit duality? Are we going to define things twice, or in terms of <code>op</code>? Or both? I don't have any experience with this... but I guess it is something that will pop up pretty soon.</p>

#### [ Scott Morrison (Aug 22 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132559605):
<p>For now I'm going to write out everything twice, with painful copy-paste-replace.</p>

#### [ Scott Morrison (Aug 22 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132559606):
<p>:-(</p>

#### [ Scott Morrison (Aug 22 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132559651):
<p>I've been thinking I should learn how to write an analogue of <code>to_additive</code>, or something even more general.</p>

#### [ Scott Morrison (Aug 22 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132559662):
<p>We certainly need to have separate definitions for limits and colimits (and all the specialisations, equalizers, coequalizers, etc), and theorems relating a limit and a colimit in the opposite category.</p>

#### [ Scott Morrison (Aug 22 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132559673):
<p>The only question is whether the "other half" of the definitions are written by hand. (And whether those theorems are automatically generated.)</p>

#### [ Johan Commelin (Aug 22 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132559783):
<p>Hmmm, <code>to_opposite</code> or <code>to_dual</code> might be a nice way of dealing with this! Especially if it could also generate the "linking" theorems.</p>

#### [ Johan Commelin (Aug 22 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132559795):
<p>I remember that some time ago there was a bit of chat about whether <code>op op C</code> was defeq to <code>C</code>. Would that help here?</p>

#### [ Scott Morrison (Aug 22 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132560744):
<p>Certainly <code>op op C</code> is defeq to <code>C</code>, since <code>op C := C</code>. I think you mean</p>
<div class="codehilite"><pre><span></span>variables {C : Type u₁} [𝒞 : category.{u₁ v₁} C]
include 𝒞

@[simp] lemma foo : @category_theory.opposite (Cᵒᵖ) (@category_theory.opposite C 𝒞) = 𝒞 := sorry
</pre></div>


<p>which is not a <code>rfl</code> lemma.</p>

#### [ Scott Morrison (Aug 22 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132560807):
<p>Of course it is true, e.g. by</p>
<div class="codehilite"><pre><span></span>@[simp] lemma foo : @category_theory.opposite (Cᵒᵖ) (@category_theory.opposite C 𝒞) = 𝒞 :=
begin
  tactic.unfreeze_local_instances,
  cases 𝒞,
  unfold category_theory.opposite,
  congr,
end
</pre></div>

#### [ Scott Morrison (Aug 22 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132560811):
<p>but I think the natural isomorphism is more useful.</p>

#### [ Johan Commelin (Aug 22 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132563707):
<p>Right, I meant your <code>foo</code>.</p>

#### [ Reid Barton (Aug 22 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132582012):
<p>Oh interesting. I read a paper on the design of a category theory library for HoTT/Coq, and they had to jump through some extra hoops to account for the fact that associativity in C^op is the <code>eq.symm</code> of associativity in C</p>

#### [ Reid Barton (Aug 22 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132582027):
<p>But I guess that doesn't show up here, because of proof irrelevance.</p>

#### [ Reid Barton (Aug 22 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132583989):
<p>The <code>op op C = C</code> question comes up if you want to dualize colimits back into limits.</p>

#### [ Reid Barton (Aug 22 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132584060):
<p>Let's suppose that we've defined a diagram in C to be a pushout when the corresponding diagram in C^op is a pullback</p>

#### [ Reid Barton (Aug 22 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132584082):
<p>Now we have some result about pushouts, for example: In a model category, a pushout of a cofibration is a cofibration.</p>

#### [ Reid Barton (Aug 22 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132584188):
<p>And we want to conclude the dual statement, namely that a pullback of a fibration is a fibration. The opposite of a model category is again a model category, with cofibrations and fibrations interchanged, so this is true by duality.<br>
(For whatever reason, it's normal in the model category literature to prove things on the "left" side and deduce the corresponding statements on the "right" side by duality, so let's just assume that we want to do it this way rather than the other way around.)</p>

#### [ Reid Barton (Aug 22 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132584285):
<p>The obvious approach is to apply the statement we already know to C^op, since C^op is also a model category.<br>
Then we obtain: A pushout (in C^op) of a cofibration (in C^op) is a cofibration (in C^op).<br>
We know that a cofibration in C^op corresponds to a fibration in C. Now we have a pushout in C^op. By definition, this is a pullback in (C^op)^op.</p>

#### [ Reid Barton (Aug 22 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132584297):
<p>In order to conclude the statement we want, we need to know (C^op)^op = C.</p>

#### [ Reid Barton (Aug 22 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132584415):
<p>Which is true, they are propositionally equal.<br>
If we have some tactic which proves the dual version of a statement from the original statement, then it can insert this propositional equality and it's no big deal.<br>
If we want to directly define the proof of the dual statement as <em>equal</em> to the original proof (with C^op substituted for C), then this will only succeed if (C^op)^op = C definitionally.</p>

#### [ Reid Barton (Aug 22 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132584511):
<p>And it's frustratingly close to being true--the proof is just this <code>cases 𝒞</code>. If we had definitional equality for structures, then (C^op)^op would be definitionally equal to C, I think.</p>

#### [ Reid Barton (Aug 22 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20design/near/132584633):
<p>If, instead of proving a theorem ("the pushout of a cofibration is a cofibration"), we were constructing a canonical isomorphism or something, I can imagine that the propositional equality (C^op)^op = C could get in the way of later reasoning about the thing we constructed</p>


{% endraw %}
