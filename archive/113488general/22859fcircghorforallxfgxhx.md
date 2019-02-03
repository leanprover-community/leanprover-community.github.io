---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22859fcircghorforallxfgxhx.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [f circ g = h or forall x, f (g x) = h x?](https://leanprover-community.github.io/archive/113488general/22859fcircghorforallxfgxhx.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 23 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544509):
<p>I am constantly proving that various functions are equal because they are both the unique function with some property. A lot of my proofs naturally prove <code>f circ g = h</code>. However Kenny often writes such goals as <code>forall x, f (g x) = h x</code>. Normally in Lean I would prove <code>f circ g = h</code>  by applying funext and then <code>intro x</code>. However in the kind of mathematics I'm currently doing this is not the way to prove things -- in fact I hardly ever get my hands dirty with explicit terms, I'm just chasing around universal properties.</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544552):
<p>Kenny set up a structure with things like <code>function.left_inverse g f</code> and <code>function.right_inverse g f</code> and I had assumed these would unravel to <code>g circ f = id</code> etc but even these core functions evaluate to <code>forall x, g (f x) = x</code></p>

#### [ Mario Carneiro (Apr 23 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544560):
<p>The left inverse thing is convenient because that way you can write <code>function.left_inverse g f x</code></p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544561):
<p>What's a nice convenient way to deduce "forall x, g (f x) = h x" from "g circ f = h" ? I keep having to enter tactic mode and then rewriting the goal with rw, and usually rw \l.</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544600):
<p>Is there a proof of <code>g circ f = h -&gt; forall x, g (f x) = h x</code>?</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544601):
<p>I am using it all the time</p>

#### [ Mario Carneiro (Apr 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544603):
<p>then make it a lemma</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544606):
<p>fair do's</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544612):
<p>what's it called?</p>

#### [ Mario Carneiro (Apr 23 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544615):
<p>it's a bit too specific for my taste, but if you fold it in with one of your definitions I'm sure it will work well</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544618):
<p>I think what I'd rather do is to rewrite all the definitions which we have which involve the x</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544672):
<p>however I am concerned that end users might need the "explicit" versions</p>

#### [ Mario Carneiro (Apr 23 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544675):
<p>then have a special constructor for your more user-facing theorems that accepts the explicit version</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544677):
<p>I don't understand this</p>

#### [ Mario Carneiro (Apr 23 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544678):
<p>I would make that lemma a biconditional BTW, you will want both directions</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544679):
<p>I know that 9 times out of 10 when i'm trying to prove f = g the first thing I do is apply funext</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544682):
<p>but here it's never true</p>

#### [ Mario Carneiro (Apr 23 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544687):
<p>My initial thought on this is to use functions, you are basically doing category theory lite</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544689):
<p>right</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544691):
<p>I don't care about my actual definition of a localised ring</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544730):
<p>all I ever use is the universal property</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544731):
<p>which is a real relief</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544733):
<p>because the localised ring is a quotient type</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544735):
<p>and they are awkward to use</p>

#### [ Mario Carneiro (Apr 23 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544740):
<p>So when do you actually need the <code>x</code>?</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544741):
<p>no idea</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544749):
<p>I am not sure I do</p>

#### [ Mario Carneiro (Apr 23 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544750):
<p>At the very least you have some notion of a "user" that will use one of the theorems and prove a hypothesis by funext</p>

#### [ Mario Carneiro (Apr 23 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544753):
<p>which theorems are most likely candidates for this?</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544755):
<p>I am not sure I have a clear notion of a user</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544756):
<p>I think I am the only user at the minute</p>

#### [ Mario Carneiro (Apr 23 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544794):
<p>hence the quotes</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544799):
<p>Maybe if Kenny does more exercises in Atiyah-Macdonald he'll become another user</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544801):
<p>Maybe I'll just rip out all the x's.</p>

#### [ Mario Carneiro (Apr 23 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544802):
<p>or maybe your theorem has a conclusion that is a function equality, and the mythical user wants to congr_fun that equality</p>

#### [ Mario Carneiro (Apr 23 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125544810):
<p>you should identify the most outward-facing of your theorems and make them as pleasant to use as you can</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125545016):
<p>This exercise (wanting a theory of localization because I have a use for it, but asking Kenny to prove the theorems) has really clarified for me how this whole process of writing a library works.</p>

#### [ Patrick Massot (Apr 23 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/f%20circ%20g%20%3D%20h%20or%20forall%20x%2C%20f%20%28g%20x%29%20%3D%20h%20x%3F/near/125558389):
<blockquote>
<p>by applying funext and then <code>intro x</code></p>
</blockquote>
<p>Side remark: you can write <code>funext x</code> instead of <code>funext, intro x</code>. Soon you'll even be able to write <code>ext x</code> without thinking about whether you deal with an actual function or any other object for which extensionality makes sense</p>


{% endraw %}
