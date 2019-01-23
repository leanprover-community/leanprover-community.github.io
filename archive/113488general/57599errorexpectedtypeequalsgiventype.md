---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57599errorexpectedtypeequalsgiventype.html
---

## Stream: [general](index.html)
### Topic: [error: expected type equals given type](57599errorexpectedtypeequalsgiventype.html)

---


{% raw %}
#### [ Johan Commelin (Jan 15 2019 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155160367):
A mystery:
```lean
type mismatch at application
  functor.on_iso (yoneda.obj F)
term
  yoneda.obj F
has type
  presheaf Xᵒᵖ ⥤ Type (max u v)
but is expected to have type
  presheaf Xᵒᵖ ⥤ Type (max u v)
```
Last week @**Reid Barton** and I encountered a similar error when working on over categories. Back then we could fix it by specifying a universe variable. But that still felt like a hack around a bug. This time universe annotations don't seem to help.

Anyway, I'm more interested in fact that Lean thinks two types are the same, but isn't happy to move on.
Here is the `pp.all` version:
```lean
has type
  @category_theory.functor.{(max u v) (max u v) (max u (v+1)) (max u v)+1}
    (category_theory.op.{(max u (v+1))} (@category_theory.presheaf.{v u} X 𝒳))
    (@category_theory.opposite.{(max u v) (max u (v+1))} (@category_theory.presheaf.{v u} X 𝒳)
       (@category_theory.presheaf.category_theory.category.{v u} X 𝒳))
    (Type (max u v))
    category_theory.types.{(max u v)}
but is expected to have type
  @category_theory.functor.{(max u v) (max u v) (max u (v+1)) (max u v)+1}
    (category_theory.op.{(max u (v+1))} (@category_theory.presheaf.{v u} X 𝒳))
    (@category_theory.opposite.{(max u v) (max u (v+1))} (@category_theory.presheaf.{v u} X 𝒳)
       (@category_theory.presheaf.category_theory.category.{v u} X 𝒳))
    (Type (max u v))
    category_theory.types.{(max u v)}
```

#### [ Sebastian Ullrich (Jan 15 2019 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155162452):
If you have too much time and want to take a closer look, you could try turning on the various defeq traces. Not sure if the output will be of any help.

#### [ Johan Commelin (Jan 15 2019 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155163901):
@**Sebastian Ullrich** I have a bit of time. Do you have a guess about what's going on? Are you interested in those traces? How do I turn them on?

#### [ Sebastian Ullrich (Jan 15 2019 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155164151):
It should be `trace.type_context.is_def_eq` and `trace.type_context.is_def_eq_detail`. I can take a look, though I won't promise anything :) .

#### [ Johan Commelin (Jan 15 2019 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155164241):
Output of `trace.type_context.is_def_eq`:
```lean
[type_context.is_def_eq] Type ? =?= Type ? ... success  (approximate mode)
[type_context.is_def_eq] category ?m_1 =?= category ?m_1 ... success  (approximate mode)
[type_context.is_def_eq] Type ? =?= Type ? ... success  (approximate mode)
[type_context.is_def_eq] category ?m_1 =?= category ?m_1 ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 ⥤ ?m_1ᵒᵖ ⥤ Type ? =?= ?m_3 ⥤ ?m_5 ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 ⥤ ?m_3 =?= ?m_5 ... success  (approximate mode)
[type_context.is_def_eq] presheaf X =?= ?m_1 ... success  (approximate mode)
[type_context.is_def_eq] presheaf X =?= ?m_1 ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 =?= F ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 =?= ?m_2 ⥤ ?m_4 ... failed  (approximate mode)
[type_context.is_def_eq] ?m_1 =?= presheaf.category_theory.category ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 =?= presheaf.category_theory.category ... success  (approximate mode)
[type_context.is_def_eq] category_theory.types =?= category_theory.types ... success  (approximate mode)
[type_context.is_def_eq] category_theory.opposite =?= category_theory.opposite ... success  (approximate mode)
[type_context.is_def_eq] functor.category presheaf Xᵒᵖ (Type (max u v)) =?= functor.category presheaf Xᵒᵖ (Type (max u v)) ... success  (approximate mode)
[type_context.is_def_eq] ?x_1 =?= presheaf Xᵒᵖ ⥤ Type (max u v) ... success  (approximate mode)
[type_context.is_def_eq] ?x_0 =?= presheaf Xᵒᵖ ⥤ Type (max u v) ... success  (approximate mode)
```

