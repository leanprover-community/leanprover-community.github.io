---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/06572rebasing.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [rebasing](https://leanprover-community.github.io/archive/144837PRreviews/06572rebasing.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Nov 13 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147631335):
<p>Hi <span class="user-mention" data-user-id="110032">@Reid Barton</span>, <span class="user-mention" data-user-id="112680">@Johan Commelin</span>. I'm about to rebase <code>limits-others-new</code>. This is going to leave <code>adjunctions</code> and <code>sheaf</code> in a strange position.</p>

#### [ Scott Morrison (Nov 13 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147631352):
<p>Would it be okay if I rebased either of both of those onto the new <code>limits</code> branch?</p>

#### [ Scott Morrison (Nov 14 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147632148):
<p>It would mean doing a force push to <code>community/adjunctions</code> and/or to <code>community/sheaf</code>, so I'd need to get the okay that you're not actively working on that branch.</p>

#### [ Reid Barton (Nov 14 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147634851):
<p>Yes, feel free, or I am also happy to take care of the rebase myself.</p>

#### [ Scott Morrison (Nov 14 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147635786):
<p>Maybe it's best if you do it, so I don't mess up authorship information.</p>

#### [ Scott Morrison (Nov 14 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147635875):
<p>oh, worked it out :-)</p>

#### [ Johan Commelin (Nov 14 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147649877):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Please go ahead with rebasing <code>sheaf</code>. I have no idea how to do that...</p>

#### [ Scott Morrison (Nov 14 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147651466):
<p>Done! Your old history is now on the <code>sheaf-old</code> branch, but if everything looks okay we can delete that.</p>

#### [ Johan Commelin (Nov 14 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147651669):
<p>Thanks, I'll take a look!</p>

#### [ Johan Commelin (Nov 14 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147651728):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Hmm, that's easier said than done.</p>

#### [ Johan Commelin (Nov 14 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147651730):
<p>How do I take a look?</p>

#### [ Johan Commelin (Nov 14 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147651733):
<p><code>git pull origin sheaf</code> gives me an aweful lot of merge conflicts in files that are not <code>sheaf.lean</code></p>

#### [ Keeley Hoek (Nov 14 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147652154):
<p>Hi Johan, Try</p>
<div class="codehilite"><pre><span></span>git merge --abort
git checkout sheaf
git branch -m sheaf-old
git branch sheaf-old -u origin/sheaf-old
git fetch
git checkout -b sheaf origin/sheaf
</pre></div>

#### [ Keeley Hoek (Nov 14 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147652156):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span></p>

#### [ Keeley Hoek (Nov 14 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147652200):
<p>The new sheafs will be <code>sheaf</code>, the old sheafs will be <code>sheaf-old</code></p>

#### [ Johan Commelin (Nov 14 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147652317):
<p>Thanks <span class="user-mention" data-user-id="110111">@Keeley Hoek</span>, that seems to have worked git-wise. Now checking if Lean is happy by recompiling.</p>

#### [ Johan Commelin (Nov 14 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147653409):
<p>Oh boy, lots of red squiggles....</p>

#### [ Kevin Buzzard (Nov 14 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147653417):
<p>how christmassy</p>

#### [ Scott Morrison (Nov 14 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147653467):
<p>Thanks Keeley for the instructions!</p>

#### [ Scott Morrison (Nov 14 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147653470):
<p>Are things working, Johan?</p>

#### [ Johan Commelin (Nov 14 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147653475):
<p>Nope, not really...</p>

#### [ Johan Commelin (Nov 14 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147653484):
<p>I feel like I should start taking a more structured approach. Because this file has been growing like a kludge of hacks.</p>

#### [ Scott Morrison (Nov 14 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147653492):
<p>Sorry, let me try compiling here. :-)</p>

#### [ Scott Morrison (Nov 14 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147655679):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>, all but one error fixed, which is just an unfinished proof at the bottom.</p>

#### [ Scott Morrison (Nov 14 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147655692):
<p>There was a universe issue, a missing simp lemma, and the syntax of yoneda had changed.</p>

#### [ Johan Commelin (Nov 14 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147661373):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Thanks a lot! (Sorry, I had seminars and then lunch...)</p>


{% endraw %}
