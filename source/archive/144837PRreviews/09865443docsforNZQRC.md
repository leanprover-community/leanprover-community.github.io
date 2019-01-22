---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/09865443docsforNZQRC.html
---

## [PR reviews](index.html)
### [#443 docs for N -> Z -> Q -> R -> C](09865443docsforNZQRC.html)

#### [Kevin Buzzard (Oct 27 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136607409):
Mathematicians find it frustrating when their goal is "obviously the same" as a hypothesis, except the hypothesis is about integers and the goal is about real numbers. These docs attempt to give some hints about how to deal with this, plus a slightly more in-depth discussion about what is going on for those who are interested. Comments are welcome.

#### [Johan Commelin (Oct 27 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136614223):
I suggested to fix two typos, and had two other minor comments. See my review on Github.

#### [Scott Olson (Oct 27 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136614403):
I was struck by the comment "your goal is `↑x * ↑y = ↑z`, something which you suspect is a statement about real numbers", which reminds me that in HoTT they always write `Path ℝ (↑x * ↑y) ↑z`. We can get goals like `⊢ @eq real x y` with `pp` options, but as soon as you throw in coercions or operator syntax, it's unreadable... I'm dreaming of more laser-focused `pp` options that would just show the types of coercions or equalities in a nice way

#### [Kevin Buzzard (Oct 27 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136615244):
There might be a way of doing it by switching `pp.implicit` on or something

#### [Kevin Buzzard (Oct 27 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136615246):
I didn't think about it too hard

#### [Scott Olson (Oct 27 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136615271):
Unfortunately it doesn't work because `pp.notation` (on by default) hides the implicit arguments of the operators, and setting that to false makes up most of the mess that `pp.all` causes

#### [Kevin Buzzard (Oct 28 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650007):
Aargh. My PR is not quite ready. My plan was to give a recipe so that undergraduate mathematicians had an algorithm to deal with any such "easy in maths" issues they came up with. But I've just found one that does not seem to be covered by what I wrote:

```lean
import data.real.basic

example (q : ℚ) (H : q = 3) : (q : ℝ) = 3 :=
begin
  rw H,
  simp
end

example (q : ℚ) (H : (q : ℝ) = 3) : q = 3 :=
begin
  -- what now?
  sorry  
end
```

The first one is fine. For the second one, I am hoping for a proof which does not require knowing the explicit name of the theorem that says that two rationals are equal iff the corresponding reals are equal. You can see that in the first example I did not need to know the name of any theorem in mathlib; there are 5 choose 2 such theorems and ideally I would like students not to have to know their names explicitly. How do I solve the second goal? I would like to add this to the docs but I don't know myself (in the past I've just found the name of the theorem and applied it directly)

#### [Mario Carneiro (Oct 28 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650021):
There are not 5 choose 2 theorems, there are 5

#### [Kevin Buzzard (Oct 28 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650029):
That sentence does not bode well

#### [Mario Carneiro (Oct 28 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650038):
I think it would help if rather than speaking vaguely about the coercions you just list all of them and their names

#### [Mario Carneiro (Oct 28 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650039):
`nat.cast`, `int.cast`, `rat.cast`, `complex.of_real`, `int.coe_nat`

#### [Mario Carneiro (Oct 28 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650079):
all the names are based on these segments

#### [Kenny Lau (Oct 28 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650087):
```quote
Aargh. My PR is not quite ready.
```
Don't worry, they haven't accepted any PR in 10 days

#### [Mario Carneiro (Oct 28 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650097):
I was looking at them earlier today FYI... I would have merged Kevin's but there were some outstanding fixes

#### [Kevin Buzzard (Oct 28 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650102):
The point of the docs was to show 1st year mathematicians an algorithm for proving everything of this nature which is "trivial in maths". The algorithm currently only relies on the students knowing `rw` and `simp` but if we cannot do this one with these tools then of course I am going to have to tell them about more tools

#### [Mario Carneiro (Oct 28 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650151):
I mean for the section where you talk about the names of the theorems

#### [Kevin Buzzard (Oct 28 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650167):
Mario what I need -- what *they* need -- is an algorithm which generates all 5 choose 2 proofs of `example (a b : X) (H : (a : Y) = b) : a = b` for `X` and `Y` running through NZQRC with `X<Y`

#### [Kevin Buzzard (Oct 28 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650173):
If the algorithm is "here are 5 choose 2 proofs" then so be it

#### [Kevin Buzzard (Oct 28 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650219):
I really want to hide the names of the theorems from the students, because we are well into "trivial in maths" territory here.

#### [Mario Carneiro (Oct 28 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650222):
This is what that `cast` tactic we talked about would be for

