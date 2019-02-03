---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/48521ringsandideals.html
---

## Stream: [maths](index.html)
### Topic: [rings and ideals](48521ringsandideals.html)

---


{% raw %}
#### [ Patrick Massot (Jul 21 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/rings%20and%20ideals/near/130050846):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> and <span class="user-mention" data-user-id="110044">@Chris Hughes</span> with the recent merge of <a href="https://github.com/leanprover/mathlib/pull/196" target="_blank" title="https://github.com/leanprover/mathlib/pull/196">PR196</a> how does current mathlib compare to <a href="https://github.com/leanprover/lean2/blob/master/library/theories/commutative_algebra/ideal.lean" target="_blank" title="https://github.com/leanprover/lean2/blob/master/library/theories/commutative_algebra/ideal.lean">Lean 2 lib</a>?</p>

#### [ Chris Hughes (Jul 21 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/rings%20and%20ideals/near/130064086):
<p>Is that a hint that I should work on ideals? I was delayed by type class problems, but now I've found a long term solution, so I can work on it properly.</p>

#### [ Mario Carneiro (Jul 21 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/rings%20and%20ideals/near/130064153):
<p>was the lean 2 ideals library significant?</p>

#### [ Chris Hughes (Jul 21 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/rings%20and%20ideals/near/130064270):
<p>Looking at it, although it's much longer than the ideals file in mathlib, a lot of it covers stuff that's already done for modules.</p>

#### [ Mario Carneiro (Jul 21 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/rings%20and%20ideals/near/130064286):
<p>aren't those easy then? I thought mathlib ideals were defined in terms of submodules, so it should just be a theorem application away</p>

#### [ Chris Hughes (Jul 21 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/rings%20and%20ideals/near/130064288):
<p>Exactly.</p>

#### [ Chris Hughes (Jul 21 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/rings%20and%20ideals/near/130064291):
<p>Is it even worth proving them specifically for ideals?</p>

#### [ Mario Carneiro (Jul 21 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/rings%20and%20ideals/near/130064337):
<p>It can be helpful to change the statement the way you need it, if it is going to be used in <code>rw</code> for example</p>

#### [ Mario Carneiro (Jul 21 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/rings%20and%20ideals/near/130064346):
<p>I have said before that the most important thing about many of the early files is the statements, not the proofs</p>


{% endraw %}
