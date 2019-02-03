---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98304setsfromquotients.html
---

## Stream: [general](index.html)
### Topic: [sets from quotients](98304setsfromquotients.html)

---


{% raw %}
#### [ Chris Hughes (Feb 26 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20from%20quotients/near/123007417):
<p>Sets from quotients. Is there a function in lean which basically gives me this <code>{a : α // setoid.r (quot.out x) a}</code>. Also is there any tutorial anywhere on how things like heq, eq.dcases_on, eq.rec_on etc work?</p>

#### [ Andrew Ashworth (Feb 26 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20from%20quotients/near/123007526):
<p>you need to fire up your Coq installation and read <a href="http://adam.chlipala.net/cpdt/html/Equality.html" target="_blank" title="http://adam.chlipala.net/cpdt/html/Equality.html">http://adam.chlipala.net/cpdt/html/Equality.html</a> :|</p>

#### [ Simon Hudon (Feb 26 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20from%20quotients/near/123007681):
<p>Once you've learned about them, feel free to write a Lean documentation for them</p>

#### [ Chris Hughes (Feb 26 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20from%20quotients/near/123009408):
<p>What I've discovered is typing <code>induction h</code> where h is the proof that the types are equal, help to solve heq goals very easily</p>

#### [ Patrick Massot (Feb 26 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20from%20quotients/near/123010391):
<p>Yes, you're in the right mindset now! You can go and write some doc</p>

#### [ Mario Carneiro (Feb 27 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20from%20quotients/near/123019353):
<p>This can also be expressed as <code>{a // ⟦a⟧ = x}</code></p>

#### [ Chris Hughes (Feb 27 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20from%20quotients/near/123019369):
<p>I just realised that. Probably more sensible.</p>


{% endraw %}
