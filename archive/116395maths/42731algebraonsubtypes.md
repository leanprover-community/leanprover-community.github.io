---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/42731algebraonsubtypes.html
---

## Stream: [maths](index.html)
### Topic: [algebra on subtypes](42731algebraonsubtypes.html)

---


{% raw %}
#### [ Patrick Massot (Jul 19 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129923410):
@**Johan Commelin** Simon has been working for us, and Mario promptly merged. You can update mathlib to at least c2f54ad03 and try to understand how to use the magic in https://gist.github.com/PatrickMassot/8afef3917a917300cf31c1396a895705

#### [ Johan Commelin (Jul 19 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129926331):
Looks interesting! I'm updating (-;

#### [ Johan Commelin (Jul 19 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129926592):
I really like where this is going! You give it the data (zero, addition, ...) and for the properties (assoc, comm, ...) you just tell Lean: look, follow your nose and you'll get there.

#### [ Patrick Massot (Jul 19 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129926847):
Indeed. This now really looks like what you would wrote on paper: explain why operations make sense and then write either nothing  or "algebraic axioms follow from the parent structure axiom"

#### [ Patrick Massot (Jul 19 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129926851):
And this will be reused a lot. Each algebraic structure need subtype instances

#### [ Patrick Massot (Jul 19 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129926923):
Note that `refine_struct` is an ongoing long-term collaboration effort using all available strengths: I do the whining and Simon does the coding. It started with the `pi_instance` tactic back in February I think

#### [ Johan Commelin (Jul 19 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927028):
Ok, so here are some explicit kudos to @**Simon Hudon** :thumbs_up: :tada: :octopus: :cake: :hammer_and_wrench: :muscle:

#### [ Johan Commelin (Jul 19 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927113):
I do wonder, in how far is this overlapping with Scott's tactics? I don't fully understand what his `obviously` does, but it is also related to deriving obvious results from fields in structures and such, right?

#### [ Mario Carneiro (Jul 19 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927179):
`obviously` is one of several "hammer" style tactics by scott

#### [ Mario Carneiro (Jul 19 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927180):
i.e. "throw every automation we have at the problem until it buckles"

#### [ Mario Carneiro (Jul 19 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927242):
I don't think `refine_struct` does anything like this

#### [ Johan Commelin (Jul 19 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927259):
Agreed, but vice versa? Would most of these goals buckle under ~~Thor's~~ Scott's hammer?

#### [ Patrick Massot (Jul 19 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927315):
No, `refine_struct` by itself carefully understand and name what Lean wants to be proved. Then specialized automation like https://github.com/leanprover/mathlib/blob/master/algebra/pi_instances.lean#L16 or https://gist.github.com/PatrickMassot/8afef3917a917300cf31c1396a895705#file-subtypes-lean-L9 take over.

#### [ Johan Commelin (Jul 19 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927370):
Since Lean supports unicode, I think we really should have a tactic called [Mjölnir](https://en.wikipedia.org/wiki/Mj%C3%B6lnir).

#### [ Kevin Buzzard (Jul 19 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927543):
You should propose a unicode character for that thing

#### [ Patrick Massot (Jul 19 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927555):
Let's ask google how to spell that in runes

#### [ Patrick Massot (Jul 19 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927563):
And then we can email Jasmin and give him one more incentive to bring us that hammer thing

#### [ Patrick Massot (Jul 19 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927614):
Looks like this could be our winner: https://static1.fjcdn.com/comments/Spelled+the+right+way+_47df3c7a85289a0912599c30d252cf08.jpg

#### [ Kenny Lau (Jul 19 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927691):
```quote
Let's ask google how to spell that in runes
```
ᛗᛃᛟᛚᚾᛁᚱ

#### [ Mario Carneiro (Jul 19 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927701):
```lean
def ᛗᛃᛟᛚᚾᛁᚱ := by ᛗᛃᛟᛚᚾᛁᚱ
```

#### [ Patrick Massot (Jul 19 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927730):
Too bad: I tried `meta def ᛗᛃᛟᛚᚾᛁᚱ : tactic unit := sorry` but Lean complains `invalid declaration, identifier expected`

#### [ Patrick Massot (Jul 19 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927771):
It seems we'll need some help from @**Sebastian Ullrich**

#### [ Mario Carneiro (Jul 19 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927772):
```
meta def «ᛗᛃᛟᛚᚾᛁᚱ» : tactic unit := sorry 
```

#### [ Sean Leather (Jul 19 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927808):
Guillemets: how appropriate.

#### [ Mario Carneiro (Jul 19 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927817):
problem solved:
```lean
meta def «ᛗᛃᛟᛚᚾᛁᚱ» : tactic unit := sorry 
notation `ᛗᛃᛟᛚᚾᛁᚱ` := «ᛗᛃᛟᛚᚾᛁᚱ»
example : true := by ᛗᛃᛟᛚᚾᛁᚱ
```

#### [ Patrick Massot (Jul 19 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927870):
This works! We're almost set. It only remains to whine long enough for someone to unsorry this

#### [ Mario Carneiro (Jul 19 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927879):
obviously `meta def «ᛗᛃᛟᛚᚾᛁᚱ» : tactic unit :=  by ᛗᛃᛟᛚᚾᛁᚱ`

#### [ Johan Commelin (Jul 19 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927891):
I like your use of "obviously"

#### [ Patrick Massot (Jul 19 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927939):
We shouldn't forget the PR to https://github.com/leanprover/vscode-lean/blob/master/translations.json


{% endraw %}
