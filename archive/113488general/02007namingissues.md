---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02007namingissues.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [naming issues](https://leanprover-community.github.io/archive/113488general/02007namingissues.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (May 02 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125982093):
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">check</span> <span class="n">sub_pos_of_lt</span>
<span class="c1">-- sub_pos_of_lt : ?M_4 &lt; ?M_3 → 0 &lt; ?M_3 - ?M_4</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">sub_neg_of_lt</span>
<span class="c1">-- sub_neg_of_lt : ?M_3 &lt; ?M_4 → ?M_3 - ?M_4 &lt; 0</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">sub_nonpos_of_le</span>
<span class="c1">-- sub_nonpos_of_le : ?M_3 ≤ ?M_4 → ?M_3 - ?M_4 ≤ 0</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">sub_nonneg_of_le</span>
<span class="c1">-- sub_nonneg_of_le : ?M_4 ≤ ?M_3 → 0 ≤ ?M_3 - ?M_4</span>
</pre></div>

#### [ Kenny Lau (May 02 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125982096):
<p>but I know the answer already: this is in core so we can't do nothing about it</p>

#### [ Mario Carneiro (May 02 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125984462):
<p>what's the issue?</p>

#### [ Kenny Lau (May 02 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125985953):
<blockquote>
<p>what's the issue?</p>
</blockquote>
<p>shouldn't one be <code>lt</code> and the other be <code>gt</code>?</p>

#### [ Mario Carneiro (May 02 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125986033):
<p>no? there is no usage of <code>gt</code> in those lemmas</p>

#### [ Kenny Lau (May 02 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125986036):
<p>I mean, how can both be lt</p>

#### [ Kenny Lau (May 02 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125986038):
<p>so does lt imply sub_pos or sub_neg?</p>

#### [ Mario Carneiro (May 02 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125986043):
<p>both...</p>

#### [ Mario Carneiro (May 02 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125986084):
<p>it's just a matter of where the variables go</p>

#### [ Mario Carneiro (May 02 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125986096):
<p>in mathlib the analogous theorem is just called <code>sub_pos</code></p>

#### [ Kenny Lau (May 02 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125986101):
<p>aha</p>

#### [ Johan Commelin (May 02 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125986144):
<p>Lol, we need Lean to generate the names for us, given the type. Then we can have <em>provably correct names</em></p>

#### [ Mario Carneiro (May 02 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125986147):
<p>although the usage of <code>pos</code> and <code>neg</code> as names for &gt;0 and &lt;0 is problematic since it overlaps <code>neg</code> meaning <code>-x</code></p>

#### [ Simon Hudon (May 02 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125991698):
<p>maybe <code>-x</code> should be called <code>minus</code> instead of <code>neg</code>?</p>


{% endraw %}
