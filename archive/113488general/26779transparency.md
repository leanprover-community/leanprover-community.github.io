---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26779transparency.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [transparency](https://leanprover-community.github.io/archive/113488general/26779transparency.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Edward Ayers (Aug 21 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transparency/near/132514588):
<p>In <code>tactic.meta</code> there is a definition called <code>transparency</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">transparency</span>
<span class="bp">|</span> <span class="n">all</span> <span class="bp">|</span> <span class="n">semireducible</span> <span class="bp">|</span> <span class="n">instances</span> <span class="bp">|</span> <span class="kn">reducible</span> <span class="bp">|</span> <span class="n">none</span>
</pre></div>


<p>which seems to be a setting for how aggressively definitions are unfolded. In the reference manual I see that you can set <code>reducible</code>, <code>semireducible</code> and <code>irreducible</code> as attributes. My impression is that these attributes and settings are used when doing unification or matching. I can't find any documentation on what <em>exactly</em> these different transparency modes are changing about the unifier. Please could someone explain it to me or point me to some docs or C++ code that will help me understand what is going on here?</p>
<p>So an example might be that you want <code>ℝ</code> to be irreducible because you rarely prove things about reals in terms of equivalence classes of cauchy sequences.</p>

#### [ Edward Ayers (Oct 10 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transparency/near/135536162):
<p>bump</p>

#### [ Scott Morrison (Oct 10 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transparency/near/135537299):
<p>Sorry, probably such documentation doesn't exists. Gabriel and Sebastian are probably the people to hope can point you to right parts of the C++ code.</p>


{% endraw %}
