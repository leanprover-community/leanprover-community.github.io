---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/38732monadicmerge.html
---

## Stream: [general](index.html)
### Topic: [monadic merge](38732monadicmerge.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 20 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123983991):
The monad refactoring PR was merged! Congratulations @**Sebastian Ullrich** !

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 20 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123983995):
You can give us Lean 4 now :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 20 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984190):
Breaking every existing monad instance with that merge should provide a small taste of Lean 4 :stuck_out_tongue:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 20 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984312):
I have a sense you may experience what the Haskell implementers experienced. The Haskell users act like addicts when breaking change occurs. Instead of yelling "You bastards! You broke my code" they say "Amazing! Where's the rest?"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 20 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984389):
Are there existing monad instances? Besides the tactic monad of course (you didn't break that one, did you?)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 20 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984393):
`list` had better be a monad

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 20 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984394):
And the IO monad that is used by leanpkg

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 20 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984396):
I'm sure you also didn't break that one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 20 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984439):
Come on, Leo wouldn't merge a Lean branch with broken `list`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 20 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984443):
`option` had better be a monad

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 20 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984444):
There's also `state` and `option` I believe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 20 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984445):
let's try #print instances monad

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 20 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984456):
```lean
native.resultT_monad : Π {M : Type → Type} [m : monad M] (E : Type), monad (native.resultT M E)
native.result_monad : Π (E : Type), monad (native.result E)
list.monad : monad list
smt_tactic.monad : monad smt_tactic
vm_core.monad : monad vm_core
option_t.monad : Π {m : Type u → Type v} [_inst_1 : monad m], monad (option_t m)
conv.monad : monad conv
monad.transformed_monad : Π (m : Type → Type u_1) (t : Π (m : Type → Type u_1) [_inst_1 : monad m], Type → Type)
[_inst_1 : monad.monad_transformer t] [_inst_2 : monad m], monad (t m)
state_t.monad : Π (σ : Type u) (m : Type u → Type v) [_inst_1 : monad m], monad (state_t σ m)
state.monad : Π (σ : Type u), monad (state σ)
option.monad : monad option
task.monad : monad task
interaction_monad.monad : Π {state : Type}, monad (interaction_monad state)
exceptional.monad : monad exceptional
monad_fail.to_monad : Π (m : Type u → Type v) [c : monad_fail m], monad m
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 21 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124001851):
I meant instances outside of core

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 21 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124003440):
Are there any in mathlib? My limited understanding is that monads are important in core or for people doing programming in Lean, but not for mathematicians

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 21 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124003584):
I guess I use the tactic monad...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 21 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124003591):
Sure, but this one is not broken

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 21 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124003593):
...and the occasional list...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 21 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124003715):
also not broken

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 21 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124003768):
`computation`, `roption`, `pfun`, `seq`, `wseq`, `filter`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 21 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124003771):
Are these names of monads in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 21 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124003773):
Is mathlib currently broken?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 21 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124003776):
probably, haven't had time to check

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 21 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124003787):
seems very unlikely that sebastian's huge merge didn't break mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 21 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124034102):
@**Sebastian Ullrich** What happened to the proofs of `is_lawful_functor option`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 21 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124034711):
Oh, found it - `init.data.option.instances`. This is the first time I've seen a file in `init` import namespace which is not imported by default. Was that deliberate?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 22 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124035075):
No, definitely not. Thanks for noticing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 22 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124035078):
We should have some noticing tool for that :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 22 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124035133):
Looks like you do :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 22 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124035943):
@**Mario Carneiro** fixed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 22 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124039009):
`mathlib` should now be fixed, although I built against sebastian's commit which won't appear until tomorrow's nightly build


{% endraw %}
