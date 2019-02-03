---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04670obtain.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [obtain](https://leanprover-community.github.io/archive/113488general/04670obtain.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Nov 09 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/obtain/near/147351059):
<p>I just realised there is <code>obtain</code>:<br>
<a href="https://github.com/leanprover/mathlib/search?q=obtain&amp;unscoped_q=obtain" target="_blank" title="https://github.com/leanprover/mathlib/search?q=obtain&amp;unscoped_q=obtain">https://github.com/leanprover/mathlib/search?q=obtain&amp;unscoped_q=obtain</a></p>

#### [ Johan Commelin (Nov 09 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/obtain/near/147351108):
<p>I have not yet figured out what it does.</p>

#### [ Bryan Gin-ge Chen (Nov 09 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/obtain/near/147351132):
<p>I think I looked it up before and I concluded it was a lean 2 thing?</p>

#### [ Mario Carneiro (Nov 09 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/obtain/near/147351875):
<p>it is a lean 2 thing. <code>obtain x h, from expr, expr'</code> is the lean 2 way of writing <code>let &lt;x, h&gt; := expr in expr'</code>, at least when <code>expr</code> has exists type. I forget how general it is</p>

#### [ Mario Carneiro (Nov 09 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/obtain/near/147351938):
<p>the style guide also uses <code>take</code>, which is no longer a keyword and is the same as <code>λ</code></p>

#### [ Johan Commelin (Nov 09 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/obtain/near/147351993):
<p>Ok, thanks for explaining!</p>

#### [ Floris van Doorn (Nov 09 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/obtain/near/147352250):
<p><code>obtain</code> used to work on all inductive types with a single constructor. It was the way to do <code>cases</code> in term mode.</p>


{% endraw %}
