---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53181dependentfinsupp.html
---

## Stream: [general](index.html)
### Topic: [dependent finsupp](53181dependentfinsupp.html)

---


{% raw %}
#### [ Kenny Lau (Sep 04 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133297941):
I want to make finsupp dependent, and then build the current finsupp as a special case. Is this a good idea?

#### [ Johannes Hölzl (Sep 04 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133298356):
I thought to suggest this as part of the direct sum PR :-)

#### [ Kenny Lau (Sep 04 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133304404):
@**Johannes Hölzl** I'm not sure what to do with this. finsupp is widely used. should I make a separate file?

#### [ Johannes Hölzl (Sep 04 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133304601):
Yes. Start with a separate file where you generalize from direct sum to `dfinsupp`, i.e. from `[Π i, module R (β i)]` to `[Π i, has_zero (β i)]`.

#### [ Kenny Lau (Sep 04 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133329943):
problem. the simp lemmas now require higher order unification, rendering them useless

#### [ Kenny Lau (Sep 05 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133375942):
@**Johannes Hölzl** should I make finsupp dependent on dfinsupp?

#### [ Johannes Hölzl (Sep 05 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133376017):
Yes, I think so. But let's first add `dfinsupp` and then see.

#### [ Kenny Lau (Sep 05 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133376899):
@**Johannes Hölzl**  there's one thing though. now for finsupp from A to B, we need decidable equality on B

#### [ Kenny Lau (Sep 05 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133376909):
I suspect that if we define finsupp differently, then we won't need decidbale equlaity on B

#### [ Kenny Lau (Sep 05 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133376917):
should I work on that?

#### [ Johannes Hölzl (Sep 05 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133377009):
I guess this is your quotient construction, the one you use in your direct sums construction? If you want to use it, that's fine for me.

#### [ Kenny Lau (Sep 05 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133377042):
yes, ok, thanks

#### [ Kenny Lau (Sep 06 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133458668):
@**Johannes Hölzl** I'm in a dilemma: I can either define dfinsupp.sum with the same arguments, but it would require decidable equality on the codomains; or I can define dfinsupp.sum without decidable equality on the codomains, but it would require me to provide an extra argument that the input function maps 0 to 0.

#### [ Johan Commelin (Sep 06 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133459061):
I would go for the latter.

#### [ Johan Commelin (Sep 06 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133459113):
Alternatively, provide both...

#### [ Kevin Buzzard (Sep 06 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133459118):
What's your motivation for defining dfinsupp? Is there some application you have in mind?

#### [ Johan Commelin (Sep 06 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133459150):
Constructive direct sums, I think

#### [ Kevin Buzzard (Sep 06 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133459219):
oh that would make sense, Kenny was talking to me about direct sums recently.

#### [ Johannes Hölzl (Sep 06 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133463204):
Since the types are usually fixed and it's super annoying to always attach the `f 0 = 0` proof: assume decidability of the codomain for `sum`.

#### [ Kenny Lau (Sep 07 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493682):
@**Johannes Hölzl** sometimes we don't actually need decidable equality in general, we just need to determine if something is zero. What should I do in that case?

#### [ Simon Hudon (Sep 07 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493759):
you can say that `(x = 0)` and `(0 = x)` are decidable.

#### [ Kenny Lau (Sep 07 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493777):
Should I make a new typeclass for that? decidable_zero

#### [ Mario Carneiro (Sep 07 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493786):
`decidable_pred (eq 0)` works

#### [ Kenny Lau (Sep 07 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493839):
if I prove that `decidable_eq \to decidable_pred (eq 0)`, will Lean be able to use it?

#### [ Simon Hudon (Sep 07 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493844):
If you look at `decidable_eq`, `decidable_pred` and `decidable_rel`, they are simply definitions on top of `decidable`. You only need to do the same for `0` if it's pervasive enough

#### [ Kenny Lau (Sep 07 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493849):
well, `option` has decidable "none"

#### [ Kenny Lau (Sep 07 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493859):
`with_zero` has decidable `zero`

#### [ Simon Hudon (Sep 07 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493863):
```quote
if I prove that `decidable_eq \to decidable_pred (eq 0)`, will Lean be able to use it?
```
I think so

#### [ Kenny Lau (Sep 07 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493928):
oh I don't even need to prove it!

#### [ Kenny Lau (Sep 07 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493931):
```lean
instance {γ : Type w} [has_zero γ] [decidable_eq γ] : decidable_pred (eq (0 : γ)) :=
by apply_instance

```

#### [ Kenny Lau (Sep 07 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493932):
Lean is smart

#### [ Kenny Lau (Sep 07 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493936):
```lean
instance {γ : Type w} [has_zero γ] [decidable_pred (eq (0 : γ))] : decidable_pred (λ x, x = 0) :=
by apply_instance
```

#### [ Kenny Lau (Sep 07 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493974):
I can't believe this, something must be wrong

#### [ Mario Carneiro (Sep 07 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493983):
`eq 0` is `\lam x, eq 0 x` which is `\lam x, 0 = x`

#### [ Mario Carneiro (Sep 07 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493985):
the other one is `(= 0)` which is `\lam x, x = 0`

#### [ Kenny Lau (Sep 07 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493992):
yeah the second one is wrong

#### [ Kenny Lau (Sep 07 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133493996):
Lean interpreted `0` as natural

#### [ Simon Hudon (Sep 07 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133494118):
So how does Lean prove the instances for you?

#### [ Kenny Lau (Sep 07 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133494220):
I proved the second one now

#### [ Kenny Lau (Sep 07 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133494222):
the first one is just solve by elim

#### [ Simon Hudon (Sep 07 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133494272):
Why does that work?

#### [ Simon Hudon (Sep 07 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133494274):
Oh, ok, it's proving less than I thought

#### [ Kenny Lau (Sep 09 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/133585305):
@**Johannes Hölzl** commited to the [PR](https://github.com/leanprover/mathlib/pull/311)

#### [ Kenny Lau (Oct 06 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/135325125):
What is preventing this [22-day-old pull request](https://github.com/leanprover/mathlib/pull/311) from being merged?

#### [ Kevin Buzzard (Oct 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/135325331):
People being busy?

#### [ Kevin Buzzard (Oct 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/135325334):
You'll understand, one day :-)

#### [ Kenny Lau (Oct 06 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/135325996):
Are there any problems with my PR? @**Mario Carneiro**

#### [ Mario Carneiro (Oct 07 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/135329645):
It conflicts with the module refactor, so don't expect this to be merged until after that

#### [ Kevin Buzzard (Oct 07 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/135329897):
But after the module refactor Kenny will be too busy working on algebraic closure to be able to fix up this PR.

#### [ Kenny Lau (Oct 07 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20finsupp/near/135343213):
ok no problem


{% endraw %}
