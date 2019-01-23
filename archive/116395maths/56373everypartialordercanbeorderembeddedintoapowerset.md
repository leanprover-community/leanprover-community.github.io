---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/56373everypartialordercanbeorderembeddedintoapowerset.html
---

## Stream: [maths](index.html)
### Topic: [every partial order can be order-embedded into a powerset](56373everypartialordercanbeorderembeddedintoapowerset.html)

---


{% raw %}
#### [ Kenny Lau (Apr 27 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/every%20partial%20order%20can%20be%20order-embedded%20into%20a%20powerset/near/125781096):
```lean
section

variables {α : Type u} [partial_order α] (x y : α)

def partial_order.embed : set α :=
{ z | z ≤ x }

theorem partial_order.embed.injective : function.injective (@partial_order.embed α _) :=
λ x y hxy,
have H1 : x ∈ partial_order.embed y, from hxy ▸ le_refl _,
have H2 : y ∈ partial_order.embed x, from hxy.symm ▸ le_refl _,
le_antisymm H1 H2

theorem partial_order.embed.ord (H : x ≤ y) : partial_order.embed x ⊆ partial_order.embed y :=
λ z hz, le_trans hz H

end
```

#### [ Kenny Lau (Apr 27 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/every%20partial%20order%20can%20be%20order-embedded%20into%20a%20powerset/near/125781102):
is there a more compact version of the title using category language?

#### [ Kenny Lau (Apr 27 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/every%20partial%20order%20can%20be%20order-embedded%20into%20a%20powerset/near/125781113):
and I used all three properties of a partial order

#### [ Kenny Lau (Apr 27 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/every%20partial%20order%20can%20be%20order-embedded%20into%20a%20powerset/near/125781335):
```lean
def converse (r : α → α → Prop) (H : r ≼o ((⊆) : set β → set β → Prop)) : partial_order α :=
{ le := inv_image (⊆) H,
  le_refl := λ _, set.subset.refl _,
  le_trans := λ _ _ _, set.subset.trans,
  le_antisymm := λ _ _ H1 H2, H.1.2 $ set.subset.antisymm H1 H2 }
```

#### [ Kenny Lau (Apr 27 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/every%20partial%20order%20can%20be%20order-embedded%20into%20a%20powerset/near/125781342):
and the converse :P

#### [ Kenny Lau (Apr 27 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/every%20partial%20order%20can%20be%20order-embedded%20into%20a%20powerset/near/125781353):
wait, that's the wrong converse

#### [ Reid Barton (Apr 27 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/every%20partial%20order%20can%20be%20order-embedded%20into%20a%20powerset/near/125783616):
It's the enriched Yoneda lemma where the enriching category is the poset of truth values {false -> true}

#### [ Reid Barton (Apr 27 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/every%20partial%20order%20can%20be%20order-embedded%20into%20a%20powerset/near/125783685):
`{ z | z ≤ x }` is the characteristic feature of Yoneda things.

#### [ Reid Barton (Apr 27 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/every%20partial%20order%20can%20be%20order-embedded%20into%20a%20powerset/near/125783948):
I guess there's slightly more going on here because you said "embedded into a powerset" = all functions from \a to V = {false -> true}, while the Yoneda embedding lands in order-reversing maps \a to V, i.e., lower sets of \a.


{% endraw %}
