---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/60002notationwithunknownsymbols.html
---

## Stream: [general](index.html)
### Topic: [notation with unknown symbols](60002notationwithunknownsymbols.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496391):
Is it possible to have notation using unknown symbols? Say I want a new notation for lambda abstraction (this is not my use case, I try to minimize). I try:
```lean
notation `mkfun` x `,` f := λ x, f
#check mkfun x, (x+1)
```
But it fails with `unknown identifier 'x'`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Apr 21 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496442):
You might want to check out how the notation for ∃ is defined: https://github.com/leanprover/lean/blob/f59c2f0ef59fdc1833b6ead6adca721123bd7932/library/init/logic.lean#L532-L533

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496451):
Thanks, it looks promising

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496452):
It works with the `binder` / `binders` keywords and `scoped`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496498):
any chance this `r:(` thing is documented somewhere?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496503):
oh, `binders` is also a special word here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496504):
Kevin and I had a long conversation about it on gitter. Let's see if I can find it again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496505):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496617):
:point_up: [January 10, 2018 5:21 PM](https://gitter.im/leanprover_public/Lobby?at=5a5691dd83152df26d570d0f)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496679):
In short `r:(...)` gives a name to an expression that can be built in one of two ways:
* `scoped`
* `foldl` / `foldr`

In `r:(scoped p, ...)`, `p` is a bound variable that you can use in `...`. It will be replaced with a lambda abstraction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496781):
It sorts of make sense, but not to the point where I could fix my `mkfun` example

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496787):
oh wait

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496788):
I can actually

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496790):
``notation `mkfun` binders `,` r:(scoped f, f) := r`` does work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496877):
So, if I may ask, why are you making fun of lambda abstractions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496885):
I laughed. Do you also want an answer?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496887):
Both are appreciated :laughing:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496922):
I'm trying to setup some notations for sums and products

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496937):
I would like to be able to write something like `def f := λ n, Sum_{0 ≤ i ≤ n} i^2`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496938):
I have no problem defining such a function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496939):
Using `list.sum` and `list.range`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496979):
I have trouble setting up the notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496981):
Cool :) btw, would it be useful to you to have a notation for `classical.epsilon`: `ε x, 1 ≤ x ≤ 3`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496982):
not sure how easy it would be to implement it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496983):
I mean, what are you going to produce when there is no such element

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496991):
in classical Hilbert epsilon it is supposed to produce "whatever"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497039):
`classical.epsilon` already exists. It's only defined on nonempty types. When no such `x` exists, an arbitrary value is picked

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497042):
but then it is empty

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497043):
what is going to be the type of the output

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497054):
@**Patrick Massot** Do you have a special provision for infinite sets in `Sum_{ ... }`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497087):
I was thinking about finite sums here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497102):
Really I want to convert 
```lean
open data.list.basic
open list
def f := λ (n : ℕ), sum (map (λ i, i*i) (range n))
```
to what I wrote earlier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497105):
having a nice notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497143):
where the name of the bound variable i is not hard-wired in the notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497161):
@**Kenny Lau** here is the type of `epsilon`:

```lean
noncomputable def epsilon {α : Sort u} [h : nonempty α] (p : α → Prop) : α :=
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497205):
oh, I misinterpreted everything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497212):
@**Patrick Massot** 
How about this as the underlying function:

```lean
sum : ℕ → (ℕ → Prop) → (ℕ → α) → α := ...
```

Basically, the notation should be hardwired to fix an upper bound on the range

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497251):
but you still get to filter individual terms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497312):
I don't really care about the underlying function. I want my notation with only the formula in term of i, not prefaced with a lambda

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497355):
One step at a time, young padawan, I'm getting there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497521):
I'm making progress
```lean
notation `Sum_{` binders `≤` n `}` r:(scoped f, f) := sum (map f $ range n)
#eval Sum_{ (i : ℕ) ≤ 4} i*i
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497568):
Not bad!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497597):
I was trying:

```lean
notation `ΣΣ ` binder ` | ` f:(scoped x, x) ∧ ub:(scoped x, x) ` ≤ ` n `, ` t:(scoped x, x) :=
sum' n f t

example : (ΣΣ x | 0 ≤ x ∧ x ≤ 7, f x) ≤ 7 := _
```

