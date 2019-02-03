---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51666Potentialvmbug.html
---

## Stream: [general](index.html)
### Topic: [Potential vm bug](51666Potentialvmbug.html)

---


{% raw %}
#### [ Keeley Hoek (Aug 11 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Potential%20vm%20bug/near/131950146):
<p>The following code typechecks:</p>
<div class="codehilite"><pre><span></span>meta def oopsie : list string → tactic (option string)
| [] := none                          -- I&#39;m being naughty on this line
| (a :: rest) := oopsie rest

#eval oopsie [&quot;a&quot;]
</pre></div>


<p>I don't understand why it should. If I inspect the output of the <code>#eval</code>, I see the output "failed". Have I found a bug in the VM?</p>

#### [ Edward Ayers (Aug 11 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Potential%20vm%20bug/near/131950892):
<p>There is a coercion from <code>option </code> to <code>tactic</code> in <code>tactic.lean</code>:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="kn">instance</span> <span class="n">opt_to_tac</span> <span class="o">:</span> <span class="n">has_coe</span> <span class="o">(</span><span class="n">option</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">tactic</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">returnopt</span><span class="bp">⟩</span>
</pre></div>

#### [ Edward Ayers (Aug 11 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Potential%20vm%20bug/near/131950909):
<p>So your tactic will throw if you give it an empty list</p>

#### [ Keeley Hoek (Aug 11 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Potential%20vm%20bug/near/131951022):
<p>Ah, cheers!</p>

#### [ Edward Ayers (Aug 11 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Potential%20vm%20bug/near/131951093):
<p>I only spotted this because I happen to be reading <code>tactic.lean</code> currently. Does anyone know if there is a way to discover what coercions are occurring in a given expression? Or a <code>#command</code> which will tell me coercions to a particular type?</p>

#### [ Edward Ayers (Aug 11 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Potential%20vm%20bug/near/131951679):
<p>I can't figure out how to use<br>
<code>set_option pp.coercions true</code></p>

#### [ Simon Hudon (Aug 11 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Potential%20vm%20bug/near/131960579):
<blockquote>
<p>I only spotted this because I happen to be reading tactic.lean currently.</p>
</blockquote>
<p>Good read! Don't spoil the ending though!</p>

#### [ Simon Hudon (Aug 11 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Potential%20vm%20bug/near/131960581):
<blockquote>
<p>Does anyone know if there is a way to discover what coercions are occurring in a given expression?</p>
</blockquote>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">print</span> <span class="n">instances</span> <span class="n">has_coe</span>
</pre></div>


{% endraw %}
