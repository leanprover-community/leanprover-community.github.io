---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/78110matchhypothesis.html
---

## Stream: [general](index.html)
### Topic: [match hypothesis](78110matchhypothesis.html)

---


{% raw %}
#### [ Alexander Bentkamp (Sep 12 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133796312):
<p>Hi, </p>
<p>I hope you can help me with the following issue:</p>
<p>I have this defintion containing a proof obligation:</p>
<div class="codehilite"><pre><span></span>  <span class="n">def</span> <span class="n">clip_tensor_index2</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">ds₁</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">ds₂</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">tensor_index</span> <span class="o">(</span><span class="n">zipdims</span> <span class="n">ds₂</span> <span class="n">ds₁</span><span class="o">)</span> <span class="bp">→</span> <span class="n">option</span> <span class="o">(</span><span class="n">tensor_index</span> <span class="n">ds₂</span><span class="o">)</span>
  <span class="bp">|</span> <span class="n">ds₁</span> <span class="n">ds₂</span> <span class="bp">⟨</span><span class="n">is</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="k">match</span> <span class="n">clip_tensor_index_list</span> <span class="n">ds₂</span> <span class="n">is</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="n">none</span> <span class="o">:=</span> <span class="n">none</span>
  <span class="bp">|</span> <span class="n">some</span> <span class="n">js</span> <span class="o">:=</span> <span class="n">some</span> <span class="bp">⟨</span> <span class="n">js</span> <span class="o">,</span> <span class="n">clip_tensor_index_list_correct</span> <span class="n">ds₂</span> <span class="n">is</span> <span class="n">js</span> <span class="n">sorry</span><span class="bp">⟩</span>
  <span class="kn">end</span>
</pre></div>


<p>Where I put <code>sorry</code>, I need to prove that <code>clip_tensor_index_list ds₂ is = some js</code>, which should be obvious since I matched <code>clip_tensor_index_list ds₂ is</code> with <code>some js</code>. How can I do this?</p>
<p><span class="user-mention" data-user-id="110596">@Rob Lewis</span>  helped me out with this solution using tactics:</p>
<div class="codehilite"><pre><span></span>  def clip_tensor_index2 : Π {ds₁ : list ℕ} (ds₂ : list ℕ), tensor_index (zipdims ds₂ ds₁) → option (tensor_index ds₂)
  | ds₁ ds₂ ⟨is, h⟩ :=
  begin
    cases h1 : clip_tensor_index_list ds₂ is with js,
    exact none,
    exact some ⟨ js , clip_tensor_index_list_correct ds₂ is js h1 ⟩
  end
</pre></div>


<p>This works, but I am curious if I could avoid using tactics inside a definition.</p>

#### [ Kevin Buzzard (Sep 12 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133798275):
<p>If the thing you're matching on (<code>clip_tensor_index_list ds₂ is</code>) is an inductive type T then you could use <code>T.rec</code> (it looks like <code>option.rec</code> in your case)</p>

#### [ Alexander Bentkamp (Sep 13 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133869597):
<p>Yes, <code>clip_tensor_index_list ds₂ is</code> is of type <code>option</code>. However, with <code>option.rec</code>, I still have the same issue. Where you see the <code>sorry</code> below, I need to provide a proof of <code>clip_tensor_index_list ds₂ is = some js</code>. How can I get it?</p>
<div class="codehilite"><pre><span></span>  <span class="n">def</span> <span class="n">clip_tensor_index2</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">ds₁</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">ds₂</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">tensor_index</span> <span class="o">(</span><span class="n">zipdims</span> <span class="n">ds₂</span> <span class="n">ds₁</span><span class="o">)</span> <span class="bp">→</span> <span class="n">option</span> <span class="o">(</span><span class="n">tensor_index</span> <span class="n">ds₂</span><span class="o">)</span>
  <span class="bp">|</span> <span class="n">ds₁</span> <span class="n">ds₂</span> <span class="bp">⟨</span><span class="n">is</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span> <span class="o">:=</span>
  <span class="n">option</span><span class="bp">.</span><span class="n">rec</span> <span class="n">none</span> <span class="o">(</span><span class="bp">λ</span><span class="n">js</span><span class="o">,</span> <span class="n">some</span> <span class="bp">⟨</span> <span class="n">js</span> <span class="o">,</span> <span class="n">clip_tensor_index_list_correct</span> <span class="n">ds₂</span> <span class="n">is</span> <span class="n">js</span> <span class="n">sorry</span> <span class="bp">⟩</span><span class="o">)</span> <span class="o">(</span><span class="n">clip_tensor_index_list</span> <span class="n">ds₂</span> <span class="n">is</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Sep 13 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133870081):
