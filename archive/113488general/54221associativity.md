---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54221associativity.html
---

## Stream: [general](index.html)
### Topic: [associativity](54221associativity.html)

---


{% raw %}
#### [ Simon Hudon (Jul 30 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130552015):
<p>I'm writing a tactic about associativity and I'm inferring the associativity of the operators that appear in an expression. It turns out that this is the bottleneck of my script: building an instance of <code>is_associative</code> takes hundreds of ms. Is there a faster way to do it?</p>

#### [ Kevin Buzzard (Jul 30 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130563174):
<p>I hardly ever understand your questions Simon (too CS!), but I'd like to begin to try. Do you mean "type class inference is taking a long time checking that my random operation is associative"? You know better than I do that you can just make your own instance and add it to the type class inference system. It occurs to me that in contrast to <code>simp</code>, where I can look at traces, I don't really know how to look at what type class inference is doing. I don't want to derail this thread though.</p>

#### [ Patrick Massot (Jul 30 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130564572):
<p>Of course you know it: <code>set_option trace.class_instances true</code></p>

#### [ Patrick Massot (Jul 30 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130564575):
<p>But you only think of it when things go wrong</p>

#### [ Simon Hudon (Jul 30 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130581550):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> That's exactly it. It's not clear to me that adding instances would improve the situation</p>

#### [ Reid Barton (Jul 30 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130581859):
<p>Are you trying to infer the associativity of some operations which don't have <code>is_associative</code> instances? If so, could you give an example?</p>

#### [ Reid Barton (Jul 30 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130581922):
<p>Or is it instance lookup itself that takes a long time?</p>

#### [ Simon Hudon (Jul 30 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130583646):
<p>Instance lookup is taking a really long lime. My work around right now is, the first time I need that information, I add it to the local assumptions and I keep looking at assumptions to see if it's there before calling <code>mk_instance</code>.</p>

#### [ Simon Hudon (Jul 30 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130583738):
<p>The other idea I'm considering is to have an internal table where I cache that kind of information. That could be faster still and less intrusive but I would redo the instance inference at least once per call to the overall tactic (which I call <code>assoc_rewrite</code>)</p>

#### [ Reid Barton (Jul 30 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130583854):
<p>Whoa, <code>assoc_rewrite</code>! I need this more than you can possibly imagine.<br>
How hard do you think it would be to make this work with category-style associativity, where the composition operator is indexed on the source and target types? I haven't looked at the implementation yet. I can probably rig up a representative example at some point if that would be helpful.</p>

#### [ Reid Barton (Jul 30 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130583893):
<p>I imagine it could involve internally needing a "thrist" rather than just a list, though maybe you can just ignore the type indices.</p>

#### [ Reid Barton (Jul 30 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130584175):
<p>Checking that a diagram in a category commutes usually comes down to these alternately reassociating and then rewriting arguments and when there are more than three morphisms involved it's a real pain to specify the reassociation you want.</p>

#### [ Simon Hudon (Jul 30 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130584182):
<p>That is very good to know! I can consider categories. I don't think it would be too hard. Given a categorical composition operator, is there an analogue to <code>is_associative</code> to get me the associativity law?</p>

#### [ Reid Barton (Jul 30 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130584248):
<p>It's just a constant--a class method of <code>category</code> (<code>category.associativity</code>)</p>

#### [ Simon Hudon (Jul 30 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130584291):
<p>Cool :) can you give me a proof example? I'll see if I can add it to my PR</p>

#### [ Reid Barton (Jul 30 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130584408):
<p>That is, my compositions are already written syntactically in terms of the fixed composition operator <code>category.compose</code>.</p>

#### [ Reid Barton (Jul 30 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130584418):
<p>Well, hmm. It might be a bit tricky, since categories are not in mathlib yet.</p>

#### [ Reid Barton (Jul 30 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130584559):
<p>I guess I'll give you a self-contained example, including the <code>category</code> class, for starters.</p>

