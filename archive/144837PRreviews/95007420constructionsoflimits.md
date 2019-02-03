---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/95007420constructionsoflimits.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#420 constructions of limits](https://leanprover-community.github.io/archive/144837PRreviews/95007420constructionsoflimits.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Oct 14 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135788640):
<p>This extends the first PR on (co)limits. It</p>
<p>Shows that C ⥤ D has limits if D does.<br>
Constructs equalizers and products from limits.<br>
Constucts limits from equalizers and products.<br>
Constructs pullback from equalizers and binary products.</p>

#### [ Kenny Lau (Oct 14 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135793797):
<p>Is <code>simp</code> slower or is <code>obviously</code> slower?</p>

#### [ Kenny Lau (Oct 14 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135793798):
<p>And do you care at all? <span class="user-mention" data-user-id="110087">@Scott Morrison</span></p>

#### [ Mario Carneiro (Oct 14 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135794099):
<p>it's <code>obviously</code> slower</p>

#### [ Mario Carneiro (Oct 14 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135794107):
<p>I'm pretty sure that your compile time optimization goals are in direct opposition with Scott's goals</p>

#### [ Mario Carneiro (Oct 14 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135794113):
<p>which is why he was so sad to read your <code>faster</code> branch</p>

#### [ Mario Carneiro (Oct 14 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135794160):
<p><code>obviously</code> calls everything else, including <code>simp</code></p>

#### [ Kenny Lau (Oct 14 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135794176):
<p>well I'm also sad to read this PR.</p>

#### [ Mario Carneiro (Oct 14 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135794323):
<p>I think that's fair. <span class="user-mention" data-user-id="110087">@Scott Morrison</span> is there a reason you have decided to use <code>obviously</code> directly instead of the script that it generates?</p>

#### [ Scott Morrison (Oct 15 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135796411):
<p>So that I don't have to do any copying and pasting? :-)</p>

#### [ Scott Morrison (Oct 15 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135796427):
<p>So that the compile time of mathlib grows so large that more effort is put into tactic caching? :-)</p>

#### [ Kenny Lau (Oct 15 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135796464):
<p>:-)</p>

#### [ Scott Morrison (Oct 15 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135796475):
<p>I've already ripped out a huge number of <code>obviously</code> in these two PRs. All the sequences of <code>rw</code> are actually generated automatically by <code>rewrite_search</code> in my still-private version of <code>obviously</code>.</p>

#### [ Scott Morrison (Oct 15 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23420%20constructions%20of%20limits/near/135796477):
<p>I can rip out more, of course ...</p>


{% endraw %}
