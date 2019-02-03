---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79543automaticcases.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [automatic cases](https://leanprover-community.github.io/archive/113488general/79543automaticcases.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Jul 28 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20cases/near/130457556):
<p>Can we have a tactic that does <code>cases</code> on the argument of <code>XX.rec</code> or <code>XX.rec_on</code>?</p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20cases/near/130457669):
<p>That sounds like a really nice basic tactic for a tactic-learner to write!</p>

#### [ Kenny Lau (Jul 28 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20cases/near/130457886):
<p>good! are you a tactic-learner?</p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20cases/near/130458769):
<p>Maybe <span class="user-mention" data-user-id="110044">@Chris Hughes</span> is? I think he got a bit disheartened when he realised he had 100 questions and couldn't face asking Mario and Simon all of them though...</p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20cases/near/130458770):
<p>(and of course I was no help)</p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20cases/near/130458776):
<p>Maybe there should be a basic tactic-writing thread. The workflow I see is: start Zulip thread, spam it with basic questions which are not covered in PIL, experts occasionally make insightful comments, someone writes some notes and sticks them up in the mathlib docs project, we all learn something.</p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20cases/near/130458988):
<p>From Programming In Lean:</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">tactic</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">destruct_conjunctions</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">repeat</span> <span class="o">(</span><span class="n">do</span>
<span class="n">l</span> <span class="err">←</span> <span class="n">local_context</span><span class="o">,</span>
<span class="n">first</span> <span class="err">$</span> <span class="n">l</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">do</span>
<span class="n">ht</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">h</span> <span class="bp">&gt;&gt;=</span> <span class="n">whnf</span><span class="o">,</span>
<span class="k">match</span> <span class="n">ht</span> <span class="k">with</span>
<span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="n">and</span> <span class="err">%%</span><span class="n">a</span> <span class="err">%%</span><span class="n">b</span><span class="o">)</span> <span class="o">:=</span> <span class="n">do</span>
<span class="n">n</span> <span class="err">←</span> <span class="n">get_unused_name</span> <span class="bp">`</span><span class="n">h</span> <span class="n">none</span><span class="o">,</span>
<span class="n">mk_mapp</span> <span class="bp">``</span><span class="n">and</span><span class="bp">.</span><span class="n">left</span> <span class="o">[</span><span class="n">none</span><span class="o">,</span> <span class="n">none</span><span class="o">,</span> <span class="n">some</span> <span class="n">h</span><span class="o">]</span> <span class="bp">&gt;&gt;=</span> <span class="n">assertv</span> <span class="n">n</span> <span class="n">a</span><span class="o">,</span>
<span class="n">n</span> <span class="err">←</span> <span class="n">get_unused_name</span> <span class="bp">`</span><span class="n">h</span> <span class="n">none</span><span class="o">,</span>
<span class="n">mk_mapp</span> <span class="bp">``</span><span class="n">and</span><span class="bp">.</span><span class="n">right</span> <span class="o">[</span><span class="n">none</span><span class="o">,</span> <span class="n">none</span><span class="o">,</span> <span class="n">some</span> <span class="n">h</span><span class="o">]</span> <span class="bp">&gt;&gt;=</span> <span class="n">assertv</span> <span class="n">n</span> <span class="n">b</span><span class="o">,</span>
<span class="n">clear</span> <span class="n">h</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">failed</span>
<span class="kn">end</span><span class="o">))</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">HPQ</span> <span class="o">:</span> <span class="n">P</span> <span class="bp">∧</span> <span class="n">Q</span><span class="o">)</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">destruct_conjunctions</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">false</span><span class="bp">.</span><span class="n">intro</span>
<span class="kn">end</span>
</pre></div>


<p>That's how to break up an <code>and</code> in the hypotheses. You just want to break up a <code>rec</code> in the conclusion. How hard can it be? ;-)</p>

#### [ Johan Commelin (Jul 28 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20cases/near/130459043):
<blockquote>
<p>Maybe there should be a basic tactic-writing thread. The workflow I see is: start Zulip thread, spam it with basic questions which are not covered in PIL, experts occasionally make insightful comments, someone writes some notes and sticks them up in the mathlib docs project, we all learn something.</p>
</blockquote>
<p>Or a "tactics" stream? We've got a "maths" stream after all. This seems like a general enough topic (in the non-Zulip sense) to turn it into a stream.</p>


{% endraw %}
