---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/42283intersections.html
---

## [general](index.html)
### [intersections](42283intersections.html)

#### [Patrick Massot (Jul 03 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129031496):
Do we have a better way to do
```lean
example {α : Type*} (a b c : set α) : a ∩ b ∩ (a ∩ c) = a ∩ b ∩ c :=
by ext x ; split ; finish
```

#### [Patrick Massot (Jul 03 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129031518):
Of course I'm not asking for the magic sequence of rewrite, I want Lean to figure it out.

#### [Sean Leather (Jul 04 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129068018):
It would be nice if there was. I run into something similar with conjunction  (e.g. `a ∧ b ∧ (a ∧ c) = a ∧ b ∧ c`) all the time.

#### [Simon Hudon (Jul 04 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129068883):
does `cc` help?

#### [Patrick Massot (Jul 04 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129073167):
no

#### [Patrick Massot (Jul 04 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129083986):
A related question is: can anyone bring https://leanprover.github.io/programming_in_lean/#09_Writing_Automation.html up to date with current Lean?

#### [Reid Barton (Jul 04 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129086682):
@**Sean Leather** for `a ∧ b ∧ (a ∧ c) ↔ a ∧ b ∧ c`, `tauto` works.

#### [Sean Leather (Jul 04 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129086756):
Yeah, that may be true for that example. But I've run into others where `tauto` didn't work.

#### [Reid Barton (Jul 04 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129086829):
Yes, `tauto` is good at failing frustratingly close to the goal

#### [Sean Leather (Jul 04 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129086836):
`true`:exclamation:

#### [Simon Hudon (Jul 04 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129090032):
```quote
Yes, `tauto` is good at failing frustratingly close to the goal
```
Excellent, that's what I wrote it for

#### [Simon Hudon (Jul 04 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129090080):
But seriously, any examples of what it can't handle?

#### [Reid Barton (Jul 04 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129090724):
as alluded to above, `example (p : Prop) : p ∧ true ↔ p := by tauto`

#### [Reid Barton (Jul 04 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129090747):
Somewhat less trivially, I often find it gets stuck needing to prove `a = b` when `b = a` is available as a hypothesis

#### [Simon Hudon (Jul 04 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129090994):
The latter should be getting better. @**Scott Morrison** recently submitted a patch to consider the symmetry of relations in `solve_by_elim` which `tauto` uses.

#### [Simon Hudon (Jul 04 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129091055):
As for the first, `true` is probably the culprit. That's an easy fix, I can submit a PR right away

#### [Simon Hudon (Jul 04 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129091070):
While I'm at it, I'll also take care of `false` in the assumptions.

#### [Simon Hudon (Jul 04 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129091736):
Done: https://github.com/leanprover/mathlib/pull/175

#### [Patrick Massot (Jul 04 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129091823):
Simon, what is the relation between this `tauto` and https://leanprover.github.io/programming_in_lean/#09_Writing_Automation.html Would you be able to update the later?

#### [Simon Hudon (Jul 04 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129092168):
I haven't looked closely but that should be doable.

#### [Simon Hudon (Jul 04 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129092252):
I'll take a look

#### [Simon Hudon (Jul 04 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129092447):
By the way, don't despair, I haven't forgotten your request for tutorials

#### [Simon Hudon (Jul 04 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129092479):
I'm preparing a talk about Lean tactics that I'll give at the DeepSpec summer school. That should be the seed for a useful tutorial

#### [Patrick Massot (Jul 04 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129092537):
Nice!

#### [Simon Hudon (Jul 04 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129092543):
I think I'll present the `transportable` problem that @**Kevin Buzzard** brought in a few months ago

#### [Kevin Buzzard (Jul 04 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129093692):
+1 from me -- as I've probably said 100 times, this is something which mathematicians do subconsciously.

#### [Johan Commelin (Jul 04 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129094956):
(And that is *subconsciously*, with big fat capital letters :wink:)

#### [Sean Leather (Jul 05 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129120435):
Reid:

```quote
Somewhat less trivially, I often find it gets stuck needing to prove `a = b` when `b = a` is available as a hypothesis
```

Same here! That's the main reason I gave up on using `tauto`.

Simon:

