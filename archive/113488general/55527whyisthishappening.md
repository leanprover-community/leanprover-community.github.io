---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55527whyisthishappening.html
---

## Stream: [general](index.html)
### Topic: [why is this happening](55527whyisthishappening.html)

---

#### [Koundinya Vajjha (Jan 16 2019 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155291582):
```lean 
open tactic expr

meta def wat : tactic unit := 
do ctx ← local_context,
  let a := app ctx.head (list.reverse ctx).head,
  type ← infer_type a,
  trace type,
  skip

lemma begins  (f : ℕ → ℕ) (a : bool) : Prop := 
begin 
wat,  -- returns ℕ
end 
```
But 
``` lean
variables (a : bool) (g : ℕ  → ℕ )
#check g a
```
returns a type mismatch error?

#### [Kenny Lau (Jan 16 2019 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155291781):
```lean
namespace tactic.interactive
open tactic lean.parser interactive expr
meta def wat : tactic unit :=
do ctx ← local_context,
  let a := app ctx.head (list.reverse ctx).head,
  type ← infer_type a,
  trace type,
  skip
end tactic.interactive

lemma begins  (f : ℕ → ℕ) (a : bool) : Prop :=
begin
wat,  -- returns ℕ
end
```

#### [Kenny Lau (Jan 16 2019 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155291999):
more info:
```lean
namespace tactic.interactive
open tactic lean.parser interactive expr
meta def wat : tactic unit :=
do ctx ← local_context,
  let a := app ctx.head (list.reverse ctx).head,
  type ← infer_type a,
  tactic.interactive.let none none ``(%%a),
  skip
end tactic.interactive

lemma begins  (f : ℕ → ℕ) (a : bool) : Prop :=
begin
wat,
sorry
end
```

tactic state after `wat`:
```
f : ℕ → ℕ,
a : bool,
this : ℕ := f a
⊢ Prop
```

and error message of lemma after I put `sorry`:
```
type mismatch at application
  f a
term
  a
has type
  bool
but is expected to have type
  ℕ
```

#### [Reid Barton (Jan 16 2019 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155292170):
You manually built an `expr`= supposedly fully elaborated expression, but the `expr` you constructed is not actually valid. I guess that `infer_type` assumes the expression is valid and then according to the typing rules its type must be the return type of `f`. You didn't get an error because you didn't do anything with the `expr`.

#### [Rob Lewis (Jan 16 2019 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155292366):
Yeah, `infer_type` doesn't completely type check the expression, otherwise it would be very expensive. There's another tactic called `type_check` that should fail if you call it on `a`.

#### [Reid Barton (Jan 16 2019 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155292374):
If you used `tactic.exact a` (supposing you change the goal to `nat`) then I imagine the tactic would succeed but then you would get a type error at a later stage.

#### [Koundinya Vajjha (Jan 16 2019 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155292406):
@**Reid Barton**  yeah seems like that's what is happening.

#### [Kenny Lau (Jan 16 2019 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155292507):
well it's `meta` so it can be unsound anyway

#### [Koundinya Vajjha (Jan 16 2019 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155292545):
`type_check` is exactly what I needed.

#### [Kenny Lau (Jan 16 2019 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155292547):
you aren't actually changing the partially generated proof by `trace`

#### [Rob Lewis (Jan 16 2019 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155292687):
In general, making applications manually can be difficult. Do it if you're confident in what you're doing, since it will be more efficient. Otherwise `mk_app` and `mk_mapp` are your friends. In particular the error messages will be more helpful.

#### [Koundinya Vajjha (Jan 16 2019 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155293217):
I'm having trouble figuring out how to use `mk_app`.  I have `f : ℕ → ℝ` and `b : ℕ`. How do I use this to make the application `f b`?

#### [Kenny Lau (Jan 16 2019 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155293421):
```lean
namespace tactic.interactive
open tactic lean.parser interactive expr
meta def wat : tactic unit :=
do ctx ← local_context,
  let a := expr.mk_app ctx.head [ctx.reverse.head],
  tactic.type_check a,
  type ← infer_type a,
  trace type,
  tactic.interactive.let none none ``(%%a),
  skip
end tactic.interactive

lemma begins  (f : ℕ → ℕ) (a : ℕ) : ℕ :=
begin
wat,  -- returns ℕ
end
```

#### [Koundinya Vajjha (Jan 16 2019 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20happening/near/155293593):
Okay that was silly. Thanks @**Kenny Lau**

