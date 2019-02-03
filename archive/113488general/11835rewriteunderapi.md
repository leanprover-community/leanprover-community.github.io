---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/11835rewriteunderapi.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [rewrite under a pi](https://leanprover-community.github.io/archive/113488general/11835rewriteunderapi.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Sep 27 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134751362):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">lemma</span> <span class="n">quadroots</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">}</span> <span class="o">:</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">-</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">↔</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">2</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">,</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">-</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="n">quadroots</span><span class="o">,</span> <span class="c1">-- fails</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p>I thought this would work. I have to <code>intro x</code> before it does. I know that <code>rw</code> can fail to rewrite under a lambda, but this is not a lambda, right? Can Lean also not rewrite under a pi?</p>

#### [ Mario Carneiro (Sep 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134751519):
<p>it cannot rewrite under a binder, because it needs to produce a substitution instance in the outer context</p>

#### [ Mario Carneiro (Sep 27 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134751597):
<p>To be clear, you can rewrite expressions that don't make use of the binder, like rewriting <code>y</code> to <code>z</code> in <code>\lam x, x = y</code></p>

#### [ Mario Carneiro (Sep 27 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134751631):
<p>but since <code>rw</code> constructs an <code>eq.rec</code> term in the outer context it doesn't make sense to refer to <code>x</code></p>

#### [ Mario Carneiro (Sep 27 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134751697):
<p>Think of it this way: <code>rw quadroots</code> is really <code>rw [quadroots _]</code>. What should go in for <code>_</code>?</p>

#### [ Reid Barton (Sep 27 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134751779):
<p>Interesting. I also encountered this exact question the other day--I expected <code>rw</code> to work in a similar situation, rewriting under a Pi, because it wasn't rewriting under a lambda. But I don't remember what ended up happening. It's possible I was in the "doesn't depend on x" situation.</p>

#### [ Reid Barton (Sep 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134751917):
<p>Can I think about it this way? I expect <code>rw</code> to apply something like "<code>Pi.congr</code>". But what is the argument to <code>Pi.congr</code>. It should just be an equality I intend to rewrite along, not something of the form <code>\all x, f x = g x</code></p>

#### [ Mario Carneiro (Sep 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134751955):
<p><code>rw</code> does not use <code>Pi.congr</code> or anything like it</p>

#### [ Mario Carneiro (Sep 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134751965):
<p>that's how <code>simp</code> works</p>

#### [ Mario Carneiro (Sep 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134752021):
<p><code>rw</code> only uses <code>eq.rec</code>, i.e. the substitution property of equality</p>

#### [ Reid Barton (Sep 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134752051):
<p>Right, okay. But <code>eq.rec</code> still has that argument we have to provide</p>

#### [ Mario Carneiro (Sep 27 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134752086):
<p>so your goal has to have the form <code>|- P a</code> in the current context, and it is given an equality <code>|- a = b</code>, again in the current context (it may have metavariables but they have to be resolved in the current context), to produce <code>|- P b</code></p>

#### [ Mario Carneiro (Sep 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134752175):
<p>In particular, it must be possible to write your goal as some function applied to the thing you want to rewrite, and this implies that it can't be a term that exists under a binder</p>

#### [ Mario Carneiro (Sep 27 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134752251):
<p>It's like you only know equality at one point and want to generalize to equality at all points - it doesn't work</p>

#### [ Mario Carneiro (Sep 27 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134752519):
<p>If you use a quantified equality as input to <code>rw</code>, it <em>first</em> applies some metavariables with the hope of matching them in the term, but before it has entered any binders. So that means you can always specify them yourself and give straight equations to <code>rw</code> with no loss of generality, unlike with <code>simp</code> where quantified equations are really more powerful</p>

#### [ Kevin Buzzard (Sep 27 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134752964):
<p>In my example, it's clear what I mean -- I want to rewrite "forall x, q(x)=0 -&gt; ..." as "forall x, (x=1 or x=2) -&gt; .."</p>

#### [ Kevin Buzzard (Sep 27 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134752988):
<p>There doesn't seem to be anything stopping that rewrite in theory</p>

#### [ Kevin Buzzard (Sep 27 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134753029):
<p>I can do it with intro, rw, revert. I'm not sure my users can though.</p>

#### [ Kevin Buzzard (Sep 27 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134753060):
<p>I guess they'll have to ;-)</p>

#### [ Mario Carneiro (Sep 27 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134753132):
<p>Of course, I follow. I'm just saying that's not how <code>rw</code> works</p>

#### [ Mario Carneiro (Sep 27 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134753150):
<p>the closest approximation to <code>rw</code> + binders is <code>conv {rw}</code></p>

#### [ Kevin Buzzard (Sep 27 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134753184):
<p>Thank you Mario for your explanation. I find now I'm a more mature Lean user that when things like this happen I am now interested in understanding why they're failing (rather than banging my head against a table)</p>

#### [ Kevin Buzzard (Sep 27 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134753303):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">lemma</span> <span class="n">quadroots</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">}</span> <span class="o">:</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">-</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">↔</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">2</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">,</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">-</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">quadroots</span><span class="o">],</span> <span class="c1">-- WORKS!</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Sep 27 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134753343):
<p>right. <code>simp</code> uses a different algorithm, based on congruence lemmas, which has the advantage that you can rewrite under binders</p>

#### [ Mario Carneiro (Sep 27 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134753465):
<p>Rather than trying to match the goal all in one go like <code>rw</code>, it recurses into the term with things like <code>funext</code> that actually give you the opportunity to bubble those equalities into the inner context</p>

#### [ Kevin Buzzard (Sep 27 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20under%20a%20pi/near/134753580):
<p>rofl just noticed example is mathematically wrong ;-) [forall needs to go inside the brackets]</p>


{% endraw %}
