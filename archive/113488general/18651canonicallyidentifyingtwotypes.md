---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/18651canonicallyidentifyingtwotypes.html
---

## Stream: [general](index.html)
### Topic: ["canonically" identifying two types](18651canonicallyidentifyingtwotypes.html)

---


{% raw %}
#### [ Kevin Buzzard (Apr 27 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125765228):
<p>How can I beef up "equiv" into "canonical isomorphism"?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125765384):
<p>I think that's my question.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125765424):
<p>I will formulate something a bit more precise in a sec.</p>

#### [ Mario Carneiro (Apr 27 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125765431):
<p>Q1: what does that mean? Is "isomorphism" sufficient?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768206):
<p>The proof of <code>funext</code> uses quot.sound</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768208):
<p>but if we restrict to two types in the same universe</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768222):
<div class="codehilite"><pre><span></span>  <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">f₁</span> <span class="n">f₂</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">β</span> <span class="n">x</span><span class="o">},</span>
    <span class="o">(</span><span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">f₁</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">f₂</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="n">f₁</span> <span class="bp">=</span> <span class="n">f₂</span>
</pre></div>

#### [ Kevin Buzzard (Apr 27 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768229):
<p>so a slightly weaker result</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768230):
<p>can one prove this without quot.sound?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768288):
<p>I'm trying to work out what a mathematician means when they say that two objects are "canonically isomorphic".</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768292):
<p>To coin a phrase, it's like pornography.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768294):
<p>You know it when you see it.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768300):
<p>I have not yet found a formulation that I like in dependent type theory.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768308):
<p>and I think that this is an underlying source of some of my frustrations in trying to do mathematics in Lean.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768310):
<p>Here's a probably much easier question:</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768312):
<p>what's the inverse of funext called?</p>

#### [ Kenny Lau (Apr 27 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768335):
<p><code>congr_fun</code></p>

#### [ Kenny Lau (Apr 27 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768354):
<p>wait, inverse not converse</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768366):
<p>that's what I wanted</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768367):
<p>no axioms</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768368):
<p>different universes</p>

#### [ Kenny Lau (Apr 27 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768378):
<p>inverse?</p>

#### [ Kenny Lau (Apr 27 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768380):
<p>not A implies not B?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768381):
<p>Is it possible to express the notion that two types are "the same" without ever mentioning any terms?</p>

#### [ Kenny Lau (Apr 27 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768383):
<p><code>==</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768388):
<p>Kenny you answered my question</p>

#### [ Kenny Lau (Apr 27 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768435):
<p>inverse is <code>mt \o congr_fun</code> :P</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768436):
<p>Here are two notions of being "close to each other in type theory", which in my mind are both certainly implied by being "the same".</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768448):
<div class="codehilite"><pre><span></span><span class="kn">universe</span> <span class="n">zfc</span>
<span class="c1">--#print extfun_app</span>

<span class="c1">-- Here is a notion from dependent type theory.</span>
<span class="c">/-</span><span class="cm">- `α ≃ β` is the type of functions from `α → β` with a two-sided inverse. -/</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">zfc</span><span class="o">}</span>

<span class="kn">structure</span> <span class="n">equiv</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">zfc</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">zfc</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">to_fun</span>    <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span>
<span class="o">(</span><span class="n">inv_fun</span>   <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span>
<span class="o">(</span><span class="n">left_inv</span>  <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">left_inverse</span> <span class="n">inv_fun</span> <span class="n">to_fun</span><span class="o">)</span>
<span class="o">(</span><span class="n">right_inv</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">right_inverse</span> <span class="n">inv_fun</span> <span class="n">to_fun</span><span class="o">)</span>


<span class="kn">variable</span> <span class="o">(</span><span class="n">to_fun</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span>
<span class="kn">variable</span> <span class="o">(</span><span class="n">inv_fun</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span>

<span class="bp">#</span><span class="n">reduce</span> <span class="n">function</span><span class="bp">.</span><span class="n">left_inverse</span> <span class="n">inv_fun</span> <span class="n">to_fun</span>
<span class="c1">-- ∀ (x : α), to_fun (inv_fun x) = x</span>
<span class="c1">-- note round brackets -- explicitly demand the term</span>

<span class="bp">#</span><span class="n">reduce</span> <span class="n">function</span><span class="bp">.</span><span class="n">right_inverse</span> <span class="n">inv_fun</span> <span class="n">to_fun</span>
<span class="c1">-- ∀ (x : β), to_fun (inv_fun x) = x</span>
<span class="c1">-- note round brackets -- explicitly demand the term</span>

<span class="c1">-- Here is a notion from category theory, translated into dependent type theory.</span>
<span class="c">/-</span><span class="cm">- The notion of being isomorphic in a category  -/</span>
<span class="kn">structure</span> <span class="n">isom</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">zfc</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">zfc</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">to_fun</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span>
<span class="o">(</span><span class="n">inv_fun</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span>
<span class="o">(</span><span class="n">left_inv</span> <span class="o">:</span> <span class="n">inv_fun</span> <span class="err">∘</span> <span class="n">to_fun</span> <span class="bp">=</span> <span class="n">id</span><span class="o">)</span>
<span class="o">(</span><span class="n">right_inv</span> <span class="o">:</span> <span class="n">to_fun</span> <span class="err">∘</span> <span class="n">inv_fun</span> <span class="bp">=</span> <span class="n">id</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Apr 27 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768450):
<p>I have stuck to one universe</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768463):
<p>because I am a traditionalist</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768494):
<p>Why does Lean prefer <code>equiv</code> (which is in core Lean) to <code>isom</code>?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768495):
<p>Is <code>isom</code> in there somewhere?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768496):
<p>These structures are canonically isomorphic, but I don't know the definition of canonically isomorphic</p>

#### [ Kenny Lau (Apr 27 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768502):
<p>because <code>equiv</code> is more usable</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768503):
<p>but in dependent type theory the only way I know to construct bijective maps between them is using quot.sound</p>

#### [ Kenny Lau (Apr 27 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768504):
<p>Just look at my proof in the other thread</p>

#### [ Kenny Lau (Apr 27 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768505):
<p>before and after changing composition equality</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768508):
<p>Is it just universally true that equiv is better than isom?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768548):
<p>I don't know what other thread you're talking about.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768549):
<p>But I would genuinely be interested to know.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768552):
<p>My memory is not what it was.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768576):
<p>Anyway, I was wondering whether if one stuck to one universe, whether the restricted funext, which sounds to me like it could logically be a strictly weaker assertion, could be proved without the axiom.</p>

#### [ Kenny Lau (Apr 27 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768619):
<p><a href="#narrow/stream/113488-general/topic/proof.20of.20the.20five.20lemma" title="#narrow/stream/113488-general/topic/proof.20of.20the.20five.20lemma">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof.20of.20the.20five.20lemma</a></p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768685):
<p>Mario, I ultimately want to formalise some possibly specialised notion of being canonically isomorphic, which I can use to do amazing rewrites which a mathematician does all the time but which I find difficult to do in dependent type theory. My problem in dependent type theory is that I sometimes run into terms which are not definitionally equal, but which are "only" canonically isomorphic.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768686):
<p>Because I am facing quite a tedious job otherwise</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768742):
<p>I think I want to make a new structure which is more useful to me than definitional equivalence.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768743):
<p>It is not Lean's <code>=</code> because I want it to apply to terms of different types.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768788):
<p>and I am quite happy to restrict to objects within one universe</p>

#### [ Kenny Lau (Apr 27 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768795):
<p>why don't you just quotient everything with equiv</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768899):
<p>Wow, props can be equal : <code>@eq</code> is defined on <code>Sort u_1</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768902):
<p>Is that concept used?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768904):
<p>being canonically isomorphic only applies to types.</p>

#### [ Kenny Lau (Apr 27 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768943):
<blockquote>
<p>Is that concept used?</p>
</blockquote>
<p>a lot</p>

#### [ Kenny Lau (Apr 27 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768944):
<p>but mostly in <code>simp</code></p>

#### [ Kenny Lau (Apr 27 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768945):
<p><code>simp</code> rewrites Props</p>

#### [ Kenny Lau (Apr 27 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125768948):
<p>using <code>propext</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769002):
<p>Is this in Lean or mathlib:</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769003):
<p><code>instance group_of_equiv [group α] (H : equiv α β) : group β := sorry</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769014):
<p>If alpha and beta are canonically isomorphic, then any group structure on alpha trivially gives you a group structure on beta, any mathematician knows that.</p>

#### [ Scott Morrison (Apr 27 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769069):
<p>I am slowly coming around to the opinion that "canonical" as used by mathematicans doesn't actually mean much, but is instead code for "we both know what is going on, and I'm just confirming that you one you have in mind is probably the one I have in mind too".</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769113):
<p><code>instance set_equiv_of_equiv (H : equiv α β) : equiv (set α) (set β) := sorry</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769114):
<p>doesn't typecheck</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769115):
<p><code>equiv</code> is not a class</p>

#### [ Kevin Buzzard (Apr 27 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769125):
<p>but if <code>\a</code> and <code>\b</code> are canonically isomorphic, then so are their power sets -- any mathematician knows that.</p>

#### [ Scott Morrison (Apr 27 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769131):
<p>We could make <code>equiv</code> a class, and have the convention that we'll only even make instances that "every mathematician knows is the right one".</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769182):
<p>But do I want to restrict myself like that?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769184):
<p>I am not sure</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769185):
<p>There are two abelian groups which show up in the Langlands Philosophy</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769188):
<p>And the Langlands Philosophy says that they are canonically isomorphic</p>

#### [ Scott Morrison (Apr 27 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769195):
<p>Well... an isomorphism from <code>a</code> to <code>b</code> gives an isomorphism from <code>2^a</code> to <code>2^b</code>, sure. If you bless one as canonical, I guess that blesses the result as canonical too.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769198):
<p>In fact, more generally there are two non-abelian groups which show up and Langlands conjectures that they are canonically isomorphic, and this is one of the reasons that we call it philosophy sometimes -- it is not quite mathematics.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769202):
<p>But back to the abelian groups</p>

#### [ Scott Morrison (Apr 27 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769206):
<p>But by that do you just mean that there's a particularly interesting/sensible isomorphism between them, and the point is not to say "these are isomorphic", but "this is an isomorphism between ..."?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769246):
<p>Mathematicians have written down not just one, but two canonical isomorphisms between these groups!</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769247):
<p>And they're different!</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769249):
<p>One is called "global class field theory normalised so that uniformisers become identified with geometric Frobenius"</p>

#### [ Scott Morrison (Apr 27 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769255):
<p>So what does canonical mean here? (I am not really confident in my skepticism of the word "canonical". I am happy to come back to the fold if the story is good.)</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769256):
<p>and the other is called "global class field theory normalised so that uniformisers become identified with arithmetic Frobenius"</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769260):
<p>The two canonical isomorphisms between the groups are related. If we write the group law multiplicatively, as is standard,</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769261):
<p>then if one of them is f(x)=y</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769263):
<p>the other is f(x)=1/y</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769303):
<p>and mathematicians choose at random which one to use</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769305):
<p>and some even sometimes forget to say which one</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769308):
<p>perhaps because the one they used was the most common one when the paper was written</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769321):
<p>So I am pretty sure I want to allow myself more than one canonical isomorphism between two objects</p>

#### [ Johan Commelin (Apr 27 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769721):
<p>So, here is Kevin's remark in a down to earth example: every abelian group has a canonical automorphism, and in fact, it has two of those: the identity, and the map <code>a \mapsto -a</code>.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769731):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> -- you wrote my function! Many thanks!</p>

#### [ Johan Commelin (Apr 27 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769733):
<p>Of course, in the case of automorphisms, we agree that <code>id</code> is slightly more canonical then the -1 map</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769777):
<p>But these were two different groups</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769778):
<p>and this has caused confusion in the mathematical community</p>

#### [ Johan Commelin (Apr 27 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769779):
<p>Exactly</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769781):
<p>I think that's interesting.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769782):
<p>Nowadays people are careful to state which of the normalisations they are using</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769789):
<p>and unfortunately, and perhaps counter-intuitively, it can sometimes be a little tricky to figure out how to translate the statements of theorems proved using one convention into the analogous statements about the same objects had we used the other convention in the paper.</p>

#### [ Johan Commelin (Apr 27 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769790):
<p>But Kevin, if we go for the restricted version of canonical first. The one that Scott suggested. That would already be incredibly helpful, right?</p>

#### [ Kenny Lau (Apr 27 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769831):
<blockquote>
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> -- you wrote my function! Many thanks!</p>
</blockquote>
<p>which function?</p>

#### [ Johan Commelin (Apr 27 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769835):
<p>If there is one 'blessed' isomorphism, it can be traced through al sorts of constructions, and induce 'blessed' equivalences/isomorphism between other objects</p>

#### [ Johan Commelin (Apr 27 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769837):
<p>Like with power sets, or group structures, etc...</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769838):
<blockquote>
<p>But by that do you just mean that there's a particularly interesting/sensible isomorphism between them, and the point is not to say "these are isomorphic", but "this is an isomorphism between ..."?</p>
</blockquote>
<p>I am quite happy to state the isomorphism. But what I want from it is a huge quota of free constructions and proofs.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769894):
<p>I want <code>canonical_isomorphism</code> to extend (possibly a restricted universe version of) <code>equiv</code></p>

#### [ Johan Commelin (Apr 27 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769898):
<p>At the Lean wizards: Kevin is pointing out an incredibly important thing. As in, it is a difference in kind, not just a difference in degree.</p>

#### [ Johan Commelin (Apr 27 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769901):
<p>It will give super-linear improvements in the de Bruijn factor.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769922):
<p>and I want functions like</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769942):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">group_of_equiv</span> <span class="o">[</span><span class="n">group</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">canonically_isomorphic</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">group</span> <span class="n">β</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kenny Lau (Apr 27 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769947):
<p>transport of structure</p>

#### [ Kenny Lau (Apr 27 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769951):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> maybe you could automate this?</p>

#### [ Johan Commelin (Apr 27 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769952):
<p>I personally feel (but I'm a novice) that this is one of the big road blocks for formalisation of a lot of maths in the algebraic geometry corner</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769959):
<p>I have this big Pokemon to kill</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769960):
<p>called proof that an affine scheme is a scheme</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769962):
<p>and it is now in its final stage</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769967):
<p>and I want to destroy it with a one liner like this</p>

#### [ Chris Hughes (Apr 27 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769968):
<p>What happened to Kenny's idea of quotienting by isomorphism?</p>

#### [ Kenny Lau (Apr 27 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125769969):
<p>Chris Hughes appears</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770009):
<p>I don't know how to implement that</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770012):
<p>Did you see my "three lemma" Chris?</p>

#### [ Johan Commelin (Apr 27 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770014):
<p>What exactly does Kenny mean by "quotienting by isomorphism"?</p>

#### [ Johan Commelin (Apr 27 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770016):
<p>Because that might be to crude...</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770017):
<p>I want to prove that if <code>A -&gt; B -&gt; C</code> is exact and we are given isomorphisms <code>A -&gt; A'</code> and <code>B -&gt; B'</code> and <code>C -&gt; C'</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770027):
<p>then there is a completely obvious new exact sequence <code>A' -&gt; B' -&gt; C'</code></p>

#### [ Kenny Lau (Apr 27 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770029):
<p>I already proved it</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770030):
<p>I know</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770034):
<p>but i don't want you to spend 70 lines proving it</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770037):
<p>I want to to agree with me that it is obvious</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770038):
<p>and hence is only worth one line</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770086):
<p>because a mathematician is capable of replacing <code>B</code> with the canonically isomorphic <code>B'</code> in one line</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770090):
<p>so I can prove the theorem in 3 lines</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770092):
<p>and I don't see anything wrong with my proof</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770095):
<p>at every stage the next line is "do the obvious thing"</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770106):
<blockquote>
<p>but i don't want you to spend 70 lines proving it</p>
</blockquote>
<p>... by which I mean</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770108):
<p>thank you very much Kenny for proving the result for me</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770112):
<p>and don't you think it's interesting that it took 70 lines</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770117):
<p>but for the purposes of this thread I want 3 lines</p>

#### [ Kenny Lau (Apr 27 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770160):
<p>lol</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770163):
<p>I want to <code>rw [H : canonically_isomorphic A A']</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770164):
<p>and then you can guess the rest</p>

#### [ Johan Commelin (Apr 27 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770166):
<p><code>[...] := by repeat {transport_de_structure}</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770173):
<p>This is exactly another one of those concepts which I have been interested in all my life but have only really now found the language to talk about them in</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770225):
<p>and perhaps this is very difficult to do in dependent type theory</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770229):
<p>because replacing <code>f A</code> with <code>f A'</code> can be quite complicated in general</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770232):
<p>but the point is that <code>A</code> and <code>A'</code> are <em>mathematical objects</em></p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770235):
<p>not these stupid general types</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770246):
<p>and so what I am hoping is that for a possibly restricted class of types there is some powerful relation on them</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770285):
<p>called "canonically isomorphic"</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770291):
<p>which you construct with functions in both directions, proofs that the composites are the identity either way (as in equiv not isom), and a little bit of extra magic</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770294):
<p>possibly</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770300):
<p>and then for hopefully a class of types including the kind of types showing up in mathematics</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770348):
<p>a lot of stuff can be moved around painlessly, substituting one type for a canonically isomorphic one.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770352):
<p>So who fancies proving <code>equiv A B -&gt; scheme A -&gt; scheme B</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770366):
<p>Wait, for what generality is this true?</p>

#### [ Johan Commelin (Apr 27 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770369):
<p>Hmmm, Kevin, I think there are two things at play</p>

#### [ Johan Commelin (Apr 27 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770417):
<p>There is functoriality, and transport de structure</p>

#### [ Johan Commelin (Apr 27 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770419):
<p>and they are related, but slightly different</p>

#### [ Johan Commelin (Apr 27 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770423):
<p>I don't know exactly how to explain the difference</p>

#### [ Johan Commelin (Apr 27 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770428):
<p>(And maybe they actually are not)</p>

#### [ Chris Hughes (Apr 27 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770430):
<p>Is this totally disgusting?</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">isom</span> <span class="o">(</span><span class="n">G</span> <span class="n">H</span> <span class="o">:</span> <span class="err">Σ</span> <span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">,</span> <span class="n">group</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">G</span><span class="bp">.</span><span class="mi">1</span> <span class="err">≃</span> <span class="n">H</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span>
<span class="o">(</span><span class="n">to_fun_hom</span> <span class="o">:</span> <span class="bp">@</span><span class="n">is_group_hom</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">G</span><span class="bp">.</span><span class="mi">2</span> <span class="n">H</span><span class="bp">.</span><span class="mi">2</span> <span class="n">f</span><span class="bp">.</span><span class="n">to_fun</span><span class="o">)</span>
<span class="o">(</span><span class="n">inv_fun_hom</span> <span class="o">:</span> <span class="bp">@</span><span class="n">is_group_hom</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span><span class="bp">.</span><span class="mi">2</span> <span class="n">G</span><span class="bp">.</span><span class="mi">2</span> <span class="n">f</span><span class="bp">.</span><span class="n">inv_fun</span><span class="o">)</span>

<span class="n">def</span> <span class="n">is_isom</span> <span class="o">(</span><span class="n">G</span> <span class="n">H</span> <span class="o">:</span> <span class="err">Σ</span> <span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">,</span> <span class="n">group</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">nonempty</span> <span class="o">(</span><span class="n">isom</span> <span class="n">G</span> <span class="n">H</span><span class="o">)</span>
</pre></div>

#### [ Scott Morrison (Apr 27 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770537):
<p>Really you want to prove <code>equiv A B -&gt; equiv (scheme A) (scheme B)</code>.</p>

#### [ Johan Commelin (Apr 27 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770539):
<p>Chris, but what does it do?</p>

#### [ Scott Morrison (Apr 27 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770580):
<p>Or even better: <code>scheme</code> is an endofunctor of the category of types and equivalences.</p>

#### [ Johan Commelin (Apr 27 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770581):
<p>Isn't that too general? You need some ring structures flying around, right?</p>

#### [ Scott Morrison (Apr 27 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770633):
<p>I'm not sure what you mean, Johan. How would rings come into the picture? We're just doing abstract nonsense with types here.</p>

#### [ Chris Hughes (Apr 27 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770638):
<p>If you quotient then you can rw. That's the idea. But it might be completely useless.</p>

#### [ Johan Commelin (Apr 27 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770639):
<p>Scott, never mind, you are right</p>

#### [ Johan Commelin (Apr 27 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770686):
<p>Ok, so then we want your proposed theorem to come for free. Does that make sense?</p>

#### [ Johan Commelin (Apr 27 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770688):
<p>And then, if we have an actual equivalence between A and B, we get an equivalence between (scheme A) and (scheme B) for free</p>

#### [ Johan Commelin (Apr 27 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770702):
<p>And I guess it comes for free for all endofunctors, and endofunctors compose</p>

#### [ Johan Commelin (Apr 27 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770708):
<p>So we might need to mark lots of definitions with [endofunctor]</p>

#### [ Johan Commelin (Apr 27 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770751):
<p>And maybe then we are happy?</p>

#### [ Scott Morrison (Apr 27 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770752):
<p>So... which functions <code>F : Type × ... × Type → Type</code> extend to endofunctors of <code>Equiv</code> (the category of types and equivalences)?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770754):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span>

<span class="kn">theorem</span> <span class="n">over_optimistic</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="kt">Type</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span>
<span class="n">equiv</span> <span class="o">(</span><span class="n">F</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Scott Morrison (Apr 27 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770755):
<p>Most things I can think of...</p>

#### [ Kenny Lau (Apr 27 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770758):
<blockquote>
<p>Is this totally disgusting?</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">isom</span> <span class="o">(</span><span class="n">G</span> <span class="n">H</span> <span class="o">:</span> <span class="err">Σ</span> <span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">,</span> <span class="n">group</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">G</span><span class="bp">.</span><span class="mi">1</span> <span class="err">≃</span> <span class="n">H</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span>
<span class="o">(</span><span class="n">to_fun_hom</span> <span class="o">:</span> <span class="bp">@</span><span class="n">is_group_hom</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">G</span><span class="bp">.</span><span class="mi">2</span> <span class="n">H</span><span class="bp">.</span><span class="mi">2</span> <span class="n">f</span><span class="bp">.</span><span class="n">to_fun</span><span class="o">)</span>
<span class="o">(</span><span class="n">inv_fun_hom</span> <span class="o">:</span> <span class="bp">@</span><span class="n">is_group_hom</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span><span class="bp">.</span><span class="mi">2</span> <span class="n">G</span><span class="bp">.</span><span class="mi">2</span> <span class="n">f</span><span class="bp">.</span><span class="n">inv_fun</span><span class="o">)</span>

<span class="n">def</span> <span class="n">is_isom</span> <span class="o">(</span><span class="n">G</span> <span class="n">H</span> <span class="o">:</span> <span class="err">Σ</span> <span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">,</span> <span class="n">group</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">nonempty</span> <span class="o">(</span><span class="n">isom</span> <span class="n">G</span> <span class="n">H</span><span class="o">)</span>
</pre></div>


</blockquote>
<p>the last parameter is redundant</p>

#### [ Kenny Lau (Apr 27 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770760):
<p>proof: exercise for M1P2</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770764):
<p>Chris -- I know it can be done! My point is that I should not be wasting my time having to do it!</p>

#### [ Scott Morrison (Apr 27 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770830):
<p>I need someone who actually groks type theory to give a counterexample to Kevin's <code>over_optimistic</code>. :-)</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770836):
<p>So my <code>over_optimistic</code> question is a question for the CS people. Presumably that is not provable. I am very unfussed about you using any of Lean's axioms here. Is</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770840):
<p>...yeah what Scott said</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770845):
<p>The thing is that for the types I am most interested in when I am doing mathematics</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770847):
<p>like groups and rings</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770851):
<p>the proof is "it's trivial"</p>

#### [ Scott Morrison (Apr 27 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770891):
<p>(and lists and manifolds and braided monoidal categories)</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770892):
<p>exactly</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770897):
<p>I have run into a ridiculous issue in my schemes code and Kenny has dug me out of a hole with 70 lines of code which no human should have to write</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770902):
<p>and indeed no mention is made of the argument in the stacks project</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770903):
<p>which is written in ZFC</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770905):
<p>This is an area where translation to DTT seems hard</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770949):
<p>currently</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770951):
<p>I have some "canonically isomorphic" objects</p>

#### [ Kevin Buzzard (Apr 27 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770954):
<p>and whilst I don't know what that means</p>

#### [ Johan Commelin (Apr 27 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770961):
<p>Hmmmz where is <code>left_inverse</code> defined again?</p>

#### [ Scott Morrison (Apr 27 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770962):
<p>I fear that someone is about to come along and say: "HoTT!"</p>

#### [ Johan Commelin (Apr 27 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770966):
<p>Yes, I was about to do that</p>

#### [ Johan Commelin (Apr 27 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770974):
<p>For 30 minutes I had the urge to say that I think this is <em>exactly</em> what Voevodsky tried to solve. His answer was HoTT</p>

#### [ Scott Morrison (Apr 27 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125770976):
<p>Voevodsky said things like: "the point is you can actually say what you mean by transport of structure"...</p>

#### [ Kenny Lau (Apr 27 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771023):
<blockquote>
<p>Hmmmz where is <code>left_inverse</code> defined again?</p>
</blockquote>
<p>ctrl shift f</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771039):
<p>I do know that from the fact that they are all canonically isomorphic that I can prove all the hypotheses in Kenny's theorem</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771040):
<p>Kenny has taken the problem down one level</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771041):
<p>there is a really weird part of the argument actually, which is worth mentioning here and is evidence to suggest that I am living in a dream world.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771042):
<p>I have B canonically isomorphic to B' (I have the maps)</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771043):
<p>I have A canonically isomorphic to A' (in the sense that I have a structure which is an approximation to such a thing, and will do for now)</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771044):
<p>but the proofs are going to be really tedious</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771048):
<p>and I can prove that the diagram commutes</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771087):
<p>my chat is being garbled</p>

#### [ Scott Morrison (Apr 27 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771098):
<p>(So which bits are by Kenny, and which by "Kevin"? :-)</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771103):
<p>but one of the arguments that it commutes is : ring hom x is the same as ring hom x' because they're both the unique ring hom</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771104):
<p>and similarly ring hom y = ring hom y'</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771111):
<p>and now we deduce that group hom x+y equals group hom x'+y'</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771114):
<p>not from the universal property itself, in some sense</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771116):
<p>well, from some shadow of the universal property applied to +</p>

#### [ Scott Morrison (Apr 27 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771226):
<p>Does anyone know how things like <code>@[derive decidable_eq]</code> work?</p>

#### [ Scott Morrison (Apr 27 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771235):
<p>Perhaps we can have <code>@[derive transportable]</code>, so when you write</p>

#### [ Scott Morrison (Apr 27 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771245):
<div class="codehilite"><pre><span></span>@[derive transportable]
structure Scheme (a : Type) := ...
</pre></div>

#### [ Scott Morrison (Apr 27 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771290):
<p>we automatically get an instance of <code>transportable Scheme</code>, which just means Scheme is functorial w.r.t equiv.</p>

#### [ Johan Commelin (Apr 27 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771300):
<p>That was what I was hinting at with the [endofunctor] annotations</p>

#### [ Johan Commelin (Apr 27 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771303):
<p>But: I don't know lean...</p>

#### [ Scott Morrison (Apr 27 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771306):
<p>ah, I see!</p>

#### [ Scott Morrison (Apr 27 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771310):
<p>Good suggestion. :-)</p>

#### [ Johan Commelin (Apr 27 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771311):
<p>Well, your suggestion is clearly more fleshed out.</p>

#### [ Sebastian Ullrich (Apr 27 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771358):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> Take a look at <a href="https://github.com/leanprover/lean/blob/f59c2f0ef59fdc1833b6ead6adca721123bd7932/library/init/meta/derive.lean#L19-L22" target="_blank" title="https://github.com/leanprover/lean/blob/f59c2f0ef59fdc1833b6ead6adca721123bd7932/library/init/meta/derive.lean#L19-L22">https://github.com/leanprover/lean/blob/f59c2f0ef59fdc1833b6ead6adca721123bd7932/library/init/meta/derive.lean#L19-L22</a></p>

#### [ Johan Commelin (Apr 27 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771419):
<blockquote>
<p>we automatically get an instance of <code>transportable Scheme</code>, which just means Scheme is functorial w.r.t equiv.</p>
</blockquote>
<p>In other words, that <code>over_optimistic Scheme</code> is a theorem, right?</p>

#### [ Scott Morrison (Apr 27 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771433):
<p>Well, even more than just <code>over_optimistic Scheme</code>.</p>

#### [ Scott Morrison (Apr 27 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771479):
<p>We want to know that the <code>equiv</code>s  you get at the <code>Scheme</code> level compose in the same way they did on the original types.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771491):
<p>So let's not jump the gun -- can you prove if A equiv B then a ring on A gives a ring on B?</p>

#### [ Kenny Lau (Apr 27 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771503):
<p>in 70 lines?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771507):
<p>:-)</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771513):
<p>Kenny I'm sure you could do it in ten</p>

#### [ Scott Morrison (Apr 27 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771516):
<p>Sure we can do it on <code>ring</code>, or any given example. (Or rather: Kenny can :-)</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771559):
<p>I mean</p>

#### [ Scott Morrison (Apr 27 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771560):
<p>but it seems rather likely that the computer can do it too, by looking at the structure fields, and working out where the parameter types appear, and plugging appropriate copies of the equivalence or its inverse everywhere.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771565):
<p>right</p>

