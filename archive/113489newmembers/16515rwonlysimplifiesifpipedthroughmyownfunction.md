---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/16515rwonlysimplifiesifpipedthroughmyownfunction.html
---

## Stream: [new members](index.html)
### Topic: [rw only simplifies if piped through my own function](16515rwonlysimplifiesifpipedthroughmyownfunction.html)

---


{% raw %}
#### [ Tobias Grosser (Sep 07 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491472):
<p>My first beginners question. I tampered with this since a while, but maybe somebody has a quick explanation for this:</p>
<p><a href="https://gist.github.com/tobig/92b17c8cac76fd07e1537c9131a25260" target="_blank" title="https://gist.github.com/tobig/92b17c8cac76fd07e1537c9131a25260">https://gist.github.com/tobig/92b17c8cac76fd07e1537c9131a25260</a></p>

#### [ Tobias Grosser (Sep 07 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491484):
<p>Rewriting with my own theorem works well, but if I directly use imp_iff_not_or things break</p>

#### [ Tobias Grosser (Sep 07 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491491):
<p>with "function expected at"</p>

#### [ Tobias Grosser (Sep 07 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491541):
<p>Probably a beginners mistake. It seems my declaration introduces some additional information which help the proof go through.</p>

#### [ Simon Hudon (Sep 07 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491641):
<p>If you check the definition of <code>imp_iff_not_or</code>, (type <code>#check imp_iff_not_or</code> in your Lean buffer), you see that it does not take <em>explicit</em> arguments, only implicit ones</p>

#### [ Simon Hudon (Sep 07 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491663):
<p>That means that they are meant to be inferred. But if you want to specify then, you can write <code>@imp_iff_not_or</code> and then you have to provide an argument for the implicit and explicit arguments.</p>

#### [ Simon Hudon (Sep 07 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491725):
<p>For reference:</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">check</span> <span class="n">imp_iff_not_or</span>
<span class="c1">-- imp_iff_not_or : ?M_1 → ?M_2 ↔ ¬?M_1 ∨ ?M_2</span>
<span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">imp_iff_not_or</span>
<span class="c1">-- imp_iff_not_or : ∀ {a b : Prop} [_inst_1 : decidable a], a → b ↔ ¬a ∨ b</span>
</pre></div>


<p>The curly brackets around <code>a</code> and <code>b</code> means that they are implicit arguments. The square brackets around <code>decidable a</code> means that it's a type class instance.</p>

#### [ Tobias Grosser (Sep 07 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491802):
<p><a href="https://leanprover.github.io/theorem_proving_in_lean/dependent_type_theory.html#implicit-arguments" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/dependent_type_theory.html#implicit-arguments">https://leanprover.github.io/theorem_proving_in_lean/dependent_type_theory.html#implicit-arguments</a></p>

#### [ Tobias Grosser (Sep 07 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491841):
<p>Works flawless. Need to read a little bit more on this.</p>

#### [ Tobias Grosser (Sep 07 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491845):
<p>Thanks for the quick help.</p>

#### [ Simon Hudon (Sep 07 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491851):
<p>No worries :)</p>

#### [ Tobias Grosser (Sep 07 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491931):
<p>One last question:</p>

#### [ Tobias Grosser (Sep 07 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491932):
<p>My proof looks now like this:</p>

#### [ Tobias Grosser (Sep 07 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491934):
<div class="codehilite"><pre><span></span>        ((B → C) → (¬(A → C)     ∧ ¬(A ∨ B)))
      = ((B → C) → (¬(¬A ∨ C)    ∧ ¬(A ∨ B)))         : by rw @imp_iff_not_or A C
  ... = ((B → C) → ((¬(¬A) ∧ ¬C) ∧ ¬(A ∨ B)))         : by rw not_or_distrib
  ... = ((B → C) → ((¬(¬A) ∧ ¬C) ∧ (¬A ∧ ¬B)))        : by rw not_or_distrib
  ... = ((B → C) → ((A ∧ ¬C) ∧ (¬A ∧ ¬B)))            : by rw not_not
  ... = ((B → C) → ((A ∧ ¬C) ∧ ¬A ∧ ¬B))              : by rw and_assoc
  ... = ((B → C) → ((¬C ∧ A) ∧ ¬A ∧ ¬B))              : by rw and_comm (A) (¬C)
  ... = ((B → C) → (¬C ∧ A ∧ ¬A ∧ ¬B))                : by rw and_assoc
  ... = ((B → C) → (¬C ∧ (A ∧ ¬A) ∧ ¬B))              : by rw and_assoc
  ... = ((B → C) → (¬C ∧ ¬ B ∧ (A ∧ ¬A)))             : by rw and_comm (¬ B) (A ∧ ¬A)
  ... = ((B → C) → (¬C ∧ ¬ B ∧ false ))               : by rw and_not_self_iff A
  ... = ((B → C) → ((¬C) ∧ false ))                   : by rw and_false
  ... = ((B → C) → (false))                           : by rw and_false
  ... = (¬(B → C) ∨ false)                            : by rw imp_iff_not_or
  ... = ¬(B → C)                                      : by rw or_false
  ... = ¬(¬B ∨ C)                                     : by rw imp_iff_not_or 
  ... = ((¬¬B) ∧ (¬C))                                : by rw not_or_distrib
  ... = (B ∧ ¬C)                                      : by rw not_not
