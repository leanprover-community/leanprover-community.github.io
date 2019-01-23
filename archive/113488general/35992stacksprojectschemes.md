---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35992stacksprojectschemes.html
---

## Stream: [general](index.html)
### Topic: [stacks project / schemes](35992stacksprojectschemes.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123081857):
Thought this was worth its own topic because we all know there are people here who are less interested in the maths side of things. Here's an update.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123081905):
Kenny and I nearly have schemes. Not in a "just about ready for mathlib" sort of way -- far from it -- but in a "the mathematically correct definition" sort of way.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123081956):
It will need a lot more work before it goes anywhere near mathlib, but I am not going to do that work quite yet because for deadline reasons it would be nice to get perfectoid spaces before 10th March, or at least to get some way towards them. After that we can think about tidying up and deciding which bits mathlib might want and in what form.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082015):
The reason I'm posting is because I need to make a call on categories. At the end of the day I currently need sheaves of commutative rings (for the _definition_ of a scheme), and to actually prove anything at all I need sheaves of modules for these rings. For perfectoid spaces I will need sheaves of topological rings on a site.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082023):
So do I go with sheaves taking values in categories or do I just muddle on?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082041):
If I go with sheaves taking values in categories then to put it bluntly it simply raises the bar even higher to getting anything in to mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082042):
Now Patrick has urged to me to get this into mathlib-ready form, and I'll start on this after the 11th.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Feb 28 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082046):
Here's a question: what is the least common denominator of all the things you need sheaves of?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Feb 28 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082099):
My hope is that it is at least a concrete category

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Feb 28 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082110):
If you project needing 3+ different kinds of sheaves, that's sufficient for making a single generalization, but it's not immediate that this generalization should be over categories in the usual sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082147):
But this has always been an independent experiment for me -- can we actually even define a scheme / perfectoid space in Lean? For me that is an interesting independent question. I don't think it is for Mario, because he looks at maths very differently and, not unreasonably, I don't think he can tell the difference between a perfectoid space and a topological space in some sense -- they're both structures with a bunch of axioms to him. And for some reason he seems very much focussed on theorems rather than definitions -- a theorem for him is proof that the definition works, whereas if I know as a mathematician that a definition is correct then for me that might be enough.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082163):
So there is certainly the possibility that my conclusion is "look, here's a definition" and Mario's response is "who cares?". And the definition might just then sit there for months just being something that mathematicians can look and go "oh look what they can do now, how fancy, that's a million miles from the odd order theorem isn't it".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082209):
The Least Common Denominator depends very much on how far you want to go.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Feb 28 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082211):
I think you are right in that assessment. It seems to me obvious that one can make a definition of scheme / perfectoid space in lean; that's obviously within Lean's capabilities. The question is only if one can make a good or useful definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082212):
The Weil Conjectures are a famous theorem.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082227):
For them you ideally would have sheaves on a more general object than a topological space and then take the derived category.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082229):
My gut feeling is that by that point you want to be using categories.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Feb 28 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082230):
by that point...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Feb 28 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082233):
I don't think you should be afraid of later revision

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Feb 28 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082273):
have goals, and plan for them. If you want the Weil Conjectures, then go for it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082289):
```quote
I think you are right in that assessment. It seems to me obvious that one can make a definition of scheme / perfectoid space in lean; that's obviously within Lean's capabilities. The question is only if one can make a good or useful definition
```
No, that's just one question. Another question is how to get mathematicians talking about Lean. And we already have ample evidence that proving a theorem which is 400 pages of ingenious but relatively straightforward calculations in group theory and which was done by mathematicians before all of us were born, does not do it. But in the math community there is huge excitement about perfectoid spaces because they are new and they are demolishing bits of the Langlands Programme which people thought were hitherto inaccessible. They are *fashionable*.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Feb 28 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082295):
Is there positive evidence that writing down a definition will interest mathematicians?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082296):
This is the part that you (Mario) cannot see at all and this is unsurprising given where you are sitting and your background

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082335):
There is positive evidence that not writing down a definition will not interest them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Feb 28 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082337):
In a sense it seems much the same as proving an old theorem formally - whoop-de-doo you formalized a definition we all know

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082338):
I am going to give a talk at an undergraduate conference on the 11th, a theoretical talk, an introduction to perfectoid spaces and what they can do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082349):
and I think it would be cool to unveil the definition there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082355):
There is a difference which you can't see.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082360):
Proving an _old_ theorem formally -- you formalised a theorem that we all understand the statement of and which was proved before we were all born

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082406):
Making a _new_ definition which is extremely complex and most mathematicians don't understand has much more of an air of mystery about it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082411):
There is a subtlety.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Feb 28 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082415):
I assume that perfectoid spaces are not themselves the object of perfectoid theory, such as it is. Presumably they are being used in some way to get things done, some proof strategy that harnesses the power of the definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082425):
Currently the word "perfectoid space" to most mathematicians means "abstract structure whose definition I have not read and would probably not understand if I did read, but I know that in the number theory community everyone is talking about them and I get the feeling that there is a general sense of excitement happening right now"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082429):
this is absolutely absolutely the opposite of everyone's feeling about the odd order theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Feb 28 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082472):
I'm obviously in the wrong place to make such pronouncements, but I won't be convinced you've done a thing with substance until you mimic such proofs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082475):
Well there is a basic "perfectoid theory" which was only worked out a few years ago

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082483):
Mario I am not suggesting I have done anything of substance with perfectoid spaces even if I manage to define them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082486):
But I am suggesting that they might be a selling point.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082496):
Because in contrast to the odd order theorem, which everyone understands and nobody cares about

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Feb 28 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082497):
I freely admit I don't understand what makes a thing a selling point for mathematicians

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082499):
perfectoid spaces have the property that nobody understands them and a lot of people care about them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082500):
```quote
I freely admit I don't understand what makes a thing a selling point for mathematicians
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082540):
Right, it's all just structures to you.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082550):
It would be like me saying "OK so you wrote a search engine and you wrote a space invaders game, they're all just computer programs at the end of the day though"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082554):
if I just couldn't tell the difference between them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082555):
because I never used either of them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082566):
I don't expect you to see any difference between the definition of a group and the definition of a perfectoid space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082571):
however I do think you should know that one is more fashionable than the other currently, in some circles.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Feb 28 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082615):
```quote
Currently the word "perfectoid space" to most mathematicians means "abstract structure whose definition I have not read and would probably not understand if I did read, but I know that in the number theory community everyone is talking about them and I get the feeling that there is a general sense of excitement happening right now"
```
I can confirm this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Feb 28 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082620):
Okay, by that analogy the proofs is where you "run the program" of the definition, that's where the differences become obvious

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Feb 28 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082631):
Otherwise I'm just staring at a bunch of code for space invaders / google, and I don't understand what does what or why

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082670):
Right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082684):
But on the other hand if you are in a community and there's a whole bunch of other people that you respect getting very excited by some computer program which you are not competent enough to use, then this might rub off.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082723):
And if you're then on some grant committee that is deciding where the money is going and you see a proposal which mentions this fancy new program which you know there are experts raving about then perhaps you are favourably inclined towards that proposal even though you can't actually understand it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Feb 28 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082729):
I think you need to get famous number theorist X involved in your project then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082733):
I think I should write the definition first!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Feb 28 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082743):
```quote
I think you need to get famous number theorist X involved in your project then
```
Yeah, who has Scholze's phone number?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Feb 28 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082745):
*That* would have an impact

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082746):
I exchange emails with him from time to time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082748):
but I've not mentioned this to him yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Feb 28 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082750):
Imagine Peter Scholze in Rio explaining he is now using Lean as a day to day tool

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082792):
That is not going to happen, but when I finish it I will certainly mention it to him.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Feb 28 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082798):
[Note to non-mathematician: Rio is where Scholze will get his Fields medal this summer]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082799):
It would be interesting to hear his opinions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082803):
The non-mathematicians have all muted this thread ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Feb 28 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082811):
Damn Zulip!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082818):
This is exactly the sort of chat that takes up 200 messages on gitter and all the poor CS guys just have to scroll through and hope that they see the CS question somewhere in the middle that we all ignore

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082864):
I think that if we figure out how to make these topics work properly then it might be of benefit to everyone.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082877):
Anyway, Patrick and Mario I suspect you have different opinions on this issue. Let's imagine I triumphantly define a perfectoid space structure at 4am on the morning of 11th March and then decide to move on to something else for a month

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082920):
and it's manifestly not mathlib-ready and I don't have the time to even prove Lemma 1 about perfectoid spaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082927):
Mario is then manifestly not interested in adding the definition to mathlib, and he has explained his reasons above.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082929):
Patrick would you be happy with it just sitting there in some random repo on my github?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082934):
a valid but potentially unusable definition?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Feb 28 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082936):
I wouldn't be happy, but who cares?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082937):
My plan is to make the definition and then just tell a bunch of undergraduates about it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082939):
and maybe some graduate students

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082940):
until I find one or two people who are interested in taking it further.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082981):
Undergraduates do do pretty weird things nowadays.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082994):
Probably people have seen MO questions of the form "I am an undergraduate but I have been reading Lurie's book and I have a question about infinity-categories"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123082996):
and sometimes the questions are just plain stupid

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123083002):
but sometimes they are graduate student level

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123083007):
For me this is evidence of a big change in the way people are accessing and learning mathematics.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123083010):
Undergraduates have access to so much information now because of the web, so they find random things and attempt to engage with them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Feb 28 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123083012):
But this will happen one month after your talk. And by that time your lone repo won't be compiling against current Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123083056):
I don't care

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123083062):
because I am going to fix this problem if necessary by fixing which version of Lean I am using

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123083064):
I would really really love for Leo to release 3.4.0. I would stick there like a shot.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123083070):
I am going to make a bunch of teaching material which will all run on some fixed version of Lean and then actively urge the undergrads not to upgrade.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123083071):
That's why I am excited about the project which is going to make old nightlies accessible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123083114):
I just think that for certain people, a formal definition of a perfectoid space will be a really interesting looking carrot.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123083122):
Schemes was enough of a carrot for Kenny, for example.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123083167):
But actually I came here to ask whether I should use @**Scott Morrison** 's category theory library or whether it's not yet ready. That's the call I have to make at the minute.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123083168):
If all I want is schemes then all I need is sheaves of rings which I can do by hand.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123083169):
But this doesn't scale.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Feb 28 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123083179):
People who care about schemes or perfectoid spaces will want the latest advances in Lean automatisation. They won't be happy with Lean 3.4.0

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123083465):
I see.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Feb 28 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123084651):
```quote
Proving an _old_ theorem formally -- you formalised a theorem that we all understand the statement of and which was proved before we were all born
```
Come on @**Assia Mahboubi** fight back!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Feb 28 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123085930):
@**Kevin Buzzard**, agreeing a bit with @**Patrick Massot** , I do think it's important that developments end up in mathlib (or otherwise in repositories with multiple contributors who may maintain things). In the current Lean ecosystem, bitrot happens incredibly quickly (in fact so much so that I think I actually agree with Leo --- possibly all of the current mathlib is doomed to need complete rewriting several times over in the next few years).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Feb 28 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123086050):
It leaves me genuinely uncertain about the best path. I think you're fundamentally right in wanting to make a dash towards an important and impressive part of modern mathematics. I agree with everything you say concerning the odd order theorem. (The initial human proof of the odd order theorem was in some ways a huge disappointment --- it was one of the first times humans encountered an interesting theorem whose shortest proof was really long. Saying that computers are helpful for doing tedious mathematics is not really a selling point.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Feb 28 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123086093):
But I'm also pretty sceptical that the March 11 dash you have in mind is going to have much effect. It's too likely that the code will fall apart quickly afterwards, or otherwise be unusable because it was written hurriedly.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Feb 28 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123086228):
I would like it to have an effect --- what we should dream about is a "mathoverflow effect", whereby one day a new thing appeared in the world that everyone realised they'd always wanted. I think there are potentially a huge number of students out there who would be interested in contributing to Lean libraries. However in combination with any "publicity", we would also need to have better strategy in place for teaching them how to work in Lean, and to productively organise their work. The current Lean community is realistically not yet ready for either of those.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Feb 28 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123086239):
It's great that documentation is coming along. TPIL is a great resource, and it's fantastic to see the mathlib documentation growing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Feb 28 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123086293):
Unfortunately writing good Lean code is really hard (I still write lots of crappy code, after 18 months of learning Lean), and so any influx of new people could potentially just overwhelm those people in the community who can actually review PRs.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Feb 28 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123086306):
Finally, to try to answer your question, @**Kevin Buzzard**, I am trying to get the category theory library ready to PR into mathlib. But collaborators and postdocs and students are starting (ha!) to notice that I'm not getting much maths done...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Feb 28 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123086418):
Hearing you wanting it of course motivates me, for better or worse. I think building good foundations (e.g. using category theory to avoid proving everything 5 times over when setting up algebraic geometry) will be really helpful.

Also, I'm still a little proud of how few proofs I have in my library (i.e. how many are proved by `obviously` with little or no human intervention). :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Feb 28 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123086446):
Oh -- and in some interesting news -- two mathematicians here at ANU, after coming to my undergraduate students' talks (on implementing Euclidean domains, and the first iso theorem for groups), said they were going home to install Lean over the weekend. There's hope. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123087019):
```quote
I would like it to have an effect --- what we should dream about is a "mathoverflow effect", whereby one day a new thing appeared in the world that everyone realised they'd always wanted. I think there are potentially a huge number of students out there who would be interested in contributing to Lean libraries. However in combination with any "publicity", we would also need to have better strategy in place for teaching them how to work in Lean, and to productively organise their work. The current Lean community is realistically not yet ready for either of those.
```
I am going to dedicate a lot of time over the summer to writing documentation for undergraduate mathematicians introducing them to how to use Lean via my introduction to proof course.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123087082):
```quote
```quote
Proving an _old_ theorem formally -- you formalised a theorem that we all understand the statement of and which was proved before we were all born
```
Come on @**Assia Mahboubi** fight back!
```
Ha ha! I was of course taking a very extreme viewpoint which I do not 100% believe in myself. I just wanted to highlight some of the obvious differences between defining a perfectoid space and proving the odd order theorem, even though "they're both computer programs".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (Feb 28 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123089878):
Hi @**Patrick Massot** ! Thanks for having pointed me to this new forum and thread!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (Feb 28 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123089937):
Hi @**Kevin Buzzard** ! Thanks for this thread, it's extremely interesting. And no worries about the assessment of the odd order theorem: in fact, 
I agree with many of the points you make.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (Feb 28 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123089994):
Fortunately, I was told what a perfectoid space is 2 weeks ago, otherwise I wouldn't have dared joining the discussion :-).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (Feb 28 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123090303):
I agree that the fact that it was possible to write down a formal proof of the odd order theorem only demonstrates that proof assistants can be used to represent good old undergraduate level algebra. Not that proof assistants are useful tools for research in mathematics.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (Feb 28 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123090373):
Even if in fact parts of the proofs involve slightly more advanced representation/character theory, etc.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Feb 28 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123090534):
```quote
Fortunately, I was told what a perfectoid space is 2 weeks ago, otherwise I wouldn't have dared joining the discussion :-).
```
Hi Assia! That's the point: Kevin wants to formalize stuff that mathematicians think are cool and intimidating

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (Feb 28 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123090587):
My hope is that one day proof assistants will be useful to discover new stuff, because the computer can in principle help you play with  the definitions, discover abstractions and test them. So yes, I agree, it would be really cool to have the definition of a perfectoid formalized, because then one could play with it interactively instead of staring at a paper definition like a fish out of water.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (Feb 28 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123090694):
But then I am not sure that the main problem is to come up with a definition which is not usable. I would say that the problem would be to formalize what  a cat  is and then to call it a perfectoid. Specially if not many people both know what a perfectoid is and how to speak/read Lean.
Lean checks proofs but only human readers check the definitions.  So a collection of theorems, and of convincing examples, helps this assessment.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (Feb 28 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123090992):
As a regular reviewer of papers about formalized mathematics, I  often read papers which claim to formalize the theory of mystuffoids, it is very interesting and the authors prove a litany of lemmas, culminating with the Fundamental Theorem of Mystuffoids. But the authors never provide a (formalized) instance of mystuffoid. So as a reviewer, I try to verify that all the elementary examples of mystuffoids I know of can indeed by equipped with the structure provided by the authors. And that a few things that are not stuffoids for a good reason will not be instances. I had myself issues with my own tentative formal definitions at several occasions, and rejected several papers because this protocole made explicit flaws in the definitions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Feb 28 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123091502):
I'm afraid there is no "elementary example" of a perfectoid space :wink:  And my daughter woke up, I need to rush to ski

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (Feb 28 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123091630):
Enjoy!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123106554):
```quote
But I'm also pretty sceptical that the March 11 dash you have in mind is going to have much effect. It's too likely that the code will fall apart quickly afterwards, or otherwise be unusable because it was written hurriedly.
```
Listen. I am in this unique position in that I get to give a lot of talks about a lot of random things to lots of people most of whom are under the age of 20 and some of whom are extremely smart. I am personally, after many conversations (and I'm sure Patrick feels the same way) no longer really interested in telling research mathematicians about formal theorem provers, because generally they are not interested. But on the other hand undergraduates are interested, and if you train them right they can really do stuff. Chris Hughes is answering other people's questions on this chat now and we all know what Kenny has done. There are other people "bubbling under" in my Thursday evening meetings and I'll train them up too. Remember that when those undergraduates started coming to my club I could not even use the software. I could not prove 2+2=4 in the reals, and nobody could prove anything about the complexes because there were no complexes. And yet a few people stuck around and are doing interesting things. Next year I am going to be a lot better and let's see what happens. But back to this conference. I think that if you're a smart 20 year old and you come to my talk on the 11th at some undergrad pure maths conference to learn about perfectoid spaces and then you hear me say that I've defined them in Lean and if you want to learn about Lean then you might want to try proving lemma 1 about them, then there is a chance that you will get curious and try. I do think there's a chance. And if you fail, which of course you might well, then you might instead want to try some of the easier lessons on my blog. And then you might get addicted, like I did and like Chris did. So I am going to continue going round the South East of the UK telling undergrads and schoolkids about Lean because there are random smart people out there who are bored at uni and who might actually want to goof around with trendy objects in a theorem prover. Maybe. I am genuinely trying to piggy back on the trendiness of the topic. I've written a paper about perfectoid spaces so I do have an excuse to talk about them, why shouldn't I tag Lean on and see what happens? I want to push undergraduates -- who don't know any better -- to start investigating theorem provers, because I think they're the future of pure mathematics and I think that thus far the CS community has singularly failed to demonstrate this to the maths community. I am trying a new idea from a new perspective, purely for fun. I want to introduce them from the bottom up and I am prepared to try lots of angles, and for me perfectoid spaces is definitely an angle worth trying. I want to try 10 different things and this is one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123106807):
```quote
As a regular reviewer of papers about formalized mathematics, I  often read papers which claim to formalize the theory of mystuffoids, it is very interesting and the authors prove a litany of lemmas, culminating with the Fundamental Theorem of Mystuffoids. But the authors never provide a (formalized) instance of mystuffoid. So as a reviewer, I try to verify that all the elementary examples of mystuffoids I know of can indeed by equipped with the structure provided by the authors. And that a few things that are not stuffoids for a good reason will not be instances. I had myself issues with my own tentative formal definitions at several occasions, and rejected several papers because this protocole made explicit flaws in the definitions.
```
Oh this is a _great_ comment! Because basically it is pointing out that until I prove some lemmas, people can just say "how do you know you have the right definition?". I am not sure that undergraduates have the guts to say that ;-) but still this comment sticks in my head. So in fact I have to prove some lemmas just to check.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123106858):
```quote
I'm afraid there is no "elementary example" of a perfectoid space :wink:  And my daughter woke up, I need to rush to ski
```
I think the empty space is perfectoid. I'm not sure that it highlights the key features though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Mar 01 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123125391):
```quote
Oh this is a _great_ comment! Because basically it is pointing out that until I prove some lemmas, people can just say "how do you know you have the right definition?". I am not sure that undergraduates have the guts to say that ;-) but still this comment sticks in my head. So in fact I have to prove some lemmas just to check.
```
@**Kevin Buzzard**: I interpreted the comment not as saying “prove some lemmas,” but as saying “give examples.” In other words, don't just give a definition and lemmas, but show that there are things that instantiate your definition. Otherwise, your lemmas might be wonderful but never be of any actual use.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 01 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123126888):
In fact for the definition I'm going to give, it will be really hard to give any examples, because we're going to cut corners and possibly come back later.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 01 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123129163):
```quote
@**Kevin Buzzard**: I interpreted the comment not as saying “prove some lemmas,” but as saying “give examples.” In other words, don't just give a definition and lemmas, but show that there are things that instantiate your definition. Otherwise, your lemmas might be wonderful but never be of any actual use.
```
@**Sean Leather** I hope you realize you are being really rude here. We are talking about Algebraic Geometry and Langlands Program here, giving an example would be a disgrace.  If needed, google "Grothendieck prime number 57".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Mar 01 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123129419):
```quote
I hope you realize you are being really rude here. We are talking about Algebraic Geometry and Langlands Program here, giving an example would be a disgrace.  If needed, google "Grothendieck prime number 57".
```
@**Patrick Massot**: You're right. I'm so accustomed to using the programs I write that I forget about mathematicians not needing to use the theorems they prove. :sweat_smile: I'm completely out of my depth here, and I apologize for any unintended insolence. :innocent:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 01 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123130673):
@**Sean Leather**  I thought about your comment a bit more and it's more complicated than I first imagined. Somehow examples and lemmas all get mixed together in this game, and definitions too. It's a bit strange. I said to Mario earlier "for you there is no difference between a perfectoid space and a group, they're both just structures" but somehow this isn't right. A group really is just a structure defined by some axioms. For these more complex objects there are theorems that you need to prove before things even make sense. For example you sometimes want to say "and my structure has an X, and if we choose a generator f of X then f also has property Y" or maybe even "and for all generators f of X, f also has property Y" but then if you actually want to get anywhere you need some lemma to say that all X's have generators, or maybe even that one generator of X has property Y iff they all do. Either you prove these lemmas or you don't. If you don't (and there are going to be a couple of times with schemes where I propose not proving the lemmas just yet) then it really would be impossible to give any examples at all because the lemmas are somehow part of the infrastructure. So perhaps I interpreted @**Assia Mahboubi** 's comments in a similar way to you but then went on and thought more about the consequences of constructing an example in the situation I had in mind, and realised that I was some genuine lemmas in algebraic geometry away from being able to give any example at all.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Mar 01 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123130781):
Makes sense. I was thinking in the first order, whereas you were at a higher order. Good thing you're the mathematician. :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 07 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123414422):
Kenny and I just finished the definition of a scheme.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 07 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123414480):
https://github.com/kbuzzard/lean-stacks-project/blob/ed8a255cef466794d4d836ffa6ffc1093532fa4b/src/scheme.lean#L430

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 07 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123414490):
It passes no basic tests whatsoever, other than "compiles" and "is mathematically correct".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 07 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123414608):
In particular, for any commutative ring R we can build an affine scheme Spec(R), but we have not yet proved that this object is a scheme.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 07 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123414620):
We are a couple of theorems away from this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 07 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123414772):
[the issue is that a scheme is a space with a sheaf, locally isomorphic to an affine scheme, but this isomorphism is an isomorphism of spaces with presheaves of rings (a morphism of sheaves is by definition a morphism of the underlying presheaves) so we do not logically need to check that the presheaf of rings that we have defined on Spec(R) is a sheaf]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 07 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/stacks%20project%20/%20schemes/near/123415572):
Now for perfectoid spaces ;-)

