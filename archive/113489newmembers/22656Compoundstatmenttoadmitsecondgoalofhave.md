---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/22656Compoundstatmenttoadmitsecondgoalofhave.html
---

## Stream: [new members](index.html)
### Topic: [Compound statment to admit second goal of have](22656Compoundstatmenttoadmitsecondgoalofhave.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Jul 21 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130061451):
I tried the following to do a "have" and admit the second goal.  What is the correct syntax:

```lean
theorem dummy (n :ℕ) : n = 3 :=
begin
    have h:n=1+2;(skip|admit)
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130061504):
```lean

theorem dummy (n :ℕ) : n = 3 :=
begin
    have h:n=1+2,
    { -- here we only see the first goal
       sorry 
    },
    { -- here we only see the second goal
      sorry
    }
end
```

Is that what you mean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Jul 21 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130061512):
thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130061557):
No problem. Note that the `have h: ...` turns one goal `G` into two goals -- first the proof of `h`, and second the proof of `G` assuming `h` (in addition to anything else which we were assuming when we wrote the `have`).

If you would rather have the goals the other way around, you can use `suffices` :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Jul 21 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130061635):
Actually, I tried the following:

```lean
theorem dummy (n :ℕ) : n = 3 :=
begin
    have h:n=1+2,{ skip },{ admit },
end
```

I would like to end up in a state where only the first goal is open and the second goal is solved.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130061700):
Since `n = 3` and `n = 1 + 2` are definitionally the same goal, you can use `change`:
```
theorem dummy (n :ℕ) : n = 3 :=
begin
    change n = 1 + 2,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130061786):
If the transformation from one goal to the other is not definitional but easy, you can use `suffices`:
```
theorem dummy (n :ℕ) : n = 3 :=
begin
    suffices h : n = 1 + 2, {exact h},
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130061999):
Here are some more tips. If you have two goals, you can use `tactic.swap` to switch them. If you have more than one goal and you want to work on one of them, you can write `show <statement of goal>` and it will switch this goal to the top. One of my students was even telling me about some sort of `rotate` tactic but I've never used it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130062011):
the mathlib `swap` tactic takes an optional argument; `swap n` moves the nth goal to the top

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Jul 21 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130062367):
Igt appears "have h:a, swap, admit" does what I want.  Now, I want to figure out something more complex:

```lean
open tactic
open monad
open expr
open smt_tactic

def andFuns (a : ℕ → Prop) (b : ℕ → Prop) : ℕ → Prop :=
    (λ q, (a q) ∧ (b q)).