<p>I see: I was too quick. This has come up before and I can't remember the answer :-(</p>

#### [ Kevin Buzzard (Sep 13 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133870103):
<p>Of course you could look at the proof term generated by the tactic version and see how Lean did it ;-)</p>

#### [ Kevin Buzzard (Sep 13 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133870338):
<p>MWE:</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">f</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">bool</span> <span class="bp">//</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">tt</span><span class="o">}</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">h</span> <span class="o">:</span> <span class="n">b</span> <span class="k">with</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span>
  <span class="o">{</span> <span class="c1">-- h : b = ff</span>
    <span class="n">exact</span> <span class="bp">⟨</span><span class="n">tt</span><span class="o">,</span><span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="o">},</span>
  <span class="o">{</span> <span class="c1">-- h : b = tt and I will now use h</span>
    <span class="n">exact</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span><span class="n">h</span><span class="bp">⟩</span>
  <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Sep 13 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133870367):
<p>and <code>#print f</code> tells me that Lean used <code>bool.cases_on</code></p>

#### [ Rob Lewis (Sep 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133870592):
<p>Like I told you yesterday, I'm sure there's a way to make <code>match</code> handle this, but I can't remember. Here's a workaround in term mode, by giving a motive to the recursor explicitly. I suspect that the tactic version is doing basically this under the hood.</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">f</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">bool</span> <span class="bp">//</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">tt</span><span class="o">}</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">bool</span><span class="bp">.</span><span class="n">rec_on</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">b&#39;</span><span class="o">,</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">b&#39;</span> <span class="bp">→</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">bool</span> <span class="bp">//</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">tt</span><span class="o">})</span> <span class="n">b</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">tt</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">)</span> <span class="n">rfl</span>
</pre></div>

#### [ Kevin Buzzard (Sep 13 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133870647):
<p>right, that's what the term looks like in my bool example. The trick is a cleverly-chosen motive.</p>

#### [ Kenny Lau (Sep 13 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133871740):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">f&#39;</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">b₁</span> <span class="n">b₂</span> <span class="o">:</span> <span class="n">bool</span><span class="o">,</span> <span class="n">b₁</span> <span class="bp">=</span> <span class="n">b₂</span> <span class="bp">→</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">bool</span> <span class="bp">//</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">tt</span><span class="o">}</span>
<span class="bp">|</span> <span class="n">b</span> <span class="n">tt</span> <span class="n">H</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span> <span class="n">H</span><span class="bp">⟩</span>
<span class="bp">|</span> <span class="n">b</span> <span class="n">ff</span> <span class="n">H</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">tt</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Sep 13 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133871743):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> is this the answer to your question?</p>

#### [ Kevin Buzzard (Sep 13 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133871755):
<p>right</p>

#### [ Kevin Buzzard (Sep 13 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133871766):
<p>so you are defining an auxiliary <code>f'</code> using pattern matching</p>

#### [ Kevin Buzzard (Sep 13 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133871768):
<p>and then you can define f using f'</p>

#### [ Kenny Lau (Sep 13 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133871811):
<p>wait, I think I have another answer</p>

#### [ Kevin Buzzard (Sep 13 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133871818):
<p>I had a look at that <code>tail</code> / <code>vector</code> example in TPIL and they also used an auxiliary function, but then they did something cleverer and got the equation compiler to do it</p>

#### [ Kevin Buzzard (Sep 13 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133871830):
<p><a href="https://leanprover.github.io/theorem_proving_in_lean/induction_and_recursion.html#dependent-pattern-matching" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/induction_and_recursion.html#dependent-pattern-matching">https://leanprover.github.io/theorem_proving_in_lean/induction_and_recursion.html#dependent-pattern-matching</a></p>

#### [ Kenny Lau (Sep 13 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133871840):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">f&#39;</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">nat</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="bp">_</span>
<span class="bp">|</span> <span class="n">k</span><span class="bp">@</span><span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="k">let</span> <span class="n">K</span> <span class="o">:=</span> <span class="n">k</span> <span class="k">in</span> <span class="bp">_</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">f&#39; : ℕ → ℕ,</span>
<span class="cm">n : ℕ,</span>
<span class="cm">K : ℕ := n + 1</span>
<span class="cm">⊢ ℕ</span>
<span class="cm">-/</span>
</pre></div>

#### [ Kenny Lau (Sep 13 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133871841):
<p>this is the answer you seek</p>

