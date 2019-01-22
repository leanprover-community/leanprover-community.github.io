---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/42973moreintnatmoansandgolfplea.html
---

## [maths](index.html)
### [more int nat moans and golf plea](42973moreintnatmoansandgolfplea.html)

#### [Kevin Buzzard (Sep 28 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134808309):
```lean
example (x y : ℤ) (h1 : nat.coprime (int.nat_abs x) (int.nat_abs y)) (h2 : x ^ 2 + 3 * y ^ 2 = 4) : 
(x = 1 ∨ x = -1) ∧ (y = 1 ∨ y = -1) := 
```

Sent to me by @**Clara List**  . The mathematician's proof: "h2 trivially implies |x|<=2 and |y|<=1; now check all cases". This line of reasoning should be feasible in Lean, right? How does one do it?

#### [Kevin Buzzard (Sep 28 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134808379):
I am embarrassed to post my solution. I decided it might be easier to convert everything to nat, but the killer `dec_trivial` line didn't work anyway:

```lean
import algebra.group_power

example (x y : ℤ) (h1 : nat.coprime (int.nat_abs x) (int.nat_abs y)) (h2 : x ^ 2 + 3 * y ^ 2 = 4) : 
(x = 1 ∨ x = -1) ∧ (y = 1 ∨ y = -1) := 
begin
  let x0 := int.nat_abs x,
  let y0 := int.nat_abs y,
  -- now effortfully change to a question about nats
  have Hx : ↑(x0 * x0) = x * x := int.nat_abs_mul_self,
  have Hy : ↑(y0 * y0) = y * y := int.nat_abs_mul_self,
  change x * (x * 1) + 3 * (y * (y * 1)) = 4 at h2,
  rw [mul_one,mul_one] at h2,
  rw [←Hx, ←Hy] at h2,
  change ↑(x0 * x0) + ((3 : ℕ) : ℤ) * ↑(y0 * y0) = (4 : ℕ) at h2,
  rw [←int.coe_nat_mul, ←int.coe_nat_add, int.coe_nat_eq_coe_nat_iff] at h2,
  -- finally got h2 : x0 * x0 + 3 * (y0 * y0) = 4
  -- but mathematicians do not want to waste their time with the last 4 lines
  -- and need training before they can even construct them. What am I missing?

  -- now change the goal in the same way
  suffices : x0 = 1 ∧ y0 = 1,
    split,
    { have H : x = ↑x0 ∨ x = -↑x0 := int.nat_abs_eq x,
      rw this.1 at H,
      exact H },
    { have H : y = ↑y0 ∨ y = -↑y0 := int.nat_abs_eq y,
      rw this.2 at H,
      exact H },

  -- It's now a question about nats. I regret doing all that.
  clear Hx Hy,

  have Hx0 : x0 * x0 ≤ 2 * 2,
    show _ ≤ 4,
    rw ←h2,
    exact nat.le_add_right (x0 * x0) (3 * (y0 * y0)),
  have Hy0 : y0 * y0 ≤ 1 * 1,
    suffices : 3 * (y0 * y0) ≤ 4,
      rwa [mul_comm, ←nat.le_div_iff_mul_le] at this, exact dec_trivial,
    rw ←h2,
    apply nat.le_add_left,
  rw ←nat.mul_self_le_mul_self_iff at Hx0,
  rw ←nat.mul_self_le_mul_self_iff at Hy0,
  have H : nat.coprime x0 y0 := h1,
  revert H,
  revert h2,
  revert Hx0,
  revert Hy0,
  -- goal now
  -- ⊢ y0 ≤ 1 → x0 ≤ 2 → x0 * x0 + 3 * (y0 * y0) = 4 → nat.coprime x0 y0 → x0 = 1 ∧ y0 = 1
  exact dec_trivial, -- AARGH! Fails!
  sorry
end
```

#### [Kevin Buzzard (Sep 28 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134808476):
That is pretty horrible and it didn't work either. (1) how to get `dec_trivial` to work and (2) can it work with ints? I guess we want `(x : int) ^ 2 <= N -> int.nat_abs x <= sqrt N` or `x ^ 2 <= N -> - sqrt N <= x and x <= sqrt N` or something. But will this be enough for dec_trivial? Are these in mathlib somewhere? Of course there will be the usual kerfuffle coming from the fact that N is an int instead of a nat (see other nat int thread where I propose a goofy typeclass solution to this)

