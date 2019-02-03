---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51786normnumbug.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [norm_num bug](https://leanprover-community.github.io/archive/113488general/51786normnumbug.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Calle Sönne (Nov 08 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num%20bug/near/147321656):
<p>Here is what I think is a bug in norm_num:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">norm_num</span>
<span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">real</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">((</span><span class="mi">8</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="mi">9</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span>
</pre></div>


<p>"tactic failed"</p>

#### [ Simon Hudon (Nov 09 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num%20bug/near/147389627):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> is norm_num supposed to handle coercions?</p>

#### [ Mario Carneiro (Nov 09 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num%20bug/near/147393172):
<p>no, or at least it has not been extended to coercions</p>

#### [ Simon Hudon (Nov 10 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num%20bug/near/147448343):
<p>That could be a nice feature</p>

#### [ Kevin Buzzard (Nov 10 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num%20bug/near/147448668):
<p>In the mean time, following the tips at <a href="https://github.com/leanprover/mathlib/blob/master/docs/extras/casts.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/extras/casts.md">https://github.com/leanprover/mathlib/blob/master/docs/extras/casts.md</a>, you can always do this:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">norm_num</span>
<span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">real</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">((</span><span class="mi">8</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="mi">9</span> <span class="o">:=</span> <span class="k">begin</span>
  <span class="n">rw</span> <span class="o">(</span><span class="k">show</span> <span class="o">((</span><span class="mi">8</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">8</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="k">by</span> <span class="n">simp</span><span class="o">),</span>
  <span class="n">norm_num</span>
<span class="kn">end</span>
</pre></div>

#### [ Nicholas Scheel (Nov 11 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num%20bug/near/147475448):
<p>I once made a stupid tactic to do exactly this: <a href="https://github.com/MonoidMusician/MATH361/blob/lean-3.4.1/src/naturally.lean" target="_blank" title="https://github.com/MonoidMusician/MATH361/blob/lean-3.4.1/src/naturally.lean">https://github.com/MonoidMusician/MATH361/blob/lean-3.4.1/src/naturally.lean</a></p>

#### [ Nicholas Scheel (Nov 11 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num%20bug/near/147475536):
<p>you can also do the same with <code>rat</code></p>


{% endraw %}
