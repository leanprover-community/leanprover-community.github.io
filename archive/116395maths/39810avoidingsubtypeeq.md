---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/39810avoidingsubtypeeq.html
---

## Stream: [maths](index.html)
### Topic: [avoiding subtype.eq](39810avoidingsubtypeeq.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 21 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132541236):
```lean
import data.real.basic

example (p : ℝ → Prop) (a b : ℝ) (ha : p (a / 2)) (hb : p (b / 2)) (hab : a / 2 = b / 2) :
@eq {x : ℝ // p x} ⟨a/2,ha⟩ ⟨b/2,hb⟩ := 
begin
  rw hab -- fails
end
-- rewrite tactic failed, motive is not type correct

example (p : ℝ → Prop) (a b : ℝ) (ha : p (a / 2)) (hb : p (b / 2)) (hab : a / 2 = b / 2) :
@eq {x : ℝ // p x} ⟨a/2,ha⟩ ⟨b/2,hb⟩ := 
begin
  subst hab -- fails
end
-- subst tactic failed, hypothesis 'hab' is not of the form (x = t) or (t = x)
-- would have worked if hab was a = b

example (p : ℝ → Prop) (a b : ℝ) (ha : p (a / 2)) (hb : p (b / 2)) (hab : a / 2 = b / 2) :
@eq {x : ℝ // p x} ⟨a/2,ha⟩ ⟨b/2,hb⟩ := 
begin
  apply subtype.eq,
  exact hab,
end
-- do I have to do it like this?
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 21 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132541258):
Is there any way of doing the rewrite without using `subtype.eq`? i.e. some high-powered tactic? I've had some luck with `subst` in the past but not here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 21 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132541320):
dammit `simp` works this time :-) It didn't work in my real world example!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 21 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132541352):
`by congr'`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 21 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132541430):
Makes me think: shouldn't `lemma subtype.ext` be marked as an extensionality lemma?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 21 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132541758):
I'm trying to reproduce the problem that @**Luca Gerolla** has. He had `rw` failing because of the motive issue, `subst` failing because the hypothesis wasn't variable=term, and `simp` timing out. I have `simp` taking ages:

```lean
example (p : ℝ → Prop) (a b : ℝ) (ha : p ((a / 2) / ( 1 / 2)))
(hb : p ((b / 2) / (1 / 2)))
(hab : a / 2 = b / 2)
(X : {x : ℝ // p x} → ℝ) :
X ⟨(a/2)/(1/2),ha⟩ = X ⟨(b/2)/(1/2),hb⟩ := 
begin
  simp [hab]
end
```

but not timing out yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 21 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542034):
```lean
import data.real.basic

example (p : ℝ → Prop) (a b : ℝ) (ha : p ((a / 2) / ( 1 / 2)))
(hb : p ((b / 2) / (1 / 2)))
(hab : a / 2 = b / 2)
(f : {x : ℝ // p x} → ℝ) :
f ⟨(a/2)/(1/2),ha⟩ = f ⟨(b/2)/(1/2),hb⟩ := 
begin
  simp [hab]
end

example (p : ℝ → Prop) (a b : ℝ) (ha : p ((a / 2) / ( 1 / 2)))
(hb : p ((b / 2) / (1 / 2)))
(hab : a / 2 = b / 2)
(X : equiv {x : ℝ // p x} ℝ) :
X ⟨(a/2)/(1/2),ha⟩ = X ⟨(b/2)/(1/2),hb⟩ := 
begin
  simp [hab]
end
```

