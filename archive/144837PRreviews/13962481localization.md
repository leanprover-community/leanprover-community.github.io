---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/13962481localization.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#481 localization](https://leanprover-community.github.io/archive/144837PRreviews/13962481localization.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Dec 20 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152240956):
<p>I need a better interface</p>

#### [ Kenny Lau (Dec 20 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152240961):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> any suggestion?</p>

#### [ Johan Commelin (Dec 20 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152240973):
<p>Hmpf, can you explain what problems you are hitting?</p>

#### [ Kenny Lau (Dec 20 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152240987):
<p>I don't know</p>

#### [ Kenny Lau (Dec 20 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152240994):
<p>I'm just not sure whether I like <code>of_comm_ring</code> and <code>div</code></p>

#### [ Johan Commelin (Dec 20 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152241135):
<p>I think they are fine. I would change <code>of_comm_ring</code> into <code>mk</code>. But that's just a name.</p>

#### [ Kenny Lau (Dec 20 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152241166):
<p>then why not change <code>div</code> to <code>mk</code> instead</p>

#### [ Johan Commelin (Dec 20 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152241207):
<p>Maybe that would be technically correct.</p>

#### [ Chris Hughes (Dec 20 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152241468):
<p>Aren't things called <code>mk</code> usually supposed to be surjective?</p>

#### [ Johan Commelin (Dec 20 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152241568):
<p>Ok, so let's not call it <code>mk</code>. (I thought of <code>mk</code> as the canonical map from the object you start with.)</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152241731):
<p>I don't think they have to be surjective, for objects with some kind of completion in them</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152241735):
<p>like the injection into a free group</p>

#### [ Johan Commelin (Dec 20 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152241755):
<p>So what about the case at hand?</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152241767):
<p>although I guess that's called <code>of</code> right now?</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152241825):
<p>By analogy to <code>rat</code>, <code>div</code> -&gt; <code>mk</code> and <code>of_comm_ring</code> -&gt; <code>of</code>?</p>

#### [ Kenny Lau (Dec 21 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152318029):
<blockquote>
<p>Hmpf, can you explain what problems you are hitting?</p>
</blockquote>
<p>I feel like the lemmas I proved are very ad-hoc and unstructured</p>

#### [ Kenny Lau (Dec 21 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152327048):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span></p>

#### [ Johan Commelin (Dec 22 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23481%20localization/near/152375140):
<p>Hmm... it looks quite fine to me. At least <em>I</em> don't see a way to improve this. (Apart from the suggestion Mario made above.)</p>


{% endraw %}
