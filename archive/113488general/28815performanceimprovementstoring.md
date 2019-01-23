---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28815performanceimprovementstoring.html
---

## Stream: [general](index.html)
### Topic: [performance improvements to ring](28815performanceimprovementstoring.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 02 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133227901):
@**Rob Lewis** The latest commit replaces some of the `mk_app` applications used in `ring`, and there was a *huge* performance gain. Now `ring` will solve `(x + y)^n = (x+y)^n` up to `n = 60` before hitting the timeout, compared to `n = 11` before

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 02 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133227944):
```
example (ε : ℚ) : ε / 3 + ε / 3 + ε / 3 = ε := by ring
```
takes a fraction of a second now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 02 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133227959):
Is this something we could learn from?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 02 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133227997):
`mk_app` sucks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 02 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133228008):
There are still some `mk_app` uses in ring, but the problems seem to be when some of the arguments are (large) proof terms, even if they aren't used in type inference

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 02 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133228011):
I think it is typechecking the terms, which is a really bad idea since it gets done so often

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 02 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133228387):
good catch Mario. I have had a lot of success with ring in the past but I usually cleared denominators myself and then applied the tactic when there were no divisions left.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 02 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133228677):
the problem wasn't denominators per se. The major slowdown was in structural parts of the proof that are done in just about every proof. For example normalizing `(x+y)^n`uses no division

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 02 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133228678):
I assume you're talking about `tactic.mk_app`. What do you replace it with? I was told it was preferable to use it to `to_expr`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 02 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133228807):
`mk_app` will build an application while performing typeclass inference and typechecking (or at least inferring the types) of all passed arguments. The alternative is just to build the expr yourself, using `expr.app` or `expr.mk_app`, which does no typechecking or inference. I thought the inference might be slow, which is why `ring` uses an `instance_cache`, but I think that this was not the problem. Now I just do the typeclass inference directly and then put the app together manually.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 02 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133228852):
```
meta def cache.mk_app (c : cache) (n inst : name) (l : list expr) : tactic expr :=
do m ← mk_instance ((expr.const inst [c.univ] : expr) c.α),
   return $ (@expr.const tt n [c.univ] c.α m).mk_app l
```
then
```
c.mk_app ``norm_num.subst_into_prod ``has_mul [l, e, tl, e, t, hl, hr, p₂],
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 02 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133229004):
That's awesome! I spent a little while profiling `linarith` earlier today and was also seeing performance problems with `mk_app`. It's not a straightforward story when to use it over `to_expr`, and yeah, making expressions by hand is probably the way to go for critical applications.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 02 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133229060):
It would be nice to have a more systematic approach to finding bottle necks. One way I could think of is to use Travis to publish metrics for every build.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 03 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133230444):
@**Mario Carneiro** I'm about to go to bed, so I'm going to leave this here for you to think about if you want to, otherwise I'll investigate tomorrow. :slight_smile: Compare the two profiles here:
```lean
set_option profiler true

constants (T : Type) (h : discrete_linear_ordered_field T)
attribute [instance] h
example (ε : T) : (41/42) * ε - (ε / 2 + ε / 3 + ε / 7) = 0 :=
by ring

example (ε : ℚ) : (41/42) * ε - (ε / 2 + ε / 3 + ε / 7) = 0 :=
by ring
```
The second one takes twice as long and spends almost all its time in the final `exact`. It's evaluating rational arithmetic in the kernel. The first one spends 20x longer in `norm_num` but that's still better than kernel evaluation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 03 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133230451):
My guess is that this is `tactic.norm_num`'s fault (the one built into core)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 03 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133255709):
After chasing down a few false leads: it isn't `tactic.norm_num`, although `tactic.norm_num` is surprisingly sensitive to typeclass short circuits. These commands take roughly the same amount of time if you add enough short circuits for `T`, otherwise the second takes 7x longer.
```lean
run_cmd prod.fst <$> norm_num `((5/60) + (1/70) : ℚ) >>= trace
run_cmd prod.fst <$> norm_num `((5/60) + (1/70) : T) >>= trace
```
I find this a little surprising since `norm_num` caches and pre-applies the instances, so it shouldn't be searching for any instance more than once. But this isn't what's causing the issue above.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 03 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133255736):
When `ring` solves `(41/42)*ε - (ε / 2 + ε / 3 + ε / 7) = 0`, it actually proves `(41/42)*ε +  -(ε / 2 + ε / 3 + ε / 7) = 0`. Unifying these over `ℚ` takes way longer than over `T` for some reason.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 03 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133255823):
There's an easy workaround: change the last lines of `ring1` to 
```lean
  ntp ← infer_type p,
  tactic.change ntp ff,
  tactic.exact p
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 03 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133255908):
The kernel is much faster at checking that the proof from `ring` has the expected type than `exact`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 03 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133278527):
Argh, this is so annoying. I inserted explicit change proof terms in the proof. I think it is fixed but keep me appraised if you find anything else.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 04 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/performance%20improvements%20to%20ring/near/133295842):
Thanks! Will do.