#### [Kevin Buzzard (Oct 28 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650227):
And my philosophy is: if it's trivial in maths, make it easy in Lean.

#### [Mario Carneiro (Oct 28 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650288):
If the theorem is literally `a = b` with variables, simp can figure it out

#### [Mario Carneiro (Oct 28 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650295):
the problem is when you have `a + b = c` so that `\u (a + b) = \u c` can simplify in two ways, to `a + b = c` and `\u a + \u b = \u c`

#### [Mario Carneiro (Oct 28 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650310):
You usually want to convert between those last two, but the path is "uphill" part of the way, to the non-simp normal form `\u (a + b) = \u c`

#### [Kevin Buzzard (Oct 28 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650378):
```lean
example (q r : ℚ) (H : (q : ℝ) = 3) : q = 3 :=
begin
  have H2 : (3 : ℝ) = (3 : ℚ),
    simp,
  rw H2 at H,
  revert H,
  simp, --- gaargh dammit
  sorry
end
```

#### [Mario Carneiro (Oct 28 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650432):
and simp chooses one of them kind of at random, leading to "gaargh dammit" moments

#### [Kevin Buzzard (Oct 28 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650433):
I understand how to get from `\u a + \u b = \u c` to `\u (a + b) = \u c` and hopefully I explain that in the docs. The trick which beginners can use is to prove `\u a + \u b = \u (a + b)` using `simp` and then rewrite.

#### [Kevin Buzzard (Oct 28 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650435):
But here I am struggling to do this just using simp and rw

#### [Kevin Buzzard (Oct 28 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650441):
and I would like to put more examples of this in until I never struggle again

#### [Mario Carneiro (Oct 28 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650444):
I know how to achieve it using only the explicit lemma `\u a = \u b <-> a = b`

#### [Kevin Buzzard (Oct 28 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650456):
Invoking `real.of_int_inj` or whatever, magical functions with mysterious and inconsistent names, is exactly what I want to avoid

#### [Kevin Buzzard (Oct 28 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650503):
However if these cannot be avoided then I think they should be explicitly listed in the docs

#### [Kevin Buzzard (Oct 28 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650511):
all 5 choose 2 of them

#### [Mario Carneiro (Oct 28 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650515):
there are not 5 choose 2!

#### [Kevin Buzzard (Oct 28 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650518):
:-)

#### [Kevin Buzzard (Oct 28 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650523):
there are, it's just that you can't tell some of them apart ;-)

#### [Mario Carneiro (Oct 28 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650526):
some of them are the same theorem

#### [Kevin Buzzard (Oct 28 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650528):
not if you fill in the implicit arguments

#### [Mario Carneiro (Oct 28 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650529):
like N -> Q and N -> R

#### [Kevin Buzzard (Oct 28 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650589):
I know I know. What I need is an algorithm which takes 5 choose 2 inputs and spits out an output in each case, and you're observing that the underlying function isn't injective.

#### [Kevin Buzzard (Oct 28 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650651):
```lean
example (q r : ℚ) (H : (q : ℝ) = 3) : q = 3 :=
begin
  have H2 : (3 : ℝ) = (3 : ℚ),
    simp,
  rw H2 at H,
  revert H,
  exact rat.cast_inj.1,
end
```

#### [Kevin Buzzard (Oct 28 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650653):
Mathematician sees : "q = 3 -> q = 3"

#### [Mario Carneiro (Oct 28 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650661):
If it is the "initial" function for N,Z,Q, it's named after the source (because it can't be named after the target, which is generic) and it's called `cast`. The functions `int.coe_nat` and `complex.of_real` are separate for reasons, and they (and other such specialized functions) are usually named by the target. More generally, the rule of thumb is it's named after whatever is introduced last

#### [Kevin Buzzard (Oct 28 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650663):
Dammit why isn't this easier

#### [Kevin Buzzard (Oct 28 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650664):
it's trivial in maths.

#### [Kevin Buzzard (Oct 28 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650665):
Did you say something about a `cast` tactic?

#### [Mario Carneiro (Oct 28 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650704):
a wishlist tactic, yes

#### [Mario Carneiro (Oct 28 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650731):
The strategy for using the `inj` functions is to take the "smaller" field and lift it to the larger one using `inj` (on the goal or the hypothesis, wherever it is). Then `simp` will bring them together

#### [Mario Carneiro (Oct 28 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650780):
does `rat.cast_inj.1 $ by simpa` work for your example?

