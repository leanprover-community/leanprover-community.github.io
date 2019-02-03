---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83984funextxrfl.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [funext $ λ x, rfl](https://leanprover-community.github.io/archive/113488general/83984funextxrfl.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Apr 02 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124521378):
<p>conjecture: everything that can be proven using <code>funext $ λ x, rfl</code> can be proven using <code>rfl</code></p>

#### [ Mario Carneiro (Apr 02 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124521441):
<p>that's correct (modulo funny business regarding algorithmic equality not really being definitional equality)</p>

#### [ Kenny Lau (Apr 02 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124521443):
<p>could you expand on your parentheses</p>

#### [ Mario Carneiro (Apr 02 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124521482):
<p>Sometimes lean doesn't know when to eta expand stuff</p>

#### [ Kenny Lau (Apr 02 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124521492):
<p>could you provide an example</p>

#### [ Mario Carneiro (Apr 02 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124521603):
<div class="codehilite"><pre><span></span>def foo : true = true → plift true := @eq.rec Prop true (λ p, plift true) ⟨trivial⟩ true
def bar : true = true → plift true := @eq.rec Prop true (λ p, plift p) ⟨trivial⟩ true
example : foo = bar := funext $ λ x, rfl
example : foo = bar := rfl
</pre></div>

#### [ Kenny Lau (Apr 02 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124521611):
<p>ah, that funny <code>rec</code> business</p>

#### [ Patrick Massot (Apr 02 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124521612):
<p>Mario, aren't you sleeping?</p>

#### [ Kenny Lau (Apr 02 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124521613):
<p>LOL</p>

#### [ Kevin Buzzard (Apr 02 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523564):
<p>I found myself writing this yesterday:</p>

#### [ Kevin Buzzard (Apr 02 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523566):
<div class="codehilite"><pre><span></span>Hid :=  λ U OU,funext (λ x,subtype.eq rfl),
Hcomp :=  λ U V W OU OV OW HUV HVW,funext (λ x, subtype.eq rfl)
</pre></div>

#### [ Kevin Buzzard (Apr 02 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523568):
<p>and I couldn't move the rfl</p>

#### [ Kenny Lau (Apr 02 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523572):
<p><code>subtype.eq rfl</code> cannot be replaced by <code>rfl</code></p>

#### [ Kevin Buzzard (Apr 02 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523573):
<p>and I could understand why <code>subtype.eq</code> wasn't a simp lemma</p>

#### [ Kenny Lau (Apr 02 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523579):
<p>well it's just <code>congr</code></p>

#### [ Kevin Buzzard (Apr 02 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523580):
<p>because it's <code> a1.val = a2.val → a1 = a2 </code></p>

#### [ Kevin Buzzard (Apr 02 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523581):
<p>which doesn't look great for simp</p>

#### [ Kevin Buzzard (Apr 02 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523582):
<p>but then I found</p>

#### [ Kevin Buzzard (Apr 02 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523584):
<p><code>subtype.mk_eq_mk</code></p>

#### [ Kevin Buzzard (Apr 02 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523626):
<p>which is an iff and is marked as a simp lemma</p>

#### [ Kevin Buzzard (Apr 02 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funext%20%24%20%CE%BB%20x%2C%20rfl/near/124523635):
<p>so I was hopeful that <code>by simp</code> would work, but I couldn't get it to</p>


{% endraw %}
