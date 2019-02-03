---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/61101simpausinghvssimpathsimph.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [simpa using h vs simp at h, simp [h]](https://leanprover-community.github.io/archive/113488general/61101simpausinghvssimpathsimph.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Sep 17 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simpa%20using%20h%20vs%20simp%20at%20h%2C%20simp%20%5Bh%5D/near/134084181):
<p>On a few occasions, I've found that <code>simp at h, simp [h]</code> works when <code>simpa using h</code> does not. I thought the latter was intended to replace the former. Is this not the case?</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simpa%20using%20h%20vs%20simp%20at%20h%2C%20simp%20%5Bh%5D/near/134084418):
<p>They are not equivalent. <code>simpa using h</code> is equivalent to <code>simp at h |-, exact h</code></p>

#### [ Mario Carneiro (Sep 17 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simpa%20using%20h%20vs%20simp%20at%20h%2C%20simp%20%5Bh%5D/near/134084429):
<p>in particular, <code>simp at h, simp [h]</code> may use <code>h</code> to rewrite in subterms, while <code>simpa</code> is just preparing to match it directly against the goal</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simpa%20using%20h%20vs%20simp%20at%20h%2C%20simp%20%5Bh%5D/near/134084491):
<p>This makes <code>simpa</code> less powerful but more controlled, especially when quantifiers get involved</p>

#### [ Sean Leather (Sep 17 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simpa%20using%20h%20vs%20simp%20at%20h%2C%20simp%20%5Bh%5D/near/134084497):
<p>Ah, okay. Thanks.</p>

#### [ Kevin Buzzard (Sep 17 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simpa%20using%20h%20vs%20simp%20at%20h%2C%20simp%20%5Bh%5D/near/134086319):
<p>Sean -- do you fancy editing the simp docs to explain this? I never really feel on top of this subtlety so never feel equipped to change them to explain it. I am still at the stage where I just try random combinations of simp, simpa, simp!, <code>simp * at *</code> and just keep going until it works.</p>

#### [ Kevin Buzzard (Sep 17 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simpa%20using%20h%20vs%20simp%20at%20h%2C%20simp%20%5Bh%5D/near/134086363):
<p><a href="https://github.com/leanprover/mathlib/blob/master/docs/extras/simp.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/extras/simp.md">https://github.com/leanprover/mathlib/blob/master/docs/extras/simp.md</a></p>

#### [ Kevin Buzzard (Sep 17 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simpa%20using%20h%20vs%20simp%20at%20h%2C%20simp%20%5Bh%5D/near/134086406):
<p>Just edit the community one I guess</p>

#### [ Sean Leather (Sep 17 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simpa%20using%20h%20vs%20simp%20at%20h%2C%20simp%20%5Bh%5D/near/134087022):
<p>Hmm, I don't know. I'm just looking at that document for the first time. I don't find it very easy to follow for reference, and I wouldn't know where to put what. I think Mario answering Zulip questions in a document would be better. <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Sean Leather (Sep 17 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simpa%20using%20h%20vs%20simp%20at%20h%2C%20simp%20%5Bh%5D/near/134101631):
<p>To make matters even more interesting, I have a goal that isn't solved by <code>by simp at h, simp [h]</code> but is solved by <code>by simp at h; simp; exact h</code> or <code>by simp at h; simp [h] {contextual := tt}</code> or <code>λ x, by simpa using h x</code>. After <code>by simp at h; simp</code>, <code>h</code> and the goal look exactly the same (with <code>set_option pp.all true</code>). I'm not clear on why it can't be solved.</p>


{% endraw %}
