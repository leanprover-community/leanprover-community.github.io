---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/65770promotingequiv.html
---

## Stream: [maths](index.html)
### Topic: [promoting equiv](65770promotingequiv.html)

---


{% raw %}
#### [ Kevin Buzzard (Apr 10 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877520):
<p>In mathematics, people constantly invoke the idea that an object is "defined up to unique isomorphism".</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877560):
<p>I have seen this really full in the face in my work on schemes</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877565):
<p>I am defining a certain gadget in algebraic geometry called "the structure sheaf on an affine scheme"</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877586):
<p>and in the mathematics literature it typically goes like this: "the open set is of the form <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>D</mi><mo>(</mo><mi>f</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">D(f)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.02778em;">D</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">)</span></span></span></span> (f is an element of a ring) and define the structure sheaf on this set to be <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span></span></span></span>" (this is just some ring)</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877624):
<p>and the catch is that the open set can be of the form <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>D</mi><mo>(</mo><mi>g</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">D(g)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.02778em;">D</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">)</span></span></span></span> for other elements <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>g</mi></mrow><annotation encoding="application/x-tex">g</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">g</span></span></span></span> of the ring</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877627):
<p>but <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>g</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/g]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">]</span></span></span></span> are isomorphic</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877637):
<p>and moreover there is a unique isomorphism between <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>g</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/g]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">]</span></span></span></span> which has some properties, and this is the isomorphism which mathematicians use to hide behind the issue that they have not actually defined the structure sheaf on this open set.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877682):
<p>Now if this isomorphism were an equality, then <code>eq.rec</code> would be really helpful</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877691):
<p>because I would be able to promote a claim involving <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span></span></span></span> to a claim involving any <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>g</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/g]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">]</span></span></span></span></p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877697):
<p>But it's not an equality -- <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>g</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/g]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">]</span></span></span></span> are most definitely different types</p>

#### [ Gabriel Ebner (Apr 10 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877700):
<p>You can make it into an equality, by taking a quotient on the ring extensions.  Not sure this makes it any simpler, though.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877755):
<p>However there is a special map <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo><mo>→</mo><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>g</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f]\to R[1/g]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">]</span></span></span></span></p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877760):
<p>which I can produce</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877764):
<p>with an inverse</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877771):
<p>and I think what I want is a recursor which enables me to effortlessly change between these rings</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877779):
<p>and just push through all the theorems I want</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877780):
<p>from theorems about <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span></span></span></span></p>

#### [ Gabriel Ebner (Apr 10 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877781):
<p>Hmm, do you care about elements of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span></span></span></span>?</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877782):
<p>to theorems about any choice of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>g</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/g]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">]</span></span></span></span>.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877786):
<p>I do care about elements of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span></span></span></span></p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877823):
<p>however</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877826):
<p>because I am doing maths and not type theory</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877827):
<p>there is some sort of implicit understanding</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877831):
<p>that any theorem I prove will only depend on my object up to "canonical isomorphism"</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877834):
<p>and the map <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo><mo>→</mo><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>g</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f]\to R[1/g]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">]</span></span></span></span> is a canonical isomorphism</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877840):
<p>The word "canonical" does not have a general definition, but in any given case one can supply one</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877844):
<p>for example in this case I can supply some technical maths definition of the form "the unique map with some property"</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877891):
<p>But I do have maps between products of such rings and want to make claims about sets of elements which go to certain other sets of elements</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877897):
<p>And whilst I have not yet embarked upon writing what will be the last proof that I will need for proving that an affine scheme is a scheme</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877898):
<p>I have planned the proof</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877908):
<p>and I know that at some point I will have to replace <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span></span></span></span> with <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>g</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/g]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">]</span></span></span></span> and instantly I will be hit with 10 proof obligations</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877913):
<p>all of which will be of the form "you need to check that the composite of this canonical map with this canonical map is this canonical map"</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877914):
<p>I know how to prove all of these things</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877954):
<p>but I was idly wondering whether I could set up the infrastructure more cleverly</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877958):
<p>because I have just been reading about UniMath</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877959):
<p>and I see that equality is not a Prop there</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877967):
<p>and indeed equality is much more strongly related to equiv than in DTT</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124877970):
<p>which made me think that maybe I was missing a trick here.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878015):
<p>I think that perhaps the way forward here is to actually write the proof</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878016):
<p>and when the explosion of obligations occurs</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878019):
<p>to really think about the simp lemmas I need to kill all of them</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878020):
<p>(or maybe they won't be valid lemmas for simp)</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878024):
<p>and then to ask again.</p>

#### [ Andrew Ashworth (Apr 10 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878029):
<p>is <code>transfer</code> as written for the integers at all helpful? here's the paper from isabelle (<a href="https://www21.in.tum.de/~kuncar/documents/huffman-kuncar-cpp2013.pdf" target="_blank" title="https://www21.in.tum.de/~kuncar/documents/huffman-kuncar-cpp2013.pdf">https://www21.in.tum.de/~kuncar/documents/huffman-kuncar-cpp2013.pdf</a>)</p>

#### [ Johannes Hölzl (Apr 10 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878033):
<p><code>transfer</code> is not only for integers</p>

#### [ Andrew Ashworth (Apr 10 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878036):
<p>of course, i only meant in lean that's where you'll find it used</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878085):
<p>At first glance, this looks like it might be the sort of thing I need</p>