#### [Kevin Buzzard (Oct 28 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650781):
```lean
import data.complex.basic

example (q r : ℕ) : (q : ℤ) = r → q = r := by simp
example (q r : ℕ) : (q : ℚ) = r → q = r := by simp
example (q r : ℕ) : (q : ℝ) = r → q = r := by simp
example (q r : ℕ) : (q : ℂ) = r → q = r := by simp

example (q r : ℤ) : (q : ℚ) = r → q = r := by simp
example (q r : ℤ) : (q : ℝ) = r → q = r := by simp
example (q r : ℤ) : (q : ℂ) = r → q = r := by simp

example (q r : ℚ) : (q : ℝ) = r → q = r := by simp
example (q r : ℚ) : (q : ℂ) = r → q = r := by simp

example (q r : ℝ) : (q : ℂ) = r → q = r := by simp
```

Lean scores 9/10 on this one

#### [Mario Carneiro (Oct 28 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650826):
like I said, try `q + q = r` and lean will score a lot less

#### [Mario Carneiro (Oct 28 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650827):
which one fails?

#### [Kevin Buzzard (Oct 28 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650828):
First one

#### [Kevin Buzzard (Oct 28 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650831):
In my notes I explain an algorithm for `q + q = r`; I think `\u q + \u q = \u (q + q)` gets solved by `simp` in all ten cases

#### [Mario Carneiro (Oct 28 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650893):
oh, `(@rat.cast_inj ℝ _ _ _ _).1 $ by simpa` works, not so nice

#### [Kevin Buzzard (Oct 28 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650899):
```lean
example (q r : ℕ) : ((q + r) : ℤ) = (q + r : ℕ) := by simp
example (q r : ℕ) : ((q + r) : ℚ) = (q + r : ℕ) := by simp
example (q r : ℕ) : ((q + r) : ℝ) = (q + r : ℕ) := by simp
example (q r : ℕ) : ((q + r) : ℂ) = (q + r : ℕ) := by simp

example (q r : ℤ) : ((q + r) : ℚ) = (q + r : ℤ) := by simp
example (q r : ℤ) : ((q + r) : ℝ) = (q + r : ℤ) := by simp
example (q r : ℤ) : ((q + r) : ℂ) = (q + r : ℤ) := by simp

example (q r : ℚ) : ((q + r) : ℝ) = (q + r : ℚ) := by simp
example (q r : ℚ) : ((q + r) : ℂ) = (q + r : ℚ) := by simp

example (q r : ℝ) : ((q + r) : ℂ) = (q + r : ℝ) := by simp
```
Lean gets 10/10 for this one

#### [Mario Carneiro (Oct 28 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650903):
no, I mean `q + q = r -> q + q = r`

#### [Mario Carneiro (Oct 28 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650951):
`q = 3` is the same kind of problem

#### [Kevin Buzzard (Oct 28 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650953):
I know, but this can be reduced to `\u a = \u b -> a = b` by proving the sublemma which I just proved above, and then rewriting it

#### [Mario Carneiro (Oct 28 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650954):
of course, they are all trivial theorems

#### [Mario Carneiro (Oct 28 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650955):
like literally two applications of lemmas

#### [Mario Carneiro (Oct 28 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650960):
but you don't want to refer to any lemmas, so it is hard

#### [Kevin Buzzard (Oct 28 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650961):
I know!

#### [Kevin Buzzard (Oct 28 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650962):
That's the point of the docs.

#### [Kevin Buzzard (Oct 28 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136650966):
To find out if I have to refer to the lemmas, and to spell out explicitly which lemmas to use, so that beginners ultimately have an algorithm for proving any "trivial in maths" statements of this form

#### [Kevin Buzzard (Oct 28 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651009):
Yesterday I thought I had got it down to 0 lemmas but now I realise there is this one glitch

#### [Mario Carneiro (Oct 28 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651011):
if you want to codify it to this extent, it's better to (prod someone to) write a tactic

#### [Johan Commelin (Oct 28 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651020):
All these things ought to be "cast everything to `complex` and run `ring`".

#### [Mario Carneiro (Oct 28 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651044):
you don't need `ring`, `simp` is enough. But "cast everything to `complex`" is the hard part here

#### [Kevin Buzzard (Oct 28 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651164):
```quote
All these things ought to be "cast everything to `complex` and run `ring`".
```
Octonians, surely?

#### [Mario Carneiro (Oct 28 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651234):
lol, you complain about `nat` subtraction having poor properties and then you cast to a number field which isn't even associative

#### [Kevin Buzzard (Oct 28 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651303):
OK maybe quaternions are better

