---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/12961subtypeinstance.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [subtype_instance](https://leanprover-community.github.io/archive/113488general/12961subtypeinstance.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Oct 15 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype_instance/near/135805972):
<p>I'm having trouble using <code>subtype_instance</code>.</p>
<p>With a state of </p>
<div class="codehilite"><pre><span></span>R S : examples.CommRing,
f g : R ⟶ S,
h : is_subring {r : ↥R | ⇑f r = ⇑g r}
⊢ comm_ring ↥{r : ↥R | ⇑f r = ⇑g r}
</pre></div>


<p>running <code>subtype_instance</code> reports:</p>
<div class="codehilite"><pre><span></span>assumption tactic failed
state:
R S : examples.CommRing,
f g : R ⟶ S,
h : is_subring {r : ↥R | ⇑f r = ⇑g r}
⊢ set ?m_1
</pre></div>


<p>Is this expected? I appreciate I may be asking too much from <code>subtype_instance</code> there.</p>

#### [ Mario Carneiro (Oct 15 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype_instance/near/135806058):
<p>isn't this a theorem?</p>

#### [ Mario Carneiro (Oct 15 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype_instance/near/135806102):
<p>A subring of a comm_ring yields a comm_ring</p>

#### [ Scott Morrison (Nov 09 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype_instance/near/147337331):
<p>Hi <span class="user-mention" data-user-id="110026">@Simon Hudon</span>, did you write <code>subtype_instance</code>? I think I need some help with it.</p>

#### [ Scott Morrison (Nov 09 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype_instance/near/147337936):
<p>Sorry, problem solved.</p>

#### [ Simon Hudon (Nov 09 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype_instance/near/147374270):
<p>Oh! I just saw that! What was the issue?</p>


{% endraw %}
