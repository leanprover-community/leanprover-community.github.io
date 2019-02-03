---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56247localnotationforfinn1.html
---

## Stream: [general](index.html)
### Topic: [local notation for fin (n+1)](56247localnotationforfinn1.html)

---


{% raw %}
#### [ Johan Commelin (May 24 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019139):
<p>How do I make the following work?</p>
<div class="codehilite"><pre><span></span><span class="n">local</span> <span class="kn">notation</span> <span class="bp">`</span> <span class="o">[</span><span class="n">n</span><span class="o">]</span> <span class="bp">`</span> <span class="o">:=</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span>
</pre></div>


<p>I need this notation a lot, and all the explicit <code>fin (n+1)</code>'s are driving me crazy. Plus all the off-by-one errors that creep into my code...</p>

#### [ Kevin Buzzard (May 24 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019201):
<p>hmm</p>

#### [ Kevin Buzzard (May 24 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019204):
<p><code>[n]</code> already means something else</p>

#### [ Kevin Buzzard (May 24 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019208):
<p>Oh -- I think that the n in quotes is a literal n</p>

#### [ Kevin Buzzard (May 24 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019213):
<p>so at the very least you'll want <code> ` [ ` n ` ] ` </code></p>

#### [ Kevin Buzzard (May 24 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019219):
<p>but I am not sure how over-riding already-used notation works</p>

#### [ Johan Commelin (May 24 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019343):
<p>Thanks, it is working now. I didn't know about the existing notation; but using <code>local notation</code> I can override it just fine (-;</p>

#### [ Kevin Buzzard (May 24 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019774):
<div class="codehilite"><pre><span></span><span class="kn">variable</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="bp">#</span><span class="kn">check</span> <span class="o">[</span><span class="n">n</span><span class="o">]</span> <span class="c1">-- list ℕ</span>
</pre></div>

#### [ Kevin Buzzard (May 24 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019779):
<p>you just broke list ;-)</p>

#### [ Kevin Buzzard (May 24 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019780):
<p>at least locally</p>

#### [ Kevin Buzzard (May 24 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019783):
<p>of course, this might be clever :-)</p>

#### [ Kevin Buzzard (May 24 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019795):
<p>although given your smiley convention I think I would have recommended <code> ` (-; ` n ` ;-) ` </code></p>

#### [ Johan Commelin (May 24 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020026):
<p>Hmm, but I guess that the <code>local</code> prefix means that I am still safe. I'm not using lists...</p>

#### [ Patrick Massot (May 24 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020289):
<p>Johan, there are plenty of brackets available. See how I use brackets for commutators in <a href="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/support.lean#L115" target="_blank" title="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/support.lean#L115">https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/support.lean#L115</a> for instance</p>

#### [ Kevin Buzzard (May 24 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020333):
<p>But <code>[n]</code> is standard in this game, isn't it?</p>

#### [ Patrick Massot (May 24 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020336):
<p>Sure. <code>[a, b]</code> for commutators is also standard</p>

#### [ Kevin Buzzard (May 24 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020337):
<p>CS : "overloading is bad"; Math "but we do it so well!"</p>

#### [ Patrick Massot (May 24 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020344):
<p>But waiting for CS people to change their notation for lists won't help</p>

#### [ Kevin Buzzard (May 24 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020345):
<p>I don't think Johan should even make the notation local</p>

#### [ Kevin Buzzard (May 24 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020348):
<p>I think Lean should just infer which notation is being used</p>

#### [ Kevin Buzzard (May 24 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020350):
<p>it has an elaborator, right?</p>

#### [ Patrick Massot (May 24 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020351):
<p>Sometimes it does</p>

#### [ Patrick Massot (May 24 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020406):
<p>Sean, I meant: "sometimes it infers which notation is being used", not "sometimes it has an elaborator"...</p>

#### [ Sean Leather (May 24 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020458):
<p>Patrick: Aww, I liked the latter interpretation better.</p>

#### [ Kevin Buzzard (May 24 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020591):
<p>Man, that would be a pretty crazy Lean 4 development</p>

#### [ Kevin Buzzard (May 24 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020594):
<p>"we removed the elaborator to encourage users to write better code"</p>

#### [ Kevin Buzzard (May 24 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020596):
<p>the metamath approach</p>

#### [ Patrick Massot (May 24 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020637):
<p>This time we are happy Mario isn't working on Lean 4</p>

#### [ Sean Leather (May 24 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020640):
<p>Slogan: How To Be Lean: Elaborate It Yourself!</p>

#### [ Reid Barton (May 24 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127041620):
<p>I wish there was something between <code>notation</code> and <code>local notation</code>, so that modules could export notation without forcing every downstream client to see it.<br>
For example, something like notation which is tied to the current namespace, so that it is only visible when that namespace is open.</p>

#### [ Reid Barton (May 24 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127041638):
<p>(I think that exact idea is probably not very good, but something of that flavor.)</p>

#### [ Mario Carneiro (May 24 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127041848):
<p>This is exactly how lean 2 notation used to work. Why it changed, I don't know, and I'm not clear on whether to expect this to be different in lean 4.</p>

#### [ Mario Carneiro (May 24 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127041932):
<p>I think that lean 3 notation is not handled very well at all, this is why I avoid all notation overloading in mathlib</p>

#### [ Johan Commelin (May 24 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127041951):
<p>Hmmm, ok. Does that mean that my <code>local notation</code> for <code>fin (n+1)</code> is dangerous?</p>

#### [ Mario Carneiro (May 24 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127041964):
<p>A local notation is fine, assuming you never use lists in that file</p>

#### [ Mario Carneiro (May 24 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127042026):
<p>but global notations require global coordination</p>

#### [ Johan Commelin (May 24 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127042033):
<p>Ok, understood</p>


{% endraw %}
