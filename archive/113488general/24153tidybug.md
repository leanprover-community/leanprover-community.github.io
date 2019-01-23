---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24153tidybug.html
---

## Stream: [general](index.html)
### Topic: [tidy bug](24153tidybug.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060203):
Can someone try
```lean
import tactic.tidy

example (X Y : Type) (f : X → Y) (h : ∀ y : Y, ∃ x : X, f(x) = y) : 
  (∃ g : Y → X, f ∘ g = id) :=
begin
  cases classical.axiom_of_choice h with g H,
  tidy,
 end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060275):
Here it says `no goals` after `tidy` but red-squiggle `example` with ``type mismatch at application  g a term  a has type  Y_1 but is expected to have type   Y types contain aliased name(s): Y remark: the tactic `dedup` can be used to rename aliases``

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 02 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060435):
```quote
Here it says `no goals` after `tidy` but red-squiggle `example` with ``type mismatch at application  g a term  a has type  Y_1 but is expected to have type   Y types contain aliased name(s): Y remark: the tactic `dedup` can be used to rename aliases``
```
I get the same.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060519):
Let's wait for @**Scott Morrison|110087** to wake up, or finish lunch, or whatever it's time to do in Australia

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 02 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060631):
Here's the trace:
```lean
/- `tidy` says -/ 
dsimp at *, 
fsplit, 
work_on_goal 0 { intros a }, 
work_on_goal 1 { ext1, dsimp at *, solve_by_elim }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060646):
I'm working on that demo file we discussed earlier, trying to see what general purpose automation can do what. The problem with magic is it's somewhat unpredictable. It seems `finish` is pretty powerful in those example, but I'd like to understand when `tidy` or `tauto` actually also work (or even work better)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060745):
Good idea Bryan!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 02 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060767):
Not sure if I misunderstand the meaning of the trace, but throwing it in as a proof fails at the first `dsimp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060783):
It's very strange to follow, it seems hopeless and then `solve_by_elim` pretends to get rid of all meta-vars and do the job

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060810):
here I get exactly the same result as with tidy itself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060834):
google says Scott may be sleeping

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 02 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060897):
I see this:
```lean
import tactic.tidy
example (X Y : Type) (f : X → Y) (h : ∀ y : Y, ∃ x : X, f(x) = y) :
  (∃ g : Y → X, f ∘ g = id) :=
begin
dsimp at *,  -- squiggly line under dsimp
/- Tactic State
X Y : Type,
f : X → Y,
h : ∀ (y : Y), ∃ (x : X), f x = y
⊢ ∃ (g : Y → X), f ∘ g = id
scratch.lean:14:0: error
dsimplify tactic failed to simplify
state:
⊢ ∀ (X Y : Type) (f : X → Y), (∀ (y : Y), ∃ (x : X), f x = y) → (∃ (g : Y → X), f ∘ g = id) -/
fsplit,
work_on_goal 0 { intros a },
work_on_goal 1 { ext1, dsimp at *, solve_by_elim }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060910):
you erased too much

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060915):
the choice idea is required

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 02 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135060932):
Oops!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 02 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135061725):
Yes, now I see the same.  

