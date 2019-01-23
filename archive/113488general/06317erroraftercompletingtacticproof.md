---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/06317erroraftercompletingtacticproof.html
---

## Stream: [general](index.html)
### Topic: [error after completing tactic proof](06317erroraftercompletingtacticproof.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 17 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%20after%20completing%20tactic%20proof/near/147866833):
```lean
type mismatch at application
  F.map (i ≫ functor.preimage f j) s
term
  s
has type
  ((functor.id (presheaf X)).obj F_1).obj U₁_1
but is expected to have type
  F.obj U₁
types contain aliased name(s): U₁ F
remark: the tactic `dedup` can be used to rename aliases
```
I have tried inserting `dedup` in several places, but it doesn't help. My `s` remains to have type `((functor.id (presheaf X)).obj F).obj U₁` in the goal window, which is defeq to `F.obj U₁`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 17 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%20after%20completing%20tactic%20proof/near/147867786):
Oh, I've had this one before. The error message is completely misleading...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 17 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%20after%20completing%20tactic%20proof/near/147867790):
Check that you haven't somehow used `_root_.functor` somewhere that should have been `category_theory.functor`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 17 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%20after%20completing%20tactic%20proof/near/147867793):
I don't remember if that was it or not.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 17 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%20after%20completing%20tactic%20proof/near/147868427):
Hmm, that sounds like a very crazy error. I'll see if I can find it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 17 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%20after%20completing%20tactic%20proof/near/147868475):
Do you spot anything suspicious in
```lean
def counit.is_iso [fully_faithful f] : is_iso (counit f) :=
{ inv :=
  { app := λ (F : _ ⥤ _),
    { app := λ U s,
      { app := λ V i, (F.map $ f.preimage i : F.obj U → F.obj V) s,
        naturality' := λ V₁ V₂ i,
        begin
          ext j,
          have := (congr $ F.map_comp (f.preimage j) i) (rfl : s = _),
          dsimp at *,
          erw ← this,
          congr,
          apply f.injectivity,
          erw f.map_comp,
          tidy {trace_result := tt},
        end },
      naturality' := λ U₁ U₂ i,
      begin
        ext s V j,
        have := (congr $ F.map_comp i (f.preimage j)) (rfl : _ = _),
        dsimp at *,
        erw ← this,
        congr,
        apply f.injectivity,
        erw f.map_comp,
        tidy {trace_result := tt},
      end },
    naturality' := λ F G α,
    begin
      ext U s V j,
      have := (congr $ α.naturality (f.op.preimage j)) rfl,
      tidy {trace_result := tt},
    end } }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 17 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%20after%20completing%20tactic%20proof/near/147872942):
@**Scott Morrison|110087** In my case it was talking about `f.preimage` while that should have been `f.op.preimage`.
I think we should have stronger barriers between categories and their opposites. Because now stuff is silently identified, and then all of a sudden it bites you 20 lines later.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 17 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%20after%20completing%20tactic%20proof/near/147873601):
Hmm, no, that wasn't the issue... it reappeared...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 17 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%20after%20completing%20tactic%20proof/near/147873776):
I pushed an update to the `sheaf` branch. The trouble is with this def: https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheaf.lean#L241
If any of the experts would want to take a look, I would be very grateful.


{% endraw %}
