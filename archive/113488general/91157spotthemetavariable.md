---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91157spotthemetavariable.html
---

## Stream: [general](index.html)
### Topic: [spot the metavariable](91157spotthemetavariable.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124814424):
```lean
#print false.rec -- protected eliminator false.rec : Π (C : Sort l), false → C
constant oops : false
definition n := false.rec ℕ oops -- the "expected type must not contain metavariables" error
definition m := @false.rec ℕ oops -- typechecks just fine 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124814469):
I am not sure I have seen `foo` and `@foo` behave differently before, in a situation where there are no implicit arguments

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Apr 09 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124823987):
In case you didn't already see it, the metavariable is in the type of the definition:
```lean
def n : _ := ...
def m : _ := ...
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Apr 09 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124824035):
The elaborator does not only take a pre-expression, but also an expected type as argument.  Expected types are important to elaborate many pre-expressions, for example recursor applications or anonymous structure instances.  This is why `foo` works but `bar` doesn't:
```lean
def foo : ℕ × ℕ := ⟨1, 2⟩
def bar := ⟨1, 2⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Apr 09 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124824642):
Elaboration of recursor applications is particularly sensitive to the expected type since the motive is computed by generalizing all occurrences of the major premise in the expected type.  So when we elaborate `nat.rec_on k _ _`, we elaborate the major premise `k` and then replace `k` by a fresh variable in the expected type to get the motive.  If the expected type is `C k (k+1)` for example, then we'd compute the motive `λ x, C x (x+1)`.  In your example, the elaborator just has a metavariable as expected type and cannot replace occurrences of the major premise (in a sensible way) to compute a motive.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Apr 09 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124824743):
Maybe this is already clear, but in elaboration the "expected type" is the type the elaborated expression is supposed to have.  For example, when we elaborate `⟨1, 2⟩ : ℕ × ℕ`, we elaborate the pre-expression `⟨1, 2⟩` with the expected type `ℕ × ℕ`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Apr 09 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124824750):
Fun trick: you can suppress expected type propagation with `: _`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124831500):
I don't understand your answer. In contrast to most `blah.rec` recursors, which have type ` Π {C : blah -> Sort u},...`, `false.rec` has type ` Π (C : Sort u_1), false → C `, so whilst in general I can see the issue and why that generic error shows up, for `false.rec` the information is there. I guess what I am saying is that perhaps the definition `false.rec` seems to have been explicitly manipulated by the system so that the motive is not implicit, but the error seems to indicate that some generic rule for recursors has been applied without noticing that in this case it does not apply. I have given Lean all the information it needs to work out the expected type and it has chosen to ignore it because I didn't put the `@`. That's the point I'm trying to make -- the elaborator, in this case, has all the information it needs, despite no `@`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124831511):
I am trying to figure out how the elaborator works without reading the source code. Am I crazy? Is this not even possible, really? Stuff like " The elaborator does not only take a pre-expression, but also an expected type as argument. " are gold dust to me because I don't see any way of working this stuff out without asking.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124831692):
Another way of saying what I don't understand -- ` false.rec ℕ oops ` and `@false.rec ℕ oops ` carry exactly the same information, but one works in a situation where the other does not, so it looks to me like some code somewhere is incorrectly distinguishing between them based on a "oh, there's an eliminator without an @, we are going to have to do some guesswork" principle which does not apply in this case.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124831834):
I guess a rather more tasteful way of demonstrating this behaviour is `definition  n (oops : false) := false.rec ℕ oops`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Apr 09 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832445):
> the error seems to indicate that some generic rule for recursors has been applied without noticing that in this case it does not apply.

You're completely right. https://github.com/leanprover/lean/blob/8f55ec4c50379c612731ced2424fd3eda0cf69a6/src/frontends/lean/elaborator.cpp#L117-L121
```c++
    if (inductive::is_elim_rule(env, n) ||
        is_aux_recursor(env, n) ||
        is_user_defined_recursor(env, n)) {
        return elaborator_strategy::AsEliminator;
    }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Apr 09 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832656):
>  I have given Lean all the information it needs

The goal of the elaborator is not to fill in missing pieces, it is to create a type-correct expression using the pre-expression as a recipe.  The meaning of `false.rec _ oops` is *not* `` app (app (const `false.rec [level.mvar `a]) [mvar `b]) (local_const `oops ...) ``, it is a *command* to the elaborator, instructing it to (essentially) do an induction on `oops`.  And well, the `induction` tactic can fail even if the goal would be solvable by induction.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832682):
Do you think that I will have to learn some C++ if I want to understand Lean well enough to use it in practice?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Apr 09 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832743):
I don't think it's necessary to know the Lean implementation or even just C++ in order to understand and use Lean.  I think I have a good mental model of how C++ or Scala work, without ever having seen their compilers.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832748):
That's a relief :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Apr 09 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832790):
I think it took me about half a year to have a mental model for the Lean elaborator.  I looked into the C++ code, though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Apr 09 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832798):
Before that, I just added type annotations everywhere until the red squiggles went away.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832800):
My impression is that it's very difficult to get a clear idea of what the elaborator is doing without reading the source.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832838):
Currently I just add type class annotations everywhere until the red squiggles go away.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832849):
I mean, there are general principles, but to get beyond them I think you just have to look at what is actually going on.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832892):
Thanks for your help, by the way!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Apr 09 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832894):
You're welcome.

