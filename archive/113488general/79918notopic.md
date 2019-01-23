---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79918notopic.html
---

## Stream: [general](index.html)
### Topic: [(no topic)](79918notopic.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 26 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123008190):
So general chatter goes in "archives" topic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 26 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123008198):
oh no I have made (no topic). Do I have to have a topic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Feb 26 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123008201):
no topic necessary for off-topic conversation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 26 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123008205):
I don't understand how to have off-topic conversation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033113):
Chris has already observed that mathematicians frequently want to sum from 0 to n, or 1 to n, and have a bunch of basic facts about such sums available to them. I know there are finsets and fintypes or whatever, but this case of summing from 0 to n or 1 to n is such a common usage case in maths. Is there already a specialised type for dealing specifically with such sums, which is easier to handle than dealing with general finsets? I am thinking about teaching induction to mathematicians without having to fill their heads with what I would call "specialised types" such as finset.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033117):
If not I might be tempted to build such things myself but I don't want to reinvent the wheel.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Feb 27 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033165):
I was faced with a similar situation last year. The formulation of `sum` I find is less than conducive to reasoning. I'm not sure if my lemmas about `foldl` and `foldr` are still around (I think they are now in mathlib) but your best bet I think is to prove `sum (xs ++ ys) = sum xs + sum ys`. That should get you started at least

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Feb 27 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033218):
DId you try `by simp`? I think this is the consequence of several lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Feb 27 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033225):
But I'm also working on a definition of sums over natural numbers to make this sort of thing easier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033478):
I didn't try simp because I was writing teaching materials and for some reason I wanted to be "explicit" about what was happening -- e.g. "this lemma with this name shows the fundamental fact which we will need, namely that the sum to n+1 is related to the sum to n in this obvious way". There is a danger with the sort of stuff I was doing that simp would just clear the goal completely and I know I can target it with (have blah, by simp) or whatever, but my goal was not to prove the lemma, it was to show math undergraduates how to use induction in Lean without any extra bells and whistles.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033519):
I suspect that in general as my thoughts about teaching progress I will want access to lemmas with possibly names that Mario disapproves of and which state things which he does not want in mathlib (e.g. because they can be done with a fold in one line or some such thing). Things like folds are what I am trying to avoid currently because I do not want to teach them any functional programming.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033527):
You CS guys might think this is mad, but look at Chris Hughes -- he showed up knowing a bit of matlab and had no idea what a functional program was, and I got him doing mathematics in Lean very quickly because of tactic mode. The more tactics / lemmas there are, the more mathematicians are able to stay away from the whole functional thing, and they can just get into it later when it all begins to make more sense.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Feb 27 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033576):
@**Kevin Buzzard** Not mad at all. Tactics are great for incrementally proving theorems.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Feb 27 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033577):
I think that will limit how much you can do but there must still be interesting fragments

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Feb 27 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033619):
... and this is coming from a CS guy, though, again, I'm not sure why that matters. :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033630):
I think that you can get through a whole bunch of my introduction to proof course in Lean without really knowing too much about functional programming. I've seen it happen.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033635):
My job is not to teach functional programming, it is to teach rigorous thinking.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Feb 27 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033666):
I think functional programming is especially hard to avoid as you're scaling up your proof efforts which often doesn't really come up in introductions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Feb 27 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033679):
@**Kevin Buzzard**  I'm sure you're right. Why do you feel the need to defend that idea?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Feb 27 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033683):
If that's the kind of teaching you are going for, I recommend giving a direct inductive definition like it is done in TPIL

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033685):
I would be interested to hear @**Chris Hughes** 's take on the issue. I am not sure he knows what a fold is but he has proved the fundamental theorem of arithmetic and much more in Lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Feb 27 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123033691):
then you can give all the natural lemmas and prove basic properties and there is no hidden magic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Feb 27 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123042606):
I totally agree that tactics is the way to teach lean to maths students. I proved the fundamental theorem of arithmetic without even knowing what lambda did, and this gave me enough proficiency very quickly, that I've probably learnt a fair amount about functional programming, whatever that is, without really thinking about trying to learn functional programming.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123061458):
Hey Patrick did you make an arbitrary product of rings a ring recently?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123061860):
@**Patrick Massot** I need that now! But it's in gitter chat and it'll be hard to find :-/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123061930):
Aah I've found it by looking through your github repos until I found the right commit :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Feb 28 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/123066299):
Yes: https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/indexed_product.lean I will make a PR at some point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960052):
[pic1.png](/user_uploads/3121/AwppWERsWgYQlkaoTxtLAKL-/pic1.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960056):
he made that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960075):
it's the syntax tree for my proof that sqrt(3) is irrational

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960087):
it's like `set_option pp.all`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960160):
In fact we made it from the output of `set_option pp.all` and some emacs trickery and some python code

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960168):
and then he made that in blender

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960195):
red dots are functions, blue are evaluated terms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 01 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960445):
I proved it for non integer nth roots of integers.
```lean
import data.nat.gcd algebra.group_power data.rat

open nat int
lemma nat.mul_pow (a b n : ℕ) : (a * b) ^ n = a ^ n * b ^ n := 
by induction n; simp [*, nat.pow_succ, mul_comm, mul_assoc, mul_left_comm]

lemma nat.dvd_of_pow_dvd_pow : ∀ {a b n : ℕ}, 0 < n → a ^ n ∣ b ^ n → a ∣ b 
| a 0     := λ n hn h, dvd_zero _
| a (b+1) := λ n hn h, 
let d := nat.gcd a (b + 1) in
have hd : nat.gcd a (b + 1) = d := rfl,
  match d, hd with
  | 0 := λ hd, (eq_zero_of_gcd_eq_zero_right hd).symm ▸ dvd_zero _
  | 1 := λ hd, 
    begin
      have h₁ : a ^ n = 1 := coprime.eq_one_of_dvd (coprime.pow n n hd) h,
      have := pow_dvd_pow a hn,
      rw [nat.pow_one, h₁] at this,
      exact dvd.trans this (one_dvd _),
    end
  | (d+2) := λ hd, 
    have (b+1) / (d+2) < (b+1) := div_lt_self dec_trivial dec_trivial,
    have ha : a = (d+2) * (a / (d+2)) := 
      by rw [← hd, nat.mul_div_cancel' (gcd_dvd_left _ _)],
    have hb : (b+1) = (d+2) * ((b+1) / (d+2)) := 
      by rw [← hd, nat.mul_div_cancel' (gcd_dvd_right _ _)],
    have a / (d+2) ∣ (b+1) / (d+2) := nat.dvd_of_pow_dvd_pow hn $ dvd_of_mul_dvd_mul_left
      (show (d + 2) ^ n > 0, from pos_pow_of_pos _ (dec_trivial))
      (by rwa [← nat.mul_pow, ← nat.mul_pow, ← ha, ← hb]),
    by rw [ha, hb];
      exact mul_dvd_mul_left _ this
  end
using_well_founded {rel_tac := λ _ _, `[exact ⟨_, measure_wf psigma.snd⟩]}

