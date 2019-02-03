---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57903inductionontwomultisets.html
---

## Stream: [general](index.html)
### Topic: [induction on two multisets](57903inductionontwomultisets.html)

---


{% raw %}
#### [ Kevin Buzzard (Jul 11 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456296):
<p>I am trying to define a function <code>multiset nat -&gt; multiset nat -&gt; nat</code>, by induction. If I have two multisets <code>C</code> and <code>L</code> and if I know the value of the function on all the pairs <code>(C-{x},L)</code>(with <code>x</code> in <code>C</code>)  and <code>(C,L-{y})</code> (with <code>y</code> in <code>L</code>) then I have a formula which will give me the value at <code>(C,L)</code>. The formula is not symmetric in <code>C</code> and <code>L</code>. The tool which the API gives me is</p>
<div class="codehilite"><pre><span></span>multiset.strong_induction_on :
  Π {α : Type u_1} {p : multiset α → Sort u_2} (s : multiset α),
    (Π (s : multiset α), (Π (t : multiset α), t &lt; s → p t) → p s) → p s
</pre></div>


<p>but I can't figure out how to use this directly.</p>

#### [ Mario Carneiro (Jul 11 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456360):
<p>You can do this by a nested induction using that function</p>

#### [ Kevin Buzzard (Jul 11 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456361):
<p>So I tried this</p>

#### [ Kevin Buzzard (Jul 11 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456408):
<p>but my interpretation of what you're saying is "define <code>f(C,L)</code> for <code>L</code> constant and <code>C</code> varying, by induction on <code>C</code>" and the problem is that the definition needs both <code>C</code> and <code>L</code> to move. What am I missing?</p>

#### [ Mario Carneiro (Jul 11 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456416):
<p>Define <code>f C L</code> for all <code>L</code> and fixed <code>C</code>, by induction on <code>C</code></p>

#### [ Mario Carneiro (Jul 11 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456461):
<p>In the IH we know <code>f (C-{x}) L'</code> for all <code>L'</code> and need to define <code>f C L</code></p>

#### [ Kevin Buzzard (Jul 11 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456465):
<p>To define <code>f C L</code> I need more</p>

#### [ Kevin Buzzard (Jul 11 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456466):
<p>I need <code>f C L'</code> for all <code>L'</code> smaller than <code>L</code></p>

#### [ Mario Carneiro (Jul 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456475):
<p>we do so by induction on <code>L</code>. Now the induction hypothesis gives us <code>f C (L-{y})</code> and we must define <code>f C L</code></p>

#### [ Kevin Buzzard (Jul 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456479):
<p>OK I'll take it from here.</p>

#### [ Kevin Buzzard (Jul 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456481):
<p>The reason I asked was that I was not 100% sure that the tools I had were enough. If you're confident that they are then I just need to work harder. Thanks for the tips.</p>

#### [ Mario Carneiro (Jul 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456486):
<p>it is two inductions</p>

#### [ Mario Carneiro (Jul 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456488):
<p>one inside the other</p>

#### [ Kevin Buzzard (Jul 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456489):
<p>Right.</p>

#### [ Kevin Buzzard (Jul 11 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456529):
<p>I'm a mathematician. I don't understand induction properly :-)</p>

#### [ Kevin Buzzard (Jul 11 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456530):
<p>We only do induction on nat in maths.</p>

#### [ Mario Carneiro (Jul 11 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456532):
<p>This can also be viewed as a well founded induction in lex order, first by <code>C</code> then <code>L</code></p>

#### [ Kevin Buzzard (Jul 11 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456533):
<p>This I know.</p>

#### [ Kevin Buzzard (Jul 11 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456535):
<p>But the only way I know to do a well-founded induction is on an inductive type.</p>

#### [ Mario Carneiro (Jul 11 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456542):
<p>and since <code>(C-{x},L)</code> and <code>(C,L-{y})</code> are both less in this order, this method should work</p>

#### [ Mario Carneiro (Jul 11 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456589):
<p>I guess an alternative to the <code>multiset.strong_induction_on</code> API is just to provide a proof that multiset <code>&lt;</code> is well founded and let you use the tools from the <code>well_founded</code> namespace</p>

#### [ Kevin Buzzard (Jul 11 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456591):
<p>I didn't even know that namespace existed!</p>

#### [ Mario Carneiro (Jul 11 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456606):
<p>That's what powers the <code>using_well_founded</code> equation compiler stuff</p>

#### [ Kevin Buzzard (Jul 11 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456609):
<p>The only time I've used well-founded stuff is when trying to persuade the equation compiler that my definition is sound.</p>

#### [ Kevin Buzzard (Jul 11 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456611):
<p>i.e. indirectly</p>

#### [ Mario Carneiro (Jul 11 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456615):
<p>Back in the old days we used <code>well_founded.fix</code> when we wanted to write a wf definition</p>

#### [ Mario Carneiro (Jul 11 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129456660):
<p>and it requires a proof that the relation du jour is well founded</p>

#### [ Andrew Ashworth (Jul 11 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129473610):
<p>I didn't get the memo that this method was passe</p>

#### [ Andrew Ashworth (Jul 11 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20on%20two%20multisets/near/129473764):
<p>Probably I need to get with the times :)</p>


{% endraw %}
