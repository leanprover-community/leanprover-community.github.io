---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/65833rcaseswithfalse.html
---

## Stream: [new members](index.html)
### Topic: [rcases with false](65833rcaseswithfalse.html)

---


{% raw %}
#### [ Kenny Lau (Oct 02 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rcases%20with%20false/near/135056202):
<p>Can I do <code>rcases</code> on <code>p \or false</code> and end up with one state where we know <code>p</code>?</p>

#### [ Reid Barton (Oct 02 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rcases%20with%20false/near/135056934):
<p>Well <code>rcases t with t'|⟨⟨⟩⟩</code> seems to work but I don't know if I would really advise it</p>

#### [ Kenny Lau (Oct 02 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rcases%20with%20false/near/135057063):
<p>would <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> advise it?</p>

#### [ Simon Hudon (Oct 02 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rcases%20with%20false/near/135057253):
<p>That looks like something I would do</p>

#### [ Chris Hughes (Oct 02 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rcases%20with%20false/near/135058277):
<p>I'm sure <code>or_false</code> is a lemma. Use that.</p>

#### [ Kenny Lau (Oct 02 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rcases%20with%20false/near/135058486):
<p>yes. but this is just a minimal example.</p>

#### [ Mario Carneiro (Oct 03 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rcases%20with%20false/near/135071726):
<p>I would advise it; if you search for that (with spaces around the <code>|</code> ) you will find me use it in several places</p>


{% endraw %}
