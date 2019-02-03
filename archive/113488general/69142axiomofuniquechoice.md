---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/69142axiomofuniquechoice.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [axiom of unique choice](https://leanprover-community.github.io/archive/113488general/69142axiomofuniquechoice.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Mar 06 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123358619):
<p>Can I define a <code>def unique_choice {α} {P : α → Prop} (s : subsingleton {a // P a}) (e : ∃ a, P a) : {a // P a} := sorry</code> without using classical choice? Or does Lean’s type theory not allow even this?</p>

#### [ Scott Morrison (Mar 06 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123358771):
<p>(Follow-up questions, if the answer is no: 1. Am I allowed to be sad about this? 2. Should I learn about <code>trunc</code>?)</p>

#### [ Reid Barton (Mar 06 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123359349):
<p>I also wondered about this. My understanding is that <code>unique_choice</code> would need to be <code>noncomputable</code>. From a classical perspective, it ought to be valid without choice, so it could be added as a separate axiom, although I'm not sure there much use in doing so.</p>

#### [ Reid Barton (Mar 06 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123359361):
<p>It's annoying when dealing with limits/colimits (maybe the same situation you are thinking about), since it means that constructively there are really two versions of each of those notions.</p>

#### [ Scott Morrison (Mar 06 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123359937):
<p>I guess the closest computable analogue of <code>unique_choice</code> is</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">quot</span>

<span class="n">def</span> <span class="n">constructive_unique_choice</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">P</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">subsingleton</span> <span class="o">{</span><span class="n">a</span> <span class="bp">//</span> <span class="n">P</span> <span class="n">a</span><span class="o">})</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">trunc</span> <span class="o">{</span><span class="n">a</span> <span class="bp">//</span> <span class="n">P</span> <span class="n">a</span><span class="o">})</span> <span class="o">:</span> <span class="o">{</span><span class="n">a</span> <span class="bp">//</span> <span class="n">P</span> <span class="n">a</span><span class="o">}</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">apply</span> <span class="n">trunc</span><span class="bp">.</span><span class="n">lift</span> <span class="n">id</span> <span class="bp">_</span> <span class="n">e</span><span class="o">,</span>
<span class="n">apply</span> <span class="n">subsingleton</span><span class="bp">.</span><span class="n">elim</span>
<span class="kn">end</span>
</pre></div>

#### [ Scott Morrison (Mar 06 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123360055):
<p>With the idea that <code>trunc {a // P a}</code> is a pretty-good replacement for <code>∃ a, P a</code>.</p>

#### [ Andrew Ashworth (Mar 06 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123361008):
<p>are you aware of anything out there that discusses <code>trunc</code> in an accessible manner? It's not something I've had to use so far, but several people have mentioned it now</p>

#### [ Andrew Ashworth (Mar 06 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123361042):
<p>i've seen a brief mention on <a href="https://homotopytypetheory.org/2012/09/16/truncations-and-truncated-higher-inductive-types/" target="_blank" title="https://homotopytypetheory.org/2012/09/16/truncations-and-truncated-higher-inductive-types/">https://homotopytypetheory.org/2012/09/16/truncations-and-truncated-higher-inductive-types/</a> but is that applicable?</p>

#### [ Mario Carneiro (Mar 06 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123363224):
<p>The answer to your first question, as you have already observed, is no. You can be sad about this if you like, but it is perfectly reasonable from a computational standpoint: Remember that from the VM's point of view, <code>subsingleton {a // P a}</code> is <code>unit</code> and <code>∃ a, P a</code> is <code>unit</code>, while <code>{a // P a}</code> is <code>α</code>. So you are asking the VM to invent an element of <code>α</code> from basically nothing.</p>

#### [ Mario Carneiro (Mar 06 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123363360):
<p>There are two options for constructivizing the <code>∃ a, P a</code> assumption. One is <code>trunc {a // P a}</code> as you have observed.</p>

#### [ Mario Carneiro (Mar 06 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123363373):
<p><span class="user-mention" data-user-email="andrew@ashworth.us" data-user-id="110025">@Andrew Ashworth</span>  Note that the <code>trunc</code> of mathlib is a bit different from the HoTT <code>trunc</code>, or rather, it has different import in a proof irrelevant setting. <code>trunc A</code> is simply a quotient of <code>A</code> by the always true relation. Alternatively stated, <code>trunc A</code> is the universal subsingleton generated by <code>A</code>. Any two elements of <code>trunc A</code> are propositionally equal, so <code>trunc A</code> has one element if <code>A</code> is nonempty and no elements if <code>A</code> is empty.</p>

#### [ Mario Carneiro (Mar 06 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123363428):
<p>But in the VM, because quotients are forgotten, <code>trunc A</code> is <code>A</code>, while the prop analogue <code>nonempty A</code> is <code>unit</code>. So <code>trunc A</code> has computational content and can be used to construct elements from constant functions, or from functions on a subsingleton.</p>

#### [ Mario Carneiro (Mar 06 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123363523):
<p>The second option for constructivizing <code>∃ a, P a</code> is <code>Σ a, P a</code>, or in the unique case we can replace <code>∃! a, P a</code> with <code>Σ! a, P a</code> (these are rarely used and so are not defined in mathlib, but it's not hard to guess what they mean). An element of <code>Σ! a, P a</code> is an element of <code>A</code> and a proof that every other element of <code>A</code> is equal to it. In HoTT this would be called <code>contr</code> I think, since it expresses that <code>A</code> is contractible</p>

#### [ Mario Carneiro (Mar 06 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123363564):
<p>In this case, you can "unique choose" simply by projecting out the first component</p>

#### [ Mario Carneiro (Mar 06 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123363726):
<p>By the way, the best introduction to propositional truncation in the HoTT sense is the HoTT book, and most of it applies to reasoning about <code>trunc</code> (although you can ignore anything that talks about n-truncating for n &gt;= 0, or anything about equality of proofs)<br>
<a href="https://hott.github.io/book/nightly/hott-online-1132-g5052dbc.pdf#section.3.7" target="_blank" title="https://hott.github.io/book/nightly/hott-online-1132-g5052dbc.pdf#section.3.7">https://hott.github.io/book/nightly/hott-online-1132-g5052dbc.pdf#section.3.7</a></p>

#### [ Mario Carneiro (Mar 06 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123363805):
<p>In the description there, you should replace the term "mere proposition" with "subsingleton". If you replace it with "proposition" instead you get <code>nonempty</code>, which is the <code>Prop</code> truncation operation</p>

#### [ Reid Barton (Mar 06 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123364120):
<p>There's also <code>A ≃ unit</code> in mathlib as a constructive version of being a singleton.</p>

#### [ Reid Barton (Mar 06 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123364177):
<p>I'm a little surprised by "these are rarely used and so are not defined in mathlib", since a great many constructions are characterized by a universal property and for a constructivist I'd think it would be natural to ask that the existence part of the universal property be given constructively</p>

#### [ Reid Barton (Mar 06 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123364245):
<p>(For instance, imagine if the induction principle for an inductive data type only allowed you to conclude <code>∃!</code> function which satisfies the recursive equations.)</p>

#### [ Mario Carneiro (Mar 06 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123364385):
<p>It is almost always better to state the two parts of sigma exists separately: one to make a definition and a second to assert everything satisfying the universal property is equal to it. What is not used is the pairing itself, which would only be useful if you are doing some kind of higher order construction like quantifying over all uniquely definable objects</p>

#### [ Reid Barton (Mar 06 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123364592):
<p>Well, here is an example: how one might write down the definition of a coproduct in a category.</p>
<div class="codehilite"><pre><span></span><span class="kn">variable</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span>
<span class="kn">variable</span> <span class="o">{</span><span class="n">Hom</span> <span class="o">:</span> <span class="n">C</span> <span class="bp">→</span> <span class="n">C</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">}</span>
<span class="kn">variable</span> <span class="o">{</span><span class="n">comp</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="n">Z</span><span class="o">},</span> <span class="n">Hom</span> <span class="n">Y</span> <span class="n">Z</span> <span class="bp">→</span> <span class="n">Hom</span> <span class="n">X</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">Hom</span> <span class="n">X</span> <span class="n">Z</span><span class="o">}</span>
<span class="n">def</span> <span class="n">coprod</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">C</span><span class="o">)</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">Hom</span> <span class="n">a</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">Hom</span> <span class="n">b</span> <span class="n">c</span><span class="o">)</span>
  <span class="o">:=</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">z</span> <span class="o">:</span> <span class="n">C</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">Hom</span> <span class="n">a</span> <span class="n">z</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">Hom</span> <span class="n">b</span> <span class="n">z</span><span class="o">),</span>
     <span class="bp">∃!</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">Hom</span> <span class="n">c</span> <span class="n">z</span><span class="o">),</span> <span class="n">comp</span> <span class="n">h</span> <span class="n">i</span> <span class="bp">=</span> <span class="n">f</span> <span class="bp">∧</span> <span class="n">comp</span> <span class="n">h</span> <span class="n">j</span> <span class="bp">=</span> <span class="n">g</span>
</pre></div>

#### [ Reid Barton (Mar 06 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123364606):
<p>I claim this definition is "wrong", because <code>∃!</code> needs to be <code>Σ!</code>.</p>

#### [ Reid Barton (Mar 06 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123364661):
<p>I'm not sure how to apply your suggestion in this situation</p>

#### [ Mario Carneiro (Mar 06 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123364871):
<p><code>coprod</code> should be a structure, with a first component that gives the hom, and two more components for the equalities</p>

#### [ Scott Morrison (Mar 06 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123366588):
<p>Thank you, Mario, for this very helpful explanation of how to think about <code>trunc</code>.</p>

#### [ Scott Morrison (Mar 06 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123366807):
<p><span class="user-mention" data-user-email="rwbarton@gmail.com" data-user-id="110032">@Reid Barton</span>, my structure for Coproduct (rather long-winded, I know) is at <a href="https://github.com/semorrison/lean-category-theory/blob/master/src/categories/universal/universal.lean#L103" target="_blank" title="https://github.com/semorrison/lean-category-theory/blob/master/src/categories/universal/universal.lean#L103">https://github.com/semorrison/lean-category-theory/blob/master/src/categories/universal/universal.lean#L103</a>. I am tempted to introduce and use the <code>Σ!</code> notation, however. The price of course is less descriptive names.</p>

#### [ Scott Morrison (Mar 06 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123366908):
<p>The reason I was thinking about unique choice was being sad that the first isomorphism theorem (e.g. for vector spaces, in mathlib already, or for groups, which Mitchell is PR’ing soon) had to be marked as noncomputable.</p>

#### [ Scott Morrison (Mar 06 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123366929):
<p>Really I would like to be able to talk about the “constructive image” of a group homomorphism. One should then be able to prove <code>G / ker f</code> is isomorphic to the constructive image, without choice.</p>

#### [ Scott Morrison (Mar 06 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123366979):
<p>But neither <code>trunc</code> nor sigma types help here, as we would want the constructive image to still be a set.</p>

#### [ Mario Carneiro (Mar 06 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123366990):
<p>Do you have a link to the theorem you are referring to?</p>

#### [ Mario Carneiro (Mar 06 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123367055):
<p>But yes, this is a problem with using <code>set</code>. Writing ideals as a subcollection of <code>set A</code> is already going mostly classical</p>

#### [ Scott Morrison (Mar 06 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123367062):
<p><span class="user-mention" data-user-email="di.gama@gmail.com" data-user-id="110049">@Mario Carneiro</span> <a href="https://github.com/leanprover/mathlib/blob/master/algebra/linear_algebra/linear_map_module.lean#L92" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/algebra/linear_algebra/linear_map_module.lean#L92">https://github.com/leanprover/mathlib/blob/master/algebra/linear_algebra/linear_map_module.lean#L92</a></p>

#### [ Scott Morrison (Mar 06 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123367074):
<p>I guess one could just not define the image as a set.</p>

#### [ Scott Morrison (Mar 06 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123367089):
<p>But rather look at pairs, an element h of H, and a truncated sigma type \Sigma g : G, f g = h, and just put a group structure on those directly.</p>

#### [ Scott Morrison (Mar 06 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123367140):
<p>That thing is classically isomorphic to the usual image, but you should be able to (?) give a constructive first isomorphism theorem.</p>

#### [ Mario Carneiro (Mar 06 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123367156):
<p>Note that such a type is equivalent to the quotient of the domain of f by <code>f a = f b</code></p>

#### [ Mario Carneiro (Mar 06 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123367163):
<p>i.e. it's basically true by equivalence of the underlying types already</p>

#### [ Scott Morrison (Mar 06 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123367208):
<p>Even better <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Mario Carneiro (Mar 06 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123367211):
<p>I think the moral of the story is: don't use the first isomorphism theorem at all, just stick to the LHS</p>

#### [ Scott Morrison (Mar 06 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123367283):
<p>Or paraphrasing: if you want to do constructive group theory, _define_ the image of a morphism as the quotient of the domain by the kernel, and have this theorem be a tautology. <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Kevin Buzzard (Mar 06 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123369230):
<p>It's this sort of talk that gives constructivism a bad name amongst mathematicians!</p>

#### [ Patrick Massot (Mar 06 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123369542):
<p>I couldn't agree more</p>

#### [ Patrick Massot (Mar 06 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123369592):
<p>I can only hope no such consideration will trigger design decision making it harder to do group theory with Lean</p>

#### [ Mario Carneiro (Mar 06 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123369671):
<p>why do you say that? It seems that the constructive interpretation reveals a deeper equivalence, that does not have anything to do with groups but extends to all the "first isomorphism theorems"</p>

#### [ Patrick Massot (Mar 06 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123369732):
<p>Errrr... Are your referring to "if you want to do constructive group theory, _define_ the image of a morphism as the quotient of the domain by the kernel, and have this theorem be a tautology."?</p>

#### [ Mario Carneiro (Mar 06 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123369746):
<p>that's the practical upshot of this observation</p>

#### [ Kevin Buzzard (Mar 06 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123369840):
<p>because what you're defining there is the co-image</p>

#### [ Kevin Buzzard (Mar 06 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123369842):
<p>we already have a name for it</p>

#### [ Kevin Buzzard (Mar 06 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123369843):
<p>and it's not the image</p>

#### [ Kevin Buzzard (Mar 06 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123369845):
<p>although it's often canonically isomorphic to it</p>

#### [ Mario Carneiro (Mar 06 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123369906):
<p>okay, then the import of the observation is "coimage is image but better"</p>

#### [ Scott Morrison (Mar 07 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123372633):
<p>Once Mitchell has finished with his PR, I may try to refactor his proof of the first isomorphism theorem into two pieces:<br>
1. The (constructive) isomorphism between <code>G / ker f</code> and <code>\Sigma h : H, trunc (\Sigma g : G, f g = h)</code> (what I was calling the “constructive image” above)<br>
2. The (noncomputable) isomorphism between the constructive image and the usual image <code>{h | \Exists g : G, f g = h}</code>.</p>

#### [ Scott Morrison (Mar 07 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123372709):
<p>I’m curious if <span class="user-mention" data-user-email="patrickmassot@free.fr" data-user-id="110031">@Patrick Massot</span> and <span class="user-mention" data-user-email="k.buzzard@imperial.ac.uk" data-user-id="110038">@Kevin Buzzard</span> would still disapprove of this. <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span> The point is that the first isomorphism is very often all you need, because however you proved that <code>h \elem image f</code> was probably (because it was probably constructive) enough to produce a point in the constructive image too, and then you can do calculations.</p>

#### [ Scott Morrison (Mar 07 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123372727):
<p>(And it’s not entirely good enough to say: “but we have Sage for calculations!” because group theory specific tactics will eventually want to do calculations internally...)</p>

#### [ Scott Morrison (Mar 07 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123372784):
<p>Alternatively, <span class="user-mention" data-user-email="u5796267@anu.edu.au" data-user-id="110504">@Mitchell Rowett</span> may like to do this himself, except that I probably should resist the temptation to suggest this to him, as he has to finish his assignment for my class, and all his other classes. <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Johannes Hölzl (Mar 07 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123389280):
<p><span class="user-mention" data-user-email="scott@tqft.net" data-user-id="110087">@Scott Morrison</span> the first and the second isomorphism laws are already in mathlib. You find them in <code>algebra/linear_algebra/prod_module.lean</code>.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123389516):
<p>I cannot really comment on these issues because in my world you can't get anywhere constructively so I never worry.</p>

#### [ Scott Morrison (Mar 07 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123402179):
<p><span class="user-mention" data-user-email="johannes.hoelzl@gmx.de" data-user-id="110294">@Johannes Hölzl</span>, I was talking about the isomorphism theorems for groups, not vector spaces. (Sorry if I wasn’t clear — one of the undergrads here has been doing some basic group theory.) There are going to be a lot of these! (Every category where images and coimages agree.)</p>

#### [ Johannes Hölzl (Mar 08 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123434947):
<p>The first and second isormorphisms theorem is about modules. So when you see groups as Z-modules then you already got the group isomorphism laws. Or are the group isomorphism laws different statements?</p>

#### [ Mario Carneiro (Mar 08 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123435108):
<p>An abelian group is a Z-module, but general groups can't be expressed as a special case of modules AFAIK</p>

#### [ Johannes Hölzl (Mar 08 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123435204):
<p>Ah, now I see the difference. Thanks!</p>

#### [ Kevin Buzzard (Mar 08 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123435860):
<p>I think that even if you allow non-commutative rings, you can't model groups as modules, because a module is an abelian group by definition.</p>

#### [ Mario Carneiro (Mar 08 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123435910):
<p>In fact, even if you drop the abelian requirement, you can prove commutativity by expanding <code>(1+1)(x+y)</code> in two ways</p>

#### [ Kevin Buzzard (Mar 08 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123435975):
<p>Ha ha, you have to be careful doing that sort of thing. When Kenny and I were on the home straight for schemes yesterday we had to define the zero element of a complicated type which we wanted to be a ring, and after the dust settled we had to check that a ring homomorphism sent 0 to 0. But Kenny had defined a ring homomorphism without putting this in as an axiom as he'd observed it followed from f(x+y)=f(x)+f(y) so we had to stop what we were doing and prove that this implied f(0)=0 :-)</p>

#### [ Mario Carneiro (Mar 08 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123436076):
<p>...that's a good thing, though</p>

#### [ Kevin Buzzard (Mar 08 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123436591):
<p>Talking of which, what should happen to the observation that the current definition of a basis of a topological space in mathlib asks for more than is necessary? Kenny and I defined <code>is_basis'</code> and proved <code>basis iff basis'</code>. It was much easier to prove that something was a <code>basis'</code> and indeed when we prove affine schemes are schemes we will be working with a <code>basis'</code> of the topology for Spec(R). Is this a satisfactory state of affairs? Because we proved basis iff basis' we don't need anything to change, I just thought it was a bit weird.</p>

#### [ Mario Carneiro (Mar 08 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123436891):
<p>Could you be more specific? What's the new definition?</p>

#### [ Mario Carneiro (Mar 08 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123437004):
<p>Hm, I think I know what you did. To me the last condition in <code>is_topological_basis</code> feels a bit artificial; I would prefer that the definition not make any reference to a topological space, in which case the first two conditions are what you want. But it's true that if you know that a collection of sets is the generating set for a topology, then there are easier ways to say the same thing</p>

#### [ Mario Carneiro (Mar 08 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123437021):
<p>Probably <code>is_topological_basis_of_open_of_nhds</code> is the characterization you would like?</p>

#### [ Kevin Buzzard (Mar 08 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123437561):
<p>We had a conversation a couple of weeks ago where I said "I was trying to prove something was a basis and I looked at the definition in mathlib, which Johannes had taken from a maths book, and it stank; I didn't want to prove two of the axioms because they followed from the rest". You replied "oh yeah, I just proved that basis -&gt; something else without using these two axioms." And then Kenny proved that my definition of basis was equivalent to mathlibs. My definition (i.e. the standard one, as far as I am concerned) is much easier to work with. The question is whether you are interested in a PR which changes the definition of a basis in mathlib. I can  be more specific over the weekend when I've got over my current deadlines. I'll look at the function you mention later, I've got to run :-/ I have starred your message :-)</p>

#### [ Johannes Hölzl (Mar 08 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123437674):
<p>The definition of <code>is_topological_basis_of_open_of_nhds</code> changed in  <a href="https://github.com/leanprover/mathlib/commit/e2a562a8df52c2b0fffad361605fcbc03cb99b4b" target="_blank" title="https://github.com/leanprover/mathlib/commit/e2a562a8df52c2b0fffad361605fcbc03cb99b4b">https://github.com/leanprover/mathlib/commit/e2a562a8df52c2b0fffad361605fcbc03cb99b4b</a> . I'm happy if there are further simplifications. But I don't yet know what you want to change</p>

#### [ Mario Carneiro (Mar 08 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123437907):
<p>Maybe this will help to clarify my intent here. To me, a topological basis is a property of a set of sets, which does not depend on a prior notion of what a topology is. It is a necessary and sufficient condition so that the collection of unions of basis elements forms a topology. However, given a topological basis, there is of course a natural associated topology, and given a topology, one can express the property of being a basis that generates that topology, and this is what <code>is_topological_basis_of_open_of_nhds</code> is for.</p>

#### [ Mario Carneiro (Mar 08 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123437979):
<p>So if your definition of topological basis starts "a basis is a collection of open sets" then it's missing the point, which is to classify what a basis is in the abstract, independently of the topology.</p>

#### [ Johannes Hölzl (Mar 08 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123438143):
<p>I agree! Interestingly, the mathlib definition of basis did not change, but the theorem got simpler.</p>

#### [ Kevin Buzzard (Mar 08 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/axiom%20of%20unique%20choice/near/123439774):
<p>I will get back to you on all this later (Saturday?). I really like this starring in Zulip; it really helps my workflow.</p>


{% endraw %}
