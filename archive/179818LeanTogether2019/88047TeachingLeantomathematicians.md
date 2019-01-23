---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/179818LeanTogether2019/88047TeachingLeantomathematicians.html
---

## Stream: [Lean Together 2019](index.html)
### Topic: [Teaching Lean to mathematicians](88047TeachingLeantomathematicians.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 06 2019 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532336):
I have been thinking for a while now about how to teach Lean to absolute beginners, because that is currently the bottleneck we have at Imperial -- not enough people able to get started. Gabriel and I are running a teaching session tomorrow 0900-1030 and 1100-1200 and some people have confessed to knowing no Lean at all, which is of course absolutely fine, but how to get them started?

My boys like learning through puzzle-solving. So here are some puzzles:

https://github.com/kbuzzard/mathematics-in-lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 06 2019 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532337):
The problem is that if you know no Lean at all, even these problems are too hard. You have to install Lean, and then how do you fill in the sorry?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 06 2019 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532342):
So there is some stuff which helps with that here:

http://wwwf.imperial.ac.uk/~buzzard/lean_together/source/leantogether.html

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 06 2019 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532354):
This is some teaching material written in sphinx.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 06 2019 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532362):
I mean, Lean is intended for CS majors..

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jan 06 2019 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532432):
> I mean, Lean is intended for CS majors..

Lean is definitely not intended for CS majors only.  Isn't the whole point of this workshop/project to get mathematicians to like Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 06 2019 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532551):
to get *more* mathematicians to like Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 06 2019 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532552):
And there's a very poor quality video which I made on my own laptop, and which is a bit laughable in places, but it's currently the best I've got. It's sort of an advert for what an absolute beginner can aspire to.

http://wwwf.imperial.ac.uk/~buzzard/lean_together/lean_intro.mp4

Videos are a pain to make, I want to zoom into various bits of the screen etc, and I know how to do all of this in theory but it would take me absolutely hours to make it exactly how I want it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 06 2019 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532607):
you can certainly give a side (or interface) of Lean that is more suitable for mathematicians, but it won't change the fact that Lean is built for CS majors

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 06 2019 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532610):
Should we  play the video tomorrow morning in case you have difficulties getting up on time?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 06 2019 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532618):
How would you understand structural induction if you're just some regular mathematician who never thinks about logic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jan 06 2019 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532665):
You think most CS majors think about logic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 07 2019 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154546873):
@**Kevin Buzzard** I like the video!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 07 2019 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154564805):
```lean
import tactic.interactive tactic.ring

inductive is_even : ℕ → Prop
| zero : is_even 0
| step {n} : is_even n → is_even (n + 2)

example : is_even 4 :=
begin
repeat { apply is_even.step },
apply is_even.zero,
end

example : ¬ is_even 5 :=
begin
intro even_five,
cases even_five with _ even_three,
cases even_three with _ even_one,
cases even_one,
end

lemma even_if_double {n} : is_even (2*n) :=
begin
induction n with d hd,
{ exact is_even.zero },
{ show is_even (2 * (d + 1)),
  rw mul_add,
  apply is_even.step,
  assumption,
 },
end

lemma double_if_even {n} : is_even n → ∃ m, n = 2*m :=
begin
intro h, induction h with d Hd ih,
{ use 0,
  refl
},
{ cases ih with n Hn,
  use (n + 1),
  rw Hn,
  refl,
 }
end

lemma even_iff_double {n} : is_even n ↔ ∃ m, n = 2*m :=
begin
split, apply double_if_even,
intro h, cases h with d Hd, rw Hd, 
  apply even_if_double
end

inductive is_odd : ℕ → Prop
| one : is_odd 1
| step {n} : is_odd n → is_odd (n + 2)

lemma odd_iff_double_add_one {n} : is_odd n ↔ ∃ m, n = 2*m + 1 :=
sorry

lemma even_of_not_odd : ∀ n, 
¬ is_odd n → is_even n
| 0 h := is_even.zero
| 1 h := begin exfalso, apply h, constructor end
| (n+2) h :=
  have ih : _, from even_of_not_odd n,
  begin
  constructor,
  apply ih,
  intro hn,
  apply h,
  constructor, assumption,
  end

#print even_of_not_odd

lemma not_odd_of_even : ∀ n, is_even n → ¬ is_odd n :=
begin
intros n h,
induction h with m m hm,
{intro h, cases h},
{intro h, apply hm, cases h, assumption},
end

lemma even_iff_not_odd : ∀ n, is_even n ↔ ¬ is_odd n :=
begin
intro n, split, apply not_odd_of_even, apply even_of_not_odd
end

lemma odd_square (n : ℕ) : is_odd n → is_odd (n*n) :=
begin
simp [odd_iff_double_add_one],
intro m,
intros  h,
use 2*m + 2*m*m, subst h, ring,
end

lemma even_square (n : ℕ) : is_even (n*n) → is_even n :=
begin
conv in (is_even (n*n)) { simp [even_iff_not_odd] },
simp [even_iff_not_odd],
intros h1 h2, apply h1,
apply odd_square, assumption
end

set_option pp.all true
#check (7 : ℤ)
```

