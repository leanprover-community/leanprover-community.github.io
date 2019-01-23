---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/65864moreexprmunging.html
---

## Stream: [general](index.html)
### Topic: [more expr munging](65864moreexprmunging.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 09 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133605425):
Say I have an `expr` representing an iterated `pi` type, which is finally an equation, something like `Π (a : ℕ) (b : ℕ), f a b = g (a + b)`. From that, I want to produce `f ?m_1 ?m_2`, where `?m_1` and `?m_2` are newly created metavariables of the appropriate types.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 09 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133605426):
Any suggestions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 09 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133605484):
Are you guaranteed that the left hand side will be literally `<something> a b`, where `a` and `b` are the variables introduced by the Pis in order? Or could it be some arbitrary expression involving `a` and `b`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 09 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133605574):
```lean
meta def get_lhs : expr -> tactic expr 
| (expr.pi n bi d b) := 
do v <- mk_local' n bi d,
      b' <- whnf $ b.instantiate_var v
      get_lhs b'
| `(%%a = %%b) := pure a
| _ := failed
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 09 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133605626):
Yes this strategy is what I was about to suggest. Peel off one outer Pi at a type, leaving a formula with a free variable, and then substitute a fresh metavariable or whatever else you want for that free variable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 09 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133605631):
Actually, we can be more direct:

```lean
meta def get_lhs : expr -> tactic expr
| (expr.pi n bi d b) :=
do v <- mk_meta_var d,
   b' <- whnf $ b.instantiate_var v
   get_lhs b'
| `(%%a = %%b) := pure a
| _ := failed
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 09 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133605633):
(I'm doubly impressed, Simon, that your code often doesn't quite compile: there's a comma missing in that first one. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 09 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133605674):
Where would be the fun if you didn't have to fix my mistakes?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 09 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133605935):
So I'm trying to do something a bit fancier here, and while `get_lhs` work as requested, really I want something more. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 09 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133605958):
I'm listening (sort of)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 09 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606018):
I had written:
```
meta def substitutions' : expr → bool → list expr → 
  tactic (tactic (expr × expr × list expr))
| (expr.pi n bi d b) symm types := 
  do substitutions' b symm (d :: types)          
| `(%%lhs = %%rhs) symm types := 
  do let (lhs, rhs) := if symm then (rhs, lhs) else (lhs, rhs),
     let tac := (do mvars ← types.mmap mk_meta_var,
        let pattern := lhs.instantiate_vars mvars,
        ty ← infer_type pattern,
        return (pattern, ty, mvars)),
     return tac
| _ _ _ := failed
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 09 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606035):
The idea being to return a tactic, which could be invoked multiple times, each time producing the pattern with "fresh" mvars.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 09 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606043):
However it's ... still somewhat mysteriously ... not working in all cases. (Sorry this is far from a MWE.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 09 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606101):
Is this supposed to be more efficient than just invoking something like `get_lhs` repeatedly?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 09 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606180):
Yeah, I guess so.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 09 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606184):
But maybe I am needlessly complicating things. :-(

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 09 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606203):
I think you need to `reverse` `mvars`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 09 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606250):
It's probably about equally or less efficient because the representation of that `tactic` object in the VM is going to be basically the same as or a more complicated structure than the outer Pis of the original type.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 09 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606328):
Hmm. I had tried (on a purely voodoo basis) reversing `mvars`, without apparent success. Let me go away on de-complicate for a bit. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 09 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606329):
Thanks for the help!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 09 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606330):
After squinting at it for a while, I agree with @**Reid Barton**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 09 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606428):
(Or at least, that would be true in the GHC runtime system, which is probably a terrible mental model for the Lean VM but the best one I have available.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 09 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606476):
My reasoning is that, for each bound variable, the expensive thing is `instantiate_var`, the number of which does not decrease in this approach

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 09 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606495):
Right, you only save the decomposition of the Pis.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 09 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606593):
Which is cheap anyways, but to make things worse, you replace it by having to do an equal number of applications-of-variable-functions (the inner `tactic`which you build up).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 09 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606693):
Oh wait, you implemented it in a way so that there is only one closure being built (`tac`), but still each invocation of `tac` has to process the list `types`, which has the same information as the outer Pis of the original expression.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 09 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606774):
and, happily it all seems to work now!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 09 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20expr%20munging/near/133606776):
(or at least the "all" that I hoped to have done tonight!)


{% endraw %}
