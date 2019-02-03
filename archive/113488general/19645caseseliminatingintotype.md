---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/19645caseseliminatingintotype.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [cases eliminating into type](https://leanprover-community.github.io/archive/113488general/19645caseseliminatingintotype.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 25 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125691805):
<p>I've just managed to internalise something Mario told me a couple of weeks ago.</p>

#### [ Kevin Buzzard (Apr 25 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125691809):
<p>Here's the <code>cases</code> tactic in action.</p>

#### [ Kevin Buzzard (Apr 25 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125691811):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">T</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">g</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">P</span> <span class="n">g</span><span class="o">)</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">4</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">g</span> <span class="n">Pg</span><span class="o">,</span>
<span class="c">/-</span><span class="cm"> context now has</span>
<span class="cm">g : γ,</span>
<span class="cm">Pg : P g</span>
<span class="cm">-/</span>
<span class="n">admit</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 25 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125691818):
<p>Now here's an example of it failing because we need to use the axiom of choice.</p>

#### [ Kevin Buzzard (Apr 25 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125691829):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">D</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">g</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">P</span> <span class="n">g</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="c1">-- cases H with g Pg -- fails as we can only eliminate into Prop</span>
<span class="n">admit</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 25 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125691862):
<p>But of course us classical people want to run cases anyway.</p>

