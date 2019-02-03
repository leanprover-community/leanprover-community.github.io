---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/62075elabaseliminator.html
---

## Stream: [general](index.html)
### Topic: [elab_as_eliminator](62075elabaseliminator.html)

---


{% raw %}
#### [ Reid Barton (Jun 27 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128740170):
<p>Is there an explanation of what <code>elab_as_eliminator</code> actually does somewhere? I once tried reading the source, but wasn't enlightened.<br>
I know there is a selection bias at work here, in that I never notice when it does the right thing, but several times I've found that it fails to infer apparently obvious type parameters, where <code>elab_with_expected_type</code> succeeds.</p>

#### [ Reid Barton (Jun 27 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128740610):
<p>Here is a toy example where <code>elab_as_eliminator</code> fails but <code>elab_with_expected_type</code> succeeds:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">equal_mod</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="bp">∃</span> <span class="n">c</span><span class="o">,</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">c</span>

<span class="n">def</span> <span class="n">mod_setoid</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">setoid</span> <span class="bp">ℤ</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">r</span> <span class="o">:=</span> <span class="n">equal_mod</span> <span class="n">n</span><span class="o">,</span> <span class="n">iseqv</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="o">}</span>

<span class="n">def</span> <span class="n">Z_mod</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:=</span> <span class="n">quotient</span> <span class="o">(</span><span class="n">mod_setoid</span> <span class="n">n</span><span class="o">)</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="n">elab_with_expected_type</span><span class="o">]</span> <span class="n">quot</span><span class="bp">.</span><span class="n">lift_on</span>

<span class="n">def</span> <span class="n">mod_dvd</span> <span class="o">(</span><span class="n">n</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">Z_mod</span> <span class="o">(</span><span class="n">n</span> <span class="bp">*</span> <span class="n">k</span><span class="o">)</span> <span class="bp">→</span> <span class="n">Z_mod</span> <span class="n">n</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">quot</span><span class="bp">.</span><span class="n">lift_on</span> <span class="n">x</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">quot</span><span class="bp">.</span><span class="n">mk</span> <span class="bp">_</span> <span class="n">a</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">a&#39;</span> <span class="bp">⟨</span><span class="n">c</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">quot</span><span class="bp">.</span><span class="n">sound</span> <span class="bp">⟨</span><span class="n">k</span> <span class="bp">*</span> <span class="n">c</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="err">←</span><span class="n">mul_assoc</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Jun 27 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128740763):
<p><code>elab_as_eliminator</code> is meant for eliminators, where lean has to infer a higher order argument, namely the "motive"</p>

#### [ Mario Carneiro (Jun 27 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128740806):
<p>It's not a good fit for nondependent elimination since you can just use the usual first order unification</p>

#### [ Reid Barton (Jun 27 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128740842):
<p>OK, that was what I suspected, but wasn't sure. So ideally, methods like <code>lift</code> and <code>lift_on</code> shouldn't have that attribute, since they are nondependent</p>

#### [ Mario Carneiro (Jun 28 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128740909):
<p>something like <code>quot.rec_on</code> would be better</p>

#### [ Reid Barton (Jun 28 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128740977):
<p>Even then, this strategy is only appropriate when you want to infer the motive from the types of the arguments, rather than from the return type, right?</p>

#### [ Reid Barton (Jun 28 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128740984):
<p>Assuming the return type is something like <code>β q</code>, for which the higher-order unification problem is trivial</p>

#### [ Mario Carneiro (Jun 28 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741005):
<p>The motive is inferred from the return type, not the types of the arguments</p>

#### [ Reid Barton (Jun 28 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741010):
<p>Oh hmm, I see</p>

#### [ Reid Barton (Jun 28 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741014):
<p>but even then the problem is not necessarily trivial</p>

#### [ Mario Carneiro (Jun 28 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741071):
<p>it finds instances of the value being inducted on and replaces them with a variable</p>

#### [ Mario Carneiro (Jun 28 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741075):
<p>and that becomes the motive</p>

#### [ Mario Carneiro (Jun 28 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741148):
<div class="codehilite"><pre><span></span>example (x y : ℕ) : x + y = y + x :=
nat.rec_on (x + y)
  _ -- ⊢ 0 = y + x
  _ -- ⊢ ∀ (n : ℕ), n = y + x → nat.succ n = y + x
</pre></div>

#### [ Reid Barton (Jun 28 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741162):
<p>So why does it fail on the <code>mod_dvd</code> example? Wouldn't it conclude that <code>quot.mk _ a : Z_mod n</code>?</p>

#### [ Mario Carneiro (Jun 28 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741233):
<p>vs:</p>
<div class="codehilite"><pre><span></span>local attribute [elab_with_expected_type] nat.rec_on
example (x y : ℕ) : x + y = y + x :=
nat.rec_on (x + y) _ _
-- unexpected argument at application
--   nat.rec_on (x + y)
-- given argument
--   x + y
-- expected argument
--   y + x
</pre></div>


<p>The reason this error is reported is since the output type is <code>C n</code>, without doing higher order unification it matches against <code>eq (x + y) (y + x)</code> so it expects the major premise to be <code>y+x</code></p>

#### [ Reid Barton (Jun 28 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741235):
<p>it seems to figure this out if I give less detail in the last argument, for example replacing it by <code>(λ a a' h, sorry)</code></p>

#### [ Mario Carneiro (Jun 28 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741405):
<p>You have to put a <code>by exact</code> in the right place, to delay the elaboration of the let match</p>

#### [ Mario Carneiro (Jun 28 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741408):
<div class="codehilite"><pre><span></span>def mod_dvd (n k : ℤ) : Z_mod (n * k) → Z_mod n :=
λ x, quot.lift_on x
  (λ a, quot.mk _ a)
  (by exact λ a a&#39; ⟨c, h⟩, quot.sound ⟨k * c, by rw ←mul_assoc; exact h⟩)
</pre></div>

#### [ Mario Carneiro (Jun 28 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator/near/128741411):
<p>this works</p>


{% endraw %}
