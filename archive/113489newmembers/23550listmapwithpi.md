---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/23550listmapwithpi.html
---

## [new members](index.html)
### [list.map with pi](23550listmapwithpi.html)

#### [Gavid Liebnich (Nov 09 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/list.map with pi/near/147355746):
Hello. I have an issue using dependent function space in conjunction with `list.map`. Could anyone take a peek?
In the following state:
```lean
α : Type,
g g' : list α,
f : Π (a : α), a ∈ g → α,
h : g = g'
⊢ map (λ (c : {x // x ∈ g}), f (c.val) _) (attach g) = nil
```
I would like to rewrite `g` with `g'`. However, I get "motive is not type correct" error.
I *think* I understand why this is. Given `c.2` is supposed to be `x ∈ g`, I would end up with mismatching types as `attach g'` would lead to `c.2` being `x ∈ g'`.
However, I am not sure how to proceed - I think I need some kind of a congruence that says I can switch `map f l` for `map f' l'` if I can show `f = f'` and `l = l'`, but "modulo types".
You can reconstruct the goal (and the error) with:
```lean
import data.list
open list
variables {α : Type} {g g' : list α} {f : Π(a : α) (h : a ∈ g), α}
def foo := map (λ(c : {x // x ∈ g}), f c.1 c.2) (attach g)
example (h : g = g') : @foo α g f = [] :=
begin
  unfold foo,
  rw h -- motive not type correct
end
```

#### [Mario Carneiro (Nov 09 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/list.map with pi/near/147356172):
Is `g` a variable? If so, `subst g` is probably the easiest thing

#### [Gavid Liebnich (Nov 09 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/list.map with pi/near/147356421):
I am not sure I know what variable means in this context, but `g` is a list computed by a function, so I think it is not. The equivalence `h : g = g'` basically expands `bar x y` to `x :: bar x' y`. I've tried `subst expand_bar`, but the "given expression is not a local constant".

#### [Gavid Liebnich (Nov 09 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/list.map with pi/near/147356591):
Definitely not a variable, come to think of it, `h : g = g'` is just `h : expand_bar a b = a :: expand_bar a' b`. And I don't think I can `subst expand_bar`.

#### [Mario Carneiro (Nov 09 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/list.map with pi/near/147357025):
I think you need to unsimplify your example then. This is generally speaking a complicated problem with nonuniform solutions, I would have to know more about the problem to say how to proceed

#### [Gavid Liebnich (Nov 09 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/list.map with pi/near/147357098):
I will give it a try, thanks. I did a lot of simplifying, may have lost something along the way :).

#### [Patrick Massot (Nov 09 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/list.map with pi/near/147357269):
The `subst` tactic (instead of `rw`) may help you

#### [Floris van Doorn (Nov 10 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/list.map with pi/near/147436293):
I don't know if this works in your actual example, but you could try reverting everything which depends on `g`:
```
example (h : g = g') : @foo α g f = [] :=
begin
  unfold foo,
  revert f,
  rw h,
  intro f
end
```

#### [Floris van Doorn (Nov 10 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/list.map with pi/near/147436358):
Note that this `rw` now also rewrites the type of `f`.

