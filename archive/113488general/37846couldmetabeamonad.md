---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37846couldmetabeamonad.html
---

## Stream: [general](index.html)
### Topic: [could meta be a monad](37846couldmetabeamonad.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135797914):
Something that popped into my head recently, and my curiosity makes me ask this question:
Could `meta` have been a monad?
In Haskell, there is the `IO` monad that marks functions "unsafe" (i.e., they can have side effects). I could imagine that `meta` could also be a monad that marks functions "unsafe" (i.e., they are meta). Would this work? What would be the pros and cons?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 15 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135802955):
Do you mean `tactic`? It's already a monad.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135806442):
No, I meant what I wrote. [Edit: misinterpreted Simon's answer.]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135806499):
I think you're conflating `meta` and `tactic` here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135806648):
No, I really meant `meta`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135806698):
If I have a trusted piece of code, I could wrap it into the "meta" tactic, and it would no longer be trusted, etc, etc...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135806700):
Or does @**Simon Hudon** mean that `tactic` is already a monad. I see. Yes, that I knew.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135806707):
So I repeat my question: *Could* `meta` be a monad?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 15 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135806807):
Ok so instead of having a keyword meta, you'd have a meta monad which would enable unbounded recursion and access to the prover's internals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 15 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135806815):
I know that they want more parts of the tactics framework to be in pure code for Lean 4 but I don't know if everything can go there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 15 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135806816):
What gain do you think it would give us?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135806917):
Like I said in my first post: just curiosity. I don't know anything about theoretical pros and cons.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 15 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135807044):
I think at the moment, pure code doesn't allow unbounded recursion yet but that could be added too. I can't think of other reasons to not write all meta code as pure code

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135807583):
I think the best analogue here is actually the `io` monad of lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135807626):
it is non-meta, but you can do lots of external manipulation stuff and unbounded recursion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Oct 15 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135814024):
```quote
Could `meta` have been a monad?
```
Yes, instead of the `meta` keyword we could have a `meta` monad as follows:
```lean
def «meta» : Type u → Type u
| α := false → α
```
I think you can derive all features of the current meta in this monad, including `undefined` and general recursion.  But I'm not sure how helpful it would be.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135814262):
I'm not sure if it is helpful. But I do find it *funny*.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 19 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/136114496):
Encoding a type of effect as a monad has various generic disadvantages, including:
* You need different syntaxes to form the application `f x` depending on whether each of `f` or `x` is a monadic value or an ordinary value (here: `meta` or not).
* You need to specify an order of effects, which forces you to linearize your program to a certain extent, whereas a pure program can have a tree structure.
* If you want to use a second monad as well (say the `list` monad), now you need to figure out some way to combine the second monad with your effect monad (using something like monad transformers perhaps).

In some contexts these points could be viewed as advantages, but the effect of nontermination is so mild that that doesn't apply here. For example, if `x` and `y` are possibly nonterminating computations, then computing `x` and then `y` is the same as computing `y` and then `x`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 19 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/136114667):
The only advantage of `meta` as a monad that I can think of is on the implementation side: Lean would no longer have to track the `meta` property. However, I think there would still be special cases required to reproduce the current behavior, e.g., `meta` inductive types have a relaxed syntax for recursion--Lean would have to make the constructors and/or recursors operate in the `meta` monad


{% endraw %}
