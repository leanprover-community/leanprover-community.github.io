---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/05921Provingfromoptionalparameter.html
---

## Stream: [new members](index.html)
### Topic: [Proving from optional parameter](05921Provingfromoptionalparameter.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Nov 13 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20from%20optional%20parameter/near/147601867):
<p>How do I fill in the sorry?</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">→</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="n">f</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">c</span> <span class="bp">-</span> <span class="n">x</span><span class="o">))</span> <span class="o">:</span>  <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">g</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">c</span> <span class="bp">-</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>Presumably I need to intro and input an <code>x</code> into <code>g</code> somehow -- but how? I know the specific example can be rewritten in a way that makes the proof <code>by assumption</code>, but this situation cropped up in another proof.</p>

#### [ Chris Hughes (Nov 13 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20from%20optional%20parameter/near/147602168):
<p>I don't think this is true. The <code>:=</code> notation for <code>g</code>, just assigns a default value to <code>g</code>, if the user doesn't specify one when using the lemma, but you still have to prove for any <code>g</code>, since the user can override the default and use whatever value for <code>g</code> they like when using the lemma.</p>

#### [ Kevin Buzzard (Nov 13 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20from%20optional%20parameter/near/147608991):
<p>Maybe you want <code>let g := ... in ...</code>?</p>

#### [ Chris Hughes (Nov 13 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20from%20optional%20parameter/near/147610158):
<p>If you have <code>let g := something</code> in some proof, you can prove <code>g = something</code>   with <code>rfl</code>.</p>


{% endraw %}
