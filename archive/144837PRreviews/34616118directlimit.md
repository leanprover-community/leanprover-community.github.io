---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/34616118directlimit.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#118 direct limit](https://leanprover-community.github.io/archive/144837PRreviews/34616118directlimit.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Oct 14 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791634):
<p>This is a can of worms. If we define a directed order to be one such that for every x and y there is z with x&lt;=z and y&lt;=z, then you can't define (x,a) + (y,b) computably, because you only have the fact that such <code>z</code> exists. So originally I defined a directed order to be one with a supremum function where <code>le_sup_left</code> and <code>le_sup_right</code> hold, but I don't require <code>sup_le</code>. But this generated much backlash, because people don't want it to be a function, but just an existential.</p>

#### [ Kenny Lau (Oct 14 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791641):
<p>I'm not sure as to how this issue can be resolved.</p>

#### [ Mario Carneiro (Oct 14 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791696):
<p>You can actually define those sorts of things computably</p>

#### [ Mario Carneiro (Oct 14 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791721):
<p>the idea is to use partial functions to keep track of how many of the indices are still valid for use, and which are invalidated by going out of range</p>

#### [ Kenny Lau (Oct 14 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791769):
<p>Could you explain it more? I don't understand what you mean by partial functions.</p>

#### [ Mario Carneiro (Oct 14 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791774):
<p>actually I need a primer on the direct limit first</p>

#### [ Mario Carneiro (Oct 14 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791779):
<p>what's the mathematician's definition?</p>

#### [ Kenny Lau (Oct 14 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791859):
<p><a href="https://stacks.math.columbia.edu/tag/04AX" target="_blank" title="https://stacks.math.columbia.edu/tag/04AX">https://stacks.math.columbia.edu/tag/04AX</a></p>

#### [ Mario Carneiro (Oct 14 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791879):
<p>do you want to work with filtered categories or posets?</p>

#### [ Kenny Lau (Oct 14 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791881):
<p>posets.</p>

#### [ Kenny Lau (Oct 14 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791885):
<p>But I can only find this version in stacks</p>

#### [ Kenny Lau (Oct 14 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791934):
<p>ah I can refer you to Atiyah Macdonald</p>

#### [ Kenny Lau (Oct 14 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135791963):
<p>Exercise 2.14, on PP.32-33</p>

#### [ Kenny Lau (Oct 14 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135792016):
<p><a href="/user_uploads/3121/PALFqY5aEbdKO93gwajVDoTz/2018-10-14-1.png" target="_blank" title="2018-10-14-1.png">2018-10-14-1.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/PALFqY5aEbdKO93gwajVDoTz/2018-10-14-1.png" target="_blank" title="2018-10-14-1.png"><img src="/user_uploads/3121/PALFqY5aEbdKO93gwajVDoTz/2018-10-14-1.png"></a></div>

#### [ Mario Carneiro (Oct 14 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135792045):
<p>wait, isn't that definition already perfectly constructive?</p>

#### [ Kenny Lau (Oct 14 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135792092):
<p>aha</p>

#### [ Kenny Lau (Oct 14 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135792093):
<p>the direct sum construction</p>

#### [ Kenny Lau (Oct 14 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135792095):
<p>ah that's the same as what you mean by finset</p>

#### [ Kenny Lau (Oct 14 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135792097):
<p>I finally understand why people use direct sum rather than union</p>

#### [ Kenny Lau (Oct 14 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135792098):
<p>thanks</p>

#### [ Kenny Lau (Oct 14 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135792109):
<p>issue resolved</p>

#### [ Kenny Lau (Oct 14 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135792426):
<p>oh well in this case this needs direct sum which needs dfinsupp which needs to wait for the module refactoring</p>

#### [ Kenny Lau (Oct 14 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23118%20direct%20limit/near/135792429):
<p>so I re-bury this PR.</p>


{% endraw %}
