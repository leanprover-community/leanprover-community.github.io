---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/45420metamutualdeferrors.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [meta mutual def errors](https://leanprover-community.github.io/archive/113488general/45420metamutualdeferrors.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mario Carneiro (Aug 24 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20mutual%20def%20errors/near/132697613):
<p>Does anyone know the source of this error? I get <code>unexpected error, failed to generate equational lemmas in the front-end</code> even though it's a meta def so it shouldn't have equations</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">mutual</span> <span class="n">def</span> <span class="n">A</span><span class="o">,</span> <span class="n">B</span>
<span class="k">with</span> <span class="n">A</span> <span class="o">:</span> <span class="n">unit</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">return</span> <span class="o">()</span>
<span class="k">with</span> <span class="n">B</span> <span class="o">:</span> <span class="n">unit</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">return</span> <span class="o">()</span>
</pre></div>

#### [ Scott Morrison (Aug 24 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20mutual%20def%20errors/near/132697723):
<p>(Mario and I are sitting next to each other and just discovered the curious answer. I'll explain while he does something useful. :-)</p>

#### [ Scott Morrison (Aug 24 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20mutual%20def%20errors/near/132697746):
<p>This doesn't work:</p>
<div class="codehilite"><pre><span></span>meta mutual def A, B
with A : ℕ → ℕ
| n := 0
with B : ℕ → ℕ
| n := 0
</pre></div>

#### [ Scott Morrison (Aug 24 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20mutual%20def%20errors/near/132697747):
<p>with the same error.</p>

#### [ Scott Morrison (Aug 24 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20mutual%20def%20errors/near/132697787):
<p>However</p>
<div class="codehilite"><pre><span></span>meta mutual def A, B
with A : ℕ → ℕ
| 0 := 0
| (n+1) := B 0
with B : ℕ → ℕ
| n := 0
</pre></div>

#### [ Scott Morrison (Aug 24 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20mutual%20def%20errors/near/132697792):
<p>or even </p>
<div class="codehilite"><pre><span></span>meta mutual def A, B
with A : ℕ → ℕ
| 0 := 0
| (n+1) := A 0
with B : ℕ → ℕ
| n := 0
</pre></div>

#### [ Scott Morrison (Aug 24 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20mutual%20def%20errors/near/132697840):
<p>Somehow the compiler is insisting that the definitions actually refer to either themselves or each other.</p>

#### [ Scott Morrison (Aug 24 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20mutual%20def%20errors/near/132697844):
<p>And this only happens in <code>meta</code>.</p>

#### [ Scott Morrison (Aug 24 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meta%20mutual%20def%20errors/near/132697846):
<p>Oh well! :-)</p>


{% endraw %}