lemma int.nat_abs_pow (a : ℤ) (n : ℕ) : a.nat_abs ^ n = (a ^ n).nat_abs := 
by induction n; simp [*, nat.pow_succ, _root_.pow_succ, nat_abs_mul, mul_comm]

lemma int.dvd_of_pow_dvd_pow {a b : ℤ} {n : ℕ} (hn : 0 < n) (h : a ^ n ∣ b ^ n) : a ∣ b :=
begin
  rw [← nat_abs_dvd, ← dvd_nat_abs, ← int.nat_abs_pow, ← int.nat_abs_pow, int.coe_nat_dvd] at h,
  rw [← nat_abs_dvd, ← dvd_nat_abs, int.coe_nat_dvd],
  exact nat.dvd_of_pow_dvd_pow hn h
end

lemma int.cast_pow {α : Type*} [ring α] (a : ℤ) (n : ℕ) : ((a ^ n : ℤ) : α) = (a : α) ^ n :=
by induction n; simp [*, _root_.pow_succ]

def nth_root_irrational {x : ℤ} {a : ℚ} {n : ℕ} (hn : 0 < n) (h : a ^ n = x) : {a' : ℤ // a = a'} :=
have had : ((a.denom : ℤ) : ℚ) ≠ 0 := int.cast_ne_zero.2 (ne_of_lt (int.coe_nat_lt.2 a.3)).symm,
⟨a.num,
begin 
  rw [rat.num_denom a, rat.mk_eq_div, div_pow _ had, div_eq_iff_mul_eq (pow_ne_zero _ had),
    ← int.cast_pow, ← int.cast_mul, ← int.cast_pow, int.cast_inj] at h,
  have := int.coe_nat_dvd.1 (dvd_nat_abs.2 (int.dvd_of_pow_dvd_pow hn (dvd_of_mul_left_eq _ h))),
  have := coprime.eq_one_of_dvd a.4.symm this,
  rw [rat.num_denom a, rat.mk_eq_div, this],
  simp,
end⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960579):
```lean
def nth_root_irrational {x : ℤ} {a : ℚ} {n : ℕ} (hn : 0 < n) (h : a ^ n = x) : {a' : ℤ // a = a'} :=
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960583):
yay you made it constructive :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960586):
```quote
he made that
```
who?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 01 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960829):
His son I believe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125960845):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 02 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125984628):
> yay you made it constructive :D

Actually, it makes no difference since if a rational number is an integer, then you can obtain its value using `rat.num`, or `rat.floor`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 02 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/125984672):
(which is to say, that theorem would still be constructive with `exists`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) gary (Jul 25 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/130300533):
Hi all,

I'm working on applying formal methods to cryptocurrency protocols. We're a well funded startup (recently raised $20 million) and pay competetively. 

If anyone has interest, please message me.

Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jason Dagit (Aug 16 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/132250941):
I have an expression that uses a type class instance. Is there a command to that prints out which instance was inferred?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 16 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/132250998):
Before the code printing the expression, use `set_option pp.implicit true` so that the pretty printer shows more parts of your expression, namely, implicit parameters (which include class instances)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jason Dagit (Aug 16 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/132251070):
Thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 18 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/132357521):
(deleted)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (Dec 16 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/151864889):
(deleted)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Namdak Tonpa (Jan 07 2019 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/154581476):
I know I'm flooding, but here is IRC bot written in pure Lean 3.4.1 (someone asked me in lounge)
https://github.com/forked-from-1kasper/leanbot
Can't wait to write WebSocket binary protocol for Lean4!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Jan 07 2019 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28no%20topic%29/near/154584968):
This is the kind of flooding that is appreciated. By all means do continue to flood.


{% endraw %}