#### [Kevin Buzzard (Oct 28 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651305):
```lean
example (q : ℕ) : (q : ℤ) = (3 : ℕ) → q = 3 := by simp
example (q : ℕ) : (q : ℚ) = (3 : ℕ) → q = 3 := by simp
example (q : ℕ) : (q : ℝ) = (3 : ℕ) → q = 3 := by simp
example (q : ℕ) : (q : ℂ) = (3 : ℕ) → q = 3 := by simp

example (q : ℤ) : (q : ℚ) = (3 : ℤ) → q = 3 := by simp
example (q : ℤ) : (q : ℝ) = (3 : ℤ) → q = 3 := by simp
example (q : ℤ) : (q : ℂ) = (3 : ℤ) → q = 3 := by simp

example (q : ℚ) : (q : ℝ) = (3 : ℚ) → q = 3 := by simp
example (q : ℚ) : (q : ℂ) = (3 : ℚ) → q = 3 := by simp

example (q : ℝ) : (q : ℂ) = (3 : ℝ) → q = 3 := by simp
```

0/10 for Lean here

#### [Kevin Buzzard (Oct 28 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651313):
and we also learn that someone thinks that Q R C are a different colour to N and Z, I only just noticed this

#### [Kevin Buzzard (Oct 28 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651435):
The reason I am interested in these questions is that they come up in real life and I am being asked them again and again by beginners attempting to do mathematics. Just a simple question such as "prove that the square root of 2 is irrational" is fraught with these difficulties. The numerator of a rational is an int, the denominator is a nat, and getting from `q ^ 2 = 2` to `n ^ 2 = 2 * d ^ 2` (the latter in int) is hard for beginners. And then getting from this to a statement about q not being `sqrt 2`in the reals is hard again. The fact that I've just been teaching this stuff in M1F means that these questions come up, and my docs are an attempt to resolve these issues once and for all. The reason I think this is important is that it's exactly the "trivial in maths, hard in Lean" phenomenon which puts beginners off, and once they're gone, I've lost them.

#### [Kevin Buzzard (Oct 28 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651480):
I realise now however that my docs do not cover all use cases, because I am currently stuck on `example (q : ℚ) (H : (q : ℝ) = 3) : q = 3`.

#### [Mario Carneiro (Oct 28 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651493):
you don't need to convince me that these problems are important, or come up often. But I am apparently more comfortable than you with asking people to use the theorems that are there expressly for the purpose

#### [Kevin Buzzard (Oct 28 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651543):
I am too old to remember a big list of theorems, and my users are too new to know the list, so this is two reasons why I really need to write this list down.

#### [Kevin Buzzard (Oct 28 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651553):
```lean
example (q : ℕ) : (q : ℤ) = (3 : ℕ) → q = 3 := by simp
example (q : ℕ) : (q : ℚ) = (3 : ℕ) → q = 3 := by simp
example (q : ℕ) : (q : ℝ) = (3 : ℕ) → q = 3 := by simp
example (q : ℕ) : (q : ℂ) = (3 : ℕ) → q = 3 := by simp

example (q : ℤ) : (q : ℚ) = (3 : ℤ) → q = 3 := by simp
example (q : ℤ) : (q : ℝ) = (3 : ℤ) → q = 3 := by simp
example (q : ℤ) : (q : ℂ) = (3 : ℤ) → q = 3 := by simp

example (q : ℚ) : (q : ℝ) = (3 : ℚ) → q = 3 := rat.cast_inj.1
example (q : ℚ) : (q : ℂ) = (3 : ℚ) → q = 3 := rat.cast_inj.1

example (q : ℝ) : (q : ℂ) = (3 : ℝ) → q = 3 := by simp
```

Two down, eight to go

#### [Kevin Buzzard (Oct 28 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651559):
[just to be clear, simp never works here]

#### [Kevin Buzzard (Oct 28 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651612):
```lean
example (q : ℕ) : (q : ℤ) = (3 : ℕ) → q = 3 := int.of_nat_inj
example (q : ℕ) : (q : ℚ) = (3 : ℕ) → q = 3 := nat.cast_inj.1
example (q : ℕ) : (q : ℝ) = (3 : ℕ) → q = 3 := nat.cast_inj.1
example (q : ℕ) : (q : ℂ) = (3 : ℕ) → q = 3 := nat.cast_inj.1

example (q : ℤ) : (q : ℚ) = (3 : ℤ) → q = 3 := int.cast_inj.1
example (q : ℤ) : (q : ℝ) = (3 : ℤ) → q = 3 := int.cast_inj.1
example (q : ℤ) : (q : ℂ) = (3 : ℤ) → q = 3 := int.cast_inj.1

example (q : ℚ) : (q : ℝ) = (3 : ℚ) → q = 3 := rat.cast_inj.1
example (q : ℚ) : (q : ℂ) = (3 : ℚ) → q = 3 := rat.cast_inj.1

example (q : ℝ) : (q : ℂ) = (3 : ℝ) → q = 3 := complex.of_real_inj.1
```

