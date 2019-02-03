---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/07195GCDforidealsfractionalfield.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [GCD for ideals, fractional field](https://leanprover-community.github.io/archive/113489newmembers/07195GCDforidealsfractionalfield.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jan 29 2019 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/GCD%20for%20ideals%2C%20fractional%20field/near/157086615):
<p>Localisation is there but I don't know if anyone specifically put the field of fractions there. What does one want? Just the statement that if you localise an integral domain at 0 then you get a field?</p>
<p>GCD of an ideal -- does that always exist? I'd not heard of it before.</p>

#### [ Aditya Agarwal (Jan 29 2019 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/GCD%20for%20ideals%2C%20fractional%20field/near/157088982):
<p>It doesn't always have to exist. But that was the definition of the GCD we used in Algebra 1, and what is used in the proof of the Gauss Lemma I'm trying to write in lean.  </p>
<p>Wikipedia also seems to use that definition. <a href="https://en.wikipedia.org/wiki/GCD_domain" target="_blank" title="https://en.wikipedia.org/wiki/GCD_domain">https://en.wikipedia.org/wiki/GCD_domain</a></p>

#### [ Aditya Agarwal (Jan 29 2019 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/GCD%20for%20ideals%2C%20fractional%20field/near/157089092):
<p>I would prefer working with the GCD being defined in terms of ideals because it lets me ignore multiplication by units.  However, working with the ordinary defintion doesn't create any insurmountable issue.</p>

#### [ Kevin Buzzard (Jan 29 2019 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/GCD%20for%20ideals%2C%20fractional%20field/near/157090327):
<p>That link is only about GCD's of finite sets of elements, not arbitrary ideals. I vaguely remember some talk here about GCD domains a few months back.</p>

#### [ Aditya Agarwal (Jan 29 2019 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/GCD%20for%20ideals%2C%20fractional%20field/near/157092574):
<p>Whoops, yeah. I totally forgot the infintie case exists.</p>

#### [ Aditya Agarwal (Jan 29 2019 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/GCD%20for%20ideals%2C%20fractional%20field/near/157092671):
<p>There is <a href="https://github.com/leanprover/mathlib/blob/master/src/algebra/gcd_domain.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/src/algebra/gcd_domain.lean">https://github.com/leanprover/mathlib/blob/master/src/algebra/gcd_domain.lean</a> , but it seems to use the normal definition of GCD.</p>

#### [ Kevin Buzzard (Jan 29 2019 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/GCD%20for%20ideals%2C%20fractional%20field/near/157093220):
<p>My memory was that the CS people at some stage wanted to choose a generator of every ideal or something. They think about stuff in really weird asymmetric ways.</p>

#### [ Kevin Buzzard (Jan 29 2019 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/GCD%20for%20ideals%2C%20fractional%20field/near/157093322):
<p>There was some discussion about whether it was possible to choose a generator of every principal ideal in a way compatible with multiplication, and it works great for some rings (eg choose the monic generator for poly rings and the non negative generator for the integers) but it can't be done in general</p>


{% endraw %}
