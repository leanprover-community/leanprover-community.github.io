---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/07374refinecantgowith.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: ["refine" can't go with λ ⟨_, _⟩, _](https://leanprover-community.github.io/archive/113488general/07374refinecantgowith.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Sep 15 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22refine%22%20can%27t%20go%20with%20%CE%BB%20%E2%9F%A8_%2C%20_%E2%9F%A9%2C%20_/near/134001592):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="bp">@</span><span class="n">subtype</span> <span class="bp">ℕ</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">true</span><span class="o">),</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">refine</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">hn</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">_</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Sep 15 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22refine%22%20can%27t%20go%20with%20%CE%BB%20%E2%9F%A8_%2C%20_%E2%9F%A9%2C%20_/near/134001614):
<div class="codehilite"><pre><span></span>don&#39;t know how to synthesize placeholder
context:
_x : {_x // true},
_fun_match : {_x // true} → 0 = 0,
n : ℕ,
hn : true
⊢ 0 = 0
state:
⊢ {_x // true} → 0 = 0
</pre></div>

#### [ Mario Carneiro (Sep 15 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22refine%22%20can%27t%20go%20with%20%CE%BB%20%E2%9F%A8_%2C%20_%E2%9F%A9%2C%20_/near/134001717):
<p>no, it can't</p>

#### [ Mario Carneiro (Sep 15 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22refine%22%20can%27t%20go%20with%20%CE%BB%20%E2%9F%A8_%2C%20_%E2%9F%A9%2C%20_/near/134001720):
<p>obvious workarounds include using <code>rintro</code> instead</p>

#### [ Mario Carneiro (Sep 15 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22refine%22%20can%27t%20go%20with%20%CE%BB%20%E2%9F%A8_%2C%20_%E2%9F%A9%2C%20_/near/134001759):
<p>Neither will using <code>match</code> or anything else that triggers the equation compiler</p>


{% endraw %}
