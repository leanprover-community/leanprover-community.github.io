---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/15510Letbindingefficiency.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Let binding efficiency](https://leanprover-community.github.io/archive/113488general/15510Letbindingefficiency.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Seul Baek (Dec 24 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446520):
<p>If a term <code>foo</code> appears multiple times in a definition in such a way that each occurrence of it will have to be normalized,  does the definition become more efficiently computable by using <code>let x := foo in</code> in the beginning? The assumption is that <code>x</code> will be structured in a way that forces (some) normalization with the let binding (e.g., if <code>foo : A × B</code>, then <code>let (a,b) := foo</code>).</p>

#### [ Mario Carneiro (Dec 24 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446627):
<p>yes, although lean does that sometimes on its own, during the common subexpression elimination pass</p>

#### [ Mario Carneiro (Dec 24 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446628):
<p>do you mean in the VM or the kernel?</p>

#### [ Mario Carneiro (Dec 24 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446634):
<p>Note that <code>let (a,b) := foo</code> is not a let binding at all, it is just notation for a recursor</p>

#### [ Seul Baek (Dec 24 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446693):
<p>I meant the kernel, although I'd be curious about the VM as well.</p>

#### [ Mario Carneiro (Dec 24 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446698):
<p>In the kernel, I am not positive but I would guess that it depends on how shared the expression object is in memory</p>

#### [ Mario Carneiro (Dec 24 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446700):
<p>using a let binding like that is a good way to make sure that the same expression object is used in each place</p>

#### [ Mario Carneiro (Dec 24 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446702):
<p>but there will be some overhead with unfolding it</p>

#### [ Mario Carneiro (Dec 24 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446745):
<p>The kernel caches the whnf operation, so it won't need to calculate it many times if it is asked for multiple times</p>

#### [ Mario Carneiro (Dec 24 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446751):
<p>but I'm not sure whether the same expression in different contexts can cause a problem (since this might mean renaming vars and unsharing)</p>

#### [ Seul Baek (Dec 24 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446851):
<p>The main downside I'm experiencing with <code>let</code> is that it doesn't play nice with the simplifier when I have to prove properties about definitions which include it (<code>_match_1</code> all over the place) and requires extra definitional lemmas for unfolding. So I was wondering if there are reasons to use it other than its concision.</p>

#### [ Seul Baek (Dec 24 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152446991):
<p>If <code>let (a,b) := foo</code> is not a let binding, is there something else I can do to normalize <code>foo</code> and bind it to fresh term(s)?</p>

#### [ Mario Carneiro (Dec 24 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152447329):
<p>like I said, it's just a recursor. If you don't like the <code>_match_1</code> stuff, you can use tactics instead to construct the term, which don't leave this junk in the term</p>

#### [ Mario Carneiro (Dec 24 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152447337):
<p>i.e. <code>by cases foo with a b; exact</code></p>

#### [ Mario Carneiro (Dec 24 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152447343):
<p>it's equivalent to writing <code>prod.rec</code> explicitly in the term</p>

#### [ Seul Baek (Dec 24 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Let%20binding%20efficiency/near/152447817):
<p>I see. Thanks!</p>


{% endraw %}