#### [ Scott Morrison (Apr 27 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771569):
<p>For many simple types (list, ring, ...) this is certainly going to work.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771573):
<p>I mean "prove it without ploughing through the axioms"</p>

#### [ Scott Morrison (Apr 27 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771584):
<p>You mean ploughing through the axioms of "ring"?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771586):
<p>yes, I want a one-line proof</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771624):
<p>that if A equiv B then a ring structure on A gives one on B</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771629):
<p>does that exist?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771631):
<p>Could it be a tactic?</p>

#### [ Scott Morrison (Apr 27 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771632):
<p>No, I think in general there just isn't a one-line proof, that would work unchanged if your substituted ring for group.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771633):
<p>Is it already a theorem?</p>

#### [ Scott Morrison (Apr 27 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771634):
<p>but yes, it can easily be a tactic</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771636):
<p>and the tactic would sometimes fail?</p>

#### [ Scott Morrison (Apr 27 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771637):
<p>and it can be one that's easy to use: just add @[derive transportable] in front of every structure.</p>

#### [ Scott Morrison (Apr 27 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771643):
<p>and yes, conceivably it might sometime fail, but I don't see where yet</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771644):
<p>I have no understanding at all the moment anyone says <code>transportable</code></p>

#### [ Scott Morrison (Apr 27 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771653):
<p>(In fact, I'm really upset that I don't see where it might fail. I'll buy anyone a beer who explains a counterexample to Kevin's <code>over_optimistic</code> :-)</p>

#### [ Scott Morrison (Apr 27 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771654):
<p>Sorry, I made up the word <code>transportable</code> just now.</p>

#### [ Kenny Lau (Apr 27 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771695):
<p>heh?</p>

#### [ Kenny Lau (Apr 27 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771702):
<p>I mean, f can send int to empty and nat to unit</p>

#### [ Scott Morrison (Apr 27 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771703):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>, do you understand what I mean by "the category of types and equivalences"?</p>

#### [ Kenny Lau (Apr 27 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771706):
<p>so int and nat are equivalent but empty and unit are not</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771709):
<p>not yet</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771711):
<p>Maybe I do understand</p>

#### [ Kevin Buzzard (Apr 27 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771712):
<p>Are the objects all in one universe?</p>

#### [ Scott Morrison (Apr 27 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771719):
<p>But Kenny, how would you actually construct such an <code>f</code> in Lean?</p>

#### [ Johan Commelin (Apr 27 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771721):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> Just write down the definition of <code>structure transportable (F : Type* \to Type*)</code></p>

#### [ Johan Commelin (Apr 27 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771725):
<p>/me has never written a structure in Lean before, otherwise he would do it</p>

#### [ Johan Commelin (Apr 27 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771726):
<p>Or should it be a class?</p>

#### [ Johan Commelin (Apr 27 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771767):
<p>So that <code>@[derive]</code> will automagically create instances of that class</p>

#### [ Johan Commelin (Apr 27 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771784):
<p>/me goes back to TPIL</p>

#### [ Scott Morrison (Apr 27 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771827):
<div class="codehilite"><pre><span></span>class transportable (f : Type u → Type u) :=
(on_equiv : Π {α β : Type u} (e : equiv α β), equiv (f α) (f β))
(on_refl  : Π (α : Type u), on_equiv (equiv.refl α) = equiv.refl (f α))
(on_trans : Π {α β γ : Type u} (d : equiv α β) (e : equiv β γ), on_equiv (equiv.trans d e) = equiv.trans (on_equiv d) (on_equiv e))
</pre></div>

#### [ Scott Morrison (Apr 27 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771839):
<p>and I claim that <span class="user-mention" data-user-id="110026">@Simon Hudon</span> knows how to implement @[derive transportable] for many type constructors. :-)</p>

#### [ Johan Commelin (Apr 27 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771889):
<p>Yes, that would be very cool</p>

#### [ Scott Morrison (Apr 27 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771933):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>, this is just saying we have a category which I'll call <code>Equiv</code>, whose objects are <code>Type u</code> for some universe <code>u</code>, and the homs between <code>\a</code> and <code>\b</code> are just <code>equiv \a \b</code>. Then a function  <code>f : Type u -&gt; Type u</code> is "transportable" exactly if it extends to a functor <code>Equiv \to Equiv</code> (i.e. <code>f</code> is what that functor does on objects).</p>

#### [ Johan Commelin (Apr 27 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771950):
<p>Can we have different universes?</p>

#### [ Scott Morrison (Apr 27 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771951):
<p>sure.</p>

#### [ Johan Commelin (Apr 27 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771952):
<p>In other words, <code>f</code> need not be "strictly endo"</p>

#### [ Scott Morrison (Apr 27 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125771964):
<p>(It's important that all the universes in classes are visible in the class parameters, but here they would be visible in the parameter <code>f : Type u -&gt; Type v</code>.)</p>

#### [ Scott Morrison (Apr 27 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772036):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  --- I'm not at all sure if this is useful. It may be saying simple things in complicated ways, that don't actually solve your problems. But perhaps it does. (And if it does, I'm guessing automatically generating instances of <code>transportable</code> could be achieved within a few days (/weeks if Simon doesn't want to help :-)).</p>

#### [ Johan Commelin (Apr 27 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772091):
<blockquote>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">group_of_equiv</span> <span class="o">[</span><span class="n">group</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">canonically_isomorphic</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">group</span> <span class="n">β</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


</blockquote>
<p>It would solve things like this, if I'm not mistaken</p>

#### [ Simon Hudon (Apr 27 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772095):
<blockquote>
<p>and I claim that <span class="user-mention" data-user-id="110026">@Simon Hudon</span> knows how to implement @[derive transportable] for many type constructors. :-)</p>
</blockquote>
<p>Do you have a proof of that?</p>

#### [ Johan Commelin (Apr 27 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772098):
<p>Yes, you are working on it</p>

#### [ Scott Morrison (Apr 27 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772141):
<p>:-)</p>

#### [ Johan Commelin (Apr 27 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772144):
<p>And it seems that you get a beer if you can prove that you can't do it in one go...</p>

#### [ Scott Morrison (Apr 27 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772149):
<p>(Sorry, I don't mean to say things like this to pressure you into doing things. Just to express my gratitude for all your recent help! No good deed goes unpunished...)</p>

#### [ Johan Commelin (Apr 27 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772211):
<p>Learning how to write tactics and such is on my todo list</p>

#### [ Johan Commelin (Apr 27 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772214):
<p>But I first need to get two papers out of the door...</p>

#### [ Simon Hudon (Apr 27 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772215):
<p>(Haha! No worries! Can people hear us when we whisper in here?)</p>

#### [ Simon Hudon (Apr 27 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772225):
<p>Yeah and writing tutorials about it is on mine</p>

#### [ Simon Hudon (Apr 27 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772269):
<p>I can look into it. I still don't know much about <code>derive</code> but I need to understand it for <code>traversable</code>. I can kill two birds with one stone</p>

#### [ Chris Hughes (Apr 27 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772286):
<p>Would it help to make everything isomorphic to a type a type class, and then prove things about the class of isomorphic types? Might be completely stupid.</p>

#### [ Johan Commelin (Apr 27 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772496):
<p>Well, you loose track of different isomorphisms between the same to types</p>

#### [ Johan Commelin (Apr 27 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125772500):
<p>And that will create trouble down the road, I guess</p>

#### [ Simon Hudon (Apr 27 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773177):
<p>Type classes are really better when instances are unique. Lean does not enforce that idea but conceptually, if the type class is not unique, the instance is an implicit argument everywhere but the exact choice of instance makes a big difference.</p>

#### [ Simon Hudon (Apr 27 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773186):
<p>It's like you're omitting a central piece of information every time</p>

#### [ Johan Commelin (Apr 27 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773189):
<p>But for Scott's proposal, that would be the case, right?</p>

#### [ Simon Hudon (Apr 27 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773404):
<p>You mean the instance would be unique?</p>

#### [ Johan Commelin (Apr 27 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773683):
<p>I think so</p>

#### [ Johan Commelin (Apr 27 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773687):
<p>You derive an instance, right.</p>

#### [ Johan Commelin (Apr 27 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773694):
<p>So there is only one of them. And people just shouldn't define additional instances</p>

#### [ Simon Hudon (Apr 27 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773760):
<p>What if other instances could be useful?</p>

#### [ Simon Hudon (Apr 27 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773770):
<p>Sorry, I'm kind of jumping in the middle here so I'm missing some context</p>

#### [ Johan Commelin (Apr 27 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773771):
<p>Hmm, we only want to use the fact that the class is inhabited</p>

#### [ Johan Commelin (Apr 27 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773775):
<p>Ok, so this is the thing</p>

#### [ Simon Hudon (Apr 27 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773782):
<p>Is it meant to be used with type constructors like <code>list</code>?</p>

#### [ Johan Commelin (Apr 27 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773783):
<p>Say you have two types. <code>A</code> and <code>B</code></p>

#### [ Johan Commelin (Apr 27 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773790):
<p>and you know that <code>A</code> is a group. You also know <code>equiv A B</code></p>

#### [ Johan Commelin (Apr 27 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773794):
<p>Then we would like to know that <code>B</code> is also a group.</p>

#### [ Johan Commelin (Apr 27 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773799):
<p>And we want Lean to do this for us.</p>

#### [ Johan Commelin (Apr 27 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773858):
<p>So, after lots of discussions, Scott came up with a strategy.</p>

#### [ Johan Commelin (Apr 27 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773864):
<p>We define a class <code>transportable</code> (or some other name, but mathematicians know this fact as "transport of structure")</p>

#### [ Johan Commelin (Apr 27 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773868):
<p>And we tag lots of definitions with <code>@[derive transportable]</code></p>

#### [ Johan Commelin (Apr 27 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773873):
<p>And then, MAGIC!</p>

#### [ Johan Commelin (Apr 27 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773886):
<p>In particular, you can only derive transportable for things of type <code>Type u \to Type v</code></p>

#### [ Simon Hudon (Apr 27 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773944):
<p>In this case, that would be <code>group</code>, right?</p>

#### [ Johan Commelin (Apr 27 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773947):
<p>And if <code>f</code> and <code>g</code> are two things that are <code>transportable</code>, then we want <code>(f,g)</code> to also be transportable, by some fact that we hope <em>you</em> can prove</p>

#### [ Johan Commelin (Apr 27 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773955):
<p>Right, <code>group</code>, <code>ring</code> etc should be examples</p>

#### [ Simon Hudon (Apr 27 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773969):
<p>I see, I see. That actually seems like a good use of classes</p>

#### [ Johan Commelin (Apr 27 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773978):
<p>and if something is defined as a <code>structure</code>, hopefully we can also derive this from how its built.</p>

#### [ Simon Hudon (Apr 27 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125773986):
<p>I'll look into doing that. If I could have a use case, that would help a lot</p>

#### [ Johan Commelin (Apr 27 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774035):
<p>And so we only need some really basic things where we actually <em>prove</em> that we have an instance. The rest is done by <code>derive</code> and <em>us</em> putting annotations in mathlib.</p>

#### [ Johan Commelin (Apr 27 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774046):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> Is that a faithful representation of your ideas?</p>

#### [ Johan Commelin (Apr 27 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774143):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> The use case is that Kevin is now facing a goal that would follow from this (and probably tomorrow he has another dozen). A mathematician would spend at most 3 words to "prove" such a fact. Kenny needed 70 lines to prove this particular goal of Kevin. But a variant of that goal can pop up any time.</p>

#### [ Scott Morrison (Apr 27 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774155):
<p>Here's a mockup of what we want:</p>
<div class="codehilite"><pre><span></span>class canonical_equiv (α : Sort*) (β : Sort*) extends equiv α β.

class transportable (f : Type u → Type u) :=
(on_equiv : Π {α β : Type u} (e : equiv α β), equiv (f α) (f β))
(on_refl  : Π (α : Type u), on_equiv (equiv.refl α) = equiv.refl (f α))
(on_trans : Π {α β γ : Type u} (d : equiv α β) (e : equiv β γ), on_equiv (equiv.trans d e) = equiv.trans (on_equiv d) (on_equiv e))

-- Finally a command like: `initialize_transport group` would create the next two declarations automagically:

def group.transportable : transportable group := sorry
instance group.transport {α β : Type u} [R : group α] [e : canonical_equiv α β] : group β := (@transportable.on_equiv group group.transportable _ _ e.to_equiv).to_fun R
</pre></div>

#### [ Scott Morrison (Apr 27 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774206):
<p>The challenge is to implement the command <code>initialize_transport</code> (sounds like Star Trek! :-)</p>

#### [ Scott Morrison (Apr 27 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774254):
<p>It will need to inspect its argument, which will be something like <code>ring</code> or <code>list</code>, and create an instance of <code>transportable ring</code> or <code>transportable list</code>, etc.</p>

#### [ Scott Morrison (Apr 27 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774269):
<p>(i.e. fill in the <code>sorry</code> above)</p>

#### [ Scott Morrison (Apr 27 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774306):
<p>The final step of <code>initialize_transport</code> is trivial: just emit the final instance declaration above.</p>

#### [ Johan Commelin (Apr 27 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774314):
<p>Right, so <code>initialize_transport</code> (or <code>derive_transportable</code>) would look at <code>group</code> and say, oh, I know how to transport <code>mul</code> and <code>inv</code> and <code>one</code> from <code>A</code> to <code>B</code></p>

#### [ Scott Morrison (Apr 27 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774315):
<p>Exactly.</p>

#### [ Johan Commelin (Apr 27 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774323):
<p>Because those are just functions... and someone told me how to do that</p>

#### [ Scott Morrison (Apr 27 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774325):
<p>I don't have a strong sense of how hard that it. :-)</p>

#### [ Simon Hudon (Apr 27 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774327):
<p>Nice idea :)</p>

#### [ Simon Hudon (Apr 27 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774336):
<p>I think keep it as my treat today between writing sessions</p>

#### [ Scott Morrison (Apr 27 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774337):
<p>But basically the thing you hand to <code>initialize_transport</code> will usually just be some inductive type</p>

#### [ Johan Commelin (Apr 27 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774338):
<p>And then there are the axioms, and it should be able to transport their proof as well...</p>

#### [ Scott Morrison (Apr 27 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774379):
<p>(e.g. a structure)</p>

#### [ Johan Commelin (Apr 27 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774383):
<p>And now you want to "inductively" deduce that almost everything a mathematician like Kevin would define is an example of <code>transportable</code></p>

#### [ Scott Morrison (Apr 27 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774407):
<p>Yes: more advanced versions of <code>initialize_transport</code> will probably do some induction: notice that internal features have already been provided with instance of transportable, and make sure of that.</p>

#### [ Scott Morrison (Apr 27 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774420):
<p>I should sleep, but I'll try to think of examples of wanting to do that while I sleep. :-)</p>

#### [ Simon Hudon (Apr 27 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125774470):
<p>Awesome! That sounds like sweet dreams</p>

#### [ Johan Commelin (Apr 27 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125775365):
<p>Here are some more basics. But I think you already got the idea.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span> <span class="n">w</span>

<span class="n">class</span> <span class="n">transportable</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">on_equiv</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">α</span> <span class="n">β</span><span class="o">),</span> <span class="n">equiv</span> <span class="o">(</span><span class="n">f</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="n">β</span><span class="o">))</span>
<span class="o">(</span><span class="n">on_refl</span>  <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">),</span> <span class="n">on_equiv</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">refl</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">refl</span> <span class="o">(</span><span class="n">f</span> <span class="n">α</span><span class="o">))</span>
<span class="o">(</span><span class="n">on_trans</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">d</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">β</span> <span class="n">γ</span><span class="o">),</span> <span class="n">on_equiv</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">trans</span> <span class="n">d</span> <span class="n">e</span><span class="o">)</span> <span class="bp">=</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">on_equiv</span> <span class="n">d</span><span class="o">)</span> <span class="o">(</span><span class="n">on_equiv</span> <span class="n">e</span><span class="o">))</span>

<span class="c1">-- Our goal is an automagic proof of the following</span>
<span class="kn">theorem</span> <span class="n">group</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">:</span> <span class="n">transportable</span> <span class="n">group</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="c1">-- These we might need to define and prove by hand</span>
<span class="n">def</span> <span class="n">Const</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="n">punit</span>
<span class="n">def</span> <span class="n">Fun</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span><span class="o">,</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span>
<span class="n">def</span> <span class="n">Prod</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span><span class="o">,</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">β</span>
<span class="n">def</span> <span class="n">Swap</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span><span class="o">,</span> <span class="n">β</span> <span class="bp">×</span> <span class="n">α</span>

<span class="kn">lemma</span> <span class="n">Const</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="n">Const</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">lemma</span> <span class="n">Fun</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="o">(</span><span class="n">Fun</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">lemma</span> <span class="n">Prod</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="o">(</span><span class="n">Prod</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">lemma</span> <span class="n">Swap</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="o">(</span><span class="n">Swap</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span> <span class="n">sorry</span>


<span class="c1">-- And then we can define</span>
<span class="n">def</span> <span class="n">Hom1</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span><span class="o">,</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span>
<span class="n">def</span> <span class="n">Hom2</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span>
<span class="n">def</span> <span class="n">Aut</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span>

<span class="c1">-- And hopefully automagically derive</span>
<span class="kn">lemma</span> <span class="n">Hom1</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="o">(</span><span class="n">Hom1</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">lemma</span> <span class="n">Hom2</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="o">(</span><span class="n">Hom1</span> <span class="n">β</span><span class="o">))</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">lemma</span> <span class="n">Aut</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="n">Aut</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="c1">-- If we have all these in place...</span>
<span class="c1">-- A bit of magic might actually be able to derive `group.transportable` on line 11.</span>
<span class="c1">-- After all, a group just is a type plus some functions... and we can now transport functions.</span>
</pre></div>

#### [ Johan Commelin (Apr 27 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125775387):
<p>Aah, and to prove the axioms for the transported functions, we need to be able to transport propositions</p>

#### [ Simon Hudon (Apr 27 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125775647):
<p>Thanks! Transporting propositions shouldn't be too hard. I have a few ideas on how to do it</p>

#### [ Simon Hudon (Apr 27 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125775719):
<p>With my recent popularity, maybe I should cash in on this new market: <a href="/user_uploads/3121/boyZ4T9BeLmq-lWnSs0tiqdb/IMG_8067.jpeg" target="_blank" title="IMG_8067.jpeg">IMG_8067.jpeg</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/boyZ4T9BeLmq-lWnSs0tiqdb/IMG_8067.jpeg" target="_blank" title="IMG_8067.jpeg"><img src="/user_uploads/3121/boyZ4T9BeLmq-lWnSs0tiqdb/IMG_8067.jpeg"></a></div>

#### [ Kevin Buzzard (Apr 27 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779148):
<p>I have proved the fundamental theorem of <code>has_mul</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779150):
<p>What a great way to spend a day.</p>

#### [ Kenny Lau (Apr 27 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779199):
<p>what is that theorem?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779205):
<div class="codehilite"><pre><span></span><span class="kn">universe</span> <span class="n">zfc_u</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">zfc_u</span><span class="o">}</span>

<span class="c1">-- ideas around the concept of α being canonically isomorphic to β</span>

<span class="kn">namespace</span> <span class="n">zfc</span>

<span class="c1">-- mod of equiv so I can save typing</span>
<span class="kn">structure</span> <span class="n">equiv&#39;</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">zfc_u</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">zfc_u</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">i</span>    <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span>
<span class="o">(</span><span class="n">j</span>    <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span>
<span class="o">(</span><span class="n">ij</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">j</span> <span class="o">(</span><span class="n">i</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">x</span><span class="o">)</span>
<span class="o">(</span><span class="n">ji</span>  <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">β</span><span class="o">),</span> <span class="n">i</span> <span class="o">(</span><span class="n">j</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">y</span><span class="o">)</span>

<span class="c1">-- it&#39;s equiv to equiv, it is absolutely fundamental for the notion of canonical isomorphism, and I like</span>
<span class="c1">-- the notation better because it gets everywhere.</span>

<span class="c1">--#print has_mul</span>
<span class="c1">--@[class]</span>
<span class="c1">--structure has_mul : Type u → Type u</span>
<span class="c1">--fields:</span>
<span class="c1">--has_mul.mul : Π {α : Type u} [c : has_mul α], α → α → α</span>

<span class="c1">-- Fundamental theorem of has_mul</span>

<span class="c1">--#print prefix has_mul -- stuff</span>
<span class="c1">--set_option pp.notation false</span>
<span class="kn">definition</span> <span class="n">equiv_mul</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">zfc_u</span><span class="o">}</span> <span class="o">:</span> <span class="n">equiv&#39;</span> <span class="n">α</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">equiv&#39;</span> <span class="o">(</span><span class="n">has_mul</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">has_mul</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">E</span><span class="o">,</span>
<span class="o">{</span> <span class="n">i</span> <span class="o">:=</span>  <span class="bp">λ</span> <span class="n">αmul</span><span class="o">,</span><span class="bp">⟨λ</span> <span class="n">b1</span> <span class="n">b2</span><span class="o">,</span> <span class="n">E</span><span class="bp">.</span><span class="n">i</span> <span class="o">(</span><span class="bp">@</span><span class="n">has_mul</span><span class="bp">.</span><span class="n">mul</span> <span class="n">α</span> <span class="n">αmul</span> <span class="o">(</span><span class="n">E</span><span class="bp">.</span><span class="n">j</span> <span class="n">b1</span><span class="o">)</span> <span class="o">(</span><span class="n">E</span><span class="bp">.</span><span class="n">j</span> <span class="n">b2</span><span class="o">))</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">j</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">βmul</span><span class="o">,</span><span class="bp">⟨λ</span> <span class="n">a1</span> <span class="n">a2</span><span class="o">,</span> <span class="n">E</span><span class="bp">.</span><span class="n">j</span> <span class="o">(</span><span class="bp">@</span><span class="n">has_mul</span><span class="bp">.</span><span class="n">mul</span> <span class="n">β</span> <span class="n">βmul</span> <span class="o">(</span><span class="n">E</span><span class="bp">.</span><span class="n">i</span> <span class="n">a1</span><span class="o">)</span> <span class="o">(</span><span class="n">E</span><span class="bp">.</span><span class="n">i</span> <span class="n">a2</span><span class="o">))</span><span class="bp">⟩</span><span class="o">,</span> <span class="c1">-- didn&#39;t I just write that?</span>
                                                                      <span class="c1">-- should we introduce E-dual?</span>
  <span class="n">ij</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="k">begin</span>
    <span class="n">cases</span> <span class="n">f</span><span class="o">,</span> <span class="c1">-- aargh why do I struggle</span>
    <span class="n">suffices</span> <span class="o">:</span>  <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">a1</span> <span class="n">a2</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">E</span><span class="bp">.</span><span class="n">j</span> <span class="o">(</span><span class="n">E</span><span class="bp">.</span><span class="n">i</span> <span class="o">(</span><span class="n">f</span> <span class="o">(</span><span class="n">E</span><span class="bp">.</span><span class="n">j</span> <span class="o">(</span><span class="n">E</span><span class="bp">.</span><span class="n">i</span> <span class="n">a1</span><span class="o">))</span> <span class="o">(</span><span class="n">E</span><span class="bp">.</span><span class="n">j</span> <span class="o">(</span><span class="n">E</span><span class="bp">.</span><span class="n">i</span> <span class="n">a2</span><span class="o">)))))</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a1</span> <span class="n">a2</span><span class="o">,</span> <span class="n">f</span> <span class="n">a1</span> <span class="n">a2</span><span class="o">),</span>
      <span class="k">by</span> <span class="n">rw</span> <span class="n">this</span><span class="o">,</span>
    <span class="n">funext</span><span class="o">,</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">E</span><span class="bp">.</span><span class="n">ij</span><span class="o">,</span><span class="n">E</span><span class="bp">.</span><span class="n">ji</span><span class="o">],</span> <span class="c1">-- got there in the end</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">ji</span> <span class="o">:=</span> <span class="c1">-- I can&#39;t even do this in term mode so I just copy out the entire tactic mode proof again.</span>
 <span class="bp">λ</span> <span class="n">g</span><span class="o">,</span> <span class="k">begin</span>
    <span class="n">cases</span> <span class="n">g</span><span class="o">,</span> <span class="c1">-- aargh why do I struggle</span>
    <span class="n">suffices</span> <span class="o">:</span>  <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">b1</span> <span class="n">b2</span> <span class="o">:</span> <span class="n">β</span><span class="o">),</span> <span class="n">E</span><span class="bp">.</span><span class="n">i</span> <span class="o">(</span><span class="n">E</span><span class="bp">.</span><span class="n">j</span> <span class="o">(</span><span class="n">g</span> <span class="o">(</span><span class="n">E</span><span class="bp">.</span><span class="n">i</span> <span class="o">(</span><span class="n">E</span><span class="bp">.</span><span class="n">j</span> <span class="n">b1</span><span class="o">))</span> <span class="o">(</span><span class="n">E</span><span class="bp">.</span><span class="n">i</span> <span class="o">(</span><span class="n">E</span><span class="bp">.</span><span class="n">j</span> <span class="n">b2</span><span class="o">)))))</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">b1</span> <span class="n">b2</span><span class="o">,</span> <span class="n">g</span> <span class="n">b1</span> <span class="n">b2</span><span class="o">),</span>
      <span class="k">by</span> <span class="n">rw</span> <span class="n">this</span><span class="o">,</span>
    <span class="n">funext</span><span class="o">,</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">E</span><span class="bp">.</span><span class="n">ij</span><span class="o">,</span><span class="n">E</span><span class="bp">.</span><span class="n">ji</span><span class="o">],</span> <span class="c1">-- got there in the end</span>
  <span class="kn">end</span><span class="o">,</span> <span class="c1">-- didn&#39;t I just write that?</span>
<span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Apr 27 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779217):
<p>it is <code>equiv_mul</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779219):
<p>but it would be happily renamed</p>

#### [ Kenny Lau (Apr 27 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779251):
<p>that's quite interesting</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779255):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Can you see that I repeat every line of code twice?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779259):
<p>I have this vague idea that this is not best practice</p>

#### [ Simon Hudon (Apr 27 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779350):
<p>No, you're right. I think this should and could be derived automatically.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779523):
<blockquote>
<p>Would it help to make everything isomorphic to a type a type class, and then prove things about the class of isomorphic types? Might be completely stupid.</p>
</blockquote>
<p>I am just catching up with chat. I've been trying to work out some of these proofs by hand.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779529):
<p>That sounds like a really cool idea though</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779575):
<p>By the way -- the reason I did <code>has_mul</code> is that there is another type class which I am targetting.</p>

#### [ Kenny Lau (Apr 27 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779576):
<blockquote>
<blockquote>
<p>Would it help to make everything isomorphic to a type a type class, and then prove things about the class of isomorphic types? Might be completely stupid.</p>
</blockquote>
<p>I am just catching up with chat. I've been trying to work out some of these proofs by hand.</p>
</blockquote>
<p>it's called cardinal</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779586):
<p>:-)</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779603):
<p>Is <code>cardinal</code> a far more useful object than I had realised?</p>

#### [ Kenny Lau (Apr 27 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779608):
<p>no</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779610):
<p>:-)</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779618):
<p>Kenny can you prove the fundamental theorem of ring?</p>

#### [ Kenny Lau (Apr 27 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779624):
<p>I can, but I won't</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779628):
<p>how many lines would it take you</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779631):
<p>the fundamental theorem of ring is a trivial result</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779653):
<p>I wanna build a tactic :-)</p>

#### [ Kenny Lau (Apr 27 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779672):
<p>a ring has many structures, you know</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125779687):
<p>yeah and you solve them all with the same tactic</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780187):
<p>rofl</p>

#### [ Kenny Lau (Apr 27 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780189):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span>

<span class="n">def</span> <span class="n">transport_ring</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">ring</span> <span class="n">β</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">symm</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">f</span><span class="bp">.</span><span class="n">symm</span> <span class="n">y</span><span class="o">),</span>
  <span class="n">zero</span> <span class="o">:=</span> <span class="n">f</span> <span class="mi">0</span><span class="o">,</span>
  <span class="n">neg</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="bp">-</span><span class="n">f</span><span class="bp">.</span><span class="n">symm</span> <span class="n">x</span><span class="o">),</span>
  <span class="n">mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">symm</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">f</span><span class="bp">.</span><span class="n">symm</span> <span class="n">y</span><span class="o">),</span>
  <span class="n">one</span> <span class="o">:=</span> <span class="n">f</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">add_assoc</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="k">from</span> <span class="n">add_assoc</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">zero_add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="k">from</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">apply_eq_iff_eq_inverse_apply</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">zero_add</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">add_zero</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="k">from</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">apply_eq_iff_eq_inverse_apply</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">add_zero</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">add_left_neg</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="k">from</span> <span class="n">add_left_neg</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">add_comm</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="k">from</span> <span class="n">add_comm</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">mul_assoc</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="k">from</span> <span class="n">mul_assoc</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">one_mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="k">from</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">apply_eq_iff_eq_inverse_apply</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">one_mul</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">mul_one</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="k">from</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">apply_eq_iff_eq_inverse_apply</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">mul_one</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">left_distrib</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="k">from</span> <span class="n">left_distrib</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">right_distrib</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="k">from</span> <span class="n">right_distrib</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Apr 27 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780193):
<p>I have proved the fundamental theorem of mul</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780198):
<p>and now I have to prove the fundamental theorem of add</p>

#### [ Kenny Lau (Apr 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780201):
<p>why would I do that</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780202):
<p>but add is canonically isomorphic to mul</p>

#### [ Kenny Lau (Apr 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780203):
<p>I just said I won't</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780204):
<p>I am doing it</p>

