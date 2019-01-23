---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/22790powltpowofltgolf.html
---

## Stream: [maths](index.html)
### Topic: [pow_lt_pow_of_lt golf](22790powltpowofltgolf.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147671439):
```lean
variable (x : ℝ) -- or [linear_ordered_field]
theorem pow_lt_pow_of_lt {i j : ℕ} : x > 1 → i < j → x^i < x^j := sorry
```
Is this in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147671985):
all the other versions of this are in `group_power.lean`, but it looks like this one was missed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147671989):
`nat.pow_lt_pow_of_lt_right : ∀ {x : ℕ}, x > 1 → ∀ {i j : ℕ}, i < j → x ^ i < x ^ j`

This should be a theorem about partially ordered semirings or something, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147672028):
linear_ordered_semiring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147672039):
because we don't have partially ordered semirings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147672170):
I spotted this hole this time last year, when I didn't understand the purpose of the mathlib library. At the time, I just figured this was the sort of thing you had to prove yourself, because I had no concept of what "should be there already" (so I proved it in the case I needed it). I understand this concept much better now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147672449):
here's my proof:
```lean
theorem pow_lt_pow {a : α} {n m : ℕ} (ha : 1 < a) (h : n < m) : a ^ n < a ^ m :=
lt_of_lt_of_le
  ((lt_mul_iff_one_lt_left (pow_pos (lt_trans zero_lt_one ha) _)).2 ha)
  (pow_le_pow (le_of_lt ha) h)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147672553):
I'm doing all my own example sheet questions again after last year's attempts. Some of the code I wrote a year ago was absolutely terrible.

Here's the library I wrote this year, to do a question on my problem sheet about n'th roots (n a positive integer)

https://github.com/ImperialCollegeLondon/M1F_example_sheets/blob/master/src/xenalib/real_nth_root.lean

Any stylistic comments or anything would be welcome. I only care about the reals but really that's for stylistic reasons -- I am trying to write a library with a lot of tactic mode proofs so maths students can follow them more easily, and I wanted to make it as simple as possible. Maybe some of this stuff is in mathlib but I understand my own proofs better -- I find them much more readable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147672666):
My proof differs from yours in the proof strategy, which is most of why it is shorter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147672690):
`lt_of_pow_lt` also has a very short proof using `pow_le_pow`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147672716):
The lesson is "use lemmas"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147672825):
And I don't just mean use theorems that have already been proven, I mean arrange the proofs of similar facts to make the best use of commonality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147673012):
your assumptions to `lt_of_pow_lt` are also stronger than they need to be - it's nice when you can learn this by attempting the proof itself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147673104):
`nth_root_unique` is reducible in the sense that it has an equality hypothesis - I would prove a lemma which doesn't have that hypothesis first

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147673417):
it also factors into `x ^ n = y ^ n -> x = y`, which should also be in `group_power` in some generality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147676410):
```quote
here's my proof:
```lean
theorem pow_lt_pow {a : α} {n m : ℕ} (ha : 1 < a) (h : n < m) : a ^ n < a ^ m :=
lt_of_lt_of_le
  ((lt_mul_iff_one_lt_left (pow_pos (lt_trans zero_lt_one ha) _)).2 ha)
  (pow_le_pow (le_of_lt ha) h)
```
```
 `pow_le_pow (le_of_lt ha) h` is a dirty trick, isn't it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147676673):
So the reason I have noticed that `pow_le_pow` trick is because I manually completely unfolded your proof:

```lean
theorem pow_lt_pow' {a : α} {n m : ℕ} (ha : 1 < a) (h : n < m) : a ^ n < a ^ m :=
begin
  apply lt_of_lt_of_le,
  { exact ((lt_mul_iff_one_lt_left (pow_pos (lt_trans zero_lt_one ha) _)).2 ha)},
  exact (pow_le_pow (le_of_lt ha) h)
end

theorem pow_lt_pow'' {a : α} {n m : ℕ} (ha : 1 < a) (h : n < m) : a ^ n < a ^ m :=
begin
  apply lt_of_lt_of_le,
  { refine (lt_mul_iff_one_lt_left _).2 ha,
    refine pow_pos _ _,
    -- got it
    exact lt_trans zero_lt_one ha
  },
  { refine pow_le_pow _ h, -- dirty trick?
    exact le_of_lt ha
  }
