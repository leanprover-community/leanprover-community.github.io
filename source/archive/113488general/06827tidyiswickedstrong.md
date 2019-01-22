---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/06827tidyiswickedstrong.html
---

## [general](index.html)
### [tidy is wicked strong](06827tidyiswickedstrong.html)

#### [Johan Commelin (Aug 03 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130822631):
Kudos to Scott!
```lean
instance LeftMod__has_ZeroObject : @universal.has_ZeroObject (R-Mod) LeftMod_.foo :=
{ zero_object :=
{ zero_object := zero_module R,
  is_initial  := ⟨λ M : R-Mod, ⟨λ _, 0, is_linear_map.map_zero⟩,
  begin
    intros M f g,
    tidy,
    rw [← zero_is_star, is_linear_map.zero f_property, is_linear_map.zero g_property]
  end ⟩,
  is_terminal := by tidy
} }
```

#### [Johan Commelin (Aug 03 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130822638):
I just told Lean the definition of the zero-module. And it figured out on its own that it is the terminal object in the category of left modules!
Mind you: I wrote only 1 `rfl`-lemma to help it:
```lean
lemma zero_is_star : (0 : (zero_module R)) = star := rfl
```

#### [Johan Commelin (Aug 03 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130822683):
It needs a bit of hand-holding for the initial object, but I guess this is only because `is_linear_map` is not a class.

#### [Johan Commelin (Aug 03 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130822696):
Long live @**Scott Morrison**! Blacksmith of hammer tactics!

#### [Johan Commelin (Aug 03 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130824101):
Ooh, and `obviously` also does the job.

#### [Kevin Buzzard (Aug 03 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130824817):
It's slowly dawning on me that my initial impression ("`tidy` is something Scott wrote to help with his category theory stuff, and it does category theory stuff") is completely wrong, and that `tidy` and `obviously` are really all-purpose tools which will help us all. But they are not even part of a PR, right? Is there some kind of plan to get them PR'ed somehow, and what are the obstructions to getting them into mathlib?

#### [Scott Morrison (Aug 03 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130824972):
Hi Kevin, `tidy` doesn't do all that much, but I agree it's helpful. Really we need to carefully read <https://arxiv.org/abs/1309.4501> and translate it all into Lean, and then we'll really have the start of a hammer that mathematicians appreciate.

#### [Scott Morrison (Aug 03 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825014):
`tidy` is relatively easy to PR to mathlib, and hopefully I will have time soon to start doing this

#### [Scott Morrison (Aug 03 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825017):
many of the gross aspects of it have become cleaner in the last month

#### [Scott Morrison (Aug 03 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825043):
`obviously` is just `tidy` equipped with an extra tactic, called `rewrite_search`, which uses edit-distance based heuristics to search for chains of rewrites to prove equational results.

#### [Scott Morrison (Aug 03 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825061):
it is harder to PR, both because the implementation is really awful, and a student is actively working on cleverer (i.e. using machine learning in the heuristics) versions, so it's a moving target

#### [Scott Morrison (Aug 03 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825112):
(actually, secretly I'm hoping that he will rewrite `rewrite_search` from scratch for me, when he realises how awful it is)

#### [Minchao Wu (Aug 03 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825305):
@**Scott Morrison**  who is the student? I'm also interested in applying machine learning to heuristics

#### [Kenny Lau (Aug 03 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825314):
@**Kevin Buzzard** did one of your students mention machine learning?

#### [Johan Commelin (Aug 03 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825391):
It seems that Mohan Ganesalingam completely left the field.

#### [Scott Morrison (Aug 03 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825447):
@**Minchao Wu** , it's Keeley Hoek, who is sometimes around here. (Also, as we're all in the same building, we should really meet up --- my apologies that I screwed up our last attempt to do so.)

#### [Scott Morrison (Aug 03 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825465):
@**Kevin Buzzard**, have you ever read that Ganesalingam-Gowers paper? If not, you really should. :-)

#### [Minchao Wu (Aug 03 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825523):
No worries :) Is the student also from the math department?

#### [Johan Commelin (Aug 03 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825616):
It's really a pity that the "future work" never materialised. I think Gowers also changed subject...

#### [Scott Morrison (Aug 03 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825624):
Well... Gowers was only ever a visitor... :-)

#### [Minchao Wu (Aug 03 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825634):
If he's coming next week we can just schedule a group meeting maybe

#### [Scott Morrison (Aug 03 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825682):
It is such a pity that they did their work in their own private interactive theorem prover, so it's not usable by the rest of us.

#### [Scott Morrison (Aug 03 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825683):
(Typical mathematicians! :-)

#### [Rob Lewis (Aug 03 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130832892):
@**Scott Morrison** Are you/your student familiar with the work on TacticToe? http://cl-informatik.uibk.ac.at/users/cek/docs/17/tgckju-lpar17.pdf They've been relatively successful with ML-guided tactic proofs in HOL4. One of the more impressive results at AITP this year, in my opinion.

#### [Scott Morrison (Aug 03 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130832996):
Thanks @**Rob Lewis** for the reference. This is very different than what we're trying.

