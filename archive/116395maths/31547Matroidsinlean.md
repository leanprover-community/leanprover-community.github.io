---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/31547Matroidsinlean.html
---

## [maths](index.html)
### [Matroids in lean](31547Matroidsinlean.html)

#### [Bryan Gin-ge Chen (Sep 21 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Matroids in lean/near/134359386):
As my next learning project, I've moved on from Fibonacci numbers and have been working on a formalization of [matroids](https://en.wikipedia.org/wiki/Matroid) based on the book "Matroid theory" by Oxley. Roughly speaking, a matroid on a set is a family of subsets that encodes an abstract version of linear dependence between the elements, and they appear in many different guises in combinatorics and related fields. My work-in-progress is in my [lean-matroids](https://github.com/bryangingechen/lean-matroids) repository. In "lean" terms, I've defined there 3 complicated `structure`s which build off of `data.finset` and proven that they are equivalent to each other.

This kind of fiddly combinatorial stuff seems to be a bit outside the interests of people here, but nonetheless I would be grateful for any feedback or suggestions on the style of the proofs. And thanks very much to everyone here for the help I've received so far! I'm off to bed now but I'll be back with various questions later on.

#### [Kevin Buzzard (Sep 21 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Matroids in lean/near/134371300):
[off-topic: I have an uncared-for repo about Fibonacci numbers by the way -- https://github.com/kbuzzard/lean-squares-in-fibonacci . I am interested in the result, it's just very low priority right now. So if you ever feel like coming back...]

#### [Bryan Gin-ge Chen (Sep 21 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Matroids in lean/near/134397598):
I noticed that matrices have been added to mathlib and that there's more stuff along the way in "kbb". Is there a convenient way to work with linear dependence of / independence of / subspaces spanned by rows of a matrix? Sorry, I'm asking this without having taken a careful look at the files in mathlib yet, in the hopes that someone will know how to do this off the top of their head.

#### [Kevin Buzzard (Sep 21 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Matroids in lean/near/134407123):
The kbb stuff was just a surprise appearance. I would recommend that you formalise a precise statement and ask if it can be proved, or formulate a precise object and ask if it can be defined. Or several statements and objects if you'd rather.

