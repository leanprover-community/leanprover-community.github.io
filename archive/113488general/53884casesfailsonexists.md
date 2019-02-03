---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53884casesfailsonexists.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [cases fails on exists](https://leanprover-community.github.io/archive/113488general/53884casesfailsonexists.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Nima (Apr 21 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485520):
<p>Can you explain this error message (it happens when I say <code>cases hm with aa bb</code>, but <code>by_cases number.has_min α with hm</code> works perfectly fine):</p>
<div class="codehilite"><pre><span></span><span class="n">induction</span> <span class="n">tactic</span> <span class="n">failed</span><span class="o">,</span> <span class="n">recursor</span> <span class="err">&#39;</span><span class="n">Exists</span><span class="bp">.</span><span class="n">dcases_on&#39;</span> <span class="n">can</span> <span class="n">only</span> <span class="n">eliminate</span> <span class="n">into</span> <span class="kt">Prop</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">number</span> <span class="n">α</span><span class="o">,</span>
<span class="n">trvk</span> <span class="o">:</span> <span class="n">triviality_kind</span><span class="o">,</span>
<span class="n">strk</span> <span class="o">:</span> <span class="n">strictness_kind</span><span class="o">,</span>
<span class="n">bnd</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span>
<span class="n">c</span> <span class="o">:</span> <span class="n">constraint</span> <span class="n">α</span> <span class="n">trvk</span> <span class="n">kupper</span> <span class="n">strk</span><span class="o">,</span>
<span class="n">ht</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">is_trivial</span> <span class="n">c</span><span class="o">,</span>
<span class="n">hs</span> <span class="o">:</span> <span class="n">is_strict</span> <span class="n">c</span><span class="o">,</span>
<span class="n">hm</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">hm</span> <span class="o">:</span> <span class="n">number</span><span class="bp">.</span><span class="n">has_min</span> <span class="n">α</span><span class="o">),</span> <span class="n">number</span><span class="bp">.</span><span class="n">min</span> <span class="n">hm</span> <span class="bp">&lt;</span> <span class="n">get_bound</span> <span class="n">c</span> <span class="bp">_</span>
<span class="err">⊢</span> <span class="n">α</span>
</pre></div>

#### [ Mario Carneiro (Apr 21 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485620):
<p>You can't destruct an exists directly because it's a (small eliminating) Prop. However, in the special case when it is an exists over a prop, you can use <code>hm.fst</code> and <code>hm.snd</code> to project out the components</p>

#### [ Nima (Apr 21 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485757):
<p>Isn't that the same situation as </p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">a</span><span class="o">:</span><span class="mi">1</span><span class="bp">&gt;</span><span class="mi">2</span><span class="o">,</span> <span class="n">false</span><span class="o">)</span> <span class="bp">→</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">h</span> <span class="k">with</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="c1">-- no problem here</span>
  <span class="n">assumption</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Apr 21 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485763):
<p>You can use cases on exists to prove a Prop, but not to construct data (something in a type that lives in Type)</p>

#### [ Mario Carneiro (Apr 21 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485803):
<p>here it's okay because <code>false : Prop</code></p>

#### [ Mario Carneiro (Apr 21 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485804):
<p>while in the other case <code>α : Type u_1 != Prop</code></p>

#### [ Mario Carneiro (Apr 21 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485850):
<p>The basic idea is that if you want to use partial functions in your code, you have to write all the actual function calls not dependent on the proof part</p>

#### [ Nima (Apr 21 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485851):
<p>Are you pointing to the <code>α</code> that is used in the goal?</p>

#### [ Mario Carneiro (Apr 21 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485852):
<p>yes</p>

#### [ Mario Carneiro (Apr 21 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485854):
<p>why are you "proving" alpha?</p>

#### [ Mario Carneiro (Apr 21 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485861):
<p>you should write all the functions first, in term mode, and only enter tactic mode to justify the proof part of your partial function</p>

#### [ Nima (Apr 21 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485862):
<p>It is supposed to be a function, not a proof.<br>
I find it easier to go into tactic mode.</p>

#### [ Mario Carneiro (Apr 21 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485904):
<p>You want to be careful about the dependency structure that the tactic creates</p>

