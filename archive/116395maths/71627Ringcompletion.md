---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/71627Ringcompletion.html
---

## Stream: [maths](index.html)
### Topic: [Ring completion](71627Ringcompletion.html)

---


{% raw %}
#### [ Patrick Massot (Dec 18 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152110493):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>  I think I just completed the topological ring completion project. Remember where we got stuck last time: we could define a ring structure on <code>completion a</code> assuming that <code>a</code> was a <em>separated</em> topological ring, see <a href="https://github.com/leanprover/mathlib/blob/master/analysis/topology/completion.lean#L1168" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/analysis/topology/completion.lean#L1168">https://github.com/leanprover/mathlib/blob/master/analysis/topology/completion.lean#L1168</a>. We could also construct a ring structure on <code>quotient (separatation_setoid a)</code>, see <a href="https://github.com/leanprover/mathlib/blob/master/analysis/topology/quotient_topological_structures.lean#L204" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/analysis/topology/quotient_topological_structures.lean#L204">https://github.com/leanprover/mathlib/blob/master/analysis/topology/quotient_topological_structures.lean#L204</a>. I did that by leveraging the algebraic quotient construction, using that the separation relation for uniform groups is the same as the left coset relation for the closure of zero. This meant fighting the system to use an equivalence relation equality to relate the quotients. Then I constructed <a href="https://github.com/leanprover/mathlib/blob/master/analysis/topology/completion.lean#L710-L711" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/analysis/topology/completion.lean#L710-L711">https://github.com/leanprover/mathlib/blob/master/analysis/topology/completion.lean#L710-L711</a> <code>completion (quotient $ separatation_setoid a) ≃ completion α</code> which I hoped to use to glue the preceding two constructions and get a ring structure on <code>completion α</code>. But this meant fighting Lean again, for lack of transport of structure along this equiv.</p>

#### [ Johannes Hölzl (Dec 18 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152110596):
<p>Yes, I remember. How did you solve it. Or did you copy the structure and wrote down the transport for each rule?</p>

#### [ Patrick Massot (Dec 18 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152110617):
<p>So I backtracked completely. I defined a ring structure on <code>sep_quot α := quotient (separatation_setoid a)</code> directly, using the link between the separation relation and the closure of zero only in the lemma proving that multiplication descends to the quotient. And then I defined <code>hcompletion α := completion (sep_quot α)</code>. This looks really weird because remember <code>completion α := quotient (separation_setoid $ Cauchy α)</code>, so we use the separation relation twice. But it works very smoothly</p>

#### [ Patrick Massot (Dec 18 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152110717):
<p>Remember how Bourbaki does it: they replace <code>Cauchy α</code> with the space of <em>minimal</em> Cauchy filters on α. And they define the completion as <code>min_cauchy (quotient $ separatation_setoid a)</code>. That's how they avoid the double quotient</p>

#### [ Patrick Massot (Dec 18 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152110728):
<p>while still first getting rid of the separation issue</p>

#### [ Patrick Massot (Dec 18 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152110785):
<p>I didn't start that road because I saw you did everything with non-minimal Cauchy filters. And of course all three constructions solve the same universal problem, so there are uniquely isomorphic</p>

#### [ Johan Commelin (Dec 18 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152110831):
<p>Cool! Congrats on completing this! <span class="emoji emoji-1f389" title="tada">:tada:</span></p>

#### [ Patrick Massot (Dec 18 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152110892):
<p>The messy thing with my construction is that <code>completion α</code> becomes a purely intermediate thing, still with a rather large theory, which needs to be restated for <code>hcompletion</code></p>

#### [ Kevin Buzzard (Dec 18 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152111034):
<p>Is "Bourbaki did it this way" an argument for or against "Lean should do it this way", or are they just independent things?</p>

#### [ Patrick Massot (Dec 18 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152111074):
<p>It's part of my excuse for creating this mess</p>

#### [ Patrick Massot (Dec 18 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152111173):
<p>I mean this mess: <code>instance : has_coe α (hcompletion α) := ⟨quotient.mk ∘ Cauchy.pure_cauchy ∘ quotient.mk⟩</code></p>