```quote
The latter should be getting better. Scott Morrison recently submitted a patch to consider the symmetry of relations in `solve_by_elim` which `tauto` uses.
```

Cool. I'll have to try it out again.

#### [Simon Hudon (Jul 05 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129121112):
Also, Mario merged my PR today. The one thing `tauto` doesn't do well still is proving disjunction. I didn't want to do back tracking out of fear that it would get slow but maybe I should do it anyway

#### [Patrick Massot (Jul 05 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129145707):
Here is what I can currently do on this topic:
```lean
variables {α : Type*} (a b c : set α) (x : α)

example : a ∩ b ∩ c = c ∩ b ∩ a :=
by simp_inter


example : a ∩ b ∩ a = a ∩ b :=
by simp_inter

example : a ∩ b ∩ (a ∩ c) = a ∩ b ∩ c :=
by simp_inter

example (x ∈ a ∩ b ∩ c) : x ∈ b :=
by simp_inter

example (x ∈ a ∩ b ∩ c) : x ∈ b ∩ a :=
by simp_inter

example (h : x ∈ a) (h' : x ∈ b) (h'' : x ∈ c) : x ∈ b ∩ a :=
by simp_inter

example : x ∈ a →  x ∈ b →  x ∈ c → x ∈ b ∩ a :=
by simp_inter
```

#### [Patrick Massot (Jul 05 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129145771):
This is based on the `destruct_conjunctions` tactic from PIL and then poor's man tactic writing

#### [Patrick Massot (Jul 05 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129145780):
```lean
open tactic monad expr
/-- Recursively destructs all hypotheses that are conjunctions. From programming in Lean. -/
meta def destruct_conjunctions : tactic unit :=
repeat (do
  l ← local_context,
  first $ l.map (λ h, do
    ht ← infer_type h >>= whnf,
    match ht with
    | `(and %%a %%b) := do
      n ← get_unused_name `h none,
      mk_mapp ``and.left [none, none, some h] >>= assertv n a,
      n ← get_unused_name `h none,
      mk_mapp ``and.right [none, none, some h] >>= assertv n b,
      clear h
    | _ := failed
    end))

/-- Simplify proving intersection and conjunctions goals -/
meta def simp_inter : tactic unit :=
`[  destruct_conjunctions, 
    try { ext } ; try { split } ; try { intros }; destruct_conjunctions,
    all_goals { repeat { split } ; assumption }]
```

#### [Patrick Massot (Jul 05 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129145791):
Any cleaner and more general way to do this is welcome :wink:

#### [Patrick Massot (Jul 05 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129145823):
Note that all examples below should really be solved by the general purpose `come_on` tactic.

#### [Simon Hudon (Jul 05 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129145893):
Haha! Have you tried `tauto` since Mario merged my PR yesterday?

#### [Patrick Massot (Jul 05 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129146378):
No. I thought you only changed stuff is `true` or `false` appears explicitly.

#### [Patrick Massot (Jul 05 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129146385):
I'm upgrading

#### [Simon Hudon (Jul 05 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129146505):
In your case, it should already work, you're right

#### [Simon Hudon (Jul 05 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129146519):
but recently, there's been added support for symmetric relations and `true` and `false` appearing in formulas

#### [Patrick Massot (Jul 05 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129146827):
`tauto` solves none of my examples

#### [Patrick Massot (Jul 05 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129146833):
even with updated mathlib

#### [Simon Hudon (Jul 05 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129146933):
and with `ext; tauto`?

#### [Patrick Massot (Jul 05 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129147034):
no luck

#### [Patrick Massot (Jul 05 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129147044):
you can try my examples, they depend on nothing else but mathlib

#### [Simon Hudon (Jul 05 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129147374):
Ok got it

#### [Simon Hudon (Jul 05 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129147387):
first `import data.set.basic`. That's where set extensionality is declared

#### [Simon Hudon (Jul 05 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129147402):
Next:

