---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08294orderonoptions.html
---

## Stream: [general](index.html)
### Topic: [order on options](08294orderonoptions.html)

---


{% raw %}
#### [ Simon Hudon (Sep 23 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134463860):
<p>Is there an instance of <code>decidable_linear_order</code> on <code>option</code> in Mathlib or core? I can't find one</p>

#### [ Kenny Lau (Sep 23 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464059):
<p>maybe <code>with_bot</code> has an order</p>

#### [ Simon Hudon (Sep 23 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464253):
<p>Yes, it does, thanks! Now I'm stuck for a new reason: I don't have a decidable linear order for <code>name</code> (from the tactics). I think I'll need to write some of those orders myself</p>

#### [ Mario Carneiro (Sep 23 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464258):
<p>There is an order on <code>name</code>, but it is <code>meta</code> and not an instance</p>

#### [ Kenny Lau (Sep 23 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464261):
<p>does it need to be meta?</p>

#### [ Mario Carneiro (Sep 23 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464262):
<p>no</p>

#### [ Simon Hudon (Sep 23 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464263):
<p>Actually, I only need a decidable relation, not an order</p>

#### [ Mario Carneiro (Sep 23 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464264):
<p>it has that already</p>

#### [ Mario Carneiro (Sep 23 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464301):
<div class="codehilite"><pre><span></span>meta instance : decidable_rel name.lt :=
λ a b, ordering.decidable_eq _ _

meta instance : has_lt name :=
⟨name.lt⟩
</pre></div>

#### [ Mario Carneiro (Sep 23 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464305):
<p>also relevant</p>
<div class="codehilite"><pre><span></span>/- Both cmp and lex_cmp are total orders, but lex_cmp implements a lexicographical order. -/
meta constant name.cmp : name → name → ordering
meta constant name.lex_cmp : name → name → ordering
</pre></div>

#### [ Simon Hudon (Sep 23 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464306):
<p>The issue is that the order relation and its decidability for <code>has_bot</code> are wrapped up in order instances</p>

#### [ Mario Carneiro (Sep 23 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464312):
<p>I guess we could generalize the definitions to <code>has_le</code> from <code>has_le</code> and <code>has_lt</code> from <code>has_lt</code>, without committing to any order properties</p>

#### [ Simon Hudon (Sep 23 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464353):
<p>Exactly</p>

#### [ Mario Carneiro (Sep 23 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464354):
<p>An easy fix is</p>
<div class="codehilite"><pre><span></span>meta instance : decidable_linear_order name :=
by refine {lt := (&lt;), le := \lam a b, \neg b &lt; a, ..}; exact undefined
</pre></div>

#### [ Simon Hudon (Sep 23 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464400):
<p>That's evil</p>

#### [ Kenny Lau (Sep 23 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464401):
<p>how exactly is <code>undefined</code> defined?</p>

#### [ Mario Carneiro (Sep 23 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464402):
<p><code>undefined := undefined</code>, effectively</p>

#### [ Kenny Lau (Sep 23 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464404):
<p>then how does VM know what to do with <code>#eval unchecked_cast</code>?</p>

#### [ Mario Carneiro (Sep 23 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464405):
<p>it's not really, because this causes loops instead of an error</p>

#### [ Simon Hudon (Sep 23 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464406):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> you may have a different opinion if you knew that this is for a mathlib PR</p>

#### [ Mario Carneiro (Sep 23 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464412):
<p><code>name</code> is basically meta. If a proof gets in your way, kill it</p>

#### [ Mario Carneiro (Sep 23 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464413):
<p>As long as it's actually true</p>

#### [ Mario Carneiro (Sep 23 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464453):
<p>or close enough to true that it doesn't matter</p>

#### [ Mario Carneiro (Sep 23 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464462):
<p>We could write <code>name.lt</code> non-meta, but I would want to see what is the performance hit first</p>

#### [ Simon Hudon (Sep 23 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464579):
<blockquote>
<p>or close enough to true that it doesn't matter</p>
</blockquote>
<p>I'm hesitant to agree because I see the type class constraint as a way the type system tells you to make sure you're satisfying assumptions and warning you when you break those assumptions. You write <code>undefined</code> and you lose all that information. Or rather, the type system tells you "all the assumptions are satisfied, no worries" when it might not be the case</p>

#### [ Mario Carneiro (Sep 23 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464780):
<p>This is true, but <code>meta</code> code doesn't have these guarantees anyway, except in a vague sense</p>

#### [ Mario Carneiro (Sep 23 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464784):
<p>A proof in <code>meta</code> land means something between "nothing at all" and "probably true"</p>

#### [ Simon Hudon (Sep 23 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464828):
<p>As a comparison, that used to be my opinion of software testing until I started grading software assignment of students who often didn't bother testing. Yes, tested software is still imperfect but untested is so much worse</p>

#### [ Mario Carneiro (Sep 23 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464829):
<p>right, which is why a meta proof can mean "probably true": the user had to make a conscious choice to either prove it or stub it out</p>

#### [ Mario Carneiro (Sep 23 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464878):
<p>I liken it to the "preconditions" requirements in programs in Haskell or Java. It says "don't fail this requirement or else" and no compile or run time checking</p>

#### [ Mario Carneiro (Sep 23 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464905):
<p>If you pass an order that is not linear to a function expecting one in the type, it's your fault if it breaks</p>

#### [ Simon Hudon (Sep 23 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20on%20options/near/134464920):
<p>I think comparing it the a quickcheck property would be closer to the truth, when you decide to write them, they nudge you in the right direction</p>


{% endraw %}
