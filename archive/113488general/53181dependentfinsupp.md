---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53181dependentfinsupp.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [dependent finsupp](https://leanprover-community.github.io/archive/113488general/53181dependentfinsupp.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Sep 04 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133297941):
<p>I want to make finsupp dependent, and then build the current finsupp as a special case. Is this a good idea?</p>

#### [ Johannes Hölzl (Sep 04 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133298356):
<p>I thought to suggest this as part of the direct sum PR :-)</p>

#### [ Kenny Lau (Sep 04 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133304404):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> I'm not sure what to do with this. finsupp is widely used. should I make a separate file?</p>

#### [ Johannes Hölzl (Sep 04 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133304601):
<p>Yes. Start with a separate file where you generalize from direct sum to <code>dfinsupp</code>, i.e. from <code>[Π i, module R (β i)]</code> to <code>[Π i, has_zero (β i)]</code>.</p>

#### [ Kenny Lau (Sep 04 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133329943):
<p>problem. the simp lemmas now require higher order unification, rendering them useless</p>

#### [ Kenny Lau (Sep 05 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133375942):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> should I make finsupp dependent on dfinsupp?</p>

#### [ Johannes Hölzl (Sep 05 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133376017):
<p>Yes, I think so. But let's first add <code>dfinsupp</code> and then see.</p>

#### [ Kenny Lau (Sep 05 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133376899):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>  there's one thing though. now for finsupp from A to B, we need decidable equality on B</p>

#### [ Kenny Lau (Sep 05 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133376909):
<p>I suspect that if we define finsupp differently, then we won't need decidbale equlaity on B</p>

#### [ Kenny Lau (Sep 05 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133376917):
<p>should I work on that?</p>

#### [ Johannes Hölzl (Sep 05 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133377009):
<p>I guess this is your quotient construction, the one you use in your direct sums construction? If you want to use it, that's fine for me.</p>

#### [ Kenny Lau (Sep 05 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133377042):
<p>yes, ok, thanks</p>

#### [ Kenny Lau (Sep 06 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133458668):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> I'm in a dilemma: I can either define dfinsupp.sum with the same arguments, but it would require decidable equality on the codomains; or I can define dfinsupp.sum without decidable equality on the codomains, but it would require me to provide an extra argument that the input function maps 0 to 0.</p>

#### [ Johan Commelin (Sep 06 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133459061):
<p>I would go for the latter.</p>

#### [ Johan Commelin (Sep 06 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133459113):
<p>Alternatively, provide both...</p>

#### [ Kevin Buzzard (Sep 06 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133459118):
<p>What's your motivation for defining dfinsupp? Is there some application you have in mind?</p>

#### [ Johan Commelin (Sep 06 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133459150):
<p>Constructive direct sums, I think</p>

#### [ Kevin Buzzard (Sep 06 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133459219):
<p>oh that would make sense, Kenny was talking to me about direct sums recently.</p>

#### [ Johannes Hölzl (Sep 06 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133463204):
<p>Since the types are usually fixed and it's super annoying to always attach the <code>f 0 = 0</code> proof: assume decidability of the codomain for <code>sum</code>.</p>

#### [ Kenny Lau (Sep 07 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493682):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> sometimes we don't actually need decidable equality in general, we just need to determine if something is zero. What should I do in that case?</p>

#### [ Simon Hudon (Sep 07 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493759):
<p>you can say that <code>(x = 0)</code> and <code>(0 = x)</code> are decidable.</p>

#### [ Kenny Lau (Sep 07 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493777):
<p>Should I make a new typeclass for that? decidable_zero</p>

#### [ Mario Carneiro (Sep 07 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493786):
<p><code>decidable_pred (eq 0)</code> works</p>

#### [ Kenny Lau (Sep 07 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493839):
<p>if I prove that <code>decidable_eq \to decidable_pred (eq 0)</code>, will Lean be able to use it?</p>

