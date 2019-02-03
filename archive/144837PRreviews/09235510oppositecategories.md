---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/09235510oppositecategories.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#510 opposite categories](https://leanprover-community.github.io/archive/144837PRreviews/09235510oppositecategories.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Dec 20 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/152239436):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I saw you fixed some stuff, but Travis is still complaining... If you don't have time for this, just let me know, and I'll try to take a look.</p>

#### [ Scott Morrison (Dec 20 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/152241278):
<p>Think I've got it now. That intermediate commit was just getting work from my office computer to my laptop.</p>

#### [ Johan Commelin (Dec 22 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/152389993):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I get that you don't like the idea of making <code>op</code> irreducible. So what is the best way forward? Just now I had to compose two arrows <code>f</code> and <code>g</code>, but <code>f</code> lived in the opposite category... so Lean complained. I would love to just write <code>f.unop</code> and move on. What do you think is the best solution?</p>

#### [ Mario Carneiro (Dec 22 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/152390040):
<p>you can have <code>unop</code> without making <code>op</code> irreducible</p>

#### [ Johan Commelin (Jan 17 2019 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/155339244):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Would you welcome a PR that puts <code>op</code> and <code>unop</code> throughout the library without making <code>op</code> irreducible?</p>

#### [ Mario Carneiro (Jan 17 2019 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/155345431):
<p>sure</p>

#### [ Scott Morrison (Jan 19 2019 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156433638):
<p>Ok, <a href="https://github.com/leanprover/mathlib/issues/510" target="_blank" title="https://github.com/leanprover/mathlib/issues/510">#510</a> no longer actually makes <code>opposite</code> irreducible. This PR has some useful cleanup in other category_theory files, as well.</p>

#### [ Reid Barton (Jan 22 2019 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156597595):
<p>It's hard to understand what is going on when reviewing a commit which contains a combination of substantial changes (like to <code>op</code>), general cleanup, and new features.</p>

#### [ Reid Barton (Jan 22 2019 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156597623):
<p>Miscellaneous cleanup PRs are fine, but they shouldn't be mixed in with actual changes.</p>

#### [ Reid Barton (Jan 22 2019 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156597697):
<p>Did we come to the conclusion that <code>opposite</code> should not be irreducible? Or are we just not changing it for now?</p>

#### [ Johan Commelin (Jan 22 2019 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156597713):
<p>Mario does not want it to be irreducible. I have no clue what's good. And others seemed to not care very much (-;</p>

#### [ Johan Commelin (Jan 22 2019 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156597718):
<p>So for now it won't be irreducible.</p>

#### [ Reid Barton (Jan 22 2019 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156598117):
<p>Hmm, but I see <code>hom.op</code> and <code>hom.unop</code> are irreducible?</p>

#### [ Reid Barton (Jan 22 2019 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156598120):
<p>Is that intentional?</p>

#### [ Reid Barton (Jan 22 2019 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156598126):
<p>and then sometimes they get made not irreducible</p>

#### [ Reid Barton (Jan 22 2019 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156598378):
<p>I guess I don't really understand what the plan is that involves introducing <code>op</code> and <code>unop</code> but not making <code>opposite</code> irreducible (or even a structure). I feel like we don't have a good chance of putting <code>op</code>/<code>unop</code> in all the right spots if not forced to do so by irreducibility of <code>opposite</code>, and then whatever problem we solve with <code>op</code>/<code>unop</code> will continue to show up later.</p>

#### [ Johan Commelin (Jan 22 2019 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156598402):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> What do you think about <span class="emoji emoji-2b06" title="up">:up:</span> ?</p>

#### [ Reid Barton (Jan 22 2019 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156598476):
<p>I think what we really want is a one-member structure with definitional eta, and this <code>irreducible</code> thing is the closest approximation we can make</p>

#### [ Reid Barton (Jan 22 2019 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156599932):
<p>I wonder whether we need <code>category.hom.op</code> at all</p>

#### [ Johan Commelin (Jan 22 2019 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156600126):
<p>I've had breakage because Lean thought <code>f</code> was in the opposite category and I wanted something in <code>C</code>.</p>

#### [ Johan Commelin (Jan 22 2019 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156600132):
<p>Or are you saying we only need <code>unop</code>?</p>

#### [ Reid Barton (Jan 22 2019 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156600316):
<p>Okay, after some experimentation, removing <code>category.hom.op</code> seems like a bad idea</p>

#### [ Reid Barton (Jan 22 2019 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156600338):
<p>But I'm not very happy about marking them as irreducible but then undoing that in various places.</p>

#### [ Reid Barton (Jan 22 2019 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156600750):
<p>I think all this <code>hom.op</code> stuff doesn't address the real issue though</p>

#### [ Reid Barton (Jan 22 2019 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156600821):
<p>it's still easy to end up with goals like <code>F.map g ≫ F.map f = F.map f ≫ F.map g</code></p>

#### [ Reid Barton (Jan 22 2019 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156601769):
<p>I think the right way to do this would be to give the hom sets the same treatment as the objects, but it seems to be impossible without splitting out the <code>hom</code> field into its own class</p>

#### [ Reid Barton (Jan 22 2019 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156601780):
<p>which I think we may want to do anyways</p>

#### [ Reid Barton (Jan 22 2019 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156603158):
<p>For example, the definition of composition in the opposite category should not be <code>λ _ _ _ f g, g ≫ f</code> but <code>λ _ _ _ f g, (g.unop ≫ f.unop).op</code></p>

#### [ Reid Barton (Jan 22 2019 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156604715):
<p>I would also be willing to try just using a structure</p>

#### [ Reid Barton (Jan 22 2019 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23510%20opposite%20categories/near/156606540):
<p>In fact, maybe we can even reuse <a href="https://github.com/leanprover/mathlib/pull/538" target="_blank" title="https://github.com/leanprover/mathlib/pull/538">https://github.com/leanprover/mathlib/pull/538</a>?</p>


{% endraw %}
