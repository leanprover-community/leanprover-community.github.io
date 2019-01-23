---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/37821partialfunctionsonquotient.html
---

## Stream: [maths](index.html)
### Topic: [partial functions on quotient](37821partialfunctionsonquotient.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 05 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130929260):
What's the easiest way to define a partial function on a quotient type, where the proof that it is well defined depends on the predicate? I tried `quotient.hrec_on` but whilst I can define the function, it's hard to prove things about it due to `motive is not type correct` errors. For context, I'm experimenting with defining the signature of a permutation as being derived from this.
```lean
def sign_aux2 : list α → perm α → units ℤ
| []     f := 1
| (x::l) f := if f x = x then sign_aux2 l f else -sign_aux2 l (swap x (f x) * f)
```
I plan to use the list underneath `finset.univ`, and prove it doesn't depend on the order of the list.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 05 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130929261):
The problem is that the list has to contain everything of the type in order to prove the `quotient.lift` condition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 05 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130929617):
`roption`/`pfun` can be helpful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 05 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130929641):
though maybe I don't quite understand what you're doing yet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 05 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130929737):
I guess it's okay. The strategy is to define a (total) function to `roption (units \Z)`, which sends all "bad" elements to `roption.none`, using `quotient.lift`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 05 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130929865):
You can also define a dependent function which takes the needed hypothesis as an argument using `quotient.rec`, but I found that approach to be really difficult when I had to do something like this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 05 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130930011):
Good plan. Thanks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 05 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130930355):
Speaking as someone whose job it is to teach students what the signature of a permutation is, I'm pleased about how it's going this year. On the other hand speaking as someone who is well aware that these notions have been around for ages, I can't help but feeling that the issues my students are running into are ones which will already have been solved. Are there already 23 different implementations of signature of a permutation in Coq, for example? I kind-of suspect that the questions we've been running into since we started thinking about this are ones which will have been seen many times before...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 05 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130938495):
I think looking at coq is good for general questions like which proof should I use, but not so good for questions like this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 05 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130938719):
By the way, I was wondering whether it would be possible to define the sign of a permutation as the determinant of the corresponding linear transformation on (say) Q^n, and define the latter in terms of the nth exterior power.
But, in order to show the nth exterior power is not zero, I think you end up needing the fact that a composition of an odd number of transpositions cannot be the identity anyways. Unless there is an even fancier approach which I missed?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 05 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130938763):
Chris (and I independently) defined sign of permutation using number of inversions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 05 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130938973):
I changed it to basically what I posted above

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 05 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130938975):
Right, but if you were given the fact that $$\bigwedge^n \mathbb{Q}^{\oplus n}$$ was one-dimensional, then you could get signs of permutations (including that it is a group homomorphism) for free.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 05 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130938980):
Or there are other facts you could start from, like $$O(n)$$ (or $$GL(n, \mathbb{R})$$) having two components

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 05 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130940233):
To prove that the n'th exterior power is not zero I guess you have to explicitly construct some alternating form? If you could come up with some definition of det which had the property that switching two rows changed the sign etc then you might be in good shape, but the only way I know how to do this is to come up with the definition of det, and the definition of det I know involves signatures. I half-suspect that there were some comments about this in my UG notes, in my office, I'll try and remember to dig them up when I get back to London.


{% endraw %}