#### [ Kenny Lau (Sep 13 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133871888):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">f&#39;</span> <span class="o">:</span> <span class="n">bool</span> <span class="bp">→</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">bool</span> <span class="bp">//</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">tt</span><span class="o">}</span>
<span class="bp">|</span> <span class="n">b</span><span class="bp">@</span><span class="n">tt</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span>
<span class="bp">|</span> <span class="n">ff</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">tt</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (Sep 13 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133871893):
<p>excellent, thanks Kenny. <span class="user-mention" data-user-id="129120">@Alexander Bentkamp</span> hopefully this is enough hints :-)</p>

#### [ Patrick Massot (Sep 13 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133872520):
<p>I have no idea what you are talking about, and yet it seems interesting. What the point of that definition of <code>f'</code>? Clearly <code>example : f' = (λ x, ⟨tt, rfl⟩) := by  ext x ; cases x; refl</code></p>

#### [ Patrick Massot (Sep 13 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133872524):
<p>So, what are you trying to do?</p>

#### [ Kenny Lau (Sep 13 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133872592):
<p>honestly, nobody knows what we're trying to do unless OP provides an MWE</p>

#### [ Alexander Bentkamp (Sep 13 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133873156):
<p>Hi, thanks for all the answers. I am trying to apply what you wrote to my situation, but I am still having trouble.</p>
<p>What's an MWE?</p>

#### [ Keeley Hoek (Sep 13 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133873162):
<p>Minimum working example</p>

#### [ Alexander Bentkamp (Sep 13 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133873179):
<p>Oh, ok. I'll try to come up with something.</p>

#### [ Kevin Buzzard (Sep 13 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133873602):
<p>Patrick my definition is too minimal. The OP just wants to define a function on <code>option A</code> by matching, and when defining its value at <code>x := some y</code> he needs the proof that <code>x = some y</code> to define the value.</p>

#### [ Kevin Buzzard (Sep 13 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133873615):
<p><span class="user-mention" data-user-id="129120">@Alexander Bentkamp</span> the reason your original post didn't get much attention is because we can't just cut and paste your code into a blank lean session, so someone had to figure out what you were actually asking.</p>

#### [ Alexander Bentkamp (Sep 13 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133873672):
<p>Oh, I feel like my post is getting a lot of attention :)<br>
I almost finished the MWE...</p>

#### [ Alexander Bentkamp (Sep 13 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133873823):
<p>Here it is:</p>
<div class="codehilite"><pre><span></span>    <span class="n">def</span> <span class="n">clip</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">option</span> <span class="o">(</span><span class="n">list</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>

    <span class="n">def</span> <span class="n">p</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span> <span class="o">:=</span> <span class="n">sorry</span>

    <span class="kn">lemma</span> <span class="n">clip_correct</span> <span class="o">(</span><span class="n">is</span> <span class="n">js</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">clip</span> <span class="n">is</span> <span class="bp">=</span> <span class="n">some</span> <span class="n">js</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="n">is</span> <span class="n">js</span> <span class="o">:=</span> <span class="n">sorry</span>

    <span class="n">def</span> <span class="n">lookup</span> <span class="o">(</span><span class="n">is</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">option</span> <span class="o">{</span> <span class="n">js</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">is</span> <span class="n">js</span><span class="o">}</span> <span class="o">:=</span>
    <span class="k">match</span> <span class="o">(</span><span class="n">clip</span> <span class="n">is</span><span class="o">)</span> <span class="k">with</span>
    <span class="bp">|</span> <span class="n">none</span> <span class="o">:=</span> <span class="n">none</span>
    <span class="bp">|</span> <span class="n">some</span> <span class="n">js</span> <span class="o">:=</span> <span class="n">some</span> <span class="bp">⟨</span> <span class="n">js</span><span class="o">,</span> <span class="n">clip_correct</span> <span class="n">is</span> <span class="n">js</span> <span class="bp">_</span> <span class="bp">⟩</span>
    <span class="kn">end</span>
</pre></div>


<p>The last underscore would need a proof that <code>clip is = some js</code>.</p>

#### [ Alexander Bentkamp (Sep 13 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133874241):
<p>If I follow <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> 's advise, i.e. I use tactic mode to generate a working definition and use #print to view it, then I get this:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">lookup</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">is</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">option</span> <span class="o">{</span><span class="n">js</span> <span class="bp">//</span> <span class="err">↥</span><span class="o">(</span><span class="n">p</span> <span class="n">is</span> <span class="n">js</span><span class="o">)}</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="o">(</span><span class="n">is</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span><span class="o">),</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="bp">_</span><span class="n">x</span> <span class="o">:</span> <span class="n">option</span> <span class="o">(</span><span class="n">list</span> <span class="bp">ℕ</span><span class="o">))</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="n">clip</span> <span class="n">is</span> <span class="bp">=</span> <span class="bp">_</span><span class="n">x</span><span class="o">),</span>
     <span class="n">option</span><span class="bp">.</span><span class="n">cases_on</span> <span class="bp">_</span><span class="n">x</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="n">clip</span> <span class="n">is</span> <span class="bp">=</span> <span class="n">none</span><span class="o">),</span> <span class="n">none</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">js</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="n">clip</span> <span class="n">is</span> <span class="bp">=</span> <span class="n">some</span> <span class="n">js</span><span class="o">),</span> <span class="n">some</span> <span class="bp">⟨</span><span class="n">js</span><span class="o">,</span> <span class="bp">_⟩</span><span class="o">)</span>
       <span class="n">h1</span><span class="o">)</span>
    <span class="o">(</span><span class="n">clip</span> <span class="n">is</span><span class="o">)</span>
    <span class="bp">_</span>
