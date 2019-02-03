---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/50998varioustostrings.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [various to_strings](https://leanprover-community.github.io/archive/113488general/50998varioustostrings.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Edward Ayers (Oct 01 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/various%20to_strings/near/134964035):
<p>Hi all, when should I use the following typeclasses to display information?<br>
- <code>has_repr</code><br>
- <code>has_to_string</code><br>
- <code>has_to_format</code><br>
- <code>has_to_tactic_format</code> -- the tactic version of <code>has_to_format</code>?<br>
In particular, why bother having both <code>has_repr</code> and <code>has_to_string</code>?<br>
Thanks!</p>

#### [ Sean Leather (Oct 01 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/various%20to_strings/near/134964119):
<p>Some background: <a href="https://github.com/leanprover/lean/issues/1664" target="_blank" title="https://github.com/leanprover/lean/issues/1664">https://github.com/leanprover/lean/issues/1664</a></p>

#### [ Edward Ayers (Oct 01 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/various%20to_strings/near/134964230):
<p>Ok, so they are exactly the same except with how they deal with chars and strings?</p>

#### [ Sean Leather (Oct 01 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/various%20to_strings/near/134964311):
<blockquote>
<p>Ok, so they are exactly the same except with how they deal with chars and strings?</p>
</blockquote>
<p>I suppose so. I haven't looked into it myself.</p>


{% endraw %}