But I think you're not allowed to use `scoped` so many times.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497617):
I can even replace `(i : ℕ)` by `(i)` but not by `i`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497623):
Not `i`? What error does it give you?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497666):
invalid expression

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497675):
That's intriguing. You may want to try giving precedences to the tokens: `` ` ≤ `:0``

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497718):
I'll catch up with you later. There an adorable 2 year old here who needs attention :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497720):
Too bad, I was hoping your nephew was also a Lean expert

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497723):
Have fun!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497729):
He's more of an Idris kind of guy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497732):
:smile:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497733):
His name is Idris but I assume that speaks to his parents preference of Idris over Agda and Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497739):
And not to the sexiness of Idris Elba :stuck_out_tongue_winking_eye:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125503970):
Does anyone has a decidable predicate on nat at hand?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 21 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504018):
`pos`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 21 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504019):
Any predicate?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 21 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504060):
`(λ n : ℕ, true)` :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504061):
Maybe somethin like even or odd exist somewhere and is decidable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504062):
I need a decidable instance in the library

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 21 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504064):
Fun fact: Idris has an `Elab` monad. Have you ever tried googling for "idris elab"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 21 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504071):
there's `prime`, in `data.nat.prime`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 21 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504072):
even is decidable, if you define it as `n % 2 = 0`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 21 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504117):
@**Reid Barton** I couldn't manage to use that instance to prove 3 is prime.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504118):
@**Patrick Massot** I did some more experiment and I managed to define a syntax for `ΣΣ i, i ≥ 3 ∧ i < 21 ∧ even i ▻ i^2` which guarantees that `i` is bounded. How do you like the notation? (I made the formula a bit ugly to demonstrate that the form is pretty flexible)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504165):
`#eval if nat.prime 3 then 1 else 0` does work here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504166):
thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 21 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504217):
`example : 1 = if nat.prime 3 then (1 : ℕ) else (0 : ℕ) := rfl` doesn't work though unfortunately. It does work for 2 though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504502):
My current achievements are at https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/bigop.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504503):
I still has precedence issues

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504508):
But I'm already happy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504510):
I have quite a lot of ways of computing 5!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504556):
And I seems I was able to state a lemma about big product for an associative operator and apply it to addition in nat

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504568):
For those who didn't follow previous discussions, I'm going after http://hal.inria.fr/docs/00/33/11/93/PDF/main.pdf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504569):
Nice!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504576):
If you're interested, I've put my code here:

https://gist.github.com/cipher1024/604d5ec28ceb29e80219ce6e69bb1ea4

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504617):
Hopefully this will be resolved in lean 4 (@**Sebastian Ullrich** vm replacements please) but right now you have to make a choice between VM efficient and kernel efficient. `decidable_prime_1` is kernel efficient and `decidable_prime` is VM efficient

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504622):
the default one you get is `decidable_prime`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504634):
https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/bigop.lean#L67 has no trouble suming primes numbers in `range 5`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504637):
That's scientific computing!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 21 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504691):
Lean 4 will use a simplifier on code to be compiled, which should also enable VM replacements

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504928):
What is the precedence voodoo I need to get rid of parentheses in  https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/bigop.lean#L71 ? I mean, everything on LHS of the equality is surrounded in parenthesis, otherwise it doesn't work. How to avoid that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504936):
use a high precedence for left brackets and a low prec for right brackets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504985):
Which brackets?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 21 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125505203):
There are alternatives characters for Pi and Sigma `\sum` and `\prod`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125505208):
I know, but they look weird in my VScode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125505209):
too tall

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125505213):
But of course I like the semantic abbreviation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 21 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125505265):
```quote
too tall
```
That's why they're called big operators.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125505270):
`\sum` and `\Sigma` aren't the same

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125505321):
What do you mean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125505322):
Of course one is taller

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125505323):
But do you mean something else?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125505325):
And of course we can give a different definition to different symbols

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125506073):
Oh, crap! My append lemma is not correct. Associativity is not enough, I really need a monoid.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125506130):
Oh! I just used `rsimp` that @**Gabriel Ebner** explained earlier today!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125506170):
No

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125506172):
Actually Lean is hanging

