---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20999cachingproofs.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [caching proofs](https://leanprover-community.github.io/archive/113488general/20999cachingproofs.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Sep 18 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150227):
<p>So I'm moving it here.</p>

#### [ Sean Leather (Sep 18 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150232):
<p>From <a href="#narrow/stream/113489-new-members/subject/caching.20proofs/near/134150221" title="#narrow/stream/113489-new-members/subject/caching.20proofs/near/134150221">https://leanprover.zulipchat.com/#narrow/stream/113489-new-members/subject/caching.20proofs/near/134150221</a></p>

#### [ Scott Morrison (Sep 18 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150236):
<p>Thanks.</p>

#### [ Scott Morrison (Sep 18 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150273):
<p>Yes, that second pass is just unavoidably slow.</p>

#### [ Johan Commelin (Sep 18 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150280):
<p>So I'm fine if Travis does that, and I never do it.</p>

#### [ Scott Morrison (Sep 18 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150281):
<p>But I think there's still useful information for the user in seeing the first pass succeed.</p>

#### [ Johan Commelin (Sep 18 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150282):
<p>Or almost never...</p>

#### [ Scott Morrison (Sep 18 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150283):
<p>Yes.</p>

#### [ Sean Leather (Sep 18 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150286):
<p>What exactly are you guys referring to when you say “proof cache”?</p>

#### [ Scott Morrison (Sep 18 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150288):
<p>The point of course is to get back as quickly as possible to responsive editing.</p>

#### [ Scott Morrison (Sep 18 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150295):
<p>(For us poor idiots who use interactive mode, and <em>can't</em>, like some people here, write Lean code while offline. :-)</p>

#### [ Scott Morrison (Sep 18 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150308):
<p>Of course, olean files _are_ a proof cache.</p>

#### [ Scott Morrison (Sep 18 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150312):
<p>So the idea might be merely this:</p>

#### [ Scott Morrison (Sep 18 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150353):
<p>if Lean notices that an olean file is outdated (i.e. the source file, or a dependency source file, is newer)</p>

#### [ Patrick Massot (Sep 18 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150356):
<p>Do you know about <a href="https://github.com/leanprover/lean/issues/1601" target="_blank" title="https://github.com/leanprover/lean/issues/1601">https://github.com/leanprover/lean/issues/1601</a>? Fixing this issue is part of the Lean 4 plan ifI understand correctly</p>

#### [ Scott Morrison (Sep 18 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150364):
<p><em>before</em> disposing of the olean file it loads it one last time</p>

#### [ Scott Morrison (Sep 18 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150380):
<p>and tries to use existing proofs for the current set of lemmas, ignoring on the first pass the actual proof term written in the source file (whether generated in term or tactic mode)</p>

#### [ Scott Morrison (Sep 18 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150386):
<p>but of course eventually there does have to be a second pass that reverifies what the user has written and constructs a new olean.</p>

#### [ Kevin Buzzard (Sep 18 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150446):
<blockquote>
<p>(For us poor idiots who use interactive mode, and <em>can't</em>, like some people here, write Lean code while offline. :-)</p>
</blockquote>
<p>Q1 What's "offline"? Q2 why can't you write code offline? What is interactive mode?</p>

#### [ Johan Commelin (Sep 18 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150523):
<p>I think "offline" here means: Writing code without Lean responding to what you write. (Just using your internal elaborater/kernel to verify your own code.)</p>

#### [ Kevin Buzzard (Sep 18 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150545):
<p>eew.</p>

#### [ Scott Morrison (Sep 18 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150547):
<p>In particular <span class="user-mention" data-user-id="110026">@Simon Hudon</span> appears to have written working code for me without ever running Lean...!</p>

#### [ Scott Morrison (Sep 18 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150599):
<p>(Sometimes I've been able to tell because of some minor typo, meaning it just barely missed actually compiling. :-)</p>

#### [ Johan Commelin (Sep 18 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150602):
<p>In Orsay I witnessed Mario writing half a proof while Lean was thinking. He didn't need to go back and change those 5 lines after Lean caught up with him.</p>

#### [ Scott Morrison (Sep 18 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150603):
<p>It's terrifying, isn't it? :-)</p>

#### [ Scott Morrison (Sep 18 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150610):
<p>Yellow bars just cause my brain to freeze up. :-)</p>

#### [ Sean Leather (Sep 18 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150678):
<p>I don't use interactive mode, so I just see walls of errors, not yellow bars.</p>

#### [ Johan Commelin (Sep 18 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150700):
<blockquote>
<p>I don't use interactive mode, so I just see walls of errors, not yellow bars.</p>
</blockquote>
<p>Wait... do you mean that you write Lean the way I would write C or Python?</p>

#### [ Johan Commelin (Sep 18 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150744):
<p>Edit file → Save → Compile/run the file in terminal → Parse errors → Go back to step 1</p>

#### [ Scott Morrison (Sep 18 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150745):
<p>Well... presumably he doesn't actually ever <em>execute</em> any code.</p>

#### [ Sean Leather (Sep 18 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150748):
<p>Yep.</p>

#### [ Scott Morrison (Sep 18 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150750):
<p>Well, Sean might, actually. :-)</p>

#### [ Sean Leather (Sep 18 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150751):
<p><span class="emoji emoji-1f604" title="big smile">:big_smile:</span></p>

#### [ Johan Commelin (Sep 18 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150756):
<p>Aaahrg... <span class="emoji emoji-1f631" title="scream">:scream:</span> you guys are really crazy...</p>

#### [ Sean Leather (Sep 18 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150807):
<p>Anyway, I'm not sure if it's the same problem as in interactive mode: I'd like to speed up <code>lean --make</code>.</p>

#### [ Sean Leather (Sep 18 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150822):
<p>So, it would be nice if I had all of the generated proof terms for, say, mathlib. So, if I make one change, <code>lean</code> doesn't have to recheck entire files.</p>

#### [ Johan Commelin (Sep 18 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150823):
<p>I guess it is the same bottleneck that we are hitting.</p>

#### [ Sean Leather (Sep 18 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150835):
<p>On the other hand, as Scott said, one small change can change tactics. But I think that should be checked at “release” time.</p>

#### [ Sean Leather (Sep 18 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150836):
<p>... as opposed to “interactive” time.</p>

#### [ Sean Leather (Sep 18 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150846):
<p>So, at the very least, I know proof works. But I may need to go back and check a tactic somewhere afterwards.</p>

#### [ Sean Leather (Sep 18 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150900):
<p>I envision it like having a <code>--fast</code> mode and a <code>--release</code> mode. Names up for debate.</p>

#### [ Johan Commelin (Sep 18 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150912):
<p>We already have trust levels...</p>

#### [ Sean Leather (Sep 18 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150918):
<p>Or <code>--fast</code> and <code>--full</code> to use alliteration.</p>

#### [ Sean Leather (Sep 18 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150922):
<p>How do trust levels come into the picture here?</p>

#### [ Johan Commelin (Sep 18 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150934):
<p>Well, you are putting "trust" in the cache, right?</p>

#### [ Johan Commelin (Sep 18 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150977):
<p>I could envision a new trust level, that will trust cached proofs.</p>

#### [ Johan Commelin (Sep 18 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150983):
<p>Does that make sense?</p>

#### [ Sean Leather (Sep 18 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134150989):
<p>Perhaps. I don't have a clear picture of what that means.</p>

#### [ Sean Leather (Sep 18 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134151006):
<p>I'm not thinking of trust. I'm thinking of checking only what changed within a single file (to simplify the problem).</p>

#### [ Sean Leather (Sep 18 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134151145):
<p>Here's something that doesn't work for all changes, but might work for some: run a quick pass over the interfaces of a file's cached proof terms, check if they differ from the source file, build the ones that differ or are not found in the cache.</p>

#### [ Sean Leather (Sep 18 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134151220):
<p>After that, perhaps you could more lazily regenerate the other proof terms of the file.</p>

#### [ Sean Leather (Sep 18 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134151306):
<p>Also, perhaps the generated proof cache could keep track of failed proofs and Lean would try to rebuild those first.</p>

#### [ Sean Leather (Sep 18 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134151318):
<p>That might improve interactive responsiveness.</p>

#### [ Johan Commelin (Sep 18 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134151328):
<p>I wouldn't mind if Lean did low-priority (in the sense of CPU scheduler) checks to see if my new <code>@[simp]</code> lemma broke a proof <code>by tidy</code> in some files that I didn't have open. But as soon as I make a change in my file the <code>--fast</code> Lean should do a high-priority check to get me back to responsive editing as soon as possible.</p>

#### [ Sean Leather (Sep 18 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134151406):
<p>Yeah, that's the idea, though I was actually thinking <code>--fast</code> wouldn't even try to check the effect of <code>@[simp]</code> lemmas or other things that change how tactics work. But I could see it going either way.</p>

#### [ Johan Commelin (Sep 18 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134151413):
<blockquote>
<p>Do you know about <a href="https://github.com/leanprover/lean/issues/1601" target="_blank" title="https://github.com/leanprover/lean/issues/1601">https://github.com/leanprover/lean/issues/1601</a>? Fixing this issue is part of the Lean 4 plan ifI understand correctly</p>
</blockquote>
<p>That definitely looks relevant! Thanks <span class="user-mention" data-user-id="110031">@Patrick Massot</span></p>

#### [ Sean Leather (Sep 18 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134151538):
<p>Here are two possibilities:</p>
<p>1. An interactive mode that optimizes for checking work-in-progress proofs and reduces the priority of full-file and full-library builds.<br>
2. A fast mode that only checks for work-in-progress proofs and builds a single file at a time and a full mode that builds everything.</p>

#### [ Simon Hudon (Sep 19 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134200810):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span> Isn't that already what the ideas do? I feel like lean-mode does it at least.</p>
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> I do use the interactive modes but sometimes I'm too lazy to go back to emacs to write my code snippets. I'm glad I don't have too bad a track record :)</p>

#### [ Sean Leather (Sep 19 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134212305):
<blockquote>
<p>Isn't that already what the ideas do? I feel like lean-mode does it at least.</p>
</blockquote>
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> What are “the ideas”?</p>
<p>I don't know exactly what does what, so I'm just throwing out some thoughts. I do know that if I make a change in a large file in mathlib and build with <code>lean --make</code>, I see that the entire file has to be built before it gets to my change. That's what I would propose improving.</p>
<p>As I said above, I don't use the interactive approach, and I don't know if the problem I have is the same problem others are discussing.</p>

#### [ Simon Hudon (Sep 19 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134213789):
<p>I misspelled IDE</p>

#### [ Simon Hudon (Sep 19 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134213795):
<p>So what is your workflow like if you don't use them?</p>

#### [ Sean Leather (Sep 19 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134213841):
<p>Edit in <code>vim</code>, run <code>leanpkg build</code>.</p>

#### [ Simon Hudon (Sep 19 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134214709):
<p>That sounds painful</p>

#### [ Sean Leather (Sep 19 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134214720):
<p><span class="emoji emoji-1f937" title="shrug">:shrug:</span> Works well for me.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134214780):
<p>I print the files out, cross out some lines in pencil and add others in, then compile in my head.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134214784):
<p>that's how we did it in the old days before computers</p>