#### [ Kenny Lau (Apr 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780209):
<p>done 10 mins</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780212):
<p>I just do a regular expression substitution</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780213):
<p>and I have the fundamental theorem of add</p>

#### [ Kenny Lau (Apr 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780215):
<p>you win</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780217):
<p>but I would rather have a tactic</p>

#### [ Kenny Lau (Apr 27 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780310):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span>
<span class="n">def</span> <span class="n">why_would_one</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">has_add</span> <span class="n">α</span> <span class="err">≃</span> <span class="n">has_mul</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">to_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">f</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">f</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">inv_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">f</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">f</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">left_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">f</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">right_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">f</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">}</span>
</pre></div>

#### [ Patrick Massot (Apr 27 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780411):
<p>It reminds me of the situation with <a href="https://github.com/PatrickMassot/lean-differential-topology/commit/f47348abf8515e23bd485683d8b351c7fd89c70f#diff-bbdfb4d2f4b405102cb35c772afdd2cc" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/commit/f47348abf8515e23bd485683d8b351c7fd89c70f#diff-bbdfb4d2f4b405102cb35c772afdd2cc">https://github.com/PatrickMassot/lean-differential-topology/commit/f47348abf8515e23bd485683d8b351c7fd89c70f#diff-bbdfb4d2f4b405102cb35c772afdd2cc</a> which was automated into <a href="https://github.com/leanprover/mathlib/blob/master/algebra/pi_instances.lean#L56" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/algebra/pi_instances.lean#L56">https://github.com/leanprover/mathlib/blob/master/algebra/pi_instances.lean#L56</a></p>

#### [ Patrick Massot (Apr 27 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780413):
<p>So I'm pretty optimistic there will be a tactic</p>

#### [ Patrick Massot (Apr 27 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780457):
<p>What would be even better would be Simon getting tired of writing our tactics and writing tactic writing tutorials instead</p>

#### [ Kenny Lau (Apr 27 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780460):
<p>aha</p>

#### [ Kenny Lau (Apr 27 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780466):
<p>Give a man a fish, and you feed him for a day; show him how to catch fish, and you feed him for a lifetime.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780685):
<p>I made an instance</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780692):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">mul_is_add</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">zfc_u</span><span class="o">}</span> <span class="o">:</span> <span class="n">equiv&#39;</span> <span class="o">(</span><span class="n">has_mul</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">has_add</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">i</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">mul</span><span class="bp">⟩</span><span class="o">,</span><span class="bp">⟨</span><span class="n">mul</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">j</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">mul</span><span class="bp">⟩</span><span class="o">,</span><span class="bp">⟨</span><span class="n">mul</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">ij</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="bp">⟩</span><span class="o">,</span><span class="k">begin</span> <span class="c1">-- *sigh*</span>
    <span class="n">constructor</span><span class="o">,</span>
  <span class="kn">end</span> <span class="o">,</span>
  <span class="n">ji</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">z</span><span class="bp">⟩</span><span class="o">,</span> <span class="k">by</span> <span class="n">constructor</span>
<span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Apr 27 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780697):
<p>but that's what I just did</p>

#### [ Kevin Buzzard (Apr 27 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780700):
<p>I am behind</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780739):
<p>I am working it all out myself</p>

#### [ Kenny Lau (Apr 27 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780745):
<p>nice</p>

#### [ Sean Leather (Apr 27 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780753):
<blockquote>
<p>Give a man a fish, and you feed him for a day; show him how to catch fish, and you feed him for a lifetime.</p>
</blockquote>
<p>Unless there is no body of water nearby...</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780788):
<p>OK Kenny, well done on ring. My next challenge for you is <code>topological_field</code></p>

#### [ Kenny Lau (Apr 27 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780794):
<p>nope.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780796):
<p>and it's a challenge to Simon as well</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780910):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span>

<span class="n">def</span> <span class="n">transport_ring</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">topological_field</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">topological_field</span> <span class="n">β</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Apr 27 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780912):
<p>Who will win out of man and machine</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125780962):
<p>and I am sitting here in ZFC and remarking that it is trivial</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781022):
<p>Aah Kenny I just saw your has_mul</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781063):
<p>well I proved the fundamental theorem of has_mul before</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781069):
<p>so can you now deduce the fundamental theorem of has_add?</p>

#### [ Andrew Ashworth (Apr 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781632):
<p>did you take a look at the <code>transfer</code> paper I linked way back? That's how in core lean they move proofs between <code>int</code> and <code>(a , b) : nat * nat</code>, which (and maybe I'm not understanding the details here very well) is your problem of transporting proofs between isomorphic types?</p>

#### [ Andrew Ashworth (Apr 27 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781815):
<p>also as far as I can tell from my (limited) experience with hott; isomorphisms are just as hard to deal with as they are in dtt, there's no magic sauce rewriting. you can try reading <a href="https://github.com/cmu-phil/Spectral" target="_blank" title="https://github.com/cmu-phil/Spectral">https://github.com/cmu-phil/Spectral</a>, which is a lean repository about the Serre spectral sequence</p>

#### [ Andrew Ashworth (Apr 27 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781820):
<p>I have no idea what a spectral sequence might be, but you can see that dealing with isomorphisms is no easier from reading the source code...</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781905):
<p>Kenny I thought of a much easier challenge for you</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781906):
<p><a href="https://github.com/kbuzzard/xena/tree/master/canonical_isomorphism" target="_blank" title="https://github.com/kbuzzard/xena/tree/master/canonical_isomorphism">https://github.com/kbuzzard/xena/tree/master/canonical_isomorphism</a></p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781909):
<p>much less boring than topological fields</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781965):
<p>can you define <code>mul_to_add</code> at the bottom?</p>

#### [ Mario Carneiro (Apr 27 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125781997):
<p>The <code>over_optimistic</code> theorem is a weak form of univalence. To see how they are related, just plug in <code>eq A</code> for the function <code>F</code>; then <code>A = A</code> is equiv to <code>A = B</code> and hence the latter is also inhabited. It is currently an open question whether this theorem is consistent with lean, but I believe it to be. (It is inconsistent with VM evaluation though.)</p>
<p>The second part of this conversation has developed a plan for showing that even if you can't prove that all functions are functorial, you might be able to show that all definable functions are functorial by working in the metatheory (i.e. giving a tactic that produces the required term). It is not contradictory that it might be possible that all lean definable terms are functorial in an appropriate sense even if you can't prove it for <em>all</em> terms, as the internal theory understands the quantifier. So this is not a "proof or counterexample" kind of question.</p>
<p>This topic is usually known in the type theory literature as "parametricity", and it is on my todo list for my paper.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782104):
<p><code>definition mul_to_add {α β : Type} : equiv' α β → equiv' (has_add α) (has_add β) := sorry</code></p>

#### [ Johan Commelin (Apr 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782105):
<p>Right, so we are kind of proposing a pragmatic approach to HoTT and univalence</p>

#### [ Johan Commelin (Apr 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782114):
<p>Kevin, did you see Scott's proposal for a class + decorators?</p>

#### [ Johan Commelin (Apr 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782122):
<p>I think you won't need to prove any of these "fundamental theorems" anymore, once we get that implemented</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782181):
<p>So in layman's terms, when can I expect a three-line proof of <code>exact_sequence A B C -&gt; exact_sequence A' B' C'</code> which is just three rewrites?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782183):
<p>I would be very happy to work on such a thing</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782184):
<p>because I really want it :-)</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782188):
<p>Can I incorporate Scott's proposal into my proofs somehow?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782195):
<p>Or is Scott's code purely for someone who is writing a tactic?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782232):
<p>I just find these quite fun and satisfying to do by hand, and I feel like if I try to get really good at them</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782238):
<p>then I might understand better how to write a tactic which is doing some of the job for me</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782248):
<p>I would be very happy if anyone wanted to comment on <a href="https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/canonically_isomorphic.lean" target="_blank" title="https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/canonically_isomorphic.lean">https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/canonically_isomorphic.lean</a></p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782252):
<p>I would really like to get some canonical proofs.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782255):
<p>Kenny can you beat any of mine?</p>

#### [ Johan Commelin (Apr 27 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782394):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> No, we can't use Scott's proposal yet. The idea is that someone proves inductively the <em>universal</em> fundamental theorem for structures (or probably: inductive types). And then we only need to prove the fundamental theorem for some basic types and we will get all the others for free.</p>

#### [ Johan Commelin (Apr 27 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782443):
<p>And it seems like Simon thought this was interesting, and might try to implement it pretty soon.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782446):
<p>Can you formalise what you think the universal fundamental theorem is?</p>

#### [ Johan Commelin (Apr 27 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782448):
<p>Hmm, I don't know enough lean yet.</p>

#### [ Johan Commelin (Apr 27 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782453):
<p>Actually, no.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782457):
<p>Can <span class="user-mention" data-user-id="110524">@Scott Morrison</span> or <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> ?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782461):
<p>Is there some kind of conjecture we can make?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782462):
<p>and give a constructive proof?</p>

#### [ Johan Commelin (Apr 27 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782464):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> The idea is that we "tag" every structure for which we want to prove it. And then actually Lean does it itself.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782466):
<p>so like the type class inference machinery?</p>

#### [ Johan Commelin (Apr 27 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782467):
<p>This is what the <code>@[derive transportable]</code> should do</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782510):
<p>so can one formulate some theorem which should be true for every...something...which is tagged with this tag?</p>

#### [ Johan Commelin (Apr 27 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782511):
<p>Lean will see that you are defining some <code>structure</code> and for all its fields it already knows that they are transportable. And thus it proves a theorem for the new structure as well.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782512):
<p>In Lean, I mean?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782514):
<p>What will the theorem be?</p>

#### [ Johan Commelin (Apr 27 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782516):
<p>Yes. That theorem is your <code>over_optimistic</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782521):
<p>I see.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782526):
<p>And we should be able to prove it for all F tagged with some tag</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782527):
<p>...automatically?</p>

#### [ Johan Commelin (Apr 27 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782528):
<p>Well, not <em>we</em> but even Lean</p>

#### [ Johan Commelin (Apr 27 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782529):
<p>After we taught it the ultimate basics.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782530):
<p>and this would be...a tactic?</p>

#### [ Johan Commelin (Apr 27 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782572):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Again, I'm not a meta-expert. But basically, it will be an automatically applied tactic.</p>

#### [ Johan Commelin (Apr 27 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782573):
<p>This is what <code>derive</code> seems to do...</p>

#### [ Johan Commelin (Apr 27 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782580):
<p>But, I now I'm in waters that I don't really know</p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782587):
<p>I have been fretting over what canonical isomorphism means for many years now</p>

#### [ Johan Commelin (Apr 27 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782596):
<p>See also my snippet:<br>
<a href="#narrow/stream/113488-general/subject/.22canonically.22.20identifying.20two.20types/near/125775365" title="#narrow/stream/113488-general/subject/.22canonically.22.20identifying.20two.20types/near/125775365">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/.22canonically.22.20identifying.20two.20types/near/125775365</a></p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782646):
<p><a href="https://mathoverflow.net/a/19663" target="_blank" title="https://mathoverflow.net/a/19663">https://mathoverflow.net/a/19663</a></p>

#### [ Kenny Lau (Apr 27 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782704):
<blockquote>
<p>Kenny can you beat any of mine?</p>
</blockquote>
<p><a href="https://github.com/kckennylau/Lean/blob/master/canonically_isomorphic.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/canonically_isomorphic.lean">https://github.com/kckennylau/Lean/blob/master/canonically_isomorphic.lean</a></p>

#### [ Kevin Buzzard (Apr 27 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782724):
<p>So is this <code>transportable</code> class some completely well-known and well-studied class in type theory?</p>

#### [ Johan Commelin (Apr 27 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125782965):
<p>I think at least in <em>homotopy</em> type theory</p>

#### [ Johan Commelin (Apr 27 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783111):
<p>I like your MO answer</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783470):
<p>How do I reduce this goal</p>
<div class="codehilite"><pre><span></span><span class="err">⊢</span> <span class="o">{</span><span class="n">to_fun</span> <span class="o">:=</span> <span class="n">A1</span><span class="o">,</span>
     <span class="n">inv_fun</span> <span class="o">:=</span> <span class="n">A2</span><span class="o">,</span>
     <span class="n">left_inv</span> <span class="o">:=</span> <span class="mi">3</span><span class="o">,</span>
     <span class="n">right_inv</span> <span class="o">:=</span> <span class="n">A4</span><span class="o">}</span> <span class="bp">=</span>
    <span class="o">{</span><span class="n">to_fun</span> <span class="o">:=</span> <span class="n">B1</span><span class="o">,</span> <span class="n">inv_fun</span> <span class="o">:=</span> <span class="n">B2</span><span class="o">,</span> <span class="n">left_inv</span> <span class="o">:=</span> <span class="n">B3</span><span class="o">,</span> <span class="n">right_inv</span> <span class="o">:=</span> <span class="n">B4</span><span class="o">}</span>
</pre></div>


<p>into the four goals <code>A1=B1</code>, <code>A2=B2</code> etc?</p>

#### [ Kenny Lau (Apr 27 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783473):
<p><code>congr</code></p>

#### [ Patrick Massot (Apr 27 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783548):
<blockquote>
<p>So in layman's terms, when can I expect a three-line proof of <code>exact_sequence A B C -&gt; exact_sequence A' B' C'</code> which is just three rewrites?</p>
</blockquote>
<p>What I'm going to write is not what you are hoping for, and unrelated to the big dreams of general transport of structures</p>

#### [ Patrick Massot (Apr 27 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783550):
<p>But I still think it's useful</p>

#### [ Patrick Massot (Apr 27 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783589):
<p>I spend most of my Lean time being frustrated by obvious statements, and then see Mario prove them</p>

#### [ Kenny Lau (Apr 27 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783597):
<blockquote>
<p>How do I reduce this goal</p>
<div class="codehilite"><pre><span></span><span class="err">⊢</span> <span class="o">{</span><span class="n">to_fun</span> <span class="o">:=</span> <span class="n">A1</span><span class="o">,</span>
     <span class="n">inv_fun</span> <span class="o">:=</span> <span class="n">A2</span><span class="o">,</span>
     <span class="n">left_inv</span> <span class="o">:=</span> <span class="mi">3</span><span class="o">,</span>
     <span class="n">right_inv</span> <span class="o">:=</span> <span class="n">A4</span><span class="o">}</span> <span class="bp">=</span>
    <span class="o">{</span><span class="n">to_fun</span> <span class="o">:=</span> <span class="n">B1</span><span class="o">,</span> <span class="n">inv_fun</span> <span class="o">:=</span> <span class="n">B2</span><span class="o">,</span> <span class="n">left_inv</span> <span class="o">:=</span> <span class="n">B3</span><span class="o">,</span> <span class="n">right_inv</span> <span class="o">:=</span> <span class="n">B4</span><span class="o">}</span>
</pre></div>


<p>into the four goals <code>A1=B1</code>, <code>A2=B2</code> etc?</p>
</blockquote>
<p>oh and that should be part of your interface</p>

#### [ Patrick Massot (Apr 27 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783603):
<p>In my experience, what happens is my mind refuses to decompose the statement and/or think about the proper setup</p>

#### [ Patrick Massot (Apr 27 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783609):
<p>Then Mario decomposes the problem into three or four lemmas and each of them is a one-liner</p>

#### [ Patrick Massot (Apr 27 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783626):
<p>So let me try a decomposition in your case</p>

#### [ Patrick Massot (Apr 27 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783679):
<p>I would define sequences of rings and maps between them (assuming we don't have an abelian categories lib right now).</p>

#### [ Patrick Massot (Apr 27 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783698):
<p>And the corresponding maps, ie sequences of maps with all squares commuting</p>

#### [ Patrick Massot (Apr 27 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783713):
<p>Then define complexes as sequences where two consecutive maps compose to zero</p>

#### [ Patrick Massot (Apr 27 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783772):
<p>prove isomorphic sequences have conjugated maps</p>

#### [ Patrick Massot (Apr 27 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783774):
<p>deduce a sequence isomorphic to a complex is a complex</p>

#### [ Patrick Massot (Apr 27 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783775):
<p>define homology of complexes</p>

#### [ Patrick Massot (Apr 27 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783782):
<p>define exact sequences as acyclic complexes</p>

#### [ Patrick Massot (Apr 27 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783788):
<p>prove isomorphic complexes have isomorphic homology</p>

#### [ Patrick Massot (Apr 27 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783798):
<p>deduce your lemma (and the version with n rings instead of only 3)</p>

#### [ Patrick Massot (Apr 27 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783804):
<p>I'm not saying the total number of lines will be 3</p>

#### [ Patrick Massot (Apr 27 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783846):
<p>But all those definitions and lemmas will be needed very soon anyway</p>

#### [ Patrick Massot (Apr 27 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783853):
<p>(with more definitions of course, especially homotopy equivalences and quasi-iso)</p>

#### [ Patrick Massot (Apr 27 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783920):
<p>You also want a lemma relating my definition of exact sequence to the direct one</p>

#### [ Patrick Massot (Apr 27 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783929):
<p>So, the proof of your lemma wouldn't by three <code>rw</code> by three <code>apply</code> (or one <code>simp</code> maybe)</p>

#### [ Kenny Lau (Apr 27 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783955):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">equiv&#39;</span><span class="bp">.</span><span class="n">ext</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">zfc_u</span><span class="o">}</span> <span class="o">:</span>
  <span class="bp">∀</span> <span class="o">{</span><span class="n">e₁</span> <span class="n">e₂</span> <span class="o">:</span> <span class="n">equiv&#39;</span> <span class="n">α</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">e₁</span><span class="bp">.</span><span class="n">i</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">e₂</span><span class="bp">.</span><span class="n">i</span> <span class="n">x</span><span class="o">),</span> <span class="n">e₁</span> <span class="bp">=</span> <span class="n">e₂</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="n">i₁</span><span class="o">,</span> <span class="n">j₁</span><span class="o">,</span> <span class="n">ij₁</span><span class="o">,</span> <span class="n">ji₁</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">i₂</span><span class="o">,</span> <span class="n">j₂</span><span class="o">,</span> <span class="n">ij₂</span><span class="o">,</span> <span class="n">ji₂</span><span class="bp">⟩</span> <span class="n">H</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">congr</span><span class="o">,</span> <span class="o">{</span> <span class="n">funext</span><span class="o">,</span> <span class="n">apply</span> <span class="n">H</span> <span class="o">},</span>
  <span class="n">simp</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">funext</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">ji₁</span> <span class="n">x</span><span class="o">,</span> <span class="n">ij₁</span><span class="o">,</span> <span class="n">H</span><span class="o">,</span> <span class="n">ij₂</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Apr 27 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125783964):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Johan Commelin (Apr 27 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784003):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Sweet.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784017):
<p>I did Level 1 of Johan's level set!</p>

#### [ Kenny Lau (Apr 27 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784020):
<p>what level set?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784021):
<div class="codehilite"><pre><span></span><span class="c1">-- level 1</span>
<span class="kn">lemma</span> <span class="n">Const</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="n">Const</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{</span>
  <span class="n">on_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">H</span><span class="o">,</span><span class="bp">⟨λ</span> <span class="bp">_</span><span class="o">,</span><span class="n">punit</span><span class="bp">.</span><span class="n">star</span><span class="o">,</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span><span class="n">punit</span><span class="bp">.</span><span class="n">star</span><span class="o">,</span><span class="bp">λ</span> <span class="n">α</span><span class="o">,</span><span class="k">begin</span> <span class="n">cases</span> <span class="n">α</span><span class="o">,</span><span class="n">simp</span> <span class="kn">end</span><span class="o">,</span><span class="bp">λ</span> <span class="n">α</span><span class="o">,</span><span class="k">begin</span> <span class="n">cases</span> <span class="n">α</span><span class="o">,</span><span class="n">simp</span> <span class="kn">end</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="c1">--I was repeating myself in that last line.</span>
  <span class="n">on_refl</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span><span class="k">begin</span>
  <span class="n">congr</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">funext</span> <span class="n">s</span><span class="o">,</span><span class="n">cases</span> <span class="n">s</span><span class="o">,</span><span class="n">refl</span><span class="o">},</span>
  <span class="o">{</span> <span class="n">funext</span> <span class="n">s</span><span class="o">,</span><span class="n">cases</span> <span class="n">s</span><span class="o">,</span><span class="n">refl</span><span class="o">}</span> <span class="c1">-- I just wrote this</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">on_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">Hαβ</span> <span class="n">Hβγ</span><span class="o">,</span><span class="k">by</span> <span class="n">congr</span>
  <span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Apr 27 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784073):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> <br>
<a href="#narrow/stream/113488-general/subject/.22canonically.22.20identifying.20two.20types/near/125775365" title="#narrow/stream/113488-general/subject/.22canonically.22.20identifying.20two.20types/near/125775365">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/.22canonically.22.20identifying.20two.20types/near/125775365</a></p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784079):
<p>Patrick I think your proof is very different to Kenny's</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784083):
<p>and I like it much better</p>

#### [ Kenny Lau (Apr 27 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784090):
<p>what is his proof?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784095):
<p>and I think that perhaps when Mario said earlier that Kenny should "work on his long game", maybe he meant thinking like this</p>

#### [ Johan Commelin (Apr 27 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784104):
<p>Well, I think we ultimately should have Patrick's idea and Scott's proposal work together.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784107):
<p>Kenny</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784109):
<p>I put the levels up on xena</p>

#### [ Johan Commelin (Apr 27 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784161):
<p>In other words, a whole series of definitions, that are all tagged with <code>@[derive transport_of_structure]</code></p>

#### [ Johan Commelin (Apr 27 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784167):
<p>And then we get Kevin's requested lemma for free</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784240):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> <a href="https://github.com/kbuzzard/xena/tree/master/canonical_isomorphism" target="_blank" title="https://github.com/kbuzzard/xena/tree/master/canonical_isomorphism">https://github.com/kbuzzard/xena/tree/master/canonical_isomorphism</a></p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784241):
<p>I am one ahead of you</p>

#### [ Kenny Lau (Apr 27 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784242):
<p>thx</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784245):
<p>on the Johan challenge</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784262):
<p><a href="https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/johan_challenge.lean" target="_blank" title="https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/johan_challenge.lean">https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/johan_challenge.lean</a></p>

#### [ Kenny Lau (Apr 27 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784265):
<p>and then <code>derive</code> will work?</p>

#### [ Kenny Lau (Apr 27 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784267):
<p>How does <code>derive</code> work?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784271):
<p>we have to work at the start</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784272):
<p>and then the machines take over</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784313):
<p>and then I can have a three line proof of the three lemma</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784322):
<p>saying that if A -&gt; B -&gt; C is exact then A' -&gt; B' -&gt; C' is exact</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784326):
<p>all I have to do is prove some diagrams commute</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784328):
<p>and say that some things are canonically isomorphic</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784330):
<p>which is obvious in ZFC</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784346):
<p>Mathematicians will not use this software unless they can do stuff that they find easy in maths, in Lean</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784350):
<p>and I thought that I enjoyed doing algebraic geometry in Lean</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784351):
<p>until I ran into this issue</p>

#### [ Kenny Lau (Apr 27 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784352):
<p>I mean, the mechanism behind <code>@[derive __]</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784397):
<p>Either Simon will write it</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784399):
<p>or Scott will write it</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784400):
<p>or I will have to write it</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784401):
<p>with their help</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784403):
<p>or you can write it</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784404):
<p>or Chris</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784414):
<p>Maybe it would be trivial for Mario, I have no idea</p>

#### [ Kenny Lau (Apr 27 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784416):
<p>you're this close from listing everyone's name</p>

#### [ Kenny Lau (Apr 27 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784419):
<p>this close.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784424):
<p>but I can certainly believe that the more easy levels we solve by hand</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784430):
<p>the easier it will be to write the tactic</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784434):
<p>and I really like solving these levels</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784438):
<p>they're even better then Zelda</p>

#### [ Kenny Lau (Apr 27 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784445):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">transportable</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">on_equiv</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">α</span> <span class="n">β</span><span class="o">),</span> <span class="n">equiv</span> <span class="o">(</span><span class="n">f</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="n">β</span><span class="o">))</span>
<span class="o">(</span><span class="n">on_refl</span>  <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">),</span> <span class="n">on_equiv</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">refl</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">refl</span> <span class="o">(</span><span class="n">f</span> <span class="n">α</span><span class="o">))</span>
<span class="o">(</span><span class="n">on_trans</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">d</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">β</span> <span class="n">γ</span><span class="o">),</span> <span class="n">on_equiv</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">trans</span> <span class="n">d</span> <span class="n">e</span><span class="o">)</span> <span class="bp">=</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">on_equiv</span> <span class="n">d</span><span class="o">)</span> <span class="o">(</span><span class="n">on_equiv</span> <span class="n">e</span><span class="o">))</span>
</pre></div>

#### [ Kenny Lau (Apr 27 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784446):
<p>functor :D</p>

#### [ Kenny Lau (Apr 27 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784510):
<p>why no use symbol?</p>

#### [ Johan Commelin (Apr 27 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784511):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> <a href="https://github.com/leanprover/lean/blob/f59c2f0ef59fdc1833b6ead6adca721123bd7932/library/init/meta/derive.lean#L19-L22" target="_blank" title="https://github.com/leanprover/lean/blob/f59c2f0ef59fdc1833b6ead6adca721123bd7932/library/init/meta/derive.lean#L19-L22">https://github.com/leanprover/lean/blob/f59c2f0ef59fdc1833b6ead6adca721123bd7932/library/init/meta/derive.lean#L19-L22</a><br>
and also L44-L45</p>

#### [ Johan Commelin (Apr 27 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784584):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> It is indeed a functor, but only on equivalences. That is how Scott first defined it (informally). But I guess we might not want this def'n to depend on a category lib. The category lib probably wants to depend on transport of structure...</p>

#### [ Johan Commelin (Apr 27 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784596):
<p>By the way, I suggest a name for the tactic that proves transport of structure: <code>chuck_norris</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784599):
<p>Kenny feel free to make the file a lot better</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784606):
<p>+1 for <code>chuck_norris</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784607):
<p>but I would be happy to hear alternatives</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784613):
<p>One of the reasons people go on about <code>sledgehammer</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784616):
<p>is that it has a really cool name</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784617):
<p>and <code>crush</code> too</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784621):
<p>I would vote for any Pokemon move name</p>

#### [ Kenny Lau (Apr 27 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125784755):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">Const</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="n">Const</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">on_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">e</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">punit</span><span class="bp">.</span><span class="n">star</span><span class="o">,</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">punit</span><span class="bp">.</span><span class="n">star</span><span class="o">,</span> <span class="bp">λ</span> <span class="bp">⟨⟩</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">,</span> <span class="bp">λ</span> <span class="bp">⟨⟩</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">on_refl</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">⟨⟩</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">on_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">e1</span> <span class="n">e2</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">⟨⟩</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">}</span>

<span class="kn">lemma</span> <span class="n">Fun</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="o">(</span><span class="n">Fun</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">on_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">e</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">e</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">),</span> <span class="bp">λ</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">e</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">),</span>
    <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">e</span><span class="bp">.</span><span class="n">inverse_apply_apply</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">),</span>
    <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">e</span><span class="bp">.</span><span class="n">apply_inverse_apply</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">on_refl</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">on_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">δ</span> <span class="n">e1</span> <span class="n">e2</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Apr 27 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785025):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">prod</span><span class="bp">.</span><span class="n">ext&#39;</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">=</span> <span class="n">q</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">=</span> <span class="n">q</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">=</span> <span class="n">q</span> <span class="o">:=</span>
<span class="n">prod</span><span class="bp">.</span><span class="n">ext</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">H1</span><span class="o">,</span> <span class="n">H2</span><span class="bp">⟩</span>

<span class="kn">lemma</span> <span class="n">Prod</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="o">(</span><span class="n">Prod</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">on_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">e</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">e</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="o">),</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">e</span><span class="bp">.</span><span class="n">symm</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="o">),</span>
    <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">prod</span><span class="bp">.</span><span class="n">ext&#39;</span> <span class="n">rfl</span> <span class="err">$</span> <span class="n">e</span><span class="bp">.</span><span class="n">inverse_apply_apply</span> <span class="n">f</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
    <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">prod</span><span class="bp">.</span><span class="n">ext&#39;</span> <span class="n">rfl</span> <span class="err">$</span> <span class="n">e</span><span class="bp">.</span><span class="n">apply_inverse_apply</span> <span class="n">f</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">on_refl</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">prod</span><span class="bp">.</span><span class="n">ext&#39;</span> <span class="n">rfl</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">on_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">δ</span> <span class="n">e1</span> <span class="n">e2</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">}</span>