```lean
example : a ∩ b ∩ c = c ∩ b ∩ a :=
by ext; dsimp; tauto


example : a ∩ b ∩ a = a ∩ b :=
by ext; dsimp; tauto

example : a ∩ b ∩ (a ∩ c) = a ∩ b ∩ c :=
by ext; dsimp; tauto

example (x ∈ a ∩ b ∩ c) : x ∈ b :=
by dsimp at *; tauto

example (x ∈ a ∩ b ∩ c) : x ∈ b ∩ a :=
by dsimp at *; tauto

example (h : x ∈ a) (h' : x ∈ b) (h'' : x ∈ c) : x ∈ b ∩ a :=
by dsimp at *; tauto

example : x ∈ a →  x ∈ b →  x ∈ c → x ∈ b ∩ a :=
by dsimp at *; tauto
```

#### [Simon Hudon (Jul 05 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129147417):
Unfortunately, you need to unfold set notation for `tauto` to work

#### [Simon Hudon (Jul 05 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129147498):
And I'm not sure that adding `dsimp` to `tauto` would be a good idea.

#### [Simon Hudon (Jul 05 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129147588):
What I could do is match on hypotheses and goal using definitional equality instead of pattern matching

#### [Simon Hudon (Jul 05 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129147667):
Then the first proof would become:

```lean
by ext; tauto
```

I'm wondering if that would make `auto` slower. Maybe we could enable this feature with `tauto!`

