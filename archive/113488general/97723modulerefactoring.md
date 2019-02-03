---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/97723modulerefactoring.html
---

## Stream: [general](index.html)
### Topic: [module refactoring](97723modulerefactoring.html)

---


{% raw %}
#### [ Mario Carneiro (Sep 21 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134359525):
<p>I'm a bit late for my birthday deadline, but I have enough of the refactoring done that I'm ready to get feedback on it. See <a href="https://github.com/leanprover/mathlib/compare/master...leanprover-community:module" target="_blank" title="https://github.com/leanprover/mathlib/compare/master...leanprover-community:module">leanprover-community/module</a>. Remarks:</p>
<ul>
<li>The main contributions here are the complete bundling of <code>linear_map</code> and <code>submodule</code>. In fact both of these were already present in mathlib, but making them primary makes everything go so much smoother.</li>
<li>The structure of <code>submodule</code> and its category-theory-like interactions with <code>linear_map</code> are emphasized heavily. In particular, <code>submodule</code> is a complete lattice, <code>map</code> and <code>comap</code> are galois connections, there are tons of theorems about the map of an inf or the comap of fst and so on.</li>
<li>The amount of duality here is staggering. I guess someone who is category theory minded will tell me that Mod is its own opposite category or some such thing, but it really shows in the equational theory. Even stuff like <code>inl</code> being dual to <code>fst</code> causes some nice properties, and some stuff plays even nicer than on Set like <code>prod p q ⊔ prod p' q' = prod (p ⊔ p') (q ⊔ q')</code>.</li>
<li>Injectivity and surjectivity of linear maps is expressed through <code>ker</code> and <code>range</code> (should I call it <code>im</code>?), and even <code>linear_independent</code> and <code>basis</code> can be expressed using properties of the <code>lc.total</code> function.</li>
</ul>
<p>On the whole, I'm feeling really good about the results, and the proofs are much cleaner.</p>

#### [ Johan Commelin (Sep 21 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134359600):
<p>This is really cool! And yes, please call use <code>im</code> <span class="emoji emoji-1f606" title="lol">:lol:</span></p>

#### [ Mario Carneiro (Sep 21 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134359655):
<p>The name <code>range</code> is of course borrowed from terminology on <code>set</code>. I would rather not confuse with <code>image</code> which is <code>map</code> here</p>

#### [ Mario Carneiro (Sep 21 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134359741):
<p><code>map f p</code> is the submodule <code>f[p]</code> where <code>p</code> is a submodule, and <code>range f = map f \top = f[univ]</code> which was previously called <code>im</code> on linear maps</p>

#### [ Mario Carneiro (Sep 21 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134359814):
<p>What is the common name for the coproduct pairing function? I called it <a href="https://github.com/leanprover-community/mathlib/blob/45f72059515083a0ae74567432dfc7853f791235/linear_algebra/basic.lean#L113-L114" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/45f72059515083a0ae74567432dfc7853f791235/linear_algebra/basic.lean#L113-L114"><code>copair</code></a> since <code>pair</code> is used for the product pairing operation</p>

#### [ Kenny Lau (Sep 21 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134360028):
<p>but it's the same...</p>

#### [ Johan Commelin (Sep 21 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134360049):
<p>I think <span class="user-mention" data-user-id="110087">@Scott Morrison</span>  and <span class="user-mention" data-user-id="110032">@Reid Barton</span> have the most experience with such decisions</p>

#### [ Johannes Hölzl (Sep 21 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134363426):
<p>this is really nice!</p>

#### [ Patrick Massot (Sep 21 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134364133):
<p>Mario, could you explain how all this solves the trouble we had with instance loops and multiple possible base rings?</p>

#### [ Kevin Buzzard (Sep 21 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134370222):
<p>I got caught up with something else this morning but later on today, when I have Lean time, I will just merge the patch and see how Hilbert basis goes with it. Does it compile sorry-free?</p>

#### [ Reid Barton (Sep 21 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134370418):
<p><code>copair</code>/<code>pair</code> seems as good as anything else.<br>
Normally we just write an arrow <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi><mo>⊕</mo><mi>B</mi><mo>→</mo><mi>C</mi></mrow><annotation encoding="application/x-tex">A \oplus B \to C</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.76666em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord mathit">A</span><span class="mbin">⊕</span><span class="mord mathit" style="margin-right:0.05017em;">B</span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.07153em;">C</span></span></span></span> and let the reader do the boring work of figuring out what map we are actually talking about.</p>

#### [ Kenny Lau (Sep 21 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134370446):
<p>how about product or coproduct as a bifunctor?</p>

#### [ Mario Carneiro (Sep 21 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134388143):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>  This doesn't address that issue, although it prepares the way a bit. I anticipate that this should be a comparatively simple change, but I didn't want the two refactorings to interact so I'm going to start on it as soon as this is done.</p>

#### [ Mario Carneiro (Sep 21 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134388211):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> It's not yet building. I finished the main linear algebra files, but I haven't finished up the cleanup of uses outside linear algebra. (There are no sorries, it just breaks.)</p>

#### [ Johannes Hölzl (Sep 21 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134388442):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> by the way: the introduction of <code>coe</code> rewrites broke some proofs in <code>set_theory/ordinal</code> and <code>cofinality</code>. I fixed this, but you might want to do a different fix</p>

#### [ Mario Carneiro (Sep 21 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134389089):
<p>yeah, apologies for pushing stuff last night that broke things; my computer was running very slow and I was lacking feedback on whether my fixes worked</p>

#### [ Johannes Hölzl (Sep 21 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134389417):
<p>No problem. But I'm not sure if these are the intended changes. I didn't look too deep how these new simp rules are supposed to work.</p>

#### [ Mario Carneiro (Sep 21 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134389493):
<p>The idea is that <code>coe</code> will infer transitive instances, but since simp rules are only written on single coercions they won't fire on these composite instances. So we unfold them to multiple coe arrows first</p>

#### [ Mario Carneiro (Sep 21 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134389521):
<p>I don't think I realized this until lately, but lean will also infer transitive instances for <code>coe</code> + <code>coe_fn</code> and <code>coe</code> + <code>coe_sort</code>, and since the instances are different there are more simp lemmas associated to these</p>

#### [ Mario Carneiro (Sep 21 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134389602):
<p>I think the breakage is because some simp LHSs were written with composite instances, which now break because simp normal form doesn't have any composite instances. The fix is to make sure simp LHSs have multiple coercion in these cases</p>

#### [ Patrick Massot (Sep 21 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134390066):
<p>Ok, I'm less confused then (about modules, I'm still 100% confused about topological groups). I couldn't understand how those changes could help with the lost ring issue</p>

#### [ Chris Hughes (Sep 21 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134390560):
<p>Is it worth bundling ideals and subgroups as well?</p>

#### [ Johannes Hölzl (Sep 21 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134391051):
<p>I think we should replace ideals by submodules, so yes we want to have them bundled. I'm not sure about subgroups. We surely want a bundled version, but maybe still an unbundled one too</p>

#### [ Kevin Buzzard (Sep 21 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134392526):
<p>Johannes -- the idea about ideals was that submodule R M makes sense for varying R and M, but ideal R = submodule R R so only one input is needed.</p>

#### [ Chris Hughes (Sep 21 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134392890):
<p>But I think you want lattice and semiring on ideals as well, so you need bundles for that.</p>

#### [ Mario Carneiro (Sep 21 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134396604):
<p>I am of the opinion that <code>subgroup</code> and other such algebraic classes should also be bundled; almost all of the lattice structure theorems done here hold for anything that fits the structure of a universal algebra. <code>ideal R := submodule R R</code> can be defined as reducible so that all the theorems about submodules still apply.</p>

#### [ Mario Carneiro (Sep 21 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134396657):
<p>What are some examples where you think not having <code>is_sub*</code> will cause problems?</p>

#### [ Johan Commelin (Sep 21 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134403252):
<blockquote>
<p><code>ideal R := submodule R R</code> can be defined as reducible so that all the theorems about submodules still apply.</p>
</blockquote>
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>  I thought you said in Orsay that you couldn't think of any reason why a definition should be reducible. Has that changed? If so, can you explain?</p>

#### [ Kevin Buzzard (Sep 22 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134412301):
<p>If I open polynomial.lean (which I need for Hilbert basis) I just get 1000 errors. I think I would be happier to give feedback by trying to write Lean code and then getting stuck or finding things easier than before and reporting back. I find it hard to theorise about changes that I may not fully understand.</p>

#### [ Mario Carneiro (Sep 22 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134414013):
<p>Yeah, sorry about that. Mostly you can just open and read <code>algebra.module</code> and <code>linear_algebra.basic</code> for now. I'll let you know when it's really done (by pushing it to <code>master</code>, unless someone objects)</p>

#### [ Mario Carneiro (Sep 22 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134414027):
<p>I just didn't want to get too far afield with a change this sweeping without some input</p>

#### [ Mario Carneiro (Sep 22 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134414217):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> That's a fair point. There are three options here: (1) nonreducible def (2) reducible def (3) notation. In Orsay I argued that either (1) or (3) suffices in most cases where you think you want (2).</p>
<p>In this case, I don't think it matters too much, although (1) will require copying some instances like the <code>complete_lattice</code> instance, and possibly some theorems. Doing this would make the cleanest separation, allowing us to present a solid API for ideals that doesn't talk about modules half the time. (2) and (3) will entail some amount of API leakage here, moreso with (3) since it is <code>submodule R R</code> that will appear in all your statements. </p>
<p>The downsides of reducible defs (inconsistent handling in rw and simp) don't really apply when the def is a type since you don't usually do rewrites on a type, you just force it to be defeq to something else.</p>

#### [ Mario Carneiro (Sep 28 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134781266):
<p>This is a change I haven't implemented, but I'm considering it and want to get some feedback. Maybe a basis should be an injective function from some type into the module, i.e. the "basis" is really the range of this function, and the function gets to pick its indexing type. The reason is because we often tend to use a basis as an index for a sum, or as the domain of the free vector space to which to express isomorphism, or as the set whose cardinality is the dimension of the space - all of these roles are better accommodated by having an algebra of indexing types (which we already have courtesy of DTT) where measuring cardinality and indexing is more natural. (Also, it allows a basis to carry computational content, which isn't super important but indicates that this might be moving in the right direction.)</p>

#### [ Reid Barton (Sep 28 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134781707):
<p>From a mathematical perspective this change is very natural. We often write things like "let {b_1, ..., b_n} be a basis of V" but usually (whether we are aware of it or not) we really mean we are working with an indexed collection b_i, i.e., a function {1, ..., n} -&gt; V.</p>

#### [ Reid Barton (Sep 28 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134781777):
<p>It's easy to say things which are false if taken literally in the "set style". For example: {x, y} is a linearly independent set in a vector space if and only if there do not exist nonzero a, b such that ax + by = 0. Well, not if x = y!</p>

#### [ Reid Barton (Sep 28 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134781792):
<p>On the other hand there are occasionally times when you genuinely need to work with subsets because you want to use the order structure and/or know that the collection of all possible bases is small, for example when proving that every vector space has a basis</p>

#### [ Mario Carneiro (Sep 28 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134781797):
<p>I think the statement about every vector space has a basis will explicitly use subsets</p>

#### [ Reid Barton (Sep 28 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134781842):
<p>I think the function approach is not really restrictive then anyways. You just say "a subset such that the inclusion is a basis".</p>

#### [ Mario Carneiro (Sep 28 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134781853):
<p>i.e. every vector space has a basis where the function is the subtype coercion and the indexing set is a subtype of the vector space</p>

#### [ Reid Barton (Sep 28 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134781855):
<p>(By the way, injectivity of the function is a consequence of being a basis, not a precondition.)</p>

#### [ Mario Carneiro (Sep 28 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134781869):
<p>I agree, I think under most circumstances you should be able to prove injectivity, except in trivial cases and in those cases you probably don't want to impose it additionally</p>

#### [ Mario Carneiro (Sep 28 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134781913):
<p>(bases over the zero ring are weird)</p>

#### [ Reid Barton (Sep 28 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134781932):
<p>Hmm... yes</p>

#### [ Mario Carneiro (Sep 28 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134781956):
<p>speaking of which... <code>unit</code> should be a ring</p>

#### [ Mario Carneiro (Sep 28 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134781998):
<p>it would fit nicely with the ring instance for products and Pis</p>

#### [ Reid Barton (Sep 28 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134782068):
<p>The nlab definition of basis is: A basis of a free R-module M (possibly a vector space, see basis of a vector space) is a linear isomorphism <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>B</mi><mo separator="true">:</mo><mi>M</mi><mo>→</mo><msub><mo>⊕</mo><mrow><mi>i</mi><mo>∈</mo><mi>I</mi></mrow></msub><mi>R</mi></mrow><annotation encoding="application/x-tex">B\colon M \to \oplus_{i\in I}R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.8607em;vertical-align:-0.17737em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05017em;">B</span><span class="mpunct">:</span><span class="mord mathit" style="margin-right:0.10903em;">M</span><span class="mrel">→</span><span class="mord"><span class="mbin">⊕</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mrel mtight">∈</span><span class="mord mathit mtight" style="margin-right:0.07847em;">I</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.17737em;"></span></span></span></span></span><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span> to a direct sum of copies of the ring R, regarded as a module over itself.</p>

#### [ Reid Barton (Sep 28 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134782086):
<p>I think this kind of property is more important than "for all i /= j, b_i /= b_j"</p>

#### [ Reid Barton (Sep 28 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134782104):
<p>... if you find yourself having to make some decision regarding the zero ring</p>

#### [ Reid Barton (Sep 28 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134782355):
<p>Yes okay, now I see you were saying the same thing regarding definition of bases over the zero ring</p>

#### [ Mario Carneiro (Sep 28 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134783593):
<p>so what does this say about linearly independent sets?</p>

#### [ Mario Carneiro (Sep 28 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134783641):
<p>I guess these should also be indexed</p>

#### [ Johan Commelin (Sep 28 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134785061):
<blockquote>
<p>speaking of which... <code>unit</code> should be a ring</p>
</blockquote>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="n">unit</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">tidy</span>
</pre></div>

#### [ Johan Commelin (Sep 28 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134785183):
<p>Good luck golfing that...</p>

#### [ Johan Commelin (Sep 28 2018 at 03:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134785315):
<p>I'm pretty sure that <code>tidy</code> will also prove for you that it is the terminal object in <code>Ring</code> and <code>CRing</code></p>

#### [ Kevin Buzzard (Sep 28 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/134807675):
<p>I must confess I was surprised when I first saw that in Lean a basis was a subset. Mulling over this, I realised that it was because I was used to teaching students about bases of <em>finite-dimensional</em> vector spaces -- and this is not a conversation about bases, this is also a conversation about the concepts of linear independence and spanning -- and in these cases it seems more convenient when developing the theory to be considering lists of elements rather than subsets (so order matters, and repeats are OK). For a dumb example, consider the zero ring <code>R</code>. Then <code>R^3=R</code> and hence I want <code>[0,0,0]</code> to be a basis for <code>R</code>, which it is. This is the only case where bases can have repeated elements and also the only case where bases can have different cardinalities. A less pathological example is that if a basis of a fdvs is a list then a linear map is a matrix, rather than some weird concept of a matrix where we don't mind permuting the rows and columns which we'd get for sets. My students did a bunch of stuff involving this over the summer -- linear maps = matrices and so on -- and although their code is probably not mathlib-ready it would not surprise me if they had worked out some good useful and correct statements.</p>
<p>The only situation I know where subsets are better than maps from a type is in the Zorn proof that every vector space has a basis. But this result is in some sense a bit of a novelty, my impression is that working mathematicians very rarely think about infinite-dimensional vector spaces with no extra structure at all, and if there is extra structure (a topology or whatever) then the abstract notion of a basis is usually not what we want anyway (c.f. "basis" of a Hilbert space = lin ind subset with dense span).</p>

#### [ Johan Commelin (Oct 04 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135187101):
<p>If we are refactoring modules... would it make sense to rename <code>span</code> to <code>generate</code>? It would be more in line with all the other forms of <code>generate</code>...</p>

#### [ Mario Carneiro (Oct 04 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135193289):
<p>I was actually thinking about going the other way :)</p>

#### [ Mario Carneiro (Oct 04 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135193368):
<p>specifically as relates to other "closure" operations e.g. subgroup closure and normal closure</p>

#### [ Mario Carneiro (Oct 04 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135193424):
<p>For set-of-set operations like <code>filter</code> and <code>topology</code> I prefer <code>generate</code>, but maybe that's not principled enough</p>

#### [ Mario Carneiro (Oct 04 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135193452):
<p>I agree some uniformity of naming would be a good thing</p>

#### [ Johan Commelin (Oct 04 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135193845):
<p>Ok, I don't really care which one gets chosen <span class="emoji emoji-1f606" title="lol">:lol:</span></p>

#### [ Mario Carneiro (Oct 08 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135377864):
<p>So I've got to working on <code>ideal</code> now, and I have come to realize that ideal theory is not simply a specialization of submodule theory. It's obvious in hindsight, but as a category the homs are different - a ring hom is not a linear map, and a linear map is not a ring hom</p>

#### [ Mario Carneiro (Oct 08 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135377912):
<p>So this means that things like <code>map</code> and <code>comap</code> don't work the same way on rings</p>

#### [ Mario Carneiro (Oct 08 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135377924):
<p>In particular I don't even think there is a notion of <code>ideal.map</code> unless you assume the map is surjective</p>

#### [ Mario Carneiro (Oct 08 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135378146):
<p>Is there a way to make sense of a ring-changing hom from (R,M) to (R',M') modules?</p>

#### [ Scott Morrison (Oct 08 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135378473):
<p>Perhaps there's a notion of a map (R,M) to (R',M') as a linear map f : M to M', and a ring hom g : R' to R (note this is backwards), satisfying g(r') m = r' f(m).</p>

#### [ Scott Morrison (Oct 08 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135378476):
<p>I'm not sure it's particularly useful.</p>

#### [ Mario Carneiro (Oct 08 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135378488):
<p>yeah I was thinking the ring part might end up contravariant</p>

#### [ Mario Carneiro (Oct 08 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135378490):
<p>so I guess this does not generalize ring homs as maps (R,R) -&gt; (R', R')</p>

#### [ Johan Commelin (Oct 08 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135378925):
<blockquote>
<p>Is there a way to make sense of a ring-changing hom from (R,M) to (R',M') modules?</p>
</blockquote>
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> What exactly do you mean with this question?</p>