#### [ Johan Commelin (Jan 15 2019 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155164317):
Output of `trace.type_context.is_def_eq_detail`:
```lean
[type_context.is_def_eq_detail] [1]: ?m_1 ⥤ ?m_1ᵒᵖ ⥤ Type ? =?= ?m_3 ⥤ ?m_5
[type_context.is_def_eq_detail] [2]: functor =?= functor
[type_context.is_def_eq_detail] process_assignment ?m_1 := ?m_2
[type_context.is_def_eq_detail] assign: ?m_1 := ?m_2
[type_context.is_def_eq_detail] process_assignment ?m_1 := ?m_2
[type_context.is_def_eq_detail] [2]: category ?m_1 =?= category ?m_2
[type_context.is_def_eq_detail] [3]: category =?= category
[type_context.is_def_eq_detail] assign: ?m_1 := ?m_2
[type_context.is_def_eq_detail] process_assignment ?m_1 := ?m_2ᵒᵖ ⥤ Type ?
[type_context.is_def_eq_detail] assign: ?m_1 := ?m_2ᵒᵖ ⥤ Type ?
[type_context.is_def_eq_detail] process_assignment ?m_1 := functor.category ?m_2ᵒᵖ (Type ?)
[type_context.is_def_eq_detail] [2]: category ?m_1 =?= category (?m_2ᵒᵖ ⥤ Type ?)
[type_context.is_def_eq_detail] [3]: category =?= category
[type_context.is_def_eq_detail] assign: ?m_1 := functor.category ?m_2ᵒᵖ (Type ?)
[type_context.is_def_eq_detail] [1]: ?m_1 ⥤ ?m_3 =?= ?m_5ᵒᵖ ⥤ Type ?
[type_context.is_def_eq_detail] [2]: functor =?= functor
[type_context.is_def_eq_detail] process_assignment ?m_1 := ?m_2ᵒᵖ
[type_context.is_def_eq_detail] assign: ?m_1 := ?m_2ᵒᵖ
[type_context.is_def_eq_detail] process_assignment ?m_1 := category_theory.opposite
[type_context.is_def_eq_detail] [2]: category ?m_1 =?= category ?m_2ᵒᵖ
[type_context.is_def_eq_detail] [3]: category =?= category
[type_context.is_def_eq_detail] assign: ?m_1 := category_theory.opposite
[type_context.is_def_eq_detail] process_assignment ?m_1 := Type ?
[type_context.is_def_eq_detail] assign: ?m_1 := Type ?
[type_context.is_def_eq_detail] process_assignment ?m_1 := category_theory.types
[type_context.is_def_eq_detail] [2]: category ?m_1 =?= large_category (Type ?)
[type_context.is_def_eq_detail] unfold right: category_theory.large_category
[type_context.is_def_eq_detail] [3]: category ?m_1 =?= category (Type ?)
[type_context.is_def_eq_detail] [4]: category =?= category
[type_context.is_def_eq_detail] assign: ?m_1 := category_theory.types
[type_context.is_def_eq_detail] process_assignment ?m_1 := presheaf X
[type_context.is_def_eq_detail] assign: ?m_1 := presheaf X
[type_context.is_def_eq_detail] process_assignment ?m_1 := F
[type_context.is_def_eq_detail] assign: ?m_1 := F
[type_context.is_def_eq_detail] [1]: presheaf Xᵒᵖ ⥤ Type ? =?= ?m_2 ⥤ ?m_4
[type_context.is_def_eq_detail] [2]: functor =?= functor
[type_context.is_def_eq_detail] [2]: category_theory.opposite =?= category_theory.opposite
[type_context.is_def_eq_detail] [2]: category_theory.types =?= category_theory.types
[type_context.is_def_eq_detail] on failure: presheaf Xᵒᵖ ⥤ Type ? =?= ?m_2 ⥤ ?m_4
[type_context.is_def_eq_detail] process_assignment ?m_1 := presheaf.category_theory.category
[type_context.is_def_eq_detail] [1]: category ?m_1 =?= category (presheaf X)
[type_context.is_def_eq_detail] [2]: category =?= category
[type_context.is_def_eq_detail] assign: ?m_1 := presheaf.category_theory.category
[type_context.is_def_eq_detail] [1]: category_theory.types =?= category_theory.types
[type_context.is_def_eq_detail] [1]: category_theory.opposite =?= category_theory.opposite
[type_context.is_def_eq_detail] process_assignment ?x_1 := presheaf Xᵒᵖ ⥤ Type (max u v)
[type_context.is_def_eq_detail] assign: ?x_1 := presheaf Xᵒᵖ ⥤ Type (max u v)
[type_context.is_def_eq_detail] process_assignment ?x_0 := presheaf Xᵒᵖ ⥤ Type (max u v)
[type_context.is_def_eq_detail] assign: ?x_0 := presheaf Xᵒᵖ ⥤ Type (max u v)
```

