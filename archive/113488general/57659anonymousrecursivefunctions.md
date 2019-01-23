---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57659anonymousrecursivefunctions.html
---

## Stream: [general](index.html)
### Topic: [anonymous recursive functions](57659anonymousrecursivefunctions.html)

---


{% raw %}
#### [ Andrew Ashworth (Jun 17 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/anonymous%20recursive%20functions/near/128191984):
is it possible to define an anonymous recursive function? so for I've been making auxiliary defs as needed, but I'm copying a development from coq that uses them a lot

#### [ Andrew Ashworth (Jun 17 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/anonymous%20recursive%20functions/near/128192028):
something like this from CPDT
```coq
Definition check_even : forall n : nat, [isEven n].
  Hint Constructors isEven.

  refine (fix F (n : nat) : [isEven n] :=
    match n with
      | 0 => Yes
      | 1 => No
      | S (S n') => Reduce (F n')
    end); auto.
Defined.
```

#### [ Mario Carneiro (Jun 17 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/anonymous%20recursive%20functions/near/128193830):
Unfortunately no, at least not in term mode. As a workaround you can use `induction`,  but the only way to get the full power of the equation compiler is to have an auxiliary def, and this is what I usually do.

#### [ Simon Hudon (Jun 17 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/anonymous%20recursive%20functions/near/128204616):
You could write 

```lean
nat.rec Yes (λ f n, match n with 
                    | 0 := No
                    | (succ n') := Reduce (f n')
                   end )
```

#### [ Mario Carneiro (Jun 17 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/anonymous%20recursive%20functions/near/128211341):
There is also a somewhat hackish way. Did you ever wonder about those `_match` and `_let_match` variables in the context sometimes? Those are the same mechanism used to support recursive definitions using the equation compiler, and if you refer to them it will get compiled to a recursive function just like a recursive def. For example:
```
def fib (n : ℕ) : ℕ :=
match n with
| 0 := 0
| 1 := 1
| n+2 := by rename _match fib; exact fib n + fib (n+1)
end
```
This doesn't work in term mode though:
```
def fib (n : ℕ) : ℕ :=
match n with
| 0 := 0
| 1 := 1
| n+2 := _match n + _match (n+1)
end
```
fails unless you insert `by exact` on the last line.

#### [ Mario Carneiro (Jun 17 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/anonymous%20recursive%20functions/near/128211656):
I guess the main reason this isn't already supported officially is because there is no obvious place in match notation to put the name of the defined function

#### [ Mario Carneiro (Jun 17 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/anonymous%20recursive%20functions/near/128211859):
Examples of the other two match types:
```
inductive tree : Type
| mk : ∀ n, (fin n → tree) → tree

def path : tree → Type :=
λ ⟨n, t⟩, by exact Σ n, _fun_match (t n)

def path' (T : tree) : Type :=
let ⟨n, t⟩ := T in
by exact Σ n, _let_match (t n)
```

#### [ Simon Hudon (Jun 17 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/anonymous%20recursive%20functions/near/128211909):
Cool hack :grin:


{% endraw %}