#### [ Mario Carneiro (Oct 08 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135378968):
<p>I wonder if there is a common generalization of ring homs, (R,R) -&gt; (R', R') and linear maps (R,M) -&gt; (R, M')</p>

#### [ Mario Carneiro (Oct 08 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135378976):
<p>is there a category theory operation for taking a "total space" over the categories R-Mod where R is an object in the category Ring?</p>

#### [ Johan Commelin (Oct 08 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135378980):
<p>Sure.</p>

#### [ Johan Commelin (Oct 08 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135378985):
<p>That's a fibered category</p>

#### [ Johan Commelin (Oct 08 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135378994):
<p>And this one is one of the first examples</p>

#### [ Johan Commelin (Oct 08 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379047):
<p>A map <code>(R,M) → (R',M')</code> is a pair <code>R → R'</code> + <code>R' \otimes_R M → M'</code>. (Or do I need commutativity for that tensor product?)</p>

#### [ Johan Commelin (Oct 08 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379051):
<p>Yes, I do.</p>

#### [ Johan Commelin (Oct 08 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379052):
<p>This doesn't work for arbitrary <code>R → R'</code>.</p>

#### [ Johan Commelin (Oct 08 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379094):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Were you planning on doing left- right- and two-sided-ideals?</p>

#### [ Johan Commelin (Oct 08 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379097):
<p>Or only ideals in comm_rings?</p>

#### [ Mario Carneiro (Oct 08 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379102):
<p>Just comm ring ideals, since that's what's there now</p>

#### [ Johan Commelin (Oct 08 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379107):
<p>Ok, so for comm_ring modules you get this really nice fibered category <code>Mod</code>.</p>

#### [ Johan Commelin (Oct 08 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379109):
<p>Is that what you were looking for?</p>

#### [ Johan Commelin (Oct 08 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379113):
<p>Note that by adjunction you can also just give a map <code>M → M'</code> that is <code>R</code>-linear</p>

#### [ Mario Carneiro (Oct 08 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379128):
<blockquote>
<p><code>R' \otimes_R M</code></p>
</blockquote>
<p>what is this</p>

#### [ Johan Commelin (Oct 08 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379153):
<p>Tensor product</p>

#### [ Johan Commelin (Oct 08 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379154):
<p>turning <code>M</code> into an <code>R'</code>-module</p>

#### [ Mario Carneiro (Oct 08 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379155):
<p>so R' is viewed as a R-module here?</p>

#### [ Johan Commelin (Oct 08 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379156):
<p>Yes</p>

#### [ Mario Carneiro (Oct 08 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379164):
<p>oh, there's an interesting construction we don't have</p>

#### [ Johan Commelin (Oct 08 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379166):
<p>Which one?</p>

#### [ Mario Carneiro (Oct 08 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379169):
<p>a ring hom <code>R -&gt; R'</code> yields a R-module structure on <code>R'</code></p>

#### [ Johan Commelin (Oct 08 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379173):
<p>You mean the forgetful functor?</p>

#### [ Johan Commelin (Oct 08 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379176):
<p>From <code>R'</code>-mod to <code>R</code>-mod?</p>

#### [ Mario Carneiro (Oct 08 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379216):
<p>It's not forgetful, right?</p>

#### [ Johan Commelin (Oct 08 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379218):
<p>Not really</p>

#### [ Mario Carneiro (Oct 08 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379219):
<p>The hom could be anything</p>

#### [ Johan Commelin (Oct 08 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379222):
<p>I still think of it as "forgetting"</p>

#### [ Johan Commelin (Oct 08 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379229):
<p>We have <code>R</code> is an <code>R</code>-mod</p>

#### [ Johan Commelin (Oct 08 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379233):
<p>So if you chain that to the "forget" instance, you have what you want.</p>

#### [ Mario Carneiro (Oct 08 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379239):
<p>I don't follow</p>

#### [ Johan Commelin (Oct 08 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379242):
<p>I tried adding "forget" about 3 months ago, and I ran into trouble.</p>

#### [ Mario Carneiro (Oct 08 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379244):
<p>what forget instance?</p>

#### [ Johan Commelin (Oct 08 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379248):
<p>But maybe with the refactor, you can now do it.</p>

#### [ Johan Commelin (Oct 08 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379249):
<p>I mean <code>R'</code> is an <code>R'</code>-mod + every <code>R'</code>-mod is an <code>R</code>-mod.</p>

#### [ Johan Commelin (Oct 08 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379273):
<p>I want your instance to be broken into 2 steps.</p>

#### [ Johan Commelin (Oct 08 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379301):
<blockquote>
<p>what forget instance?</p>
</blockquote>
<p>The "forgetful" functor instance</p>

#### [ Mario Carneiro (Oct 08 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379302):
<blockquote>
<p>every R'-mod is an R-mod</p>
</blockquote>
<p>This one requires an explicit ring hom input</p>

#### [ Johan Commelin (Oct 08 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379308):
<p>Hmmm, it does... unless we turn <code>R'</code> into an algebra</p>

#### [ Johan Commelin (Oct 08 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379310):
<p>over <code>R</code></p>

#### [ Mario Carneiro (Oct 08 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379318):
<p>ah, we don't have anything like that yet</p>

#### [ Mario Carneiro (Oct 08 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379369):
<p>I needed assoc algebras around this time in metamath, now I forget why</p>

#### [ Mario Carneiro (Oct 08 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379428):
<p>Ah - multivariate polynomials are the free assoc algebra</p>

#### [ Johan Commelin (Oct 08 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379457):
<p>The ones we have are also commutative</p>

#### [ Johan Commelin (Oct 08 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379496):
<p>At some point we might want non-commutative polynomials as well</p>

#### [ Mario Carneiro (Oct 08 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379511):
<p>I have never touched noncomm polynomials, but I guess it's not so hard with the group ring construction</p>

#### [ Mario Carneiro (Oct 08 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379514):
<p>... + free monoid construction which we already have</p>

#### [ Johan Commelin (Oct 08 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379515):
<p>So, could we have <code>f^* M'</code>?</p>

#### [ Mario Carneiro (Oct 08 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379555):
<p>I think so, what does that mean?</p>

#### [ Johan Commelin (Oct 08 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379556):
<p>where <code>f</code> is a ring hom <code>R → R'</code> and <code>M'</code> is an <code>R'</code>-mod</p>

#### [ Johan Commelin (Oct 08 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379559):
<p>So <code>f^*</code> is the functor <code>R'-mod → R-mod</code></p>

#### [ Mario Carneiro (Oct 08 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379565):
<p>ah, okay so this is the contravariant thing that scott mentioned</p>

#### [ Johan Commelin (Oct 08 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379567):
<p>Right, and it is adjoint to tensoring.</p>

#### [ Johan Commelin (Oct 08 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379568):
<p>Which is covariant</p>

#### [ Johan Commelin (Oct 08 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379570):
<p>no, that's bullcrap</p>

#### [ Johan Commelin (Oct 08 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379571):
<p>I'm brainfarting</p>

#### [ Johan Commelin (Oct 08 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379609):
<p>tensor is adjoint to hom</p>

#### [ Johan Commelin (Oct 08 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135379614):
<p>Lol. So you get to choose: either you use <code>f^*</code> which is contravariant. Or you use tensor products, and you get something covariant, but "harder to parse".</p>

#### [ Johan Commelin (Oct 08 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135383276):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> How would all this abstract nonsense help with:</p>
<blockquote>
<p>So I've got to working on <code>ideal</code> now, and I have come to realize that ideal theory is not simply a specialization of submodule theory. It's obvious in hindsight, but as a category the homs are different - a ring hom is not a linear map, and a linear map is not a ring hom</p>
</blockquote>

#### [ Kenny Lau (Oct 08 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135383285):
<p>And nobody here has pointed out that extensions of ideals exist, c.f. Atiyah-Macdonald P.9</p>

#### [ Kenny Lau (Oct 08 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135383328):
<blockquote>
<p>In particular I don't even think there is a notion of <code>ideal.map</code> unless you assume the map is surjective</p>
</blockquote>
<p>if f:A-&gt;B is a ring hom and L is an ideal in A then L^e is the ideal generated by f(L)</p>

#### [ Kenny Lau (Oct 08 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135383339):
<p><a href="/user_uploads/3121/OAIFV_UuuBZXylsyoLFs_sUK/2018-10-08.png" target="_blank" title="2018-10-08.png">2018-10-08.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/OAIFV_UuuBZXylsyoLFs_sUK/2018-10-08.png" target="_blank" title="2018-10-08.png"><img src="/user_uploads/3121/OAIFV_UuuBZXylsyoLFs_sUK/2018-10-08.png"></a></div>

#### [ Mario Carneiro (Oct 08 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135383404):
<p>yeah, okay that's a better idea</p>

#### [ Mario Carneiro (Oct 08 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135383408):
<p>just close the resulting set under ideal operations</p>

#### [ Johan Commelin (Oct 08 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135383456):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Do you have some sort of todo list of what remains for this refactor?</p>

#### [ Mario Carneiro (Oct 08 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135383458):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> It's just some idle speculation on my part, I don't really have any concrete implementation ideas</p>

#### [ Mario Carneiro (Oct 08 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135383464):
<p>I'm currently in "tying up loose ends" mode in the refactor, I don't want to introduce new things</p>

#### [ Johan Commelin (Oct 08 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135383467):
<p>Great!</p>

#### [ Mario Carneiro (Oct 08 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135383470):
<p>it's already behind schedule too much</p>

#### [ Mario Carneiro (Oct 08 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135383513):
<p>although it has made several other projects come to the fore, which I will probably have to start working on after I'm done</p>

#### [ Mario Carneiro (Oct 08 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135383515):
<p>foremost of which is the multiple scalar field thing</p>

#### [ Johan Commelin (Oct 08 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135383519):
<p>After you are done, I think <code>faster</code> should be the first thing on your list. <span class="emoji emoji-1f606" title="lol">:lol:</span></p>

#### [ Mario Carneiro (Oct 08 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135383522):
<p>I'm actually working on that ATM</p>

#### [ Johan Commelin (Oct 08 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135383525):
<p>Wonderful! Thanks for doing that!</p>

#### [ Kevin Buzzard (Oct 08 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135384515):
<p>Here are some thoughts. The fundamental notion in algebraic geometry is an "f-map" -- see 6.21.7 in <a href="https://stacks.math.columbia.edu/tag/008C" target="_blank" title="https://stacks.math.columbia.edu/tag/008C">the stacks project</a>. Lemma 6.21.8 shows that this is a natural idea. Although it's dressed up in a geometric language, this is something related to the conversation here. The notion of an f-map shows up in the definition of a morphism of ringed spaces in <a href="https://stacks.math.columbia.edu/tag/0090" target="_blank" title="https://stacks.math.columbia.edu/tag/0090">definition 6.21</a>. In the discussion just below 6.26.3 <a href="https://stacks.math.columbia.edu/tag/0094" target="_blank" title="https://stacks.math.columbia.edu/tag/0094">here</a> we see the notion of an f-map of sheaves of modules. Note in particular in that discussion that the f-maps from G to F are in canonical bijection with two other hom sets, one involving only sheaves on X and one involving only sheaves on Y.</p>
<p>Now of course all this needs a lot of unravelling, and the way to unravel is to ask how what de Jong writes translates into the case of affine schemes, which are just commutative rings in disguise. If I got it right, then he says to focus on the following idea: if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>:</mo><mi>A</mi><mo>→</mo><mi>B</mi></mrow><annotation encoding="application/x-tex">f:A\to B</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mrel">:</span><span class="mord mathit">A</span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span> is a map of rings and if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi></mrow><annotation encoding="application/x-tex">G</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">G</span></span></span></span> is an <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">A</span></span></span></span>-module and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>F</mi></mrow><annotation encoding="application/x-tex">F</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">F</span></span></span></span> a <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>B</mi></mrow><annotation encoding="application/x-tex">B</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span>-module, an <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi></mrow><annotation encoding="application/x-tex">f</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span></span></span></span>-map <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi><mo>→</mo><mi>F</mi></mrow><annotation encoding="application/x-tex">G\to F</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">G</span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.13889em;">F</span></span></span></span> is simply an <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">A</span></span></span></span>-module homomorphism from <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi></mrow><annotation encoding="application/x-tex">G</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">G</span></span></span></span> to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>F</mi></mrow><annotation encoding="application/x-tex">F</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">F</span></span></span></span>, and the observation is that such maps naturally biject with the <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>B</mi></mrow><annotation encoding="application/x-tex">B</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span>-module homomorphisms from <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi><msub><mo>⊗</mo><mi>A</mi></msub><mi>B</mi></mrow><annotation encoding="application/x-tex">G\otimes_AB</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord mathit">G</span><span class="mbin"><span class="mbin">⊗</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">A</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span> to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>F</mi></mrow><annotation encoding="application/x-tex">F</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">F</span></span></span></span>. I think this is different to what Scott suggests -- he went the other way.</p>

#### [ Kevin Buzzard (Oct 08 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135384772):
<blockquote>
<p>I wonder if there is a common generalization of ring homs, (R,R) -&gt; (R', R') and linear maps (R,M) -&gt; (R, M')</p>
</blockquote>
<p>I think <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi></mrow><annotation encoding="application/x-tex">f</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span></span></span></span>-maps give this. An <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi></mrow><annotation encoding="application/x-tex">f</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span></span></span></span>-map <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>R</mi><mo separator="true">,</mo><mi>M</mi><mo>)</mo><mo>→</mo><mo>(</mo><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup><mo separator="true">,</mo><msup><mi>M</mi><mo mathvariant="normal">′</mo></msup><mo>)</mo></mrow><annotation encoding="application/x-tex">(R,M)\to (R',M')</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:1.001892em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.10903em;">M</span><span class="mclose">)</span><span class="mrel">→</span><span class="mopen">(</span><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mord"><span class="mord mathit" style="margin-right:0.10903em;">M</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span> is a ring map <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>→</mo><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">R\to R'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mrel">→</span><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> and an <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span>-module map <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>M</mi><mo>→</mo><msup><mi>M</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">M\to M'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">M</span><span class="mrel">→</span><span class="mord"><span class="mord mathit" style="margin-right:0.10903em;">M</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> (note I'm constantly using this trick of, the moment I have a ring map <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>→</mo><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">R\to R'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mrel">→</span><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span>, considering all <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">R'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span>-modules as <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span>-modules). If <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>→</mo><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">R\to R'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mrel">→</span><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> is the identity then this is just an <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span>-module homomorphism, and an <em>example</em> of an <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi></mrow><annotation encoding="application/x-tex">f</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span></span></span></span>-map <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>R</mi><mo separator="true">,</mo><mi>R</mi><mo>)</mo><mo>→</mo><mo>(</mo><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup><mo separator="true">,</mo><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup><mo>)</mo></mrow><annotation encoding="application/x-tex">(R,R)\to(R',R')</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:1.001892em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mclose">)</span><span class="mrel">→</span><span class="mopen">(</span><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span> is given by <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>f</mi><mo separator="true">,</mo><mi>f</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">(f,f)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">)</span></span></span></span>, but given <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>:</mo><mi>R</mi><mo>→</mo><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">f:R\to R'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.946332em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mrel">:</span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mrel">→</span><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> there are <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi></mrow><annotation encoding="application/x-tex">f</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span></span></span></span>-maps <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>R</mi><mo separator="true">,</mo><mi>R</mi><mo>)</mo><mo>→</mo><mo>(</mo><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup><mo separator="true">,</mo><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup><mo>)</mo></mrow><annotation encoding="application/x-tex">(R,R)\to (R',R')</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:1.001892em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mclose">)</span><span class="mrel">→</span><span class="mopen">(</span><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span> which are not <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>f</mi><mo separator="true">,</mo><mi>f</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">(f,f)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">)</span></span></span></span>.</p>

#### [ Kevin Buzzard (Oct 08 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135385018):
<p>OK so Johan has isolated exactly the same idea, but somehow it seems that he has come from a completely different viewpoint (I don't know what a fibred category is). Regarding commutative v non-commutative, I think it's a good idea to push commutative here. Someone impressed on me decades ago that one should not think of commutative ring theory as a special case of non-commutative ring theory but regard them as completely different areas. I don't know anything about research into non-commutative ring theory, but commutative ring theory is very much alive and kicking -- e.g. ideas from the theory of perfectoid spaces were used here <a href="https://arxiv.org/abs/1608.08882" target="_blank" title="https://arxiv.org/abs/1608.08882">https://arxiv.org/abs/1608.08882</a> to resolve a the direct summand conjecture. Commutative algebra is the foundation of modern algebraic geometry and I have always been of the opinion (even before I knew anything about formal proof verification software) that books like Atiyah--Macdonald and Matsumura (both standard commutative algebra textbooks) somehow "operated close to the axioms" whilst still being of great modern interest. If we want to push Lean as a tool for algebraic geometry, which it one day might become, then there's no harm focussing on commutative algebra. When someone eventually decides to do some basic representation theory of finite groups we might have to plough through basics of semisimple algebras but that is somehow a completely different project.</p>

#### [ Johan Commelin (Oct 08 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135385035):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> A fibered category is the thing that underlies a stack.</p>

#### [ Johan Commelin (Oct 08 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135385039):
<p>Basically it abstracts <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi></mrow><annotation encoding="application/x-tex">f</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span></span></span></span>-maps</p>

#### [ Kevin Buzzard (Oct 08 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135385344):
<blockquote>
<blockquote>
<p>every R'-mod is an R-mod</p>
</blockquote>
<p>This one requires an explicit ring hom input</p>
</blockquote>
<p>Patrick mentioned recently that sometimes it's best to concentrate on the morphisms, not the objects. In alg geom we even see it in the name -- an <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi></mrow><annotation encoding="application/x-tex">f</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span></span></span></span>-map is a construction which depends on a map <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi></mrow><annotation encoding="application/x-tex">f</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span></span></span></span> of rings. In fact Johan is saying all the right things, I need to get up much earlier to get ahead of him. Given <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>:</mo><mi>R</mi><mo>→</mo><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">f:R\to R'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.946332em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mrel">:</span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mrel">→</span><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> there are then adjoint functors <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>R</mi><mo>−</mo><mi>m</mi><mi>o</mi><mi>d</mi><mo>)</mo><mo>→</mo><mo>(</mo><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup><mo>−</mo><mi>m</mi><mi>o</mi><mi>d</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">(R-mod)\to(R'-mod)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:1.001892em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mbin">−</span><span class="mord mathit">m</span><span class="mord mathit">o</span><span class="mord mathit">d</span><span class="mclose">)</span><span class="mrel">→</span><span class="mopen">(</span><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span><span class="mbin">−</span><span class="mord mathit">m</span><span class="mord mathit">o</span><span class="mord mathit">d</span><span class="mclose">)</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup><mo>−</mo><mi>m</mi><mi>o</mi><mi>d</mi><mo>)</mo><mo>→</mo><mo>(</mo><mi>R</mi><mo>−</mo><mi>m</mi><mi>o</mi><mi>d</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">(R'-mod)\to(R-mod)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:1.001892em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span><span class="mbin">−</span><span class="mord mathit">m</span><span class="mord mathit">o</span><span class="mord mathit">d</span><span class="mclose">)</span><span class="mrel">→</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mbin">−</span><span class="mord mathit">m</span><span class="mord mathit">o</span><span class="mord mathit">d</span><span class="mclose">)</span></span></span></span> and hopefully Kenny proved enough about universal property of tensor products to show that these are adjoints. I think that Scott's punt went in the wrong direction. There is a time when you get maps one way and the other way, but that's when you go back to schemes.</p>

