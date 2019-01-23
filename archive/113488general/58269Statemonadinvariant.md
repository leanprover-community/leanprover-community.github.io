---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58269Statemonadinvariant.html
---

## Stream: [general](index.html)
### Topic: [State monad invariant](58269Statemonadinvariant.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (Jul 17 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/State%20monad%20invariant/near/129815515):
I been wondering if there’s a way to encode invariants on monadic state computations in Lean, such that every update to the state must preserve those invariants? I haven’t actually make use of monads in a DTT language before, but it seems like a good way to verify systems.

Maybe the two ways would be to build a new state monad with a proof term on the state ... wait I suppose that’s the same as using psigma for state, right?

`verifiedStateChange {s : Type} {p : s -> Prop} (s0 : s) (p0 : p s0) : psigma p`

Or working to verify that each building block preserves the invariant ...

Has anyone done this before? Are there examples out there?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jul 17 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/State%20monad%20invariant/near/129815890):
The preferred style for program verification in Lean and similar systems seems to be to separate programs and proofs as much as possible. But if you wanted to, you could use `state_t` with a `subtype` (which is equivalent to a `psigma` into `Prop`), yes.


{% endraw %}
