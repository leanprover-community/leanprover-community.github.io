---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56242Howtoprovevalsucceqsuccval.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [How to prove val_succ_eq_succ_val](https://leanprover-community.github.io/archive/113488general/56242Howtoprovevalsucceqsuccval.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (May 15 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126591309):
<p>This feels almost defeq to me. But I am stumped how to prove this:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">val_succ_eq_succ_val</span> <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">j</span><span class="bp">.</span><span class="n">succ</span><span class="bp">.</span><span class="n">val</span> <span class="bp">=</span> <span class="n">j</span><span class="bp">.</span><span class="n">val</span><span class="bp">.</span><span class="n">succ</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Sean Leather (May 15 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126591395):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">val_succ_eq_succ_val</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">j</span><span class="bp">.</span><span class="n">succ</span><span class="bp">.</span><span class="n">val</span> <span class="bp">=</span> <span class="n">j</span><span class="bp">.</span><span class="n">val</span><span class="bp">.</span><span class="n">succ</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">cases</span> <span class="n">j</span><span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="n">fin</span><span class="bp">.</span><span class="n">succ</span><span class="o">]</span>
</pre></div>

#### [ Johan Commelin (May 15 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126591498):
<p>Aaaahaaa.</p>

#### [ Patrick Massot (May 15 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592224):
<p>I think we should add this sentence to our bluff toolbox. Instead of saying "the following is trivial", as we always do, we could say "the following is almost defeq".</p>

#### [ Patrick Massot (May 15 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592283):
<p>People may think we are a bit weird (at least until proof assistant manage to take over the world).</p>

#### [ Patrick Massot (May 15 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592313):
<p>But it won't be worse than all those students who took Kevin's exam on Monday and will get as their only explanation for poor grade: this doesn't type check.</p>

#### [ Patrick Massot (May 15 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592377):
<p>Actually I'm reading this because I procrastinate writing a referee report. I should send "this paper does not type check" and be done with it</p>

#### [ Kevin Buzzard (May 15 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592408):
<p>I have taken off many points for solutions which don't type-check.</p>

#### [ Kevin Buzzard (May 15 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592466):
<p>I ask them what <code>P_4(X)</code> is, and many people tell me that it is <code>8cos(theta)^4-8cos(theta)^2+1</code></p>

#### [ Kevin Buzzard (May 15 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592475):
<p>[P_n(X) satisfies P_n(cos(theta))=cos(n.theta)]</p>

#### [ Patrick Massot (May 15 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592507):
<p>Right now I'm staring at some <code>wlog</code> without filling in the proof obligation in that paper I need to referee</p>

#### [ Kevin Buzzard (May 15 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592537):
<p>One student wrote down the answer and said it was true "by symmetry"</p>

#### [ Kevin Buzzard (May 15 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592577):
<p>and I thought "hmm, I don't think that will work in Lean"</p>

#### [ Kevin Buzzard (May 15 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126592579):
<p>but at least it typechecks</p>

#### [ Reid Barton (May 15 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126599292):
<p>Replying to the original question; alternatively</p>
<div class="codehilite"><pre><span></span><span class="k">by</span> <span class="n">cases</span> <span class="n">j</span><span class="bp">;</span> <span class="n">refl</span>
</pre></div>


<p>which shows how almost-defeq it really is</p>

#### [ Johan Commelin (May 15 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126601422):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Should this be in mathlib?</p>

#### [ Johan Commelin (May 15 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126601623):
<p>And the analogue for <code>pred</code>.</p>

#### [ Johan Commelin (May 15 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126601692):
<p>More generally: should I just create PR's for such small additions, or is it too trivial for that?</p>

#### [ Mario Carneiro (May 15 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126610125):
<p>Small additions are fine, since they are focused and usually don't have dependency problems they are easy to review. I think it is not a good idea to have a lower bound on "too trivial" because then you have to find other things to do in the PR or forget about your little fix. It's rules like that that make typos like <code>αdditive</code> persist in lean core for so long</p>

#### [ Mario Carneiro (May 15 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126610143):
<p>I would call the theorem <code>succ_val</code> though</p>

#### [ Johan Commelin (May 16 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20to%20prove%20val_succ_eq_succ_val/near/126660987):
<p>Done: <a href="https://github.com/leanprover/mathlib/pull/138" target="_blank" title="https://github.com/leanprover/mathlib/pull/138">https://github.com/leanprover/mathlib/pull/138</a></p>


{% endraw %}
