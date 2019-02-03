---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/82737grouphom.html
---

## Stream: [maths](index.html)
### Topic: [group_hom](82737grouphom.html)

---


{% raw %}
#### [ Chris Hughes (Dec 12 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group_hom/near/151505639):
<p>Can we define <code>is_group_hom</code> to be <code>is_monoid_hom</code> and make it reducible? It would avoid cycles.</p>

#### [ Johan Commelin (Dec 12 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group_hom/near/151510233):
<p>I would like this too. Especially if we could fill in the condition <code>f 1 = 1</code> using some default argument or auto_param. (Because for groups, as opposed to monoid, you can derive this condition from the multiplicativity.)</p>

#### [ Johan Commelin (Dec 12 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group_hom/near/151510242):
<p>Whether it should be reducible, I don't know.</p>

#### [ Chris Hughes (Dec 12 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group_hom/near/151510669):
<p>If it's reducible then every  group hom is automatically a monoid hom and vice versa</p>


{% endraw %}
