---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/83428Equationformatchcase.html
---

## Stream: [new members](index.html)
### Topic: [Equation for match-case](83428Equationformatchcase.html)

---


{% raw %}
#### [ Erika (Nov 09 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147352744):
<p>Is there way to fill this hole (similar to coq's match-return)</p>
<div class="codehilite"><pre><span></span><span class="k">match</span> <span class="n">f</span> <span class="n">x</span> <span class="k">with</span>
<span class="bp">|</span> <span class="n">case1</span> <span class="n">y</span> <span class="o">:=</span> <span class="n">g</span> <span class="n">x</span> <span class="n">y</span> <span class="o">(</span><span class="bp">_</span><span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">case1</span> <span class="n">y</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">...</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Nov 09 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353395):
<p>It's not built in to the <code>match</code> syntax, but there is a tactic for this, <code>cases</code></p>

#### [ Mario Carneiro (Nov 09 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353401):
<div class="codehilite"><pre><span></span>cases h : f x with y,
{ -- case1 y
  exact g x y h, }
</pre></div>

#### [ Erika (Nov 09 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353467):
<p>ooh, that's good to know, I also noticed that <code>refine</code> will not make goals for <code>_</code> within a match arm</p>

#### [ Mario Carneiro (Nov 09 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353504):
<p>Lean does have match-return as well, but you have to handhold it a bit to get this goal</p>
<div class="codehilite"><pre><span></span><span class="k">match</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">P</span> <span class="k">with</span>
<span class="bp">|</span> <span class="n">case1</span> <span class="n">y</span><span class="o">,</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">g</span> <span class="n">x</span> <span class="n">y</span> <span class="o">(</span><span class="n">h</span><span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">case1</span> <span class="n">y</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">...</span>
<span class="kn">end</span>
</pre></div>

#### [ Erika (Nov 09 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353510):
<p>ah, I see, this is acceptable too</p>

#### [ Mario Carneiro (Nov 09 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353526):
<p>I'm not sure I know what you mean by not making goals for <code>_</code></p>

#### [ Mario Carneiro (Nov 09 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353529):
<p>refine will make goals for anything it can't infer</p>

#### [ Mario Carneiro (Nov 09 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353575):
<p>oh, maybe you mean <code>match</code> blocks refine because it uses the equation compiler (so it is typechecking in a different context, for a standalone definition)</p>

#### [ Erika (Nov 09 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353590):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">test</span> <span class="o">(</span><span class="n">b</span><span class="o">:</span> <span class="n">bool</span><span class="o">)</span> <span class="o">:</span> <span class="n">bool</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">refine</span> <span class="o">(</span><span class="k">match</span> <span class="n">b</span> <span class="k">with</span> <span class="bp">|</span> <span class="n">tt</span> <span class="o">:=</span> <span class="n">tt</span> <span class="bp">|</span> <span class="n">ff</span> <span class="o">:=</span> <span class="bp">_</span> <span class="kn">end</span><span class="o">),</span> <span class="c1">-- error for _, instead of new goal</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Nov 09 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353592):
<p>right</p>

#### [ Mario Carneiro (Nov 09 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353593):
<p>same happens when you use <code>let &lt;...&gt; = e1 in e2</code></p>

#### [ Erika (Nov 09 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353604):
<p>thanks for the help</p>

#### [ Mario Carneiro (Nov 09 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353611):
<p>you can still use tactics in there, but you have to make a separate begin-end block</p>

#### [ Mario Carneiro (Nov 09 2018 at 07:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Equation%20for%20match-case/near/147353653):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">test</span> <span class="o">(</span><span class="n">b</span><span class="o">:</span> <span class="n">bool</span><span class="o">)</span> <span class="o">:</span> <span class="n">bool</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">exact</span> <span class="o">(</span><span class="k">match</span> <span class="n">b</span> <span class="k">with</span> <span class="bp">|</span> <span class="n">tt</span> <span class="o">:=</span> <span class="n">tt</span> <span class="bp">|</span> <span class="n">ff</span> <span class="o">:=</span> <span class="k">begin</span>
    <span class="bp">...</span>
  <span class="kn">end</span> <span class="kn">end</span><span class="o">),</span>
<span class="kn">end</span>
</pre></div>


{% endraw %}
