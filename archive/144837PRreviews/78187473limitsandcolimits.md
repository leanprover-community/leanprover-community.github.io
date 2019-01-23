---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/78187473limitsandcolimits.html
---

## Stream: [PR reviews](index.html)
### Topic: [#473 limits and colimits](78187473limitsandcolimits.html)

---


{% raw %}
#### [ Johan Commelin (Nov 19 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952349):
@**Scott Morrison|110087** has taken this PR through a couple of revisions, but I think it is quite solid and stable now. I've been stress testing it quite a bit on my `sheaf` branch, and I think it works well. Do others have any comments?

#### [ Johan Commelin (Nov 19 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952393):
I don't think we should add new stuff to this PR, but people are accumulating follow-up stuff.

#### [ Mario Carneiro (Nov 19 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952555):
I think Kenny pointed out that this PR uses a lot of high automation. Are there any really expensive files in here?

#### [ Mario Carneiro (Nov 19 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952606):
maybe add a few more `tidy says:` bits

#### [ Johan Commelin (Nov 19 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952756):
@**Mario Carneiro** Isn't this battling in the wrong direction?

#### [ Johan Commelin (Nov 19 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952768):
And tons of this automation is hidden in auto_params. We really don't want to see those.

#### [ Mario Carneiro (Nov 19 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952911):
yes, I realize that, and we had this conversation already with the `faster` branch

#### [ Mario Carneiro (Nov 19 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952920):
The fact is that people compile mathlib often, and doubling the compile time is not a good thing

#### [ Johan Commelin (Nov 19 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952922):
Sure, but there we didn't really rewrite much. We only expanded `simp`s into `simp only`s.

#### [ Mario Carneiro (Nov 19 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952928):
and here we can expand `tidy` into its proof script without much work

#### [ Mario Carneiro (Nov 19 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952977):
If it is fast enough, I don't even think that is necessary, but any tactics that take more than a few seconds should probably be unrolled a bit

#### [ Scott Morrison (Nov 19 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147954782):
Ok, the `limits` directory currently invokes `tidy` 156 times, and spends  107s inside `tidy`.  34 of these invocations take more than a second each.

#### [ Scott Morrison (Nov 19 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147954784):
Only one takes more than 4.

#### [ Scott Morrison (Nov 19 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955040):
How do you make `lean --make` run single threaded?

#### [ Scott Morrison (Nov 19 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955047):
The output from `--profile` is all jumbled up, and I can't tell which output is from which declaration. :-(

#### [ Rob Lewis (Nov 19 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955100):
`-j0`, I think.

#### [ Kenny Lau (Nov 19 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955104):
if you use `--profile`, only look at the STDERR

#### [ Kenny Lau (Nov 19 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955106):
I mean

#### [ Kenny Lau (Nov 19 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955108):
only look at the STDOUT

#### [ Kenny Lau (Nov 19 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955112):
I actually forgot which one to look at

#### [ Scott Morrison (Nov 19 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955121):
even then, if two declarations are running at once, I was having their profile output interspersed

#### [ Kenny Lau (Nov 19 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955148):
`git ls-files *.lean | xargs -I % sh -c '>&2 echo %; lean --profile % >/dev/null;' > profile.txt 2>&1`

#### [ Kenny Lau (Nov 19 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955151):
this is how I use it

#### [ Scott Morrison (Nov 19 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955152):
hmm.. even with `-j0` I can't make sense of the output.

#### [ Scott Morrison (Nov 19 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955199):
Hmm... could you show me how to run that just on a subdirectory?

#### [ Scott Morrison (Nov 19 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955211):
Can I just change the `*.lean`?

#### [ Scott Morrison (Nov 19 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955243):
Kenny, your scripts seems to only tell me totals by file. Is that what you intended?

#### [ Kenny Lau (Nov 19 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955521):
yes...

#### [ Scott Morrison (Nov 19 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955582):
That's not going to help me at all.

#### [ Kenny Lau (Nov 19 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955586):
i'll excuse myself before you realize that i don't know anything about bash :P

#### [ Scott Morrison (Nov 19 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955591):
From what I can see, the instances of `tidy` that take more than a second don't even appear in the source file, they're in `auto_param`s.

#### [ Johan Commelin (Nov 19 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955669):
/me hears a background choir chanting *"We want caching! We want caching! We want caching..."*

#### [ Scott Morrison (Nov 19 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955737):
I think, until someone comes up with caching and/or faster tactic execution, I might find something more productive to do... Writing out human-irrelevant proofs for the sake of compilation times is the surest sign I've seen yet that this is all a bad idea. :-(

#### [ Mario Carneiro (Nov 19 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147956525):
If you would rather have someone else do it we can postpone it until someone else gets annoyed at compile times enough to do something about it...

#### [ Mario Carneiro (Nov 19 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147956557):
or until someone actually puts those caching ideas into practice