#### [ Johan Commelin (Oct 08 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135385406):
<blockquote>
<p>In fact Johan is saying all the right things, I need to get up much earlier to get ahead of him. </p>
</blockquote>
<p>I've got a 2-year old daughter. You can't win.</p>

#### [ Johan Commelin (Oct 08 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135385439):
<p>Well, what I think that Scott meant that <code>f → f^*</code> is contravariant.</p>

#### [ Kevin Buzzard (Oct 08 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135385440):
<p>Kenny's construction is something else though. If <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>L</mi></mrow><annotation encoding="application/x-tex">L</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">L</span></span></span></span> is an ideal of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">A</span></span></span></span> then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>L</mi><mi>e</mi></msup></mrow><annotation encoding="application/x-tex">L^e</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">L</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">e</span></span></span></span></span></span></span></span></span></span></span>, the pushforward ideal, is less well-behaved. <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>L</mi><mi>e</mi></msup></mrow><annotation encoding="application/x-tex">L^e</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">L</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">e</span></span></span></span></span></span></span></span></span></span></span> is the image of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>L</mi><msub><mo>⊗</mo><mi>A</mi></msub><mi>B</mi></mrow><annotation encoding="application/x-tex">L\otimes_AB</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord mathit">L</span><span class="mbin"><span class="mbin">⊗</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">A</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span> (the canonical thing when it comes to modules) under the natural map from this guy to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>B</mi></mrow><annotation encoding="application/x-tex">B</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span> corresponding by adjointness to the map <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>L</mi><mo>→</mo><mi>B</mi></mrow><annotation encoding="application/x-tex">L\to B</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">L</span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span>. So it might satisfy some universal property for ideals, but probably not for modules.</p>

#### [ Kevin Buzzard (Oct 08 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135385492):
<p>OK I think that's all I have to say and I think that most of it had been said already, but at least I caught up.</p>

#### [ Johan Commelin (Oct 08 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135385493):
<p>For ideals it will probably give you a Galois connection. Here! I said it. Without checking.</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135385562):
<p>But I guess <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>L</mi><mi>e</mi></msup></mrow><annotation encoding="application/x-tex">L^e</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">L</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">e</span></span></span></span></span></span></span></span></span></span></span> is the best you can do when you have a ring hom A-&gt;B and an ideal L?</p>

#### [ Johan Commelin (Oct 08 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135385574):
<p>If you want an ideal of <code>B</code>, yes.</p>

#### [ Johan Commelin (Oct 08 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135385584):
<p>Otherwise, you could just tensor, and treat it as a module.</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135385586):
<p>Is this a thing we can currently do?</p>

#### [ Johan Commelin (Oct 08 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135385590):
<p>What?</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135385592):
<p>tensoring like that</p>

#### [ Johan Commelin (Oct 08 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135385594):
<p>I guess almost</p>

#### [ Johan Commelin (Oct 08 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135385634):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Did you include extension of scalars in your work on tensor products?</p>

#### [ Johan Commelin (Oct 08 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135385647):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Given what we have, it shouldn't be too hard</p>

#### [ Kenny Lau (Oct 08 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135385977):
<p>I don’t think I did.</p>

#### [ Kevin Buzzard (Oct 08 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135386823):
<p>Oh I see. The issue is that if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>M</mi></mrow><annotation encoding="application/x-tex">M</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">M</span></span></span></span> is an <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">A</span></span></span></span>-module and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>B</mi></mrow><annotation encoding="application/x-tex">B</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span> is an <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">A</span></span></span></span>-algebra (and hence an <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">A</span></span></span></span>-module) then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>M</mi><msub><mo>⊗</mo><mi>A</mi></msub><mi>B</mi></mrow><annotation encoding="application/x-tex">M\otimes_AB</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">M</span><span class="mbin"><span class="mbin">⊗</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">A</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span> is not just an <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">A</span></span></span></span>-module but a <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>B</mi></mrow><annotation encoding="application/x-tex">B</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span>-module.</p>

#### [ Johan Commelin (Oct 08 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135386914):
<p>Right, we don't have something like that atm</p>

#### [ Johan Commelin (Oct 08 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135386928):
<p>But it shouldn't be hard to put a <code>B</code>-mod structure on the tensor product.</p>

#### [ Johan Commelin (Oct 08 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135387004):
<p>I don't know if it should "extend" the <code>A</code>-mod structure, in the sense that if you "restrict" scalars you get an <code>A</code>-mod that is defeq to what you started with.</p>

#### [ Patrick Massot (Oct 08 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/135421783):
<blockquote>
<p>foremost of which is the multiple scalar field thing</p>
</blockquote>
<p>I'm completely lost: I thought this module refactor was mostly about multiple scalars</p>

#### [ Kenny Lau (Oct 23 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136304439):
<p>How's it going? <span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Mario Carneiro (Oct 23 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136306139):
<p>waiting on my school work to decrease in intensity</p>

#### [ Mario Carneiro (Oct 23 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136306145):
<p>hopefully I should be able to find some time for it this week</p>

#### [ Kenny Lau (Nov 01 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136911662):
<p><a href="https://github.com/leanprover-community/mathlib/commits/module" target="_blank" title="https://github.com/leanprover-community/mathlib/commits/module">https://github.com/leanprover-community/mathlib/commits/module</a></p>

#### [ Kenny Lau (Nov 01 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136911664):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> is there anything we can help with?</p>

#### [ Mario Carneiro (Nov 01 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136912060):
<p>Possibly... I'm just short on time these days. The main work is done, I think, but a bunch of files still need to be updated</p>

#### [ Kenny Lau (Nov 01 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136912064):
<p>what can we do?</p>

#### [ Kenny Lau (Nov 01 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136912067):
<p>should I fix the errors?</p>

#### [ Mario Carneiro (Nov 01 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136912068):
<p>go in there and make the red squiggles go away</p>

#### [ Kenny Lau (Nov 01 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136912116):
<p>roger that</p>

#### [ Mario Carneiro (Nov 01 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136912204):
<p>Don't get too attached to anything that you write there, I'll probably have a look through all the files anyway, but it will be a lot easier if it's not already broken</p>

#### [ Kenny Lau (Nov 01 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136919089):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> there are things that you deleted and things that depend on them, right</p>

#### [ Kenny Lau (Nov 01 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136919093):
<p>I'll just leave those untouched</p>

#### [ Mario Carneiro (Nov 01 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136919165):
<p>like what? I think all deleted files have equivalents</p>

#### [ Kenny Lau (Nov 01 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136919191):
<p>like the order embedding of submodules of submodules, and the prime ideal, and the trivial ideal</p>

#### [ Kenny Lau (Nov 01 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136919263):
<p>and also this:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">Union_set_of_directed</span> <span class="o">{</span><span class="n">ι</span><span class="o">}</span> <span class="o">(</span><span class="n">hι</span> <span class="o">:</span> <span class="n">nonempty</span> <span class="n">ι</span><span class="o">)</span>
  <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">ι</span> <span class="bp">→</span> <span class="n">submodule</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="n">j</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">k</span><span class="o">,</span> <span class="n">S</span> <span class="n">i</span> <span class="bp">≤</span> <span class="n">S</span> <span class="n">k</span> <span class="bp">∧</span> <span class="n">S</span> <span class="n">j</span> <span class="bp">≤</span> <span class="n">S</span> <span class="n">k</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">((</span><span class="n">supr</span> <span class="n">S</span> <span class="o">:</span> <span class="n">submodule</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="n">β</span><span class="o">)</span> <span class="bp">=</span> <span class="err">⋃</span> <span class="n">i</span><span class="o">,</span> <span class="n">S</span> <span class="n">i</span> <span class="o">:=</span>
</pre></div>

#### [ Mario Carneiro (Nov 01 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136919265):
<p>prime ideals are still there</p>

#### [ Mario Carneiro (Nov 01 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136919287):
<p>search for that, it moved somewhere else</p>

#### [ Mario Carneiro (Nov 01 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136919297):
<p>I think it is Union_coe now</p>

#### [ Kenny Lau (Nov 01 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136919305):
<p><code>prime_ideal</code> doesn't give me anything</p>

#### [ Kenny Lau (Nov 01 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136919307):
<p>and i wouldn't search for <code>prime</code></p>

#### [ Mario Carneiro (Nov 01 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136919355):
<p>the trivial ideal is bottom</p>

#### [ Kenny Lau (Nov 01 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136919360):
<p>ok I searched for <code>prime</code> and I found it</p>

#### [ Kenny Lau (Nov 01 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136925189):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what about the embedding “submodules of N” -&gt; “submodules of M” where N is a submodule of M?</p>

#### [ Mario Carneiro (Nov 01 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136928650):
<p>I think that's <code>map N.subtype</code> or <code>map_subtype.order_iso</code></p>

#### [ Kenny Lau (Nov 01 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136942283):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I've pushed a partial fix</p>

#### [ Kenny Lau (Nov 01 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136942285):
<p>I'll see what more I can do</p>

#### [ Kenny Lau (Nov 02 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136986811):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> for principal ideal domains, the situation is that <code>{x | a ∣ x}</code> is a set not an ideal, so these definitions are a bit troublesome:</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">is_principal_ideal</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">principal</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">S</span> <span class="bp">=</span> <span class="o">{</span><span class="n">x</span> <span class="bp">|</span> <span class="n">a</span> <span class="err">∣</span> <span class="n">x</span><span class="o">})</span>

<span class="n">class</span> <span class="n">principal_ideal_domain</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">integral_domain</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">principal</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">ideal</span> <span class="n">α</span><span class="o">),</span> <span class="n">is_principal_ideal</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">))</span>
</pre></div>

#### [ Kenny Lau (Nov 02 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/136986813):
<p>what should I do?</p>

#### [ Kenny Lau (Nov 02 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137008240):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <a href="https://github.com/leanprover/mathlib/blob/master/ring_theory/ideals.lean#L140" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/ring_theory/ideals.lean#L140"><code>ideal.quotient.eq</code></a> is missing</p>