#### [ Nima (Apr 21 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485948):
<p>For example, here is a function in term mode.</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">has_min</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
  <span class="k">if</span> <span class="n">ht</span> <span class="o">:</span> <span class="n">is_trivial</span> <span class="n">c</span> <span class="k">then</span> <span class="n">number</span><span class="bp">.</span><span class="n">has_min</span> <span class="n">α</span> <span class="k">else</span>
  <span class="k">match</span> <span class="n">dirk</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="n">klower</span> <span class="o">:=</span> <span class="n">is_strict</span> <span class="n">c</span> <span class="bp">→</span>
                <span class="bp">¬</span><span class="n">number</span><span class="bp">.</span><span class="n">is_dense</span> <span class="n">α</span> <span class="bp">∧</span>
                <span class="bp">∀</span> <span class="n">hm</span><span class="o">:</span><span class="n">number</span><span class="bp">.</span><span class="n">has_max</span> <span class="n">α</span><span class="o">,</span>
                  <span class="n">get_bound</span> <span class="n">c</span> <span class="o">(</span><span class="n">not_trivial_is_not_ktrv</span> <span class="n">c</span> <span class="n">ht</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="n">number</span><span class="bp">.</span><span class="n">max</span> <span class="n">hm</span>
  <span class="bp">|</span> <span class="n">kupper</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="n">hm</span> <span class="o">:</span> <span class="n">number</span><span class="bp">.</span><span class="n">has_min</span> <span class="n">α</span><span class="o">,</span>
                <span class="o">(</span><span class="n">is_strict</span> <span class="n">c</span> <span class="bp">→</span>
                  <span class="o">(</span><span class="n">number</span><span class="bp">.</span><span class="n">min</span> <span class="n">hm</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="n">get_bound</span> <span class="n">c</span> <span class="o">(</span><span class="n">not_trivial_is_not_ktrv</span> <span class="n">c</span> <span class="n">ht</span><span class="o">)))</span>
  <span class="kn">end</span>
</pre></div>


<p>Now suppose, <code>has_min</code> is true. What is the value of <code>min</code>? I have to first check triviality, then direction, then whether or not alpha is dense, then ...<br>
Every one of these gives me a different function that I should use to find minimum value. So I entered tactic mode.</p>

#### [ Mario Carneiro (Apr 21 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485950):
<p>For example with your if then else function from before:</p>
<div class="codehilite"><pre><span></span>def f (c:check) : nat :=
if h : p then
  f₁ (begin ... end)
else
  f₂ (begin ... end)
</pre></div>


<p>you should enter tactic mode for the proof part but not while determining which function to call</p>

#### [ Mario Carneiro (Apr 21 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485998):
<p>I already mentioned before that you are making your life harder with this encoding, you really want to encode this in the structure of your inductive types. You would be better served encoding <code>has_min</code> as an inductive type as well</p>

#### [ Mario Carneiro (Apr 21 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125486151):
<p>Have you considered using <code>roption</code>? It encodes a pair of a proof and a partial function, which makes it easy to write super dependent partial functions like this</p>

#### [ Nima (Apr 21 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125486261):
<p>Nope, I have to look into <code>roption</code>.</p>

#### [ Mario Carneiro (Apr 21 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125486627):
<p>Why do you use so many decidable propositions instead of bools for your work? Usually the answer is convenience but it's clearly not helping you</p>

#### [ Nima (Apr 21 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125486992):
<p>Not sure, practice ;) or avoiding coe as much as possible</p>

#### [ Mario Carneiro (Apr 21 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487285):
<p>What do you think of having the <code>number</code> fields like this? I find that using <code>option</code> makes the proofs and statements much easier</p>
<div class="codehilite"><pre><span></span>def has_in_between {α} [has_lt α] (x y : α) := ∃ z : α, x &lt; z ∧ z &lt; y

class number (α:Type*) extends decidable_linear_order α :=
[nonempty_decidable : decidable (nonempty α)]
(arbitrary : ∀ [nonempty α], α)
[subsingleton_decidable : decidable (subsingleton α)]
(min : option α)
(max : option α)
(min_prop : ∀ a, a ∈ min ↔ ∀ m:α, a ≤ m)
(max_prop : ∀ a, a ∈ max ↔ ∀ m:α, m ≤ a)

(next : α → option α)
(next_prop : ∀ x y, y ∈ next x ↔ x &lt; y ∧ ∀ z:α, z ≤ x ∨ y ≤ z)
(prev : α → option α)
(prev_prop : ∀ x y, y ∈ next x ↔ x &lt; y ∧ ∀ z:α, z ≤ x ∨ y ≤ z)
(is_dense : bool)
(is_dense_prop :
    if is_dense then
      ∀ x y : α, x &lt; y → ∃ z : α, x &lt; z ∧ z &lt; y
    else
      (∀ x ∉ max, ∃ y, y ∈ next x) ∧
      (∀ x ∉ min, ∃ y, y ∈ prev x))

[has_in_between_decidable : ∀ x y : α, decidable (has_in_between x y)]

(zero   : option α)

(neg₀ : α     → option α)
(add₀ : α → α → option α)
(mul₀ : α → α → option α)
(sub₀ : α → α → option α)
(div₀ : α → α → option α)

(neg₁ : α     → option α)
(add₁ : α → α → option α)
(mul₁ : α → α → option α)
(sub₁ : α → α → option α)
(div₁ : α → α → option α)
</pre></div>

