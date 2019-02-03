---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28061Modulerefactor.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Module refactor](https://leanprover-community.github.io/archive/113488general/28061Modulerefactor.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Jan 08 2019 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Module%20refactor/near/154648106):
<p><a href="https://github.com/leanprover-community/mathlib/tree/module-refactor" target="_blank" title="https://github.com/leanprover-community/mathlib/tree/module-refactor">I have refactored modules in order to make it possible for a module to be based on two rings.</a> However, there is a small part in analysis/normed_space written by <span class="user-mention" data-user-id="110031">@Patrick Massot</span> and <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> which I do not know how to fix. I would be grateful if they could kindly offer their assistance.</p>

#### [ Kenny Lau (Jan 26 2019 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Module%20refactor/near/156905982):
<p>I am rebasing it to the current mathlib; I would appreciate it if we could pause merging module-related stuff for a while (that would include my recent <a href="https://github.com/leanprover/mathlib/issues/625" target="_blank" title="https://github.com/leanprover/mathlib/issues/625">#625</a>)</p>

#### [ Kenny Lau (Jan 26 2019 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Module%20refactor/near/156905983):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> do you think this is a good time?</p>

#### [ Mario Carneiro (Jan 26 2019 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Module%20refactor/near/156906025):
<p>sure, what's the status?</p>

#### [ Kenny Lau (Jan 26 2019 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Module%20refactor/near/156906039):
<p>expect a PR in 10 minutes</p>

#### [ Kenny Lau (Jan 26 2019 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Module%20refactor/near/156906149):
<p>make that 1 hour</p>

#### [ Kenny Lau (Jan 26 2019 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Module%20refactor/near/156907809):
<p><a href="https://github.com/leanprover/mathlib/issues/626" target="_blank" title="https://github.com/leanprover/mathlib/issues/626">#626</a></p>

#### [ Patrick Massot (Jan 26 2019 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Module%20refactor/near/156916951):
<p>I'm sorry I didn't find the right time to think about this thread. <span class="user-mention" data-user-id="110064">@Kenny Lau</span> did you manage to fix your normed space issue?</p>

#### [ Kenny Lau (Jan 26 2019 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Module%20refactor/near/156919459):
<p>yes</p>

#### [ Kenny Lau (Jan 26 2019 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Module%20refactor/near/156922108):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <code>pi_instance</code> fails for <code>smul</code> because <code>pi_instance</code> tries to apply <code>has_scalar.smul</code> but it fails because the instance cannot be synthesized</p>

#### [ Kenny Lau (Jan 26 2019 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Module%20refactor/near/156928213):
<ul>
<li>The first parameters of <code>has_scalar</code>, <code>semimodule</code>, <code>module</code>, and <code>vector_space</code> are no longer <code>out_param</code>s. The implication is that the base ring will have to be inferred either from being provided explicitly or from context.</li>
<li>The base ring of linear maps are now specified via <code>β →ₗ[α] γ</code>, alongside the original notation <code>β →ₗ γ</code>. A similar notation has been introduced for tensor products.</li>
<li>The base ring in some definitions/theorems are made explicit.</li>
</ul>

#### [ Kenny Lau (Jan 26 2019 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Module%20refactor/near/156928216):
<p>do you guys have any suggestions / objections?</p>

#### [ Kenny Lau (Jan 26 2019 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Module%20refactor/near/156928481):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Kevin Buzzard (Jan 26 2019 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Module%20refactor/near/156939434):
<p>In real life one often sees phrases like "<span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span>-linear maps from <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>M</mi></mrow><annotation encoding="application/x-tex">M</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">M</span></span></span></span> to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>N</mi></mrow><annotation encoding="application/x-tex">N</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">N</span></span></span></span>" so I'm very happy. I live in a world where one often can consider both <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span>-linear and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span>-linear maps between two modules.</p>

#### [ Kenny Lau (Jan 26 2019 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Module%20refactor/near/156942441):
<blockquote>
<p>I am rebasing it to the current mathlib; I would appreciate it if we could pause merging module-related stuff for a while (that would include my recent <a href="https://github.com/leanprover/mathlib/issues/625" target="_blank" title="https://github.com/leanprover/mathlib/issues/625">#625</a>)</p>
</blockquote>
<p><a href="#narrow/stream/113488-general/topic/Module.20refactor/near/156905982" title="#narrow/stream/113488-general/topic/Module.20refactor/near/156905982">Kenny Lau, 2019 Jan 26 03:41 (UTC)</a> <span aria-label="point up" class="emoji emoji-1f446" role="img" title="point up">:point_up:</span> </p>
<p>I hope I didn't start a one-month module hiatus</p>


{% endraw %}
