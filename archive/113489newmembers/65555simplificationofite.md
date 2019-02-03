---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/65555simplificationofite.html
---

## Stream: [new members](index.html)
### Topic: [simplification of ite](65555simplificationofite.html)

---


{% raw %}
#### [ Ken Roe (Aug 11 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simplification%20of%20ite/near/131967259):
<p>How do I complete the following theorem:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">th</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">b</span> <span class="bp">→</span> <span class="o">(</span><span class="k">if</span> <span class="n">a</span><span class="bp">=</span><span class="n">b</span> <span class="k">then</span> <span class="mi">5</span> <span class="k">else</span> <span class="mi">3</span><span class="o">)</span><span class="bp">=</span><span class="mi">3</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intros</span><span class="o">,</span> <span class="bp">...</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Aug 11 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simplification%20of%20ite/near/131967372):
<p><code>simp *</code></p>

#### [ Chris Hughes (Aug 11 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simplification%20of%20ite/near/131967501):
<p>Also <code>rw if_neg h</code> if <code>h</code> is your proof of <code>a \ne b</code></p>

#### [ Simon Hudon (Aug 11 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simplification%20of%20ite/near/131967526):
<p>For <span class="user-mention" data-user-id="110044">@Chris Hughes</span> 's solution, you might make it clearer as <code>introv h, rw if_neg h</code>. As a habit, you should avoid referring to auto generated variable names.</p>

#### [ Patrick Massot (Aug 11 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simplification%20of%20ite/near/131967584):
<p>why <code>introv</code> instead of <code>intro</code> or <code>intros</code>?</p>

#### [ Patrick Massot (Aug 11 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simplification%20of%20ite/near/131967631):
<p>I would have done <code>intros a b h</code></p>

#### [ Simon Hudon (Aug 11 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simplification%20of%20ite/near/131967640):
<p>Because the two natural numbers already have a name and we can just keep them. The assumption however is anonymous in the statement and you should rely on the name given under the hood. Additionally, we don't refer to <code>a</code> and <code>b</code> in the proof so renaming them is not very useful.</p>

#### [ Patrick Massot (Aug 11 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simplification%20of%20ite/near/131967645):
<p>I didn't know that tactic!</p>

#### [ Simon Hudon (Aug 11 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simplification%20of%20ite/near/131967693):
<p>Pretty neat eh? :)</p>

#### [ Patrick Massot (Aug 11 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simplification%20of%20ite/near/131967704):
<p>what does the v stand for?</p>

#### [ Simon Hudon (Aug 11 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simplification%20of%20ite/near/131967708):
<p>Btw <span class="user-mention" data-user-id="121306">@Ken Roe</span>, feel free to migrate your questioning to the <code>general</code> stream of Zulip. <code>new members</code> is more for introductions I believe.</p>


{% endraw %}