</pre></div>


<p>But if I copy paste this into the editor, I get </p>
<div class="codehilite"><pre><span></span>invalid &#39;option.cases_on&#39; application, elaborator has special support for this kind of application (it is handled as an &quot;eliminator&quot;), but the expected type must be known
</pre></div>


<p>What type needs to be known?</p>

#### [ Kenny Lau (Sep 13 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133875506):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">clip</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">option</span> <span class="o">(</span><span class="n">list</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="n">def</span> <span class="n">p</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">lemma</span> <span class="n">clip_correct</span> <span class="o">(</span><span class="n">is</span> <span class="n">js</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">clip</span> <span class="n">is</span> <span class="bp">=</span> <span class="n">some</span> <span class="n">js</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="n">is</span> <span class="n">js</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="n">def</span> <span class="n">lookup_aux</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">is</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">cis</span> <span class="o">:</span> <span class="n">option</span> <span class="o">(</span><span class="n">list</span> <span class="bp">ℕ</span><span class="o">)),</span> <span class="n">clip</span> <span class="n">is</span> <span class="bp">=</span> <span class="n">cis</span> <span class="bp">→</span> <span class="n">option</span> <span class="o">{</span> <span class="n">js</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">is</span> <span class="n">js</span><span class="o">}</span>
<span class="bp">|</span> <span class="n">is</span> <span class="n">none</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">none</span>
<span class="bp">|</span> <span class="n">is</span> <span class="o">(</span><span class="n">some</span> <span class="n">js</span><span class="o">)</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">some</span> <span class="bp">⟨</span><span class="n">js</span><span class="o">,</span> <span class="n">clip_correct</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span><span class="bp">⟩</span>

<span class="n">def</span> <span class="n">lookup</span> <span class="o">(</span><span class="n">is</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">option</span> <span class="o">{</span> <span class="n">js</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">is</span> <span class="n">js</span><span class="o">}</span> <span class="o">:=</span>
<span class="n">lookup_aux</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">rfl</span>
</pre></div>

#### [ Kevin Buzzard (Sep 13 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133875547):
<p>my guess is that it's the type of of the lambda which you're evaluating at <code>clip is</code></p>

#### [ Kevin Buzzard (Sep 13 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133875555):
<p>So Kenny's solution is via the auxiliary function trick which is mentioned in TPIL</p>

