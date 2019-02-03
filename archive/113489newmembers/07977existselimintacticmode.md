---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/07977existselimintacticmode.html
---

## Stream: [new members](index.html)
### Topic: [exists.elim in tactic mode?](07977existselimintacticmode.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Oct 11 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135602582):
<p>Hi -- I've been trying to prove a certain relation is symmetric -- is there a way to use "exists.elim" in tactic mode? It always gives me errors.</p>

#### [ Johan Commelin (Oct 11 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135602627):
<p>Is that <code>existsi</code>?</p>

#### [ Edward Ayers (Oct 11 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135602711):
<p><code>cases h with x p</code> will take an existential hypothesis and hit it with <code>exists.elim</code></p>

#### [ Johan Commelin (Oct 11 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135602728):
<p>Aah, in that case, you might also be interested in <code>rcases</code>. It is <code>cases</code> on steroids.</p>

#### [ Edward Ayers (Oct 11 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135602865):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">Q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">P</span><span class="o">(</span><span class="n">x</span><span class="o">))</span> <span class="o">(</span><span class="n">h₂</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">P</span><span class="o">(</span><span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="n">Q</span><span class="o">)</span> <span class="o">:</span> <span class="n">Q</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">cases</span> <span class="n">h₁</span> <span class="k">with</span> <span class="n">x</span> <span class="n">h₃</span><span class="o">,</span> <span class="c1">-- you can also omit the `with` and it will name them `h₁_w` and `h₁_h`</span>
    <span class="n">apply</span> <span class="n">h₂</span> <span class="bp">_</span> <span class="n">h₃</span>
<span class="kn">end</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Oct 11 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135602884):
<p>Ok, that seems to work, thanks. It's quite natural to uses cases on ∃, certainly.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 11 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135603772):
<p>(deleted)</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 11 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135603852):
<p>(deleted)</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 11 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135603888):
<p>(deleted)</p>

#### [ Bryan Gin-ge Chen (Oct 11 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135610299):
<p>I've been writing <code>exact exists.elim h (by { intro x hx, ... })</code>, but maybe that's considered less elegant.</p>

#### [ Kenny Lau (Oct 11 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135610649):
<p>yes, that is considered less elegant</p>

#### [ Kevin Buzzard (Oct 11 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135616278):
<p>Elegance was never my strong point when it came to Lean code.</p>

#### [ Kevin Buzzard (Oct 11 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135616293):
<p>Lucky I might now have an MSc student who will elegantify my code :D</p>


{% endraw %}
