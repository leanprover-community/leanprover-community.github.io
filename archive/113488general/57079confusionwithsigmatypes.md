---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57079confusionwithsigmatypes.html
---

## Stream: [general](index.html)
### Topic: [confusion with sigma types](57079confusionwithsigmatypes.html)

---


{% raw %}
#### [ Scott Morrison (Sep 22 2018 at 05:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134419058):
<p>Oops... oversimplified my example.</p>

#### [ Scott Morrison (Sep 22 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134419121):
<div class="codehilite"><pre><span></span>def f (n : ℕ) : Type := { l : list ℕ // l.length = n }

def foo : Σ n ≥ 5, f n := sorry
def foo&#39; : Σ n : ℕ, Σ H : n ≥ 5, f n := sorry
</pre></div>

#### [ Scott Morrison (Sep 22 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134419163):
<p>both <code>foo</code> and <code>foo'</code>error with </p>
<div class="codehilite"><pre><span></span>type mismatch at application
  Σ (H : n ≥ 5), f n
term
  λ (H : n ≥ 5), f n
has type
  n ≥ 5 → Type : Type 1
but is expected to have type
  ?m_1 → Type : Type (max ? 1)
</pre></div>

#### [ Scott Morrison (Sep 22 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134419164):
<p>what am I doing wrong?</p>

#### [ Scott Morrison (Sep 22 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134419170):
<p>Can you just not index sigma types by Props?!</p>

#### [ Scott Morrison (Sep 22 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134419171):
<p>ugh.</p>

#### [ Mario Carneiro (Sep 22 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134419236):
<p>use <code>Σ'</code> or <code>subtype</code></p>

#### [ Scott Morrison (Sep 22 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134419775):
<p>Thanks.</p>

#### [ Simon Hudon (Sep 22 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134420363):
<p>Does <code>subtype</code> do anything that <code>Σ'</code> doesn't do?</p>

#### [ Mario Carneiro (Sep 22 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134420404):
<p>no, except have easier universe constraints</p>

#### [ Simon Hudon (Sep 22 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134420439):
<p>Could it benefit from a <code>unit</code> / <code>punit</code> approach?</p>

#### [ Mario Carneiro (Sep 22 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134421471):
<p>Huh? It is a <code>unit</code>/<code>punit</code> approach. I mean it's even called <code>psigma</code></p>

#### [ Simon Hudon (Sep 22 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/confusion%20with%20sigma%20types/near/134421513):
<p>Right but what happened with <code>unit</code> is that it became a synonym for <code>punit.{0}</code></p>


{% endraw %}