#### [Kevin Buzzard (Sep 28 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134809743):
`example (n : ℕ) : n ≤ 0 → n = 0 := dec_trivial -- fails`. What modification makes this work? I'm sure I've seen people get `dec_trivial` to check a finite set of nats before

#### [Mario Carneiro (Sep 28 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134809799):
revert `n`

#### [Kevin Buzzard (Sep 28 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134809887):
gaargh it's still not over

#### [Kevin Buzzard (Sep 28 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134809949):
```lean
example (x : ℤ) (h : int.nat_abs x ≤ 0) : int.nat_abs x = 0 :=
begin
  let n := int.nat_abs x,
  change n ≤ 0 at h,
  show n = 0,
  revert h,
  revert n,
  -- ⊢ let n : ℕ := int.nat_abs x in n ≤ 0 → n = 0
  exact dec_trivial -- fails
end
```

#### [Kevin Buzzard (Sep 28 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134809967):
I could fix this with `generalize` instead of `let` but in my actual use case there are 20 lines of manipulating `n` and `x` before I want to apply `exact dec_trivial`. I will work on the `generalize` trick though.

#### [Kevin Buzzard (Sep 28 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134810341):
Oh -- here's the problem. OK I'm stuck again :-( 

```lean
example : ∀ (n : ℕ), n ≤ 0 → n = 0 := dec_trivial -- type class inference fails
-- ⊢ decidable (∀ (n : ℕ), n ≤ 0 → n = 0)
```
Oh -- I can fix this with a random import :-/

#### [Kevin Buzzard (Sep 28 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134810537):
Oh, nope, still can't do it. I think I do need @**Chris Hughes** now.

```lean
import algebra.group_power

example : ∀ (x1 y1 : ℕ), y1 ≤ 1 → x1 ≤ 2 → x1 * x1 + 3 * (y1 * y1) = 4
  → nat.coprime x1 y1 → x1 = 1 ∧ y1 = 1 := dec_trivial
/-
failed to synthesize type class instance for
⊢ decidable
    (∀ (x1 y1 : ℕ),
       y1 ≤ 1 → x1 ≤ 2 → x1 * x1 + 3 * (y1 * y1) = 4 → nat.coprime x1 y1 → x1 = 1 ∧ y1 = 1)
-/
```

How do I begin to figure out what is not decidable here?

#### [Kevin Buzzard (Sep 28 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134810830):
```lean
example : ∀ (y1 : ℕ), y1 ≤ 1 → ∀ (x1 : ℕ), x1 ≤ 2 → x1 * x1 + 3 * (y1 * y1) = 4
  → nat.coprime x1 y1 → x1 = 1 ∧ y1 = 1 := dec_trivial
```
:grinning:

#### [Kevin Buzzard (Sep 28 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134811186):
```lean
import algebra.group_power

example (x y : ℤ) (h1 : nat.coprime (int.nat_abs x) (int.nat_abs y)) (h2 : x ^ 2 + 3 * y ^ 2 = 4) : 
(x = 1 ∨ x = -1) ∧ (y = 1 ∨ y = -1) :=
begin
  let x0 := int.nat_abs x,
  let y0 := int.nat_abs y,
  -- now effortfully change to a question about nats
  have Hx : ↑(x0 * x0) = x * x := int.nat_abs_mul_self,
  have Hy : ↑(y0 * y0) = y * y := int.nat_abs_mul_self,
  change x * (x * 1) + 3 * (y * (y * 1)) = 4 at h2,
  rw [mul_one,mul_one] at h2,
  rw [←Hx, ←Hy] at h2,
  change ↑(x0 * x0) + ((3 : ℕ) : ℤ) * ↑(y0 * y0) = (4 : ℕ) at h2,
  rw [←int.coe_nat_mul, ←int.coe_nat_add, int.coe_nat_eq_coe_nat_iff] at h2,
  -- finally got h2 : x0 * x0 + 3 * (y0 * y0) = 4
  -- but mathematicians do not want to waste their time with the last 4 lines
  -- and need training before they can even construct them. What am I missing?

  -- now change the goal in the same way
  suffices : x0 = 1 ∧ y0 = 1,
    split,
    { have H : x = ↑x0 ∨ x = -↑x0 := int.nat_abs_eq x,
      rw this.1 at H,
      exact H },
    { have H : y = ↑y0 ∨ y = -↑y0 := int.nat_abs_eq y,
      rw this.2 at H,
      exact H },

  -- now a question about nats. I regret doing all that.
  clear Hx Hy,

  have Hx0 : x0 * x0 ≤ 2 * 2,
    show _ ≤ 4,
    rw ←h2,
    exact nat.le_add_right (x0 * x0) (3 * (y0 * y0)),
  have Hy0 : y0 * y0 ≤ 1 * 1,
    suffices : 3 * (y0 * y0) ≤ 4,
      rwa [mul_comm, ←nat.le_div_iff_mul_le] at this, exact dec_trivial,
    rw ←h2,
    apply nat.le_add_left,
  rw ←nat.mul_self_le_mul_self_iff at Hx0,
  rw ←nat.mul_self_le_mul_self_iff at Hy0,
  have H : nat.coprime x0 y0 := h1,
  revert H,
  revert h2,
  revert Hy0,
  generalize : y0 = y1,
  revert y1,
  revert Hx0,
  generalize : x0 = x1,
  revert x1,
  exact dec_trivial,
end
```

Those reverts and generalizes near the end have to be done in pretty much exactly the right order :-)

