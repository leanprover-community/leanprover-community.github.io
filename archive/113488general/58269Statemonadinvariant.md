---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58269Statemonadinvariant.html
---

## Stream: [general](index.html)
### Topic: [State monad invariant](58269Statemonadinvariant.html)

---


{% raw %}
#### [ Nicholas Scheel (Jul 17 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/State%20monad%20invariant/near/129815515):
<p>I been wondering if there’s a way to encode invariants on monadic state computations in Lean, such that every update to the state must preserve those invariants? I haven’t actually make use of monads in a DTT language before, but it seems like a good way to verify systems.</p>
<p>Maybe the two ways would be to build a new state monad with a proof term on the state ... wait I suppose that’s the same as using psigma for state, right?</p>
<p><code>verifiedStateChange {s : Type} {p : s -&gt; Prop} (s0 : s) (p0 : p s0) : psigma p</code></p>
<p>Or working to verify that each building block preserves the invariant ...</p>
<p>Has anyone done this before? Are there examples out there?</p>

#### [ Sebastian Ullrich (Jul 17 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/State%20monad%20invariant/near/129815890):
<p>The preferred style for program verification in Lean and similar systems seems to be to separate programs and proofs as much as possible. But if you wanted to, you could use <code>state_t</code> with a <code>subtype</code> (which is equivalent to a <code>psigma</code> into <code>Prop</code>), yes.</p>


{% endraw %}