#### [ Simon Hudon (Jul 30 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130584560):
<p>Yeah, that's tricky. Are you working on a branch of mathlib? If so I could make a version for that. Alternatively, I could make a <code>associativity</code> attribute that you can put on that associativity law.</p>

#### [ Simon Hudon (Jul 30 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130584575):
<p>That's a good start.</p>

#### [ Reid Barton (Jul 30 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130585073):
<p>Here is a simple, but very common sort of example: <a href="https://gist.github.com/rwbarton/b10c0229be25bd6880661afb2f1b32f5" target="_blank" title="https://gist.github.com/rwbarton/b10c0229be25bd6880661afb2f1b32f5">https://gist.github.com/rwbarton/b10c0229be25bd6880661afb2f1b32f5</a></p>

#### [ Reid Barton (Jul 30 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130585145):
<p>An <code>associativity</code> attribute would be a good solution for me.</p>

#### [ Simon Hudon (Jul 30 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130585592):
<p>Cool! Thanks! With the associativity attribute, it would probably be enough to put it on the associativity law from <code>semigroup</code> and <code>add_semigroup</code> and <code>semi_lattice</code>, what do you think?</p>

#### [ Simon Hudon (Jul 30 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130585718):
<p>From an aesthetic perspective, if you use <code>x*y = a*b</code> to rewrite <code>p * x * y * q</code>, do you prefer the tactic to leave the expression flat (i.e. <code>p * a * b * q</code>) or manipulated only minimally after rewrite (i.e. <code>p * (a * b) * q</code>)?</p>

#### [ Reid Barton (Jul 30 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130585914):
<p>If using an attribute is faster than instance lookup then that sounds like a good approach, since users can mark their own operations with the attribute anyways. I doubt we need the Prolog-style search power here. (I'm also wondering why instance synthesis is so slow, though.)</p>

#### [ Reid Barton (Jul 30 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130585956):
<p>Good question. Probably I can answer it better after trying it out in a few dozen proofs <span class="emoji emoji-1f642" title="slight smile">:slight_smile:</span></p>

#### [ Simon Hudon (Jul 30 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586040):
<p>What I'm suspecting that there are some dead alleys in the set of instances. Maybe I should start tracing the instance search process</p>

#### [ Reid Barton (Jul 30 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586042):
<p>I think it usually won't matter for me, since I'd probably follow it with either more <code>assoc_rw</code>s or <code>simp</code>, which applies <code>associativity</code> everywhere anyways.</p>

#### [ Simon Hudon (Jul 30 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586094):
<p>If you follow with <code>simp</code>, it might be more effective to flatten the expression so that <code>simp</code> doesn't waste time flattening it one associativity at a time.</p>

#### [ Reid Barton (Jul 30 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586197):
<p>BTW, when do I get <code>assoc_simp</code>? :)</p>

#### [ Simon Hudon (Jul 30 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586278):
<p>On Christmas if you've been a good boy ;-)</p>

#### [ Simon Hudon (Jul 30 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586328):
<p>Actually, I'd like to tackle <code>simp</code> as well but it seems like a bigger project.</p>

#### [ Simon Hudon (Jul 30 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586349):
<p>I'll keep you posted</p>

#### [ Reid Barton (Jul 30 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586357):
<p>I have a way to deal with associativity in <code>simp</code> to some degree already, so it's not so bad. Actually it's stolen from <span class="user-mention" data-user-id="110087">@Scott Morrison</span>'s idea here: <a href="https://github.com/semorrison/lean-category-theory-pr/blob/lean-3.4.1/src/categories/isomorphism.lean#L34" target="_blank" title="https://github.com/semorrison/lean-category-theory-pr/blob/lean-3.4.1/src/categories/isomorphism.lean#L34">https://github.com/semorrison/lean-category-theory-pr/blob/lean-3.4.1/src/categories/isomorphism.lean#L34</a></p>