#### [Kevin Buzzard (Sep 28 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134812553):
OK here is my challenge. This is a concrete example of the sort of thing which my undergraduate mathematicians are reading in their lecture notes and are finding very hard to put into Lean. The following result is extremely easy for a mathematician and I have supplied a 4-line pseudocode proof. How many lines does take an expert Leaner? I would very much like to get this answer down to 4. Even eight lines would be fine at this point -- between each line of code corresponding to the pseudocode it would be fine to have a`show` or something, or `suffices : ..., by simp` or whatever. What I don't want is random bursts of 5 lines of garbage to get Lean to jump from line to line, because on some very concrete level that pseudocode proof looks complete to me and, more to the point, will look complete to most mathematicians.

```lean
import data.rat algebra.group_power

example (x y : ℤ) : (x : ℚ) ^ 2 + 2 * y ^ 2 = 3 → (x = 1 ∨ x = -1) ∧ (y = 1 ∨ y = -1) := sorry
/-
Pseudo-code proof
1) Squares are non-negative
2) Hence x ^ 2 <= 3 and y ^ 2 <= 3/2
3) Hence |x| <= 1 and |y| <= 1
4) Now check all cases.
-/
```

#### [Kevin Buzzard (Sep 28 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134813633):
PS I guess the "and" lines can be split, giving us six lines of pseudocode, and i would even allow for seven if we wanted to get from 2y^2 le 3 to y^2 le 3/2

#### [Kevin Buzzard (Sep 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134813668):
The lean issues are getting from rat to int (and when?) and getting dec_trivial to check the cases

#### [Kevin Buzzard (Sep 28 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134813807):
PPS I recommend not going via nat. @**Kenny Lau** how many lines of tactic mode does it take you to solve my challenge?

#### [Kevin Buzzard (Sep 28 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134814042):
PPPS `example (x y : ℤ) : (x : ℚ) ^ 2 + 2 * y ^ 2 = 3 ↔ x ^ 2 + 2 * y ^ 2 = 3 := by simp` fails :-(. Why?? PPPPS you will all be pleased to know that I am now going to do 5 hours of admin with Lean chat off.

#### [Johannes Hölzl (Sep 28 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134814377):
I guess for step 2) you can try to use `linarith`.

#### [Mario Carneiro (Sep 28 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134814523):
it doesn't look very linear to me

#### [Rob Lewis (Sep 28 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134814559):
Step 2 is linear if you treat the squares as atoms. But this isn't the hard part of the proof.

#### [Rob Lewis (Sep 28 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134814603):
```lean
example (x y : ℤ) : (x : ℚ) ^ 2 + 2 * y ^ 2 = 3 → (x = 1 ∨ x = -1) ∧ (y = 1 ∨ y = -1) := 
λ h, 
have hxn : (x : ℚ) ^ 2 ≥ 0, from pow_two_nonneg _,
have hyn : (y : ℚ) ^ 2 ≥ 0, from pow_two_nonneg _,
have hx3 : (x : ℚ) ^ 2 ≤ 3, by linarith,
have hy3 : (y : ℚ) ^ 2 ≤ 3/2, by linarith,
_
```

#### [Mario Carneiro (Sep 28 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134814767):
can you prove `(x : ℚ) ^ 2 < 4` and `(y : ℚ) ^ 2 < 4` instead by linarith?

