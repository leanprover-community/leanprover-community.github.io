---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/92286dumpexprtocontext.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [dump expr to context](https://leanprover-community.github.io/archive/113489newmembers/92286dumpexprtocontext.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Nov 24 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dump%20expr%20to%20context/near/148282282):
<p>Is there a way to dump an expr to the context?</p>

#### [ Rob Lewis (Nov 24 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dump%20expr%20to%20context/near/148282927):
<p>What do you mean?</p>

#### [ Rob Lewis (Nov 24 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dump%20expr%20to%20context/near/148282942):
<p><code>tactic.pose</code>?</p>

#### [ Kenny Lau (Nov 24 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dump%20expr%20to%20context/near/148286561):
<p><span class="user-mention" data-user-id="110596">@Rob Lewis</span> that dumps the evaluated expression to the context; I want the unevaluated expression as an <code>expr</code> itself</p>

#### [ Kevin Buzzard (Nov 24 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dump%20expr%20to%20context/near/148286627):
<p>You should learn to ask better questions Kenny.</p>

#### [ Rob Lewis (Nov 24 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dump%20expr%20to%20context/near/148290574):
<p>You want a tactic that adds a local hypothesis of type <code>expr</code>, defined to be some particular <code>expr</code> that you have? Could you explain what you're trying to do? I kind of doubt this is the way to do it.</p>

#### [ Chris Hughes (Nov 26 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/dump%20expr%20to%20context/near/148359542):
<p>Can't you just use pose and give it <code> `(e) </code>, where <code>e : expr</code>?</p>


{% endraw %}