This is what Gabriel and I generated in the second hour of the tutorial

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 07 2019 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154565129):
If any beginners have any questions about this then feel free to ask.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 07 2019 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154566899):
https://github.com/kbuzzard/xena/tree/master/lean_together Random stuff from Monday tutorial

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Holmes (Jan 07 2019 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154581547):
Does anyone have a hint for the following exercise? The idea is to replace the `sorry' with a proof, as elementary as possible (without importing any libraries, if possible). As you can guess, I'm quite new to this! 

```variables (X : Type) (P Q : X → Prop)```

```example : ∀ x, P x ∧ Q x → ∀ x, Q x ∧ P x :=
begin
sorry
end```

So far I have 
``` intro a, intro G, cases G with PH QH, intro b, split, ```
but then I have a proof of Q a, and I want a proof of Q b. I want to say `but a was arbitrary', but don't know how to do this in Lean... 

Thanks very much!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 07 2019 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154581665):
I think you are missing a pair of parentheses

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 07 2019 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154581713):
Yes, I think you want to prove `(∀ x, P x ∧ Q x) → (∀ x, Q x ∧ P x)`, that will be easier!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Holmes (Jan 07 2019 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154581797):
Thanks, will try that. The version I gave was Kevin's exercise, so maybe there is a type there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 07 2019 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154581808):
Note, on Zulip you can format Lean code by enclosing it with  
```
```lean
```
and three backticks at the end.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 07 2019 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154592069):
Oh many thanks David -- I always forget that \forall is super-greedy. Do you know how computer scientists do BIDMAS by the way?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 07 2019 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154594472):
PS did I manage to fix it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Holmes (Jan 07 2019 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154600678):
Yup, looks good (and also the exists one below). I'm almost there, having fun with the final one now... BIDMAS I'm not sure about, but for now I like lots of brackets for certainty!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 07 2019 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604138):
Each piece of notation has a number between 0 and about 1000 attached to it (to both sides of it in the case that it's an infix operator like +)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 07 2019 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604237):
You can see the numbers using `#print notation *` or whatever notation you want to understand

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 07 2019 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604272):
My favourite piece of notation is `$`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 07 2019 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604360):
Away from notation, actual functions given by name have a super high number

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 07 2019 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604397):
You can tell functions from notation because function names are in lower case letters and notation is pretty much everything else

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 07 2019 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604490):
And then you just say "Pratt parser" and all your inputs are resolved by lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 07 2019 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604521):
Functions don't have to be lower case letters. But function application indeed has super high priority

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 07 2019 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604523):
And the CS guys are excited about something in Lean 4 relating to this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 07 2019 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604592):
I think because it will make notation cooler or something

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 07 2019 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604660):
Have you seen the notation for "mod n" is some crazy [ZMOD n] thing? I can't even remember what the notation is, I always have to look it up

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 07 2019 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604719):
Will this be fixed in Lean 4?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 07 2019 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604726):
I had better get back to my talk

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 07 2019 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604915):
The notation for a ≡ b (mod n) when n, a, and b are integers is `a ≡ b [ZMOD n]`, that hardly seems so crazy.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 08 2019 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154609481):
```quote
The notation for a ≡ b (mod n) when n, a, and b are integers is `a ≡ b [ZMOD n]`, that hardly seems so crazy.
```
 Why isn't it just `a ≡ b mod n` ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zans Mihejevs (Jan 08 2019 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154636786):
