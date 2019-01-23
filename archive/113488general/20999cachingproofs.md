---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20999cachingproofs.html
---

## Stream: [general](index.html)
### Topic: [caching proofs](20999cachingproofs.html)

---

#### [Scott Morrison (Sep 18 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150227):
So I'm moving it here.

#### [Sean Leather (Sep 18 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150232):
From https://leanprover.zulipchat.com/#narrow/stream/113489-new-members/subject/caching.20proofs/near/134150221

#### [Scott Morrison (Sep 18 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150236):
Thanks.

#### [Scott Morrison (Sep 18 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150273):
Yes, that second pass is just unavoidably slow.

#### [Johan Commelin (Sep 18 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150280):
So I'm fine if Travis does that, and I never do it.

#### [Scott Morrison (Sep 18 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150281):
But I think there's still useful information for the user in seeing the first pass succeed.

#### [Johan Commelin (Sep 18 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150282):
Or almost never...

#### [Scott Morrison (Sep 18 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150283):
Yes.

#### [Sean Leather (Sep 18 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150286):
What exactly are you guys referring to when you say “proof cache”?

#### [Scott Morrison (Sep 18 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150288):
The point of course is to get back as quickly as possible to responsive editing.

#### [Scott Morrison (Sep 18 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150295):
(For us poor idiots who use interactive mode, and *can't*, like some people here, write Lean code while offline. :-)

#### [Scott Morrison (Sep 18 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150308):
Of course, olean files _are_ a proof cache.

#### [Scott Morrison (Sep 18 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150312):
So the idea might be merely this:

#### [Scott Morrison (Sep 18 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150353):
if Lean notices that an olean file is outdated (i.e. the source file, or a dependency source file, is newer)

#### [Patrick Massot (Sep 18 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150356):
Do you know about https://github.com/leanprover/lean/issues/1601? Fixing this issue is part of the Lean 4 plan ifI understand correctly

#### [Scott Morrison (Sep 18 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150364):
*before* disposing of the olean file it loads it one last time

#### [Scott Morrison (Sep 18 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150380):
and tries to use existing proofs for the current set of lemmas, ignoring on the first pass the actual proof term written in the source file (whether generated in term or tactic mode)

#### [Scott Morrison (Sep 18 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150386):
but of course eventually there does have to be a second pass that reverifies what the user has written and constructs a new olean.

#### [Kevin Buzzard (Sep 18 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150446):
```quote
(For us poor idiots who use interactive mode, and *can't*, like some people here, write Lean code while offline. :-)
```
Q1 What's "offline"? Q2 why can't you write code offline? What is interactive mode?

#### [Johan Commelin (Sep 18 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150523):
I think "offline" here means: Writing code without Lean responding to what you write. (Just using your internal elaborater/kernel to verify your own code.)

#### [Kevin Buzzard (Sep 18 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150545):
eew.

#### [Scott Morrison (Sep 18 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150547):
In particular @**Simon Hudon** appears to have written working code for me without ever running Lean...!

#### [Scott Morrison (Sep 18 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150599):
(Sometimes I've been able to tell because of some minor typo, meaning it just barely missed actually compiling. :-)

#### [Johan Commelin (Sep 18 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150602):
In Orsay I witnessed Mario writing half a proof while Lean was thinking. He didn't need to go back and change those 5 lines after Lean caught up with him.

#### [Scott Morrison (Sep 18 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150603):
It's terrifying, isn't it? :-)

#### [Scott Morrison (Sep 18 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150610):
Yellow bars just cause my brain to freeze up. :-)

#### [Sean Leather (Sep 18 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150678):
I don't use interactive mode, so I just see walls of errors, not yellow bars.

#### [Johan Commelin (Sep 18 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150700):
```quote
I don't use interactive mode, so I just see walls of errors, not yellow bars.
```
Wait... do you mean that you write Lean the way I would write C or Python?

#### [Johan Commelin (Sep 18 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150744):
Edit file → Save → Compile/run the file in terminal → Parse errors → Go back to step 1

#### [Scott Morrison (Sep 18 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150745):
Well... presumably he doesn't actually ever *execute* any code.

#### [Sean Leather (Sep 18 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150748):
Yep.

#### [Scott Morrison (Sep 18 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150750):
Well, Sean might, actually. :-)

#### [Sean Leather (Sep 18 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150751):
:big_smile:

#### [Johan Commelin (Sep 18 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150756):
Aaahrg... :scream: you guys are really crazy...

#### [Sean Leather (Sep 18 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150807):
Anyway, I'm not sure if it's the same problem as in interactive mode: I'd like to speed up `lean --make`.

#### [Sean Leather (Sep 18 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150822):
So, it would be nice if I had all of the generated proof terms for, say, mathlib. So, if I make one change, `lean` doesn't have to recheck entire files.

#### [Johan Commelin (Sep 18 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150823):
I guess it is the same bottleneck that we are hitting.

#### [Sean Leather (Sep 18 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150835):
On the other hand, as Scott said, one small change can change tactics. But I think that should be checked at “release” time.

#### [Sean Leather (Sep 18 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150836):
... as opposed to “interactive” time.

#### [Sean Leather (Sep 18 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150846):
So, at the very least, I know proof works. But I may need to go back and check a tactic somewhere afterwards.

