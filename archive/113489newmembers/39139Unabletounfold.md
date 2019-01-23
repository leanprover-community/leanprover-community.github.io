---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/39139Unabletounfold.html
---

## Stream: [new members](index.html)
### Topic: [Unable to unfold](39139Unabletounfold.html)

---

#### [AHan (Nov 02 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136968269):
I'm trying to prove the prime field addition that I defined is correct,  but somehow I can't unfold the equation...
https://gist.github.com/potsrevennil/0cbf2204a8a16daa6eab367f153be748#file-primefield-lean-L71

#### [Mario Carneiro (Nov 02 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136968471):
from your definitions it looks like the proof is just `eq.symm (add_equiv _)`

#### [Mario Carneiro (Nov 02 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136968579):
if you want to get at this by unfolding, you should `dsimp [pf.add, (+)]`, although this might unfold too much

#### [Mario Carneiro (Nov 02 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136968646):
normally we would state a simp lemma expressing the definitional unfolding here, exactly because it's hard to get at unless you say it explicitly

#### [AHan (Nov 02 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136968659):
what's dism's usage?
And why is that I can unfold eq in add_equiv but not of_int_add?

#### [Mario Carneiro (Nov 02 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136968681):
because `of_int_add` does not have the form `of_int ... = of_int ...`

#### [Mario Carneiro (Nov 02 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136968726):
you have to unfold the addition on the lhs first, then you can unfold eq

#### [Mario Carneiro (Nov 02 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136968747):
`dsimp` and `unfold` are very similar, they are implemented as the same tactic behind the scenes with different configuration options

#### [Mario Carneiro (Nov 02 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136968759):
in this case it's just because `dsimp` accepts operators like `(+)` for simplifying and `unfold` doesn't

#### [AHan (Nov 02 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136968824):
oh yes  I should unfold addition first!
But after unfold add, I still cannot unfold eq....

#### [AHan (Nov 02 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unable%20to%20unfold/near/136970809):
Anyway `eq.symm (add_equiv _)` is really a nice solution, thanks a lot!

