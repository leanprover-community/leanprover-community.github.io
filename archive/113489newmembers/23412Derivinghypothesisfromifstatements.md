---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/23412Derivinghypothesisfromifstatements.html
---

## Stream: [new members](index.html)
### Topic: [Deriving hypothesis from if statements](23412Derivinghypothesisfromifstatements.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056007):
Hi, I am currently cleaning up my gaussian elimination proof. At one point I defined the following functions:
```lean
def fin_first {n m} (i : fin (n + m)) {h: i.val < n}: fin (n) :=
⟨i.1, begin apply h end⟩

def fin_second {n m} (i : fin (n + m)) {h: i.val >= n}: fin (m) :=
⟨i.1 - n, begin sorry end⟩

def block_mx {m_down m_up n_left n_right: nat} :
  matrix (fin m_up) (fin n_left) α →
  matrix (fin m_up) (fin n_right) α →
  matrix (fin m_down) (fin n_left) α →
  matrix (fin m_down) (fin n_right) α →
  matrix (fin (m_up + m_down)) (fin (n_left + n_right)) α
| up_left up_right down_left down_right := 
λ i j,
 if i.val < m_up
 then 
    if j.val < n_left
    then
      up_left (fin_first i) (fin_first j)
    else
      up_right (fin_first i) (fin_second j)
  else
   if j.val < n_left
    then
      down_left (fin_second i)  (fin_first j)
    else
      down_right (fin_second i) (fin_second j)
``` app

Whenever I apply fin_first and fin_second, I would like to make the hypothesis "h" available based on the information in the if-condition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056162):
I feel this is a super trivial question, but I did not find a good example googling for it. Can somebody throw me the right keywords / reference?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 02 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056304):
If you write `if h :  j.val < n_left then _ else _` you'll get local hypotheses with the right types in the placeholders.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056328):
```lean
test.lean:25:29: error

don't know how to synthesize placeholder
context:
α : Type,
m_down m_up n_left n_right : ℕ,
block_mx :
  matrix (fin m_up) (fin n_left) α →
  matrix (fin m_up) (fin n_right) α →
  matrix (fin m_down) (fin n_left) α →
  matrix (fin m_down) (fin n_right) α → matrix (fin (m_up + m_down)) (fin (n_left + n_right)) α,
up_left : matrix (fin m_up) (fin n_left) α,
up_right : matrix (fin m_up) (fin n_right) α,
down_left : matrix (fin m_down) (fin n_left) α,
down_right : matrix (fin m_down) (fin n_right) α,
i : fin (m_up + m_down),
j : fin (n_left + n_right),
h : j.val < n_left
⊢ j.val < n_left
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056374):
I seem to be so close.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056407):
I would hope lean picks this from the context. But it does not seem to do so.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056461):
https://leanprover.github.io/theorem_proving_in_lean/type_classes.html?highlight=dite#decidable-propositions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 02 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056479):
You want Lean to fill in those arguments automatically when it finds them in the local context?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 02 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056539):
You can write `def fin_first {n m} (i : fin (n + m)) {h: i.val < n . assumption}: fin (n)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 02 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056555):
(I think that's the right syntax, don't have Lean open right this second to check.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056569):
binders in `def fin_first {n m} (i : fin (n + m)) {h: i.val < n}: fin (n)` are a bit strange, how `h` could be inferred from the explicit arguments?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056585):
I have no idea what I am doing here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056588):
Of course Rob's solution should work in your use case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056601):
I hoped "{" and "}" would create a "free" argument

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056610):
Which would be filled in if available in the local context.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056664):
Rob suggested to use "assumption", right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056695):
This gives:
```lean
test.lean:7:52: error

invalid declaration, '}' expected
test.lean:7:55: error

command expected
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056704):
Will  ook for assumption in the lean doc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 02 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056711):
{ } creates implicit arguments. They're arguments that can be filled in completely from other arguments, basically. Lean won't automatically search your local context for matches, because (1) there could be tons of stuff in the context, and (2) there could be multiple matches there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056784):
I see. How do I tell lean which matches I want? Should I use ! to make the parameters explicit and then provide the ones needed explicitly?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 02 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056795):
Here's the correct syntax for using auto parameters like my suggestion:
```lean
def f (n : ℕ) (h : n > 1 . tactic.assumption) : true := trivial

example (n : ℕ) : true :=
if h : n > 1 then f n else trivial
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 02 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056932):
With auto parameters, you give a tactic that will be executed to fill in that argument. So using `tactic.assumption` with an auto param will try to find something in the context that will work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 02 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057019):
```quote
I see. How do I tell lean which matches I want? Should I use ! to make the parameters explicit and then provide the ones needed explicitly?
```
I'm not sure exactly what you mean. It's usually clear in a signature which arguments are inferrable from others, assuming the declaration is fully applied. The custom is to make as much implicit as you can.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 02 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057088):
There's no ! syntax anymore, that was only in Lean 2. But you can use placeholders `_` to ask the elaborator to fill in explicit arguments.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057250):
Great.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057251):
I got this working.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057301):
I previously used "{}" around the assumption tactic, but I need to use "()"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 02 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057335):
Great! Sorry, I should have checked before I wrote it with {}, heh.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057408):
These seem to be really basic questions, but I have now only a last issue.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057411):
h_j : ¬j.val < n_left
⊢ j.val ≥ n_left

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057416):
Is what I see in the else branch.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057421):
This seems to be an obvious rewrite.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057431):
Unfortunately, I don't understand where I would even insert my tactic to do the rewrite.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 02 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057433):
`le_of_not_gt`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057443):
No you need a lemma here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057446):
Yes, that lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 02 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057473):
Are you using the auto param trick? Because I see that this might complicate things a bit.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057563):
I currently write "up_right (fin_first i) (fin_second j (begin rw of_not_gt at h_j end))"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057567):
```lean
up_right (fin_first i) (fin_second j (begin rw of_not_gt at h_j end))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057621):
Which seems to not type-check even syntactically.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057635):
I feel I mix proofs and normal programs beyond what is reasonable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057762):
Also, as a lemma I seem to need "ge_of_not_lt", but I can fix this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057808):
```lean
meta def tobias : tactic unit :=
`[apply le_of_not_gt,  assumption] <|>  `[assumption]

