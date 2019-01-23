---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85947ProgramminginLean.html
---

## Stream: [general](index.html)
### Topic: [Programming in Lean](85947ProgramminginLean.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129464604):
The following code from Chapter 9 of Programming in Lean doesn't work in `lean-nightly-2018-04-20`
```lean
meta def normalize_hyp (lemmas : list expr) (hyp : expr) : tactic unit :=
do try (simp_at hyp lemmas)

meta def normalize_hyps : tactic unit :=
do hyps ← local_context,
lemmas ← monad.mapm mk_const [``iff_iff_implies_and_implies,
``implies_iff_not_or, ``not_and_iff, ``not_or_iff, ``not_not_iff,
``not_true_iff, ``not_false_iff],
monad.for' hyps (normalize_hyp lemmas)
```

Can someone help me get it working??

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 11 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465591):
You can rewrite the first function as:

```lean
meta def normalize_hyp (lemmas : list expr) (hyp : expr) : tactic unit :=
do try (simp_hyp lemmas [] hyp)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 11 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465655):
For the second function, this should work:

```lean
meta def normalize_hyps : tactic unit :=
do hyps ← local_context,
lemmas ← list.mmap mk_const [``iff_iff_implies_and_implies,
``implies_iff_not_or, ``not_and_iff, ``not_or_iff, ``not_not_iff,
``not_true_iff, ``not_false_iff],
hyps.mmap' (normalize_hyp lemmas)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465732):
It doesn't quite work. It complains lemmas has type `list expr` but needs to have type `simp_lemmas`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465747):
I'm a bit confused about the type `simp_lemmas`. It's defined as a constant, which seems a bit odd to me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465798):
it's a special cached representation of a simp set

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465801):
you should use the `simp_lemmas` functions to construct one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465810):
So it looks almost like an inductive type, but they made all the constructors constants for some reason.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465815):
I'll see if I can fix the list myself.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 11 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465842):
`simp_lemmas.append` and `simp_lemmas.mk` should be sufficient

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 11 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465874):
```lean
meta def normalize_hyps : tactic unit :=
do hyps ← local_context,
lemmas ← list.mmap mk_const [``iff_iff_implies_and_implies,
``implies_iff_not_or, ``not_and_iff, ``not_or_iff, ``not_not_iff,
``not_true_iff, ``not_false_iff],
simp_lemmas.append simp_lemmas.mk lemmas,
hyps.mmap' (normalize_hyp lemmas)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 11 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465882):
... and adjust `normalize_hyp` accordingly ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129466489):
Yesterday we found something else in PIL which didn't work any more (I think the first line was `open state` and already that failed IIRC). Maybe Chris and I should collect up some updates for Lean 3.4.1 and submit a PR. Would that sort of thing be welcome?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129466694):
How does the notation with the backticks and brackets work? What's the difference between `'x`, `'''x`, `'''x`, `'(x)`, `''(x) and `'''(x)`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129467739):
* `` `my.name`` is the way to refer to a name. It is essentially a form of string quoting; no checks are done besides parsing dots into namespaced names
* ``` ``some ``` does name resolution at parse time, so it expands to `` `option.some`` and will error if the given name doesn't exist
* `` `(my expr)`` constructs an expression at parse time, resolving what it can in the current (of the tactic) namespace
* ``` ``(my pexpr)``` constructs a pre-expression at parse time, resolving in the current (of the tactic) namespace
* ```` ```(my pexpr)```` constructs a pexpr, but defers resolution to run time (of the tactic), meaning that any references will be resolved in the namespace of the begin end block of the user, rather than the tactic itself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129468544):
So can I give ` ''(my pexpr)` when an `expr` is expected and it will elaborate it into an `expr` at parse time?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 11 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129468811):
About back ticks and quoting them: you can include them ``` `` `(foo) `` ``` by using one more backtick to quote what's inside

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 11 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129468833):
And I produced the above by writing  ```` ``` `` `(foo) `` ``` ````

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129468922):
If an `expr` is expected, then you should either use `` `(my expr)`` to construct one, or ```to_expr ``(my pexpr)``` or one of its variants to perform elaboration (but not name resolution) at run time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jul 11 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471102):
I see you are starting a very useful cheat sheet on backticks. Maybe you could add a word on `` `[apply %%h]``? (as far as I can tell, it is not mentioned in Programming in Lean)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471295):
``` `[tac...] ``` is exactly the same as `begin tac... end` in the sense that it parses `tac...` using the interactive mode parser, but instead of evaluating the tactic to produce a term, it just wraps up the list of tactics as a single tactic of type `tactic unit`. This is useful for writing "macros" or light-weight tactic writing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471423):
What is `%%`? I couldn't find it in programming in lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471498):
Re `%%`: This is called anti-quotation, and is supported in all the expr and pexpr quoting expressions `` `(expr)``,  ``` ``(pexpr)```,  ```` ```(pexpr)````, as well as `` `[tacs]``. Wherever an expression is expected inside one of these quoting constructs, you can use `%%e` instead, where `e` has type `expr` in the outer context of the tactic, and it will be spliced into the constructed expr/pexpr/etc.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471551):
are `` ` `` and `%%` notation for some function or some deeper inbuilt thing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471568):
a bit of both

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471589):
It is difficult to completely replicate the behavior of the quoting expressions, but `%%` is supported through `pexpr.subst` if I recall correctly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471593):
so `%%` turns an `expr` into the thing that the `expr` represents, like a `real` or a `nat` or something?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471638):
You can always just write it down and then inspect the resulting tactic with `#print` to find out how the sausage is made

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471654):
No, `%%` inserts the `expr` into a hole in another `expr` you are creating

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471681):
For example, if `a b : expr` then `` `(%%a + %%b)`` is of type `expr`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471748):
Probably `a` and `b` are expressions for something of type `nat`, say, and then the resulting `expr` will also be a valid expression for a `nat`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471969):
Also worth mentioning are `expr` pattern matches, which have the same syntax like `` `(%%a + %%b)``. These can be used in the pattern position of a `match` or on the left side of a `<-` in do notation, and will destruct an expression and bind the antiquoted variables

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129472100):
For example, if `e` is an expression then ``do `(%%a = %%b) <- return e, ...`` will check that `e` is an equality, and bind the LHS and RHS to `a` and `b` (of type `expr`), and if it is not an equality the tactic will fail

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129472732):
so when you say `` `(my expr)  ``, `my expr` is not an object of type `expr` it's an actual expression like `` `(2 + 2) ``

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129472907):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129482162):
How do tactics that take arguments work? I'm trying to write the easiest tactic I could think of, which basically does `apply quotient.induction_on, intros` I'm not sure what the type of the argument to the tactic should be, or even if it should be an argument. I couldn't find anything in `PIL` on this.
```lean
import tactic.interactive data.multiset

meta def qcases (x : pexpr) : tactic unit :=
`[apply quotient.induction_on %%x, intro]