Nothing seems strange with the intermediate tactic states. Is there a way to use the `discharger` option for `solve_by_elim` to make it spit out what it's doing at each stage?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135061835):
How is it possible that none of our general purpose weapon can kill
```lean
example (X Y : Type) (f : X → Y) (g : Y → X) (h : f ∘ g = id ) (y : Y) : f (g y) = y 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 02 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135061909):
I don't use weapons :P
```lean
example (X Y : Type) (f : X → Y) (g : Y → X) (h : f ∘ g = id ) (y : Y) : f (g y) = y := congr_fun h y
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135061953):
Kenny, this is exactly what I did at https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/demo.lean#L60 but I'm trying to rewrite this file using automation, for comparison

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062010):
I guess this is again because tactic writers don't like function equalities, especially with compositions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 02 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062015):
Replacing `solve_by_elim` with `apply_assumption` gives the same strange behavior.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 02 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062022):
Higher order reasoning is hard!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062062):
`finish` and its friends could try to turn each function equality assumption into a forall

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062136):
```lean
example (X Y : Type) (f : X → Y) (g : Y → X) (h : ∀ z, (f ∘ g) z = id z) (y : Y):
  f (g y) = y :=
by finish
```
does work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062179):
Of course rewriting `h` like this is the most un-mathematical thing you could see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 02 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062206):
```quote
`finish` and its friends
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062395):
its friends are `tauto` and `tidy`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 02 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062619):
Could it be that there's something strange happening with `work_on_goal`? The following works:
```lean
import tactic.tidy
example (X Y : Type) (f : X → Y) (h : ∀ y : Y, ∃ x : X, f(x) = y) :
  (∃ g : Y → X, f ∘ g = id) :=
begin
  cases classical.axiom_of_choice h with g H,
  dsimp at *,
  fsplit,
  { exact g },
  { ext1, 
  dsimp at *,
  apply_assumption }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 02 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062701):
Compare this, which gives the same `no goals` + weird error as the initial `tidy` call:
```lean
import tactic.tidy
example (X Y : Type) (f : X → Y) (h : ∀ y : Y, ∃ x : X, f(x) = y) :
  (∃ g : Y → X, f ∘ g = id) :=
begin
  cases classical.axiom_of_choice h with g H,
  dsimp at *,
  fsplit,
  --{ exact g },
  work_on_goal 1 { ext1,
  dsimp at *,
  apply_assumption }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062782):
interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135062942):
Even better:
```clean
 example (X Y : Type) (f : X → Y) (h : ∀ y : Y, ∃ x : X, f(x) = y) :
  (∃ g : Y → X, f ∘ g = id) :=
begin
  cases classical.axiom_of_choice h with g H,
  dsimp at *,
  fsplit,
  { exact g },
  work_on_goal 0 { ext1,
  dsimp at *,
  apply_assumption }
end
```
works!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135063047):
but actually this is getting far away from what tidy suggested

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 02 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135063189):
[Here's](https://github.com/leanprover/mathlib/blob/decb0302869ac70069ba26708367e460695683cb/tactic/chain.lean#L44) `work_on_goal`. If I had to guess, there's something wrong in here, possibly in handling what happens if a goal gets solved.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 02 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135065300):
I think the problem is that when `apply_assumption` kills off a goal, it does not return properly to `work_on_goal`. Then lean thinks it has finished, but in reality there are more goals that `work_on_goal` just temporarily deleted. There are no issues when `exact g` finishes a goal inside `work_on_goal`, so there's something going on with this particular interaction.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 02 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135065407):
`apply_assumption` is [here](https://github.com/leanprover/mathlib/blob/c2df6b1f3f62575649dbe128a2c5fc9e2de26ffb/tactic/basic.lean#L422), but it's too monad-y for me to make sense of at the moment.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 02 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135065867):
What problem are you looking for?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 03 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135066963):
Patrick started this thread with [an example](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/tidy.20bug/near/135060203) where `tidy` leaves the tactic state with `no goals` but there is a strange error.

I'm proposing that the root cause of this is due to `apply_assumption` not returning properly to `work_on_goal`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 03 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135067028):
Thanks for these bug reports. I probably won't have a chance to work on it until the weekend.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 03 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135068289):
```lean
import tactic.interactive

example (X Y : Type) (f : X → Y) (g : Y → X) (h : ∀ z, (f ∘ g) z = id z) (y : Y):
  f (g y) = y := by tauto
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 03 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135068292):
@**Patrick Massot**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20bug/near/135085753):
Thanks Kenny, but this is the version I don't want, because `h` is stated un-mathematically


{% endraw %}
