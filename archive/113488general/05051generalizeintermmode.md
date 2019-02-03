---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/05051generalizeintermmode.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [generalize in term mode](https://leanprover-community.github.io/archive/113488general/05051generalizeintermmode.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Apr 21 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497304):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="n">def</span> <span class="n">generalize</span>
  <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">Π</span> <span class="n">x</span><span class="o">,</span> <span class="n">β</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">H</span> <span class="n">x</span>
</pre></div>


<p>I have made a <code>generalize</code> in term mode</p>

#### [ Kenny Lau (Apr 21 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497307):
<p>let's say this is the goal:</p>
<div class="codehilite"><pre><span></span><span class="n">refl_trans</span> <span class="n">red</span> <span class="n">x</span> <span class="n">z</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∃</span> <span class="o">(</span><span class="n">w</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">refl_trans</span> <span class="o">(</span><span class="n">refl_trans</span> <span class="n">red</span><span class="o">)</span> <span class="n">y</span> <span class="n">w</span> <span class="bp">∧</span> <span class="n">refl_trans</span> <span class="o">(</span><span class="n">refl_trans</span> <span class="n">red</span><span class="o">)</span> <span class="n">z</span> <span class="n">w</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Apr 21 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497313):
<p>doing <code>generalize z _</code> will give you this on the underscore:</p>

#### [ Kenny Lau (Apr 21 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497314):
<div class="codehilite"><pre><span></span><span class="err">⊢</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x_1</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span>
    <span class="n">refl_trans</span> <span class="n">red</span> <span class="n">x</span> <span class="n">x_1</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∃</span> <span class="o">(</span><span class="n">w</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">refl_trans</span> <span class="o">(</span><span class="n">refl_trans</span> <span class="n">red</span><span class="o">)</span> <span class="n">y</span> <span class="n">w</span> <span class="bp">∧</span> <span class="n">refl_trans</span> <span class="o">(</span><span class="n">refl_trans</span> <span class="n">red</span><span class="o">)</span> <span class="n">x_1</span> <span class="n">w</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Apr 21 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497315):
<p>is this a good idea?</p>

#### [ Kenny Lau (Apr 21 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497412):
<p>example:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="n">def</span> <span class="n">generalize</span>
  <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">Π</span> <span class="n">x</span><span class="o">,</span> <span class="n">β</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">H</span> <span class="n">x</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">red</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span>

<span class="kn">inductive</span> <span class="n">refl_trans</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">refl</span> <span class="o">{</span><span class="n">x</span><span class="o">}</span> <span class="o">:</span> <span class="n">refl_trans</span> <span class="n">x</span> <span class="n">x</span>
<span class="bp">|</span> <span class="n">step_trans</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">}</span> <span class="o">:</span> <span class="n">red</span> <span class="n">x</span> <span class="n">y</span> <span class="bp">→</span> <span class="n">refl_trans</span> <span class="n">y</span> <span class="n">z</span> <span class="bp">→</span> <span class="n">refl_trans</span> <span class="n">x</span> <span class="n">z</span>

<span class="bp">@</span><span class="o">[</span><span class="n">trans</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">refl_trans</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">refl_trans</span> <span class="n">red</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">refl_trans</span> <span class="n">red</span> <span class="n">y</span> <span class="n">z</span> <span class="bp">→</span> <span class="n">refl_trans</span> <span class="n">red</span> <span class="n">x</span> <span class="n">z</span> <span class="o">:=</span>
<span class="n">generalize</span> <span class="n">z</span> <span class="err">$</span> <span class="n">refl_trans</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">H</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">z</span> <span class="n">H</span><span class="o">,</span> <span class="n">H</span><span class="o">)</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="n">hxy</span> <span class="n">hyz</span> <span class="n">ih</span> <span class="n">w</span> <span class="n">hzw</span><span class="o">,</span>
<span class="n">refl_trans</span><span class="bp">.</span><span class="n">step_trans</span> <span class="n">hxy</span> <span class="err">$</span> <span class="n">ih</span> <span class="n">w</span> <span class="n">hzw</span>
</pre></div>

#### [ Kenny Lau (Apr 21 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497413):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> <span class="user-mention" data-user-id="110031">@Patrick Massot</span> what do you guys think?</p>

#### [ Patrick Massot (Apr 21 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497453):
<p>I'm afraid I still have to learn what the tactic mode <code>generalize</code> is good for</p>

#### [ Patrick Massot (Apr 21 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497454):
<p>I'm very curious because it came up a lot recently</p>

#### [ Patrick Massot (Apr 21 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497455):
<p>But I can't learn everything at the same time</p>

#### [ Kenny Lau (Apr 21 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497456):
<p>well you know how <code>induction</code> works with <code>generalizing</code> right</p>

#### [ Patrick Massot (Apr 21 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497457):
<p>No I don't</p>

#### [ Kenny Lau (Apr 21 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497462):
<p>hmm</p>

#### [ Patrick Massot (Apr 21 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497463):
<p>I only do induction on natural numbers</p>

#### [ Kenny Lau (Apr 21 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497464):
<p>so when you're proving that natural number addition is commutative</p>

#### [ Kenny Lau (Apr 21 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497465):
<p>you want to prove that x+y=y+x</p>

#### [ Kenny Lau (Apr 21 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497466):
<p>you induct on the proposition <code>\forall y, x+y=y+x</code> instead</p>

#### [ Kenny Lau (Apr 21 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497467):
<p>(and you prove the base case and inductive step both by induction)</p>

#### [ Kenny Lau (Apr 21 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497504):
<p>(I call this "double induction')</p>

#### [ Kenny Lau (Apr 21 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497509):
<p>the very action of moving the goalpost from <code>x+y=y+x</code> to <code>\forall y, x+y=y+x</code> is called generalizing</p>

#### [ Kenny Lau (Apr 21 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497518):
<p><a href="https://math.stackexchange.com/a/2438135/328173" target="_blank" title="https://math.stackexchange.com/a/2438135/328173">https://math.stackexchange.com/a/2438135/328173</a></p>

#### [ Kenny Lau (Apr 21 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497520):
<p>here is it in Fitch style (only part 1 is relevant)</p>

#### [ Simon Hudon (Apr 21 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497664):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> I'll have to get back to you a bit later. My nephew just arrived</p>

#### [ Kenny Lau (Apr 21 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497665):
<p>ok</p>

#### [ Patrick Massot (Apr 21 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497882):
<p>I can understand why you used your Kenny identity to post such an answer</p>

#### [ Patrick Massot (Apr 21 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497883):
<p>Thanks for the explanation</p>

#### [ Kenny Lau (Apr 21 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497888):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="n">def</span> <span class="n">generalize</span>
  <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">Π</span> <span class="n">x</span><span class="o">,</span> <span class="n">β</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">H</span> <span class="n">x</span>

<span class="kn">inductive</span> <span class="n">xnat</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">zero</span> <span class="o">:</span> <span class="n">xnat</span>
<span class="bp">|</span> <span class="n">succ</span> <span class="o">:</span> <span class="n">xnat</span> <span class="bp">→</span> <span class="n">xnat</span>

<span class="kn">namespace</span> <span class="n">xnat</span>

<span class="n">def</span> <span class="n">add</span> <span class="o">:</span> <span class="n">xnat</span> <span class="bp">→</span> <span class="n">xnat</span> <span class="bp">→</span> <span class="n">xnat</span>
<span class="bp">|</span> <span class="n">x</span> <span class="n">zero</span> <span class="o">:=</span> <span class="n">x</span>
<span class="bp">|</span> <span class="n">x</span> <span class="o">(</span><span class="n">succ</span> <span class="n">y</span><span class="o">)</span> <span class="o">:=</span> <span class="n">succ</span> <span class="err">$</span> <span class="n">add</span> <span class="n">x</span> <span class="n">y</span>

<span class="kn">theorem</span> <span class="n">add_comm</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">xnat</span><span class="o">}</span> <span class="o">:</span> <span class="n">add</span> <span class="n">x</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">add</span> <span class="n">y</span> <span class="n">x</span> <span class="o">:=</span>
<span class="n">generalize</span> <span class="n">y</span> <span class="err">$</span> <span class="n">xnat</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">x</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">y</span><span class="o">,</span> <span class="n">xnat</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">y</span> <span class="n">rfl</span> <span class="err">$</span>
     <span class="bp">λ</span> <span class="n">y</span> <span class="n">ih</span><span class="o">,</span> <span class="k">show</span> <span class="n">succ</span> <span class="bp">_</span> <span class="bp">=</span> <span class="n">succ</span> <span class="bp">_</span><span class="o">,</span> <span class="k">from</span> <span class="n">congr_arg</span> <span class="n">succ</span> <span class="n">ih</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">y</span> <span class="n">ih1</span> <span class="n">z</span><span class="o">,</span> <span class="n">xnat</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">z</span>
     <span class="o">(</span><span class="k">show</span> <span class="n">succ</span> <span class="bp">_</span> <span class="bp">=</span> <span class="n">succ</span> <span class="bp">_</span><span class="o">,</span> <span class="k">from</span> <span class="n">congr_arg</span> <span class="n">succ</span> <span class="err">$</span> <span class="n">ih1</span> <span class="n">zero</span><span class="o">)</span>
     <span class="o">(</span><span class="bp">λ</span> <span class="n">z</span> <span class="n">ih2</span><span class="o">,</span> <span class="n">congr_arg</span> <span class="n">succ</span> <span class="err">$</span> <span class="n">ih2</span><span class="bp">.</span><span class="n">trans</span> <span class="err">$</span> <span class="n">eq</span><span class="bp">.</span><span class="n">trans</span>
       <span class="o">(</span><span class="k">show</span> <span class="n">succ</span> <span class="bp">_</span> <span class="bp">=</span> <span class="n">succ</span> <span class="bp">_</span><span class="o">,</span> <span class="k">from</span> <span class="n">congr_arg</span> <span class="n">succ</span> <span class="o">(</span><span class="n">ih1</span> <span class="n">z</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span><span class="o">)</span> <span class="o">(</span><span class="n">ih1</span> <span class="err">$</span> <span class="n">succ</span> <span class="n">z</span><span class="o">)))</span>

<span class="kn">end</span> <span class="n">xnat</span>
</pre></div>

#### [ Kenny Lau (Apr 21 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497890):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> somehow it took me a long time to prove this</p>

#### [ Kenny Lau (Apr 21 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497891):
<p>but here you go</p>

#### [ Kenny Lau (Apr 21 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497892):
<p>why did I use my Kenny identity to post such an answer?</p>

#### [ Kenny Lau (Apr 21 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497894):
<p>and you can see that <code>generalize</code> is necessary because I used <code>ih1</code> twice</p>

#### [ Kenny Lau (Apr 21 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497934):
<p>I should make <code>show</code> a term-tactic</p>

#### [ Kenny Lau (Apr 21 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497935):
<p>well that won't really be necessary, forget that</p>

#### [ Kenny Lau (Apr 21 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497936):
<p>but I like my <code>generalize</code></p>

#### [ Kenny Lau (Apr 21 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497937):
<p>a tactic in term mode</p>

#### [ Kenny Lau (Apr 21 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497938):
<p>(a tactic, here, is one which converts your goal to something useful)</p>

#### [ Kenny Lau (Apr 21 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497945):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> do you think it is a good idea? I have too many <code>aux</code> theorems in my <code>free_group.lean</code> that can be eliminated by my new invention :P</p>

#### [ Kenny Lau (Apr 21 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497946):
<p>assuming that it is an invention</p>

#### [ Kenny Lau (Apr 21 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497988):
<p>bonus points! <code>generalize</code> also works as <code>revert</code></p>

#### [ Kenny Lau (Apr 21 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125497993):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="n">def</span> <span class="n">generalize</span>
  <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">Π</span> <span class="n">x</span><span class="o">,</span> <span class="n">β</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">H</span> <span class="n">x</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="n">generalize</span> <span class="n">H</span> <span class="bp">_</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">don&#39;t know how to synthesize placeholder</span>
<span class="cm">context:</span>
<span class="cm">x y : ℕ,</span>
<span class="cm">H : x = y</span>
<span class="cm">⊢ x = y → false</span>
<span class="cm">-/</span>
</pre></div>

#### [ Kenny Lau (Apr 21 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499063):
<p>I think I made a mistake. What I have built is really <code>revert</code></p>

#### [ Kenny Lau (Apr 21 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499065):
<p>Here's the real <code>generalize</code>:</p>

#### [ Kenny Lau (Apr 21 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499066):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="n">def</span> <span class="n">generalize</span>
  <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">Π</span> <span class="n">z</span><span class="o">,</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">z</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">z</span><span class="o">)</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">H</span> <span class="n">x</span> <span class="n">rfl</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="n">generalize</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">_</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">don&#39;t know how to synthesize placeholder</span>
<span class="cm">context:</span>
<span class="cm">m n : ℕ</span>
<span class="cm">⊢ ∀ (z : ℕ), m + n = z → z = 0</span>
<span class="cm">-/</span>
</pre></div>

#### [ Chris Hughes (Apr 21 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499110):
<p>I always wondered how to revert in term mode, however not sure I've ever had to do it.</p>

#### [ Kenny Lau (Apr 21 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499111):
<p>thanks for your appreciation</p>

#### [ Kenny Lau (Apr 21 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499112):
<p>so, for the sake of completeness:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="n">def</span> <span class="n">revert</span>
  <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">Π</span> <span class="n">x</span><span class="o">,</span> <span class="n">β</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">H</span> <span class="n">x</span>

<span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="n">def</span> <span class="n">generalize</span>
  <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">Π</span> <span class="n">z</span><span class="o">,</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">z</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">z</span><span class="o">)</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">H</span> <span class="n">x</span> <span class="n">rfl</span>
</pre></div>

#### [ Andrew Ashworth (Apr 21 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499155):
<p>in the old days when we didn't have a tactic mode you'd revert using clever <code>heq</code> tricks</p>

#### [ Chris Hughes (Apr 21 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499158):
<p>Usually I just do this.</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">add_comm</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">xnat</span><span class="o">}</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">y</span><span class="o">},</span> <span class="n">add</span> <span class="n">x</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">add</span> <span class="n">y</span> <span class="n">x</span> <span class="o">:=</span>
<span class="n">xnat</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">x</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">y</span><span class="o">,</span> <span class="n">xnat</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">y</span> <span class="n">rfl</span> <span class="err">$</span>
     <span class="bp">λ</span> <span class="n">y</span> <span class="n">ih</span><span class="o">,</span> <span class="k">show</span> <span class="n">succ</span> <span class="bp">_</span> <span class="bp">=</span> <span class="n">succ</span> <span class="bp">_</span><span class="o">,</span> <span class="k">from</span> <span class="n">congr_arg</span> <span class="n">succ</span> <span class="n">ih</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">y</span> <span class="n">ih1</span> <span class="n">z</span><span class="o">,</span> <span class="n">xnat</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">z</span>
     <span class="o">(</span><span class="k">show</span> <span class="n">succ</span> <span class="bp">_</span> <span class="bp">=</span> <span class="n">succ</span> <span class="bp">_</span><span class="o">,</span> <span class="k">from</span> <span class="n">congr_arg</span> <span class="n">succ</span> <span class="err">$</span> <span class="bp">@</span><span class="n">ih1</span> <span class="n">zero</span><span class="o">)</span>
     <span class="o">(</span><span class="bp">λ</span> <span class="n">z</span> <span class="n">ih2</span><span class="o">,</span> <span class="n">congr_arg</span> <span class="n">succ</span> <span class="err">$</span> <span class="n">ih2</span><span class="bp">.</span><span class="n">trans</span> <span class="err">$</span> <span class="n">eq</span><span class="bp">.</span><span class="n">trans</span>
       <span class="o">(</span><span class="k">show</span> <span class="n">succ</span> <span class="bp">_</span> <span class="bp">=</span> <span class="n">succ</span> <span class="bp">_</span><span class="o">,</span> <span class="k">from</span> <span class="n">congr_arg</span> <span class="n">succ</span> <span class="o">(</span><span class="bp">@</span><span class="n">ih1</span> <span class="n">z</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">ih1</span> <span class="err">$</span> <span class="n">succ</span> <span class="n">z</span><span class="o">)))</span>
</pre></div>

#### [ Kenny Lau (Apr 21 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499159):
<p>right, that's what I did in my free group file</p>

#### [ Kenny Lau (Apr 21 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499160):
<p>until I realized that I can build tactics in term mode</p>

#### [ Andrew Ashworth (Apr 21 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499199):
<p>does your generalize use <code>heq</code> under the hood?</p>

#### [ Chris Hughes (Apr 21 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499200):
<p>Are there any examples where you can't just do that?</p>

#### [ Kenny Lau (Apr 21 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499201):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> so my file has a lot of auxiliary theorems</p>

#### [ Kenny Lau (Apr 21 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499202):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">red</span><span class="bp">.</span><span class="n">trans</span><span class="bp">.</span><span class="n">aux</span> <span class="o">(</span><span class="n">H12</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L₁</span> <span class="n">L₂</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">L₃</span><span class="o">},</span> <span class="n">red</span> <span class="n">L₂</span> <span class="n">L₃</span> <span class="bp">→</span> <span class="n">red</span> <span class="n">L₁</span> <span class="n">L₃</span> <span class="o">:=</span>
<span class="n">red</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">H12</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">id</span><span class="o">)</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H1</span> <span class="n">H2</span> <span class="n">ih</span> <span class="n">L₃</span> <span class="n">H23</span><span class="o">,</span>
<span class="n">red</span><span class="bp">.</span><span class="n">step_trans</span> <span class="n">H1</span> <span class="err">$</span> <span class="n">ih</span> <span class="n">H23</span>

<span class="bp">@</span><span class="o">[</span><span class="n">trans</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">red</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">H12</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L₁</span> <span class="n">L₂</span><span class="o">)</span> <span class="o">(</span><span class="n">H23</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L₂</span> <span class="n">L₃</span><span class="o">)</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L₁</span> <span class="n">L₃</span> <span class="o">:=</span>
<span class="n">red</span><span class="bp">.</span><span class="n">trans</span><span class="bp">.</span><span class="n">aux</span> <span class="n">H12</span> <span class="n">H23</span>
</pre></div>

#### [ Kenny Lau (Apr 21 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499203):
<p>now I can do it in one go:</p>

#### [ Kenny Lau (Apr 21 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499204):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">trans</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">red</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">H12</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L₁</span> <span class="n">L₂</span><span class="o">)</span> <span class="o">(</span><span class="n">H23</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L₂</span> <span class="n">L₃</span><span class="o">)</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L₁</span> <span class="n">L₃</span> <span class="o">:=</span>
<span class="n">revert</span> <span class="n">H23</span> <span class="err">$</span> <span class="n">revert</span> <span class="n">L₃</span> <span class="err">$</span>
<span class="n">red</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">H12</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">id</span><span class="o">)</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H1</span> <span class="n">H2</span> <span class="n">ih</span> <span class="n">L₃</span> <span class="n">H23</span><span class="o">,</span>
<span class="n">red</span><span class="bp">.</span><span class="n">step_trans</span> <span class="n">H1</span> <span class="err">$</span> <span class="n">ih</span> <span class="bp">_</span> <span class="n">H23</span>
</pre></div>

#### [ Kenny Lau (Apr 21 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499210):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> are we talking about the same <code>heq</code>, i.e. the <code>heq</code> as in Lean? I don't know Coq at all. I showed you my code above though.</p>

#### [ Kenny Lau (Apr 21 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499211):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> not that I'm aware of</p>

#### [ Kenny Lau (Apr 21 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499212):
<p>I just built that an hour ago, I don't know everything about it</p>

#### [ Andrew Ashworth (Apr 21 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499213):
<p>yeah, because in Coq it'd be <code>JMeq</code>, heh</p>

#### [ Kenny Lau (Apr 21 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499214):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="n">def</span> <span class="n">revert</span>
  <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">Π</span> <span class="n">x</span><span class="o">,</span> <span class="n">β</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">H</span> <span class="n">x</span>

<span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="n">def</span> <span class="n">generalize</span>
  <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">Π</span> <span class="n">z</span><span class="o">,</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">z</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">z</span><span class="o">)</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">H</span> <span class="n">x</span> <span class="n">rfl</span>
</pre></div>

#### [ Kenny Lau (Apr 21 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499237):
<p>I don't see any <code>heq</code> here</p>

#### [ Andrew Ashworth (Apr 21 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499254):
<p>when you print an example that uses generalize</p>

#### [ Andrew Ashworth (Apr 21 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499255):
<p>do you get a <code>heq</code> term</p>

#### [ Andrew Ashworth (Apr 21 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499257):
<p>it may or may not, i'm just curious</p>

#### [ Chris Hughes (Apr 21 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499259):
<p>You can just do some extra lambdas. i.e<br>
<code>theorem red.trans.aux  : ∀ {L₃}, red L₁ L₂ → red L₂ L₃ → red L₁ L₃</code><br>
What's wrong with that?</p>

#### [ Kenny Lau (Apr 21 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499262):
<p>I need to rec on the first red</p>

#### [ Chris Hughes (Apr 21 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499269):
<p>I see. Makes a lot of sense then.</p>

#### [ Kenny Lau (Apr 21 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499270):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="n">def</span> <span class="n">revert</span>
  <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">Π</span> <span class="n">x</span><span class="o">,</span> <span class="n">β</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">H</span> <span class="n">x</span>

<span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="n">def</span> <span class="n">generalize</span>
  <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">Π</span> <span class="n">z</span><span class="o">,</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">z</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">z</span><span class="o">)</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">H</span> <span class="n">x</span> <span class="n">rfl</span>

<span class="kn">theorem</span> <span class="n">test</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="n">generalize</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">z</span> <span class="n">hz</span><span class="o">,</span> <span class="n">sorry</span>

<span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">all</span> <span class="n">true</span>
<span class="bp">#</span><span class="kn">print</span> <span class="n">test</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">theorem test : ∀ (m n : nat), @eq.{1} nat (@has_add.add.{0} nat nat.has_add m n) (@has_zero.zero.{0} nat nat.has_zero) :=</span>
<span class="cm">λ (m n : nat),</span>
<span class="cm">  @generalize.{1 0} nat (λ (_x : nat), @eq.{1} nat _x (@has_zero.zero.{0} nat nat.has_zero))</span>
<span class="cm">    (@has_add.add.{0} nat nat.has_add m n)</span>
<span class="cm">    (λ (z : nat) (hz : @eq.{1} nat (@has_add.add.{0} nat nat.has_add m n) z), sorry)</span>
<span class="cm">-/</span>
</pre></div>

#### [ Kenny Lau (Apr 21 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499271):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> is this what you're talking about?</p>

#### [ Chris Hughes (Apr 21 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499317):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> Are you talking about Kenny's generalize or tactics mode generalize?</p>

#### [ Kenny Lau (Apr 21 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499320):
<p>in that case:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="n">def</span> <span class="n">revert</span>
  <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">Π</span> <span class="n">x</span><span class="o">,</span> <span class="n">β</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">H</span> <span class="n">x</span>

<span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="n">def</span> <span class="n">generalize</span>
  <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">Π</span> <span class="n">z</span><span class="o">,</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">z</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">z</span><span class="o">)</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">H</span> <span class="n">x</span> <span class="n">rfl</span>

<span class="kn">theorem</span> <span class="n">test</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="n">generalize</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">z</span> <span class="n">hz</span><span class="o">,</span> <span class="n">sorry</span>

<span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">all</span> <span class="n">true</span>
<span class="bp">#</span><span class="kn">print</span> <span class="n">test</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">theorem test : ∀ (m n : nat), @eq.{1} nat (@has_add.add.{0} nat nat.has_add m n) (@has_zero.zero.{0} nat nat.has_zero) :=</span>
<span class="cm">λ (m n : nat),</span>
<span class="cm">  @generalize.{1 0} nat (λ (_x : nat), @eq.{1} nat _x (@has_zero.zero.{0} nat nat.has_zero))</span>
<span class="cm">    (@has_add.add.{0} nat nat.has_add m n)</span>
<span class="cm">    (λ (z : nat) (hz : @eq.{1} nat (@has_add.add.{0} nat nat.has_add m n) z), sorry)</span>
<span class="cm">-/</span>

<span class="kn">theorem</span> <span class="n">test&#39;</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">generalize</span> <span class="n">h</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">z</span><span class="o">,</span>
  <span class="n">admit</span>
<span class="kn">end</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">test&#39;</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">theorem test&#39; : ∀ (m n : nat), @eq.{1} nat (@has_add.add.{0} nat nat.has_add m n) (@has_zero.zero.{0} nat nat.has_zero) :=</span>
<span class="cm">λ (m n : nat),</span>
<span class="cm">  (λ (z : nat) (h : @eq.{1} nat (@has_add.add.{0} nat nat.has_add m n) z), sorry)</span>
<span class="cm">    (@has_add.add.{0} nat nat.has_add m n)</span>
<span class="cm">    (@rfl.{1} nat (@has_add.add.{0} nat nat.has_add m n))</span>
<span class="cm">-/</span>
</pre></div>

#### [ Andrew Ashworth (Apr 21 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499409):
<p>hm, interesting, i'd have to dig further when I have time</p>

#### [ Kenny Lau (Apr 21 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499416):
<p>thanks for your appreciation</p>

#### [ Andrew Ashworth (Apr 21 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499417):
<p><code>heq</code> is important when doing dependent case analysis, which is why i was expecting heq to show up in the term there somewhere</p>

#### [ Andrew Ashworth (Apr 21 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499418):
<p>it's probably buried in there somewhere... maybe... underneath one of the definitions</p>

#### [ Andrew Ashworth (Apr 21 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499419):
<p>it's quite a low-level idea</p>

#### [ Andrew Ashworth (Apr 21 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499421):
<p>or i could be really wrong about how lean works, and that also wouldn't surprise me</p>

#### [ Kenny Lau (Apr 21 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499422):
<p>so, eh, which one?</p>

#### [ Kenny Lau (Apr 21 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499463):
<p><code>eq</code> is already an inductive type</p>

#### [ Andrew Ashworth (Apr 21 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499464):
<p>i can't say because i'm a lean scrub</p>

#### [ Kenny Lau (Apr 21 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499465):
<p>it doesn't depend on <code>heq</code></p>

#### [ Kenny Lau (Apr 21 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499467):
<p>I don't think it uses <code>heq</code> anywhere</p>

#### [ Chris Hughes (Apr 21 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499522):
<p>Here's an alternative method</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">add_comm</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">xnat</span><span class="o">}</span> <span class="o">:</span> <span class="n">add</span> <span class="n">x</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">add</span> <span class="n">y</span> <span class="n">x</span> <span class="o">:=</span>
<span class="n">xnat</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">x</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">y</span><span class="o">,</span> <span class="n">xnat</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">y</span> <span class="n">rfl</span> <span class="err">$</span>
     <span class="bp">λ</span> <span class="n">y</span> <span class="n">ih</span><span class="o">,</span> <span class="k">show</span> <span class="n">succ</span> <span class="bp">_</span> <span class="bp">=</span> <span class="n">succ</span> <span class="bp">_</span><span class="o">,</span> <span class="k">from</span> <span class="n">congr_arg</span> <span class="n">succ</span> <span class="n">ih</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">y</span> <span class="n">ih1</span> <span class="n">z</span><span class="o">,</span> <span class="n">xnat</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">z</span>
     <span class="o">(</span><span class="k">show</span> <span class="n">succ</span> <span class="bp">_</span> <span class="bp">=</span> <span class="n">succ</span> <span class="bp">_</span><span class="o">,</span> <span class="k">from</span> <span class="n">congr_arg</span> <span class="n">succ</span> <span class="err">$</span> <span class="bp">@</span><span class="n">ih1</span> <span class="n">zero</span><span class="o">)</span>
     <span class="o">(</span><span class="bp">λ</span> <span class="n">z</span> <span class="n">ih2</span><span class="o">,</span> <span class="n">congr_arg</span> <span class="n">succ</span> <span class="err">$</span> <span class="n">ih2</span><span class="bp">.</span><span class="n">trans</span> <span class="err">$</span> <span class="n">eq</span><span class="bp">.</span><span class="n">trans</span>
       <span class="o">(</span><span class="k">show</span> <span class="n">succ</span> <span class="bp">_</span> <span class="bp">=</span> <span class="n">succ</span> <span class="bp">_</span><span class="o">,</span> <span class="k">from</span> <span class="n">congr_arg</span> <span class="n">succ</span> <span class="o">(</span><span class="bp">@</span><span class="n">ih1</span> <span class="n">z</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">ih1</span> <span class="err">$</span> <span class="n">succ</span> <span class="n">z</span><span class="o">)))</span> <span class="n">y</span>
</pre></div>

#### [ Andrew Ashworth (Apr 21 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499524):
<p>sure, and why that might be is interesting to me, most other tactics in coq that do this sort of thing use <code>heq</code></p>

#### [ Andrew Ashworth (Apr 21 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499525):
<p><a href="https://coq.inria.fr/refman/proof-engine/detailed-tactic-examples.html" target="_blank" title="https://coq.inria.fr/refman/proof-engine/detailed-tactic-examples.html">https://coq.inria.fr/refman/proof-engine/detailed-tactic-examples.html</a></p>

#### [ Kenny Lau (Apr 21 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499568):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> interesting. usually it fails if I put <code>y</code> at the end</p>

#### [ Kenny Lau (Apr 21 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499571):
<p>I still like my method more :P</p>

#### [ Chris Hughes (Apr 21 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499572):
<p>I was expecting it not to work.</p>

#### [ Kenny Lau (Apr 21 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499574):
<p>did you do anything more than my eyes could see</p>

#### [ Kenny Lau (Apr 21 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499575):
<p>I can't really tell if you changed anything in the middle</p>

#### [ Chris Hughes (Apr 21 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499576):
<p>No.</p>

#### [ Kenny Lau (Apr 21 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125499579):
<p>very curious indeed</p>

#### [ Kenny Lau (Apr 21 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125500272):
<p>more examples: <a href="https://github.com/kckennylau/Lean/commit/c9d0c76f7d807f48f4cea0c6043bcc9caf48e09a#diff-fdee7d198ee1f7316cba5649313e084a" target="_blank" title="https://github.com/kckennylau/Lean/commit/c9d0c76f7d807f48f4cea0c6043bcc9caf48e09a#diff-fdee7d198ee1f7316cba5649313e084a">https://github.com/kckennylau/Lean/commit/c9d0c76f7d807f48f4cea0c6043bcc9caf48e09a#diff-fdee7d198ee1f7316cba5649313e084a</a></p>

#### [ Patrick Massot (Apr 21 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125500481):
<p>Congratulations!</p>

#### [ Patrick Massot (Apr 21 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125500485):
<p>Two docstrings is a very good start!</p>

#### [ Kenny Lau (Apr 21 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125500486):
<p>:P</p>

#### [ Kenny Lau (Apr 21 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125500488):
<p>I was making docstrings</p>

#### [ Kenny Lau (Apr 21 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125500490):
<p>and then I got carried away by <code>revert</code> and <code>generalize</code></p>

#### [ Kenny Lau (Apr 22 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521584):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> do you like this?</p>

#### [ Kenny Lau (Apr 22 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521591):
<p>recap:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="n">def</span> <span class="n">revert</span>
  <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">Π</span> <span class="n">x</span><span class="o">,</span> <span class="n">β</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">H</span> <span class="n">x</span>

<span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="n">def</span> <span class="n">generalize</span>
  <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">Π</span> <span class="n">z</span><span class="o">,</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">z</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">z</span><span class="o">)</span> <span class="bp">→</span> <span class="n">β</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">H</span> <span class="n">x</span> <span class="n">rfl</span>
</pre></div>

#### [ Mario Carneiro (Apr 22 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521631):
<p>I'm not sure I buy the particular applications you've used it for, but this seems okay for <code>logic.basic</code></p>

#### [ Mario Carneiro (Apr 22 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521632):
<p>probably should be <code>reducible</code></p>

#### [ Kenny Lau (Apr 22 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521633):
<p>woohoo, tactics in term mode</p>

#### [ Mario Carneiro (Apr 22 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521638):
<p>I mean, you can use <code>match</code> to the same effect</p>

#### [ Mario Carneiro (Apr 22 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521640):
<p>but I usually just set up my intros in the right order so this isn't needed</p>

#### [ Kenny Lau (Apr 22 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521641):
<p>right, but setting up them make for a bunch of auxiliary theorems</p>

#### [ Mario Carneiro (Apr 22 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521682):
<p>not in my experience</p>

#### [ Kenny Lau (Apr 22 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521683):
<p><a href="https://github.com/kckennylau/Lean/commit/c9d0c76f7d807f48f4cea0c6043bcc9caf48e09a#diff-fdee7d198ee1f7316cba5649313e084a" target="_blank" title="https://github.com/kckennylau/Lean/commit/c9d0c76f7d807f48f4cea0c6043bcc9caf48e09a#diff-fdee7d198ee1f7316cba5649313e084a">https://github.com/kckennylau/Lean/commit/c9d0c76f7d807f48f4cea0c6043bcc9caf48e09a#diff-fdee7d198ee1f7316cba5649313e084a</a></p>

#### [ Kenny Lau (Apr 22 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521684):
<p>here</p>

#### [ Mario Carneiro (Apr 22 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521691):
<p>why don't you use the equation compiler?</p>

#### [ Kenny Lau (Apr 22 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521693):
<p>that also needs to be auxiliary</p>

#### [ Mario Carneiro (Apr 22 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521694):
<p>for <code>red.trans</code></p>

#### [ Kenny Lau (Apr 22 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521695):
<p>because <code>rec_on</code> is shorter</p>

#### [ Mario Carneiro (Apr 22 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521739):
<p>eww</p>

#### [ Kenny Lau (Apr 22 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521740):
<p>I thought someone likes short proofs</p>

#### [ Mario Carneiro (Apr 22 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521742):
<p>I like straightforward proofs</p>

#### [ Mario Carneiro (Apr 22 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521749):
<p>the equation compiler makes it really clear how an induction proceeds, and what is the IH</p>

#### [ Mario Carneiro (Apr 22 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521751):
<p>plus, I very much doubt you recouped the loss of having to state an auxiliary</p>

#### [ Mario Carneiro (Apr 22 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521794):
<p>We haven't talked about it much since they appear to be going extinct, but it's possible to write brittle term proofs too</p>

#### [ Mario Carneiro (Apr 22 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521797):
<p>this was a big problem in lean 2</p>

#### [ Mario Carneiro (Apr 22 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize%20in%20term%20mode/near/125521838):
<p>when you do a proof with lots of omitted type information relying on lean to pick up the pieces, if something changes in the unification algorithm or something it can be very difficult to understand the broken proof</p>


{% endraw %}
