---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/75408finsetimplementation.html
---

## Stream: [general](index.html)
### Topic: [finset implementation](75408finsetimplementation.html)

---


{% raw %}
#### [ Kenny Lau (Sep 08 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133565775):
<p>What is the advantage of implementing <code>finset</code> as it is now, over implementing it as <code>multiset</code> quotient by extensionality?</p>

#### [ Chris Hughes (Sep 08 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133566086):
<p>I'm guessing efficiency of computation, but also perhaps some of the proofs are easier, since the functions are more or less identical to the multiset versions. Something like <code>finset.sum</code> is harder to implement with finsets as a quotient.</p>

#### [ Kenny Lau (Sep 08 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133575013):
<p>But if we implement it as a quotient, then we can have <code>finset.union</code></p>

#### [ Chris Hughes (Sep 08 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133575019):
<p>Without <code>decidable_eq</code> you mean? Hooray. On the downside we'll need <code>decidable_eq</code> for <code>finset.sum</code> and <code>finset.card</code></p>

#### [ Simon Hudon (Sep 09 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586038):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> I think both implementations can be valuable. Find a different name and then you can provide that new implementation.</p>

#### [ Kenny Lau (Sep 09 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586041):
<p>great</p>

#### [ Kenny Lau (Sep 09 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586043):
<p>could you help me think of a name?</p>

#### [ Simon Hudon (Sep 09 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586089):
<p>One benefit of <code>finset</code>'s current implementation is in writing programs that are meant to be executed. Keeping the list minimal is more economical on memory.</p>

#### [ Simon Hudon (Sep 09 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586181):
<p>The most obvious candidate would be <code>finset'</code> but I'm not sure that it's good. We could go with variations on <code>finset</code> (like <code>finite_set</code>) but I think that's more confusing than anything else. How about <code>no_eq.finset</code>?</p>

#### [ Simon Hudon (Sep 09 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586195):
<p>The other alternative would be to change the name of the current implementation to <code>compact.finset</code> or <code>minimal.finset</code> or <code>efficient.finset</code></p>

#### [ Simon Hudon (Sep 09 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586247):
<p>I like your idea. Your kind of implementation makes a set that is easier to use as a monad and as a traversable collection.</p>

#### [ Mario Carneiro (Sep 09 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586291):
<p>I would suggest something like <code>qfinset</code> or <code>stacked_finset</code></p>

#### [ Mario Carneiro (Sep 09 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586293):
<p>I'm not seeing where the gains are though</p>

#### [ Kevin Buzzard (Sep 09 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586299):
<p>you can have union without decidable equality :-)</p>

#### [ Mario Carneiro (Sep 09 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586300):
<p>gain<em>s</em> plural</p>

#### [ Kevin Buzzard (Sep 09 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586301):
<p>:-)</p>

#### [ Kevin Buzzard (Sep 09 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586340):
<p>Presumably this means that the two definitions can't be proved to be equal without decidable equality?</p>

#### [ Mario Carneiro (Sep 09 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586342):
<p>For the most part anything you can do with a stacked finset you can also do with a multiset</p>

#### [ Mario Carneiro (Sep 09 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586354):
<p>There is a computable function <code>finset -&gt; qfinset</code> but the reverse is <code>erase_dup</code> which requires decidable eq</p>

#### [ Kevin Buzzard (Sep 09 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586356):
<p>gotcha</p>

#### [ Mario Carneiro (Sep 09 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586398):
<p>But all these functions already exist, between <code>finset</code> and <code>multiset</code></p>

#### [ Simon Hudon (Sep 09 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586470):
<p>I can see three reasons for using stacked sets. </p>
<p>1. you mean it to form a monad (or a similar kind of functor)<br>
2. you need it to be traversable<br>
3. you want to work with finite sets while using set equality directly without translating back and forth between set and multiset.</p>

#### [ Simon Hudon (Sep 09 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20implementation/near/133586519):
<p><code>qfinset</code> is then like <code>set</code>+ finiteness invariant, similarly to <code>multiset</code></p>


{% endraw %}
