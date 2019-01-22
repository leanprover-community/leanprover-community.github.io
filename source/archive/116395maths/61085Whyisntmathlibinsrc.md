---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/61085Whyisntmathlibinsrc.html
---

## [maths](index.html)
### [Why isn't mathlib in `src`?](61085Whyisntmathlibinsrc.html)

#### [Kevin Buzzard (Nov 04 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Why%20isn%27t%20mathlib%20in%20%60src%60%3F/near/137161687):
I thought I'd try proving Hilbert Basis theorem again with the new module stuff (although it's been impossible because my nephews have been here all weekend) and I realised that building my version of community mathlib is really annoying because my scratch files don't compile (as they were all doing things with old versions of module). This  could all be fixed if mathlib lived in src like everything else does. Can we make this change at some point?

#### [Mario Carneiro (Nov 04 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Why%20isn%27t%20mathlib%20in%20%60src%60%3F/near/137162523):
what is the connection between mathlib in src and your files not compiling?

#### [Kevin Buzzard (Nov 04 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Why%20isn%27t%20mathlib%20in%20%60src%60%3F/near/137162572):
I could `cd src;lean --make` if mathlib weren't in root

#### [Kevin Buzzard (Nov 04 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Why%20isn%27t%20mathlib%20in%20%60src%60%3F/near/137162586):
my non-compiling scratch files have no place to hide this way

#### [Kevin Buzzard (Nov 04 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Why%20isn%27t%20mathlib%20in%20%60src%60%3F/near/137162605):
All of my other project have everything in src and a directory called scratch in root and in .gitignore

#### [Kenny Lau (Nov 04 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Why%20isn%27t%20mathlib%20in%20%60src%60%3F/near/137166753):
@**Kevin Buzzard** in fact that is what i had been doing on the train

#### [Kenny Lau (Nov 04 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Why%20isn%27t%20mathlib%20in%20%60src%60%3F/near/137166757):
and you can make it compile by making it the first workspace of vscode

#### [Scott Morrison (Nov 04 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Why%20isn%27t%20mathlib%20in%20%60src%60%3F/near/137172205):
I've had the same problem; I like having a scratch directory sometimes.

