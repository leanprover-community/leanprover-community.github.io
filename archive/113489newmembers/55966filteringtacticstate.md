---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/55966filteringtacticstate.html
---

## Stream: [new members](index.html)
### Topic: [filtering tactic state](55966filteringtacticstate.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 12 2019 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/filtering%20tactic%20state/near/154957016):
once in a blue moon I managed to accidentally discover a “filter” drop down menu in the tactic state which allowed me to remove the _ variables or just show the goal, and I have no idea how to see this drop down menu again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 12 2019 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/filtering%20tactic%20state/near/154957025):
is this a secret feature?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Jan 12 2019 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/filtering%20tactic%20state/near/154957848):
The dropdown will only appear if (1) you're in "Display Goal" mode (2) your cursor is inside a tactic mode block so that there's something to filter (3) you haven't replaced the array of filters in your extension settings with an empty array.