#### [ Rob Lewis (Sep 13 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133875645):
<p>The elaborator isn't able to infer the motive for <code>cases_on</code>. If you don't want to use an aux declaration, you can give the motive manually, but personally I think the tactic version is cleaner than all of these.</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">lookup&#39;</span> <span class="o">(</span><span class="n">is</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">option</span> <span class="o">{</span> <span class="n">js</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">is</span> <span class="n">js</span><span class="o">}</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">option</span><span class="bp">.</span><span class="n">cases_on</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="n">clip</span> <span class="n">is</span> <span class="bp">=</span> <span class="n">i</span> <span class="bp">→</span> <span class="n">option</span> <span class="o">{</span> <span class="n">js</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">is</span> <span class="n">js</span><span class="o">})</span> <span class="o">(</span><span class="n">clip</span> <span class="n">is</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">none</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">js</span> <span class="n">h</span><span class="o">,</span> <span class="n">some</span> <span class="bp">⟨</span><span class="n">js</span><span class="o">,</span> <span class="n">clip_correct</span> <span class="n">is</span> <span class="n">js</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">)</span>
  <span class="n">rfl</span>

<span class="n">def</span> <span class="n">lookup&#39;&#39;</span> <span class="o">(</span><span class="n">is</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">option</span> <span class="o">{</span> <span class="n">js</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">is</span> <span class="n">js</span><span class="o">}</span> <span class="o">:=</span>
<span class="k">have</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">i</span><span class="o">},</span> <span class="n">clip</span> <span class="n">is</span> <span class="bp">=</span> <span class="n">i</span> <span class="bp">→</span> <span class="n">option</span> <span class="o">{</span> <span class="n">js</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">is</span> <span class="n">js</span><span class="o">},</span> <span class="k">from</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span>
<span class="k">match</span> <span class="n">i</span> <span class="k">with</span>
<span class="bp">|</span> <span class="n">none</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">none</span>
<span class="bp">|</span> <span class="n">some</span> <span class="n">js</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">some</span> <span class="bp">⟨</span> <span class="n">js</span><span class="o">,</span> <span class="n">clip_correct</span> <span class="n">is</span> <span class="n">js</span> <span class="n">h</span> <span class="bp">⟩</span>
<span class="kn">end</span><span class="o">,</span>
<span class="n">this</span> <span class="n">rfl</span>
</pre></div>

#### [ Alexander Bentkamp (Sep 13 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133877252):
<p>Ok, I guess you are right. I'll stick to the tactic version. Anyway, good to know how the other options look like. Thanks!</p>

#### [ Johannes Hölzl (Sep 14 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133918080):
<p><span class="user-mention" data-user-id="129120">@Alexander Bentkamp</span>  for this concrete example you can use the following solution: </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">lookup</span> <span class="o">(</span><span class="n">is</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">option</span> <span class="o">{</span> <span class="n">js</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">is</span> <span class="n">js</span><span class="o">}</span> <span class="o">:=</span>
<span class="k">match</span> <span class="n">clip</span> <span class="n">is</span><span class="o">,</span> <span class="n">clip_correct</span> <span class="n">is</span> <span class="k">with</span>
<span class="bp">|</span> <span class="n">none</span><span class="o">,</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">none</span>
<span class="bp">|</span> <span class="n">some</span> <span class="n">js</span><span class="o">,</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">some</span> <span class="bp">⟨</span> <span class="n">js</span><span class="o">,</span> <span class="n">h</span> <span class="bp">_</span> <span class="n">rfl</span> <span class="bp">⟩</span>
<span class="kn">end</span>
</pre></div>


<p>The trick is to put the <code>clip_correct</code> into the parameters to <code>match</code>, with enough instantiations that <code>clip is</code> is found in it. But Rob is right, for more complicated things tactics will be easier.</p>

#### [ Kenny Lau (Sep 14 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133919060):
<p>interesting!</p>

#### [ Mario Carneiro (Sep 14 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133919298):
<p>By the way, Rob's last match example can also be written using the (rarely used) "return" argument of match (i.e. <code>match stuff : type with</code> syntax):</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">lookup</span> <span class="o">(</span><span class="n">is</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">option</span> <span class="o">{</span> <span class="n">js</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">is</span> <span class="n">js</span><span class="o">}</span> <span class="o">:=</span>
<span class="k">match</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">clip</span> <span class="n">is</span> <span class="bp">=</span> <span class="n">i</span> <span class="bp">→</span> <span class="n">option</span> <span class="o">{</span> <span class="n">js</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">is</span> <span class="n">js</span><span class="o">}</span> <span class="k">with</span>
<span class="bp">|</span> <span class="n">none</span><span class="o">,</span>    <span class="bp">_</span> <span class="o">:=</span> <span class="n">none</span>
<span class="bp">|</span> <span class="n">some</span> <span class="n">js</span><span class="o">,</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">some</span> <span class="bp">⟨</span> <span class="n">js</span><span class="o">,</span> <span class="n">clip_correct</span> <span class="n">is</span> <span class="n">js</span> <span class="n">h</span> <span class="bp">⟩</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Sep 14 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133919453):
<p>wow</p>

#### [ Kenny Lau (Sep 14 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133919461):
<p>this is amazing</p>

#### [ Kenny Lau (Sep 14 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133919463):
<p>I learn something new every day</p>

#### [ Alexander Bentkamp (Sep 14 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20hypothesis/near/133941546):
<p>cool! I went for Johannes's solution now.</p>


{% endraw %}
