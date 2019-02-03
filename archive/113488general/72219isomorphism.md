---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72219isomorphism.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [isomorphism](https://leanprover-community.github.io/archive/113488general/72219isomorphism.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Blair Shi (Jul 30 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphism/near/130566051):
<p>Can anyone tell me what should I do to prove a basis v1,v2,...,vn of a fdvs V/k is just an isomorphism k^n -&gt; V in lean? Should I show the homomorphism firstly and then show the homomorphism is bijective?</p>

#### [ Kenny Lau (Jul 30 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphism/near/130566059):
<p>I would think so</p>

#### [ Johan Commelin (Jul 30 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphism/near/130566275):
<p>Yes, that is best... it will make your life easier when you prove injectivity.</p>

#### [ Kevin Buzzard (Jul 30 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphism/near/130566917):
<blockquote>
<p>Can anyone tell me what should I do to prove a basis v1,v2,...,vn of a fdvs V/k is just an isomorphism k^n -&gt; V in lean? Should I show the homomorphism firstly and then show the homomorphism is bijective?</p>
</blockquote>
<p>An <em>ordered</em> basis of a fdvs is just an isomorphism. Note that the inbuilt basis stuff in Lean is not ordered, so you need the notion of an ordered basis, which I think you have. </p>
<p>What you should then maybe do is: (1) for a fixed vector space V and natural number n, define a type of "bases for V of size n" and define a type of "isomorphisms k^n -&gt; V". Then write down maps in both directions and prove that the composites are the identity in both directions. Keji was doing something similar the other day (but not the same -- he was looking at matrices = linear maps, you're doing something else). </p>
<p>I think first I would prove that for V and n, there's a bijection between k-linear maps k^n -&gt; V and lists of elements of V of length n.</p>
<p>I have some minor hold-ups at home but I hope to be at work for 11:30 -- are you in today Blair? We could talk more then.</p>

#### [ Blair Shi (Jul 30 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphism/near/130568215):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I am in mlc now. I think we can talk later</p>


{% endraw %}
