---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40901ringrefactoring.html
---

## [general](index.html)
### [ring refactoring](40901ringrefactoring.html)

#### [Kenny Lau (Nov 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring refactoring/near/147427723):
In the module refactoring, we turned `(N : set M) [is_submodule N]` into `(N: submodule R M)`, and we turned `(f : M -> N) (hf : is_linear_map f)` into `(f : linear_map M N)`. And I found this very helpful.

#### [Kenny Lau (Nov 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring refactoring/near/147427733):
Should we also change `(S : set R) [is_subring S]` into `(S : subring R)` and turn `(f : R -> S) [is_ring_hom f]` into `(f : ring_hom R S)`?

#### [Kenny Lau (Nov 10 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring refactoring/near/147427736):
@**Kevin Buzzard** @**Johan Commelin** @**Mario Carneiro**

#### [Kenny Lau (Nov 10 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring refactoring/near/147427742):
I think this would make defining / using algebras easier

#### [Kevin Buzzard (Nov 10 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring refactoring/near/147430470):
What do I know about this sort of thing? I tend to just see what the state of stuff is, and then try to write mathematics, and if I get stuck I ask here and then people that understand these infrastructure issues say things like "oh OK looks like we need to entirely refactor modules". Make all the changes you like; I will finish my UG course in 5 weeks' time and then I will start proving a bunch of lemmas about complete rings which we need for https://github.com/kbuzzard/lean-perfectoid-spaces/issues/25 and will certainly be reporting back here with any problems I find. This is exactly the sort of behaviour I am seeing people like @**Johan Commelin** and @**Patrick Massot**  doing too, and which I guess will be a common theme amongst people who have PhDs in mathematics -- they find a project, they try it, and then they report back on the bits where they had to fight Lean and offer partial insights which are then typically instantly understood by the more CS-y people who are much better at seeing to the core of the underlying problem and how to solve it. This is one of the reasons that this is such an amazing community.

#### [Chris Hughes (Nov 10 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring refactoring/near/147431769):
Same question for subgroups

#### [Johan Commelin (Nov 10 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring refactoring/near/147435630):
Intuitively, I really like bundling things. But there were good reasons not to bundle `group` and `is_group_hom` etc... I don't claim to understand these reasons. But I feel like the way an ITP can handle bundling is an extremely important feature. For mathematicians bundling and unbundling is completely transparent. In Lean I have the feeling we need both versions, and we also need to state lots of lemmas twice. But again, I'm not an expert, and these are mostly feelings...

