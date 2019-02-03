---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68526typeresizing.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [type resizing](https://leanprover-community.github.io/archive/113488general/68526typeresizing.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Jun 01 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20resizing/near/127424550):
<p>Suppose I have a type <code>α : Type (u+1)</code> and I know <code>∃ β : Type u, nonempty (β ≃ α)</code>. Is there a "canonical" (= without choice, I guess?) way to obtain a type <code>α' : Type u</code> and an equivalence <code>α ≃ α'</code>?</p>

#### [ Simon Hudon (Jun 01 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20resizing/near/127424655):
<p>I think you would be able to prove the axiom of choice if you had that</p>

#### [ Simon Hudon (Jun 01 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20resizing/near/127424744):
<p>Sorry, I take it back, you could pick <code>α</code> and <code>α ≃ α'</code> as the identity equivalence</p>

#### [ Mario Carneiro (Jun 01 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20resizing/near/127425203):
<p>You could use <code>ordinal</code> to give it a kind of canonicity, but that doesn't really avoid choice, it's nonconstructive all over the place.</p>

#### [ Mario Carneiro (Jun 01 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20resizing/near/127425253):
<p>Also that doesn't provide the equiv itself, just a proof of existence; only the type is canonical</p>


{% endraw %}