#### [ Johannes Hölzl (Apr 10 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878097):
<p>there are still many things are missing. I never continued to work on it, I think with all the subtypes and quotient types we have now it may worth a try</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878101):
<p>Here is a toy example of the kind of thing I might need</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878164):
<p>It is ridiculous to continually write <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span></span></span></span>, I may as well write <code>X f</code> where <code>f : R</code> (<span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span> is a ring but may as well be a type) and <code>X : Π (f : R), Type</code></p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878215):
<p>There is an equivalence relation on <code>R</code>, and if <code>f</code> and <code>g</code> are equivalent then, in my language, <code>X f</code> and <code>X g</code> are canonically isomorphic.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878225):
<p>This means in practice that if <code>f</code> and <code>g</code> are equivalent then there is a map <code>Y f g : X f -&gt; X g</code></p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878226):
<p>satisfying <code>Y f f = id</code></p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878261):
<p>and <code>Y f g</code> composed with <code>Y g h</code> equals <code>Y f h</code></p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878275):
<p>Now I might have maps <code>X f₁ -&gt; X f₂</code> and <code>X f₂ -&gt; X f₃</code> and a theorem saying that the image of the first map is precisely the preimage of <code>0</code> of the second map</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878277):
<p>(X f is a ring and Y f g sends 0 to 0)</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878321):
<p>and now I want to know _immediately_ that if <code>f_1</code> is equivalent to <code>g_1</code> etc</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878322):
<p>then the image of <code>X g_1 -&gt; X g_2</code> equals the preimage of 0 in <code>X g_2 -&gt; X g_3</code></p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878337):
<p>The proof in Lean is a diagram chase</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878339):
<p>but I have a gazillion of such diagram chases</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878341):
<p>I want the proof to be a tactic or something</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878378):
<p>I want the proof to follow from some foundational properties which I do not need to invoke explicitly.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878390):
<p>That's what going on in my head as a mathematician</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878391):
<p>I don't want to have to invoke lemmas from the mathlib set files</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878395):
<p>I want to say that this is all obvious</p>

#### [ Patrick Massot (Apr 10 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878397):
<p>What about using the limit ring?</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878402):
<p>Yes, the projective limit. I have considered this</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878405):
<p>But do you think that this is what mathematicians do?</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878406):
<p>I am not so sure</p>

#### [ Patrick Massot (Apr 10 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878409):
<p>This is what they do when then get cornered</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878410):
<p>I have seen Lean do impressive things</p>

#### [ Patrick Massot (Apr 10 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878412):
<p>But not otherwise</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878413):
<p>automatically</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878457):
<p>I have seen quite complex goals being solved by refl because I set stuff up right</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878459):
<p>but this will not be refl because <code>X f</code> is not _equal_ to <code>X g</code></p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878471):
<p>Can you see my point Patrick? If <code>X f_i</code> were _equal_ to <code>X g_i</code> then this [image = kenel] would be refl</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878484):
<p>and they're not equal, but they're sufficiently equal that everything that I will be doing with them would yield to some analogue of refl</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878534):
<p>I think that's my point. I have seen the power of <code>rfl</code> and I want it more generally</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878547):
<p>and I don't see why I can't have something like it here</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878550):
<p>because I must be only using some specific collection of ideas which are invariant under canonical isomorphism</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878594):
<p>and I would love to just be able to write down these ideas in this specific case and then just get everything for free</p>

