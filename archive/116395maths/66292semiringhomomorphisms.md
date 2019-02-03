---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/66292semiringhomomorphisms.html
---

## Stream: [maths](index.html)
### Topic: [semiring homomorphisms](66292semiringhomomorphisms.html)

---


{% raw %}
#### [ Johan Commelin (May 08 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126249853):
<p>There is a class for ring homomorphisms: <a href="https://github.com/leanprover/mathlib/blob/7d1ab388bb097db5d631d11892e8f110e1f2e9cd/algebra/ring.lean#L60" target="_blank" title="https://github.com/leanprover/mathlib/blob/7d1ab388bb097db5d631d11892e8f110e1f2e9cd/algebra/ring.lean#L60">https://github.com/leanprover/mathlib/blob/7d1ab388bb097db5d631d11892e8f110e1f2e9cd/algebra/ring.lean#L60</a><br>
But there is no class for semiring homomorphisms. Does it make sense to change broaden this class into semiring homomorphisms?</p>

#### [ Mario Carneiro (May 08 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126249910):
<p>You need to preserve zero for a semiring homomorphism</p>

#### [ Mario Carneiro (May 08 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126249917):
<p>in fact, I guess it's just the same as a monoid homomorphism which is also an additive monoid homo</p>

#### [ Johan Commelin (May 08 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250020):
<p>Aah, yes. That is not automatic</p>

#### [ Johan Commelin (May 08 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250030):
<p>Ok, so, shall I add a new class for semiring homs?</p>

#### [ Mario Carneiro (May 08 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250073):
<p>if you like</p>

#### [ Johan Commelin (May 08 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250095):
<p>What is a natural place for it? I am a bit surprised that the definition of a semiring is in core...</p>

#### [ Johan Commelin (May 08 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250098):
<p>Otherwise it would be natural to add it after the definition of semiring</p>

#### [ Mario Carneiro (May 08 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250099):
<p>the mathlib file for ring-like stuff is <code>algebra/ring.lean</code></p>

#### [ Johan Commelin (May 08 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250139):
<p>Ok, I will find some place in that file</p>

#### [ Mario Carneiro (May 08 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250142):
<p>semiring is defined in core because nat is a semiring and that defines all the operations on nat</p>

#### [ Mario Carneiro (May 08 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250145):
<p>I think this will change in lean 4 though</p>

#### [ Johan Commelin (May 08 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250197):
<p>Ok</p>

#### [ Johan Commelin (May 08 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250257):
<p>Aah, and it seems like monoid_homs are also not yet there</p>

#### [ Johan Commelin (May 08 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250694):
<p>Does this have anything to do with the "algebraic hierarchy" that I sometimes hear people talking about?</p>

#### [ Johan Commelin (May 08 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250713):
<p>At the moment there is a class for homomorphisms between two <code>group</code>s but if one (or both) of my groups are additive, there is no class for homomorphisms. Does this mean we need 4 classes to cover all the possibilities?</p>

#### [ Mario Carneiro (May 08 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250760):
<p>let's just say that is a point of discussion</p>

#### [ Mario Carneiro (May 08 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250763):
<p>One option is to use <code>multiplicative</code> to interpret an additive group as a multiplicative group</p>

#### [ Mario Carneiro (May 08 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250772):
<p>We have not made any significant effort to have a full complement of morphisms between the various available structures in mathlib</p>

#### [ Mario Carneiro (May 08 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250811):
<p>the ones that exist have basically been added ad-hoc as people needed them, and I'm fine with that</p>

#### [ Johan Commelin (May 08 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250812):
<p>Ok, I see</p>

#### [ Johan Commelin (May 08 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250820):
<p>Am I correct that parametricity could help here?</p>

#### [ Mario Carneiro (May 08 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250859):
<p>Well, <code>transport_to_additive</code> can be seen as a special case of parametricity</p>

#### [ Mario Carneiro (May 08 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250863):
<p>but there is also a lot of renaming to be done by the tactic</p>


{% endraw %}
