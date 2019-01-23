---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58179thetypeofapitype.html
---

## Stream: [general](index.html)
### Topic: [the type of a pi type.](58179thetypeofapitype.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Mar 15 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123762898):
After a few months break I am revisiting lean basics. I'm looking back at dependent types.

I understand why this typechecks: `((λ k: nat, eq.refl k) : (Π k : nat, k = k))` essentially we have a function, which returns a type, which depends on the parameter the function takes. We need this because we want to have a family of proofs 0 = 0, 1 = 1, etc.

But I don't get why these typecheck: `((Π k : nat, k = k) : Prop)` or `((Π k: nat, Prop) : Type)`. The rule seems to be that the type signature of any pi type "forgets" the parameters that the type on the left depends on  and behaves as if it was a simple type.

Are there any particular reasons of why that is or is it just the way it is?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 15 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763082):
Yes. Let's look at the non-dependent case first. Let's first notice that everything has a type:

```
(λ n : ℕ, n+1) : ℕ → ℕ 
ℕ → ℕ : Type 0
Type 0 : Type 1
-- and so on
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 15 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763084):
@**Adam Kurkiewicz** if A has type u and B has type v, then `A -> B` has type `max u v`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 15 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763161):
And `ℕ → ℕ` is basically syntactic sugar for `Π n : ℕ, ℕ`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 15 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763501):
```quote
The rule seems to be that the type signature of any pi type "forgets" the parameters that the type on the left depends on and behaves as if it was a simple type.
```

That's correct. 

```quote
Are there any particular reasons of why that is or is it just the way it is?
```

For one thing it is useful. But let's look at an alternative:

```
(Π k : nat, k = k) : nat -> Prop
```

That means that that proposition is not true on its own. It would be true about a given number. But that's not the case. `Π` is the same as `∀`. The statement is not "if you give me a number, I'll state that it is equal to itself". It is "every number is equal to itself". If you want the first, you'll use `(λ k : nat, k = k) : nat -> Prop`. It is not an assertion on its own. You feed it a natural number and then the result will state something about that natural number.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Mar 15 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763607):
I see. So it doesn't forget the type of the parameter, it just takes the maximum of the type of the parameter and the type of the type. So `Prop` is effectively `Type -1`, right? And since `nat : Type 0`, then `k : Type -1` and `k = k : Type -1` is `Type -1`, so the total result is `Type max -1 -1`, which is `Type -1`, which is `Prop`. This might be a little bit barbarian, but I think I'm getting it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 15 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763673):
A less barbarian way of seeing is that `Prop` and `Type` are both syntactic sugar for `Sort`: `Prop = Sort 0` and `Type u = Sort (u+1)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 15 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763727):
I am surprised you would care so much about universes (given that you are a beginner I assume). This information is not very useful in my opinion :).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Mar 15 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763751):
@**Simon Hudon** I actually do not think that my original statement was correct. The type of the parameter is not forgotten, it's the maximum like @**Kenny Lau** said, for example this typechecks `#check ((Π k: Type 0, Prop) : Type 1)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 15 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763757):
Really? For small proofs maybe but as soon as you have types within types, you have to start caring about universes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 15 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763803):
Not quite. You can rely on `Type*` to do the work for you.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 15 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763826):
```quote
@**Simon Hudon** I actually do not think that my original statement was correct. The type of the parameter is not forgotten, it's the maximum like @**Kenny Lau** said, for example this typechecks `#check ((Π k: Type 0, Prop) : Type 1)`
```
That's true, in that sense, it does not forget. More specifically, it does not forget the universe of the parameter. The type itself becomes unavailable though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Mar 15 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763874):
I've largely ignored universes so far, and most of the underlying type theory, but given that I might be teaching lean to others from next semester I'm trying to make sure I know at least a little bit of the foundations.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 15 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763883):
Interesting detail:

```
#check ((Π k: Type 7, k = k) : Prop)
```

If the result type is Prop, the whole thing can stay in Prop

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 15 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763889):
I think you've done well to ignore them for the most part :P!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 15 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763932):
I think I agree. I don't particularly like to have to specify them. I wonder what justify that design choice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 15 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123764002):
I use `Type*` and only think about it once I run into issues. From my experience, I find it not too difficult to fix them post-facto. I have yet to encounter a case where I wish I had considered it beforehand. But perhaps I avoid the kinds of things that might require more universe-thought. I mostly write certificates of functional programs.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Mar 15 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123764081):
@**Simon Hudon** hmm... So it turns out it's not `max u v`after all? It can't be, since in this case it would have to be `Type 7` as opposed to `Prop`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Mar 15 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123764133):
It's actually `imax u v` which is 0 if `v` is 0, and otherwise `max u v`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 15 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123764146):
<deleted>

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Mar 15 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123764165):
Useful to know mainly because you might see `imax` in Lean output/error messages and wonder what it means, I think.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Mar 15 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123764339):
Thanks @**Reid Barton**, this will definitely come useful at some point.

@**Simon Hudon** I really like your example with natural numbers. I think it's another productive way of thinking about Pi types.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 15 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123764351):
Do you mean that `nat -> Prop` example?


{% endraw %}
