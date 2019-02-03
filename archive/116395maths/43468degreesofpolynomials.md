---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/43468degreesofpolynomials.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [degrees of polynomials](https://leanprover-community.github.io/archive/116395maths/43468degreesofpolynomials.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Sep 07 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/degrees%20of%20polynomials/near/133505238):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> told me a while ago that the degree of a polynomial is a bit of a nightmare, because the zero polynomial has degree -1 or -infinity or something, and these are not nats. It seems that he went with <code>degree</code> into <code>with_bot nat</code> and <code>nat_degree</code> into <code>nat</code> (with nat_degree of 0 being 0). I am now faced with goals like</p>
<div class="codehilite"><pre><span></span>hf : ¬f = 0,
hg : ¬g = 0,
hd : nat_degree f &lt; nat_degree g,
⊢ degree f + ↑(nat_degree g - nat_degree f) = degree g
</pre></div>


<p>There's a lemma saying that if <code>f</code> is non-zero then <code>degree f = ↑(nat_degree f)</code> but if I go down that route then I can't seem to use <code>nat.cast_add</code> etc, probably because although <code>with_bot nat</code> is an add_monoid, the coercion is not the usual one from nat to an add_monoid with a 1, it's like the coercion from nat to int. I think that this may mean that all of the lemmas of the form <code>↑(m+n)=↑m+↑n</code> for add, mul, le etc all need to be written by hand for this coercion from nat to <code>with_bot nat</code>, just like we have <code>int.coe_nat_add</code> etc. Am I correct? I ask because I need them for Hilbert Basis and I may as well get on and do them if they need doing. Or am I missing a trick?</p>

#### [ Chris Hughes (Sep 07 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/degrees%20of%20polynomials/near/133505345):
<p>I think <code>with_bot.coe_add</code> is the lemma you need.</p>

#### [ Kevin Buzzard (Sep 07 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/degrees%20of%20polynomials/near/133505354):
<p>oh boy -- so I'm right but they're already there? Thanks Chris!</p>


{% endraw %}
