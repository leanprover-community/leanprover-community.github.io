---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/70528introducingvariables.html
---

## Stream: [new members](index.html)
### Topic: [introducing variables](70528introducingvariables.html)

---


{% raw %}
#### [ Ali Sever (Jul 19 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/129956826):
<p>If I have a Prop that says <code>∃ a b c, p</code>, whats the quickest way of introducing a b c and p? In tactic mode, I have to use <code>cases</code> three times to obtain all of them.</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/129957010):
<p>mathlib has <code>rcases</code> for this</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/129957025):
<p><code>rcases h with ⟨a, b, c, hp⟩</code></p>

#### [ Mario Carneiro (Jul 19 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/129957121):
<p>there is also <code>rintro</code> for introducing and casing at the same time, <code>rintro ⟨a, b, c, hp⟩</code> takes a goal of the form <code>(∃ a b c, p) -&gt; q</code> and splits off the parts and has <code>q</code> as subgoal</p>

#### [ Ali Sever (Jul 19 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/129957266):
<p>Is there a similar thing for term mode?</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/129957292):
<p><code>let ⟨a, b, c, hp⟩ := h in ...</code> is the equivalent of <code>rcases</code> and <code>λ ⟨a, b, c, hp⟩,</code> is the equivalent of <code>rintro</code>. Neither of those require mathlib</p>

#### [ Ali Sever (Jul 21 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130049223):
<p>I have <code>def col (a b c : point) : Prop := B a b c ∨ B b c a ∨ B c a b</code>. I want to prove <code>col a b c ∧ (some other stuff) → col a' b' c'</code>. Depending on the cases of <code>col a b c</code>, all the proofs are the same. So can I name <code>{a, b, c} = {x, y, z}</code> such that <code>B x y z</code> is true. So that when I prove <code>B x' y' z'</code>,  I will have proven <code>col a' b' c'</code>?</p>

#### [ Mario Carneiro (Jul 21 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130049272):
<p>what is the relation between <code>x',y',z'</code> and <code>a',b',c'</code>?</p>

#### [ Mario Carneiro (Jul 21 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130049324):
<p>One option is to prove as a lemma/<code>have</code> something like <code>\forall x y z, B x y z ∧ (some other stuff) → B x' y' z'</code> (where presumably <code>x'</code> is a function of <code>x</code> or something), and then instantiate it three times for the final proof</p>

#### [ Ali Sever (Jul 21 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130049325):
<p>I can prove <code>B a b c → B a' b' c'</code> for any order of a,b and c. So if <code>x  = a</code>, <code>x' = a'</code>.</p>

#### [ Ali Sever (Jul 21 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130049374):
<p>Ah, and then when I do cases, I can just use <code>lemma _ _ _</code> and let lean guess the order.</p>

#### [ Mario Carneiro (Jul 21 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130049381):
<p>Depending on how often you need this, it might even be worth making a lemma to abstract this proof pattern</p>

#### [ Mario Carneiro (Jul 21 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130049389):
<p>By the way, from your two questions I have a pretty good idea what you are working on ;)</p>

#### [ Patrick Massot (Jul 21 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130050497):
<p><span class="user-mention" data-user-id="120256">@Ali Sever</span> Are you aware of <a href="http://geocoq.github.io/GeoCoq/" target="_blank" title="http://geocoq.github.io/GeoCoq/">http://geocoq.github.io/GeoCoq/</a>?</p>

#### [ Mario Carneiro (Jul 21 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130050501):
<p>wow that's a nice project page</p>

#### [ Patrick Massot (Jul 21 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130050605):
<p>Yes, mathlib could use a webdesigner</p>

#### [ Ali Sever (Jul 21 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130050654):
<p>Yes, I looked around and I found out they were using the same book I was. I don't know exactly how Coq works, but when I get better at lean, I hope to write some interesting tactics.</p>

#### [ Patrick Massot (Jul 21 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130050695):
<p>But the message for Ali was rather more: beware that formalizing elementary geometry can be a lifetime project, especially because of the kind of symmetry issues that appeared in your question. See in particular <a href="https://hal.inria.fr/hal-00989781v2" target="_blank" title="https://hal.inria.fr/hal-00989781v2">https://hal.inria.fr/hal-00989781v2</a></p>


{% endraw %}