<span class="kn">lemma</span> <span class="n">Swap</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="o">(</span><span class="n">Swap</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">on_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">e</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="n">e</span> <span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="o">),</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="n">e</span><span class="bp">.</span><span class="n">symm</span> <span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="o">),</span>
    <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">prod</span><span class="bp">.</span><span class="n">ext&#39;</span> <span class="o">(</span><span class="n">e</span><span class="bp">.</span><span class="n">inverse_apply_apply</span> <span class="n">f</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="n">rfl</span><span class="o">,</span>
    <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">prod</span><span class="bp">.</span><span class="n">ext&#39;</span> <span class="o">(</span><span class="n">e</span><span class="bp">.</span><span class="n">apply_inverse_apply</span> <span class="n">f</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">on_refl</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">prod</span><span class="bp">.</span><span class="n">ext&#39;</span> <span class="n">rfl</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">on_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">δ</span> <span class="n">e1</span> <span class="n">e2</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Apr 27 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785027):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Kenny Lau (Apr 27 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785091):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">Hom1</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="o">(</span><span class="n">Hom1</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span>
<span class="n">Fun</span><span class="bp">.</span><span class="n">transportable</span> <span class="n">α</span>
</pre></div>


<p>?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785192):
<div class="codehilite"><pre><span></span><span class="c1">-- level 2</span>
<span class="kn">lemma</span> <span class="n">Fun</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="o">(</span><span class="n">Fun</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span> <span class="o">{</span>
    <span class="n">on_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">Hβγ</span><span class="o">,</span><span class="bp">⟨</span>
        <span class="bp">λ</span> <span class="n">f</span> <span class="n">a</span><span class="o">,</span><span class="n">Hβγ</span><span class="bp">.</span><span class="n">to_fun</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">),</span>
        <span class="bp">λ</span> <span class="n">f</span> <span class="n">a</span><span class="o">,</span><span class="n">Hβγ</span><span class="bp">.</span><span class="n">inv_fun</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">),</span>
        <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span><span class="k">by</span> <span class="n">funext</span> <span class="n">a</span><span class="bp">;</span><span class="n">exact</span> <span class="n">Hβγ</span><span class="bp">.</span><span class="n">left_inv</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">),</span>
        <span class="bp">λ</span> <span class="n">g</span><span class="o">,</span><span class="k">by</span> <span class="n">funext</span> <span class="n">a</span><span class="bp">;</span><span class="n">exact</span> <span class="n">Hβγ</span><span class="bp">.</span><span class="n">right_inv</span> <span class="o">(</span><span class="n">g</span> <span class="n">a</span><span class="o">)</span>
    <span class="bp">⟩</span><span class="o">,</span>
    <span class="n">on_refl</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span><span class="o">,</span><span class="k">by</span> <span class="n">congr</span><span class="o">,</span>
    <span class="n">on_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">δ</span> <span class="n">Hβγ</span> <span class="n">Hγδ</span><span class="o">,</span><span class="k">by</span> <span class="n">congr</span>
<span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Apr 27 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785196):
<p>I see you caught up :-)</p>

#### [ Kenny Lau (Apr 27 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785199):
<p>I'm faster :P</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785256):
<p>Kenny you repeat yourself in your code</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785259):
<p>you say most things twice</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785261):
<p>this means it is bad code, right?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785263):
<p>Can you write better code?</p>

#### [ Kenny Lau (Apr 27 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785264):
<p>let's see whether you can avoid repeating yourself lol</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785268):
<p>You know the dual of an equiv is an equiv</p>

#### [ Kevin Buzzard (Apr 27 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785278):
<p>I repeat myself IRL</p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785354):
<blockquote>
<p>I'm faster :P</p>
</blockquote>
<p>Yes but you're working on my conjecture ;-)</p>

#### [ Kenny Lau (Apr 27 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785534):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">Hom1</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="o">(</span><span class="n">Hom1</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span>
<span class="n">Fun</span><span class="bp">.</span><span class="n">transportable</span> <span class="n">α</span>

<span class="kn">lemma</span> <span class="n">Hom2</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="o">(</span><span class="n">Hom2</span> <span class="n">β</span><span class="o">))</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">on_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">γ</span> <span class="n">e</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">e</span><span class="bp">.</span><span class="n">symm</span> <span class="n">x</span><span class="o">),</span> <span class="bp">λ</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">e</span> <span class="n">x</span><span class="o">),</span>
    <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">congr_arg</span> <span class="n">f</span> <span class="err">$</span> <span class="n">e</span><span class="bp">.</span><span class="n">inverse_apply_apply</span> <span class="n">x</span><span class="o">,</span>
    <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">congr_arg</span> <span class="n">f</span> <span class="err">$</span> <span class="n">e</span><span class="bp">.</span><span class="n">apply_inverse_apply</span> <span class="n">x</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">on_refl</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">on_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">δ</span> <span class="n">e1</span> <span class="n">e2</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">}</span>

<span class="kn">lemma</span> <span class="n">Aut</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="n">Aut</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">on_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">e</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">e</span> <span class="o">(</span><span class="n">f</span> <span class="o">(</span><span class="n">e</span><span class="bp">.</span><span class="n">symm</span> <span class="n">x</span><span class="o">)),</span> <span class="bp">λ</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">e</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">f</span> <span class="o">(</span><span class="n">e</span> <span class="n">x</span><span class="o">)),</span>
    <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span>
    <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">on_refl</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">on_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">e1</span> <span class="n">e2</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span> <span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Apr 27 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785536):
<p>Kenny my proof of <code>Const.transportable.on_trans</code> is better than yours</p>

#### [ Kenny Lau (Apr 27 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785577):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> all done. now I can shorten my proof lol</p>

#### [ Kenny Lau (Apr 27 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785585):
<p>well</p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785587):
<p><code>on_trans := λ α β γ Hαβ Hβγ,by congr</code></p>

#### [ Kenny Lau (Apr 27 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785589):
<p>I like term mode :P</p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785592):
<p>don't you lie to me</p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785593):
<p>you like golf</p>

#### [ Kenny Lau (Apr 27 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785595):
<p>lol</p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785599):
<p>:-)</p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785704):
<p>in <code>Fun_transportable.on_equiv</code> you have <code>e.inverse_apply_apply (f x)</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785712):
<p>and I have <code>e.left_inv (f a)</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785733):
<p>which is better?</p>

#### [ Kenny Lau (Apr 27 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785854):
<p>they say <code>e.symm</code> and etc are more idiomatic</p>

#### [ Kenny Lau (Apr 27 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785871):
<p>because they are actually simp lemmas</p>

#### [ Kenny Lau (Apr 27 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785877):
<p>so I can just replace it with <code>by simp</code> and outgolf you</p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785886):
<p>So I should switch to all this <code>apply_inverse_apply</code> stuff?</p>

#### [ Kenny Lau (Apr 27 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785929):
<p>no, you should use <code>simp</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785930):
<p>And you use <code>coe_to_fun</code> to get the function directly?</p>

#### [ Kenny Lau (Apr 27 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125785934):
<p>yes</p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125786016):
<p>OK I pushed</p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125786025):
<p><a href="https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/johan_challenge.lean" target="_blank" title="https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/johan_challenge.lean">https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/johan_challenge.lean</a></p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125786034):
<p>has levels 1 and 2 solved</p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125786043):
<p>and I'll now look at your other work Kenny</p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125786048):
<p>Let me know if you think the solutions can be improved <span class="user-mention" data-user-id="110064">@Kenny Lau</span></p>

#### [ Kenny Lau (Apr 27 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125786270):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">refl</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span> <span class="n">w</span>

<span class="n">class</span> <span class="n">transportable</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">on_equiv</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">α</span> <span class="n">β</span><span class="o">),</span> <span class="n">equiv</span> <span class="o">(</span><span class="n">f</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="n">β</span><span class="o">))</span>
<span class="o">(</span><span class="n">on_refl</span>  <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">),</span> <span class="n">on_equiv</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">refl</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">refl</span> <span class="o">(</span><span class="n">f</span> <span class="n">α</span><span class="o">))</span>
<span class="o">(</span><span class="n">on_trans</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">d</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">β</span> <span class="n">γ</span><span class="o">),</span> <span class="n">on_equiv</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">trans</span> <span class="n">d</span> <span class="n">e</span><span class="o">)</span> <span class="bp">=</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">on_equiv</span> <span class="n">d</span><span class="o">)</span> <span class="o">(</span><span class="n">on_equiv</span> <span class="n">e</span><span class="o">))</span>

<span class="c1">-- Our goal is an automagic proof of the following (level 20)</span>
<span class="kn">theorem</span> <span class="n">group</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">:</span> <span class="n">transportable</span> <span class="n">group</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="c1">-- These we might need to define and prove by hand</span>
<span class="n">def</span> <span class="n">Const</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="n">punit</span>
<span class="n">def</span> <span class="n">Fun</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span><span class="o">,</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span>
<span class="n">def</span> <span class="n">Prod</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span><span class="o">,</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">β</span>
<span class="n">def</span> <span class="n">Swap</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span><span class="o">,</span> <span class="n">β</span> <span class="bp">×</span> <span class="n">α</span>

<span class="c1">-- level 1</span>
<span class="kn">lemma</span> <span class="n">Const</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="n">Const</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">on_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">e</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">punit_equiv_punit</span><span class="o">,</span>
  <span class="n">on_refl</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">⟨⟩</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">on_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">e1</span> <span class="n">e2</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">⟨⟩</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">}</span>

<span class="kn">lemma</span> <span class="n">Fun</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="o">(</span><span class="n">Fun</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">on_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">e</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">arrow_congr</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">refl</span> <span class="n">α</span><span class="o">)</span> <span class="n">e</span><span class="o">,</span>
  <span class="n">on_refl</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">on_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">δ</span> <span class="n">e1</span> <span class="n">e2</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span>
    <span class="k">by</span> <span class="n">cases</span> <span class="n">e1</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">e2</span><span class="bp">;</span> <span class="n">refl</span> <span class="o">}</span>

<span class="kn">theorem</span> <span class="n">prod</span><span class="bp">.</span><span class="n">ext&#39;</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">=</span> <span class="n">q</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">=</span> <span class="n">q</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">=</span> <span class="n">q</span> <span class="o">:=</span>
<span class="n">prod</span><span class="bp">.</span><span class="n">ext</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">H1</span><span class="o">,</span> <span class="n">H2</span><span class="bp">⟩</span>

<span class="kn">lemma</span> <span class="n">Prod</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="o">(</span><span class="n">Prod</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">on_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">e</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">prod_congr</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">refl</span> <span class="n">α</span><span class="o">)</span> <span class="n">e</span><span class="o">,</span>
  <span class="n">on_refl</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">y</span><span class="bp">⟩</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span>
  <span class="n">on_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">δ</span> <span class="n">e1</span> <span class="n">e2</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">y</span><span class="bp">⟩</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">}</span>

<span class="kn">lemma</span> <span class="n">Swap</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="o">(</span><span class="n">Swap</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">on_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">e</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">prod_congr</span> <span class="n">e</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">refl</span> <span class="n">α</span><span class="o">),</span>
  <span class="n">on_refl</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">y</span><span class="bp">⟩</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span>
  <span class="n">on_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">δ</span> <span class="n">e1</span> <span class="n">e2</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">y</span><span class="bp">⟩</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">}</span>

<span class="c1">-- And then we can define</span>
<span class="n">def</span> <span class="n">Hom1</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span><span class="o">,</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span>
<span class="n">def</span> <span class="n">Hom2</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span>
<span class="n">def</span> <span class="n">Aut</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span>

<span class="c1">-- And hopefully automagically derive</span>
<span class="kn">lemma</span> <span class="n">Hom1</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="o">(</span><span class="n">Hom1</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span>
<span class="n">Fun</span><span class="bp">.</span><span class="n">transportable</span> <span class="n">α</span>

<span class="kn">lemma</span> <span class="n">Hom2</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="o">(</span><span class="n">Hom2</span> <span class="n">β</span><span class="o">))</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">on_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">γ</span> <span class="n">e</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">arrow_congr</span> <span class="n">e</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">refl</span> <span class="n">β</span><span class="o">),</span>
  <span class="n">on_refl</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">on_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">δ</span> <span class="n">e1</span> <span class="n">e2</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span>
    <span class="k">by</span> <span class="n">cases</span> <span class="n">e1</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">e2</span><span class="bp">;</span> <span class="n">refl</span> <span class="o">}</span>

<span class="kn">lemma</span> <span class="n">Aut</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="n">Aut</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">on_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">e</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">arrow_congr</span> <span class="n">e</span> <span class="n">e</span><span class="o">,</span>
  <span class="n">on_refl</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">on_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">e1</span> <span class="n">e2</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span>
    <span class="k">by</span> <span class="n">cases</span> <span class="n">e1</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">e2</span><span class="bp">;</span> <span class="n">refl</span> <span class="o">}</span>

<span class="c1">-- If we have all these in place...</span>
<span class="c1">-- A bit of magic might actually be able to derive `group.transportable` on line 11.</span>
<span class="c1">-- After all, a group just is a type plus some functions... and we can now transport functions.</span>
</pre></div>

#### [ Kenny Lau (Apr 27 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125786273):
<p>golfed</p>

#### [ Kenny Lau (Apr 27 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125786284):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Kenny Lau (Apr 27 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125786301):
<p><a href="https://github.com/kckennylau/Lean/blob/master/johan_challenge.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/johan_challenge.lean">https://github.com/kckennylau/Lean/blob/master/johan_challenge.lean</a></p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787049):
<p>This is looking good</p>

#### [ Kenny Lau (Apr 27 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787068):
<p>unfortunately, they wrote a destructor for <code>equiv.prod_congr</code> but not <code>equiv.arrow_congr</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787133):
<p>Wooah what is going on in that proof of <code>Prod.transportable.on_equiv</code></p>

#### [ Kenny Lau (Apr 27 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787138):
<p>that's the example of a good destructor</p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787210):
<p>kenny you still didn't beat the boss</p>

#### [ Kenny Lau (Apr 27 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787228):
<p>who is the boss?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787429):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> Kenny did all your levels</p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787430):
<p>except for group</p>

#### [ Kenny Lau (Apr 27 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787432):
<p>I thought <code>group</code> is to be automated lol</p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787439):
<p><a href="https://github.com/kckennylau/Lean/blob/master/johan_challenge.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/johan_challenge.lean">https://github.com/kckennylau/Lean/blob/master/johan_challenge.lean</a></p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787450):
<p>So I think that you were looking for destructors in <code>equiv.lean</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787454):
<p>which is a really good place to look for them</p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787504):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> what is the next move?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787520):
<p>Are these solutions in any way useful to help writing a general tactic which would prove <code>equiv a b -&gt; equiv (topological_field a) (topological_field b)</code>?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787526):
<p>What needs to be done next?</p>

#### [ Simon Hudon (Apr 27 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787601):
<p>I'm looking into automating those proofs. I'm keeping it for later tonight, when I've met my writing goals for the week</p>

#### [ Simon Hudon (Apr 27 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787647):
<p>I have a tactic, <code>refine_struct</code>, on the back burner which I might have to finish to facilitate this exercise</p>

#### [ Kevin Buzzard (Apr 27 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787731):
<p>Simon is there anything I can do to help?</p>

#### [ Simon Hudon (Apr 27 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787876):
<p>Thanks for offering. Are you thinking of something in particular?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787888):
<p>I don't understand how <a href="#narrow/stream/113488-general/subject/proof.20of.20the.20five.20lemma/near/125768238" title="#narrow/stream/113488-general/subject/proof.20of.20the.20five.20lemma/near/125768238">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/proof.20of.20the.20five.20lemma/near/125768238</a> fits into the picture</p>

#### [ Kevin Buzzard (Apr 27 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787896):
<p>Simon I am just interested in the question and it's the weekend</p>

#### [ Kevin Buzzard (Apr 27 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787907):
<p>I really enjoyed playing some of Johan's levels</p>

#### [ Kenny Lau (Apr 27 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787910):
<p>I enjoyed outgolfing kevin :P</p>

#### [ Kevin Buzzard (Apr 27 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787954):
<p>and I wondered if you might say something of the form "please give me a human proof of <code>foo.transportable</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787958):
<p>because these proofs are all really easy to do</p>

#### [ Kevin Buzzard (Apr 27 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787960):
<p>because Kenny has found a million tricks</p>

#### [ Kevin Buzzard (Apr 27 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787970):
<p>so the two motivations for doing more levels are</p>

#### [ Kevin Buzzard (Apr 27 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787971):
<p>(1) it's fun</p>

#### [ Kevin Buzzard (Apr 27 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787980):
<p>(2) it might help you see patterns</p>

#### [ Kevin Buzzard (Apr 27 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125787984):
<p>(3) it might be necessary to get the automation off the ground</p>

#### [ Simon Hudon (Apr 27 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788036):
<p>I don't know how much fun it would be but how do you feel about writing a few sentences on some of the tricks that Kenny found?</p>

#### [ Simon Hudon (Apr 27 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788097):
<p>... or a minimal example for them</p>

#### [ Johan Commelin (Apr 27 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788446):
<p>Ok, really cool</p>

#### [ Johan Commelin (Apr 27 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788486):
<p>I knew that Hom1 would be easy, given Fun</p>

#### [ Johan Commelin (Apr 27 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788500):
<p>But currying should also help, right?</p>

#### [ Johan Commelin (Apr 27 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788504):
<p>to express some of the lemmas in terms of others...</p>

#### [ Johan Commelin (Apr 27 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788596):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> You did not dissappoint me (-;</p>

#### [ Kenny Lau (Apr 27 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788603):
<p>:D</p>

#### [ Johan Commelin (Apr 27 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788704):
<p>By the way, what do you think... <code>transportable</code> or <code>transport_of_structure</code> ?</p>

#### [ Johan Commelin (Apr 27 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788707):
<p>I think I actually prefer the latter...</p>

#### [ Johan Commelin (Apr 27 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788792):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> <code>Aut = Fun \circ Prod</code>. Doesn't that help?</p>

#### [ Johan Commelin (Apr 27 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788837):
<p>I hope it does... because that is how a mathematician would prove it...</p>

#### [ Johan Commelin (Apr 27 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788844):
<p>Aaah, so maybe here is "level 3": show that transportable stuff composes</p>

#### [ Johan Commelin (Apr 27 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788852):
<p>Lean is a nightmare on the machine that I am typing on.</p>

#### [ Johan Commelin (Apr 27 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788859):
<p>So I can't actually do anything myself (-;</p>

#### [ Patrick Massot (Apr 27 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788866):
<p>Have you compiled mathlib on this machine?</p>

#### [ Johan Commelin (Apr 27 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788873):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> If you are looking for another small challenge, maybe show that if <code>f</code> and <code>g</code> are transportable, then so is <code>g \circ f</code>.</p>

#### [ Johan Commelin (Apr 27 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788917):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> An old version... it took more then an hour and the machine was unusable and almost overheating.</p>

#### [ Kenny Lau (Apr 27 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788922):
<blockquote>
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> <code>Aut = Fun \circ Prod</code>. Doesn't that help?</p>
</blockquote>
<p>unfortunately the transitive destructor is not available :P</p>

#### [ Johan Commelin (Apr 27 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788929):
<p>This is a Thinkpad X61: older than my kids...</p>

#### [ Kenny Lau (Apr 27 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788933):
<p>I might have to prove those destructors</p>

#### [ Johan Commelin (Apr 27 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125788938):
<p>That sounds like it is useful</p>

#### [ Kenny Lau (Apr 27 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789003):
<p>oh that isn't a transitive destructor though</p>

#### [ Kenny Lau (Apr 27 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789007):
<p>I mean, <code>@[trans]</code> won't work</p>

#### [ Kevin Buzzard (Apr 27 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789226):
<p>here is a recent Lean tip -- occasionally get your file and give it a good shake</p>

#### [ Kenny Lau (Apr 27 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789235):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> how is Aut = Fun \o Prod?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789241):
<p>I think Gabriel changed the VS Code Lean extension</p>

#### [ Kevin Buzzard (Apr 27 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789244):
<p>so it only compiles parts of the file</p>

#### [ Kevin Buzzard (Apr 27 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789246):
<p>and sometimes it can get confused</p>

#### [ Kenny Lau (Apr 27 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789247):
<p>the compiler is very slow for me recently</p>

#### [ Kenny Lau (Apr 27 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789249):
<p>I often have to wait 10+ minutes before things compile</p>

#### [ Kevin Buzzard (Apr 27 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789250):
<p>and giving it a shake works well for me</p>

#### [ Kevin Buzzard (Apr 27 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789253):
<p>oh that's not good</p>

#### [ Johan Commelin (Apr 27 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789302):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> That was a bit of a brain-fart. Sorry</p>

#### [ Kenny Lau (Apr 27 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789314):
<div class="codehilite"><pre><span></span><span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="n">transportable</span><span class="bp">.</span><span class="n">on_refl</span> <span class="n">transportable</span><span class="bp">.</span><span class="n">on_trans</span>

<span class="n">def</span> <span class="n">transportable</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">)</span>
  <span class="o">[</span><span class="n">transportable</span> <span class="n">f</span><span class="o">]</span> <span class="o">[</span><span class="n">transportable</span> <span class="n">g</span><span class="o">]</span> <span class="o">:</span> <span class="n">transportable</span> <span class="o">(</span><span class="n">g</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">on_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">e</span><span class="o">,</span> <span class="k">show</span> <span class="n">g</span> <span class="o">(</span><span class="n">f</span> <span class="n">α</span><span class="o">)</span> <span class="err">≃</span> <span class="n">g</span> <span class="o">(</span><span class="n">f</span> <span class="n">β</span><span class="o">),</span> <span class="k">from</span> <span class="n">transportable</span><span class="bp">.</span><span class="n">on_equiv</span> <span class="n">g</span> <span class="o">(</span><span class="n">transportable</span><span class="bp">.</span><span class="n">on_equiv</span> <span class="n">f</span> <span class="n">e</span><span class="o">),</span>
  <span class="n">on_refl</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span>
  <span class="n">on_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">e₁</span> <span class="n">e₂</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Apr 27 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789315):
<p>Mi mas go slip nau. Gutpela wok olgeta! Lukim!</p>

#### [ Kenny Lau (Apr 27 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789317):
<p>I like my addition</p>

#### [ Kenny Lau (Apr 27 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789318):
<p><a href="https://github.com/kckennylau/Lean/blob/master/johan_challenge.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/johan_challenge.lean">https://github.com/kckennylau/Lean/blob/master/johan_challenge.lean</a></p>

#### [ Kevin Buzzard (Apr 27 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789320):
<blockquote>
<p>I don't know how much fun it would be but how do you feel about writing a few sentences on some of the tricks that Kenny found?</p>
</blockquote>
<p>I would love to do that.</p>

#### [ Kenny Lau (Apr 27 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789322):
<p>tok pisin :o</p>

#### [ Johan Commelin (Apr 27 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125789327):
<p>Em nau.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790151):
<p>Hey! <code>topological_ring _</code> is a <code>Prop</code> not a <code>Type</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790167):
<p><code>theorem topological_ring.transportable : transportable topological_ring := sorry</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790210):
<p>gives an error</p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790214):
<div class="codehilite"><pre><span></span><span class="n">type</span> <span class="n">mismatch</span> <span class="n">at</span> <span class="n">application</span>
  <span class="n">transportable</span> <span class="n">topological_ring</span>
<span class="n">term</span>
  <span class="n">topological_ring</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="bp">Π</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="err">?</span><span class="o">)</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_2</span> <span class="o">:</span> <span class="n">ring</span> <span class="n">α</span><span class="o">],</span> <span class="kt">Prop</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="err">?</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="kt">Type</span> <span class="err">?</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="err">?</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="o">(</span><span class="err">?</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="err">?</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span>
</pre></div>

#### [ Kevin Buzzard (Apr 27 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790240):
<p>My new toy is broken</p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790251):
<p><code>class transportable (f : Type u → Type v) :=</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790311):
<p>it's not that it's a prop</p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790314):
<p>is the issue that it's not a function?</p>

#### [ Kenny Lau (Apr 27 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790321):
<p>right</p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790331):
<p>but a topological ring is the same as a group</p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790357):
<p>if I have a topological ring structure on X and a canonical isomorphism <code>X -&gt; Y</code> then I want a topological ring structure on <code>Y</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125790950):
<p>What is <code>theorem topological_ring.transportable </code> ?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125791009):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_structures</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">topological_ring</span>
</pre></div>

#### [ Kevin Buzzard (Apr 27 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125791026):
<p>this doesn't typecheck</p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125791027):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">topological_ring</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">:</span> <span class="n">transportable</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">R</span> <span class="o">:</span> <span class="o">(</span><span class="err">Σ</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">),</span> <span class="o">(</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">)</span> <span class="bp">×</span> <span class="o">(</span><span class="n">ring</span> <span class="n">α</span><span class="o">))</span> <span class="o">,</span>
    <span class="bp">@</span><span class="n">topological_ring</span> <span class="n">R</span><span class="bp">.</span><span class="n">fst</span> <span class="o">(</span><span class="n">R</span><span class="bp">.</span><span class="n">snd</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">R</span><span class="bp">.</span><span class="n">snd</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Apr 27 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125791031):
<p>What am I doing wrong?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125791039):
<p>Simon -- I was writing some goals in the docs</p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125791044):
<p>and transfer of a topological ring structure is one of the goals</p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125791207):
<p>we can write this</p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125791210):
<p><code>def transport_ring {α β : Type} [topological_field α] (f : α ≃ β) : topological_field β := sorry</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125791214):
<p>but I don't understand how to embed it in the <code>transportable</code> class</p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792177):
<p>Kenny you posted this earlier:</p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792187):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span>

<span class="n">def</span> <span class="n">transport_ring</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">ring</span> <span class="n">β</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">symm</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">f</span><span class="bp">.</span><span class="n">symm</span> <span class="n">y</span><span class="o">),</span>
  <span class="n">zero</span> <span class="o">:=</span> <span class="n">f</span> <span class="mi">0</span><span class="o">,</span>
  <span class="n">neg</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="bp">-</span><span class="n">f</span><span class="bp">.</span><span class="n">symm</span> <span class="n">x</span><span class="o">),</span>
  <span class="n">mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">symm</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">f</span><span class="bp">.</span><span class="n">symm</span> <span class="n">y</span><span class="o">),</span>
  <span class="n">one</span> <span class="o">:=</span> <span class="n">f</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">add_assoc</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="k">from</span> <span class="n">add_assoc</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">zero_add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="k">from</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">apply_eq_iff_eq_inverse_apply</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">zero_add</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">add_zero</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="k">from</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">apply_eq_iff_eq_inverse_apply</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">add_zero</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">add_left_neg</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="k">from</span> <span class="n">add_left_neg</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">add_comm</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="k">from</span> <span class="n">add_comm</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">mul_assoc</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="k">from</span> <span class="n">mul_assoc</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">one_mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="k">from</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">apply_eq_iff_eq_inverse_apply</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">one_mul</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">mul_one</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="k">from</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">apply_eq_iff_eq_inverse_apply</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">mul_one</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">left_distrib</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="k">from</span> <span class="n">left_distrib</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">right_distrib</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="k">from</span> <span class="n">right_distrib</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Apr 27 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792191):
<p>and if I change the top lines to</p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792208):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span>
<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>
<span class="n">def</span> <span class="n">transport_ring</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">ring</span> <span class="n">β</span> <span class="o">:=</span>
</pre></div>

#### [ Kevin Buzzard (Apr 27 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792210):
<p>then your code doesn't compile any more</p>

#### [ Kenny Lau (Apr 27 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792257):
<p>this is interesting</p>

#### [ Kevin Buzzard (Apr 27 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792259):
<p>Are you only proving <code>transport_ring</code> for types in the same universe, and is this easier to do than the general case?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792706):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span>
<span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_structures</span>

<span class="n">def</span> <span class="n">transport_topological_ring</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span>
  <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="bp">@</span><span class="n">topological_ring</span> <span class="n">β</span> <span class="n">sorry</span> <span class="n">sorry</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Chris Hughes (Apr 27 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792744):
<p>I doesn't seem like it would be any easier in the same universe.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792746):
<p>Least it typechecks</p>

#### [ Kevin Buzzard (Apr 27 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792751):
<p>I tried putting Kenny's proof into the same universe and there were still errors</p>

#### [ Kevin Buzzard (Apr 27 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792754):
<p>there are universe subtleties I don't understand</p>

#### [ Kevin Buzzard (Apr 27 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792796):
<p>Chris this is all your fault :-)</p>

#### [ Kevin Buzzard (Apr 27 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125792804):
<p>You proved the lemma only for rings canonically isomorphic to the rings I wanted</p>

#### [ Reid Barton (Apr 28 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795177):
<p>By adding more <code>transportable</code> classes for type constructors with multiple arguments, we could extend these ideas to situations where we have an isomorphism which respects some existing structure and we want to transport some additional structure (or property) across it. Here is a sketch of the idea: <a href="https://gist.github.com/rwbarton/d847ef6d1783f0d0859eb80de8327bad" target="_blank" title="https://gist.github.com/rwbarton/d847ef6d1783f0d0859eb80de8327bad">https://gist.github.com/rwbarton/d847ef6d1783f0d0859eb80de8327bad</a></p>

#### [ Reid Barton (Apr 28 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795238):
<p>The key point is the definition</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">is_homeomorphism</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">tα</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">tβ</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">tβ</span> <span class="bp">=</span> <span class="n">transport</span> <span class="n">topological_space</span> <span class="n">e</span> <span class="n">tα</span>
</pre></div>


<p>which seems to be more fundamental than the category-style definition "continuous function with a continuous inverse", since the definition of <code>transport</code> does not even need the notion of continuous function.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795266):
<p>This proof does not work:</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795307):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Const</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="n">punit</span>
<span class="kn">lemma</span> <span class="n">Const</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="n">Const</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">on_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">e</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">punit_equiv_punit</span><span class="o">,</span>
  <span class="n">on_refl</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">⟨⟩</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">on_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">e1</span> <span class="n">e2</span><span class="o">,</span> <span class="k">by</span> <span class="n">congr</span><span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Apr 28 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795310):
<p>but this proof works:</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795316):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Const</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="n">punit</span>
<span class="kn">lemma</span> <span class="n">Const</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="n">Const</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">on_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">e</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">punit_equiv_punit</span><span class="o">,</span>
  <span class="n">on_refl</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">⟨⟩</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">on_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">e1</span> <span class="n">e2</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">⟨⟩</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Apr 28 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795325):
