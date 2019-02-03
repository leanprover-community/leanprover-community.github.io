---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/94306Isabelle.html
---

## Stream: [maths](index.html)
### Topic: [Isabelle](94306Isabelle.html)

---


{% raw %}
#### [ Sebastien Gouezel (Aug 27 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Isabelle/near/132841692):
<p>I just wanted to thank <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>  for this in Isabelle:</p>
<div class="codehilite"><pre><span></span>have &quot;81 * exp(8 * ln 2/21) / 4 ≤ 80/3&quot;
 by (approximation 8)
</pre></div>


<p>(where 80/3 is just some good upper approximation I chose for simplicity, accurate within 1%)</p>

#### [ Johannes Hölzl (Aug 27 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Isabelle/near/132847688):
<p>Thanks! How long did it take to figure out 8? And how long did you play around to find the expression which finally worked :-)</p>

#### [ Sebastien Gouezel (Aug 27 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Isabelle/near/132848332):
<p>To chose a good upper approximation, I computed the continued fraction expansion of <code>81 * exp(8 * ln 2/21) / 4</code> and truncated it to some terms. To figure out the 8, I tried first with 5 but it failed, then 6, then 7, then 8, and it succeeded. Simple enough :) For another numerical approximation in the same file, I had to go up to <code>approximation 17</code> (which I found by dichotomoy), but the proof is still almost instantaneous. That's a wonderful tool! (If I had to give a proof by hand, it would be super-tedious and certainly 100 lines long...)</p>


{% endraw %}
