---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/90517484miscellaneoustopology.html
---

## Stream: [PR reviews](index.html)
### Topic: [#484 miscellaneous topology](90517484miscellaneoustopology.html)

---


{% raw %}
#### [ Sebastien Gouezel (Dec 09 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23484%20miscellaneous%20topology/near/151228688):
<p>I have a lot of new material to add on top of <a href="https://github.com/leanprover/mathlib/issues/484" target="_blank" title="https://github.com/leanprover/mathlib/issues/484">#484</a>, especially on the Hausdorff distance but I think the main interest for the community would be all the missing lemmas I had to add to the library while developping the Hausdorff distance. However, it makes no sense to PR it while <a href="https://github.com/leanprover/mathlib/issues/484" target="_blank" title="https://github.com/leanprover/mathlib/issues/484">#484</a> (and <a href="https://github.com/leanprover/mathlib/issues/464" target="_blank" title="https://github.com/leanprover/mathlib/issues/464">#464</a>) are not integrated. Is there something I could do to help the process?</p>

#### [ Patrick Massot (Dec 09 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23484%20miscellaneous%20topology/near/151234264):
<p>I agree it would be nice to merge this and add more stuff. <span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span> would you mind pushing this to the community repository so that I could try some  stylistic improvements? You could revert anything you don't like. <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> could you make sure Sébastien has push access to the community repository?</p>

#### [ Patrick Massot (Dec 09 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23484%20miscellaneous%20topology/near/151234314):
<p>Also, I think that, once this will be merged, I'll probably try to reorganize files in this topology directory which is a mess (I'm working again on uniform spaces)</p>

#### [ Patrick Massot (Dec 09 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23484%20miscellaneous%20topology/near/151234715):
<p>Is it accepted mathlib style to use all those <code>have ..., begin ... end</code> instead of curly brackets?</p>

#### [ Sebastien Gouezel (Dec 09 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23484%20miscellaneous%20topology/near/151235986):
<blockquote>
<p><span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span> would you mind pushing this to the community repository so that I could try some  stylistic improvements?</p>
</blockquote>
<p>Should be done, if my git almost-nonexisting-skills did not betray me.</p>

#### [ Sebastien Gouezel (Dec 09 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23484%20miscellaneous%20topology/near/151236184):
<blockquote>
<p>Is it accepted mathlib style to use all those <code>have ..., begin ... end</code> instead of curly brackets?</p>
</blockquote>
<p>My impression is that curly brackets are for the case where there are several goals and you want to solve them one by one, separating them explicitly. While begin...end is for proof blocks in general.</p>

#### [ Johannes Hölzl (Dec 10 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23484%20miscellaneous%20topology/near/151259207):
<p>Hi <span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span> , the lectures end this week, I hope I find some time to review &amp; merge your PRs</p>


{% endraw %}
