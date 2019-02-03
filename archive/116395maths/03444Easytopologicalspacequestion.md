---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/03444Easytopologicalspacequestion.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Easy topological space question](https://leanprover-community.github.io/archive/116395maths/03444Easytopologicalspacequestion.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 02 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507196):
<p>I've been struggling on this one for about an hour :-/ I have a topological space X and an open set U and a  basis B for the topology. I have x in U, and I simply want to find V in B with x in V and V in U.</p>

#### [ Kevin Buzzard (Apr 02 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507203):
<p>I wanted to use <code>mem_nhds_of_is_topological_basis</code></p>

#### [ Kevin Buzzard (Apr 02 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507210):
<p><code>lemma  mem_nhds_of_is_topological_basis {a : α} {s : set α} {b : set (set α)}
(hb : is_topological_basis b) : s ∈ (nhds a).sets ↔ ∃t∈b, a ∈ t ∧ t ⊆ s :=...</code></p>

#### [ Kevin Buzzard (Apr 02 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507211):
<p>but I am now sucked into some nonsense regarding filters</p>

#### [ Kevin Buzzard (Apr 02 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507250):
<p>So I would be done if I could prove that for U open and x in U, <code>U ∈ (nhds x).sets</code></p>

#### [ Kevin Buzzard (Apr 02 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507252):
<p>which should be trivial</p>

#### [ Mario Carneiro (Apr 02 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507261):
<p>use <code>mem_nhds_sets</code></p>

#### [ Kevin Buzzard (Apr 02 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507300):
<p>no suggestions</p>

#### [ Mario Carneiro (Apr 02 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507303):
<p>it's in <code>analysis.topology.topological_space</code></p>

#### [ Kevin Buzzard (Apr 02 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507308):
<p>oh but it's not topological_space.mem_nhds_sets :-)</p>

#### [ Kevin Buzzard (Apr 02 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507365):
<p>works :-) Thanks! What's that doing in the root namespace?</p>

#### [ Mario Carneiro (Apr 02 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507619):
<p><code>nhds</code> is in the root namespace, so so are its lemmas</p>

#### [ Kevin Buzzard (Apr 02 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507622):
<p>Why is anything non-trivial in the root namespace?</p>

#### [ Kevin Buzzard (Apr 02 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507624):
<p>Won't there be trouble ahead?</p>

#### [ Kevin Buzzard (Apr 02 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507629):
<p>I import some topology module and all of a sudden there's extra stuff in the root namespace? I thought that that was some sort of disaster in CS</p>

#### [ Kevin Buzzard (Apr 02 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507631):
<p>Isn't that exactly why python tells you not to do crazy <code>import *</code> sort of things?</p>

#### [ Kevin Buzzard (Apr 02 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507670):
<p>But here you can't even avoid it?</p>

#### [ Mario Carneiro (Apr 02 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Easy%20topological%20space%20question/near/124507741):
<p>Many basic structures are in the root namespace. But moving things around is not too painful, so we can adjust later if it becomes a problem</p>


{% endraw %}
