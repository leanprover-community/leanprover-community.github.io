---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/33174fixesagainstthelatestmathlib.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [fixes against the latest mathlib](https://leanprover-community.github.io/archive/113488general/33174fixesagainstthelatestmathlib.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Apr 08 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fixes%20against%20the%20latest%20mathlib/near/124799280):
<p>now there is a global <code>^</code> called <code>pow</code>, and now the type of <code>n</code> will not be inferred from <code>f^n</code> (you need to manually state that <code>n</code> is of type <code>nat</code>). In that case, <code>pow</code> unfolds to <code>monoid.pow</code>, which can be unfolded as before the latest version.</p>

#### [ Kevin Buzzard (Apr 08 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fixes%20against%20the%20latest%20mathlib/near/124799512):
<p>Are you talking about the nightly from the 6th?</p>

#### [ Kenny Lau (Apr 08 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fixes%20against%20the%20latest%20mathlib/near/124799513):
<p>right</p>

#### [ Chris Hughes (Apr 08 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fixes%20against%20the%20latest%20mathlib/near/124800387):
<p>So no more nat.pow?</p>

#### [ Kenny Lau (Apr 08 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fixes%20against%20the%20latest%20mathlib/near/124800392):
<p>I have not tested, but I believe Lean figures out whether you mean <code>monoid.pow</code> or <code>nat.pow</code></p>

#### [ Kenny Lau (Apr 08 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fixes%20against%20the%20latest%20mathlib/near/124800393):
<p>depending on the first argument</p>

#### [ Chris Hughes (Apr 08 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fixes%20against%20the%20latest%20mathlib/near/124804713):
<p>Getting rid of <code>local  infix </code> ^ <code> := monoid.pow</code> seems to help, so it uses <code>has_pow.pow</code> which is definitionally equal, but has rw lemmas.</p>


{% endraw %}
