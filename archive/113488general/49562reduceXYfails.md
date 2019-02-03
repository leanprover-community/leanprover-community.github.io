---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49562reduceXYfails.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [#reduce "X"++"Y" fails](https://leanprover-community.github.io/archive/113488general/49562reduceXYfails.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Sullivan (Sep 03 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20%22X%22%2B%2B%22Y%22%20fails/near/133264218):
<p>Evaluating this expression in Lean (VSCode is what I'm using) hangs for a while then reports deep recursion detected, increase stack space. Not very undergraduate-student-friendly. Bug or feature?</p>

#### [ Patrick Massot (Sep 03 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20%22X%22%2B%2B%22Y%22%20fails/near/133264296):
<p>As usual, <code>#eval</code> succeeds here</p>

#### [ Kevin Sullivan (Sep 03 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20%22X%22%2B%2B%22Y%22%20fails/near/133264323):
<p>Why this failure?</p>

#### [ Kevin Sullivan (Sep 03 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20%22X%22%2B%2B%22Y%22%20fails/near/133265394):
<p>Also note that #eval also fails in ways guaranteed to be confusing to new students. Try this (posted previously).</p>
<p>theorem t : true := true.intro<br>
#check t<br>
#eval t</p>
<p>The real question then, I suppose, is by what simple rule should a new student choose between #eval and #reduce?</p>
<p>And for the curious student, why do they fail in cases where on the face of it, it looks like they might be expected to work?</p>

#### [ Rob Lewis (Sep 03 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20%22X%22%2B%2B%22Y%22%20fails/near/133265406):
<p>Even just <code>#reduce 'X'</code> is asking the kernel to normalize a proof of <code>88 &lt; 55296</code>. This normalizes to 55207 nested applications of <code>nat.less_than_or_equal.step</code>. And this is a subproblem of what you're asking.</p>

#### [ Rob Lewis (Sep 03 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20%22X%22%2B%2B%22Y%22%20fails/near/133265477):
<p><code>#eval</code> is useful for computing values, it will ignore <code>Prop</code>-valued terms.</p>

#### [ Patrick Massot (Sep 03 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20%22X%22%2B%2B%22Y%22%20fails/near/133266004):
<p>My simple rule is to choose <code>#eval</code></p>

#### [ Kevin Sullivan (Sep 03 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20%22X%22%2B%2B%22Y%22%20fails/near/133266225):
<p>Thanks.</p>


{% endraw %}