<p>and this proof works:</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795331):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Const&#39;</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="n">punit</span>
<span class="kn">lemma</span> <span class="n">Const&#39;</span><span class="bp">.</span><span class="n">transportable</span> <span class="o">:</span> <span class="o">(</span><span class="n">transportable</span> <span class="n">Const</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{</span>
  <span class="n">on_equiv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">H</span><span class="o">,</span><span class="bp">⟨λ</span> <span class="bp">_</span><span class="o">,</span><span class="n">punit</span><span class="bp">.</span><span class="n">star</span><span class="o">,</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span><span class="n">punit</span><span class="bp">.</span><span class="n">star</span><span class="o">,</span><span class="bp">λ</span> <span class="bp">⟨⟩</span><span class="o">,</span><span class="n">rfl</span><span class="o">,</span><span class="bp">λ</span> <span class="bp">⟨⟩</span><span class="o">,</span><span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">on_refl</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ext</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨⟩</span><span class="o">,</span><span class="n">rfl</span><span class="o">),</span>
  <span class="n">on_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">Hαβ</span> <span class="n">Hβγ</span><span class="o">,</span><span class="k">by</span> <span class="n">congr</span>
  <span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Apr 28 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795386):
<p>I am interested in the idea of filling in fields using tactics but I can only use <code>congr</code> if I set it up in a certain way</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795472):
<blockquote>
<p>did you take a look at the <code>transfer</code> paper I linked way back? That's how in core lean they move proofs between <code>int</code> and <code>(a , b) : nat * nat</code>, which (and maybe I'm not understanding the details here very well) is your problem of transporting proofs between isomorphic types?</p>
</blockquote>
<p>Can you remind me of the link?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795475):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span></p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795476):
<p>My search skills are weak today</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795552):
<blockquote>
<p>The key point is the definition</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">is_homeomorphism</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">tα</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">tβ</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">tβ</span> <span class="bp">=</span> <span class="n">transport</span> <span class="n">topological_space</span> <span class="n">e</span> <span class="n">tα</span>
</pre></div>


<p>which seems to be more fundamental than the category-style definition "continuous function with a continuous inverse", since the definition of <code>transport</code> does not even need the notion of continuous function.</p>
</blockquote>
<p>At some point I am going to want more than just an equiv -- I will want that two canonical isomorphisms <code>equiv A A'</code> and <code>equiv B B'</code> commute with some given maps <code>A -&gt; B</code> and <code>A' -&gt; B'</code> which are both "defined naturally".</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795611):
<p>For example Reid, I proved that if <code>D(g) sub D(f)</code> then not only is <code>f</code> a unit in <code>R[1/g]</code>, but the rings <code>R[1/g]</code> and <code>R[1/f][1/gbar]</code> were canonically isomorphic, where <code>gbar</code> is the image of <code>g</code> in <code>R[1/f]</code></p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795634):
<p>And by "prove that they're canonically isomorphic" I mean in practice that I proved that I could write down an isomorphism of R-algebras which was also the unique R-algebra homomorphism in either direction.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795640):
<p>and I am pretty sure that I don't need to prove any more "canonicalness" for my application to schemes.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795686):
<p>The idea is that <code>f : R</code> is now fixed</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795695):
<p>and <code>g : { g : R // D(g) sub D(f) }</code> varies</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795699):
<p>and <code>A g := R[1/g]</code></p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795702):
<p>and <code>A' g := R[1/f][1/gbar]</code></p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795711):
<p>Does this fit into your "extra structure" idea?</p>

#### [ Reid Barton (Apr 28 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795894):
<p><code>B</code> is <code>A g'</code> for another <code>g'</code>?</p>

#### [ Reid Barton (Apr 28 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795909):
<p>Or something else entirely?</p>

#### [ Kenny Lau (Apr 28 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125795971):
<p>I'm back</p>

#### [ Reid Barton (Apr 28 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796055):
<p>It sounds like you want to prove that your isomorphism between <code>R[1/g]</code> and <code>R[1/f][1/gbar]</code> is natural (in the category theory sense) when these two localization constructions are viewed as functors of something (R and/or g?), and that is probably not a purely formal fact that follows from transporting across "equalities". (On the other hand, it is probably a slightly less formal fact that follows easily from some universal property.)</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796240):
<p>docs</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796244):
<p><a href="https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/canonical.md" target="_blank" title="https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/canonical.md">https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/canonical.md</a></p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796245):
<p>permanlink</p>

#### [ Kenny Lau (Apr 28 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796294):
<p>speaking of which, it's almost a month since your last post in xena</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796296):
<p>don't know how to do permalink</p>

#### [ Kenny Lau (Apr 28 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796298):
<p><a href="https://github.com/kbuzzard/xena/blob/e77228397ad21215a927f93d315edf3cbadbc567/canonical_isomorphism/canonical.md" target="_blank" title="https://github.com/kbuzzard/xena/blob/e77228397ad21215a927f93d315edf3cbadbc567/canonical_isomorphism/canonical.md">https://github.com/kbuzzard/xena/blob/e77228397ad21215a927f93d315edf3cbadbc567/canonical_isomorphism/canonical.md</a></p>

#### [ Kenny Lau (Apr 28 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796299):
<p>there you go</p>

#### [ Kenny Lau (Apr 28 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796303):
<p>try deleting the file :P</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796305):
<p>I want to focus on schemes Kenny, and I guess the situation is that it would be nice to resolve this canonical isomorphism issue before I go any further</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796313):
<p>I will probably blog about this though</p>

#### [ Kenny Lau (Apr 28 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796317):
<p>should I write a guest post</p>

#### [ Reid Barton (Apr 28 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796376):
<p>(You can click on the commit id near the right side of the blue bar, and then View)</p>

#### [ Reid Barton (Apr 28 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796713):
<p>Let me address the question at the end of those docs, since your "three lemma" was what prompted the gist I linked earlier.<br>
You could define a structure indexed on A B C that consists of abelian group structures on A B C and group homomorphisms f : A -&gt; B and g : B -&gt; C. The input to the "three lemma" is an isomorphism of such structures.<br>
The further structure would be exactness of the sequence, i.e., the equation ker g = im f; that's what you want to transport to the new sequence.</p>

#### [ Reid Barton (Apr 28 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796852):
<p>Simply transporting the combined structure of "being an exact sequence" across your isomorphisms A -&gt; A', B -&gt; B', C -&gt; C' won't be enough, since you also need to know that the transported group structures and maps agree with your original ones.</p>

#### [ Reid Barton (Apr 28 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796860):
<p>(for which you need precisely that the maps are group isomorphisms and the squares commute)</p>

#### [ Reid Barton (Apr 28 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125796932):
<p>I guess if you had lemmas to calculate the components of the transported structure, then that would be another way to do it.</p>

#### [ Reid Barton (Apr 28 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125797044):
<p>I need to make dinner but I'll try to produce some example code later</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125797105):
<p>I see! I find it much easier to understand this example.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125797107):
<p>So one makes a new structure</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125797113):
<p>and then attempts to transport it</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125797115):
<p>This sounds like a beautiful way of thinking about it.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125797487):
<p>Kenny you are welcome to write a guest post</p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125797493):
<p>On whatever topic you like</p>

#### [ Andrew Ashworth (Apr 28 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125798645):
<p>the transfer paper is here:  <a href="https://www21.in.tum.de/~kuncar/documents/huffman-kuncar-cpp2013.pdf" target="_blank" title="https://www21.in.tum.de/~kuncar/documents/huffman-kuncar-cpp2013.pdf">https://www21.in.tum.de/~kuncar/documents/huffman-kuncar-cpp2013.pdf</a></p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125798996):
<p>Thanks Andrew.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799001):
<p>Reid -- you probably know the full story anyway, but let me spell it out.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799058):
<p>Chris proved a lemma saying that if <code>R</code> is a ring and <code>f1,f2,...,fn</code> are elements which generate the unit ideal, then the structure sheaf on Spec(R) satisfies the sheaf axiom with respect to the open cover D(f1),..,D(fn).</p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799065):
<p>Formally, as you know, this says that the canonical map from <code>R</code> to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi mathvariant="normal">Π</mi><mi>i</mi></msub><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><msub><mi>f</mi><mi>i</mi></msub><mo>]</mo></mrow><annotation encoding="application/x-tex">\Pi_i R[1/f_i]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathrm">Π</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:-0.10764em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mclose">]</span></span></span></span> is an injection,</p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799110):
<p>with image equal to the kernel of the usual map <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi mathvariant="normal">Π</mi><mi>i</mi></msub><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><msub><mi>f</mi><mi>i</mi></msub><mo>]</mo><mo>→</mo><msub><mi mathvariant="normal">Π</mi><mrow><mi>i</mi><mo separator="true">,</mo><mi>j</mi></mrow></msub><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><msub><mi>f</mi><mi>i</mi></msub><msub><mi>f</mi><mi>j</mi></msub><mo>]</mo></mrow><annotation encoding="application/x-tex">\Pi_i R[1/f_i] \to \Pi_{i,j} R[1/f_if_j]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1.036108em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord mathrm">Π</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:-0.10764em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mclose">]</span><span class="mrel">→</span><span class="mord"><span class="mord mathrm">Π</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.311664em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mpunct mtight">,</span><span class="mord mathit mtight" style="margin-right:0.05724em;">j</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:-0.10764em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.311664em;"><span style="top:-2.5500000000000003em;margin-left:-0.10764em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.05724em;">j</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mclose">]</span></span></span></span></p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799118):
<p>and note that this latter map sends <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><msub><mi>s</mi><mi>i</mi></msub><msub><mo>)</mo><mrow><mi>i</mi><mo>∈</mo><mi>I</mi></mrow></msub></mrow><annotation encoding="application/x-tex">(s_i)_{i\in I}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord"><span class="mord mathit">s</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mrel mtight">∈</span><span class="mord mathit mtight" style="margin-right:0.07847em;">I</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.17737em;"></span></span></span></span></span></span></span></span> to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><msub><mi>s</mi><mi>i</mi></msub><mo>−</mo><msub><mi>s</mi><mi>j</mi></msub><msub><mo>)</mo><mrow><mi>i</mi><mo separator="true">,</mo><mi>j</mi></mrow></msub></mrow><annotation encoding="application/x-tex">(s_i-s_j)_{i,j}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1.036108em;vertical-align:-0.286108em;"></span><span class="base"><span class="mopen">(</span><span class="mord"><span class="mord mathit">s</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mbin">−</span><span class="mord"><span class="mord mathit">s</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.311664em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.05724em;">j</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.311664em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mpunct mtight">,</span><span class="mord mathit mtight" style="margin-right:0.05724em;">j</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span></span></span></span></p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799120):
<p>which is not a ring homomorphism</p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799128):
<p>but it is a difference of two such</p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799133):
<p>and hence the whole map is a group homomorphism</p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799137):
<p>Now I have done some abstract ring theory in Lean over the last few weeks, working on "an interface for localisation"</p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799181):
<p>and I have now proved some technical lemma which says that if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>D</mi><mo>(</mo><mi>g</mi><mo>)</mo><mo>⊆</mo><mi>D</mi><mo>(</mo><mi>f</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">D(g)\subseteq D(f)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.02778em;">D</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">)</span><span class="mrel">⊆</span><span class="mord mathit" style="margin-right:0.02778em;">D</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">)</span></span></span></span> then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>g</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/g]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">]</span></span></span></span> is canonically isomorphic to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>g</mi><mi>b</mi><mi>a</mi><mi>r</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f][1/gbar]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mord mathit">b</span><span class="mord mathit">a</span><span class="mord mathit" style="margin-right:0.02778em;">r</span><span class="mclose">]</span></span></span></span></p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799182):
<p>with <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>g</mi><mi>b</mi><mi>a</mi><mi>r</mi></mrow><annotation encoding="application/x-tex">gbar</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mord mathit">b</span><span class="mord mathit">a</span><span class="mord mathit" style="margin-right:0.02778em;">r</span></span></span></span> the image of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>g</mi></mrow><annotation encoding="application/x-tex">g</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">g</span></span></span></span></p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799191):
<p>and canonical isomorphism for me at this point means that we are given an element of <code>equiv</code> <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>g</mi><mo>]</mo><mo>)</mo></mrow><annotation encoding="application/x-tex">(R[1/g])</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">]</span><span class="mclose">)</span></span></span></span> <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>g</mi><mi>b</mi><mi>a</mi><mi>r</mi><mo>]</mo><mo>)</mo></mrow><annotation encoding="application/x-tex">(R[1/f][1/gbar])</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mord mathit">b</span><span class="mord mathit">a</span><span class="mord mathit" style="margin-right:0.02778em;">r</span><span class="mclose">]</span><span class="mclose">)</span></span></span></span></p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799193):
<p>(maths notation is better than Lean)</p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799194):
<p>with the following wonderful properties:</p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799236):
<p>1) the functions are ring homs (and hence ring isoms)</p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799238):
<p>2) The only <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span>-algebra hom from <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>g</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/g]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">]</span></span></span></span> to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>g</mi><mi>b</mi><mi>a</mi><mi>r</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f][1/gbar]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mord mathit">b</span><span class="mord mathit">a</span><span class="mord mathit" style="margin-right:0.02778em;">r</span><span class="mclose">]</span></span></span></span> is our given element.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799246):
<p>I am _hoping_ that this is a good definition of "canonical isomorphism" here.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799249):
<p>These are the facts which I isolated as important</p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799250):
<p>I made a structure for each of them</p>

#### [ Kevin Buzzard (Apr 28 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799308):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">R_alg_equiv</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm</span>
<span class="bp">_</span><span class="n">ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">β</span><span class="o">]</span>
  <span class="o">(</span><span class="n">sα</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">sβ</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">ring_equiv</span> <span class="n">α</span> <span class="n">β</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">R_alg_hom</span> <span class="o">:</span> <span class="n">sβ</span> <span class="bp">=</span> <span class="n">to_fun</span> <span class="err">∘</span> <span class="n">sα</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Apr 28 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799360):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">is_unique_R_alg_hom</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">β</span><span class="o">]</span>
<span class="o">(</span><span class="n">sα</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">sβ</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">sα</span><span class="o">]</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">sβ</span><span class="o">]</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">R_alg_hom</span> <span class="o">:</span> <span class="n">sβ</span> <span class="bp">=</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">sα</span><span class="o">)</span>
<span class="o">(</span><span class="n">is_unique</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">g</span><span class="o">],</span> <span class="n">sβ</span> <span class="bp">=</span> <span class="n">g</span> <span class="err">∘</span> <span class="n">sα</span> <span class="bp">→</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">f</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Apr 28 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799370):
<p>(NB it was <code>is_unique_R_alg_hom</code> which I noticed was not a <code>Prop</code> even though it could be -- I made it a Prop.)</p>

#### [ Kevin Buzzard (Apr 28 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799381):
<p>I have lots of cunning ways of producing unique R-algebra homs</p>

#### [ Kevin Buzzard (Apr 28 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799386):
<p>for example given a ring hom <code>R -&gt; \beta</code> with the property that every element of a mult subset <code>S</code> gets sent to a unit</p>

#### [ Kevin Buzzard (Apr 28 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799428):
<p>I have a unique <code>R</code>-alg com <code>R[1/S] -&gt; beta</code></p>

#### [ Kevin Buzzard (Apr 28 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799431):
<p>I am hoping that the ideas I already have will be enough to see me through</p>

#### [ Kevin Buzzard (Apr 28 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799440):
<p>so I am going to try and define the structures that we want to identify and then see if I can figure out what needs doing.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799448):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> In short I am saying that your proof of exactness being preserved stinks</p>

#### [ Kevin Buzzard (Apr 28 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799454):
<p>and it would be better to have a proof which looks a whole lot more abstract</p>

#### [ Kevin Buzzard (Apr 28 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799497):
<p>because then when next week I have to prove something ten times longer but just as trivial</p>

#### [ Kevin Buzzard (Apr 28 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125799500):
<p>we can get xena to do it for us</p>

#### [ Scott Morrison (Apr 28 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125800546):
<p>Wow... a lot happened while I slept. :-)</p>

#### [ Simon Hudon (Apr 28 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125800763):
<p>Let this be a lesson to you: don't sleep</p>

#### [ Kevin Buzzard (Apr 28 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801226):
<p>Does this look OK:</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801228):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span>
<span class="c1">-- recall the interface for equiv:</span>
<span class="c1">-- C : equiv α β;</span>
<span class="c1">-- the function is C, the function the other way is C.symm, which is also the equiv the other way</span>
<span class="c1">-- and the proofs are C.inverse_apply_apply and C.apply_inverse_apply</span>
<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span> <span class="n">w</span> <span class="n">u&#39;</span> <span class="n">v&#39;</span> <span class="n">w&#39;</span>

<span class="kn">open</span> <span class="n">equiv</span>

<span class="c1">-- Scott&#39;s basic class.</span>
<span class="n">class</span> <span class="n">transportable</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">on_equiv</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">α</span> <span class="n">β</span><span class="o">),</span> <span class="n">equiv</span> <span class="o">(</span><span class="n">f</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="n">β</span><span class="o">))</span>
<span class="o">(</span><span class="n">on_refl</span>  <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">),</span> <span class="n">on_equiv</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">refl</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">refl</span> <span class="o">(</span><span class="n">f</span> <span class="n">α</span><span class="o">))</span>
<span class="o">(</span><span class="n">on_trans</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">d</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">β</span> <span class="n">γ</span><span class="o">),</span> <span class="n">on_equiv</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">trans</span> <span class="n">d</span> <span class="n">e</span><span class="o">)</span> <span class="bp">=</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">on_equiv</span> <span class="n">d</span><span class="o">)</span> <span class="o">(</span><span class="n">on_equiv</span> <span class="n">e</span><span class="o">))</span>

<span class="kn">variables</span>
<span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">}</span> <span class="o">{</span><span class="n">α&#39;</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u&#39;</span><span class="o">}</span> <span class="o">{</span><span class="n">β&#39;</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v&#39;</span><span class="o">}</span> <span class="o">{</span><span class="n">γ&#39;</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w&#39;</span><span class="o">}</span>

<span class="kn">structure</span> <span class="n">canonically_isomorphic_functions</span>
<span class="o">(</span><span class="n">Cα</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">α</span> <span class="n">α&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">Cβ</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">β</span> <span class="n">β&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f&#39;</span> <span class="o">:</span> <span class="n">α&#39;</span> <span class="bp">→</span> <span class="n">β&#39;</span><span class="o">)</span> <span class="c1">-- extends equiv α α&#39;, equiv β β&#39;</span>
<span class="o">:=</span>
<span class="o">(</span><span class="n">commutes</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">Cβ</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f&#39;</span> <span class="o">(</span><span class="n">Cα</span> <span class="n">a</span><span class="o">))</span>
<span class="c1">-- is there a better way to do this with &quot;extends&quot;?</span>

<span class="c1">-- Do I need an interface for this? Why can&#39;t I make this a simp lemma?</span>
<span class="kn">theorem</span> <span class="n">canonically_isomorphic_functions</span><span class="bp">.</span><span class="n">diag_commutes</span>
<span class="o">(</span><span class="n">Cα</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">α</span> <span class="n">α&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">Cβ</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">β</span> <span class="n">β&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f&#39;</span> <span class="o">:</span> <span class="n">α&#39;</span> <span class="bp">→</span> <span class="n">β&#39;</span><span class="o">)</span>
<span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="n">canonically_isomorphic_functions</span> <span class="n">Cα</span> <span class="n">Cβ</span> <span class="n">f</span> <span class="n">f&#39;</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">Cβ</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f&#39;</span> <span class="o">(</span><span class="n">Cα</span> <span class="n">a</span><span class="o">)</span> <span class="o">:=</span> <span class="n">C</span><span class="bp">.</span><span class="n">commutes</span>

<span class="kn">definition</span> <span class="n">canonically_isomorphic_functions</span><span class="bp">.</span><span class="n">refl</span> <span class="o">:</span>
<span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">),</span> <span class="n">canonically_isomorphic_functions</span>
<span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">refl</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">refl</span> <span class="n">β</span><span class="o">)</span> <span class="n">f</span> <span class="n">f</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">f</span><span class="o">,</span><span class="bp">⟨λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span>

<span class="kn">definition</span> <span class="n">canonically_isomorphic_functions</span><span class="bp">.</span><span class="n">symm</span> <span class="o">:</span>
<span class="bp">∀</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f&#39;</span> <span class="o">:</span> <span class="n">α&#39;</span> <span class="bp">→</span> <span class="n">β&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">Cα</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">α</span> <span class="n">α&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">Cβ</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">β</span> <span class="n">β&#39;</span><span class="o">),</span>
<span class="n">canonically_isomorphic_functions</span> <span class="n">Cα</span> <span class="n">Cβ</span> <span class="n">f</span> <span class="n">f&#39;</span> <span class="bp">→</span>
<span class="n">canonically_isomorphic_functions</span> <span class="n">Cα</span><span class="bp">.</span><span class="n">symm</span> <span class="n">Cβ</span><span class="bp">.</span><span class="n">symm</span> <span class="n">f&#39;</span> <span class="n">f</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">f</span> <span class="n">f&#39;</span> <span class="n">Cα</span> <span class="n">Cβ</span> <span class="n">Cf</span><span class="o">,</span><span class="bp">⟨λ</span> <span class="n">a&#39;</span><span class="o">,</span><span class="k">begin</span>
  <span class="n">suffices</span> <span class="o">:</span> <span class="n">Cβ</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">f&#39;</span> <span class="o">(</span><span class="n">Cα</span> <span class="o">(</span><span class="n">Cα</span><span class="bp">.</span><span class="n">symm</span> <span class="n">a&#39;</span><span class="o">)))</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">(</span><span class="n">Cα</span><span class="bp">.</span><span class="n">symm</span> <span class="n">a&#39;</span><span class="o">),</span>
    <span class="k">by</span> <span class="n">simpa</span> <span class="kn">using</span> <span class="n">this</span><span class="o">,</span>
  <span class="n">suffices</span> <span class="o">:</span> <span class="n">Cβ</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">Cβ</span> <span class="o">(</span><span class="n">f</span> <span class="o">(</span><span class="n">Cα</span><span class="bp">.</span><span class="n">symm</span> <span class="n">a&#39;</span><span class="o">)))</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">(</span><span class="n">Cα</span><span class="bp">.</span><span class="n">symm</span> <span class="n">a&#39;</span><span class="o">),</span>
    <span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">Cf</span><span class="bp">.</span><span class="n">commutes</span> <span class="o">(</span><span class="n">Cα</span><span class="bp">.</span><span class="n">symm</span> <span class="n">a&#39;</span><span class="o">)],</span>
  <span class="n">simp</span><span class="o">,</span>
<span class="kn">end</span>
<span class="bp">⟩</span>


<span class="kn">definition</span> <span class="n">canonically_isomorphic_functions</span><span class="bp">.</span><span class="n">trans</span> <span class="o">:</span>
<span class="bp">∀</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f&#39;</span> <span class="o">:</span> <span class="n">α&#39;</span> <span class="bp">→</span> <span class="n">β&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="o">(</span><span class="n">g&#39;</span> <span class="o">:</span> <span class="n">β&#39;</span> <span class="bp">→</span> <span class="n">γ&#39;</span><span class="o">)</span>
<span class="o">(</span><span class="n">Cα</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">α</span> <span class="n">α&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">Cβ</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">β</span> <span class="n">β&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">Cγ</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">γ</span> <span class="n">γ&#39;</span><span class="o">),</span>
<span class="n">canonically_isomorphic_functions</span> <span class="n">Cα</span> <span class="n">Cβ</span> <span class="n">f</span> <span class="n">f&#39;</span> <span class="bp">→</span>
<span class="n">canonically_isomorphic_functions</span> <span class="n">Cβ</span> <span class="n">Cγ</span> <span class="n">g</span> <span class="n">g&#39;</span> <span class="bp">→</span>
<span class="n">canonically_isomorphic_functions</span> <span class="n">Cα</span> <span class="n">Cγ</span> <span class="o">(</span><span class="n">g</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">g&#39;</span> <span class="err">∘</span> <span class="n">f&#39;</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">f</span> <span class="n">f&#39;</span> <span class="n">g</span> <span class="n">g&#39;</span> <span class="n">Cα</span> <span class="n">Cβ</span> <span class="n">Cγ</span> <span class="n">Cf</span> <span class="n">Cg</span><span class="o">,</span><span class="bp">⟨λ</span> <span class="n">a</span><span class="o">,</span><span class="k">begin</span>
  <span class="k">show</span> <span class="n">Cγ</span> <span class="o">(</span><span class="n">g</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">))</span> <span class="bp">=</span> <span class="n">g&#39;</span> <span class="o">(</span><span class="n">f&#39;</span> <span class="o">(</span><span class="n">Cα</span> <span class="n">a</span><span class="o">)),</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">Cg</span><span class="bp">.</span><span class="n">commutes</span><span class="o">,</span><span class="n">Cf</span><span class="bp">.</span><span class="n">commutes</span><span class="o">]</span>
<span class="kn">end</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (Apr 28 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801279):
<p>Scott, I was inspired by your structure</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801280):
<p>Did you see the docs?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801284):
<p>It's a summary of what happened</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801299):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Can you fit these canonically isomorphic functions into your way of thinking?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801342):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> Johan expanded out your idea into a series of little definitions</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801345):
<p>And <span class="user-mention" data-user-id="110064">@Kenny Lau</span> filled them all in</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801346):
<p><a href="https://github.com/kckennylau/Lean/blob/master/johan_challenge.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/johan_challenge.lean">https://github.com/kckennylau/Lean/blob/master/johan_challenge.lean</a></p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801350):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> wrote something I didn't understand yet:</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801351):
<p><a href="https://gist.github.com/rwbarton/d847ef6d1783f0d0859eb80de8327bad" target="_blank" title="https://gist.github.com/rwbarton/d847ef6d1783f0d0859eb80de8327bad">https://gist.github.com/rwbarton/d847ef6d1783f0d0859eb80de8327bad</a></p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801359):
<p>and I wrote some docs</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801360):
<p><a href="https://github.com/kbuzzard/xena/blob/e77228397ad21215a927f93d315edf3cbadbc567/canonical_isomorphism/canonical.md" target="_blank" title="https://github.com/kbuzzard/xena/blob/e77228397ad21215a927f93d315edf3cbadbc567/canonical_isomorphism/canonical.md">https://github.com/kbuzzard/xena/blob/e77228397ad21215a927f93d315edf3cbadbc567/canonical_isomorphism/canonical.md</a></p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801407):
<p>and now I am wondering about whether it's a good idea to think of the concept that a square with equivs down the sides commutes</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801411):
<p>as an equiv between the other two sides</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801426):
<p>The definition doesn't seem to fit into your "transportable" yoga</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801480):
<p>and this</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801481):
<p><code>theorem topological_ring.transportable : transportable topological_ring := sorry</code></p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801482):
<p>is a type mismatch</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801490):
<p>but on the other hand I am pretty sure I want to transport topological rings</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801495):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> I wrote docs</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801497):
<p>Do you want me to add anything else?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801499):
<p>I am currently working on formalising a high-level proof of the exactness statement I want</p>

#### [ Reid Barton (Apr 28 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801605):
<p>I haven't really caught up on any of the recent discussion, but regarding the commutative square with two equivs <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>e</mi><mi>A</mi></msub><mo>:</mo><mi>A</mi><mo>→</mo><msup><mi>A</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">e_A : A \to A'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.901892em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">e</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">A</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mrel">:</span><span class="mord mathit">A</span><span class="mrel">→</span><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>e</mi><mi>B</mi></msub><mo>:</mo><mi>B</mi><mo>→</mo><msup><mi>B</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">e_B : B \to B'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.901892em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">e</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.05017em;">B</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mrel">:</span><span class="mord mathit" style="margin-right:0.05017em;">B</span><span class="mrel">→</span><span class="mord"><span class="mord mathit" style="margin-right:0.05017em;">B</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span>, my current way of thinking about this is that transporting the structure of a map <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>:</mo><mi>A</mi><mo>→</mo><mi>B</mi></mrow><annotation encoding="application/x-tex">f : A \to B</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mrel">:</span><span class="mord mathit">A</span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span> along these two equivs produces a map <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>A</mi><mo mathvariant="normal">′</mo></msup><mo>→</mo><msup><mi>B</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">A' \to B'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span><span class="mrel">→</span><span class="mord"><span class="mord mathit" style="margin-right:0.05017em;">B</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> which will be given by the formula <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>e</mi><mi>B</mi></msub><mo>∘</mo><mi>f</mi><mo>∘</mo><msubsup><mi>e</mi><mi>A</mi><mrow><mo>−</mo><mn>1</mn></mrow></msubsup></mrow><annotation encoding="application/x-tex">e_B \circ f \circ e_A^{-1}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.854239em;"></span><span class="strut bottom" style="height:1.14777em;vertical-align:-0.293531em;"></span><span class="base"><span class="mord"><span class="mord mathit">e</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.05017em;">B</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mbin">∘</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mbin">∘</span><span class="mord"><span class="mord mathit">e</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.854239em;"><span style="top:-2.4064690000000004em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">A</span></span></span><span style="top:-3.1031310000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mathrm mtight">1</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.293531em;"></span></span></span></span></span></span></span></span></p>

#### [ Reid Barton (Apr 28 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801610):
<p>and the condition that your square commutes can then be reinterpreted as saying that the bottom map is the map that you get by transporting the top map along the sides</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801620):
<p>So is this a relation between <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi></mrow><annotation encoding="application/x-tex">f</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>f</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">f'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.946332em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> like <code>equiv</code>?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801622):
<p>Or is this a transportation of the structure?</p>