#### [ Patrick Massot (Nov 19 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147956620):
An intermediate goal which looks much easier would be to find a way to collect olean built by travis as something people could download and use right away

#### [ Mario Carneiro (Nov 19 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147957272):
How portable have you found them to be?

#### [ Patrick Massot (Nov 19 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147957330):
Sebastian claims they should be portable enough

#### [ Kevin Buzzard (Nov 19 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147957997):
For sure I've had no problem making them on one win10 machine and using them on another

#### [ Kevin Buzzard (Nov 19 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147958014):
One has to make sure that the file transfer doesn't mangle the timestamps though

#### [ Patrick Massot (Nov 19 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147958020):
If I remember correctly, Sebastian said they should even work across OSs. The only things that needs care are timestamps

#### [ Patrick Massot (Nov 19 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147998722):
Who wants to try downloading https://www.math.u-psud.fr/~pmassot/mathlib.tar.gz and play with it to see whether olean can be reused? It's a freshly compiled mathlib (without the `.git` directory)

#### [ Rob Lewis (Nov 19 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147999684):
This doesn't work for me, at least not in an obvious way. I unzipped and created `test.lean` in the root directory. Adding `import data.real.basic` starts recompiling everything.

#### [ Rob Lewis (Nov 19 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147999870):
(I'm on my Windows laptop, by the way, using msys2.)

#### [ Patrick Massot (Nov 19 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000002):
What if you touch all olean files? (assuming `touch` exists on Windows)

#### [ Rob Lewis (Nov 19 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000259):
Doesn't seem to make a difference.

#### [ Mario Carneiro (Nov 19 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000638):
I have had success with using `touch` in the past

#### [ Mario Carneiro (Nov 19 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000680):
if you touch the files then lean will accept them as correct without checking, regardless of the actual status

#### [ Mario Carneiro (Nov 19 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000691):
so you get funny errors sometimes but it usually worksish

#### [ Rob Lewis (Nov 19 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000744):
Just the .oleans? Just the .leans? Both?

#### [ Mario Carneiro (Nov 19 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000754):
just the oleans

#### [ Rob Lewis (Nov 19 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000759):
I tried just the .oleans and both, neither seemed to do the trick.

#### [ Mario Carneiro (Nov 19 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000769):
also the oleans have to be touched in dependency order or very fast

#### [ Rob Lewis (Nov 19 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000803):
Um, okay, that I definitely didn't do.

#### [ Rob Lewis (Nov 19 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000811):
`find  -type f  -name "*.olean" -exec touch {} +` must not have been fast enough.

#### [ Mario Carneiro (Nov 19 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000821):
I think within a second should do

#### [ Mario Carneiro (Nov 19 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000866):
you can check the modification dates

#### [ Mario Carneiro (Nov 19 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000876):
alternatively, find a bashism to get the current time and set all the files to that

#### [ Rob Lewis (Nov 19 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148001821):
Still not having any luck. I've set the timestamp on all .olean files to match a random file (with a later timestamp than any of the .leans). It still starts recompiling when I import anything.

#### [ Mario Carneiro (Nov 19 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148002004):
oh I see

#### [ Mario Carneiro (Nov 19 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148002016):
I get a quick `lean --make` this way

#### [ Rob Lewis (Nov 19 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148002162):
But with your own .oleans, right? Not with foreign ones?

#### [ Mario Carneiro (Nov 19 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148002171):
yes

#### [ Mario Carneiro (Nov 19 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148002245):
I've never tested anything with foreign oleans. It's hard enough to get lean to accept native ones

#### [ Reid Barton (Nov 19 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148002544):
Unrelated to sharing olean files... I'm inclined to take this PR and split it into a logical series of commits, partly for my own understanding and partly to aid with review. Would that be helpful?

#### [ Mario Carneiro (Nov 20 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148002745):
yes. Anything I can't review in one sitting gets delayed a lot more than it should

#### [ Scott Morrison (Nov 20 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148008047):
Thank you, Reid, that would be fantastic.

#### [ Patrick Massot (Nov 20 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148028515):
I just tested in my office: my olean compiled at home work perfectly here. I'm not running up to date mathlib, I can use `mono` without any delay

#### [ Rob Lewis (Nov 20 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148028645):
Patrick, what steps are you doing to test it, and what OS are you using on either end?

#### [ Rob Lewis (Nov 20 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148028654):
I just tried it on my (Linux) office desktop and saw the same behavior as on my laptop last night.

#### [ Patrick Massot (Nov 20 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148030294):
I'm using Linux on all my computers. What I just did was: 
```
cd mathlib
mv .git ..
cd ..
rm -rf mathlib
wget https://www.math.u-psud.fr/~pmassot/mathlib.tar.gz 
tar xf mathlib.tar.gz
mv .git mathlib/
```
Then I opened the mathlib folder in VScode, created a scratch file at the root of mathlib, with the monotonicity examples I wrote yesterday in the "What's new" thread

#### [ Patrick Massot (Nov 20 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148030375):
Of course the `.git` stuff is there only because I want to preserve my local branches and didn't want to clutter the tar.gz with them

#### [ Rob Lewis (Nov 20 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148031165):
Then I don't know what the difference is, I did effectively the same thing (without the git stuff).

#### [ Rob Lewis (Nov 20 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148031179):
Do .olean files track the version of Lean used to compile them? What versions are you using on each computer?

#### [ Johan Commelin (Nov 20 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148032765):
It works for me! I downloaded Patrick's files, and I could immediately run the `mono` example from the other thread. No recompiles.

#### [ Johan Commelin (Nov 20 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148032767):
I'm on a Linux box.

#### [ Patrick Massot (Nov 20 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148034169):
The version of Lean should be enforced by the leanpkg.toml (I'm using elan)

#### [ Scott Morrison (Nov 22 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148147105):
Reid has just pushed a subset of the limits PR, which just contains the preparatory work. https://github.com/leanprover/mathlib/pull/488

#### [ Scott Morrison (Nov 22 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148147109):
Thanks, @**Reid Barton**, very much for doing this!

#### [ Scott Morrison (Nov 24 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148270095):
@**Reid Barton**, the preliminary PR was just merged. How should we handle the next chunk? I could rebase the big PR onto master, but I'm not actually sure that's useful.

#### [ Scott Morrison (Nov 26 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148336028):
@**Reid Barton**, do you have a moment to discuss next steps with the limits PRs?

#### [ Reid Barton (Nov 26 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148336287):
I'm actually in the midst of going through `limits.lean`

#### [ Scott Morrison (Nov 26 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148336290):
Great, okay, I'll leave you to it, in that case!

#### [ Reid Barton (Nov 26 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148336990):
currently in the phase of dualizing all my changes. It's a lot of typing...

#### [ Scott Morrison (Nov 26 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148337094):
sorry :-(

#### [ Scott Morrison (Nov 26 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148337099):
Think of it as a meditative practice.

#### [ Reid Barton (Nov 26 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148337213):
Well, it suddenly got interesting because one of the proofs is refusing to dualize

#### [ Reid Barton (Nov 26 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148337460):
OK, I defeated it, but a mystery for sure...

#### [ Reid Barton (Nov 26 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148337470):
I suspect `erw` uses some black magic

#### [ Johan Commelin (Nov 26 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148345984):
I made some trivial comments. Feel free to ignore them.
I squashed some double newlines into one. (Don't know if this is appreciated.)
I also think we can scrape a bunch of lemmas into namespaces, because now we have 20 lemmas after each other, that all start with `limit.`.

#### [ Reid Barton (Nov 26 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148370732):
@**Scott Morrison|110087** I'm going to drop the stuff about creating limits for now, because it doesn't appear to be used currently and I found about seven definitions of "F creates limits" which I think are all inequivalent.

#### [ Scott Morrison (Nov 26 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148388233):
Sounds very reasonable. I think I followed the definition in Emily Riehl's book, but I agree it's a mess, and a mess better left until later.

#### [ Patrick Massot (Nov 26 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148388303):
isn't useful for the reflexive subcategory stuff?

#### [ Scott Morrison (Nov 26 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148388328):
Yes, but that's not in "this" PR.

#### [ Kevin Buzzard (Dec 01 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/150678603):
This PR has conflicts, apparently. @**Ramon Fernandez Mir** and @**Kenny Lau** have constructed colimits in the category of commutative rings as part of the refactoring schemes project so I got interested in it. This PR is very large -- over 3000 lines. That's a lot of work for Mario and Johannes. Am I right in thinking that this PR is being actively tested and used by Scott, Reid and Johan? My teaching finishes in two weeks. Is there anything I can do to help?

#### [ Johan Commelin (Dec 01 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/150678669):
The current plan is to chop this PR into pieces. Parts have been merged, other parts are currently being PRd.

#### [ Johan Commelin (Dec 01 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/150678674):
So this PR is only around for historical reasons.

#### [ Kevin Buzzard (Dec 01 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/150678725):
I see. Thanks. I've not been watching this category theory stuff at all because I've been extremely busy at work for the last two months. I can now see the light at the end of the tunnel though and I'm trying to work out the state of things. Would the correct thing to do to be to close this PR? Thanks for the pointer to `limits-2`.

#### [ Johan Commelin (Dec 01 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/150678849):
Maybe it should be closed, yes. Or at least a big fat notice that we keep it around because of the discussion on that page, but that it is actively being chopped into pieces.

#### [ Scott Morrison (Dec 02 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/150710544):
I've just closed the original mega-PR.


{% endraw %}
