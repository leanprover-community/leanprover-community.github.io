---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98683recname.html
---

## Stream: [general](index.html)
### Topic: [rec_name](98683recname.html)

---


{% raw %}
#### [ Jakob von Raumer (Mar 19 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_name/near/123916531):
<p>After adding an inductive type to the environment using <code>add_inductive</code>, I can use the <code>induction</code> tactic, but it doesn't return any useful case names... Can I solve this by defining <code>rec_name</code>?</p>

#### [ Sebastian Ullrich (Mar 19 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_name/near/123916665):
<p>Sounds like it: <a href="https://github.com/leanprover/lean/blob/master/library/init/meta/tactic.lean#L425-L426" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/meta/tactic.lean#L425-L426">https://github.com/leanprover/lean/blob/master/library/init/meta/tactic.lean#L425-L426</a></p>

#### [ Sebastian Ullrich (Mar 19 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_name/near/123916666):
<p>Good to know that <code>induction</code> works at all</p>

#### [ Jakob von Raumer (Mar 19 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_name/near/123917223):
<p>Yes, that's indeed a good thing. I don't even have to add the <code>using</code> clause...</p>

#### [ Sebastian Ullrich (Mar 19 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_name/near/123917266):
<p>Apparently you do, if you want nice case names :)</p>

#### [ Sebastian Ullrich (Mar 19 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_name/near/123917320):
<p>The alternative is to set the case names on your own, using a wrapper around the <code>induction</code> tactic</p>

#### [ Jakob von Raumer (Mar 19 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_name/near/123917471):
<p>I don't _really_ need the case names so far, but I'm kind of feeling that I don't have enough control over which case belongs to which constructor while the tactic is working on it...</p>


{% endraw %}
