---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/61101simpausinghvssimpathsimph.html
---

## Stream: [general](index.html)
### Topic: [simpa using h vs simp at h, simp [h]](61101simpausinghvssimpathsimph.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Sep 17 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simpa%20using%20h%20vs%20simp%20at%20h%2C%20simp%20%5Bh%5D/near/134084181):
On a few occasions, I've found that `simp at h, simp [h]` works when `simpa using h` does not. I thought the latter was intended to replace the former. Is this not the case?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simpa%20using%20h%20vs%20simp%20at%20h%2C%20simp%20%5Bh%5D/near/134084418):
They are not equivalent. `simpa using h` is equivalent to `simp at h |-, exact h`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simpa%20using%20h%20vs%20simp%20at%20h%2C%20simp%20%5Bh%5D/near/134084429):
in particular, `simp at h, simp [h]` may use `h` to rewrite in subterms, while `simpa` is just preparing to match it directly against the goal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simpa%20using%20h%20vs%20simp%20at%20h%2C%20simp%20%5Bh%5D/near/134084491):
This makes `simpa` less powerful but more controlled, especially when quantifiers get involved

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Sep 17 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simpa%20using%20h%20vs%20simp%20at%20h%2C%20simp%20%5Bh%5D/near/134084497):
Ah, okay. Thanks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simpa%20using%20h%20vs%20simp%20at%20h%2C%20simp%20%5Bh%5D/near/134086319):
Sean -- do you fancy editing the simp docs to explain this? I never really feel on top of this subtlety so never feel equipped to change them to explain it. I am still at the stage where I just try random combinations of simp, simpa, simp!, `simp * at *` and just keep going until it works.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simpa%20using%20h%20vs%20simp%20at%20h%2C%20simp%20%5Bh%5D/near/134086363):
https://github.com/leanprover/mathlib/blob/master/docs/extras/simp.md

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simpa%20using%20h%20vs%20simp%20at%20h%2C%20simp%20%5Bh%5D/near/134086406):
Just edit the community one I guess

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Sep 17 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simpa%20using%20h%20vs%20simp%20at%20h%2C%20simp%20%5Bh%5D/near/134087022):
Hmm, I don't know. I'm just looking at that document for the first time. I don't find it very easy to follow for reference, and I wouldn't know where to put what. I think Mario answering Zulip questions in a document would be better. :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Sep 17 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simpa%20using%20h%20vs%20simp%20at%20h%2C%20simp%20%5Bh%5D/near/134101631):
To make matters even more interesting, I have a goal that isn't solved by `by simp at h, simp [h]` but is solved by `by simp at h; simp; exact h` or `by simp at h; simp [h] {contextual := tt}` or `λ x, by simpa using h x`. After `by simp at h; simp`, `h` and the goal look exactly the same (with `set_option pp.all true`). I'm not clear on why it can't be solved.


{% endraw %}