#### [ Mario Carneiro (Jan 15 2019 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155164531):
what does `convert yoneda F` give?

#### [ Johan Commelin (Jan 15 2019 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155164556):
The error is in a `have` statement...
```lean
have := @functor.on_iso _ _ _ _ (yoneda.obj F),
```

#### [ Mario Carneiro (Jan 15 2019 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155164575):
can you fill in the underscores?

#### [ Johan Commelin (Jan 15 2019 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155164579):
I'll try. Give me a second.

#### [ Mario Carneiro (Jan 15 2019 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155164640):
also your `op` has a really confusing precedence

#### [ Mario Carneiro (Jan 15 2019 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155164651):
there is no way lean can parse `presheaf Xᵒᵖ` means `(presheaf X)ᵒᵖ` but the printer seems to think so

#### [ Johan Commelin (Jan 15 2019 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155164673):
```lean
have := @functor.on_iso ((presheaf X)ᵒᵖ) _ _ _ (yoneda.obj F),
```
Wow... this works...

#### [ Reid Barton (Jan 15 2019 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155165054):
```quote
there is no way lean can parse `presheaf Xᵒᵖ` means `(presheaf X)ᵒᵖ` but the printer seems to think so
```
 I thought this was actually possible by using a precedence above 1000?

#### [ Reid Barton (Jan 15 2019 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155165061):
I was wondering whether we should do that

#### [ Mario Carneiro (Jan 15 2019 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155165111):
I think you want high precedence (above `max = 1024`) to get `presheaf Xᵒᵖ` = `presheaf (Xᵒᵖ)`

#### [ Reid Barton (Jan 15 2019 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155165174):
Oh, I misread

#### [ Reid Barton (Jan 15 2019 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155165181):
What you just wrote is what I want

#### [ Mario Carneiro (Jan 15 2019 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155165245):
most postfix notations are at precedence `:max+1` for this reason

#### [ Kevin Buzzard (Jan 15 2019 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155165251):
Has this fixed the error Johan?

#### [ Reid Barton (Jan 15 2019 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155165253):
I'm not really sure how it works now actually. But I know there are a lot of parentheses in `category_theory` that look like they ought to be unnecessary

#### [ Mario Carneiro (Jan 15 2019 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155165266):
I doubt it addresses the error though, I'm still perplexed

#### [ Mario Carneiro (Jan 15 2019 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155165294):
it seems like it's an elaboration order issue

#### [ Mario Carneiro (Jan 15 2019 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155165388):
what's up with this name? `category_theory.presheaf.category_theory.category`

#### [ Mario Carneiro (Jan 15 2019 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155165394):
just in case you forgot it's about categories

#### [ Reid Barton (Jan 15 2019 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155165589):
Just wait until we have the category of categories

#### [ Reid Barton (Jan 15 2019 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155165640):
or the category of theories

#### [ Chris Hughes (Jan 15 2019 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155165686):
```quote
or the category of theories
```
 Is that a thing?

#### [ Johan Commelin (Jan 15 2019 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155165751):
I still don't understand the error.
But I no longer need a solution, because I proved it differently.

#### [ Johan Commelin (Jan 15 2019 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155165758):
It's just weird that this shows up. And like I said: Reid and I had a similar thing last week when we worked with over categories.

#### [ Mario Carneiro (Jan 15 2019 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155165860):
> is that a thing?

Sure, you can use interpretations as morphisms between theories even with different languages

#### [ Reid Barton (Jan 16 2019 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155247432):
```quote
I think you want high precedence (above `max = 1024`) to get `presheaf Xᵒᵖ` = `presheaf (Xᵒᵖ)`
```
 Implemented at https://github.com/leanprover/mathlib/pull/600 (@**Johan Commelin** FYI)

#### [ Johan Commelin (Jan 16 2019 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20expected%20type%20equals%20given%20type/near/155248248):
@**Reid Barton** Thanks!


{% endraw %}
