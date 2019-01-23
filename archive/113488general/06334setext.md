---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/06334setext.html
---

## Stream: [general](index.html)
### Topic: [setext](06334setext.html)

---


{% raw %}
#### [ Patrick Massot (Apr 16 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125155122):
Core lib has a `funext` tactic which allows to replace `apply funext, intro x` by `funext x`. Would it be a good idea to copy the definition of this tactic to get a `setext` tactic?

#### [ Kenny Lau (Apr 16 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125155142):
the `funext` tactic is really `repeat {apply funext, intro x}` though

#### [ Kenny Lau (Apr 16 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125155159):
but right, `set.ext` can only be used once

#### [ Kenny Lau (Apr 16 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125155166):
well you can just set `setext` to be `apply set.ext; intro x`

#### [ Patrick Massot (Apr 16 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125155173):
I want `x` to be an argument of the tactic

#### [ Kenny Lau (Apr 16 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125155215):
sure

#### [ Patrick Massot (Apr 16 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125155220):
It's mostly a cosmetic question, but also about consistency

#### [ Patrick Massot (Apr 16 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125155225):
Because I keep trying `setext x` before remembering it doesn't work yet

#### [ Mario Carneiro (Apr 16 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125158190):
@**Simon Hudon** I recall discussing a generic `ext` tactic as a complement to the `monotonicity` tactic, perhaps it would help here

#### [ Simon Hudon (Apr 16 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125158338):
Yes, I have it in `lean-lib`. I can create a pull request. I have a `extensionality` attribute that I used to tag extentionality on sets, stream and maybe other things too

#### [ Patrick Massot (Apr 16 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125164007):
nice

#### [ Simon Hudon (Apr 16 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166265):
I just submitted a pull request: https://github.com/leanprover/mathlib/pull/104

#### [ Simon Hudon (Apr 16 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166322):
In tests/examples.lean you should see a bunch of situations where `ext` is useful.

#### [ Simon Hudon (Apr 16 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166324):
Let me know if you think there should be more extensionality lemmas

#### [ Patrick Massot (Apr 16 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166339):
Thanks!

#### [ Patrick Massot (Apr 16 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166347):
Can you give it names like with funext?

#### [ Patrick Massot (Apr 16 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166423):
Oh, you put sorries in tests again :disappointed:

#### [ Simon Hudon (Apr 16 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166431):
Yes. `ext` will apply all extensionality lemmas that make sense while `ext a b c` will only apply three (not necessarily the same) and name the introduced locals `a`,`b`, `c`,

#### [ Patrick Massot (Apr 16 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166439):
What is this `ext1` I see in tests? Apply it only once?

#### [ Patrick Massot (Apr 16 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166442):
like `congr_n 1`?

#### [ Simon Hudon (Apr 16 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166443):
It shouldn't affect the built because the final proof is just `trivial`

#### [ Patrick Massot (Apr 16 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166448):
Ahah

#### [ Simon Hudon (Apr 16 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166506):
I don't know of `congr_n 1` but it sounds like you got the right idea

#### [ Simon Hudon (Apr 16 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166536):
(I'm so glad `congr_n` exists! I'll be able to use that now!)

#### [ Patrick Massot (Apr 16 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166606):
I was looking to my mathlib tactics docs to point to and, shame on me, I didn't include congr_n! :disappointed:

#### [ Simon Hudon (Apr 16 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166620):
*shake head in  disapproval*

#### [ Simon Hudon (Apr 16 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166733):
Would it be useful to have a `monoid` and `add_monoid` instance for `fin n` in `mathlib`?

#### [ Patrick Massot (Apr 16 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166871):
What would be the law? Again some truncation thing?

#### [ Simon Hudon (Apr 16 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166894):
Yes. It would be modulo arithmetic with the modulo baked into the type

#### [ Patrick Massot (Apr 16 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166943):
Oh, modulo

#### [ Patrick Massot (Apr 16 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166948):
That's a bit sneaky

#### [ Patrick Massot (Apr 16 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166951):
https://github.com/leanprover/mathlib/pull/105

#### [ Simon Hudon (Apr 16 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166987):
What kind of sneaky? Evil-sneaky or just effective-sneaky?

#### [ Patrick Massot (Apr 16 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167052):
I don't know. People could be taken off guard. But who would want to add elements of `fin n` anyway?

#### [ Simon Hudon (Apr 16 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167066):
After a quick survey, there's me

