---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53958metareduceanexpr.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [[meta] reduce an expr](https://leanprover-community.github.io/archive/113488general/53958metareduceanexpr.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Zesen Qian (Aug 11 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bmeta%5D%20reduce%20an%20expr/near/131968299):
<p>So I have an <code>expr</code> of the form <code>not a</code>, can I evaluate this expr further? because <code>not</code> is defined as <code>\lam a, (a -&gt; false)</code>.</p>

#### [ Zesen Qian (Aug 11 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bmeta%5D%20reduce%20an%20expr/near/131968352):
<p><code>a</code> is of type <code>Prop</code>, BTW.</p>

#### [ Simon Hudon (Aug 11 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bmeta%5D%20reduce%20an%20expr/near/131968459):
<p>When you say evaluate, do you mean simplify? if so, you can find rules about <code>not</code> in <code>logic.basic</code> (mathlib) and <code>init.logic</code> (core), then you can call <code>simp [...]</code> with those rules your expression.</p>

#### [ Zesen Qian (Aug 11 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bmeta%5D%20reduce%20an%20expr/near/131968478):
<p>hmm, is it possible to do it without explicitly refering to the def of <code>not</code>?</p>

#### [ Simon Hudon (Aug 11 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bmeta%5D%20reduce%20an%20expr/near/131968606):
<p>I'm not following you. My <code>simp</code> expression only lists lemmas to use with your reduction.</p>

#### [ Zesen Qian (Aug 11 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bmeta%5D%20reduce%20an%20expr/near/131968653):
<p>I see what you are saying, thank you.</p>

#### [ Zesen Qian (Aug 17 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bmeta%5D%20reduce%20an%20expr/near/132324576):
<p>(deleted)</p>


{% endraw %}