#### [ Patrick Massot (Apr 10 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878613):
<p>Of course we all want magic for free</p>

#### [ Patrick Massot (Apr 10 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878619):
<p>But <code>rfl</code> magic is very special. It's meta-theoretic magic</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878664):
<p>eq.refl is just some constructor</p>

#### [ Patrick Massot (Apr 10 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878671):
<p>Definitional (or judgemental) equality is not inside type theory</p>

#### [ Scott Morrison (Apr 10 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878681):
<p>(I suspect Kevin wants univalence here, but having read the HoTT book doesn't seem to qualify me to speak coherent sentences about univalence in practice...)</p>

#### [ Patrick Massot (Apr 10 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878689):
<p><code>eq.refl</code> is something else</p>

#### [ Patrick Massot (Apr 10 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878740):
<p>You could try to write a proof and then see if some tactic could help. But the mathematical way to solve this problems seems to be using the projective limit</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878742):
<p>It doesn't solve the problem</p>

#### [ Patrick Massot (Apr 10 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878743):
<p>The fact that we don't need it in the real world is the power of sloppy maths discussion</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878744):
<p>does it?</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878748):
<p>It just moves the work I think</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878752):
<p>I prove that some image equals some kernel</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878754):
<p>wait</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878757):
<p>the theorem I have is that the image equals the kernel in the <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span></span></span></span> world</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878800):
<p>I then have to promote this theorem to the projective limit world</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878801):
<p>so I get some canonical object which depends only on the equivalence class of <code>f</code> and is canonically isomorphic to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span></span></span></span></p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878806):
<p><code>X f</code></p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878819):
<p>and now I still have to prove that the image equals the kernel in the projective limit world</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878875):
<p>the only difference being that before <code>X g</code> depended on <code>g</code>, known to be in the same equivalence class of <code>f</code>, whereas now I have some new object <code>X-univ [[f]]</code> which depends only on the equivalence class of <code>f</code></p>

#### [ Patrick Massot (Apr 10 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878878):
<p>You need to do the full proof in the limit world</p>

#### [ Patrick Massot (Apr 10 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878880):
<p>I guess</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878881):
<p>that can't happen</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878885):
<p>the proof only works</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878888):
<p>in the world where I have one f</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878889):
<p>because the proof depends on f</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878890):
<p>The maps don't</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878891):
<p>but the proof does</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878892):
<p>the proof of exactness</p>

#### [ Patrick Massot (Apr 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878894):
<p>What are you proving exactly?</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878896):
<p>I want to go from this:</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878938):
<p><a href="https://stacks.math.columbia.edu/tag/00EJ" target="_blank" title="https://stacks.math.columbia.edu/tag/00EJ">https://stacks.math.columbia.edu/tag/00EJ</a></p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878949):
<p>to the statement that the sheaf axiom holds for finite covers of Spec(R) by basic open sets of the form D(f_i)</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878957):
<p>and the proof is "those two statements say the same thing"</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124878976):
<p>just like Chris' lemma the other day which he found hard to prove, which was that sum from 1 to n of f(i) equalled sum from 1 to n of f(i) formalised in a different way</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124879020):
<p>But the problem is that if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>U</mi></mrow><annotation encoding="application/x-tex">U</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">U</span></span></span></span> is an open set which equals <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>D</mi><mo>(</mo><mi>f</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">D(f)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.02778em;">D</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">)</span></span></span></span> for some <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi></mrow><annotation encoding="application/x-tex">f</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span></span></span></span></p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124879024):
<p>then it is almost certainly equal to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>D</mi><mo>(</mo><mi>g</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">D(g)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.02778em;">D</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">)</span></span></span></span> for lots of other <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>g</mi></mrow><annotation encoding="application/x-tex">g</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">g</span></span></span></span></p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124879033):
<p>and I am not allowed to define the global sections on <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>D</mi><mo>(</mo><mi>f</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">D(f)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.02778em;">D</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">)</span></span></span></span> to be <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span></span></span></span></p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124879035):
<p>because this involves choosing <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi></mrow><annotation encoding="application/x-tex">f</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span></span></span></span>.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124879080):
<p>So like you say I can do some projective limit construction over all <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>g</mi></mrow><annotation encoding="application/x-tex">g</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">g</span></span></span></span> with <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>D</mi><mo>(</mo><mi>f</mi><mo>)</mo><mo>=</mo><mi>D</mi><mo>(</mo><mi>g</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">D(f)=D(g)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.02778em;">D</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.02778em;">D</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">)</span></span></span></span></p>