#### [ Nima (Apr 21 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487469):
<p>They used to be like this.<br>
The reason I separated <code>min</code> and <code>has_min</code> is just for performance of the final <strong>hypothetical</strong> code.<br>
<code>has_min</code> is never slower than <code>min</code>, but it is quite possible for it to be faster.<br>
For example, </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">has_inf</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="k">if</span> <span class="n">is_satisfiable</span> <span class="n">c</span> <span class="k">then</span> <span class="n">is_bounded_left</span>  <span class="n">c</span> <span class="k">else</span> <span class="n">number</span><span class="bp">.</span><span class="n">has_max</span> <span class="n">α</span>
<span class="n">def</span> <span class="n">inf</span> <span class="o">(</span><span class="n">h</span><span class="o">:</span> <span class="n">has_inf</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="o">:=</span>
  <span class="k">if</span> <span class="n">hsat</span> <span class="o">:</span> <span class="n">is_satisfiable</span> <span class="n">c</span> <span class="k">then</span>
    <span class="k">let</span> <span class="n">hbl</span> <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">mp</span> <span class="o">(</span><span class="n">if_pos</span> <span class="n">hsat</span><span class="o">)</span> <span class="n">h</span> <span class="k">in</span>
    <span class="k">if</span> <span class="n">ht</span> <span class="o">:</span> <span class="n">is_trivial</span> <span class="n">c</span>  <span class="k">then</span> <span class="n">number</span><span class="bp">.</span><span class="n">min</span> <span class="o">(</span><span class="n">hbl</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">ht</span><span class="o">))</span> <span class="k">else</span>
    <span class="k">if</span> <span class="n">hd</span> <span class="o">:</span> <span class="n">dirk</span> <span class="bp">=</span> <span class="n">kupper</span> <span class="k">then</span> <span class="n">number</span><span class="bp">.</span><span class="n">min</span> <span class="o">(</span><span class="n">hbl</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">hd</span><span class="o">))</span> <span class="k">else</span>
    <span class="n">get_bound</span> <span class="n">c</span> <span class="o">(</span><span class="n">not_trivial_is_not_ktrv</span> <span class="n">c</span> <span class="n">ht</span><span class="o">)</span>
  <span class="k">else</span>
    <span class="n">number</span><span class="bp">.</span><span class="n">max</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">mp</span> <span class="o">(</span><span class="n">if_neg</span> <span class="n">hsat</span><span class="o">)</span> <span class="n">h</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Apr 21 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487513):
<p>when will knowing <code>has_inf</code> make computation of <code>inf</code> faster?</p>

#### [ Mario Carneiro (Apr 21 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487560):
<p>A quick and simple addition to allow for faster implementations of <code>has_min</code> is the following extra field:</p>
<div class="codehilite"><pre><span></span>[has_min : decidable min.is_some]
</pre></div>

#### [ Nima (Apr 21 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487566):
<p>I did not say using <code>has_inf</code> makes <code>inf</code> faster, suppose all I want is <code>has_inf</code>. If I use option, I have to call <code>inf</code>. But <code>has_inf</code> could have been implemented faster.</p>

#### [ Mario Carneiro (Apr 21 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487609):
<p>or you could do it in two stages with a <code>bool</code> function:</p>
<div class="codehilite"><pre><span></span>(has_min : bool) (has_min_prop : has_min = min.is_some)
</pre></div>

#### [ Mario Carneiro (Apr 21 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487614):
<p>that way it won't interfere with the definition of <code>min</code> or <code>inf</code> or whatever</p>

#### [ Nima (Apr 21 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487615):
<p>May be we mean different things by <code>implementation</code>. I mean non-lean code, more specifically C++. If I did not care about performance, I would never consider C++.</p>

#### [ Mario Carneiro (Apr 21 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487665):
<p>I care about performance more than most lean users, indeed I'm writing a compiler and we have to think about these things. But the extra hypothesis parameter is not as erasable as it appears at first</p>

#### [ Nima (Apr 21 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487708):
<p>Are you talking about <code>(h: has_inf c)</code> as a parameter to <code>inf</code>?</p>

#### [ Mario Carneiro (Apr 21 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487709):
<p>yes</p>

#### [ Mario Carneiro (Apr 21 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487714):
<p>How do you intend to relate the lean code you are writing to C++? This affects performance considerations</p>

#### [ Mario Carneiro (Apr 21 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487721):
<p>Is this code to be <code>#eval</code>d? Compiled to C++ and then run? Used only for correctness verification?</p>

#### [ Nima (Apr 21 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487859):
<p>But that is for <code>inf</code> and not <code>has_inf</code>.<br>
Right now I know nothing about automatic code generation in lean. I doubt it does exactly what I wish (not sure what exactly that is either). For example, if I have a constraint, I want it to be mutable. If I define addition of two constraints, there is going to be 5 (I guess) additions, but in lean I will have only one. So mostly manual transformation. That could also be a reason why I am not a fan of <code>match</code> in lean. I don't know any formal semantics for c++, so not much into verification/validation. But I was thinking about an interval that support both strict and non-strict constraint in both dynamic and static, and realized that is too much for me to verify on my mind. So it would be nice if I can prove the operations first (on a scratch paper) and then at least be sure about the correct behavior.</p>


{% endraw %}