#### [ Kevin Buzzard (Dec 18 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152111181):
<p>If it works, it works :-)</p>

#### [ Kenny Lau (Dec 18 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152111293):
<p>you can't maintain a library by bodging...</p>

#### [ Patrick Massot (Dec 18 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152111369):
<p>It has a very clean interface since it solves a very clearly specified universal problem</p>

#### [ Kevin Buzzard (Dec 18 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152111438):
<p>Is one of the the issues that we need to transport theorems along isomorphisms and this is still not yet possible, so we fudge our way around it?</p>

#### [ Patrick Massot (Dec 18 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152111474):
<p>The transport idea was already a work-around actually</p>

#### [ Patrick Massot (Dec 18 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152113098):
<p>The big thing is at <a href="https://github.com/PatrickMassot/mathlib/commit/6dbdbbfe5304e85d95784f18d9a978ab129a84c8" target="_blank" title="https://github.com/PatrickMassot/mathlib/commit/6dbdbbfe5304e85d95784f18d9a978ab129a84c8">https://github.com/PatrickMassot/mathlib/commit/6dbdbbfe5304e85d95784f18d9a978ab129a84c8</a></p>

#### [ Patrick Massot (Dec 18 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152113142):
<p>That's 500 more lines to <code>completion.lean</code></p>

#### [ Patrick Massot (Dec 18 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152113277):
<p>But some of them should move elsewhere, independently of the reorganization discussion</p>

#### [ Patrick Massot (Dec 18 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152113409):
<p>It includes using <code>def function.comp₂ (f : α → β → γ) (g : γ → δ) : α → β → δ := λ  x y, g (f x y)</code> and its companions <code>def continuous₂ (f : α → β → γ) := continuous (function.uncurry f)</code> etc to nicely handle functions of two variables (like addition and multiplication), as was mentioned in another thread</p>

#### [ Patrick Massot (Dec 18 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152113626):
<p>I'd like to get <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> input before finishing restating stuff for <code>hcompletion</code></p>

#### [ Johannes Hölzl (Dec 18 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152113645):
<p>I think <code> continuous₂</code> and <code>uniform_continuous₂</code> should be fully transparent, without any rules about them. So only use them when writing down concrete instances</p>

#### [ Patrick Massot (Dec 18 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152113690):
<p>I need them as assumption for many statements</p>

#### [ Johannes Hölzl (Dec 18 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152113703):
<p>Yes, there its okay</p>

#### [ Patrick Massot (Dec 18 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152113719):
<p>and the most important piece is the composition lemma</p>

#### [ Patrick Massot (Dec 18 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152113731):
<p><a href="https://github.com/PatrickMassot/mathlib/commit/6dbdbbfe5304e85d95784f18d9a978ab129a84c8#diff-f7d0385aaa9b17579cee0f2af9cc9135R120" target="_blank" title="https://github.com/PatrickMassot/mathlib/commit/6dbdbbfe5304e85d95784f18d9a978ab129a84c8#diff-f7d0385aaa9b17579cee0f2af9cc9135R120">https://github.com/PatrickMassot/mathlib/commit/6dbdbbfe5304e85d95784f18d9a978ab129a84c8#diff-f7d0385aaa9b17579cee0f2af9cc9135R120</a></p>

#### [ Patrick Massot (Dec 18 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152113791):
<p>This is what make this so convenient</p>

#### [ Patrick Massot (Dec 18 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152124223):
<blockquote>
<p>Remember how Bourbaki does it: they replace <code>Cauchy α</code> with the space of <em>minimal</em> Cauchy filters on α. And they define the completion as <code>min_cauchy (quotient $ separatation_setoid a)</code>. That's how they avoid the double quotient</p>
</blockquote>
<p>I just checked, and actually the above is not quite correct. It seems that minimal Cauchy filters are already separated.</p>

#### [ Patrick Massot (Dec 18 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Ring%20completion/near/152124381):
<p>So this is a really more economical way of building the Hausdorff completion. But they don't solve problem of factorizing morphisms into complete spaces (not hausdorff complete spaces), whereas we do it.</p>


{% endraw %}
