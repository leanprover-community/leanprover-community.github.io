---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66435Whattacticforcesbetareductioningoalorhypothesis.html
---

## Stream: [general](index.html)
### Topic: [What tactic forces beta reduction in goal or hypothesis](66435Whattacticforcesbetareductioningoalorhypothesis.html)

---


{% raw %}
#### [ Kevin Sullivan (Oct 10 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135516798):
<p>Clearly a newbie question -- but I don't see the answer at hand. Sorry to have to ask. E.g., if my current goal is 3 * 3 -= 8, how, in a tactic script, do I force the * expression to be evaluated, yielding 9 = 8 as the new goal?</p>

#### [ Simon Hudon (Oct 10 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135516869):
<p>If you're dealing with number literals, use <code>norm_num</code>. It works whether you have large numbers or small ones. Reduction will get pretty slow.</p>

#### [ Kevin Buzzard (Oct 10 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135521476):
<p>Because <code>3 * 3 = 9</code> is true by definition, if your goal is <code>3 * 3 = ...</code> then in tactic mode you can change it to <code>9 = ...</code> with the <code>show</code> tactic. </p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="mi">9</span> <span class="bp">=</span> <span class="mi">8</span><span class="o">)</span> <span class="o">:</span> <span class="mi">3</span> <span class="bp">*</span> <span class="mi">3</span> <span class="bp">=</span> <span class="mi">8</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">show</span> <span class="mi">9</span> <span class="bp">=</span> <span class="mi">8</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">h</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Oct 10 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135521541):
<p>The funny thing is that this works too:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="mi">9</span> <span class="bp">=</span> <span class="mi">8</span><span class="o">)</span> <span class="o">:</span> <span class="mi">3</span> <span class="bp">*</span> <span class="mi">3</span> <span class="bp">=</span> <span class="mi">8</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">exact</span> <span class="n">h</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>because Lean is quite happy to treat <code>3 * 3</code> and <code>9</code> as equal objects when attempting to convince itself that the hypothesis really is equal to the goal.</p>

#### [ Kevin Sullivan (Oct 10 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135541690):
<p>The more general case  is one where the current goal involves expressions in which functions are applied to arguments. I'm looking for the tactic that simplifies the goal by reducing all of the (or perhaps selected) function application expressions to values.</p>

#### [ Patrick Massot (Oct 10 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135541985):
<p>If you are ready to provide the new goal explicitly then <code>change</code> will do that</p>

#### [ Kevin Sullivan (Oct 10 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135542310):
<p>I was hoping to be able to just use a "simpl" (or whatever) tactic. Seems that Lean doesn't natively provide such a thing. I find that surprising.</p>

#### [ Patrick Massot (Oct 10 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135542359):
<p>Hold on</p>

#### [ Patrick Massot (Oct 10 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135542610):
<p>you could try something like:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span><span class="bp">.</span><span class="n">beta_red</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span> <span class="bp">`</span><span class="o">[</span><span class="n">dsimp</span> <span class="n">only</span> <span class="o">[]</span> <span class="o">{</span><span class="n">beta</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">}]</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>  <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="o">)</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">beta_red</span><span class="o">,</span>
  <span class="n">refl</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Oct 10 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135542635):
<p>and probably set other config flag to false</p>

#### [ Patrick Massot (Oct 10 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135542646):
<p>I think we already has the same discussion before (or a closely related one)</p>

#### [ Kevin Buzzard (Oct 10 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20tactic%20forces%20beta%20reduction%20in%20goal%20or%20hypothesis/near/135565975):
<p>Maybe <code>unfold</code> is what you're looking for? Do you want to post an example of what you're trying to do?</p>


{% endraw %}