#### [Mario Carneiro (Oct 28 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651657):
```lean
example (q : ℕ) (h : (q : ℤ) = (3 : ℕ)) : q = 3 := int.coe_nat_inj'.1 $ by simpa
example (q : ℕ) (h : (q : ℚ) = (3 : ℕ)) : q = 3 := (@nat.cast_inj ℚ _ _ _ _ _).1 $ by simpa
example (q : ℕ) (h : (q : ℝ) = (3 : ℕ)) : q = 3 := (@nat.cast_inj ℝ _ _ _ _ _).1 $ by simpa
example (q : ℕ) (h : (q : ℂ) = (3 : ℕ)) : q = 3 := (@nat.cast_inj ℂ _ _ _ _ _).1 $ by simpa

example (q : ℤ) (h : (q : ℚ) = (3 : ℤ)) : q = 3 := (@int.cast_inj ℚ _ _ _ _ _).1 $ by simpa
example (q : ℤ) (h : (q : ℝ) = (3 : ℤ)) : q = 3 := (@int.cast_inj ℝ _ _ _ _ _).1 $ by simpa
example (q : ℤ) (h : (q : ℂ) = (3 : ℤ)) : q = 3 := (@int.cast_inj ℂ _ _ _ _ _).1 $ by simpa

example (q : ℚ) (h : (q : ℝ) = (3 : ℚ)) : q = 3 := (@rat.cast_inj ℝ _ _ _ _).1 $ by simpa
example (q : ℚ) (h : (q : ℂ) = (3 : ℚ)) : q = 3 := (@rat.cast_inj ℂ _ _ _ _).1 $ by simpa

example (q : ℝ) (h : (q : ℂ) = (3 : ℝ)) : q = 3 := complex.of_real_inj.1 $ by simpa
```
8/10

#### [Mario Carneiro (Oct 28 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651662):
the `rat.cast_inj` ones don't work for some reason

#### [Kevin Buzzard (Oct 28 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651672):
?! :-)

#### [Mario Carneiro (Oct 28 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651732):
lol, `by simpa using h` works

#### [Mario Carneiro (Oct 28 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651813):
```lean
example (q : ℕ) (h : (q : ℤ) = (3 : ℕ)) : q = 3 := int.coe_nat_inj'.1 $ by simpa using h
example (q : ℕ) (h : (q : ℚ) = (3 : ℕ)) : q = 3 := (@nat.cast_inj ℚ _ _ _ _ _).1 $ by simpa using h
example (q : ℕ) (h : (q : ℝ) = (3 : ℕ)) : q = 3 := (@nat.cast_inj ℝ _ _ _ _ _).1 $ by simpa using h
example (q : ℕ) (h : (q : ℂ) = (3 : ℕ)) : q = 3 := (@nat.cast_inj ℂ _ _ _ _ _).1 $ by simpa using h

example (q : ℤ) (h : (q : ℚ) = (3 : ℤ)) : q = 3 := (@int.cast_inj ℚ _ _ _ _ _).1 $ by simpa using h
example (q : ℤ) (h : (q : ℝ) = (3 : ℤ)) : q = 3 := (@int.cast_inj ℝ _ _ _ _ _).1 $ by simpa using h
example (q : ℤ) (h : (q : ℂ) = (3 : ℤ)) : q = 3 := (@int.cast_inj ℂ _ _ _ _ _).1 $ by simpa using h

example (q : ℚ) (h : (q : ℝ) = (3 : ℚ)) : q = 3 := (@rat.cast_inj ℝ _ _ _ _).1 $ by simpa using h
example (q : ℚ) (h : (q : ℂ) = (3 : ℚ)) : q = 3 := (@rat.cast_inj ℂ _ _ _ _).1 $ by simpa using h

example (q : ℝ) (h : (q : ℂ) = (3 : ℝ)) : q = 3 := complex.of_real_inj.1 $ by simpa using h
```
10/10

