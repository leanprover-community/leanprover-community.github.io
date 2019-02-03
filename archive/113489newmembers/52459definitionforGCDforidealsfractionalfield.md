---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/52459definitionforGCDforidealsfractionalfield.html
---

## Stream: [new members](index.html)
### Topic: [definition for GCD for ideals, fractional field](52459definitionforGCDforidealsfractionalfield.html)

---


{% raw %}
#### [ Aditya Agarwal (Jan 29 2019 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/definition%20for%20GCD%20for%20ideals%2C%20fractional%20field/near/157078442):
<p>Is the fractional field for an arbitrary integral domain defined anywhere in mathlib?<br>
I see that localization is defined, which I guess would be the way to define a fractional field if it isn't already present. </p>
<p>Also, is the ideal definition of GCD, i.e. <code>gcd(I) = the smallest Principal Ideal containing I</code> present in Lean?</p>

#### [ Patrick Massot (Jan 29 2019 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/definition%20for%20GCD%20for%20ideals%2C%20fractional%20field/near/157088306):
<p><a href="https://github.com/leanprover/mathlib/blob/042c290dac25b5f1c77255f1039fae301774d6cf/src/ring_theory/localization.lean#L161" target="_blank" title="https://github.com/leanprover/mathlib/blob/042c290dac25b5f1c77255f1039fae301774d6cf/src/ring_theory/localization.lean#L161">https://github.com/leanprover/mathlib/blob/042c290dac25b5f1c77255f1039fae301774d6cf/src/ring_theory/localization.lean#L161</a></p>

#### [ Aditya Agarwal (Jan 29 2019 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/definition%20for%20GCD%20for%20ideals%2C%20fractional%20field/near/157088406):
<p>Thanks! Somehow I missed that one while grepping for quotient <span aria-label="upside down" class="emoji emoji-1f643" role="img" title="upside down">:upside_down:</span></p>


{% endraw %}
