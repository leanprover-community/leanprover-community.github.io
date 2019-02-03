---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/44283Thiswillbrickyourcomputer.html
---

## Stream: [general](index.html)
### Topic: [This will brick your computer!](44283Thiswillbrickyourcomputer.html)

---


{% raw %}
#### [ Kenny Lau (Sep 14 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/133943778):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">int</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">set_option</span> <span class="n">trace</span><span class="bp">.</span><span class="n">class_instances</span> <span class="n">true</span>
<span class="bp">#</span><span class="kn">check</span> <span class="bp">λ</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">,</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Sep 14 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/133945380):
<p>This is well known. Lean will time out trying to coerce an int into a nat rather than give up</p>

#### [ Kenny Lau (Sep 14 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/133945390):
<p>remove the first line and it's fine!</p>

#### [ Kevin Buzzard (Sep 14 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/133945432):
<p>Hopefully fixed in Lean 4</p>

#### [ Kenny Lau (Sep 17 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134082892):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">polynomial</span>

<span class="kn">universe</span> <span class="n">u</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span>

<span class="n">def</span> <span class="n">derivative</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">finsupp</span><span class="bp">.</span><span class="n">sum</span> <span class="n">p</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">n</span> <span class="n">c</span><span class="o">,</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">C</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">X</span><span class="err">^</span><span class="o">(</span><span class="n">n</span><span class="bp">-</span><span class="mi">1</span><span class="o">)</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">derivative_C_mul_X</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">derivative</span> <span class="o">(</span><span class="n">polynomial</span><span class="bp">.</span><span class="n">C</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">X</span><span class="err">^</span><span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">C</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">X</span><span class="err">^</span><span class="o">(</span><span class="n">n</span><span class="bp">-</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">derivative</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">single_eq_C_mul_X</span><span class="o">,</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">sum_single_index</span><span class="o">],</span>
  <span class="n">all_goals</span> <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="n">polynomial</span><span class="bp">.</span><span class="n">C_0</span><span class="o">,</span> <span class="n">mul_zero</span><span class="o">,</span> <span class="n">zero_mul</span><span class="o">]</span> <span class="o">}</span>
<span class="kn">end</span>

<span class="c1">--timeout</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">derivative_C</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">derivative</span> <span class="o">(</span><span class="n">polynomial</span><span class="bp">.</span><span class="n">C</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="n">derivative_C_mul_X</span> <span class="n">x</span> <span class="mi">0</span>
</pre></div>

#### [ Mario Carneiro (Sep 17 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134082945):
<p>there are some nontrivial defeq simplifications there</p>

#### [ Mario Carneiro (Sep 17 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134082985):
<p>at least try <code>by simpa using derivative_C_mul_X x 0</code> first</p>

#### [ Kenny Lau (Sep 17 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134083001):
<p>it's intentionally incorrect</p>

#### [ Mario Carneiro (Sep 17 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134083004):
<p>then what's the surprise?</p>

#### [ Kenny Lau (Sep 17 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134083005):
<p>well Lean should tell me instead of time out</p>

#### [ Mario Carneiro (Sep 17 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134083008):
<p>you just asked it to reduce some big expression to 0</p>

#### [ Mario Carneiro (Sep 17 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134083048):
<p>it's got to unfold a bunch of definitions and run the power function, etc</p>

#### [ Mario Carneiro (Sep 17 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134083051):
<p>it's not obviously not defeq</p>

#### [ Kenny Lau (Sep 17 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134083053):
<p>I don't actually know if it's defeq</p>

#### [ Mario Carneiro (Sep 17 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134083056):
<p>neither does lean...</p>

#### [ Kenny Lau (Sep 17 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134083268):
<p>oh wow it's already done</p>

#### [ Kenny Lau (Sep 17 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134083271):
<p>i'm lucky i realized so soon</p>


{% endraw %}
