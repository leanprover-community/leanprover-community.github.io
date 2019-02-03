---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/95204directedsets.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [directed sets](https://leanprover-community.github.io/archive/116395maths/95204directedsets.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Sep 01 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20sets/near/133171891):
<p>I was expecting to find a type <code>[directed α]</code>, to go along with <code>preorder</code>, <code>partial_order</code>, etc. Instead I can only find these:</p>
<div class="codehilite"><pre><span></span>/-- A family of elements of α is directed (with respect to a relation `≼` on α)
  if there is a member of the family `≼`-above any pair in the family.  -/
def directed {ι : Sort v} (f : ι → α) := ∀x y, ∃z, f z ≼ f x ∧ f z ≼ f y
/-- A subset of α is directed if there is an element of the set `≼`-above any
  pair of elements in the set. -/
def directed_on (s : set α) := ∀ (x ∈ s) (y ∈ s), ∃z ∈ s, z ≼ x ∧ z ≼ y
</pre></div>

#### [ Scott Morrison (Sep 01 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20sets/near/133171897):
<p>Am I just mean to use <code>directed (id α)</code>? It seems strange that the simplest thing isn't there.</p>

#### [ Reid Barton (Sep 01 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20sets/near/133173805):
<p>Beware also <code>directed</code> does not include nonempty</p>

#### [ Reid Barton (Sep 01 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20sets/near/133173849):
<p>AFAIK, those are the only directed set-related things in mathlib</p>


{% endraw %}