end
```

into a form which I can actually *read*. Could there be some code which helps me do this unravelling? It is so much easier for me to inspect nodes of the tree when in tactic mode. @**Simon Hudon** can code do this? Break down some simple class of term mode functions into a tactic proof?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147677006):
`explode` does this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147677009):
Even after this breaking-down I still lose information. For example after that first `lt_of_lt_of_le` -- when I do it in tactic mode I get an extra metavariable goal which Lean has solved in the term mode proof but has not solved in the tactic mode proof. I just want to inspect the metavariable-free goal which is actually proved at each function application I think. How does one do this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147677072):
How do I run `explode`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147677126):
found it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147677334):
ooh, `explode` actually works pretty well on that proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147677383):
Quick, we need an emoji

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147677426):
hey `#explode` is exactly the answer to my question!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147677441):
:grinning:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147677664):
```lean
import tactic.explode
import algebra.group_power

variables {α : Type*} [linear_ordered_semiring α]
theorem pow_lt_pow {a : α} {n m : ℕ} (ha : 1 < a) (h : n < m) : a ^ n < a ^ m :=
lt_of_lt_of_le
  ((lt_mul_iff_one_lt_left (pow_pos (lt_trans zero_lt_one ha) _)).2 ha)
  (pow_le_pow (le_of_lt ha) h)

#explode pow_lt_pow
```
MWE. Say kids! Understand Mario's proofs in seconds with `#explode`! Cool name, cool tactic.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147678779):
```lean
variables {α : Type*} [linear_ordered_semiring α]
theorem pow_lt_pow {a : α} {n m : ℕ} (ha : 1 < a) (h : n < m) : a ^ n < a ^ m :=
lt_of_lt_of_le
  ( iff.mpr 
      ( lt_mul_iff_one_lt_left $ 
        pow_pos 
          ( lt_trans 
              zero_lt_one 
              ha
          ) 
          _
      )
      ha
  )
  ( pow_le_pow 
      ( le_of_lt $
        ha
      ) 
      h
  )
```

Here is another way of taking your proof apart Mario. I have tried to have some sort of a system when unravelling. Is there some sort of name for a form like this? Again I feel like I applied an algorithm. I used $ for functions of one variable and indented for two or more.

How do I tell which term fills the underscore in that proof, by the way? What's the easiest way?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 14 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147678945):
I discovered recently if you replace a `_` by a hole `{! !}` then Lean will give you an error saying there's only one way to fill the hole and tell you what it should be

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 14 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147678962):
I was just about to say that ^

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 14 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147678971):
In this case it's `n`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147679302):
```lean
theorem pow_lt_pow' {a : α} {n m : ℕ} (ha : 1 < a) (h : n < m) :
a ^ n < a ^ m :=
lt_of_lt_of_le -- 14
  ( iff.mpr -- 11 
      ( lt_mul_iff_one_lt_left $ -- 10
        pow_pos -- 9 -- takes two inputs
          ( lt_trans -- 8
              zero_lt_one -- 7
              ha -- 5
          ) 
          _ -- gaargh explode doesn't tell me
      )
      ha -- 5
  )
  ( pow_le_pow -- 13
      ( le_of_lt $ -- 12
        ha -- 5
      ) 
      h -- 6
  )

```

I can't immediately see how to fill in that hole using the output of `#explode` though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147679309):
Funky numbering by the way.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 14 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147679900):
This is post-hoc and probably not immediate enough, but first note that the underscore is the second argument to `pow_pos` (easy to see right away with the bracket colorizer extension), and then compare with the corresponding line of `#explode`, which says `0 < a ^ n`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147679928):
Maybe this indentation is better:
```lean
import tactic.explode
import algebra.group_power

variables {α : Type*} [linear_ordered_semiring α]
theorem pow_lt_pow' {a : α} {n m : ℕ} (ha : 1 < a) (h : n < m) :
a ^ n < a ^ m :=
lt_of_lt_of_le -- 14
  ( iff.mpr -- 11 
      ( lt_mul_iff_one_lt_left  -- 10
        ( pow_pos -- 9 -- takes two inputs
          ( lt_trans -- 8
              zero_lt_one -- 7
            ha -- 5
          ) 
        _ -- gaargh explode doesn't tell me
        )
      )
    ha -- 5
  )
  ( pow_le_pow -- 13
      ( le_of_lt -- 12
        ha -- 5
      ) 
    h -- 6
  )

#explode pow_lt_pow'
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147679979):
```lean
import tactic.explode
import algebra.group_power

