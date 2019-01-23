---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/44550Projectionaftermkstructure.html
---

## Stream: [general](index.html)
### Topic: [Projection after mk-structure](44550Projectionaftermkstructure.html)

---

#### [Keeley Hoek (Sep 16 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Projection%20after%20mk-structure/near/134060550):
Say I've got a function `mk_struct` which takes some arguments and produces something of type `struct`. The function `mk_struct` needn't be the `struct.mk` constructor---maybe it takes some arguments, proves some stuff about them, and then packages it all up by calling the constructor `struct.mk` (the point is that the arguments of `mk_struct` can be totally different).

#### [Keeley Hoek (Sep 16 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Projection%20after%20mk-structure/near/134060552):
Now say `struct` has a projection `struct.foo`. There is a single unambiguous way to construct a function `mk_struct.foo`, which forgets all of the components of whatever `mk_struct` outputs except for `foo`. I'd like to programmatically obtain the *type* of this function `mk_struct.foo`.

Actually, I've essentially done this, but it was incredibly stupid: I directly built everything over `expr.xxx`'s and manually wrote code to unify the arguments of the projection and the output-type of `mk_struct`, and in the end it wasn't robust enough to deal with universe parameters.

#### [Keeley Hoek (Sep 16 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Projection%20after%20mk-structure/near/134060594):
But I'm sure this was all crazy---I'm sure I can exploit lean's facilities (at the very least `unify`) to do the resolution which I need. Perhaps I'm looking for a suped-up `tactic.mk_app` that can unroll the quantifiers from the argument I want to apply? What's the canonical way to go about `expr` fiddling like this?

#### [Mario Carneiro (Sep 16 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Projection%20after%20mk-structure/near/134066795):
I'm confused why this is different from `struct.foo ∘ mk_struct`. Can't you just figure out the type of this?

#### [Keeley Hoek (Sep 17 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Projection%20after%20mk-structure/near/134079723):
@**Mario Carneiro**  Thanks for taking a look. Here's a concrete example:
````
structure struct (n : ℤ) :=
(foo : ℕ)

def mk_struct (m : ℕ) : struct m := ⟨m, 2 * m⟩

#check struct.foo ∘ mk_struct
#check λ m, (mk_struct m).foo
````
The second-to-bottom line fails to typecheck, since `mk_struct` takes a (possibly a few) potentially random arguments. I'd really like to be able to compose to essentially do what the last line does, without having to know the arguments of `mk_struct` in advance.

#### [Mario Carneiro (Sep 17 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Projection%20after%20mk-structure/near/134080030):
do you know the arguments of `struct.foo`?

#### [Mario Carneiro (Sep 17 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Projection%20after%20mk-structure/near/134080101):
this function in `tactic/alias.lean` seems similar:
```
meta def mk_iff_mp_app (iffmp : name) : expr → (nat → expr) → tactic expr
| (expr.pi n bi e t) f := expr.lam n bi e <$> mk_iff_mp_app t (λ n, f (n+1) (expr.var n))
| `(%%a ↔ %%b) f := pure $ @expr.const tt iffmp [] a b (f 0)
| _ f := fail "Target theorem must have the form `Π x y z, a ↔ b`"
```
it constructs the term `\lam x y z, iff.mp (f x y z)`

