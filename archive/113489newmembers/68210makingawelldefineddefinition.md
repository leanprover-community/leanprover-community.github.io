---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/68210makingawelldefineddefinition.html
---

## Stream: [new members](index.html)
### Topic: [making a well-defined definition](68210makingawelldefineddefinition.html)

---


{% raw %}
#### [ Ali Sever (Aug 05 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20a%20well-defined%20definition/near/130922260):
<p>I have two sets <code>A B</code> and I want to define <code>f A B = g A b</code>(another set) for some <code>b ∈ B</code>.  I have the fact that <code>∃ b, b ∈ B</code>, but I'm not allowed to use Exists.dcases_on. Also, how/when do I prove this is well-defined and doesn't depend on the choice of <code>b</code>?</p>

#### [ Chris Hughes (Aug 05 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20a%20well-defined%20definition/near/130923186):
<p>You can use <code>classical.some</code> in which case you don't have to prove that it's well defined. Alternatively, if the possible values for <code>B</code> form a partition, you could use quotients.</p>

#### [ Ali Sever (Aug 05 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20a%20well-defined%20definition/near/130923232):
<p>I can prove that every value gives the same result.</p>

#### [ Chris Hughes (Aug 05 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20a%20well-defined%20definition/near/130923365):
<p>Presumably then, it isn't defined or at least used on any sets, just sets that meet some criteria?</p>

#### [ Ali Sever (Aug 05 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20a%20well-defined%20definition/near/130923702):
<p>Yep, (lines)</p>

#### [ Chris Hughes (Aug 05 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20a%20well-defined%20definition/near/130923849):
<p>If you want it to be defined on the set you pretty much have to  use <code>classical.some</code></p>

#### [ Kevin Buzzard (Aug 05 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20a%20well-defined%20definition/near/130923850):
<p>You can't get data (the set) from a proof (the fact that there exists a b) constructively -- even if you can prove uniqueness results. I've been using <code>cases (classical.indefinite_description _ H) with b Hb</code> to get b out of the hypothesis H that b exists, recently, but I found a glitch with this idiom recently; it doesn't always do quite what I want it to. Might work here though.</p>

#### [ Kevin Buzzard (Aug 05 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20a%20well-defined%20definition/near/130923938):
<p>The problem is that if you imagine a function as a computer program, the proof that a number exists (like Waring's number G(3) in my Monday talk) doesn't give you the right to be able to compute it for free.</p>

#### [ Chris Hughes (Aug 05 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20a%20well-defined%20definition/near/130924046):
<p>A lot of the time when you know something exists, you can compute it however, because that's how you proved it exists. I'm guessing Ali might be in this situation.</p>

#### [ Ali Sever (Aug 05 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20a%20well-defined%20definition/near/130924053):
<p>I just want to use the existence to show the set is non-empty. I think I might have to define the thing I want in a different way, and show it's equal to what I wanted.</p>

#### [ Kevin Buzzard (Aug 05 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20a%20well-defined%20definition/near/130925602):
<p>Computing the set can't be done constructively, but I should think that proving it's non-empty might be possible. If your goal is the assertion that some set is non-empty then you'll be able to uses cases on the exists normally, because your goal is to prove a proposition, not to construct some data.</p>


{% endraw %}
