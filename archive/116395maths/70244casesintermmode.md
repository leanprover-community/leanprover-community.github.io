---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/70244casesintermmode.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [cases in term mode](https://leanprover-community.github.io/archive/116395maths/70244casesintermmode.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (May 01 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937140):
<p>I am trying to tell Lean what a path in a quiver is. How do I finish <code>is_a_path</code>?</p>
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span>

<span class="kn">structure</span> <span class="n">quiver</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span>
<span class="o">(</span><span class="n">E</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span>
<span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">E</span> <span class="bp">→</span> <span class="n">V</span><span class="o">)</span>
<span class="o">(</span><span class="n">t</span> <span class="o">:</span> <span class="n">E</span> <span class="bp">→</span> <span class="n">V</span><span class="o">)</span>

<span class="kn">variable</span> <span class="o">{</span><span class="n">Q</span> <span class="o">:</span> <span class="n">quiver</span><span class="o">}</span>

<span class="kn">definition</span> <span class="n">is_a_path</span> <span class="o">:</span> <span class="o">(</span><span class="n">list</span> <span class="n">Q</span><span class="bp">.</span><span class="n">E</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">l</span><span class="o">,</span> <span class="n">sorry</span>
</pre></div>

#### [ Mario Carneiro (May 01 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937192):
<p>hint: use <code>list.chain</code></p>

#### [ Kenny Lau (May 01 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937200):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">list</span><span class="bp">.</span><span class="n">chain</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">},</span> <span class="o">(</span><span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="n">constructors</span><span class="o">:</span>
<span class="n">list</span><span class="bp">.</span><span class="n">chain</span><span class="bp">.</span><span class="n">nil</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">list</span><span class="bp">.</span><span class="n">chain</span> <span class="n">R</span> <span class="n">a</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span>
<span class="n">list</span><span class="bp">.</span><span class="n">chain</span><span class="bp">.</span><span class="n">cons</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">},</span>
  <span class="n">R</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">list</span><span class="bp">.</span><span class="n">chain</span> <span class="n">R</span> <span class="n">b</span> <span class="n">l</span> <span class="bp">→</span> <span class="n">list</span><span class="bp">.</span><span class="n">chain</span> <span class="n">R</span> <span class="n">a</span> <span class="o">(</span><span class="n">b</span> <span class="bp">::</span> <span class="n">l</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (May 01 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937201):
<p>interesting</p>

#### [ Johan Commelin (May 01 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937248):
<p>By the way, do you think it is a good idea to use lists to capture paths?</p>

#### [ Mario Carneiro (May 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937304):
<p>You may want more complicated inductive structures in some circumstances, but here a list of edges is sufficient</p>

#### [ Kenny Lau (May 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937307):
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>

<span class="kn">structure</span> <span class="n">quiver</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span>
<span class="o">(</span><span class="n">E</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span>
<span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">E</span> <span class="bp">→</span> <span class="n">V</span><span class="o">)</span>
<span class="o">(</span><span class="n">t</span> <span class="o">:</span> <span class="n">E</span> <span class="bp">→</span> <span class="n">V</span><span class="o">)</span>

<span class="kn">variable</span> <span class="o">{</span><span class="n">Q</span> <span class="o">:</span> <span class="n">quiver</span><span class="o">}</span>

<span class="kn">definition</span> <span class="n">is_a_path</span> <span class="o">:</span> <span class="o">(</span><span class="n">list</span> <span class="n">Q</span><span class="bp">.</span><span class="n">E</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="o">[]</span>             <span class="o">:=</span> <span class="n">true</span>
<span class="bp">|</span> <span class="o">[</span><span class="n">x</span><span class="o">]</span>            <span class="o">:=</span> <span class="n">true</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">hd1</span><span class="bp">::</span><span class="n">hd2</span><span class="bp">::</span><span class="n">tl</span><span class="o">)</span> <span class="o">:=</span> <span class="n">Q</span><span class="bp">.</span><span class="n">t</span> <span class="n">hd1</span> <span class="bp">=</span> <span class="n">Q</span><span class="bp">.</span><span class="n">s</span> <span class="n">hd2</span> <span class="bp">∧</span> <span class="n">is_a_path</span> <span class="o">(</span><span class="n">hd2</span><span class="bp">::</span><span class="n">tl</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (May 01 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937323):
<p>Aaah, so I should use <code>|</code>. Thanks! But now you are not using <code>list.chain</code></p>

#### [ Mario Carneiro (May 01 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937326):
<p>you could use <code>list.chain</code> for the latter two cases</p>

#### [ Kenny Lau (May 01 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937328):
<p>the definition using <code>list.chain</code> is left to the reader as an exercise :P</p>

#### [ Mario Carneiro (May 01 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937371):
<p>alternatively, you could define it as an inductive type, which may be more natural</p>

#### [ Kenny Lau (May 01 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937375):
<p>oh... I just realized I wanted induction-recursion</p>

#### [ Mario Carneiro (May 01 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937379):
<p>not for this...</p>

#### [ Kenny Lau (May 01 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937383):
<div class="codehilite"><pre><span></span><span class="n">mutual</span> <span class="kn">inductive</span> <span class="n">path</span><span class="o">,</span> <span class="n">head</span>
<span class="k">with</span> <span class="n">path</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">A</span> <span class="o">:</span> <span class="n">Q</span><span class="bp">.</span><span class="n">E</span> <span class="bp">→</span> <span class="n">path</span>
<span class="k">with</span> <span class="n">head</span> <span class="o">:</span> <span class="n">path</span> <span class="bp">→</span> <span class="n">Q</span><span class="bp">.</span><span class="n">V</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">path</span><span class="bp">.</span><span class="n">A</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">_</span>
</pre></div>


<p>failed idea</p>

#### [ Mario Carneiro (May 01 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937390):
<p>you want the head to be a parameter, like in <code>chain</code></p>

#### [ Kenny Lau (May 01 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937446):
<p>oh what</p>

#### [ Johan Commelin (May 01 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937459):
<p>Kenny, I don't understand your last definition. What does <code>mutual</code> do?</p>

#### [ Kenny Lau (May 01 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937460):
<p><a href="https://leanprover.github.io/theorem_proving_in_lean/theorem_proving_in_lean.pdf" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/theorem_proving_in_lean.pdf">https://leanprover.github.io/theorem_proving_in_lean/theorem_proving_in_lean.pdf</a><br>
P.120, Section 7.9</p>

#### [ Kenny Lau (May 01 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937499):
<p>note that I was trying induction-recursion which is not a thing</p>

#### [ Kenny Lau (May 01 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937501):
<p>not to confuse you</p>

#### [ Johan Commelin (May 01 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937524):
<p>But your current definition is not equivalent to mine, right?</p>

#### [ Kenny Lau (May 01 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937532):
<p>yours? I haven't seen your definition</p>

#### [ Johan Commelin (May 01 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937572):
<p>Hmm, agreed. My bad.</p>

#### [ Johan Commelin (May 01 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937574):
<p>Let me try again: your second definition is not equivalent to your first, right?</p>

#### [ Kenny Lau (May 01 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937576):
<p>but I haven't finished my second definition</p>

#### [ Johan Commelin (May 01 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937591):
<p>Aaah, ok</p>

#### [ Kenny Lau (May 01 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937592):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> (maybe on its own thread?) if Lean had induction-recursion, would you be able to prove false? would there be a shorter proof than following godel?</p>

#### [ Mario Carneiro (May 01 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937643):
<p>No. Induction recursion would strengthen the system, it wouldn't be able to prove its own consistency because it now has induction-recursion and the simulated lean language would not</p>

#### [ Kenny Lau (May 01 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937649):
<p>why can't you simulate induction-recursion with induction-recursion?</p>

#### [ Mario Carneiro (May 01 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937654):
<p>you probably need induction-recursion-recursion or something</p>

#### [ Kenny Lau (May 01 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cases%20in%20term%20mode/near/125937655):
<p>hmm</p>


{% endraw %}