For me, the yellow bars take far longer for the `f` version than the `X` version. Is that expected? I still haven't got the timeout but I get quite a long pause with the `f` version.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 21 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542095):
use `congr'`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 21 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542434):
fair enough. I used `apply congr_arg`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Aug 21 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542590):
Was the fact that `ha` and `hab` were "lost" (i.e. left with _) that caused the deterministic timeout with `simp`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Aug 21 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542609):
Thanks for this, I was completely unaware of the `congr` tactic - another good learning!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 21 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542694):
Luca I've failed to reproduce your timeout in a controlled setting so far and I don't really want to post a 1300 line file :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 21 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542711):
`congr` unfolds as many layers as it can (i.e. reduces $$f(g(x))=f(g(y))$$ to $$x=y$$ and `congr' 1` just removes one layer.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Aug 21 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542761):
I completely understand! :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Luca Gerolla (Aug 21 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542787):
```quote
`congr` unfolds as many layers as it can (i.e. reduces $$f(g(x))=f(g(y))$$ to $$x=y$$ and `congr' 1` just removes one layer.
```
That's quite helpful, probably I should implement `congr` also in other similar proofs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 21 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542860):
also with `congr'` if at any point a subgoal matches a hypothesis the subgoal will be closed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 21 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132542875):
hence why `a / 2 = b / 2 |- X ⟨(a/2)/(1/2),ha⟩ = X ⟨(b/2)/(1/2),hb⟩` is provable by `congr'`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 21 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132543105):
```quote
also with `congr'` if at any point a subgoal matches a hypothesis the subgoal will be closed
```
Good to know. https://github.com/leanprover/mathlib/pull/270

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 21 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/avoiding%20subtype.eq/near/132543959):
`simp` is taking far longer than the profiler says. If I write this:

```lean
import data.real.basic

set_option profiler true

set_option trace.simplify true

theorem X234 (p : ℝ → Prop) (a b : ℝ) (ha : p ((a / 2) / ( 1 / 3)))
(hb : p ((b / 2) / (1 / 3)))
(hab : a / 2 = b / 2)
(f : {x : ℝ // p x} → ℝ) :
f ⟨(a/2)/(1/3),ha⟩ = f ⟨(b/2)/(1/3),hb⟩ := 
by simp [hab]
```

then the profiler says that elaboration takes under 0.5 seconds, but if I change the name of the theorem then I see the orange bars for around 4 seconds (on a reasonable machine). 

Possibly unrelated: I'd never seen this sort of thing in the simp trace debugging output before:

```
[simplify] iff: function.injective f
[simplify] eq: function.injective f
[simplify] eq: f
[simplify] eq: function.injective
[simplify.failure] proof stuck at: function.injective f
[simplify.failure] failed to prove: ?x_3 : function.injective f
1. [simplify.failure] fail to instantiate emetas: 'function.injective.eq_iff' at
f (@subtype.mk ℝ (λ (x : ℝ), p x) (b / 2 / 3⁻¹) _) = f (@subtype.mk ℝ (λ (x : ℝ), p x) (b / 2 / 3⁻¹) _)
partially instantiated lemma:
@function.injective.eq_iff {x // p x} ℝ f ?x_3
  (@subtype.mk ℝ (λ (x : ℝ), p x) (b / 2 / 3⁻¹)
     (@eq.rec ℝ (a / 2 / (1 / 3)) (λ (val : ℝ), (λ (x : ℝ), p x) val) ha (b / 2 / 3⁻¹)
        (@(λ [c : has_div ℝ] (a a_1 : ℝ) (e_2 : a = a_1) (a_2 a_3 : ℝ) (e_3 : a_2 = a_3),
            @congr ℝ ℝ (@has_div.div ℝ c a) (@has_div.div ℝ c a_1) a_2 a_3
              (@congr_arg ℝ (ℝ → ℝ) a a_1 (@has_div.div ℝ c) e_2)
              e_3)
           (@division_ring_has_div ℝ real.division_ring real.division_ring)
           (a / 2)
           (b / 2)
           hab
           (1 / 3)
           3⁻¹
           (@one_div_eq_inv ℝ real.division_ring 3))))
  (@subtype.mk ℝ (λ (x : ℝ), p x) (b / 2 / 3⁻¹)
     (@eq.rec ℝ (b / 2 / (1 / 3)) (λ (val : ℝ), (λ (x : ℝ), p x) val) hb (b / 2 / 3⁻¹)
        (@(λ [c : has_div ℝ] (a a_1 : ℝ) (e_2 : a = a_1) (a_2 a_3 : ℝ) (e_3 : a_2 = a_3),
            @congr ℝ ℝ (@has_div.div ℝ c a) (@has_div.div ℝ c a_1) a_2 a_3
              (@congr_arg ℝ (ℝ → ℝ) a a_1 (@has_div.div ℝ c) e_2)
              e_3)
           (@division_ring_has_div ℝ real.division_ring real.division_ring)
           (b / 2)
           (b / 2)
           (@eq.refl ℝ (b / 2))
           (1 / 3)
           3⁻¹
           (@one_div_eq_inv ℝ real.division_ring 3))))
```


{% endraw %}
