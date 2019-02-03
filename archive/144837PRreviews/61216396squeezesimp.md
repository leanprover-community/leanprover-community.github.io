---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/61216396squeezesimp.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#396 squeeze_simp](https://leanprover-community.github.io/archive/144837PRreviews/61216396squeezesimp.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Oct 07 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135353930):
<p><a href="https://github.com/leanprover/mathlib/issues/396" target="_blank" title="https://github.com/leanprover/mathlib/issues/396">#396</a></p>

#### [ Kenny Lau (Oct 07 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135353970):
<p>I'm afraid some of the changes to the tactic files in the <code>faster</code> branch hasn't been transferred to the <code>squeeze_simp</code> PR</p>

#### [ Kenny Lau (Oct 07 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135353972):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what should I do?</p>

#### [ Mario Carneiro (Oct 07 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354026):
<p>make another follow-on PR...  what was it?</p>

#### [ Kenny Lau (Oct 07 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354029):
<p>I don't really know what happened, now that the history has been erased</p>

#### [ Kenny Lau (Oct 07 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354036):
<p>I just see that some changes to the tactic files have not been incorporated</p>

#### [ Mario Carneiro (Oct 07 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354083):
<p>if you rebase the <code>faster</code> branch on master, it should remove any parts that are already merged, leaving only the stuff that is missing</p>

#### [ Kenny Lau (Oct 07 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354089):
<p>I've rebased the <code>faster</code> branch on master</p>

#### [ Kenny Lau (Oct 07 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354090):
<p>maybe I should rebase the <code>squeeze-simp</code> branch on master and see what happens</p>

#### [ Kenny Lau (Oct 07 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354091):
<p>is this a good idea?</p>

#### [ Mario Carneiro (Oct 07 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354137):
<p>squeeze-simp is already merged, so if you rebase it on master it will disappear</p>

#### [ Kenny Lau (Oct 07 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354144):
<p>just look at <a href="https://github.com/leanprover/mathlib/compare/master...leanprover-community:faster#diff-a5e03974850487ddd92200ffaf57f9b2L18" target="_blank" title="https://github.com/leanprover/mathlib/compare/master...leanprover-community:faster#diff-a5e03974850487ddd92200ffaf57f9b2L18">this</a></p>

#### [ Kenny Lau (Oct 07 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354152):
<p>hmm</p>

#### [ Kenny Lau (Oct 07 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354153):
<p>I see that the <code>squeeze-simp</code> branch has been changed after its separation from <code>faster</code></p>

#### [ Kenny Lau (Oct 07 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354154):
<p>at this point I don't know what to do anymore</p>

#### [ Mario Carneiro (Oct 07 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354156):
<p>just delete/revert any changes in those files</p>

#### [ Kenny Lau (Oct 07 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354201):
<p>hmm</p>

#### [ Kenny Lau (Oct 07 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354261):
<p>how about <a href="https://github.com/leanprover/mathlib/compare/master...leanprover-community:faster#diff-47cbe97193e277c9a413e62bc8afadffR15" target="_blank" title="https://github.com/leanprover/mathlib/compare/master...leanprover-community:faster#diff-47cbe97193e277c9a413e62bc8afadffR15">this</a>?</p>

#### [ Kenny Lau (Oct 07 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135354266):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> could you clarify which one is the intended version?</p>

#### [ Simon Hudon (Oct 07 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135360028):
<p>Hi! I made some changes to in <code>squeeze-simp</code> to add documentation and make the tactic usable for <span class="user-mention" data-user-id="110087">@Scott Morrison</span> to use in <code>tidy</code></p>

#### [ Simon Hudon (Oct 07 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135360029):
<p>This is a great idea to have this stream btw</p>

#### [ Kenny Lau (Oct 07 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135360133):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> did you see my link?</p>

#### [ Simon Hudon (Oct 07 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135360194):
<p>I have. It seems to confirm what I thought the diff would be. Is there something in particular that you're trying to highlight?</p>

#### [ Kenny Lau (Oct 07 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135360241):
<p>if you wait for a while after opening the link, it will show you one line I highlighted</p>

#### [ Kenny Lau (Oct 07 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135360247):
<p>so in particular I'm talking about the file <code>meta/rb_map.lean</code></p>

#### [ Kenny Lau (Oct 07 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135360248):
<p>could you clarify which side is the version you want mathlib to have</p>

#### [ Simon Hudon (Oct 07 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135360943):
<p>I think either one can work. I ended up not needing those functions I think but they are generally useful functions so we can keep them.</p>

#### [ Kenny Lau (Oct 07 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135362776):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> then which one of us should make a new PR?</p>

#### [ Simon Hudon (Oct 07 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135362782):
<p>Why do we need a new PR?</p>

#### [ Kenny Lau (Oct 07 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135362786):
<p>the same reason this one is a PR separate from <code>faster</code></p>

#### [ Simon Hudon (Oct 07 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135362891):
<p>I don't think it's worth making a separate PR for it. If you want to take it out of yours, let's just bring it back when we need it.</p>

#### [ Kenny Lau (Oct 07 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135362894):
<p>ok</p>

#### [ Kenny Lau (Oct 07 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135362895):
<p>how do I do this?</p>

#### [ Kenny Lau (Oct 07 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135362900):
<p>is there some <code>git</code> magic that will let me do this or do I have to do it manually?</p>

#### [ Simon Hudon (Oct 07 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135363076):
<p>With <code>git log meta/rb_map.lean</code>, you can check what is the latest commit that changed the file, that's probably where I introduced those functions.</p>

#### [ Simon Hudon (Oct 07 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23396%20squeeze_simp/near/135363086):
<p>Actually, let me look into it, I'll create the PR while I'm at it</p>


{% endraw %}
