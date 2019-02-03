---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/96236Wellfoundednessdeclarations.html
---

## Stream: [new members](index.html)
### Topic: [Well foundedness declarations](96236Wellfoundednessdeclarations.html)

---


{% raw %}
#### [ Ken Roe (Jul 11 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Well%20foundedness%20declarations/near/129479543):
<p>It seems for the mutually recursive function below, Lean cannot find the well founded relation.  How can I specify the relation?</p>
<p>inductive Value : Type<br>
| NatValue : ℕ -&gt; Value<br>
| ListValue : list Value -&gt; Value<br>
| NoValue : Value</p>
<p>mutual def findRecord, findRecordHelper<br>
with findRecord : ℕ → Value → (list Value)<br>
| l (Value.ListValue ((Value.NatValue x)::r)) :=<br>
                 if beq_nat x l then<br>
                     ((Value.NatValue x)::r)<br>
                 else findRecordHelper x r<br>
| _ _ := list.nil<br>
with findRecordHelper : ℕ → (list Value) → (list Value)<br>
| _ list.nil := list.nil<br>
| v (f::r) := match findRecord v f with<br>
              | list.nil := findRecordHelper v r<br>
              | x        := x<br>
              end.</p>

#### [ Kevin Buzzard (Jul 11 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Well%20foundedness%20declarations/near/129479933):
<p>Do you know about the triple back tick thing? It makes code much easier to read</p>

#### [ Kevin Buzzard (Jul 11 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Well%20foundedness%20declarations/near/129479954):
<p><code> ```lean </code> at the beginning and <code> ``` </code> at the end</p>

#### [ Ken Roe (Jul 11 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Well%20foundedness%20declarations/near/129480038):
<p>Here it is with the triple back thing.</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">Value</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">NatValue</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">-&gt;</span> <span class="n">Value</span>
<span class="bp">|</span> <span class="n">ListValue</span> <span class="o">:</span> <span class="n">list</span> <span class="n">Value</span> <span class="bp">-&gt;</span> <span class="n">Value</span>
<span class="bp">|</span> <span class="n">NoValue</span> <span class="o">:</span> <span class="n">Value</span>

<span class="n">mutual</span> <span class="n">def</span> <span class="n">findRecord</span><span class="o">,</span> <span class="n">findRecordHelper</span>
<span class="k">with</span> <span class="n">findRecord</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">Value</span> <span class="bp">→</span> <span class="o">(</span><span class="n">list</span> <span class="n">Value</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">l</span> <span class="o">(</span><span class="n">Value</span><span class="bp">.</span><span class="n">ListValue</span> <span class="o">((</span><span class="n">Value</span><span class="bp">.</span><span class="n">NatValue</span> <span class="n">x</span><span class="o">)</span><span class="bp">::</span><span class="n">r</span><span class="o">))</span> <span class="o">:=</span>
<span class="k">if</span> <span class="n">beq_nat</span> <span class="n">x</span> <span class="n">l</span> <span class="k">then</span>
<span class="o">((</span><span class="n">Value</span><span class="bp">.</span><span class="n">NatValue</span> <span class="n">x</span><span class="o">)</span><span class="bp">::</span><span class="n">r</span><span class="o">)</span>
<span class="k">else</span> <span class="n">findRecordHelper</span> <span class="n">x</span> <span class="n">r</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span>
<span class="k">with</span> <span class="n">findRecordHelper</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="o">(</span><span class="n">list</span> <span class="n">Value</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">list</span> <span class="n">Value</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span> <span class="o">:=</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span>
<span class="bp">|</span> <span class="n">v</span> <span class="o">(</span><span class="n">f</span><span class="bp">::</span><span class="n">r</span><span class="o">)</span> <span class="o">:=</span> <span class="k">match</span> <span class="n">findRecord</span> <span class="n">v</span> <span class="n">f</span> <span class="k">with</span>
<span class="bp">|</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span> <span class="o">:=</span> <span class="n">findRecordHelper</span> <span class="n">v</span> <span class="n">r</span>
<span class="bp">|</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">x</span>
<span class="kn">end</span><span class="bp">.</span>
</pre></div>


{% endraw %}
