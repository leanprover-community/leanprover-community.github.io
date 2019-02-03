---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/17064howtousesolvebyelim.html
---

## Stream: [general](index.html)
### Topic: [how to use `solve_by_elim`](17064howtousesolvebyelim.html)

---


{% raw %}
#### [ Chris Hughes (Aug 17 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/132313630):
<p>What is the syntax for giving <code>solve_by_elim</code> a discharger. I tried <code>solve_by_elim `[cc] </code> like the docs suggest, but I couldn't get it to work.</p>

#### [ Simon Hudon (Aug 17 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/132313735):
<p>That would be a case of outdated documentation. Try <code>solve_by_elim { discharger := `[cc] }</code></p>

#### [ Simon Hudon (Aug 17 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/132314890):
<p>I just updated it. <a href="https://github.com/leanprover/mathlib/pull/266" target="_blank" title="https://github.com/leanprover/mathlib/pull/266">https://github.com/leanprover/mathlib/pull/266</a></p>

#### [ Scott Morrison (Sep 09 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/133587653):
<p>Hi <span class="user-mention" data-user-id="110026">@Simon Hudon</span>, I proposed a further modification to <code>solve_by_elim</code> at <a href="https://github.com/leanprover/mathlib/pull/324" target="_blank" title="https://github.com/leanprover/mathlib/pull/324">https://github.com/leanprover/mathlib/pull/324</a>. I'd be interested in your opinion sometime.</p>

#### [ Scott Morrison (Sep 09 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/133587655):
<p>It's essentially just an extra option to make it convenient to add <code>congr_fun</code> and <code>congr_arg</code> to the assumptions.</p>

#### [ Simon Hudon (Sep 09 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/133587801):
<p>Cool idea!</p>

#### [ Scott Morrison (Sep 25 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/134573606):
<p>Thanks, <span class="user-mention" data-user-id="110026">@Simon Hudon</span> and <span class="user-mention" data-user-id="110032">@Reid Barton</span> for looking at my proposed changes to <code>solve_by_elim</code>. I've just pushed another change that make it quite a bit more usable --- it's now quite like the syntax for adding and removing lemmas from <code>simp</code>.</p>

#### [ Scott Morrison (Sep 25 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/134573610):
<p><a href="https://github.com/leanprover/mathlib/pull/324" target="_blank" title="https://github.com/leanprover/mathlib/pull/324">https://github.com/leanprover/mathlib/pull/324</a></p>

#### [ Simon Hudon (Sep 25 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/134574016):
<p>What's the attribute name?</p>

#### [ Scott Morrison (Sep 25 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/134578415):
<p>Oh -- there's no attribute that is automatically hooked into <code>solve_by_elim</code>, although we could do that!</p>

#### [ Scott Morrison (Sep 25 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/134578467):
<p>You can write <code>solve_by_elim [f, a]</code>, where <code>f</code> is a lemma, and <code>a</code> is an attribute, it will will look up all lemmas tagged with <code>a</code>, and then use the local context, <code>f</code>, and those <code>a</code>-lemmas.</p>

#### [ Scott Morrison (Sep 25 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/134578473):
<p>You can also write <code>solve_by_elim only [f, a]</code> to not include the local context.</p>

#### [ Simon Hudon (Sep 25 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/134578564):
<p>Actually, now I see what you did and it might be better to refrain from having a default <code>solve_by_elim</code> attribute, at least for now. We're battling the huge size of the <code>simp</code> list at the moment, maybe we can avoid or at least postpone the same situation for <code>solve_by_elim</code> and other attribute-based tactics.</p>

#### [ Scott Morrison (Oct 06 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/135292325):
<p>Hi <span class="user-mention" data-user-id="110026">@Simon Hudon</span>, I noticed what I think is a bug, or at least suboptimal behaviour in solve_by_elim, preventing successful backtracking when an <code>apply</code> generates multiple subgoals:</p>
<div class="codehilite"><pre><span></span>example {α : Type} (r : α → α → Prop) (f : α → α → α)
  (l : ∀ a b c : α, r a b → r a (f b c) → r a c)
  (a b c : α) (h₁ : r a b) (h₂ : r a (f b c)) : r a c :=
begin
  -- solve_by_elim ought to work here:
  have w : r a c,
  { apply l,
    apply h₁,
    apply h₂ },
  clear w,
  -- sadly, it doesn&#39;t, because of the way we recurse to subgoals.
  solve_by_elim,
  -- (Once solve_by_elim successfully uses h₂ on the first goal, it can&#39;t
  -- backtrack after realising that was a bad idea.)
end
</pre></div>

#### [ Scott Morrison (Oct 06 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/135292330):
<p>There's an easy fix, but I thought I'd check if you agreed it warrants fixing before I PR it.</p>

#### [ Simon Hudon (Oct 06 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/135292921):
<p>It looks like your proof of <code>w</code> is the only path that <code>solve_by_elim</code> can take. Can you show me the mistaken approach it tries?</p>

#### [ Scott Morrison (Oct 06 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/135295040):
<p>It can trying applying h2 first. That succeeds, but then it has no where to go, and it fails to backtrack.</p>

#### [ Scott Morrison (Oct 06 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/135295082):
<p>(Because with multiple sub goals solve_by_elim currently uses <code>;</code> to recurse into them, it can’t backtrack across multiple sub goals.</p>

#### [ Scott Morrison (Oct 06 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/135295134):
<p>That is, it tries:</p>
<div class="codehilite"><pre><span></span>apply l,
apply h2
</pre></div>


<p>And then is faced with the goal <code>r a (f (f b c) ?m)</code> and can’t proceed.</p>

#### [ Simon Hudon (Oct 06 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/135295233):
<p>Ah! I see! How do you suggest to solve this?</p>

#### [ Scott Morrison (Oct 06 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/135298736):
<p>It's pretty easy: see <a href="https://github.com/leanprover/mathlib/pull/393/commits/3fab845ccdfb081febf09821c4c1e43dbb82f75b" target="_blank" title="https://github.com/leanprover/mathlib/pull/393/commits/3fab845ccdfb081febf09821c4c1e43dbb82f75b">https://github.com/leanprover/mathlib/pull/393/commits/3fab845ccdfb081febf09821c4c1e43dbb82f75b</a></p>


{% endraw %}
