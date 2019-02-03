---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/19425usesofchoice.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [uses of choice](https://leanprover-community.github.io/archive/113488general/19425usesofchoice.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Floris van Doorn (Oct 07 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135362955):
<p>Inspired by my post in the thread "what is wrong with HoTT" I had two questions:</p>
<p>(1) What are some uses of <code>classical.choice</code> in mathlib. I'm not interested in uses of LEM or the axiom of choice, but in the strong form of choice which is inconsistent with HoTT. Are the applications of them avoidable if some things were designed a little differently? </p>
<p>(2) Can you define something of the following type without using choice?<br>
<code>Π(A : ℕ → Type) (f : Πn, A n → A (n+1)) (n m : ℕ) : n ≤ m → A n → A m</code><br>
It is easy to do if <code>≤</code> lives in <code>Type</code>, by induction on <code>≤</code> (as an inductive family), but it is less obvious when <code>≤</code> lives in <code>Prop</code>, since then it doesn't eliminate into <code>Type</code>.</p>

#### [ Johan Commelin (Oct 07 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135363015):
<p>Re (1): Would you please recall the difference between AoC and "strong form of choice". Mere mathematicians don't exactly know the difference...</p>

#### [ Floris van Doorn (Oct 07 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135363414):
<p><code>classical.choice</code> states <code>nonempty A -&gt; A</code> (it allows you to construct "data" out of a proposition). The axiom of choice states for every surjective function there <em>exists</em> a section (which is still a proposition).</p>

#### [ Kenny Lau (Oct 07 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135363419):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">Π</span><span class="n">n</span><span class="o">,</span> <span class="n">A</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">A</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="o">(</span><span class="n">n</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">≤</span> <span class="n">m</span> <span class="bp">→</span> <span class="n">A</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">A</span> <span class="n">m</span> <span class="o">:=</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">m</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">n</span> <span class="n">H</span> <span class="n">An</span><span class="o">,</span> <span class="bp">@</span><span class="n">eq</span><span class="bp">.</span><span class="n">rec_on</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">A</span> <span class="bp">_</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">eq_zero_of_le_zero</span> <span class="n">H</span><span class="o">)</span> <span class="n">An</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span> <span class="n">ih</span> <span class="n">n</span> <span class="n">H</span> <span class="n">An</span><span class="o">,</span> <span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">≤</span> <span class="n">m</span> <span class="k">then</span> <span class="n">f</span> <span class="n">m</span> <span class="o">(</span><span class="n">ih</span> <span class="n">n</span> <span class="n">h</span> <span class="n">An</span><span class="o">)</span>
    <span class="k">else</span> <span class="n">eq</span><span class="bp">.</span><span class="n">rec_on</span> <span class="o">(</span><span class="n">le_antisymm</span> <span class="n">H</span> <span class="o">(</span><span class="n">lt_of_not_ge</span> <span class="n">h</span><span class="o">))</span> <span class="n">An</span><span class="o">)</span> <span class="n">n</span>
</pre></div>

#### [ Kenny Lau (Oct 07 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135363463):
<p><span class="user-mention" data-user-id="111080">@Floris van Doorn</span></p>

#### [ Floris van Doorn (Oct 07 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135363530):
<p>nice!</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135364864):
<p>Regarding (1), <a href="#narrow/stream/116395-maths/topic/Nuances.20regarding.20naturality" title="#narrow/stream/116395-maths/topic/Nuances.20regarding.20naturality">this recent thread</a> is distantly related (at least we talk about using <code>choice</code> in the context of defining the dimension of a vector space.)</p>

#### [ Mario Carneiro (Oct 08 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135371908):
<p><span class="user-mention" data-user-id="111080">@Floris van Doorn</span> One interesting use of <code>choice</code> is in <code>filter.lim</code>, which constructs the limit of a filter</p>

#### [ Mario Carneiro (Oct 08 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135371916):
<p>It's a unique choice only if we assume the topology is T2 (and it is a topology)</p>

#### [ Mario Carneiro (Oct 08 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135371990):
<p>There are also things like <code>quotient.out</code> (pick an element from an equivalence class), which are fully nonconstructive. You might be able to encapsulate this in a proof method for subsingletons, though</p>

#### [ Johan Commelin (Oct 08 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387211):
<p><span class="user-mention" data-user-id="111080">@Floris van Doorn</span> I think this might be a deal-breaker. I would like to explore it further.</p>

#### [ Johan Commelin (Oct 08 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387218):
<p>I don't even know what "eliminating into Prop" or "into Type" means.</p>