#### [ Kevin Buzzard (Apr 10 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124879084):
<p>[the equivalence relation on <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span> is that <code>f</code> and <code>g</code> are equivalent iff <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>D</mi><mo>(</mo><mi>f</mi><mo>)</mo><mo>=</mo><mi>D</mi><mo>(</mo><mi>g</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">D(f)=D(g)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.02778em;">D</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.02778em;">D</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">)</span></span></span></span>]</p>

#### [ Kevin Buzzard (Apr 10 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124879091):
<p>or I could also do some construction involving inverting all <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>g</mi></mrow><annotation encoding="application/x-tex">g</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">g</span></span></span></span> which are non-vanishing on <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>U</mi></mrow><annotation encoding="application/x-tex">U</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">U</span></span></span></span></p>

#### [ Kevin Buzzard (Apr 10 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124879096):
<p>and either way I get a new ring which is not definitionally equal to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span></span></span></span></p>

#### [ Kevin Buzzard (Apr 10 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124879099):
<p>but which is uniquely isomorphic to it as <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span>-algebra</p>

#### [ Kevin Buzzard (Apr 10 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124879102):
<p>and now I have to push the diagram chase over</p>

#### [ Kevin Buzzard (Apr 10 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124879103):
<p>It's just a little thing</p>

#### [ Kevin Buzzard (Apr 10 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124879145):
<p>but I feel like it's some variant of <code>rfl</code></p>

#### [ Kevin Buzzard (Apr 10 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124879147):
<p>"you're only chasing around images and kernels of maps, so everything is fine if you replace your rings with isomorphic rings"</p>

#### [ Patrick Massot (Apr 10 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124880478):
<blockquote>
<p>"you're only chasing around images and kernels of maps, so everything is fine if you replace your rings with isomorphic rings"</p>
</blockquote>
<p>I though about this, and I think you are cheating a bit here. You still need the maps in your exact sequence to commute with your canonical isomorphisms. I think you can only hope for automation if you have a really fancy categorical way of defining both your canonical isomorphisms <em>and</em> the maps entering the exact sequence. Otherwise you can still define standard open subsets as equivalence classes of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi></mrow><annotation encoding="application/x-tex">f</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span></span></span></span>, the associated system of rings <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span></span></span></span>, and the sheaf on such an open subsets as the limit of this system. And you can have many lemmas about diagrams of rings (or modules), their limits and how to build exact sequences of limits out of exact sequences and commutation relations. Actually this should probably all be provided by <span class="user-mention" data-user-id="110524">@Scott Morrison</span>'s category theory lib.</p>

#### [ Scott Morrison (Apr 10 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124880767):
<p>(getting there...)</p>

#### [ Kevin Buzzard (Apr 10 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124880888):
<p>My maps are also "canonical" in the sense that they are "built from" the unique R-algebra maps between these rings.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124880941):
<p>By which I mean the map <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo><mo>→</mo><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mi>g</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f]\to R[1/fg]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">]</span></span></span></span> is the unique <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span>-algebra map, and then everything is put together just from such maps in such a way as to not break anything.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/124880951):
<p>Maybe this is going towards telling me exactly which lemmas I need to prove.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/125763232):
<p>Two weeks later and I have all the infrastructure I need to prove that all my diagrams commute painlessly</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/125763237):
<p>In particular, Patrick said "I though about this, and I think you are cheating a bit here. You still need the maps in your exact sequence to commute with your canonical isomorphisms.", and he's right, and I now have this</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/125763243):
<p>so now I start the painful task of taking some exact sequence, replacing every term with an isomorphic term, and then proving that it's still exact</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting%20equiv/near/125763283):
<p>not painful because it's hard, but painful because it's obvious :-)</p>


{% endraw %}
