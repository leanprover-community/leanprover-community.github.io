---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/60452reflvrfl.html
---

## Stream: [general](index.html)
### Topic: [refl v rfl](60452reflvrfl.html)

---


{% raw %}
#### [ Kevin Buzzard (Nov 26 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refl%20v%20rfl/near/148383637):
<p>I've always had it in the back of my mind that <code>refl</code> was slightly more general than <code>rfl</code>, because the tactic works with anything tagged <code>@[refl]</code>. But I've been trying to write a blog post about equality and I ran into this -- <code>rfl</code> working but <code>refl</code> not working.</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">set_of</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">3</span><span class="o">)</span> <span class="mi">3</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">set_of</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">3</span><span class="o">)</span> <span class="mi">3</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refl</span> <span class="c1">-- fails</span>
</pre></div>


<p>What's happening there? For some reason <code>refl</code> is deciding not to unfold <code>set_of</code>, but it is not marked <code>irreducible</code>. There's something I'm not understanding correctly.</p>

#### [ Chris Hughes (Nov 26 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refl%20v%20rfl/near/148383903):
<p>My guess is that it doesn't know that the relation in question is equality</p>


{% endraw %}
