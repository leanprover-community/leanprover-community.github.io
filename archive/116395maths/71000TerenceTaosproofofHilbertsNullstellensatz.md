---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/71000TerenceTaosproofofHilbertsNullstellensatz.html
---

## Stream: [maths](index.html)
### Topic: [Terence Tao's proof of Hilbert's Nullstellensatz](71000TerenceTaosproofofHilbertsNullstellensatz.html)

---


{% raw %}
#### [ Kenny Lau (May 15 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Terence%20Tao%27s%20proof%20of%20Hilbert%27s%20Nullstellensatz/near/126611223):
<p>In <a href="http://terrytao.wordpress.com/2007/11/26/hilberts-nullstellensatz/" target="_blank" title="http://terrytao.wordpress.com/2007/11/26/hilberts-nullstellensatz/">this post by Terence Tao</a>, he proved Hilbert's Nullstellensatz in a more elementary and computational manner. My question is: how constructive is this proof?</p>

#### [ Mario Carneiro (May 15 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Terence%20Tao%27s%20proof%20of%20Hilbert%27s%20Nullstellensatz/near/126611535):
<p>I believe it is constructive, but note:</p>
<blockquote>
<p>in an explicitly computable fashion (using only the operations of addition, subtraction, multiplication, division, and branching on whether a given field element is zero or non-zero)</p>
</blockquote>
<p>Of course "branching on whether a given field element is zero or non-zero" means he needs decidable equality for the base field, so the most obvious application, for the base field C, doesn't work without a bit of nonconstructive magic. However there are decidable algebraically closed fields; the algebraic numbers have decidable equality and are algebraically closed so would probably work with the proof.</p>


{% endraw %}
