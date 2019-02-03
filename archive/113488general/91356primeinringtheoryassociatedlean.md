---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91356primeinringtheoryassociatedlean.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [prime in `ring_theory/associated.lean`](https://leanprover-community.github.io/archive/113488general/91356primeinringtheoryassociatedlean.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Nov 23 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148200980):
<p><code>ring_theory/associated.lean</code> defines </p>
<div class="codehilite"><pre><span></span>/-- prime element of a semiring -/
def prime [comm_semiring α] (p : α) : Prop :=
p ≠ 0 ∧ ¬ is_unit p ∧ (∀a b, p ∣ a * b → p ∣ a ∨ p ∣ b)
</pre></div>


<p>in the root namespace, which then causes clashes with <code>nat.prime</code> if you have <code>nat</code> open.</p>

#### [ Scott Morrison (Nov 23 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148200985):
<p>Could we rename or namespace this? <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>  introduced it <a href="https://github.com/leanprover/mathlib/commit/f2beca809321e92b1cb543c2bcac2b031754da43" target="_blank" title="https://github.com/leanprover/mathlib/commit/f2beca809321e92b1cb543c2bcac2b031754da43">here</a>.</p>

#### [ Chris Hughes (Nov 23 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148201039):
<p>We could just get rid of nat prime as well.</p>

#### [ Kenny Lau (Nov 23 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148201079):
<p>wat @_@</p>

#### [ Scott Morrison (Nov 23 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148201259):
<p>What do you mean, <span class="user-mention" data-user-id="110044">@Chris Hughes</span>?</p>

#### [ Chris Hughes (Nov 23 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148201315):
<p>Just get rid of <code>nat.prime</code> and use prime in its place. I just realized that currently nat.prime is basically <code>irreducible </code>, so this would be a non trivial redactor.</p>

#### [ Scott Morrison (Nov 23 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148201407):
<p>Oh, I see! That sounds both a good idea and ambitious. :-)</p>

#### [ Scott Morrison (Nov 23 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148201408):
<p>Is there a good fix in the meantime?</p>

#### [ Johan Commelin (Nov 23 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148209287):
<p>I would just call this one <code>ring.prime</code></p>

#### [ Mario Carneiro (Nov 23 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148209416):
<p>I'm okay with <code>ring.prime</code> if the kill nat.prime thing doesn't work</p>

#### [ Mario Carneiro (Nov 23 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prime%20in%20%60ring_theory/associated.lean%60/near/148209463):
<p>although I've already fixed some bugs caused by this in the library (adding <code>nat.prime</code> when <code>nat</code> was open), maybe they should be re-ambiguated if it lands?</p>


{% endraw %}