#### [Simon Hudon (Jul 05 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129147699):
(In French, that would sound like you're insulting someone, with the exclamation mark)

#### [Simon Hudon (Jul 05 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129148500):
@**Mario Carneiro** I managed to add support for disjunction but it requires `tactic.interactive` to import `logic.basic`. I think the creation of `tactic.cache` would fix that situation. Should I submit that change in a separate PR? (separate from the traversable PR) If you need more time to review the traversable PR, I think that would be a good way to move forward

#### [Patrick Massot (Jul 05 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129150374):
It does look like one could define 
```lean
meta def come_one : tactic unit := `[try { ext ; dsimp at *; tauto}, try { dsimp at *; tauto}]
```
or something like this. It looks much better, thanks!

#### [Simon Hudon (Jul 05 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129150498):
:) At your service

#### [Simon Hudon (Jul 05 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129150550):
I would advise you to call it `COME_ON`. And you may want to add three exclamation marks, to communicate impatience ;-)

#### [Simon Hudon (Jul 05 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129150584):
Consider:

```lean
meta def COME_ON (x y z : parse (tk "!")) : tactic unit := ...
```

#### [Patrick Massot (Jul 05 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129161526):
The version is used currently is at https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/tactic/easy.lean It passes both the tests I had for `simp_inter` and the `tauto` tests from mathlib.

#### [Patrick Massot (Jul 05 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129161810):
Oh, it doesn't work in my real use case :(

#### [Patrick Massot (Jul 05 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129161817):
`failed to prove recursive application is decreasing, well founded relation`

#### [Reid Barton (Jul 05 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129162109):
Do you have a `_let_match` or similar in the tactic state?

#### [Patrick Massot (Jul 05 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129162191):
I don't know what is similar to `_let_match` since I have no idea what it means

#### [Patrick Massot (Jul 05 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129162291):
The full error is:
```lean
failed to prove recursive application is decreasing, well founded relation
  @has_well_founded.r
    (Σ' (a : @smooth_compatible X _inst_1 φ ψ) (a : @smooth_compatible X _inst_1 ψ φ),
       @smooth_compatible X _inst_1 ψ χ)
    (@has_well_founded_of_has_sizeof
       (Σ' (a : @smooth_compatible X _inst_1 φ ψ) (a : @smooth_compatible X _inst_1 ψ φ),
          @smooth_compatible X _inst_1 ψ χ)
       (default_has_sizeof
          (Σ' (a : @smooth_compatible X _inst_1 φ ψ) (a : @smooth_compatible X _inst_1 ψ φ),
             @smooth_compatible X _inst_1 ψ χ)))
Possible solutions: 
  - Use 'using_well_founded' keyword in the end of your definition to specify tactics for synthesizing well founded relations and decreasing proofs.
  - The default decreasing tactic uses the 'assumption' tactic, thus hints (aka local proofs) can be provided using 'have'-expressions.
The nested exception contains the failure state for the decreasing tactic.
nested exception message:
invalid apply tactic, failed to unify
  0 < 0
with
  ?m_1 < ?m_1 + ?m_2
state:
X : Type,
_inst_1 : inhabited X,
φ ψ χ : chart X,
open_triple_intersection :
  (Σ' (a : smooth_compatible φ ψ) (a : smooth_compatible ψ φ), smooth_compatible ψ χ) →
  is_open (⇑φ '' (φ.domain ∩ ψ.domain ∩ χ.domain)),
op_φ_ψ : is_open_intersection φ ψ,
smooth_φ_ψ : is_smooth_transition φ ψ,
op_ψ_φ : is_open_intersection ψ φ,
smooth_ψ_φ : is_smooth_transition ψ φ,
op_ψ_χ : is_open_intersection ψ χ,
smooth_ψ_χ : is_smooth_transition ψ χ,
x : X,
a : smooth_compatible φ ψ,
a : smooth_compatible ψ φ,
a : smooth_compatible ψ χ
⊢ 0 < 0
```

#### [Patrick Massot (Jul 05 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129162377):
Replacing ``meta def easy : tactic unit := `[try { ext } , try { dsimp at * }, all_goals { tauto }]`` by ``meta def easy : tactic unit := `[try { ext } , try { dsimp }, all_goals { tauto }]`` make it work in this case but fail in others. Somehow the `try` is not enough to prevent the error.

#### [Simon Hudon (Jul 05 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129162807):
Well-foundedness is only checked at the end of the proof I believe which means that it won't make individual tactics fail.

#### [Simon Hudon (Jul 05 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129162845):
You may just need to add a `have : _ < _, from _` expression to state and prove that some quantity decreases in your recursive function

#### [Patrick Massot (Jul 05 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129162858):
I don't have any recursive function

#### [Patrick Massot (Jul 05 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129162902):
I have no idea what Lean is talking about

#### [Simon Hudon (Jul 05 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129162947):
Can you show the goal prior to calling the tactic? There might be a way of saying "I'm not trying to bring in the curse of recursion"

#### [Patrick Massot (Jul 05 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129162972):
```lean
X : Type,
_inst_1 : inhabited X,
φ ψ χ : chart X,
open_triple_intersection :
  smooth_compatible φ ψ →
  smooth_compatible ψ φ → smooth_compatible ψ χ → is_open (⇑φ '' (φ.domain ∩ ψ.domain ∩ χ.domain)),
op_φ_ψ : is_open_intersection φ ψ,
smooth_φ_ψ : is_smooth_transition φ ψ,
op_ψ_φ : is_open_intersection ψ φ,
smooth_ψ_φ : is_smooth_transition ψ φ,
op_ψ_χ : is_open_intersection ψ χ,
smooth_ψ_χ : is_smooth_transition ψ χ,
op : is_open (⇑ψ '' (ψ.domain ∩ φ.domain ∩ χ.domain)),
this : ⇑ψ '' (ψ.domain ∩ φ.domain ∩ χ.domain) ⊆ ⇑ψ '' (ψ.domain ∩ φ.domain),
op : is_open (transition ψ φ '' (⇑ψ '' (ψ.domain ∩ φ.domain ∩ χ.domain))),
h :
  transition ψ φ '' (⇑ψ '' (ψ.domain ∩ φ.domain ∩ χ.domain)) =
    ⇑φ '' (ψ.domain ∩ φ.domain ∩ χ.domain)
⊢ ψ.domain ∩ φ.domain ∩ χ.domain = φ.domain ∩ ψ.domain ∩ χ.domain
```

#### [Simon Hudon (Jul 05 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163052):
Is the lemma that you're trying to prove  `open_triple_intersection`? If so, try `clear open_triple_intersection` before calling the tactic.

#### [Patrick Massot (Jul 05 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163058):
Note that `ext, dsimp, tauto` works here, but I want a tactic which also works when you need to `dsimp` something from context

#### [Patrick Massot (Jul 05 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163081):
Indeed, this is what I'm proving

#### [Patrick Massot (Jul 05 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163083):
and clearing this works

#### [Patrick Massot (Jul 05 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163084):
WTF?

#### [Patrick Massot (Jul 05 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163128):
Is it because I have pattern matching?

#### [Patrick Massot (Jul 05 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163133):
https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/manifold.lean#L185

#### [Patrick Massot (Jul 05 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163174):
Indeed

#### [Patrick Massot (Jul 05 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163191):
If I remove the matching  and start with 
```lean
  intros h h' h'',
  rcases h with ⟨op_φ_ψ, smooth_φ_ψ⟩,
  rcases h' with ⟨op_ψ_φ, smooth_ψ_φ⟩,
  rcases h'' with ⟨op_ψ_χ, smooth_ψ_χ⟩,
```
Then `easy` works

#### [Patrick Massot (Jul 05 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163245):
Do you understand what happens?

#### [Patrick Massot (Jul 05 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163297):
@**Mario Carneiro**  We really need a hybrid of `intros` and `rcases` that would allow writing `intros ⟨op_φ_ψ, smooth_φ_ψ⟩ ⟨op_ψ_φ, smooth_ψ_φ⟩ ⟨op_ψ_χ, smooth_ψ_χ⟩`

#### [Patrick Massot (Jul 05 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163310):
instead of the four lines of the previous code block

#### [Simon Hudon (Jul 05 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163364):
The situation is that pattern matching and recursion are rooted in the same machinery

#### [Simon Hudon (Jul 05 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163423):
When you pattern match, Lean gives you the opportunity to make a recursive call. It gives you more than you need and once you're done with the proof, it checks whether you introduced recursion / induction and makes sure that it's well-founded

#### [Simon Hudon (Jul 05 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163442):
Tactics don't see the difference between assumptions that are in fact a recursive call and the rest

#### [Patrick Massot (Jul 05 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163950):
Thanks

#### [Patrick Massot (Jul 05 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129163980):
I'll forget about matching and patiently wait for `rintros` to land in mathlib.

#### [Patrick Massot (Jul 05 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129164000):
And I'll go sleeping.

#### [Simon Hudon (Jul 05 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129164449):
You could do something like `clear_rec` that you call after pattern matching

#### [Mario Carneiro (Jul 06 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129183277):
>  I managed to add support for disjunction but it requires tactic.interactive to import logic.basic. I think the creation of tactic.cache would fix that situation. Should I submit that change in a separate PR? (separate from the traversable PR) If you need more time to review the traversable PR, I think that would be a good way to move forward

@**Simon Hudon** I think this is a good idea. Splitting up the different unrelated parts will make it easier to merge things

#### [Simon Hudon (Jul 06 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129183346):
Nice, I hadn't thought of it that way but we'll kill two birds with one stone. I can pull a few more PRs from `traversable`

#### [Simon Hudon (Jul 06 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129183658):
What's your opinion about using lemmas in tactics that require predicates to be decidable? Would you just let it fail if some predicate is not decidable or would you silently use `prop_decidable`?

#### [Mario Carneiro (Jul 06 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129183777):
Depends on the use case. I think `by_cases` will fail, but adding `prop_decidable` as a local instance fixes this, so this seems sufficiently flexible

#### [Simon Hudon (Jul 06 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129183969):
That's straightforward. With `tauto`, `decidable` constraints can come from a lot of different sources and become relevant without obvious reasons

#### [Mario Carneiro (Jul 06 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129184379):
It would be nice if the tactic reports the decidability problem in the error, that way the user can decide what to do about it

#### [Simon Hudon (Jul 06 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129184508):
That's true. Unfortunately, `tauto` can keep going for a while once it has failed to find a `decidable` instance

#### [Simon Hudon (Jul 06 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129184704):
I'm thinking that `tauto!` could add `prop_decidable` as a local instance right from the start. Then when you're not sure why `tauto` failed, you can try that and move on.

#### [Mario Carneiro (Jul 06 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129187322):
> I'll forget about matching and patiently wait for `rintros` to land in mathlib.

Your wish is my command...

#### [Simon Hudon (Jul 06 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129187353):
@**Mario Carneiro** Tag, you're it! https://github.com/leanprover/mathlib/pull/178

#### [Patrick Massot (Jul 06 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129187470):
I love that! My next wish is you answer my Wednesday email :wink:

#### [Patrick Massot (Jul 06 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129187481):
And I'm sure this `rintro` tactic will soon be all over the place.

#### [Simon Hudon (Jul 06 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intersections/near/129187492):
What is this `rintro` thing?

