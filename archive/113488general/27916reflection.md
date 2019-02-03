---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27916reflection.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [reflection](https://leanprover-community.github.io/archive/113488general/27916reflection.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sarah Mameche (Sep 25 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflection/near/134585528):
<p>Hi, <br>
I'm trying to map meta expressions to an inductive type in the object language (with pattern matching on expr as described in <a href="https://leanprover.github.io/papers/tactic.pdf" target="_blank" title="https://leanprover.github.io/papers/tactic.pdf">https://leanprover.github.io/papers/tactic.pdf</a>). <br>
There's a constructor taking a natural number as argument (var : ℕ → term). How can the number be extracted from an expression with this constructor?<br>
Also, how does this work if I go from the inductive type back to exprs?</p>

#### [ Rob Lewis (Sep 25 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflection/near/134586345):
<p>I'm not sure if I understand exactly what you're after. You want a function <code>expr → ℕ</code> that will return the index if the input is made with <code>expr.var</code>?</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">var_index</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">var</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">n</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="mi">0</span>
</pre></div>


<p>You can do the same in the other direction, if the nat appears in a constructor of your inductive type. Match on your type, get the nat argument, and feed it back into <code>expr.var</code>.</p>

#### [ Rob Lewis (Sep 25 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflection/near/134586346):
<p>Or did you mean something else?</p>

#### [ Sarah Mameche (Sep 25 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflection/near/134592201):
<p>No, that helped, thanks!</p>


{% endraw %}
