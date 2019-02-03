---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/24388toPropinj.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [to_Prop_inj](https://leanprover-community.github.io/archive/113489newmembers/24388toPropinj.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Jan 11 2019 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/to_Prop_inj/near/154908038):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">to_Prop_inj</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">bool</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="bp">↔</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)),</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span>
<span class="bp">|</span> <span class="n">a</span> <span class="n">tt</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">H</span><span class="bp">.</span><span class="mi">2</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="n">a</span> <span class="n">ff</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">bool</span><span class="bp">.</span><span class="n">eq_ff_of_ne_tt</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">absurd</span> <span class="o">(</span><span class="n">H</span><span class="bp">.</span><span class="mi">1</span> <span class="n">h</span><span class="o">)</span> <span class="n">dec_trivial</span>
</pre></div>

#### [ Kenny Lau (Jan 11 2019 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/to_Prop_inj/near/154908043):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> is this currently in mathlib?</p>


{% endraw %}
