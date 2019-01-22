---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/43922congrargandsuperficiallydependentfunctions.html
---

## [general](index.html)
### [congr_arg and superficially dependent functions](43922congrargandsuperficiallydependentfunctions.html)

#### [Scott Morrison (Aug 02 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr_arg%20and%20superficially%20dependent%20functions/near/130781762):
I'm having trouble constructing `congr_arg` expressions, where the function superficially looks like a dependent function, but after some definitionally unfolding you can see that it isn't really.

#### [Scott Morrison (Aug 02 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr_arg%20and%20superficially%20dependent%20functions/near/130781777):
I've worked out how to get around this in interactive mode, but I can't do it with `expr`s.

#### [Scott Morrison (Aug 02 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr_arg%20and%20superficially%20dependent%20functions/near/130781780):
Here's my work so far.

#### [Scott Morrison (Aug 02 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr_arg%20and%20superficially%20dependent%20functions/near/130781824):
````
def F : Π n : ℕ, Type := λ n, ℕ 
def G : Π n : ℕ, F n := λ n, begin dunfold F, exact 0 end

lemma test (m n : ℕ) (w : m = n) : G n == G m :=
begin
  -- This doesn't work, because `G` looks like a dependent function
  success_if_fail { 
    have h := congr_arg G w
  },
  -- In fact it isn't really, and we can discover this with `dsimp`.
  let g := G,
  dsimp [F] at g,
  -- Now we can use congr_arg.
  let h := congr_arg g w,
  dsimp [g] at h,
  rw h,
end

-- Now I want to do this via `expr` munging:

open tactic

meta def mk_congr_arg_using_dsimp (G W : expr) (F : name) : tactic expr := 
-- I have no idea how to achieve this: this doesn't work, but is my best guess.
do
  s ← simp_lemmas.mk_default,
  t ← infer_type G,
  t' ← s.dsimplify [F] t {fail_if_unchanged := ff},
  trace t',
  to_expr ```(congr_arg (%%G : %%t') %%W)

lemma test2 (m n : ℕ) (w : m = n) : G n == G m :=
begin
  let h := by tactic.get_local `w >>= λ W, mk_congr_arg_using_dsimp `(G) W `F,
  rw h,
end
````

#### [Scott Morrison (Aug 02 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr_arg%20and%20superficially%20dependent%20functions/near/130781907):
If anyone could replace the definition of `mk_congr_arg_using_dsimp` so that `test2` works, that would be amazing. :-)

#### [Minchao Wu (Aug 03 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr_arg%20and%20superficially%20dependent%20functions/near/130826815):
A quick solution:
```
meta def mk_congr_arg_using_dsimp (G W : expr) (F : name) : tactic unit :=
do 
  eg ← to_expr ```(λ n:nat, id 0),
  t ← infer_type G,
  s ← simp_lemmas.mk_default,
  t' ← s.dsimplify [F] t {fail_if_unchanged := ff},
  definev `g t' eg,
  eg ← get_local `g,
  eeq ← to_expr ```(%%G = %%eg),
  assert `h eeq,
  try reflexivity

lemma test2 (m n : ℕ) (w : m = n) : G n == G m :=
begin
  tactic.get_local `w >>= λ W, mk_congr_arg_using_dsimp `(G) W `F,
  rw h
end

```

#### [Minchao Wu (Aug 03 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr_arg%20and%20superficially%20dependent%20functions/near/130827714):
The attempt is to force lean to be aware that the two types of G collapse, however `(%%G : %%t')` doesn't do the trick. This introduces an additional local hypothesis which has the non-dependent type and proves that it is just `G`.

#### [Scott Morrison (Aug 03 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr_arg%20and%20superficially%20dependent%20functions/near/130827909):
Thanks @**Minchao Wu**. In the meantime I'd come up with my own solution:
````
-- Sometimes `mk_congr_arg` fails, when the function is 'superficially dependent'.
-- This hack first dsimplifies the function before building the `congr_arg` expression.
-- Unfortunately it creates a dummy hypothesis that I can't work out how to avoid or dispose of cleanly.
meta def mk_congr_arg_using_dsimp (G W : expr) (u : list name) : tactic expr := 
do
  s ← simp_lemmas.mk_default,
  t ← infer_type G,
  t' ← s.dsimplify u t {fail_if_unchanged := ff},
  tactic.definev `_mk_congr_arg_aux t' G,
  to_expr ```(congr_arg _mk_congr_arg_aux %%W)
````
which is fairly similar!

#### [Scott Morrison (Aug 03 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr_arg%20and%20superficially%20dependent%20functions/near/130827938):
The next question is how to achieve this without making the local hypothesis, so this tactic doesn't pollute the current goal.

#### [Minchao Wu (Aug 03 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr_arg%20and%20superficially%20dependent%20functions/near/130828082):
Yeah I'm also wondering if there is a neater solution :)

