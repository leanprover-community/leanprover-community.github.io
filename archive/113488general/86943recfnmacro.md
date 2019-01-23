---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86943recfnmacro.html
---

## Stream: [general](index.html)
### Topic: [rec_fn_macro](86943recfnmacro.html)

---

#### [Ben Sherman (May 21 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126885006):
I just updated Lean from 3.3.0 to 3.4.1, and now when I write this code:
```
axiom R : Type

inductive Sampler : Type
| Ret : Sampler
| BindUniform : (R → Sampler) → Sampler

def Bind : Sampler → (ℕ → Sampler) → Sampler
| Sampler.Ret f := f 0
| (Sampler.BindUniform k) f := Sampler.BindUniform (λ x, Bind (k x) f)
```
I get the error `rec_fn_macro only allowed in meta definitions` in the definition of `Bind`. Is this a bug? Should I submit it as a Github issue? Or do I just not understand what's going on?

#### [Andrew Ashworth (May 21 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126886035):
whether or not it's a bug, lean 3.4.1 is the last release in the 3xx series and only critical issues are going to be fixed

#### [Andrew Ashworth (May 21 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126886556):
if you change out `axiom R` for `variable R` do you get a more educational error message?

#### [Andrew Ashworth (May 21 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126886865):
This is some kind of universe problem, I bet

#### [Andrew Ashworth (May 21 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126887061):
maybe not. I just pasted it into my vscode and replaced `axiom R` with `variable R`. If you `#print` Sampler you get that the Sampler type is `Type u -> Type u`. Your definition is type incorrect. Now I'm confused why it ever worked in `3.3.0`...

#### [Andrew Ashworth (May 21 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126887150):
```lean
inductive Sampler : Type u₁ → Type u₁
constructors:
Sampler.Ret : Π (R : Type u₁), Sampler R
Sampler.BindUniform : Π {R : Type u₁}, (R → Sampler R) → Sampler R
```

#### [Andrew Ashworth (May 21 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126887244):
huh, interesting. The definition is correct if you use `axiom`...

#### [Kevin Buzzard (May 21 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888047):
I guess a variable is something which, if mentioned in a definition, secretly appends itself as a "forall R : type" in front of definitions

#### [Ben Sherman (May 21 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888052):
Yeah, if I switch to using a `variable` or a `parameter` in a section, the definition goes through fine. And I don't think `Sampler` becomes universe-polymorphic in any case

#### [Kevin Buzzard (May 21 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888067):
whereas perhaps with an axiom this does not happen.

#### [Kevin Buzzard (May 21 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888086):
But isn't the error with `Bind` simply because Lean can't prove that the definition "terminates"?

#### [Kevin Buzzard (May 21 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888148):
cf the meta def of that 91 function in Programming In Lean, where the definition is OK but this is too hard for Lean to spot so you have to make it meta

#### [Kevin Buzzard (May 21 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888224):
```lean
axiom R : Type
variable S : Type

theorem X : R = R := rfl
theorem Y : S = S := rfl

#check X -- R = R
#check Y -- ∀ (S : Type), S = S
```

#### [Kevin Buzzard (May 21 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888301):
The axiom makes a new constant, like `quotient.sound` or whatever -- when you mention quotient.sound you don't get random "forall quotient.sound" hypotheses appearing in theorems

#### [Kevin Buzzard (May 21 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888317):
but the variable gets inserted. I guess you guys both know this.

#### [Ben Sherman (May 21 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888389):
@**Kevin Buzzard** No,  this is actually a primitive recursive definition:
```
protected eliminator Sampler.rec : Π {real : Type} {C : Sampler real → Sort l},
  C (Sampler.Ret real) →
  (Π (a : real → Sampler real), (Π (a_1 : real), C (a a_1)) → C (Sampler.BindUniform a)) →
  Π (n : Sampler real), C n
```
Notice how the inductive hypothesis allows you to apply the continuation to any argument.

#### [Kevin Buzzard (May 21 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888423):
I am suggesting that your definition of Bind relies on evaluating Bind elsewhere, does it not?

#### [Kevin Buzzard (May 21 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888487):
And with the definition of nat, Lean can use some recursion principle to check that the definition is good.

