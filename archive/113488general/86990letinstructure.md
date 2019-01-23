---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86990letinstructure.html
---

## Stream: [general](index.html)
### Topic: [let in structure](86990letinstructure.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451506):
```lean
structure foo :=
let bar := ℕ in
(3 : bar)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451510):
doesn't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451512):
moans about the let

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451518):
Am I doomed to write `power_bounded_elements R` throughout this entire definition?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451561):
well, we can make some notation for it, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451618):
Isn't double-superscript-circ common for this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451693):
aah here notation will solve my problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451695):
wait

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451697):
oh I have to leave the stupid gap

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451738):
$$R\ {}^\circ$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451740):
need the gap because of some fussy tokenizer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451804):
It feels a bit like we are back to the typography of SGA etc, doesn't it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451805):
```lean
def bar : Type := ℕ

structure foo :=
(x : bar)
```
I am unsure how to choose between notation and defs when you don't need infix/postfix parsing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 02 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451843):
I assume you're making it into a postfix operator. Why not make the whole thing (`R∘`) a notation?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451851):
You mean including the R?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 02 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451853):
Exactly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451854):
But that's variable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451861):
``notation : R `ᵒ` := power_bounded_subring R``

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451862):
How does notation work? I never know. I need some notation notes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 02 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451863):
If you declare it with `variable`, and make your notation local, that should be ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451864):
I know I can search through TPIL

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451865):
Yay for Zulip's parsing of "`".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 02 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451866):
Use more ticks until it works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451867):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451870):
I use two outer ticks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451919):
@**Simon Hudon** Aah, it's not `variable` like that. It is really variable in the notation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451920):
Like `x` and `y` in `x + y`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451923):
I can't get the notation to work though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 02 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451934):
I must have misunderstood. I thought you wanted a local shorthand for the current file.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451935):
Hmm, but now you didn't leave a gap in the ticks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451980):
I think it wants spaces around the `\circ`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 02 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451981):
Otherwise, you can use ``postfix `ᵒ` := power_bounded_subring``

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451983):
oh that looks like a nicer way to do it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451988):
it wants a number

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451990):
``postfix `ᵒ` : 37 := power_bounded_subring``

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452028):
that should do it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452034):
I must say, operator precedence is something else I am not sure I have a good feeling about

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452035):
I guess I want this one to be very sticky

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452042):
so should it be like 6 or 999999?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 02 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452044):
To be fair, I'm not fond of putting precedence on a linear scale. I feel like specifying a partial order would be easier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452083):
OK how about this:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452086):
```lean
structure perfectoid_ring (R : Type) (p : ℕ) [is_prime p] extends Tate_ring R :=
(is_complete : complete R)
(is_uniform  : uniform R)
(ramified    : ∃ ω : R ᵒ, 
                 (is_pseudo_uniformizer ω) ∧ (ω ^ p ∣ p))
 (Frob       : ∀ a : R ᵒ,
                 ∃ b c : R ᵒ, a = b ^ p + p * c)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 02 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452087):
Think about the operators that are likely to appear in the same formula (including `=`) and what should take precedence

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452094):
I want the circ to take precedence in the sense that I want R circ being evaluated ASAP

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452097):
i.e. `A x B o` is definitely `A x (B o)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 02 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452098):
precedence and evaluation order are not the same

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452099):
@**Johan Commelin** I reckon that looks fairly readable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452139):
Simon I don't know anything about this stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452140):
Yes, this looks very good. I hope you can maintain this throughout the top-down approach.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452141):
and I know I can learn it but I'm not that interested in it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 02 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452144):
I'll leave you guys to it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452145):
do you have a good suggestion for a number?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452150):
or else I'll leave it as 37 :-/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452151):
same as unary minus?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452157):
which is 65

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 02 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452159):
That looks like asking for trouble. Go one over or one below

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452198):
Is there anything below `50` at the moment?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452201):
tons

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452203):
propositional stuff mostly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452208):
50 is `=`, so that's about as low as you get for atomic propositions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452209):
ha ha (-Ro) -- is that what you're worried about Simon?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452212):
but types go lower than that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452213):
can that sort of thing be an issue?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452216):
equal isn't really a problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452219):
in fact it's important for having things be at the same level, like `a + b - c`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452220):
which is left associated regardless of whether `+` or `-` comes first

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452267):
@**Kevin Buzzard** If you want to squeeze out a little bit more readability, then maybe `Frob` should be phrased as a statement modulo `p`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452268):
there aren't many postfix operators in standard lean; there is `⁻¹` which has a crazy high precedence `max+10`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 02 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452307):
@**Kevin Buzzard** I'm not sure what Lean does in that kind of situation and I can't think of reasons why either of (-R)o or -(Ro) would be always the best default

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452309):
I wasn't sure how to do quotient rings in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452310):
But I guess, you rather prefer avoiding quotients.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452311):
actually I recently learnt how to use quotient types

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452312):
I was forced to

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452313):
All notations come with a binding power, whichever is higher wins

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452315):
I needed direct limits and Kenny's work is still not in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452321):
that includes mixing pre/postfix

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452322):
@**Simon Hudon** In both cases the unary minus doens't make much sense. (At least not in contemporary maths. Maybe someone wants to overload it, but that thought gives me shudders...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452324):
So I guess in practice there won't be a problem.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452364):
Since `R o` here is a type it really doesn't matter as long as it's higher than 50 or so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452372):
@**Kevin Buzzard** I told you before that `57` is a better default value than `37`! Grothendieck was careful when choosing his prime!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452378):
lol it would be funny if all the notation precedences were primes just because

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452379):
Ooh, now I have a crazy question. What is the type of `65` in the notation for unary minus? Does it even have a type?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452420):
It was once `num`, which was for a long time the only use of `num`. Now it's `nat`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452423):
`instance p : nat`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452424):
Does this lead me into trouble?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452425):
I am sick of this p

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452430):
I want access to it at all times and yet I never want to carry it around

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452434):
It's a global variable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452435):
see e.g. `std.prec.max`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452437):
In actual notation commands though the number is not an expression of type nat, it's a literal number string

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452478):
although you can use `max` and other things in that spot too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452482):
wait

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452483):
I have to make nat a class

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452484):
oh jeez where's that bit in the manual

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452485):
now I finally want to do it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452532):
Do you mean like `attribute [class] nat`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452581):
don't make `nat` a class

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452590):
make `Prime` a class

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452635):
@**Kevin Buzzard** Can't you have
```lean
variables (p : nat) (hp : prime p)
include p hp
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452638):
Does that make `p` and `hp` available everywhere you want them?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452689):
I'm using type class inference to carry around primality of p

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452690):
```
import data.nat.prime algebra.group_power

