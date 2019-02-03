---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/42611574quotientkerequivrange.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#574 quotient_ker_equiv_range](https://leanprover-community.github.io/archive/144837PRreviews/42611574quotientkerequivrange.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Jan 05 2019 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154473405):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> Nice job. Should you also prove that the equiv is an iso?</p>

#### [ Chris Hughes (Jan 05 2019 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154474606):
<p>Yes, but I'm not sure of the best way to state it. We already have that fact, since <code>lift</code> is a group hom but not with the best statement.</p>

#### [ Chris Hughes (Jan 05 2019 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154474663):
<p>Should it just be an instance, or do we want bundled group isomorphisms. I guess we do want bundled group isomorphisms at some point.</p>

#### [ Johan Commelin (Jan 05 2019 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154474671):
<p>Right, and then define the category <code>Grp</code> while you are at it.</p>

#### [ Chris Hughes (Jan 05 2019 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154474777):
<p>Should group isomorphisms be represented exclusively in terms of category theory?</p>

#### [ Chris Hughes (Jan 05 2019 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154474788):
<p>We have <code>linear_equiv</code> which doesn't mention categories.</p>

#### [ Chris Hughes (Jan 05 2019 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154474789):
<p>I don't know anything about categories so I can't really comment.</p>

#### [ Johan Commelin (Jan 05 2019 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154474887):
<p>Hmm, I don't know if we should have a separate version.</p>

#### [ Johan Commelin (Jan 05 2019 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154474888):
<p>All I meant was that once you have bundled group homs, defining the category is also trivial. (Using the bundled category machinery.)</p>

#### [ Johan Commelin (Jan 05 2019 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154474899):
<p>What is a group iso for you? A group hom that is bijective, or an equiv where <code>to_fun</code> is a group hom?</p>

#### [ Johan Commelin (Jan 05 2019 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154474901):
<p>Category theory will give you the latter (and also require <code>to_inv</code> to be a group hom)</p>

#### [ Chris Hughes (Jan 05 2019 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23574%20quotient_ker_equiv_range/near/154475012):
<p>Definitely an equiv</p>


{% endraw %}