#### [ Johan Commelin (Oct 08 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387228):
<p>But my gut feeling says that we need to be able to <code>choose</code> data.</p>

#### [ Kevin Buzzard (Oct 08 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387461):
<blockquote>
<p>I don't even know what "eliminating into Prop" or "into Type" means.</p>
</blockquote>
<p>I think it means that if you do <code>cases</code> on <code>A or B</code> then stuff breaks if your goal is data, because <code>or</code> "only eliminates into Prop", i.e. <code>or.rec</code> is <code>protected eliminator or.rec : ∀ {a b C : Prop}, (a → C) → (b → C) → a ∨ b → C</code></p>

#### [ Mario Carneiro (Oct 08 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387465):
<p>The idea is that you can construct choicy things but at the end of the day it has to be in service of proving an exists</p>

#### [ Kevin Buzzard (Oct 08 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387467):
<p>Note that the "motive" <code>C</code> has to be a Prop.</p>

#### [ Mario Carneiro (Oct 08 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387525):
<p>incidentally, this is the way things are in metamath - with ZFC the axiom of choice ends in an exists</p>

#### [ Johan Commelin (Oct 08 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387540):
<p>So there might not be a problem after all?</p>

#### [ Johan Commelin (Oct 08 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387552):
<p>Can we do algebraic closures with HoTT's AoC?</p>

#### [ Johan Commelin (Oct 08 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387560):
<p>And Zorn, and all the other things?</p>

#### [ Mario Carneiro (Oct 08 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387566):
<p>Zorn's lemma proves <em>there exists</em> a maximal element</p>

#### [ Mario Carneiro (Oct 08 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387569):
<p>and <em>there exists</em> an algebraic closure</p>

#### [ Mario Carneiro (Oct 08 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387574):
<p>but unless you can turn these into unique exists this isn't actually a construction</p>

#### [ Johan Commelin (Oct 08 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387613):
<p>Aah, you forgot to typeset that as <em>exists</em></p>

#### [ Johan Commelin (Oct 08 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387620):
<p>Are constructions important for these things?</p>

#### [ Mario Carneiro (Oct 08 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387621):
<p>it is for various conveniences</p>

#### [ Mario Carneiro (Oct 08 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387629):
<p>i.e. it is messy to talk about "a complete ordered field" every time you just want R</p>

#### [ Mario Carneiro (Oct 08 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387647):
<p>it makes all your theorems longer and gives you more things to juggle</p>

#### [ Johan Commelin (Oct 08 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387654):
<p>Ok... I don't understand enough of this.</p>

#### [ Mario Carneiro (Oct 08 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387711):
<p>But for example if all you have is a proof that there exists an alg closure, then you just have a relatively long lived hypothesis saying E is an algebraic closure of F</p>

#### [ Johan Commelin (Oct 08 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387714):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Do you think it means that algebraic closures are harder to do in HoTT than in DTT?</p>

#### [ Johan Commelin (Oct 08 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387721):
<p>And harder to <em>use</em></p>

#### [ Mario Carneiro (Oct 08 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387726):
<p>and then when you get to the end of whatever you needed them for you use the exists assumption to discharge the hypothesis</p>

#### [ Mario Carneiro (Oct 08 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387800):
<p>it means there is no function <code>alg_closure : field -&gt; field</code></p>

#### [ Johan Commelin (Oct 08 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387820):
<p>I see</p>

#### [ Johan Commelin (Oct 08 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387832):
<p>But we <em>can</em> prove that such a function exists.</p>

#### [ Mario Carneiro (Oct 08 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387839):
<p>but there is a kind of yoneda version <code>(closure -&gt; p) -&gt; (field -&gt; p)</code> (where <code>p : Prop</code>)</p>

#### [ Kevin Buzzard (Oct 08 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135387989):
<blockquote>
<p>But we <em>can</em> prove that such a function exists.</p>
</blockquote>
<p>I think in number theory it's very easy to forget that you have to make a big choice here.</p>

