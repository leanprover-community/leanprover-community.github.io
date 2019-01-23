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
Can I do `rcases` on `p \or false` and end up with one state where we know `p`?

#### [ Reid Barton (Oct 02 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rcases%20with%20false/near/135056934):
Well `rcases t with t'|⟨⟨⟩⟩` seems to work but I don't know if I would really advise it

#### [ Kenny Lau (Oct 02 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rcases%20with%20false/near/135057063):
would @**Mario Carneiro** advise it?

#### [ Simon Hudon (Oct 02 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rcases%20with%20false/near/135057253):
That looks like something I would do

#### [ Chris Hughes (Oct 02 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rcases%20with%20false/near/135058277):
I'm sure `or_false` is a lemma. Use that.

#### [ Kenny Lau (Oct 02 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rcases%20with%20false/near/135058486):
yes. but this is just a minimal example.

#### [ Mario Carneiro (Oct 03 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rcases%20with%20false/near/135071726):
I would advise it; if you search for that (with spaces around the `|` ) you will find me use it in several places


{% endraw %}
