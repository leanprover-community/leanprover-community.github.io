---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00230proofwithoutrsimp.html
---

## Stream: [general](index.html)
### Topic: [proof without rsimp](00230proofwithoutrsimp.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 16 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129752082):
Any suggestion on how to prove this? `rsimp` works, but I'm guessing there's a better way.

```lean
α : Type u_1,
n : ℕ,
i j : fin n,
a : fin n → α,
h : i = j
⊢ eq.rec (a j) ((eq.rec (iff.refl (i = j)) (eq.trans (congr (congr_arg eq h) (eq.refl j)) (propext (eq_self_iff_true j)))).mpr true.intro) = a j
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 16 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129752174):
what is `rsimp`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129752244):
I can't test because that's not a MWE but I think `rfl` should work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 16 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129752301):
```quote
I can't test because that's not a MWE but I think `rfl` should work
```
It doesn't.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129752329):
What are the types of things?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 16 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129752343):
```quote
what is `rsimp`?
```
I'm not sure, but it's slow. I reworked a couple of proofs in mathlib to not use it because it slowed down the build. :simple_smile:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 16 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129752482):
@**Mario Carneiro** Why isn't it a MWE? That's the entire context. What else do you need?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 16 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129752504):
something he can copy-paste

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129752509):
DId you try making an `example` out of that? the motive of the `eq.rec` isn't inferrable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 16 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129752604):
Right, I see. I can try.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 16 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129752774):
This is my current hacky proof progress:

```lean
variables {α : Type*} {n : ℕ}

def modify (a : array n α) (i : fin n) (f : α → α) : array n α :=
a.write i $ f $ a.read i

@[simp] theorem modify_id (a : array n α) (i : fin n) : a.modify i id = a :=
by simp [modify, read, write, d_array.write, d_array.read];
   cases a with a;
   congr;
   funext j;
   dsimp; dsimp at a;
   by_cases h : i = j; simp [h]; dsimp
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 16 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129752816):
Oh, I just realized I don't have `decidable_eq α`. Perhaps that's what's missing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129752881):
You don't need it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129753171):
```
@[simp] theorem modify_id (a : array n α) (i : fin n) : a.modify i id = a :=
array.ext $ λ j, by by_cases i = j; simp [h, modify]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 16 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129753229):
Very nice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129753235):
Don't gratuitously unfold things, it often makes your life harder

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 16 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129753264):
Huh, looks like my hacks were doing something similar:

```lean
protected lemma ext {a b : d_array n α} (h : ∀ i, read a i = read b i) : a = b :=
by cases a; cases b; congr; exact funext h
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 16 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129753306):
```quote
Don't gratuitously unfold things, it often makes your life harder
```
Indeed. I didn't think to look for an extensionality lemma.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 16 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129767892):
```quote
```quote
what is `rsimp`?
```
I'm not sure, but it's slow. I reworked a couple of proofs in mathlib to not use it because it slowed down the build. :simple_smile:
```
```lean
set_option profiler true 
example : true := by rsimp 
```

```
elaboration: tactic execution took 2.91s
num. allocated objects:  6337
num. allocated closures: 4935
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 16 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129767914):
human speed :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 17 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129796766):
```quote
```lean
set_option profiler true 
example : true := by rsimp 
```

```lean
elaboration: tactic execution took 2.91s
num. allocated objects:  6337
num. allocated closures: 4935
```
```

The allocation results make sense. When I looked at the generated proof terms of some `rsimp` usages, they included tons of gratuitous reflexivity, commutativity, and transitivity terms. I bet that's the case here, too.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 17 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129796870):
[2018-07-17.png](/user_uploads/3121/xKzjHVDogyMIr2UJ8bK1i4vB/2018-07-17.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 17 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129796873):
irreproducible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 17 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129798091):
tactic compilation != tactic execution

```
kb_value.lean:302:8: information
parsing took 0.0767ms
kb_value.lean:302:21: information
elaboration: tactic compilation took 2.74ms
kb_value.lean:302:21: information tactic profile data
elaboration: tactic execution took 5.34s
num. allocated objects:  7164
num. allocated closures: 5642
 5343ms   100.0%   scope_trace
 5343ms   100.0%   _interaction._lambda_2
 5343ms   100.0%   tactic.istep
 5343ms   100.0%   tactic.step
 5343ms   100.0%   tactic.rsimp
 5343ms   100.0%   tactic.focus1
 5343ms   100.0%   tactic.istep._lambda_1
 5343ms   100.0%   using_smt
 4694ms    87.9%   interaction_monad_orelse
 4477ms    83.8%   rsimp.collect_implied_eqs._lambda_4
 4475ms    83.8%   rsimp.collect_implied_eqs._lambda_1
 4475ms    83.8%   smt_tactic.iterate_at_most._main._lambda_3
 4475ms    83.8%   smt_tactic.ematch_core
  866ms    16.2%   smt_state.mk
  225ms     4.2%   rsimp_attr._lambda_1
  224ms     4.2%   _private.410121379.to_hinst_lemmas._main._lambda_5
  224ms     4.2%   to_hinst_lemmas
  219ms     4.1%   _private.3989697749.add_lemma._lambda_1
  214ms     4.0%   _private.410121379.to_hinst_lemmas._main._lambda_3
  214ms     4.0%   hinst_lemma.mk_from_decl_core
  214ms     4.0%   interaction_monad.monad._lambda_9
   38ms     0.7%   _private.410121379.to_hinst_lemmas._main._lambda_2
    5ms     0.1%   hinst_lemmas.add
    2ms     0.0%   name_set.contains
    1ms     0.0%   attribute.get_instances
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 17 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129798137):
Profiler seems to be giving out strictly less info in javascript version

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 17 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129798195):
@**Kenny Lau** try `#check id` (or indeed anything) after the `rsimp` in the online version

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 17 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129798321):
[2018-07-17-1.png](/user_uploads/3121/wbYWo5azpuBeH-w-iuMj3s4T/2018-07-17-1.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 17 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129798322):
reproduced

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 17 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20without%20rsimp/near/129798337):
Okay, so the allocations aren't what I thought they might be.

