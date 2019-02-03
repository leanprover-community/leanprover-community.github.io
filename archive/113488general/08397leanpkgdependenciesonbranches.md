---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08397leanpkgdependenciesonbranches.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [leanpkg dependencies on branches](https://leanprover-community.github.io/archive/113488general/08397leanpkgdependenciesonbranches.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (May 13 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20dependencies%20on%20branches/near/126495443):
<p>I'd like to add a leanpkg dependency to a non-master branch of a github. Does anyone know how to do this?</p>

#### [ Simon Hudon (May 13 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20dependencies%20on%20branches/near/126508892):
<p>On github, get the commit hash of the head of that branch and paste it leanpkg.toml</p>

#### [ Scott Morrison (May 14 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20dependencies%20on%20branches/near/126513243):
<p>Okay -- I discovered the same thing in the meantime, but <code>leanpkg upgrade</code> then takes me off that branch back to master, which is not ideal, although certainly manageable.</p>


{% endraw %}