#### [ Simon Hudon (Apr 28 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801623):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Thanks! </p>
<blockquote>
<p>I am currently working on formalising a high-level proof of the exactness statement I want</p>
</blockquote>
<p>That's a good idea. Maybe apologize everywhere you'd expect to derive a transferable instance</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801661):
<p>Right</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801664):
<p>or admit defeat</p>

#### [ Reid Barton (Apr 28 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125801665):
<p>Which in turn, is going to be the condition you need to know that the fact that you transported across the isomorphisms (like exactness) is actually about your original maps A' -&gt; B' -&gt; C'.</p>

#### [ Reid Barton (Apr 28 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125803762):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I finished writing up the proof of the "three lemma" from <code>transportable</code> instances/lemmas which could plausibly be autogenerated. It's still pretty gross and could probably use some refinement.<br>
<a href="https://gist.github.com/rwbarton/08924014ebc7b1cf68ec624989249aff" target="_blank" title="https://gist.github.com/rwbarton/08924014ebc7b1cf68ec624989249aff">https://gist.github.com/rwbarton/08924014ebc7b1cf68ec624989249aff</a></p>

#### [ Reid Barton (Apr 28 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125804891):
<p>Updated version uses a simp attribute to handle all the goals at once</p>

#### [ Reid Barton (Apr 28 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125805096):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>, you might also be interested in the above--stuff defined as <code>magic</code> is what I would like to have autogenerated</p>

#### [ Johan Commelin (Apr 28 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125805104):
<blockquote>
<p>By adding more <code>transportable</code> classes for type constructors with multiple arguments, we could extend these ideas to situations where we have an isomorphism which respects some existing structure and we want to transport some additional structure (or property) across it. Here is a sketch of the idea: <a href="https://gist.github.com/rwbarton/d847ef6d1783f0d0859eb80de8327bad" target="_blank" title="https://gist.github.com/rwbarton/d847ef6d1783f0d0859eb80de8327bad">https://gist.github.com/rwbarton/d847ef6d1783f0d0859eb80de8327bad</a></p>
</blockquote>
<p>I want some emphasis on this remark by Reid.</p>

#### [ Johan Commelin (Apr 28 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125805143):
<p>This is very important. And our current proposal does not fit...</p>

#### [ Johan Commelin (Apr 28 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125805146):
<p>So, how about this: Every time we define/prove a coercion, we also derive <code>transportable2</code> in the other direction.</p>

#### [ Johan Commelin (Apr 28 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125805153):
<p>Which means, if you have two <code>int</code> that are equal, and one of them came from a <code>nat</code>, then the other one came from the same <code>nat</code></p>

#### [ Johan Commelin (Apr 28 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125805210):
<p>But also, if you have a <code>ring R</code> that is group-isomorphic to some <code>group G</code>, then you get a ring structure on <code>G</code> for free, and the underlying group structure of this new ring structure is exactly the group structure on <code>G</code> that you started with.</p>

#### [ Johan Commelin (Apr 28 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125805211):
<p>I think coercions exactly determine where transport of structure applies.</p>

#### [ Johan Commelin (Apr 28 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125805440):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Is what I'm saying canonically isomorphic to your remarks? I.e., did I transport the structure of your remarks?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806580):
<p>So I pushed my work on "canonically isomorphic functions" between canonically isomorphic types</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806581):
<p><a href="https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/sheaf_canonical.lean" target="_blank" title="https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/sheaf_canonical.lean">https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/sheaf_canonical.lean</a></p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806594):
<p>Let me state what I think the state of things is</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806595):
<p>We had an idea about defining a class called transportable</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806597):
<p>and I want to define a structure called a canonical isomorphism</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806598):
<p>which doesn't have to be the maths one</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806638):
<p>but it has to be good enough to deal the mortal blow to the final boss in affine schemes.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806648):
<p>Transportable originally ate a function <code>Type -&gt; Type</code> or perhaps <code>Type u -&gt; Type v</code> depending on what mood people were in. Because this is a CS thing I suppose we will end up with <code>Type u -&gt; Type v</code></p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806649):
<p>But now we want it to eat more</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806690):
<p>for example we want it to eat the instance of the type class resolution system which sends a ring to an additive group</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806699):
<p>and spit out a theorem that says that if a equiv a' then the square commutes up to definitional equality.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806700):
<p>by which I mean Lean definitional equality, ideally.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806742):
<p>the square goes from ring a to ring a' on the top, from group a to group a' on the bottom, and the maps down are coming from the type class inference system</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806745):
<p>So which instances of type class inference will commute with equiv in this way?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806802):
<p>Can we not _assume_ that if alpha is a type which happens to have both a group structure and a ring structure then the group structure associated to the ring structure is the one which the type class inference system would associate to the ring structure?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806803):
<p>Because if this is not the case then the Diamond is nigh, right?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806843):
<p>So this would seem like the correct theorem to prove</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806848):
<p>Oh I have a question <span class="user-mention" data-user-id="112680">@Johan Commelin</span> !</p>

#### [ Reid Barton (Apr 28 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806849):
<p>Kevin, I'm not sure how helpful this remark will be, but your <code>canonically_isomorphic_functions Cα Cβ f f'</code> is in my setup <code>f' = transport2 (→) Cα Cβ f</code></p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806850):
<p>Do you know those WIP docs?</p>

#### [ Andrew Ashworth (Apr 28 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806852):
<p>a tactic that takes two types, a function relating the two, and from Prop (input 1) return Prop (input 2), is that what people are discussing?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806853):
<p>Mario gave me an example of a way to break the type class resolution system in a really annoying way</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806858):
<p>What happens if you try and prove that those maps are all canonical?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806861):
<p>Does that make any sense?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806863):
<p>Reid, I am sure you are thinking about it in a better way than me</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806865):
<p>and I am absolutely convinved that we should get this as abstract as possible</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806866):
<p>thanks for the pointer!</p>

#### [ Johan Commelin (Apr 28 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806904):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> Yes, more or less.</p>

#### [ Reid Barton (Apr 28 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806908):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>, I'm not sure what you mean by coercion. Are you talking about <code>has_coe</code>?</p>

#### [ Johan Commelin (Apr 28 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806909):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> The basic example. Given <code>a b : Type</code>, <code>equiv a b</code> and also <code>[group a]</code> we want to automagically have <code>group b</code></p>

#### [ Andrew Ashworth (Apr 28 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806915):
<p>i'll mention again the transfer tactic in core lean that produces <code>int</code> from <code>pairs of nat</code>, and the paper that describes it is linked earlier... unless i'm totally off-base</p>

#### [ Johan Commelin (Apr 28 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806917):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> I'm still a novice. But I guess that is what I mean.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806918):
<p><a href="https://github.com/kbuzzard/mathlib/blob/WIP_docs/docs/WIPs/type_class_inference.md" target="_blank" title="https://github.com/kbuzzard/mathlib/blob/WIP_docs/docs/WIPs/type_class_inference.md">https://github.com/kbuzzard/mathlib/blob/WIP_docs/docs/WIPs/type_class_inference.md</a></p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806958):
<p>In the "to be tidied" section</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806960):
<p>there is Mario busting the type class inference system</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806962):
<p>following an idea of mine</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806963):
<p>trying to find a fairly explicit example of how it can bust</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125806966):
<p>because two natural numbers are equal but the proof is not "rfl"</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807014):
<p>The type class system breaks quite badly if you find two different ways of getting from A to B</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807015):
<p>On the other hand I am pretty sure that I want to allow more than one canonical isomorphism between two objects</p>

#### [ Andrew Ashworth (Apr 28 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807021):
<p>transfer in action: constructing an efficient representation of <code>int</code> from the pre-int pair of nat... <a href="https://github.com/leanprover/lean/blob/master/library/init/data/int/basic.lean" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/data/int/basic.lean">https://github.com/leanprover/lean/blob/master/library/init/data/int/basic.lean</a></p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807022):
<p>For example I think I want the sum of two canonical isomorphisms from a group to a group to be a canonical isomorphism</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807024):
<p>I know int.basic pretty well</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807025):
<p>What does this have to do with anything?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807026):
<p>I understand the int typeclass</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807066):
<p>and you are saying that int canonically bijects with nat + nat?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807067):
<p>I would say that that bijection is not canonical</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807068):
<p>It's a junk theorem I think</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807069):
<p>In a parallel universe int was constructed as a quotient type on nat x nat</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807072):
<p>or one day Leo changes int to this</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807075):
<p>and nobody notices</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807076):
<p>because maybe we all use the int interface</p>

#### [ Andrew Ashworth (Apr 28 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807079):
<p>isn't that the tactic machinery you're interested in, however?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807080):
<p>Evidence that that bijection is not canonical is that it does not behave well with respect to arithmetic operations like +</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807081):
<p>Oh -- I see</p>

#### [ Johan Commelin (Apr 28 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807084):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Concerning Mario's example. Basically, you prove that <code>nat \times nat</code> has a ring structure, and then coerce by taking the sum. But the sum is not a ring homomorphism... Is that what is going on?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807085):
<p>I'm afraid my eyes glaze over whenever I see tactic machinery</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807123):
<p>I don't understand it at all</p>

#### [ Reid Barton (Apr 28 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807133):
<p>It actually is using <code>nat \times nat</code>.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807134):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> no multiplication is involved</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807151):
<p>no multiplication of nats at least</p>

#### [ Kenny Lau (Apr 28 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807153):
<blockquote>
<p>because maybe we all use the int interface</p>
</blockquote>
<p>nope. lots of things in mathlib use the definition of int</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807156):
<p>Johan -- the only canonical thing you are allowed to do with nats is add them up in Mario's example</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807157):
<p>So there's a type which carries a nat</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807194):
<p>and one which carries two nats</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807197):
<p>and the type class inference system will take you from the two nat guys to the one nat guys by just adding up their two nats</p>

#### [ Johan Commelin (Apr 28 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807198):
<p>Ah, sorry, brainfarting again</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807202):
<p>But there is also this product construction</p>

#### [ Reid Barton (Apr 28 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807203):
<p>Er, to clarify, the <code>int</code> transfer stuff (which I don't know anything about) uses <code>nat \times nat</code></p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807209):
<p>and you just add up the nats</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807214):
<p>so now there's two ways of getting from a pair <code>(a,b)</code> of two-nat guys</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807215):
<p>to one one-nat guy</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807256):
<p>and <code>(r+s)+(t+u)</code> is not definitionally equal to <code>(r+t)+(s+u)</code></p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807257):
<p>you need a proof by induction for that</p>

#### [ Johan Commelin (Apr 28 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807259):
<p>Right, that's what is going on</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807264):
<p>and then rw stops working</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807268):
<p>because rw keeps track of the exact definitions of the instances</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807269):
<p>no</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807270):
<p>the types keep track</p>

#### [ Johan Commelin (Apr 28 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807271):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> Which lines should we look at, to see transfer in action, in int/basic.lean</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807273):
<p>and rw looks at the types</p>

#### [ Andrew Ashworth (Apr 28 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807315):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> line 399 proves the integers form a ring</p>

#### [ Andrew Ashworth (Apr 28 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807324):
<p>the setup starts at line 269</p>

#### [ Johan Commelin (Apr 28 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807367):
<p>I have the instinctive feeling that this is related, but somewhat different from what we are discussing.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807370):
<p>I guess I understand much less of this part of int.nat than I remembered</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807375):
<p>what is all this rel stuff?</p>

#### [ Johan Commelin (Apr 28 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807378):
<p>But maybe I don't get what this part of the file is trying to prove</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807437):
<p>I see.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807439):
<p><code>rel_int_nat_nat (z : int)</code></p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807442):
<p>is the set of pairs (a,b) in nat x nat</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807446):
<p>such that a - b = z</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807447):
<p>so it's the equivalence class</p>

#### [ Johan Commelin (Apr 28 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807486):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> Are you saying: there is a ring structure on a quotient of <code>nat \times nat</code> and there is a bijection between <code>Z</code> and this quotient. And this is how we transfer the ring structure onto <code>Z</code></p>

#### [ Johan Commelin (Apr 28 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807487):
<p>Is that what is going on?</p>

#### [ Johan Commelin (Apr 28 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807489):
<p>I think it is. And if so, that is a perfect example.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807490):
<p>So there's all this rel stuff</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807492):
<p>and suddenly there are some transfer tactics and it's all over.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807493):
<p>Who wrote that stuff?</p>

#### [ Andrew Ashworth (Apr 28 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807494):
<p>johannes hoezl</p>

#### [ Johan Commelin (Apr 28 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807499):
<blockquote>
<p>Who wrote that stuff?</p>
</blockquote>
<p><code>git blame</code></p>

#### [ Johan Commelin (Apr 28 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807501):
<p><a href="https://github.com/leanprover/lean/blame/f59c2f0ef59fdc1833b6ead6adca721123bd7932/library/init/data/int/basic.lean#L393" target="_blank" title="https://github.com/leanprover/lean/blame/f59c2f0ef59fdc1833b6ead6adca721123bd7932/library/init/data/int/basic.lean#L393">https://github.com/leanprover/lean/blame/f59c2f0ef59fdc1833b6ead6adca721123bd7932/library/init/data/int/basic.lean#L393</a></p>

#### [ Johan Commelin (Apr 28 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807543):
<p>Andrew, so now, we want to abstract this notion of transfer, and automatically derive it for lots of structures, given equivalences between types.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807544):
<p>I see</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807545):
<p>Maybe he has something to say about what it means to be canonically isomorphic.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807546):
<p>Johannes introduced the transfer method</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807594):
<p>Scott introduced this class with this cool <code>transportable</code> name and I've spent some time over the last 24 hours (I should probably sleep at some point) creating instances of this class and moving them around.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807597):
<p>What started me off was Johan's list of levels</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807600):
<p>If we have a more general idea</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807601):
<p>do we have another game to play?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807647):
<p>Johan -- here's how to catch an instance of the type class resolution system</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807648):
<div class="codehilite"><pre><span></span>theorem T {α : Type u} [ring α] : add_group α := by apply_instance
#print T
</pre></div>

#### [ Kevin Buzzard (Apr 28 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807654):
<p><code>apply_instance</code> is a tactic which tries to solve things by type class inference</p>

#### [ Johan Commelin (Apr 28 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807659):
<p>Ok, let me think about how that might be useful</p>

#### [ Kevin Buzzard (Apr 28 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807683):
<p>Unfortunately I don't think we have an instance of <code>transportable add_group</code> yet</p>

#### [ Kevin Buzzard (Apr 28 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807701):
<p>Kenny wrote the ring one</p>

#### [ Kevin Buzzard (Apr 28 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807702):
<p>and one could copy</p>

#### [ Kevin Buzzard (Apr 28 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807706):
<p>These maps are in general forgetful functors</p>

#### [ Reid Barton (Apr 28 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807707):
<p>I think you would just delete all the lines which don't appear in <code>add_group</code>, yeah.</p>

#### [ Reid Barton (Apr 28 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807708):
<p>Then I guess your square involving forgetful functors and transported equivalences ought to commute definitionally</p>

#### [ Kevin Buzzard (Apr 28 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807716):
<div class="codehilite"><pre><span></span>@[instance, priority 100]
def add_comm_group.to_add_group : Π (α : Type u) [s : add_comm_group α], add_group α :=
λ (α : Type u) [s : add_comm_group α],
  {add := add_comm_group.add s,
   add_assoc := _,
   zero := add_comm_group.zero α s,
   zero_add := _,
   add_zero := _,
   neg := add_comm_group.neg s,
   add_left_neg := _}
</pre></div>

#### [ Kevin Buzzard (Apr 28 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807717):
<p>I am sure it will</p>

#### [ Kevin Buzzard (Apr 28 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807758):
<p>A different class of instance is the following:</p>

#### [ Kevin Buzzard (Apr 28 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807771):
<p>Wait</p>

#### [ Kevin Buzzard (Apr 28 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807772):
<p>this fails:</p>

#### [ Kevin Buzzard (Apr 28 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807803):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">T</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">group</span> <span class="n">β</span><span class="o">]</span> <span class="o">:</span>
<span class="n">group</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">β</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
</pre></div>

#### [ Kevin Buzzard (Apr 28 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807814):
<p>I was assuming "product of groups is a group" would be there</p>

#### [ Kevin Buzzard (Apr 28 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807815):
<p>Maybe it's in mathlib</p>

#### [ Reid Barton (Apr 28 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807912):
<p>I think you're talking about instances like</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">blah</span> <span class="o">[</span><span class="n">ring</span> <span class="n">t</span><span class="o">]</span> <span class="o">:</span> <span class="n">some_other_thing</span> <span class="n">t</span> <span class="o">:=</span> <span class="bp">...</span>
</pre></div>

#### [ Reid Barton (Apr 28 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125807968):
<p>Which is essentially just some arbitrary user-defined function <code>ring t \to some_other_thing t</code></p>

#### [ Reid Barton (Apr 28 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125808150):
<p>So now your question from earlier becomes whether an arbitrary function of type <code>Π α : Type, ring α → add_comm_group α</code> will commute with the equivalences <code>ring α ≃ ring β</code>, <code>add_comm_group α ≃ add_comm_group β</code> obtained by transportation of structure along an equivalence <code>α ≃ β</code>.  The answer is (probably) that it is true for every function you can define in Lean, but you can't prove it as a theorem within Lean that applies to an arbitrary function. This is parametricity again</p>

#### [ Johan Commelin (Apr 28 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125808311):
<p>Ok, and now we need some magic to automaticlly prove it for every function that we define.</p>

#### [ Johan Commelin (Apr 28 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125808314):
<p>And then we don't care that we can't prove it for arbitrary functions. And we don't have to repeat ourselves in dozens of tiny variations.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125808358):
<p>Here's an instance for "product of groups is a group"</p>

#### [ Kevin Buzzard (Apr 28 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125808359):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">prod_group</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">[</span><span class="n">HG</span> <span class="o">:</span> <span class="n">group</span> <span class="n">G</span><span class="o">]</span> <span class="o">[</span><span class="n">HH</span> <span class="o">:</span> <span class="n">group</span> <span class="n">H</span><span class="o">]</span> <span class="o">:</span> <span class="n">group</span> <span class="o">(</span><span class="n">G</span> <span class="bp">×</span> <span class="n">H</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">g1</span><span class="o">,</span><span class="n">h1</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">g2</span><span class="o">,</span><span class="n">h2</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">g1</span> <span class="bp">*</span> <span class="n">g2</span><span class="o">,</span><span class="n">h1</span> <span class="bp">*</span> <span class="n">h2</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">mul_assoc</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">g1</span><span class="o">,</span><span class="n">h1</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">g2</span><span class="o">,</span><span class="n">h2</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">g3</span><span class="o">,</span><span class="n">h3</span><span class="bp">⟩</span><span class="o">,</span><span class="n">prod</span><span class="bp">.</span><span class="n">ext</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">mul_assoc</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span><span class="n">mul_assoc</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_⟩</span><span class="o">,</span>
  <span class="n">one</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">HG</span><span class="bp">.</span><span class="n">one</span><span class="o">,</span><span class="n">HH</span><span class="bp">.</span><span class="n">one</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">one_mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">g</span><span class="o">,</span><span class="n">h</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">prod</span><span class="bp">.</span><span class="n">ext</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">one_mul</span> <span class="bp">_</span><span class="o">,</span><span class="n">one_mul</span> <span class="bp">_⟩</span><span class="o">,</span>
  <span class="n">mul_one</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">g</span><span class="o">,</span><span class="n">h</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">prod</span><span class="bp">.</span><span class="n">ext</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">mul_one</span> <span class="bp">_</span><span class="o">,</span><span class="n">mul_one</span> <span class="bp">_⟩</span><span class="o">,</span>
  <span class="n">inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">g</span><span class="o">,</span><span class="n">h</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">group</span><span class="bp">.</span><span class="n">inv</span> <span class="n">g</span><span class="o">,</span><span class="n">group</span><span class="bp">.</span><span class="n">inv</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">,</span><span class="c1">--begin end,--λ ⟨g,h⟩, ⟨HG.inv g,HH.inv h⟩,</span>
  <span class="n">mul_left_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">g</span><span class="o">,</span><span class="n">h</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">prod</span><span class="bp">.</span><span class="n">ext</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">mul_left_inv</span> <span class="n">g</span><span class="o">,</span><span class="n">mul_left_inv</span> <span class="n">h</span><span class="bp">⟩</span>
<span class="o">}</span>
</pre></div>

#### [ Reid Barton (Apr 28 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125808360):
<p>Yes, though it doesn't sound very easy, because the meta-level argument is some induction over the definition of the function, and I'm not sure whether a tactic even has access to the syntactic definition of a function</p>

#### [ Reid Barton (Apr 28 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125808365):
<p>Maybe Mario could comment when he reappears</p>

#### [ Johan Commelin (Apr 28 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125808463):
<blockquote>
<p>I'm not sure whether a tactic even has access to the syntactic definition of a function</p>
</blockquote>
<p>Right. This is the important question. If one of the Lean experts could help out, that would be awesome.</p>

#### [ Scott Morrison (Apr 28 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125808787):
<p>Yes, in the tactic world we can look at the syntactic definitions of things.</p>

#### [ Scott Morrison (Apr 28 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125808826):
<p>It's all just <code>expr</code>s.</p>

#### [ Mario Carneiro (Apr 28 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125813008):
<p>Geez, you guys work too fast. I was going to say as a followup to my last post that parametricity is not as simple as <code>transportable</code>, and it seems like you are already running into its limitations. The problem is that it only works for unary type operators <code>Type u -&gt; Type v</code>, but for the induction to work you need a parametricity statement for many different sorts of higher order type operators. For example, a <code>Type -&gt; Type -&gt; Type</code> operator is parametric if whenever <code>A ~= A'</code> and <code>B ~= B'</code> then <code>F A B ~= F A B</code>. A <code>(Type -&gt; Type) -&gt; Type</code> operator is parametric if whenever <code>F</code> and <code>F'</code> are such that <code>A ~= A'</code> implies <code>F A ~= F' A'</code>, then <code>G F ~= G F'</code>.</p>
<p>There is some recursive definition of parametric that goes over the type of the higher-order functor, but you can't even define this recursion in lean since <code>Type</code> is not inductively generated by the Pi type and other stuff. But you can define tactics that produce such definitions, and tactics that prove that everything you care about satisfy its appropriate parametricity theorem. This is what "Theorems for free!" is about.</p>

#### [ Mario Carneiro (Apr 28 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125813265):
<p>Also, in the presence of <code>choice</code> parametricity fails, so it's not actually true that all lean-definable terms are parametric. For example, given choice you have that everything is decidable, in particular type equality, so you can make definitions like <code>if x = nat then nat else empty</code> which is nonempty on <code>nat</code> and empty on <code>int</code> even though <code>nat ~= int</code>.</p>

#### [ Mario Carneiro (Apr 28 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125813314):
<p>Or at least, that would be a counterexample if you knew <code>nat != int</code>. This comes back to the possible consistency of <code>A ~= B -&gt; A = B</code>; assuming it's consistent with lean <code>nat != int</code> is not provable, although there are certainly models of lean which refute <code>nat = int</code>.</p>

#### [ Johan Commelin (Apr 28 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125819688):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> There you have your counterexample.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820700):
<p>I am not interested in weird questions about whether int is equal to nat.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820703):
<p>It seems to me that a canonical isomorphism is a pair of things</p>

#### [ Kenny Lau (Apr 28 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820705):
<p>I don't remember anyone asking your opinion :P</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820706):
<p>firstly an equiv</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820707):
<p>:-)</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820710):
<p>and secondly a promise</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820714):
<p>and the promise is that you promise not to do stuff which isn't respected by the equiv</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820716):
<p>And in ZFC this promise is brushed under the carpet and there is a gentleman's agreement</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820756):
<p>and all good mathematicians are aware of the agreement</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820760):
<p>But in dependent type theory we have a bunch of uncultured computer scientists</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820761):
<p>who don't know our gentlemanly ways</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820763):
<p>and they are asking to see more details of the promise</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820764):
<p>and what is worse</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820768):
<p>they are demanding that we keep our promises.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820772):
<p>They are not buying the argument that we are gentlemen who keep our promises</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820773):
<p>they want to see proof</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820777):
<p>so now it is the mathematician's job to give them that proof.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820819):
<p>There is a wonderful story which goes back to a paper by Dick Gross in the early 1990s which was crucial in Wiles' original proof of Fermat's Last Theorem</p>

#### [ Kenny Lau (Apr 28 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820820):
<blockquote>
<p>But in dependent type theory we have a bunch of uncultured computer scientists</p>
</blockquote>
<p>right. you just said this in front of a bunch of computer scientists.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820823):
<p>Kenny: my provocative language is intentional</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820829):
<p>I am trying to isolate what I believe is an important issue</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820831):
<p>and I am using provocative language in an attempt to explain it and to get people interested in it.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820832):
<p>The story is that Dick Gross needed to analyse two cohomology groups</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820872):
<p>and these cohomology groups were coming from two completely different cohomology theories</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820874):
<p>but someone had written down a map between them which was completely natural and depended on no choices</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820876):
<p>and they had proved that this map was an isomorphism</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820877):
<p>and had asserted that it was a canonical isomorphism</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820879):
<p>and we all believed them</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820885):
<p>And Dick Gross needed to use some extra structure on these cohomology theories</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820887):
<p>each of the cohomology theories came with a bunch of linear maps called Hecke operators</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820890):
<p>which are completely canonically defined operators</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820941):
<p>and Gross asserted without proof that the canonical isomorphism identified the canonically-defined actions of the Hecke operators on each of the theories</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820943):
<p>and the referee was Jean-Pierre Serre</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820944):
<p>and he caught this</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820945):
<p>and he demanded that Gross prove it</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820948):
<p>and this would have held up publication of this important paper for probably quite some time</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820949):
<p>so Gross said no</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820958):
<p>and instead he wrote in the introduction to his paper that his theorem depended on unchecked compatibilities between canonically defined operators on canonically isomorphic objects</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125820999):
<p>And Brian Conrad got a student of his to work out the details and the student wrote an entire PhD thesis checking that the diagrams did indeed commute</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821000):
<p>because the proof was by no means formal</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821001):
<p>and I am now wondering</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821002):
<p>whether actually</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821005):
<p>one could write a tactic to prove that theorem</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821006):
<p>That would be an extraordinary project</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821009):
<p>because that would be a computer not only checking the main result of a Stanford student's PhD thesis</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821013):
<p>it would be a computer program which automatically generated the main result of a Stanford student's PhD thesis.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821014):
<p>A _mathematics_ student.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821053):
<p>And the reason a tactic might be able to prove this</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821054):
<p>would be that when you prove that various maps are isomorphisms</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821055):
<p>you don't just say "they are canonical"</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821056):
<p>you write down what you mean, properly</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125821063):
<p>and then you check that all the operations that you do respect the canonical maps</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125822241):
<p>OK so here is a challenge to the mathematics / computer science community:</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125822282):
<p>write a tactic which proves that Gross' canonically defined Hecke operators on his canonically isomorphic spaces all match up with each other</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125822286):
<p>That sounds like a really fun project</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125822290):
<p>because it will need a mix of genuinely deep mathematics</p>

#### [ Kenny Lau (Apr 28 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125822291):
<p>for M1R?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125822292):
<p>and clever programming</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125822293):
<p>Kenny, that would be a great first year project :-)</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125822295):
<p>It would be an even better PhD project.</p>

#### [ Simon Hudon (Apr 28 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125826517):
<blockquote>
<blockquote>
<p>But in dependent type theory we have a bunch of uncultured computer scientists</p>
</blockquote>
<p>right. you just said this in front of a bunch of computer scientists.</p>
</blockquote>
<p>I'm not sure if it's that I'm too uncultured to be insulted but it feels like Kevin paid the CS / formal methods community a beautiful compliment</p>

#### [ Johan Commelin (Apr 28 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125827355):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I love this story!</p>

#### [ Johan Commelin (Apr 28 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125827363):
<p>Is this story only oral folklore? Or is there some written version (besides what you just wrote down in the chat)? I would love to be able to point others towards this story</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831766):
<p>just google for Bryden Cais' PhD thesis</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831768):
<p>I think it would be an absolutely monumental challenge to get a computer to prove it</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831809):
<p>but anyone who tried would probably learn a lot about what a mathematician means when they say something is canonical</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831813):
<p>Bryden is in AZ now</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831822):
<p>and go from there to Dick Gross' paper</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831862):
<p>and see the explanation about the unchecked compatibilities, a throw-away "well this is not 100% rigorous" admission in a paper which a few years later was to play a fundamental role in Wiles' proof of Fermat's Last Theorem.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831863):
<p>And mathematicans worried not one jot</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831864):
<p>See Wiles' FLT paper and verify it references Gross' paper.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831872):
<p>perhaps because one day we knew a computer would come along and check the details.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831918):
<p>I bet Taylor-Wiles (the paper that fills in the gap) references the paper too.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831926):
<p>Absolutely wonderful.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831927):
<p>I just checked.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831928):
<p><a href="http://www.math.ias.edu/~rtaylor/hecke.pdf" target="_blank" title="http://www.math.ias.edu/~rtaylor/hecke.pdf">http://www.math.ias.edu/~rtaylor/hecke.pdf</a></p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831931):
<p>Seminal paper by Taylor and Wiles filling in the gap in Wiles' proof of Fermat's Last Theorem.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831933):
<p>Theorem: We fill in a gap.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831935):
<p>Footnote: WARNING : paper contains gap</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831980):
<p>but we're not worried about that one</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831986):
<p>And there was me thinking we were doing ZFC</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125831987):
<p>When did we stop?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125832031):
<p>Bryden Cais thesis 2007, 12 years after FLT proved.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125832033):
<p>You know what, I am pretty sure that the experts knew that there was a way around Gross' problems.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125832036):
<p>So probably nobody made a fuss</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125832040):
<p>they only occurred in certain "higher weight" situations</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125832042):
<p>and the applications to FLT may not need that level of generality</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125832043):
<p>but I'm not sure you'll find a published explanation of this</p>

