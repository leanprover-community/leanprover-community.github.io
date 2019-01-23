---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30756monadrefactoring.html
---

## Stream: [general](index.html)
### Topic: [monad refactoring](30756monadrefactoring.html)

---


{% raw %}
#### [ Patrick Massot (Mar 01 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123127367):
@**Sebastian Ullrich** woke up with a lot of homework... Does anyone knows whether basic users like me will see any difference after merging this?

#### [ Simon Hudon (Mar 01 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123127532):
Are you referring to the commits in his own fork?

#### [ Sean Leather (Mar 01 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123127592):
To avoid ambiguity and for posterity: https://github.com/leanprover/lean/pull/1881

#### [ Simon Hudon (Mar 01 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123127763):
Thanks @**Sean Leather**

#### [ Sean Leather (Mar 01 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123127842):
```quote
woke up with a lot of homework... Does anyone knows whether basic users like me will see any difference after merging this?
```
@**Patrick Massot**: I'm guessing you're referring to Leo's comments, of which there were a lot.

#### [ Patrick Massot (Mar 01 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123127851):
Yes.

#### [ Patrick Massot (Mar 01 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128035):
There are a lot of comments but there is a *lot* of code in this PR.

#### [ Mario Carneiro (Mar 01 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128054):
I'm also curious about this. @**Sebastian Ullrich** , could you maybe discuss or point to a place where you discuss the purpose of the monad refactoring project? From what little I can garner from Leo's comments, it looks like you are maybe adding more advanced monad features from Haskell like monad transformers, the continuation monad and call/cc?

#### [ Simon Hudon (Mar 01 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128087):
I think you'll see a difference (hopefully for the best) if you use Lean to write programs. Otherwise, I don't think you'll see a difference

#### [ Patrick Massot (Mar 01 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128109):
It's very hard to resist going to Leo's most cryptic comment and add: "Yeah, I wondered about that too".

#### [ Patrick Massot (Mar 01 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128115):
What do you mean "write program"? Write a tactic?

#### [ Simon Hudon (Mar 01 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128135):
I think not much if you write tactics. More if you use Lean as a functional programming language (with or without much verification)

#### [ Patrick Massot (Mar 01 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128181):
Are there people doing that?

#### [ Sean Leather (Mar 01 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128182):
As in I/O?! :scream:

#### [ Simon Hudon (Mar 01 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128187):
On top of my head, there's me

#### [ Simon Hudon (Mar 01 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128230):
I/O or other kind of code. There's a lot you can do with monads

#### [ Simon Hudon (Mar 01 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128232):
Why do you seem so scared of I/O?

#### [ Patrick Massot (Mar 01 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128233):
Doesn't sound functional to me

#### [ Sean Leather (Mar 01 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128234):
I meant, as in writing a “real” program that does I/O, not as in using the `io` monad... :wink:

#### [ Simon Hudon (Mar 01 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128241):
```quote
Doesn't sound functional to me
```
Why not?

#### [ Sean Leather (Mar 01 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128285):
```quote
Why do you seem so scared of I/O?
```
Because of the meme that theorem-proving languages are generally only used for proofs and type-checking.

#### [ Kevin Buzzard (Mar 01 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128287):
```quote
```quote
Doesn't sound functional to me
```
Why not?
```
Every article I read about functional programming makes a huge fuss about i/o. That's probably what he means. In contrast to procedural languages, where the first program you ever see is "print hello world"

#### [ Patrick Massot (Mar 01 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128290):
I thought functional programming swears to be isolated from real world

#### [ Sean Leather (Mar 01 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128301):
```quote
I thought functional programming swears to be isolated from real world
```
That's a myth and a well-disproven one at that.

#### [ Simon Hudon (Mar 01 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128303):
That was true of Haskell before they invented monads but the `io` monad makes I/O into a perfectly ok part of pure functional programming.

#### [ Simon Hudon (Mar 01 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128365):
Some people write OSs and web servers using purely functional programming. It looks pretty real to me and their users :)

#### [ Sean Leather (Mar 01 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128373):
It's funny how, as you climb up the ladder of high-level programming languages, each level above seems to be less useful than the level you're on, at least until you understand it.

#### [ Patrick Massot (Mar 01 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128376):
What's funny is right now I'm staring at my NodeJS I/O code which doesn't work. I don't know why it insisted trying to read all 29668 files in this directory before starting to work on the first one (and then FATAL ERROR: CALL_AND_RETRY_LAST Allocation failed - JavaScript heap out of memory)

#### [ Simon Hudon (Mar 01 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128378):
Yeah! And as I climb up, I get nervous about climbing down. Everything makes sense up here!

#### [ Sean Leather (Mar 01 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128420):
Yes, you can get complacent with all of the protection you have.

#### [ Patrick Massot (Mar 01 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128433):
I love functional programming languages guys. They are brothers to mathematicians. We also think what we do is more powerful and more beautiful than what other do. And normal people think what we do is un-understandable and useless

