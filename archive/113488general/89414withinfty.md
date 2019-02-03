---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89414withinfty.html
---

## Stream: [general](index.html)
### Topic: [with_infty](89414withinfty.html)

---


{% raw %}
#### [ Johan Commelin (Oct 08 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135383943):
<p>I am looking at Sebastien's PR for emetric spaces. And I'm wondering, we have <code>with_top</code>, <code>with_bot</code> and <code>with_zero</code>. Would it make sense to have <code>with_infty</code>, or is it not worth it?</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135383952):
<p>that's <code>with_top</code></p>

#### [ Johan Commelin (Oct 08 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135383993):
<p>I know. But why do we have <code>with_zero</code>?</p>

#### [ Johan Commelin (Oct 08 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135383994):
<p>It is just <code>with_bot</code>.</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135383999):
<p>I think there are some algebraic definitions on <code>with_top</code>, and they correspond to treating it like infinity</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135384003):
<p><code>with_zero</code> and <code>with_bot</code> are not the same on algebra stuff</p>

#### [ Johan Commelin (Oct 08 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135384004):
<p>I see</p>

#### [ Johan Commelin (Oct 08 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135384012):
<p>So if someone wants to use <code>∞</code> notation, they should just introduce it locally?</p>

#### [ Johan Commelin (Oct 08 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135384016):
<p>Because that might be nice...</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135384080):
<p>yes, <code>∞</code> is not a notation associated to any typeclass</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135384086):
<p>indeed I was thinking of eliminating it from <code>ennreal</code> in favor of top everywhere</p>

#### [ Johan Commelin (Oct 08 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135384152):
<p>Hmmm, I would vote for keeping the notation.</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135384210):
<p>I think I hit a dependency problem anyway</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135384216):
<p>but it's a local notation, use what you like</p>

#### [ Simon Hudon (Oct 08 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135416708):
<p>Do you ever add both a bottom and a top? In what order do you add them? Or do you build it as a <code>sum bool a</code>?</p>

#### [ Johannes Hölzl (Oct 10 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135555509):
<p>fyi: <code>∞</code> is only a local notation for top. <a href="https://github.com/leanprover/mathlib/blob/master/data/real/ennreal.lean#L19" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/data/real/ennreal.lean#L19">https://github.com/leanprover/mathlib/blob/master/data/real/ennreal.lean#L19</a></p>

#### [ Johannes Hölzl (Oct 10 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/with_infty/near/135555544):
<p>I don't think we currently have a case where we add a top and a bot. But we add top to structures which already have a bot, like ennreal, or enat.</p>


{% endraw %}