```quote
The problem is that if you know no Lean at all, even these problems are too hard. You have to install Lean, and then how do you fill in the sorry?
```
 Hmm,  I know someone who co-wrote a book for teaching haskell to complete beginners (Haskell Book). She might be a good person to talk to!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 10 2019 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154832510):
@**David Holmes** complained that the basic logic exercises were too boring :-) [I think in the sense that he felt that the proofs should be done by automation rather than by him]. He liked the canonical nat exercise (defining `+ and `*` and `<` and proving basic stuff about them) at https://xenaproject.wordpress.com/2017/10/31/building-the-non-negative-integers-from-scratch/

That exercise involves building a new structure from scratch and then defining functions on it and proving stuff about it. But the new structure relies on nothing at all. Here is a sketch of how to build the complex numbers, given the real numbers.

https://github.com/kbuzzard/xena/blob/master/lean_together/complex.lean

Here we need to have mathlib installed, so we can have the reals. Actually probably one could get away with axiomatising the reals here and avoiding mathlib, but I did not do this. If we made a new constant called `real` and added an axiom that it was a ring, one should be able to prove that the complexes are also a ring, because really we are constructing $$R[x]/(x^2+1)$$ where $$R$$ is an arbitrary ring.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Holmes (Jan 10 2019 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154863761):
Too boring? Hmm, maybe. I think the problem is that I would have found them painful to do on paper, forgetting lean, because I'm not sure what I should assume and what needs to be proven (for example, it was not immediately clear that I should assume excluded middle, but prove `\not (p \and \not p)`, just because I am not used to working with these things. Certainly I wouldn't be unhappy to have them done by automation! I did find the exercises with the natural numbers much more fun, because I felt I understood what I was aiming for. Occasionally it felt like fighting with the system, but most of the time things just worked as I hoped. May have a go at the complexes soon...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Holmes (Jan 10 2019 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154877253):
Hmm, can I cheat/have a hint? Is there a command to say 'apply the ring structure of the real numbers' without giving every detail? For example, I want to show `re a * re c - im a * im c + (re b * re c - im b * im c) = re a * re c - im a * im c + re b * re c - im b * im c`, which is `immediate' from the fact that \bbR is a commutative ring, but fiddly to prove step by step... Thanks! On the other hand, if this is part of the exercise I'm pretty sure I can do it, but I don't want to :-).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 10 2019 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154877565):
`by ring`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 11 2019 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154899369):
When I do this exercise now David, I write a tactic to do all the work for me :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 11 2019 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154899374):
Ie a tactic which just applies other tactics :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Holmes (Jan 11 2019 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154900247):
Thanks very much, but I'm still doing something wrong. A minimal non-working example with the same error is 
```
import data.real.basic
example : (1 : ℝ) + 2 = 3 := 
begin
by ring, 
end

example (a b c: ℝ) :
(a + b) * c = a * c + b * c := 
begin
by ring, 
end
```
giving the error 

type mismatch at application
  tactic.istep 5 3 5 3 ring
term
  ring
has type
  Type ? → Type ? : Type (?+1)
but is expected to have type
  tactic ?m_1 : Type ?

