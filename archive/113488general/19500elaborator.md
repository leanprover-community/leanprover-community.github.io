---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/19500elaborator.html
---

## [general](index.html)
### [elaborator](19500elaborator.html)

#### [Kevin Buzzard (Apr 01 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491100):
Over the last few months I have been idly writing something called "from unicode to bytecode", which is some (still extremely incomplete) documentation as to how Lean turns a string of unicode characters (the input file) into bytecode. One reason it's incomplete currently is that I have no real idea what bytecode is. But when I started this project I had no idea what a scanner / parser / token / etc was either, so I'm definitely moving forwards.

#### [Kevin Buzzard (Apr 01 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491140):
I am now trying to understand the elaborator better. Here is a very basic question.

#### [Kevin Buzzard (Apr 01 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491183):
This works (by which I think I mean "Lean's kernel manages to fully parse and elaborate the string of characters and add a new term `easy` to the environment"):

#### [Kevin Buzzard (Apr 01 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491186):
`theorem  easy {i : ℕ} {n : ℕ} : i < n → i < nat.succ n :=  λ H, lt.trans H $ nat.lt_succ_self n`

#### [Kevin Buzzard (Apr 01 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491187):
If I replace the `n` with an underscore, it still works

#### [Kevin Buzzard (Apr 01 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491188):
`theorem  easy {i : ℕ} {n : ℕ} : i < n → i < nat.succ n :=  λ H, lt.trans H $ nat.lt_succ_self _`

#### [Kevin Buzzard (Apr 01 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491196):
Somehow Lean knows from the type of everything that it wants `nat.lt_succ_self _` to have type `n  < nat.succ n` and hence it knows `_` should be `n`

#### [Kevin Buzzard (Apr 01 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491197):
But this doesn't work:

#### [Kevin Buzzard (Apr 01 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491238):
`theorem  easy {i : ℕ} {n : ℕ} : i < n → i < nat.succ n :=  λ H, lt.trans _ $ nat.lt_succ_self n`

#### [Kevin Buzzard (Apr 01 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491239):
Here Lean knows from type theory that it wants `_` to be a proof of `i < n`

#### [Kevin Buzzard (Apr 01 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491245):
and even though `H : i < n` is in the local context, it won't take it and insert it.

#### [Kevin Buzzard (Apr 01 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491246):
We get an error which, if you don't understand magic, looks silly:

#### [Kevin Buzzard (Apr 01 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491248):
```
don't know how to synthesize placeholder
context:
i n : ℕ,
H : i < n
⊢ i < n 
```

#### [Kevin Buzzard (Apr 01 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491289):
"Well, you knew how to synthesize `n` when that was in the local context..."

#### [Kevin Buzzard (Apr 01 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491296):
I think that as a learner (as I still am, but I am thinking more about people who are like I was last October, i.e. complete beginners), you have to just trust some stuff to magic.

#### [Kevin Buzzard (Apr 01 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491297):
You type "simp" and sometimes it works and sometimes it doesn't, but if it does, then you'll take it.

#### [Gabriel Ebner (Apr 01 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491338):
Maybe your confusion comes from the fact that the two situations are in fact very different.  In the first one, Lean doesn't just guess and take a natural number from the local context.  The reason that the placeholder gets filled in is because `n` is *the only possible choice* if you want the theorem to type-check.

#### [Gabriel Ebner (Apr 01 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491339):
In the second case, *any value* of type `i < n` would work.

#### [Kevin Buzzard (Apr 01 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491340):
I think that whilst initially this way of thinking -- "sometimes it just works by magic" -- is initially the only way to proceed.  But now I want to start understanding Lean properly and in particular I want to know exactly what I can expect the elaborator to do.

#### [Kevin Buzzard (Apr 01 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491345):
Thanks Gabriel, I could see that the situations somehow felt different but you have very quickly got to the heart of the matter.

#### [Sebastian Ullrich (Apr 01 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491396):
In other words, the first placeholder can be solved by unification while type checking the right-hand side. The second one cannot.

