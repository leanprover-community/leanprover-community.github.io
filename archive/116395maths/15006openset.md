---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/15006openset.html
---

## Stream: [maths](index.html)
### Topic: [open_set](15006openset.html)

---


{% raw %}
#### [ Reid Barton (Oct 09 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open_set/near/135489758):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I'm curious why you reversed the direction of the arrows of <code>open_set</code>. I would rather put the contravariant-ness in the notion of (pre)sheaf.</p>

#### [ Scott Morrison (Oct 09 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open_set/near/135500583):
<p>Ah, I hadn't seen this, and asked your opinion elsewhere. I'll reverse it again when I get there.</p>

#### [ Kevin Buzzard (Oct 09 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open_set/near/135502013):
<p>Yes Scott mentioned this before I think. Maybe he said something like he had ops everywhere at all times with no obvious purpose?</p>

#### [ Kevin Buzzard (Oct 09 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open_set/near/135502023):
<p>I guess the point is that we never use the unopped category</p>

#### [ Johan Commelin (Oct 10 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open_set/near/135511685):
<p>Right, but once we start doing sheaves over sites we will want contravariant (pre)sheaves. And we also want those to specialise to "plain old" (pre)sheaves on open sets. So I vote for keeping the <code>op</code>.</p>

#### [ Kevin Buzzard (Oct 10 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open_set/near/135521274):
<p>Another question of course is where you want the <code>op</code> -- source or target. It's funny this is coming up now. I distinctly remember Scott saying "eew there are <code>op</code>s everywhere, but I've had a brilliant idea -- if we just redefine the open set category then they all go away and it's much easier to use" and it was one of those moments where I just thought "yeah, it's not ideal but I can completely see his point. It removes all of them at once."</p>


{% endraw %}