#### [Kevin Buzzard (Oct 28 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651866):
You still need to know the names of the five theorems though :-(

#### [Mario Carneiro (Oct 28 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651889):
that's probably the best you will get unless you write a tactic that applies these five theorems. (It's not that hard, I'm sure your minions can do it)

#### [Kevin Buzzard (Oct 28 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651891):
I will fix up the docs giving as much of an algorithm as I can.

#### [Kevin Buzzard (Oct 28 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651930):
But I am always looking for challenges for my minions.

#### [Kevin Buzzard (Oct 28 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651933):
What exactly are you envisaging?

#### [Kevin Buzzard (Oct 28 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651937):
How much can one hope for?

#### [Mario Carneiro (Oct 28 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136651947):
look at the type of the equality of the selected hypothesis or the target, if it's real or int or rat you can apply the right theorem by a lookup table

#### [Kevin Buzzard (Oct 28 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136652004):
```lean
example (a : ℕ) (b : ℤ) (c : ℚ) (d : ℝ) (e : ℂ)
  (h : ((((a + b) : ℝ) + (c * d)) : ℂ) + e = 53) :
(a : ℂ) + b + c * d + e = 53 := by cast [h]
```

#### [Kevin Buzzard (Oct 28 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136652005):
Would something like that require Hudon-like powers?

#### [Mario Carneiro (Oct 28 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136652052):
as long as you keep the scope limited it should be fine

#### [Kevin Buzzard (Oct 28 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136652058):
I am trying to get from you a feeling as to what is reasonable here

#### [Kevin Buzzard (Oct 28 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136652060):
so I can give them an accessible challenge

#### [Mario Carneiro (Oct 28 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136652063):
the hudon powers come in when generalizing it to multiple hypotheses, reverting things, evaluating numerals or something

#### [Mario Carneiro (Oct 28 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136652072):
I'm thinking closer to just automating literally those 10 examples

#### [Kevin Buzzard (Oct 28 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136652075):
OK! I guess that is already a challenge as far as I am concerned!

#### [Mario Carneiro (Oct 28 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136652124):
also possibly where the hypothesis and goal are switched

#### [Kevin Buzzard (Oct 28 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136652751):
```lean
example (q r : ℕ) : (q : ℤ) = r → q = r := by simp -- fails
example (q r : ℕ) : (q : ℚ) = r → q = r := by simp
example (q r : ℕ) : (q : ℝ) = r → q = r := by simp
example (q r : ℕ) : (q : ℂ) = r → q = r := by simp

example (q r : ℤ) : (q : ℚ) = r → q = r := by simp
example (q r : ℤ) : (q : ℝ) = r → q = r := by simp
example (q r : ℤ) : (q : ℂ) = r → q = r := by simp

example (q r : ℚ) : (q : ℝ) = r → q = r := by simp
example (q r : ℚ) : (q : ℂ) = r → q = r := by simp

example (q r : ℝ) : (q : ℂ) = r → q = r := by simp

@[simp] theorem should_I_be_a_simp_lemma (q r : ℕ) :
(q : ℤ) = r ↔ q = r := ⟨int.of_nat_inj,λ h, h ▸ rfl⟩

example (q r : ℕ) : (q : ℤ) = r → q = r := by simp -- works
```

Is that a bad simp lemma? Is it already there if I do the right import?

#### [Johan Commelin (Oct 28 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136653290):
@**Keeley Hoek** How would `rewrite_search` fare on these problems?

#### [Keeley Hoek (Oct 28 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136653417):
I suspect `rewrite_search!` (bang) will dispatch them using `simp` accidentally, but I'll give `rewrite_search` a try and see if it gets lost.

#### [Johan Commelin (Oct 28 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136653478):
Well, I don't really mind which version you try... it would be nice if some tactic kills these.

#### [Kevin Buzzard (Oct 28 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136653623):
Here are the 11 examples which `simp` doesn't kill.

```lean
example (q : ℕ) : (q : ℤ) = (3 : ℕ) → q = 3 := int.of_nat_inj
example (q : ℕ) : (q : ℚ) = (3 : ℕ) → q = 3 := nat.cast_inj.1
example (q : ℕ) : (q : ℝ) = (3 : ℕ) → q = 3 := nat.cast_inj.1
example (q : ℕ) : (q : ℂ) = (3 : ℕ) → q = 3 := nat.cast_inj.1

example (q : ℤ) : (q : ℚ) = (3 : ℤ) → q = 3 := int.cast_inj.1
example (q : ℤ) : (q : ℝ) = (3 : ℤ) → q = 3 := int.cast_inj.1
example (q : ℤ) : (q : ℂ) = (3 : ℤ) → q = 3 := int.cast_inj.1

example (q : ℚ) : (q : ℝ) = (3 : ℚ) → q = 3 := rat.cast_inj.1
example (q : ℚ) : (q : ℂ) = (3 : ℚ) → q = 3 := rat.cast_inj.1

example (q : ℝ) : (q : ℂ) = (3 : ℝ) → q = 3 := complex.of_real_inj.1

example (q r : ℕ) : (q : ℤ) = r → q = r := int.of_nat_inj
```

#### [Kevin Buzzard (Oct 28 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136653673):
My understanding is that `simp` knows the right lemma in most cases, but applies things in the wrong order and gets stuck (it simplifies `\u 3` to 3). The iff statement corresponding to`int.of_nat_inj` should perhaps be a simp lemma, and if I've got this right then that kills the last example.

#### [Keeley Hoek (Oct 28 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136654313):
I fed it
````lean
import data.complex.basic
example (a b : ℤ) : ((a + b : ℤ) : ℝ) = a + b := int.cast_add a b
-- set_option trace.simplify.rewrite true
example (a : ℤ) (b : ℕ) (c : ℚ) (d : ℝ) :
(a : ℂ) + b * c - d = (((a + ((b * c) : ℚ) : ℚ) - d) : ℝ) :=
begin
  rw rat.cast_add,
  rw rat.cast_coe_int,
  rw complex.of_real_sub,
  rw complex.of_real_add,
  rw rat.cast_mul,
  rw complex.of_real_mul,
  rw rat.cast_coe_nat,
  rw complex.of_real_int_cast,
  rw complex.of_real_nat_cast,
  rw complex.of_real_rat_cast,
end
````
and it gives back the proof
````
rw complex.of_real_sub,
rw complex.of_real_rat_cast,
rw rat.cast_add,
rw rat.cast_mul,
rw rat.cast_coe_int,
rw rat.cast_coe_nat,
````
or in short form
````
conv_rhs { rw complex.of_real_sub, congr, rw [complex.of_real_rat_cast, rat.cast_add],
           congr, rw rat.cast_coe_int, skip, rw rat.cast_mul, congr, rw rat.cast_coe_nat }
````

#### [Johan Commelin (Oct 28 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136654427):
Ok, I don't understand completely. Did you give it hints, or did it find these proofs all alone?

#### [Keeley Hoek (Oct 28 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136654501):
I had to cheat an tell it "use the coersion bundle of lemmas",
we have a cute little command `suggestion coes` to do this

To get it I just stripped out the body of the `begin...end` block and inserted a call to `rewrite_search {trace_result := tt}` instead
And yeah `rewrite_search!` just cheats

#### [Johan Commelin (Oct 28 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136654571):
Ok, but could we potentially use this as a hammer to kill variants of these lemmas in one line (one word)...

#### [Keeley Hoek (Oct 28 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136654660):
Actually I didn't even need to write `suggestion coes`, I just needed to *create* the coes bundle, which didn't exist until it needed to just now. Rewrite search can detect its getting desperate and searches through its library of things to see if any bundle of things "coersions, category_theory, arithmetic, etc." are applicable and it starts trying the detected most relevant ones. This is still pretty crude though, we want to minimise the amount of handling like this

That's right. I mean, so long as you give it access to `simp` (which it doesn't have without the bang) it is just like a shotgun version of `simp`, which should be at least as strong

