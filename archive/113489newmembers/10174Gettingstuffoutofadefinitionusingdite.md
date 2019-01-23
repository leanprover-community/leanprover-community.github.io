---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/10174Gettingstuffoutofadefinitionusingdite.html
---

## Stream: [new members](index.html)
### Topic: [Getting stuff out of a definition using dite](10174Gettingstuffoutofadefinitionusingdite.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alexandru-Andrei Bosinta (Nov 26 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Getting%20stuff%20out%20of%20a%20definition%20using%20dite/near/148336981):
How do I use a definition that uses dite? All my attempts of writing the definition, it's required arguments followed by a proof of the if condition failed, with Lean giving me an error like it had no idea what I was trying to do.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 26 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Getting%20stuff%20out%20of%20a%20definition%20using%20dite/near/148337033):
`dif_pos` / `dif_neg`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 26 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Getting%20stuff%20out%20of%20a%20definition%20using%20dite/near/148353486):
in tactic mode perhaps `split_ifs` can also help.


{% endraw %}
