---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20749leanisprettysweet.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [lean is pretty sweet](https://leanprover-community.github.io/archive/113488general/20749leanisprettysweet.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Andrew Ashworth (Mar 14 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123678987):
<p>i went back to doing some programming in fsharp since its the only mixed-paradigm language with any traction, and i really miss lean</p>

#### [ Andrew Ashworth (Mar 14 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679000):
<p>doing everything in the equivalent of <code>meta def</code> land is no fun</p>

#### [ Simon Hudon (Mar 14 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679053):
<p>What do you miss about trusted code?</p>

#### [ Andrew Ashworth (Mar 14 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679057):
<p>i like when the compiler spots issues for me and not runtime exceptions</p>

#### [ Andrew Ashworth (Mar 14 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679110):
<p>on the other hand being able to call into a bajillion .NET libraries is also pretty awesome... sigh</p>

#### [ Simon Hudon (Mar 14 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679118):
<p>I'm wondering if the type vs untyped languages will gain one dimension:</p>
<ul>
<li>(Haskell / F# proponent to JavaScript programmers): why does your language not have types? Come over to the civilized world!</li>
<li>(Lean user to Haskell / F# programmer): why can't you write proofs in your language? Come over to the civilized world!</li>
</ul>

#### [ Scott Morrison (Mar 14 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679125):
<p>Let's hope so. :-)</p>

#### [ Simon Hudon (Mar 14 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679180):
<blockquote>
<p>on the other hand being able to call into a bajillion .NET libraries is also pretty awesome... sigh</p>
</blockquote>
<p>True but doesn't it scare you how weak their contracts are? Does this function terminate? Does it perform io? Does it mutate state? Does it satisfy beautiful laws? Who knows! It's just a chunk of code that does stuff</p>

#### [ Andrew Ashworth (Mar 14 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679182):
<p>the important thing is that it's a chunk of code i didn't write</p>

#### [ Andrew Ashworth (Mar 14 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679190):
<p>i mean, i write all my quick and dirty scripts in python for that reason</p>

#### [ Mario Carneiro (Mar 14 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679394):
<p>For me it's more than just being able to write proofs. I think a better characterization is the ability to have really expressive types, like a type of prime numbers, or expressing pre/post-conditions of a function in the type</p>

#### [ Simon Hudon (Mar 14 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679529):
<p>That is pretty cool, true</p>

#### [ Simon Hudon (Mar 14 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679531):
<p>I especially like that type classes come with laws</p>

#### [ Andrew Ashworth (Mar 14 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679538):
<p>i hope the ffi story is good in lean 4, then you could use lean for more than just standalone projects</p>

#### [ Mario Carneiro (Mar 14 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679673):
<p>and of course, being able to substantively make use of a nontrivial precondition, like if you have a list and a proof it is <code>[]</code> then you don't even have to supply the cons case</p>

#### [ Mario Carneiro (Mar 14 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679730):
<p>and there are no apologetics or assertions or unreachables</p>

#### [ Andrew Ashworth (Mar 14 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679745):
<p>too bad lean can't bootstrap lean</p>

#### [ Simon Hudon (Mar 14 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679746):
<p>What do you mean by no assertions?</p>

#### [ Simon Hudon (Mar 14 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679753):
<p>Do you mean that the assertions are not checked dynamically?</p>

#### [ Mario Carneiro (Mar 14 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679813):
<p>In any other programming language, if I have a division function with a precondition, I still have to handle the case when the precondition is violated, and maybe throw an assertion violation or unreachable exception. The compiler can't prove that you are following your precondition so it has to be done</p>

#### [ Mario Carneiro (Mar 14 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679822):
<p>but in lean I can just omit the case and it can prove that the branch is impossible, so it's just not a code path</p>

#### [ Simon Hudon (Mar 14 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123679883):
<p>Darn! You're right! I really don't miss that! Especially the Java flavor. Luckily, I haven't touched Java in years</p>

#### [ Andrew Ashworth (Mar 14 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123680025):
<p>if you're on the JVM, scala isn't bad</p>

#### [ Andrew Ashworth (Mar 14 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123680034):
<p>haven't had a chance to use it very much though</p>

#### [ Andrew Ashworth (Mar 14 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123680099):
<p>but i know people who speak highly of it</p>

#### [ Scott Morrison (Mar 14 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123680227):
<p>I've written a lot of Scala, and in particular a lot of maths in Scala. I'm hoping to never go back, however. :-)</p>

#### [ Scott Morrison (Mar 14 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123684915):
<p>(It is great, but Lean is greater still.)</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123695407):
<blockquote>
<p>I've written a lot of Scala, and in particular a lot of maths in Scala. I'm hoping to never go back, however. :-)</p>
</blockquote>
<p>I was trying to do something like this in scala, <a href="https://scalafiddle.io/sf/enaGqD4/0" target="_blank" title="https://scalafiddle.io/sf/enaGqD4/0">https://scalafiddle.io/sf/enaGqD4/0</a> I hated myself why I thought it might work, and original version, without defining natural induction is this <a href="https://scalafiddle.io/sf/A56KTgD/1" target="_blank" title="https://scalafiddle.io/sf/A56KTgD/1">https://scalafiddle.io/sf/A56KTgD/1</a> (I made lot of changes its not compiling, I dont remember now what I did and its completely incomprehensible now)</p>

#### [ Mario Carneiro (Mar 14 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123695549):
<p>This reminds me of those people that wrote a BF interpreter in C++ template language</p>

#### [ VinothKumar Raman (Mar 14 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20is%20pretty%20sweet/near/123695640):
<p>Yea, it felt more like programming in BF itself. But I understand a lot about types now after the ordeal.</p>


{% endraw %}
