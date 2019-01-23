---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20537Whatsgoodnotationforconvergence.html
---

## Stream: [general](index.html)
### Topic: [What's good notation for convergence?](20537Whatsgoodnotationforconvergence.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jan-David Salchow (Jan 15 2019 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20good%20notation%20for%20convergence%3F/near/155162064):
To avoid introducing constants, @**Johannes Hölzl** asked me to change

```lean
/-- The notion of convergence of sequences in topological spaces. -/
def converges_to (x : ℕ → X) (limit : X) : Prop :=
∀ U : set X, limit ∈ U → is_open U → ∃ n0 : ℕ, ∀ n ≥ n0, (x n) ∈ U
```

(and a similar definition for convergence in metric spaces) into notation.

I'm struggling to find good notation. My first try was

```lean 
notation x `⟶t` limit := ∀ U : set X, limit ∈ U → is_open U → ∃ n0 : ℕ, ∀ n ≥ n0, (x n) ∈ U
```

but this only works for a fixed topological space X. Is there a way to determine the domain for (the sequence) x without using meta programming? Or is the price for using notation that you always have to specify sequence, limit, and domain?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 15 2019 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20good%20notation%20for%20convergence%3F/near/155162103):
Uh, no, more like: `notation x `⟶t` limit := tendsto x at_top (nhds limit)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 15 2019 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20good%20notation%20for%20convergence%3F/near/155162107):
never put a big term on the right of a `notation`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 15 2019 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20good%20notation%20for%20convergence%3F/near/155162167):
also the term we want to operate on should be using `tendsto` and then we have different views on `tendsto` telling us how to unfold tendsto into a concrete representation.
```lean
tendsto x at_top (nhds limit) <-> ∀ U : set X, limit ∈ U → is_open U → ∃ n0 : ℕ, ∀ n ≥ n0, (x n) ∈ U
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jan-David Salchow (Jan 15 2019 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20good%20notation%20for%20convergence%3F/near/155168674):
I see, that's better :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jan-David Salchow (Jan 15 2019 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20good%20notation%20for%20convergence%3F/near/155168742):
The difference between equality and iff is a propext, why is it better to state it as an equality?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20good%20notation%20for%20convergence%3F/near/155170227):
usually it's stated as an iff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 15 2019 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20good%20notation%20for%20convergence%3F/near/155173772):
its an iff now ;-)