#### [ Reid Barton (Jul 30 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586402):
<p>The general form is: if you have a <code>@[simp]</code> lemma which states that <code>a * b = c * d * e</code>, first generalize it to the form <code>z * (a * b) = z * (c * d * e)</code>, and then reassociate the parentheses on the left side (there can be more than two original factors).</p>

#### [ Reid Barton (Jul 30 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586465):
<p>Make that another simp lemma. Then you have a left-hand side of the form <code>(z * a) * b = ...</code> where <code>z</code> can be anything. So it will match any left-nested tree in which <code>a</code> and <code>b</code> appear "consecutively".</p>

#### [ Reid Barton (Jul 30 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586492):
<p>(You can reassociate the parentheses on the right-hand side too, so that <code>simp</code> doesn't have to do it every time you apply the lemma.)</p>

#### [ Reid Barton (Jul 30 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586662):
<p>This is like a Knuth-Bendix completion step: we could simplify <code>z * (a * b)</code> to either <code>z * (c * d * e)</code> or <code>(z * a) * b</code>, so add another rewrite rule to make those confluent.</p>

#### [ Reid Barton (Jul 30 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586765):
<p>So one wishlist item is an tactic/attribute to put on a simp lemma which will apply this transformation and make a new simp lemma.</p>

#### [ Reid Barton (Jul 30 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586779):
<p>I've done this by hand in a few cases, and it simplified some proofs.</p>

#### [ Reid Barton (Jul 30 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586917):
<p>But this is not by itself sufficient to deal with situations where we want to use hypotheses, rather than simp lemmas, like the equation <code>e</code> in my example earlier. That's why I still want <code>assoc_rw</code> for this situation. (Maybe an alternative is to generate a transformed version of the hypotheses, but I might also want to rewrite using equations tucked away inside fields of structures and things like that.)</p>

#### [ Simon Hudon (Jul 30 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586920):
<p>Ah I see! So <code>assoc_simp</code> would be better still I assume because then you wouldn't need to duplicate so many lemmas</p>

#### [ Reid Barton (Jul 30 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130587032):
<p>Right, I mean in general <code>rw</code> and <code>simp</code> are distinct, but overlapping in their uses, so both <code>assoc_rw</code> and <code>assoc_simp</code> ought to be useful as well.</p>

#### [ Reid Barton (Jul 30 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130587101):
<p>Maybe <code>assoc_simp</code> with arguments could apply this transformation to those arguments, as well as all simp lemmas</p>

#### [ Simon Hudon (Jul 30 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130587366):
<p>I was thinking of rewriting the <code>simp</code> tactic and changing the rewriting function so that it matches modulo associativity.</p>

#### [ Reid Barton (Jul 30 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130587508):
<p>Ah, I see. Sounds more ambitious, but probably more powerful as well.<br>
Is <code>simp</code> in Lean? Maybe worth waiting for Lean 4?</p>

#### [ Simon Hudon (Jul 30 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130587539):
<p>Where it gets tricky I find is when you have a lemma <code>forall x, x * y = foo</code>, you may instantiate <code>x</code> with <code>a * b</code> which is harder for my current matching to consider.</p>

#### [ Simon Hudon (Jul 30 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130587627):
<blockquote>
<p>Ah, I see. Sounds more ambitious, but probably more powerful as well.<br>
Is <code>simp</code> in Lean? Maybe worth waiting for Lean 4?</p>
</blockquote>
<p>It might be. In any case, maybe I should first roll out <code>assoc_rw</code> and wait for feedback before getting started on <code>assoc_simp</code></p>

#### [ Simon Hudon (Jul 30 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130589220):
<p>I think the category theory development looks beautiful, by the way. I wish I understood more of it</p>

#### [ Scott Morrison (Jul 31 2018 at 04:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130616056):
<p>On the subject of associativity, there is something I would like to work on soon, but that I think it still orthogonal to <code>rw_assoc</code> and <code>simp_assoc</code>.</p>

#### [ Scott Morrison (Jul 31 2018 at 04:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130616067):
<p>When working with monoidal categories, very often one has to insert associators (which are isomorphisms, not equations!) in order to be able to compose.</p>

#### [ Scott Morrison (Jul 31 2018 at 04:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130616356):
<p>For example, if I have <code>f : A -&gt; (B ⊗ C) ⊗ D</code> and <code>g : B ⊗ (C ⊗ D) -&gt; E</code>, of course <code>f  ≫ g</code> doesn't typecheck.</p>

#### [ Scott Morrison (Jul 31 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130616450):
<p>I would like to define some extra notation, e.g. <code>f ⊗≫ g</code>, which would invoke a tactic that inspects the target of <code>f</code> and the source of <code>g</code>, and decides if they are isomorphic via associator isomorphisms (probably also via identity isomorphisms, absorbing the monoidal unit on either side), and if so contructs that isomorphism <code>α</code> and returns <code>f ≫ α ≫ g </code>.</p>

#### [ Scott Morrison (Jul 31 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130616499):
<p>(By the axioms for monoidal categories, it doesn't matter _which_ associator isomorphism we use, as they are all equal.)</p>

#### [ Simon Hudon (Jul 31 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130619435):
<p>should there be an arrow in the type of <code>g</code>?</p>

#### [ Simon Hudon (Jul 31 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130619565):
<p>I think I see where you're going for. Similar logic to my <code>assoc_rw</code> tactic can be used to construct <code>α</code></p>

#### [ Simon Hudon (Jul 31 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620191):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> applying <code>assoc_rw</code> to categories is more complicated than I thought. It might be that I should just write a <code>cat_rw</code> specifically for categories. Is there any other context in which such a tactic would be useful or would it make sense to just refer to composition from <code>category</code>?</p>

#### [ Mario Carneiro (Jul 31 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620280):
<p>a semigroupoid? :D</p>

#### [ Simon Hudon (Jul 31 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620518):
<p>:) Shouldn't that be an ancestor of category?</p>

#### [ Simon Hudon (Jul 31 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620524):
<p>I could hard-code semigroupoid composition instead of category composition, no?</p>

#### [ Scott Morrison (Jul 31 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620591):
<p>I've heard the word <code>semicategory</code>, and there's actually some natural reasons to study them.</p>

#### [ Scott Morrison (Jul 31 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620598):
<p>(Idempotent completion takes semicategories to categories, and in a certain sense is adjoint to the functor which forgets identities)</p>

#### [ Simon Hudon (Jul 31 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620696):
<p>Would it be worth introducing a <code>has_comp</code> type class?</p>

#### [ Simon Hudon (Jul 31 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620815):
<p>(I assume semicategories have an associative composition)</p>

#### [ Mario Carneiro (Jul 31 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620826):
<p>I'm joking. I prefer to introduce concepts when they become useful and not before</p>

#### [ Mario Carneiro (Jul 31 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620866):
<p>it's not hard to retrofit them if some time in the future we see a genuine semigroupoid which is not a category</p>

#### [ Simon Hudon (Jul 31 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620877):
<p>Fair enough :) my sense of usefulness for category theory still needs sharpening</p>

