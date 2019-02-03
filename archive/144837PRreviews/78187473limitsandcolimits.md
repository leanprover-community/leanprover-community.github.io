---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/78187473limitsandcolimits.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#473 limits and colimits](https://leanprover-community.github.io/archive/144837PRreviews/78187473limitsandcolimits.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Nov 19 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952349):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> has taken this PR through a couple of revisions, but I think it is quite solid and stable now. I've been stress testing it quite a bit on my <code>sheaf</code> branch, and I think it works well. Do others have any comments?</p>

#### [ Johan Commelin (Nov 19 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952393):
<p>I don't think we should add new stuff to this PR, but people are accumulating follow-up stuff.</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952555):
<p>I think Kenny pointed out that this PR uses a lot of high automation. Are there any really expensive files in here?</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952606):
<p>maybe add a few more <code>tidy says:</code> bits</p>

#### [ Johan Commelin (Nov 19 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952756):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Isn't this battling in the wrong direction?</p>

#### [ Johan Commelin (Nov 19 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952768):
<p>And tons of this automation is hidden in auto_params. We really don't want to see those.</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952911):
<p>yes, I realize that, and we had this conversation already with the <code>faster</code> branch</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952920):
<p>The fact is that people compile mathlib often, and doubling the compile time is not a good thing</p>

#### [ Johan Commelin (Nov 19 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952922):
<p>Sure, but there we didn't really rewrite much. We only expanded <code>simp</code>s into <code>simp only</code>s.</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952928):
<p>and here we can expand <code>tidy</code> into its proof script without much work</p>

#### [ Mario Carneiro (Nov 19 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147952977):
<p>If it is fast enough, I don't even think that is necessary, but any tactics that take more than a few seconds should probably be unrolled a bit</p>

#### [ Scott Morrison (Nov 19 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147954782):
<p>Ok, the <code>limits</code> directory currently invokes <code>tidy</code> 156 times, and spends  107s inside <code>tidy</code>.  34 of these invocations take more than a second each.</p>

#### [ Scott Morrison (Nov 19 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147954784):
<p>Only one takes more than 4.</p>

#### [ Scott Morrison (Nov 19 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955040):
<p>How do you make <code>lean --make</code> run single threaded?</p>

#### [ Scott Morrison (Nov 19 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955047):
<p>The output from <code>--profile</code> is all jumbled up, and I can't tell which output is from which declaration. :-(</p>

#### [ Rob Lewis (Nov 19 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955100):
<p><code>-j0</code>, I think.</p>

#### [ Kenny Lau (Nov 19 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955104):
<p>if you use <code>--profile</code>, only look at the STDERR</p>

#### [ Kenny Lau (Nov 19 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955106):
<p>I mean</p>

#### [ Kenny Lau (Nov 19 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955108):
<p>only look at the STDOUT</p>

#### [ Kenny Lau (Nov 19 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955112):
<p>I actually forgot which one to look at</p>

#### [ Scott Morrison (Nov 19 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955121):
<p>even then, if two declarations are running at once, I was having their profile output interspersed</p>

#### [ Kenny Lau (Nov 19 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955148):
<p><code>git ls-files *.lean | xargs -I % sh -c '&gt;&amp;2 echo %; lean --profile % &gt;/dev/null;' &gt; profile.txt 2&gt;&amp;1</code></p>

#### [ Kenny Lau (Nov 19 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955151):
<p>this is how I use it</p>

#### [ Scott Morrison (Nov 19 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955152):
<p>hmm.. even with <code>-j0</code> I can't make sense of the output.</p>

#### [ Scott Morrison (Nov 19 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955199):
<p>Hmm... could you show me how to run that just on a subdirectory?</p>

#### [ Scott Morrison (Nov 19 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955211):
<p>Can I just change the <code>*.lean</code>?</p>

#### [ Scott Morrison (Nov 19 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955243):
<p>Kenny, your scripts seems to only tell me totals by file. Is that what you intended?</p>

#### [ Kenny Lau (Nov 19 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955521):
<p>yes...</p>

#### [ Scott Morrison (Nov 19 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955582):
<p>That's not going to help me at all.</p>