def f (n : ℕ) (h : n ≤ 1 . tobias) : true := trivial

example (n : ℕ) : true :=
if h : ¬ n > 1 then f n else trivial

example (n : ℕ) : true :=
if h :  n ≤ 1 then f n else trivial
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 02 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057878):
Haha, you beat me to it, I just wrote almost exactly the same thing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057900):
And my daughter tried to help you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057932):
This is very much appreciated!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057944):
The full family working on lean!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057963):
What I understand is that I can only provide tactics at function definition, not at the call-site.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 02 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058030):
Oh, you can certainly provide them at the call site too.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058039):
In this case, I could just change the hypothesis of fin_second to what I want.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058056):
I tried to avoid this, as I felt the hypothesis that I stated is more canonical.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058066):
Cool so how would I add them to the call site?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058097):
I meant my daughter tried to help Rob winning the race

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 02 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058115):
If you make the inequality hypotheses to `fin_first` and `fin_second` explicit arguments, using `(h : i.val < n)`, then you can apply it using `fin_first i (by assumption)`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 02 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058182):
Or `by tobias` in this case.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058314):
More seriously, the basics of implicit arguments goes like this: say you have a lemma (or function) with arguments `(f : a -> b) (hf : continuous f)`. Then having `hf` forces the value of `f`, so you can mark `f` as implicit by changing the declaration to `{f : a -> b} (hf : continuous f)`. This was you can provide only `hf` when applying the lemma and Lean will figure out `f`. In your case Lean had no hope to figure out `h` from other arguments so you need to keep it explicit, or use auto-param like in Rob's solution.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058479):
I see.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058485):
Got it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058505):
I can now successfully forward the hypothesis.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058510):
Thanks again, I learned sth new.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058568):
For completeness, this is how my code looks like:

```lean
import ring_theory.matrix

variables {α : Type} {n m : Type} [fintype n] [fintype m]

local infixl ` *ₘ ` : 70 := matrix.mul

def fin_first {n m} (i : fin (n + m)) (h : i.val < n ): fin (n) :=
⟨i.1, begin apply h end⟩

def fin_second {n m} (i : fin (n + m)) (h: i.val >= n): fin (m) :=
⟨i.1 - n, sorry⟩

def block_mx {m_down m_up n_left n_right: nat} :
  matrix (fin m_up) (fin n_left) α →
  matrix (fin m_up) (fin n_right) α →
  matrix (fin m_down) (fin n_left) α →
  matrix (fin m_down) (fin n_right) α →
  matrix (fin (m_up + m_down)) (fin (n_left + n_right)) α
| up_left up_right down_left down_right := 
λ i j,
 if h_i: i.val < m_up
 then 
    if h_j: j.val < n_left
    then
      up_left (fin_first i (by assumption)) (fin_first j (by assumption))
    else
      up_right (fin_first i (by assumption)) (fin_second j (by apply le_of_not_gt; assumption))
  else
   if h_j: j.val < n_left
    then
      down_left (fin_second i (by apply le_of_not_gt; assumption))  (fin_first j (by assumption))
    else
      down_right (fin_second i (by apply le_of_not_gt; assumption)) (fin_second j (by apply le_of_not_gt; assumption))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 02 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058597):
It's not that common to use auto params, but this is actually a pretty good application. `linarith` would be a reasonable auto param too if it handled negations of inequalities.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058621):
I can feel the approximate SMT solver temptation here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058629):
:D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058649):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/linarith.20.26.20nat/near/134919571

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058650):
I certainly would like to explore more powerful linarithmetic tactics here. But this is a separate discussion.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 02 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058720):
I know, we have a solver for full Presburger arithmetic based on dual simplex. Eventually, this is what I would like to understand if we can make it work in lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 02 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135061274):
```quote
I can feel the approximate SMT solver temptation here
```
https://github.com/leanprover/mathlib/pull/384

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 03 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135087439):
Amazing. This got even merged already. Will try to use it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 03 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135087599):
I fact, i tried to use it already and it did not work. Thought I need to dig deeper, but then I found this in the tactic description:  "In particular, it will not work on nat."

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 03 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135087622):
Seems that's a problem in my case. Any reason why it would not work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 03 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135089959):
Oops, I guess the description is outdated. It will work on `nat`, but it isn't complete (it's just doing Fourier Motzkin elimination). It also doesn't know about nat subtraction, which could be a problem in your case.

