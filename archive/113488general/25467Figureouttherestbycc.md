---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/25467Figureouttherestbycc.html
---

## Stream: [general](index.html)
### Topic: [Figure out the rest by cc](25467Figureouttherestbycc.html)

---


{% raw %}
#### [ Johan Commelin (Aug 02 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130779658):
<p>Can I tell Lean to work out the rest <code>by cc</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">module</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span>

<span class="kn">open</span> <span class="n">punit</span>

<span class="n">def</span> <span class="n">zero_module</span> <span class="o">:</span> <span class="n">module</span> <span class="n">R</span> <span class="n">punit</span> <span class="o">:=</span>
  <span class="o">{</span> <span class="n">smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">star</span><span class="o">,</span>
    <span class="n">zero</span> <span class="o">:=</span> <span class="n">star</span><span class="o">,</span>
    <span class="n">add</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">star</span><span class="o">,</span>
    <span class="n">neg</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">star</span><span class="o">,</span>
    <span class="n">add_zero</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">cc</span><span class="o">,</span>
    <span class="n">zero_add</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">cc</span><span class="o">,</span>
    <span class="n">add_comm</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">cc</span><span class="o">,</span>
    <span class="n">add_left_neg</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">cc</span><span class="o">,</span>
    <span class="n">one_smul</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">cc</span><span class="o">,</span>
    <span class="n">mul_smul</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">cc</span><span class="o">,</span>
    <span class="n">add_smul</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">cc</span><span class="o">,</span>
    <span class="n">smul_add</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">cc</span><span class="o">,</span>
    <span class="n">add_assoc</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">cc</span> <span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Aug 02 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130779703):
<p>I found that I was repeating myself, while trying to make a point to Lean.</p>

#### [ Scott Morrison (Aug 02 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130779783):
<p>sure, something like: </p>
<div class="codehilite"><pre><span></span>begin
  refine
  { smul := λ _ _, star,
    zero := star,
    add  := λ _ _, star,
    neg  := λ _, star,
    .. } ; cc
end
</pre></div>

#### [ Johan Commelin (Aug 02 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130779915):
<p>Aaah, I need to understand <code>refine</code>.</p>

#### [ Scott Morrison (Aug 02 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780063):
<p>Curiously that doesn't actually work...</p>

#### [ Scott Morrison (Aug 02 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780069):
<p>Of course, replacing <code>cc</code> with <code>obviously</code> does it. :-)</p>

#### [ Scott Morrison (Aug 02 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780103):
<p>In fact just <code>by obviously</code> should work, except for some reason <code>split</code> doesn't work on modules, for some reason I can't see at the moment (type class inference throws an error?)</p>

#### [ Johan Commelin (Aug 02 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780108):
<p><code>finish</code> works instead of <code>cc</code>.</p>

#### [ Kenny Lau (Aug 02 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780164):
<p>what is <code>obviously</code>? is it in mathlib?</p>

#### [ Johan Commelin (Aug 02 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780199):
<p>No, it is Scott's Hammer.</p>

#### [ Johan Commelin (Aug 02 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780206):
<p>Well, maybe <code>tidy</code> is his hammer.</p>

#### [ Sean Leather (Aug 02 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780270):
<p><a href="https://github.com/semorrison/lean-tidy/blob/master/src/tidy/tidy.lean#L81" target="_blank" title="https://github.com/semorrison/lean-tidy/blob/master/src/tidy/tidy.lean#L81"><code>obviously</code></a></p>

#### [ Johan Commelin (Aug 02 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780292):
<p>So, the current golf record is:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">zero_module&#39;</span> <span class="o">:</span> <span class="n">module</span> <span class="n">R</span> <span class="n">punit</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">refine</span>
<span class="o">{</span> <span class="n">add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">punit</span><span class="bp">.</span><span class="n">star</span><span class="o">,</span>
  <span class="n">zero</span> <span class="o">:=</span> <span class="n">punit</span><span class="bp">.</span><span class="n">star</span><span class="o">,</span>
  <span class="n">neg</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">punit</span><span class="bp">.</span><span class="n">star</span><span class="o">,</span>
  <span class="n">smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">c</span> <span class="n">x</span><span class="o">,</span> <span class="n">punit</span><span class="bp">.</span><span class="n">star</span><span class="o">,</span>
  <span class="bp">..</span> <span class="o">}</span><span class="bp">;</span> <span class="n">finish</span>
</pre></div>

#### [ Kenny Lau (Aug 02 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780309):
<p>gadvardammt finish</p>

#### [ Johan Commelin (Aug 02 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780310):
<p>Let's assume we open <code>punit</code>.</p>

#### [ Scott Morrison (Aug 02 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780403):
<p>If someone can explain to me why you can't <code>split</code> when the goal is a module, maybe I can golf the entire proof to <code>by tidy</code>.</p>

#### [ Kenny Lau (Aug 02 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780415):
<p>isn't the right command <code>constructor</code></p>

#### [ Kenny Lau (Aug 02 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780432):
<p><code>split</code> is for inductive types I think</p>

#### [ Johan Commelin (Aug 02 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Figure%20out%20the%20rest%20by%20cc/near/130780438):
<p><code>constructor</code> also fails...</p>


{% endraw %}
