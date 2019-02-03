---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85011constructingproofsbyhand.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [constructing proofs by hand](https://leanprover-community.github.io/archive/113488general/85011constructingproofsbyhand.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Apr 10 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867540):
<p>If I have <code>X Y Z : expr</code>, and a <code>P : expr</code> representing a proof that <code>X = Y</code>, how do I make the expression that says <code>(X = Z) = (Y = Z)</code>?</p>

#### [ Scott Morrison (Apr 10 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867582):
<p>(deleted)</p>

#### [ Simon Hudon (Apr 10 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867698):
<p><code>to_expr ``(congr_arg (λ x, x = %%Z) %%P)</code></p>

#### [ Scott Morrison (Apr 10 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867800):
<p>woah, okay, that's much better than what I was doing.</p>

#### [ Scott Morrison (Apr 10 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867805):
<p>I was trying things along the lines of </p>
<div class="codehilite"><pre><span></span>eq ← mk_const `eq,
prf&#39; ← mk_congr_arg eq prf,
prf&#39; ← mk_congr_fun prf&#39; rhs,
 ````
</pre></div>

#### [ Scott Morrison (Apr 10 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867808):
<p>but quotations are much nicer</p>

#### [ Kenny Lau (Apr 10 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867815):
<p>so people are making programs that program</p>

#### [ Scott Morrison (Apr 10 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867818):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span>, this has been happening since the dawn of time :-)</p>

#### [ Mario Carneiro (Apr 10 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124867819):
<p>you might even call them... <em>metaprograms</em></p>

#### [ Simon Hudon (Apr 10 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124868318):
<p>I guess now is a good time to bring up the Curry-Howard-Lambek correspondence and point out that, similarly, you can use a logical system to show that another logic is sound or complete. You can also use category theory to study the category of categories</p>

#### [ Sean Leather (Apr 10 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872852):
<p>Whoa, slow down there, <span class="user-mention" data-user-id="110026">@Simon Hudon</span>. Next thing you know, we'll be using English to describe... English. (Or choose your preferred self-describing language of choice.)</p>

#### [ Kenny Lau (Apr 10 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872856):
<p>isn't that what dictionaries do?</p>

#### [ Sean Leather (Apr 10 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872858):
<p>Also, hi, everyone. <span class="emoji emoji-1f44b" title="wave">:wave:</span> I've been away for a while.</p>

#### [ Sean Leather (Apr 10 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872864):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> OMG! You mean it's already happening?!</p>

#### [ Sean Leather (Apr 10 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872866):
<p>The end of the world is nigh!</p>

#### [ Simon Hudon (Apr 10 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872868):
<p>Hi Sean! We missed you! I hope you still managed to get your daily recommended dose of math and nerdiness ;-)</p>

#### [ Sean Leather (Apr 10 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872909):
<p>I tried here and there, but nothing came close to this. <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Kenny Lau (Apr 10 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872918):
<p>i'm high rn</p>

#### [ Kenny Lau (Apr 10 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20proofs%20by%20hand/near/124872919):
<p>high on homological algebra / wedderburn's theorem</p>


{% endraw %}
