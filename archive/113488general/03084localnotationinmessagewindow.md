---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03084localnotationinmessagewindow.html
---

## Stream: [general](index.html)
### Topic: [local notation in message window](03084localnotationinmessagewindow.html)

---


{% raw %}
#### [ Patrick Massot (Apr 23 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125571696):
<p>I have a local infix notation for an operation which is a local variable. Is there any hope to see Lean using this notation in the Lean messages window?</p>

#### [ Patrick Massot (Apr 23 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574186):
<p>No idea, anyone? That would really help me.</p>

#### [ Simon Hudon (Apr 23 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574294):
<p>I've struggled with that too. Recently, I had an idea but I haven't tried it yet. What's the type of your variable?</p>

#### [ Patrick Massot (Apr 23 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574380):
<p>It's a composition law</p>

#### [ Patrick Massot (Apr 23 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574393):
<p><code>op : R → R → R</code></p>

#### [ Patrick Massot (Apr 23 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574400):
<p><code>local infix ` ◆ `:70 := op</code></p>

#### [ Simon Hudon (Apr 23 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574420):
<p>Cool. Let's try this:</p>
<div class="codehilite"><pre><span></span>def my_op := op

local infix ` ◆ `:70 := my_op op
</pre></div>

#### [ Patrick Massot (Apr 23 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574479):
<p>breaks everything <span class="emoji emoji-1f61e" title="disappointed">:disappointed:</span></p>

#### [ Simon Hudon (Apr 23 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574569):
<p>Was that not what you were going for?</p>

#### [ Kenny Lau (Apr 23 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574605):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">my_op</span> <span class="o">:=</span> <span class="n">op</span>

<span class="n">local</span> <span class="kn">infix</span> <span class="bp">`</span> <span class="err">◆</span> <span class="bp">`</span><span class="o">:</span><span class="mi">70</span> <span class="o">:=</span> <span class="n">my_op</span>
</pre></div>

#### [ Kenny Lau (Apr 23 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574607):
<p>I think that's what he means</p>

#### [ Patrick Massot (Apr 23 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574667):
<p>I understood he meant that</p>

#### [ Patrick Massot (Apr 23 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574669):
<p>still breaks everything</p>

#### [ Simon Hudon (Apr 23 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574679):
<p>is <code>op</code> a <code>parameter</code> or a variable?</p>

#### [ Patrick Massot (Apr 23 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574684):
<p>variable</p>

#### [ Simon Hudon (Apr 23 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574689):
<p>Are you inside a section?</p>

#### [ Simon Hudon (Apr 23 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574703):
<p>Can you make it a parameter?</p>

#### [ Patrick Massot (Apr 23 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574704):
<p>no</p>

#### [ Patrick Massot (Apr 23 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574709):
<p>I meant no I'm not inside a section</p>

#### [ Patrick Massot (Apr 23 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574719):
<p>I don't know about parameters</p>

#### [ Simon Hudon (Apr 23 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574794):
<p><span class="emoji emoji-1f606" title="laughing">:laughing:</span> I thought so. They're not great in Lean but sometimes you need them. Before I go there, can you show me the output of <code>#check @my_op</code>?</p>

#### [ Patrick Massot (Apr 23 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574877):
<p><code>my_op : Π {R : Type u_3}, (R → R → R) → R → R → R</code></p>

#### [ Kenny Lau (Apr 23 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125574897):
<p>let's just forget that algebraic hierarchy</p>

#### [ Simon Hudon (Apr 23 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125575047):
<p>With a variable, if you use <code>my_op</code> somewhere, you need to provide an argument for each variable. With parameters, inside the section, the parameters are a bit like constant. Inside tactic proofs, they get a bit flaky though.</p>

#### [ Patrick Massot (Apr 23 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125575092):
<p>I don't see the relation between the hierarchy and the problem we discuss here</p>

#### [ Simon Hudon (Apr 23 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20in%20message%20window/near/125575103):
<p>Try making <code>op</code> a parameter and wrap it and the related definitions in a section</p>


{% endraw %}
