---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/73085507functorialityofcocones.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#507 functoriality of (co)cones](https://leanprover-community.github.io/archive/144837PRreviews/73085507functorialityofcocones.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Dec 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23507%20functoriality%20of%20%28co%29cones/near/150766258):
<p>I just created PR <a href="https://github.com/leanprover/mathlib/issues/507" target="_blank" title="https://github.com/leanprover/mathlib/issues/507">#507</a>. This is something that I wanted to have for my work with presheaves. I don't know if I should expand things. Maybe it's better to keep things small. Feedback appreciated!</p>

#### [ Reid Barton (Dec 07 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23507%20functoriality%20of%20%28co%29cones/near/151128674):
<p>I really like these statements <code>lim_yoneda</code> and <code>colim_coyoneda</code> because they say at once everything there is to know about <code>lim</code> and <code>colim</code>. Of course we will still need to relate them to <code>limit</code> and <code>colimit</code>, for those cases in which one is not so fortunate to have all limits or colimits...</p>

#### [ Reid Barton (Dec 07 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23507%20functoriality%20of%20%28co%29cones/near/151128797):
<p>The "functoriality" stuff added here is really pointing out the asymmetry between <code>cones</code> and <code>cocones</code>. Can we make them more uniform?</p>

#### [ Reid Barton (Dec 07 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23507%20functoriality%20of%20%28co%29cones/near/151128907):
<p>I also wonder whether we should just define <code>cones</code> and <code>cocones</code> as functors in the first place</p>


{% endraw %}