#### [ Kenny Lau (Nov 02 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137008271):
<p>(and <code>submodule.quotient.eq</code> doesn't count)</p>

#### [ Kenny Lau (Nov 02 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137064504):
<p>Successfully reduced to 4 errors. Pushed.</p>

#### [ Mario Carneiro (Nov 02 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137076716):
<p>the ideal <code>{x | a ∣ x}</code> is now spelled <code>span {a}</code></p>

#### [ Kenny Lau (Nov 02 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137079093):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> by "now" do you mean "I've changed that in my private copy" or "I should change that and then push it"?</p>

#### [ Mario Carneiro (Nov 02 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137079105):
<p>I mean in the module branch that's how it is currently used</p>

#### [ Mario Carneiro (Nov 02 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137079113):
<p>so if you find it elsewhere you should use that</p>

#### [ Kenny Lau (Nov 02 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137079114):
<p>so it's the latter?</p>

#### [ Kenny Lau (Nov 02 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137079118):
<p>ok</p>

#### [ Mario Carneiro (Nov 02 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137079137):
<p>is_principal_ideal should be a property of S : ideal</p>

#### [ Kenny Lau (Nov 02 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137079292):
<p>and what is to become of <code>ideal.quotient.eq</code>? <span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Mario Carneiro (Nov 02 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137079358):
<p>what does <code>quotient_ring</code> look like now?</p>

#### [ Kenny Lau (Nov 02 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137079414):
<p>it looks like <code>ideal.quotient</code> now</p>

#### [ Kenny Lau (Nov 02 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137079430):
<p>we have <code>ideal.quotient.mk := submodule.quotient.mk</code> and we have <code>submodule.quotient,eq</code></p>

#### [ Kenny Lau (Nov 02 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137079446):
<p>but not <code>ideal.quotient.eq</code></p>

#### [ Mario Carneiro (Nov 02 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137079455):
<p>oh sure, you can state <code>ideal.quotient.eq</code></p>

#### [ Kenny Lau (Nov 02 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137079458):
<p>ok</p>

#### [ Mario Carneiro (Nov 02 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137079464):
<p>it's just a defeq copy paste job</p>

#### [ Kenny Lau (Nov 02 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137079476):
<p>I just thought I wouldn't add things without first asking you</p>

#### [ Mario Carneiro (Nov 02 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137079481):
<p>I have not added all theorems from submodules to ideals, I intended to add them as needed</p>

#### [ Mario Carneiro (Nov 02 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137079549):
<p>you can often just use the submodule version directly, but it is slightly less ergonomic</p>

#### [ Kenny Lau (Nov 02 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137079650):
<p>I agree (with the latter statement)</p>

#### [ Kenny Lau (Nov 02 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137084347):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">mem_span_singleton</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span>
  <span class="n">x</span> <span class="err">∈</span> <span class="n">span</span> <span class="o">({</span><span class="n">y</span><span class="o">}</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="bp">↔</span> <span class="bp">∃</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:=</span>
</pre></div>

#### [ Kenny Lau (Nov 02 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137084351):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> can I change this to use dvd?</p>

#### [ Mario Carneiro (Nov 02 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137084382):
<p>maybe make another theorem</p>

#### [ Kenny Lau (Nov 02 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137084453):
<p>but nobody uses that theorem</p>

#### [ Kenny Lau (Nov 02 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137084455):
<p>you added that theorem yourself</p>

#### [ Kenny Lau (Nov 02 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137085654):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">is_maximal_of_irreducible</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">hp</span> <span class="o">:</span> <span class="kn">irreducible</span> <span class="n">p</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">is_maximal</span> <span class="o">(</span><span class="n">span</span> <span class="o">({</span><span class="n">p</span><span class="o">}</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span>
</pre></div>


<p>Should this be an instance?</p>

#### [ Mario Carneiro (Nov 02 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137085959):
<p>oh I see, it's copy pasted from the analogous theorem on submodule, where you can't use dvd</p>

#### [ Mario Carneiro (Nov 02 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137086049):
<p>as for that last one - probably not. Things like <code>irreducible</code> and <code>maximal</code> and <code>nat.prime</code> are forming a new kind of idiom, where the predicate is a <code>class</code> but most of the theorems use it like normal assumptions</p>

#### [ Mario Carneiro (Nov 02 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137086099):
<p>This is primarily intended to support the few cases where you have to use typeclass inference, like in Z/nZ is a field</p>

#### [ Kevin Buzzard (Nov 03 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137089370):
<p>I want there to be an "is_an_integer" predicate on eg rat to save me from coercions.</p>

#### [ Kenny Lau (Nov 03 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137089440):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> wrong thread?</p>

#### [ Kevin Buzzard (Nov 03 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137089490):
<p>Isn't that a predicate which is a class?</p>

#### [ Kenny Lau (Nov 03 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137089518):
<p>oh well this is going off track</p>

#### [ Chris Hughes (Nov 03 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137089626):
<p>Why is it a class?</p>

#### [ Mario Carneiro (Nov 03 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137089816):
<p>I don't just mean a predicate that is a class, we have plenty of those like <code>first_countable X</code>. I mean predicates that are classes that we use without instance brackets in most theorems</p>

#### [ Kenny Lau (Nov 03 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137090743):
<p>I feel like there is not enough transparency with the module refactoring, so I've decided to write something about it.</p>
<p>Major changes made:</p>
<ul>
<li><code>semimodule α β</code> and <code>module α β</code> and <code>vector_space α β</code> now take one more argument, that <code>β</code> is an <code>add_comm_group</code>, i.e. before making an instance of a module, you need to prove that it's an abelian group first.</li>
<li>vector space is no longer over a field, but a discrete field.</li>
<li>The idiom for making an instance <code>module α β</code> (after proving that <code>β</code> is an abelian group) is <code>module.of_core { smul := sorry, smul_add  := sorry, add_smul := sorry, mul_smul := sorry, one_smul := sorry }</code>.</li>
<li><code>is_linear_map</code> and <code>linear_map</code> are now both structures, and they are independent, meaning that <code>linear_map</code> is no longer defined as <code>subtype is_linear_map</code>. The idiom for making <code>linear_map</code> from <code>is_linear_map</code> is <code>is_linear_map.mk' (f : M -&gt; N) (sorry : is_linear_map f)</code>, and the idiom for making <code>is_linear_map</code> from <code>linear_map</code> is <code>f.is_linear</code> (i.e. <code>linear_map.is_linear f</code>).</li>
<li><code>is_linear_map.add</code> etc no longer exist. instead, you can now add two linear maps together, etc.</li>
<li>the class<code>is_submodule</code> is gone, replaced by the structure <code>submodule</code> which contains a carrier, i.e. if <code>N : submodule R M</code> then <code>N.carrier</code> is a type. And there is an instance <code>module R N</code> in the same situation.</li>
<li>similarly, the class <code>is_ideal</code> is gone, replaced by the structure <code>ideal</code>, which also contains a carrier.</li>
<li>endomorphism ring and general linear group are defined.</li>
<li>submodules form a complete lattice. the trivial ideal is now idiomatically the bottom element, and the universal ideal the top element.</li>
<li><code>linear_algebra/quotient_module.lean</code> is deleted, and it's now <code>submodule.quotient</code> (so if <code>N : submodule R M</code> then <code>submodule R N.quotient</code>) Similarly, <code>quotient_ring.quotient</code> is replaced by <code>ideal.quotient</code>. The canonical map from <code>N</code> to <code>N.quotient</code> is <code>submodule.quotient.mk</code>, and the canonical map from the ideal <code>I</code> to <code>I.quotient</code> is <code>ideal.quotient.mk I</code>.</li>
<li><code>linear_equiv</code> is now based on a linear map and an equiv, and the difference being that now you need to prove that the inverse is also linear, and there is currently no interface to get around that.</li>
<li>Everything you want to know about linear independence and basis is now in the newly created file <code>linear_algebra/basis.lean</code>.</li>
<li>Everything you want to know about linear combinations is now in the newly created file <code>linear_algebra/lc.lean</code>.</li>
<li><code>linear_algebra/linear_map_module.lean</code> and <code>linear_algebra/prod_module.lean</code> and <code>linear_algebra/quotient_module.lean</code> and <code>linear_algebra/submodule.lean</code> and <code>linear_algebra/subtype_module.lean</code> are deleted (with their contents placed elsewhere).</li>
</ul>

#### [ Mario Carneiro (Nov 03 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137090764):
<p>Ha, this was my secret plan all along</p>

#### [ Kenny Lau (Nov 03 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137090808):
<p>I think one would prefer transparency</p>

#### [ Mario Carneiro (Nov 03 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137090810):
<p>now that kenny had to read the stuff he knows what changed</p>

#### [ Mario Carneiro (Nov 03 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137090817):
<p>and can write a nice summary for us</p>

#### [ Kenny Lau (Nov 03 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137090822):
<p>lol</p>

#### [ Mario Carneiro (Nov 03 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137090864):
<p>A remark on <code>module.of_core</code>: it's only intended for use when you aren't proving it's a semimodule first</p>

#### [ Mario Carneiro (Nov 03 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137090910):
<p>like if you don't care about semimodules</p>

#### [ Kenny Lau (Nov 03 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137090954):
<p>I'm sure Kevin doesn't</p>

#### [ Mario Carneiro (Nov 03 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137090961):
<p>By the way, <code>is_linear_map</code> is a late addition. I'm hoping it will not be needed much at all, but it's useful to have as a mixin occasionally</p>

#### [ Kenny Lau (Nov 03 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137091015):
<p>one would have to refactor <code>tensor_product</code> to get rid of all the dependencies thereto, I believe</p>

#### [ Mario Carneiro (Nov 03 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137091016):
<p>I really want <code>linear_map</code> to be the primary one</p>

#### [ Mario Carneiro (Nov 03 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137091023):
<p>oh, I may have done that already</p>

#### [ Kenny Lau (Nov 03 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137091025):
<p>not entirely</p>

#### [ Mario Carneiro (Nov 03 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137091026):
<p>shoot, I have an unsaved file in vscode</p>

#### [ Kenny Lau (Nov 03 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137091030):
<p>lol</p>

#### [ Mario Carneiro (Nov 03 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137091130):
<p>re: interface for linear_equiv, you don't need to prove the inverse is linear, that's not in the structure</p>

#### [ Mario Carneiro (Nov 03 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137091149):
<p>it's just the union (pushout?) of linear_map and equiv</p>

#### [ Kenny Lau (Nov 03 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137091304):
<p>oh, right</p>

#### [ Kenny Lau (Nov 03 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137091863):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> are you going to push your file?</p>

#### [ Mario Carneiro (Nov 03 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137092023):
<p>oh wait, looks like I already pushed most of it</p>

#### [ Mario Carneiro (Nov 03 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137092026):
<p>you already had the important stuff</p>

#### [ Kenny Lau (Nov 03 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137092090):
<p>but tensor product still depends on is_linear_map right?</p>

#### [ Kenny Lau (Nov 03 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137092235):
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="n">def</span> <span class="n">id</span> <span class="o">:</span> <span class="n">R</span> <span class="err">⊗</span> <span class="n">M</span> <span class="err">≃ₗ</span> <span class="n">M</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">inv_fun</span> <span class="o">:=</span> <span class="o">(</span><span class="err">⊗ₜ</span><span class="o">)</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">left_inv</span> <span class="o">:=</span> <span class="n">lift</span><span class="bp">.</span><span class="n">ext</span>
    <span class="o">(</span><span class="n">linear_map</span><span class="bp">.</span><span class="n">is_linear</span> <span class="err">$</span> <span class="n">linear_map</span><span class="bp">.</span><span class="n">comp</span> <span class="o">(</span><span class="n">is_linear_map</span><span class="bp">.</span><span class="n">mk&#39;</span> <span class="bp">_</span> <span class="err">$</span> <span class="o">(</span><span class="n">bilinear</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">linear_right</span> <span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">lift</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">))</span>
    <span class="n">linear_map</span><span class="bp">.</span><span class="n">id</span><span class="bp">.</span><span class="n">is_linear</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">tmul_smul</span><span class="o">,</span> <span class="err">←</span> <span class="n">smul_tmul</span><span class="o">,</span> <span class="n">smul_eq_mul</span><span class="o">,</span> <span class="n">mul_one</span><span class="o">]),</span>
  <span class="n">right_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span>
  <span class="bp">..</span> <span class="o">(</span><span class="n">lift</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">c</span> <span class="n">x</span><span class="o">,</span> <span class="n">c</span> <span class="err">•</span> <span class="n">x</span><span class="o">)</span>
    <span class="bp">⟨λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">linear_map</span><span class="bp">.</span><span class="n">is_linear</span> <span class="o">(</span><span class="n">linear_map</span><span class="bp">.</span><span class="n">smul_right</span> <span class="n">linear_map</span><span class="bp">.</span><span class="n">id</span> <span class="n">m</span><span class="o">),</span>
    <span class="bp">λ</span> <span class="n">r</span><span class="o">,</span> <span class="n">linear_map</span><span class="bp">.</span><span class="n">is_linear</span> <span class="o">(</span><span class="n">r</span> <span class="err">•</span> <span class="n">linear_map</span><span class="bp">.</span><span class="n">id</span><span class="o">)</span><span class="bp">⟩</span> <span class="o">:</span> <span class="n">R</span> <span class="err">⊗</span> <span class="n">M</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">M</span><span class="o">)</span> <span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Nov 03 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137092236):
<p>I don't think anyone wants to see this</p>

#### [ Mario Carneiro (Nov 03 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137092333):
<p>what is your objection exactly?</p>

#### [ Kenny Lau (Nov 03 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137092419):
<p>1. the linear map needs to be put after <code>..</code>; 2. lack of <code>is_linear_map.comp</code> and the fact that <code>lift.ext</code> and most of the things in <code>tensor_product</code> depend on <code>is_linear_map</code> make proofs very long and cumbersome</p>

#### [ Mario Carneiro (Nov 03 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137093199):
<p>I've only done the first half of that file, so some things may still need to be hashed out</p>

#### [ Mario Carneiro (Nov 03 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137093203):
<p><code>lift.ext</code> should take linear maps as input</p>

#### [ Mario Carneiro (Nov 03 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137093273):
<p>You shouldn't feel bound to the current way statements of theorems are written, that's what refactoring is about</p>

#### [ Mario Carneiro (Nov 03 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137093296):
<p>Ideally, this construction should be easy, just cobbling together functions we already know are linear</p>

#### [ Mario Carneiro (Nov 03 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137093354):
<p>I think we need another constructor for is_bilinear_map, or is_linear_map, that takes a linear function and asks you to prove equality to the target function</p>

#### [ Mario Carneiro (Nov 03 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137093401):
<p>which corresponds to the alternate definition <code>def is_linear_map (f : β → γ) := ∃ g : β →ₗ γ, ∀ x, f x = g x</code></p>

#### [ Kenny Lau (Nov 03 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096037):
<blockquote>
<p><code>lift.ext</code> should take linear maps as input</p>
</blockquote>
<p>I don't think that will work, because there are things that need to be proved to be linear</p>

#### [ Kenny Lau (Nov 03 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096098):
<p>do you think I should change <code>is_bilinear_map</code> to <code>bilinear_map</code>?</p>

#### [ Mario Carneiro (Nov 03 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096203):
<p>Huh? <code>lift.ext</code> takes two functions and proofs that they are linear</p>

#### [ Mario Carneiro (Nov 03 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096204):
<p>that can always be contracted to a function taking a <code>linear_map</code> arg</p>

#### [ Mario Carneiro (Nov 03 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096254):
<p>I thought about it, but do the set of all bilinear maps have a nice structure like linear maps? Like can you add them and such</p>

#### [ Kenny Lau (Nov 03 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096331):
<p>yes</p>

#### [ Kenny Lau (Nov 03 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096332):
<p>they're even a module</p>

#### [ Kenny Lau (Nov 03 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096371):
<p>they're as nice as linear maps</p>

#### [ Kenny Lau (Nov 03 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096374):
<p>(because of the universal property of tensor product :P)</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096836):
<p>well okay then</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096849):
<p>I think <code>bilinear_map</code> still needs to reference <code>is_linear_map</code> though</p>

#### [ Kenny Lau (Nov 03 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096851):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="n">def</span> <span class="n">bilinear_map</span> <span class="o">:=</span> <span class="n">M</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">N</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">P</span>
</pre></div>

#### [ Kenny Lau (Nov 03 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096852):
<p>how about this</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096854):
<p>oh! does that work?</p>

#### [ Kenny Lau (Nov 03 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096856):
<p>I'm experimenting with it now</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096859):
<p>is Mod(R) a CCC?</p>

#### [ Kenny Lau (Nov 03 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096898):
<p>CCC?</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096899):
<p>cartesian closed category</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096900):
<p>i.e. that thing means what you want it to</p>

#### [ Kenny Lau (Nov 03 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096901):
<p>yes</p>

#### [ Kenny Lau (Nov 03 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096910):
<p>actually I don't know</p>

#### [ Kenny Lau (Nov 03 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096913):
<p>I just know that Hom(M tensor N, P) = Hom(M, Hom(N, P))</p>

#### [ Kenny Lau (Nov 03 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096914):
<p>so (- tensor N) is right adjoint to Hom(N, -)</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096923):
<p>that looks a lot like the universal property of the exponential</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137096963):
<p>Hom(N,P) there is actually an object of the category</p>

#### [ Kenny Lau (Nov 03 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137097797):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">group_theory</span><span class="bp">.</span><span class="n">free_abelian_group</span>
<span class="kn">import</span> <span class="n">linear_algebra</span><span class="bp">.</span><span class="n">basic</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">squeeze</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">N</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">{</span><span class="n">Q</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
<span class="kn">variables</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">M</span><span class="o">]</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">N</span><span class="o">]</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">P</span><span class="o">]</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">Q</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">[</span><span class="n">module</span> <span class="n">R</span> <span class="n">M</span><span class="o">]</span> <span class="o">[</span><span class="n">module</span> <span class="n">R</span> <span class="n">N</span><span class="o">]</span> <span class="o">[</span><span class="n">module</span> <span class="n">R</span> <span class="n">P</span><span class="o">]</span> <span class="o">[</span><span class="n">module</span> <span class="n">R</span> <span class="n">Q</span><span class="o">]</span>
<span class="n">include</span> <span class="n">R</span>

<span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="n">def</span> <span class="n">bilinear_map</span> <span class="o">:=</span> <span class="n">M</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">N</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">P</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="n">M</span> <span class="n">N</span> <span class="n">P</span><span class="o">}</span>

<span class="kn">namespace</span> <span class="n">bilinear_map</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">M</span> <span class="n">N</span> <span class="n">P</span> <span class="n">Q</span><span class="o">}</span>

<span class="kn">section</span> <span class="n">mk</span>
<span class="kn">variable</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">M</span> <span class="bp">→</span> <span class="n">N</span> <span class="bp">→</span> <span class="n">P</span><span class="o">)</span>
<span class="kn">variable</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">m₁</span> <span class="n">m₂</span> <span class="n">n</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">m₁</span> <span class="bp">+</span> <span class="n">m₂</span><span class="o">)</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">m₁</span> <span class="n">n</span> <span class="bp">+</span> <span class="n">f</span> <span class="n">m₂</span> <span class="n">n</span><span class="o">)</span>
<span class="kn">variable</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">c</span> <span class="n">m</span> <span class="n">n</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">c</span> <span class="err">•</span> <span class="n">m</span><span class="o">)</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">c</span> <span class="err">•</span> <span class="n">f</span> <span class="n">m</span> <span class="n">n</span><span class="o">)</span>
<span class="kn">variable</span> <span class="o">(</span><span class="n">H3</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">m</span> <span class="n">n₁</span> <span class="n">n₂</span><span class="o">,</span> <span class="n">f</span> <span class="n">m</span> <span class="o">(</span><span class="n">n₁</span> <span class="bp">+</span> <span class="n">n₂</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">m</span> <span class="n">n₁</span> <span class="bp">+</span> <span class="n">f</span> <span class="n">m</span> <span class="n">n₂</span><span class="o">)</span>
<span class="kn">variable</span> <span class="o">(</span><span class="n">H4</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">c</span> <span class="n">m</span> <span class="n">n</span><span class="o">,</span> <span class="n">f</span> <span class="n">m</span> <span class="o">(</span><span class="n">c</span> <span class="err">•</span> <span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="n">c</span> <span class="err">•</span> <span class="n">f</span> <span class="n">m</span> <span class="n">n</span><span class="o">)</span>

<span class="n">def</span> <span class="n">bilinear_map</span><span class="bp">.</span><span class="n">mk</span> <span class="o">:</span>
  <span class="n">bilinear_map</span> <span class="n">R</span> <span class="n">M</span> <span class="n">N</span> <span class="n">P</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">m</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">f</span> <span class="n">m</span><span class="o">,</span> <span class="n">H3</span> <span class="n">m</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">c</span><span class="o">,</span> <span class="n">H4</span> <span class="n">c</span> <span class="n">m</span><span class="bp">⟩</span><span class="o">,</span>
<span class="bp">λ</span> <span class="n">m₁</span> <span class="n">m₂</span><span class="o">,</span> <span class="n">linear_map</span><span class="bp">.</span><span class="n">ext</span> <span class="err">$</span> <span class="n">H1</span> <span class="n">m₁</span> <span class="n">m₂</span><span class="o">,</span>
<span class="bp">λ</span> <span class="n">c</span> <span class="n">m</span><span class="o">,</span> <span class="n">linear_map</span><span class="bp">.</span><span class="n">ext</span> <span class="err">$</span> <span class="n">H2</span> <span class="n">c</span> <span class="n">m</span><span class="bp">⟩</span>

<span class="kn">theorem</span> <span class="n">bilinear_map</span><span class="bp">.</span><span class="n">mk_apply</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">M</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">N</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">bilinear_map</span><span class="bp">.</span><span class="n">mk</span> <span class="n">f</span> <span class="n">H1</span> <span class="n">H2</span> <span class="n">H3</span> <span class="n">H4</span> <span class="n">m</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">m</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="kn">end</span> <span class="n">mk</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">bilinear_map</span> <span class="n">R</span> <span class="n">M</span> <span class="n">N</span> <span class="n">P</span><span class="o">)</span>

<span class="n">def</span> <span class="n">comm</span> <span class="o">:</span> <span class="n">bilinear_map</span> <span class="n">R</span> <span class="n">N</span> <span class="n">M</span> <span class="n">P</span> <span class="o">:=</span>
<span class="n">bilinear_map</span><span class="bp">.</span><span class="n">mk</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">n</span> <span class="n">m</span><span class="o">,</span> <span class="n">f</span> <span class="n">m</span> <span class="n">n</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">n₁</span> <span class="n">n₂</span> <span class="n">m</span><span class="o">,</span> <span class="o">(</span><span class="n">f</span> <span class="n">m</span><span class="o">)</span><span class="bp">.</span><span class="n">map_add</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">c</span> <span class="n">n</span> <span class="n">m</span><span class="o">,</span> <span class="o">(</span><span class="n">f</span> <span class="n">m</span><span class="o">)</span><span class="bp">.</span><span class="n">map_smul</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">n</span> <span class="n">m₁</span> <span class="n">m₂</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">f</span><span class="bp">.</span><span class="n">map_add</span><span class="bp">;</span> <span class="n">refl</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">c</span> <span class="n">n</span> <span class="n">m</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">f</span><span class="bp">.</span><span class="n">map_smul</span><span class="bp">;</span> <span class="n">refl</span><span class="o">)</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">comm_apply</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">M</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">N</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span><span class="bp">.</span><span class="n">comm</span> <span class="n">n</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">m</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="n">def</span> <span class="n">left</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">N</span><span class="o">)</span> <span class="o">:</span> <span class="n">M</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">P</span> <span class="o">:=</span> <span class="n">f</span><span class="bp">.</span><span class="n">comm</span> <span class="n">y</span>
<span class="n">def</span> <span class="n">right</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">M</span><span class="o">)</span> <span class="o">:</span> <span class="n">N</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">P</span> <span class="o">:=</span> <span class="n">f</span> <span class="n">x</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">left_apply</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">M</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">N</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span><span class="bp">.</span><span class="n">left</span> <span class="n">y</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">right_apply</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">M</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">N</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span><span class="bp">.</span><span class="n">right</span> <span class="n">x</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="kn">theorem</span> <span class="n">zero_left</span> <span class="o">(</span><span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="mi">0</span> <span class="n">y</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">left</span> <span class="n">y</span><span class="o">)</span><span class="bp">.</span><span class="n">map_zero</span>
<span class="kn">theorem</span> <span class="n">zero_right</span> <span class="o">(</span><span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">right</span> <span class="n">x</span><span class="o">)</span><span class="bp">.</span><span class="n">map_zero</span>

<span class="kn">theorem</span> <span class="n">neg_left</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="o">(</span><span class="bp">-</span><span class="n">x</span><span class="o">)</span> <span class="n">y</span> <span class="bp">=</span> <span class="bp">-</span><span class="n">f</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:=</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">left</span> <span class="n">y</span><span class="o">)</span><span class="bp">.</span><span class="n">map_neg</span> <span class="bp">_</span>
<span class="kn">theorem</span> <span class="n">neg_right</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="o">(</span><span class="bp">-</span><span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="bp">-</span><span class="n">f</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:=</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">right</span> <span class="n">x</span><span class="o">)</span><span class="bp">.</span><span class="n">map_neg</span> <span class="bp">_</span>

<span class="kn">theorem</span> <span class="n">add_left</span> <span class="o">(</span><span class="n">x₁</span> <span class="n">x₂</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="o">(</span><span class="n">x₁</span> <span class="bp">+</span> <span class="n">x₂</span><span class="o">)</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x₁</span> <span class="n">y</span> <span class="bp">+</span> <span class="n">f</span> <span class="n">x₂</span> <span class="n">y</span> <span class="o">:=</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">left</span> <span class="n">y</span><span class="o">)</span><span class="bp">.</span><span class="n">map_add</span> <span class="bp">_</span> <span class="bp">_</span>
<span class="kn">theorem</span> <span class="n">add_right</span> <span class="o">(</span><span class="n">x</span> <span class="n">y₁</span> <span class="n">y₂</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="o">(</span><span class="n">y₁</span> <span class="bp">+</span> <span class="n">y₂</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x</span> <span class="n">y₁</span> <span class="bp">+</span> <span class="n">f</span> <span class="n">x</span> <span class="n">y₂</span> <span class="o">:=</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">right</span> <span class="n">x</span><span class="o">)</span><span class="bp">.</span><span class="n">map_add</span> <span class="bp">_</span> <span class="bp">_</span>

<span class="kn">theorem</span> <span class="n">smul_left</span> <span class="o">(</span><span class="n">r</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="o">(</span><span class="n">r</span> <span class="err">•</span> <span class="n">x</span><span class="o">)</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">r</span> <span class="err">•</span> <span class="n">f</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:=</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">left</span> <span class="n">y</span><span class="o">)</span><span class="bp">.</span><span class="n">map_smul</span> <span class="bp">_</span> <span class="bp">_</span>
<span class="kn">theorem</span> <span class="n">smul_right</span> <span class="o">(</span><span class="n">r</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="o">(</span><span class="n">r</span> <span class="err">•</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">r</span> <span class="err">•</span> <span class="n">f</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:=</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">right</span> <span class="n">x</span><span class="o">)</span><span class="bp">.</span><span class="n">map_smul</span> <span class="bp">_</span> <span class="bp">_</span>

<span class="n">def</span> <span class="n">comp₁</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">Q</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">M</span><span class="o">)</span> <span class="o">:</span> <span class="n">bilinear_map</span> <span class="n">R</span> <span class="n">Q</span> <span class="n">N</span> <span class="n">P</span> <span class="o">:=</span>
<span class="n">linear_map</span><span class="bp">.</span><span class="n">comp</span> <span class="n">f</span> <span class="n">g</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">comp₁_apply</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">Q</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">M</span><span class="o">)</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="n">Q</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">N</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">f</span><span class="bp">.</span><span class="n">comp₁</span> <span class="n">g</span> <span class="n">q</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="n">q</span><span class="o">)</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="n">def</span> <span class="n">comp₂</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">Q</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">N</span><span class="o">)</span> <span class="o">:</span> <span class="n">bilinear_map</span> <span class="n">R</span> <span class="n">M</span> <span class="n">Q</span> <span class="n">P</span> <span class="o">:=</span>
<span class="n">linear_map</span><span class="bp">.</span><span class="n">comp</span> <span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">linear_map</span><span class="bp">.</span><span class="n">comp</span> <span class="n">x</span> <span class="n">g</span><span class="o">,</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span> <span class="n">f</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">comp₂_apply</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">Q</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">N</span><span class="o">)</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">M</span><span class="o">)</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="n">Q</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">f</span><span class="bp">.</span><span class="n">comp₂</span> <span class="n">g</span> <span class="n">m</span> <span class="n">q</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">m</span> <span class="o">(</span><span class="n">g</span> <span class="n">q</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="n">def</span> <span class="n">comp₃</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">P</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">Q</span><span class="o">)</span> <span class="o">:</span> <span class="n">bilinear_map</span> <span class="n">R</span> <span class="n">M</span> <span class="n">N</span> <span class="n">Q</span> <span class="o">:=</span>
<span class="n">linear_map</span><span class="bp">.</span><span class="n">comp</span> <span class="bp">⟨</span><span class="n">g</span><span class="bp">.</span><span class="n">comp</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">linear_map</span><span class="bp">.</span><span class="n">ext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="n">g</span><span class="bp">.</span><span class="n">map_add</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="bp">λ</span> <span class="n">c</span> <span class="n">x</span><span class="o">,</span> <span class="n">linear_map</span><span class="bp">.</span><span class="n">ext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="n">g</span><span class="bp">.</span><span class="n">map_smul</span> <span class="bp">_</span> <span class="bp">_⟩</span> <span class="n">f</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">comp₃_apply</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">P</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">Q</span><span class="o">)</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">M</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">N</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">f</span><span class="bp">.</span><span class="n">comp₃</span> <span class="n">g</span> <span class="n">m</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">g</span> <span class="o">(</span><span class="n">f</span> <span class="n">m</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="kn">end</span> <span class="n">bilinear_map</span>
</pre></div>

#### [ Kenny Lau (Nov 03 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137097798):
<p>looking good</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137097901):
<p>maybe I'm spoiled, but I would hope that there was a direct way to get <code>comm</code></p>

#### [ Mario Carneiro (Nov 03 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137097902):
<p>maybe it requires the tensor product though</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137097943):
<p>I guess it is equivalent to saying that <code>left</code> is a linear map</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137098004):
<p>If <code>apply : M -&gt; (M -&gt;l N) -&gt;l N</code> was linear we would have it</p>

#### [ Kenny Lau (Nov 03 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137098005):
<p>and if <code>comp</code> was also linear.. :P</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137098051):
<p>yeah, there should be a principled way to do this using CCCs</p>

#### [ Kenny Lau (Nov 03 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137098052):
<p>but that would be too category-theoretical for our purposes</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137098057):
<p>I mean with the categories unfolded away</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137098062):
<p>We know that CCCs interpret lambda calculus, so literally anything you can write down that is type correct will be linear</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137098104):
<p>we just need the right building blocks to get everything else</p>

