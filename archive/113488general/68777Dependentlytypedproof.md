---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68777Dependentlytypedproof.html
---

## Stream: [general](index.html)
### Topic: [Dependently typed proof](68777Dependentlytypedproof.html)

---


{% raw %}
#### [ Frantisek Silvasi (Feb 27 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20typed%20proof/near/123038173):
<p>I don't suppose this sorry is provable - how does one convince Lean that whatever it is that I am mapping over comes from the list being mapped over? I can show that: <code>x ∈ filter P xs -&gt; P x</code>, but I can't tell map <code>x ∈ filter P xs</code>, even though it's "obvious". This is a toy version of what I am trying to do:</p>
<div class="codehilite"><pre><span></span>def positive := {x : ℤ // x &gt; 0}
def x_of_positive : positive → ℤ | ⟨a, _⟩ := a
def is_positive (x : ℤ) := x &gt; 0
instance {x : ℤ} : decidable (is_positive x) := by simp [is_positive]; apply_instance
def make_positive (x : ℤ) (h : x &gt; 0) : positive := ⟨x, h⟩
def test_two (x : positive) :=
  let pos := x_of_positive x in [pos+1, pos-1]
def foo (x : positive) :=
  let to_check  := test_two x in
  let checked   := list.filter is_positive to_check in
  let positives := list.map (λx, make_positive x sorry) checked in
  positives
</pre></div>

#### [ Andrew Ashworth (Feb 27 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20typed%20proof/near/123039719):
<p>you want the <code>of_mem_filter</code> lemma in mathlib</p>

#### [ Andrew Ashworth (Feb 27 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20typed%20proof/near/123039771):
<p>wait, sorry, I didn't look closely enough at your code snippet</p>

#### [ Frantisek Silvasi (Feb 27 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20typed%20proof/near/123039815):
<p>The idea is to escape positive to Z and check x+/-1. Then I filter the ones that are not positive and now I need a way to inject them back to the dependent type.</p>

#### [ Chris Hughes (Feb 27 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20typed%20proof/near/123039868):
<p>list.pmap in mathlib is probably what you want</p>

#### [ Andrew Ashworth (Feb 27 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20typed%20proof/near/123039927):
<p>one way to do it would be to prove that all the operations you use preserve the <code>is_positive</code> invariant</p>

#### [ Andrew Ashworth (Feb 27 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20typed%20proof/near/123039980):
<p>this is kind of tedious, i'd be hunting for a appropriate function in the data.list namespace, maybe <code>pmap</code> would be appropriate as Chris mentioned</p>

#### [ Patrick Massot (Feb 27 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20typed%20proof/near/123039982):
<p>Don't forget to use<code>```lean</code> instead of ````` at the beginning of your code blocks to have (partial) syntax highlighting</p>

#### [ Frantisek Silvasi (Feb 27 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20typed%20proof/near/123039988):
<p>I'll take a look at the pmap, thank you.</p>

#### [ Frantisek Silvasi (Feb 27 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20typed%20proof/near/123040083):
<p>Interesting. This <code>pmap</code> contraption is basically <code>map . filter</code>, which is exactly what I do, except I manage to lose some information in between.</p>

#### [ Chris Hughes (Feb 27 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20typed%20proof/near/123040088):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">def</span> <span class="n">positive</span> <span class="o">:=</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℤ</span> <span class="bp">//</span> <span class="n">x</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">}</span>
<span class="n">def</span> <span class="n">x_of_positive</span> <span class="o">:</span> <span class="n">positive</span> <span class="bp">→</span> <span class="bp">ℤ</span> <span class="bp">|</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="bp">_⟩</span> <span class="o">:=</span> <span class="n">a</span>
<span class="n">def</span> <span class="n">is_positive</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:=</span> <span class="n">x</span> <span class="bp">&gt;</span> <span class="mi">0</span>
<span class="kn">instance</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">}</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">is_positive</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">is_positive</span><span class="o">]</span><span class="bp">;</span> <span class="n">apply_instance</span>
<span class="n">def</span> <span class="n">make_positive</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="n">positive</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span>
<span class="n">def</span> <span class="n">test_two</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">positive</span><span class="o">)</span> <span class="o">:=</span>
  <span class="k">let</span> <span class="n">pos</span> <span class="o">:=</span> <span class="n">x_of_positive</span> <span class="n">x</span> <span class="k">in</span> <span class="o">[</span><span class="n">pos</span><span class="bp">+</span><span class="mi">1</span><span class="o">,</span> <span class="n">pos</span><span class="bp">-</span><span class="mi">1</span><span class="o">]</span>
<span class="n">def</span> <span class="n">foo</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">positive</span><span class="o">)</span> <span class="o">:=</span>
  <span class="k">let</span> <span class="n">to_check</span>  <span class="o">:=</span> <span class="n">test_two</span> <span class="n">x</span> <span class="k">in</span>
  <span class="k">let</span> <span class="n">checked</span>   <span class="o">:=</span> <span class="n">list</span><span class="bp">.</span><span class="n">filter</span> <span class="n">is_positive</span> <span class="n">to_check</span> <span class="k">in</span>
  <span class="k">let</span> <span class="n">positives</span> <span class="o">:=</span> <span class="n">list</span><span class="bp">.</span><span class="n">pmap</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="o">(</span><span class="n">hx</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">),</span> <span class="n">make_positive</span> <span class="n">x</span> <span class="n">hx</span><span class="o">)</span> <span class="n">checked</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">ha</span><span class="o">,</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">mem_filter</span><span class="bp">.</span><span class="mi">1</span> <span class="n">ha</span><span class="o">)</span><span class="bp">.</span><span class="n">right</span><span class="o">)</span> <span class="k">in</span>
  <span class="n">positives</span>
</pre></div>

#### [ Frantisek Silvasi (Feb 27 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20typed%20proof/near/123040098):
<p>Is the <code>a ha</code> accidental ;)?</p>

#### [ Frantisek Silvasi (Feb 27 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20typed%20proof/near/123040102):
<p>Thank you kindly for your help, I'm going to take <code>pmap</code> for a spin.</p>

#### [ Mario Carneiro (Feb 27 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20typed%20proof/near/123051610):
<p><span class="user-mention" data-user-email="frantisek.silvasi@tuke.sk" data-user-id="110099">@Frantisek Silvasi</span> The combination of filter and map in the positive case is <code>filter_map</code>. You should <code>filter_map</code> with the function <code>if h : x &gt; 0 then some (is_positive x h) else none</code></p>


{% endraw %}
