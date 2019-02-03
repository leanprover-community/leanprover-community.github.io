---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/19949issubtypeinjective.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [is "subtype" injective?](https://leanprover-community.github.io/archive/113489newmembers/19949issubtypeinjective.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Sep 13 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133907830):
<p>if {x // p x} = {x // q x}, then is it true that p = q?</p>

#### [ Chris Hughes (Sep 13 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133907874):
<p>Pretty sure it's independent unless they're different sizes.</p>

#### [ Kenny Lau (Sep 13 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133908076):
<p>great, I just found another independent proposition</p>

#### [ Kenny Lau (Sep 13 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133908080):
<p>ZFC 1 : 0 Lean</p>

#### [ Mario Carneiro (Sep 13 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133909373):
<p>Lean has loads of independent propositions like this</p>

#### [ Kenny Lau (Sep 13 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133909397):
<p>ZFC aleph[0] : 0 Lean</p>

#### [ Mario Carneiro (Sep 13 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133909398):
<p>Equality of types is essentially "freely generated"; unless it's obviously true it's probably independent</p>

#### [ Mario Carneiro (Sep 13 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133909453):
<p>of course there is a whole cottage industry built around alternative models that fit in this gap (see: HoTT)</p>

#### [ Mario Carneiro (Sep 13 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133909548):
<p>the distance from axioms to independent statements is very short in lean:</p>
<div class="codehilite"><pre><span></span>inductive A. inductive B.
example : A = B := independent
</pre></div>

#### [ Kenny Lau (Sep 13 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133909561):
<p>wait what</p>

#### [ Kenny Lau (Sep 13 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133909567):
<p>well I suppose it makes sense</p>

#### [ Kenny Lau (Sep 13 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133909593):
<p>so we can essentially have two copies of <code>empty</code> and nobody will notice</p>

#### [ Kenny Lau (Sep 13 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133909604):
<p>also is there any way to create an inductive type?</p>

#### [ Kenny Lau (Sep 13 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133909605):
<p>inside a proof?</p>

#### [ Kenny Lau (Sep 13 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133909613):
<p>i.e. how much does Lean itself know about inductive types?</p>

#### [ Mario Carneiro (Sep 13 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133909625):
<p>oh wait, I forgot to define equality</p>
<div class="codehilite"><pre><span></span>prelude
inductive A. inductive B.
inductive eqA : Type → Type | refl : eqA A
example : eqA B := independent
</pre></div>

#### [ Kenny Lau (Sep 13 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133909675):
<p>lol</p>

#### [ Mario Carneiro (Sep 13 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133909720):
<p>inductive types in lean are essentially an axiom schema</p>

#### [ Mario Carneiro (Sep 13 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133909741):
<p>you have to write down the type specification, and then poof appears a new type constant</p>

#### [ Mario Carneiro (Sep 13 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133909795):
<p>so they only work at the top level</p>

#### [ Kenny Lau (Sep 13 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133909828):
<p>I see</p>

#### [ Mario Carneiro (Sep 13 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/is%20%22subtype%22%20injective%3F/near/133909849):
<p>although you can always define a very general type and then narrow it down from inside a definition, i.e. defining a particular subtype of sigma of W type of whatever rather than writing a new inductive type</p>


{% endraw %}