#### [Sean Leather (Sep 18 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150900):
I envision it like having a `--fast` mode and a `--release` mode. Names up for debate.

#### [Johan Commelin (Sep 18 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150912):
We already have trust levels...

#### [Sean Leather (Sep 18 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150918):
Or `--fast` and `--full` to use alliteration.

#### [Sean Leather (Sep 18 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150922):
How do trust levels come into the picture here?

#### [Johan Commelin (Sep 18 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150934):
Well, you are putting "trust" in the cache, right?

#### [Johan Commelin (Sep 18 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150977):
I could envision a new trust level, that will trust cached proofs.

#### [Johan Commelin (Sep 18 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150983):
Does that make sense?

#### [Sean Leather (Sep 18 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150989):
Perhaps. I don't have a clear picture of what that means.

#### [Sean Leather (Sep 18 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134151006):
I'm not thinking of trust. I'm thinking of checking only what changed within a single file (to simplify the problem).

#### [Sean Leather (Sep 18 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134151145):
Here's something that doesn't work for all changes, but might work for some: run a quick pass over the interfaces of a file's cached proof terms, check if they differ from the source file, build the ones that differ or are not found in the cache.

#### [Sean Leather (Sep 18 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134151220):
After that, perhaps you could more lazily regenerate the other proof terms of the file.

#### [Sean Leather (Sep 18 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134151306):
Also, perhaps the generated proof cache could keep track of failed proofs and Lean would try to rebuild those first.

#### [Sean Leather (Sep 18 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134151318):
That might improve interactive responsiveness.

#### [Johan Commelin (Sep 18 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134151328):
I wouldn't mind if Lean did low-priority (in the sense of CPU scheduler) checks to see if my new `@[simp]` lemma broke a proof `by tidy` in some files that I didn't have open. But as soon as I make a change in my file the `--fast` Lean should do a high-priority check to get me back to responsive editing as soon as possible.

#### [Sean Leather (Sep 18 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134151406):
Yeah, that's the idea, though I was actually thinking `--fast` wouldn't even try to check the effect of `@[simp]` lemmas or other things that change how tactics work. But I could see it going either way.

#### [Johan Commelin (Sep 18 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134151413):
```quote
Do you know about https://github.com/leanprover/lean/issues/1601? Fixing this issue is part of the Lean 4 plan ifI understand correctly
```
That definitely looks relevant! Thanks @**Patrick Massot**

#### [Sean Leather (Sep 18 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134151538):
Here are two possibilities:

1. An interactive mode that optimizes for checking work-in-progress proofs and reduces the priority of full-file and full-library builds.
2. A fast mode that only checks for work-in-progress proofs and builds a single file at a time and a full mode that builds everything.

#### [Simon Hudon (Sep 19 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134200810):
@**Sean Leather** Isn't that already what the ideas do? I feel like lean-mode does it at least.

@**Scott Morrison** I do use the interactive modes but sometimes I'm too lazy to go back to emacs to write my code snippets. I'm glad I don't have too bad a track record :)

#### [Sean Leather (Sep 19 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134212305):
```quote
Isn't that already what the ideas do? I feel like lean-mode does it at least.
```

@**Simon Hudon** What are “the ideas”?

I don't know exactly what does what, so I'm just throwing out some thoughts. I do know that if I make a change in a large file in mathlib and build with `lean --make`, I see that the entire file has to be built before it gets to my change. That's what I would propose improving.

As I said above, I don't use the interactive approach, and I don't know if the problem I have is the same problem others are discussing.

#### [Simon Hudon (Sep 19 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134213789):
I misspelled IDE

#### [Simon Hudon (Sep 19 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134213795):
So what is your workflow like if you don't use them?

#### [Sean Leather (Sep 19 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134213841):
Edit in `vim`, run `leanpkg build`.

#### [Simon Hudon (Sep 19 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134214709):
That sounds painful

#### [Sean Leather (Sep 19 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134214720):
:shrug: Works well for me.

#### [Kevin Buzzard (Sep 19 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134214780):
I print the files out, cross out some lines in pencil and add others in, then compile in my head.

#### [Kevin Buzzard (Sep 19 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134214784):
that's how we did it in the old days before computers

#### [Sean Leather (Sep 19 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134214792):
How did you print files without computers? :computer: :right: :printer:

#### [Kevin Buzzard (Sep 19 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134214831):
I use my typewriter

#### [Sean Leather (Sep 19 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134214849):
Oh, they usually refer to that as typing, not printing, right?

#### [Johan Commelin (Sep 19 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134214864):
He has a printing press à la Gutenberg in his cellar (-;

#### [Kevin Buzzard (Sep 19 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134214865):
I guess they call it that nowadays.

#### [Simon Hudon (Sep 19 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134214929):
Amateurs. Here's my workflow: https://xkcd.com/378/

#### [Johan Commelin (Sep 19 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134215138):
`C-x M-c M-butterfly`

#### [Simon Hudon (Sep 19 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134256955):
@**Sean Leather** I think this is a case in which, before you see what you're missing out on, you don't know that you're missing out. I find it incredibly useful when writing tactic that, as I type and change my scripts, I can see the print out of the example I'm using the tactic on. That save a whole lot of time

