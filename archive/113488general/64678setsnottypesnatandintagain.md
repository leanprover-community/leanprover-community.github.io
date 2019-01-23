---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64678setsnottypesnatandintagain.html
---

## Stream: [general](index.html)
### Topic: [sets not types? nat and int again](64678setsnottypesnatandintagain.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 27 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134728630):
John Harrison suggests a return to set theory in this talk : http://aitp-conference.org/2018/slides/JH.pdf . Some of what he said rings very true. I told a bunch of beginners over the summer to go and formalise some number theory, but the constant battle with coercions from nat to int to rat made everything far harder than it should be. One thing which particularly should be stressed was that I found on more than one occasion that mathematicians were *really surprised* that `5 / 2 = 2` for nat or int. This is very counter to the approach of "normal" mathematical software (sage etc) which in 99% of cases just makes a rational even if the inputs were integers. 

I have said this before but I really want the inclusions nat to int to rat to be easier for the beginner. However I have had no experience with formalising in set theory and am not at all convinced that it is the answer either. My proposal is to educate mathematicians so that they know that subtraction is not what they think it is on nat, and division is not what they think it is on nat or int, and then to have a tactic which literally eats a name representing something of type nat and introduces a new variable which is an int, adds the hypothesis that the int is >= 0 into the context and changes every occurrence of the old nat to the new int. And a similar one from nat/int to rat, with the hypothesis that the denominator is 1. I want the tactic to do all the donkeywork. 

This term I hope to get a whole bunch of data concerning what mathematicians actually find difficult when they try to learn dependent type theory by doing basic mathematics questions and I am already pretty sure that the (coercion from nat to int) fact that` \u(m^n)=\u m^\u n` is probably not `refl` and might not even typecheck (actually it might be refl, I can't check right now) and that `\u(m-n)=\u m-\u n` is not even true will be high up on the list.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 27 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134738904):
OK so here is a proposal. We create a new type which is the kind of number which a mathematician is used to using. Let's just call it `number`. For the sake of argument let's say it's just defined by `number := rat`, although `real` and `complex` would also be fine. `number` inherits everything from `rat` and so it's a totally ordered distrib and all the other things. And for `x : number` there's a typeclass `actually_an_integer x` with fields an integer and a proof that the coercion of the integer to rat is `x`, and similarly `actually_a_natural x`. Now you can have definitions like `number.nat.prime (x : number) [actually_a_natural x] := ...`I am envisaging a lot of theorems and definitions of this form being deduced automatically. I don't know to what extent I am living in cloud cuckoo land here. However, even if we have to port theorems by hand, the resulting user experience will hopefully be a darn sight better than my users faced with goals mentioning `neg_succ_of_nat`. I'd be very interested in feedback.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 27 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134738938):
Oh -- the answer to "why?" is "for pedagogical purposes".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 27 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134742043):
I can't give any feed back on the actual proposal. I do suggest that those typeclasses be called `is_nat` and `is_int`, for brevity and analogy with existing names.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 27 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134742305):
Maybe `maths_rat` is the name for these rationals, and `math_real` etc etc. Stuff like "sum of two nats is a nat" can be done by typeclass inference I would imagine.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 27 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134745401):
and "difference of two `is_nat`s is an `is_nat`" would *not* be an instance, because the difference would be an int.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 27 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134745472):
This would make a "number" class which is far more aligned with the kind of numbers which mathematicians are used to.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andreas Swerdlow (Sep 27 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134746770):
Might it be worth creating a “pedagogical” mathlib for things like this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andreas Swerdlow (Sep 27 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134747033):
Then we could avoid clogging up mathlib with several versions of the same thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Sep 27 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134754586):
A simpler solution may be to just rename the CS operators that do not correspond to their mathematical counterparts, e.g. go with `//` for truncated division as in Python, and `∸` for truncated subtraction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 27 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134754728):
we could certainly have `is_nat` and `is_int` typeclasses; they are valid in any type where `{nat,int}.cast` makes sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 27 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134754777):
the big question: are they data?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 27 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134754907):
You could conceivably use them to do integer or rational calculations on nondecidable types

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 27 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134756208):
I am assuming you can get data from the prop in this case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134756234):
(the prop being "this rational is definitely an integer, but I'm not telling you which")

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134756275):
certainly not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134756289):
it's just the numerator, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134756303):
Oh I see you're not talking about `rat`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134756307):
from rat, sure, but not from more interesting types like real

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134756309):
gotcha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 27 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134756347):
of course the lean version of `number` is just `A` where `A` has some niceness typeclass

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 27 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134756459):
I don't think Sebastian's solution will solve all of the problems I saw over the summer, although it would be a good way of reminding the students that something fishy is going on. Of course all divisions should have a weird dot on them because division by zero is not what mathematicians expect either :-) (not that any of them should be dividing by zero anyway...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 27 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134757204):
It would also make it a bit easier to look at a goal involving a bunch of coercions and a subtraction and understand where the subtraction is happening, at least to the extent that we would know whether or not it is "real" subtraction.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Leonardo de Moura (Sep 27 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134757867):
@**Kevin Buzzard** You may find this classical paper relevant: https://lamport.azurewebsites.net/pubs/lamport-types.pdf
Leslie, one of the authors, is now at MSR, and he still believes specification languages should be untyped. He has a system called TLA: https://lamport.azurewebsites.net/tla/tla.html

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 27 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134762284):
Newbie question: would "specification languages" be suitable for formalising mathematics? Or are they meant for other applications? (I thought Lamport mostly focused on hardware verification, but I might be way off the mark...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 27 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134762697):
I am also a newbie, but there appear to be a a few "mathematical" examples [in the TLA+ "Examples" repo](https://github.com/tlaplus/Examples). Most of the examples seem to be algorithmic in nature, but there are a few puzzles and also ["Two proofs of the fact that x+x is even, for any natural number x."](https://github.com/tlaplus/Examples/tree/master/specifications/sums_even).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 27 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134767673):
What's the difference between operators and functions, which means operators over all sets are consistent?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 28 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134807973):
@**Chris Hughes** You can quantify over functions even if they are unapplied: they are objects. Operators aren't objects. You can't have sets of operators and you can't quantify over them. A bit like universes in Lean, they are a different beast from the rest.


{% endraw %}
