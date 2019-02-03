---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98055lambdatemptation.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [lambda temptation](https://leanprover-community.github.io/archive/113488general/98055lambdatemptation.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Apr 24 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lambda%20temptation/near/125641452):
<p>Do I get kicked out of this forum by CS people if I use</p>
<div class="codehilite"><pre><span></span><span class="kn">notation</span> <span class="bp">`</span> <span class="bp">`</span> <span class="n">binders</span> <span class="bp">`</span><span class="err">↦</span><span class="bp">`</span> <span class="n">F</span><span class="o">:(</span><span class="n">scoped</span> <span class="n">f</span><span class="o">,</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span> <span class="n">F</span>
<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="err">↦</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">y</span> <span class="bp">+</span> <span class="mi">1</span>
</pre></div>

#### [ Patrick Massot (Apr 24 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lambda%20temptation/near/125641513):
<p>I learned to much about notations on Saturday</p>

#### [ Patrick Massot (Apr 24 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lambda%20temptation/near/125641523):
<p>With great power comes great responsibility</p>

#### [ Reid Barton (Apr 25 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lambda%20temptation/near/125642990):
<p>I like it. Makes things a little friendlier for mathematicians who aren't used to <code>λx y,</code></p>

#### [ Simon Hudon (Apr 25 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lambda%20temptation/near/125646078):
<p>Actually, the CS people had a meeting and your past violations are already sufficient to get you booted out</p>

#### [ Simon Hudon (Apr 25 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lambda%20temptation/near/125646299):
<p>But seriously, I understand it's tempting because it's a more traditional notation but I think it's worth re-examining conventions every now and then. In mathematics, the same idea (bound variables) seems to be reinvented over and over and over. If you look at notations like indexed unions, <code>argmax</code> and sums, there are a lot of vary different conventions in application. I think it's worth streamlining those notations and writing conceptually similar things with similar notations.</p>

#### [ Mario Carneiro (Apr 25 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lambda%20temptation/near/125647689):
<p>I'm not sure I'm ready to give up <code>↦</code> as an available notation, arrows are hard to come by</p>

#### [ Scott Morrison (Apr 25 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lambda%20temptation/near/125649077):
<p>I actually agree with Simon, that it's not a bad thing to ask mathematicians to get used to using lambdas. Conversely, I would be upset by Mario using <code>↦ </code> for something other than "maps to"! :-)</p>

#### [ Mario Carneiro (Apr 25 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lambda%20temptation/near/125649299):
<p>It's conceivable that something that is morally "maps to" but isn't literally lambda could come up, like ZFC maps to producing a Set</p>

#### [ Patrick Massot (Apr 25 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lambda%20temptation/near/125659462):
<p>Actually I think the unicode thin space at the beginning of the notation is worse than the Church sacrilege. But I don't know another way. Maybe I don't know enough about notations in the end.</p>


{% endraw %}
