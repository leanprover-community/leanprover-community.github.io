---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/62392piecewisefunctions.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [piecewise functions](https://leanprover-community.github.io/archive/113489newmembers/62392piecewisefunctions.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Aymon Wuolanne (Dec 20 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152232475):
<p>Does anyone have any tips for dealing with piecewise functions, in particular showing that they're continuous? I have something like the following in mind:</p>
<div class="codehilite"><pre><span></span>variables (a : ℝ) (f : ℝ → ℝ) (g : ℝ → ℝ)
def pw : ℝ → ℝ := λ x, if x ≤ a then f x else g x
lemma continuous_pw : continuous f → continuous g → f a = g a → continuous (pw a f g) := sorry
</pre></div>

#### [ Jeremy Avigad (Dec 20 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152234041):
<p>Coincidentally, I just issued a pull request with some additions to the analysis library. There is a lemma called <code>tendsto_if</code> which will be helpful: <a href="https://github.com/avigad/mathlib/blob/limit_stuff/order/filter.lean#L1257-L1261" target="_blank" title="https://github.com/avigad/mathlib/blob/limit_stuff/order/filter.lean#L1257-L1261">https://github.com/avigad/mathlib/blob/limit_stuff/order/filter.lean#L1257-L1261</a>. I'd use the fact that a function is continuous if it is continuous at every point (which used to be called <code>continuous_iff_tendsto</code> but in my PR is <code>continuous_iff_continuous_at</code>. Using <code>metric_space</code> you can unwrap the definition of neighborhoods in terms of distance.</p>

#### [ Reid Barton (Dec 20 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152236649):
<p>There's also <code>continuous_if</code> and <code>continuous_subtype_is_closed_cover</code></p>

#### [ Patrick Massot (Dec 20 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152238561):
<blockquote>
<p>Coincidentally, I just issued a pull request with some additions to the analysis library. </p>
</blockquote>
<p>You should expect a lot of homework now, that Mario guy is merciless...</p>

#### [ Patrick Massot (Dec 20 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152238630):
<p>Seriously I'm very excited to see some PR from your analysis work. I hope you already discussed it enough with Mario, and will convince Johannes quickly. It would be very nice to have a topology PR merge sprint before Amsterdam (or even before Christmas, and then a second one before Amsterdam)</p>

#### [ Kenny Lau (Dec 20 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152238643):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> merciless</p>

#### [ Johan Commelin (Dec 20 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152239509):
<p>Completely agree. Let's get these PRs moving.</p>

#### [ Aymon Wuolanne (Dec 20 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240099):
<p>Thanks! I think I should be able to get it working with <code>continuous_if</code></p>

#### [ Aymon Wuolanne (Dec 20 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240118):
<p>Side note: <code>frontier</code> is defined as <code>closure s \ interior s</code>, isn't this usually referred to as the boundary?</p>

#### [ Johan Commelin (Dec 20 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240169):
<p>I've never heard of <code>frontier</code> before. I learned it as <code>boundary</code>.</p>

#### [ Mario Carneiro (Dec 20 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240177):
<p>I thought frontier was <code>closure s \ s</code></p>

#### [ Johan Commelin (Dec 20 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240204):
<p>So what is <code>s \ interior s</code> called?</p>

#### [ Reid Barton (Dec 20 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240214):
<p>apparently it is sometimes called the boundary! not even making this up</p>

#### [ Reid Barton (Dec 20 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240216):
<p><a href="https://en.wikipedia.org/wiki/Boundary_(topology)" target="_blank" title="https://en.wikipedia.org/wiki/Boundary_(topology)">https://en.wikipedia.org/wiki/Boundary_(topology)</a></p>

#### [ Mario Carneiro (Dec 20 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240264):
<blockquote>
<p>So what is <code>s \ interior s</code> called?</p>
</blockquote>
<p>outliers?</p>

#### [ Johan Commelin (Dec 20 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240292):
<p><a href="https://www.thesaurus.com/browse/boundary" target="_blank" title="https://www.thesaurus.com/browse/boundary">https://www.thesaurus.com/browse/boundary</a> enough words to choose from (-;</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240303):
<p>periphery is nice</p>

#### [ Johan Commelin (Dec 20 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240314):
<p>is borderline acceptable</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240318):
<p>it's borderline acceptable</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240374):
<p>but actually I find very little use for these concepts, they are more a historical note for me</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240378):
<p>boundary is useful though</p>

#### [ Jeremy Avigad (Dec 20 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152284935):
<p>Mario has gone easy on me so far. I am about to get on a flight to California to visit my in-laws, but I should be able to make the corrections there.</p>

#### [ Mario Carneiro (Dec 20 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152285351):
<p>It looks pretty good. there is absolutely no chance of a conflict of interest, yep</p>

#### [ Patrick Massot (Dec 20 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152285645):
<p>Would you give this PR a master's thesis?</p>


{% endraw %}