#### [Kevin Buzzard (Apr 01 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491445):
I think that the `_` (when it is representing `n`) gets filled in initially as something like `?m_1`

#### [Kevin Buzzard (Apr 01 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491451):
Oh it perhaps even initially gets filled in as `(?m_1 : nat)`

#### [Kevin Buzzard (Apr 01 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491492):
and then we have to solve `nat.lt_succ_self (?m_1 : nat) : n < nat.succ n`

#### [Kevin Buzzard (Apr 01 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491499):
and we know the type of `nat.lt.succ_self` is `?m_1 < nat.succ ?m_1`

#### [Kevin Buzzard (Apr 01 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491541):
and those two types really now have to be _equal_. I realise now I am slightly unsure what it means for two types to be equal. For example if `?m_1` was equal to `m` and it was a theorem that `m = n`, would these two types be equal?

#### [Gabriel Ebner (Apr 01 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491542):
Pretty much in this order.  You essentially start with `?m_1: ?m_2` and `?m_2: Sort ?u_3` for the underscore. Then the elaborator wants to construct the application `nat.lt_succ_self ?m_1`, so it needs to make sure that the type of `?m_1` is `nat`, and you get the unification constraint `?m_2 =?= nat`.

#### [Kevin Buzzard (Apr 01 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491547):
I have seen Mario writing these `=?=`s

#### [Gabriel Ebner (Apr 01 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491548):
>   it was a theorem that m = n, would these two types be equal?

No, only definitional equality is used in unification.

#### [Kevin Buzzard (Apr 01 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491549):
And these types would be equal because of some theorem

#### [Gabriel Ebner (Apr 01 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491551):
`=?=` is just the notation for "should unify with"

#### [Kevin Buzzard (Apr 01 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491552):
I could probably answer these questions myself now

#### [Gabriel Ebner (Apr 01 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491587):
unification = assign the ?m_1, ..., ?m_n in such a way that the two sides are definitionally equal

#### [Kevin Buzzard (Apr 01 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491593):
if I could get Lean to print out these `=?=` constraints myself.

#### [Kevin Buzzard (Apr 01 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491595):
Is there some set_option I can turn on

#### [Kevin Buzzard (Apr 01 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491596):
so I can just watch it all happening?

#### [Kevin Buzzard (Apr 01 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491597):
I remember when I discovered set_option pp.all true and very quickly developed a much better understanding of what a term was

#### [Kevin Buzzard (Apr 01 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491605):
and when I discovered various set_option things for simp and very quickly got a much better understanding of what simp di.

#### [Kevin Buzzard (Apr 01 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491606):
did

#### [Gabriel Ebner (Apr 01 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491607):
```lean
set_option trace.type_context.is_def_eq true
```

#### [Kevin Buzzard (Apr 01 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491660):
oh gosh

#### [Kevin Buzzard (Apr 01 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491661):
even when I fill in all the `_`

#### [Kevin Buzzard (Apr 01 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491662):
I still get outputs

#### [Kevin Buzzard (Apr 01 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491702):
This must be because of `@`

#### [Kevin Buzzard (Apr 01 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491709):
`theorem  easy {i : ℕ} {n : ℕ} : i < n → i < nat.succ n :=  λ H, lt.trans H $ nat.lt_succ_self n`

#### [Gabriel Ebner (Apr 01 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491712):
The output also includes all the unification you get for type-checking, even if there are no underscores.

#### [Kevin Buzzard (Apr 01 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491713):
produces two bursts of excitement:

#### [Kevin Buzzard (Apr 01 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491714):
```


[type_context.is_def_eq] ℕ =?= ?m_1 ... success  (approximate mode)
[type_context.is_def_eq] ℕ =?= ?m_1 ... success  (approximate mode)
[type_context.is_def_eq] ℕ =?= ?m_1 ... success  (approximate mode)
[type_context.is_def_eq] ℕ =?= ?m_1 ... success  (approximate mode)
[type_context.is_def_eq] ℕ =?= ?m_1 ... success  (approximate mode)
[type_context.is_def_eq] ℕ =?= ?m_1 ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 =?= ℕ ... success  (approximate mode)
[type_context.is_def_eq] ℕ =?= ℕ ... success  (approximate mode)
[type_context.is_def_eq] ℕ =?= ℕ ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 =?= n ... success  (approximate mode)
[type_context.is_def_eq] ℕ =?= ?m_1 ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 =?= nat.has_lt ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 =?= nat.has_lt ... success  (approximate mode)


 
```