class Prime :=
(p : ℕ) (pp : nat.prime p)
open Prime

section
variable [Prime]

example (R) [ring R] (x : R) : x ^ 2 = x ^ p := sorry

end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452737):
I thought `Prime` was supposed to be the subtype

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452738):
it is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452739):
I suppose

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452746):
this way you get to change the name from `val` to `p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452748):
Actually I said "bundled structure", so this is in some sense more faithful to the convention

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452749):
Is this sort of stuff mathlib-acceptable?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452788):
only if you use it a lot

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452791):
I would prefer that you postprocess all your final theorems or whatever to make the prime explicit, but you can do this within the development if it helps

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452806):
is `p` actually `default nat` in that code snippet?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452846):
it's like `default nat` but not the same value

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452847):
This is one of the important aspects of creating a new `class` - you get to create your own typeclass graph

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452853):
in this case, since there are no instances of `Prime`, it will only ever pick up `[Prime]` in the context

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452895):
maybe `fixed_prime` is a better name for this typeclass

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452896):
at first glance, this seems kinda hackish to me, but I need to think about it some

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452897):
It very much conveys what's going on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452901):
the whole `variable [Prime]` has me for a loop

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452905):
I won't be using it a lot for the definition of perfectoid spaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452906):
Same here. I still don't get how Lean figures out what `p` means in the line
`example (R) [ring R] (x : R) : x ^ 2 = x ^ p := sorry`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452907):
it's just you'll use it all the time the moment you start proving theorems about them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452908):
Since `Prime` was opened, that's `Prime.p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452947):
Aah, cool!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452948):
which has an implicit typeclass argument `[Prime]`, which is discovered in the context

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452951):
So then once we start doing etale cohomology we want another class `fixed_coprime_prime`, and constructor `ℓ`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452954):
And a proof that it is not `p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452998):
```
class fixed_prime :=
(p : ℕ)
(pp : nat.prime p)
open fixed_prime