def existsFuns {t : Type} (a : t → ℕ → Prop) : ℕ → Prop :=
    (λ n, (∃ (e:t), a e n).

def test := (λ x, x > 3)
def test2 := (λ x, x < 8)

theorem test1 (v: ℕ) : (λ (e:ℕ), (andFuns test test2) (v+1)) v :=
begin

    have h: (andFuns (λ (e:ℕ), test e) (λ (e:ℕ), test2 e)) v,
    swap,admit,
end
```
In the above theorem, I would like to create a tactic that automates the conversion of "(λ (e:ℕ), (andFuns test test2) (v+1)) v" to "h(andFuns (λ (e:ℕ), test e) (λ (e:ℕ), test2 e)) v". 

I have created the following meta tactic which has many syntax errors.  How do I correct the errors:

```lean
meta def divide_lambda : name → binder_info → expr → expr → expr → expr → expr
| n b e1 ``(andFuns %%l %%r) v y :=
      (app (app `(andFuns) (divide_lambda n b e1 l v y))
                           (divide_lambda n b e1 r v y))
| n b e1 x y v := (app (lam n b e1 (app x y)) v).

meta def transform_lambda_app : expr → option expr
| (app (lam n b e1 (app x y)) val) := some (divide_lambda n b eq x y val)
| _ := none.

meta def split_lambda : tactic unit :=
do { t ← target,
     nt ← transform_lambda_app t,
     (have h:nt;swap;admit) }.
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130062736):
I'm confused - `(λ (e:ℕ), (andFuns test test2) (v+1)) v` and `h(andFuns (λ (e:ℕ), test e) (λ (e:ℕ), test2 e)) v` are not the same

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130062747):
are the `v` supposed to be de bruijn variables?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Jul 21 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130062892):
I didn't state the theorem quite right:

```lean
theorem test1 (v: ℕ) : (λ (e:ℕ), (andFuns test test2) (e+1)) v :=
begin

    have h: (andFuns (λ (e:ℕ), test (e+1)) (λ (v:ℕ), test2 (e+1))) v,
    swap,admit,
end
```

Hopefully this make more sense.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130063016):
You should be able to use `change` instead of `swap, admit` if you got it right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130063050):
```
theorem test1 (v: ℕ) : (λ (e:ℕ), (andFuns test test2) (e+1)) v :=
begin
    change (andFuns (λ (e:ℕ), test (e+1)) (λ (e:ℕ), test2 (e+1))) v,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130063159):
Here is fixing the syntax errors, although it doesn't work yet:
```
meta def divide_lambda : name → binder_info → expr → expr → expr → expr → expr
| n b e1 `(andFuns %%l %%r) v y :=
      (app (app `(andFuns) (divide_lambda n b e1 l v y))
                           (divide_lambda n b e1 r v y))
| n b e1 x y v := (app (lam n b e1 (app x y)) v).

meta def transform_lambda_app : expr → option expr
| (app (lam n b e1 (app x y)) val) := some (divide_lambda n b e1 x y val)
| _ := none.

meta def split_lambda : tactic unit :=
do { t ← target,
     nt ← transform_lambda_app t,
     change nt }

theorem test1 (v: ℕ) : (λ (e:ℕ), (andFuns test test2) (e+1)) v :=
begin
  split_lambda,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Jul 21 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130063222):
It looks like change works.  The theorem looks like this now:

```lean
theorem test1 (v: ℕ) : (λ (e:ℕ), (andFuns test test2) (e+1)) v :=
begin

    change (andFuns (λ (e:ℕ), test (e+1)) (λ (e:ℕ), test2 (e+1))) v,
end
```

Now the challenge is to get the tactic working that generates the expression.  The tactic code now looks like this:

```lean
meta def divide_lambda : name → binder_info → expr → expr → expr → expr → expr
| n b e1 ``(andFuns %%l %%r) v y :=
      (app (app `(andFuns) (divide_lambda n b e1 l v y))
                           (divide_lambda n b e1 r v y))
| n b e1 x y v := (app (lam n b e1 (app x y)) v).

meta def transform_lambda_app : expr → option expr
| (app (lam n b e1 (app x y)) val) := some (divide_lambda n b eq x y val)
| _ := none.

meta def split_lambda : tactic unit :=
do { t ← target,
     nt ← transform_lambda_app t,
     (change nt) }.
```

I'm getting the error "invalid pattern, must be an application, constant, variable, type ascription, aliasing pattern or inaccessible term" in divide_lambda on the pattern "n b e1 ``(andFuns %%l %%r) v y".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130063291):
use single backtick on line 2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130063366):
For me the tactic fails in `transform_lambda_app` because right after the `begin` the goal says `⊢ andFuns test test2 (v + 1)` so there is no lambda in sight

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130063382):
I wasn't aware of this - it looks like lean is really eager to unfold raw lambda-app beta reductions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130063528):
I'm not exactly sure what your goal is; perhaps this is a suitable compromise:
```
theorem test1 (v: ℕ) : id (λ (e:ℕ), (andFuns test test2) (e+1)) v :=
begin
  -- split_lambda,
  change id (andFuns (λ (e:ℕ), test (e+1)) (λ (e:ℕ), test2 (e+1))) v,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130063733):
This works, with the `id` to protect the lambda at the start:
```
meta def divide_lambda : name → binder_info → expr → expr → expr → expr
| n b e1 `(andFuns %%l %%r) y :=
      (app (app `(andFuns) (divide_lambda n b e1 l y))
                           (divide_lambda n b e1 r y))
| n b e1 x y := (lam n b e1 (app x y))

meta def transform_lambda_app : expr → option expr
| (app (lam n b e1 (app x y)) val) := some (app (divide_lambda n b e1 x y) val)
| (app `(id %%(lam n b e1 (app x y))) val) := some (app (divide_lambda n b e1 x y) val)
| _ := none

meta def split_lambda : tactic unit :=
do { t ← target,
    trace t.to_raw_fmt,
     nt ← transform_lambda_app t,
     change nt }

theorem test1 (v: ℕ) : id (λ (e:ℕ), (andFuns test test2) (e+1)) v :=
begin
  split_lambda,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Jul 21 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130066480):
Thanks--Now for the next trick, I would like to extend split_lambda to be able to propagate an expression into a closure.  Note that now, the tactic may need to rename variables,

```lean
def existsFuns {t : Type} (a : t → ℕ → Prop) : ℕ → Prop :=
    (λ n, (∃ (e:t), a e n)).

theorem capture (v: ℕ) (q : ℕ) : id (λ (e:ℕ), (andFuns (existsFuns (λ (x y : ℕ), x = y)) test) (e+q)) v :=
begin
    change
        andFuns (existsFuns (λ (x e : ℕ), (λ y, x=y) (e+q)))
                (λ (e:ℕ), test (e + q)) v,
end
```

Notice how the (e+q) is propagated inside a closure involving "x".  The variable may in some cases need to be renamed.   Is there a way to get a fresh variable name and to rename the variables when reconstructing lambda expressions?
end

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130067152):
You don't have to worry about variable capture for the most part. Lean uses unique names in all lambdas, so it shouldn't be a problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130067208):
The tactics `mk_fresh_name` and `get_unused_name` can be used to generate unique and human-readable names respectively

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Jul 21 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130069632):
OK--I've updated my tactic.  It looks like this now:

```lean
meta def divide_lambda : name → binder_info → expr → expr → expr → expr
| n b e1 `(andFuns %%l %%r) y :=
      (app (app `(andFuns) (divide_lambda n b e1 l y))
                           (divide_lambda n b e1 r y))
| n b e1 `(existsFuns (λ (v:ℕ), %%ll)) y :=
      (app `(existsFuns (λ (v:ℕ), %%(divide_lambda n b e1 ll y))))
