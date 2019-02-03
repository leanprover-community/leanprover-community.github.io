---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/79405Mutualrecursioonmadness.html
---

## Stream: [new members](index.html)
### Topic: [Mutual recursioon madness](79405Mutualrecursioonmadness.html)

---


{% raw %}
#### [ Ken Roe (Jul 25 2018 at 04:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mutual%20recursioon%20madness/near/130250392):
<p>How do I complete the following theorem:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">Value</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">NatValue</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">-&gt;</span> <span class="n">Value</span>
<span class="bp">|</span> <span class="n">ListValue</span> <span class="o">:</span> <span class="n">list</span> <span class="n">Value</span> <span class="bp">-&gt;</span> <span class="n">Value</span>
<span class="bp">|</span> <span class="n">NoValue</span> <span class="o">:</span> <span class="n">Value</span>

<span class="n">mutual</span> <span class="n">def</span> <span class="n">rangeSet</span><span class="o">,</span> <span class="n">rangeSetList</span>
<span class="k">with</span> <span class="n">rangeSet</span> <span class="o">:</span> <span class="n">Value</span> <span class="bp">-&gt;</span> <span class="n">option</span> <span class="o">(</span><span class="n">list</span> <span class="n">nat</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">Value</span><span class="bp">.</span><span class="n">ListValue</span> <span class="o">((</span><span class="n">Value</span><span class="bp">.</span><span class="n">NatValue</span> <span class="n">loc</span><span class="o">)</span><span class="bp">::</span><span class="n">r</span><span class="o">))</span> <span class="o">:=</span>
   <span class="k">match</span> <span class="n">rangeSetList</span> <span class="n">r</span> <span class="k">with</span>
   <span class="bp">|</span> <span class="n">option</span><span class="bp">.</span><span class="n">some</span> <span class="n">ll</span> <span class="o">:=</span> <span class="n">option</span><span class="bp">.</span><span class="n">some</span> <span class="o">(</span><span class="n">loc</span><span class="bp">::</span><span class="n">ll</span><span class="o">)</span>
   <span class="bp">|</span> <span class="bp">_</span>              <span class="o">:=</span> <span class="n">option</span><span class="bp">.</span><span class="n">none</span>
   <span class="kn">end</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">Value</span><span class="bp">.</span><span class="n">NatValue</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">option</span><span class="bp">.</span><span class="n">some</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span>
<span class="bp">|</span> <span class="bp">_</span>                  <span class="o">:=</span> <span class="n">option</span><span class="bp">.</span><span class="n">none</span>
<span class="k">with</span> <span class="n">rangeSetList</span> <span class="o">:</span> <span class="n">list</span> <span class="n">Value</span> <span class="bp">→</span> <span class="n">option</span> <span class="o">(</span><span class="n">list</span> <span class="n">nat</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">f</span><span class="bp">::</span><span class="n">r</span><span class="o">)</span> <span class="o">:=</span> <span class="k">match</span> <span class="n">rangeSet</span> <span class="n">f</span>
                     <span class="k">with</span>
                     <span class="bp">|</span> <span class="n">some</span> <span class="n">l</span> <span class="o">:=</span>
                         <span class="k">match</span> <span class="n">rangeSetList</span> <span class="n">r</span> <span class="k">with</span>
                         <span class="bp">|</span> <span class="n">option</span><span class="bp">.</span><span class="n">some</span> <span class="n">ll</span> <span class="o">:=</span> <span class="o">(</span><span class="n">some</span> <span class="o">(</span><span class="n">append</span> <span class="n">l</span> <span class="n">ll</span><span class="o">))</span>
                         <span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">option</span><span class="bp">.</span><span class="n">none</span>
                         <span class="kn">end</span>
                     <span class="bp">|</span> <span class="bp">_</span>     <span class="o">:=</span> <span class="n">option</span><span class="bp">.</span><span class="n">none</span>
                     <span class="kn">end</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">list</span><span class="bp">.</span><span class="n">nil</span> <span class="bp">ℕ.</span>

<span class="n">def</span> <span class="n">beq_nat</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">tt</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">beq_nat</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">ff</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">ff</span>

<span class="n">def</span> <span class="n">listmem</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span> <span class="o">:=</span> <span class="n">ff</span>
<span class="bp">|</span> <span class="n">e</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">cons</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span> <span class="k">if</span> <span class="n">beq_nat</span> <span class="n">e</span> <span class="n">a</span> <span class="k">then</span> <span class="n">tt</span> <span class="k">else</span> <span class="n">listmem</span> <span class="n">e</span> <span class="n">b</span>

<span class="n">def</span> <span class="n">Rmember</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">Value</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="n">a</span> <span class="n">v</span> <span class="o">:=</span> <span class="k">match</span> <span class="o">(</span><span class="n">rangeSet</span> <span class="n">v</span><span class="o">)</span> <span class="k">with</span>
         <span class="bp">|</span> <span class="n">option</span><span class="bp">.</span><span class="n">some</span> <span class="n">l</span> <span class="o">:=</span> <span class="n">listmem</span> <span class="n">a</span> <span class="n">l</span>
         <span class="bp">|</span> <span class="n">option</span><span class="bp">.</span><span class="n">none</span> <span class="o">:=</span> <span class="n">ff</span>
         <span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">rootIsMemberAux</span> <span class="o">(</span><span class="n">root</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">r</span><span class="o">:</span><span class="n">list</span> <span class="n">Value</span><span class="o">)</span> <span class="o">:</span>
        <span class="n">Rmember</span> <span class="n">root</span> <span class="o">(</span><span class="n">Value</span><span class="bp">.</span><span class="n">ListValue</span> <span class="o">(</span><span class="n">Value</span><span class="bp">.</span><span class="n">NatValue</span> <span class="n">root</span> <span class="bp">::</span> <span class="n">r</span><span class="o">))</span> <span class="bp">=</span> <span class="n">to_bool</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">unfold</span> <span class="n">Rmember</span><span class="o">,</span> <span class="n">unfold</span> <span class="n">rangeSet</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>I cannot find a way to properly unfold Rmember.</p>

#### [ Kenny Lau (Jul 25 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mutual%20recursioon%20madness/near/130250613):
<p>after the definition, prove the relevant equations (and tag it as a simp lemma if you want)</p>

#### [ Kenny Lau (Jul 25 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mutual%20recursioon%20madness/near/130250617):
<p>because you used <code>match</code></p>

#### [ Kevin Buzzard (Jul 25 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mutual%20recursioon%20madness/near/130263606):
<p>The philosophy is: the moment you write your definition, you should decide exactly which basic statements should be "true by definition" or "true because this is an immediate consequence of the definition with no additional arguments needed", formalise those statements, give them good names if possible, prove them with rfl or discover that they're not proved with rfl and then prove them using the equation lemmas generated by the equation compiler for you (the stuff called <code>beq_nat._main.equation8</code> and stuff like that) and tag them with <code>simp</code>. Then your definition begins to behave the way you intuitively want it to behave. It has taken me about a year to understand this but I think I'm slowly getting it straight now.</p>

#### [ Kenny Lau (Jul 29 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mutual%20recursioon%20madness/near/130519619):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">rootIsMemberAux_false</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">root</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">r</span><span class="o">:</span><span class="n">list</span> <span class="n">Value</span><span class="o">),</span>
        <span class="n">Rmember</span> <span class="n">root</span> <span class="o">(</span><span class="n">Value</span><span class="bp">.</span><span class="n">ListValue</span> <span class="o">(</span><span class="n">Value</span><span class="bp">.</span><span class="n">NatValue</span> <span class="n">root</span> <span class="bp">::</span> <span class="n">r</span><span class="o">))</span> <span class="bp">=</span> <span class="n">to_bool</span> <span class="n">true</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">specialize</span> <span class="n">H</span> <span class="mi">0</span> <span class="o">[</span><span class="n">Value</span><span class="bp">.</span><span class="n">NoValue</span><span class="o">],</span>
  <span class="n">unfold</span> <span class="n">Rmember</span> <span class="n">rangeSet</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">bool</span><span class="bp">.</span><span class="n">ff_ne_tt</span> <span class="n">H</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Jul 29 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mutual%20recursioon%20madness/near/130519620):
<p>thread is madness, mutual recursion is not</p>

#### [ Kenny Lau (Jul 29 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mutual%20recursioon%20madness/near/130520226):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">Value</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">NatValue</span>  <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">Value</span>
<span class="bp">|</span> <span class="n">ListValue</span> <span class="o">:</span> <span class="n">list</span> <span class="n">Value</span> <span class="bp">→</span> <span class="n">Value</span>
<span class="bp">|</span> <span class="n">NoValue</span>   <span class="o">:</span> <span class="n">Value</span>

<span class="n">mutual</span> <span class="n">def</span> <span class="n">rangeSet</span><span class="o">,</span> <span class="n">rangeSetList</span>
<span class="k">with</span> <span class="n">rangeSet</span> <span class="o">:</span> <span class="n">Value</span> <span class="bp">→</span> <span class="n">option</span> <span class="o">(</span><span class="n">list</span> <span class="n">nat</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">Value</span><span class="bp">.</span><span class="n">ListValue</span> <span class="o">((</span><span class="n">Value</span><span class="bp">.</span><span class="n">NatValue</span> <span class="n">loc</span><span class="o">)</span><span class="bp">::</span><span class="n">r</span><span class="o">))</span> <span class="o">:=</span>
  <span class="k">match</span> <span class="n">rangeSetList</span> <span class="n">r</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="n">option</span><span class="bp">.</span><span class="n">some</span> <span class="n">ll</span> <span class="o">:=</span> <span class="n">some</span> <span class="o">(</span><span class="n">loc</span><span class="bp">::</span><span class="n">ll</span><span class="o">)</span>
  <span class="bp">|</span> <span class="bp">_</span>              <span class="o">:=</span> <span class="n">some</span> <span class="o">[</span><span class="n">loc</span><span class="o">]</span>
  <span class="kn">end</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">Value</span><span class="bp">.</span><span class="n">NatValue</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">some</span> <span class="o">[]</span>
<span class="bp">|</span> <span class="bp">_</span>                  <span class="o">:=</span> <span class="n">none</span>
<span class="k">with</span> <span class="n">rangeSetList</span> <span class="o">:</span> <span class="n">list</span> <span class="n">Value</span> <span class="bp">→</span> <span class="n">option</span> <span class="o">(</span><span class="n">list</span> <span class="n">nat</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">f</span><span class="bp">::</span><span class="n">r</span><span class="o">)</span> <span class="o">:=</span> <span class="k">match</span> <span class="n">rangeSet</span> <span class="n">f</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="n">some</span> <span class="n">l</span> <span class="o">:=</span> <span class="k">match</span> <span class="n">rangeSetList</span> <span class="n">r</span> <span class="k">with</span>
    <span class="bp">|</span> <span class="n">option</span><span class="bp">.</span><span class="n">some</span> <span class="n">ll</span> <span class="o">:=</span> <span class="n">some</span> <span class="o">(</span><span class="n">append</span> <span class="n">l</span> <span class="n">ll</span><span class="o">)</span>
    <span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">none</span>
    <span class="kn">end</span>
  <span class="bp">|</span> <span class="bp">_</span>     <span class="o">:=</span> <span class="n">rangeSetList</span> <span class="n">r</span>
  <span class="kn">end</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">some</span> <span class="o">[]</span>

<span class="n">def</span> <span class="n">beq_nat</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">tt</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">beq_nat</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">ff</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">ff</span>

<span class="n">def</span> <span class="n">listmem</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span> <span class="o">:=</span> <span class="n">ff</span>
<span class="bp">|</span> <span class="n">e</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">cons</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span> <span class="k">if</span> <span class="n">beq_nat</span> <span class="n">e</span> <span class="n">a</span> <span class="k">then</span> <span class="n">tt</span> <span class="k">else</span> <span class="n">listmem</span> <span class="n">e</span> <span class="n">b</span>

<span class="n">def</span> <span class="n">Rmember</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">Value</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="n">a</span> <span class="n">v</span> <span class="o">:=</span> <span class="k">match</span> <span class="o">(</span><span class="n">rangeSet</span> <span class="n">v</span><span class="o">)</span> <span class="k">with</span>
         <span class="bp">|</span> <span class="n">option</span><span class="bp">.</span><span class="n">some</span> <span class="n">l</span> <span class="o">:=</span> <span class="n">listmem</span> <span class="n">a</span> <span class="n">l</span>
         <span class="bp">|</span> <span class="n">option</span><span class="bp">.</span><span class="n">none</span> <span class="o">:=</span> <span class="n">ff</span>
         <span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">rootIsMemberAux</span> <span class="o">(</span><span class="n">root</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">r</span><span class="o">:</span><span class="n">list</span> <span class="n">Value</span><span class="o">)</span> <span class="o">:</span>
        <span class="n">Rmember</span> <span class="n">root</span> <span class="o">(</span><span class="n">Value</span><span class="bp">.</span><span class="n">ListValue</span> <span class="o">(</span><span class="n">Value</span><span class="bp">.</span><span class="n">NatValue</span> <span class="n">root</span> <span class="bp">::</span> <span class="n">r</span><span class="o">))</span> <span class="bp">=</span> <span class="n">to_bool</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">unfold</span> <span class="n">Rmember</span><span class="o">,</span> <span class="n">unfold</span> <span class="n">rangeSet</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">rangeSetList</span> <span class="n">r</span><span class="bp">;</span>
    <span class="n">unfold</span> <span class="n">rangeSet</span><span class="bp">._</span><span class="n">match_1</span> <span class="n">Rmember</span><span class="bp">._</span><span class="n">match_1</span> <span class="n">listmem</span><span class="bp">;</span>
    <span class="n">rw</span> <span class="n">if_pos</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">refl</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">induction</span> <span class="n">root</span> <span class="k">with</span> <span class="bp">_</span> <span class="n">ih</span><span class="o">,</span> <span class="n">constructor</span><span class="o">,</span> <span class="n">apply</span> <span class="n">ih</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">refl</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">induction</span> <span class="n">root</span> <span class="k">with</span> <span class="bp">_</span> <span class="n">ih</span><span class="o">,</span> <span class="n">constructor</span><span class="o">,</span> <span class="n">apply</span> <span class="n">ih</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Jul 29 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Mutual%20recursioon%20madness/near/130520265):
<p>changed the definition of <code>rangeSet</code> and <code>rangeSetList</code></p>


{% endraw %}