#### [ Simon Hudon (Sep 07 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493844):
<p>If you look at <code>decidable_eq</code>, <code>decidable_pred</code> and <code>decidable_rel</code>, they are simply definitions on top of <code>decidable</code>. You only need to do the same for <code>0</code> if it's pervasive enough</p>

#### [ Kenny Lau (Sep 07 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493849):
<p>well, <code>option</code> has decidable "none"</p>

#### [ Kenny Lau (Sep 07 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493859):
<p><code>with_zero</code> has decidable <code>zero</code></p>

#### [ Simon Hudon (Sep 07 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493863):
<blockquote>
<p>if I prove that <code>decidable_eq \to decidable_pred (eq 0)</code>, will Lean be able to use it?</p>
</blockquote>
<p>I think so</p>

#### [ Kenny Lau (Sep 07 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493928):
<p>oh I don't even need to prove it!</p>

#### [ Kenny Lau (Sep 07 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493931):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">}</span> <span class="o">[</span><span class="n">has_zero</span> <span class="n">γ</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">γ</span><span class="o">]</span> <span class="o">:</span> <span class="n">decidable_pred</span> <span class="o">(</span><span class="n">eq</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">γ</span><span class="o">))</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">apply_instance</span>
</pre></div>

#### [ Kenny Lau (Sep 07 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493932):
<p>Lean is smart</p>

#### [ Kenny Lau (Sep 07 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493936):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">}</span> <span class="o">[</span><span class="n">has_zero</span> <span class="n">γ</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="o">(</span><span class="n">eq</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">γ</span><span class="o">))]</span> <span class="o">:</span> <span class="n">decidable_pred</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">apply_instance</span>
</pre></div>

#### [ Kenny Lau (Sep 07 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493974):
<p>I can't believe this, something must be wrong</p>

#### [ Mario Carneiro (Sep 07 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493983):
<p><code>eq 0</code> is <code>\lam x, eq 0 x</code> which is <code>\lam x, 0 = x</code></p>

#### [ Mario Carneiro (Sep 07 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493985):
<p>the other one is <code>(= 0)</code> which is <code>\lam x, x = 0</code></p>

#### [ Kenny Lau (Sep 07 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493992):
<p>yeah the second one is wrong</p>

#### [ Kenny Lau (Sep 07 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493996):
<p>Lean interpreted <code>0</code> as natural</p>

#### [ Simon Hudon (Sep 07 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133494118):
<p>So how does Lean prove the instances for you?</p>

#### [ Kenny Lau (Sep 07 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133494220):
<p>I proved the second one now</p>

#### [ Kenny Lau (Sep 07 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133494222):
<p>the first one is just solve by elim</p>

#### [ Simon Hudon (Sep 07 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133494272):
<p>Why does that work?</p>

#### [ Simon Hudon (Sep 07 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133494274):
<p>Oh, ok, it's proving less than I thought</p>

#### [ Kenny Lau (Sep 09 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133585305):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> commited to the <a href="https://github.com/leanprover/mathlib/pull/311" target="_blank" title="https://github.com/leanprover/mathlib/pull/311">PR</a></p>

#### [ Kenny Lau (Oct 06 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/135325125):
<p>What is preventing this <a href="https://github.com/leanprover/mathlib/pull/311" target="_blank" title="https://github.com/leanprover/mathlib/pull/311">22-day-old pull request</a> from being merged?</p>

#### [ Kevin Buzzard (Oct 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/135325331):
<p>People being busy?</p>

#### [ Kevin Buzzard (Oct 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/135325334):
<p>You'll understand, one day :-)</p>

#### [ Kenny Lau (Oct 06 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/135325996):
<p>Are there any problems with my PR? <span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Mario Carneiro (Oct 07 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/135329645):
<p>It conflicts with the module refactor, so don't expect this to be merged until after that</p>

#### [ Kevin Buzzard (Oct 07 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/135329897):
<p>But after the module refactor Kenny will be too busy working on algebraic closure to be able to fix up this PR.</p>

#### [ Kenny Lau (Oct 07 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/135343213):
<p>ok no problem</p>


{% endraw %}