#### [ Kenny Lau (Nov 19 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955586):
<p>i'll excuse myself before you realize that i don't know anything about bash :P</p>

#### [ Scott Morrison (Nov 19 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955591):
<p>From what I can see, the instances of <code>tidy</code> that take more than a second don't even appear in the source file, they're in <code>auto_param</code>s.</p>

#### [ Johan Commelin (Nov 19 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955669):
<p>/me hears a background choir chanting <em>"We want caching! We want caching! We want caching..."</em></p>

#### [ Scott Morrison (Nov 19 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147955737):
<p>I think, until someone comes up with caching and/or faster tactic execution, I might find something more productive to do... Writing out human-irrelevant proofs for the sake of compilation times is the surest sign I've seen yet that this is all a bad idea. :-(</p>

#### [ Mario Carneiro (Nov 19 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147956525):
<p>If you would rather have someone else do it we can postpone it until someone else gets annoyed at compile times enough to do something about it...</p>

#### [ Mario Carneiro (Nov 19 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147956557):
<p>or until someone actually puts those caching ideas into practice</p>

#### [ Patrick Massot (Nov 19 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147956620):
<p>An intermediate goal which looks much easier would be to find a way to collect olean built by travis as something people could download and use right away</p>

#### [ Mario Carneiro (Nov 19 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147957272):
<p>How portable have you found them to be?</p>

#### [ Patrick Massot (Nov 19 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147957330):
<p>Sebastian claims they should be portable enough</p>

#### [ Kevin Buzzard (Nov 19 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147957997):
<p>For sure I've had no problem making them on one win10 machine and using them on another</p>

#### [ Kevin Buzzard (Nov 19 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147958014):
<p>One has to make sure that the file transfer doesn't mangle the timestamps though</p>

#### [ Patrick Massot (Nov 19 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147958020):
<p>If I remember correctly, Sebastian said they should even work across OSs. The only things that needs care are timestamps</p>

#### [ Patrick Massot (Nov 19 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147998722):
<p>Who wants to try downloading <a href="https://www.math.u-psud.fr/~pmassot/mathlib.tar.gz" target="_blank" title="https://www.math.u-psud.fr/~pmassot/mathlib.tar.gz">https://www.math.u-psud.fr/~pmassot/mathlib.tar.gz</a> and play with it to see whether olean can be reused? It's a freshly compiled mathlib (without the <code>.git</code> directory)</p>

#### [ Rob Lewis (Nov 19 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147999684):
<p>This doesn't work for me, at least not in an obvious way. I unzipped and created <code>test.lean</code> in the root directory. Adding <code>import data.real.basic</code> starts recompiling everything.</p>

