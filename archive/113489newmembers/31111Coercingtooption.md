---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/31111Coercingtooption.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Coercing to option](https://leanprover-community.github.io/archive/113489newmembers/31111Coercingtooption.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155204948):
<p>Where can I find lemmas about coercing to option (e.g. <code>ℕ</code> to <code>option ℕ</code>)? I want basic things like <code>↑(n - m) = ↑n - ↑m</code>.</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155204961):
<p>what does subtraction mean?</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155204982):
<p>I don't think option has a <code>has_sub</code> instance</p>

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205154):
<p>But option N does.</p>

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205221):
<p>Oh wait, you mean <code>↑n - ↑m</code> won't be defined at all.</p>

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205251):
<p>What about something like <code>1 + ↑(n - 1) = ↑n</code>? That's what I actually need to prove.</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205270):
<p>option doesn't have an add or 1 either</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205286):
<p>what are you doing?</p>

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205303):
<p>Degrees of polynomials.</p>

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205315):
<p>You can add degrees of polynomials, but they're defined via option.</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205329):
<p>Isn't it <code>with_bot N</code> or something?</p>

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205336):
<p>Yeah.</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205346):
<p>that's a different thing</p>

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205412):
<p>Ok, because <code>with_bot</code> has additional structure.</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205415):
<p><code>with_bot</code> has an addition, <code>option</code> doesn't</p>

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205416):
<p>But how do I coerce to <code>with_bot</code>?</p>

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205423):
<p>I mean, are there lemmas about it in mathlib?</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205548):
<p>I think you want <code>with_bot.coe_add</code></p>

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205551):
<p>Ah, I see.</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205560):
<p>the lemmas are in <code>algebra.ordered_group</code></p>

#### [ Mario Carneiro (Jan 15 2019 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205587):
<p>but if <code>n : nat</code> then <code>1 + \u(n - 1) = \u n</code> is false at 0</p>

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205616):
<p>Yeah, I have an <code>n &gt; 1</code> hypothesis, that's alright.</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205634):
<p>if you cases on <code>n</code> then the zero case is impossible and the succ case is by refl</p>

#### [ Mario Carneiro (Jan 15 2019 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205704):
<p>oh wait, not refl, you have to commute the 1+ first</p>

#### [ Kevin Buzzard (Jan 15 2019 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155206605):
<blockquote>
<p>that's a different thing</p>
</blockquote>
<p>It's a definitionally equal thing. Definitional equality is a subtle beast. At times you should just treat definitionally equal things as the same, but at other times you shouldn't, and this is one of those times. This came up today in my M1P1 talk. We tried <code>linarith</code> to finish the proof that any two limits of a sequence were equal, and it failed, because we had hypotheses of the form <code>l &lt; m -&gt; false</code>. When we changed them to the definitionally equal <code>\not (l &lt; m)</code> linarith suddenly worked! What is going on, I guess, is that linarith is looking at what "kind" of an expression it can see, and <code>l &lt; m -&gt; false</code> is "just some function" to linarith, whereas <code>\not (l &lt; m)</code> is "a linear inequality that I can use". Similarly type class inference for + is going to trigger on <code>with_bot nat</code> but perhaps not on <code>option nat</code> even though they're definitionally equal. I hope I've got this mostly right. These things might be definitionally equal, but they are different expressions so tactics or other bits of Lean might treat them in different ways. For unification they will be the same but for rewrites they won't. etc etc.</p>


{% endraw %}
