---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/32457evaluatingproofs.html
---

## Stream: [general](index.html)
### Topic: [evaluating proofs?](32457evaluatingproofs.html)

---


{% raw %}
#### [ Kenny Lau (Dec 12 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495074):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I think you said that it is possible to evaluate proofs... do you have an example? can we also break proof irrelevance? maybe have an unsound but computable <code>non-classical.some</code>?</p>

#### [ Mario Carneiro (Dec 12 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495093):
<p>the axiom of choice is definitely nonconstructive</p>

#### [ Mario Carneiro (Dec 12 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495102):
<p>You can evaluate proofs by using <code>#reduce</code></p>

#### [ Kenny Lau (Dec 12 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495105):
<blockquote>
<p>the axiom of choice is definitely nonconstructive</p>
</blockquote>
<p>even unsound?</p>

#### [ Mario Carneiro (Dec 12 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495107):
<p>no...</p>

#### [ Mario Carneiro (Dec 12 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495151):
<p>wait, I don't think I understand what you are asking</p>

#### [ Mario Carneiro (Dec 12 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495165):
<p>it's easy to compute a value if you are allowed to be wrong</p>

#### [ Kenny Lau (Dec 12 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495173):
<p>so I want a function that <code>reduce</code>s to <code>0</code> when given the input <code>(⟨0, rfl⟩ : ∃ n, n = n)</code></p>

#### [ Mario Carneiro (Dec 12 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495179):
<p>Not in the VM</p>

#### [ Kenny Lau (Dec 12 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495180):
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="n">reduce</span> <span class="o">(</span><span class="bp">⟨</span><span class="mi">0</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">n</span><span class="o">,</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">n</span><span class="o">)</span> <span class="c1">-- Exists.intro 0 (eq.refl 0)</span>
</pre></div>

#### [ Kenny Lau (Dec 12 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495182):
<p>why not?</p>

#### [ Mario Carneiro (Dec 12 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495187):
<p>because that term has no representation in the VM</p>

#### [ Mario Carneiro (Dec 12 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495190):
<p>it is a neutral value, a "unit"</p>

#### [ Kenny Lau (Dec 12 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495232):
<p>so <code>reduce</code> is not VM?</p>

#### [ Mario Carneiro (Dec 12 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495233):
<p>no</p>

#### [ Mario Carneiro (Dec 12 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495235):
<p>it is kernel reduction</p>

#### [ Kenny Lau (Dec 12 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495236):
<p>interesting</p>


{% endraw %}
