---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/96443unificationmagic.html
---

## Stream: [general](index.html)
### Topic: [unification magic](96443unificationmagic.html)

---


{% raw %}
#### [ Kevin Buzzard (Apr 23 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543006):
I wrote a `noncomputable definition` which was an instance of a structure. The structure had 6 fields, and I was filling in the last one, which was a proof. The other 5 fields had already used a bunch of constructions. I was filling in this 6th field and I started by getting the syntax right and writing `_` for several things, including a function `_ : R -> S` between two rings. Once I'd got the syntax correct and complete, Lean evaluated the term and to my surprise found no problems with it.  In particular I think it must have figured out which function I meant.

#### [ Kevin Buzzard (Apr 23 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543009):
Now there's only one sensible function `R -> S`, and this function has almost certainly been mentioned earlier in the definition

#### [ Kevin Buzzard (Apr 23 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543015):
however I could not really imagine how type class unification could solve this.

#### [ Kevin Buzzard (Apr 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543018):
Is this sort of thing sometimes possible?

#### [ Simon Hudon (Apr 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543058):
Is there a lemma in your structure about the function?

#### [ Kevin Buzzard (Apr 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543060):
could well be

#### [ Kevin Buzzard (Apr 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543062):
the function is used all over the place

#### [ Kevin Buzzard (Apr 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543065):
It's just got rather a long name

#### [ Kevin Buzzard (Apr 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543066):
so I couldn't be bothered to type it

#### [ Simon Hudon (Apr 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543067):
That's probably how it's inferred

#### [ Kevin Buzzard (Apr 23 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543074):
It's a term, not a type.

#### [ Kevin Buzzard (Apr 23 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543075):
Perhaps that's what I was surprised about

#### [ Kevin Buzzard (Apr 23 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543122):
actually looking at it now I can begin to see how this amazing thing is possible

#### [ Kevin Buzzard (Apr 23 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543124):
ultimately this function f appears in the statement of the thing I'm trying to prove

#### [ Kevin Buzzard (Apr 23 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543133):
I'm constructing a proof of `f x = blah`

#### [ Kevin Buzzard (Apr 23 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543134):
and I skipped the definition of f

#### [ Simon Hudon (Apr 23 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543136):
Since we have dependent types, the line between types and terms is blurred. Similarly, if you have `f : Π n : ℕ, fin n → ℕ` and `x : fin (m+n)`, you can write `f _ x` and trust Lean to infer `m+n`

#### [ Kevin Buzzard (Apr 23 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543180):
I guess what I am saying is that I thought I was getting a pretty good instinct of what unification could do for me

#### [ Kevin Buzzard (Apr 23 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543181):
but it's even better than I thought

#### [ Kevin Buzzard (Apr 23 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543183):
Does Coq not have term mode?

#### [ Kevin Buzzard (Apr 23 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543189):
I used to be terrified of term mode

#### [ Kevin Buzzard (Apr 23 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543191):
but now I use it a lot

#### [ Kevin Buzzard (Apr 23 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543196):
all this was happening in term mode

#### [ Simon Hudon (Apr 23 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543244):
Ah ok! I thought you needed clarification.

#### [ Kevin Buzzard (Apr 23 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543246):
Writing the message myself was enough to get me thinking in the right way

#### [ Kevin Buzzard (Apr 23 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543251):
That's the problem with these chat rooms

#### [ Kevin Buzzard (Apr 23 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543253):
Sometimes I have a question about a maths paper and I start writing an email to the author and by the time I've finished the email, I've answered the question

#### [ Kevin Buzzard (Apr 23 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543254):
but then I never send the email

#### [ Simon Hudon (Apr 23 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543255):
In a way, Coq has a term mode because terms can be used as proofs but I believe it doesn't have the `have` / `show` / `suffices` notation so it's not made for writing proofs.

#### [ Kevin Buzzard (Apr 23 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543256):
here I started writing the question and it was already mostly sent before I realised what had happened