Kevin's suggestion of writing a tactic sounds sensible, but I think I'm not at that point yet...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154900257):
`import tactic.ring`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154900261):
Or whatever auto-completion makes of that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154900306):
I agree that the error message is cryptic. It would be nicer if it said "tactic ring not found" or something like that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 11 2019 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154900327):
I'm not at a pc right now (indeed I'm waiting for a 51 and am going to be a few minutes late) but I just mean defining a new tactic which strings together other tactics, it's trivial

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154900331):
@**David Holmes**  The problem is: tactics are just a certain kind of types. And now we have two versions of `ring`, living in different namespaces. One is a tactic, and the other is the typeclass that gives ring structure to a `R : Type`. (E.g. the ring structure on the reals). Without importing the tactic, it finds the other one, which confuses Lean, and gives you a cryptic error message.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Holmes (Jan 11 2019 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154900643):
It works, thanks Johan! Kevin, writing tactics to string together others sounds really neat, especially if its trivial :-).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 11 2019 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154900739):
If you want to know what `ring` does (up to "isomorphism of algorithms" :lol:), you should read Kevin's blogpost about it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 11 2019 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154901337):
A small additional note: `by _` is equivalent to `begin _ end`, where `_` is a single tactic. So you can just write `by ring`, or `begin ring end`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Holmes (Jan 11 2019 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154928489):
Hi Kevin, 
In the `complex' exercises, I made it up to and including 
``` 
theorem add_mul (a b c : ℂ) :
(a + b) * c = a * c + b * c := sorry
```
Will try the next ones later. The only thing I needed (other than what you provided) was the line 
```
import tactic.ring
```
and the tactic `by ring`. 

I wonder about more efficient ways to do some of this. I defined addition by 
```
definition add : ℂ → ℂ → ℂ 
| ⟨x1,y1⟩ ⟨x2,y2⟩ := ⟨x1 + x2, y1 + y2⟩
```
then needed things like 
```
lemma re_add (a b : ℂ) : 
re (a + b) = re a + re b:=
begin
have h : a + b = ⟨re(a+b), im(a+b) ⟩, rw eta, 
have ha : a = ⟨ re a, im a ⟩,rw eta, 
have hb : b = ⟨ re b, im b ⟩,rw eta,  
have H : a + b = ⟨re(a) + re(b), im(a+b) ⟩, rw ha, rw hb, 
unfold re, refl, rw H, refl, 
end
```
whose proof was harder than I expected. Then my proof of distributivity was 
```
theorem add_mul (a b c : ℂ) :
(a + b) * c = a * c + b * c := 
begin
apply ext, 
have Hrleft: re ((a+b) * c) = re(a + b)* re(c) - im(a + b) * im(c), 
apply re_mult,  
have Hrright : re(a * c + b * c) = re a * re c - im a * im c + re b * re c - im b * im c, 
have h1 : re(a*c) = re a * re c - im a * im c, apply re_mult, 
have h2 : re(b*c) = re b * re c - im b * im c, apply re_mult, 
rw [re_add], rw[h1], rw [h2], by ring, rw [Hrright], 
have H : re(a + b)* re(c) - im(a + b) * im(c) = re a * re c - im a * im c + re b * re c - im b * im c, 
rw [re_add], rw im_add, by ring, rw [Hrleft], rw H, -- now done with the real component
-- onto the imaginary part
have Hileft : im((a + b) * c) = re (a + b) * im c + re c * im (a + b), 
apply im_mult, 
have Hiright : im(a * c + b * c) = re a * im c + re c * im a + re b * im c + re c * im b, 
have h1 : im(a*c) = re a * im c + re c * im a, apply im_mult, 
have h2 : im(b*c) = re b * im c + re c * im b, apply im_mult, 
rw [im_add], rw[h1], rw [h2], by ring, rw [Hiright], 
have H : re(a + b)* im(c) + re(c) * im(a + b) = re a * im c + re b * im c + re c * im a + re c * im b, 
rw [re_add], rw im_add, by ring, rw [Hileft], rw H, by ring, 
end
```
(attached my code [complex.lean](/user_uploads/3121/W5bzU97AUkl2kyShuTAzZRbM/complex.lean) in case interesting/easier to read). Which was not really so bad, but doing this for every axiom would hurt a bit. 

These proof were all basically computations, so maybe tactic mode was not the best choice? But I am starting to like tactic mode quite a bit. 

I often felt I wanted to start a proof about a complex number `a` by saying 'write `a = x + iy`', but not sure if there is an analogue of that in Lean that functions as I would hope. Working around it got kind of messy, but perhaps that's life. 

[I'm putting this here (and not as a pm to Kevin) in case it is useful to other people, but I don't really know how the forum works so please let me know if I'm spamming!]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 11 2019 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154930105):
Posts like this are fine. Yes, there are better ways, but in my mind these struggles are interesting to go through once, just to make sure you understand what's going on.

https://github.com/leanprover/mathlib/blob/774e7fa39a8513c5c06e27c3e8bf4c124efd9db7/analysis/complex.lean

That was my effort at the time. I wrote a tactic called `crunch` which just did the ring theory I needed.

Defining structures and making them work properly is hard for mathematicians, because mathematicians don't instinctively think to define things like eta and ext.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 12 2019 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154987156):
```lean
theorem add_mul (a b c : ℂ) :
(a + b) * c = a * c + b * c := 
begin
  apply ext,
  { rw [re_add,re_mul,re_add,im_add,re_mul,re_mul],
    ring },
  { rw [im_add,im_mul,re_add,im_add,im_mul,im_mul],
    ring },
