---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/41600orderonfilter.html
---

## Stream: [new members](index.html)
### Topic: [order on filter](41600orderonfilter.html)

---


{% raw %}
#### [ Kenny Lau (Oct 09 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order%20on%20filter/near/135489142):
Why is the order on filter reverse inclusion instead of just inclusion?

#### [ Mario Carneiro (Oct 09 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order%20on%20filter/near/135489824):
@**Johannes Hölzl** will know. I +1 this question, it throws me off every time

#### [ Kevin Buzzard (Oct 09 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order%20on%20filter/near/135490958):
I just assumed it was because the set of subsets of X embeds into the set of filters on X via principal filters, and the smaller the subset the bigger the filter.

#### [ Kenny Lau (Oct 09 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order%20on%20filter/near/135491024):
interesting

#### [ Mario Carneiro (Oct 09 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order%20on%20filter/near/135491228):
Here is one way to look at it: the identity function is continuous on topologies when the topologies are `dom <= cod`. In other words, the poset of topologies is embedded in the category of topological spaces by the functor `T -> (X,T)`

#### [ Mario Carneiro (Oct 09 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order%20on%20filter/near/135491311):
If you try to do the same thing with filters, the replacement for "continuous" is `tendsto`, and in order to keep the `<=` relation going the same way we have to reverse the order of filters

#### [ Mario Carneiro (Oct 09 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order%20on%20filter/near/135491420):
That is, `tendsto id L1 L2` iff `L2 ⊆ L1`


{% endraw %}