#### [Kevin Buzzard (May 21 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888566):
Presumably the error means "I find myself trying to prove that this definition of Bind has a decent recursor but I find myself trying to write some induction over functions, so I give up, make me meta so I don't have to worry about this sort of thing and can just be untrusted code"

#### [Kevin Buzzard (May 21 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888576):
heh

#### [Kevin Buzzard (May 21 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888586):
making the definition of Bind meta doesn't make the error go away :-)

#### [Ben Sherman (May 21 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888735):
So the definition works if I apply the recursor directly:
```
axiom real : Type

inductive Sampler : Type
| Ret : Sampler
| BindUniform : (real → Sampler) → Sampler

def Bind (x : Sampler) : (ℕ → Sampler) → Sampler
:= @Sampler.rec_on (λ _, (ℕ → Sampler) → Sampler) x
     (λ f, f 0)
     (λ k ih f, Sampler.BindUniform (λ x, ih x f))
```
So, even though the definition is primitive recursive, it does look to be something to do with it failing in figuring out the recursion scheme.

#### [Kevin Buzzard (May 21 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126889923):
I am really confused by that recursor

#### [Kevin Buzzard (May 21 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126889945):
`(Π (a_1 : R), C (a a_1))`

#### [Kevin Buzzard (May 21 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890135):
```lean

inductive Sampler : Type
| Ret : Sampler
| BindUniform : (ℤ → Sampler) → Sampler



def Bind : Sampler → (ℕ → Sampler) → Sampler
| Sampler.Ret f := f 0
| (Sampler.BindUniform k) f := Sampler.BindUniform (λ x, Bind (k x) f)


```

#### [Kevin Buzzard (May 21 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890137):
That works fine

#### [Kevin Buzzard (May 21 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890155):
replacing the constant with an explicit type

#### [Kevin Buzzard (May 21 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890565):
The definition with rec_on looks a bit funny to me -- k doesn't seem to play a role

#### [Kevin Buzzard (May 21 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890599):
oh I see

#### [Kevin Buzzard (May 21 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890616):
`ih x` is `Bind (k x)`

#### [Kevin Buzzard (May 21 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890620):
that's the role of `ih`

#### [Ben Sherman (May 21 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890770):
@**Kevin Buzzard** Yes, exactly!

#### [Kevin Buzzard (May 21 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890773):
so I finally understand the question :-)

#### [Kevin Buzzard (May 21 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890852):
so it is a bit weird that it will work for a concrete type like the integers but won't work for the constant, or at least it's weird to me

#### [Ben Sherman (May 21 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890872):
Right, and if you change from `axiom` to `parameter` or `variable`, it works again. So I'm thinking it's a bug.

#### [Kevin Buzzard (May 21 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890895):
well, with variable you change the type

#### [Kevin Buzzard (May 21 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890900):
so you have to fiddle with everything

#### [Ben Sherman (Nov 08 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/147271354):
I'm having another issue with rec_fn_macro: I've reduced it to this bug this time:
```
import analysis.real
def foo : bool → list ℝ
| tt := list.nil
| ff := 1/2 :: foo tt
```
I get the error:
```
equation compiler failed to generate bytecode for 'foo._main'
nested exception message:
code generation failed, VM does not have code for 'real.division_ring'
```
If I try to mark `foo` as `noncomputable`, I instead get an error about a failure to prove the recursion well-founded.
Does anyone have any idea for how to get around this issue?
In my actual code, I'm getting a `rec_fn_macro` issue that appears nonlocally - it's failing for a definition that calls some other function `bar` that involves division on ℝ. If I redefine `bar` as `sorry`, there is no longer any issue. But it doesn't even help for me to mark `bar` as `irreducible`.

#### [Mario Carneiro (Nov 08 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/147271582):
I don't see the issue. This is certainly `noncomputable`, and that's the error you get if you don't mark it so. And it is failing to prove the recursion is well founded because the default well founded instance on bool has tt and ff incomparable, so you can't do any recursion.

#### [Mario Carneiro (Nov 08 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/147271643):
perhaps you have oversimplified your example?

#### [Ben Sherman (Nov 08 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/147271849):
Thanks! I didn't know that details about the well-foundedness. Then I indeed oversimplified my example - originally it was nat. Let me backtrack with a revised example.

