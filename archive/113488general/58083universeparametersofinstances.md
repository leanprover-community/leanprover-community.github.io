---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58083universeparametersofinstances.html
---

## Stream: [general](index.html)
### Topic: [universe parameters of instances](58083universeparametersofinstances.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127507965):
Is this a known issue?
```lean
class {u v} cat (α : Type u) :=
(β : Type v)
(x : β)

section
universe u
-- OK                                                                                                                                                                         
example {α : Type u} [cat α] : cat.x α = cat.x α := rfl
end

section
universe u
variables {α : Type u} [cat α]
-- Fails: "invalid reference to undefined universe level parameter 'u_1'"                                                                                                     
example : cat.x α = cat.x α := rfl
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508011):
It is known in the sense that it is a design that's hard to work with.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508012):
It seems that the elaborator fails to gather the second universe variable of `cat`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508022):
If you absolutely need to use it, you need to specify the universes as `cat.{u v} α`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508024):
It makes it unpleasant to use though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508025):
That makes no difference (except the error message complains about `v` now)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508032):
I think this one is just a bug

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508073):
I don't think so. Can you try `cat.{v u} α` instead?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508077):
why `{v u}`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508082):
```lean
section
universes u v
variables {α : Type u} [cat.{u v} α]
-- Fails: "invalid reference to undefined universe level parameter 'v'"                                                                                                       
example : cat.x α = cat.x α := rfl
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508083):
Sometimes, the order of the universes is weird

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508090):
`{v u}` gives many worse errors

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508093):
I think if we could just, like, `include` the universe parameter `v`, then this would work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508095):
Is the error on the equality?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508096):
The error is located on the word `example`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508130):
You may need `cat.x.{u v} α = cat.x.{u v} α`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508153):
This here works for me:

```
section
universes u v
variables {α : Type u} [cat.{u v} α]
example : cat.x.{u v} α = cat.x α := rfl
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508207):
That does work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508220):
Can you show me an example where using two universes is necessary? Maybe I can show you a way around it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508221):
But, this also works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508223):
```lean
section
universes u v
variables {α : Type u} [cat.{u v} α]
-- OK                                                                                                                                                                         
example : cat.x α = cat.x α ∧ nonempty (punit.{v}) := ⟨rfl, ⟨⟨⟩⟩⟩
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508283):
That makes sense. Every definition and theorem has an implicit list of free universe variables. The type of `example` did not mention `v` which meant that the instance of `cat` it needed was not necessarily parameterized by `v`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508285):
So it really seems that the elaborator just does not understand that it ought to bind the universe variable `v`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508326):
The type of `example` does mention `v` though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508327):
I don't think I would say that it ought to.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508341):
Only the versions that work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508343):
No, all of them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508344):
since they are really `∀ {α : Type u} [_inst_1 : cat.{u v} α], ...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508386):
Consider the other original working version, which did not use `variables`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508394):
Its full inferred type is `ok.{u_1 u_2} : ∀ {α : Type u_1} [_inst_1 : cat.{u_1 u_2} α], cat.x.{u_1 u_2} α = cat.x.{u_1 u_2} α`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508395):
`v` does not appear in it either. It is inferred

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508442):
Since it's not specified, it's found through unification. `v` starts off as a universe meta variable and `cat` and `cat.x` start off with different universe variables, we do instance resolution and then unification and then they are forced to be the same.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508453):
The the example with `variable`, the `cat` instance already has a universe so it's not inferred during elaboration

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508502):
Universe polymorphism is a pretty nasty can of worms. Keep it to a minimum. `ulift` can help you with that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508514):
I have to say I still don't really buy any of this!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508554):
```lean
section
universes u v
variables {α : Type u} [cat.{u v} α] {γ : Type v} (y : γ)
-- OK                                                                                                                                                                         
def foo : cat.x α = cat.x α ∧ nonempty γ := ⟨rfl, ⟨y⟩⟩
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508558):
This is consistent with my explanation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508570):
Think of it as matching universe levels by name.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508627):
FWIW, this is the full error message with the failing version
```lean
kernel failed to type check declaration 'test' this is usually due to a buggy tactic or a bug in the builtin elaborator
elaborated type:
  ∀ {α : Type u} [_inst_1 : cat.{u v} α],
    @eq.{v+1} (@cat.β.{u v} α _inst_1) (@cat.x.{u v} α _inst_1) (@cat.x.{u v} α _inst_1)
elaborated value:
  λ {α : Type u} [_inst_1 : cat.{u v} α], @rfl.{v+1} (@cat.β.{u v} α _inst_1) (@cat.x.{u v} α _inst_1)
nested exception message:
invalid reference to undefined universe level parameter 'v'
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508628):
In `cat.x` we don't what the universes will be so they start off as meta variables. `α` brings in universe `u` and `γ` brings in `v`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508668):
So why doesn't the instance resolution of `cat.x` bring in `v`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508674):
Because its `v` is a local `v` to the class.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508714):
It's using this variable `_inst_1` whose type mentions `v`, and when I make it use the variables `γ` and `y` then it understands that it should bring in `v`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508717):
I just tried:

```
universes u v

