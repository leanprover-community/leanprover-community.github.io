---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91089structurevsclass.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [structure vs class](https://leanprover-community.github.io/archive/113488general/91089structurevsclass.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Apr 02 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124512218):
<p>The age-old question: when to use <code>structure</code> and when to use <code>class</code>?</p>

#### [ Kevin Buzzard (Apr 02 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124523699):
<p>You have to step back and decide whether you want a global, unique instance or not.</p>

#### [ Kenny Lau (Apr 03 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124558513):
<div class="codehilite"><pre><span></span>universes u v

variables (G : Type u) [group G] (X : Type v)

class group_action : Type (max u v) :=
(fn : G → X → X)
(one : ∀ x, fn 1 x = x)
(mul : ∀ g h x, fn (g * h) x = fn g (fn h x))
</pre></div>

#### [ Kenny Lau (Apr 03 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124558514):
<p>should this be a <code>class</code> or a <code>structure</code>?</p>

#### [ Mario Carneiro (Apr 03 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124558557):
<p>A class, I would think, if you want that notation to work</p>

#### [ Mario Carneiro (Apr 03 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124558565):
<p>You may also be able to make one of the two type arguments an <code>out_param</code>. Would you say that one (kind of) uniquely determines the other?</p>

#### [ Kenny Lau (Apr 03 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124558605):
<blockquote>
<p>A class, I would think, if you want that notation to work</p>
</blockquote>
<p>I also think so, but then the following becomes awkward, since it suggests that I can synthesize more than one group actions:</p>
<div class="codehilite"><pre><span></span>protected def trivial : group_action G S :=
⟨λ g, id, λ x, rfl, λ g h x, rfl⟩
</pre></div>

#### [ Kenny Lau (Apr 03 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124558607):
<blockquote>
<p>You may also be able to make one of the two type arguments an <code>out_param</code>. Would you say that one (kind of) uniquely determines the other?</p>
</blockquote>
<p>a <code>module</code> is just an R-action right, so maybe we can use the same strategy</p>

#### [ Kenny Lau (Apr 03 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124558608):
<p>although the set has an abelian group structure</p>

#### [ Kenny Lau (Apr 03 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124558615):
<p>I don't know in this case, what do you think?</p>

#### [ Mario Carneiro (Apr 03 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124558618):
<p>Of course there are multiple group actions in actuality, but probably you want to focus on just one in a given context. Maybe using <code>local instance</code>?</p>

#### [ Kenny Lau (Apr 03 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124558662):
<p>I actually just want to state it, so maybe <code>def</code> is fine</p>

#### [ Patrick Massot (Apr 03 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124561840):
<blockquote>
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">group</span> <span class="n">G</span><span class="o">]</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span>

<span class="n">class</span> <span class="n">group_action</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">fn</span> <span class="o">:</span> <span class="n">G</span> <span class="bp">→</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span>
<span class="o">(</span><span class="n">one</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">fn</span> <span class="mi">1</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">x</span><span class="o">)</span>
<span class="o">(</span><span class="n">mul</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">g</span> <span class="n">h</span> <span class="n">x</span><span class="o">,</span> <span class="n">fn</span> <span class="o">(</span><span class="n">g</span> <span class="bp">*</span> <span class="n">h</span><span class="o">)</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">fn</span> <span class="n">g</span> <span class="o">(</span><span class="n">fn</span> <span class="n">h</span> <span class="n">x</span><span class="o">))</span>
</pre></div>


</blockquote>
<p>Why not</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span>  <span class="n">action</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">group</span> <span class="n">G</span><span class="o">]</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">map</span> <span class="o">:</span> <span class="n">G</span> <span class="bp">→</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">perm</span> <span class="n">α</span><span class="o">)</span>
<span class="o">(</span><span class="n">homo</span> <span class="o">:</span> <span class="n">is_group_hom</span> <span class="n">map</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Apr 03 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124561884):
<p>because.</p>

#### [ Kenny Lau (Apr 03 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124561886):
<p>because stating it more abstractly makes it less useful</p>

#### [ Kenny Lau (Apr 03 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124561889):
<p>conciseness c’est pas tous</p>

#### [ Patrick Massot (Apr 03 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124561902):
<p>See also <a href="https://github.com/PatrickMassot/lean-scratchpad/blob/master/subgroups.lean" target="_blank" title="https://github.com/PatrickMassot/lean-scratchpad/blob/master/subgroups.lean">https://github.com/PatrickMassot/lean-scratchpad/blob/master/subgroups.lean</a> for related random stuff</p>

#### [ Patrick Massot (Apr 03 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124561946):
<p>Using group homomorphism should give you access to lemmas you'll need to reprove with your less abstract definition</p>

#### [ Mario Carneiro (Apr 03 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124561951):
<p>you want to restate them anyway though</p>

#### [ Mario Carneiro (Apr 03 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124561993):
<p>I think that kenny's version more accurately represents the data content, which is a single function G -&gt; X -&gt; X satisfying some properties, rather than a function to a pair of functions</p>

#### [ Mario Carneiro (Apr 03 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124561996):
<p>of course you want your version stated as lemmas, and then all those theorems become available in the end anyway</p>

#### [ Patrick Massot (Apr 03 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124562198):
<p>Mathematically the accurate representation of content if certainly mine. About Lean usability I don't know of course</p>

#### [ Mario Carneiro (Apr 03 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124562574):
<p>they are certainly equivalent, but the data content is different. It's like the difference between representing the integers by an integer, or by a pair of an integer and its negative. The representations are equivalent, but one has some additional redundancy</p>

#### [ Kenny Lau (Apr 03 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124562588):
<p>let’s all just represent nat by Pi X, X-&gt;(X-&gt;X)-&gt;X</p>

#### [ Patrick Massot (Apr 03 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574243):
<p>Ok, I think I understand the confusion: we are talking about two separate issues. My claim is that the mathematically meaningful and redundancy free point of view is to define a group action as a group homomorphism. It seems you are discussing the redundancy in your definition of <code>perm X</code>. Now I'm even more confused. A long time ago you told I should build homeomorphisms on top of equiv. Since then I've been suffering through two levels of coercions (<code>homeo</code> to <code>equiv</code> to <code>function</code>). And I have loads of attempted proofs where I'm stuck with expression mixing multiplication in the group <code>homeo X X</code> and composition of <code>equiv</code> and composition of  functions, which are all the same but I never know how to tell Lean.  And a few days ago you proved this <code>f '' (-s) = - f '' s</code> by throwing away <code>equiv</code> and use <code>function.bijective</code>, so this is the second time in a couple of days where you seem to avoid <code>equiv</code>. I would appreciate any clue about what I should be doing with my groups of homeomorphisms.</p>

#### [ Kenny Lau (Apr 03 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574254):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> How would you state a G-Set homomorphism in your definition of G-Set? In mine, f:X-&gt;Y is a homomorphism if f(gx)=gf(x)</p>

#### [ Patrick Massot (Apr 03 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574430):
<p>I don't understand your question. If ρ_X : G → perm X and ρ_Y : G → perm Y are two G-action then f : X → Y is a G-morphism if, for all g, f ∘ ρ_X(g) = ρ_Y(g) ∘ f</p>

#### [ Kenny Lau (Apr 03 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574442):
<p>interesting</p>

#### [ Patrick Massot (Apr 03 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574443):
<p>Of course you could phrase this in terms of natural transformations</p>

#### [ Kenny Lau (Apr 03 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574445):
<p>I can see a commutative diagram inside :P</p>

#### [ Patrick Massot (Apr 03 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574447):
<p>If you want Mario to run away</p>

#### [ Kenny Lau (Apr 03 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574448):
<p>oh really</p>

#### [ Patrick Massot (Apr 03 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574455):
<p>Sure</p>

#### [ Kenny Lau (Apr 03 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574458):
<p>could you enlighten me?</p>

#### [ Kenny Lau (Apr 03 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574468):
<p>and I feel like I've seen this in group rep</p>

#### [ Patrick Massot (Apr 03 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574540):
<p>But what I was advocating is an intermediate point of view, not going all the way to using categories to define group actions</p>

#### [ Kenny Lau (Apr 03 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574579):
<p>I am writing a category theory repo</p>

#### [ Kenny Lau (Apr 03 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574581):
<p>so it is helpful to me</p>

#### [ Kenny Lau (Apr 03 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574584):
<p><a href="https://github.com/kckennylau/category-theory" target="_blank" title="https://github.com/kckennylau/category-theory">https://github.com/kckennylau/category-theory</a></p>

#### [ Kenny Lau (Apr 03 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574586):
<p>in fact I'm proving that the forgetful functor GSet-&gt;Set has right adjoint</p>

#### [ Patrick Massot (Apr 03 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574591):
<p>A group is a category with one object, and morphisms given by the group element</p>

#### [ Patrick Massot (Apr 03 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574601):
<p>then a G-set is simply a functor from G to Set</p>

#### [ Kenny Lau (Apr 03 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574603):
<p>but it would be a fun fact to prove that that functor thing is isomorphic to the GSet in the category of categories</p>

#### [ Kenny Lau (Apr 03 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574611):
<p>aha, so it's the slice category</p>

#### [ Patrick Massot (Apr 03 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574612):
<p>And a morphism of G-set is a morphism in this category</p>

#### [ Patrick Massot (Apr 03 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574617):
<p>hence a natural transformation</p>

#### [ Kenny Lau (Apr 03 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574621):
<p>very interesting</p>

#### [ Patrick Massot (Apr 03 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574657):
<p>It's meant to be the very first exercise you do after reading the definition of a natural transformation</p>

#### [ Kenny Lau (Apr 03 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574667):
<p>where do you learn category theory?</p>

#### [ Patrick Massot (Apr 03 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574668):
<p>Are you talkin to Scott about this repo?</p>

#### [ Kenny Lau (Apr 03 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574671):
<p>I'm not; he hasn't replied to my message</p>

#### [ Kenny Lau (Apr 03 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574676):
<p>I don't think I've seen him here for a while</p>

#### [ Patrick Massot (Apr 03 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574689):
<p>He was probably captured by real life</p>

#### [ Patrick Massot (Apr 03 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574694):
<p>This happened to me during the last couple of weeks</p>

#### [ Patrick Massot (Apr 03 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574741):
<p>And actually students will probably invade my office soon, and I'll have to let you do your category theory exercises</p>

#### [ Kenny Lau (Apr 03 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574747):
<p>alright</p>

#### [ Kevin Buzzard (Apr 03 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124578652):
<blockquote>
<p>I don't think I've seen him here for a while</p>
</blockquote>
<p>Scott is on holiday at the minute.</p>

#### [ Scott Morrison (Apr 04 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599463):
<p>I am back, but actual maths has captured my attention for a moment --- a collaborator is here this week.</p>

#### [ Kenny Lau (Apr 04 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599466):
<p>omg you're back</p>

#### [ Scott Morrison (Apr 04 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599523):
<p>I am definitely still working on getting my category theory library reading for a PR, but there is still some work to do, which I haven't been finding a lot of time for.</p>

#### [ Kenny Lau (Apr 04 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599529):
<p>hope you don't mind the fact that i'm creating another</p>

#### [ Scott Morrison (Apr 04 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599532):
<p>No, not at all.</p>

#### [ Scott Morrison (Apr 04 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599537):
<p>If you would like to join forces, however, I would be very happy.</p>

#### [ Kenny Lau (Apr 04 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599545):
<p>sure</p>

#### [ Scott Morrison (Apr 04 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599549):
<p>I think it is good to have different eyes and different opinions on projects.</p>

#### [ Scott Morrison (Apr 04 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599554):
<p>I think my focus for category theory for a while will be not adding new material, but rather getting the basics PR'd into mathlib.</p>

#### [ Scott Morrison (Apr 04 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599558):
<p>If you would like to add material, however, that is certainly fine.</p>

#### [ Scott Morrison (Apr 04 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599601):
<p>Also, if you have comments and criticisms of the basics, I'm very happy to hear them concurrently with preparing to PR.</p>

#### [ Kenny Lau (Apr 04 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599609):
<p>have you looked at mine?</p>

#### [ Scott Morrison (Apr 04 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599610):
<p>I'm happy to just give you commit access on the repository if you'd like, or I'll merge PRs as they come.</p>

#### [ Scott Morrison (Apr 04 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599614):
<p>Looking at yours is on my todo list, but Lean is not getting to the top of the todo list again until next week.</p>

#### [ Kenny Lau (Apr 04 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599615):
<p>well you would need to fix your repo first, I heard it doesn't work well with the latest mathlib</p>

#### [ Scott Morrison (Apr 04 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599627):
<p>It was working after the "monad merge" on Lean, and the subsequent update to Lean. I will check again in a moment. Hopefully it is okay, however.</p>

#### [ Scott Morrison (Apr 04 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599949):
<p>Besides irrelevant problems in mathlib, lean-category-theory builds fine against the HEAD of Lean at the moment.</p>

#### [ Kevin Buzzard (Apr 04 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124616405):
<p>Kenny's top priority at the minute is revising for mechanics, but let me give a huge +1 to the idea of you two collaborating on category theory. Kenny seems to understand all the standard category theoretic notions well now, and has a bunch of examples in his head, so whilst he might not yet be at the stage of doing infinity-1 categories or whatever, he will almost certainly have more time to work on categories in the near future (e.g. after his mechanics exam in mid-May)</p>

#### [ Kenny Lau (Apr 04 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124616411):
<p>right, there's mechanics</p>

#### [ Kevin Buzzard (Apr 04 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124616413):
<p>And I am doing my schemes library by proving lots of things about sheaves and presheaves of types, and then writing ad hoc extensions to sheaves of rings</p>

#### [ Kevin Buzzard (Apr 04 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124616422):
<p>and the sooner I can do sheaves of objects the better</p>

#### [ Patrick Massot (Apr 04 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124616865):
<p>Exams are in mid-May and they are already revising?</p>

#### [ Patrick Massot (Apr 04 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124616867):
<p>That's even more amazing than first year students using Lean!</p>

#### [ Kenny Lau (Apr 04 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124616918):
<p>"they are already revising", more like "they are already being told to revise"</p>

#### [ Patrick Massot (Apr 04 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124617037):
<p>This afternoon I will attend a talk whose title is: "Perfectoid spaces and us"</p>

#### [ Patrick Massot (Apr 04 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124617046):
<p>for a general mathematical audience</p>

#### [ Kenny Lau (Apr 04 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124617047):
<p>by thomas hales?</p>

#### [ Patrick Massot (Apr 04 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124617050):
<p>Did you make any progress in formalizing perfectoid spaces</p>

#### [ Kenny Lau (Apr 04 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124617055):
<p>aucun</p>

#### [ Patrick Massot (Apr 04 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124617056):
<p>No, by Ariane Mézard</p>

#### [ Kevin Buzzard (Apr 04 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124627096):
<p>Our progress so far is a new empty repository, and Kenny wrote some stuff about valuations and then found he didn't have push access.</p>

#### [ Kevin Buzzard (Apr 04 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124627162):
<p>I think that claiming that we "did" schemes but not even being able to construct one example is not such a great advertisement, so when I write Lean code I typically try and fix this problem. We are nearly there. I broke the problem down into three parts; part (3) is basically done, part (1) Chris Hughes has nearly finished and part (2) should be easy (and I will start on it soon, hopefully). When we can prove that an affine scheme is a scheme I will get back to perfectoid spaces.</p>

#### [ Kevin Buzzard (Apr 04 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124627166):
<blockquote>
<p>by thomas hales?</p>
</blockquote>
<p>Kenny, I don't think Tom Hales knows too much about perfectoid spaces.</p>

#### [ Patrick Massot (Apr 04 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124633933):
<p>I was sitting next to Fontaine during that talk and, according to him, Ariane also doesn't know much about perfectoid spaces.</p>

#### [ Patrick Massot (Apr 04 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124633945):
<p>Which probably means we are lucky Mézard gave this talk instead of Fontaine <span class="emoji emoji-1f604" title="smile">:smile:</span></p>

#### [ Patrick Massot (Apr 04 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124633959):
<p>Also, I didn't tell Fontaine about schemes without example</p>

#### [ Patrick Massot (Apr 04 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124633963):
<p>But I confess I told this story to François Charles a couple of days ago</p>

#### [ Patrick Massot (Apr 04 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124634012):
<p>He agrees the fact that affine schemes are schemes is not trivial, but still disapproves having defined schemes with no example</p>

#### [ Patrick Massot (Apr 04 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124634029):
<p>During that inauguration thing I also got the opportunity of chatting a bit with Christine Paulin (the dean of my university, who was involved in the theoretical foundations of Coq).</p>

#### [ Patrick Massot (Apr 04 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124634194):
<p>Then a colleague asked me why I was talking to her, and I may have found one new recruit for Lean</p>

#### [ Kevin Buzzard (Apr 04 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124638886):
<blockquote>
<p>Which probably means we are lucky Mézard gave this talk instead of Fontaine <span class="emoji emoji-1f604" title="smile">:smile:</span></p>
</blockquote>
<p>Anyone who wants to hear Fontaine's opinion can just read his Sem Bourbaki :-)</p>

#### [ Patrick Massot (Apr 04 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124642522):
<p>I once opened this Bourbaki seminar and decided it was not written for me <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Patrick Massot (Apr 04 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124642590):
<p>But, to be honest, I don't think Fontaine would say the Bourbaki I wrote about flexibility of contact structures in higher dimensions was written for him.</p>


{% endraw %}