#### [ Kenny Lau (Nov 03 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137098106):
<p>but we also know that lambda calculus is generated by abstraction and application?</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137098113):
<p>yes</p>

#### [ Kenny Lau (Nov 03 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137098114):
<p>but abstraction isn't a linear map?</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137098116):
<p>That's <code>apply</code></p>

#### [ Kenny Lau (Nov 03 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137098159):
<p>so what's the conclusion?</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137098162):
<p>er, no - abstraction is the UMP of apply</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137098170):
<p>it works because the families we are considering are themselves linear in their free variables</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137098173):
<p>so you get a "lambda" like operator</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137098216):
<p>In this context we wouldn't actually be able to write down lambda, because we have "the wrong lambda", it isn't linear because we don't have the right notion of family for the category</p>

#### [ Mario Carneiro (Nov 03 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137098221):
<p>but we can run any lambda term through the CCC translation to get a term using only CCC primitives, and we can prove these are all linear</p>

#### [ Johan Commelin (Nov 03 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137103669):
<p>I really like where this is going! Keep up the good work!</p>

#### [ Kevin Buzzard (Nov 03 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137104926):
<p>Yes many thanks Kenny for trying to get the show back on the road. Does this stuff compile yet? Is it worth going back to Hilbert basis theorem yet?</p>

#### [ Kenny Lau (Nov 03 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137110271):
<p>Fixed</p>

#### [ Kenny Lau (Nov 03 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137110475):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what's the next step?</p>

#### [ Mario Carneiro (Nov 03 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137110481):
<p>is it compiling now?</p>

#### [ Kenny Lau (Nov 03 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137110485):
<p>yes</p>

#### [ Mario Carneiro (Nov 03 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137110524):
<p>sweet</p>

#### [ Mario Carneiro (Nov 03 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137110532):
<p>unfortunately I still need to finish and review it myself, so it's in the queue with the other PRs now</p>

#### [ Mario Carneiro (Nov 03 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137110546):
<p>If things go well I will have time this weekend for it</p>

#### [ Kenny Lau (Nov 03 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137110590):
<p>nice</p>

#### [ Mario Carneiro (Nov 03 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137110591):
<p>but if you see any other ways to improve it, add more theorems etc, now's the time</p>

#### [ Mario Carneiro (Nov 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137110605):
<p>the CCC laws seem like a good place to start</p>

#### [ Mario Carneiro (Nov 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137110608):
<p>prove that <code>curry : (A X B -&gt; C) -&gt; (A -&gt; B -&gt; C)</code> is a linear map</p>

#### [ Mario Carneiro (Nov 03 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137110655):
<p>an equiv, even</p>

#### [ Kenny Lau (Nov 03 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137110661):
<p>ok</p>

#### [ Kenny Lau (Nov 03 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137110702):
<p>I don't think that's true</p>

#### [ Mario Carneiro (Nov 03 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137110907):
<p>put <code>l</code> everywhere</p>

#### [ Mario Carneiro (Nov 03 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137110908):
<p>that's homs in the category</p>

#### [ Kenny Lau (Nov 03 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137110950):
<p>it's <code>(M tensor N) -&gt; P</code> equiv <code>M -&gt; (N -&gt; P)</code></p>

#### [ Kenny Lau (Nov 03 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137111063):
<div class="codehilite"><pre><span></span>1. (M ⊗ N) ⊗ P -&gt; M ⊗ (N ⊗ P)
2. (M ⊗ N) -&gt; P -&gt; M ⊗ (N ⊗ P)
3. P -&gt; (M ⊗ N) -&gt; M ⊗ (N ⊗ P)
4. P -&gt; M -&gt; N -&gt; M ⊗ (N ⊗ P)
5. M -&gt; P -&gt; N -&gt; M ⊗ (N ⊗ P)
6. M -&gt; N -&gt; P -&gt; M ⊗ (N ⊗ P)
7. M -&gt; N ⊗ P -&gt; M ⊗ (N ⊗ P)
````
</pre></div>

#### [ Mario Carneiro (Nov 03 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137111403):
<p>yes</p>

#### [ Mario Carneiro (Nov 03 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137111408):
<p>linear equiv I assume</p>

#### [ Mario Carneiro (Nov 03 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137111419):
<p>But I chose that one specifically because it's one of the CCC primitives</p>

#### [ Johan Commelin (Nov 03 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137111422):
<p><em>canonical</em> linear equiv, even... <span class="emoji emoji-1f601" title="grinning face with smiling eyes">:grinning_face_with_smiling_eyes:</span></p>

#### [ Mario Carneiro (Nov 03 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137111473):
<p><code>apply</code> is another: <code>(M -&gt; N) X M -&gt; N</code></p>

#### [ Mario Carneiro (Nov 03 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137111476):
<p>it's trivial with that equiv though</p>

#### [ Mario Carneiro (Nov 03 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137111486):
<p>I think the hom adjunction is equivalent to a few terms that you can compose</p>

#### [ Mario Carneiro (Nov 03 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137111490):
<p>like apply and curry</p>

#### [ Mario Carneiro (Nov 03 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137111532):
<p>do we have everything we need for the tensor product to be a product?</p>

#### [ Mario Carneiro (Nov 03 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137111538):
<p>Is it also the coproduct?</p>

#### [ Johan Commelin (Nov 03 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137111546):
<p>Nope</p>

#### [ Johan Commelin (Nov 03 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137111550):
<p>Coproduct is the direct sum, which is also the product</p>

#### [ Johan Commelin (Nov 03 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137111594):
<p>Tensor product is in fact the coproduct in the category of commutative rings</p>

#### [ Kevin Buzzard (Nov 03 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137111617):
<p>Yes but for modules over a commutative ring it's a different story. You can see something funny is going on because there aren't natural maps from M to M tensor N or from M tensor N to M</p>

#### [ Kevin Buzzard (Nov 03 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137111643):
<p>Other than the zero map</p>

#### [ Mario Carneiro (Nov 03 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137111668):
<p>wait what?</p>

#### [ Mario Carneiro (Nov 03 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137111674):
<p>this is a funny product indeed</p>

#### [ Kenny Lau (Nov 03 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137112176):
<div class="codehilite"><pre><span></span>1. (M ⊗ N) ⊗ P -&gt; M ⊗ (N ⊗ P)
2. (M ⊗ N) -&gt; P -&gt; M ⊗ (N ⊗ P)
3. M -&gt; N -&gt; P -&gt; M ⊗ (N ⊗ P)
4. M -&gt; N ⊗ P -&gt; M ⊗ (N ⊗ P)
</pre></div>

#### [ Kenny Lau (Nov 03 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137112714):
<p><code>(N ≃ₗ P) -&gt; ((M →ₗ N) ≃ₗ (M →ₗ P))</code></p>

#### [ Johan Commelin (Nov 03 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137112878):
<p>Are you listing the things that you are currently proving?</p>

#### [ Mario Carneiro (Nov 03 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137113439):
<p>I think he's just enumerating type correct statements and looking for inhabited types?</p>

#### [ Johan Commelin (Nov 03 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137113487):
<p>Do we have <code>dual</code>?</p>

#### [ Johan Commelin (Nov 03 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137113493):
<p>Because <code>M.dual \otimes N = Hom(M,N)</code> might be an interesting statement...</p>

#### [ Kenny Lau (Nov 03 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137113504):
<p>that's just <code>M -&gt;L R</code></p>

#### [ Kenny Lau (Nov 03 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137113549):
<p>and what you said is only true for M finitely dimensional vector space</p>

#### [ Johan Commelin (Nov 03 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137113551):
<p>Of course, but it is a useful concept.</p>

#### [ Johan Commelin (Nov 03 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137113555):
<p>I'm probably missing some hypotheses...</p>

#### [ Mario Carneiro (Nov 03 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137113557):
<p>don't let truth get in the way of beauty</p>