#### [ Simon Hudon (Apr 16 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167146):
The other alternative I see is the `p ≡ q [MOD k]` notation but that looks more restricted. `fin n` is usable in other contexts that congruences or equalities.

#### [ Patrick Massot (Apr 16 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167210):
I notice your ext PR doesn't include documentation :unamused:

#### [ Simon Hudon (Apr 16 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167238):
What's this `documentation` thing?

#### [ Simon Hudon (Apr 16 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167272):
Alright, I'll add a comment :)

#### [ Simon Hudon (Apr 16 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167274):
Is that better?

#### [ Patrick Massot (Apr 16 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167328):
By the way, you told me we found a bug in `wlog` when I asked questions about it. Did you manage to fix it?

#### [ Simon Hudon (Apr 16 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167358):
That's true! I forgot about it. It was pretty tricky. I'll get back to it.

#### [ Simon Hudon (Apr 16 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167362):
Sorry for the delay

#### [ Patrick Massot (Apr 16 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167372):
Adding a docstring to `tactic/interactive.lean` would be good enough. Then I can copy it to tactic.md

#### [ Patrick Massot (Apr 16 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167378):
But in this case I could also write the docstring I guess

#### [ Patrick Massot (Apr 16 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167422):
The problem is I could write nonsense

#### [ Patrick Massot (Apr 16 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167447):
There is no delay problem with wlog, I was only asking so you don't forget

#### [ Simon Hudon (Apr 16 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167472):
Thanks for reminding me

#### [ Patrick Massot (Apr 16 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167513):
Speaking of documentation, I wonder if @**Sebastian Ullrich**  of @**Gabriel Ebner**  could answer Kevin's questions in https://github.com/leanprover/mathlib/blob/master/docs/extras/calc.md (you only need to search for "Kevin" in this file)

#### [ Simon Hudon (Apr 16 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167526):
I'll write both no worries. I was joking.

#### [ Kevin Buzzard (Apr 16 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167620):
I'm not at a computer right now, but IIRC I think `fin n` already has an `+` but it is not very well behaved!

#### [ Simon Hudon (Apr 16 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167632):
Actually, I think `-` is more problematic. And we don't have laws for them

#### [ Kevin Buzzard (Apr 16 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167676):
My memory is that these structures on `fin n` are defined in core and didn't make it into a sensible mathematical object

#### [ Kevin Buzzard (Apr 16 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167682):
I think 2+2 wasn't 2-2 in fin 4 for example

#### [ Kevin Buzzard (Apr 16 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167702):
Docs -- yes I'd forgotten I'd left those in!

#### [ Patrick Massot (Apr 16 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167708):
`#reduce (2 : fin 4) - (2 : fin 4)  -- ⟨0, _⟩`

#### [ Patrick Massot (Apr 16 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167749):
`#reduce (2 : fin 4) + (2 : fin 4)  -- ⟨0, _⟩`

#### [ Kevin Buzzard (Apr 16 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167753):
Try 1+2 and 1-2

#### [ Kevin Buzzard (Apr 16 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167755):
Maybe that was it

#### [ Patrick Massot (Apr 16 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167764):
1+2 is 3 and 1 - 2 is 0

#### [ Kevin Buzzard (Apr 16 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167765):
2+2=0 so adding 2 and subtracting 2 should be the same

#### [ Kevin Buzzard (Apr 16 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167772):
Thanks

#### [ Patrick Massot (Apr 16 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167773):
hard to tell what is the rule here

#### [ Patrick Massot (Apr 16 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167779):
it seems substration is truncated at zero

#### [ Kevin Buzzard (Apr 16 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167781):
Subtracting is just subtraction on nat I think

#### [ Patrick Massot (Apr 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167782):
and addition wraps

#### [ Kevin Buzzard (Apr 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167821):
Right

#### [ Kevin Buzzard (Apr 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167829):
Does that make it a monoid?

#### [ Kevin Buzzard (Apr 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167831):
🙂

#### [ Patrick Massot (Apr 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167835):
I think I remember reading this discussion in the past

#### [ Kevin Buzzard (Apr 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167837):
Right

#### [ Simon Hudon (Apr 16 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167845):
What was the conclusion?

#### [ Patrick Massot (Apr 16 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167896):
Current definitions are... odd

#### [ Kenny Lau (Apr 20 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125341724):
https://github.com/leanprover/mathlib/pull/109/commits

#### [ Kenny Lau (Apr 20 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125341725):
ext is in PR


{% endraw %}
