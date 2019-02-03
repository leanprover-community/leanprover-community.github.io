---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/79835Linearmapsandmodulehomomorphisms.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Linear maps and module homomorphisms](https://leanprover-community.github.io/archive/116395maths/79835Linearmapsandmodulehomomorphisms.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (May 08 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Linear%20maps%20and%20module%20homomorphisms/near/126260883):
<p>In <code>algebra/module.lean</code> on line 78 there is <code>structure is_linear_map</code>. I have two questions:<br>
(1) Why is this not a class?<br>
(2) Would it make sense to call this <code>is_module_hom</code>? (For me that would be the 'expected' name.)</p>

#### [ Kevin Buzzard (May 08 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Linear%20maps%20and%20module%20homomorphisms/near/126261114):
<p>maps between algebraic structures are a relatively new thing in Lean and I guess people are still trying to decide whether they should be classes or not. <code>is_group_hom</code>was a <code>definition</code> a few weeks ago and is now a <code>class</code>.</p>

#### [ Johan Commelin (May 08 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Linear%20maps%20and%20module%20homomorphisms/near/126261184):
<p>Ok, that's good to know. To make another comment on terminology: I think it is funny that we write <code>[group G]</code> and <code>[is_group_hom f]</code>. I would expect <code>is_group</code> or <code>group_hom</code> for either of those.</p>

#### [ Johan Commelin (May 08 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Linear%20maps%20and%20module%20homomorphisms/near/126261186):
<p>But I guess this is also due to the organic growth...</p>

#### [ Johan Commelin (May 08 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Linear%20maps%20and%20module%20homomorphisms/near/126261195):
<p>Are proposals to "normalise" such conventions welcome? Or is this already in some pipeline?</p>

#### [ Johan Commelin (May 08 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Linear%20maps%20and%20module%20homomorphisms/near/126261204):
<p>On the other hand, I realise now that there is a real difference between homs and groups</p>

#### [ Johan Commelin (May 08 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Linear%20maps%20and%20module%20homomorphisms/near/126261247):
<p>A group gives you extra data, being a group_hom is merely a property</p>

#### [ Johan Commelin (May 08 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Linear%20maps%20and%20module%20homomorphisms/near/126261252):
<p>This is maybe reflected in the terminology</p>


{% endraw %}
