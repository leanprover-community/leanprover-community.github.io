---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64106deeplyunhappywithcoercions.html
---

## Stream: [general](index.html)
### Topic: [deeply unhappy with coercions](64106deeplyunhappywithcoercions.html)

---


{% raw %}
#### [ Scott Morrison (Oct 25 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136441426):
<p>We've tried using coercions throughout the <code>category_theory/</code> development within mathlib, so that one can write <code>F X</code> for a functor applied to an object, and <code>a X</code> for a natural transformation applied to an object.</p>

#### [ Scott Morrison (Oct 25 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136441491):
<p>This causes a lot of problems. In particular coercions incorrectly applied, deep inside the enormous implicit arguments common in dependent type theory, cause <code>simp</code> and <code>rw</code> to often fail.</p>

#### [ Scott Morrison (Oct 25 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136441521):
<p>I think I'm about ready to declare the experiment of using coercions a failure, and to rip them out  of the category_theory development for now.</p>

#### [ Scott Morrison (Oct 25 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136441610):
<p>The time I have wasted diagnosing "why won't simp just do this" seems to far outweigh the value of not having to write <code>F.obj X</code> or <code>a.app X</code>.</p>

#### [ Scott Morrison (Oct 25 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136441741):
<p>Just as a typical example:</p>
<div class="codehilite"><pre><span></span>rewrite tactic failed, did not find instance of the pattern in the target expression
  ⇑α X ≫ ⇑(iso.symm α) X
state:
C : Type u,
𝒞 : category C,
J : Type v,
_inst_1 : small_category J,
F G : isos (J ⥤ C),
α : F ⟶ G,
x : cone F,
X : J
⊢ ⇑↑α X ≫ ⇑↑(iso.symm α) X = ?m_1
</pre></div>

#### [ Scott Morrison (Oct 25 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136441750):
<p><code>erw</code> works fine, but <code>rw</code> and <code>simp</code> choke.</p>

#### [ Chris Hughes (Oct 25 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136441768):
<p>Make a <code>simp</code> lemma that simplifies the double coercions?</p>

#### [ Scott Morrison (Oct 25 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136441979):
<p>I mean, yes, I can try that. But diagnosing what the double coercion going on here actually is will take me more time than I ever would have spent in the entire history of working on mathlib writing out the explicit <code>.obj</code> and <code>.app</code> fields myself...</p>

#### [ Scott Morrison (Oct 25 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136447529):
<p>And yet more examples, in the same proof, all caused by coercions.</p>
<p>With tactic state:</p>
<div class="codehilite"><pre><span></span>C : Type u,
𝒞 : category C,
J : Type v,
_inst_1 : small_category J,
F G : isos (J ⥤ C),
α : F ⟶ G,
x : cone F,
X : J
⊢ ⇑(functor.map (functor.const J) (𝟙 (x.X))) X ≫ ⇑(x.π) X = ⇑(x.π) X
</pre></div>


<p>Of course <code>simp</code> should work, by applying the <code>@[simp]</code> lemma <code>functor.map_id</code>. It doesn't, even though <code>rw functor.map_id</code> works fine. The reason of course is because the coercion to function types break <code>simp</code>, because it doesn't have congruence lemmas that let it reliably step inside dependent functions.</p>

#### [ Scott Morrison (Oct 25 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136447573):
<p>You can see a similar thing if you instead try to <code>conv</code> your way in:</p>

#### [ Scott Morrison (Oct 25 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136447584):
<p><code>conv {to_lhs, congr}</code> gets you to the state </p>
<div class="codehilite"><pre><span></span>2 goals
C : Type u,
𝒞 : category C,
J : Type v,
_inst_1 : small_category J,
F G : isos (J ⥤ C),
α : F ⟶ G,
x : cone F,
X : J
| ⇑(functor.map (functor.const J) (𝟙 (x.X))) X

C : Type u,
𝒞 : category C,
J : Type v,
_inst_1 : small_category J,
F G : isos (J ⥤ C),
α : F ⟶ G,
x : cone F,
X : J
| ⇑(x.π) X
</pre></div>

#### [ Scott Morrison (Oct 25 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136447597):
<p>but one further <code>congr</code> (which should step us inside the coercion), just says <code>congr tactic failed, unsupported congruence lemma</code>.</p>

#### [ Scott Morrison (Oct 25 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136447602):
<p>On every front, coercions are just unpleasant.</p>

#### [ Chris Hughes (Oct 25 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136449146):
<p>The dependent argument problem is a biggy. It might even be fixed by having a non-dependent <code>has_coe_to_fun</code> class, since most of them are non-dependent anyway.</p>

#### [ Scott Morrison (Oct 25 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136450130):
<p>I think all my cases really are coercions to dependent function types.</p>

#### [ Chris Hughes (Oct 25 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136450426):
<p>Won't it still break simp if you don't use <code>coe_to_fun</code> then?</p>

