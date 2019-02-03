---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24153tidybug.html
---

## Stream: [general](index.html)
### Topic: [tidy bug](24153tidybug.html)

---


{% raw %}
#### [ Patrick Massot (Oct 02 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060203):
<p>Can someone try</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">tidy</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">y</span> <span class="o">:</span> <span class="n">Y</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span> <span class="n">f</span><span class="o">(</span><span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">∃</span> <span class="n">g</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">X</span><span class="o">,</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">id</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">classical</span><span class="bp">.</span><span class="n">axiom_of_choice</span> <span class="n">h</span> <span class="k">with</span> <span class="n">g</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">tidy</span><span class="o">,</span>
 <span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Oct 02 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060275):
<p>Here it says <code>no goals</code> after <code>tidy</code> but red-squiggle <code>example</code> with <code>type mismatch at application  g a term  a has type  Y_1 but is expected to have type   Y types contain aliased name(s): Y remark: the tactic `dedup` can be used to rename aliases</code></p>

#### [ Bryan Gin-ge Chen (Oct 02 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060435):
<blockquote>
<p>Here it says <code>no goals</code> after <code>tidy</code> but red-squiggle <code>example</code> with <code>type mismatch at application  g a term  a has type  Y_1 but is expected to have type   Y types contain aliased name(s): Y remark: the tactic `dedup` can be used to rename aliases</code></p>
</blockquote>
<p>I get the same.</p>

#### [ Patrick Massot (Oct 02 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060519):
<p>Let's wait for <span class="user-mention" data-user-id="110087">@Scott Morrison</span> to wake up, or finish lunch, or whatever it's time to do in Australia</p>

#### [ Bryan Gin-ge Chen (Oct 02 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060631):
<p>Here's the trace:</p>
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm"> `tidy` says -/</span>
<span class="n">dsimp</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
<span class="n">fsplit</span><span class="o">,</span>
<span class="n">work_on_goal</span> <span class="mi">0</span> <span class="o">{</span> <span class="n">intros</span> <span class="n">a</span> <span class="o">},</span>
<span class="n">work_on_goal</span> <span class="mi">1</span> <span class="o">{</span> <span class="n">ext1</span><span class="o">,</span> <span class="n">dsimp</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span> <span class="n">solve_by_elim</span> <span class="o">}</span>
</pre></div>

#### [ Patrick Massot (Oct 02 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060646):
<p>I'm working on that demo file we discussed earlier, trying to see what general purpose automation can do what. The problem with magic is it's somewhat unpredictable. It seems <code>finish</code> is pretty powerful in those example, but I'd like to understand when <code>tidy</code> or <code>tauto</code> actually also work (or even work better)</p>

#### [ Patrick Massot (Oct 02 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060745):
<p>Good idea Bryan!</p>

#### [ Bryan Gin-ge Chen (Oct 02 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060767):
<p>Not sure if I misunderstand the meaning of the trace, but throwing it in as a proof fails at the first <code>dsimp</code></p>

#### [ Patrick Massot (Oct 02 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060783):
<p>It's very strange to follow, it seems hopeless and then <code>solve_by_elim</code> pretends to get rid of all meta-vars and do the job</p>

#### [ Patrick Massot (Oct 02 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060810):
<p>here I get exactly the same result as with tidy itself</p>

#### [ Patrick Massot (Oct 02 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060834):
<p>google says Scott may be sleeping</p>

