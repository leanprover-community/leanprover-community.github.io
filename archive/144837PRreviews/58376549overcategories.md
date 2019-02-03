---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/58376549overcategories.html
---

## Stream: [PR reviews](index.html)
### Topic: [#549 over categories](58376549overcategories.html)

---


{% raw %}
#### [ Scott Morrison (Dec 21 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23549%20over%20categories/near/152321838):
<p>Hi <span class="user-mention" data-user-id="112680">@Johan Commelin</span>, is it a good idea to define over and under categories in terms of comma categories?</p>

#### [ Scott Morrison (Dec 21 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23549%20over%20categories/near/152321844):
<p>It is certainly less ergonomic that just defining them from scratch.</p>

#### [ Scott Morrison (Dec 21 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23549%20over%20categories/near/152321858):
<p>So the question is if things are actually defeq enough that you can use theorems about comma categories directly.</p>

#### [ Scott Morrison (Dec 21 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23549%20over%20categories/near/152321868):
<p>If they aren't, I'd suggest biting the bullet and making them separate, and explicitly showing at equivalence.</p>

#### [ Scott Morrison (Dec 21 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23549%20over%20categories/near/152321912):
<p>But I'm not sure, and can't tell just from looking at the PR.</p>

#### [ Johan Commelin (Dec 21 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23549%20over%20categories/near/152322555):
<p>Well, so far I haven't had much problems with using this definition. So I like it (-;</p>

#### [ Johan Commelin (Jan 03 2019 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23549%20over%20categories/near/154225310):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> You say that it is less ergonomic than defining from scratch. Otoh I think almost every line that I wrote would need an equivalent line in the "from scratch" definition (all the simp-lemmas). And lines such as</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">forget</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">T</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="n">over</span> <span class="n">X</span><span class="o">)</span> <span class="err">⥤</span> <span class="n">T</span> <span class="o">:=</span> <span class="n">comma</span><span class="bp">.</span><span class="n">fst</span> <span class="bp">_</span> <span class="bp">_</span>
</pre></div>


<p>can hardly be shorter when defining things from scratch. So far I haven't really felt like I was battling generality.</p>

#### [ Scott Morrison (Jan 03 2019 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23549%20over%20categories/near/154262094):
<p>Oh, I agree that it's exactly as much effort for this PR. The question is how it differs to users. In particular the "from scratch" approach means users might not need to worry about filling in 'unit.star' in a few places.</p>

#### [ Scott Morrison (Jan 03 2019 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23549%20over%20categories/near/154262108):
<p>But I'm not at all confident about this.</p>

#### [ Johan Commelin (Jan 05 2019 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23549%20over%20categories/near/154487442):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> What do you think?</p>


{% endraw %}