#### [Kevin Buzzard (Apr 01 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491755):
and

#### [Gabriel Ebner (Apr 01 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491757):
Yes, I'm not sure how much you can learn from the output.

#### [Kevin Buzzard (Apr 01 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491758):
```
[type_context.is_def_eq] ?m_1 =?= i < n ... success  (approximate mode)
[type_context.is_def_eq] i < nat.succ n =?= ?m_3 < ?m_4 ... success  (approximate mode)
[type_context.is_def_eq] partial_order.to_preorder ℕ =?= partial_order.to_preorder ℕ ... success  (approximate mode)
[type_context.is_def_eq] i < n =?= ?m_3 < ?m_4 ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 =?= ?m_4 < ?m_5 ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 =?= H ... success  (approximate mode)
[type_context.is_def_eq] ?m_3 < ?m_4 =?= ?m_5 < nat.succ ?m_5 ... success  (approximate mode)
[type_context.is_def_eq] ℕ =?= ℕ ... success  (approximate mode)
[type_context.is_def_eq] ℕ =?= ℕ ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 =?= n ... success  (approximate mode)
[type_context.is_def_eq] n < nat.succ n =?= ?m_3 < ?m_4 ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 =?= nat.lt_succ_self n ... success  (approximate mode)
[type_context.is_def_eq] i < n → i < nat.succ n =?= i < n → i < nat.succ n ... success  (approximate mode) 
```

#### [Kevin Buzzard (Apr 01 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491760):
In my current state I can probably learn quite a bit

#### [Kevin Buzzard (Apr 01 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491810):
I think the guilty party is `lt.trans`

#### [Kevin Buzzard (Apr 01 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491811):
or, as it should really be known

#### [Kevin Buzzard (Apr 01 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491813):
[rips mask off in Scooby-doo like manner]

#### [Kevin Buzzard (Apr 01 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491815):
`@lt_trans _ _ _ _ _`

#### [Kevin Buzzard (Apr 01 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491865):
Hmm

#### [Kevin Buzzard (Apr 01 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491866):
```
definition  Npreorder : preorder ℕ :=  by apply_instance

theorem  easy' {i : ℕ} {n : ℕ} : i < n → i < nat.succ n :=
λ H, @lt.trans ℕ Npreorder i n (nat.succ n) H $ nat.lt_succ_self n
```

#### [Kevin Buzzard (Apr 01 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491911):
I still get a bunch of output from ` set_option trace.type_context.is_def_eq true `

#### [Kevin Buzzard (Apr 01 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491913):
aargh it's the notation

#### [Kevin Buzzard (Apr 01 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491958):
` [type_context.is_def_eq] ?m_1 =?= n ... success  (approximate mode)`

#### [Kevin Buzzard (Apr 01 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491959):
Nice to see we're in "approximate mode"

#### [Kevin Buzzard (Apr 01 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491960):
Doesn't fill me with confidence

#### [Gabriel Ebner (Apr 01 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491965):
Checking the equality of two terms without metavariables is a special case of unification.  That's also why it's called `is_def_eq`.  So whenever the elaborator makes sure that a term type-checks, it will produce unification constraints.

#### [Kevin Buzzard (Apr 01 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492018):
Am I "being the elaborator" at the minute? So far I am up to

#### [Kevin Buzzard (Apr 01 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492020):
``` 
definition  Npreorder : preorder ℕ :=  by apply_instance
definition  Nhas_lt : has_lt ℕ :=  by apply_instance

theorem  easy' {i : ℕ} {n : ℕ} : @has_lt.lt ℕ Nhas_lt i n →  @has_lt.lt ℕ Nhas_lt i (nat.succ n) :=
λ H, @lt.trans ℕ Npreorder i n (nat.succ n) H $ nat.lt_succ_self n
```