#### [ Sean Leather (Sep 19 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134214792):
<p>How did you print files without computers? <span class="emoji emoji-1f4bb" title="computer">:computer:</span> <span class="emoji emoji-27a1" title="right">:right:</span> <span class="emoji emoji-1f5a8" title="printer">:printer:</span></p>

#### [ Kevin Buzzard (Sep 19 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134214831):
<p>I use my typewriter</p>

#### [ Sean Leather (Sep 19 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134214849):
<p>Oh, they usually refer to that as typing, not printing, right?</p>

#### [ Johan Commelin (Sep 19 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134214864):
<p>He has a printing press à la Gutenberg in his cellar (-;</p>

#### [ Kevin Buzzard (Sep 19 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134214865):
<p>I guess they call it that nowadays.</p>

#### [ Simon Hudon (Sep 19 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134214929):
<p>Amateurs. Here's my workflow: <a href="https://xkcd.com/378/" target="_blank" title="https://xkcd.com/378/">https://xkcd.com/378/</a></p>

#### [ Johan Commelin (Sep 19 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134215138):
<p><code>C-x M-c M-butterfly</code></p>

#### [ Simon Hudon (Sep 19 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/caching%20proofs/near/134256955):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span> I think this is a case in which, before you see what you're missing out on, you don't know that you're missing out. I find it incredibly useful when writing tactic that, as I type and change my scripts, I can see the print out of the example I'm using the tactic on. That save a whole lot of time</p>


{% endraw %}
