---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/53658namingofbinarypropertieswithleftandright.html
---

## Stream: [maths](index.html)
### Topic: [naming of binary properties with left and right](53658namingofbinarypropertieswithleftandright.html)

---


{% raw %}
#### [ Sean Leather (Apr 26 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/naming%20of%20binary%20properties%20with%20left%20and%20right/near/125715828):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> updated his <code>finset.disjoint</code> PR with a <a href="https://github.com/leanprover/mathlib/commit/009ff9b" target="_blank" title="https://github.com/leanprover/mathlib/commit/009ff9b">change</a> to rename the following:</p>
<ul>
<li><code>empty_disjoint</code> → <code>disjoint_empty_left</code></li>
<li><code>disjoint_empty</code> → <code>disjoint_empty_right</code></li>
</ul>
<p>Personally, I prefer the new names: they are more descriptive and don't rely on positional naming, which can be confusing. But I wanted to open up a discussion on this in general to determine the mathlib style guidelines. I don't think these types of things have been consistently named.</p>

#### [ Sean Leather (Apr 26 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/naming%20of%20binary%20properties%20with%20left%20and%20right/near/125715961):
<p>We probably want feedback from <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> and <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> in particular.</p>

#### [ Chris Hughes (Apr 26 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/naming%20of%20binary%20properties%20with%20left%20and%20right/near/125730500):
<p>There's also the question of which one's <code>right</code> and which one's <code>left</code>. I would have named <code>dvd_mul_right : a ∣ a * b</code> <code>dvd_mul_left</code></p>

#### [ Kenny Lau (Apr 26 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/naming%20of%20binary%20properties%20with%20left%20and%20right/near/125732771):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> confer or.inl and or.inr</p>

#### [ Sean Leather (Apr 30 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/naming%20of%20binary%20properties%20with%20left%20and%20right/near/125881780):
<p>I created a <a href="https://github.com/leanprover/mathlib/issues/129" target="_blank" title="https://github.com/leanprover/mathlib/issues/129">GitHub issue</a> for this discussion. Please leave any thoughts there.</p>


{% endraw %}
