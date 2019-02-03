---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58749iffassoc.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [iff.assoc](https://leanprover-community.github.io/archive/113488general/58749iffassoc.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jul 25 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130294374):
<p>Chris asked today if <code>iff</code> was associative and a room full of mathematicians had no clue between them :-) We proved it by checking all 8 cases in Lean :-) </p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">finish</span>
<span class="kn">open</span> <span class="n">classical</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="n">R</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="o">((</span><span class="n">P</span> <span class="bp">↔</span> <span class="n">Q</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">R</span><span class="o">)</span> <span class="bp">↔</span> <span class="o">(</span><span class="n">P</span> <span class="bp">↔</span> <span class="o">(</span><span class="n">Q</span> <span class="bp">↔</span> <span class="n">R</span><span class="o">))</span> <span class="o">:=</span>
<span class="k">begin</span> <span class="n">cases</span> <span class="o">(</span><span class="n">em</span> <span class="n">P</span><span class="o">)</span><span class="bp">;</span><span class="n">cases</span> <span class="o">(</span><span class="n">em</span> <span class="n">Q</span><span class="o">)</span><span class="bp">;</span><span class="n">cases</span> <span class="o">(</span><span class="n">em</span> <span class="n">R</span><span class="o">)</span><span class="bp">;</span><span class="n">finish</span>
<span class="kn">end</span>
</pre></div>


<p>I was surprised that <code>finish</code> didn't do it alone:</p>
<div class="codehilite"><pre><span></span><span class="c1">-- example (P Q R : Prop) : ((P ↔ Q) ↔ R) ↔ (P ↔ (Q ↔ R)) := by finish -- fails</span>
</pre></div>

#### [ Kevin Buzzard (Jul 25 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130294462):
<p>I later found a better proof: if we break with convention and define true = 0 and false = 1 then iff is addition mod 2, and addition mod 2 is associative.</p>
<p>Is it true constructively? I struggled, but then again I am certainly no expert.</p>

#### [ Kevin Buzzard (Jul 25 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130294870):
<p>Here's one place I get stuck:</p>
<div class="codehilite"><pre><span></span>P Q R : Prop,
HQPQ : Q → (P ↔ Q),
HPQQ : (P ↔ Q) → Q,
H : Q → P,
HP : P
⊢ Q
</pre></div>


<p>I eliminated R (WLOG I believe) and I can't see how to do this. I am now minded to look for a counterexample. <span class="user-mention" data-user-id="110064">@Kenny Lau</span> to prove it's not constructively provable it would suffice to find some topological space with three subsets such that some random statement in topology is false, right?</p>

#### [ Simon Hudon (Jul 25 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130294880):
<p>I think <code>tauto</code> should manage to prove it</p>

#### [ Kevin Buzzard (Jul 25 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130294921):
<div class="codehilite"><pre><span></span>done tactic failed, there are unsolved goals
state:
P Q R : Prop,
a : P ↔ Q ↔ R,
a_1 : P,
a_2 : Q
⊢ R
</pre></div>

#### [ Kevin Buzzard (Jul 25 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130294937):
<p>Is <code>tauto</code> constructive?</p>

#### [ Patrick Massot (Jul 25 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130294941):
<p>Kevin, don't you have serious math to formalize?</p>

#### [ Kenny Lau (Jul 25 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130294942):
<p>I think so</p>

#### [ Kevin Buzzard (Jul 25 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130295020):
<p>Blame Chris. He pointed out that when a mathematician writes <code>A iff B iff C</code>, they mean <code>A iff B, and B iff C, so A iff C</code>, i.e. <code>iff.trans</code>. <code>iff.assoc</code> is a different question entirely :-) It's like the <code>1 &lt;= k &lt;= n</code> thing.</p>

#### [ Simon Hudon (Jul 25 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130295036):
<p>Yes, I believe it sticks to classical lemmas and if your propositions are decidable, it can prove more</p>

#### [ Patrick Massot (Jul 25 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130295241):
<p>The original question is perfectly legit, it's the constructivist deviance that I frown upon.</p>

#### [ Johan Commelin (Jul 25 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130295283):
<blockquote>
<p>I later found a better proof: if we break with convention and define true = 0 and false = 1 then iff is addition mod 2, and addition mod 2 is associative.</p>
</blockquote>
<p>That sounds like a proof by transport of structure (-;</p>

#### [ Chris Hughes (Jul 25 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130298421):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">em_of_iff_assoc</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">p</span> <span class="n">q</span> <span class="n">r</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">,</span> <span class="o">((</span><span class="n">p</span> <span class="bp">↔</span> <span class="n">q</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">r</span><span class="o">)</span> <span class="bp">↔</span> <span class="o">(</span><span class="n">p</span> <span class="bp">↔</span> <span class="o">(</span><span class="n">q</span> <span class="bp">↔</span> <span class="n">r</span><span class="o">)))</span> <span class="bp">→</span> <span class="bp">∀</span> <span class="n">p</span><span class="o">,</span> <span class="n">p</span> <span class="bp">∨</span> <span class="bp">¬</span><span class="n">p</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">h</span> <span class="n">p</span><span class="o">,</span> <span class="o">((</span><span class="n">h</span> <span class="o">(</span><span class="n">p</span> <span class="bp">∨</span> <span class="bp">¬</span><span class="n">p</span><span class="o">)</span> <span class="n">false</span> <span class="n">false</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span>
<span class="bp">⟨λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">h</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">hp</span><span class="o">,</span> <span class="n">h</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">hp</span><span class="o">))),</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">h</span><span class="bp">.</span><span class="n">elim</span><span class="bp">⟩</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="n">iff</span><span class="bp">.</span><span class="n">rfl</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">axioms</span> <span class="n">em_of_iff_assoc</span>
</pre></div>

#### [ Kevin Buzzard (Jul 25 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130298440):
<p>[no axioms]</p>

#### [ Kevin Buzzard (Jul 25 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130298446):
<p>Aah yes that's another way of resolving this</p>

#### [ Mario Carneiro (Jul 26 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130314672):
<p>I recall having this exact conversation with Kenny a while ago (prove LEM from iff assoc)</p>

#### [ Kenny Lau (Jul 26 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130323420):
<p>it was xor assoc</p>

#### [ Chris Hughes (Jul 26 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130323717):
<p>Did you prove XOR assoc -&gt; em?</p>

#### [ Kenny Lau (Jul 26 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130323718):
<blockquote>
<p>so here is a proof of LEM from xor assoc:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">p</span> <span class="n">q</span> <span class="n">r</span><span class="o">,</span> <span class="n">xor</span> <span class="n">p</span> <span class="o">(</span><span class="n">xor</span> <span class="n">q</span> <span class="n">r</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">xor</span> <span class="o">(</span><span class="n">xor</span> <span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="n">r</span><span class="o">)</span> <span class="o">{</span><span class="n">p</span><span class="o">}</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">∨</span> <span class="bp">¬</span> <span class="n">p</span> <span class="o">:=</span>
<span class="k">have</span> <span class="bp">¬</span> <span class="n">xor</span> <span class="n">p</span> <span class="n">p</span><span class="o">,</span> <span class="k">from</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">h</span><span class="bp">.</span><span class="n">elim</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">hp</span><span class="o">,</span> <span class="n">np</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">np</span> <span class="n">hp</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">hp</span><span class="o">,</span> <span class="n">np</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">np</span> <span class="n">hp</span><span class="o">),</span>
<span class="k">have</span> <span class="n">xor</span> <span class="n">p</span> <span class="o">(</span><span class="n">xor</span> <span class="n">p</span> <span class="n">true</span><span class="o">),</span> <span class="k">from</span> <span class="o">(</span><span class="n">h</span> <span class="n">p</span> <span class="n">p</span> <span class="n">true</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="bp">⟨</span><span class="n">trivial</span><span class="o">,</span> <span class="n">this</span><span class="bp">⟩</span><span class="o">),</span>
<span class="n">this</span><span class="bp">.</span><span class="n">imp</span> <span class="n">and</span><span class="bp">.</span><span class="n">left</span> <span class="n">and</span><span class="bp">.</span><span class="n">right</span>
</pre></div>


</blockquote>
<p><a href="#narrow/stream/116395-maths/subject/xor.20is.20not.20associative/near/125266318" title="#narrow/stream/116395-maths/subject/xor.20is.20not.20associative/near/125266318">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/xor.20is.20not.20associative/near/125266318</a></p>

#### [ Kenny Lau (Jul 26 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130323745):
<p>by Mario</p>

#### [ Kevin Buzzard (Jul 26 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130327664):
<p><code>xor</code> is associative because if you label false as 0 and true as 1 then it's addition mod 2. I thought it was funny that iff could be proved associative with the other labelling. It's almost like this is a proof strat and then you make all labellings and find out what each labelling proves :-)</p>

#### [ Kenny Lau (Jul 26 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130327717):
<p>can we create a Kripke frame where ((p ↔ q) ↔ r) but not (p ↔ (q ↔ r))?</p>

#### [ Kevin Buzzard (Jul 26 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130327883):
<p><code>and</code> is associative because multiplication is associative, and <code>or</code> is associative because multiplication is associative. <code>nand</code> is not associative (however it is commutative, answering a question which an UG asked me last Oct -- "does commutative imply associative?")</p>

#### [ Kevin Buzzard (Jul 26 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130327886):
<p>Is a Kripke frame just a fancy name for a topological space in this context?</p>

#### [ Kenny Lau (Jul 26 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130327900):
<p>Kripke frame is a semantics for constructive logic</p>

#### [ Kenny Lau (Jul 26 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130327903):
<p>I think topological space is another semantics</p>

#### [ Patrick Massot (Jul 26 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/iff.assoc/near/130327904):
<p>topos!</p>


{% endraw %}
