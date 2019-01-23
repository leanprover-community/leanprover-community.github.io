---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/90517484miscellaneoustopology.html
---

## Stream: [PR reviews](index.html)
### Topic: [#484 miscellaneous topology](90517484miscellaneoustopology.html)

---


{% raw %}
#### [ Sebastien Gouezel (Dec 09 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23484%20miscellaneous%20topology/near/151228688):
I have a lot of new material to add on top of #484, especially on the Hausdorff distance but I think the main interest for the community would be all the missing lemmas I had to add to the library while developping the Hausdorff distance. However, it makes no sense to PR it while #484 (and #464) are not integrated. Is there something I could do to help the process?

#### [ Patrick Massot (Dec 09 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23484%20miscellaneous%20topology/near/151234264):
I agree it would be nice to merge this and add more stuff. @**Sebastien Gouezel** would you mind pushing this to the community repository so that I could try some  stylistic improvements? You could revert anything you don't like. @**Mario Carneiro** could you make sure Sébastien has push access to the community repository?

#### [ Patrick Massot (Dec 09 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23484%20miscellaneous%20topology/near/151234314):
Also, I think that, once this will be merged, I'll probably try to reorganize files in this topology directory which is a mess (I'm working again on uniform spaces)

#### [ Patrick Massot (Dec 09 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23484%20miscellaneous%20topology/near/151234715):
Is it accepted mathlib style to use all those `have ..., begin ... end` instead of curly brackets?

#### [ Sebastien Gouezel (Dec 09 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23484%20miscellaneous%20topology/near/151235986):
```quote
@**Sebastien Gouezel** would you mind pushing this to the community repository so that I could try some  stylistic improvements?
```
 Should be done, if my git almost-nonexisting-skills did not betray me.

#### [ Sebastien Gouezel (Dec 09 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23484%20miscellaneous%20topology/near/151236184):
```quote
Is it accepted mathlib style to use all those `have ..., begin ... end` instead of curly brackets?
```
My impression is that curly brackets are for the case where there are several goals and you want to solve them one by one, separating them explicitly. While begin...end is for proof blocks in general.

#### [ Johannes Hölzl (Dec 10 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23484%20miscellaneous%20topology/near/151259207):
Hi @**Sebastien Gouezel** , the lectures end this week, I hope I find some time to review & merge your PRs


{% endraw %}