</pre></div>

#### [ Tobias Grosser (Sep 07 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491975):
<p>It seems only imp_iff_not_or needs the '@'. All other functions are OK with explicit arguments (if given).</p>

#### [ Tobias Grosser (Sep 07 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491980):
<p>Is there some schema when theorems take explicit arguments in mathlib?</p>

#### [ Mario Carneiro (Sep 07 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133491999):
<p>most iff theorems have implicit args</p>

#### [ Kenny Lau (Sep 07 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492001):
<p><code>rw ← imp_iff_not_or</code></p>

#### [ Kenny Lau (Sep 07 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492009):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">logic</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span> <span class="bp">_</span> <span class="bp">=</span> <span class="bp">_</span> <span class="o">:=</span>
<span class="k">calc</span>
        <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">¬</span><span class="o">(</span><span class="n">A</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span>     <span class="bp">∧</span> <span class="bp">¬</span><span class="o">(</span><span class="n">A</span> <span class="bp">∨</span> <span class="n">B</span><span class="o">)))</span>
      <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">¬</span><span class="o">(</span><span class="bp">¬</span><span class="n">A</span> <span class="bp">∨</span> <span class="n">C</span><span class="o">)</span>    <span class="bp">∧</span> <span class="bp">¬</span><span class="o">(</span><span class="n">A</span> <span class="bp">∨</span> <span class="n">B</span><span class="o">)))</span>         <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="err">←</span> <span class="n">imp_iff_not_or</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">((</span><span class="bp">¬</span><span class="o">(</span><span class="bp">¬</span><span class="n">A</span><span class="o">)</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">C</span><span class="o">)</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="o">(</span><span class="n">A</span> <span class="bp">∨</span> <span class="n">B</span><span class="o">)))</span>         <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">not_or_distrib</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">((</span><span class="bp">¬</span><span class="o">(</span><span class="bp">¬</span><span class="n">A</span><span class="o">)</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">C</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">¬</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">B</span><span class="o">)))</span>        <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">not_or_distrib</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">((</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">C</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">¬</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">B</span><span class="o">)))</span>            <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">not_not</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">((</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">C</span><span class="o">)</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">B</span><span class="o">))</span>              <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">and_assoc</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">((</span><span class="bp">¬</span><span class="n">C</span> <span class="bp">∧</span> <span class="n">A</span><span class="o">)</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">B</span><span class="o">))</span>              <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">and_comm</span> <span class="o">(</span><span class="n">A</span><span class="o">)</span> <span class="o">(</span><span class="bp">¬</span><span class="n">C</span><span class="o">)</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">¬</span><span class="n">C</span> <span class="bp">∧</span> <span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">B</span><span class="o">))</span>                <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">and_assoc</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">¬</span><span class="n">C</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">A</span><span class="o">)</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">B</span><span class="o">))</span>              <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">and_assoc</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">¬</span><span class="n">C</span> <span class="bp">∧</span> <span class="bp">¬</span> <span class="n">B</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">A</span><span class="o">)))</span>             <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">and_comm</span> <span class="o">(</span><span class="bp">¬</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">A</span><span class="o">)</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">¬</span><span class="n">C</span> <span class="bp">∧</span> <span class="bp">¬</span> <span class="n">B</span> <span class="bp">∧</span> <span class="n">false</span> <span class="o">))</span>               <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">and_not_self_iff</span> <span class="n">A</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">((</span><span class="bp">¬</span><span class="n">C</span><span class="o">)</span> <span class="bp">∧</span> <span class="n">false</span> <span class="o">))</span>                   <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">and_false</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">false</span><span class="o">))</span>                           <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">and_false</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">¬</span><span class="o">(</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">∨</span> <span class="n">false</span><span class="o">)</span>                            <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">imp_iff_not_or</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="bp">¬</span><span class="o">(</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span>                                      <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">or_false</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="bp">¬</span><span class="o">(</span><span class="bp">¬</span><span class="n">B</span> <span class="bp">∨</span> <span class="n">C</span><span class="o">)</span>                                     <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">imp_iff_not_or</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="bp">¬¬</span><span class="n">B</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">¬</span><span class="n">C</span><span class="o">))</span>                                <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">not_or_distrib</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">(</span><span class="n">B</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">C</span><span class="o">)</span>                                      <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">not_not</span>
</pre></div>

#### [ Tobias Grosser (Sep 07 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492210):
<p>Is there a specific reason why 'iff' terms have implict  arguments and others not?</p>

#### [ Kenny Lau (Sep 07 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492230):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">logic</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span> <span class="bp">_</span> <span class="bp">=</span> <span class="bp">_</span> <span class="o">:=</span>
<span class="k">calc</span>
        <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">¬</span><span class="o">(</span><span class="n">A</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="o">(</span><span class="n">A</span> <span class="bp">∨</span> <span class="n">B</span><span class="o">)))</span>
      <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">((</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">C</span><span class="o">)</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="o">(</span><span class="n">A</span> <span class="bp">∨</span> <span class="n">B</span><span class="o">)))</span>  <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">not_imp</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">((</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">C</span><span class="o">)</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">B</span><span class="o">))</span>   <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">not_or_distrib</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">((</span><span class="bp">¬</span><span class="n">C</span> <span class="bp">∧</span> <span class="n">A</span><span class="o">)</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">B</span><span class="o">))</span>   <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">and_comm</span> <span class="o">(</span><span class="n">A</span><span class="o">)</span> <span class="o">(</span><span class="bp">¬</span><span class="n">C</span><span class="o">)</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">¬</span><span class="n">C</span> <span class="bp">∧</span> <span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">B</span><span class="o">))</span>     <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">and_assoc</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">¬</span><span class="n">C</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">A</span><span class="o">)</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">B</span><span class="o">))</span>   <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">and_assoc</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">¬</span><span class="n">C</span> <span class="bp">∧</span> <span class="bp">¬</span> <span class="n">B</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">A</span><span class="o">)))</span>  <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">and_comm</span> <span class="o">(</span><span class="bp">¬</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">A</span><span class="o">)</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">¬</span><span class="n">C</span> <span class="bp">∧</span> <span class="bp">¬</span> <span class="n">B</span> <span class="bp">∧</span> <span class="n">false</span> <span class="o">))</span>    <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">and_not_self_iff</span> <span class="n">A</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">((</span><span class="bp">¬</span><span class="n">C</span><span class="o">)</span> <span class="bp">∧</span> <span class="n">false</span> <span class="o">))</span>        <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">and_false</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">false</span><span class="o">))</span>                <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">and_false</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="bp">¬</span><span class="o">(</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span>                           <span class="o">:</span> <span class="n">rfl</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">(</span><span class="n">B</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">C</span><span class="o">)</span>                           <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">not_imp</span>
</pre></div>

#### [ Tobias Grosser (Sep 07 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492326):
<p>Nice</p>

#### [ Tobias Grosser (Sep 07 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492329):
<p>Really helpful.</p>

#### [ Tobias Grosser (Sep 07 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492344):
<p>Thank you!</p>

#### [ Kenny Lau (Sep 07 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492346):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">logic</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span> <span class="bp">_</span> <span class="bp">=</span> <span class="bp">_</span> <span class="o">:=</span>
<span class="k">calc</span>
        <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">¬</span><span class="o">(</span><span class="n">A</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="o">(</span><span class="n">A</span> <span class="bp">∨</span> <span class="n">B</span><span class="o">)))</span>
      <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">((</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">C</span><span class="o">)</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="o">(</span><span class="n">A</span> <span class="bp">∨</span> <span class="n">B</span><span class="o">)))</span>  <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">not_imp</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">((</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">C</span><span class="o">)</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">B</span><span class="o">))</span>   <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">not_or_distrib</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">((</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">B</span><span class="o">)</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">C</span><span class="o">))</span>   <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">and</span><span class="bp">.</span><span class="n">right_comm</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(((</span><span class="n">A</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">A</span><span class="o">)</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">B</span><span class="o">)</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">C</span><span class="o">))</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="err">←</span> <span class="n">and_assoc</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">((</span><span class="n">false</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">B</span><span class="o">)</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">C</span><span class="o">))</span>    <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">and_not_self_iff</span> <span class="n">A</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">false</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">C</span><span class="o">))</span>           <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">false_and</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">false</span><span class="o">))</span>                <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">false_and</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="bp">¬</span><span class="o">(</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span>                           <span class="o">:</span> <span class="n">rfl</span>
  <span class="bp">...</span> <span class="bp">=</span> <span class="o">(</span><span class="n">B</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">C</span><span class="o">)</span>                           <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">not_imp</span>
</pre></div>

#### [ Simon Hudon (Sep 07 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492460):
<p>I'm a bit vague on the rule for <code>iff</code> and other rewrite rules but in general, if an argument can be inferred from other arguments, it should be implicit. For rewrite rules, I think all the arguments that can be inferred from the lhs of the equation should be implicit.</p>

#### [ Tobias Grosser (Sep 07 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492546):
<p>I see. Thanks <span class="user-mention" data-user-id="110026">@Simon Hudon</span></p>

#### [ Mario Carneiro (Sep 07 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492706):
<div class="codehilite"><pre><span></span>example {A B C : Prop} : ((B → C) → (¬(A → C) ∧ ¬(A ∨ B))) = (B ∧ ¬C) :=
by apply classical.cases_on A;
   apply classical.cases_on B;
   apply classical.cases_on C; simp
</pre></div>


<p>The idea behind the rule for iff is that these are more often used as combined unidirectional rules, and in this case any argument present on both lhs and rhs are inferrable</p>

#### [ Simon Hudon (Sep 07 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492713):
<p>Have you tried <code>tauto</code>?</p>

#### [ Mario Carneiro (Sep 07 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492719):
<p>doesn't seem to do anything</p>

#### [ Mario Carneiro (Sep 07 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492758):
<p><code>propext $ by tauto</code> works though</p>

#### [ Simon Hudon (Sep 07 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492768):
<p>Right! You need the propositions to be decidable</p>

#### [ Kenny Lau (Sep 07 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492774):
<blockquote>
<p>example {A B C : Prop} : ((B → C) → (¬(A → C) ∧ ¬(A ∨ B))) = (B ∧ ¬C) :=<br>
by apply classical.cases_on A;<br>
   apply classical.cases_on B;<br>
   apply classical.cases_on C; simp</p>
</blockquote>
<p>that's the proof of completeness!</p>

#### [ Simon Hudon (Sep 07 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492780):
<blockquote>
<p><code>propext $ by tauto</code> works though</p>
</blockquote>
<p>Interesting! That should be worth adding to the tactic</p>

#### [ Mario Carneiro (Sep 07 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492790):
<p>mathlib tries to avoid equality of propositions though</p>

#### [ Mario Carneiro (Sep 07 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492794):
<p>it's always stated as an iff</p>

#### [ Kenny Lau (Sep 07 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492795):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span> <span class="o">((</span><span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">¬</span><span class="o">(</span><span class="n">A</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="o">(</span><span class="n">A</span> <span class="bp">∨</span> <span class="n">B</span><span class="o">)))</span> <span class="bp">=</span> <span class="o">(</span><span class="n">B</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">C</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">by_cases</span> <span class="n">A</span><span class="bp">;</span> <span class="n">by_cases</span> <span class="n">B</span><span class="bp">;</span> <span class="n">by_cases</span> <span class="n">C</span><span class="bp">;</span> <span class="n">simp</span><span class="bp">*</span>
</pre></div>

#### [ Mario Carneiro (Sep 07 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133492839):
<p>oh, of course - <code>simp</code> will rewrite <code>A</code> to <code>true</code> or <code>false</code> given the <code>by_cases</code> assumption</p>

#### [ Tobias Grosser (Sep 07 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493165):
<p>Nice. I am currently translating some student exercises, so I try to use the 'calc' mode to really show step-by-step how things evolve.</p>

#### [ Tobias Grosser (Sep 07 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493168):
<p>This worked quite well so far. Nice to see that the tactics work so well too.</p>

#### [ Mario Carneiro (Sep 07 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493180):
<p>you should be able to use <code>&lt;-&gt;</code> in those calc blocks</p>

#### [ Tobias Grosser (Sep 07 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493249):
<p>Yes, I can replace = with &lt;-&gt;</p>

#### [ Tobias Grosser (Sep 07 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493250):
<p>Does this have any benefits?</p>

#### [ Mario Carneiro (Sep 07 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493323):
<p>only it's more idiomatic; <code>rw</code> and friends will work either way</p>

#### [ Tobias Grosser (Sep 07 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493366):
<p>Why exactly is it more idiomatic?</p>

#### [ Mario Carneiro (Sep 07 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493378):
<p>because it's easier to work with iff since you can destruct it, and you don't need the propext axiom to prove things about it</p>

#### [ Simon Hudon (Sep 07 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493381):
<p><code>=</code> has stronger precedence than <code>&lt;-&gt;</code> and the other connectives so <code>&lt;-&gt;</code> yields formulas with fewer brackets</p>

#### [ Tobias Grosser (Sep 07 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493395):
<p>Great.</p>

#### [ Tobias Grosser (Sep 07 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493439):
<p>Need to get back to normal life. Thanks for your help.</p>

#### [ Mario Carneiro (Sep 07 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493443):
<p>But "idiomatic" really just means that it is used, like a convention - it doesn't need a reason per se, it's valuable because it is the convention</p>

#### [ Mario Carneiro (Sep 07 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493454):
<p>i.e. it will make it easier to fit with and apply existing theorems</p>

#### [ Tobias Grosser (Sep 07 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493465):
<p>I understand the meaning of idiomatic.</p>

#### [ Tobias Grosser (Sep 07 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493475):
<p>Wanted understand the underlying motivation.</p>

#### [ Mario Carneiro (Sep 07 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493477):
<p>so another answer is "there are two options, we picked one"</p>

#### [ Tobias Grosser (Sep 07 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493517):
<p>If I want my proofs to be understood in the end, it helps to learn the choices you as a community have taken.</p>

#### [ Mario Carneiro (Sep 07 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493522):
<p>I think logic textbooks usually use &lt;-&gt;</p>

#### [ Mario Carneiro (Sep 07 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493526):
<p>or sometimes ≡</p>

#### [ Tobias Grosser (Sep 07 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133493527):
<p>I can learn them easier if I can get an intuition where things come from.</p>

#### [ Keeley Hoek (Sep 11 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133708725):
<p>Cool fact: <code>rewrite_search</code> solves this problem instantly:</p>
<div class="codehilite"><pre><span></span>local attribute [search] imp_iff_not_or not_or_distrib not_not and_assoc and_comm and_not_self_iff and_false not_not

example {A B C : Prop} : ((B → C) → (¬(A → C) ∧ ¬(A ∨ B))) = (B ∧ ¬C) :=
  by rewrite_search_using [`search]
</pre></div>

#### [ Scott Morrison (Sep 11 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133712079):
<p>We really need to think about automatic lemma selection for rewrite_search.</p>

#### [ Scott Morrison (Sep 11 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133712089):
<p>Possible just finer attribute tagging (e.g. [search logic], [search list], [search category_theory]).</p>

#### [ Scott Morrison (Sep 11 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133712100):
<p>Perhaps even teach rewrite_search to automatically select from different bundles of lemmas depending on what it sees in the goal.</p>

#### [ Keeley Hoek (Sep 11 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133712505):
<p>At least for me, just printing out every definition in a modest real-ish maths environment takes 30 seconds, so I think some form of bundling will have to be the way to go. Maybe barring some emergency "show me the way" mode.</p>

#### [ Keeley Hoek (Sep 11 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133712553):
<p>Though "find me a lemma" mode could be a useful tactic in its own right I suppose</p>

#### [ Keeley Hoek (Sep 11 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133712665):
<p>I guess that's what I'll try next</p>

#### [ Patrick Massot (Sep 11 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/rw%20only%20simplifies%20if%20piped%20through%20my%20own%20function/near/133714529):
<blockquote>
<p>We really need to think about automatic lemma selection for rewrite_search.</p>
</blockquote>
<p>This is all very nice, but don't forget that this is a whole research area. So don't expect this to be super easy, and maybe have a look at what already exists. I think the keyword is "relevance filter"</p>


{% endraw %}