#### [Rob Lewis (Sep 28 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134814816):
Yup.

#### [Mario Carneiro (Sep 28 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134814823):
I believe there is a theorem that says `a^2 < b^2 <-> a < b`

#### [Rob Lewis (Sep 28 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134814837):
I hope there's no theorem that says that on `rat`.

#### [Rob Lewis (Sep 28 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134814854):
Or `int`, for that matter.

#### [Mario Carneiro (Sep 28 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134814860):
It should hold on rat, but I'm omitting the nonnegativity assumptions

#### [Scott Morrison (Sep 28 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134815413):
@**Rob Lewis**, how hard do you think it would be to ask `linarith` to "try harder", automatically treating subexpressions it doesn't understand as atoms?

#### [Mario Carneiro (Sep 28 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134815488):
isn't that what it's already doing?

#### [Scott Morrison (Sep 28 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134815551):
```
example (x y : ℕ) (h : 6 + ((x + 4) * x + (6 + 3 * y) * y) = 3) : false :=
by linarith
```

#### [Scott Morrison (Sep 28 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134815556):
Says `no args to linarith`.

#### [Scott Morrison (Sep 28 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134815584):
While I'm hoping for something that would first generalize `(x + 4) * x` and `(6 + 3 * y) * y` ftw.

#### [Scott Morrison (Sep 28 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134815654):
I guess I can see how to do this, I'm just hoping someone says there's an easier way than what I have in mind. :-)

#### [Rob Lewis (Sep 28 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134816758):
It wouldn't be hard to make it handle things like that. Right now, if it sees an obvious nonlinearity, it will reject that hypothesis. `x^2` doesn't count as obvious because it's only checking + and *.

#### [Rob Lewis (Sep 28 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134816870):
@**Mario Carneiro** I don't think we have the necessary nonnegativity assumptions in Kevin's problem, at least not without some work, which kind of defeats the point. And there's still some pain dealing with casts. Ultimately, I think we need some sort of "cast correction" tactic and integer arithmetic to do that properly.

#### [Mario Carneiro (Sep 28 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134816931):
well, you want to rewrite with `a^2 = (abs a)^2` first, and then you have your nonnegativity assumption

#### [Rob Lewis (Sep 28 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134817679):
@**Scott Morrison|110087** Hmm, let me qualify my last response -- the way `linarith` handles nats right now makes it slightly harder. I'll think about a clean way to do this.

#### [Rob Lewis (Sep 28 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134817712):
But it's easy to make it handle this:
```lean
example (x y : ℚ) (h : 6 + ((x + 4) * x + (6 + 3 * y) * y) = 3) (h' : (x + 4) * x ≥ 0)
  (h'' : (6 + 3 * y) * y ≥ 0)  : false :=
by linarith
```

#### [Scott Morrison (Sep 28 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134818221):
That's great. (And the same for nats would be great!)

#### [Rob Lewis (Sep 28 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134818589):
https://github.com/leanprover/mathlib/pull/379

#### [Kenny Lau (Sep 28 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134828582):
```quote
PPS I recommend not going via nat. @**Kenny Lau** how many lines of tactic mode does it take you to solve my challenge?
```
I respectfully decline for personal reasons.

#### [Scott Morrison (Sep 29 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879587):
Hi @**Kevin Buzzard**, with a few(!) additional `simp` lemmas, some of which are perfectly sensible, and some of which are less so, we can do:
```
@[tidy] meta def la := `[linarith]
@[tidy] meta def cases_xy := `[cases x; cases y]

example (x y : ℤ) (h1 : nat.coprime (int.nat_abs x) (int.nat_abs y)) (h2 : x ^ 2 + 3 * y ^ 2 = 4) :
  (x = 1 ∨ x = -1) ∧ (y = 1 ∨ y = -1) :=
by tidy
```

#### [Kevin Buzzard (Sep 29 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879621):
That's not exactly what I asked but I agree that this is a big step forward

#### [Scott Morrison (Sep 29 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879626):
Oh, it isn't? I must have changed it at some point and forgotten I changed it.

#### [Scott Morrison (Sep 29 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879627):
Let me go find the original :-)

#### [Kevin Buzzard (Sep 29 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879628):
I don't care about efficiency, I care about making life easier for beginner mathematicians

#### [Kevin Buzzard (Sep 29 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879631):
The equality was over rat

