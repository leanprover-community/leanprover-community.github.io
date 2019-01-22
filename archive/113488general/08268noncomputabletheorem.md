---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08268noncomputabletheorem.html
---

## [general](index.html)
### [noncomputable theorem](08268noncomputabletheorem.html)

#### [Reid Barton (Oct 19 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable theorem/near/136123067):
Is there any sense in writing `noncomputable theorem`, as in mathlib `logic.basic` lines 516-519?

#### [Simon Hudon (Oct 19 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable theorem/near/136124051):
What happens if you remove `noncomputable`?

#### [Reid Barton (Oct 19 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable theorem/near/136124347):
Probably I wait a long time for mathlib to rebuild and then nothing interesting happens--I've written lots of `theorem`s that use noncomputable things before.

#### [Reid Barton (Oct 19 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable theorem/near/136124359):
I wonder whether they should be `noncomputable def`, or just `theorem`, or maybe none of this matters

#### [Reid Barton (Oct 19 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable theorem/near/136124519):
Actually I could be wrong--these `theorem`s are special because their result types are not Props (that's why I'm looking at them), and maybe that is what triggers the `noncomputable` check

#### [Reid Barton (Oct 19 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable theorem/near/136124688):
Okay yes, that seems to be the case.

#### [Reid Barton (Oct 19 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable theorem/near/136125141):
I never thought about exactly what is going on with `def` and `theorem`. I guess the difference is like `let` vs `have`, that is, something defined with `def` can be replaced by its definition by one of the reduction rules, while something defined with `theorem` can't be replaced by, well, its proof?

#### [Reid Barton (Oct 19 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable theorem/near/136125354):
The VM can't reduce a `theorem` either, right? So why bother with the `noncomputable` check for theorems?

#### [Reid Barton (Oct 19 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable theorem/near/136125488):
In the case of `classical.dec` I guess someone decided that it was useless to allow it to be unfolded because it's essentially just an application of an axiom, and it's uniquely determined up to propositional equality, anyways?

#### [Reid Barton (Oct 19 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable theorem/near/136125590):
This all seems to make sense, I'm just not sure my mental picture is actually correct.

#### [Simon Hudon (Oct 19 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable theorem/near/136129728):
I'm wondering if it's about generating byte code for the VM. If the theorem's type is in `Prop`, then, it doesn't matter.

#### [Simon Hudon (Oct 19 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable theorem/near/136129843):
But otherwise, you may have to say explicitly "Don't generate code" with `noncomputable`

#### [Mario Carneiro (Oct 20 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable theorem/near/136143543):
If you mark something as *either* `noncomputable` or `theorem`, then the VM does not generate code for the definition. This is why sometimes you get those errors about bytecode generation failed when you accidentally mark something as a `theorem`

#### [Mario Carneiro (Oct 20 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable theorem/near/136143755):
`noncomputable theorem` is almost always not needed, but it is used in a few specialized instances. One other consequence of defining something as a `theorem` is that it is "definition irrelevant", that is, lean will not generate or use the definitional equation for this definition. This is almost never appropriate for a `Type` valued expression, since it provides relations between definiendum and definiens that we can't otherwise recover. So the place where it makes sense is when the definition is already ambiguous, as in `classical.some` - unfolding it will not tell us any more about its value - and it is also using the axiom of choice so it should not have any code generation.

#### [Mario Carneiro (Oct 20 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noncomputable theorem/near/136143757):
@**Reid Barton**

