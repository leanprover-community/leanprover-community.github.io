---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/11403reflexivetransitiveclosureandrecursion.html
---

## [general](index.html)
### [reflexive-transitive closure and recursion](11403reflexivetransitiveclosureandrecursion.html)

#### [Shachar Itzhaky (Jun 12 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127960102):
Lean has a transitive closure but I want a reflexive-transitive one. So I wrote the following definition:
```lean
variable {D : Type}
variable R : D -> D -> Prop

inductive rtc : D -> D -> Prop
| refl : ∀ s, rtc s s
| step : ∀ (s u t), R s u → rtc u t → rtc s t
```

I was happy that without knowing much Lean upfront, I was able to prove a simple theorem.
```lean
theorem rtc_trans : forall (s u t : D), rtc R s u -> rtc R u t -> rtc R s t :=
  begin
    intros s u t H1 H2, induction H1, { exact H2 }, 
    { apply rtc.step, apply H1_a, apply H1_ih, apply H2 }
  end
```

The proof utilizes `rtc.drec`. Which is fine. But it would be very illustrative to carry out the same proof via a recursive definition. This, however, requires a `match`, and I was not able to destructure `rtc R s t` in any way:
```lean
def hmm (s t : D) (H : rtc R s t) : true :=
  match H with
  | rtc.refl _ _ := true.intro
  | rtc.step R u _ su ut := λ h, true.intro
```

This fails to typecheck because `rtc.refl _ _` gets the type `rtc R _x _x`, which does not unify with `rtc R s t`. While the error message sounds reasonable, it sounds weird that there is an inductive type that cannot be `match`ed on. Is there any way around that?

#### [Kenny Lau (Jun 12 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127960356):
put the hypothesis after the colon and use the equation compiler instead of `match`

#### [Kenny Lau (Jun 12 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127960364):
put everything after the colon

#### [Johannes Hölzl (Jun 12 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127960374):
In mahlib we have the reflexive transitive closure: https://github.com/leanprover/mathlib/blob/master/logic/relation.lean#L61

#### [Johannes Hölzl (Jun 12 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127960479):
`match` can do cases on `rtc` but you need to give it the allowance, e.g. one of `s` and `t` in `rtc s t` should be a variable, and you need to pass this variable into `match` so that it can change it, a.l.a `match s, h : rtc s t where _, rtc.refl _ := ... end`

#### [Shachar Itzhaky (Jun 13 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127977723):
Thanks... I know nothing about the equation compiler and I am still struggling with dependent match but at least fixing one side of the rtc to a variable makes sense to me. I am trying to encode a system that has both unfolding rules --- one that unfolds the first step of the path, and one that unfolds the last step. I will probably define those as two inductive Props and prove their equivalence.

What is the meaning of the `refl` constructor having an empty implicit parameter list `{}`?

#### [Andrew Ashworth (Jun 13 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127977878):
it is an instruction to lean to infer the implicit argument from the return type

#### [Andrew Ashworth (Jun 13 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127977884):
consider 
```lean
inductive sum (α : Type u) (β : Type v)
| inl {} : α → sum
| inr {} : β → sum
```

#### [Andrew Ashworth (Jun 13 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127977895):
here the empty implicit parameter list is an annotation to infer the type alpha in `inl` and beta in `inr`

#### [Andrew Ashworth (Jun 13 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127978043):
hrm, maybe not the greatest example since the definition goes through without the brackets anyway...

#### [Andrew Ashworth (Jun 13 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127978175):
ok, if you paste this
```lean
inductive sum' (α β : Type) 
| inl : α → sum'
| inr {} : β → sum'

#print sum'
```

#### [Andrew Ashworth (Jun 13 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127978178):
then you'll see a difference in how lean evaluates the expression

#### [Shachar Itzhaky (Jun 13 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127978234):
Ok, so in fact the `{}` is for *beta*  in `inl` (since alpha is already there).

#### [Andrew Ashworth (Jun 13 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127978248):
oops, haha

#### [Andrew Ashworth (Jun 13 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127978250):
yes

#### [Shachar Itzhaky (Jun 13 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127978257):
How does Lean know that alpha has to be implicit, in inl without the `{}`?

#### [Shachar Itzhaky (Jun 13 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127978303):
Oh silly me, of course the first parameter is of type alpha.

#### [Shachar Itzhaky (Jun 13 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127978461):
Ok, this was immaterial to the discussion of matches, back to struggling with `match s, h : rtc R s t` then. Can anyone explain that cryptic line above?

#### [Shachar Itzhaky (Jun 13 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127978796):
I didn't manage to put the type annotation `H : rtc R s t` but the match seemed to work even without it, by virtue of having `s` available to the equation compiler perhaps?
```lean
def hmm (s t : D) (H : rtc R s t) : true :=
  match s, H with
  | _, rtc.refl := fun h, trivial
  | _, rtc.step _ _ _ := fun h, trivial
```

I am a bit perplexed still by the fact that the match branches have type `?? -> true` rather than just `true`...

