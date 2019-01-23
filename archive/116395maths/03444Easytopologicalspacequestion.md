---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/03444Easytopologicalspacequestion.html
---

## Stream: [maths](index.html)
### Topic: [Easy topological space question](03444Easytopologicalspacequestion.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507196):
I've been struggling on this one for about an hour :-/ I have a topological space X and an open set U and a  basis B for the topology. I have x in U, and I simply want to find V in B with x in V and V in U.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507203):
I wanted to use `mem_nhds_of_is_topological_basis`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507210):
`lemma  mem_nhds_of_is_topological_basis {a : α} {s : set α} {b : set (set α)}
(hb : is_topological_basis b) : s ∈ (nhds a).sets ↔ ∃t∈b, a ∈ t ∧ t ⊆ s :=...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507211):
but I am now sucked into some nonsense regarding filters

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507250):
So I would be done if I could prove that for U open and x in U, `U ∈ (nhds x).sets`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507252):
which should be trivial

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507261):
use `mem_nhds_sets`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507300):
no suggestions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507303):
it's in `analysis.topology.topological_space`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507308):
oh but it's not topological_space.mem_nhds_sets :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507365):
works :-) Thanks! What's that doing in the root namespace?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507619):
`nhds` is in the root namespace, so so are its lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507622):
Why is anything non-trivial in the root namespace?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507624):
Won't there be trouble ahead?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507629):
I import some topology module and all of a sudden there's extra stuff in the root namespace? I thought that that was some sort of disaster in CS

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507631):
Isn't that exactly why python tells you not to do crazy `import *` sort of things?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507670):
But here you can't even avoid it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507741):
Many basic structures are in the root namespace. But moving things around is not too painful, so we can adjust later if it becomes a problem