#### [ Kenny Lau (Nov 03 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114111):
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="n">def</span> <span class="n">assoc</span> <span class="o">:</span> <span class="o">(</span><span class="n">M</span> <span class="err">⊗</span> <span class="n">N</span><span class="o">)</span> <span class="err">⊗</span> <span class="n">P</span> <span class="err">≃ₗ</span> <span class="n">M</span> <span class="err">⊗</span> <span class="o">(</span><span class="n">N</span> <span class="err">⊗</span> <span class="n">P</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">linear_equiv</span><span class="bp">.</span><span class="n">of_linear</span>
  <span class="o">(</span><span class="n">lift</span> <span class="err">$</span> <span class="n">lift</span> <span class="err">$</span> <span class="n">comp</span> <span class="o">(</span><span class="n">unlift&#39;</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="err">$</span> <span class="n">unlift</span> <span class="n">id</span><span class="o">)</span>
  <span class="o">(</span><span class="n">lift</span> <span class="err">$</span> <span class="n">comp</span> <span class="o">(</span><span class="n">lift&#39;</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="err">$</span> <span class="n">unlift</span> <span class="err">$</span> <span class="n">unlift</span> <span class="n">id</span><span class="o">)</span>
  <span class="o">(</span><span class="n">lift</span><span class="bp">.</span><span class="n">ext&#39;</span> <span class="err">$</span> <span class="n">linear_map</span><span class="bp">.</span><span class="n">ext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">lift</span><span class="bp">.</span><span class="n">ext&#39;</span> <span class="err">$</span> <span class="n">bilinear_map</span><span class="bp">.</span><span class="n">ext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">n</span> <span class="n">p</span><span class="o">,</span>
    <span class="k">by</span> <span class="n">repeat</span> <span class="o">{</span> <span class="n">rw</span> <span class="n">lift</span><span class="bp">.</span><span class="n">tmul</span> <span class="bp">&lt;|&gt;</span> <span class="n">rw</span> <span class="n">comp₃_apply</span> <span class="bp">&lt;|&gt;</span> <span class="n">rw</span> <span class="n">comp_apply</span> <span class="bp">&lt;|&gt;</span> <span class="n">rw</span> <span class="n">mk_apply</span> <span class="bp">&lt;|&gt;</span>
        <span class="n">rw</span> <span class="n">lift&#39;_apply</span> <span class="bp">&lt;|&gt;</span> <span class="n">rw</span> <span class="n">comm&#39;_apply</span> <span class="bp">&lt;|&gt;</span> <span class="n">rw</span> <span class="n">unlift_apply</span> <span class="bp">&lt;|&gt;</span> <span class="n">rw</span> <span class="n">unlift&#39;_apply</span> <span class="bp">&lt;|&gt;</span> <span class="n">rw</span> <span class="n">id_apply</span> <span class="o">})</span>
  <span class="o">(</span><span class="n">lift</span><span class="bp">.</span><span class="n">ext&#39;</span> <span class="err">$</span> <span class="n">comm_inj</span> <span class="err">$</span> <span class="n">linear_map</span><span class="bp">.</span><span class="n">ext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">p</span><span class="o">,</span> <span class="n">lift</span><span class="bp">.</span><span class="n">ext&#39;</span> <span class="err">$</span> <span class="n">bilinear_map</span><span class="bp">.</span><span class="n">ext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">m</span> <span class="n">n</span><span class="o">,</span>
    <span class="k">by</span> <span class="n">repeat</span> <span class="o">{</span> <span class="n">rw</span> <span class="n">lift</span><span class="bp">.</span><span class="n">tmul</span> <span class="bp">&lt;|&gt;</span> <span class="n">rw</span> <span class="n">comp₃_apply</span> <span class="bp">&lt;|&gt;</span> <span class="n">rw</span> <span class="n">comp_apply</span> <span class="bp">&lt;|&gt;</span> <span class="n">rw</span> <span class="n">comm_apply</span> <span class="bp">&lt;|&gt;</span> <span class="n">rw</span> <span class="n">mk_apply</span> <span class="bp">&lt;|&gt;</span>
        <span class="n">rw</span> <span class="n">lift&#39;_apply</span> <span class="bp">&lt;|&gt;</span> <span class="n">rw</span> <span class="n">comm&#39;_apply</span> <span class="bp">&lt;|&gt;</span> <span class="n">rw</span> <span class="n">unlift_apply</span> <span class="bp">&lt;|&gt;</span> <span class="n">rw</span> <span class="n">unlift&#39;_apply</span> <span class="bp">&lt;|&gt;</span> <span class="n">rw</span> <span class="n">id_apply</span> <span class="o">})</span>
</pre></div>

#### [ Johan Commelin (Nov 03 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114113):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> How far are we from defining the category of commutative <code>R</code>-algebras?</p>

#### [ Kenny Lau (Nov 03 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114114):
<p>oh well</p>

#### [ Kenny Lau (Nov 03 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114116):
<p>what's the concrete version of your question?</p>

#### [ Johan Commelin (Nov 03 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114155):
<p>Flat ring homs</p>

#### [ Kenny Lau (Nov 03 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114159):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="n">def</span> <span class="n">bilinear_map</span> <span class="o">:=</span> <span class="n">M</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">N</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">P</span>
</pre></div>

#### [ Kenny Lau (Nov 03 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114160):
<p>should we just remove <code>bilinear_map</code> entirely?</p>

#### [ Johan Commelin (Nov 03 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114169):
<p>I think we can leave it out till people start complaining.</p>

#### [ Johan Commelin (Nov 03 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114173):
<p>I would encourage everyone to use linear maps out of the tensor product.</p>

#### [ Johan Commelin (Nov 03 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114231):
<p>Anyway, I would be really happy if we have flat ring homs. Especially if it is readable, instead of the obfuscated kludge that we sometimes see... I think flat ring homs can be a good test case to see if mathlib is ready for the 25 other properties of ring homs that algebraic geometry depends upon.</p>

#### [ Kenny Lau (Nov 03 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114271):
<p>what are the 25 other properties?</p>

#### [ Kenny Lau (Nov 03 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114278):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">map</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">M</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">P</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">N</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">Q</span><span class="o">)</span> <span class="o">:</span> <span class="n">M</span> <span class="err">⊗</span> <span class="n">N</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">P</span> <span class="err">⊗</span> <span class="n">Q</span> <span class="o">:=</span>
<span class="n">lift</span> <span class="err">$</span> <span class="n">comp₁</span> <span class="o">(</span><span class="n">comp₂</span> <span class="o">(</span><span class="n">mk</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="n">g</span><span class="o">)</span> <span class="n">f</span>
</pre></div>


<p>man my interface is really good</p>

#### [ Johan Commelin (Nov 03 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114317):
<p><a href="https://stacks.math.columbia.edu/tag/02WE" target="_blank" title="https://stacks.math.columbia.edu/tag/02WE">https://stacks.math.columbia.edu/tag/02WE</a> most of these have an equivalent for rings</p>

#### [ Kenny Lau (Nov 03 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114408):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">map</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">M</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">P</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">N</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">Q</span><span class="o">)</span> <span class="o">:</span> <span class="n">M</span> <span class="err">⊗</span> <span class="n">N</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">P</span> <span class="err">⊗</span> <span class="n">Q</span> <span class="o">:=</span>
<span class="n">lift</span> <span class="err">$</span> <span class="n">comp₁</span> <span class="o">(</span><span class="n">comp₂</span> <span class="o">(</span><span class="n">mk</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="n">g</span><span class="o">)</span> <span class="n">f</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">map_tmul</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">M</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">P</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">N</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">Q</span><span class="o">)</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">M</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">N</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">map</span> <span class="n">f</span> <span class="n">g</span> <span class="o">(</span><span class="n">m</span> <span class="err">⊗ₜ</span> <span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">m</span> <span class="err">⊗ₜ</span> <span class="n">g</span> <span class="n">n</span> <span class="o">:=</span>
<span class="n">rfl</span>
</pre></div>


<p>how on earth is this <code>rfl</code></p>

#### [ Mario Carneiro (Nov 03 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114472):
<p>of course it is, it's a quotient</p>

#### [ Kenny Lau (Nov 03 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114480):
<p>well then why isn't this <code>rfl</code>:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">lift</span><span class="bp">.</span><span class="n">tmul</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">lift</span> <span class="n">f</span> <span class="o">(</span><span class="n">x</span> <span class="err">⊗ₜ</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:=</span>
</pre></div>

#### [ Kenny Lau (Nov 03 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114580):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">lift</span><span class="bp">.</span><span class="n">tmul</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">lift</span> <span class="n">f</span> <span class="o">(</span><span class="n">x</span> <span class="err">⊗ₜ</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:=</span>
<span class="n">zero_add</span> <span class="bp">_</span>
</pre></div>

#### [ Kenny Lau (Nov 03 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114583):
<p>I guess that's why</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114587):
<p>where'd that come from?</p>

#### [ Kenny Lau (Nov 03 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114639):
<p>the free group</p>

#### [ Chris Hughes (Nov 03 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114640):
<blockquote>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">lift</span><span class="bp">.</span><span class="n">tmul</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">lift</span> <span class="n">f</span> <span class="o">(</span><span class="n">x</span> <span class="err">⊗ₜ</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:=</span>
<span class="n">zero_add</span> <span class="bp">_</span>
</pre></div>


</blockquote>
<p>I love proofs like this.</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114643):
<p><code>free_abelian_group.lift</code> also isn't <code>rfl</code></p>

#### [ Kenny Lau (Nov 03 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114655):
<p>right</p>

#### [ Kenny Lau (Nov 03 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114656):
<p>it's zero_add as well</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114700):
<p>but why? It's built out of pieces that are rfl</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114702):
<p>is it <code>free_group.to_group</code>?</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114716):
<p>ah yes</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114756):
<div class="codehilite"><pre><span></span>def to_group.aux : list (α × bool) → β :=
λ L, list.prod $ L.map $ λ x, cond x.2 (f x.1) (f x.1)⁻¹

def to_group : free_group α → β :=
quot.lift (to_group.aux f) $ λ L₁ L₂ H, red.step.to_group H
</pre></div>

#### [ Mario Carneiro (Nov 03 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114760):
<div class="codehilite"><pre><span></span>@[simp] lemma to_group.of {x} : to_group f (of x) = f x :=
one_mul _
</pre></div>

#### [ Kenny Lau (Nov 03 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114810):
<p>so it's all in <code>list.prod</code></p>

#### [ Kenny Lau (Nov 03 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114879):
<p>under which semantics is <code>by simp; simp only [linear_equiv.apply_symm_apply]</code> supposed to work where <code>by simp [linear_equiv.apply_symm_apply]</code> fails?</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114881):
<p>lol, now this has got me thinking about rewriting <code>free_group</code> again</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114931):
<p>one way to get the right defeqs here is to have the actual definition of <code>free_group</code> be the quotient of expressions in the language of groups with the group laws, and then prove that this is isomorphic to lists</p>

#### [ Kenny Lau (Nov 03 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114932):
<p>and how would one implement "expressions"?</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114933):
<p>expressions in the language of groups means trees</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114935):
<p>you just have a symbol for one and inv and mul</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114977):
<p>and the basis elements</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114979):
<p>and you get trees</p>

#### [ Kenny Lau (Nov 03 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114980):
<p>and what do you mean by tree?</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114987):
<div class="codehilite"><pre><span></span>inductive group_expr (A) : Type
| one : group_expr
| inv : group_expr -&gt; group_expr
| mul : group_expr -&gt; group_expr -&gt; group_expr
</pre></div>

#### [ Kenny Lau (Nov 03 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137114999):
<p>aha</p>

#### [ Kenny Lau (Nov 03 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115007):
<p>how would that help?</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115008):
<p>if you define this as  an inductive, and define the relations as a quotient, you will get really nice defeq</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115051):
<p><code>lift (x * y) = lift x * lift y</code>, <code>lift 1 = 1</code>, <code>lift x = f x</code></p>

#### [ Kenny Lau (Nov 03 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115052):
<p>I don't see how this is different from redefining <code>list.prod</code> so that <code>list.prod [f]</code> is definitionally equivalent to <code>f</code>?</p>

#### [ Kenny Lau (Nov 03 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115054):
<p>oh</p>

#### [ Kenny Lau (Nov 03 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115056):
<p>fair enough</p>

#### [ Johan Commelin (Nov 03 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115068):
<blockquote>
<p>one way to get the right defeqs here is to have the actual definition of <code>free_group</code> be the quotient of expressions in the language of groups with the group laws, and then prove that this is isomorphic to lists</p>
</blockquote>
<p>Wait... in the other thread you said we shouldn't focus on getting all the right defeqs... <span class="emoji emoji-2639" title="sad">:sad:</span></p>

#### [ Mario Carneiro (Nov 03 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115069):
<p>lol</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115071):
<p>sometimes it matters</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115081):
<p>The reason quotient types exist is because of defeqs</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115116):
<p>otherwise we would just use sets of sets</p>

#### [ Johan Commelin (Nov 03 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115127):
<p>/me doesn't follow... noob alert...</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115130):
<p>there is no way to build quotient types like lean's without an axiom</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115169):
<p>we can get something provably isomorphic, but it won't have the defeq on lift</p>

#### [ Johan Commelin (Nov 03 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115173):
<p>I probably haven't experience the pain of working without lean's quotient types... what is wrong with sets of sets?</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115182):
<p>It allows you to define functions that have a certain behavior by definition on the basis elements</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115224):
<p>You can live without defeq, in set theory they do this</p>

#### [ Kenny Lau (Nov 03 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115225):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> so, are you going to do it, or do you intend me to do it? :P</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115226):
<p>but it is nice to have for computational purposes</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115235):
<p>I think I have enough major projects to do :) Like Johan says, it's not essential</p>

#### [ Kenny Lau (Nov 03 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115237):
<p>ok</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115239):
<p>but if it interests you, feel free</p>

#### [ Johan Commelin (Nov 03 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115242):
<p>I encourage both of you to first get this merged into mathlib before embarking on new projects...</p>

#### [ Johan Commelin (Nov 03 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115287):
<p>(or expanding the scope of this refactor)</p>

#### [ Kenny Lau (Nov 03 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115306):
<p>ok I pushed the tensor product</p>

#### [ Kenny Lau (Nov 03 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115308):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> should we PR it now?</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115350):
<p>sure, that will give it more exposure</p>

#### [ Kenny Lau (Nov 03 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115356):
<p>more exposure to what?</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115365):
<p>people with ideas</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115406):
<p>or who like to read about new things on github</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115409):
<p>obviously I'm already aware of this PR, and I will merge it when ready</p>

#### [ Kenny Lau (Nov 03 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115420):
<p>and when is it ready?</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115514):
<p>when I am satisfied with all the changes? It was unfinished when I last reviewed it</p>

#### [ Mario Carneiro (Nov 03 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137115519):
<p>thank you for fixing the bugs, but some things still take time</p>

#### [ Patrick Massot (Nov 03 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137120657):
<p>Thank you very much <span class="user-mention" data-user-id="110064">@Kenny Lau</span> for the documentation effort (and help with actual Lean)! Should we already copy that to <a href="https://github.com/leanprover/mathlib/blob/master/docs/theories/linear_algebra.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/theories/linear_algebra.md">docs/theories/linear_algebra</a> or could it still change?</p>

#### [ Kenny Lau (Nov 03 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137120659):
<p>It could still change</p>

#### [ Patrick Massot (Nov 03 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137120699):
<p>Ok. It would be very useful if you could update it when it will stabilize, so that we'll be able to incorporate it to the docs</p>

#### [ Kenny Lau (Nov 03 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137130652):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> ok I pushed the refactored <code>free_group.lean</code></p>

#### [ Kenny Lau (Nov 03 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137130654):
<p>(it won't build now; I'll fix the errors if you like the new <code>free_group</code>)</p>

#### [ Kenny Lau (Nov 03 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137131106):
<p>also, I don't understand why it is ok that <code>linear_map</code> doesn't take the ring as an argument</p>

#### [ Kenny Lau (Nov 03 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137131918):
<p>ok I put the free group in <a href="https://github.com/leanprover-community/mathlib/tree/module-with-free-group" target="_blank" title="https://github.com/leanprover-community/mathlib/tree/module-with-free-group">a new branch</a> and resetted the PR'ed branch</p>

#### [ Kevin Buzzard (Nov 04 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166041):
<p>So I thought I'd try and get the hang of modules in Lean. Is this construction somewhere in the module branch:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">linear_algebra</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">R</span> <span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">S</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>
  <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">M</span><span class="o">]</span> <span class="o">(</span><span class="n">HM</span> <span class="o">:</span> <span class="n">module</span> <span class="n">S</span> <span class="n">M</span><span class="o">)</span> <span class="o">:</span> <span class="n">module</span> <span class="n">R</span> <span class="n">M</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>?</p>

#### [ Kevin Buzzard (Nov 04 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166228):
<p>Idly trying to prove it myself:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">linear_algebra</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">R</span> <span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">S</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>
  <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">M</span><span class="o">]</span> <span class="o">[</span><span class="n">HM</span> <span class="o">:</span> <span class="n">module</span> <span class="n">S</span> <span class="n">M</span><span class="o">]</span> <span class="o">:</span> <span class="n">module</span> <span class="n">R</span> <span class="n">M</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">smul_add</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">add_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">mul_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">one_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">zero_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">smul_zero</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="o">}</span>
<span class="c">/-</span><span class="cm"></span>

<span class="cm">failed to synthesize type class instance for</span>
<span class="cm">R S : Type,</span>
<span class="cm">_inst_1 : comm_ring R,</span>
<span class="cm">_inst_2 : comm_ring S,</span>
<span class="cm">f : R → S,</span>
<span class="cm">_inst_3 : is_ring_hom f,</span>
<span class="cm">M : Type,</span>
<span class="cm">_inst_4 : add_comm_group M,</span>
<span class="cm">HM : module S M</span>
<span class="cm">⊢ has_scalar R M</span>

<span class="cm">-/</span>
</pre></div>

#### [ Chris Hughes (Nov 04 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166337):
<p>It's a new structure. Don't you just have to define a <code>has_scalar</code> instance first?</p>

#### [ Kevin Buzzard (Nov 04 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166359):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">linear_algebra</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">instance</span> <span class="n">has_scalar_of_ring_hom</span> <span class="o">(</span><span class="n">R</span> <span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">S</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">has_scalar</span> <span class="n">S</span> <span class="n">M</span><span class="o">]</span> <span class="o">:</span>
<span class="n">has_scalar</span> <span class="n">R</span> <span class="n">M</span> <span class="o">:=</span> <span class="o">{</span>
  <span class="n">smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span> <span class="n">m</span><span class="o">,</span> <span class="o">(</span><span class="n">f</span> <span class="n">r</span><span class="o">)</span> <span class="err">•</span> <span class="n">m</span>
<span class="o">}</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">R</span> <span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">S</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>
  <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">M</span><span class="o">]</span> <span class="o">[</span><span class="n">HM</span> <span class="o">:</span> <span class="n">module</span> <span class="n">S</span> <span class="n">M</span><span class="o">]</span> <span class="o">:</span> <span class="n">module</span> <span class="n">R</span> <span class="n">M</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">smul_add</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">add_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">mul_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">one_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">zero_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">smul_zero</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="o">}</span>
<span class="c1">-- maximum class-instance resolution depth has been reached</span>
</pre></div>


<p>My question is whether this is already in the module refactoring, which I think was to a certain extent inspired by the fact that this used to be hard to do</p>

#### [ Chris Hughes (Nov 04 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166407):
<p>I don't think type class inference knows how to infer <code>f</code>. Try making the first things a def, and then giving <code>to_has_scalar</code> or whatever explicitly. Thinking about it, I don't think the second thing can be an instance with the current setup either.</p>

#### [ Kevin Buzzard (Nov 04 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166579):
<p>Oh this is exactly one of those situations where I don't know how to put something into the type class inference machine because I'm in term mode.</p>

#### [ Chris Hughes (Nov 04 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166582):
<p><code>by haveI := _; exact _</code></p>

#### [ Kevin Buzzard (Nov 04 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166634):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">linear_algebra</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">def</span> <span class="n">has_scalar_of_ring_hom</span> <span class="o">(</span><span class="n">R</span> <span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">S</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">has_scalar</span> <span class="n">S</span> <span class="n">M</span><span class="o">]</span> <span class="o">:</span>
<span class="n">has_scalar</span> <span class="n">R</span> <span class="n">M</span> <span class="o">:=</span> <span class="o">{</span>
  <span class="n">smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span> <span class="n">m</span><span class="o">,</span> <span class="o">(</span><span class="n">f</span> <span class="n">r</span><span class="o">)</span> <span class="err">•</span> <span class="n">m</span>
<span class="o">}</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">R</span> <span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">S</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>
  <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">M</span><span class="o">]</span> <span class="o">[</span><span class="n">HM</span> <span class="o">:</span> <span class="n">module</span> <span class="n">S</span> <span class="n">M</span><span class="o">]</span> <span class="o">:</span> <span class="n">module</span> <span class="n">R</span> <span class="n">M</span> <span class="o">:=</span>
  <span class="k">begin</span> <span class="n">haveI</span> <span class="o">:=</span> <span class="n">has_scalar_of_ring_hom</span> <span class="n">R</span> <span class="n">S</span> <span class="n">f</span> <span class="n">M</span><span class="o">,</span>
  <span class="n">exact</span>
<span class="o">{</span> <span class="n">smul_add</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">add_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">mul_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">one_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">zero_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">smul_zero</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Nov 04 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166635):
<p>no errors :D</p>

#### [ Kevin Buzzard (Nov 04 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166642):
<p>so I have to go into tactic mode to put something into the type class inference machine?</p>

#### [ Chris Hughes (Nov 04 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166648):
<p>I think so.</p>

#### [ Chris Hughes (Nov 04 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166690):
<p>This should also work I think.</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">R</span> <span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">S</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>
  <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">M</span><span class="o">]</span> <span class="o">[</span><span class="n">HM</span> <span class="o">:</span> <span class="n">module</span> <span class="n">S</span> <span class="n">M</span><span class="o">]</span> <span class="o">:</span> <span class="n">module</span> <span class="n">R</span> <span class="n">M</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">to_has_scalar</span> <span class="o">:=</span> <span class="n">has_scalar_of_ring_hom</span> <span class="n">R</span> <span class="n">S</span> <span class="n">f</span> <span class="n">M</span><span class="o">,</span>
  <span class="n">smul_add</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">add_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">mul_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">one_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">zero_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">smul_zero</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Nov 04 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166812):
<p>Now I have problems with two smuls. <span class="user-mention" data-user-id="110064">@Kenny Lau</span> Is this done already? I don't want to waste my time if it's already there, but this is exactly what I have always needed for Hilbert basis.</p>

#### [ Chris Hughes (Nov 04 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166821):
<p>I would wait until after module refactorign</p>

#### [ Kenny Lau (Nov 04 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166822):
<p>the right thing to do is just say smul := sorry, right</p>

#### [ Kenny Lau (Nov 04 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166823):
<p>no, this hasn’t been done</p>

#### [ Kevin Buzzard (Nov 04 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166867):
<p>I thought module refactoring had happened</p>

#### [ Kenny Lau (Nov 04 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166871):
<p>you should also read my summary of the changes, this is mentioned there</p>

#### [ Kenny Lau (Nov 04 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166872):
<p>and also you should use module.of_core</p>

#### [ Kenny Lau (Nov 04 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166873):
<p>and also you should use module.of_core</p>

#### [ Kevin Buzzard (Nov 04 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166874):
<p>I thought I had read your summary of the changes :-/</p>

#### [ Kevin Buzzard (Nov 04 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137166884):
<p>Chris your version is better:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">R</span> <span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">S</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>
  <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">M</span><span class="o">]</span> <span class="o">[</span><span class="n">HM</span> <span class="o">:</span> <span class="n">module</span> <span class="n">S</span> <span class="n">M</span><span class="o">]</span> <span class="o">:</span> <span class="n">module</span> <span class="n">R</span> <span class="n">M</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">to_has_scalar</span> <span class="o">:=</span> <span class="n">has_scalar_of_ring_hom</span> <span class="n">R</span> <span class="n">S</span> <span class="n">f</span> <span class="n">M</span><span class="o">,</span>
  <span class="n">smul_add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span><span class="n">smul_add</span> <span class="o">(</span><span class="n">f</span> <span class="n">r</span><span class="o">)</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="c1">-- works</span>
  <span class="n">add_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">mul_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">one_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">zero_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">smul_zero</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="o">}</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">R</span> <span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">S</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>
  <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">M</span><span class="o">]</span> <span class="o">[</span><span class="n">HM</span> <span class="o">:</span> <span class="n">module</span> <span class="n">S</span> <span class="n">M</span><span class="o">]</span> <span class="o">:</span> <span class="n">module</span> <span class="n">R</span> <span class="n">M</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">haveI</span> <span class="o">:=</span> <span class="n">has_scalar_of_ring_hom</span> <span class="n">R</span> <span class="n">S</span> <span class="n">f</span> <span class="n">M</span><span class="bp">;</span>
  <span class="n">exact</span>