example (x : multiset ℕ) : x = sorry :=
begin
  qcases x,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jul 11 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129483237):
See section 6 of https://leanprover.github.io/papers/tactic.pdf; this is the best source for tactic writing, because it's the only one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129483792):
Thanks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 13 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129608241):
One thing I've noticed is that putting tactics in the `tactic.interactive` namespace changes their behaviour. For example the following code.
Should all tactics be in the `tactic.interactive` namespace? What difference does this namespace make to their behaviour?
```lean
open tactic tactic.interactive interactive.types interactive lean.parser

meta def skip2 (p : parse texpr) : tactic unit :=
do `[skip]

meta def skip3 : tactic unit :=
do `[skip]

namespace tactic.interactive

meta def skip4 (p : parse texpr) : tactic unit :=
do `[skip]

end tactic.interactive

example (s : ℕ) : s = sorry := 
begin
  skip4 s, --works
  skip3,   --works
  skip2 s, --fails
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jul 13 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129608635):
Also section 6 :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129614422):
The interactive namespace is where the tactics which you use in tactic mode live. Is there a difference between `by x` and `begin x end`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 13 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129615276):
I think officially, `begin x end` is shorthand for `by { x }`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 14 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129654459):
So if I look at the definition of `monad`, and some other definitions in `tactic.interactive`, there are `:=` in places I haven't seen them before. What does it mean to put a `:=` in a field of a structure like this? Same question for the `cfg` argument of `dunfold`.
```lean
class monad (m : Type u → Type v) extends applicative m, has_bind m : Type (max (u+1) v) :=
(map := λ α β f x, x >>= pure ∘ f)
(seq := λ α β f x, f >>= (<$> x))

meta def dunfold (cs : parse ident*) (l : parse location) (cfg : dunfold_config := {}) : tactic unit :=
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 14 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129654705):
Aren't they default values for these fields?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 14 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129655071):
I thought that's what they probably were, but I wasn't sure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 14 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129655083):
see https://leanprover.github.io/reference/declarations.html#structures-and-records

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 14 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129655118):
> Lean also allows you to specify a default value for any field in a structure by writing (fieldᵢ : βᵢ := t).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 14 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129657371):
Here's an example from core lean (init/algebra/order):

```lean
class preorder (α : Type u) extends has_le α, has_lt α :=
(le_refl : ∀ a : α, a ≤ a)
(le_trans : ∀ a b c : α, a ≤ b → b ≤ c → a ≤ c)
(lt := λ a b, a ≤ b ∧ ¬ b ≤ a)
(lt_iff_le_not_le : ∀ a b : α, a < b ↔ (a ≤ b ∧ ¬ b ≤ a) . order_laws_tac)
```

I guess it means you can either skip the definition of `lt` or decide to over-write

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 14 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129659353):
Another thing that's very odd about the `meta` code is the use of the `constant` keyword everywhere. If I look at the type `simp_lemmas` for example, it's almost like an inductive type, but all the constructors are constants. This just seems totally unworkable to me, because there aren't any eliminators. Is this because this stuff interfaces with C++ code? Or is this some weird case of the programming with expressions rather than data, where defeq terms can give different behaviour if they are syntactically different.
```lean
meta constant simp_lemmas : Type
meta constant simp_lemmas.mk : simp_lemmas
meta constant simp_lemmas.join : simp_lemmas → simp_lemmas → simp_lemmas
meta constant simp_lemmas.erase : simp_lemmas → list name → simp_lemmas
meta constant simp_lemmas.mk_default : tactic simp_lemmas
meta constant simp_lemmas.add : simp_lemmas → expr → tactic simp_lemmas
meta constant simp_lemmas.add_simp : simp_lemmas → name → tactic simp_lemmas
meta constant simp_lemmas.add_congr : simp_lemmas → name → tactic simp_lemmas
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 14 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129659882):
It's not an inductive type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 14 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129659925):
that's why there are no eliminators

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 14 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129659944):
The reason it's all meta constants is, as you say, that it is interfacing with C++

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 14 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129659946):
these are all just hooks to C++ functions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 14 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129660104):
If by "eliminator" you mean "a way to use this `simp_lemmas` thing once I've built one", that would be in tactics like `ext_simplify_core` and such that accept a `simp_lemmas` object to simp with

