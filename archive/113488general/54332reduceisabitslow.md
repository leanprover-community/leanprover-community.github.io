---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54332reduceisabitslow.html
---

## [general](index.html)
### [#reduce is a bit slow?](54332reduceisabitslow.html)

#### [Arseniy Alekseyev (Jul 17 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129783924):
These reductions work a bit slow for me:

    #reduce (10 : fin 3) -- over 10 seconds
    #reduce (15 : fin 3) -- over 5 minutes

Is this normal? :-)

#### [Simon Hudon (Jul 17 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129784259):
It is. Natural numbers are represented in unary notation so arithmetic on them in the kernel (not the VM) is bound to be slow. Numerals such as `(15 : fin 3)` are represented using the `bit0`, `bit1` and `zero` functions as `bit1 (bit1 (bit1 (bit1 zero)))` and `bit1 (x : a) := x + x + 1`. You're a getting a bunch of additions and each one is one addition and one modulo.

#### [Mario Carneiro (Jul 17 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129784278):
yes, #reduce is very slow, particularly for well founded recursive functions like mod. I would estimate this is something like cubic in the *value* of `n : fin 3` there

#### [Simon Hudon (Jul 17 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129784327):
If you want to test your definitions, I recommend `#eval`

#### [Simon Hudon (Jul 17 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129784340):
It uses the virtual machine instead of the kernel to do its computations.

#### [Arseniy Alekseyev (Jul 17 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129784454):
Ah, #eval is probably what I want. Thanks! 
@Mario, I figured unary numbers were the reason, but I'm not sure cubic is enough to explain it. Could it also be exponential due to call-by-name somewhere? Does lean use call-by-name?

#### [Mario Carneiro (Jul 17 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129784467):
cubic in the value of n means exponential in the length

#### [Mario Carneiro (Jul 17 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129784536):
And yes, #reduce is essentially call by name execution, although it's not exactly implemented that way

#### [Arseniy Alekseyev (Jul 17 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129784540):
Not sure what you mean, the value is 15: 15 cubed is not a large number. Do you call value something else?

#### [Mario Carneiro (Jul 17 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129784547):
I mean 15 cubed

#### [Mario Carneiro (Jul 17 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129784583):
but there is also a large constant factor due to the kernel manipulation of expressions at every stage (the expressions get huge, like 100000 lines long)

#### [Arseniy Alekseyev (Jul 17 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129785191):
Ok, the expression (1 + 1 + 1 + 1 ... : fin 20) has clear exponential scaling: the time ~exactly doubles with each +1. The binary encoding (as explained by Simon) made the timings of the original example much more random-looking.

#### [Mario Carneiro (Jul 17 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129785300):
actually on second thought I'm not sure if it is really exponential, since it is in fact `bit0` on `fin 3`, which should be constant time - it does not first calculate `15 : nat` and then turn it into a `fin 3`

#### [Arseniy Alekseyev (Jul 17 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129785576):
Given that it's approximately as slow as the empirically exponential-time (1 + 1 + ... ), I say it's almost certainly the same. Mod 3 won't help if all the call-by-name-duplication of the terms happens before you have a chance to compute the mod.

#### [Mario Carneiro (Jul 17 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129785673):
I honestly don't know exactly what kind of optimization if any is in place for duplication caused by beta reduction, but it is surely nonzero - I'm pretty sure there is a whnf_core cache which allows to avoid repeated calculation of normal forms

#### [Simon Hudon (Jul 17 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129785938):
Still, because we're talking about `fin`, you perform the modulo at every addition

#### [Simon Hudon (Jul 17 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129785953):
It does not do it in nat first. All those `1`s are of type `fin 3`

#### [Arseniy Alekseyev (Jul 17 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129786041):
probably type class stuff has something to do with it too because replacing + with fin.add makes it fast again

#### [Mario Carneiro (Jul 17 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129786062):
that's very strange

#### [Mario Carneiro (Jul 17 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129786070):
typeclass stuff should be a negligible fraction of the work

#### [Arseniy Alekseyev (Jul 17 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129786199):
I guess with call-by-name it's not really about the work but about whether you somehow duplicate the argument or not (and whether or not the detection you mentioned kicks in)

#### [Arseniy Alekseyev (Jul 17 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129786231):
anyway, I'm going to stop looking because #eval solves my problem and sounds like this slowness is expected. thanks!

#### [Arseniy Alekseyev (Jul 17 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129800058):
Even more pathological example:

    #reduce (λ (x : nat) (y : x < 1), (fin.mk x y + 0 : fin 1)) -- 5 seconds
    #reduce (λ (x : nat) (y : x < 2), (fin.mk x y + 0 : fin 2)) -- > 1 minute

no "15" necessary :-)

#### [Gabriel Ebner (Jul 17 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129800675):
Please be aware that `fin` contains both a natural number *and* a proof.  The `#reduce` command normalizes both parts, including the proof.  You can use `set_option pp.all true` to see the full term.  If you run `#reduce (10 : fin 3).1`, you'll only get the number (in unary) but not the proof; this is a bit faster.

#### [Gabriel Ebner (Jul 17 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129800677):
In any case, avoid kernel computation.

#### [Kevin Buzzard (Jul 17 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce is a bit slow?/near/129800877):
Lean was not designed to do fully-verified computation quickly :-) `#reduce 10000+10000` will bring the system to its knees. This is the whole point of `#eval`

