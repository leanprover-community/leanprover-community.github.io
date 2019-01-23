---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/34165products.html
---

## Stream: [general](index.html)
### Topic: [products](34165products.html)

---

#### [Patrick Massot (Jul 30 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130544059):
If I have `(a b c : Type) (f : a → b) (g : a → c)`, do we have a name or notation for the function mapping `x` to `(f x, g x)`?

#### [Sebastian Ullrich (Jul 30 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545155):
We probably don't yet, but Haskell has one, if anyone wants to copy that
```
> :t (&&&)
(&&&) :: Arrow a => a b c -> a b c' -> a b (c, c')
> :t snd &&& fst
snd &&& fst :: (a, c) -> (c, a)
```
where `Arrow` is an abstraction of functions https://wiki.haskell.org/Arrow_tutorial

#### [Simon Hudon (Jul 30 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545270):
For this particular operator, `applicative` is sufficient: `x &&& y = prod.mk <$> x <*> y` 

(that is to say, we only need `applicative (a b)`)

#### [Patrick Massot (Jul 30 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545321):
You're trying to scare me with your notations

#### [Patrick Massot (Jul 30 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545322):
It works pretty well

#### [Simon Hudon (Jul 30 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545369):
What works well? Scaring you or using the notation?

#### [Patrick Massot (Jul 30 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545371):
scaring me

#### [Simon Hudon (Jul 30 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545382):
Oh, good, so my work here is done

#### [Simon Hudon (Jul 30 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545488):
As far as I know, the definition is not in mathlib so you make it as simple as you need and leave it to others to generalize so that it looks more like Haskell (the generalization has a few stumbling blocks I think)

#### [Patrick Massot (Jul 30 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545538):
Ok, I may do that. But first I'll sleep. Thanks!

#### [Simon Hudon (Jul 30 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545596):
:+1:

#### [Simon Hudon (Jul 30 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545597):
Good night!

#### [Nicholas Scheel (Jul 30 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130583767):
here’s some discussion on the Arrow class: https://www.eyrie.org/~zednenem/2017/07/twist

PureScript has opted not to create an Arrow class (see link 3 above); instead it just defined `(&&&)` using `Strong` and `Category`: https://pursuit.purescript.org/packages/purescript-profunctor/4.0.0/docs/Data.Profunctor.Strong#v:fanout

#### [Simon Hudon (Jul 30 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130586742):
I think in Haskell as well, people think Arrow might not have been the right abstraction

#### [Sebastian Ullrich (Jul 30 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130587542):
```quote
PureScript has opted not to create an Arrow class (see link 3 above); instead it just defined `(&&&)` using `Strong` and `Category`: https://pursuit.purescript.org/packages/purescript-profunctor/4.0.0/docs/Data.Profunctor.Strong#v:fanout
```
Is there actually any implementation anywhere apart from `Function` :sweat_smile: ? But thanks for the information!

#### [Nicholas Scheel (Jul 30 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130589452):
haha, we can go one step away from Function with Star :wink: https://github.com/purescript/purescript-profunctor/blob/v4.0.0/src/Data/Profunctor/Star.purs#L70 (actually that package has a variety of profunctors, a number of which implement Strong)

