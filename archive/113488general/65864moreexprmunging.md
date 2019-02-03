---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/65864moreexprmunging.html
---

## Stream: [general](index.html)
### Topic: [more expr munging](65864moreexprmunging.html)

---


{% raw %}
#### [ Scott Morrison (Sep 09 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133605425):
<p>Say I have an <code>expr</code> representing an iterated <code>pi</code> type, which is finally an equation, something like <code>Π (a : ℕ) (b : ℕ), f a b = g (a + b)</code>. From that, I want to produce <code>f ?m_1 ?m_2</code>, where <code>?m_1</code> and <code>?m_2</code> are newly created metavariables of the appropriate types.</p>

#### [ Scott Morrison (Sep 09 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133605426):
<p>Any suggestions?</p>

#### [ Reid Barton (Sep 09 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133605484):
<p>Are you guaranteed that the left hand side will be literally <code>&lt;something&gt; a b</code>, where <code>a</code> and <code>b</code> are the variables introduced by the Pis in order? Or could it be some arbitrary expression involving <code>a</code> and <code>b</code>?</p>

#### [ Simon Hudon (Sep 09 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133605574):
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">get_lhs</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">-&gt;</span> <span class="n">tactic</span> <span class="n">expr</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">pi</span> <span class="n">n</span> <span class="n">bi</span> <span class="n">d</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">v</span> <span class="bp">&lt;-</span> <span class="n">mk_local&#39;</span> <span class="n">n</span> <span class="n">bi</span> <span class="n">d</span><span class="o">,</span>
      <span class="n">b&#39;</span> <span class="bp">&lt;-</span> <span class="n">whnf</span> <span class="err">$</span> <span class="n">b</span><span class="bp">.</span><span class="n">instantiate_var</span> <span class="n">v</span>
      <span class="n">get_lhs</span> <span class="n">b&#39;</span>
<span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="err">%%</span><span class="n">a</span> <span class="bp">=</span> <span class="err">%%</span><span class="n">b</span><span class="o">)</span> <span class="o">:=</span> <span class="n">pure</span> <span class="n">a</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">failed</span>
</pre></div>

#### [ Reid Barton (Sep 09 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133605626):
<p>Yes this strategy is what I was about to suggest. Peel off one outer Pi at a type, leaving a formula with a free variable, and then substitute a fresh metavariable or whatever else you want for that free variable</p>

#### [ Simon Hudon (Sep 09 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133605631):
<p>Actually, we can be more direct:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">get_lhs</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">-&gt;</span> <span class="n">tactic</span> <span class="n">expr</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">pi</span> <span class="n">n</span> <span class="n">bi</span> <span class="n">d</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">v</span> <span class="bp">&lt;-</span> <span class="n">mk_meta_var</span> <span class="n">d</span><span class="o">,</span>
   <span class="n">b&#39;</span> <span class="bp">&lt;-</span> <span class="n">whnf</span> <span class="err">$</span> <span class="n">b</span><span class="bp">.</span><span class="n">instantiate_var</span> <span class="n">v</span>
   <span class="n">get_lhs</span> <span class="n">b&#39;</span>
<span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="err">%%</span><span class="n">a</span> <span class="bp">=</span> <span class="err">%%</span><span class="n">b</span><span class="o">)</span> <span class="o">:=</span> <span class="n">pure</span> <span class="n">a</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">failed</span>
</pre></div>

#### [ Scott Morrison (Sep 09 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133605633):
<p>(I'm doubly impressed, Simon, that your code often doesn't quite compile: there's a comma missing in that first one. :-)</p>

#### [ Simon Hudon (Sep 09 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133605674):
<p>Where would be the fun if you didn't have to fix my mistakes?</p>

#### [ Scott Morrison (Sep 09 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133605935):
<p>So I'm trying to do something a bit fancier here, and while <code>get_lhs</code> work as requested, really I want something more. :-)</p>

#### [ Simon Hudon (Sep 09 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133605958):
<p>I'm listening (sort of)</p>

#### [ Scott Morrison (Sep 09 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606018):
<p>I had written:</p>
<div class="codehilite"><pre><span></span>meta def substitutions&#39; : expr → bool → list expr →
  tactic (tactic (expr × expr × list expr))
| (expr.pi n bi d b) symm types :=
  do substitutions&#39; b symm (d :: types)
| `(%%lhs = %%rhs) symm types :=
  do let (lhs, rhs) := if symm then (rhs, lhs) else (lhs, rhs),
     let tac := (do mvars ← types.mmap mk_meta_var,
        let pattern := lhs.instantiate_vars mvars,
        ty ← infer_type pattern,
        return (pattern, ty, mvars)),
     return tac
| _ _ _ := failed
</pre></div>

#### [ Scott Morrison (Sep 09 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606035):
<p>The idea being to return a tactic, which could be invoked multiple times, each time producing the pattern with "fresh" mvars.</p>

#### [ Scott Morrison (Sep 09 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606043):
<p>However it's ... still somewhat mysteriously ... not working in all cases. (Sorry this is far from a MWE.)</p>

#### [ Reid Barton (Sep 09 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606101):
<p>Is this supposed to be more efficient than just invoking something like <code>get_lhs</code> repeatedly?</p>

#### [ Scott Morrison (Sep 09 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606180):
<p>Yeah, I guess so.</p>

#### [ Scott Morrison (Sep 09 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606184):
<p>But maybe I am needlessly complicating things. :-(</p>

#### [ Simon Hudon (Sep 09 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606203):
<p>I think you need to <code>reverse</code> <code>mvars</code></p>

#### [ Reid Barton (Sep 09 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606250):
<p>It's probably about equally or less efficient because the representation of that <code>tactic</code> object in the VM is going to be basically the same as or a more complicated structure than the outer Pis of the original type.</p>

#### [ Scott Morrison (Sep 09 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606328):
<p>Hmm. I had tried (on a purely voodoo basis) reversing <code>mvars</code>, without apparent success. Let me go away on de-complicate for a bit. :-)</p>

#### [ Scott Morrison (Sep 09 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606329):
<p>Thanks for the help!</p>

#### [ Simon Hudon (Sep 09 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606330):
<p>After squinting at it for a while, I agree with <span class="user-mention" data-user-id="110032">@Reid Barton</span></p>

#### [ Reid Barton (Sep 09 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606428):
<p>(Or at least, that would be true in the GHC runtime system, which is probably a terrible mental model for the Lean VM but the best one I have available.)</p>

#### [ Simon Hudon (Sep 09 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606476):
<p>My reasoning is that, for each bound variable, the expensive thing is <code>instantiate_var</code>, the number of which does not decrease in this approach</p>

#### [ Reid Barton (Sep 09 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606495):
<p>Right, you only save the decomposition of the Pis.</p>

#### [ Reid Barton (Sep 09 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606593):
<p>Which is cheap anyways, but to make things worse, you replace it by having to do an equal number of applications-of-variable-functions (the inner <code>tactic</code>which you build up).</p>

#### [ Reid Barton (Sep 09 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606693):
<p>Oh wait, you implemented it in a way so that there is only one closure being built (<code>tac</code>), but still each invocation of <code>tac</code> has to process the list <code>types</code>, which has the same information as the outer Pis of the original expression.</p>

#### [ Scott Morrison (Sep 09 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606774):
<p>and, happily it all seems to work now!</p>

#### [ Scott Morrison (Sep 09 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606776):
<p>(or at least the "all" that I hoped to have done tonight!)</p>


{% endraw %}
