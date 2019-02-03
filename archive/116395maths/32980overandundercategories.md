---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/32980overandundercategories.html
---

## Stream: [maths](index.html)
### Topic: [over and under categories](32980overandundercategories.html)

---


{% raw %}
#### [ Johan Commelin (Dec 17 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/over%20and%20under%20categories/near/151910153):
<p>Over and under categories show up all over the place (notably covers and structure maps can use over categories, and algebras can use under categories). I've written the definitions and a bunch of simp lemmas in <a href="https://github.com/leanprover-community/mathlib/blob/over_under/category_theory/comma.lean#L195" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/over_under/category_theory/comma.lean#L195">https://github.com/leanprover-community/mathlib/blob/over_under/category_theory/comma.lean#L195</a><br>
Now I would like to prove some facts about limits/colimits in these categories. What would be the right file in mathlib to put these?</p>

#### [ Reid Barton (Dec 17 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/over%20and%20under%20categories/near/151911457):
<p>I guess the current "convention" would be a new file <code>category_theory.limits.&lt;something&gt;</code></p>

#### [ Johan Commelin (Dec 17 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/over%20and%20under%20categories/near/152007049):
<p>Ok, I'll do that. So that would probably be <code>category_theory.limits.over</code>.</p>

#### [ Chris Hughes (Dec 17 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/over%20and%20under%20categories/near/152011380):
<p>(deleted)</p>

#### [ Johan Commelin (Dec 18 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/over%20and%20under%20categories/near/152132709):
<p>It seems I'm pushing the limits of the category library again.<br>
I'm trying to prove an equivalence of two categories: <a href="https://github.com/leanprover-community/mathlib/blob/over_under/category_theory/comma.lean#L238" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/over_under/category_theory/comma.lean#L238">https://github.com/leanprover-community/mathlib/blob/over_under/category_theory/comma.lean#L238</a><br>
This is completely math-trivial: If I take <code>Y</code> in the category <code>over X</code>, then <code>over Y</code> is equivalent to <code>over (Y.left)</code>. There is almost no content... just composing some arrows. Still I'm running into deterministic timeouts and such. Is this just stuff that should wait?</p>

#### [ Reid Barton (Dec 18 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/over%20and%20under%20categories/near/152134163):
<p>I think you should write out the components of the natural isomorphisms anyways</p>

#### [ Patrick Massot (Dec 18 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/over%20and%20under%20categories/near/152141717):
<p>Does it mean that Scott's magic auto-param are failing here?</p>

#### [ Johan Commelin (Dec 19 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/over%20and%20under%20categories/near/152158162):
<p>Partly, yes. Maybe that would be fixed once <code>back</code> and <code>rewrite_search</code> are part of mathlib. But another problem is that the code is just terribly slow. At some point I close a goal by <code>exact foobar</code> and this takes several seconds. I guess that is just exhibiting that we are stacking lots of stuff on top of each other. (In particular the <code>pp.all</code> output is usually not much fun to look at.)</p>


{% endraw %}