end
```
The `ring` tactic can solve a goal of the form `(re a + re b) * re c - (im a + im b) * im c = re a * re c - im a * im c + (re b * re c - im b * im c)` so we just apply the lemmas we know to turn it into a goal of this form. If the lemmas `re_add` etc are all tagged with the `simp` attribute then perhaps instead of the rewrite one could write `suffices : (re a + re b) * re c - blah blah blah, by simp`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 12 2019 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154987800):
```lean
theorem add_mul (a b c : ℂ) : (a + b) * c = a * c + b * c :=
ext
  (show (_+_)*_-(_+_)*_=(_-_)+(_-_), by rw [add_mul, add_mul, add_sub_comm])
  (show (_+_)*_+(_+_)*_=(_+_)+(_+_), by rw [add_mul, add_mul, add_assoc, add_left_comm (b.1*_), ← add_assoc])
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Jan 15 2019 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/155132580):
@**Kevin Buzzard** What's the new link for whatever was at http://wwwf.imperial.ac.uk/~buzzard/lean_together/source/leantogether.html ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/155152962):
Sorry -- link fixed. I added some more (very sketchy) exercises and broke everything in the process.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Holmes (Jan 18 2019 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/156402310):
Thanks Kevin, your proof is very nice - doing in 2 lines what took me 7. Also much easier to read! Moving on to the other cases seems more reasonable now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Holmes (Jan 18 2019 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/156402395):
Kenny, what you wrote looks very neat, but I can't get it to work. I guess i need to add `begin` and `end`, but then I get an error on the first `show`, saying `function expected at
  (λ (this : (?m_5 + ?m_6) * ?m_7 - (?m_10 + ?m_11) * ?m_12 = ?m_15 - ?m_16 + (?m_18 - ?m_19)), this) ?m_20
term has type
  (?m_5 + ?m_6) * ?m_7 - (?m_10 + ?m_11) * ?m_12 = ?m_15 - ?m_16 + (?m_18 - ?m_19)
`.
Any suggestions on what I'm doing wrong?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 18 2019 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/156402574):
I think at that time I couldn't import mathlib so I made up my own complex numbers; the definition of multiplication may have been different (my proof relies heavily on definitional equalities)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/156403084):
doesn't something like `by ext; ring` work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/156403365):
```lean
import data.complex.basic

attribute [extensionality] complex.ext

theorem add_mul' (a b c : ℂ) : (a + b) * c = a * c + b * c :=
by ext; simp; ring
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Holmes (Jan 18 2019 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/156405084):
Hi Mario, 
Thanks for the suggestion. I'm sure that works with the complex numbers in Lean, but this was part of an exercise to construct the complex numbers from the real numbers (so never used `import data.complex.basic`). I just get the usual `simplify tactic failed to simplify`. I think if some of my earlier lemmas had the simp attribute it might also work, but not yet sure how to go about that (and maybe it is not the goal of the exercise).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 19 2019 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/156408900):
You need simp lemmas for addition and multiplication

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 19 2019 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/156408917):
```lean
@[simp] lemma add_re (z w : ℂ) : (z + w).re = z.re + w.re := rfl
@[simp] lemma add_im (z w : ℂ) : (z + w).im = z.im + w.im := rfl
@[simp] lemma mul_re (z w : ℂ) : (z * w).re = z.re * w.re - z.im * w.im := rfl
@[simp] lemma mul_im (z w : ℂ) : (z * w).im = z.re * w.im + z.im * w.re := rfl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 19 2019 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/156408984):
of course you can prove the theorem by `add_mul` since this is already proven in `data.complex.basic`, but if you are rewriting it on your own you want `complex.ext` and these re/im lemmas and then everything should follow by `ring` like I said

