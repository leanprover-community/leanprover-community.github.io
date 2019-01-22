---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22086computableminreal.html
---

## [general](index.html)
### [computable min (real)](22086computableminreal.html)

#### [Kenny Lau (Mar 14 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123699788):
Do we have a computable function that gives the minimum of two real numbers?

#### [Chris Hughes (Mar 14 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123701880):
I don't think so. Why not write one?

#### [Andrew Ashworth (Mar 14 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123702327):
the way reals are defined, how could you decide if any two arbitrary reals are smaller than another

#### [Andrew Ashworth (Mar 14 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123702332):
two cauchy sequences could differ only in the eleventy billionth term

#### [Chris Hughes (Mar 14 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123702377):
I'm pretty sure it's not possible. Although if reals were implemented differently it might be, so long as they weren't equal.

#### [Kevin Buzzard (Mar 14 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123704162):
If the reals were given as actual Cauchy sequences (as some are I guess) then you could just take the min of the Cauchy sequences I guess. But if you just had the equivalence class then what can you do?

#### [Andrew Ashworth (Mar 14 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123712992):
turns out i am mistaken, btw, earlier i mentioned it being hard to compute with cauchy sequences

#### [Andrew Ashworth (Mar 14 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123713037):
actually i'm watching a presentation on how somebody did exactly that

#### [Andrew Ashworth (Mar 14 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123713041):
http://videolectures.net/aug09_spitters_oconnor_cvia/

#### [Andrew Ashworth (Mar 14 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123713079):
unfortunately it looks like producing that library was enough work that it was somebody's PhD dissertation

#### [Andrew Ashworth (Mar 14 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123713300):
Bishop would be proud

#### [Chris Hughes (Mar 14 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123719063):
@**Kevin Buzzard** quotients are computed as the objects they were quotiented from, so lean has access to the actual cauchy sequences. But how do you find the min of two cauchy sequences in general?

#### [Kevin Buzzard (Mar 14 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123719304):
If you have two real numbers represented as Cauchy sequences of rationals then you can just take the termwise min and this will be Cauchy and tend to the min (this is a good exercise ;-) ) ; equality is decidable on the rationals so this shouldn't be a problem I guess. Or am I missing something?

#### [Chris Hughes (Mar 14 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123719909):
No, I didn't think of that.

#### [Kenny Lau (Mar 14 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123723307):
that's actually exactly the point of this thread. Real inequality is undecidable, but the min function is computable.

#### [Mario Carneiro (Mar 14 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123723311):
As Kevin says, given two cauchy sequences and a continuous function of two reals (extending a function on rat) that you want to compute, you can get a cauchy sequence by applying the function pointwise. At no point do you need to decide inequality

#### [Kenny Lau (Mar 14 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123723398):
is it easy to do in Lean?

#### [Mario Carneiro (Mar 14 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123723646):
Sure, you would just need to show that `min` is uniformly continuous, which isn't so hard (i.e. `|min x y - min z w| <= |x - z| + |y - w|`)

#### [Kenny Lau (Mar 14 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123723838):
which theorem should I use, after showing that it is uniformly continuous?

#### [Chris Hughes (Mar 14 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123724023):
`def rmin : cau_seq ℚ abs → cau_seq ℚ abs → cau_seq ℚ abs := 
λ ⟨x, hx⟩ ⟨y, hy⟩, ⟨λ n, min (x n) (y n), λ ε ε0, begin end⟩`

#### [Chris Hughes (Mar 14 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123724031):
and then lift to R

#### [Kenny Lau (Mar 14 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123724048):
and then one would have to prove that the lift is well-defined

#### [Mario Carneiro (Mar 14 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123724101):
That will be the major part of showing that the sequence `min (f n) (g n)` is cauchy. Then you have to prove that when two cauchy sequences are near their output is also near, so that this lifts to a function on reals. Finally, you prove that it is in fact the min: it is clearly le than reals `x` and `y`, and if `z <= x` and `z <= y` then `z <= min x y`.

#### [Kenny Lau (Mar 14 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20min%20%28real%29/near/123724108):
right

