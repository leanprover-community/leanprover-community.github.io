---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29043hiddenfunction.html
---

## Stream: [general](index.html)
### Topic: [hidden function](29043hiddenfunction.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 15 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/151838238):
I just noticed a very clever trick that was used in a Coq development. We can define the following function:
```lean
@[reducible] def hidden {α : Sort*} {a : α} := a
```
This obviously isn't a very ergonomic function to write directly, but it can be used in tactics that have to manipulate large proof states and display them to the user, without getting in the way of any automation. (I should investigate if this is an appropriate use of `abbreviation`.) For example, we could have a tactic `hide x` which `change`s the type of `x : T` to `x : @hidden _ T`. The zero arg version could just do this for all assumptions whose pp is above a certain length. The Coq example was using this when proving theorems about large programs, to hide the "rest" of the program when working one statement at a time.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 15 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/151838734):
demo:
```lean
@[reducible] def hidden {α : Sort*} {a : α} := a

open tactic
meta def repl : expr → ℕ → tactic expr
| e 0 := do
  t ← infer_type e,
  expr.sort u ← infer_type t,
  return (expr.app (expr.const ``hidden [u]) t e)
| (expr.app f x) (i+1) := do f' ← repl f (i+1), x' ← repl x i, return (f' x')
| (expr.lam n b d e) (i+1) := do
  var ← mk_local' n b d,
  e' ← repl (expr.instantiate_var e var) i,
  return (expr.lam n b d (expr.abstract_local e' var.local_uniq_name))
| e (i+1) := return e

meta def tactic.interactive.elide (n : ℕ) : tactic unit :=
do t ← target,
  t' ← repl t n,
  tactic.change t'

example : 2 + 2 = 4 :=
begin
  dunfold has_add.add, delta nat.add,
  -- ⊢ nat.brec_on 2
  --       (λ (a : ℕ) (_F : nat.below (λ (a : ℕ), ℕ → ℕ) a) (a_1 : ℕ),
  --         (λ (a a_1 : ℕ) (_F : nat.below (λ (a : ℕ), ℕ → ℕ) a_1),
  --             nat.cases_on a_1 (λ (_F : nat.below (λ (a : ℕ), ℕ → ℕ) 0), id_rhs ℕ a)
  --               (λ (a_1 : ℕ) (_F : nat.below (λ (a : ℕ), ℕ → ℕ) (nat.succ a_1)),
  --                 id_rhs ℕ (nat.succ ((_F.fst).fst a)))
  --               _F)
  --           a_1
  --           a
  --           _F)
  --       2 =
  --     4
  elide 5,
  -- ⊢ nat.brec_on 2 (λ (a : ℕ) (_F : nat.below (λ (a : ℕ), ℕ → ℕ) a) (a_1 : ℕ), hidden) 2 = 4
  refl
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 15 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/151839702):
that's pretty cool :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 15 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/151841751):
It looks pretty cool. What is the exact meaning of the numeric parameter?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 15 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/151841879):
it's the depth at which to start replacing subterms by `hidden`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 15 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/151841932):
so higher means less hidden

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 30 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154049336):
Would it be possible to have a version which replaces proofs by `proof_of P`, where `@[reducible] def proof_of (P : Prop) {p : P} := p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 30 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154049346):
and then maybe add some notation for `proof_of P` to match `\f<P\f>`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 30 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154049362):
I thought that some combination of `pp` options was supposed to do this already, but I never figured out how

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 30 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052011):
well, just replacing that on its own won't work since it's still a prop so it gets displayed as `_` anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 30 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052013):
Oh dang

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 30 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052015):
but if you turn off `pp.proofs` then you can see it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 30 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052068):
Then again, I think tactics can change options so you could have a tactic like `elide` that turns of `pp.proofs` at the same time as the replacement

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 30 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052069):
Oh, turn *off*? Okay, that's one thing that confused me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 30 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052072):
oh that's a good point, I forget the polarity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 30 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052111):
and what difference does `reducible` make?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 30 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052114):
actually now I'm doubly confused

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 30 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052117):
By experiment, I find that `set_option pp.proofs true` will display proofs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 30 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052118):
but that's the default?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 30 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052119):
Yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 30 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052120):
That is what is confusing me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 30 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052126):
At least, that's what the autocompletion menu claims is the default. But setting it to `true` still causes proofs to be printed, and `false` causes them to be elided (which they are by default)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 30 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052128):
reducible doesn't matter much, but it makes these identity functions not interfere with other tactics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 30 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052178):
also the option description is a bit interesting -
> (pretty printer) if set to false, the type will be displayed instead of the value for every proof appearing as an argument to a function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 30 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052187):
Okay, that's where I saw it. I knew I'd seen it claimed somewhere that this feature already existed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 30 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052246):
Maybe there are like... two options with the same name or something

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 30 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052297):
I think the description is outdated... it used to do that and I recall lobbying for the `_` behavior

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 30 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052301):
I'm not sure if the type display thing was removed or replaced

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 30 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052308):
at least in the original version it just put the type instead of the proof and it was really confusing because it wasn't typecorrect

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 30 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052357):
looking at the code, I see no evidence that it does anything other than put `_` in places, and only when `pp.proofs = false`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 30 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052437):
I see. That does sound confusing, if there was nothing distinguishing the types of proofs from actual terms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 30 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052486):
but I still can't figure out how the default turns out to be `false`, the code says it's `true`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 30 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052595):
truth is an illusion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Dec 30 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052597):
There is no constant default: :smile: https://github.com/leanprover/lean/blob/30d883efef422facab3bf351d9fcff90c943298f/src/frontends/lean/pp.cpp#L1911-L1917

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 30 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052639):
wtf is that special case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 30 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052649):
so sneaky

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 30 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052693):
I guess this is so that `#print theorem` doesn't show `theorem thm : T := _` which would not be nice

