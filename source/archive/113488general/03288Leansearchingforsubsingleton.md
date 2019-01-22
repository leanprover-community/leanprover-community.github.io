---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03288Leansearchingforsubsingleton.html
---

## [general](index.html)
### [Lean searching for subsingleton?](03288Leansearchingforsubsingleton.html)

#### [Kenny Lau (Nov 09 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147398515):
https://gist.github.com/kckennylau/2b5890b44f2f66196254a50e9fd6fa96#file-subsingleton-L727
What motivates Lean to use 10 second to search for a subsingleton instance?

#### [Kenny Lau (Nov 09 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147398535):
The code was
```lean
theorem monic_X_sub_C' (x : α) : monic (X - C x) :=
by unfold monic leading_coeff nat_degree degree coeff
```

#### [Kenny Lau (Nov 09 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147398546):
but I'm afraid one cannot reproduce this because I modified polynomials in some other ways

#### [Kenny Lau (Nov 09 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147398611):
So unfortunately my link would have to suffice

#### [Kenny Lau (Nov 09 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147398794):
Actually the subsingleton thing might not be related at all

#### [Kenny Lau (Nov 09 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147398798):
I really don't know why Lean uses 10 seconds to elaborate the type

#### [Kenny Lau (Nov 09 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147398916):
How will it scale when our library gets 2 times bigger?

#### [Kenny Lau (Nov 09 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147399015):
Would we need a day to compile the mathlib?

#### [Kenny Lau (Nov 09 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147399022):
We only have ~260 files now

#### [Kenny Lau (Nov 09 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147399188):
also very strangely, if I go to my sandbox and import data.polynomial and do exactly the same thing, it compiles in a fraction in a second

#### [Kenny Lau (Nov 09 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147399197):
despite the environment being the same

#### [Kevin Buzzard (Nov 09 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147400866):
You have been posting some very hard-to-reproduce issues recently

#### [Mario Carneiro (Nov 09 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147401204):
Usually searches for subsingleton instances are prompted by `congr` (also used inside `simp`), which will use subsingleton instances to avoid some subgoals

#### [Kenny Lau (Nov 09 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147401342):
ok

