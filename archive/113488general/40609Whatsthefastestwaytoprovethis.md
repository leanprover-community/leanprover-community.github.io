---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40609Whatsthefastestwaytoprovethis.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [What's the fastest way to prove this?](https://leanprover-community.github.io/archive/113488general/40609Whatsthefastestwaytoprovethis.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (May 27 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20the%20fastest%20way%20to%20prove%20this%3F/near/127145665):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">m</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">∨</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Nicholas Scheel (May 27 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20the%20fastest%20way%20to%20prove%20this%3F/near/127146413):
<p>I would do <code>by_cases m = 0</code> and <code>eq_of_mul_eq_mul_left</code></p>

#### [ Nicholas Scheel (May 27 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20the%20fastest%20way%20to%20prove%20this%3F/near/127146414):
<p>(after <code>mul_one</code>)</p>

#### [ Nicholas Scheel (May 27 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20the%20fastest%20way%20to%20prove%20this%3F/near/127146464):
<p>or maybe even <code>by_cases n = 1</code> and <code>eq_zero_of_mul_eq_self_right</code></p>

#### [ Nicholas Scheel (May 27 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20the%20fastest%20way%20to%20prove%20this%3F/near/127146473):
<p>(both of those long theorems are from integral domains <a href="https://github.com/leanprover/lean/blob/master/library/init/algebra/ring.lean#L290" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/algebra/ring.lean#L290">https://github.com/leanprover/lean/blob/master/library/init/algebra/ring.lean#L290</a> )</p>

#### [ Kenny Lau (May 27 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20the%20fastest%20way%20to%20prove%20this%3F/near/127146560):
<p>but they don't apply to natural numbers</p>

#### [ Nicholas Scheel (May 27 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20the%20fastest%20way%20to%20prove%20this%3F/near/127146567):
<p>oh whoops, you’re right ... rings and all</p>

#### [ Nicholas Scheel (May 27 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20the%20fastest%20way%20to%20prove%20this%3F/near/127146620):
<p><a href="https://github.com/leanprover/lean/blob/master/library/init/data/nat/lemmas.lean#L332" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/data/nat/lemmas.lean#L332">https://github.com/leanprover/lean/blob/master/library/init/data/nat/lemmas.lean#L332</a></p>

#### [ Kenny Lau (May 27 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20the%20fastest%20way%20to%20prove%20this%3F/near/127146625):
<p>thanks</p>


{% endraw %}
