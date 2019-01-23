---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/93951ordcaseson.html
---

## Stream: [general](index.html)
### Topic: [or.dcases_on](93951ordcaseson.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Jul 02 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128973389):
In general, what does this message mean? induction tactic failed, recursor "or.dcases_on" can only eliminate into Prop.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Jul 02 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128973395):
this happens at the head of a inductive function def.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 02 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128973396):
it means you can't decompose an `or` into data

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Jul 02 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128974745):
is it just `or`, or any inductive types in general? because there is no `or` in my code.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 02 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128974933):
A lot of (but not all) inductive propositions cannot eliminate into data. inductive non-propositions can always eliminate into data.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 02 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128975489):
Stupid question: can one get around this somehow with classical or noncomputable assumptions? Or does one run into contradictions in this generality?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 02 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128975510):
```quote
is it just `or`, or any inductive types in general? because there is no `or` in my code.
```
@**Zesen Qian** If you post a minimal working example as a gist then perhaps someone can locate the `or` ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 02 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128975607):
You can, but you have to decide what to do when both sides are true.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 02 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128975772):
So you might end up with a function whose behaviour is unknown when they're both true.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 02 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128976030):
By using `prod_decidable`, you can make a function to go from or to sum:

```lean
local attribute [instance] classical.prop_decidable

noncomputable def or.to_sum (h : p ∨ q) : plift p ⊕ plift q :=
if h' : p then sum.inl ⟨ h' ⟩
          else sum.inr ⟨ by { rw ← false_or q, exact or.imp_left h' h } ⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jul 02 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128977157):
What you can't get when eliminating into non-Prop is the computation rule that reduces an application `or.cases_on (or.inl p) f g` to `f p` and also `or.cases_on (or.inr q) f g` to `g q`, since `or.inl trivial = or.inr trivial` but `f trivial` might not be equal to `g trivial` (unless the result type is a proposition).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Jul 02 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128978404):
sorry so what's default universe level of inductive types that's not specified level? Is it polymorphisized on all levels?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 02 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128978561):
I'm sorry I can't parse your question. Are you talking of an error message?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Jul 02 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128978664):
no I mean like 
```
inductive bool
| true
| false
```
will there be universe polymorphism for this, or just Type 1?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 02 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128978673):
universe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 02 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128978856):
I would guess it's a `Type 0` but I recommend you discover it for yourself. Try `#check bool`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Jul 02 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128978943):
yes it's Type 0, thank you.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 02 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979001):
```lean
inductive bool1
| true : bool1
| false : bool1 

#check bool1 -- Type 

universe u 

inductive bool2 : Type u
| true : bool2 
| false : bool2 

#check bool2 -- Type u_1 (i.e. universe is "whatever")

universe v 

#check bool2.{v} -- Type v
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 02 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979004):
There are some tricks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Jul 02 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979252):
Thanks, I guess we can use it to workaround "universe too big" issue with this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Jul 02 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979305):
I now have an error saying the argument of a constructor is too big.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Jul 02 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979327):
```
inductive t0 : Type u
...

inductive t1 : Type u
| cons : t0 -> t1
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 02 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979349):
On `t1`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Jul 02 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979513):
yeah, says the first argument of cons, t0, is too big.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 02 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979547):
If you don't tell `t1` what type it is then this might fix it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 02 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979615):
```lean
universe u 

inductive t0 : Type u
| foo : t0

inductive t1 
| cons : t0 -> t1
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jul 02 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979630):
Maybe the `u` of `t0` is not the same `u` as in `t1`, although I would expect a different error message then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 02 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979636):
I was thinking maybe this would be required:

```lean
inductive t1 : Type u
| cons : t0.{u} -> t1
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 02 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979662):
But more generally, there is no reason for `t0` not to be in `Type 0`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Jul 02 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979673):
@**Simon Hudon** thanks, this fixes it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Jul 02 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979685):
basically I'm still trying out the universes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 02 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979752):
```lean
inductive t0 : Type
| foo : t0

inductive t1 : Type
| cons : t0 → t1
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 02 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979755):
I learned this the hard way: when definitions are more universe polymorphic than strictly necessary, it gets really painful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Jul 02 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979843):
@**Kevin Buzzard** but this doesn't provide universe polymorphism.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 02 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979851):
Case in point: my current `traversable` pull request took me one year to set up. It was not all about universe polymorphism but it certainly made it difficult

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Jul 02 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979855):
and I kind of feel my first error in this stream, has something to do with it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jul 02 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979859):
I'm not sure what universe polymorphism is good for when it comes to concrete programs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 02 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979870):
universe is for consistency

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jul 02 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979871):
I feel like everything I need to do lives in `Type`, for the most part

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 02 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979887):
and strengthening

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Jul 02 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979892):
I don't know what dependent types is good for when it comes to concrete programs, TBH.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 02 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979895):
and category theory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jul 02 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979982):
dtt is a bit of an academic stretch right now, true, but one day when there's an efficient method for program extraction, it might be awesome

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 02 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980001):
I think we can weaken @**Andrew Ashworth** 's suggestion and generalize it into: work in `Type 0` until you run into trouble. Then make the smallest necessary universe generalization

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jul 02 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980012):
if you knew how terribly written most of the software that runs the electronics around us was, you'd be rooting for Lean too :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 02 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980019):
There are tools for lifting monomorphic definitions to using them in polymorphic contexts so `Type 0` is not handicapping

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 02 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980075):
Amen

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 02 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980109):
@**Andrew Ashworth** I'm getting ready for the DeepSpec summer school where people like Adam Chlipala will show us how he uses dependent type theory for building reliable cryptographic implementation. It's hard to argue that it's really just academic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jul 02 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980166):
isn't anything chlipala does academic by definition ;]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 02 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980218):
It depends. Is your definition of academic "anything that happens in a university"? In that case, is the university's janitor studying academic sweeping?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 02 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980322):
In the case of the DeepSpec project, academics are playing the role of leader but the project involves industrial partners so the point is not (only) publication but building systems that work Monday through Sunday

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Jul 02 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980388):
before it's getting too far, let me ask one last question:  can I define structure as universe polymorphic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Hoang Le Truong (Jul 02 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980390):
Yes it depend. how I get   f (x:α) because I need it to define next object

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 02 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980618):
@**Hoang Le Truong** I think you're in the wrong thread

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jul 02 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980679):
@**Zesen Qian** about your original error, it has to do with the difference between `Prop` and `Type` (or more generally `Type u`), which is rather different from the difference between `Type u` for varying `u`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jul 02 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980778):
You can generalize over both `Prop` and `Type` with `Sort`, but all the `Type u` for different `u` work pretty much the same way, while `Prop` has some different rules

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Jul 02 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128982406):
thanks, I will look into it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Jul 03 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/129029014):
yeah I give up. Here is the line causing this error:
https://github.com/riaqn/smtlean/blob/6e5c20aaa344e972528d8089af01f638819ff06c/src/cvc4.lean#L129

