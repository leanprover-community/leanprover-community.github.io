---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63880lemmasurprisinglynotprovedbyrfl.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [lemma surprisingly not proved by rfl](https://leanprover-community.github.io/archive/113488general/63880lemmasurprisinglynotprovedbyrfl.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Jul 02 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128969240):
<p>Is there a shorter way to prove this and why isn't <code>rfl</code> working? Is it because the type of the lhs is <code>with_bot ℕ</code> and the rhs is <code>option ℕ</code>? (The types are defeq)</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">ordered_group</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">with_bot</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">some</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">rfl</span> <span class="c1">-- doesn&#39;t work</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">with_bot</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">some</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">unfold</span> <span class="n">has_zero</span><span class="bp">.</span><span class="n">zero</span> <span class="n">add_monoid</span><span class="bp">.</span><span class="n">zero</span> <span class="n">has_one</span><span class="bp">.</span><span class="n">one</span> <span class="n">monoid</span><span class="bp">.</span><span class="n">one</span>
  <span class="n">add_comm_monoid</span><span class="bp">.</span><span class="n">zero</span> <span class="n">semiring</span><span class="bp">.</span><span class="n">zero</span> <span class="n">ordered_semiring</span><span class="bp">.</span><span class="n">zero</span> <span class="n">linear_ordered_semiring</span><span class="bp">.</span><span class="n">zero</span>
  <span class="n">decidable_linear_ordered_semiring</span><span class="bp">.</span><span class="n">zero</span> <span class="n">comm_semiring</span><span class="bp">.</span><span class="n">zero</span>
</pre></div>

#### [ Chris Hughes (Jul 02 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128970431):
<p>Looked a little deeper and it seems <code>(0 : with_bot ℕ)</code> is defeq to <code>some (1 : multplicative ℕ)</code>. I feel like perhaps the fact that this lemma is not <code>rfl</code> means the definition ought to be changed.</p>

#### [ Mario Carneiro (Jul 02 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128986937):
<p>Oh, this is weird! It is in fact the case that <code>(0 : with_bot ℕ) = some 0</code>, but the tactics are very confused about it. Here's <code>simp</code> proving that they are different, and then the kernel says it's a wrong proof:</p>
<div class="codehilite"><pre><span></span>example : (0 : with_bot ℕ) ≠ (some 0 : option ℕ) :=
show some _ ≠ some 0, begin
  simp [multiplicative.monoid],
end
</pre></div>

#### [ Mario Carneiro (Jul 02 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128986953):
<p>I will add a lemma for it</p>

#### [ Mario Carneiro (Jul 02 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128986995):
<p>as a slight hack, you can instead prove it by <code>dec_trivial</code></p>

#### [ Kevin Buzzard (Jul 02 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128987480):
<div class="codehilite"><pre><span></span>failed to synthesize type class instance for
⊢ has_zero (with_bot ℕ)
</pre></div>


<p>-- am I missing an import?</p>

#### [ Mario Carneiro (Jul 02 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128987708):
<p><code>algebra.ordered_group</code></p>

#### [ Mario Carneiro (Jul 02 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128988232):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> Minimized:</p>
<div class="codehilite"><pre><span></span>def nat2 := nat
instance : has_one nat2 := ⟨(0 : ℕ)⟩
example : (0 : ℕ) ≠ (1 : nat2) := by simp
</pre></div>

#### [ Mario Carneiro (Jul 02 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128988318):
<p>In this example <code>example : (0 : ℕ) = (1 : nat2) := rfl</code> also fails</p>

#### [ Sebastian Ullrich (Jul 02 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128988873):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Thanks, this seems to be an imprecise term pattern match at <a href="https://github.com/leanprover/lean/blob/master/src/library/type_context.cpp#L2906-L2907" target="_blank" title="https://github.com/leanprover/lean/blob/master/src/library/type_context.cpp#L2906-L2907">https://github.com/leanprover/lean/blob/master/src/library/type_context.cpp#L2906-L2907</a></p>

#### [ Mario Carneiro (Jul 02 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128988933):
<p>Ooh, that's a tricky one. I'd hate for you to have to do defeq checks constantly there out of paranoia for tricks like I showed...</p>

#### [ Sebastian Ullrich (Jul 02 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128989538):
<p>Yeah. It's probably not a good idea in general to declare instances on semireducible defs like <code>multiplicative</code>. Is it feasible to change that?</p>

#### [ Mario Carneiro (Jul 02 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128989548):
<p>Not really, I mean that is the point</p>

#### [ Sebastian Ullrich (Jul 02 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128989559):
<p>Sorry, I meant making it irreducible or a newtype.</p>

#### [ Mario Carneiro (Jul 02 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128989625):
<p>Probably not. An important aspect of the semireducible part is that you can prove multiplicative versions of additive theorems by defeq</p>

#### [ Mario Carneiro (Jul 02 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128989657):
<p>It's fine as long as it gives way to a sufficiently forceful "unfold", but I'm not sure irreducible will</p>

#### [ Mario Carneiro (Jul 02 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128989728):
<p>I would say that users should avoid having things of type <code>multiplicative A</code> in their goal at all</p>

#### [ Mario Carneiro (Jul 02 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128989802):
<p>so I think I will change the definition of the <code>with_bot</code> instance so that it unfolds directly rather than showing the multiplicative stuff</p>

#### [ Mario Carneiro (Jul 03 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128992229):
<p>fixed</p>


{% endraw %}
