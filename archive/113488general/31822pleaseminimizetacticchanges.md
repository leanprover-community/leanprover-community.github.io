---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31822pleaseminimizetacticchanges.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [please minimize tactic changes](https://leanprover-community.github.io/archive/113488general/31822pleaseminimizetacticchanges.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Feb 01 2019 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157346599):
<p>Please minimize tactic changes as it requires the recompiling of essentially the whole mathlib, so the cache is essentially useless, which would cause quite some inconvenience...</p>

#### [ Kenny Lau (Feb 01 2019 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157346602):
<p>particularly the file <code>tactic.interactive</code></p>

#### [ Kenny Lau (Feb 01 2019 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157346652):
<p>AFAICT it takes travis ~ 1 hour to compile the whole mathlib</p>

#### [ Kenny Lau (Feb 01 2019 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157346922):
<p><span class="user-mention" data-user-id="110596">@Rob Lewis</span> What are L349 and L480 doing here? <a href="https://github.com/leanprover-community/mathlib/commit/c9e4f8edc30da76ffa740000957e26aaf79cc31e" target="_blank" title="https://github.com/leanprover-community/mathlib/commit/c9e4f8edc30da76ffa740000957e26aaf79cc31e">https://github.com/leanprover-community/mathlib/commit/c9e4f8edc30da76ffa740000957e26aaf79cc31e</a></p>

#### [ Kenny Lau (Feb 01 2019 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157346935):
<p>(no, don't add another commit to delete those lines, just keep them there)</p>

#### [ Mario Carneiro (Feb 01 2019 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157347046):
<p>Kenny, I'm not sure what your goal is here. Some things invalidate the cache, it's a fact of life. The solution is to make caching better or more precise, not to avoid improvements</p>

#### [ Kenny Lau (Feb 01 2019 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157347095):
<p>I said minimize, not avoid.</p>

#### [ Kenny Lau (Feb 01 2019 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157347122):
<p>So for example we can discuss the details before making changes in order to not generate a situation where A made changes and B is unhappy and then make more changes and then C comes along and make 10 more changes</p>

#### [ Mario Carneiro (Feb 01 2019 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157347143):
<p>sure, but tactic changes require some iteration to get right anyway. I assume it's in a branch, so that's the right place for it</p>

#### [ Kenny Lau (Feb 01 2019 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157347151):
<p>And also we can double check the changes before pushing it to mathlib to make sure that it doesn't contain extra lines.</p>

#### [ Kenny Lau (Feb 01 2019 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157347200):
<blockquote>
<p>sure, but tactic changes require some iteration to get right anyway. I assume it's in a branch, so that's the right place for it</p>
</blockquote>
<p>it's in the master branch...</p>

#### [ Kenny Lau (Feb 01 2019 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157347213):
<p>Have you clicked on the link above?</p>

#### [ Mario Carneiro (Feb 01 2019 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157347327):
<p>there are obviously some commented trace lines that were added. They can be removed</p>

#### [ Mario Carneiro (Feb 01 2019 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157347430):
<p>but it's absolutely the wrong idea to change commit or PR habits for worry of recompilation. Problems that need fixing should be fixed</p>

#### [ Kevin Buzzard (Feb 01 2019 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157348123):
<p>I am the anti-Kenny on this one. What is the hurry? Who cares if something takes an hour to compile? It will take less than an hour next year. Kenny just needs a better computer, that's the real problem. We can't change our behaviour to work around the fact that Kenny needs a better computer.</p>

#### [ Mario Carneiro (Feb 01 2019 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157348249):
<p>also it's an hour of Travis's time, not mine</p>

#### [ Mario Carneiro (Feb 01 2019 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157348278):
<p>(thanks travis for your donation of significant computing time to FOSS projects)</p>

#### [ Joe Hendrix (Feb 02 2019 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157405161):
<p>I definitely consider imports and impact of frequent changes on compilation in developing Haskell.  Like I'll think about partitioning a module if part of it changes frequently, but modules that import it tend to only need the stable parts.<br>
That said, you shouldn't hold off deleting dead code just to avoid recompiling a module.</p>

#### [ Simon Hudon (Feb 02 2019 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157405636):
<p>mathlib could definitely stand to be divided more finely and its dependencies need to be disentangled. But we don't have a warning on spurious imports. We need to build a tool for that</p>

#### [ Kenny Lau (Feb 02 2019 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157405698):
<p>I think someone can produce an import graph... I don't know enough programming to do that</p>

#### [ Simon Hudon (Feb 02 2019 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/please%20minimize%20tactic%20changes/near/157405749):
<p>Mario wrote a parser for olean files. I think that will be a good starting point. It's on my todo list</p>


{% endraw %}
