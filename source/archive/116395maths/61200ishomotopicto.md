---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/61200ishomotopicto.html
---

## [maths](index.html)
### [is_homotopic_to](61200ishomotopicto.html)

#### [Kevin Buzzard (Aug 09 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131163659):
I just saw this in @**Luca Gerolla** 's code.

`definition is_homotopic_to { x y : β } (f : path x y) ( g : path x y) : Prop := nonempty ( path_homotopy f g)`

I feel like `is_homotopic_to` is an important concept and it sounds like a prop to me, but of course there might well be many homotopies between f and g. Is Luca unwise to use `nonempty` or is this exactly what he wants? I still feel very unsure about this kind of thing. Given an explicit homotopy from f to g and an explicit homotopy from g to h he will surely want an explicit homotopy from f to h, and of course he proves this, but...I think what I'm saying is that I am confused about both wanting a proposition and wanting to keep track of the homotopy at the same time.

#### [Reid Barton (Aug 09 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131171197):
You need both, I think. And here we do have both, since we also have `path_homotopy` itself.

#### [Reid Barton (Aug 09 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131171234):
What you don't want to do is define `is_homotopic_to` without `path_homotopy`

#### [Mario Carneiro (Aug 09 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131171736):
I think you will want a quotient type over the is_homotopic_to relation

#### [Mario Carneiro (Aug 09 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131171744):
so the homotopy itself won't be in the structure

#### [Luca Gerolla (Aug 09 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131172455):
So you think this is the appropriate way to define the equivalence relation that I will define the quotient on? When needed to get an actual  `path_homotopy f g `  from ` H : is_homotopic_to f g `  I use `cases `; while to show (for example) `is_homotopic_to f g` I construct an actual `F : path_homotopy f g ` and feed this with `nonempty.intro `.  Would this be a good way to manage the homotopy binary relation? At first,  I just felt I was loosing some information with `nonempty ` in later proofs.

#### [Kenny Lau (Aug 09 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131172493):
I think Kevin wants a `trunc` instead of a `nonempty`

#### [Kenny Lau (Aug 09 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131172500):
but this will be to HoTT-like

#### [Mario Carneiro (Aug 09 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131172508):
To take a quotient you need a Prop

#### [Mario Carneiro (Aug 09 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131172560):
Consider the way `cardinal` is defined - it is a quotient over the relation `nonempty (A ≃ B)`

#### [Luca Gerolla (Aug 09 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_homotopic_to/near/131174279):
I see.. thank you! I will stick to `nonempty`

