---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/53044Variablewithbracesparenthesesandsquarebrackets.html
---

## Stream: [new members](index.html)
### Topic: [Variable with braces, parentheses and  square brackets](53044Variablewithbracesparenthesesandsquarebrackets.html)

---

#### [AHan (Nov 08 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147280537):
The below code works.
However, if I changed the `h` to `pp` in function `p_mod_range`, pp will become unknown identifier....
No matter I changed the brackets of variable pp to parentheses or square brackets or braces, neither of them can make variable `pp` be identified by lean....
Why can't lean identifies variable `pp`, and how can I fix this ?
```
import data.nat.prime
import data.int.basic
import data.int.modeq

open nat

lemma mod_range {b : ℕ} : (b > 0) → ∀ (x : ℤ), 0 ≤ x % b ∧ x % b < b := 
begin
  intros h₁ x,
  apply and.intro,
  begin 
    apply int.mod_nonneg, simp,
    assume h₃,
    rw h₃ at *,
    cases h₁
  end,
  begin
    apply int.mod_lt_of_pos,
    apply int.coe_nat_lt.elim_right,
    assumption
  end,
end

namespace pf

variables { p: ℕ }  {pp : prime p}

lemma p_mod_range (h: prime p): ∀ (x : ℤ),  0 ≤ x % p ∧ x % p < p :=
  begin
    intro, apply mod_range, apply (prime.pos h),
  end
```

#### [Mario Carneiro (Nov 08 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147282373):
`variables` are not added by default to the context of the current theorem unless they appear in the type

#### [Mario Carneiro (Nov 08 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147282417):
you should use `include pp` to explicitly add it to the context

#### [AHan (Nov 08 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147282435):
Oh Yeah!! include works!

#### [AHan (Nov 08 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147282473):
But why isn't it be added by default to the context?

#### [Johan Commelin (Nov 08 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147282760):
This allows you to introduce a bunch of variables at the top, and selectively use them in the theorems you prove.

#### [Johan Commelin (Nov 08 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147282770):
Otherwise a lot of theorems (and definitions) would have unnecessary assumptions.

#### [AHan (Nov 08 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147282946):
Got it!!
Is the include scope ends until the end of the section or the namespace?
Can I stop include in the middle point, like only include the variables for one function?

#### [Johan Commelin (Nov 08 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147282993):
Yes: `omit pp`. Otherwise it stops at `end section/namespace`

#### [AHan (Nov 08 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147283011):
Ok! Thanks a lot for the explanations!

#### [AHan (Nov 08 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147284728):
Although including variable works, some functions like `has_mul`, `has_one` in the following code, will have to explicitly name out the variables `p`, `p_gt_one`.
And which seems to make using the symbols `*`, `1` failed, like in function `pf_is_right_inv` below...
Is there any better way to handle this?
```
def pf {p : ℕ} := {e : ℤ// 0 ≤ e ∧ e < p}

namespace pf

variables { p: ℕ } { p_gt_one : p > 1 } { pp : prime p }
include p_gt_one

def mul (a b : @pf p) : @pf p :=  ⟨(a.val * b.val) % p,  begin apply mod_range, apply (trans p_gt_one zero_lt_one) end⟩
instance : has_mul (@pf p) := ⟨@mul p p_gt_one⟩
protected def one  : @pf p := ⟨1, begin apply and.intro, apply zero_le_one, apply (int.coe_nat_le.elim_right p_gt_one), end⟩
instance : has_one (@pf p) := ⟨@pf.one p p_gt_one⟩

lemma pf_is_right_inv (a : @pf p) : (a.1 > 0) → a * (@pf.inv p p_gt_one a) = 1 := sorry
end pf
```

#### [Johan Commelin (Nov 08 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147284864):
I don't think you should have `pp` and `p_gt_one`. Because you can deduce `p_gt_one` from `pp`.

#### [Johan Commelin (Nov 08 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147284880):
Also, you should make the `p` argument of `pf` explicit, so that you can remove the `@` from `pf` later.

#### [AHan (Nov 08 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147284948):
yeah I know I can deduce `p_gt_one` from `pp`, but I'm thinking of if in some cases like `add`, `mul`, `sub`, maybe I can make it a bit general, since `pp` isn't actually needed

#### [Johan Commelin (Nov 08 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285095):
Ok, but then I wouldn't make it a `variable`. Just include it as an assumption on that line.

#### [Johan Commelin (Nov 08 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285106):
And consider renaming `p` to `n` to show that you also care about non-primes.

#### [AHan (Nov 08 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285194):
What do you mean include it as an assumption on that line?