<span class="o">{</span> <span class="n">smul_add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">smul_add</span> <span class="o">(</span><span class="n">f</span> <span class="n">r</span><span class="o">)</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="c1">-- fails</span>
  <span class="n">add_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">mul_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">one_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">zero_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">smul_zero</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Nov 04 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137167005):
<p>I see. I think Kenny is pointing out that by "The idiom for making an instance module α β (after proving that β is an abelian group) is module.of_core" he means the strong statement that end users should actually never make modules directly. Is that right Kenny? I still need an instance of <code>module R M</code> though -- how do I get it?</p>

#### [ Kevin Buzzard (Nov 04 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137167057):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">R</span> <span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">S</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>
  <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">M</span><span class="o">]</span> <span class="o">[</span><span class="n">HM</span> <span class="o">:</span> <span class="n">module</span> <span class="n">S</span> <span class="n">M</span><span class="o">]</span> <span class="o">:</span> <span class="n">module</span> <span class="n">R</span> <span class="n">M</span> <span class="o">:=</span> <span class="n">module</span><span class="bp">.</span><span class="n">of_core</span> <span class="o">{</span>
    <span class="n">smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
    <span class="n">smul_add</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
    <span class="n">add_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
    <span class="n">mul_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
    <span class="n">one_smul</span> <span class="o">:=</span> <span class="n">sorry</span>
  <span class="o">}</span>
</pre></div>


<p>Maybe I'm on the right lines now</p>

#### [ Kenny Lau (Nov 04 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137167070):
<p>right</p>

#### [ Kevin Buzzard (Nov 04 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137167310):
<div class="codehilite"><pre><span></span>    <span class="n">add_smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span> <span class="n">s</span> <span class="n">m</span><span class="o">,</span> <span class="c1">-- (is_ring_hom.map_add f).symm ▸ (add_smul (f r) (f s) m), -- stupid triangle never works for me</span>
      <span class="k">begin</span> <span class="k">show</span> <span class="n">f</span> <span class="o">(</span><span class="n">r</span> <span class="bp">+</span> <span class="n">s</span><span class="o">)</span> <span class="err">•</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">r</span> <span class="err">•</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">f</span> <span class="n">s</span> <span class="err">•</span> <span class="n">m</span><span class="o">,</span> <span class="n">rw</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_add</span> <span class="n">f</span><span class="o">,</span> <span class="n">exact</span> <span class="n">add_smul</span> <span class="o">(</span><span class="n">f</span> <span class="n">r</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="n">s</span><span class="o">)</span> <span class="n">m</span><span class="o">,</span><span class="kn">end</span><span class="o">,</span>
</pre></div>

#### [ Kenny Lau (Nov 04 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137167371):
<p>i think you are missing two arguments</p>

#### [ Kevin Buzzard (Nov 04 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137167450):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">linear_algebra</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">R</span> <span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">S</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>
  <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">M</span><span class="o">]</span> <span class="o">[</span><span class="n">HM</span> <span class="o">:</span> <span class="n">module</span> <span class="n">S</span> <span class="n">M</span><span class="o">]</span> <span class="o">:</span> <span class="n">module</span> <span class="n">R</span> <span class="n">M</span> <span class="o">:=</span> <span class="n">module</span><span class="bp">.</span><span class="n">of_core</span> <span class="o">{</span>
    <span class="n">smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span> <span class="n">m</span><span class="o">,</span> <span class="o">(</span><span class="n">f</span> <span class="n">r</span><span class="o">)</span> <span class="err">•</span> <span class="n">m</span><span class="o">,</span>
    <span class="n">smul_add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span><span class="o">,</span> <span class="n">smul_add</span> <span class="err">$</span> <span class="n">f</span> <span class="n">r</span><span class="o">,</span>
    <span class="n">add_smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span> <span class="n">s</span> <span class="n">m</span><span class="o">,</span> <span class="c1">-- (is_ring_hom.map_add f).symm ▸ (add_smul (f r) (f s) m), -- stupid triangle never works for me</span>
      <span class="k">begin</span> <span class="k">show</span> <span class="n">f</span> <span class="o">(</span><span class="n">r</span> <span class="bp">+</span> <span class="n">s</span><span class="o">)</span> <span class="err">•</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">r</span> <span class="err">•</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">f</span> <span class="n">s</span> <span class="err">•</span> <span class="n">m</span><span class="o">,</span> <span class="n">rw</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_add</span> <span class="n">f</span><span class="o">,</span> <span class="n">exact</span> <span class="n">add_smul</span> <span class="o">(</span><span class="n">f</span> <span class="n">r</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="n">s</span><span class="o">)</span> <span class="n">m</span><span class="o">,</span><span class="kn">end</span><span class="o">,</span>
    <span class="n">mul_smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span> <span class="n">s</span> <span class="n">m</span><span class="o">,</span> <span class="k">begin</span> <span class="k">show</span> <span class="n">f</span> <span class="o">(</span><span class="n">r</span> <span class="bp">*</span> <span class="n">s</span><span class="o">)</span> <span class="err">•</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">r</span> <span class="err">•</span> <span class="o">(</span><span class="n">f</span> <span class="n">s</span> <span class="err">•</span> <span class="n">m</span><span class="o">),</span> <span class="n">rw</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_mul</span> <span class="n">f</span><span class="o">,</span> <span class="n">exact</span> <span class="n">mul_smul</span> <span class="o">(</span><span class="n">f</span> <span class="n">r</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="n">s</span><span class="o">)</span> <span class="n">m</span><span class="o">,</span><span class="kn">end</span><span class="o">,</span>
    <span class="n">one_smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="k">begin</span> <span class="k">show</span> <span class="n">f</span> <span class="mi">1</span> <span class="err">•</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">m</span><span class="o">,</span> <span class="n">rw</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_one</span> <span class="n">f</span><span class="o">,</span> <span class="n">exact</span> <span class="n">one_smul</span> <span class="n">m</span><span class="o">,</span> <span class="kn">end</span>
  <span class="o">}</span>
</pre></div>


<p>Still haven't lost my touch ;-) [ugh]</p>

#### [ Kevin Buzzard (Nov 04 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137167457):
<p>well so far I got 0% of the way through proving Hilbert basis, but at least I learnt not to use <code>module</code></p>

#### [ Kevin Buzzard (Nov 04 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137167736):
<p>Does this completely fundamental fact have a name?</p>
<p>Current version:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">linear_algebra</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">instance</span> <span class="n">module_of_module_of_ring_hom</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">S</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">{</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
  <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">M</span><span class="o">]</span> <span class="o">[</span><span class="n">HM</span> <span class="o">:</span> <span class="n">module</span> <span class="n">S</span> <span class="n">M</span><span class="o">]</span> <span class="o">:</span> <span class="n">module</span> <span class="n">R</span> <span class="n">M</span> <span class="o">:=</span> <span class="n">module</span><span class="bp">.</span><span class="n">of_core</span> <span class="o">{</span>
    <span class="n">smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span> <span class="n">m</span><span class="o">,</span> <span class="o">(</span><span class="n">f</span> <span class="n">r</span><span class="o">)</span> <span class="err">•</span> <span class="n">m</span><span class="o">,</span>
    <span class="n">smul_add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span><span class="o">,</span> <span class="n">smul_add</span> <span class="err">$</span> <span class="n">f</span> <span class="n">r</span><span class="o">,</span>
    <span class="n">add_smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span> <span class="n">s</span> <span class="n">m</span><span class="o">,</span> <span class="c1">-- (@is_ring_hom.map_add _ _ _ _ f _ r s) ▸ (add_smul (f r) (f s) m), -- stupid triangle never works for me</span>
      <span class="k">begin</span> <span class="k">show</span> <span class="n">f</span> <span class="o">(</span><span class="n">r</span> <span class="bp">+</span> <span class="n">s</span><span class="o">)</span> <span class="err">•</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">r</span> <span class="err">•</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">f</span> <span class="n">s</span> <span class="err">•</span> <span class="n">m</span><span class="o">,</span> <span class="n">rw</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_add</span> <span class="n">f</span><span class="o">,</span> <span class="n">exact</span> <span class="n">add_smul</span> <span class="o">(</span><span class="n">f</span> <span class="n">r</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="n">s</span><span class="o">)</span> <span class="n">m</span><span class="o">,</span><span class="kn">end</span><span class="o">,</span>
    <span class="n">mul_smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span> <span class="n">s</span> <span class="n">m</span><span class="o">,</span> <span class="k">begin</span> <span class="k">show</span> <span class="n">f</span> <span class="o">(</span><span class="n">r</span> <span class="bp">*</span> <span class="n">s</span><span class="o">)</span> <span class="err">•</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">r</span> <span class="err">•</span> <span class="o">(</span><span class="n">f</span> <span class="n">s</span> <span class="err">•</span> <span class="n">m</span><span class="o">),</span> <span class="n">rw</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_mul</span> <span class="n">f</span><span class="o">,</span> <span class="n">exact</span> <span class="n">mul_smul</span> <span class="o">(</span><span class="n">f</span> <span class="n">r</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="n">s</span><span class="o">)</span> <span class="n">m</span><span class="o">,</span><span class="kn">end</span><span class="o">,</span>
    <span class="n">one_smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="k">begin</span> <span class="k">show</span> <span class="n">f</span> <span class="mi">1</span> <span class="err">•</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">m</span><span class="o">,</span> <span class="n">rw</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_one</span> <span class="n">f</span><span class="o">,</span> <span class="n">exact</span> <span class="n">one_smul</span> <span class="n">m</span><span class="o">,</span> <span class="kn">end</span>
  <span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Nov 04 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137167788):
<p>rw doesn't do unfolding (i.e. if I tell it <code>rw H</code> with <code>H : X = Y</code> and <code>X</code> isn't directly in view, it won't start unfolding things in an attempt to find <code>X</code>, even if something immediately unfolds to give <code>X</code>). Is the same true for the stupid triangle?</p>

#### [ Chris Hughes (Nov 04 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137167790):
<p>Yes. What about <code>erw</code></p>

#### [ Kevin Buzzard (Nov 04 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137167798):
<p>I still seem to need the <code>show</code> for <code>add_smul</code>.</p>

#### [ Kevin Buzzard (Nov 04 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137167925):
<p><code>    add_smul := λ r s m, (((@is_ring_hom.map_add _ _ _ _ f _ r s).symm ▸ (add_smul (f r) (f s) m)) :  f (r + s) • m = f r • m + f s • m),</code></p>

#### [ Kevin Buzzard (Nov 04 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137167926):
<p>longer than the tactic proof ;-)</p>

#### [ Johan Commelin (Nov 04 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137167940):
<p>It ought to be <code>by tidy</code>.</p>

#### [ Kevin Buzzard (Nov 04 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137167986):
<p>does <code>tidy</code> know to try a theorem called <code>add_smul</code> when proving something called <code>add_smul</code>?</p>

#### [ Johan Commelin (Nov 04 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137167991):
<p>Only if it is a simp-lemma</p>

#### [ Johan Commelin (Nov 04 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137168005):
<p>But maybe, once backwords reasoning is merged, this could realistically done by <code>tidy</code>.</p>

#### [ Kevin Buzzard (Nov 04 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137168971):
<p>Will this instance ever trigger?</p>

#### [ Chris Hughes (Nov 04 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137170222):
<p>I doubt it. It will have to find a ring hom out of nowhere.</p>

#### [ Kenny Lau (Nov 04 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137170360):
<p>maybe we should make ring_hom just like linear_map</p>

#### [ David Michael Roberts (Nov 04 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/137171588):
<blockquote>
<p>is Mod(R) a CCC?</p>
</blockquote>
<p>No, because the monoidal structure is not cartesian. What you want is <a href="https://ncatlab.org/nlab/show/closed+monoidal+category" target="_blank" title="https://ncatlab.org/nlab/show/closed+monoidal+category">https://ncatlab.org/nlab/show/closed+monoidal+category</a></p>

#### [ Kenny Lau (Nov 05 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145302840):
<p>(deleted)</p>

#### [ Kenny Lau (Nov 05 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145302841):
<p>(deleted)</p>

#### [ Mario Carneiro (Nov 05 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145303310):
<p>okay, my other obligations are done, so I'm working on finishing the refactoring tonight</p>

#### [ Kenny Lau (Nov 05 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145303430):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">polynomial</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">,</span> <span class="n">priority</span> <span class="mi">1</span><span class="o">]</span> <span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span> <span class="n">w</span>

<span class="kn">open</span> <span class="n">polynomial</span>

