---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/82678convandassociativity.html
---

## Stream: [maths](index.html)
### Topic: [conv and associativity](82678convandassociativity.html)

---


{% raw %}
#### [ Scott Morrison (Nov 13 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/conv%20and%20associativity/near/147579358):
If any category theorists have recently been fighting with associativity, they might like the new `conv` tactic I just wrote:
```
/-- 
`slice` is a conv tactic; if the current focus is a composition of several morphisms,
`slice a b` reassociates as needed, and zooms in on the `a`-th through `b`-th morphisms.
    
Thus if the current focus is `(a ≫ b) ≫ ((c ≫ d) ≫ e)`, then `slice 2 3` zooms to `b ≫ c`.
 -/
```

#### [ Scott Morrison (Nov 13 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/conv%20and%20associativity/near/147579364):
@**Reid Barton**, @**Michael Jendrusch**, @**Johan Commelin** in particular may like this.

#### [ Scott Morrison (Nov 13 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/conv%20and%20associativity/near/147579390):
It needs a better name, and perhaps to be generalised to an arbitrary associative operation ...

#### [ Johan Commelin (Nov 13 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/conv%20and%20associativity/near/147579530):
Hurray! That looks really cool. And yes, I wouldn't mind having this for groups and rings as well!

#### [ Patrick Massot (Nov 13 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/conv%20and%20associativity/near/147580947):
Oh yes, I already asked for this tactic in groups and rings

#### [ Kevin Buzzard (Nov 13 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/conv%20and%20associativity/near/147589525):
I was doing some basic binomial theorem stuff yesterday for the UGs and this would have been very convenient if it worked for + i.e. let me zoom into `(a+b)+((c+d)+e)`


{% endraw %}