#### [Johan Commelin (Oct 28 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136654705):
Cool! @**Kevin Buzzard** What do you think of this?

#### [Kevin Buzzard (Oct 28 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136655787):
I don't really understand what is being said. I generated that long begin end proof with simp. Proving the equalities is not the problem, proving the injectivity of the coercions is the problem

#### [Kenny Lau (Oct 28 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136657206):
https://github.com/leanprover/mathlib/pull/447

#### [Jean Lo (Oct 28 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136665415):
Hi. I'm one of @**Kevin Buzzard**'s minions who's just started learning about Lean. Here's a first attempt at a tactic that obviates the need to remember the names for all the `cast_inj` things by just trying each of them in sequence:

```lean
import data.rat data.real.basic data.complex.basic

open tactic

meta def nzqrc : tactic unit := do
  eh ← intro `h,
  to_expr ```(int.of_nat_inj h) >>= exact <|>
  to_expr ```(nat.cast_inj.1 h) >>= exact <|>
  to_expr ```(int.cast_inj.1 h) >>= exact <|>
  to_expr ```(rat.cast_inj.1 h) >>= exact <|>
  to_expr ```(complex.of_real_inj.1 h) >>= exact <|>
  trace "failed: no matching coercion"

example (q : ℤ) : (q : ℂ) = (3 : ℤ) → q = 3 := by nzqrc
```

I mentioned that I suspect the code could be made a lot tidier, and he suggested that I post it again in this stream. Would be very grateful if I could get some guidance with maybe taking something like this further as a tactic that makes dealing with coercions more straightforward for beginners?

#### [Kevin Buzzard (Oct 28 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136665750):
I guess my dream would be a tactic which takes as input a hypothesis which a mathematician would find indistinguishable from the goal (ie the same modulo coercions) and solves the goal. Is that asking too much?