#### [AHan (Nov 08 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285196):
OH yes, renaming is a good suggestion!

#### [Johan Commelin (Nov 08 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285207):
`def mul {h : p > 1} (a b : @pf p) : @pf p := blah`

#### [Johan Commelin (Nov 08 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285211):
But it will be annoying to use, because you have to carry that proof around all the time.

#### [Johan Commelin (Nov 08 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285258):
And I think you don't need it.

#### [Johan Commelin (Nov 08 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285266):
You can define it for `p = 1` just fine.

#### [AHan (Nov 08 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285268):
Yes.... seems like really annoying...
Maybe I should give up the idea of taking care of non-primes

#### [Johan Commelin (Nov 08 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285271):
I guess `p = 0` is problematic.

#### [Johan Commelin (Nov 08 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285280):
Sure, after all, others have already done that. So if you are just experimenting, I wouldn't try to be as general as possible.

#### [AHan (Nov 08 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285399):
Yeah I'm just experimenting, but "others have already done that", do you mean in the mathlib or is it in some other trustable third party library?

#### [Johan Commelin (Nov 08 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285404):
No in mathlib.

#### [AHan (Nov 08 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285486):
Which file does it reside in?
Cause this experiment isn't actually my main goal, I did this mainly because my main goal need this, and I didn't find this in mathlib...

#### [Mario Carneiro (Nov 08 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285516):
What are you doing exactly? I'm not sure if it's in mathlib but I don't know what it is. It looks sort of like `zmod`

#### [AHan (Nov 08 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285657):
I want to examine some algorithms correctness, and the algorithms need `prime field`
So I'm thinking of defining a type of `prime field` and use as an instance of class `field`

#### [Mario Carneiro (Nov 08 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285717):
If by prime field you mean Z/pZ where `p` is a prime, that's `zmod`

#### [Mario Carneiro (Nov 08 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285740):
Or do you mean the smallest subfield of a given field? I don't think we have that but you can fake it with `rat.cast`

#### [AHan (Nov 08 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285787):
@**Johan Commelin**  I've done what you suggested, but the problem that I can't use the symbol `*` and `1` still exists...
```
def pf (p : ℕ) := {e : ℤ// 0 ≤ e ∧ e < p}

namespace pf

variables ( p: ℕ ) ( pp : prime p )
include pp

def mul (a b : pf p) : pf p := ⟨(a.val * b.val) % p,     begin apply mod_range, apply prime.pos pp end⟩
instance : has_mul (pf p) := ⟨@mul p pp⟩
protected def one  : pf p := ⟨1, begin apply and.intro, apply zero_le_one, apply (int.coe_nat_lt.elim_right (prime.gt_one pp)), end⟩
instance : has_one (pf p) := ⟨@pf.one p pp⟩

lemma pf_is_right_inv (a : pf p) : (a.1 > 0) → a * (@pf.inv p pp a) = 1 := 
```

#### [Johan Commelin (Nov 08 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285867):
Ok, what happens if you do not include `pp`?

#### [Johan Commelin (Nov 08 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285875):
Just don't make any assumptions on `p`.

#### [Johan Commelin (Nov 08 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285889):
But, like Mario said, you are basically redefining `zmod n`.

#### [AHan (Nov 08 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147285989):
@**Mario Carneiro**  Yeah `Z/pZ ` exactly the thing I want
Do you mean the `zmod` in `modeq` ? Isn't is some sort of equivalence class instead of some types like `int` or `nat` ?

#### [Johan Commelin (Nov 08 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147286042):
https://github.com/leanprover/mathlib/blob/dbb3ff0b5b2e42aa71d8167d7efdb3aa12d6e483/data/zmod/basic.lean#L10

#### [Johan Commelin (Nov 08 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147286049):
It is really almost the same as what you did. The set of naturals between `0` and `n`.

#### [AHan (Nov 08 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147286167):
If I don't include pp, since I have to prove the result of `mul` < p, I will have to include something like `p_gt_zero`in the assumption

#### [AHan (Nov 08 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147286405):
Oh!! Thank you very much! (Didn't notice this... as I can't find zmod via C-c C-d....)

#### [Johan Commelin (Nov 08 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147287978):
@**AHan** Sure, that's right. You will notice that `zmod` uses `pnat`: positive natural numbers.

#### [AHan (Nov 08 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Variable%20with%20braces%2C%20parentheses%20and%20%20square%20brackets/near/147296994):
Yes, didn't even notice that there were `pnat`, this really helped a lot! Thank you!

