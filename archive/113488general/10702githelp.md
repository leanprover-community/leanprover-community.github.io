---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/10702githelp.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [git help](https://leanprover-community.github.io/archive/113488general/10702githelp.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Apr 11 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124926688):
<p>Sorry to have to ask about mundane things like how to use git, but... Say that I've got a fork of mathlib that is borked in some way (in my case, I merged in a commit from master, that Mario shortly thereafter deleted, but I have a branch that includes it).</p>
<p>Should I:<br>
1) Just delete my whole fork (this is a good moment to do so, I have only two modified files).<br>
2) Learn about ... rebasing? something else? Is it possible to actually get my master branch back to matching the main repository's master branch?</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124926741):
<blockquote>
<p>Is it possible to actually get my master branch back to matching the main repository's master branch?</p>
</blockquote>
<p><code>git reset --hard origin/master</code></p>

#### [ Scott Morrison (Apr 11 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124926745):
<p>But what about all the pushed commits to master on my github fork?</p>

#### [ Scott Morrison (Apr 11 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124926784):
<p>That won't bring my fork hosted on github back to matching the corresponding branch on the main github repo, will it?</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124926797):
<p>Ah. It will after a <code>git push --force &lt;your remote&gt;</code>.</p>

#### [ Scott Morrison (Apr 11 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124926866):
<p>But ... don't I have to strip commits or something?</p>

#### [ Scott Morrison (Apr 11 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124926869):
<p>I want my master branch in my fork to really look (history and everything) just like the master branch in origin.</p>

#### [ Scott Morrison (Apr 11 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124926911):
<p>Or is it okay to just continue on with my fork having its own alternative borked history?</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124926913):
<p>After these two commands, your fork's master will look exactly like the one in origin</p>

#### [ Scott Morrison (Apr 11 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124926967):
<p>Ah, and the <code>--hard</code> you added above means I don't even need to <code>git checkout -- .</code>. Thanks.</p>

#### [ Scott Morrison (Apr 11 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124927019):
<p>Wow, amazing! Everything is beautiful. :-)</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124927025):
<p>:)</p>


{% endraw %}
