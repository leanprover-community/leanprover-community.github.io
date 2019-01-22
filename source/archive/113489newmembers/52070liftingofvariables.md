---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/52070liftingofvariables.html
---

## [new members](index.html)
### [%% lifting of variables](52070liftingofvariables.html)

#### [Ken Roe (Jul 22 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%25%25%20lifting%20of%20variables/near/130095457):
I've discovered that %% automatically lifts bound variables as shown in the following example:

```lean
meta def test_dummy : tactic unit :=
do {
     test ← some ``((λ (v:ℕ),v=%%(@var tt 1)) 3),
     trace test.to_raw_fmt,
     admit
   }

theorem dummy : 3=4 :=
begin
    test_dummy
end
```

The trace generates the following output:
```lean
(app (lam v default [macro annotation (const nat [])] (app (app [macro annotation (const eq [])] (var 0)) [macro annotation (var 2)])) [macro prenum])
```

Notice that the @var tt 1 in the "trace" has become (var 2).  Is there a way to prevent this lifting of variables?

#### [Simon Hudon (Jul 22 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%25%25%20lifting%20of%20variables/near/130101029):
I recommend you not to use `var` directly because much of the Lean API assumes that your expressions are closed (not `var` without their binders). What you can do is:

```lean
do my_var <- mk_local_def `my_var `(nat),
   e <- to_expr ``((λ (v:ℕ),v=%%my_var) 3),
   return $ lambdas [my_var] e
```

It also works with Pi-binders:

```lean
   -- ...
   return $ pis [my_var] e
```