#### [Kevin Buzzard (Apr 01 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492021):
I am having real trouble elaborating this any more.

#### [Kevin Buzzard (Apr 01 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492068):
In fact I would go so far to say that this term can't be elaborated any more.

#### [Kevin Buzzard (Apr 01 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492070):
although of course things could be unfolded.

#### [Kevin Buzzard (Apr 01 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492081):
What does the unfolding? Is that still the elaborator? Does the elaborator have to think about the actual definition of the term `@has_lt.lt` or does it just check its type?

#### [Kevin Buzzard (Apr 01 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492125):
I am not sure I care at all about the definition of `@has_lt.lt nat Nhas_lt`, all I need to know is that N is a preorder.

#### [Gabriel Ebner (Apr 01 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492126):
If you need to unify `has_lt.lt a b c d` and `nat.lt c d`, then yes, the elaborator will unfold `has_lt.lt`.

#### [Gabriel Ebner (Apr 01 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492128):
In this case, I don't think we unfold `has_lt.lt` anywhere.  (At least we don't need to.)

#### [Gabriel Ebner (Apr 01 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492180):
The `easy'` theorem is still missing the domain of the lambda, if you want to write down a "fully elaborated" term.

#### [Gabriel Ebner (Apr 01 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492235):
BTW, I believe it's a mistake to think of elaboration as "filling things in" (even though that may be literal meaning of the word).  From a big picture point of view elaboration is the translation of pre-expressions (which are close to what you write down) to type-correct terms in the core type theory.  Personally I think of a pre-expression more like a recipe that tells the elaborator to do what you want.

#### [Kevin Buzzard (Apr 01 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492240):
Oh! Yes, I forgot about the lambda.

#### [Kevin Buzzard (Apr 01 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492245):
So am I changing a `pexpr` to an `expr`?

#### [Gabriel Ebner (Apr 01 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492248):
No, you're changing one `pexpr` into another `pexpr`.

#### [Kevin Buzzard (Apr 01 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492254):
dammit I want an expr

#### [Kevin Buzzard (Apr 01 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492259):
I read about them in the manual

#### [Kevin Buzzard (Apr 01 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492267):
I am concerned that I might have more than one `<=` on my `nat`

#### [Kevin Buzzard (Apr 01 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492279):
`Npreorder` says that `nat` has the structure of a `preorder`

#### [Gabriel Ebner (Apr 01 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492310):
I guess as an exercise you could write down the proof of `easy` using the `expr` constructors:
```lean
open tactic expr
theorem easy {i n} : i < n -> i < nat.succ n :=
by do exact $ lam /- fill in here -/
```

#### [Kevin Buzzard (Apr 01 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492323):
and the `<` on it is I think called something like `Npreorder.lt`

#### [Kevin Buzzard (Apr 01 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492331):
but the `<` I want is called `has_lt.lt`

#### [Kevin Buzzard (Apr 01 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492373):
Actually I don't even know what it's called

#### [Gabriel Ebner (Apr 01 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492379):
Yes, they are many `lt`s on `nat` and they all mean the same in the end.  AFAICT you have `has_lt.lt` everywhere though, as you should.

#### [Kevin Buzzard (Apr 01 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492380):
it's called `Nhas_lt` I guess

#### [Kevin Buzzard (Apr 01 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492383):
I am not so sure about the `lt` coming from the preorder

#### [Kevin Buzzard (Apr 01 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492391):
I used type class inference to define the preorder on `nat`

#### [Gabriel Ebner (Apr 01 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492433):
Ah, I understand now.  The question is about the relation between `Npreorder` and `Nhas_lt`: the terms `@preorder.to_has_lt nat Npreorder` and `Nhas_lt` are definitionally equal.  (And type-checking actually needs to verify this equality.)

#### [Kevin Buzzard (Apr 01 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492439):
The more I elaborate, the greater the output of ` set_option trace.type_context.is_def_eq true` becomes!

