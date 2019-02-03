---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/13525512discretecategories.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#512 discrete categories](https://leanprover-community.github.io/archive/144837PRreviews/13525512discretecategories.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Dec 05 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/150904838):
<p>Really this is "everything that I thought worth saving from the old limits PR, not including anything about special shapes".</p>

#### [ Scott Morrison (Dec 05 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/150904883):
<p>In particular it includes discrete categories, and some minor tidying in several files.</p>

#### [ Scott Morrison (Dec 05 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/150904974):
<p>I've also rebased what remains of my "special shape limits" work onto this. (This is not intended as any endorsement of the contents. :-)</p>

#### [ Johan Commelin (Dec 05 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/150905483):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Looks good to me. Isn't the <code>of_obj</code> in your PR superseded by my <code>of</code>-PR?</p>

#### [ Scott Morrison (Dec 05 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/150905494):
<p>Ah, yes, I'd forgotten that.</p>

#### [ Scott Morrison (Dec 05 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/150905496):
<p>Is yours already merged?</p>

#### [ Johan Commelin (Dec 05 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/150905546):
<p>Nope, not yet.</p>

#### [ Scott Morrison (Dec 05 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/150905778):
<p>ok, I removed <code>of_obj</code> again</p>

#### [ Reid Barton (Dec 07 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/151128542):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span>, I think it's better to make "assorted changes" into separate PRs or at least separate commits.<br>
That makes it easier for the maintainers to commit parts as soon as they are happy with them, and not have to think about those parts again for every round of review of the other, more substantial changes</p>

#### [ Johan Commelin (Dec 16 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/151891968):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Do you think you have time somewhere this week to look at this PR? There's a couple of comments. Would it make sense to split of the discrete categories as a separate PR? (I think smaller chunks get merged faster...)</p>

#### [ Kenny Lau (Dec 17 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/151902875):
<p>is discrete category the free functor Set -&gt; Cat?</p>

#### [ Reid Barton (Dec 17 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/151907735):
<p>Yes, although we don't have Cat as a category yet.</p>

#### [ Scott Morrison (Dec 20 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23512%20discrete%20categories/near/152244018):
<p>I've updated this PR now. (Sorry it was a grab-bag PR. I'll avoid these in future.)</p>


{% endraw %}
