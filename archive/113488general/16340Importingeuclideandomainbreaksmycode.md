---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16340Importingeuclideandomainbreaksmycode.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Importing euclidean_domain  breaks my code](https://leanprover-community.github.io/archive/113488general/16340Importingeuclideandomainbreaksmycode.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (May 27 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Importing%20euclidean_domain%20%20breaks%20my%20code/near/127176176):
<p>For some reason importing euclidean domain breaks my code, and causes a deterministic timeout. The same problem happens if I try to import <code>algebra.euclidean_domain</code> into <code>linear_algebra.multivariate_polynomial</code>. What's happening?</p>

#### [ Chris Hughes (May 28 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Importing%20euclidean_domain%20%20breaks%20my%20code/near/127180205):
<p>Discovered a solution. Delete the unnecessary <code>decidable_equality</code> argument from the euclidean_domain class</p>


{% endraw %}