#### [Kenny Lau (Sep 29 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879671):
how many seconds does it take to compile?

#### [Kevin Buzzard (Sep 29 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879676):
Because moving from rat to int is another great example of something which is easy in maths

#### [Scott Morrison (Sep 29 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879683):
Oh -- this was your original question (exactly), but then you asked a different one I didn't see yet.

#### [Kevin Buzzard (Sep 29 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879687):
Oh! Yes you're exactly right

#### [Kevin Buzzard (Sep 29 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879690):
I asked a challenge problem later

#### [Kevin Buzzard (Sep 29 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879736):
which you have made serious inroads into

#### [Kevin Buzzard (Sep 29 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879744):
Are those safe tidy lemmas by the way?

#### [Scott Morrison (Sep 29 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879754):
@**Kenny Lau** --- it takes 13 seconds, or 5 seconds after you substitute in the proof `tidy` provides.

#### [Scott Morrison (Sep 29 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879762):
It's fine to use linarith in `tidy`, as long as you don't care about how long things take to run. :-)

#### [Kevin Buzzard (Sep 29 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879765):
Scott I think this is the first time I've seen tidy do something which I really did not want to do myself

#### [Scott Morrison (Sep 29 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879803):
It's completely insane to let `tidy` case bash on ints or nats unless you know case bashing is the right thing to do.

#### [Kevin Buzzard (Sep 29 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879814):
Kenny I don't care how long it takes to run because this is for undergraduates solving cheap problems, not a library

#### [Scott Morrison (Sep 29 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879872):
I'm hiding here quite a few simp lemmas I had to write before this could work.

#### [Scott Morrison (Sep 29 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879877):
The dubious one was:

#### [Scott Morrison (Sep 29 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879879):
```
meta def dt := `[exact dec_trivial]
@[simp] lemma int.of_nat_eq_neg (n : ℕ) (m : ℤ) (h : m < 0 . dt) : int.of_nat n = m ↔ false := sorry
```

#### [Scott Morrison (Sep 29 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879904):
(And here of course by "write" I mean "write the statement of and sorry the proof", as usual. :-)

#### [Kevin Buzzard (Sep 29 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879916):
I think I could manage a proof of that one

#### [Scott Morrison (Sep 29 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879963):
oh -- there's nothing scary with the proof. The scary thing is have the `exact dec_trivial` autoparam.

#### [Scott Morrison (Sep 29 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879972):
I've no idea if that is a viable thing to do in a `@[simp]` lemma. I mean, it works, apparently, but it may be insane for some reason I don't understand. :-)

#### [Scott Morrison (Sep 29 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879975):
The full set of `simp` lemmas I needed was 
```
@[simp] lemma nat.coprime_zero (n : ℕ) : nat.coprime n 0 = false := sorry
@[simp] lemma nat.zero_coprime (n : ℕ) : nat.coprime 0 n = false := sorry

local attribute [simp] nat.succ_eq_add_one

@[simp] lemma nat.add_has_add (a b : ℕ) : nat.add a b = a + b := rfl
@[simp] lemma nat.mul_has_mul (a b : ℕ) : nat.mul a b = a * b := rfl
@[simp] lemma nat.pow_has_pow (a b : ℕ) : nat.pow a b = a ^ b := rfl

local attribute [simp] int.of_nat_add
local attribute [simp] int.of_nat_one

@[simp] lemma foo_1 (a b : ℕ) : a + b = a ↔ b = 0 := sorry
@[simp] lemma foo_2 (a b c : ℕ) : a + (b + c) = c ↔ a + b = 0 := sorry

@[simp] lemma nat.square_zero (n : ℕ) : n^2 = 0 ↔ n = 0 := sorry

local attribute [simp] nat.pow_zero
local attribute [simp] nat.pow_one

meta def dt := `[exact dec_trivial]

@[simp] lemma int.of_nat_eq_neg (n : ℕ) (m : ℤ) (h : m < 0 . dt) : int.of_nat n = m ↔ false := sorry
@[simp] lemma int.of_nat_eq_one (n : ℕ) : int.of_nat n = 1 ↔ n = 1 := sorry
@[simp] lemma int.neg_succ_of_nat_eq_nneg (n : ℕ) (m : ℤ) (h : m ≥ 0 . dt) : int.neg_succ_of_nat n = m ↔ false := sorry
@[simp] lemma int.neg_succ_of_nat_eq_minus_one (n : ℕ) : int.neg_succ_of_nat n = -1 ↔ n = 0 := sorry
```

