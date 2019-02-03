---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64871pnatandequationcompiler.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [pnat and equation compiler?](https://leanprover-community.github.io/archive/113488general/64871pnatandequationcompiler.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Nov 16 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pnat%20and%20equation%20compiler%3F/near/147850385):
<p>Can I somehow make the equation compiler work on pnat as well as it works on nat? Something like</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ+</span> <span class="bp">→</span> <span class="bp">ℕ+</span>
<span class="bp">|</span> <span class="mi">1</span> <span class="o">:=</span> <span class="mi">37</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">f</span> <span class="n">n</span>
</pre></div>


<p>How does the equation compiler work? It is presumably bound to the inbuilt constructors? Would this basically just entail writing a new pnat with <code>one</code> and <code>succ</code> and then defining stuff like <code>*</code> on the new structure?</p>

#### [ Kenny Lau (Nov 16 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pnat%20and%20equation%20compiler%3F/near/147850569):
<p>is it possible to build a custom equation compiler?</p>

#### [ Mario Carneiro (Nov 16 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pnat%20and%20equation%20compiler%3F/near/147850900):
<p>right. Lean 3 doesn't have the necessary customizability for this</p>

#### [ Mario Carneiro (Nov 16 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pnat%20and%20equation%20compiler%3F/near/147850924):
<p>Although we could write our own equation compiler if we write our own version of <code>def</code></p>


{% endraw %}
