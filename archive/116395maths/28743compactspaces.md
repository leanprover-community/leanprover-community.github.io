---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/28743compactspaces.html
---

## Stream: [maths](index.html)
### Topic: [compact spaces](28743compactspaces.html)

---


{% raw %}
#### [ Reid Barton (Sep 22 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20spaces/near/134451428):
I'm inclined to add the following class, following the naming scheme of `t2_space`, `separable_space`, etc.
```lean
structure compact_space {α : Type*} [topological_space α] :=
(compact_univ : compact (univ : set α))
```
Advantages: we can write a lot of instances, and various theorems have "$$X$$ compact" as a hypothesis, and it's not always possible or useful to generalize to "Let $$S$$ be a compact subset of $$X$$".

#### [ Reid Barton (Sep 22 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20spaces/near/134451430):
Any thoughts?

#### [ Kevin Buzzard (Sep 22 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20spaces/near/134452154):
My only comment was that ever since I saw the definition of compact I was surprised it applied to a subspace rather than the space. What is the advantage of the subset approach? It's not how mathematicians traditionally do it.

#### [ Mario Carneiro (Sep 23 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20spaces/near/134455015):
I agree. I don't think there is much advantage to working with subsets here, since you get exactly the right behavior with `compact_space s` with the subtype coercion


{% endraw %}
