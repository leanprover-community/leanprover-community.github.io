---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/63203updatingvectors.html
---

## Stream: [new members](index.html)
### Topic: [updating vectors](63203updatingvectors.html)

---


{% raw %}
#### [ Marcus Klaas (Dec 11 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151447262):
<p>Hi! Can anyone provide some pointers here? I'm trying to define a function that updates a vector at a given index. This seems to work, but it's very unwieldy:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">update_nth</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">:</span> <span class="n">vector</span> <span class="n">α</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">fin</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">vector</span> <span class="n">α</span> <span class="n">n</span>
<span class="bp">|</span> <span class="n">v</span> <span class="n">i</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">vector</span><span class="bp">.</span><span class="n">map₂</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span> <span class="n">idx</span><span class="o">,</span> <span class="k">if</span> <span class="n">idx</span> <span class="bp">=</span> <span class="n">i</span> <span class="k">then</span> <span class="n">a</span> <span class="k">else</span> <span class="n">b</span><span class="o">)</span> <span class="n">v</span> <span class="err">$</span> <span class="n">vector</span><span class="bp">.</span><span class="n">of_fn</span> <span class="n">id</span>
</pre></div>


<p>In particular, proving elementary lemmas on it seems near impossible:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">update_nth_helper</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">v</span> <span class="o">:</span> <span class="n">vector</span> <span class="n">α</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>
    <span class="o">:</span> <span class="n">vector</span><span class="bp">.</span><span class="n">cons</span> <span class="n">b</span> <span class="o">(</span><span class="n">update_nth</span> <span class="n">v</span> <span class="n">i</span> <span class="n">a</span><span class="o">)</span> <span class="bp">=</span> <span class="n">update_nth</span> <span class="o">(</span><span class="n">vector</span><span class="bp">.</span><span class="n">cons</span> <span class="n">b</span> <span class="n">v</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span><span class="bp">.</span><span class="n">succ</span> <span class="n">i</span><span class="o">)</span> <span class="n">a</span> <span class="o">:=</span>
<span class="n">sorry</span>
</pre></div>


<p>I'd like to provide a recursive definition, but I can't get it to work. Lean seems to think <code>n</code> is fixed.</p>
<p>Any tips on best approach here?</p>

#### [ Mario Carneiro (Dec 11 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151447862):
<p>another way to define that function is using <code>vector.nth</code> with <code>vector.of_fn</code></p>

#### [ Mario Carneiro (Dec 11 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151447871):
<p>or by referring to <code>list.update_nth</code></p>

#### [ Marcus Klaas (Dec 11 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151447990):
<p>ooh, there is a <code>list.update_nth</code>? hadn't seen that! thanks!</p>

#### [ Mario Carneiro (Dec 11 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151447994):
<p>as for <code>n</code> fixed, that happens when you put it left of the colon</p>

#### [ Marcus Klaas (Dec 11 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151448014):
<p>I'd like to put it right of the colon, but then I cannot name it any more, correct?</p>

#### [ Mario Carneiro (Dec 11 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151448021):
<p>sure you can</p>

#### [ Marcus Klaas (Dec 11 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151448026):
<p>and almost all other arguments depend on it :o</p>

#### [ Marcus Klaas (Dec 11 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151448036):
<p>oh wow</p>

#### [ Marcus Klaas (Dec 11 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151448050):
<p>i feel silly now</p>

#### [ Marcus Klaas (Dec 11 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151448115):
<p>can u provide 1 more hint on how <code>vector.nth</code> + <code>vector.of_fn</code> would work?</p>

#### [ Marcus Klaas (Dec 11 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151448713):
<p><code>list.update_nth</code> worked beautifully btw - thanks a million mario!</p>

#### [ Rob Lewis (Dec 11 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151448913):
<p>I guess Mario might have been thinking of something like <code>vector.of_fn (λ k, if k = n then a else v.nth k)</code>.</p>

#### [ Rob Lewis (Dec 11 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151448958):
<p>Depending on your application here, you might consider using <code>array</code> instead of <code>vector</code>.</p>

#### [ Marcus Klaas (Dec 11 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151449413):
<p>:O</p>

#### [ Marcus Klaas (Dec 11 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151449421):
<p>what's the trade-off?</p>

#### [ Mario Carneiro (Dec 11 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151449598):
<p>array is already basically functions from <code>fin n</code></p>

#### [ Mario Carneiro (Dec 11 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151449663):
<p>it's also more efficient for computational purposes, dunno if that matters</p>

#### [ Mario Carneiro (Dec 11 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151449711):
<p>plus this function already exists on <code>array</code>, it's called <code>array.write</code> and it's the most basic array function (everything else is in terms of it) so you should be in a good place wrt lemmas</p>

#### [ Marcus Klaas (Dec 11 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151449741):
<p>i like that</p>

#### [ Marcus Klaas (Dec 11 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151449751):
<p>thanks a bunch folks!</p>

#### [ Marcus Klaas (Dec 11 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151449887):
<p>can't wait to see your presentation on p-adic numbers this thursday btw <span class="user-mention" data-user-id="110596">@Rob Lewis</span> :-)</p>

#### [ Rob Lewis (Dec 11 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151450160):
<p>Hmm, yeah, I should finish those slides at some point.</p>

#### [ Marcus Klaas (Dec 11 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/updating%20vectors/near/151450283):
<p>^^</p>


{% endraw %}