#### [Kevin Buzzard (Apr 01 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492993):
```quote
I guess as an exercise you could write down the proof of `easy` using the `expr` constructors:
```lean
open tactic expr
theorem easy {i n} : i < n -> i < nat.succ n :=
by do exact $ lam /- fill in here -/
```
```
Oh I like this comment. Thanks! I might start with something easier than `easy` but this looks like a fun game :-)

#### [Kevin Buzzard (Apr 01 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124493033):
I might well find it a challenge to prove `1 + 1 = 2` in this mode

#### [Kevin Buzzard (Apr 01 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124493239):
woo I made Prop

#### [Kevin Buzzard (Apr 01 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124493240):
`meta  definition  prop : expr (ff) := expr.sort level.zero`

#### [Kevin Buzzard (Apr 01 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124493279):
That's the proof that `expr` is inhabited

#### [Sebastian Ullrich (Apr 01 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124493342):
Note that `expr ff = pexpr`

#### [Kevin Buzzard (Apr 01 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124493495):
I just noticed that expr was demanding a bool so I gave it one

#### [Kevin Buzzard (Apr 01 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124493541):
Hmm, that's funny. `pexpr.lean` says ` @[reducible]  meta  def  pexpr  := expr ff`

#### [Kevin Buzzard (Apr 01 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124493545):
but `#print pexpr` says that it's ` id_rhs Type (expr ff) `

#### [Kevin Buzzard (Apr 01 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124493584):
rofl and `id_rhs` is an abbreviation. @**Kenny Lau** here's when you should use reducible, apparently, and abbreviations too.

#### [Kenny Lau (Apr 01 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124493591):
so when exactly?

#### [Kevin Buzzard (Apr 01 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494493):
Oh this is all much too hard. I don't know how to turn anything at all into an expr. How do I turn a nat into an expr? How do I turn a Prop into an expr? How do I turn a proof into an expr? How do I turn a Type into an expr? Oh -- are these questions too general?

#### [Kevin Buzzard (Apr 01 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494496):
How do I turn a constructor into an expr? Is that a sensible question?

#### [Kevin Buzzard (Apr 01 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494501):
How do I turn` nat.zero` into an expr?

#### [Kevin Buzzard (Apr 01 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494542):
If `f : X -> Y` and I have an expr `ex` representing the...name? `x : X` , how do I create an expr corresponding to `f x`?

#### [Kevin Buzzard (Apr 01 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494550):
How do I turn `eq.refl` into an expr?

#### [Kevin Buzzard (Apr 01 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494589):
This sort of exercise might be a really good bridge to the Programming In Lean book.

#### [Kevin Buzzard (Apr 01 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494590):
All this expr stuff is introduced at the same time as everything else somehow

#### [Kevin Buzzard (Apr 01 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494592):
Perhaps one can abstract it away first

#### [Kevin Buzzard (Apr 01 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494598):
and think about making exprs from usual Lean terms rather than letting the elaborator do it

#### [Kevin Buzzard (Apr 01 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494647):
Does the elaborator take a list of tokens and return an expr?

#### [Kevin Buzzard (Apr 01 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494686):
I am still at the stage where I don't know if I have the words right

#### [Kevin Buzzard (Apr 01 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494741):
I feel like this could be a cute blog post, explaining how to get from a string of unicode characters to an expr, even a really stupid string like `theorem  X : unit = unit := eq.refl unit`

#### [Kevin Buzzard (Apr 01 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494748):
I don't know how to turn this into an expr

#### [Kevin Buzzard (Apr 01 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124498667):
```
theorem  very_easy : unit = unit :=
by  do to_expr ```(eq.refl unit) >>= exact
```

#### [Kevin Buzzard (Apr 01 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124498669):
that's kind of a cheat because I didn't start ` by do exact $ `

#### [Kevin Buzzard (Apr 01 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124498712):
but all this stuff like `get_local` and `to_expr`, all these functions return `tactic` something.

#### [Kevin Buzzard (Apr 01 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124498724):
Do I have to use the tactic monad?

