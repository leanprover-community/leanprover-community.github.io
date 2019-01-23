---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/95204directedsets.html
---

## Stream: [maths](index.html)
### Topic: [directed sets](95204directedsets.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 01 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20sets/near/133171891):
I was expecting to find a type `[directed α]`, to go along with `preorder`, `partial_order`, etc. Instead I can only find these:

```
/-- A family of elements of α is directed (with respect to a relation `≼` on α)
  if there is a member of the family `≼`-above any pair in the family.  -/
def directed {ι : Sort v} (f : ι → α) := ∀x y, ∃z, f z ≼ f x ∧ f z ≼ f y
/-- A subset of α is directed if there is an element of the set `≼`-above any
  pair of elements in the set. -/
def directed_on (s : set α) := ∀ (x ∈ s) (y ∈ s), ∃z ∈ s, z ≼ x ∧ z ≼ y
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 01 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20sets/near/133171897):
Am I just mean to use `directed (id α)`? It seems strange that the simplest thing isn't there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 01 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20sets/near/133173805):
Beware also `directed` does not include nonempty

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 01 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20sets/near/133173849):
AFAIK, those are the only directed set-related things in mathlib


{% endraw %}
