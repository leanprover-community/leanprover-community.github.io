---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/82678convandassociativity.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [conv and associativity](https://leanprover-community.github.io/archive/116395maths/82678convandassociativity.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Nov 13 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/conv%20and%20associativity/near/147579358):
<p>If any category theorists have recently been fighting with associativity, they might like the new <code>conv</code> tactic I just wrote:</p>
<div class="codehilite"><pre><span></span>/--
`slice` is a conv tactic; if the current focus is a composition of several morphisms,
`slice a b` reassociates as needed, and zooms in on the `a`-th through `b`-th morphisms.

Thus if the current focus is `(a ≫ b) ≫ ((c ≫ d) ≫ e)`, then `slice 2 3` zooms to `b ≫ c`.
 -/
</pre></div>

#### [ Scott Morrison (Nov 13 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/conv%20and%20associativity/near/147579364):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>, <span class="user-mention" data-user-id="128547">@Michael Jendrusch</span>, <span class="user-mention" data-user-id="112680">@Johan Commelin</span> in particular may like this.</p>

#### [ Scott Morrison (Nov 13 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/conv%20and%20associativity/near/147579390):
<p>It needs a better name, and perhaps to be generalised to an arbitrary associative operation ...</p>

#### [ Johan Commelin (Nov 13 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/conv%20and%20associativity/near/147579530):
<p>Hurray! That looks really cool. And yes, I wouldn't mind having this for groups and rings as well!</p>

#### [ Patrick Massot (Nov 13 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/conv%20and%20associativity/near/147580947):
<p>Oh yes, I already asked for this tactic in groups and rings</p>

#### [ Kevin Buzzard (Nov 13 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/conv%20and%20associativity/near/147589525):
<p>I was doing some basic binomial theorem stuff yesterday for the UGs and this would have been very convenient if it worked for + i.e. let me zoom into <code>(a+b)+((c+d)+e)</code></p>


{% endraw %}
