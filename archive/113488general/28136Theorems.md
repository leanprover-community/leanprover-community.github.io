---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28136Theorems.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Theorems](https://leanprover-community.github.io/archive/113488general/28136Theorems.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Guillermo Barajas Ayuso (Aug 04 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Theorems/near/130894817):
<p>Hi guys do you know how types can somehow be theorems? E.g. strong_indefinite_description in classical.</p>

#### [ Mario Carneiro (Aug 04 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Theorems/near/130894929):
<p>There is nothing preventing you from marking a type as a theorem, or a prop as a def</p>

#### [ Mario Carneiro (Aug 04 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Theorems/near/130895079):
<p>Usually we stick to <code>theorem</code> or <code>lemma</code> for things in <code>Prop</code> and <code>def</code> for things in <code>Sort</code> or <code>Type</code>, though, for a few reasons. The VM will not generate code for <code>theorem</code>s, and this will affect downstream definitions as well, so that is one reason; it is not a problem with <code>strong_indefinite_description</code> because this theorem is not computable anyway. Also a <code>theorem</code> is never unfolded, which is almost never necessary for a <code>Prop</code> because of proof irrelevance but is often important for <code>def</code>s since we may want to prove theorems about the def later. Here it is not a problem in <code>strong_indefinite_description</code> because the definition is supposed to be arbitrary in its type, so unfolding should never be necessary.</p>

#### [ Guillermo Barajas Ayuso (Aug 05 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Theorems/near/130936748):
<p>Ok that makes sense, thanks a lot!</p>


{% endraw %}