#### [ Johan Commelin (Oct 25 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136453416):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> two reactions:</p>
<ul>
<li>Reading this makes me sad. It shows that we aren't there yet. I hope Lean 4 fixes this, maybe using the idea of Reid to have type-dependent notation.</li>
<li>Writing <code>.obj</code>, <code>.map</code> and <code>.app</code> isn't so much of a hassle. I'll get used to it quickly.</li>
</ul>

#### [ Floris van Doorn (Oct 25 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136455046):
<p>The coercion mechanism in Lean 3 was one of the major headaches/bottlenecks in porting the HoTT library from Lean 2 to Lean 3. In Lean 2, coercions worked much better. My two main complaints with the coercion mechanism in Lean 3 (neither of which was a problem in Lean 2):</p>
<ul>
<li>The  same complaint as Scott gave: it is super hard to make coercions reduce well. You need lemmas to rewrite the non-coercion function to the coercion (or the other way around), and you need to make sure that <em>all</em> simplification lemmas use the "normal form": either they all use coercions, or all use the underlying function explicitly.</li>
<li>Lean 3 is more restrictive when inserting coercions. If the preprocessor has found out that <code>F : functor ?M1 ?M2</code> and it needs to be of type <code>?M3 -&gt; ?M4</code> (for example, when it is applied to a term), then in Lean 3, the coercion mechanism doesn't fire yet, because for some reason, it needs to know the exact type of <code>F</code> without any metavariables in it. In Lean 2, a coercion was inserted, and then from the context, it could afterwards figure out the exact value of the metavariables.</li>
</ul>

#### [ Kevin Buzzard (Oct 25 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136456991):
<p>There is some sort of sociological side to all of this. As mathematicians we are <em>so used</em> to these coercions that the thought of some computer claiming that they can do all pure maths means that surely it must be smart enough to do the coercions too, like us. But of course we know they're there, and it is a <em>complete triviality</em> to write them ("if I write <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>F</mi><mo>(</mo><mi>X</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">F(X)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mclose">)</span></span></span></span> it's clearly the functor on objects; if I write <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>F</mi><mo>(</mo><mi>f</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">F(f)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">)</span></span></span></span> it's clearly the functor on morphisms, so I guess I could write <code>F.obj</code> easily, it's not as if I don't know which one I'm using"). This now raises the question -- if it's so easy, how come the computer can't do it? But if Scott has found an answer to this (and of course he may not have -- one can't rule out Mario just appearing and saying "do this trick and it'll be fine") then so be it. I know at all times if I'm applying my functor to an object or a morphism and I'm not scared of telling you, if you really want to know.</p>

#### [ Reid Barton (Oct 25 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136479587):
<p>I think I was one of the people asking for coercions in category theory. However, when I tried upgrading the mathlib dependency of my homotopy theory project to the version which uses coercions, I also found them to be much more of a hassle then they were worth. So, I'm actually glad to hear that Scott is of the same opinion.</p>

#### [ Reid Barton (Oct 25 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136479710):
<p>It really is the combination of the two points mentioned by Floris: <code>simp</code> really wants you to write the same thing in the same way every time, but coercions are not always conveniently available because of the way they interact with metavariables.</p>

#### [ Reid Barton (Oct 25 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136479750):
<p>On the plus side, I now have a better understanding of how to use <code>erw</code> :)</p>

#### [ Scott Morrison (Oct 26 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136534446):
<p>So, ... <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> and <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>, how would you feel about me exploring removing the coercions from <code>category_theory/</code>?</p>

#### [ Johannes Hölzl (Oct 26 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136535059):
<p>I would prefer them to stay. But I can see why you want to remove them. In your original example <code>⇑↑α X ≫ ⇑↑(iso.symm α) X = ?m_1</code>, where does the coercion on <code>↑α</code> and <code>↑(iso.symm α)</code> come from?</p>

#### [ Scott Morrison (Oct 26 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136536337):
<p>There are coercions there from isomorphisms to morphisms, and from natural transformations to the component function.</p>

#### [ Scott Morrison (Oct 26 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136536358):
<p>That original example is not the complaint I should have started with. Adding yet more simp lemmas about certain classes of double coercions solves it.</p>

#### [ Scott Morrison (Oct 26 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136536525):
<p>The real problems are:</p>
<ul>
<li>the presence of coercions to dependent function types significantly inhibits <code>simp</code> and <code>conv</code>, forcing us to construct long <code>rw</code> proofs by hand</li>
<li>even in rewrite proofs, we find ourselves having to use <code>erw</code> instead of <code>rw</code> at mysterious moments, because of coercions not being in the perfect form deep inside implicit arguments</li>
<li>it's an extra "dimension" for <code>simp</code> to work in, and we need to consistently simp everything back to the coerced form.</li>
<li>sometimes the coercions just don't fire, and so we need to write things explicitly, and then perform trickery to rewrite lemmas back into coerced form, so they are relevant in the "always use coercions" world.</li>
</ul>

#### [ Scott Morrison (Oct 26 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deeply%20unhappy%20with%20coercions/near/136536535):
<p>In all, very unpleasant.</p>


{% endraw %}
