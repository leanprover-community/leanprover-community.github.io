---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/65987453irrationallean.html
---

## [PR reviews](index.html)
### [#453 irrational.lean](65987453irrationallean.html)

#### [Kevin Buzzard (Nov 01 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23453%20irrational.lean/near/136888753):
@**Calle Sönne**  @**Abhimanyu Pallavi Sudhir**  and @**Jean Lo**  are all first year undergraduates at Imperial (who'd never used Lean 1 month ago) and this is joint work of theirs, subsequently tidied up by Chris and Kenny. The genesis of this project was some basic example sheet questions from my course, but it then it grew a bit. It feels to me like most of the things you'd ever want to know about irrational numbers, modulo theorems such as e or pi is irrational (the latter probably being hard to formalise).

#### [Mario Carneiro (Nov 04 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23453%20irrational.lean/near/137135207):
I had a 'whaaaat' moment when I saw [`rat.sqrt`](https://github.com/leanprover/mathlib/blob/9e888483c6532e4d3719a8b63696c14dc1b36040/data/rat.lean#L1045-L1046). For fun, here's a plot of the behavior of this function:
[sqrt.png](/user_uploads/3121/eM1mUm8wVIf29WCMLI8kN9ha/sqrt.png) 
I suspect it is dense in the top half-plane.

#### [Mario Carneiro (Nov 04 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23453%20irrational.lean/near/137135720):
Correction: it's not dense in the top half-plane, and its closure is probably just the real square root function (plus countably many discrete points). Because the "jumps" away from the real square root function are smaller for better approximations, so there is a finite number of points which differ by more than $$\epsilon$$ from the real square root (on a bounded interval).

#### [Kenny Lau (Nov 05 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23453%20irrational.lean/near/146797600):
@**Kevin Buzzard** @**Abhimanyu Pallavi Sudhir** @**Jean Lo** @**Calle Sönne** It has been merged