#### [ Kevin Buzzard (Apr 25 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125691880):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">D</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">g</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">P</span> <span class="n">g</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="c1">-- cases H with g Pg -- fails as we can only eliminate into Prop</span>
<span class="k">let</span> <span class="n">g</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="n">H</span><span class="o">,</span>
<span class="k">have</span> <span class="n">Pg</span> <span class="o">:</span> <span class="n">P</span> <span class="n">g</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="n">H</span><span class="o">,</span>
<span class="c">/-</span><span class="cm"> ... but I made it anyway. Context now</span>
<span class="cm">g : γ := ...</span>
<span class="cm">Pg : P g</span>
<span class="cm">-/</span>
<span class="n">admit</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 25 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125691969):
<p>Using this trick (classical some and some_spec, <em>plus</em> the thing which I think Mario was trying to explain to me, which was that the moment you run <code>classical.some</code> you should make something _useful_ from <code>classical.some_spec</code> rather than just <code>have Pg := classical.some_spec H</code> which is a statement about <code>classical.some _</code> and hence harder to work with.</p>

#### [ Kevin Buzzard (Apr 25 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125691997):
<p>I am going to use this idiom again and again</p>

#### [ Kevin Buzzard (Apr 25 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125692002):
<p>but surely this should just be a tactic</p>

#### [ Kevin Buzzard (Apr 25 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125692011):
<p><code>classical_cases H with g Pg</code></p>

#### [ Kevin Buzzard (Apr 25 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125692082):
<p>I have been fretting a bit over things like the fact that the "obvious in maths" statement that if there's a surjection <code>X -&gt; Y</code> then there's an injection <code>Y -&gt; X</code> looks so convoluted in Lean.</p>

#### [ Kevin Buzzard (Apr 25 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125692096):
<p>But this tactic is probably trivial to write and just looks like an extension of <code>cases</code>, which the students learn very early on when learning Lean anyway</p>

#### [ Kevin Buzzard (Apr 25 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125692105):
<p>Is this there already?</p>

#### [ Kevin Buzzard (Apr 25 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125692161):
<p>If not -- I _really_ think it should be! It is far more natural to write than all this classical.some_spec or indefinite_confusion or whatever it's called</p>

#### [ Kevin Buzzard (Apr 25 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125692256):
<p>Let me stress that the trick is that you force the type of <code>Pg</code> to be <code>P g</code>, the thing you want it to be, by explicitly making it of this type when you construct it. Just writing <code>have Pg := classical.some_spec H</code> doesn't work.</p>

#### [ Reid Barton (Apr 25 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125692355):
<p>Maybe <code>choose</code> for the tactic name?</p>

#### [ Simon Hudon (Apr 25 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125692512):
<p>Have a look at <a href="https://github.com/unitb/lean-lib/blob/master/test/tactic/classical.lean" target="_blank" title="https://github.com/unitb/lean-lib/blob/master/test/tactic/classical.lean">https://github.com/unitb/lean-lib/blob/master/test/tactic/classical.lean</a> . It is not quite behaving like <code>cases</code> but it does make <code>some</code> and <code>epsilon</code> easier to work with. (I linked to the test case so that you see how I use it rather than how it works).</p>

#### [ Kevin Buzzard (Apr 25 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125693176):
<p>How do I use <code>apply_some_spec</code> Simon? I mean how do I get it running on my machine?</p>

#### [ Simon Hudon (Apr 25 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125693242):
<div class="codehilite"><pre><span></span>leanpkg add unitb/lean-lib
</pre></div>


<p>and don't forget:</p>
<div class="codehilite"><pre><span></span>import util.classical
</pre></div>

#### [ Kevin Buzzard (Apr 25 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125693530):
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">function</span>
<span class="kn">theorem</span> <span class="n">inj_of_surj</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">Hf</span> <span class="o">:</span> <span class="n">surjective</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">g</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">X</span><span class="o">,</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">id</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">existsi</span> <span class="bp">_</span><span class="o">,</span> <span class="c1">--slightly weird first move</span>
<span class="n">tactic</span><span class="bp">.</span><span class="n">swap</span><span class="o">,</span> <span class="c1">-- ha ha, swap is now overloaded because I opened function!</span>
<span class="o">{</span> <span class="n">intro</span> <span class="n">y</span><span class="o">,</span>
  <span class="c1">--classical_cases (Hf y) with x Hx,</span>
  <span class="k">let</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="o">(</span><span class="n">Hf</span> <span class="n">y</span><span class="o">),</span>
  <span class="k">have</span> <span class="n">Hx</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="o">(</span><span class="n">Hf</span> <span class="n">y</span><span class="o">),</span>
  <span class="n">exact</span> <span class="n">x</span>
<span class="o">},</span>
<span class="o">{</span> <span class="n">funext</span> <span class="n">y</span><span class="o">,</span>
  <span class="c1">--classical_cases (Hf y) with x Hx,</span>
  <span class="k">let</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="o">(</span><span class="n">Hf</span> <span class="n">y</span><span class="o">),</span>
  <span class="k">have</span> <span class="n">Hx</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="o">(</span><span class="n">Hf</span> <span class="n">y</span><span class="o">),</span>
  <span class="n">exact</span> <span class="n">Hx</span>
<span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 25 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125693535):
<p>I think my way looks a bit less intimidating for the newbie</p>

#### [ Simon Hudon (Apr 26 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125695647):
<p>You can do it like this:</p>
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">tactic</span>
<span class="kn">namespace</span> <span class="n">interactive</span>

<span class="kn">open</span> <span class="n">interactive</span> <span class="n">interactive</span><span class="bp">.</span><span class="n">types</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">ccases</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">cases_arg_p</span><span class="o">)</span> <span class="o">(</span><span class="n">ids</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">with_ident_list</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">cases</span> <span class="o">(</span><span class="n">e</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span><span class="bp">``</span><span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">indefinite_description</span> <span class="bp">_</span> <span class="err">%%</span><span class="o">(</span><span class="n">e</span><span class="bp">.</span><span class="mi">2</span><span class="o">)))</span> <span class="n">ids</span>

<span class="kn">end</span> <span class="n">interactive</span>
<span class="kn">end</span> <span class="n">tactic</span>

<span class="kn">open</span> <span class="n">function</span>
<span class="kn">theorem</span> <span class="n">inj_of_surj</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">Hf</span> <span class="o">:</span> <span class="n">surjective</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">g</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">X</span><span class="o">,</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">id</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">split</span><span class="o">,</span> <span class="c1">--slightly weird first move</span>
<span class="n">tactic</span><span class="bp">.</span><span class="n">swap</span><span class="o">,</span> <span class="c1">-- ha ha, swap is now overloaded because I opened function!</span>
<span class="o">{</span> <span class="n">intro</span> <span class="n">y</span><span class="o">,</span>
  <span class="n">ccases</span> <span class="o">(</span><span class="n">Hf</span> <span class="n">y</span><span class="o">)</span> <span class="k">with</span> <span class="n">x</span> <span class="n">Hx</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">x</span>
<span class="o">},</span>
<span class="o">{</span> <span class="n">funext</span> <span class="n">y</span><span class="o">,</span>
  <span class="n">ccases</span> <span class="o">(</span><span class="n">Hf</span> <span class="n">y</span><span class="o">)</span> <span class="k">with</span> <span class="n">x</span> <span class="n">Hx</span><span class="o">,</span>
  <span class="c1">-- let x := classical.some (Hf y),</span>
  <span class="c1">-- have Hx : f x = y := classical.some_spec (Hf y),</span>
  <span class="n">simp</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">Hx</span>
<span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Apr 26 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125696083):
<p>Lol @ indefinite_confusion. But the right way to do this is to do cases on the pair <code>some, some_spec</code>, which is indeed <code>classical.indefinite_description</code>.</p>

#### [ Mario Carneiro (Apr 26 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125696468):
<p>Here's an idea that might help:</p>
<div class="codehilite"><pre><span></span>@[elab_as_eliminator]
noncomputable def classical.rec_on
  {α} {p : α → Prop} {C : Sort*}
  (h : ∃ a, p a) (H : ∀ a, p a → C) : C :=
H (classical.some h) (classical.some_spec h)
</pre></div>

#### [ Mario Carneiro (Apr 26 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125696509):
<p>You can <code>apply</code> that theorem to do cases on an exists without making <code>cases</code> complain</p>

#### [ Kenny Lau (Apr 26 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125696540):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> what if I told you “surjective functions have right inverse” is already in mathlib as <code>inv_fun</code></p>

#### [ Mario Carneiro (Apr 26 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125696553):
<p>But in the case of <code>inj_of_surj</code>, this is the wrong approach (same for <code>ccases</code> or cases on indefinite description), because you are doing the case twice, once to define the function and again to give its properties. That means that you will have to unfold whatever proof term you constructed in the first half, i.e. <code>classical.rec_on</code> or <code>subtype.rec_on</code> or something</p>

#### [ Mario Carneiro (Apr 26 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125696594):
<p>The right solution here is to use <code>axiom_of_choice</code></p>

#### [ Mario Carneiro (Apr 26 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125696615):
<div class="codehilite"><pre><span></span>theorem inj_of_surj (X Y : Type) (f : X → Y) (Hf : surjective f) : ∃ g : Y → X, f ∘ g = id :=
let ⟨g, h⟩ := classical.axiom_of_choice Hf in ⟨g, funext h⟩
</pre></div>

#### [ Mario Carneiro (Apr 26 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125696623):
<p>(Also this theorem already exists in core IIRC)</p>

#### [ Mario Carneiro (Apr 26 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125697084):
<p>For the golfers:</p>
<div class="codehilite"><pre><span></span>(classical.axiom_of_choice Hf).imp $ λ g, funext
</pre></div>

#### [ Kevin Buzzard (Apr 26 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125711834):
<p>The inj of surj example was pedagogical -- I know it's there, but I want to teach students how to write it without pain. There are other times this comes up too. I suspect a lot of undergraduate mathematicians will be very confused by constructive maths so I want to hide it from them. Many thanks for the tactic Simon and for the comments everyone.</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125711847):
<p>I think in particular that you should add <code>axiom_of_choice</code> to your toolkit</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125711911):
<p>You are certainly right in that it's not currently in my toolkit.</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125711913):
<p>I remember really struggling with all of this the first time around.</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125711954):
<p>It's only revisiting it now I'm older and wiser that I understand it well enough to try and manipulate it into a form which I think beginners with no programming background might find more comprehensible.</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125711961):
<p>I would think that <code>axiom_of_choice</code> is the version of choice people are most used to</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125711965):
<p><code>classical.some</code> is more like global choice, which ZFC doesn't usually admit so most proofs aren't framed that way</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712014):
<p>The problem is that most mathematicians apply the axiom of choice without noticing, and those that are aware of it believe that it says that an infinite product of non-empty sets is non-empty.</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712015):
<p>Mathematicians don't know the difference between the different kinds of non-empty</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712022):
<p>I'm not talking about LEM here though</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712027):
<p>right</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712028):
<p>all notions of nonempty are basically the same modulo LEM</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712031):
<p>they don't know what LEM is either</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712063):
<p>I'm talking about how to use AC proper</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712073):
<p>I think it is not a good thing that lean thinks LEM and AC are the same</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712074):
<p>mathematicians certainly don't</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712081):
<p>you can argue that mathematicians think both are true, but I think they admit LEM implicitly and don't see the need for AC until they reach a certain level</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712082):
<p>exactly</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712084):
<p>LEM is part of the logic</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712121):
<p>AC has some content</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20eliminating%20into%20type/near/125712127):
<p>Lean kind of gives you the ability to distinguish the two, since LEM is computable but AC is not</p>


{% endraw %}