#### [ Simon Hudon (Jul 31 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620944):
<p>While we wait for the category theory stuff to be merged, would it be worth it to add <code>has_comp</code> to mathlib if I can use it in <code>assoc_rw</code>? That might facilitate the development of the category theory proofs.</p>

#### [ Mario Carneiro (Jul 31 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130621378):
<p>that sounds like it would be tied to a notation, but probably <code>assoc_rw</code> will need to be usable with at least a few notations, in particular <code>+</code>, <code>*</code>, and <code>o</code></p>

#### [ Simon Hudon (Jul 31 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130621439):
<p>What I'm thinking is for operators with simpler types (e.g. <code>+</code>, <code>*</code>) I can rely on <code>is_associative</code> and then make a special case for categorical composition. The matching is a bit different anyway</p>

#### [ Mario Carneiro (Jul 31 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130622261):
<p>that sounds reasonable. I doubt categorical composition will use any other notation than whatever Scott is setting up</p>

#### [ Patrick Massot (Jul 31 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130633467):
<p>I also have something like Scott's associators everywhere in my group completion work. For every uniform space <code>a</code>, I have a complete Hausdorff <code>completion a</code> and a map from <code>a</code> to <code>completion a</code>, and every uniformly continuous map from <code>a</code> to <code>b</code> lifts to a map between completions. This is all fun. The trouble comes when product spaces are involved. I have an isomorphism from <code>completion (a × b)</code> to<code>completion a × completion  b</code>, but I need to insert it and its inverse at a lot of places.</p>