#### [ Kevin Buzzard (Apr 28 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125832083):
<p>I'll ask Conrad whether he thinks his student proved Fermat's Last Theorem</p>

#### [ Scott Morrison (Apr 29 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125834143):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> ,</p>
<blockquote>
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> There you have your counterexample.</p>
</blockquote>
<p>I haven't quite caught up on this thread, but does this mean that "in the presence of <code>choice</code> I owe <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>  a beer"? Ok, I'll honour that anyway.</p>

#### [ Reid Barton (Apr 29 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125839073):
<p>Do we have parametricity for things which are not <code>noncomputable</code>?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 04:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125839370):
<p>I will remark that the thing I want to prove is functorial, is noncomputable.</p>

#### [ Kevin Buzzard (Apr 29 2018 at 04:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125839420):
<p>attempting to make it computable would not be a question I was that interested in</p>

#### [ Kevin Buzzard (Apr 29 2018 at 04:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125839421):
<p>but I am unsure as to whether or not it can be done. This goes back to the old question of how to represent the functions on a standard open in an affine scheme</p>

#### [ Johan Commelin (Apr 29 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125846328):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> I guess so... you didn't post any formal requirements, and I am not a judge (-;</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854648):
<p>Church numerals are kind of cool</p>

#### [ Kenny Lau (Apr 29 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854656):
<p>what is that message related to?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854697):
<p><a href="https://github.com/kbuzzard/xena/blob/06476597bd53a111bb3060d2d583e04c972d5204/canonical_isomorphism/church_blog_questions.lean" target="_blank" title="https://github.com/kbuzzard/xena/blob/06476597bd53a111bb3060d2d583e04c972d5204/canonical_isomorphism/church_blog_questions.lean">https://github.com/kbuzzard/xena/blob/06476597bd53a111bb3060d2d583e04c972d5204/canonical_isomorphism/church_blog_questions.lean</a></p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854698):
<p>Kenny, there are some more challenges for you</p>

#### [ Kenny Lau (Apr 29 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854699):
<p>nice, i love challenges</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854700):
<p>I'm sure you won't have much trouble with succ, add and mul</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854701):
<p>do you know how to do pow?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854702):
<p>And what about Ackermann?</p>

#### [ Kenny Lau (Apr 29 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854707):
<p>oh i thought you were talking about those proofs in your file</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854708):
<p>And can you prove the equiv?</p>

#### [ Kenny Lau (Apr 29 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854709):
<p>they aren't equivalent</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854710):
<p>The link I just posted is to a file with some sorries</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854711):
<p>but I can fill in some of the sorries</p>

#### [ Kenny Lau (Apr 29 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854712):
<p>they aren't provable</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854713):
<p>stop</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854714):
<p>some are provable because I proved them</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854715):
<p>you need to look at the file</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854752):
<p>for each sorry in the file, either fill it in, or tell me confidently that it cannot be filled in</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854755):
<p>that's your challenge</p>

#### [ Kenny Lau (Apr 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854756):
<p>ok</p>

#### [ Kenny Lau (Apr 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854757):
<p>I saw the word blog :D</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854758):
<p>yes, I am going to write another blog post</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854760):
<p>talking of blog posts</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854761):
<p>I have a file which is both beautiful and disgusting</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854767):
<p>beautiful because all the proofs are really uncluttered</p>

#### [ Kenny Lau (Apr 29 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854768):
<p>that tone in <code>KB doesn't understand</code> though lmao</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854769):
<p>disgusting because I use constants</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854814):
<p>Kenny -- is nat some inductive type which is somehow canonically associated to the Pi type of church numerals?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854815):
<p>look at my definition of <code>to_nat</code></p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854816):
<p>it takes all the ingredients of nat exactly once, and nothing more</p>

#### [ Kenny Lau (Apr 29 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854821):
<p>sure, <code>Π X : Type, (X → X) → X → X</code> is the Church encoding of the type <code>nat</code></p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854822):
<p>I don't know what that means</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854823):
<p>which types have a church encoding?</p>

#### [ Kenny Lau (Apr 29 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854824):
<p>inductive types I guess</p>

#### [ Kenny Lau (Apr 29 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854825):
<p>not very sure</p>

#### [ Kenny Lau (Apr 29 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854826):
<p>maybe pi types as well</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854865):
<p>so you cannot formalise the assertion you just made?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854866):
<p>You are making some informal statement?</p>

#### [ Kenny Lau (Apr 29 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854867):
<p>I don't know everything about church encoding</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854868):
<p>but is there some rigorous statement that an expert can make?</p>

#### [ Kenny Lau (Apr 29 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854869):
<p>I believe so</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854870):
<p>"church encoding" has a formal definition?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854876):
<p>What is the church encoding of a scheme?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854877):
<p>what is the church encoding of int as defined in Lean?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854878):
<p>what is the church encoding of list?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854879):
<p>what is the church encoding of bool?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854880):
<p>what is the church encoding of false?</p>

#### [ Kenny Lau (Apr 29 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854881):
<blockquote>
<p>what is the church encoding of bool?</p>
</blockquote>
<p><code>X -&gt; X -&gt; X</code> :P</p>

#### [ Kenny Lau (Apr 29 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854918):
<blockquote>
<p>what is the church encoding of false?</p>
</blockquote>
<p><code>X</code></p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854921):
<p>Does the church encoding of anything just have one type X?</p>

#### [ Kenny Lau (Apr 29 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854922):
<blockquote>
<p>Does the church encoding of anything just have one type X?</p>
</blockquote>
<p>didn't I just answer that question</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854923):
<p>No</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854924):
<p>you only answered it for bool and false</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854930):
<p>and nat</p>

#### [ Kenny Lau (Apr 29 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854931):
<p>what do you mean by one type X?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854932):
<p>I mean that all your answers so far (for nat, bool and false) only had one letter in</p>

#### [ Kenny Lau (Apr 29 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854972):
<p>oh, I misunderstood "anything"</p>

#### [ Kenny Lau (Apr 29 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125854973):
<p>english ~</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855019):
<p>did you do ack yet?</p>

#### [ Kenny Lau (Apr 29 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855020):
<p>I've been searching church encoding online</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855021):
<p>here's a much easier</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855022):
<p>one</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855023):
<p><code>pred</code></p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855028):
<p>The untyped lambda calculus is so last year</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855030):
<p>I want to know how it works in Lean</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855068):
<p>although these questions might not be good for this thread, because did you say that it was not true that nat was equiv to church nat?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855071):
<p>or not provable?</p>

#### [ Kenny Lau (Apr 29 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855072):
<p>if your functions are computable, then I believe they will represent some natural number</p>

#### [ Kenny Lau (Apr 29 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855075):
<p>but noncomputable functions are permitted in Lean, breaking the equivalence</p>

#### [ Kenny Lau (Apr 29 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855076):
<p>(but I can't give you any example :P)</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855124):
<p>So one can write down a <code>noncomputable</code> church nat which is provably not in the image of <code>of_nat</code>?</p>

#### [ Kenny Lau (Apr 29 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855127):
<p>I don't know</p>

#### [ Kenny Lau (Apr 29 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855128):
<p>maybe you can write something like <code>if X == int then _ else _</code></p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855129):
<p>well maybe it won't come up in the mechanics exam</p>

#### [ Kenny Lau (Apr 29 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855130):
<p>...</p>

#### [ Kenny Lau (Apr 29 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855214):
<blockquote>
<p>what is the church encoding of list?</p>
</blockquote>
<p><code>list A = X -&gt; (A -&gt; X -&gt; X) -&gt; X</code> I guess. can't find anything online</p>

#### [ Kenny Lau (Apr 29 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855302):
<blockquote>
<p>what is the church encoding of int as defined in Lean?</p>
</blockquote>
<p><code>nat -&gt; nat -&gt; X</code>, I guess</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855303):
<p>that doesn't look like something that Church would like</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855304):
<p>it has something in which isn't X</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855309):
<p>or -&gt; or ()</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855311):
<p>Is it OK?</p>

#### [ Kenny Lau (Apr 29 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855313):
<p>but <code>list</code> isn't a type</p>

#### [ Kenny Lau (Apr 29 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855314):
<p><code>list</code> is a function from types to types</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855315):
<p>I see</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855317):
<p>I thought those were types too ;-)</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855354):
<p><a href="https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/church_blog_questions.lean" target="_blank" title="https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/church_blog_questions.lean">https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/church_blog_questions.lean</a></p>

#### [ Kenny Lau (Apr 29 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855356):
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">check</span> <span class="n">list</span>
<span class="c1">--list : Type u_1 → Type u_1</span>
</pre></div>

#### [ Kevin Buzzard (Apr 29 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855358):
<p>I slightly updated the church numerals file</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855359):
<p>I am a bit unclear about what is provable and what isn't.</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855364):
<p>I also have a file with some solutions in</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855370):
<p>and the only reason I did not push it</p>

#### [ Kevin Buzzard (Apr 29 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125855372):
<p>is because the definition of <code>pow</code> on church nats is so beautiful that I wanted to let you find it if you hadn't seen it already</p>

#### [ Kenny Lau (Apr 29 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125856002):
<p>interesting</p>

#### [ Kevin Buzzard (Apr 29 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125856248):
<p>I am finally trying to write down a "canonical isomorphism" proof of the result I need to apply Chris' Lemma to the affine scheme boss</p>

#### [ Kevin Buzzard (Apr 29 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125856249):
<p>Does this structure already have a name?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125856250):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">is_unique_ring_hom</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">ring</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">is_unique</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">g</span><span class="o">],</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">f</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Apr 29 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125856294):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">is_ring_hom</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">ring</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">map_add</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span><span class="o">},</span> <span class="n">f</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">f</span> <span class="n">y</span><span class="o">)</span>
<span class="o">(</span><span class="n">map_mul</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span><span class="o">},</span> <span class="n">f</span> <span class="o">(</span><span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">f</span> <span class="n">y</span><span class="o">)</span>
<span class="o">(</span><span class="n">map_one</span> <span class="o">:</span> <span class="n">f</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Apr 29 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125856305):
<p>(sorry, I was half rings and half commutative rings)</p>

#### [ Kevin Buzzard (Apr 29 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125856306):
<p>(I am all rings now)</p>

#### [ Kenny Lau (Apr 29 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125856635):
<p>I don't think it has a name</p>

#### [ Kenny Lau (Apr 29 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125858145):
<p><a href="https://github.com/kckennylau/Lean/blob/master/church_blog_questions.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/church_blog_questions.lean">https://github.com/kckennylau/Lean/blob/master/church_blog_questions.lean</a></p>

#### [ Kenny Lau (Apr 29 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125858173):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I don't think Ack can be done</p>

#### [ Kevin Buzzard (Apr 29 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125858640):
<p>What is your opinion of the other <code>sorry</code>s?</p>

#### [ Kenny Lau (Apr 29 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125858642):
<p>can't be done</p>

#### [ Kevin Buzzard (Apr 29 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125858654):
<p>Are there any for which you feel that you can convince me rigorously that they can't be done?</p>

#### [ Kenny Lau (Apr 29 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125858655):
<p>the last one, I think</p>

#### [ Kevin Buzzard (Apr 29 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125858697):
<p><code>theorem is_it_true (X : Type) (f : X → X) (x : X) : f x = x := sorry</code></p>

#### [ Kevin Buzzard (Apr 29 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125858700):
<p>that theorem looks really appealing to me</p>

#### [ Kenny Lau (Apr 29 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125858703):
<p>I think you want <code>f : \Pi X : Type, X \to X</code></p>

#### [ Kevin Buzzard (Apr 29 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125859158):
<div class="codehilite"><pre><span></span><span class="c1">-- bad church numeral</span>
<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span>
<span class="n">noncomputable</span> <span class="kn">definition</span> <span class="n">satan</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span> <span class="n">dite</span> <span class="o">(</span><span class="n">X</span> <span class="bp">=</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">H</span><span class="o">,</span><span class="k">begin</span> <span class="k">show</span> <span class="n">X</span><span class="o">,</span><span class="n">rw</span> <span class="n">H</span><span class="o">,</span><span class="n">rw</span> <span class="n">H</span> <span class="n">at</span> <span class="n">x</span><span class="o">,</span><span class="n">exact</span> <span class="n">x</span> <span class="kn">end</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span>
<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span><span class="n">satan</span> <span class="o">:</span> <span class="n">chℕ</span><span class="o">)</span> <span class="c1">-- 1 everywhere apart from nat, where it&#39;s zero</span>

<span class="kn">theorem</span> <span class="n">satan_is_bad</span> <span class="o">:</span> <span class="n">of_nat</span> <span class="o">(</span><span class="n">to_nat</span> <span class="n">satan</span><span class="o">)</span> <span class="bp">=</span> <span class="n">satan</span> <span class="bp">→</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
<span class="k">have</span> <span class="n">H2</span> <span class="o">:</span> <span class="o">(</span><span class="n">of_nat</span> <span class="o">(</span><span class="n">to_nat</span> <span class="n">satan</span><span class="o">))</span> <span class="n">bool</span> <span class="n">bnot</span> <span class="n">tt</span> <span class="bp">=</span> <span class="n">satan</span> <span class="n">bool</span> <span class="n">bnot</span> <span class="n">tt</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">H</span><span class="o">,</span>
<span class="c1">-- now what?</span>
<span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 29 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125859159):
<p>Trying to write down a counterexample</p>

#### [ Kenny Lau (Apr 29 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125859165):
<p>aha, I used <code>==</code> and I failed</p>

#### [ Kenny Lau (Apr 29 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125859169):
<p>turns out you need <code>=</code> instead</p>

#### [ Kevin Buzzard (Apr 29 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125859170):
<p>well, it typechecks</p>

#### [ Kevin Buzzard (Apr 29 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125859171):
<p>but it's not over yet</p>

#### [ Kevin Buzzard (Apr 29 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125859172):
<p>unless you see that it's over</p>

#### [ Kenny Lau (Apr 29 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125859211):
<p>so what is your thought and why are you stuck?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860599):
<p>well presumably now I have to prove things like bool ne nat</p>

#### [ Kenny Lau (Apr 29 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860603):
<p>oh I thought you can just feed in <code>bool</code> to both sides</p>

#### [ Kenny Lau (Apr 29 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860604):
<p>and have one side give <code>ff</code> and the other side give <code>tt</code></p>

#### [ Kevin Buzzard (Apr 29 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860693):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">satan_is_bad</span> <span class="o">:</span> <span class="n">of_nat</span> <span class="o">(</span><span class="n">to_nat</span> <span class="n">satan</span><span class="o">)</span> <span class="bp">=</span> <span class="n">satan</span> <span class="bp">→</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
<span class="k">have</span> <span class="n">H2</span> <span class="o">:</span> <span class="o">(</span><span class="n">of_nat</span> <span class="o">(</span><span class="n">to_nat</span> <span class="n">satan</span><span class="o">))</span> <span class="n">bool</span> <span class="n">bnot</span> <span class="n">tt</span> <span class="bp">=</span> <span class="n">satan</span> <span class="n">bool</span> <span class="n">bnot</span> <span class="n">tt</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">H</span><span class="o">,</span>
<span class="n">unfold</span> <span class="n">to_nat</span> <span class="n">at</span> <span class="n">H2</span><span class="o">,</span>
<span class="n">unfold</span> <span class="n">satan</span> <span class="n">at</span> <span class="n">H2</span><span class="o">,</span>
<span class="n">simp</span> <span class="n">at</span> <span class="n">H2</span><span class="o">,</span>
<span class="n">change</span> <span class="n">tt</span> <span class="bp">=</span> <span class="bp">_</span> <span class="n">at</span> <span class="n">H2</span><span class="o">,</span>
<span class="c1">-- H2 : tt = dite (bool = ℕ) (λ (H : bool = ℕ), eq.mpr _ (eq.mp _ tt)) (λ (_x : ¬bool = ℕ), ff)</span>
<span class="c1">-- now what?</span>
<span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 29 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860695):
<p>if only I had a good destructor for dite</p>

#### [ Kenny Lau (Apr 29 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860700):
<p>oh, you need to prove that <code>bool</code> and <code>nat</code> are not equal lol</p>

#### [ Kevin Buzzard (Apr 29 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860701):
<p>exactly</p>

#### [ Kenny Lau (Apr 29 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860741):
<p>cardinality <span class="emoji emoji-1f923" title="rolling on the floor laughing">:rolling_on_the_floor_laughing:</span></p>

#### [ Kevin Buzzard (Apr 29 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860751):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">satan_is_bad</span> <span class="o">:</span> <span class="n">of_nat</span> <span class="o">(</span><span class="n">to_nat</span> <span class="n">satan</span><span class="o">)</span> <span class="bp">=</span> <span class="n">satan</span> <span class="bp">→</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
<span class="k">have</span> <span class="n">H2</span> <span class="o">:</span> <span class="o">(</span><span class="n">of_nat</span> <span class="o">(</span><span class="n">to_nat</span> <span class="n">satan</span><span class="o">))</span> <span class="n">bool</span> <span class="n">bnot</span> <span class="n">tt</span> <span class="bp">=</span> <span class="n">satan</span> <span class="n">bool</span> <span class="n">bnot</span> <span class="n">tt</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">H</span><span class="o">,</span>
<span class="n">unfold</span> <span class="n">to_nat</span> <span class="n">at</span> <span class="n">H2</span><span class="o">,</span>
<span class="n">unfold</span> <span class="n">satan</span> <span class="n">at</span> <span class="n">H2</span><span class="o">,</span>
<span class="n">simp</span> <span class="n">at</span> <span class="n">H2</span><span class="o">,</span>
<span class="n">change</span> <span class="n">tt</span> <span class="bp">=</span> <span class="bp">_</span> <span class="n">at</span> <span class="n">H2</span><span class="o">,</span>
<span class="n">suffices</span> <span class="o">:</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">bool</span> <span class="bp">=</span> <span class="bp">ℕ</span><span class="o">),</span>
<span class="n">simp</span> <span class="o">[</span><span class="n">this</span><span class="o">]</span> <span class="n">at</span> <span class="n">H2</span><span class="o">,</span><span class="n">assumption</span><span class="o">,</span>
<span class="c1">-- ⊢ ¬bool = ℕ</span>
<span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 29 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860752):
<p>Indeed it's the only problem left</p>

#### [ Kenny Lau (Apr 29 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860753):
<p>if they're equal then their cardinality is equal</p>

#### [ Kenny Lau (Apr 29 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860754):
<p>but bool is finite</p>

#### [ Kevin Buzzard (Apr 29 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860756):
<p>can you do it?</p>

#### [ Kenny Lau (Apr 29 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860795):
<p>heh...</p>

#### [ Kevin Buzzard (Apr 29 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860798):
<p><code>example : ¬bool = ℕ := sorry</code></p>

#### [ Kenny Lau (Apr 29 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125860850):
<p>tactic mode slows things down</p>

#### [ Reid Barton (Apr 29 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125861579):
<p>It would be a lot easier if you changed <code>bool</code> to <code>empty</code></p>

#### [ Kenny Lau (Apr 29 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125861595):
<p>hmm</p>

#### [ Kenny Lau (Apr 29 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125861598):
<p>maybe we should use <code>false</code> instead</p>

#### [ Kevin Buzzard (Apr 29 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862258):
<p>the proof crucially uses "this map X -&gt; X is not this other map"</p>

#### [ Kevin Buzzard (Apr 29 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862261):
<p>so I can't see how we can use empty or false :-/</p>

#### [ Kevin Buzzard (Apr 29 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862304):
<p>but we can use any type which is provably not \N and which provably has a map which is not the identity map</p>

#### [ Reid Barton (Apr 29 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862356):
<p>Oh I see, sorry</p>

#### [ Kenny Lau (Apr 29 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862365):
<p>I have never proved that two types are not the same</p>

#### [ Kevin Buzzard (Apr 29 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862409):
<p>I think there is some notion of finite and infinite, and it will be known that bool is finite and nat is infinite</p>

#### [ Kevin Buzzard (Apr 29 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862410):
<p>of course a = b implies a equiv b</p>

#### [ Kevin Buzzard (Apr 29 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862415):
<p>by rw</p>

#### [ Kenny Lau (Apr 29 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862416):
<blockquote>
<p>by rw</p>
</blockquote>
<p><strong>by <code>eq.rec_on</code></strong></p>

#### [ Kevin Buzzard (Apr 29 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862427):
<p>that's what I said</p>

#### [ Kenny Lau (Apr 29 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862429):
<p>:P</p>

#### [ Kevin Buzzard (Apr 29 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862430):
<p>:-)</p>

#### [ Reid Barton (Apr 29 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125862640):
<p>As a further step, you could try adding the "free theorem" for the type <code>Π X : Type, (X → X) → X → X</code> as a field of your church numerals and then see if you can prove <code>of_nat (to_nat c) = c</code></p>

#### [ Chris Hughes (Apr 29 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863436):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">finite</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">bool</span> <span class="bp">≠</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span>
<span class="k">by</span> <span class="n">haveI</span> <span class="o">:</span> <span class="n">fintype</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">h</span> <span class="o">(</span><span class="k">by</span> <span class="n">apply_instance</span><span class="o">)</span><span class="bp">;</span>
<span class="n">exact</span> <span class="n">set</span><span class="bp">.</span><span class="n">not_injective_nat_fintype</span> <span class="bp">@</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ_inj</span>
</pre></div>

#### [ Kenny Lau (Apr 29 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863443):
<p>lol</p>

#### [ Chris Hughes (Apr 29 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863503):
<p>Not very often you get to use <code>eq.rec_on</code> for something that's not a prop.</p>

#### [ Kenny Lau (Apr 29 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863505):
<p>it is a prop</p>

#### [ Chris Hughes (Apr 29 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863554):
<p><code>fintype</code> isn't</p>

#### [ Kenny Lau (Apr 29 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863556):
<p>oh, I misunderstood</p>

#### [ Kenny Lau (Apr 29 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863558):
<p>your proof makes me laugh for some reason</p>

#### [ Kevin Buzzard (Apr 29 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863615):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">satan_is_bad</span> <span class="o">:</span> <span class="n">of_nat</span> <span class="o">(</span><span class="n">to_nat</span> <span class="n">satan</span><span class="o">)</span> <span class="bp">=</span> <span class="n">satan</span> <span class="bp">→</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
<span class="k">have</span> <span class="n">H2</span> <span class="o">:</span> <span class="o">(</span><span class="n">of_nat</span> <span class="o">(</span><span class="n">to_nat</span> <span class="n">satan</span><span class="o">))</span> <span class="n">bool</span> <span class="n">bnot</span> <span class="n">tt</span> <span class="bp">=</span> <span class="n">satan</span> <span class="n">bool</span> <span class="n">bnot</span> <span class="n">tt</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">H</span><span class="o">,</span>
<span class="n">unfold</span> <span class="n">to_nat</span> <span class="n">at</span> <span class="n">H2</span><span class="o">,</span>
<span class="n">unfold</span> <span class="n">satan</span> <span class="n">at</span> <span class="n">H2</span><span class="o">,</span>
<span class="n">simp</span> <span class="n">at</span> <span class="n">H2</span><span class="o">,</span>
<span class="n">change</span> <span class="n">tt</span> <span class="bp">=</span> <span class="bp">_</span> <span class="n">at</span> <span class="n">H2</span><span class="o">,</span>
<span class="n">suffices</span> <span class="o">:</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">bool</span> <span class="bp">=</span> <span class="bp">ℕ</span><span class="o">),</span>
<span class="n">simp</span> <span class="o">[</span><span class="n">this</span><span class="o">]</span> <span class="n">at</span> <span class="n">H2</span><span class="o">,</span><span class="n">assumption</span><span class="o">,</span>
<span class="n">exact</span> <span class="n">bool_not_nat</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 29 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863618):
<p>so it really is not provable</p>

#### [ Kenny Lau (Apr 29 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863622):
<p>nice!</p>

#### [ Chris Hughes (Apr 29 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863668):
<p>What's satan?</p>

#### [ Kenny Lau (Apr 29 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863675):
<div class="codehilite"><pre><span></span><span class="n">noncomputable</span> <span class="kn">definition</span> <span class="n">satan</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span> <span class="n">dite</span> <span class="o">(</span><span class="n">X</span> <span class="bp">=</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">H</span><span class="o">,</span><span class="k">begin</span> <span class="k">show</span> <span class="n">X</span><span class="o">,</span><span class="n">rw</span> <span class="n">H</span><span class="o">,</span><span class="n">rw</span> <span class="n">H</span> <span class="n">at</span> <span class="n">x</span><span class="o">,</span><span class="n">exact</span> <span class="n">x</span> <span class="kn">end</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span>
</pre></div>

#### [ Chris Hughes (Apr 29 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863766):
<p>What's <code>of_nat</code>?</p>

#### [ Kenny Lau (Apr 29 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863768):
<p><a href="https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/church_blog_questions.lean" target="_blank" title="https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/church_blog_questions.lean">https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/church_blog_questions.lean</a></p>

#### [ Chris Hughes (Apr 29 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863920):
<p>What's the purpose of church nats?</p>

#### [ Kenny Lau (Apr 29 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863925):
<p>to defeat satan</p>

#### [ Kenny Lau (Apr 29 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125863926):
<p>well church numerals is an essential part of lambda calculus</p>

#### [ Chris Hughes (Apr 29 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125864023):
<p>Am i doing something wrong</p>
<div class="codehilite"><pre><span></span><span class="c1">--KB can&#39;t do this one. Is it unprovable? If so, move definition of to_nat much further down.</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">chℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">to_nat</span> <span class="o">(</span><span class="n">succ</span> <span class="n">m</span><span class="o">)</span> <span class="bp">=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="o">(</span><span class="n">to_nat</span> <span class="n">m</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Kenny Lau (Apr 29 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125864024):
<p>I also used <code>rfl</code> lol</p>

#### [ Chris Hughes (Apr 29 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125864232):
<p>Is this cheating?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">add</span> <span class="o">:</span> <span class="n">chℕ</span> <span class="bp">→</span> <span class="n">chℕ</span> <span class="bp">→</span> <span class="n">chℕ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">of_nat</span> <span class="o">(</span><span class="n">to_nat</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">to_nat</span> <span class="n">b</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Apr 29 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125864240):
<p>yes it is</p>

#### [ Chris Hughes (Apr 29 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125864756):
<p>Stuck on add_succ</p>

#### [ Kenny Lau (Apr 29 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125864757):
<p>you can do it</p>

#### [ Chris Hughes (Apr 29 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125864775):
<p>Is it even true? There are loads of chnats that aren't constructed from naturals.</p>

#### [ Kenny Lau (Apr 29 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125864776):
<p>it is true</p>

#### [ Chris Hughes (Apr 29 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125864913):
<p>Are you sure <code>add_succ</code> is true? <code>succ_add</code> certainly is. I think it's the wrong approach to try to prove that.</p>

#### [ Kenny Lau (Apr 29 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125864952):
<p>depends on your definition of add</p>

#### [ Chris Hughes (Apr 29 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865010):
<p><code> λ a b X f, (a X f) ∘ (b X f)</code></p>

#### [ Kenny Lau (Apr 29 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865013):
<p>then destruct <code>a</code></p>

#### [ Chris Hughes (Apr 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865054):
<p>I proved of_nat_add without it, so I'm okay.</p>

#### [ Chris Hughes (Apr 29 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865060):
<p>I ended up with this</p>
<div class="codehilite"><pre><span></span>m n : chℕ,
X : Type,
f : X → X,
x : X
⊢ m X f (f (n X f x)) = f (m X f (n X f x))
</pre></div>

#### [ Kenny Lau (Apr 29 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865063):
<p>what is the theorem?</p>

#### [ Chris Hughes (Apr 29 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865243):
<p>m + succ n = succ (m + n)</p>

#### [ Kenny Lau (Apr 29 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865246):
<p>oh...</p>

#### [ Kenny Lau (Apr 29 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865249):
<p>sorry</p>

#### [ Kenny Lau (Apr 29 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865253):
<p>I thought it was one of the questions from the file and then I reflexively answered that it's true</p>

#### [ Kevin Buzzard (Apr 29 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865379):
<p>Apparently defining pred is interesting</p>

#### [ Chris Hughes (Apr 29 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865486):
<p>pretty sure <code>add_comm</code> isn't true. all you need is two functions whose composition doesn't commute surely?</p>

#### [ Chris Hughes (Apr 29 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865785):
<p>Just disproved <code>add_comm</code></p>

#### [ Kenny Lau (Apr 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865788):
<p>nice!</p>

#### [ Kevin Buzzard (Apr 29 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865903):
<p>the problem is that a church numeral has to be defined on every type</p>

#### [ Kevin Buzzard (Apr 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865910):
<p>If you were to specialise to one specific type X then they won't commute</p>

#### [ Kenny Lau (Apr 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865915):
<p>the problem is that noncomputable functions exist</p>

#### [ Kevin Buzzard (Apr 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865916):
<p>right</p>

#### [ Kenny Lau (Apr 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865922):
<p>now I haven't even started dinner and you have already finished it</p>

#### [ Kevin Buzzard (Apr 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865924):
<p>also right</p>

#### [ Kevin Buzzard (Apr 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865927):
<p>but I have a lot of tidying up to do</p>

#### [ Kenny Lau (Apr 29 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125865967):
<p>heh</p>

#### [ Chris Hughes (Apr 29 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125866020):
<blockquote>
<p>the problem is that a church numeral has to be defined on every type<br>
If you were to specialise to one specific type X then they won't commute</p>
</blockquote>
<p>What do you mean?</p>

#### [ Chris Hughes (Apr 29 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125866185):
<p>I fixed has_pow <code>instance : has_pow chℕ chℕ := ⟨pow⟩</code></p>

#### [ Kevin Buzzard (Apr 29 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125866347):
<p>I mean that you can't say "I can think of a type X and two functions f and g which don't commute, so done", because a church numeral is defined on all types</p>

#### [ Kevin Buzzard (Apr 29 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125866350):
<p>But of course if you do the trick I did then this gets round it, at a cost of making the function noncomputable</p>

#### [ Chris Hughes (Apr 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125866405):
<p>You can.</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">not_add_comm</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">chℕ</span><span class="o">,</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">≠</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">a</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">dite</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">=</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">eq</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">h</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">h</span><span class="bp">.</span><span class="n">symm</span> <span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)))</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">x</span><span class="o">),</span>
<span class="bp">λ</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">dite</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">=</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">eq</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">h</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">h</span><span class="bp">.</span><span class="n">symm</span> <span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)))</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">x</span><span class="o">),</span>
<span class="bp">λ</span> <span class="n">h</span><span class="o">,</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="o">:=</span> <span class="n">congr_fun</span> <span class="n">h</span> <span class="bp">ℕ</span><span class="o">,</span>
  <span class="k">have</span> <span class="o">:=</span> <span class="n">congr_fun</span> <span class="n">this</span> <span class="n">id</span><span class="o">,</span>
  <span class="k">have</span> <span class="o">:=</span> <span class="n">congr_fun</span> <span class="n">this</span> <span class="mi">0</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">has_add</span><span class="bp">.</span><span class="n">add</span><span class="o">,</span> <span class="n">add</span><span class="o">]</span> <span class="n">at</span> <span class="n">this</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">absurd</span> <span class="n">this</span> <span class="n">dec_trivial</span><span class="o">,</span>