#### [ Bryan Gin-ge Chen (Oct 02 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060897):
<p>I see this:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">tidy</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">y</span> <span class="o">:</span> <span class="n">Y</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span> <span class="n">f</span><span class="o">(</span><span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">∃</span> <span class="n">g</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">X</span><span class="o">,</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">id</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">dsimp</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>  <span class="c1">-- squiggly line under dsimp</span>
<span class="c">/-</span><span class="cm"> Tactic State</span>
<span class="cm">X Y : Type,</span>
<span class="cm">f : X → Y,</span>
<span class="cm">h : ∀ (y : Y), ∃ (x : X), f x = y</span>
<span class="cm">⊢ ∃ (g : Y → X), f ∘ g = id</span>
<span class="cm">scratch.lean:14:0: error</span>
<span class="cm">dsimplify tactic failed to simplify</span>
<span class="cm">state:</span>
<span class="cm">⊢ ∀ (X Y : Type) (f : X → Y), (∀ (y : Y), ∃ (x : X), f x = y) → (∃ (g : Y → X), f ∘ g = id) -/</span>
<span class="n">fsplit</span><span class="o">,</span>
<span class="n">work_on_goal</span> <span class="mi">0</span> <span class="o">{</span> <span class="n">intros</span> <span class="n">a</span> <span class="o">},</span>
<span class="n">work_on_goal</span> <span class="mi">1</span> <span class="o">{</span> <span class="n">ext1</span><span class="o">,</span> <span class="n">dsimp</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span> <span class="n">solve_by_elim</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Oct 02 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060910):
<p>you erased too much</p>

#### [ Patrick Massot (Oct 02 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060915):
<p>the choice idea is required</p>

#### [ Bryan Gin-ge Chen (Oct 02 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060932):
<p>Oops!</p>

#### [ Bryan Gin-ge Chen (Oct 02 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135061725):
<p>Yes, now I see the same.  </p>
<p>Nothing seems strange with the intermediate tactic states. Is there a way to use the <code>discharger</code> option for <code>solve_by_elim</code> to make it spit out what it's doing at each stage?</p>

#### [ Patrick Massot (Oct 02 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135061835):
<p>How is it possible that none of our general purpose weapon can kill</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">id</span> <span class="o">)</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">y</span>
</pre></div>

#### [ Kenny Lau (Oct 02 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135061909):
<p>I don't use weapons :P</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">id</span> <span class="o">)</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">y</span> <span class="o">:=</span> <span class="n">congr_fun</span> <span class="n">h</span> <span class="n">y</span>
</pre></div>

#### [ Patrick Massot (Oct 02 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135061953):
<p>Kenny, this is exactly what I did at <a href="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/demo.lean#L60" target="_blank" title="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/demo.lean#L60">https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/demo.lean#L60</a> but I'm trying to rewrite this file using automation, for comparison</p>

#### [ Patrick Massot (Oct 02 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062010):
<p>I guess this is again because tactic writers don't like function equalities, especially with compositions</p>

#### [ Bryan Gin-ge Chen (Oct 02 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062015):
<p>Replacing <code>solve_by_elim</code> with <code>apply_assumption</code> gives the same strange behavior.</p>

#### [ Rob Lewis (Oct 02 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062022):
<p>Higher order reasoning is hard!</p>

#### [ Patrick Massot (Oct 02 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062062):
<p><code>finish</code> and its friends could try to turn each function equality assumption into a forall</p>

#### [ Patrick Massot (Oct 02 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062136):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">z</span><span class="o">,</span> <span class="o">(</span><span class="n">f</span> <span class="err">∘</span> <span class="n">g</span><span class="o">)</span> <span class="n">z</span> <span class="bp">=</span> <span class="n">id</span> <span class="n">z</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">Y</span><span class="o">):</span>
  <span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">finish</span>
</pre></div>


<p>does work</p>

#### [ Patrick Massot (Oct 02 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062179):
<p>Of course rewriting <code>h</code> like this is the most un-mathematical thing you could see</p>

#### [ Kenny Lau (Oct 02 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062206):
<blockquote>
<p><code>finish</code> and its friends</p>
</blockquote>

#### [ Patrick Massot (Oct 02 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062395):
<p>its friends are <code>tauto</code> and <code>tidy</code></p>

#### [ Bryan Gin-ge Chen (Oct 02 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062619):
<p>Could it be that there's something strange happening with <code>work_on_goal</code>? The following works:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">tidy</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">y</span> <span class="o">:</span> <span class="n">Y</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span> <span class="n">f</span><span class="o">(</span><span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">∃</span> <span class="n">g</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">X</span><span class="o">,</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">id</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">classical</span><span class="bp">.</span><span class="n">axiom_of_choice</span> <span class="n">h</span> <span class="k">with</span> <span class="n">g</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">dsimp</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
  <span class="n">fsplit</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="n">g</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">ext1</span><span class="o">,</span>
  <span class="n">dsimp</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
  <span class="n">apply_assumption</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Bryan Gin-ge Chen (Oct 02 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062701):
<p>Compare this, which gives the same <code>no goals</code> + weird error as the initial <code>tidy</code> call:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">tidy</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">y</span> <span class="o">:</span> <span class="n">Y</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span> <span class="n">f</span><span class="o">(</span><span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">∃</span> <span class="n">g</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">X</span><span class="o">,</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">id</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">classical</span><span class="bp">.</span><span class="n">axiom_of_choice</span> <span class="n">h</span> <span class="k">with</span> <span class="n">g</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">dsimp</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
  <span class="n">fsplit</span><span class="o">,</span>
  <span class="c1">--{ exact g },</span>
  <span class="n">work_on_goal</span> <span class="mi">1</span> <span class="o">{</span> <span class="n">ext1</span><span class="o">,</span>
  <span class="n">dsimp</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
  <span class="n">apply_assumption</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Oct 02 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062782):
<p>interesting</p>

#### [ Patrick Massot (Oct 02 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062942):
<p>Even better:</p>
<div class="codehilite"><pre><span></span><span class="w"> </span><span class="n">example</span><span class="w"> </span><span class="p">(</span><span class="n">X</span><span class="w"> </span><span class="n">Y</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="n">Type</span><span class="p">)</span><span class="w"> </span><span class="p">(</span><span class="n">f</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="n">X</span><span class="w"> </span><span class="err">→</span><span class="w"> </span><span class="n">Y</span><span class="p">)</span><span class="w"> </span><span class="p">(</span><span class="n">h</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">∀</span><span class="w"> </span><span class="n">y</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="n">Y</span><span class="p">,</span><span class="w"> </span><span class="err">∃</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="n">X</span><span class="p">,</span><span class="w"> </span><span class="n">f</span><span class="p">(</span><span class="n">x</span><span class="p">)</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">y</span><span class="p">)</span><span class="w"> </span><span class="p">:</span><span class="w"></span>
<span class="w">  </span><span class="p">(</span><span class="err">∃</span><span class="w"> </span><span class="n">g</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="n">Y</span><span class="w"> </span><span class="err">→</span><span class="w"> </span><span class="n">X</span><span class="p">,</span><span class="w"> </span><span class="n">f</span><span class="w"> </span><span class="err">∘</span><span class="w"> </span><span class="n">g</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">id</span><span class="p">)</span><span class="w"> </span><span class="p">:</span><span class="o">=</span><span class="w"></span>
<span class="n">begin</span><span class="w"></span>
<span class="w">  </span><span class="n">cases</span><span class="w"> </span><span class="n">classical.axiom_of_choice</span><span class="w"> </span><span class="n">h</span><span class="w"> </span><span class="k">with</span><span class="w"> </span><span class="n">g</span><span class="w"> </span><span class="n">H</span><span class="p">,</span><span class="w"></span>
<span class="w">  </span><span class="n">dsimp</span><span class="w"> </span><span class="n">at</span><span class="w"> </span><span class="o">*</span><span class="p">,</span><span class="w"></span>
<span class="w">  </span><span class="n">fsplit</span><span class="p">,</span><span class="w"></span>
<span class="w">  </span><span class="p">{</span><span class="w"> </span><span class="n">exact</span><span class="w"> </span><span class="n">g</span><span class="w"> </span><span class="p">},</span><span class="w"></span>
<span class="w">  </span><span class="n">work_on_goal</span><span class="mi"> 0</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="n">ext1</span><span class="p">,</span><span class="w"></span>
<span class="w">  </span><span class="n">dsimp</span><span class="w"> </span><span class="n">at</span><span class="w"> </span><span class="o">*</span><span class="p">,</span><span class="w"></span>
<span class="w">  </span><span class="n">apply_assumption</span><span class="w"> </span><span class="p">}</span><span class="w"></span>
<span class="n">end</span><span class="w"></span>
</pre></div>


<p>works!</p>

#### [ Patrick Massot (Oct 02 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135063047):
<p>but actually this is getting far away from what tidy suggested</p>

#### [ Bryan Gin-ge Chen (Oct 02 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135063189):
<p><a href="https://github.com/leanprover/mathlib/blob/decb0302869ac70069ba26708367e460695683cb/tactic/chain.lean#L44" target="_blank" title="https://github.com/leanprover/mathlib/blob/decb0302869ac70069ba26708367e460695683cb/tactic/chain.lean#L44">Here's</a> <code>work_on_goal</code>. If I had to guess, there's something wrong in here, possibly in handling what happens if a goal gets solved.</p>

#### [ Bryan Gin-ge Chen (Oct 02 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135065300):
<p>I think the problem is that when <code>apply_assumption</code> kills off a goal, it does not return properly to <code>work_on_goal</code>. Then lean thinks it has finished, but in reality there are more goals that <code>work_on_goal</code> just temporarily deleted. There are no issues when <code>exact g</code> finishes a goal inside <code>work_on_goal</code>, so there's something going on with this particular interaction.</p>

#### [ Bryan Gin-ge Chen (Oct 02 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135065407):
<p><code>apply_assumption</code> is <a href="https://github.com/leanprover/mathlib/blob/c2df6b1f3f62575649dbe128a2c5fc9e2de26ffb/tactic/basic.lean#L422" target="_blank" title="https://github.com/leanprover/mathlib/blob/c2df6b1f3f62575649dbe128a2c5fc9e2de26ffb/tactic/basic.lean#L422">here</a>, but it's too monad-y for me to make sense of at the moment.</p>

#### [ Simon Hudon (Oct 02 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135065867):
<p>What problem are you looking for?</p>

#### [ Bryan Gin-ge Chen (Oct 03 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135066963):
<p>Patrick started this thread with <a href="#narrow/stream/113488-general/subject/tidy.20bug/near/135060203" title="#narrow/stream/113488-general/subject/tidy.20bug/near/135060203">an example</a> where <code>tidy</code> leaves the tactic state with <code>no goals</code> but there is a strange error.</p>
<p>I'm proposing that the root cause of this is due to <code>apply_assumption</code> not returning properly to <code>work_on_goal</code>.</p>

#### [ Scott Morrison (Oct 03 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135067028):
<p>Thanks for these bug reports. I probably won't have a chance to work on it until the weekend.</p>

#### [ Kenny Lau (Oct 03 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135068289):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">z</span><span class="o">,</span> <span class="o">(</span><span class="n">f</span> <span class="err">∘</span> <span class="n">g</span><span class="o">)</span> <span class="n">z</span> <span class="bp">=</span> <span class="n">id</span> <span class="n">z</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">Y</span><span class="o">):</span>
  <span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">y</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">tauto</span>
</pre></div>

#### [ Kenny Lau (Oct 03 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135068292):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span></p>

#### [ Patrick Massot (Oct 03 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135085753):
<p>Thanks Kenny, but this is the version I don't want, because <code>h</code> is stated un-mathematically</p>


{% endraw %}
