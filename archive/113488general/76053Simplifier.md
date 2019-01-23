---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/76053Simplifier.html
---

## Stream: [general](index.html)
### Topic: [Simplifier](76053Simplifier.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Oct 23 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136326024):
I'm realizing I don't understand how the simplifier works. I have a complicated goal involving product spaces, and in the middle of this goal there is the expression `(f, x).fst`. When I apply `simp` to my goal, it does not reduce to `f`. To help simp, I wrote down an auxiliary statement exactly with the good types and elements `f` and `x`, but still it does not help `simp`. Even when I turn on `set_option pp.all true` I can't see what is wrong.
My helper lemma is `should_help : (prod.mk f x).fst = f`. Fully expanded, it reads
```lean
should_help :
  @eq.{(max u v)+1} (@bounded_continuous_function.{u v} α β _inst_1 _inst_2)
    (@prod.fst.{(max u v) u} (@bounded_continuous_function.{u v} α β _inst_1 _inst_2) α
       (@prod.mk.{(max u v) u} (@bounded_continuous_function.{u v} α β _inst_1 _inst_2) α f x))
    f
```
And in my goal I have the lines
```lean
(@prod.fst.{(max u v) u} (@bounded_continuous_function.{u v} α β _inst_1 _inst_2) α
                         (@prod.mk.{(max u v) u} (@bounded_continuous_function.{u v} α β _inst_1 _inst_2) α f x))
```
Can someone explain why `simp [should_help]` does not reduce this term to `f`? (I can certainly work it around, but still I would be very happy to understand what is going on here...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Oct 23 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136326122):
Does `dsimp` work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Oct 23 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136326263):
Yes it does.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Oct 23 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136326513):
Then welcome to dependent type theory!  Basically `simp` can only rewrite at non-dependent arguments.  The automatically generated congruence lemmas only have hypotheses for the non-dependent arguments.  We could also rewrite at dependent arguments, but then you'd get casts all over the place.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Oct 23 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136326860):
OK. Not sure I really understand: is the problem the fact that my type is `@bounded_continuous_function.{u v} α β _inst_1 _inst_2`, so depending on other types and instances? In any case, thanks a lot, I will add `dsimp` to my toolbox and try to apply it when `simp` does not work, even if I don't know why. (And this is a perfectly well-defined and efficient algorithm!)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Oct 23 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136327235):
No, I think the problem is that `prod.fst ...` *occurs* as a subterm of some dependent argument, and hence simp cannot reach it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 23 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136351767):
Consider the following example: suppose `h` has type `is_prime (1+n)` and somewhere in the goal I have `⟨1+n, h⟩` as a subterm. Suppose I want to rewrite `1+n` to `n+1` using (using `rw [add.comm 1 n]` or `simp`) then I get the subterm `⟨1+n, h⟩`, but this is not type correct: `h` has type `is_prime (1+n)`, not type `is_prime (n+1)`. Therefore, `rw` and `simp` will fail if you do this.

Now we modify the example, and `h` has type `is_prime (1+4)`. `1+4` and `5` are definitionally equal, which implies that `h` *also* has type `is_prime 5`. Therefore, if your goal contains `⟨2+3, h⟩` you are allowed to rewrite this to `⟨5, h⟩`. However, `simp` and `rw` will not do this for you, but `dsimp` (which only rewrites with definitional equalities) happily will.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136352123):
simp should handle this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136353224):
simp will produce a term like `⟨1+n, cast (add_comm 1 n) h⟩`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 23 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136356668):
Oh yeah, my example is wrong, `simp` does handly my case correctly.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 23 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136356985):
but only because `is_prime` is a proposition. If you replace `is_prime` by `vector bool` or anything else living in `Type*`, then what I described is correct.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 23 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136357623):
Actually it will work as long as the second argument is a subsingleton. This is because this cast thing is being inserted by the congr lemma, that automatically discharges subsingleton arguments (even if they are in Type)