#### [ Simon Hudon (Apr 23 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543308):
Haha! Yeah, I know the feeling. A while back, a supervisor told me that I should try asking my questions to a cactus or a rubber duck because I didn't actually need him there

#### [ Simon Hudon (Apr 23 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543316):
Maybe you can signal this is happening by tagging your own message with :light_bulb:

#### [ Kevin Buzzard (Apr 23 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543357):
nice idea :-)

#### [ Simon Hudon (Apr 23 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543380):
I wouldn't be surprised if people jump in anyway and ask you to explain your newfound insight

#### [ Kevin Buzzard (Apr 23 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543381):
Thanks for listening :-)

#### [ Kevin Buzzard (Apr 23 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543428):
I agree about the rubber duck suggestion. I feel silly talking to inanimate objects but as I already said, the technique I've used which really works for me is to start writing an email to someone who will know the answer, and really explain all the background and details about what you're confused about.

#### [ Kevin Buzzard (Apr 23 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543434):
And a lot of the time, the email ends up never sent and becomes an answer to your own question

#### [ Simon Hudon (Apr 23 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543509):
I feel silly talking to inanimate things too ... the worse is when they talk back!

#### [ Andrew Ashworth (Apr 23 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543554):
I am pretty excited for lean 4 and playing around with {! !}

#### [ Andrew Ashworth (Apr 23 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543557):
i think term mode has been a little neglected, which is a shame since writing programs with tactics is a bit scary

#### [ Simon Hudon (Apr 23 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543561):
But if someone walk into the room, it's pretty embarrassing too. Then I have to pretend that there's a song about inductive proofs of liveness.

#### [ Simon Hudon (Apr 23 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543615):
```quote
i think term mode has been a little neglected, which is a shame since writing programs with tactics is a bit scary
```
Why is it scary?

#### [ Andrew Ashworth (Apr 23 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543631):
because i have no idea how certain tactics get compiled down to certain terms, or how those terms might be evaluated in the vm

#### [ Simon Hudon (Apr 23 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543673):
That's true. What about mixing terms and tactics?

#### [ Andrew Ashworth (Apr 23 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543679):
sure. tactics are great for Props, which get erased

#### [ Andrew Ashworth (Apr 23 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543736):
i mean, i don't doubt you can do crazy things with tactic automation, but it's another layer of abstraction on top of a bunch of stuff I don't understand already :)

#### [ Andrew Ashworth (Apr 23 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543743):
i have a slightly ill feeling when I have to read other people's template and macro hackery

#### [ Andrew Ashworth (Apr 23 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543744):
already

#### [ Andrew Ashworth (Apr 23 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543787):
i'm hoping programming in lean gets updated at some point as well... i've been holding off on writing metaprograms in lean since there's little documentation

#### [ Andrew Ashworth (Apr 23 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543788):
and I don't have the interest to hack away at it without some hand-holding

#### [ Simon Hudon (Apr 23 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543842):
Regardless of meta programming skills, it's true that tactics can easily obscure the operational aspect of programs

#### [ Simon Hudon (Apr 23 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543885):
If we had an execution model and performance specifications, maybe that wouldn't be so bad. What do you think?

#### [ Moses Schönfinkel (Apr 23 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543891):
I think he's talking about the entire pexpr stuff and magical functions to convert from and to varius opaque intermediate forms :)? At least that's what is fairly annoying for me and Ltac simply does better.

#### [ Simon Hudon (Apr 23 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543935):
Because in Ltac you don't have to perform conversions? It's funny because I find Ltac much more obscure at the operational level. I find I'm never sure what my tactics will actually do

#### [ Andrew Ashworth (Apr 23 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543941):
you're assuming i'm even aware of these magical functions to intermediate forms

#### [ Andrew Ashworth (Apr 23 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543943):
i cracked open PIL, saw it had only a few chapters finished, and then walked away back to term mode

#### [ Kevin Buzzard (Apr 23 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125544405):
My _impression_ is that the missing chapters in PIL are mostly stuff which is documented in TPIL


{% endraw %}