#### [Kevin Buzzard (Sep 29 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134879981):
I am supposed to be suggesting a list of projects for third year undergraduate joint maths/computing students and they want the list by Monday. I was going to propose making my `number` class as one of them

#### [Scott Morrison (Sep 29 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134880024):
Also -- this relies on Robert's latest PR for linarith; it doesn't work with the current mathlib one.

#### [Kevin Buzzard (Sep 29 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134880030):
I don't mind about that either

#### [Scott Morrison (Sep 29 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134880104):
I'm always surprised by how little is marked with @[simp] in mathlib

#### [Mario Carneiro (Sep 29 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134880111):
I'm sure Kenny doesn't feel the same way

#### [Scott Morrison (Sep 29 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134880113):
Like `int.of_nat_one`. How is that not a simp lemma?

#### [Mario Carneiro (Sep 29 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134880157):
Isn't that in core?

#### [Scott Morrison (Sep 29 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134880159):
Ah, okay :-)

#### [Scott Morrison (Sep 29 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134880160):
We can still add the attribute, I guess!

#### [Mario Carneiro (Sep 29 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134880165):
At the start of `int.basic` is
```
attribute [simp] int.coe_nat_add int.coe_nat_mul int.coe_nat_zero int.coe_nat_one int.coe_nat_succ
```

#### [Mario Carneiro (Sep 29 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134880178):
I think we need a simp lemma for of_nat -> coe_nat

#### [Scott Morrison (Sep 29 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134880183):
I see. Sounds good!

#### [Scott Morrison (Sep 29 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134880231):
And how about
```
attribute [simp] nat.pow_zero nat.pow_one
```

#### [Scott Morrison (Sep 30 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134916514):
I'm curious about
```
@[simp] theorem int.cast_pow [ring α] (n : ℤ) (m : ℕ) : (↑(n ^ m) : α) = ↑n ^ m :=
```

#### [Scott Morrison (Sep 30 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134916521):
My instinct would be to `simp` the other way here!

#### [Kenny Lau (Sep 30 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134916523):
well it's the same as `int.cast_mul` and `int.cast_add` and etc

#### [Scott Morrison (Sep 30 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134916524):
Yes. :-)

#### [Scott Morrison (Sep 30 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134916564):
Do you know situations where it's useful to `simp` in this direction?

#### [Mario Carneiro (Sep 30 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917057):
`int.of_nat (n - m)`

#### [Mario Carneiro (Sep 30 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917102):
Usually it doesn't matter as long as it is in a consistent direction, but generally speaking it is harder to simp the other way around because it is a kind of "distribution" lemma - the casts on the rhs have to line up for the simp to work, which can be a problem if simp wants to write `\u a + b + \u c`

#### [Mario Carneiro (Sep 30 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917120):
The recommended technique for bringing your casts together is to assert the form you want and `simpa` to reduce it to your goal

#### [Kenny Lau (Sep 30 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917159):
`simpa only`

#### [Kevin Buzzard (Sep 30 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917160):
Chris made a comment to me about all this -- he said the rule of thumb was that simp wants to make the up-arrows as close as possible to the variables

#### [Kevin Buzzard (Sep 30 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917180):
That clarified things for me. My main beef is that you need to know the general cast lemmas from nat to blah and then a bunch of different ones for going from nat to int.

#### [Mario Carneiro (Sep 30 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917225):
I hope we get the `cast` tactic for dealing with this

#### [Kevin Buzzard (Sep 30 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917229):
My hope was to let everything be a `number` and let type class inference deal with everything

#### [Kevin Buzzard (Sep 30 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917234):
Is this related?

#### [Kevin Buzzard (Sep 30 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917238):
Would part of this tactic be the `is_actually_an_int` typeclass?

#### [Mario Carneiro (Sep 30 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917280):
I wasn't planning on it

#### [Mario Carneiro (Sep 30 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917283):
I'm not sure how those plans interact with the `is_int` class

#### [Kevin Buzzard (Sep 30 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917333):
I am unclear on the details, but I am very clear on what I want the outcome to be: easy passing from `(x : rat) ^ 2  + 2 * y ^ 2 = 7` to `x ^ 2 + 2 * y ^ 2 = 7` with x y ints, where some of those 2's are nats and some are rats, and some of those 7's are ints are some are rats, and in the future this won't matter.

