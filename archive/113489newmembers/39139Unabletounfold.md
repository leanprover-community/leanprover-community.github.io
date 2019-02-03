---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/39139Unabletounfold.html
---

## Stream: [new members](index.html)
### Topic: [Unable to unfold](39139Unabletounfold.html)

---


{% raw %}
#### [ AHan (Nov 02 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136968269):
<p>I'm trying to prove the prime field addition that I defined is correct,  but somehow I can't unfold the equation...<br>
<a href="https://gist.github.com/potsrevennil/0cbf2204a8a16daa6eab367f153be748#file-primefield-lean-L71" target="_blank" title="https://gist.github.com/potsrevennil/0cbf2204a8a16daa6eab367f153be748#file-primefield-lean-L71">https://gist.github.com/potsrevennil/0cbf2204a8a16daa6eab367f153be748#file-primefield-lean-L71</a></p>

#### [ Mario Carneiro (Nov 02 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136968471):
<p>from your definitions it looks like the proof is just <code>eq.symm (add_equiv _)</code></p>

#### [ Mario Carneiro (Nov 02 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136968579):
<p>if you want to get at this by unfolding, you should <code>dsimp [pf.add, (+)]</code>, although this might unfold too much</p>

#### [ Mario Carneiro (Nov 02 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136968646):
<p>normally we would state a simp lemma expressing the definitional unfolding here, exactly because it's hard to get at unless you say it explicitly</p>

#### [ AHan (Nov 02 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136968659):
<p>what's dism's usage?<br>
And why is that I can unfold eq in add_equiv but not of_int_add?</p>

#### [ Mario Carneiro (Nov 02 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136968681):
<p>because <code>of_int_add</code> does not have the form <code>of_int ... = of_int ...</code></p>

#### [ Mario Carneiro (Nov 02 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136968726):
<p>you have to unfold the addition on the lhs first, then you can unfold eq</p>

#### [ Mario Carneiro (Nov 02 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136968747):
<p><code>dsimp</code> and <code>unfold</code> are very similar, they are implemented as the same tactic behind the scenes with different configuration options</p>

#### [ Mario Carneiro (Nov 02 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136968759):
<p>in this case it's just because <code>dsimp</code> accepts operators like <code>(+)</code> for simplifying and <code>unfold</code> doesn't</p>

#### [ AHan (Nov 02 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136968824):
<p>oh yes  I should unfold addition first!<br>
But after unfold add, I still cannot unfold eq....</p>

#### [ AHan (Nov 02 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136970809):
<p>Anyway <code>eq.symm (add_equiv _)</code> is really a nice solution, thanks a lot!</p>


{% endraw %}
