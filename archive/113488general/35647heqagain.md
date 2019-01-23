---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35647heqagain.html
---

## Stream: [general](index.html)
### Topic: [heq again](35647heqagain.html)

---


{% raw %}
#### [ Reid Barton (Sep 10 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673026):
Hmm, I wasn't expecting this to work.
```lean
lemma types_eq_of_heq : Π {α : Type} (a : α) {β : Type} (b : β) (h : a == b), α = β
| α a _ _ (heq.refl _) := rfl
```

#### [ Kenny Lau (Sep 10 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673064):
why not?

#### [ Kenny Lau (Sep 10 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673078):
casing on `h` makes sure that the types are equal and the arguments are equal

#### [ Reid Barton (Sep 10 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673143):
Mostly because I haven't seen this fact in core or mathlib, so I guess I assumed it was not provable.

#### [ Reid Barton (Sep 10 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673150):
Now I have a followup question about `congr`.

#### [ Reid Barton (Sep 10 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673156):
```lean
import data.set

section   
parameters {F : Type → Type} {α β α' β' : Type} (hα : F α = F α') (hβ : F β = F β')
parameters (f : F α → F β) (f' : F α' → F β') (h : f == f')
include hα hβ h
   
def fns := Σ' X Y : set.range F, X.1 → Y.1
def g : fns := ⟨⟨F α, α, rfl⟩, ⟨F β, β, rfl⟩, f⟩
def g' : fns := ⟨⟨F α', α', rfl⟩, ⟨F β', β', rfl⟩, f'⟩

def e : g = g' :=
begin
  dsimp [g, g'],
  /- ⊢ ⟨⟨F α, _⟩, ⟨⟨F β, _⟩, f⟩⟩ = ⟨⟨F α', _⟩, ⟨⟨F β', _⟩, f'⟩⟩ -/
  /- How to proceed? My solution: -/
  congr' 1, { simp [hα] },
  congr' 1, { rw hα }, { simp [hβ] },
  simp [h],
end
   
end
```

#### [ Kenny Lau (Sep 10 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673185):
are you going to livestream?

#### [ Mario Carneiro (Sep 10 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673186):
`type_eq_of_heq`

#### [ Reid Barton (Sep 10 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673196):
I'm annoyed about this `{ rw hα }` thing. The goal there is
```lean
⊢ (λ (Y : {x // x ∈ set.range F}), F α → Y.val) = λ (Y : {x // x ∈ set.range F}), F α' → Y.val
```
which I think is trying to say that when I do the second `congr'`, the types of the two sides are equal.

#### [ Reid Barton (Sep 10 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673243):
Wow, my grep skills failed

#### [ Reid Barton (Sep 10 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673266):
If I put `{ admit }` there, the rest of the proof seems to go through fine. So couldn't `congr'` deduce that the types are equal after the fact, using `type_eq_of_heq`?

#### [ Reid Barton (Sep 10 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673394):
Here's a dumber example.
```lean
example {α β : Type} (a : α) (b : β) : (a, a) == (b, b) :=
begin
  congr,
end
```
There are four goals, `⊢ α = β` twice and `⊢ a == b` twice. But I can get the former from the latter.

#### [ Reid Barton (Sep 10 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673520):
Or a nicer presentation
```lean
example {α α' β β' : Type} (a : α) (b : β) (a' : α') (b' : β') : (a, b) == (a', b') :=
```

#### [ Kenny Lau (Sep 10 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673525):
```lean
import data.set

section
parameters {F : Type → Type} {α β α' β' : Type} (hα : F α = F α') (hβ : F β = F β')
parameters (f : F α → F β) (f' : F α' → F β') (h : f == f')
include hα hβ h

def fns := Σ' X Y : set.range F, X.1 → Y.1
def g : fns := ⟨⟨F α, α, rfl⟩, ⟨F β, β, rfl⟩, f⟩
def g' : fns := ⟨⟨F α', α', rfl⟩, ⟨F β', β', rfl⟩, f'⟩

