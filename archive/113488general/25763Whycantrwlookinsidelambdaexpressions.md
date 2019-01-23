---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/25763Whycantrwlookinsidelambdaexpressions.html
---

## Stream: [general](index.html)
### Topic: [Why can't `rw` look inside lambda expressions?](25763Whycantrwlookinsidelambdaexpressions.html)

---

#### [Johan Commelin (Jul 24 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Why%20can%27t%20%60rw%60%20look%20inside%20lambda%20expressions%3F/near/130212033):
I often find myself trying to do a rewrite, and then it fails miserably while it shouldn't. Suppose I have a `finset.sum univ (\lam x, f(x + x))` in my goal, and I know that `f` is a group hom. Then I want to rewrite that `f(x + x)` to `f(x) + f(x)`. But Lean always complains. So I have to do a little dance with `rw show [relevant part goes here]`, which feels clumsy. What am I doing wrong?

#### [Simon Hudon (Jul 24 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Why%20can%27t%20%60rw%60%20look%20inside%20lambda%20expressions%3F/near/130212074):
`rw` can't rewrite bound variables. `simp` is more useful there.

#### [Simon Hudon (Jul 24 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Why%20can%27t%20%60rw%60%20look%20inside%20lambda%20expressions%3F/near/130212168):
If you're worried about `simp` trying too many rules, you can restrict it with `simp only [my interesting rule]` or disable individual `simp` rules with `simp [my_rule, - no_no_rule]`

#### [Johan Commelin (Jul 24 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Why%20can%27t%20%60rw%60%20look%20inside%20lambda%20expressions%3F/near/130212196):
It works!

#### [Simon Hudon (Jul 24 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Why%20can%27t%20%60rw%60%20look%20inside%20lambda%20expressions%3F/near/130212256):
:party_popper:

#### [Kevin Buzzard (Jul 24 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Why%20can%27t%20%60rw%60%20look%20inside%20lambda%20expressions%3F/near/130220271):
You can also use `conv in (f(x+x)) begin rw ... end`. See Patrick's `conv` notes in the mathlib docs.

#### [Johan Commelin (Jul 24 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Why%20can%27t%20%60rw%60%20look%20inside%20lambda%20expressions%3F/near/130221167):
Thanks, I'll take a look.

#### [Kevin Buzzard (Jul 24 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Why%20can%27t%20%60rw%60%20look%20inside%20lambda%20expressions%3F/near/130221281):
https://github.com/leanprover/mathlib/tree/master/docs/extras

#### [Kevin Buzzard (Jul 24 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Why%20can%27t%20%60rw%60%20look%20inside%20lambda%20expressions%3F/near/130221286):
`conv.md`

#### [Johan Commelin (Jul 24 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Why%20can%27t%20%60rw%60%20look%20inside%20lambda%20expressions%3F/near/130221751):
Ok, it was a long time ago that I read that doc. It's really cool! I will be able to use that quite a lot I guess.

