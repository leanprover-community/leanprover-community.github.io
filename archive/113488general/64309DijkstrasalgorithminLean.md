---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64309DijkstrasalgorithminLean.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Dijkstra's algorithm in Lean](https://leanprover-community.github.io/archive/113488general/64309DijkstrasalgorithminLean.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Dec 08 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dijkstra%27s%20algorithm%20in%20Lean/near/151183263):
<p>One of my children was explaining Dijkstra's algorithm to me -- they are far more computer-sciency than I am. After some conversation I decided that they might be saying this:</p>
<div class="codehilite"><pre><span></span><span class="c1">-- Dijkstra&#39;s algorithm in Lean</span>

<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fintype</span>

<span class="kn">structure</span> <span class="n">finite_directed_graph</span> <span class="o">:=</span>
<span class="c1">-- finite type of vertices</span>
<span class="o">(</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">HVfin</span><span class="o">:</span> <span class="n">fintype</span> <span class="n">V</span><span class="o">]</span>
<span class="c1">-- finite type of directed edges</span>
<span class="o">(</span><span class="n">E</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">HE</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">E</span><span class="o">]</span> <span class="o">(</span><span class="n">Esrc</span> <span class="o">:</span> <span class="n">E</span> <span class="bp">→</span> <span class="n">V</span><span class="o">)</span> <span class="o">(</span><span class="n">Etrg</span> <span class="o">:</span> <span class="n">E</span> <span class="bp">→</span> <span class="n">V</span><span class="o">)</span>


<span class="kn">definition</span> <span class="n">Dijkstra</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="n">finite_directed_graph</span><span class="o">)</span>
<span class="c1">-- I need an algorithm which spits out an element of V from a non-empty subset</span>
<span class="o">[</span><span class="n">HVord</span> <span class="o">:</span> <span class="n">decidable_linear_order</span> <span class="n">G</span><span class="bp">.</span><span class="n">V</span><span class="o">]</span>
<span class="c1">-- I&#39;d rather have a decidable linear ordered monoid for my weights</span>
<span class="o">(</span><span class="n">W</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">HW</span> <span class="o">:</span> <span class="n">decidable_linear_ordered_comm_group</span> <span class="n">W</span><span class="o">]</span>
<span class="c1">-- Weight of an edge</span>
<span class="o">(</span><span class="n">Ewt</span> <span class="o">:</span> <span class="n">G</span><span class="bp">.</span><span class="n">E</span> <span class="bp">→</span> <span class="n">W</span><span class="o">)</span>
<span class="c1">-- start and finish vertex</span>
<span class="o">(</span><span class="n">start</span> <span class="o">:</span> <span class="n">G</span><span class="bp">.</span><span class="n">V</span><span class="o">)</span> <span class="o">(</span><span class="n">finish</span> <span class="o">:</span> <span class="n">G</span><span class="bp">.</span><span class="n">V</span><span class="o">)</span>
<span class="o">:</span> <span class="n">with_top</span> <span class="n">W</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="n">finite_directed_graph</span><span class="o">}</span> <span class="o">[</span><span class="n">HVord</span> <span class="o">:</span> <span class="n">decidable_linear_order</span> <span class="n">G</span><span class="bp">.</span><span class="n">V</span><span class="o">]</span>
<span class="o">{</span><span class="n">W</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">HW</span> <span class="o">:</span> <span class="n">decidable_linear_ordered_comm_group</span> <span class="n">W</span><span class="o">]</span> <span class="o">(</span><span class="n">Ewt</span> <span class="o">:</span> <span class="n">G</span><span class="bp">.</span><span class="n">E</span> <span class="bp">→</span> <span class="n">W</span><span class="o">)</span>
<span class="o">(</span><span class="n">start</span> <span class="o">:</span> <span class="n">G</span><span class="bp">.</span><span class="n">V</span><span class="o">)</span> <span class="o">(</span><span class="n">finish</span> <span class="o">:</span> <span class="n">G</span><span class="bp">.</span><span class="n">V</span><span class="o">)</span>

<span class="n">def</span> <span class="n">is_path_from_start_to_finish</span> <span class="o">:</span> <span class="n">G</span><span class="bp">.</span><span class="n">V</span> <span class="bp">→</span> <span class="n">G</span><span class="bp">.</span><span class="n">V</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">G</span><span class="bp">.</span><span class="n">E</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">start</span> <span class="n">finish</span> <span class="o">[]</span> <span class="o">:=</span> <span class="o">(</span><span class="n">start</span> <span class="bp">=</span> <span class="n">finish</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">start</span> <span class="n">finish</span> <span class="o">(</span><span class="n">l</span> <span class="bp">::</span> <span class="n">ls</span><span class="o">)</span> <span class="o">:=</span> <span class="n">G</span><span class="bp">.</span><span class="n">Esrc</span> <span class="n">l</span> <span class="bp">=</span> <span class="n">start</span> <span class="bp">∧</span> <span class="n">is_path_from_start_to_finish</span> <span class="o">(</span><span class="n">G</span><span class="bp">.</span><span class="n">Etrg</span> <span class="n">l</span><span class="o">)</span> <span class="o">(</span><span class="n">finish</span><span class="o">)</span> <span class="n">ls</span>

<span class="n">include</span> <span class="n">HW</span>
<span class="n">def</span> <span class="n">path_length</span> <span class="o">(</span><span class="n">Ewt</span> <span class="o">:</span> <span class="n">G</span><span class="bp">.</span><span class="n">E</span> <span class="bp">→</span> <span class="n">W</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="n">G</span><span class="bp">.</span><span class="n">E</span> <span class="bp">→</span> <span class="n">W</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">l</span> <span class="bp">::</span> <span class="n">ls</span><span class="o">)</span> <span class="o">:=</span> <span class="n">Ewt</span> <span class="n">l</span> <span class="bp">+</span> <span class="n">path_length</span> <span class="n">ls</span>

<span class="n">include</span> <span class="n">HVord</span>
<span class="c1">-- do we want an existence result or should the algorithm return an actual minimal path?</span>
<span class="kn">theorem</span> <span class="n">Dijkstra_attained</span> <span class="o">:</span> <span class="n">Dijkstra</span> <span class="n">G</span> <span class="n">W</span> <span class="n">Ewt</span> <span class="n">start</span> <span class="n">finish</span> <span class="bp">≠</span> <span class="n">none</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">Es</span> <span class="o">:</span> <span class="n">list</span> <span class="n">G</span><span class="bp">.</span><span class="n">E</span><span class="o">,</span> <span class="n">is_path_from_start_to_finish</span> <span class="n">start</span> <span class="n">finish</span> <span class="n">Es</span>
<span class="bp">∧</span> <span class="n">Dijkstra</span> <span class="n">G</span> <span class="n">W</span> <span class="n">Ewt</span> <span class="n">start</span> <span class="n">finish</span> <span class="bp">=</span> <span class="n">some</span> <span class="o">(</span><span class="n">path_length</span> <span class="n">Ewt</span> <span class="n">Es</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">theorem</span> <span class="n">Dijkstra_best</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">Es</span> <span class="o">:</span> <span class="n">list</span> <span class="n">G</span><span class="bp">.</span><span class="n">E</span><span class="o">,</span>
<span class="o">(</span><span class="bp">∀</span> <span class="n">w</span> <span class="o">:</span> <span class="n">W</span><span class="o">,</span> <span class="n">w</span> <span class="err">∈</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">Ewt</span> <span class="bp">→</span> <span class="n">w</span> <span class="bp">≥</span> <span class="mi">0</span><span class="o">)</span> <span class="bp">→</span>
<span class="n">is_path_from_start_to_finish</span> <span class="n">start</span> <span class="n">finish</span> <span class="n">Es</span> <span class="bp">→</span>
<span class="n">Dijkstra</span> <span class="n">G</span> <span class="n">W</span> <span class="n">Ewt</span> <span class="n">start</span> <span class="n">finish</span> <span class="bp">≤</span> <span class="n">some</span> <span class="o">(</span><span class="n">path_length</span> <span class="n">Ewt</span> <span class="n">Es</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>What happens next? I (or he) need(s) to implement the algorithm (the first sorry) and then prove that it has the properties I claim (the other sorries). Does this algorithm get written in Lean or meta Lean? It can be written in Lean, right? Then I can prove things about it. Have I got this straight? My sons are learning a bunch of algorithms and I'm trying to figure out what I can say about them in Lean.</p>

#### [ Johan Commelin (Dec 08 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dijkstra%27s%20algorithm%20in%20Lean/near/151184026):
<p>Right. I would implement it in Lean. My guess/hope is that it shouldn't be too hard.</p>

#### [ Johan Commelin (Dec 08 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dijkstra%27s%20algorithm%20in%20Lean/near/151184072):
<p>But I think one of the reasons that graph theory hasn't been fleshed out much is that it's hard to get the data structures right. You want to be both general enough and usable. But for a one-off push for Dijkstra, I guess this should work.</p>

#### [ Kevin Buzzard (Dec 08 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dijkstra%27s%20algorithm%20in%20Lean/near/151184218):
<p>This is exactly the sort of thing I don't understand, and which my children were telling me about. So now we have to think about issues involving exactly how to implement the data structures which show up in the implementation of the algorithm?</p>

#### [ Johan Commelin (Dec 08 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dijkstra%27s%20algorithm%20in%20Lean/near/151184617):
<p>Well, I'm certainly not an expert in graph theory. So I would probably just go for it, and see where I get stuck.</p>

#### [ Johan Commelin (Dec 08 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dijkstra%27s%20algorithm%20in%20Lean/near/151184621):
<p>But probably Mario, Sean or Simon can share a lot more wisdom here.</p>

#### [ Johan Commelin (Dec 08 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dijkstra%27s%20algorithm%20in%20Lean/near/151184664):
<p>Dijkstra is just a form of BFS, and Simon already implemented a BFS algorithm in meta Lean for the <code>tfae</code> tactic.</p>

#### [ Kevin Buzzard (Dec 08 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dijkstra%27s%20algorithm%20in%20Lean/near/151184794):
<p>Is implementing it in Lean and implementing it in meta Lean two completely different problems? I tried to put in enough hypotheses to guarantee that the algorithm terminates in finite type. My son and I were desperate to get some kinds of infinite graphs in but we pretty soon found some weird examples where the algorithm was poorly behaved, so we decided to stick to finite types for vertex and edge types.</p>

#### [ Johan Commelin (Dec 08 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dijkstra%27s%20algorithm%20in%20Lean/near/151184909):
<p>It probably is a different game whether you use <code>meta</code> or not.</p>

#### [ Andrew Ashworth (Dec 08 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dijkstra%27s%20algorithm%20in%20Lean/near/151194004):
<p>There's a bit on graphs in Coq here: <a href="https://softwarefoundations.cis.upenn.edu/vfa-current/Color.html" target="_blank" title="https://softwarefoundations.cis.upenn.edu/vfa-current/Color.html">https://softwarefoundations.cis.upenn.edu/vfa-current/Color.html</a>, if this has caught your interest.</p>


{% endraw %}
