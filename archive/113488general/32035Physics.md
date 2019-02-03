---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/32035Physics.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Physics?](https://leanprover-community.github.io/archive/113488general/32035Physics.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Wojciech Nawrocki (Sep 27 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Physics%3F/near/134742787):
<p>Hey, I'm curious - are there any physicists here looking at formalising some of the vector algebra for quantum theory? I couldn't find anything related to e.g. Hilbert spaces.</p>

#### [ Kevin Buzzard (Sep 27 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Physics%3F/near/134743245):
<p>A first year undergraduate student of mine formalised the definition of Hilbert spaces as part of their summer project, but I don't think there's anything in the official maths library.</p>

#### [ Sean Leather (Sep 27 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Physics%3F/near/134743354):
<p>I don't recall any physicists coming forward openly. But if you are one, you'd better <a href="#narrow/stream/116395-maths/subject/physics.20attack/near/134230265" title="#narrow/stream/116395-maths/subject/physics.20attack/near/134230265">beware</a>.</p>

#### [ Kevin Buzzard (Sep 27 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Physics%3F/near/134743483):
<p><a href="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Banach%20spaces.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Banach%20spaces.lean">https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Banach%20spaces.lean</a> and and there are inner product spaces too, but actually I don't see Hilbert space yet.</p>

#### [ Andreas Swerdlow (Sep 27 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Physics%3F/near/134746069):
<p>I’m pretty sure I fixed the issue with Hilbert space so hope to PR soon</p>

#### [ Andreas Swerdlow (Sep 27 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Physics%3F/near/134746268):
<p>Although I only have one trivial lemma about Hilbert Spaces specifically</p>

#### [ Wojciech Nawrocki (Sep 28 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Physics%3F/near/134777737):
<p>Ok, thanks! I was looking at (maybe) formalising some results that require notions of a Hilbert space.<br>
<span class="user-mention" data-user-id="120943">@Andreas Swerdlow</span> do you mean it might be included in mathlib at some point?</p>

#### [ Andreas Swerdlow (Sep 28 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Physics%3F/near/134779717):
<p>Hopefully, but it probably needs some cleaning up</p>


{% endraw %}
