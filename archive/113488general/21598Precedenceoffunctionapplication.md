---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21598Precedenceoffunctionapplication.html
---

## Stream: [general](index.html)
### Topic: [Precedence of function application](21598Precedenceoffunctionapplication.html)

---


{% raw %}
#### [ Joe Hendrix (Aug 08 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Precedence%20of%20function%20application/near/131073950):
<p>Can notation bind tighter than function application?  e.g. For an operator <code>^</code> make <code>f x ^ y</code> parse as <code>f (x ^ y)</code>?</p>

#### [ Chris Hughes (Aug 08 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Precedence%20of%20function%20application/near/131074272):
<p>I think not.</p>

#### [ Kevin Buzzard (Aug 08 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Precedence%20of%20function%20application/near/131074274):
<p>I think that (a) function application has super-high binding power and (b) if you want to use notation which already exists in Lean (like <code>^</code>) then, whilst you can define it to mean new things, you cannot change its default binding power, which is lower than the super-high binding power of functions. So at the very least you would have to use notation which is not already used in Lean, e.g. <code>\clubsuit</code> or some random thing like that.</p>

#### [ Joe Hendrix (Aug 08 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Precedence%20of%20function%20application/near/131074958):
<p>Yes, I meant "^" as a placeholder.   It looks like I can, but it was a much higher binding power than I tested at first.</p>

#### [ Joe Hendrix (Aug 08 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Precedence%20of%20function%20application/near/131075107):
<p>This seemed to work,  but if the precedence is any lower it doesn't.</p>
<div class="codehilite"><pre><span></span>set_option pp.all true

infix ` &lt;&gt; `:1025 := and
constant f : Prop → Prop
#check f true &lt;&gt; false
</pre></div>


<p>Anyways, thanks for suggesting the "super-high" binding power.</p>

#### [ Mario Carneiro (Aug 08 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Precedence%20of%20function%20application/near/131077736):
<p>Yes, you can. The binding power of application is <code>max = 1024</code>, which despite the name is not the maximum possible bonding power; you can see <code>max+10</code> used in the <code>core.lean</code> file.</p>

#### [ François G. Dorais (Aug 08 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Precedence%20of%20function%20application/near/131078180):
<p>BTW: <code>max_plus</code> is useful, it evaluates to 1034 (aka <code>max+10</code>) and avoids silly incidents like <code>max+11</code> (aka <code>max_spinal_tap</code>).</p>


{% endraw %}
