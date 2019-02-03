---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39506priorityoftypeclassinferences.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [priority of typeclass inferences](https://leanprover-community.github.io/archive/113488general/39506priorityoftypeclassinferences.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Apr 21 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125473385):
<p>If I proved <code>A.to_B</code> and <code>A.to_C</code> and <code>B.to_D</code> and <code>C.to_D</code>, when I want to coerce <code>A</code> to <code>D</code>, how does Lean judge which path to use?</p>

#### [ Mario Carneiro (Apr 21 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125473768):
<p>Unless you explicitly set priorities using <code>@[priority n]</code>, the highest priority goes to the last declared instance. So if it's looking for a <code>D</code> and <code>C.to_D</code> was declared second, it uses that and looks for a <code>C</code>, finding <code>A.to_C</code>.</p>
<p>That said, it is possible to end up with the other path if you perform a typeclass search before the second instance is declared, or if you compose typeclass proofs, so this is why I recommend <code>B.to_D (A.to_B inst)</code> be defeq to <code>C.to_D (A.to_C inst)</code> in this circumstance.</p>

#### [ Kenny Lau (Apr 21 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125473817):
<p>is it even possible to make them defeq?</p>

#### [ Mario Carneiro (Apr 21 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125473893):
<p>sure... most "forgetful functor" type instances will have this property</p>

#### [ Kenny Lau (Apr 21 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125473944):
<p>aha, my functors are usually free functors though</p>

#### [ Kenny Lau (Apr 21 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125473946):
<p>I'm making a free group ^^</p>

#### [ Mario Carneiro (Apr 21 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125473949):
<p>do you have a particular diamond in mind?</p>

#### [ Kenny Lau (Apr 21 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125474065):
<p>aha, I had one when I analyzed onote.repr wrongly</p>

#### [ Kenny Lau (Apr 21 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125474112):
<p>i.e. providing a constructive path that <code>nat.lt</code> is computably well-founded</p>

#### [ Mario Carneiro (Apr 21 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125474123):
<p>By the way if you are on a quest to remove <code>noncomputable</code> you should start with the <code>ordinal</code> file which contains tons of <code>noncomputable</code> things</p>

#### [ Kenny Lau (Apr 21 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125474124):
<p>you're right</p>

#### [ Mario Carneiro (Apr 21 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125474170):
<p>I think you will hit your head against some hard problems and realize it's impossible eventually, but feel free to try :)</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125505702):
<p>Kenny, did you follow the metric space / topological space story a couple of months ago?</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125505705):
<p>Patrick was horrified to find that the _definition_ of metric space was a structure which included the metric _and_ the topology!</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125505713):
<p>It turned out that it was because the mathlib people wanted the coercion from a metric space to a top space to be a forgetful functor!</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125505759):
<p>Now they have the clever solution of putting the topology as part of the structure, but auto-generating it from the metric :-)</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125505767):
<p><a href="https://github.com/kbuzzard/mathlib/blob/WIP_docs/docs/WIPs/type_class_inference.md" target="_blank" title="https://github.com/kbuzzard/mathlib/blob/WIP_docs/docs/WIPs/type_class_inference.md">https://github.com/kbuzzard/mathlib/blob/WIP_docs/docs/WIPs/type_class_inference.md</a></p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125505768):
<p>Unfinished notes</p>

#### [ Kevin Buzzard (Apr 21 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/priority%20of%20typeclass%20inferences/near/125505770):
<p>Maybe I should add something from this thread</p>


{% endraw %}