def e : g = g' :=
begin
  dsimp only [g, g'],
  congr; try {assumption},
  ext Y, rw hα
end

end
```

#### [ Reid Barton (Sep 10 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673613):
The `ext Y, rw hα` part is still there, though. That's the only part I care about because it seems unnecessary.
In my real use case, I have three of them and they are bigger

#### [ Reid Barton (Sep 10 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673768):
Does `set_option trace.congr_lemma true` do anything?

#### [ Reid Barton (Sep 10 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673872):
Kenny, I was thinking I would try this evening US eastern time today, maybe a bit late for you

#### [ Mario Carneiro (Sep 10 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674237):
That's a pretty messy goal. I would clean it up by hand as follows:
```
begin
  let G := λ A B (f : A → B) h h', (⟨⟨A, h⟩, ⟨B, h'⟩, f⟩ : fns),
  suffices : ∀ {f f' h₁ h₂ h₃ h₄}, f == f' →
    G (F α) (F β) f h₁ h₂ = G (F α') (F β') f' h₃ h₄, exact this h,
  rw [hα, hβ], intros, congr', apply eq_of_heq a
end
```

#### [ Mario Carneiro (Sep 10 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674250):
I would avoid having type equalities and heqs in the hypotheses to begin with

#### [ Mario Carneiro (Sep 10 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674301):
`congr` is clearly dropping the ball here. There are lots of superfluous goals being generated

#### [ Mario Carneiro (Sep 10 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674319):
But usually you don't want to deduce a type equality from a heq; rather you want to assume the type equality and prove a regular equality dependent on it

#### [ Kenny Lau (Sep 10 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674335):
is there any way to prove this goal?

#### [ Kenny Lau (Sep 10 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674338):
```lean
import data.set

section
parameters {F : Type → Type} {α β α' β' : Type} (hα : F α = F α') (hβ : F β = F β')
parameters (f : F α → F β) (f' : F α' → F β') (h : f == f')
include hα hβ h

def fns := Σ' X Y : set.range F, X.1 → Y.1
def g : fns := ⟨⟨F α, α, rfl⟩, ⟨F β, β, rfl⟩, f⟩
def g' : fns := ⟨⟨F α', α', rfl⟩, ⟨F β', β', rfl⟩, f'⟩

set_option pp.proofs true
theorem e : g = g' :=
begin
  fapply psigma.eq,
  { exact subtype.eq hα },
  fapply psigma.eq,
  { /- (eq.rec_on (subtype.eq hα) (g.snd)).fst = (g'.snd).fst -/ }
end

end
```

#### [ Reid Barton (Sep 10 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674402):
Well how about the following modification to `congr`. After each single layer of `congr`, try filling each of the new goals by applying `exact type_eq_of_heq ?m_i` where `?m_i` is the metavariable of each other goal.

#### [ Mario Carneiro (Sep 10 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674429):
That's not what you want though. You will have to deduce those type equalities anyway in order to prove the heq

#### [ Reid Barton (Sep 10 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674434):
But I didn't!

#### [ Reid Barton (Sep 10 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674447):
I happen to have the heq lying around, and where I proved it, the type equalities were obvious

#### [ Mario Carneiro (Sep 10 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674498):
You satisfied the type equality proof by `assumption`

#### [ Reid Barton (Sep 10 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674522):
Which type equality proof?

#### [ Mario Carneiro (Sep 10 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674533):
`hα`

#### [ Mario Carneiro (Sep 10 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674581):
and `hβ` later in the proof

#### [ Reid Barton (Sep 10 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674591):
Right, but then there is an inner proof obligation I have to take care of, the one I solve using `{ rw hα }`

#### [ Reid Barton (Sep 10 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674615):
Let me put up my real code

#### [ Mario Carneiro (Sep 10 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674626):
you have to solve that anyway

#### [ Reid Barton (Sep 10 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674682):
No, it follows from being able to solve the rest of the goals

#### [ Mario Carneiro (Sep 10 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674706):
how?

#### [ Reid Barton (Sep 10 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674714):
By `type_eq_of_heq`. Right?

#### [ Mario Carneiro (Sep 10 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674717):
applied to what?

#### [ Reid Barton (Sep 10 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674730):
Isn't it the same thing as this?
```lean
example {α α' β β' : Type} (a : α) (b : β) (a' : α') (b' : β') (ha : a == a') (hb : b == b') :
  (a, b) == (a', b') :=
begin
  congr, { exact type_eq_of_heq ha }, { exact type_eq_of_heq hb }, { exact ha }, { exact hb }
end
```

#### [ Mario Carneiro (Sep 10 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674845):
sure, but this is an unrealistic goal. Where are you going to get those heqs without a type equality?

#### [ Reid Barton (Sep 10 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674859):
so in my real code it happens here https://gist.github.com/rwbarton/dfb90b2552f09b51798bb52af9948d48#file-filtered-lean-L249

#### [ Reid Barton (Sep 10 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674928):
S is the image of a functor F : I -> C considered as a subgraph, defined here https://gist.github.com/rwbarton/dfb90b2552f09b51798bb52af9948d48#file-filtered-lean-L87

#### [ Mario Carneiro (Sep 10 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675006):
can you MWE the state just before the `rintro`?

#### [ Mario Carneiro (Sep 10 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675033):
or maybe just after

#### [ Reid Barton (Sep 10 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675129):
It should be more or less what I pasted originally.
Note `hg : functor.map F ((⟨i', ⟨j', g⟩⟩.snd).snd) == f`, which came from the definition of `S`

#### [ Reid Barton (Sep 10 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675183):
Corresponding to my original `(h : f == f')`

#### [ Mario Carneiro (Sep 10 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675193):
I want to catch the state before the type equalities enter the context

#### [ Reid Barton (Sep 10 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675269):
Ah, so you mean `hi', hj'`

#### [ Mario Carneiro (Sep 10 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675288):
ideally you should be able to match on `hi', hj', hg` and save all the mess

#### [ Mario Carneiro (Sep 10 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675304):
don't match on `⟨X, i, rfl⟩, ⟨Y, j, rfl⟩`, just do `⟨X, _⟩, ⟨Y, _⟩`

#### [ Reid Barton (Sep 10 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675399):
Hmm, I will try that

#### [ Reid Barton (Sep 10 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675614):
Meanwhile I updated the gist with a version which is not M, but should be a WE

#### [ Reid Barton (Sep 10 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675723):
Oh, there is a trick in `F ijg.1 = X ∧ F ijg.2.1 = Y ∧ ...`. That is not just `X`, but `X.val`

#### [ Reid Barton (Sep 10 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675726):
because of my representation of a subgraph, which I now infinitely regret

#### [ Reid Barton (Sep 10 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675824):
I have a subgraph as (1) a subset of the vertices, (2) for each pair of vertices in that set (as a subtype), a subset of the edges between them

#### [ Mario Carneiro (Sep 10 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675941):
works for me:
```
    rintro ⟨⟨X, _⟩, ⟨Y, _⟩, ⟨f, ⟨i, j, g⟩, ⟨⟩, ⟨⟩, ⟨⟩⟩⟩,
    exact ⟨⟨i, j, g⟩, rfl⟩,
```

#### [ Mario Carneiro (Sep 10 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676015):
using `rfl` instead of `⟨⟩` calls `subst` instead of `cases`, and `subst` is not sufficiently aggressive wrt definitionally unfolding one side to a variable

#### [ Reid Barton (Sep 10 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676023):
Ahh

#### [ Mario Carneiro (Sep 10 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676103):
I would suggest, if you are okay with the added verbosity, that you use an inductive type to define your hom sets instead of ands of eqs and heqs

#### [ Reid Barton (Sep 10 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676111):
I see
```lean
rfl : ⇑F (⟨i', ⟨j', g⟩⟩.fst) = ↑⟨X, b_fst_property⟩,
```

#### [ Mario Carneiro (Sep 10 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676128):
it names the variable `rfl` before substing, I think

#### [ Reid Barton (Sep 10 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676134):
Looks that way.

#### [ Reid Barton (Sep 10 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676219):
that's a whole lot better, thanks!

#### [ Reid Barton (Sep 10 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676236):
You mean, in the definition of S?

#### [ Mario Carneiro (Sep 10 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676240):
yes

#### [ Mario Carneiro (Sep 10 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676274):
it's up to you, you can use tricks like this to match on it either way

#### [ Reid Barton (Sep 10 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676290):
oh, I could replace the whole `λ X Y, {f | ∃ (ijg : Σ (i j : I), i ⟶ j), F ijg.1 = X ∧ F ijg.2.1 = Y ∧ F.map ijg.2.2 == f}` with an inductive type I guess

#### [ Mario Carneiro (Sep 10 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676299):
right

#### [ Mario Carneiro (Sep 10 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676371):
it would give nicer equations, but if this is a one-off it's probably not worth it

#### [ Reid Barton (Sep 10 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676380):
and elsewhere I have similar constructions, like the union of a family of subgraphs

#### [ Reid Barton (Sep 10 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676387):
Yeah, I'm not sure I will need any of these constructions more than once, inside the associated proof

#### [ Reid Barton (Sep 10 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676399):
But a good technique to keep in mind

#### [ Mario Carneiro (Sep 10 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676456):
oh, looks like you don't even need to match on `ijg` in that proof

#### [ Reid Barton (Sep 10 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676522):
Yep

#### [ Reid Barton (Sep 10 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676543):
I think I know what happened here

#### [ Reid Barton (Sep 10 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676558):
I started without the `F ijg.1 = X ∧ F ijg.2.1 = Y ∧ ` part

#### [ Reid Barton (Sep 10 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676605):
in the definition of S. And then I realized that wasn't going to work

#### [ Reid Barton (Sep 10 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676623):
but I think I had already written the `⟨X, i, rfl⟩, ⟨Y, j, rfl⟩` patterns

#### [ Mario Carneiro (Sep 10 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676760):
yeah, of course you can't deduce `X = X'` and `Y = Y'` from `X ⟶ Y = X' ⟶ Y'`

#### [ Mario Carneiro (Sep 10 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676778):
not for function types and definitely not for homsets

#### [ Reid Barton (Sep 10 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676917):
Although it curiously would not even matter for the cardinality estimate I need to do here, because it would blow things up by a factor of less than $$\kappa$$

#### [ Reid Barton (Sep 10 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676941):
But anyways, that's when I started to wonder: would it be better to just define the edges as `(mors : set (Σ X Y, X ⟶ Y))`

#### [ Mario Carneiro (Sep 10 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133677178):
I'm inclined to say no, although possibly you might want `homs` to be defined on all objects, not just those in the subset

#### [ Mario Carneiro (Sep 10 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133677188):
and just require that it be empty outside the subset

#### [ Mario Carneiro (Sep 10 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133677264):
```
structure subgraph (C : Type u) [small_category C] : Type u :=
(objs : set C)
(homs : Π X Y : C, set (X ⟶ Y))
(dom_mem : Π X Y f, f ∈ homs X Y → X ∈ objs)
(cod_mem : Π X Y f, f ∈ homs X Y → Y ∈ objs)
```

#### [ Reid Barton (Sep 10 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133677305):
Right, I would need those last two fields anyways. Just a difference between `set (Σ X Y, X ⟶ Y)` and `Π X Y : C, set (X ⟶ Y)`

#### [ Mario Carneiro (Sep 10 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133677362):
having a big sigma will make things more complicated with heqs and stuff as you've seen

#### [ Reid Barton (Sep 10 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133677367):
Given that some of the things I do are look at the cardinality of the set of edges, and form the union of subgraphs

#### [ Reid Barton (Sep 10 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133677381):
but I guess those are not significantly harder with the Pi approach

#### [ Mario Carneiro (Sep 10 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133677396):
I think `arrows := Σ X Y, X ⟶ Y` is a useful definition in a category though


{% endraw %}