#### [ Kevin Buzzard (Oct 08 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388234):
<p>This is one of those issues where a whole bunch of stuff (Frobenius elements, traces of Galois representations etc etc) is all built with an implicit understanding that nobody will ever say anything which will depend on the choice of algebraic closure. Some people probably don't check this or even understand it. But you follow what other people do and it works. Any statement you make about "the" absolute Galois group of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Q</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{Q}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.85556em;vertical-align:-0.16667em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Q</span></span></span></span></span> or "the" maximal extension of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Q</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{Q}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.85556em;vertical-align:-0.16667em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Q</span></span></span></span></span> unramified outside a finite set of primes <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span> -- all these sentences should have an inbuilt resiliance to changing your choice. The moment you make such a choice you are in some sense running the risk that someone else might need your constructions or theorems but with a different choice, and then you need this <code>transfer</code> tactic to make sure that you can move from your choice to theirs.</p>

#### [ Mario Carneiro (Oct 08 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388391):
<p>Now ZF (even without the C) has unique choice, so you can actually do constructions if you can prove the choice doesn't matter</p>

#### [ Mario Carneiro (Oct 08 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388445):
<p>but mathematicians actually take this one step further, by conflating unique with unique up to isomorphism</p>

#### [ Johan Commelin (Oct 08 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388472):
<p>Well, we are ok with "unique up to contractible choice"</p>

#### [ Mario Carneiro (Oct 08 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388499):
<p>I am pretty sure that lots of field extension arguments are not unique in the strict sense required by ZFC or DTT</p>

#### [ Mario Carneiro (Oct 08 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388584):
<p>Interestingly HoTT has exactly the right combination of univalence + unique choice to make this work</p>

#### [ Mario Carneiro (Oct 08 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388666):
<p>actually, maybe not... it depends on how the isomorphisms are presented. If you just prove there exists an isomorphism even HoTT won't swallow it</p>

#### [ Kevin Buzzard (Oct 08 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388691):
<p>The choice of algebraic closure is unique up to hugely non-unique isomorphism and this exactly the problem. It makes talking about elements of absolute Galois groups almost meaningless. Even if you choose a different algebraic closure to me and instantly fix an isomorphism of yours with mine, I might find that I want to fix a different isomorphism of mine with yours, so our dictionaries from moving between the two isomorphic absolute Galois groups are different -- they differ by an inner automorphism. This is why Langlands' philosophy is so successful -- it pushed the idea of looking at representations of Galois groups rather than understanding the structure of the groups themselves. Representations are not changed (up to isomorphism) by an inner automorphism of the group.</p>

#### [ Mario Carneiro (Oct 08 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388756):
<p>right, it's only stuff that is invariant under inner automorphism that would be HoTT constructible</p>

#### [ Mario Carneiro (Oct 08 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388839):
<p>ZFC might still have trouble turning this into a construction, unless you can get the carrier to sit still</p>

#### [ Mario Carneiro (Oct 08 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135388842):
<p>and lean will of course use its global choice function to construct anything you like with no assumptions</p>

#### [ Kevin Buzzard (Oct 08 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135389252):
<blockquote>
<p>and lean will of course use its global choice function to construct anything you like with no assumptions</p>
</blockquote>
<p>Right -- but then you need the transport de structure tactic to ensure that people can apply the theorem.</p>

#### [ Floris van Doorn (Oct 08 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135415520):
<p>These are interesting comments. My experience in undergraduate math courses is that mathematicians are careful with things like non-unique limits in a topological space which is not T2. But maybe that just in undergraduate math courses :)<br>
For something like algebraic closures, I think mathematicians will be careless, since the algebraic closure is unique, even though the isomorphism between two instances is non-unique. This means that in HoTT you indeed cannot write a function <code>algebraic_closure : field -&gt; field</code>. </p>
<p>What's interesting, is that we can express this situation very nicely in HoTT. In HoTT, the type <code>field</code> is considered as the groupoid of fields and isomorphisms. If we just knew that for every field there <em>exists</em> an algebraic closure, we can write that as a function: <code>field -&gt; ∥ field ∥_{-1}</code>, where <code>∥ X ∥_{-1}</code> is called the <em>propositional truncation</em> of <code>X</code>, which is the HoTT-analogue of <code>nonempty</code> (turning a type into a prop by making all elements equal). However, we can express the fact "for every field there exists an algebraic closure unique up to non-unique isomorphism" as a function <code>field -&gt; ∥ field ∥_{0}</code>. Here <code>∥ X ∥_{0}</code> is the <strong>set</strong> of connected components of <code>X</code>, turning a type into a set by making all proof of equality in <code>X</code> equal. This means that in HoTT, as long as you are constructing an element in a set (or proposition), you may assume that a given field has a chosen algebraic closure.</p>

#### [ Johan Commelin (Oct 08 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uses%20of%20choice/near/135415608):
<p>This sounds really cool!</p>


{% endraw %}