#### [Mario Carneiro (Sep 30 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917344):
Yes, I think this can be done

#### [Mario Carneiro (Sep 30 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917393):
The idea is you point at an equation and say "make this an equation on int" and it figures out the appropriate coercions rewriting this way and that

#### [Kevin Buzzard (Sep 30 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917403):
Is this tactic just on a list of things to do, or are there actually plans to develop it? My users would find it extremely helpful.

#### [Mario Carneiro (Sep 30 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917404):
somewhere in between

#### [Mario Carneiro (Sep 30 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917444):
I have a fairly concrete idea of how to implement it, but I haven't tried

#### [Kevin Buzzard (Sep 30 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917445):
That's great news. I'm really glad it's on your radar in some sense.

#### [Kevin Buzzard (Sep 30 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917504):
This is I think the third time when I have managed to pinpoint an issue which is "trivial in maths and hard in Lean", and you solved both the previous ones. The first was that it seemed to be very hard to prove things like "2 + 2 \not= 5" for real numbers in Lean, and then `norm_num` appeared. The second was that it seemed to be very hard to prove `(x+y)^3=x^3+3x^2y+3xy^2+y^3` in Lean and then `ring` appeared. The reason I find these sorts of questions particularly interesting to focus on is that undergraduate mathematicians take these sorts of things for granted, having no insight into what actually goes in to proving them, but I would rather not try to teach them that insight, I would rather it were just easy.

#### [Mario Carneiro (Sep 30 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917549):
usually the hard part with these tactics is just figuring out what you want them to do (and what is not in scope)

#### [Mario Carneiro (Sep 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917590):
it's hard to do anything with "I want magic", but "I want a decision procedure for linear inequalities on nat" has a clear enough specification to actually get implemented

#### [Kevin Buzzard (Sep 30 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917598):
"the hard part" -- I beg to differ. From where I'm standing, the hard part is that there are an extremely small number of people in the world who are equipped to write these tactics, and they are all busy. And I am not yet one of those people. That's why I wrote the ring blog post, to get some sort of insight into how these things might work. I am also not yet convinced that I will be able to write a convincing grant proposal to pay for a computer scientist to write these tactics for me, because the applications are firmly pedagogical and the big grant funders in the UK are more interested in research.

#### [Kevin Buzzard (Sep 30 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917643):
But I saw undergraduates bravely struggling with this sort of thing all summer, and the reason I got up to speed with how casts currently work in Lean is so I could write the code myself which solved their problems in the particular instances they got stuck at.

#### [Kevin Buzzard (Sep 30 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917685):
e.g. https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions.20N-.3EZ-.3EQ-.3ER-.3EC

#### [Mario Carneiro (Sep 30 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917686):
By the way, it is very easy to write a tactic that does what this `cast` would do, if you aren't picky about the flexibility

#### [Kevin Buzzard (Sep 30 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917691):
It is very easy for you. I have never written meta code and currently I don't have the time to learn.

