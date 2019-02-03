---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/19492Definitionalreduction.html
---

## Stream: [general](index.html)
### Topic: [Definitional reduction](19492Definitionalreduction.html)

---


{% raw %}
#### [ Moses Schönfinkel (Jun 04 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitional%20reduction/near/127532389):
<p>If I can <code>#eval f a b</code> to <code>tt</code>, should I make sure that <code>example : f a b = tt</code>is <code>rfl</code>? In my case, <code>b = g a</code> and <code>g</code> seems to be naughty enough for Lean being to unwilling to expand everything. (<code>f a a = tt</code> is indeed <code>rfl</code>)</p>

#### [ Simon Hudon (Jun 04 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitional%20reduction/near/127540799):
<p>This may be a case where you suffer from the fact that definitional equality is not transitive.</p>

#### [ Moses Schönfinkel (Jun 05 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitional%20reduction/near/127618197):
<p>Let's suppose <code>#reduce f x</code> evaluates to <code>tt</code>. Is there a general easy way to prove <code>example : f x = tt</code> if <code>rfl</code> doesn't get the job done (probably due to non-transitive defeq)?</p>

#### [ Mario Carneiro (Jun 05 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitional%20reduction/near/127618259):
<p>If <code>#reduce</code> works, then <code>rfl</code> should also</p>

#### [ Moses Schönfinkel (Jun 05 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitional%20reduction/near/127618290):
<p>Would there by any difference between <code>#eval</code> and <code>#reduce</code>?</p>

#### [ Mario Carneiro (Jun 05 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitional%20reduction/near/127618298):
<p>yes, the same statement doesn't hold if you use <code>#eval</code></p>

#### [ Mario Carneiro (Jun 05 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitional%20reduction/near/127618356):
<p>there are some terms that <code>#eval</code> can evaluate which <code>#reduce</code> gets stuck on due to axioms like <code>propext</code></p>

#### [ Moses Schönfinkel (Jun 05 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitional%20reduction/near/127618595):
<p>I would love to at least try <code>#reduce</code> but deterministic timeout is making it somewhat impossible. I am pretty sure everything I use is fairly computable tho. Should I just write a tactic that unfolds everything explicitly until <code>refl</code> or should I try to find a way to make the whole thing <code>rfl</code>? (In the case where <code>#eval f x</code> yields <code>tt</code> but <code>f x = tt</code> is not <code>rfl</code>.)</p>


{% endraw %}
