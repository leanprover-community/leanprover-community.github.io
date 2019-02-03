---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55735categorytheorydirectories.html
---

## Stream: [general](index.html)
### Topic: [category theory directories](55735categorytheorydirectories.html)

---


{% raw %}
#### [ Reid Barton (Aug 23 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20directories/near/132605394):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span>, would you accept PRs to <code>lean-category-theory</code> and <code>lean-category-theory-pr</code> which move everything from <code>categories/</code> to <code>category_theory/</code>?</p>

#### [ Reid Barton (Aug 23 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20directories/near/132605484):
<p>I'm trying to update my project to use the new mathlib with categories, and I'd rather only go through the Great Renaming of modules once</p>

#### [ Reid Barton (Aug 23 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20directories/near/132605487):
<p>And, I also use your <code>-pr</code> library.</p>

#### [ Reid Barton (Aug 23 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20directories/near/132609260):
<p>Actually, I may just add some "forwarding" modules to my project for now, since I think I only use a few modules from <code>-pr</code> at this point.</p>

#### [ Scott Morrison (Aug 25 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20directories/near/132751901):
<p>Okay, the <code>lean-category-theory-pr</code>library has finally been laid to rest, and there's just mathlib and <code>lean-category-theory</code>.  Sorry about that. :-)</p>

#### [ Scott Morrison (Aug 25 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20directories/near/132751912):
<p>In related news, <code>lean-category-theory</code> now contains my updated version of limits (not all the colimit stuff is filled in yet, hoping someone wants to write me a nice tactic. :-)</p>

#### [ Scott Morrison (Aug 25 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20directories/near/132751960):
<p>It's missing some things that used to be in <code>lean-category-theory</code>, in particular constructing limits from products and equalizers, and showing that if D has limits, the functor category <code>C \lea D</code> has limits too. Hopefully these should be easier to reimplement with the new design, anyway.</p>

#### [ Reid Barton (Aug 25 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/category%20theory%20directories/near/132752036):
<p>It turned out <code>.isomorphisms</code> was the only module I was using, so it was easy to work around.</p>


{% endraw %}
