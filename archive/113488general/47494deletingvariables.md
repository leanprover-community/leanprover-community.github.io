---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/47494deletingvariables.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [deleting variables](https://leanprover-community.github.io/archive/113488general/47494deletingvariables.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Jun 03 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485299):
<p>Is it possible to delete something that has been declared using <code>variables</code>? (I want to "upgrade" an instance variable to a class which extends the original one.)</p>

#### [ Kenny Lau (Jun 03 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485300):
<p>no</p>

#### [ Simon Hudon (Jun 03 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485309):
<p>Can you show me concretely what you're going for?</p>

#### [ Reid Barton (Jun 03 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485402):
<p>My actual example involves my own classes, but something like</p>
<div class="codehilite"><pre><span></span><span class="kn">section</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">monoid</span> <span class="n">α</span><span class="o">]</span>

<span class="c">/-</span><span class="cm"> other definitions that don&#39;t require the group structure... -/</span>

<span class="kn">variables</span> <span class="o">[</span><span class="n">group</span> <span class="n">α</span><span class="o">]</span>

<span class="n">def</span> <span class="n">g</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">x</span><span class="bp">⁻¹</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">g</span> <span class="n">x</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">g</span><span class="o">]</span>

<span class="kn">end</span>
</pre></div>

#### [ Reid Barton (Jun 03 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485439):
<p>I can just put the earlier definitions in their own section which has the <code>monoid</code> variable</p>

#### [ Reid Barton (Jun 03 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485452):
<p>but I was hoping for something more convenient</p>

#### [ Simon Hudon (Jun 03 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485457):
<p>Ah I see! Your best bet I think is to end your section and start it just before the <code>group</code> variable</p>

#### [ Simon Hudon (Jun 03 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485460):
<p>What is the inconvenient in doing that?</p>

#### [ Reid Barton (Jun 03 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485469):
<p>Not really very inconvenient, just a few extra lines of <code>section</code>/<code>end</code></p>

#### [ Simon Hudon (Jun 03 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485519):
<p>One downside I can see is if you have other variables declared in the first section that you want to keep in the rest of the section</p>

#### [ Simon Hudon (Jun 03 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485562):
<p>In that case, I would do this:</p>
<div class="codehilite"><pre><span></span>section
variables {α : Type}
section
variables [monoid α]

/- other definitions that don&#39;t require the group structure... -/
end
variables [group α]
end
</pre></div>

#### [ Simon Hudon (Jun 03 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485613):
<p>Actually, if you don't do anything, what error do you get?</p>

#### [ Reid Barton (Jun 03 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485719):
<p>There I got an error which arose because <code>*</code> was using the monoid instance and <code>\-1</code> was using the group instance</p>

#### [ Simon Hudon (Jun 03 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485732):
<p>Ah, ok, I thought maybe it would go through the group by default</p>

#### [ Mario Carneiro (Jun 03 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485734):
<p>well it's still a problem to have redundant typeclasses on a def</p>

#### [ Simon Hudon (Jun 03 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485815):
<p>Why?</p>

#### [ Mario Carneiro (Jun 03 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485832):
<p>in the theorem itself, it's a problem since they aren't the same structure, in uses it's a nuisance to have a redundant assumption</p>

#### [ Simon Hudon (Jun 03 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127485882):
<p>Right in theorems I know the issues. With defs, I can't see it will be a nuisance down the line but not how that definition would be invalid</p>

#### [ Mario Carneiro (Jun 03 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127486403):
<p>It won't be invalid. Often things like duplicate typeclass hypotheses will go unnoticed for a long time because they aren't really visibly different</p>

#### [ Mario Carneiro (Jun 03 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127486404):
<p>unless you use <code>@thm</code> and notice two underscores in place of one</p>

#### [ Simon Hudon (Jun 03 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deleting%20variables/near/127486500):
<p>It would be nice to have warnings for that kind of stuff. Actually, more warnings in general would be nice</p>


{% endraw %}