#### [ Reid Barton (Jul 31 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130654032):
<blockquote>
<p>Would it be worth introducing a <code>has_comp</code> type class?</p>
</blockquote>
<p>Hmm, I wonder if moving <code>∘</code> to notation for a <code>has_comp</code> class would be viable, with an instance for <code>function.comp</code>... though I guess that is all in core Lean, so not viable at the moment.</p>

#### [ Kevin Buzzard (Jul 31 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130654630):
<p>Although this is even less under our control, is the correct long-term solution really to try and rethink how the actual type class system works? Or is the type class system some sort of standard machine which clearly will never change and we have to figure out how to work around it?</p>

#### [ Johannes Hölzl (Jul 31 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130662971):
<p>The mechanism will not change, at least there are no public plans for Lean 4 to change the type class mechanism. What will change, is the type class hierarchy. One thing is to move properties like commutativity, or <code>zero_ne_one</code> to be type class <em>mixins</em>, i.e. predicates over other type classes. <code>[comm_ring A]</code> will become <code>[ring A] [is_commutative A (*)]</code> (or similar). Also the lower type classes in the hierarcht like semigroups, monoid, etc, will be parameterized in their operators. This could eliminate parts of the additive / multiplicative split of the type class hierarchy.</p>

#### [ Johan Commelin (Aug 01 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130704179):
<p>Concerning Lean 4: in what time scales should I think about the release? 3 weeks, 3 months, 3 years, 3 decades? Is there any hope/expectation/statement about this?</p>

#### [ Kevin Buzzard (Aug 01 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130704197):
<p>"Not before the end of 2018" said Leo in Oxford IIRC</p>

#### [ Kevin Buzzard (Aug 01 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130704200):
<p>Maybe some of my students with better memories than me can confirm this</p>

#### [ Johan Commelin (Aug 01 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130704286):
<p>Ok. I didn't know anything at all. So if people said we would have to wait till at least 2025, I wouldn't have been surprised either.</p>

#### [ Reid Barton (Aug 01 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130731512):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> was there a question here left over from yesterday?<br>
There isn't currently anything which generalizes <code>category.compose</code> nor any concrete plans to add such a thing.<br>
I assume it would be easy to change <code>assoc_rw</code> later if this changes, anyways.</p>

#### [ Reid Barton (Aug 01 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130731684):
<p>By the way how do you feel about the name <code>rw_assoc</code> (and potentially <code>simp_assoc</code>) instead? Potentially more discoverable by autocompletion, for one</p>

#### [ Simon Hudon (Aug 01 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130733107):
<p>Yes you're right. The other thing that such a generalization helps with is separating the category code  from the code of <code>assoc_rw</code></p>

#### [ Simon Hudon (Aug 01 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130733213):
<p>I chose <code>assoc_rw</code> to conform with <code>ac_refl</code>. I think I could be convinced in favor of <code>rw_assoc</code></p>


{% endraw %}
