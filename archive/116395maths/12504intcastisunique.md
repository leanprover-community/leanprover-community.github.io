---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/12504intcastisunique.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [int.cast is unique](https://leanprover-community.github.io/archive/116395maths/12504intcastisunique.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Jan 21 2019 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.cast%20is%20unique/near/156541423):
<p>Do we already know that <code>int.cast</code> is the unique ring hom <code>ℤ → R</code>?</p>

#### [ Kevin Buzzard (Jan 21 2019 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.cast%20is%20unique/near/156541435):
<p>I knew that, yes.</p>

#### [ Johan Commelin (Jan 21 2019 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.cast%20is%20unique/near/156541482):
<p>Did your Lean also know it?</p>

#### [ Kevin Buzzard (Jan 21 2019 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.cast%20is%20unique/near/156541503):
<p>Eew, is it some pretty grim induction?</p>

#### [ Johan Commelin (Jan 21 2019 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.cast%20is%20unique/near/156541568):
<p>I don't know, I just want to use it if it's in mathlib.</p>

#### [ Kevin Buzzard (Jan 21 2019 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.cast%20is%20unique/near/156541575):
<p>Yes, I don't think I've seen my Lean know it...</p>

#### [ Johan Commelin (Jan 21 2019 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.cast%20is%20unique/near/156541579):
<p>I can probably write a proof in a couple of minutes...</p>

#### [ Kevin Buzzard (Jan 21 2019 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.cast%20is%20unique/near/156541683):
<p>If we have two ring homomorphisms from <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">A</span></span></span></span> to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>B</mi></mrow><annotation encoding="application/x-tex">B</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span> then the subset of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">A</span></span></span></span> where they coincide is a subring. Do we know that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Z</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{Z}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.68889em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Z</span></span></span></span></span> has no subrings other than itself?</p>

#### [ Chris Hughes (Jan 21 2019 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.cast%20is%20unique/near/156542839):
<p><code>int.eq_cast</code></p>

#### [ Johan Commelin (Jan 21 2019 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.cast%20is%20unique/near/156543031):
<p>Aah... nice. Too bad it isn't stated in terms of ring homs.</p>


{% endraw %}
