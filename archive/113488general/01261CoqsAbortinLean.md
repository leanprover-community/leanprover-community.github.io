---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01261CoqsAbortinLean.html
---

## Stream: [general](index.html)
### Topic: [Coq's Abort in Lean](01261CoqsAbortinLean.html)

---


{% raw %}
#### [ Kevin Sullivan (Oct 08 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135406580):
<p>What is Lean's equivalent of Abort in Coq?</p>

#### [ Mario Carneiro (Oct 08 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135406598):
<p>what does it do?</p>

#### [ Kevin Sullivan (Oct 08 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135406720):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Abort terminates (gives up on) a failing or incomplete proof (whereas Coq's "Admitted" gives up and accepts the proposition being proved as an axiom, like sorry in Lean).</p>

#### [ Mario Carneiro (Oct 08 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135406812):
<p>Lean doesn't have this. I guess it makes more sense with the line-based input approach to coq</p>

#### [ Mario Carneiro (Oct 08 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135406836):
<p>but in lean once you have written <code>def</code> you are committed to either finishing it or getting an error or warning</p>

#### [ Kevin Sullivan (Oct 08 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135407728):
<p>For pedagogical purposes in any case it'd be good to have, as one can then exhibit proof strategies that don't work out. Students can see how the tactic state evolves until one gets stuck and gives up.</p>

#### [ Mario Carneiro (Oct 08 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135407747):
<p>Usually we use <code>sorry</code> for that</p>

#### [ Kevin Sullivan (Oct 08 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135418308):
<p>Yes but sorry accepts the proposition axiomatically, which in general is not what one wants to do. E.g., when showing why P \or \not P isn't provable without em.</p>

#### [ Simon Hudon (Oct 08 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135418336):
<p>You can use <code>run_cmd</code>: it allows you to run tactics and failing to prove the goal has no consequences</p>

#### [ Sebastian Ullrich (Oct 08 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135418499):
<p><code>example</code> may be more appropriate in that case</p>

#### [ Simon Hudon (Oct 08 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135418627):
<p><code>example</code> has the down side that, if you use <code>sorry</code>, it still produces warnings.</p>

#### [ Mario Carneiro (Oct 08 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135418882):
<p>There is always the trick used in the tests: use <code>sorry</code> in a <code>have</code> subproof that doesn't get used</p>

#### [ Kevin Sullivan (Oct 09 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135478380):
<blockquote>
<p>There is always the trick used in the tests: use <code>sorry</code> in a <code>have</code> subproof that doesn't get used</p>
</blockquote>
<p>There are work-arounds, albeit with some compromises, but wouldn't it be cleaner to just provide an "abort" tactic. The context for this suggestion is not expert use of Lean but rather early undergraduate education, where every inelegant complexity causes additional pain and suffering amongst students.</p>

#### [ Sebastian Ullrich (Oct 09 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479771):
<p>Note that <code>Abort</code> is not a tactic but a built-in command in Coq. We would need to change the <code>begin...end</code> syntax and parts of the elaborator for something similar.</p>

#### [ Rob Lewis (Oct 09 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479775):
<p>From what (little) I know about Coq, <code>Abort</code> isn't a tactic, it's a top-level command. I don't think there's a way to implement it as a tactic in Lean 3, at least not in a way that mimics the usage of the Coq command. This seems like the kind of thing you might be able to do in Lean 4.</p>

#### [ Sebastian Ullrich (Oct 09 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479780):
<p>Nice timing :)</p>

#### [ Rob Lewis (Oct 09 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479782):
<p>Haha, good timing!</p>

#### [ Sebastian Ullrich (Oct 09 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479784):
<p>:D</p>

#### [ Patrick Massot (Oct 09 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479789):
<p>Amazing duo</p>

#### [ Rob Lewis (Oct 09 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479859):
<p>To keep repeating Sebastian, I agree that using <code>example</code> is the Lean-style way to do this.</p>

#### [ Rob Lewis (Oct 09 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479876):
<p>To show a failing proof attempt, start an example and don't finish it.</p>

#### [ Patrick Massot (Oct 09 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479889):
<p>No, the Lean way is to finish the proof.</p>

#### [ Rob Lewis (Oct 09 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479907):
<p>There's no problem leaving an attempt unfinished like there is in Coq, it doesn't stop the processing of future declarations.</p>

#### [ Patrick Massot (Oct 09 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135479921):
<p>Even if <code>==</code> suddenly appear in the proof</p>

#### [ Simon Hudon (Oct 09 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135494007):
<p>What if we treated <code>abort</code> like <code>sorry</code> except that, when it appears in an example, it doesn't produce warnings?</p>

#### [ Kevin Sullivan (Oct 10 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135516025):
<blockquote>
<p>What if we treated <code>abort</code> like <code>sorry</code> except that, when it appears in an example, it doesn't produce warnings?</p>
</blockquote>
<p>It would need both (1) to not produce warnings, and (2) to not accept the goal axiomatically.</p>
<p>And, yes,  to Rob L. Abort is a command, not a tactic, in Coq.</p>
<p>By the way, Coq's command, analogous to Lean's sorry, is Admitted. It gives up on the current proof and accepts the goal axiomatically. By contrast, Abort gives up on the current proof but discards rather than accepts the current goal.</p>

#### [ Simon Hudon (Oct 10 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135516089):
<p>I think examples can't be invoked from other proofs so that part is already there.</p>

#### [ Rob Lewis (Oct 10 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135528161):
<p>I've only used Coq for  simple things. Specifically, I don't know how <code>Abort</code> works in nested proofs like they describe in the manual. Here's something that very roughly approximates its behavior in the top-level case. If you use <code>example</code>, the environment will be the same before and after processing this, and there are no warnings. </p>
<div class="codehilite"><pre><span></span><span class="kn">constant</span> <span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="n">abort</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span> <span class="o">:</span> <span class="n">α</span>

<span class="kn">open</span> <span class="n">tactic</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span><span class="bp">.</span><span class="n">abort</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">all_goals</span> <span class="bp">`</span><span class="o">[</span><span class="n">exact</span> <span class="n">abort</span><span class="o">]</span>

<span class="kn">example</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="mi">0</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="n">abort</span>
<span class="kn">end</span>
</pre></div>

#### [ Rob Lewis (Oct 10 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coq%27s%20Abort%20in%20Lean/near/135528193):
<p>But I still think the Lean-style way to do this is to just leave the example unfinished.</p>


{% endraw %}
