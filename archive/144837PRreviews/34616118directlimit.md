---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/34616118directlimit.html
---

## Stream: [PR reviews](index.html)
### Topic: [#118 direct limit](34616118directlimit.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791634):
This is a can of worms. If we define a directed order to be one such that for every x and y there is z with x<=z and y<=z, then you can't define (x,a) + (y,b) computably, because you only have the fact that such `z` exists. So originally I defined a directed order to be one with a supremum function where `le_sup_left` and `le_sup_right` hold, but I don't require `sup_le`. But this generated much backlash, because people don't want it to be a function, but just an existential.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791641):
I'm not sure as to how this issue can be resolved.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791696):
You can actually define those sorts of things computably

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791721):
the idea is to use partial functions to keep track of how many of the indices are still valid for use, and which are invalidated by going out of range

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791769):
Could you explain it more? I don't understand what you mean by partial functions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791774):
actually I need a primer on the direct limit first

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791779):
what's the mathematician's definition?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791859):
https://stacks.math.columbia.edu/tag/04AX

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791879):
do you want to work with filtered categories or posets?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791881):
posets.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791885):
But I can only find this version in stacks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791934):
ah I can refer you to Atiyah Macdonald

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791963):
Exercise 2.14, on PP.32-33

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135792016):
[2018-10-14-1.png](/user_uploads/3121/PALFqY5aEbdKO93gwajVDoTz/2018-10-14-1.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135792045):
wait, isn't that definition already perfectly constructive?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135792092):
aha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135792093):
the direct sum construction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135792095):
ah that's the same as what you mean by finset

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135792097):
I finally understand why people use direct sum rather than union

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135792098):
thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135792109):
issue resolved

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135792426):
oh well in this case this needs direct sum which needs dfinsupp which needs to wait for the module refactoring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135792429):
so I re-bury this PR.


{% endraw %}