#### [Kevin Buzzard (Oct 28 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136665790):
I wouldn't have a clue how to start writing it though

#### [Johan Commelin (Oct 28 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136665870):
I think Keeley demonstrated that `rewrite_search!` can do that. So we should just get that tactic into mathlib.

#### [Chris Hughes (Oct 28 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136665925):
Can `rewrite_search` simplify this proof from `data.zmod.quadratic_reciprocity`
```lean
lemma euler_criterion_units {x : units (zmodp p hp)} :
  (∃ y : units (zmodp p hp), y ^ 2 = x) ↔ x ^ (p / 2) = 1 := _

lemma euler_criterion {a : zmodp p hp} (ha : a ≠ 0) :
  (∃ y : zmodp p hp, y ^ 2 = a) ↔ a ^ (p / 2) = 1 :=
⟨λ ⟨y, hy⟩,
  have hy0 : y ≠ 0, from λ h, by simp [h, _root_.zero_pow (succ_pos 1)] at hy; cc,
  by simpa using (units.ext_iff.1 $ (euler_criterion_units hp).1 ⟨units.mk0 _ hy0, show _ = units.mk0 _ ha,
    by rw [units.ext_iff]; simpa⟩),
λ h, let ⟨y, hy⟩ := (euler_criterion_units hp).2 (show units.mk0 _ ha ^ (p / 2) = 1, by simpa [units.ext_iff]) in
  ⟨y, by simpa [units.ext_iff] using hy⟩⟩
```

#### [Chris Hughes (Oct 28 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136665964):
6 lines is outrageously long.

#### [Chris Hughes (Oct 28 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136665992):
And this certainly fits into the category of indistinguishable to most mathematicians.

#### [Keeley Hoek (Oct 29 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136681427):
It cannot Chris, but maybe it is just missing a lemma. If you strip the body of that proof and replace it with a call to `tidy` I get two goals (this is with the suped-up `tidy` of Scott's category theory library though, so mathlib tidy might be different). Do the goals you get look reasonable? I just looked very quickly and couldn't tell if they were nonsense or not.

#### [Kevin Buzzard (Oct 29 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136690806):
@**Johan Commelin** @**Keeley Hoek** @**Jean Lo** if I take a step back and look at the current state of [what I wrote](https://github.com/leanprover-community/mathlib/blob/cast_docs/docs/extras/casts.md), it seems to me that where we are is something like the following:

```lean
import data.complex.basic

example (q : ℚ) (h : (q : ℂ) = 3) : q = 3 := by simp [h] -- fails
example (q : ℚ) (h : q = 3) : (q : ℂ) = 3 := by simp [h] -- works
example (q r : ℚ) : q ^ 2 = r + 7 ↔ (q : ℝ) ^ 2 = r + 7 := by simp -- fails
-- next one fails but
-- attribute [simp] int.of_nat_eq_of_nat_iff
-- fixes is it. Is this a good simp lemma?
example (q r : ℕ) : (q : ℤ) = r → q = r := by simp -- currently fails
example (a : ℕ) (b : ℤ) (c : ℚ) (d : ℝ) (e : ℂ) :
((((a + b) : ℚ) * c : ℝ) : ℂ)= d * e + 12 ↔ ((a : ℂ) + b) * c = d * e + 12 := by simp -- works
```

I think beginners would be rightly confused about the randomness of this. I am dreaming of a failsafe `cast_num` tactic which can replace `simp` here and which would solve every case. I do not know anything about `rewrite_search!` other than the fact that it doesn't seem to be in my mathlib -- sorry -- I've not been following these tactic developments. But this post is supposed to be some sort of indication as to what my ~~minions~~clients would be after.

#### [Chris Hughes (Oct 29 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136726568):
```quote
It cannot Chris, but maybe it is just missing a lemma. If you strip the body of that proof and replace it with a call to `tidy` I get two goals (this is with the suped-up `tidy` of Scott's category theory library though, so mathlib tidy might be different). Do the goals you get look reasonable? I just looked very quickly and couldn't tell if they were nonsense or not.
```
I tried it. The second goal was false, it guessed `1` as a solution for the `exists` statement.

#### [Johan Commelin (Oct 29 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136726817):
But this is not related to the NZQRC casts, right?

#### [Chris Hughes (Oct 29 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136727453):
No

#### [Chris Hughes (Oct 29 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23443%20docs%20for%20N%20-%3E%20Z%20-%3E%20Q%20-%3E%20R%20-%3E%20C/near/136727490):
But actually you might find similar problems with more complicated statements involving things like exists.

