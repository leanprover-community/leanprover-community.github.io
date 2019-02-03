---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23433instances.html
---

## Stream: [general](index.html)
### Topic: [instances](23433instances.html)

---


{% raw %}
#### [ Jakob von Raumer (Oct 20 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instances/near/136163177):
<p>Can someone explain this?</p>
<div class="codehilite"><pre><span></span><span class="n">failed</span> <span class="n">to</span> <span class="n">synthesize</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">for</span>
<span class="n">TL</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="o">[</span><span class="bp">...</span><span class="o">]</span>
<span class="bp">_</span><span class="n">inst_9</span> <span class="o">:</span> <span class="n">is_contr</span> <span class="n">TL</span><span class="o">,</span>
<span class="o">[</span><span class="bp">...</span><span class="o">]</span>
<span class="err">⊢</span> <span class="n">is_contr</span> <span class="n">TL</span>
</pre></div>


<p>Even if I set <code>pp.all true</code>, it shows that TL is the right thing and there's no hidden difference...</p>

#### [ Kevin Buzzard (Oct 20 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instances/near/136164270):
<p>Did you try using <code>letI</code> to add the instance to the type class inference system? I appreciate that its name indicates that it should be in it already..</p>

#### [ Jakob von Raumer (Oct 20 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instances/near/136164360):
<p>The environment looks like this:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">hott</span><span class="o">]</span> <span class="n">def</span> <span class="n">pushout_of_embedding</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="err">₋₂</span><span class="o">}</span> <span class="o">[</span><span class="n">is_embedding</span> <span class="n">g</span><span class="o">]</span> <span class="o">:</span>
  <span class="bp">Π</span> <span class="o">[</span><span class="n">is_trunc</span> <span class="n">n</span> <span class="n">TL</span><span class="o">]</span> <span class="o">[</span><span class="n">is_trunc</span> <span class="n">n</span> <span class="n">TR</span><span class="o">]</span> <span class="o">[</span><span class="n">is_trunc</span> <span class="n">n</span> <span class="n">BL</span><span class="o">],</span>
  <span class="n">is_trunc</span> <span class="n">n</span> <span class="o">(</span><span class="n">pushout</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span> <span class="n">IH</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intros</span><span class="o">,</span> <span class="n">apply</span> <span class="n">base_case</span><span class="o">,</span>  <span class="o">}</span>
<span class="kn">end</span>
</pre></div>


<p>So it's mentioned after the <code>:</code>, maybe that's what prevents it from being a local instance?</p>

#### [ Kevin Buzzard (Oct 20 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instances/near/136164637):
<p>Yes that's exactly it.</p>

#### [ Kevin Buzzard (Oct 20 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instances/near/136164639):
<p>You need to explicitly add it to the instance list with <code>letI</code></p>

#### [ Jakob von Raumer (Oct 20 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instances/near/136164640):
<p>Okay, thanks <span class="emoji emoji-1f44d" title="+1">:+1:</span></p>

#### [ Kevin Buzzard (Oct 20 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instances/near/136164675):
<p>Leo changed this behaviour a few months ago. Nothing right of the colon goes in any more</p>

#### [ Kenny Lau (Oct 20 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instances/near/136167263):
<p>you should use <code>resetI</code> there instead of <code>letI</code></p>


{% endraw %}
