---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29680refinementofpartitions.html
---

## Stream: [general](index.html)
### Topic: [refinement of partitions](29680refinementofpartitions.html)

---


{% raw %}
#### [ Kenny Lau (Apr 18 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refinement%20of%20partitions/near/125224068):
<p>what are the existing lemmas related to refinement of partitions, i.e. the idea that if there are two partitions of a list, then there is a partition that refines both?</p>

#### [ Mario Carneiro (Apr 18 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refinement%20of%20partitions/near/125224340):
<p>What do you mean by partition?</p>

#### [ Kenny Lau (Apr 18 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refinement%20of%20partitions/near/125224380):
<p>preimage of <code>list.join</code></p>

#### [ Mario Carneiro (Apr 18 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refinement%20of%20partitions/near/125224546):
<p>It seems a bit trivial, since there is a maximal partition</p>

#### [ Kenny Lau (Apr 18 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refinement%20of%20partitions/near/125224593):
<p>well there's a minimal refinement</p>

#### [ Mario Carneiro (Apr 18 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refinement%20of%20partitions/near/125224606):
<p>I don't think the subpartition relation exists in mathlib, but you could prove it's a lattice</p>


{% endraw %}
