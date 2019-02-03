---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08878fromtacticstoterms.html
---

## Stream: [general](index.html)
### Topic: [from tactics to terms](08878fromtacticstoterms.html)

---


{% raw %}
#### [ Johan Commelin (Aug 24 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20tactics%20to%20terms/near/132682307):
<p>Even though I'm beginning to understand a bit of the <code>meta</code>-world, I still don't fully comprehend the tactic monad. For example: is it possible to extract a concrete term from a <code>begin ... end</code>-block?</p>

#### [ Johan Commelin (Aug 24 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20tactics%20to%20terms/near/132696207):
<p>Ok, I found <code>format_result</code> in Ed's recent docs on <code>meta</code>.</p>

#### [ Johan Commelin (Aug 24 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20tactics%20to%20terms/near/132696477):
<p>The problem is that I don't see any output anywhere, when I plug it into some <code>begin ... end</code> block.</p>

#### [ Scott Morrison (Aug 24 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20tactics%20to%20terms/near/132697545):
<p>You'll need to <code>trace</code> it?</p>

#### [ Johan Commelin (Aug 24 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20tactics%20to%20terms/near/132697964):
<p>Hmm. Good idea. But <code>trace tactic.format_result</code> gives the error</p>
<div class="codehilite"><pre><span></span><span class="n">failed</span> <span class="n">to</span> <span class="n">synthesize</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">for</span>
<span class="err">⊢</span> <span class="n">has_to_tactic_format</span> <span class="o">(</span><span class="n">tactic</span> <span class="n">format</span><span class="o">)</span>
</pre></div>

#### [ Patrick Massot (Aug 24 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20tactics%20to%20terms/near/132698024):
<p>sounds ironic</p>

#### [ Kevin Buzzard (Aug 24 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20tactics%20to%20terms/near/132700521):
<p><code>trace_state</code> usually prints a trace.</p>

#### [ Sebastian Ullrich (Aug 24 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/from%20tactics%20to%20terms/near/132702583):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> See <code>tactic.trace_result</code></p>


{% endraw %}
