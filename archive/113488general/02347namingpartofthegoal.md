---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02347namingpartofthegoal.html
---

## Stream: [general](index.html)
### Topic: [naming part of the goal](02347namingpartofthegoal.html)

---


{% raw %}
#### [ Reid Barton (Jan 01 2019 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20part%20of%20the%20goal/near/154143914):
<p>I discovered a trick for referring to parts of the goal without having to write them out. For example, suppose your goal is to prove that some really complicated expression equals 0. You can give that expression a name <code>lhs</code> by writing</p>
<div class="codehilite"><pre><span></span>  <span class="k">let</span> <span class="n">lhs</span> <span class="o">:=</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">change</span> <span class="n">lhs</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">,</span>
</pre></div>

#### [ Patrick Massot (Jan 01 2019 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20part%20of%20the%20goal/near/154143960):
<p>Oh, that's sneaky</p>

#### [ Patrick Massot (Jan 01 2019 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20part%20of%20the%20goal/near/154143970):
<p>It could be nice to wrap this trick in a small tactic</p>

#### [ Sebastian Ullrich (Jan 01 2019 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20part%20of%20the%20goal/near/154144846):
<p>omg</p>

#### [ Patrick Massot (Jan 01 2019 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20part%20of%20the%20goal/near/154145021):
<p>I can feel this trick won't be allowed in Lean 4...</p>

#### [ Kevin Buzzard (Jan 01 2019 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20part%20of%20the%20goal/near/154146061):
<p>(deleted)</p>

#### [ Sebastian Ullrich (Jan 02 2019 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20part%20of%20the%20goal/near/154146598):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> I don't see anything wrong with any specific part here, it's more like a surprising combination of features</p>

#### [ Mario Carneiro (Jan 02 2019 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20part%20of%20the%20goal/near/154159623):
<p>you can also use <code>let lhs, swap,</code> which is what I usually use for this trick</p>

#### [ Mario Carneiro (Jan 02 2019 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20part%20of%20the%20goal/near/154159626):
<p>since there is no <code>let_suffices</code> tactic</p>

#### [ Mario Carneiro (Jan 02 2019 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20part%20of%20the%20goal/near/154159654):
<p>I think having a tactic for this wouldn't be a bad idea though. Possibly using conv patterns to find the expression to name</p>

#### [ Mario Carneiro (Jan 02 2019 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20part%20of%20the%20goal/near/154159836):
<p>How about this: <code>name foo + 1 + bar</code> will treat any undefined names in the expression like <code>foo</code> and <code>bar</code> as holes to be filled. It searches for the first unifying subterm of the goal (or hyps) and let binds them and replaces them in the target (not just in the pattern, in the whole goal). So if the goal is <code>(x - 3) + 1 + (y - 3) = x - 3</code> then the resulting goal is <code>foo := x - 3, bar := y - 3 |- foo + 1 + bar = foo</code></p>

#### [ Mario Carneiro (Jan 02 2019 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20part%20of%20the%20goal/near/154159916):
<p>It doesn't work in the presence of binders; or more specifically it won't match any open terms. I don't see what other option is available</p>

#### [ Mario Carneiro (Jan 02 2019 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20part%20of%20the%20goal/near/154159984):
<p>so if the goal was <code>\exists y, (x - 3) + 1 + y = x - 3</code> then the inner match <code>(x - 3) + 1 + #0</code> would be ignored</p>

#### [ Johan Commelin (Jan 02 2019 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20part%20of%20the%20goal/near/154163289):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> That's brilliant!</p>


{% endraw %}
