---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04369unfoldrefusestounfold.html
---

## Stream: [general](index.html)
### Topic: [`unfold` refuses to unfold](04369unfoldrefusestounfold.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Arseniy Alekseyev (May 12 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471033):
Here `t2_to_t1` is fully applied to a constructor, but lean still refuses to unfold/reduce. How so?

```lean
inductive t1
| c1 : t1

inductive t2
| c2 : t2

@[simp] def t2_to_t1 : t2 → t1
| t2.c2 := t1.c1

theorem hmm : ∀ (x : t2), (t1.rec 5 (t2_to_t1 x) : ℕ) = 5 := begin
    intro x,
    induction x,
    unfold t2_to_t1,
    -- simplify tactic failed to simplify
    --state:
    -- ⊢ t1.rec 5 (t2_to_t1 t2.c2) = 5
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471093):
`rw` works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (May 12 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471136):
`dunfold` too, probably?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471137):
and `dsimp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Arseniy Alekseyev (May 12 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471138):
yep, they all work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471145):
The problem is that it is a dependent function, so non-definitional rewrites don't necessarily work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Arseniy Alekseyev (May 12 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471188):
you mean t1.rec is dependent so those tactics don't even try to rewrite it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Arseniy Alekseyev (May 12 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471189):
rewrite its argument*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471191):
it will only rewrite in certain locations, depending on the generated congr lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Arseniy Alekseyev (May 12 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471197):
interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Arseniy Alekseyev (May 12 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471237):
thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471242):
```
open tactic
run_cmd do
  c ← mk_const `t1.rec >>= mk_congr_lemma,
  trace c.type

-- ∀ {C : t1 → Sort ?} (e_1 e_1_1 : C t1.c1), e_1 = e_1_1 →
--   ∀ (n : t1), t1.rec e_1 n = t1.rec e_1_1 n
``

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471249):
as you can see from the type, it only rewrites the first argument, the `n` is fixed on both sides

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471294):
here's what you would get with a less dependent function:
```
run_cmd do
  c ← mk_const `has_add.add >>= mk_congr_lemma,
  trace c.type
-- ∀ {α : Type ?} [c : has_add α] (a a_1 : α), a = a_1 →
--   ∀ (a_2 a_3 : α), a_2 = a_3 → a + a_2 = a_1 + a_3
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Arseniy Alekseyev (May 12 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471295):
is it based purely on the type of the function?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471306):
There is a general procedure for generating "congruence" theorems such as these. The only input is the type of the function, and as you can see it doesn't really try to rewrite in dependent argument positions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Arseniy Alekseyev (May 12 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471349):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Arseniy Alekseyev (May 12 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471353):
because it doesn't even work in general for higher-than-Prop sorts, is that right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471360):
The cool part is that it will automatically use known `subsingleton` arguments to change values without any equality hypothesis. In particular, that means that proof arguments can be freely rewritten

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471400):
even if they are dependent on some earlier argument

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471401):
This is where the `simp` approach to rewriting wins over `rw`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Arseniy Alekseyev (May 12 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471463):
I didn't get that (I don't know where `subsingleton` instances would come from).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471464):
```
example (f : ∀ n : ℕ, n > 0 → ℕ) (x : ℕ) (x0 : 0 + x > 0) : f (0 + x) x0 = 1 :=
by simp; admit

example (f : ∀ n : ℕ, n > 0 → ℕ) (x : ℕ) (x0 : 0 + x > 0) : f (0 + x) x0 = 1 :=
by rw zero_add; admit --error: motive is not type correct
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471505):
after the `simp`, the goal looks like `f x _ = 1` where `_` is some proof depending on the equality that was used to rewrite

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471513):
whereas `rw` attempts to rewrite to `f x x0` and then gives up when it finds out this is not type correct

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471517):
`subsingleton` is a typeclass, it is inferred by typeclass inference

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471567):
For example, `decidable p` is a subsingleton, because any two instances of `decidable p` must either both be `of_true` or both `of_false`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Arseniy Alekseyev (May 12 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471569):
oh, "proof arguments" as in arguments that are themselves proofs rather than arguments of proofs. I guess all `Prop`s are subsingletons then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471574):
All elements of Prop are subsingletons

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471575):
if `p : Prop` and `h1 h2 : p` then `h1 = h2`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471616):
that equality is definitional, but `simp` will use it even if it is not definitional like in the `decidable p` example

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Arseniy Alekseyev (May 12 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471621):
right, cool

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Arseniy Alekseyev (May 12 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471626):
what's "sub" about this notion of singleton?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471627):
`empty` is a subsingleton too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471628):
`subsingleton A` is defined to mean that if `a b : A` then `a = b`; classically that means `A` is a singleton or empty

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Arseniy Alekseyev (May 12 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471629):
ah, of course!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471673):
"singleton" is usually stated as `\ex a, \all b, a = b`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Arseniy Alekseyev (May 12 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471774):
subsingleton is what they call proposition in hott land, isn't it? Interestingly, it's one truncation hierarchy level *higher* than singleton there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471835):
Yes, if you are familiar with HoTT terminology then "singleton" is "contractible" is -2 truncated, and "subsingleton" is "proposition" is -1 truncated. "set" or 0 truncated is true of all types in lean, because equality is a proposition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471879):
I also find it a bit funny that -2 truncated types have elements while -1 truncated types may not, but the ordering there makes sense: every -2 truncated type is -1 truncated but not the other way around.

