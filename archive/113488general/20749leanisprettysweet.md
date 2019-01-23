---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20749leanisprettysweet.html
---

## Stream: [general](index.html)
### Topic: [lean is pretty sweet](20749leanisprettysweet.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 14 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123678987):
i went back to doing some programming in fsharp since its the only mixed-paradigm language with any traction, and i really miss lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 14 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679000):
doing everything in the equivalent of `meta def` land is no fun

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 14 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679053):
What do you miss about trusted code?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 14 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679057):
i like when the compiler spots issues for me and not runtime exceptions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 14 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679110):
on the other hand being able to call into a bajillion .NET libraries is also pretty awesome... sigh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 14 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679118):
I'm wondering if the type vs untyped languages will gain one dimension:

- (Haskell / F# proponent to JavaScript programmers): why does your language not have types? Come over to the civilized world!
- (Lean user to Haskell / F# programmer): why can't you write proofs in your language? Come over to the civilized world!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 14 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679125):
Let's hope so. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 14 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679180):
```quote
on the other hand being able to call into a bajillion .NET libraries is also pretty awesome... sigh
```
True but doesn't it scare you how weak their contracts are? Does this function terminate? Does it perform io? Does it mutate state? Does it satisfy beautiful laws? Who knows! It's just a chunk of code that does stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 14 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679182):
the important thing is that it's a chunk of code i didn't write

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 14 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679190):
i mean, i write all my quick and dirty scripts in python for that reason

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 14 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679394):
For me it's more than just being able to write proofs. I think a better characterization is the ability to have really expressive types, like a type of prime numbers, or expressing pre/post-conditions of a function in the type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 14 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679529):
That is pretty cool, true

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 14 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679531):
I especially like that type classes come with laws

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 14 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679538):
i hope the ffi story is good in lean 4, then you could use lean for more than just standalone projects

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 14 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679673):
and of course, being able to substantively make use of a nontrivial precondition, like if you have a list and a proof it is `[]` then you don't even have to supply the cons case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 14 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679730):
and there are no apologetics or assertions or unreachables

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 14 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679745):
too bad lean can't bootstrap lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 14 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679746):
What do you mean by no assertions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 14 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679753):
Do you mean that the assertions are not checked dynamically?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 14 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679813):
In any other programming language, if I have a division function with a precondition, I still have to handle the case when the precondition is violated, and maybe throw an assertion violation or unreachable exception. The compiler can't prove that you are following your precondition so it has to be done

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 14 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679822):
but in lean I can just omit the case and it can prove that the branch is impossible, so it's just not a code path

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 14 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679883):
Darn! You're right! I really don't miss that! Especially the Java flavor. Luckily, I haven't touched Java in years

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 14 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123680025):
if you're on the JVM, scala isn't bad

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 14 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123680034):
haven't had a chance to use it very much though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 14 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123680099):
but i know people who speak highly of it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 14 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123680227):
I've written a lot of Scala, and in particular a lot of maths in Scala. I'm hoping to never go back, however. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 14 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123684915):
(It is great, but Lean is greater still.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) VinothKumar Raman (Mar 14 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123695407):
```quote
I've written a lot of Scala, and in particular a lot of maths in Scala. I'm hoping to never go back, however. :-)
```
I was trying to do something like this in scala, https://scalafiddle.io/sf/enaGqD4/0 I hated myself why I thought it might work, and original version, without defining natural induction is this https://scalafiddle.io/sf/A56KTgD/1 (I made lot of changes its not compiling, I dont remember now what I did and its completely incomprehensible now)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 14 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123695549):
This reminds me of those people that wrote a BF interpreter in C++ template language

#### [![Click to go to Zulip](../../assets/img/zulip2.png) VinothKumar Raman (Mar 14 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123695640):
Yea, it felt more like programming in BF itself. But I understand a lot about types now after the ordeal.


{% endraw %}
