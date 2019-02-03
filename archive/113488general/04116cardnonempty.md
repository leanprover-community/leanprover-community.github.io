---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04116cardnonempty.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [card_nonempty](https://leanprover-community.github.io/archive/113488general/04116cardnonempty.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Sep 08 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/card_nonempty/near/133577651):
<p>Is there some easy way to tackle this goal:</p>
<div class="codehilite"><pre><span></span><span class="n">n</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">n</span><span class="o">,</span>
<span class="n">h</span> <span class="o">:</span> <span class="n">nonempty</span> <span class="n">n</span>
<span class="err">⊢</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="n">n</span>
</pre></div>

#### [ Kenny Lau (Sep 08 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/card_nonempty/near/133577761):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fintype</span>

<span class="kn">universe</span> <span class="n">u</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">n</span><span class="o">]</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">nonempty</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">by_contra</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">not_lt</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">le_zero_iff</span><span class="o">,</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card_eq_zero_iff</span><span class="o">]</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">h</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">H</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Sep 08 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/card_nonempty/near/133577817):
<p>I guess this could be a simp lemma in mathlib?</p>

#### [ Johan Commelin (Sep 08 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/card_nonempty/near/133577822):
<p>Ooh, and thanks!</p>

#### [ Kenny Lau (Sep 08 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/card_nonempty/near/133577926):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">set_theory</span><span class="bp">.</span><span class="n">cardinal</span>

<span class="kn">universe</span> <span class="n">u</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">nonempty</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">cardinal</span><span class="bp">.</span><span class="n">mk</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rwa</span> <span class="o">[</span><span class="n">cardinal</span><span class="bp">.</span><span class="n">pos_iff_ne_zero</span><span class="o">,</span> <span class="n">cardinal</span><span class="bp">.</span><span class="n">ne_zero_iff_nonempty</span><span class="o">]</span>
</pre></div>

#### [ Kenny Lau (Sep 08 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/card_nonempty/near/133577929):
<p>I think Mario likes <a href="http://cardinal.mk" target="_blank" title="http://cardinal.mk">cardinal.mk</a> more than fintype.card</p>

#### [ Chris Hughes (Sep 08 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/card_nonempty/near/133578072):
<p>It is in mathlib. <code>fintype.card_pos_iff</code> I believe.</p>

#### [ Johan Commelin (Sep 08 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/card_nonempty/near/133578180):
<p>Aaah, thanks! (Sorry, Kenny)</p>


{% endraw %}
