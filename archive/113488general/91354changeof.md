---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91354changeof.html
---

## Stream: [general](index.html)
### Topic: [change of ^](91354changeof.html)

---


{% raw %}
#### [ Kevin Buzzard (Apr 06 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/change%20of%20%5E/near/124717957):
<p>Are there any general tips for how to fix up files which no longer compile because of changes to <code>^</code>? I have files which start <code>local  infix ` ^ ` := monoid.pow</code>, and for x and y in a comm_semiring <code> (x + y) ^ 0 = x ^ 0 * y ^ 0</code> used to be solved by simp and now does not seem to be.</p>

#### [ Kevin Buzzard (Apr 06 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/change%20of%20%5E/near/124717960):
<p>I should say that I'm looking at <span class="user-mention" data-user-id="110044">@Chris Hughes</span> 's code here so I might not have got this 100 percent right</p>

#### [ Kevin Buzzard (Apr 06 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/change%20of%20%5E/near/124718005):
<p>but basically our stacks project is quite broken now I upgraded to the current nightly</p>

#### [ Chris Hughes (Apr 06 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/change%20of%20%5E/near/124719712):
<p><code>simp [pow_succ, pow_zero]</code>?</p>


{% endraw %}