#### [Mario Carneiro (Sep 30 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917692):
you can just define a tactic like `` `[rw <- int.cast_inj, simp [int.cast_one, int.cast_add, ...]]``

#### [Kevin Buzzard (Sep 30 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917693):
Also it takes me a long time to learn things, far longer than it takes people like you or Chris or Kenny.

#### [Mario Carneiro (Sep 30 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917694):
I mean a "poor mans tactic"

#### [Mario Carneiro (Sep 30 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917744):
I think I've even used essentially this tactic in `data.num.lemmas`

#### [Kevin Buzzard (Sep 30 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917785):
My strategy is different. I encourage Chris and Kenny to learn tactics and next week I will be encouraging many more people to learn Lean and then encouraging the best ones to learn tactics. One might argue that part of the reason that localisations of rings and quadratic reciprocity are now in mathlib is that people near me somehow got persuaded that these were important projects. And for me they are extremely important because they are undergraduate level mathematics, which is something I am hugely trying to push.

#### [Kevin Buzzard (Sep 30 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917791):
I don't know to what extent `norm_num` and `ring` got written because of rants by me about how mathematicians needed them, but I know for sure that I am extremely grateful for both.

#### [Kevin Buzzard (Sep 30 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917967):
Another thing I know for sure is that a bright undergraduate is less busy than a bright PhD student, because it's much easier for the bright undergraduate to coast.

#### [Mario Carneiro (Sep 30 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134917983):
The rants were definitely a factor :)

#### [Mario Carneiro (Sep 30 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918026):
I try to let the community decide my priorities to some extent, so being loud is not ineffective if you want me to make something for you

#### [Kevin Buzzard (Sep 30 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918032):
Thank you Mario for not just writing me off as an asshole.

#### [Mario Carneiro (Sep 30 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918071):
you're just a guy with crazy pants

#### [Kevin Buzzard (Sep 30 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918074):
My summer students would have been completely lost without ring and norm_num.

#### [Patrick Massot (Sep 30 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918091):
Don't forget we also rant about the module refactoring and the `module` tactic

#### [Kevin Buzzard (Sep 30 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918093):
I am writing teaching materials and I introduce ring and norm_num at the same time as rw. That's how important they seem to be in practice when doing undergraduate problem sheets in mathematics.

#### [Patrick Massot (Sep 30 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918134):
The point where module refactoring is the main stumbling block of the perfectoid project is approaching fast.

#### [Mario Carneiro (Sep 30 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918137):
it's my top lean priority right now

#### [Kevin Buzzard (Sep 30 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918138):
ROFL the slower module refactoring goes the longer I have an excuse for putting off the perfectoid project, which is what I have needed to do over the last week or two

#### [Patrick Massot (Sep 30 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918139):
With the category theory PR

#### [Patrick Massot (Sep 30 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918144):
Is 33 open PR our new record?

#### [Mario Carneiro (Sep 30 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918147):
I think second is merging the ever growing zoo of community branches

#### [Patrick Massot (Sep 30 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918188):
The community (not only you) needs to go through the community repo and delete or rename branches

#### [Kevin Buzzard (Sep 30 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918189):
Patrick I was thinking about pushing perfectoids forward by epsilon yesterday but all I managed to do was write down a bit more precisely what needed to be done next. I pushed a commit which was just about ten lines of comments!

#### [Kevin Buzzard (Sep 30 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918190):
Again I think that the long term solution for this is training

#### [Mario Carneiro (Sep 30 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918191):
I wonder whether it would be possible to set up a voting system for the PRs

#### [Mario Carneiro (Sep 30 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918196):
so we can prioritize them a bit

#### [Mario Carneiro (Sep 30 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918262):
are thumbs up on a PR visible from the PR list?

#### [Kevin Buzzard (Sep 30 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918263):
The risk with that is that if Patrick and I start rallying the troops to vote for the mathsy ones then Simon's work on traversable or other stuff which I don't understand the point of ends up languishing forever.

#### [Mario Carneiro (Sep 30 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918269):
that seems fair - you actually have more users

#### [Kevin Buzzard (Sep 30 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918270):
I'm not saying there's no point though

#### [Kevin Buzzard (Sep 30 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918310):
and what I worry about is that actually in the long term whatever simon is doing might end up being much more important for making stuff work

#### [Mario Carneiro (Sep 30 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918315):
I think I can judge that to some extent, any voting would be a suggestion at best

#### [Kevin Buzzard (Sep 30 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918320):
Patrick, I got into the habit of calling my branches `kmb_...` because I felt it only right that I should take some sort of responsibility for their existence.

#### [Kevin Buzzard (Sep 30 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918368):
After module refactoring I will go back to them and take a good look at all of the ones I created and then tidy them up. But (in contrast to you) I am not in a hurry for this because I am trying to put together a bunch of cocalc example sheets and a bunch of lean example sheets and in the long term I believe it's in my (and possibly the community's) interests to make the delivery of my course as smooth as possible.

#### [Mario Carneiro (Sep 30 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918413):
yeah, I realize that the module refactoring is going to cause some disruption

#### [Mario Carneiro (Sep 30 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918472):
In my metamath days the main database set.mm was like 90% of the existing code in the community, so if I do a refactoring and fix everything that's there most people don't feel the change.  With mathlib it's probably closer to 60% so I either have to visit everyone's projects or trust that they can fix it themselves

#### [Kevin Buzzard (Sep 30 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918517):
I am very happy to fix my comm alg stuff and perfectoid stuff myself.

#### [Kevin Buzzard (Sep 30 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134918526):
I understand how all this works much better now. But it's also a reason why I don't want to write anything new right now (that and the far more important reason that I have no time).

#### [Patrick Massot (Sep 30 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more int nat moans and golf plea/near/134919521):
Sorry, I was captured by my children. My votes are: module refactoring and Scott's PR