#### [Andrew Ashworth (Jun 13 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127979054):
if you had to write out the definition by hand using `rtc.drec_on` or `rtc.rec_on`, how would you avoid the first argument? (match uses those under the hood iirc, but somebody correct me if I'm mistaken)

#### [Andrew Ashworth (Jun 13 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127979117):
```lean
def hmm' (s t : D) (H : rtc R s t) : true :=
rtc.rec_on H 
  (λ _, true.intro) 
  (by intros; exact true.intro)
```

#### [Shachar Itzhaky (Jun 13 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127979287):
Yes, it looks like it does — it just clashes somehow with my understanding of Type Theory and CIC (where there is a `fix` construct).

#### [Shachar Itzhaky (Jun 13 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127979411):
BTW the compiler seems to make quite a monster out of my small match:
```lean
def ReflexiveTransitiveClosure.hmm._match_1 : ∀ {D : Type} (R : D → D → Prop) (t _a : D), rtc R _a t → true :=
λ {D : Type} (R : D → D → Prop) (t _a : D) (_a_1 : rtc R _a t),
  rtc.dcases_on _a_1
    (λ (H_1 : t = _a), eq.rec (λ (_a : rtc R t t) (H_2 : _a == rtc.refl), id_rhs true trivial) H_1 _a_1)
    (λ (u : D) {t_2 : D} (a : rtc R _a u) (a_1 : R u t_2) (H_1 : t = t_2),
       eq.rec (λ (a_1 : R u t) (H_2 : _a_1 == rtc.step u a a_1), id_rhs true trivial) H_1 a_1)
    (eq.refl t)
    (heq.refl _a_1)
```

#### [Andrew Ashworth (Jun 13 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127979551):
i don't know if this is any prettier to you 
```lean
def hmm' : ∀ (s t : D) (H : rtc R s t), true 
| _ _ (rtc.refl _ _ ) := true.intro
| _ _ (rtc.step _ _ _ _ _) := true.intro

#print hmm'._main
```

#### [Andrew Ashworth (Jun 13 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127979666):
when I want a definition that unfolds nicely I tend to write it out by hand using the appropriate recursion lemma. If you use the equation compiler as I did above, the main def is somewhat ugly but it generates quite nice ._eqn1, ._eqn2 branches

#### [Shachar Itzhaky (Jun 13 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127995826):
Yes, I ended up doing that myself, eventually. I found `hmm'._main` but what are `._eqn1`, `._eqn2`?

At any rate, the purpose of this mental exercise was to demonstrate that explicit induction and "normal" recursion coincide, so of course I could write it with `rec_on` but that would miss the point...

#### [Kevin Buzzard (Jun 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127996308):
You can try `#print prefix hmm'` to see everything starting `hmm'.`

#### [Kevin Buzzard (Jun 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/127996316):
although in the back of my mind I think there might be an easier way of just seeing the equation lemmas...

#### [Shachar Itzhaky (Jun 13 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/128002149):
I somehow get `no declaration starting with prefix 'hmm''`.

#### [Mario Carneiro (Jun 13 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/128002289):
In lean, type ascriptions have required parentheses, it should be `(H : rtc R s t)` not `H : rtc R s t`

#### [Shachar Itzhaky (Jun 13 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/128002346):
I was convinced I tried that when the original suggestion didn't work... but yeah, parenthesis do the trick! Although, as I said, the definition goes through without the ascription as well.

#### [Mario Carneiro (Jun 13 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/128002348):
Lean is a bit limited in its ability to do induction on inductive predicates using the equation compiler. I recommend using the `induction` tactic instead if you have any problems with writing it the way Andrew suggested

#### [Shachar Itzhaky (Jun 13 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/128002364):
Yes, I will reiterate: using tactic mode as well as `rec_on` were pretty smooth. The reason I am in this discussion is that I wanted to demonstrate to my students how induction is just a form of recursion that they know from programming.

#### [Mario Carneiro (Jun 13 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/128002429):
I usually point at the type of rec_on, remark that it looks a lot like induction, and then use it to define a recursive function and also prove some property about it

#### [Shachar Itzhaky (Jun 13 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/128002441):
:thumbs_up: I assume this is "the Lean way" then.

#### [Mario Carneiro (Jun 13 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/128002498):
In the case of an inductive predicate like `rtc`, it actually can't be used for recursion, since it has small elimination

#### [Mario Carneiro (Jun 13 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/128002499):
it can only be used to prove props

#### [Mario Carneiro (Jun 13 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/128002543):
If you put the inductive type in `Type` though it could

#### [Shachar Itzhaky (Jun 13 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/128002564):
Of course. The analogue that I can refer to is that in Coq I wrote the same proof, once with `induction`, and once with `Fixpoint` -- of course, since you destructure the `Prop` inside the def, the function must return a `Prop`.

#### [Shachar Itzhaky (Jun 13 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive closure and recursion/near/128002573):
I still see that as a form of recursion though, since it's expressed via `Fixpoint`.