#### [ Rob Lewis (Nov 19 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/147999870):
<p>(I'm on my Windows laptop, by the way, using msys2.)</p>

#### [ Patrick Massot (Nov 19 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000002):
<p>What if you touch all olean files? (assuming <code>touch</code> exists on Windows)</p>

#### [ Rob Lewis (Nov 19 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000259):
<p>Doesn't seem to make a difference.</p>

#### [ Mario Carneiro (Nov 19 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000638):
<p>I have had success with using <code>touch</code> in the past</p>

#### [ Mario Carneiro (Nov 19 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000680):
<p>if you touch the files then lean will accept them as correct without checking, regardless of the actual status</p>

#### [ Mario Carneiro (Nov 19 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000691):
<p>so you get funny errors sometimes but it usually worksish</p>

#### [ Rob Lewis (Nov 19 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000744):
<p>Just the .oleans? Just the .leans? Both?</p>

#### [ Mario Carneiro (Nov 19 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000754):
<p>just the oleans</p>

#### [ Rob Lewis (Nov 19 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000759):
<p>I tried just the .oleans and both, neither seemed to do the trick.</p>

#### [ Mario Carneiro (Nov 19 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000769):
<p>also the oleans have to be touched in dependency order or very fast</p>

#### [ Rob Lewis (Nov 19 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000803):
<p>Um, okay, that I definitely didn't do.</p>

#### [ Rob Lewis (Nov 19 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000811):
<p><code>find  -type f  -name "*.olean" -exec touch {} +</code> must not have been fast enough.</p>

#### [ Mario Carneiro (Nov 19 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000821):
<p>I think within a second should do</p>

#### [ Mario Carneiro (Nov 19 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000866):
<p>you can check the modification dates</p>

#### [ Mario Carneiro (Nov 19 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148000876):
<p>alternatively, find a bashism to get the current time and set all the files to that</p>

#### [ Rob Lewis (Nov 19 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148001821):
<p>Still not having any luck. I've set the timestamp on all .olean files to match a random file (with a later timestamp than any of the .leans). It still starts recompiling when I import anything.</p>

#### [ Mario Carneiro (Nov 19 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148002004):
<p>oh I see</p>

#### [ Mario Carneiro (Nov 19 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148002016):
<p>I get a quick <code>lean --make</code> this way</p>

#### [ Rob Lewis (Nov 19 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148002162):
<p>But with your own .oleans, right? Not with foreign ones?</p>

#### [ Mario Carneiro (Nov 19 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148002171):
<p>yes</p>

#### [ Mario Carneiro (Nov 19 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148002245):
<p>I've never tested anything with foreign oleans. It's hard enough to get lean to accept native ones</p>

#### [ Reid Barton (Nov 19 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148002544):
<p>Unrelated to sharing olean files... I'm inclined to take this PR and split it into a logical series of commits, partly for my own understanding and partly to aid with review. Would that be helpful?</p>

#### [ Mario Carneiro (Nov 20 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148002745):
<p>yes. Anything I can't review in one sitting gets delayed a lot more than it should</p>

#### [ Scott Morrison (Nov 20 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148008047):
<p>Thank you, Reid, that would be fantastic.</p>

#### [ Patrick Massot (Nov 20 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148028515):
<p>I just tested in my office: my olean compiled at home work perfectly here. I'm not running up to date mathlib, I can use <code>mono</code> without any delay</p>

#### [ Rob Lewis (Nov 20 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148028645):
<p>Patrick, what steps are you doing to test it, and what OS are you using on either end?</p>

#### [ Rob Lewis (Nov 20 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148028654):
<p>I just tried it on my (Linux) office desktop and saw the same behavior as on my laptop last night.</p>

#### [ Patrick Massot (Nov 20 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148030294):
<p>I'm using Linux on all my computers. What I just did was: </p>
<div class="codehilite"><pre><span></span>cd mathlib
mv .git ..
cd ..
rm -rf mathlib
wget https://www.math.u-psud.fr/~pmassot/mathlib.tar.gz
tar xf mathlib.tar.gz
mv .git mathlib/
</pre></div>


<p>Then I opened the mathlib folder in VScode, created a scratch file at the root of mathlib, with the monotonicity examples I wrote yesterday in the "What's new" thread</p>

#### [ Patrick Massot (Nov 20 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148030375):
<p>Of course the <code>.git</code> stuff is there only because I want to preserve my local branches and didn't want to clutter the tar.gz with them</p>

#### [ Rob Lewis (Nov 20 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148031165):
<p>Then I don't know what the difference is, I did effectively the same thing (without the git stuff).</p>

#### [ Rob Lewis (Nov 20 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148031179):
<p>Do .olean files track the version of Lean used to compile them? What versions are you using on each computer?</p>

#### [ Johan Commelin (Nov 20 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148032765):
<p>It works for me! I downloaded Patrick's files, and I could immediately run the <code>mono</code> example from the other thread. No recompiles.</p>

#### [ Johan Commelin (Nov 20 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148032767):
<p>I'm on a Linux box.</p>

#### [ Patrick Massot (Nov 20 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148034169):
<p>The version of Lean should be enforced by the leanpkg.toml (I'm using elan)</p>

#### [ Scott Morrison (Nov 22 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148147105):
<p>Reid has just pushed a subset of the limits PR, which just contains the preparatory work. <a href="https://github.com/leanprover/mathlib/pull/488" target="_blank" title="https://github.com/leanprover/mathlib/pull/488">https://github.com/leanprover/mathlib/pull/488</a></p>

#### [ Scott Morrison (Nov 22 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148147109):
<p>Thanks, <span class="user-mention" data-user-id="110032">@Reid Barton</span>, very much for doing this!</p>

#### [ Scott Morrison (Nov 24 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148270095):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>, the preliminary PR was just merged. How should we handle the next chunk? I could rebase the big PR onto master, but I'm not actually sure that's useful.</p>

#### [ Scott Morrison (Nov 26 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148336028):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>, do you have a moment to discuss next steps with the limits PRs?</p>

#### [ Reid Barton (Nov 26 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148336287):
<p>I'm actually in the midst of going through <code>limits.lean</code></p>

#### [ Scott Morrison (Nov 26 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148336290):
<p>Great, okay, I'll leave you to it, in that case!</p>

#### [ Reid Barton (Nov 26 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148336990):
<p>currently in the phase of dualizing all my changes. It's a lot of typing...</p>

#### [ Scott Morrison (Nov 26 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148337094):
<p>sorry :-(</p>

#### [ Scott Morrison (Nov 26 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148337099):
<p>Think of it as a meditative practice.</p>

#### [ Reid Barton (Nov 26 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148337213):
<p>Well, it suddenly got interesting because one of the proofs is refusing to dualize</p>

#### [ Reid Barton (Nov 26 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148337460):
<p>OK, I defeated it, but a mystery for sure...</p>

#### [ Reid Barton (Nov 26 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148337470):
<p>I suspect <code>erw</code> uses some black magic</p>

#### [ Johan Commelin (Nov 26 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148345984):
<p>I made some trivial comments. Feel free to ignore them.<br>
I squashed some double newlines into one. (Don't know if this is appreciated.)<br>
I also think we can scrape a bunch of lemmas into namespaces, because now we have 20 lemmas after each other, that all start with <code>limit.</code>.</p>

#### [ Reid Barton (Nov 26 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148370732):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I'm going to drop the stuff about creating limits for now, because it doesn't appear to be used currently and I found about seven definitions of "F creates limits" which I think are all inequivalent.</p>

#### [ Scott Morrison (Nov 26 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148388233):
<p>Sounds very reasonable. I think I followed the definition in Emily Riehl's book, but I agree it's a mess, and a mess better left until later.</p>

#### [ Patrick Massot (Nov 26 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148388303):
<p>isn't useful for the reflexive subcategory stuff?</p>

#### [ Scott Morrison (Nov 26 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/148388328):
<p>Yes, but that's not in "this" PR.</p>

#### [ Kevin Buzzard (Dec 01 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/150678603):
<p>This PR has conflicts, apparently. <span class="user-mention" data-user-id="132858">@Ramon Fernandez Mir</span> and <span class="user-mention" data-user-id="110064">@Kenny Lau</span> have constructed colimits in the category of commutative rings as part of the refactoring schemes project so I got interested in it. This PR is very large -- over 3000 lines. That's a lot of work for Mario and Johannes. Am I right in thinking that this PR is being actively tested and used by Scott, Reid and Johan? My teaching finishes in two weeks. Is there anything I can do to help?</p>

#### [ Johan Commelin (Dec 01 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/150678669):
<p>The current plan is to chop this PR into pieces. Parts have been merged, other parts are currently being PRd.</p>

#### [ Johan Commelin (Dec 01 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/150678674):
<p>So this PR is only around for historical reasons.</p>

#### [ Kevin Buzzard (Dec 01 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/150678725):
<p>I see. Thanks. I've not been watching this category theory stuff at all because I've been extremely busy at work for the last two months. I can now see the light at the end of the tunnel though and I'm trying to work out the state of things. Would the correct thing to do to be to close this PR? Thanks for the pointer to <code>limits-2</code>.</p>

#### [ Johan Commelin (Dec 01 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/150678849):
<p>Maybe it should be closed, yes. Or at least a big fat notice that we keep it around because of the discussion on that page, but that it is actively being chopped into pieces.</p>

#### [ Scott Morrison (Dec 02 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23473%20limits%20and%20colimits/near/150710544):
<p>I've just closed the original mega-PR.</p>


{% endraw %}
