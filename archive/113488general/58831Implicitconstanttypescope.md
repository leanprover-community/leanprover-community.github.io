---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58831Implicitconstanttypescope.html
---

## [general](index.html)
### [Implicit constant-type scope](58831Implicitconstanttypescope.html)

#### [Moses Schönfinkel (Mar 14 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123699670):
Is there a way to tell lean that every numeric constant (a'la `1` `42`) I use in <some scope> is actually from `Z` rather than `N` or am I stuck with `(0 : Z)`? (Coq has `Open Scope ZScope` command that lets me do this sort of thing.)

#### [Kevin Buzzard (Mar 14 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123704252):
I asked this a while ago and got the response "3 means 3:N by default and this is wired in". Maybe this is a question for Lean 4 devs?

#### [Kevin Buzzard (Mar 14 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123710068):
PS as a mathematician I would say that N in general stinks (it's not even a ring) and I know many common (to mathematicians) use cases where every single numeral would be a real number by default, and it would be really lovely just to be able to write 7, 5/2, -0.26 and e*pi^2 and have them all interpreted as real numbers by default. This is what mathematicians are used to (e.g. in python, maple etc). I would be happy to jump through hoops on line 1 in order to get this functionality for the rest of the file.

#### [Kevin Buzzard (Mar 14 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123710200):
PS Chris Hughes implemented sin and cos and exp in Lean so we have formal definitions of e and pi (they could also be trivially defined as infinite series, e.g. pi = 4 (1 - 1/3 + 1/5 + 1/7 - 1/9 + ...), e = 1/0! + 1/1! + 1/2! + 1/3! + ...)

#### [Kevin Buzzard (Mar 14 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123710219):
(modulo proofs that these things converge :-/

#### [Kevin Buzzard (Mar 14 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123710220):
)

#### [Andrew Ashworth (Mar 14 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123711262):
python numbers are reals? maybe you mean the rationals

#### [Kevin Buzzard (Mar 14 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123711343):
I think python's math.pi is real ;-)

#### [Kevin Buzzard (Mar 14 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123711346):
The terrifying is that in maths there is only one 5/2, and it's the rational real complex 5/2.

#### [Kevin Buzzard (Mar 14 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123711404):
```
>>> type(2.6)
<type 'float'>
>>> 
```

#### [Kevin Buzzard (Mar 14 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123711507):
```
>>> type(7/2)
<class 'float'>
>>> 
```
in python3

#### [Kevin Buzzard (Mar 14 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123711550):
and in python2 it's an int ;-) I think there was a certain amount of fuss made about the change...

#### [Andrew Ashworth (Mar 14 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123711621):
the problem with the default type being `rat` (i.e. float) is that for many cs applications, you want to recurse on the size of a set

#### [Andrew Ashworth (Mar 14 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123711630):
for that reason, I think that's why `nat` is the default

#### [Andrew Ashworth (Mar 14 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123711765):
fsharp uses `int` as the default value for numeric constants, if you want a `float` you need to write `2.` for example

#### [Kevin Buzzard (Mar 14 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123711859):
But in mathematics a very common use case is "here we are doing a question about vectors in R^3 (R the real numbers). So let's let v be the vector (1,2,3) and now let's multiply it by 2" and whilst we know the CS tricks of putting in a decimal point, we don't need them there because on line 1 we just said that every number was a real number until further notice.

#### [Kevin Buzzard (Mar 14 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123711892):
That is what mathematics undergraduate example sheets look like, so +1 to Mr Schönfinkel

#### [Kevin Buzzard (Mar 14 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123711983):
PS whilst we both know that a float is neither a rat nor a real, I think that reals are a better approximation ;-)

#### [Kevin Buzzard (Mar 14 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123711992):
```
>>> type(math.pi)
<type 'float'>
>>> 
```

#### [Andrew Ashworth (Mar 14 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123711996):
woaaaah

#### [Andrew Ashworth (Mar 14 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712009):
math.pi can't ever be a real

#### [Andrew Ashworth (Mar 14 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712017):
in a very real sense it's an approximation like `22/7`

#### [Kevin Buzzard (Mar 14 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712024):
in Lean math.pi can be a real

#### [Andrew Ashworth (Mar 14 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712065):
in python, at least

#### [Kevin Buzzard (Mar 14 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712072):
?

#### [Andrew Ashworth (Mar 14 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712082):
in python, math.pi is a rational approximation to pi with 32 bits of precision

#### [Kevin Buzzard (Mar 14 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712087):
it's a real in the sense that my 15 year old son can take its square root in python using `math.sqrt`

#### [Kevin Buzzard (Mar 14 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712095):
whilst knowing that the square root of a rational is not rational

#### [Kevin Buzzard (Mar 14 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712097):
in general

#### [Andrew Ashworth (Mar 14 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712250):
ah, i see what you mean. still in my brain i've always though of float as actually being `rat`

#### [Andrew Ashworth (Mar 14 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712361):
if we had a constructive theory of the reals, we could compute with them!

#### [Andrew Ashworth (Mar 14 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712462):
and then maybe we could relate that in some way to the actual computer implementation of floating point numbers... and i'd be pretty happy

#### [Kevin Buzzard (Mar 14 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712589):
the map from floats to reals, I hear, stinks. Floats almost guaranteed not to be associative for example: `N + (-N + epsilon) != (N + -N) + epsilon`

#### [Kevin Buzzard (Mar 14 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712590):
the LHS being zero

#### [Kevin Buzzard (Mar 14 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712648):
so I think this rules out being able to write down any map which commutes with addition

#### [Kevin Buzzard (Mar 14 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712667):
Maybe a better idea is just to implement floats in Lean, which might well already have been done

#### [Kevin Buzzard (Mar 14 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712676):
although quite who is interested in floats nowadays I don't know ;-)

#### [Andrew Ashworth (Mar 14 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712729):
i know you meant that jokingly but float verification is a huge issue in computer hardware

#### [Andrew Ashworth (Mar 14 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712746):
an error in how Intel handled floating point numbers cost them $475 million in 1994

#### [Kevin Buzzard (Mar 14 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712805):
Oh I remember it :-) It was all over usenet :-)

#### [Kevin Buzzard (Mar 14 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123712837):
"Ten reasons why Intel's floating point error is a problem.
1.0000000000000000034737) People doing astronomy need calculations to high accuracy
1.9999999999999999994734) ...
3.0000000000000000007567) ...

etc etc

#### [Moses Schönfinkel (Mar 15 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Implicit constant-type scope/near/123746096):
Here's my favourite mental model of when to not worry about IEEE floats. When you use it for natural quantities that one needs to measure, they implicitly capture the imprecision. So when you want to model something like weight and you say that my thing weighs 1 kilogram, floats will give you some approximation to it and that should be fine considering pretty much nothing weighs **exactly** 1 kilogram anyway, probably even the platinum-irridium thing that is supposed to weigh exactly 1 kilogram (in our corner of the universe). It's only man-made entities where floats become a problem, because those were made from our understanding of fractions and reals and we would expect them to behave accordingly (the obvious example is balance in your bank account, you don't want floats to randomly round nor not add associatively).

