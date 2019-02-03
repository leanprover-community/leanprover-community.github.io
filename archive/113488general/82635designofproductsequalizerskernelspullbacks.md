---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/82635designofproductsequalizerskernelspullbacks.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [design of products/equalizers/kernels/pullbacks](https://leanprover-community.github.io/archive/113488general/82635designofproductsequalizerskernelspullbacks.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Aug 08 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/design%20of%20products/equalizers/kernels/pullbacks/near/131099434):
<p>I'm looking for some advice/opinions on a design issue for category theory. In particular this is about categorical products (or equalizers, or kernels, or pullbacks). I think there ought to be at least two descriptions of these, along with appropriate lemmas to move back on forth. One description will be as a special case of limits, and the other description will be more "concrete".</p>

#### [ Scott Morrison (Aug 08 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/design%20of%20products/equalizers/kernels/pullbacks/near/131099446):
<p>Writing them as special cases of limits is of course useful so we can save effort on proving things like "products are unique, up to unique isomorphism" and "equalizers are unique, up to unique isomorphism" without duplication.</p>

#### [ Scott Morrison (Aug 08 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/design%20of%20products/equalizers/kernels/pullbacks/near/131099452):
<p>But I'm pretty sure it will be too cumbersome to actually use them when presented like this.</p>

#### [ Scott Morrison (Aug 08 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/design%20of%20products/equalizers/kernels/pullbacks/near/131099467):
<p>My question is just how concrete to make the concrete version. (One possible answer here is to have several versions.)</p>

#### [ Scott Morrison (Aug 08 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/design%20of%20products/equalizers/kernels/pullbacks/near/131099622):
<p>My first inclination is to make them extremely explicit: for example for a product it would be a structure containing separate fields for the data:</p>
<p>1. an object P of the category<br>
2. maps \pi_i to each factor X_i<br>
3. if you have an object Q equipped with maps g_i to each of the X_i, then you get a map f : Q \to P<br>
4. moreover, this means that g_i factors as f then \pi_i<br>
5. finally, if you have two maps from Q to P making the g_i's factor in this way, then the two maps are equal.</p>

#### [ Scott Morrison (Aug 08 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/design%20of%20products/equalizers/kernels/pullbacks/near/131099652):
<p>Slightly less explicit would be</p>
<p>1. an object P of the category<br>
2. maps \pi_i to each factor X_i<br>
3. given Q and maps g_i : Q \to X_i, the fact that the set of maps Q \to P giving those factorisations is a singleton set</p>

#### [ Scott Morrison (Aug 08 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/design%20of%20products/equalizers/kernels/pullbacks/near/131099719):
<p>Maybe there's not much difference between the two. In any case, if someone cares let me know, as this is easy to change now. :-)</p>

#### [ Scott Morrison (Aug 08 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/design%20of%20products/equalizers/kernels/pullbacks/near/131099743):
<p>The advantage of the first approach is that if you just want the map Q \to P, you can ask for it directly without having to unpack a witness that a certain type is a singleton to actually get the element.</p>

#### [ Scott Morrison (Aug 08 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/design%20of%20products/equalizers/kernels/pullbacks/near/131099746):
<p>The disadvantage is that it's a bit grosser to write everything out.</p>

#### [ Scott Morrison (Aug 08 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/design%20of%20products/equalizers/kernels/pullbacks/near/131099795):
<p>I'm curious to know which choice feels more usable to people.</p>

#### [ Johan Commelin (Aug 08 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/design%20of%20products/equalizers/kernels/pullbacks/near/131099814):
<p>Hi Scott! Those are the difficult questions that we will have to tackle!</p>

#### [ Johan Commelin (Aug 08 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/design%20of%20products/equalizers/kernels/pullbacks/near/131099816):
<p>Did you see Reid's approach in his homotopy lib?</p>

#### [ Johan Commelin (Aug 08 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/design%20of%20products/equalizers/kernels/pullbacks/near/131099858):
<p>He basically provides both. Your (1,2,3) would be a wrapper around (1,2,3,4,5)</p>

#### [ Scott Morrison (Aug 08 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/design%20of%20products/equalizers/kernels/pullbacks/near/131100108):
<p>Great, thanks for the pointer! (And my apologies to <span class="user-mention" data-user-id="110032">@Reid Barton</span>, for not having yet read his work, although he told me about it a few days ago.)</p>

#### [ Scott Morrison (Aug 08 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/design%20of%20products/equalizers/kernels/pullbacks/near/131100185):
<p>Seeing that Reid went for two versions, I'm further inclined to go for lots of versions: the gory one, the "singleton" based one, and the "this is just a limit" one.</p>

#### [ Patrick Massot (Aug 08 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/design%20of%20products/equalizers/kernels/pullbacks/near/131100527):
<p>I'm almost sure we need several versions, with "constructors" to get the most explicit ones out of implicit information.</p>

#### [ Scott Morrison (Aug 08 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/design%20of%20products/equalizers/kernels/pullbacks/near/131100582):
<p>Yes. Having just looked at <span class="user-mention" data-user-id="110032">@Reid Barton</span>'s design for this, I like it. (Well... I might try rewriting it myself before I really like it, but the overall approach looks right.)</p>

#### [ Scott Morrison (Aug 08 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/design%20of%20products/equalizers/kernels/pullbacks/near/131100638):
<p>Although I think/hope all his lemmas about various types of colimits interacting can be simplified! I'd hope you can just prove a Fubini theorem for colimits, and then specialise to get many of the lemmas there. Haven't thought about this very hard, however!</p>

#### [ Patrick Massot (Aug 08 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/design%20of%20products/equalizers/kernels/pullbacks/near/131100815):
<p>What would be really really useful is a convenient way to be able to use all this as an external tool. For instance, we have uniform spaces in mathlib, and all lemmas required to make a category of those, but we don't have that category. Same for complete Hausdorff uniform spaces. Then we have <a href="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/completion.lean#L8-L15" target="_blank" title="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/completion.lean#L8-L15">https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/completion.lean#L8-L15</a>. And I'd like <a href="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/completion.lean#L20-L24" target="_blank" title="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/completion.lean#L20-L24">https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/completion.lean#L20-L24</a> to be done by invoking a function defined in <code>category_theory</code> with minimal effort, without necessarily being tied to use the content of <code>category_theory</code> everywhere else.</p>

#### [ Patrick Massot (Aug 08 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/design%20of%20products/equalizers/kernels/pullbacks/near/131100843):
<p>same for the uniqueness up to unique iso of the completion</p>


{% endraw %}
