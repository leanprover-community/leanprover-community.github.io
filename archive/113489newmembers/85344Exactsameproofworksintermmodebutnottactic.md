---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/85344Exactsameproofworksintermmodebutnottactic.html
---

## Stream: [new members](index.html)
### Topic: [Exact same proof works in term mode but not tactic](85344Exactsameproofworksintermmodebutnottactic.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Nov 16 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147838170):
This works:
```lean
import data.real.basic
lemma DUH : abs (2 : ℝ) = (2 : ℝ) := abs_of_pos two_pos
```
This works:
```lean
import data.real.basic
lemma DUH : abs (2 : ℝ) = (2 : ℝ) := begin apply abs_of_pos, exact two_pos end
```
This doesn't work:
```lean
import data.real.basic
lemma DUH : abs (2 : ℝ) = (2 : ℝ) := begin apply abs_of_pos (two_pos) end
```
This doesn't work:
```lean
import data.real.basic
lemma DUH : abs (2 : ℝ) = (2 : ℝ) := begin apply @abs_of_pos _ _ 2 (two_pos) end
```
This works:
```lean
lemma DUH : abs (2 : ℝ) = (2 : ℝ) := begin rw abs_of_pos, exact two_pos end
```
This doesn't work:
```lean
lemma DUH : abs (2 : ℝ) = (2 : ℝ) := begin rw abs_of_pos (two_pos) end
```
Why? What's going on?

#### [ Abhimanyu Pallavi Sudhir (Nov 16 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147838350):
Oh, and this works: 

```lean
import data.real.basic
lemma DUH : abs (2 : ℝ) = (2 : ℝ) := begin exact abs_of_pos (two_pos) end
```

#### [ Abhimanyu Pallavi Sudhir (Nov 16 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147838487):
I can understand there may be some "metavariables make things weird" explanation for `exact` working where `apply` doesn't, but I really don't get why the two rewrites have different results.

#### [ Patrick Massot (Nov 16 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147839688):
This all about elaboration

#### [ Patrick Massot (Nov 16 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147839772):
The elaborator needs to guess the type of 2 in 2 > 0 (which is the statement of `two_pos`). When it tries to do that too early this fails

#### [ Patrick Massot (Nov 16 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147839801):
You could probably save all attempts by type ascribing this two_pos using `(two_pos : (2 : R) > 0)`

#### [ Abhimanyu Pallavi Sudhir (Nov 16 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147839856):
Ah yes, it seems `apply @abs_of_pos ℝ _ 2 (two_pos)` works too.

#### [ Abhimanyu Pallavi Sudhir (Nov 16 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147839979):
But how does that explain `exact` working where `apply` doesn't?

#### [ Mario Carneiro (Nov 16 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147840032):
apply needs to guess how many pis the result type has

#### [ Mario Carneiro (Nov 16 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147840095):
`apply x` is basically the same as `refine x _ _ _` where the number of underscores depends on the type of `x`

#### [ Mario Carneiro (Nov 16 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147840125):
This means that when elaborating `x` we don't know what type it is yet, while with `refine` or `exact` we know the type of `x` is the type of the goal

#### [ Abhimanyu Pallavi Sudhir (Nov 16 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exact%20same%20proof%20works%20in%20term%20mode%20but%20not%20tactic/near/147840325):
That makes sense. Thanks.


{% endraw %}