class fixed_coprime [fixed_prime] :=
(q : ℕ)
(co : nat.coprime p q)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453000):
Mario, I really like this! I hope that it is not to hackish for Lean. This reflects how `p` is used in a lot of number theory/alg.geom. You just fix `p` at the beginning of your paper, and it doesn't change for 50 pages.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453006):
Yes, but the `ℓ` has to be prime as well. As in "ℓ-adic cohomology" etc...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453007):
I haven't attempted to use this technique before. I'd be interested to see how it goes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453008):
it feels like an end run around `parameter`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453047):
you get the idea

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453050):
Sure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453051):
I will try to use it in the stuff on p-adic valuations.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453056):
Note that actually applying this for real primes, like if you want 57-adic cohomology, is a bit of a pain

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453091):
Hmm, I see.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453097):
well, maybe not so bad, you can use `local instance`s or `haveI` to introduce a `fixed_prime` without doing so globally

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453098):
That's a bit of a problem, I guess. For example squares in Q_2 behave different from squares in Q_p for p ≠ 2.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453145):
I mean, worst case scenario is you have to write `@thm` whenever you want to apply the theorem in a non `p` case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453146):
Yes, I see. That makes sense.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453148):
also you can prove things with the assumption `p = 2`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453150):
Right.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453157):
Actually the `@` notation reflects exactly how most mathematicians feel about working with one concrete prime. (Of course not the symbol "@", but the fact that all of a sudden you want to be specific about `p`.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453194):
You only do this in 1% of the time. And it always feels a bit disorienting.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453198):
whence the 57 thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453202):
I really think that we have theorems about `Q_p`, `Q_ℓ` and `Q_2`, and that is about it (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453247):
one other messy thing is if you want to use `l` as your `p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453252):
So, have to unpack stuff with `@` is expected behaviour.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453253):
Aah, yes, that might get messy...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453254):
Also, there is a very delicate theory about what happens when `ℓ = p`...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453255):
Headache ensues

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453261):
(Note: this is not relevant for defining perfectoid spaces. But it will definitely pop up later.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453302):
Long story short, this technique is useful for fixing a value for a long time, with the downside being it makes unfixing it hard

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453303):
parameters are easier to unfix, but then they stay unfixed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453347):
Ok, so maybe we should do the same thing as with multiplicative groups and additive groups. And just develop the theory both for `p` and for `ℓ`...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453351):
That's not unreasonable; the theorems are defeq so you just have to state them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453354):
Hmm, but sometimes you also want to compare what happens at `ℓ_1` and `ℓ_2`... and both are different from `p`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453360):
maybe ` ℓ` shouldn't be as fixed as `p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453361):
Or statements like `\forall ℓ : (ℓ ≠ p) blabla`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453401):
an argument for using a parameter might be that when you use `haveI` and friends, you don't get to benefit from type class caching... although I am unsure how much time Lean spends searching the type class graph - it's not something I have a good feel for

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453402):
in practice I've never seen an appreciable difference from using `haveI`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453407):
Ok, maybe `ℓ` should indeed have less fixiness than `p`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453505):
I think it might be a bigger deal for people working in interactive tactic mode... who have very large proofs / definitions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453512):
again, it ::sounds:: scary to me, also because I don't mind at all being explicit, but that may be because I don't have enough Lean experience

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453756):
would it affect memoization? suppose you had
```lean
def myDef := 
begin
  expensive_tac1,  -- uses typeclass inference somewhere
  expensive_tac2  -- does this mean we can't memoize the results of expensive_tac1 if we disable type class cache?
end
```


{% endraw %}