<span class="kn">theorem</span> <span class="n">leading_term_aux</span> <span class="o">{</span><span class="n">R</span><span class="o">}</span> <span class="o">[</span><span class="n">nonzero_comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">R</span><span class="o">}</span> <span class="o">(</span><span class="n">Hle</span> <span class="o">:</span> <span class="n">nat_degree</span> <span class="n">f</span> <span class="bp">≤</span> <span class="n">nat_degree</span> <span class="n">g</span><span class="o">)</span>
  <span class="o">(</span><span class="n">Hf</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">Hg</span> <span class="o">:</span> <span class="n">g</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">Hh</span> <span class="o">:</span> <span class="n">leading_coeff</span> <span class="n">f</span> <span class="bp">+</span> <span class="n">leading_coeff</span> <span class="n">g</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span>
<span class="n">leading_coeff</span> <span class="o">(</span><span class="n">f</span> <span class="bp">*</span> <span class="n">X</span> <span class="err">^</span> <span class="o">(</span><span class="n">nat_degree</span> <span class="n">g</span> <span class="bp">-</span> <span class="n">nat_degree</span> <span class="n">f</span><span class="o">)</span> <span class="bp">+</span> <span class="n">g</span><span class="o">)</span> <span class="bp">=</span> <span class="n">leading_coeff</span> <span class="n">f</span> <span class="bp">+</span> <span class="n">leading_coeff</span> <span class="n">g</span> <span class="o">:=</span>
<span class="n">sorry</span>

<span class="n">def</span> <span class="n">ideal</span><span class="bp">.</span><span class="n">leading_coeff</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">nonzero_comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">I</span> <span class="o">:</span> <span class="n">ideal</span> <span class="o">(</span><span class="n">polynomial</span> <span class="n">R</span><span class="o">))</span> <span class="o">:</span> <span class="n">ideal</span> <span class="n">R</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">carrier</span> <span class="o">:=</span> <span class="n">leading_coeff</span> <span class="err">&#39;&#39;</span> <span class="n">I</span><span class="o">,</span>
  <span class="n">zero</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="mi">0</span><span class="o">,</span> <span class="n">I</span><span class="bp">.</span><span class="n">zero_mem</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">⟨</span><span class="n">f</span><span class="o">,</span> <span class="n">hf1</span><span class="o">,</span> <span class="n">hf2</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">g</span><span class="o">,</span> <span class="n">hg1</span><span class="o">,</span> <span class="n">hg2</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">sorry</span><span class="c">/-</span><span class="cm">begin</span>
<span class="cm">    by_cases h0 : a + b = 0, rw h0, exact ⟨0, I.zero_mem, rfl⟩,</span>
<span class="cm">    by_cases hf : f = 0, rw [← hf2, ← hg2, hf, leading_coeff_zero, zero_add], exact ⟨g, hg1, rfl⟩,</span>
<span class="cm">    by_cases hg : g = 0, rw [← hf2, ← hg2, hg, leading_coeff_zero, add_zero], exact ⟨f, hf1, rfl⟩,</span>
<span class="cm">    cases le_total (nat_degree f) (nat_degree g) with hd hd, -- can&#39;t get WLOG to work</span>
<span class="cm">    { refine ⟨f * X ^ (nat_degree g - nat_degree f) + g,</span>
<span class="cm">        I.add_mem (I.mul_mem_right hf1) hg1, _⟩,</span>
<span class="cm">      have := leading_term_aux hd hf hg (by rwa [hf2, hg2]),</span>
<span class="cm">      rwa [hf2, hg2] at this },</span>
<span class="cm">    { refine ⟨g * X ^ (nat_degree g - nat_degree f) + f,</span>
<span class="cm">        I.add_mem (I.mul_mem_right hg1) hf1, _⟩,</span>
<span class="cm">      have := leading_term_aux hd hg hf (by rwa [hf2, hg2, add_comm]),</span>
<span class="cm">      rwa [hf2, hg2] at this }</span>
<span class="cm">  end-/</span><span class="o">,</span>
  <span class="n">smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">c</span> <span class="n">a</span> <span class="bp">⟨</span><span class="n">f</span><span class="o">,</span> <span class="n">hf1</span><span class="o">,</span> <span class="n">hf2</span><span class="bp">⟩</span><span class="o">,</span> <span class="k">begin</span>
    <span class="n">by_cases</span> <span class="n">hcr</span> <span class="o">:</span> <span class="n">c</span> <span class="err">•</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">,</span> <span class="n">rw</span> <span class="n">hcr</span><span class="o">,</span> <span class="n">exact</span> <span class="bp">⟨</span><span class="mi">0</span><span class="o">,</span> <span class="n">I</span><span class="bp">.</span><span class="n">zero_mem</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">refine</span> <span class="bp">⟨</span><span class="n">C</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">f</span><span class="o">,</span> <span class="n">I</span><span class="bp">.</span><span class="n">mul_mem_left</span> <span class="n">hf1</span><span class="o">,</span> <span class="bp">_⟩</span><span class="o">,</span>
    <span class="k">have</span> <span class="o">:</span> <span class="n">leading_coeff</span> <span class="o">(</span><span class="n">C</span> <span class="n">c</span><span class="o">)</span> <span class="bp">*</span> <span class="n">leading_coeff</span> <span class="n">f</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">rwa</span> <span class="o">[</span><span class="n">leading_coeff_C</span><span class="o">,</span> <span class="n">hf2</span><span class="o">,</span> <span class="err">←</span> <span class="n">smul_eq_mul</span><span class="o">]</span> <span class="o">},</span>
    <span class="n">rw</span> <span class="o">[</span><span class="n">leading_coeff_mul&#39;</span> <span class="n">this</span><span class="o">,</span> <span class="n">leading_coeff_C</span><span class="o">,</span> <span class="n">hf2</span><span class="o">,</span> <span class="n">smul_eq_mul</span><span class="o">]</span>
  <span class="kn">end</span> <span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Nov 05 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145303431):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> why does this time out?</p>

#### [ Mario Carneiro (Nov 05 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145303491):
<p>polynomials have had problems with long elaboration in the past</p>

#### [ Mario Carneiro (Nov 05 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145303494):
<p>check that it isn't doing any crazy typeclass searches?</p>

#### [ Kenny Lau (Nov 05 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145303620):
<p>it's searching for <code>has_one nat</code> and <code>has_add nat</code> like a billion times</p>

#### [ Mario Carneiro (Nov 05 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145303719):
<p>still profiling (slow business, of course) but it looks like the second block takes much longer than the first</p>

#### [ Kenny Lau (Nov 05 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145303725):
<p>oh, thanks</p>

#### [ Kenny Lau (Nov 05 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145303733):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> should I push what I have in my kmb_hilbert_basis?</p>

#### [ Mario Carneiro (Nov 05 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145303748):
<p>it takes 3.5 seconds with the sorry in, which is bad but not that bad so I guess you are worried about the commented out bit</p>

#### [ Kenny Lau (Nov 05 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145303805):
<p>but why does <code>polynomial</code> have long elaboration time?</p>

#### [ Mario Carneiro (Nov 05 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145304062):
<p>If I replace the last <code>rwa</code> in the second block with <code>rw</code>, the final state is:</p>
<div class="codehilite"><pre><span></span>...
this : leading_coeff (g * X ^ (nat_degree f - nat_degree g) + f) = b + a
⊢ leading_coeff (g * X ^ (nat_degree g - nat_degree f) + f) = a + b
</pre></div>


<p>I'm not sure how assumption is supposed to close that</p>

#### [ Kenny Lau (Nov 05 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145304145):
<p>ah</p>

#### [ Mario Carneiro (Nov 05 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145304160):
<p>it's probably taking forever unfolding all the things to see if those are actually the same</p>

#### [ Kenny Lau (Nov 05 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145304269):
<p>should I add two submodules together?</p>

#### [ Kenny Lau (Nov 05 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145304491):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">module</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">M</span><span class="o">]</span> <span class="o">[</span><span class="n">module</span> <span class="n">R</span> <span class="n">M</span><span class="o">]</span>

<span class="kn">instance</span> <span class="n">submodule</span><span class="bp">.</span><span class="n">has_add&#39;</span> <span class="o">:</span> <span class="n">has_add</span> <span class="o">(</span><span class="n">submodule</span> <span class="n">R</span> <span class="n">M</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">N₁</span> <span class="n">N₂</span><span class="o">,</span> <span class="o">{</span>
  <span class="n">carrier</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">z</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">x</span> <span class="err">∈</span> <span class="n">N₁</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span> <span class="err">∈</span> <span class="n">N₂</span><span class="o">),</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">z</span> <span class="o">},</span>
  <span class="n">zero</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="mi">0</span><span class="o">,</span> <span class="n">N₁</span><span class="bp">.</span><span class="n">zero_mem</span><span class="o">,</span> <span class="mi">0</span><span class="o">,</span> <span class="n">N₂</span><span class="bp">.</span><span class="n">zero_mem</span><span class="o">,</span> <span class="n">add_zero</span> <span class="bp">_⟩</span><span class="o">,</span>
  <span class="n">add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">z₁</span> <span class="n">z₂</span> <span class="bp">⟨</span><span class="n">x₁</span><span class="o">,</span> <span class="n">hx₁</span><span class="o">,</span> <span class="n">y₁</span><span class="o">,</span> <span class="n">hy₁</span><span class="o">,</span> <span class="n">hz₁</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">x₂</span><span class="o">,</span> <span class="n">hx₂</span><span class="o">,</span> <span class="n">y₂</span><span class="o">,</span> <span class="n">hy₂</span><span class="o">,</span> <span class="n">hz₂</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="bp">⟨</span><span class="n">x₁</span> <span class="bp">+</span> <span class="n">x₂</span><span class="o">,</span> <span class="n">N₁</span><span class="bp">.</span><span class="n">add_mem</span> <span class="n">hx₁</span> <span class="n">hx₂</span><span class="o">,</span> <span class="n">y₁</span> <span class="bp">+</span> <span class="n">y₂</span><span class="o">,</span> <span class="n">N₂</span><span class="bp">.</span><span class="n">add_mem</span> <span class="n">hy₁</span> <span class="n">hy₂</span><span class="o">,</span>
    <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">hz₁</span><span class="o">,</span> <span class="err">←</span> <span class="n">hz₂</span><span class="o">,</span> <span class="n">add_assoc</span><span class="o">,</span> <span class="n">add_left_comm</span> <span class="n">x₂</span><span class="o">,</span> <span class="err">←</span> <span class="n">add_assoc</span><span class="o">]</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">c</span> <span class="n">z</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="o">,</span> <span class="n">y</span><span class="o">,</span> <span class="n">hy</span><span class="o">,</span> <span class="n">hz</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="bp">⟨</span><span class="n">c</span> <span class="err">•</span> <span class="n">x</span><span class="o">,</span> <span class="n">N₁</span><span class="bp">.</span><span class="n">smul_mem</span> <span class="n">c</span> <span class="n">hx</span><span class="o">,</span> <span class="n">c</span> <span class="err">•</span> <span class="n">y</span><span class="o">,</span> <span class="n">N₂</span><span class="bp">.</span><span class="n">smul_mem</span> <span class="n">c</span> <span class="n">hy</span><span class="o">,</span>
    <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">hz</span><span class="o">,</span> <span class="n">smul_add</span><span class="o">]</span><span class="bp">⟩</span> <span class="o">}</span><span class="bp">⟩</span>
</pre></div>

#### [ Mario Carneiro (Nov 05 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145304533):
<p>isn't this <code>\sup</code>?</p>

#### [ Kenny Lau (Nov 05 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145304534):
<p>oh</p>

#### [ Kenny Lau (Nov 05 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145304535):
<p>lol</p>

#### [ Mario Carneiro (Nov 05 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/145304565):
<p>I realize that ring theorists prefer the notations <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow><annotation encoding="application/x-tex">A + B</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.76666em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord mathit">A</span><span class="mbin">+</span><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi><mo>∩</mo><mi>B</mi></mrow><annotation encoding="application/x-tex">A\cap B</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">A</span><span class="mbin">∩</span><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span> to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi><mo>∨</mo><mi>B</mi></mrow><annotation encoding="application/x-tex">A\vee B</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">A</span><span class="mbin">∨</span><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi><mo>∧</mo><mi>B</mi></mrow><annotation encoding="application/x-tex">A\wedge B</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">A</span><span class="mbin">∧</span><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span>, but I think we should go for more notational uniformity</p>

#### [ Kenny Lau (Nov 05 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146784108):
<p>oh, <code>coeff_is_linear</code> uses <code>is_linear_map</code>, should I refactor that? <span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Kenny Lau (Nov 05 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146784560):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">map_mk</span> <span class="o">(</span><span class="n">I</span> <span class="n">J</span> <span class="o">:</span> <span class="n">ideal</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">ideal</span> <span class="n">I</span><span class="bp">.</span><span class="n">quotient</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">carrier</span> <span class="o">:=</span> <span class="n">mk</span> <span class="n">I</span> <span class="err">&#39;&#39;</span> <span class="n">J</span><span class="o">,</span>
  <span class="n">zero</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="mi">0</span><span class="o">,</span> <span class="n">J</span><span class="bp">.</span><span class="n">zero_mem</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">add</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rintro</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="n">hy</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩;</span>
    <span class="n">exact</span> <span class="bp">⟨</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">,</span> <span class="n">J</span><span class="bp">.</span><span class="n">add_mem</span> <span class="n">hx</span> <span class="n">hy</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">smul</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rintro</span> <span class="bp">⟨</span><span class="n">c</span><span class="bp">⟩</span> <span class="bp">_</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩;</span>
    <span class="n">exact</span> <span class="bp">⟨</span><span class="n">c</span> <span class="bp">*</span> <span class="n">x</span><span class="o">,</span> <span class="n">J</span><span class="bp">.</span><span class="n">mul_mem_left</span> <span class="n">hx</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span> <span class="o">}</span>
</pre></div>


<p>I think we can generalize this <span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Mario Carneiro (Nov 05 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146784575):
<p>to what?</p>

#### [ Mario Carneiro (Nov 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146784617):
<p>yes on <code>coeff</code> btw, you may need a second function though</p>

#### [ Kenny Lau (Nov 05 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146785589):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> and how far away are we from the refactoring?</p>

#### [ Mario Carneiro (Nov 05 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146785630):
<p>plan is to finish it today; I am currently rejiggering some stuff with <code>is_unit</code> and <code>nonunits</code> prompted by some of Rob's applications</p>

#### [ Kenny Lau (Nov 05 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146786349):
<p>are you working on a separate branch or a private repo or something? i.e. should I just push to that branch?</p>

#### [ Mario Carneiro (Nov 05 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146786408):
<p>I'm working locally, feel free to keep committing to the <code>module</code> branch and I'll merge when I push</p>

#### [ Kenny Lau (Nov 05 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146786420):
<p>do you want to push your work to the community branches?</p>

#### [ Kevin Buzzard (Nov 05 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146786436):
<p>Kenny and I are just chatting on Skype</p>

#### [ Kevin Buzzard (Nov 05 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146786437):
<p>For Hilbert basis</p>

#### [ Kevin Buzzard (Nov 05 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146786489):
<p>one perhaps needs that there's some inclusion of lattices -- if R -&gt; S is a ring hom and M is an S-module</p>

#### [ Kevin Buzzard (Nov 05 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146786501):
<p>then there's an order preserving injection from the lattice of sub-S-modules to the lattice of sub-R-modules</p>

#### [ Mario Carneiro (Nov 05 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146786568):
<p>okay, it's broken tho</p>

#### [ Kevin Buzzard (Nov 05 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146786582):
<p>A sub-R-module is just a sub-f(R)-module where f(R) is the subring of S</p>

#### [ Kevin Buzzard (Nov 05 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146786605):
<p>If R -&gt; S is an injection with M an S-module then there's an injection from the sub-S-modules to the sub-R-modules</p>

#### [ Kevin Buzzard (Nov 05 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146786657):
<p>If R -&gt; S is a surjection and M is an R-module then the submodule of M consisting of stuff which is annihiliated by the kernel of R-&gt;S is an S-module</p>

#### [ Kevin Buzzard (Nov 05 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146786709):
<p>and that way you get an injection from sub-S-modules to sub-R-modules</p>

#### [ Kenny Lau (Nov 05 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146787850):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">polynomial</span>

<span class="kn">universe</span> <span class="n">u</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">R</span><span class="o">]</span>
<span class="kn">variable</span> <span class="o">(</span><span class="n">I</span> <span class="o">:</span> <span class="n">ideal</span> <span class="o">(</span><span class="n">polynomial</span> <span class="n">R</span><span class="o">))</span>

<span class="n">def</span> <span class="n">ideal</span><span class="bp">.</span><span class="n">of_polynomial</span> <span class="o">:</span> <span class="n">submodule</span> <span class="n">R</span> <span class="o">(</span><span class="n">polynomial</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">carrier</span> <span class="o">:=</span> <span class="o">(</span><span class="bp">@</span><span class="n">submodule</span><span class="bp">.</span><span class="n">carrier</span> <span class="o">(</span><span class="n">polynomial</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="n">polynomial</span> <span class="n">R</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">ring</span><span class="bp">.</span><span class="n">to_module</span> <span class="n">I</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">polynomial</span> <span class="n">R</span><span class="o">)),</span>
  <span class="n">zero</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span> <span class="n">add</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span> <span class="n">smul</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="o">}</span>

<span class="n">def</span> <span class="n">ideal</span><span class="bp">.</span><span class="n">of_polynomial&#39;</span> <span class="o">:</span> <span class="n">submodule</span> <span class="n">R</span> <span class="o">(</span><span class="n">polynomial</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">carrier</span> <span class="o">:=</span> <span class="o">(</span><span class="n">I</span><span class="bp">.</span><span class="n">carrier</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">polynomial</span> <span class="n">R</span><span class="o">)),</span> <span class="c1">-- doesn&#39;t work</span>
  <span class="n">zero</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span> <span class="n">add</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span> <span class="n">smul</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="o">}</span>
</pre></div>


<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Mario Carneiro (Nov 05 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146787867):
<p>it's probably guessing the wrong scalar ring here</p>

#### [ Kevin Buzzard (Nov 05 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146787870):
<p>I thought it never had to guess anything nowadays?</p>

#### [ Mario Carneiro (Nov 05 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146787918):
<p>that's the next thing on the list after the module refactor</p>

#### [ Kevin Buzzard (Nov 05 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146787923):
<p>There's a _list_??</p>

#### [ Johan Commelin (Nov 05 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146787928):
<p>I feel there is a need for module refactor 2.0 <span class="emoji emoji-1f923" title="rolling on the floor laughing">:rolling_on_the_floor_laughing:</span></p>

#### [ Kevin Buzzard (Nov 05 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146787930):
<p>I never realised modules were so hard :-)</p>

#### [ Kenny Lau (Nov 05 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146787987):
<p>yeah that's 'coz you're a mathematician</p>

#### [ Mario Carneiro (Nov 05 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146788414):
<p>the list is my todo list, and it's on the list because people want modules to have multiple scalar rings</p>

#### [ Kevin Buzzard (Nov 05 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146788582):
<p>I am just trying to formalise various standard results in undergraduate algebra like Hilbert basis and reporting back on what mathematicians use</p>

#### [ Mario Carneiro (Nov 05 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146794422):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> The final draft of the module refactor is pushed</p>

#### [ Kenny Lau (Nov 05 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146794432):
<p>so... coeff is linear?</p>

#### [ Mario Carneiro (Nov 05 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146794653):
<p>it is now</p>

#### [ Kenny Lau (Nov 05 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146794754):
<p>thanks</p>

#### [ Kevin Buzzard (Nov 05 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146794766):
<p>So how do I make an S-module into an R-module if I have a ring hom <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>:</mo><mi>R</mi><mo>→</mo><mi>S</mi></mrow><annotation encoding="application/x-tex">f : R \to S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mrel">:</span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span>?</p>

#### [ Kevin Buzzard (Nov 05 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146794771):
<p>thanks too</p>

#### [ Mario Carneiro (Nov 05 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146794880):
<p>Maybe there should be a way to put chosen ring homs in the typeclass infrastructure?</p>

#### [ Mario Carneiro (Nov 05 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146794939):
<p>Otherwise you just have to introduce it locally every time</p>

#### [ Mario Carneiro (Nov 05 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146794957):
<p>I assume you aren't asking how to define the R-module structure, that's not difficult at all</p>

#### [ Johan Commelin (Nov 05 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146795078):
<blockquote>
<p>Maybe there should be a way to put chosen ring homs in the typeclass infrastructure?</p>
</blockquote>
<p>I think we could also try using a structure <code>algebra</code>.</p>

#### [ Kevin Buzzard (Nov 05 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146795319):
<blockquote>
<p>I assume you aren't asking how to define the R-module structure, that's not difficult at all</p>
</blockquote>
<p>Right -- I'm asking for the idiomatic way to do it.</p>

#### [ Johannes Hölzl (Nov 05 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146796014):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>  why  is it now a mixing, i.e. why is the group structure not part of modules anymore?</p>

#### [ Mario Carneiro (Nov 05 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146796108):
<p>Because the parent coercion <code>module R M =&gt; add_comm_group M</code> was causing much of the module typeclass issues</p>

#### [ Mario Carneiro (Nov 05 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146796123):
<p>plus if <code>R</code> becomes not an <code>out_param</code> then it won't even work</p>

#### [ Johannes Hölzl (Nov 05 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146802129):
<p>the module PR looks very good to me</p>

#### [ Johan Commelin (Nov 05 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146804978):
<p>It's merged <span class="emoji emoji-1f389" title="tada">:tada:</span> <span class="emoji emoji-1f44d" title="thumbs up">:thumbs_up:</span> <span class="emoji emoji-1f419" title="octopus">:octopus:</span></p>

#### [ Johannes Hölzl (Nov 05 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/146804983):
<p>COMMIT 1000</p>

#### [ Neil Strickland (Feb 01 2019 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/157346031):
<p>Bases should <strong>definitely</strong> be maps or lists.  Some treatments of finite-dimensional linear algebra purport to use subsets, but they are almost always wrong if read literally, and would require fiddly side-conditions to make them right.  Also, to talk about the standard algorithms you need efficient translation between bases and matrices, which becomes very awkward if you use subsets.</p>

#### [ Johan Commelin (Feb 01 2019 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/157346162):
<p>It isn't too hard to convert between a subset and a map. But maybe there should be a bit more API for this. Is there something specific that you are missing?</p>

#### [ Johan Commelin (Feb 01 2019 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/157346171):
<p>Matrices are currently indexed by fintypes (not necessarily ordered).</p>

#### [ Kenny Lau (Feb 01 2019 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/157346354):
<p>... is this related to the previous discussion?</p>

#### [ Neil Strickland (Feb 01 2019 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20refactoring/near/157346582):
<p>I think not, sorry.  Zulip sometimes gets in a funny state where it shows me very old posts mixed in with new ones, and I was accidentally replying to one of those.  I am not quite sure what is going on with that.</p>


{% endraw %}
