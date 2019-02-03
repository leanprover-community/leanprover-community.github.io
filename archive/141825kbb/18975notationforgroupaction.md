---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/141825kbb/18975notationforgroupaction.html
---

## Stream: [kbb](https://leanprover-community.github.io/archive/141825kbb/index.html)
### Topic: [notation for group action](https://leanprover-community.github.io/archive/141825kbb/18975notationforgroupaction.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Sep 14 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/notation%20for%20group%20action/near/133932189):
<p>I think we should just group actions an instance of <code>has_smul</code>. What do others think?</p>

#### [ Mario Carneiro (Sep 14 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/notation%20for%20group%20action/near/133932247):
<p>it <em>probably</em> won't cause problems</p>

#### [ Johan Commelin (Sep 14 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/notation%20for%20group%20action/near/133932291):
<p>And then we get <code>group_module G A</code> with an instance to <code>module (group_ring G) A</code> and we will have to versions of <code>has_smul</code> <span class="emoji emoji-1f631" title="scream">:scream:</span></p>

#### [ Johan Commelin (Sep 14 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/notation%20for%20group%20action/near/133933127):
<p>Ooo, I guess it just means we will always have to explicitly write the coercion <code>G → (group_ring G)</code> to distinguish which action we mean.</p>


{% endraw %}