<span class="kn">end</span><span class="bp">⟩</span>
</pre></div>


<p>Are you saying that the definition is not correct?</p>

#### [ Chris Hughes (Apr 29 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125866797):
<p>Or maybe my definition of add is incorrect.</p>

#### [ Chris Hughes (Apr 29 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867627):
<p>I disproved <code>free_chnat</code> as well</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">free_chnat</span> <span class="o">:</span> <span class="bp">¬∀</span> <span class="o">(</span><span class="n">A</span> <span class="n">B</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">),</span> <span class="bp">∀</span> <span class="n">f</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">,</span>
<span class="bp">∀</span> <span class="n">r</span> <span class="o">:</span> <span class="n">chℕ</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">A</span><span class="o">,</span> <span class="n">r</span> <span class="o">(</span><span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">g</span><span class="o">,</span> <span class="n">f</span><span class="o">)</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">r</span> <span class="o">(</span><span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">g</span><span class="o">,</span> <span class="n">g</span><span class="o">)</span> <span class="n">f</span> <span class="n">a</span>
 <span class="o">:=</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="k">begin</span>
 <span class="k">let</span> <span class="n">r</span> <span class="o">:</span> <span class="n">chℕ</span> <span class="o">:=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">dite</span> <span class="o">((</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">eq</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">h</span>
    <span class="o">(</span><span class="k">let</span> <span class="n">f</span> <span class="o">:</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">h</span><span class="bp">.</span><span class="n">symm</span> <span class="n">f</span> <span class="k">in</span>
    <span class="n">ite</span> <span class="o">(</span><span class="n">f</span> <span class="bp">=</span> <span class="n">id</span><span class="o">)</span> <span class="n">id</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span><span class="o">))</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">x</span><span class="o">)),</span>
  <span class="k">have</span> <span class="o">:=</span> <span class="o">(</span><span class="n">h</span> <span class="bp">ℕ</span> <span class="bp">ℕ</span> <span class="n">id</span> <span class="n">r</span> <span class="mi">8</span><span class="o">),</span>
  <span class="k">have</span> <span class="n">h₁</span> <span class="o">:</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">id</span><span class="o">)</span> <span class="bp">≠</span> <span class="n">id</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">absurd</span> <span class="o">(</span><span class="n">congr_fun</span> <span class="o">(</span><span class="n">congr_fun</span> <span class="n">h</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span><span class="o">)</span> <span class="mi">0</span><span class="o">)</span> <span class="n">dec_trivial</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">h₂</span> <span class="o">:</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">g</span><span class="o">)</span> <span class="bp">=</span> <span class="n">id</span> <span class="o">:=</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">r</span><span class="o">,</span> <span class="n">id</span><span class="o">,</span> <span class="n">h₁</span><span class="o">,</span> <span class="n">h₂</span><span class="o">]</span> <span class="n">at</span> <span class="n">this</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">absurd</span> <span class="n">this</span> <span class="n">dec_trivial</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 29 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867731):
<p>yes, those free theorems aren't very good are they</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867733):
<p>I would ask for my money back</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867740):
<p>The free theorem for <code>Pi X, X</code> is: for all X, for all f : X -&gt; X, for all x : X, f x = x :-)</p>

#### [ Chris Hughes (Apr 29 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867742):
<p>Is it because we're defining church numerals as something bigger than those that can be constructed from nats?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867746):
<p>I think constructively it's very difficult to tell the difference between church numerals and numerals</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867785):
<p>you have to use this dite trick and make it noncomputable</p>

#### [ Chris Hughes (Apr 29 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867790):
<p>Probably. But that doesn't make the lemmas true. It just makes them undisprovable</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867798):
<p>I think that in some other logics they might be provable</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867799):
<p>I am certainly not an expert in these variants of the lambda calculus</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867837):
<p>Chris I have been failing to apply your lemma :-)</p>

#### [ Chris Hughes (Apr 29 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867845):
<p>The 00EJ?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867846):
<p>yes</p>

#### [ Chris Hughes (Apr 29 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867849):
<p>Because of the isomorphism problem?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867856):
<p>I have some situation with a bunch of types each of which are canonically isomorphic to your types that you proved something about</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867858):
<p>but I have got distracted</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867867):
<p>and am trying to write quite a high-level proof which mirrors how I actually think about the question</p>

#### [ Chris Hughes (Apr 29 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867920):
<p>Did the tactics session get anywhere?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867966):
<p>There was a preliminary idea about how to model the notion of being canonically isomorphic</p>

#### [ Chris Hughes (Apr 29 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867967):
<p>To make tactics that prove it's a ring?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867968):
<p>but then we realised that it wasn't strong enough</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867980):
<p>and I am now trying to write down some abstract ideas at a high level to see if I can make any sense out of them</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867989):
<p>It seems to me that when a mathematician says that two things are canonically isomorphic they are making a promise</p>

#### [ Chris Hughes (Apr 29 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867990):
<p>I don't understand how it could have been someone's PhD project to prove a result still held for an isomorphic thing</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125867993):
<p>the project did something else</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868035):
<p>but this came out in the wash</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868040):
<p>But the problem was hard</p>

#### [ Chris Hughes (Apr 29 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868041):
<p>I see.</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868042):
<p>Here was the problem.</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868045):
<p>We have two finite-dimensional vector spaces V and W</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868048):
<p>and we have two linear maps T : V -&gt; V and T' : W -&gt; W</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868053):
<p>and T and T' are both defined "by using the same sort of ideas"</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868059):
<p>but on two different spaces</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868069):
<p>and then there's a theorem that there's a "canonical isomorphism" phi from V to W</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868070):
<p>which means "an isomorphism which somehow dropped out really nicely"</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868112):
<p>and what Dick Gross used without proof was that phi (T v) = T' (phi v)</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868117):
<p>for all v</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868120):
<p>and his proof was not a formal one</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868122):
<p>his proof was "this must be true because that's surely how it works"</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868124):
<p>"because everything is canonical"</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868133):
<p>V and W were two different cohomology theories attached to the same space</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868143):
<p>and T and T' were defined using some other spaces (the same other spaces for T and T')</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868187):
<p>e.g. maps between spaces often induce maps between cohomology theories</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868188):
<p>but it was just a case of making sure that all the diagrams commuted</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868195):
<p>and some of the definition were done using very abstract algebra and the diagrams were difficult to chase</p>

#### [ Simon Hudon (Apr 29 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868198):
<p>Short digression:</p>
<p>I'm working on deriving <code>transportable</code>. Do you guys have a preference between making such instances lemmas (i.e. you can't unfold them) or definitions?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868201):
<p>that's an interesting question Simon</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868243):
<p>transportable is what we can transfer equiv over, right?</p>

#### [ Simon Hudon (Apr 29 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868246):
<p>Exactly</p>

#### [ Simon Hudon (Apr 29 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868250):
<p>Here's the class:</p>
<div class="codehilite"><pre><span></span>class transportable (f : Type u → Type v) :=
(on_equiv : Π {α β : Type u} (e : equiv α β), equiv (f α) (f β))
(on_refl  : Π (α : Type u), on_equiv (equiv.refl α) = equiv.refl (f α))
(on_trans : Π {α β γ : Type u} (d : equiv α β) (e : equiv β γ), on_equiv (equiv.trans d e) = equiv.trans (on_equiv d) (on_equiv e))
</pre></div>

#### [ Kevin Buzzard (Apr 29 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868260):
<p>I guess if I had a group on X and an equiv from X to Y I'd definitely like to be able to get at the induced group on Y</p>

#### [ Simon Hudon (Apr 29 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868302):
<p>Ah very good. Right now, the instances I'm generating are kind of messy. I'll try to structure them so that you can look into them then</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868306):
<p>but that might be a different question</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868317):
<p>I am not sure I can give a definitive answer to your question</p>

#### [ Simon Hudon (Apr 29 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868319):
<p>If I don't structure them but I make them definitions, you still benefit from defeq</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868375):
<p>My impression was that for theoretical reasons some people wanted things more general than maps between types to be transportable</p>

#### [ Simon Hudon (Apr 29 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868378):
<p>You mean like groups, rings, etc?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868427):
<p>I think the issue raised was that if X and Y were equiv and then X got a group structure, then Y would get a group structure, but if then X got a ring structure on top of that, which induced the group structure, then one would want to push over both the ring structure on Y and the proof that the ring structure on Y reduced to the group structure</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868428):
<p>But I am not too worried about this at the minute. We might just want to try a prototype at the minute</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868429):
<p>to see if we can get anything working</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868438):
<p>I have thought about this a certain amount today. If X and Y have extra structure, e.g. if they're both rings, then there is ring_equiv, which equiv + assumption that the maps are ring isomorphisms</p>

#### [ Simon Hudon (Apr 29 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868440):
<p>Cool. I'm going to push it on a repo on Github before making a PR for mathlib. This way you can play with it and tell me what you need</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868481):
<p>And if two things are ring-equiv then you can get some more theorems</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868482):
<p>e.g. if something is a module for one ring then it becomes a module for the other ring</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868485):
<p>That would not be true if the rings were just equiv</p>

#### [ Simon Hudon (Apr 29 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868492):
<p>That's going to be interesting. I'll have to think on how to do that</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868493):
<p>So some wise people made some comments about this earlier</p>

#### [ Simon Hudon (Apr 29 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868496):
<blockquote>
<p>That would not be true if the rings were just equiv</p>
</blockquote>
<p>Does that mean ring-equiv also asserts that the ring operations respect the underlying isomorphism?</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868536):
<p>right</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868539):
<p>If X is a ring</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868540):
<p>then this means in practice that you have add and mul and neg and one and zero</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868541):
<p>and all of those transfer</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868542):
<p>so if you have an equiv X = Y</p>

#### [ Simon Hudon (Apr 29 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868543):
<p>Right and you need access to their definitions</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868549):
<p>then you can transfer them all over from X to Y</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868552):
<p>On the other hand if X and Y are already rings</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868553):
<p>and you decide that there's a canonical isomorphism between them</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868555):
<p>then you're going to have to prove that the add mul neg etc all transfer over from one to the other</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868556):
<p>and once you've done that, you have a better class of equiv which is specifically for rings</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868596):
<p>and you can prove more theorems with it</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868604):
<p>each of which is trivial to a mathematician</p>

#### [ Kevin Buzzard (Apr 29 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868610):
<p>such as "oh look, M is a free R-module and R is isomorphic to S so M is now a free S-module"</p>

#### [ Kevin Buzzard (Apr 30 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868661):
<p>or "M is a Noetherian Cohen-Macauley R-module which is R-generated by these three elements and R is isomorphic to S so now M is a Noetherian Cohen-Macauley S-module which is S-generated by these three elements"</p>

#### [ Kevin Buzzard (Apr 30 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868662):
<p>and the definition of Cohen-Macauley is pretty complicated</p>

#### [ Kevin Buzzard (Apr 30 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868663):
<p>but it complies with the unwritten promise</p>

#### [ Kevin Buzzard (Apr 30 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868667):
<p>which is that it only depends on the underlying ring up to ring-isomorphism</p>

#### [ Kevin Buzzard (Apr 30 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868678):
<p>It seems to me that mathematicians have got a really good intuitive feeling for these promises</p>

#### [ Simon Hudon (Apr 30 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868728):
<p>Nice</p>

#### [ Simon Hudon (Apr 30 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868774):
<p>Given a structure like group or ring, if you derive <code>transportable</code> it gives automatically the isomorphism between the properties of the structures whenever you have an isomorphism between two types</p>

#### [ Simon Hudon (Apr 30 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125868815):
<p>I'm getting close to a complete derivation and it works with group so far. It will be fun to see you try it with other structures</p>

#### [ Mario Carneiro (Apr 30 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125874746):
<blockquote>
<p>The free theorem for <code>Pi X, X</code> is: for all X, for all f : X -&gt; X, for all x : X, f x = x :-)</p>
</blockquote>
<p>That's not correct. You need to quantify over polymorphic functions: for all f : (\forall X, X -&gt; X), for all X, for all x : X, f X x = x</p>

#### [ Mario Carneiro (Apr 30 2018 at 04:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125874930):
<p>As Kenny and others have noted, the definition of chN is not correct in dependent type theories like lean because there are additional polymorphic functions that are not parametric. However, you can repair the church nat construction by taking a subtype to enforce that the polymorphic functions are functorial. For example, church unit is:</p>
<div class="codehilite"><pre><span></span>def ch_unit := { f : ∀ X : Type, X → X // ∀ (X Y) (g : X → Y) x, f Y (g x) = g (f X x) }
</pre></div>


<p>Can you see the correct condition for church nat?</p>

#### [ Mario Carneiro (Apr 30 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125874995):
<p>By the way, to generate the type of a church encoding, the idea is just look at the recursor for the inductive type. For example, ignoring dependencies in the motive, the type of nat.rec is <code>∀ C, C → (C → C) → ℕ → C</code>, so if you move the <code>ℕ → </code>to the beginning this is exactly the canonical map from N to chN (and the remainder <code>∀ C, C → (C → C) → C</code> is chN itself). (The ordering of the two arguments is not important, and only reflects that <code>zero</code> is the first constructor and <code>succ</code> is the second.)</p>

#### [ Reid Barton (Apr 30 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125875260):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>, did you see <a href="https://gist.github.com/rwbarton/08924014ebc7b1cf68ec624989249aff" target="_blank" title="https://gist.github.com/rwbarton/08924014ebc7b1cf68ec624989249aff">https://gist.github.com/rwbarton/08924014ebc7b1cf68ec624989249aff</a>?</p>

#### [ Reid Barton (Apr 30 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125875554):
<p>I'm thinking now that having a <code>class</code> is problematic because the type of the transport function depends on the parameters of the structure in a way that I don't think can be encoded in a <code>class</code> declaration. Plus I don't see any real advantage to having the class anyways. Rather we could just generate definitions <code>group.transport</code>, <code>ring.transport</code> etc.</p>

#### [ Simon Hudon (Apr 30 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125875922):
<p>I don't think I see your point</p>

#### [ Reid Barton (Apr 30 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125875971):
<p>My two messages above are unrelated to each other</p>

#### [ Reid Barton (Apr 30 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125875978):
<p>so I'm not sure what the point that you don't see is <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Reid Barton (Apr 30 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876020):
<p>The gist is supposed to be an example of what we want to have autogenerated: everything defined by <code>magic</code></p>

#### [ Reid Barton (Apr 30 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876032):
<p>But making <code>group.transportable</code> be an instance of a class is unnecessary and in general awkward (my gist already contains three classes, and if there are dependencies between the parameters of a structure then things get even more complicated)</p>

#### [ Simon Hudon (Apr 30 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876229):
<p>Does your gist illustrate the awkwardness that you're referring to?</p>

#### [ Reid Barton (Apr 30 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876246):
<p>To the extent that I already had to define three separate classes <code>transportable</code>, <code>transportable2</code>, <code>transportable3</code></p>

#### [ Reid Barton (Apr 30 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876252):
<p>It doesn't illustrate what happens when there are dependencies between arguments</p>

#### [ Simon Hudon (Apr 30 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876298):
<p>But if you don't make them classes you still need to define records, no?</p>

#### [ Reid Barton (Apr 30 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876311):
<p>Well the instance called <code>group.transportable</code> is only really used as <code>transport group</code>, so <code>transport group</code> can just be named <code>group.transport</code> and no need for a structure.</p>

#### [ Reid Barton (Apr 30 2018 at 04:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876352):
<p>If we need the <code>on_refl</code> and <code>on_trans</code> fields then they can be called <code>group.transport_on_refl</code> or something</p>

#### [ Reid Barton (Apr 30 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876409):
<p>By analogy, there's no class that contains all the <code>.rec</code> functions which are defined for inductive types</p>

#### [ Simon Hudon (Apr 30 2018 at 05:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876510):
<p>I see that you're arguing against the necessity. I don't see any issue with using a class nonetheless. And the upside of having one is that it allows you to generalize lemmas or definitions. It might be that, as you seem to suggest, there's no ground breaking theorems about those classes. It can still allow you to reduce the boilerplate code</p>

#### [ Reid Barton (Apr 30 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876762):
<p>Well at a minimum, you'd need one class per number of type arguments, unless there is a clever way to express <code>transportable2</code> in terms of <code>transportable</code> twice.</p>

#### [ Reid Barton (Apr 30 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125876766):
<p>I'm not entirely sure what should happen when there are dependencies between arguments. <a href="https://gist.github.com/rwbarton/d847ef6d1783f0d0859eb80de8327bad" target="_blank" title="https://gist.github.com/rwbarton/d847ef6d1783f0d0859eb80de8327bad">https://gist.github.com/rwbarton/d847ef6d1783f0d0859eb80de8327bad</a> shows one possibility. Here <code>t1_space</code> has two arguments, a type <code>α</code> and a topology on <code>α</code>. Since the second argument is not a type, there is no equivalence in that position.</p>

#### [ Simon Hudon (Apr 30 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125877059):
<p>Having three separate classes does not seem like much of a problem to me. But you can probably equate <code>transportable2 f</code> to <code>transportable (uncurry f)</code>, that way, you can use some of the same definitions for both. And for dependent arguments, if it's more trouble than it's worth, you may have a more ad hoc approach (without classes) for those cases.</p>

#### [ Mario Carneiro (Apr 30 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125880638):
<p>The range of possible <code>transportable</code> classes is unbounded, not just because of things like <code>transportable2</code> for other values of 2 but also because of higher order functors like <code>(Type -&gt; Type) -&gt; Type</code>, and Pi types like <code>\forall A, group A -&gt; Type</code>. If a tactic generated the transportable theorem for a functor, it would need to select the theorem statement from an unbounded class of statements, namely the "free theorems"</p>

#### [ Mario Carneiro (Apr 30 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125880688):
<p>You can express <code>transportable2</code> in a more modular way, by generalizing <code>equiv</code>. Define an <code>~=</code> relation on (many) types by induction as follows: If <code>x y : Type</code> then <code>x ~= y</code> means <code>equiv x y</code> (i.e. the usual sense), and if <code>f g : A -&gt; B</code> then <code>f ~= g</code> iff <code>\forall x y, x ~= y -&gt; f x ~= g y</code>. Then <code>transportable x</code> means <code>x ~= x</code>. This generalizes <code>transportable2</code> and <code>transportable3</code>, and also yields transportable for <code>F : (Type -&gt; Type) -&gt; Type</code>, asserting that if <code>f ~= g</code> at <code>Type -&gt; Type</code> then <code>F f ~= F g</code>.</p>

#### [ Kevin Buzzard (Apr 30 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125881912):
<blockquote>
<p>As Kenny and others have noted, the definition of chN is not correct in dependent type theories like lean because there are additional polymorphic functions that are not parametric. However, you can repair the church nat construction by taking a subtype to enforce that the polymorphic functions are functorial.</p>
</blockquote>
<p>You have put the "free theorem" in with the definition! It really is free now :-)</p>

#### [ Kevin Buzzard (Apr 30 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125881965):
<p>If you demand that a church numeral is functorial, then the naturals are a universal object because they are freely generated by <code>x : X</code> (zero) and <code>f : X -&gt; X</code> (succ), so any church numeral will be determined by its behaviour on the universal object, with proof by a trivial diagram chase.</p>

#### [ Kevin Buzzard (Apr 30 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125881967):
<p>And so a church numeral is uniquely determined by what it does on nat, which is precisely the missing theorem for proving the equiv between church nat and nat</p>

#### [ Kevin Buzzard (Apr 30 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125882007):
<p>A follow-up to the paper should be "Dependent type theory : extra conditions for free"</p>

#### [ Kevin Buzzard (Apr 30 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125882009):
<p>doesn't sound as marketable</p>

#### [ Kevin Buzzard (Apr 30 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125882053):
<p>Initially I had thought that church numerals were just some stupid trick for encoding nat. I hadn't until now realised that they were a literal translation of the inductive definition of nat into another language.</p>

#### [ Kevin Buzzard (Apr 30 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125882071):
<p>But I hadn't got the translation quite right -- I was using the definition I found in Software Foundations. Maybe they are the translation into some other flavour of theory e.g. some lambda calculus thing</p>

#### [ Kevin Buzzard (Apr 30 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125882116):
<p>So satan was bad after all -- he shouldn't really be allowed to be a church nat because he's not functorial enough.</p>

#### [ Kevin Buzzard (May 01 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125958209):
<p>Some more church nat puzzles</p>

#### [ Kevin Buzzard (May 01 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125958215):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">chℕ</span> <span class="o">:=</span> <span class="bp">Π</span> <span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span> <span class="o">(</span><span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="bp">→</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span>

<span class="kn">namespace</span> <span class="n">chnat</span>

<span class="kn">open</span> <span class="n">nat</span>

<span class="kn">definition</span> <span class="n">to_nat</span> <span class="o">:</span> <span class="n">chℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="n">m</span> <span class="bp">ℕ</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="mi">0</span>

<span class="n">def</span> <span class="n">of_nat</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">chℕ</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">zero</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">of_nat</span> <span class="n">n</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="c1">-- f (f^n x)</span>

<span class="kn">definition</span> <span class="n">of_nat&#39;</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">chℕ</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">of_nat&#39;</span> <span class="n">n</span> <span class="n">X</span> <span class="n">f</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="c1">-- f^n (f x)</span>

<span class="kn">theorem</span> <span class="n">nat_of_chnat_of_nat</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">to_nat</span> <span class="o">(</span><span class="n">of_nat</span> <span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">theorem</span> <span class="n">nat_of_chnat_of_nat&#39;</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">to_nat</span> <span class="o">(</span><span class="n">of_nat&#39;</span> <span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">theorem</span> <span class="n">of_nat&#39;_is_of_nat</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">of_nat</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">of_nat&#39;</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">end</span> <span class="n">chnat</span>
</pre></div>

#### [ Kevin Buzzard (May 01 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/125958222):
<p>I haven't proved all of them, I expected them all to be true.</p>

#### [ Kevin Buzzard (May 10 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359013):
<p>The typeclass <code>is_group_hom</code> (in <code>algebra/group.lean</code> in mathlib) transports across a lot of structure</p>

#### [ Kevin Buzzard (May 10 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359063):
<p>For example, <code>equiv.Pi_congr_right</code> says that if (F i) and (G i) biject for all i, then Pi i, F i bijects with Pi i, G i</p>

#### [ Kevin Buzzard (May 10 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359070):
<p>but if the bijections are all group homs then the product bijection is also a group hom</p>

#### [ Kevin Buzzard (May 10 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359073):
<p>and the proof is idea-free</p>

#### [ Kevin Buzzard (May 10 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359117):
<p>so instead of having to write my own instance for this (which I just did)</p>

#### [ Kevin Buzzard (May 10 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359133):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">equiv</span><span class="bp">.</span><span class="n">Pi_congr_right</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">add_group</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">add_group</span> <span class="o">(</span><span class="n">G</span> <span class="n">i</span><span class="o">)]</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span> <span class="err">≃</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">is_add_group_hom</span> <span class="o">(</span><span class="n">H</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span>
 <span class="n">is_add_group_hom</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">Pi_congr_right</span> <span class="n">H</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span>
 <span class="k">show</span> <span class="n">H</span> <span class="n">i</span> <span class="o">((</span><span class="n">a</span> <span class="n">i</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="n">i</span><span class="o">))</span> <span class="bp">=</span> <span class="n">H</span> <span class="n">i</span> <span class="o">(</span><span class="n">a</span> <span class="n">i</span><span class="o">)</span> <span class="bp">+</span> <span class="n">H</span> <span class="n">i</span> <span class="o">(</span><span class="n">b</span> <span class="n">i</span><span class="o">),</span>
</pre></div>

#### [ Kevin Buzzard (May 10 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359135):
<p>(OK so it was additive group homs, which is a slightly different typeclass)</p>

#### [ Kevin Buzzard (May 10 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359143):
<p>this should surely have been auto-generated for me when the type class inference system realised I needed it. Right?</p>

#### [ Kevin Buzzard (May 10 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359150):
<p>Similarly, given</p>

#### [ Kevin Buzzard (May 10 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359187):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">Pi_lift_map₁</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span> <span class="bp">→</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">G</span> <span class="n">i</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">Fi</span> <span class="n">i</span><span class="o">,</span> <span class="n">H</span> <span class="n">i</span> <span class="o">(</span><span class="n">Fi</span> <span class="n">i</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (May 10 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359192):
<p>I should get a free instance of "all the H i are group homs implies their product is"</p>

#### [ Kenny Lau (May 10 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359252):
<p>that's the UMP of product right</p>

#### [ Kevin Buzzard (May 10 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359306):
<p>Pi_lift_map2 is the UMP of product</p>

#### [ Mario Carneiro (May 10 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359317):
<p>This is not exactly trivial. It's conceivable it falls out of the <code>Pi_instance</code> tactic stuff, but you do have to make use of some lemmas and funext in appropriate places</p>

#### [ Kevin Buzzard (May 10 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359366):
<p>I would like to make Lean behave more like a mathematician</p>

#### [ Kevin Buzzard (May 10 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359369):
<p>and mathematicians know that the function one is easy</p>

#### [ Kevin Buzzard (May 10 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359371):
<p>and they instantly deduce the equiv one</p>

#### [ Mario Carneiro (May 10 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359372):
<p>I can see <code>simp</code> being able to do this one with some hints</p>

#### [ Mario Carneiro (May 10 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359376):
<p>the equiv one is literally the same theorem though</p>

#### [ Kevin Buzzard (May 10 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359382):
<p>There's a meta-hint for this sort of thing</p>

#### [ Mario Carneiro (May 10 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359384):
<p>that is trivial even by lean's standards</p>

#### [ Kevin Buzzard (May 10 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359385):
<p>"To prove axiom X for the product, use axiom X on the factors"</p>

#### [ Kevin Buzzard (May 10 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359388):
<p>I agree it's the same theorem, that's why it has the same proof</p>

#### [ Kevin Buzzard (May 10 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359391):
<p>but you told me to write it twice</p>

#### [ Kevin Buzzard (May 10 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359392):
<p>because you said Lean needs to be told it twice</p>

#### [ Kevin Buzzard (May 10 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359393):
<p>Right?</p>

#### [ Mario Carneiro (May 10 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359394):
<p>you should apply the theorem, not prove it twice</p>

#### [ Kevin Buzzard (May 10 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359445):
<p>heh</p>

#### [ Mario Carneiro (May 10 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359447):
<p>def X := proof, def Y := X</p>

#### [ Kevin Buzzard (May 10 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359507):
<p>ha ha</p>

#### [ Kevin Buzzard (May 10 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359509):
<p>proof <code>is_add_group_hom.Pi_lift H</code> fails</p>

#### [ Kevin Buzzard (May 10 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359510):
<p>proof <code>is_add_group_hom.Pi_lift (λ i, H i)</code> succeeds</p>

#### [ Kevin Buzzard (May 10 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359518):
<p>Lean knows it's looking for something of a certain type lam i, map</p>

#### [ Kevin Buzzard (May 10 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359519):
<p>and H i is an equiv which coerces to map</p>

#### [ Kevin Buzzard (May 10 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126359520):
<p>but it's not smart enough to do it without the i</p>

#### [ Mario Carneiro (May 10 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126360142):
<p>what about <code>is_add_group_hom.Pi_lift _</code>?</p>

#### [ Kevin Buzzard (May 10 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/126365134):
<p>nope</p>

#### [ Kevin Buzzard (Oct 08 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22canonically%22%20identifying%20two%20types/near/135390412):
<p>Ooh look, this is back in the days when I used to post one paragraph as ten one-sentence posts.</p>
<p>I finally got around to making this an issue.</p>
<p><a href="https://github.com/leanprover/mathlib/issues/408" target="_blank" title="https://github.com/leanprover/mathlib/issues/408">https://github.com/leanprover/mathlib/issues/408</a></p>


{% endraw %}