| n b e1 x y := (lam n b e1 (app x y))

meta def transform_lambda_app : expr → option expr
| (app (lam n b e1 (app x y)) val) := some (app (divide_lambda n b e1 x y) val)
| (app `(id %%(lam n b e1 (app x y))) val) := some (app (divide_lambda n b e1 x y) val)
| _ := none

meta def split_lambda : tactic unit :=
do { t ← target,
     trace t.to_raw_fmt,
     nt ← transform_lambda_app t,
     trace nt.to_raw_fmt,
     change nt }
```

I' trying to use it in this theorem:

```lean
theorem capture (v: ℕ) (q : ℕ) : id (λ (e:ℕ), (andFuns (existsFuns (λ x:ℕ, test3 x)) test) (e+q)) v :=
begin
    split_lambda,
    --change
    --    andFuns (existsFuns (λ (y e:ℕ), test3 y (e+q)))
    --            (λ (e:ℕ), test (e + q)) v,
end
```

It seems like no output goal is being generated.  I suspect the tactic is crashing somehow.  Is the pattern matching being done properly in divide_lambda?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130069868):
I get an error `trying to evaluate sorry` in the test theorem, which means that there is a syntax error in the tactic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130069927):
and the error at `divide_lambda` says the `existsFuns` branch has incorrect type `expr -> expr` instead of `expr`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130069932):
because you used `expr.app` applied to only one argument

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Jul 21 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130071032):
OK-- I fixed divide_lambda

```lean
meta def divide_lambda : name → binder_info → expr → expr → expr → expr
| n b e1 `(andFuns %%l %%r) y :=
      (app (app `(andFuns) (divide_lambda n b e1 l y))
                           (divide_lambda n b e1 r y))
| n b e1 `(existsFuns (λ (v:ℕ), %%ll)) y :=
      `(existsFuns (λ (v:ℕ), %%(divide_lambda n b e1 ll y)))
| n b e1 x y := (lam n b e1 (app x y))
```

but I get the error:

```lean
tactic.change failed, given type
  andFuns (existsFuns (λ (v e : ℕ), test3 e (e + q))) (λ (e : ℕ), test (e + q)) v
is not definitionally equal to
  id (λ (e : ℕ), andFuns (existsFuns (λ (x : ℕ), test3 x)) test (e + q)) v
```

It appears the bound variable "x" is being changed to "e".  Why is this happening?  It appears the capture mechanism is not naming variables properly.


{% endraw %}