#### [ Simon Hudon (Mar 01 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128434):
I have a friend whom i'm mentoring with Haskell. He works with JavaScript. He's more courageous than me. I don't think I'd want to go back to object oriented programming ... unless it was generated from afull functional specification

#### [ Simon Hudon (Mar 01 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128479):
And we're also insufferable when coming in contact with other communities

#### [ Patrick Massot (Mar 01 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128484):
In my case the trouble is not object oriented programming, it's asynchronicity

#### [ Simon Hudon (Mar 01 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128485):
"You're getting into trouble because your pointers are aliasing each other? How quaint!"

#### [ Sean Leather (Mar 01 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128527):
Aliased pointers in JavaScript? :confused:

#### [ Simon Hudon (Mar 01 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128532):
Object oriented programming is supposed to be a solution (some might disagree *cough cough*) but asynchronicity is an actual programming challenge ... at the center of my research as it happens

#### [ Simon Hudon (Mar 01 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128538):
```quote
Aliased pointers in JavaScript? :confused:
```
References to objects, etc. I'm fairly sure they don't have a complete value semantics

#### [ Patrick Massot (Mar 01 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128579):
It's fun here but I need to take a shower, see you

#### [ Simon Hudon (Mar 01 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128585):
Alright! Let's be insufferable later! :grin:

#### [ Sebastian Ullrich (Mar 01 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123131312):
I'll leave this link as a hint to our motivation... :P https://github.com/Kha/syntax/blob/master/macro.lean#L5

#### [ Scott Morrison (Mar 01 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123134401):
Hi @**Sebastian Ullrich** , is there some explanation I can read of what you did to `bind`?

#### [ Sebastian Ullrich (Mar 01 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123134448):
@**Scott Morrison** Does the test file help? https://github.com/leanprover/lean/blob/master/tests/lean/run/rebind_bind.lean

#### [ Scott Morrison (Mar 01 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123134454):
There are lots of places mathlib has broken, e.g.
```lean
theorem length_bind (l : list α) (f : α → list β) : length (bind l f) = sum (map (length ∘ f) l)
```

#### [ Scott Morrison (Mar 01 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123134460):
Where is says
````
type mismatch at application
  l >>= f
term
  f
has type
  α → list β : Type (max u v)
but is expected to have type
  α → list ?m_1 : Type u
````

#### [ Sebastian Ullrich (Mar 01 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123134518):
Ah, `list.bind` is `protected` now, as it should have been from the beginning

#### [ Scott Morrison (Mar 01 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123134572):
So it should use ...?

#### [ Sebastian Ullrich (Mar 01 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123134588):
You can replace `bind` with `list.bind`

#### [ Scott Morrison (Mar 01 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123134589):
thanks

#### [ Sebastian Ullrich (Mar 01 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123134636):
But I would argue that we should usually prefer using the generic operations (i.e. `bind`/`>>=` here) even if it means that alpha and beta have to live in the same universe in this case

#### [ Sebastian Ullrich (Mar 01 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123134637):
@**Mario Carneiro** thoughts?

#### [ Scott Morrison (Mar 01 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123135235):
The other place I'm seeing trouble from the monad refactoring is in mathlib's `data/encodable.lean`.

#### [ Scott Morrison (Mar 01 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123135285):
where it looks like the problem is that there are too many `bind`s available

#### [ Scott Morrison (Mar 01 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123135288):
and the `do` notation is now failing as a result.

#### [ Sebastian Ullrich (Mar 01 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123136383):
I guess `option.bind` should be protected as well? Gaah.

#### [ Mario Carneiro (Mar 01 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123140100):
The "named" bind is there in part exactly for this universe distinguishing thing. There are times when it matters, and you need the polymorphic version. For most of these operations, there is also a symbol name for them, which is preferred when universes don't matter or you are over a known structure.

#### [ Sebastian Ullrich (Mar 01 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123140604):
Yah, it's the curse of the monad. I'll mark `option.bind` as protected then.

#### [ Simon Hudon (Mar 01 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123157560):
I took the liberty of commenting on your pull request. Is this the best way to interact on this subject or should I stick to Zulip / Gitter?

#### [ Sebastian Ullrich (Mar 02 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123159187):
That's fine, I just didn't get to it yet

#### [ Simon Hudon (Mar 02 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123159201):
No worries. I just don't want to be intrusive by commenting directly on github

#### [ Sebastian Ullrich (Mar 02 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123159573):
I'm happy for any feedback by experienced Haskell programmers, since neither Leo nor me is one of them

#### [ Simon Hudon (Mar 02 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123159859):
Excellent then :) I'll keep them coming. In passing, I am truly amazed by the language that you guys came up with. Learning Haskell was like a religious conversion for me and it ended a three year programming hiatus. Lean is comparing really well

#### [ Sebastian Ullrich (Mar 02 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123160171):
Thank you :smile:


{% endraw %}
