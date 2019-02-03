---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/05925Proofexamples.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Proof examples?](https://leanprover-community.github.io/archive/113488general/05925Proofexamples.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Ryan Smith (Sep 21 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134356151):
<p>Hi, I'm entirely new to lean. I've read the docs, but I'm struggling to see what it would look like to prove anything in practice. The homepage didn't have much of a gallery, do we have examples of what a simple proof of the infinitude of primes or Lagrange's theorem for finite groups would look like?</p>

#### [ Bryan Gin-ge Chen (Sep 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134356286):
<p>You may want to check out <a href="https://github.com/leanprover/mathlib" target="_blank" title="https://github.com/leanprover/mathlib">the lean mathlib project</a>; many of the contributors are quite active in this chat.  <a href="https://github.com/leanprover/mathlib/blob/master/data/nat/prime.lean#L212" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/data/nat/prime.lean#L212">Here's the proof of the infinitude of primes</a> in mathlib, and <a href="https://github.com/leanprover/mathlib/blob/master/group_theory/order_of_element.lean#L126" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/group_theory/order_of_element.lean#L126">here's the proof of Lagrange's theorem</a>.</p>

#### [ Mario Carneiro (Sep 21 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134356350):
<p>Yay, mathlib already contains two theorems selected at random from math. Thus, mathlib has 75% of math, QED</p>

#### [ Johan Commelin (Sep 21 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134356351):
<p>Welcom <span class="user-mention" data-user-id="130170">@Ryan Smith</span> If you want you can write a little introduction about your background in <a href="#narrow/stream/113489-new-members/subject/Introductions" title="#narrow/stream/113489-new-members/subject/Introductions">https://leanprover.zulipchat.com/#narrow/stream/113489-new-members/subject/Introductions</a>. We're a bunch of enthousiastic mathematicians and computer scientists trying to build a library of data structures, automation and of course a bunch of mathematics.</p>

#### [ Bryan Gin-ge Chen (Sep 21 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134356352):
<p>I also forgot to say welcome! I'm also fairly new to lean and I've been asking silly questions in the <a class="stream" data-stream-id="113489" href="/#narrow/stream/113489-new-members">#new members</a>  stream for the past month or so.</p>

#### [ Johan Commelin (Sep 21 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134356410):
<p>Since a couple of weeks we try to post in <a href="#narrow/stream/116395-maths/subject/What's.20new.20in.20Lean.20maths.3F" title="#narrow/stream/116395-maths/subject/What's.20new.20in.20Lean.20maths.3F">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/What's.20new.20in.20Lean.20maths.3F</a> to tell people about new stuff in the library</p>

#### [ Mario Carneiro (Sep 21 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134356426):
<p>Johan, could you summarize the results of the kbb project in that thread?</p>

#### [ Johan Commelin (Sep 21 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134356470):
<p>I will try <span class="emoji emoji-1f603" title="smiley">:smiley:</span></p>

#### [ Simon Hudon (Sep 21 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134356499):
<p>Btw, why is that thread in <a class="stream" data-stream-id="116395" href="/#narrow/stream/116395-maths">#maths</a> ? That's a stream I don't follow</p>

#### [ Ryan Smith (Sep 21 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134356612):
<p>Oh cool, a number of basic primitives are already implemented. I thought things were a bit more rudimentary from reading the documentation.</p>

#### [ Johan Commelin (Sep 21 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134356959):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Because it really is about What's new in maths in Lean. We could probably have a similar thread in general where we post about new tactics and data structures and so on. But that thread is really about "Yeah, we have the fact that quotients of Noetherian modules are Noetherian!".</p>

#### [ Johan Commelin (Sep 21 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134356964):
<p>Also see my latest post there <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Simon Hudon (Sep 21 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134357028):
<p>The one summarize Kevin's birthday present?</p>

#### [ Johan Commelin (Sep 21 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134357077):
<p>Right, that one.</p>

#### [ Johan Commelin (Sep 21 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134357081):
<p>Is that the kind of stuff you would be interested in to know?</p>

#### [ Simon Hudon (Sep 21 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134357190):
<p>I think I misread, I thought you also announced tactics there (like <code>linarith</code>). To be frank, I didn't understand too much of what was put in Kevin's present.</p>

#### [ Johan Commelin (Sep 21 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134357205):
<p>We also announced <code>linarith</code> there. So there might be some overlap... but I think we could cross post those announcements to a "What's new in Lean thread in <code>#general</code>"</p>

#### [ Simon Hudon (Sep 21 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134357251):
<p>That sounds like a good idea. Thanks :)</p>

#### [ Mario Carneiro (Sep 21 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134357417):
<p>I cross posted <code>abel</code> there since there is an overlap of interest, but also because people always want to have a conversation about these news items and I would rather not clutter up an announcement thread with that</p>

#### [ Mario Carneiro (Sep 21 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134357488):
<p>In fact, I suggest we get in the habit of linking each news item to a thread about it specifically so people can use it as a hub</p>

#### [ Johan Commelin (Sep 21 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20examples%3F/near/134357742):
<p>Done.</p>


{% endraw %}
