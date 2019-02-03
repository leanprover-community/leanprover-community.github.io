---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52145submodulespan.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [submodule.span](https://leanprover-community.github.io/archive/113488general/52145submodulespan.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ petercommand (Nov 18 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147901978):
<p>I am trying to understand submodule.span, why can the type of <code>Inf { p | s \sub p } </code> (set beta) be converted to <code>submodule \alpha \beta</code>? Thanks!</p>

#### [ petercommand (Nov 18 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147902039):
<p>is there an option to show this information?</p>

#### [ Mario Carneiro (Nov 18 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147902082):
<p>There is a coercion on <code>p</code> there</p>

#### [ Mario Carneiro (Nov 18 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147902089):
<p>it is the infimum (in the lattice of submodules) of all submodules that when converted to a set are supersets of <code>s</code></p>

#### [ Mario Carneiro (Nov 18 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147902129):
<p>Lean knows the inf is taken in submodules, and <code>p</code> is a submodule, because type inference is done from the outside in and the target type is a <code>submodule</code></p>

#### [ petercommand (Nov 18 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147902130):
<p>hmm, how can I know that there is a coercion on <code>p</code>?</p>

#### [ Mario Carneiro (Nov 18 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147902131):
<p>If you print it there will be an up arrow</p>

#### [ petercommand (Nov 18 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147902137):
<p>ah</p>

#### [ petercommand (Nov 18 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147902227):
<p>can I know which coercion is applied?</p>

#### [ petercommand (Nov 18 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147902234):
<p>like where the coercion is defined</p>

#### [ petercommand (Nov 18 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147902280):
<p>Ah, there is only one <code>submodule.has_coe</code> in submodule.lean</p>


{% endraw %}
