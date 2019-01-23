---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/87862liftingthetacticmonad.html
---

## Stream: [general](index.html)
### Topic: [lifting the tactic monad](87862liftingthetacticmonad.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132682369):
Several times I have wanted to use a lift of the tactic monad, in order to carry along some additional state. (As a simple example, I would like to carry along a ℕ that limits how much more computation is allowed, that several different subtactics need to respect.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132682450):
I've successfully written some infrastructure to do this (essentially, some typeclasses and coercions that let you move up and down from standard `tactic α` to `stateful_tactic β α`), but it was gross and hackish.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132682468):
Is this something that others would find useful? If so, could we agree on a basic design that everyone would be happy with?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 24 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132682484):
I think https://github.com/EdAyers/lean-humanproof/blob/a3df90b4ccd1356283e47cf56b986701944f4100/src/robot.lean#L38 might be an example of how to do that...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 24 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132682490):
So you need to use `state_t`...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132682628):
Yes --- that's exactly another example of what I have in mind.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132682641):
The problem is now writing metatactics that are "monad polymorphic".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132682671):
We need a typeclass that you can decorate your lift of `tactic` (e.g. @**Edward Ayers**'s `robot`) with, that says that it really is a lift of `tactic`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132682966):
Ah, there is more in `state_t` than I'd seen before.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132684057):
I think I'm still not understanding how I'm meant to use `state_t`. I want to be able to write something like
```
variables {m : Type → Type → Type} [stateful_tactic m]

meta def my_meta_tactic {α β} (f : α → β) (t : m σ α) : m σ β :=
do
  get_state >>= trace, -- prints the current state, a term of type σ
  r ← t,
  trace r,             -- prints the result of t, a term of type α
  get_state >>= trace, -- prints the new state, a term of type σ
  done,
  return (f r)
```

Here `trace` and `done` are meant to just be the standard ones from `tactic`, that are being automatically lifted to `stateful_tactic`
(such that they just preserve the σ state).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132684651):
Clearly `state_t` isn't quite doing this: it doesn't even mention `tactic`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 24 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132685496):
Your `m` is just `λ σ, state_t σ tactic`. I'm not sure if the coercions from `tactic` are in the library, but they're very easy to write.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 24 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132690060):
```lean
meta structure my_state :=
(my_bool : bool)
(my_nat : nat) 
@[reducible] meta def state_tactic : Type → Type := state_t my_state tactic
meta def of_tactic {α} : tactic α → state_tactic α := state_t.lift
meta instance {α} : has_coe (tactic α) (state_tactic α) := ⟨of_tactic⟩
open tactic
meta def my_meta_tactic {α β : Type} (f : α → β) (t : state_tactic α) : state_tactic β :=
do
    state ← get, --get the state
    trace state.my_nat,
    r ← t,
    put {my_nat:= 100, ..state}, --set the state
    done, -- done is a tactic but the coercion converts it to a state_tactic.
    return $ f r



```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 24 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132690204):
All of the `alternative` stuff works out of the box. `<|>`, `guard` and so on.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132691315):
Thanks @**Edward Ayers**. This isn't quite there yet: I still want to abstract over `my_state`. That is, I want to be able to write `my_meta_tactic` so that it works with many different monads, as long as they come with a promise that they contain `my_state`, but possibly may carry additional state as well.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132691330):
That is, sometimes I will write tactics that refer to some specific notion of state.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 24 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132691379):
But other times I want to write a meta tactic that is merely sufficient polymorphic that is can pass through notions of state that other people might need.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 24 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132692605):
I guess if you are only storing bools nats and strings you can use `tactic.set_options` as a quick fix.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 24 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132693624):
I came up with a crazy idea that would solve this. The trouble is the type universes don't work and one would have to implement the `dependent_dict` object!

```lean
--I think that you can implement this as an rbtree but it's a lot of effort.
universe u
constant dependent_dict (key : Type u) (α : key → Type u) : Type u
namespace dependent_dict
    variables {key : Type u} {α : key → Type u}
    constant get (k : key) (d : dependent_dict key α) : option (α k)
    constant set (k : key) (value : α k) (d : dependent_dict key α) : dependent_dict key α
end dependent_dict

meta structure custom_state :=
(name : string)
(type : Type)
(default : type)
-- [TODO] define an ordering according to `name`
meta def custom_state_tactic := state_t (dependent_dict custom_state (λ c:custom_state, c.type)) tactic
namespace custom_state_tactic
    meta def get (st : custom_state) : custom_state_tactic st.type := do
        d ← state_t.get,
        pure $ option.get_or_else (dependent_dict.get st.name d) st.default
    meta def set (st : custom_state) (value : st.type) : (custom_state_tactic unit) := do
        d ← state_t.get,
        state_t.put (dependent_dict.set st value d)
end custom_state_tactic
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 24 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132693642):
So the idea is you would always use `custom_state_tactic` but define your own instance of `custom_state` to get the values that you care about.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 24 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132693690):
I don't think this will work but I thought I'd share.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 24 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132693809):
It also wouldn't work because you could give two `custom_state`s the same name but different types, and I don't think we have decidable equality for types

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 24 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132701340):
@**Scott Morrison** are you familiar with the design of [mtl](http://hackage.haskell.org/package/mtl)?
[MonadState](http://hackage.haskell.org/package/mtl-2.2.2/docs/Control-Monad-State-Class.html) is your "monad that comes with a promise that it contains `my_state`", I think.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 24 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132701413):
But I'm not sure if this encompasses everything you want

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Aug 24 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132702480):
`monad_state` is already in Lean 3. A `monad_tactic` might be introduced in Lean 4.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 24 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132703270):
It would just be `has_monad_lift_t tactic`, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 24 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132703274):
Up to specializing names

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Aug 24 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132703524):
That is not sufficient for lifting `tactic _ -> tactic _` functions or even more complex ones

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 24 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132703985):
Oh, I've never actually wanted to do that with IO, and I'm not sure I trust any of the packages which claim to solve that problem anyways.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 24 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132703997):
Maybe `tactic` has more compelling use cases

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Aug 24 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132704242):
Yeah, it's way more important for `tactic` since it has a bunch of combinators like `try`, `focus`, `any_goals`, ...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 28 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132912880):
Using `monad_state`works really well for me.


{% endraw %}