class cat (α : Type u) :=
(β : Type v)
(x : β)
```

and that doesn't work either. That's weird

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508727):
Ok, I'm not sure now. Maybe @**Sebastian Ullrich** or @**Gabriel Ebner** can come clear this up

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508833):
I guess it cannot "see" the dependence on the `variable` which was used through instance resolution as easily as it can see a direct reference

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508981):
Or, here is another way to look at it. Intuitively, I expect `variables <bindings>` to prepend `<bindings>` to the parameters of every definition/lemma. Well that's not quite true, I only expect bindings that are used somehow to get prepended.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127508987):
Here lean obviously understands that it needs to include the `cat` instance, since otherwise there would be an error earlier about `cat.x`. But, if I just manually prepend both variables, as in the first example, then it works fine.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127509033):
aha, here is another workaround!
```lean
section
universes u v
variables {α : Type u} [inst : cat α]
include inst
-- OK                                                                                                                                                                         
def ok : cat.x α = cat.x α := rfl
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 03 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127509248):
not very surprising that that works, but certainly a palatable workaround. Actually, this could nicely solve my "upgrading" type class issue too. Just name both instances as variables and then `include` the one you want at any given time and `hide` it when done.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127520290):
Thanks for the interesting discussion here! I've absolutely run into this in my category theory library. Unfortunately, universe issues are a pain. Unavoidably, one needs to be able to discuss "small_category", where objects and morphisms live in the same universe, and "large_category", where objects live in a universe one higher than the morphisms.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127520333):
Rather than develop these in parallel (and deal with the combinatorial explosion of functors and natural transformations going between the worlds), I've settled on the somewhat ugly solution of having a single "category", with

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127520339):
```
abbreviation large_category (C : Type (u+1)) : Type (u+1) := category.{u+1 u} C
abbreviation small_category (C : Type u)     : Type (u+1) := category.{u u} C
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127520354):
If you're only dealing with small or large categories (or even one of each at the same time), everything works nicely, and typeclass inference remains your friend.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127520378):
If you're trying to write library code that covers both cases, it is slightly ugly, and we need to specify universes explicitly and do a certain amount of "including" typeclass instances.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 04 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127520399):
As you might have guessed, `cat` stands for your `category` class.
In my so far limited use, I haven't had any issues just using `category` directly where mathematically reasonable, aside from the issue discussed in this topic, which I now have a workaround for.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127520400):
I have to write:
````
variable {C : Type u₁}
variable [𝒞 : category.{u₁ v₁} C]
variable {D : Type u₂}
variable [𝒟 : category.{u₂ v₂} D]
include 𝒞 𝒟
````

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127520402):
quite often!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 04 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127520406):
Aha, so you already discovered the `include` workaround I guess.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127520411):
(But that said, that's usually as ugly as it gets, and after those includes everything works pretty naturally.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 04 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127559852):
Here's another, admittedly silly workaround for the issue here:
```lean
def {u v} Type₂ : Type (u+1) := Type u
variables {C : Type₂.{u v}} [category.{u v} C]
```
Now the type of `C` mentions `v`, so the elaborator correctly includes `v`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Thang Nguyen (Jun 08 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779348):
Hi, I am new in lean programming. I am attending to Hanoi FABS summer school 2018 and really interested in doing. 
My homework is formalizing the statement of Polignac Conjecture: **For every even number 2n, there are infinitely many pairs of consecutive primes which differ by 2n.**
I have formalized and wonder regarding that: 
```lean
def Polignac :Prop := ∀ n, isEven n → ∀ m, ∃ p q > m, isPrime p ∧ isPrime q ∧ ((p - q) = n ∨ (q - p) =n)
```
I need your help!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 08 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779506):
Can you be a bit more specific? Why do you wonder about that definition? Or more precisely, what is giving you trouble about that definition?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 08 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779510):
It would be easier to actually use n as in the informal statement (and write `2*n` where you want 2n

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 08 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779524):
And the disjunction at the end is unnecessary

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 08 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779645):
Note also that your attempt says nothing about p and q being consecutive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Thang Nguyen (Jun 08 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779806):
I need to define the statement of Polignac Conjecture. And I defined it and dont know that is okay.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Thang Nguyen (Jun 08 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779824):
```quote
Note also that your attempt says nothing about p and q being consecutive
```
so how to fix to p q consecutive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 08 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779871):
What you wrote is not the correct statement, even assuming isEven and isPrime are defined

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 08 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779910):
You'd need to say every number between `p` and `q` is not prime. Using a different definition for that may be best

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 08 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779911):
You could add a condition that no natural number between p and q (p and q excluded) is prime

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 08 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779916):
And you don't need to have a notation for q

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 08 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779926):
You really want `n`, a prime `p` and asserting that `p+2*n` is also prime

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 08 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127779968):
and there is no prime number in between

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Thang Nguyen (Jun 08 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127780320):
That is correct?
```lean 
def Polignac :Prop := ∀ n m: nat, ∃ p : nat, isPrime m → (m = p ∨ m = (p + 2*n))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 08 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127782321):
No, it's not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 08 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127785046):
today I learned about https://en.wikipedia.org/wiki/Sexy_prime

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 08 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127785119):
I learned that when I got married: our age is 6 apart and both of our ages were prime numbers. It's probably partly responsible for my saying yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 08 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127786525):
(23, 29)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 08 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127786669):
(31,37)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 08 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127787334):
Going back to his question, I feel like you would want to define a prime gap counting function, as in wikipedia (the number of prime gaps of size n below x). Then you take the limit as x goes to infinity. Is that a standard way to formalize it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127787405):
Given `k`the size of the gaps, I would write: `\forall n, \ex p, p > n \and is_prime_gap p k`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127787438):
And then you need to express that `p` and `p+k` have a prime gap of size `k` in `is_prime_gap p k : Prop`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 11 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20parameters%20of%20instances/near/127889246):
@**Thang Nguyen**, just a suggestion --- in zulipchat you can set the "topic" name for a conversation, and it helps organise the conversation here a lot! For example, this one could have been "help with a statement about primes".

