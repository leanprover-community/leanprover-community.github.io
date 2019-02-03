---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22683mathlibpullrequests.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [mathlib pull requests](https://leanprover-community.github.io/archive/113488general/22683mathlibpullrequests.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Jun 19 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128290679):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> and <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>: There are a lot of pending <a href="https://github.com/leanprover/mathlib/pulls" target="_blank" title="https://github.com/leanprover/mathlib/pulls">PRs</a>. What would you like to do with them?</p>
<p>I understand you were busy in Hanoi for a while. And perhaps you're still busy with other things. This is just a friendly ping to see what your status is.</p>
<p>Every now and then, something comes up that I want to contribute to mathlib, but then I see the list of pending PRs, and I get a bit discouraged, thinking that it might not be worth it. Some pretty simple PRs have not seen any response to indicate what will happen to them.</p>
<p>That said, if you need help managing contributions, I can volunteer some time. I can do commenting, labeling, and merging of simple PRs, while leaving the more interesting ones to you. (Of course, it's <code>git</code>, so things can always be changed later.)</p>

#### [ Sean Leather (Jun 19 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128301673):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Thanks for all your recent PR merges and comments. Just so you know, if you'd like more help with mathlib maintenance, my offer stands.</p>

#### [ Mario Carneiro (Jun 19 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128301799):
<p>I did all the easy stuff. I'm still a bit busy with Tom Hales' conference this week, but some organization or prioritization of existing PRs would be a thing third parties could do to make it easier. Unfortunately in many of the remaining PRs there is something I see a problem with but I haven't found the time to write about it, so for those you may have to just wait or guess (or ask).</p>

#### [ Simon Hudon (Jun 19 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128301866):
<p>Anything I should be doing for <code>refine_struct</code>?</p>

#### [ Mario Carneiro (Jun 19 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128301943):
<p>I'd rather not merge conflicts from github, could you do that? Otherwise it's okay (the conversation and travis failure made it look more complicated than it is, but I see it's ready for merge now.)</p>

#### [ Simon Hudon (Jun 19 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128301948):
<p>Cool, sure thing</p>

#### [ Sean Leather (Jun 19 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128302469):
<blockquote>
<p>some organization or prioritization of existing PRs would be a thing third parties could do to make it easier.</p>
</blockquote>
<p>Yeah, that's basically what I was thinking: triage with labels, assign issues and reviewers, ping the various parties every now and then, and update statuses. If it's an easy/obvious PR, merge it.</p>
<blockquote>
<p>Unfortunately in many of the remaining PRs there is something I see a problem with but I haven't found the time to write about it, so for those you may have to just wait or guess (or ask).</p>
</blockquote>
<p>Yep.</p>

#### [ Simon Hudon (Jun 19 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128307611):
<p>The build time for mathlib is truly incredible. I wonder if we could minimize the rebuild size on every change</p>

#### [ Simon Hudon (Jun 19 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128307764):
<p>This is where a lint tool would be very useful: we could find dead code and spurious dependencies</p>

#### [ Scott Morrison (Jun 20 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128347867):
<p>The <code>refine_struct</code> in mathlib seems to be misbehaving. Here's my MWE:</p>
<div class="codehilite"><pre><span></span>import tactic.interactive

variable (α : Type)
def foo : semigroup α :=
begin
  refine_struct ({ .. } : semigroup α),
end
</pre></div>

#### [ Scott Morrison (Jun 20 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128347907):
<p>Which just says <code>failed</code> on the <code>refine_struct</code>. It seems that it's failing at the very first line <code>str ← e.get_structure_instance_info,</code> of <code>refine_struct</code>.</p>

#### [ Scott Morrison (Jun 20 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128347909):
<p>(<span class="user-mention" data-user-id="110026">@Simon Hudon</span>)</p>

#### [ Sean Leather (Jun 20 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128347969):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Would you mind creating a <a href="https://github.com/leanprover/mathlib/issues/new" target="_blank" title="https://github.com/leanprover/mathlib/issues/new">new GitHub issue</a> with this information? It will make tracking the problem and its solution easier.</p>

#### [ Scott Morrison (Jun 20 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128347984):
<p>Can do! I thought that since it was such a basic thing I might be doing something stupid, and should ask here first. :-)</p>

#### [ Sean Leather (Jun 20 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128348032):
<blockquote>
<p>Can do! I thought that since it was such a basic thing I might be doing something stupid, and should ask here first. :-)</p>
</blockquote>
<p>Even if it is something stupid, others might run into it, too. And it's still easier to search GitHub than Zulip. <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Sean Leather (Jun 20 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128348046):
<p>(That's my personal experience, anyway. Others may have different thoughts.)</p>

#### [ Sean Leather (Jun 20 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128348091):
<p>Of course, you can always check here first and put it there later, I suppose. But I think that creates extra work for you.</p>

#### [ Scott Morrison (Jun 20 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128348372):
<p><a href="https://github.com/leanprover/mathlib/issues/160" target="_blank" title="https://github.com/leanprover/mathlib/issues/160">https://github.com/leanprover/mathlib/issues/160</a></p>

#### [ Simon Hudon (Jun 20 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128358661):
<p>(deleted)</p>


{% endraw %}
