---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/46163congrwithsubsingleton.html
---

## Stream: [general](index.html)
### Topic: [congr with subsingleton](46163congrwithsubsingleton.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 15 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128141922):
Is this a bug in `congr`?
```lean
example {α : Type} [subsingleton α] (x y : α) : x = y := by congr -- fails                                                                                                    
example {α : Type} [subsingleton α] (x y : α) (f : α → nat) : f x = f y := by congr -- ok                                                                                       
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 15 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128141939):
what is supposed to the state after the first `by congr`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 15 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128141945):
"no goals"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 15 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128141948):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 15 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128141949):
Actually, I made the second example slightly poor.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 15 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128141956):
Edited now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 15 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128141958):
Not in the sense that I'm not surprised by the result

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 15 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142002):
`congr` only gets its subsingleton optimization when it actually applies a function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 15 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142007):
because it simplifies the congruence lemma for `f`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 15 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142018):
so if `congr_core` applies 0 times the optimization never gets a chance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 15 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142028):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 15 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142047):
I have a more complicated example where `congr` fails even when there is a function being applied, but I need to minimize it first.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 15 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142090):
Is `simp` supposed to understand subsingletons then? What exactly does it do with them? It can't handle either of these goals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 15 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142125):
`simp` uses `congr` to enter a term, so it gets subsingleton handling indirectly that way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 15 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142133):
but it won't rewrite `x` to `y` if that's what you mean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 15 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142180):
mostly it's helpful for carrying along dependent arguments

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 15 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142183):
Oh, so by "it [`congr`] simplifies the congruence lemma" you don't mean using `simp`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 15 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142191):
No, I mean that the congruence lemma that is generated lacks an equality subgoal for any subsingleton arguments

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 15 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142196):
is this stuff in C++, in `mk_specialized_congr_lemma`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 15 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142203):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 15 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142207):
but you can see the resulting lemma by using the `mk_congr_lemma` function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 15 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128142838):
OK, the reason `congr` didn't work in my actual code is because I only have a subsingleton instance for a particular value of one of the type arguments, and the generated congruence lemma was too general and didn't specify the value of that type.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 15 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20with%20subsingleton/near/128143036):
(Namely, I have a subsingleton instance for `a ⟶ b` only when `a` is the initial object of a category)

