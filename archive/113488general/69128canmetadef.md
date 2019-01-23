---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/69128canmetadef.html
---

## Stream: [general](index.html)
### Topic: [can meta `def`?](69128canmetadef.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 05 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133394258):
Can you have meta code that writes definitions and lemmas for you? Probably yes, and this is how things like `to_additive` work. Is that right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 05 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133394409):
Is this somehow what `add_decl` is for?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 05 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133394637):
Yes it is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 05 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133394664):
Ok cool! I could imagine some uses for it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 05 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133394687):
For example, you define multiplication of matrices, and immediately afterwards, there is a simp-lemma `mul_val`. This happens a lot. Couldn't we auto-generate those?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 05 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133394756):
I feel like at least half of the simp lemmas after definitions could be auto-generated.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 05 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133394817):
Here is a claim: every lemma that is proved by `rfl` is a good candidate for being auto-generated.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 05 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133394857):
Yes, they can be generated. But could it be that you could get rid of the lemmas altogether by tagging your definition as `simp`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 05 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133394898):
Hmm, I think usually there is notation introduced in between.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 05 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395156):
But the notation doesn't affect rewriting.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 05 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395204):
Hmm... then I'm just really confused.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 05 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395224):
Take https://github.com/leanprover-community/mathlib/blob/noetherian/ring_theory/ideals.lean#L176 for example.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 05 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395268):
Those lines have completely predictable names (even to me), and are completely boring statements.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 05 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395286):
I would definitely forget to write them, until I need the after 50 other lines, and then only write half of them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 05 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395396):
Do you think stuff like this could be automated?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 05 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395464):
Maybe the question is to general...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 05 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395514):
I think the issue there is the combination of `coe` (which comes from a type class) and its underlying definition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 05 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395533):
At least I got an answer to the original question. And I am glad that it was positive. I'll keep it in mind, because I'm sure it will come in handy at some point.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 05 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395540):
It is not as trivial as I thought but there might be something to do with it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 05 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395641):
In general, maybe the question is to do `simp` lemmas from a type class instance which is just built on top of stand alone definitions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 05 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395779):
If you have 

```lean
instance : my_class my_type :=
{ op := my_type.op }
```

we can take all the equations of `my_type.op`, replace the occurrences of `my_type.op` with `my_class.op` and label the result as `simp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 05 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395833):
Right. That sounds useful. But I don't know what the experts think (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 05 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395896):
More import still: does it seem like a generalization of the problem you were asking about?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 05 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133396014):
Yes, I think so... although there might also be other cases. For example https://github.com/leanprover/mathlib/pull/316/files#diff-dcac36203421953a8cefa07fecd35a79R71 might be enhanced to also define a functor along the way.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 05 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133396029):
But I'm not suggesting that these are special cases of one sort of automation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 05 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133396047):
It is just that they could both benefit from some `add_decl` if I'm not mistaken.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 05 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133396183):
If you want, I can walk you through the construction of the solution I suggested and then we can see if something similar can be done for your second example

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 05 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133396356):
Ok, would definitely like to do that. But maybe not tonight (-; I need to catch up with some sleep, so I'll be gone in a couple of minutes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 05 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133396393):
Sure, let me know when you're ready and I'll give you a hand

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 05 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133397167):
Just for your information: Isabelle has a tool called `lift_definition` which lifts a term along subtypes / quotients / other relations etc.
If one wants to define a function `lift f : {a : A // p a} -> {b : B // q b}`, it provides one with the following two goals:
the function itself: `f : A -> B` and a proof `forall a : A, p a -> q (f b)`. The nice thing is that this also works for quotients, but in Isabelle this is done by assuming that there is a canonical projection (i.e. `quot.out`) which we may want to avoid, and instead use a more generic lifting constant.

My idea for a lift function would be: get typing information (which includes the information for which types the representation should change) and the term to lift. Then it puts `lift` or `cases` around the term to translate into the other type. All further proofs are left as subgoals to the user. Finally it produces the constant itself, and a rewrite rule which adds coercions etc at all places necessary to remove all lift constants.


{% endraw %}
