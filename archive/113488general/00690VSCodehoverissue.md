---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00690VSCodehoverissue.html
---

## Stream: [general](index.html)
### Topic: [VS Code hover issue](00690VSCodehoverissue.html)

---


{% raw %}
#### [ Kevin Buzzard (Jan 12 2019 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VS%20Code%20hover%20issue/near/154997129):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">A</span> <span class="n">C</span> <span class="n">D</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">zzz</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">C</span> <span class="bp">→</span> <span class="n">C</span> <span class="bp">→</span> <span class="n">D</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">A</span><span class="o">)</span> <span class="o">:</span> <span class="n">D</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">g</span> <span class="o">(</span><span class="n">zzz</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">zzz</span> <span class="n">a</span><span class="o">),</span>
<span class="kn">end</span>
</pre></div>


<p>If I try this in VS Code (on Ubuntu) and hover over the two <code>zzz</code>s in the <code>apply</code> tactic line, the first one doesn't give me a little transient window saying <code>zzz : A \to C</code> but the second one does. Can someone else reproduce? Should I expect the window to pop up for the first <code>zzz</code> as well?</p>

#### [ Reid Barton (Jan 12 2019 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VS%20Code%20hover%20issue/near/154997252):
<p>I get the corresponding behavior in emacs too, so I guess it is an issue with Lean itself</p>

#### [ Kenny Lau (Jan 12 2019 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VS%20Code%20hover%20issue/near/154997256):
<p>reproduced (Windows, VS Code)</p>

#### [ Kevin Buzzard (Jan 12 2019 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VS%20Code%20hover%20issue/near/154997258):
<p><code>by exact g (zzz a) (zzz a)</code> has the issue, but just giving the term mode proof makes things work again.</p>

#### [ Kenny Lau (Jan 12 2019 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VS%20Code%20hover%20issue/near/154997300):
<p>reproduced all three behaviours</p>

#### [ Chris Hughes (Jan 12 2019 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VS%20Code%20hover%20issue/near/154997657):
<p>This is actually quite annoying whenever I do a <code>by haveI := _; exact _</code> proof</p>

#### [ Kevin Buzzard (Jan 12 2019 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VS%20Code%20hover%20issue/near/154997702):
<p>So it's the Lean server which ships these little windows out?</p>

#### [ Kenny Lau (Jan 12 2019 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VS%20Code%20hover%20issue/near/154997714):
<p>can we have the complicated diagram again?</p>


{% endraw %}
