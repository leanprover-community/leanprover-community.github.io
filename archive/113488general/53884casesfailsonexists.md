---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53884casesfailsonexists.html
---

## Stream: [general](index.html)
### Topic: [cases fails on exists](53884casesfailsonexists.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 21 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485520):
Can you explain this error message (it happens when I say `cases hm with aa bb`, but `by_cases number.has_min α with hm` works perfectly fine):
```lean
induction tactic failed, recursor 'Exists.dcases_on' can only eliminate into Prop
state:
α : Type u_1,
_inst_1 : number α,
trvk : triviality_kind,
strk : strictness_kind,
bnd : α,
c : constraint α trvk kupper strk,
ht : ¬is_trivial c,
hs : is_strict c,
hm : ∃ (hm : number.has_min α), number.min hm < get_bound c _
⊢ α

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485620):
You can't destruct an exists directly because it's a (small eliminating) Prop. However, in the special case when it is an exists over a prop, you can use `hm.fst` and `hm.snd` to project out the components

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 21 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485757):
Isn't that the same situation as 
```lean
example : (∃ a:1>2, false) → false :=
begin
  intro h,
  cases h with a b, -- no problem here
  assumption
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485763):
You can use cases on exists to prove a Prop, but not to construct data (something in a type that lives in Type)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485803):
here it's okay because `false : Prop`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485804):
while in the other case `α : Type u_1 != Prop`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485850):
The basic idea is that if you want to use partial functions in your code, you have to write all the actual function calls not dependent on the proof part

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 21 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485851):
Are you pointing to the `α` that is used in the goal?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485852):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485854):
why are you "proving" alpha?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485861):
you should write all the functions first, in term mode, and only enter tactic mode to justify the proof part of your partial function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 21 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485862):
It is supposed to be a function, not a proof.
I find it easier to go into tactic mode.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485904):
You want to be careful about the dependency structure that the tactic creates

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 21 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485948):
For example, here is a function in term mode.
```lean
def has_min : Prop :=
  if ht : is_trivial c then number.has_min α else
  match dirk with
  | klower := is_strict c →
                ¬number.is_dense α ∧
                ∀ hm:number.has_max α, 
                  get_bound c (not_trivial_is_not_ktrv c ht) < number.max hm
  | kupper := ∃ hm : number.has_min α, 
                (is_strict c → 
                  (number.min hm) < (get_bound c (not_trivial_is_not_ktrv c ht)))
  end 
```
Now suppose, `has_min` is true. What is the value of `min`? I have to first check triviality, then direction, then whether or not alpha is dense, then ...
Every one of these gives me a different function that I should use to find minimum value. So I entered tactic mode.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485950):
For example with your if then else function from before:
```
def f (c:check) : nat :=
if h : p then
  f₁ (begin ... end)
else
  f₂ (begin ... end)
```
you should enter tactic mode for the proof part but not while determining which function to call

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125485998):
I already mentioned before that you are making your life harder with this encoding, you really want to encode this in the structure of your inductive types. You would be better served encoding `has_min` as an inductive type as well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125486151):
Have you considered using `roption`? It encodes a pair of a proof and a partial function, which makes it easy to write super dependent partial functions like this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 21 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125486261):
Nope, I have to look into `roption`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125486627):
Why do you use so many decidable propositions instead of bools for your work? Usually the answer is convenience but it's clearly not helping you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 21 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125486992):
Not sure, practice ;) or avoiding coe as much as possible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487285):
What do you think of having the `number` fields like this? I find that using `option` makes the proofs and statements much easier
```
def has_in_between {α} [has_lt α] (x y : α) := ∃ z : α, x < z ∧ z < y

class number (α:Type*) extends decidable_linear_order α :=
[nonempty_decidable : decidable (nonempty α)]
(arbitrary : ∀ [nonempty α], α)
[subsingleton_decidable : decidable (subsingleton α)]
(min : option α)
(max : option α)
(min_prop : ∀ a, a ∈ min ↔ ∀ m:α, a ≤ m)
(max_prop : ∀ a, a ∈ max ↔ ∀ m:α, m ≤ a)

(next : α → option α)
(next_prop : ∀ x y, y ∈ next x ↔ x < y ∧ ∀ z:α, z ≤ x ∨ y ≤ z)
(prev : α → option α)
(prev_prop : ∀ x y, y ∈ next x ↔ x < y ∧ ∀ z:α, z ≤ x ∨ y ≤ z)
(is_dense : bool)
(is_dense_prop : 
    if is_dense then
      ∀ x y : α, x < y → ∃ z : α, x < z ∧ z < y
    else
      (∀ x ∉ max, ∃ y, y ∈ next x) ∧ 
      (∀ x ∉ min, ∃ y, y ∈ prev x))

[has_in_between_decidable : ∀ x y : α, decidable (has_in_between x y)]

(zero   : option α)

(neg₀ : α     → option α)
(add₀ : α → α → option α)
(mul₀ : α → α → option α)
(sub₀ : α → α → option α)
(div₀ : α → α → option α)

(neg₁ : α     → option α)
(add₁ : α → α → option α)
(mul₁ : α → α → option α)
(sub₁ : α → α → option α)
(div₁ : α → α → option α)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 21 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487469):
They used to be like this.
The reason I separated `min` and `has_min` is just for performance of the final **hypothetical** code.
`has_min` is never slower than `min`, but it is quite possible for it to be faster.
For example, 
```lean
def has_inf : Prop := if is_satisfiable c then is_bounded_left  c else number.has_max α
def inf (h: has_inf c) : α :=
  if hsat : is_satisfiable c then 
    let hbl := eq.mp (if_pos hsat) h in
    if ht : is_trivial c  then number.min (hbl (or.inl ht)) else
    if hd : dirk = kupper then number.min (hbl (or.inr hd)) else
    get_bound c (not_trivial_is_not_ktrv c ht)
  else
    number.max (eq.mp (if_neg hsat) h)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487513):