theorem pow_lt_pow'
{α : Type*} -- 0
[linear_ordered_semiring α] -- 1
{a : α} -- 2
{n m : ℕ} -- 3,4
(ha : 1 < a) -- 5
(h : n < m) : -- 6
a ^ n < a ^ m := -- proof starts
lt_of_lt_of_le -- 14
  ( iff.mpr -- 11 
      ( lt_mul_iff_one_lt_left  -- 10
        ( pow_pos -- 9
          ( lt_trans -- 8
              zero_lt_one -- 7
            ha) -- 5 
        _)) -- gaargh explode doesn't tell me
    ha) -- 5
  ( pow_le_pow -- 13
      ( le_of_lt -- 12
        ha) -- 5
    h) -- 6

#explode pow_lt_pow'
```
explode covers basically every other line of code

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680151):
```lean
#explode zmodp.quadratic_reciprocity
-- (deterministic) timeout
```
boo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 14 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680230):
Hmm, so the line in the output of `#explode` corresponding to `pow_pos` is this:
```
9 │8    │ pow_pos                │ 0 < a ^ n
```
Why doesn't the second column read `8,3` (`3` is the line corresponding to `n : nat`)? It's the same whether I put in `n` or `_`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680270):
Non-propositional arguments are automatically suppressed, because they would otherwise dominate the output and they are inferrable from the (fully elaborated) types in the right column

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jeremy Avigad (Nov 14 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680342):
Wow, `explode` is really nice. It is great for teaching. I just tried
```
theorem foo (A B C : Prop) : (A → B → C) → (A ∧ B → C) :=
λ h hab, and.elim hab (λ ha hb, h ha hb)

#explode foo
```
It made me realize that the proof can be shortened:
```
theorem foo' (A B C : Prop) : (A → B → C) → (A ∧ B → C) :=
λ h hab, and.elim hab h
```
The tactic doesn't behave well with `have`, though.
```
theorem bar  (A B C : Prop) : A ∧ (B ∨ C) → (A ∧ B) ∨ (A ∧ C) :=
assume h : A ∧ (B ∨ C),
have h₁ : A, from and.left h,
have h₂ : B ∨ C, from and.right h,
or.elim h₂
  (assume h₃ : B,
    or.inl (and.intro h₁ h₃))
  (assume h₃ : C,
    or.inr (and.intro h₁ h₃))

#explore bar
```
@**Mario Carneiro** Would it be hard to handle `have` nicely in the tactic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680687):
hm, it's `explode` not `explore` but that is also an interesting name

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jeremy Avigad (Nov 14 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680738):
Oops, sorry, I forgot to cut-and-paste that part and added it manually. You are right, it is also a good name.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680791):
`have` should be handled well since it will translate to a proof line that is referred to twice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680818):
what does it look like now? (on my phone)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680925):
indeed it is best suited to the basic dtt proofs used in intro logic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680929):
In general, I think I'd rather read the output from the bottom up when trying to figure out what you're doing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680940):
yes absolutely

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680953):
so...it's upside-down?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680979):
well no, it is meant to be read bottom up

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147680988):
but it follows the usual proof order

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147681053):
it is a fitch style proof display

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147681070):
Thanks a lot for alerting me to it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 14 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147681091):
`#explode bar` looks like this now:
```
bar : ∀ (A B C : Prop), A ∧ (B ∨ C) → A ∧ B ∨ A ∧ C
0│   │ A                                                                                                                     ├ Prop
1│   │ B                                                                                                                     ├ Prop
2│   │ C                                                                                                                     ├ Prop
3│   │ h                                                                                                                     ├ A ∧ (B ∨ C)
4│   │ λ (h₁ : A),
  have h₂ : B ∨ C, from h.right,
  or.elim h₂ (λ (h₃ : B), or.inl ⟨h₁, h₃⟩) (λ (h₃ : C), or.inr ⟨h₁, h₃⟩) │ A → A ∧ B ∨ A ∧ C
5│3  │ and.left                                                                                                              │ A
6│4,5│ ∀E                                                                                                                    │ A ∧ B ∨ A ∧ C
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pow_lt_pow_of_lt%20golf/near/147681164):
also pp.beta helps sometimes