when will knowing `has_inf` make computation of `inf` faster?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487560):
A quick and simple addition to allow for faster implementations of `has_min` is the following extra field:
```
[has_min : decidable min.is_some]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 21 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487566):
I did not say using `has_inf` makes `inf` faster, suppose all I want is `has_inf`. If I use option, I have to call `inf`. But `has_inf` could have been implemented faster.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487609):
or you could do it in two stages with a `bool` function:
```
(has_min : bool) (has_min_prop : has_min = min.is_some)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487614):
that way it won't interfere with the definition of `min` or `inf` or whatever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 21 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487615):
May be we mean different things by `implementation`. I mean non-lean code, more specifically C++. If I did not care about performance, I would never consider C++.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487665):
I care about performance more than most lean users, indeed I'm writing a compiler and we have to think about these things. But the extra hypothesis parameter is not as erasable as it appears at first

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 21 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487708):
Are you talking about `(h: has_inf c)` as a parameter to `inf`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487709):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487714):
How do you intend to relate the lean code you are writing to C++? This affects performance considerations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487721):
Is this code to be `#eval`d? Compiled to C++ and then run? Used only for correctness verification?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nima (Apr 21 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases%20fails%20on%20exists/near/125487859):
But that is for `inf` and not `has_inf`.
Right now I know nothing about automatic code generation in lean. I doubt it does exactly what I wish (not sure what exactly that is either). For example, if I have a constraint, I want it to be mutable. If I define addition of two constraints, there is going to be 5 (I guess) additions, but in lean I will have only one. So mostly manual transformation. That could also be a reason why I am not a fan of `match` in lean. I don't know any formal semantics for c++, so not much into verification/validation. But I was thinking about an interval that support both strict and non-strict constraint in both dynamic and static, and realized that is too much for me to verify on my mind. So it would be nice if I can prove the operations first (on a scratch paper) and then at least be sure about the correct behavior.

