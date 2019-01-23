---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/09895noobquestion.html
---

## Stream: [new members](index.html)
### Topic: [noob question](09895noobquestion.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Sep 04 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133315850):
Hello! Very new to Lean and logic in general;  i'm interested in how i can find the function names that i might need for various deduction steps (e.g. `and.intro`), since the std/maths library sections of "theorem proving in lean" are empty :anguished: in particular, i want to go from `¬p → false` to `p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 04 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133316001):
https://github.com/leanprover/lean/blob/master/library/init/classical.lean#L160

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 04 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133316038):
This is in directory init of the core library, so you don't have to import anything, but it's in namespace `classical` so you need either open the namespace or use the full name

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 04 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133316044):
Welcome to Lean! Figuring out the names of lemmas etc is still a bit of a dark art. Most of us are learning by asking lots of questions here. So feel free to ask more :smiley:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 04 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133316100):
Yes, welcome, and don't let constructivist Kenny scare you!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 04 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133316111):
Also, don't mind about Kenny. He doesn't like the stuff in `classical.lean`. But he's a nice guy if you ignore that bit :rolling_on_the_floor_laughing:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 04 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133316199):
See also [this discussion in the book "Logic and Proof"](http://avigad.github.io/logic_and_proof/classical_reasoning.html).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 04 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133316422):
There's a subtle difference between constructive mathematics and constructive pedagogy.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 04 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133316638):
But more generally, if you're looking for theorems that follow a particular pattern, you can try the `#find` command. e.g. 
```lean
import tactic.find
#find  (¬ _ → false) → _
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Sep 04 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133316668):
Oh, that book looks great, maybe it should also be visible in the "Documentation" section of leanprover.github.io . I'll definitely give it a go! I came across this while trying to prove de morgan both ways, and turns out classical is indeed required :) https://math.stackexchange.com/questions/120187/do-de-morgans-laws-hold-in-propositional-intuitionistic-logic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 04 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133316690):
You can PR that book to the documentation of mathlib, if you want (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Sep 04 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133319056):
How horrible is this proof? :mischievous:

```lean
variables p q : Prop

theorem de_morgan_1_a (hnpnq: ¬p ∨ ¬q): ¬(p ∧ q) :=
  assume (hpq: p ∧ q),
  or.elim hnpnq
    (assume hnp: ¬p,
      show false, from hnp hpq.left)
    (assume hnq: ¬q,
      show false, from hnq hpq.right)

-- only provable within classical logic!
theorem de_morgan_1_b (hnpq: ¬(p ∧ q)): ¬p ∨ ¬q :=
  classical.by_contradiction
    (assume not_conclusion: ¬(¬p ∨ ¬q),
      have hpq: p ∧ q, from and.intro
        (show p, from classical.by_contradiction
          (assume hnp: ¬p,
            not_conclusion (show ¬p ∨ ¬q, from or.intro_left (¬q) hnp)))
        (show q, from classical.by_contradiction
          (assume hnq: ¬q,
            not_conclusion (show ¬p ∨ ¬q, from or.intro_right (¬p) hnq))),
      show false, from hnpq hpq)

theorem de_morgan_1: ¬(p ∧ q) ↔ ¬p ∨ ¬q :=
  -- annpoying having to specify p and q
  iff.intro (de_morgan_1_b p q) (de_morgan_1_a p q)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133319479):
it's alright

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 04 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133319596):
In the last theorem, you can use underscores instead of p's and q's if you want.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133319665):
It's so much easier and nicer to do it in tactic mode if you're going to spell it all out like this:

```lean
variables p q : Prop

theorem de_morgan_1_a (hnpnq: ¬p ∨ ¬q): ¬(p ∧ q) :=
begin
  intro hpq,
  cases hnpnq with hnp hnq,
  { apply hnp,
    exact hpq.left},
  { apply hnq,
    exact hpq.right}
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133319673):
You can see where you're going!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133319764):
If you're going to do it in term mode you may as well just do

```lean
variables p q : Prop

theorem de_morgan_1_a (hnpnq: ¬p ∨ ¬q): ¬(p ∧ q) :=
λ hpq, or.elim hnpnq (λ hnp, hnp hpq.1) (λ hnq, hnq hpq.2)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133319796):
yeah but you've already known Lean for a year

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133319938):
Kenny can you golf `de_morgan_1_b`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133319954):
oh it will already be in mathlib I guess

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Sep 04 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133320201):
Thanks for the feedback! Haven't quite grasped tactics yet, so doing things explicitly for now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133320295):
tactics are the bomb if you're a learner. I don't know why they leave them so late in TPIL.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133320299):
```lean
theorem de_morgan_1_a (hnpnq: ¬p ∨ ¬q): ¬(p ∧ q)
| ⟨hp, hq⟩ := or.elim hnpnq (absurd hp) (absurd hq)
```
Mathlib's proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133320304):
Absolutely terrifying for beginners :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133320377):
The theorem is supposed to be constructing a proof of false from a proof of `p and q`, so the equation compiler matches the proof of `p and q` with a proof of p and a proof of q and then it's pretty much the same as before.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133320508):
re: specifying p and q. How about this?

```lean
variables {p q : Prop} -- trick for making variables implicit

theorem de_morgan_1_a (hnpnq: ¬p ∨ ¬q): ¬(p ∧ q) :=
  assume (hpq: p ∧ q),
  or.elim hnpnq
    (assume hnp: ¬p,
      show false, from hnp hpq.left)
    (assume hnq: ¬q,
      show false, from hnq hpq.right)

-- only provable within classical logic!
theorem de_morgan_1_b (hnpq: ¬(p ∧ q)): ¬p ∨ ¬q :=
  classical.by_contradiction
    (assume not_conclusion: ¬(¬p ∨ ¬q),
      have hpq: p ∧ q, from and.intro
        (show p, from classical.by_contradiction
          (assume hnp: ¬p,
            not_conclusion (show ¬p ∨ ¬q, from or.intro_left (¬q) hnp)))
        (show q, from classical.by_contradiction
          (assume hnq: ¬q,
            not_conclusion (show ¬p ∨ ¬q, from or.intro_right (¬p) hnq))),
      show false, from hnpq hpq)

theorem de_morgan_1: ¬(p ∧ q) ↔ ¬p ∨ ¬q :=
  -- no longer annpoying
  iff.intro (de_morgan_1_b) (de_morgan_1_a)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Sep 04 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133320865):
Oh, that's nice! I missed that they can be made implicit globally
re: mathlib, i'll just quote TPIL: "Once again, you should exercise judgment as to whether such abbreviations enhance or diminish readability."

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133320883):
Instead of assuming classical logic, mathlib (in `logic/basic.lean`) just assumes decidability of `p`:

```lean
theorem de_morgan_1_b (hnpq: ¬(p ∧ q)) [decidable p] : ¬p ∨ ¬q :=
if hp : p then or.inr (λ hq, hnpq ⟨hp, hq⟩) else or.inl hp

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133320908):
my impression is that mathlib is not meant to be readable, they are looking for speed and breadth

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Sep 04 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133321554):
Hm, more noob questions, what's the difference between classical logic and "decidable p"? Since LEM states that p is either true or false, isn't that effectively "p is decidable"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133321628):
Here's a classical proof.
```lean
theorem de_morgan_1_b (hnpq: ¬(p ∧ q)) : ¬p ∨ ¬q :=
or.elim (classical.em p) (λ hp, or.inr $ λ hq, hnpq ⟨hp, hq⟩) or.inl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 04 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133321649):
Not quite, em means you know p is either true or false, decidable means you know which one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133321663):
The classical proof gives this:
```lean
#print axioms de_morgan_1_b 
/-
classical.choice
quot.sound
propext
-/
```

The decidable proof uses no "maths axioms"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133321725):
As Chris says, assuming decidability is slightly stronger.  But to a mathematician like me they're all the same.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133321740):
Furthermore they're all assumable without any worries :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/133321778):
Johannes Hoelzl once argued that trying to write as small proofs as possible was a good exercise.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) zaa (Sep 29 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134895335):
Hello! Is there some way to use Lean without emacs or VisualStudio? Asking for CoqIde-like editor would be probably too much, but maybe there's some way to use Notepad or command line?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 29 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134895390):
Sure, you can use command line, after editing your file in any editor you like

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134895434):
you can always use any editor to edit the file and then `lean --make` the file, although you won't be able to interact easilier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Olson (Sep 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134895437):
In case you're not familiar, the Lean reference manual recommends use with Visual Studio Code, which is actually a completely separate IDE from Visual Studio, which is cross platform, simpler, etc. I personally find the experience using Lean in VSCode similar to using CoqIde

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134895439):
(why isn't easilier a word?)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) zaa (Sep 29 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134895493):
Ok, then I will both try  Visual Studio Code and get used to `lean --make`.
Thank you!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 29 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134895899):
I'm not sure lean --make will be much fun, but I could imagine it would work. Two other possibilities are the Lean Web Editor, and CoCalc; these are both web-based ways to run Lean. I use unix and am quite anti-MS software in general (and they typically don't target my platform anyway) but actually I've had a very positive experience using VS code in linux. Emacs runs in a terminal window.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) zaa (Sep 29 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134896721):
> Lean: Error: Command failed: lean --version 'lean' is not recognized as an internal or external command, operable program or batch file.
 
Trying to run Lean extension in VSCode. I have added both necessary paths to PATH, but, it seems, i'm missing something else.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134896868):
maybe you have a space in your path

#### [![Click to go to Zulip](../../assets/img/zulip2.png) zaa (Sep 29 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134897137):
It's working now, yay. I just closed and reopened VSCode.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 30 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134897811):
```quote
(why isn't easilier a word?)
```
I think it's because it's an adverb not an adjective. Off the top of my head, I can't think of any English adverbs that can be suffixed with -er.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) zaa (Sep 30 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134918464):
Does Lean have a tactic similar to Omega in coq?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 30 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134918538):
I believe the answer is "not yet". I know nothing about Coq but I've heard people talk about Omega. Can you briefly describe what it does? Another noob question :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 30 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134918579):
We have `linarith` and `cc`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 30 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134918645):
I think omega is `cooper`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) zaa (Sep 30 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134918695):
It solves goals in Presburger arithmetic. Equalities containing only addition and substraction (and multiplication by constant, ofc).
 
For example: 8n = 4m+3 -> False

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 30 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134918764):
what do you use it for? is it just divisibility goals like that one?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) zaa (Sep 30 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134918822):
Oh, it seems to work with inequalities too. Will test on Coq a bit, as I have already forgotten things.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 30 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134918871):
no, my question is when do you think "I should use omega"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 30 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134918911):
I know about presburger arithmetic but I think it's probably a bit too wide a target - I doubt people really need the crazy quantifier complexity part

#### [![Click to go to Zulip](../../assets/img/zulip2.png) zaa (Sep 30 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134918966):
https://coq.inria.fr/refman/addendum/omega.html - found the documentation.
There's an example:
z > 0 -> 2 * z + 1 > z
 
As far as i can remember, I mostly used it for goals like
[inequality/equality] -> [another one] -> x = something
or A <= x <= B
or maybe False

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 30 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134919013):
`cooper` is a tactic for presburger arithmetic written in lean by Seul Baek, but I don't think it is ready for production

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 30 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134920434):
```quote
https://coq.inria.fr/refman/addendum/omega.html - found the documentation.
```
Oh thank you! I know nothing about Coq or where to look for this stuff.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) zaa (Sep 30 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134936881):
Yes, that's the website where it lives. I had fun with Coq for some time but paused it some year ago (will return to it soon, probably simultaneously to more serious lean learning).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) zaa (Sep 30 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134937308):
Next noob question:
Is there some simple example/tutorial of quotient types - how to define and use them?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 01 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134937617):
There is a section in TPIL: https://leanprover.github.io/theorem_proving_in_lean/axioms_and_computation.html#quotients

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 01 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134937730):
For a real-world example you can take a look at `linear_algebra.quotient_module`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) zaa (Oct 01 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134937793):
Thank you!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134939308):
https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching.20use.20of.20quotients.20in.20Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/134939327):
I wrote https://github.com/kbuzzard/xena/blob/master/xenalib/m1f/zmod37.lean specifically to help some of my students to learn about using quotients in Lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Oct 24 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136428236):
Using my old thread for more noob questions:
Can I use something like `cases` but without stating the hypothesis name? Namely, I'd like a tactic that splits conjunctions into two hypotheses and disjunctions into two goals. More generally, how does one go about searching for tactics that do something?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 24 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136428440):
`split` will split goals.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Oct 24 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136428479):
Yep, sorry I should've specified - I want to split hypotheses.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 24 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136428496):
Like `have h1 := h.left, have h2 := h.right`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 24 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136428503):
And now you want to do that automatically for all hypotheses, recursively?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 24 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136428549):
`cases` does both of those things already, so I guess you mean something that applies `cases` automatically?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Oct 24 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136428563):
Yep, that would be for ANDs, but without stating what the name is, and also do it for ORs (in which case two  or more goals would appear). Yep, automatically and recursively.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 24 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136428584):
I think the answer to the more general question is "read through https://github.com/leanprover/mathlib/blob/master/docs/tactics.md, and then look through `tactic.interactive` in mathlib and more generally the rest of `tactic.*` to find more things"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 24 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136428667):
`tidy` does things like this; it tries a bunch of different tactics in a loop, one of which is `auto_cases`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Oct 24 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136428862):
That looks about right, thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 24 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136429144):
`safe` will do this, and a bit more. I think it should be less aggressive than `tidy`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Oct 24 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136430875):
Oh damn, it just solves everything by itself O.o

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Oct 26 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/136531665):
c.f. `auto_cases`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Nov 03 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137094276):
More questions!
What's the syntax for matching on inductive constructors by name? E.g. for list, something like `Nil => 0, Cons(hd, tl) => 1 + (len tl)` would be a Rust way to define `len` recursively

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 03 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137094949):
Do you mean something like this?
```lean
def len : list α → ℕ
| list.nil := 0
| (list.cons a b) := 1 + len b
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Nov 03 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137095066):
Yep that's it - thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Nov 03 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137121205):
Ignore me, mixed up my languages.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Nov 03 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137123573):
Is there any reason why `fin` and `multiset` don't support the `{1, 2, 3}` notation that `set` does? What's the best way to construct concrete `finset`s?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 03 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137123629):
Do you want a type or a set?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 03 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137123686):
You need `decidable_eq α` to use that notation for `finset α`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 03 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137123713):
For multisets this works for me without any decidability assumptions

```lean
example {α : Type*} (a b c : α) : multiset α := {a,b,c}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Nov 03 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137123720):
@**Johan Commelin** a concrete set, say `{v}` for some given `v: \a`
@**Chris Hughes** ah indeed, why does `set` not require it then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 03 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137123840):
They notation is for `has_insert.insert` 
For sets `insert a s := {b : α | b = a ∨ b ∈ s}`, and there's no decidable equality required.

For finsets, there has to be an underlying list with no duplicates, so it has to check whether `a` is already in the set, which requires `decidable_eq`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Nov 03 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137125503):
Then given a singleton set, how can I extract the element? I tried folding it into a list to grab the first element, but `fold` requires commutativity and `list.append` is not commutative.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 03 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137125773):
Do you have a proof that it's a singleton? I think there's a PR about finite unique computable choice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Nov 03 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137125848):
Yeah, i'm grabbing it under the assumption that `card vals = 1`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 03 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137126149):
do you need it to be computable? You can use `finset.exists_mem_of_ne_empty` if you don't. Do you need the fact that everything in the singleton is equal?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Nov 03 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137126804):
I think `exists_mem_of_ne_empty` will work. thx!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Nov 03 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137127553):
So now i'm seeing a really strange error when trying to decompose the `Exists`:
```lean
constant α: Type
constant a: α
constant as: finset α
#check a ∈ as -- Prop
constant ex : ∃ (a : α), a ∈ as
def test := match ex with ⟨a, b⟩ := -- induction tactic failed, recursor 'Exists.dcases_on' can only eliminate into Prop
  0
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 03 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128633):
The recursor only eliminates into prop and your goal is a type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 03 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128637):
so the recursor cannot be applied

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Nov 03 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128659):
Yep, I just realised this. Basically, i'm trying to extract a concrete value of the type `\a` from a proof of existence. But I guess this could only work in purely constructionist logic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 03 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128709):
There are tools in the classical namespace which should let you do this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 03 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128711):
You shouldn't use constants by the way, you should use variables -- they work a bit better and there's less risk

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Nov 03 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128760):
Oh yeah, that was just to make the example code short

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 03 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128774):
It should be possible to define the function you want constructively, but it hasn't been done yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 03 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128815):
```lean
import data.finset
variable {α: Type}
variable {a: α}
variable {as: finset α}
#check a ∈ as -- Prop
variable ex : ∃ (a : α), a ∈ as
noncomputable def test : α := classical.some ex
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 03 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128832):
Right -- this noncomputable approach works for any existence statement. But I now understand that in the specific case of finsets you might be able to do better.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 03 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128834):
[This is the relevant PR](https://github.com/leanprover/mathlib/pull/421), right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 03 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137128879):
```lean
import data.finset

variables {α : Type} {a : α} {as : finset α} (ex : ∃ (a : α), a ∈ as)

noncomputable def test : α := classical.some ex
```
Shorter and no constants ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Nov 03 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137129014):
Also works with `constants`, but fair enough :)
Anyhow, I need it to be computable because I want to extract concrete elements from concrete sets and do things with them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 03 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137129717):
something that almost works:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 03 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137129718):
```lean
import data.finset

lemma list.perm_singleton {α : Type*} {L : list α} {x : α} (H : L ~ [x]) : L = [x] :=
begin
  generalize_hyp hs : [x] = S at H ⊢,
  induction H,
  case list.perm.nil { refl },
  case list.perm.skip : y L₁ L₂ H ih {
    cases hs, cases list.perm_nil.1 H, refl
  },
  case list.perm.swap { injections },
  case list.perm.trans : L₁ L₂ L₃ H12 H23 ih1 ih2 {
    cases hs, cases ih2 rfl, cases ih1 rfl, refl
  }
end

def extract {α : Type*} (s : finset α) (hs : s.card = 1) : α :=
finset.rec_on s
  (λ m, quotient.hrec_on m
    (λ L _, list.cases_on L
      (assume hcard : 0 = 1, absurd hcard dec_trivial)
      (λ hd tl hcard, hd))
    (λ L₁ L₂ HL, function.hfunext (congr_arg _ $ quotient.sound HL) $
    λ hnd1 hnd2 hheq, begin
  cases L₂,
  case list.nil { cases list.perm_nil.1 HL, refl },
  case list.cons : hd₂ tl₂ {
    cases L₁,
    case list.nil { cases list.perm_nil.1 (list.perm.symm HL) },
    case list.cons : hd₁ tl₁ {
      apply function.hfunext,
      { simp only [finset.card_def, multiset.card],
        rw quotient.sound HL },
      intros hcard₁ hcard₂ hheq,
      cases multiset.card_eq_one.1 hcard₁ with x₁ hx₁,
      cases multiset.card_eq_one.1 hcard₂ with x₂ hx₂,
      cases list.perm_singleton (quotient.exact hx₁),
      cases list.perm_singleton (quotient.exact hx₂),
      cases list.perm_singleton HL,
      refl
    }
  }
end)) hs
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 03 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137129720):
@**Chris Hughes** can you fix this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 03 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137130012):
```lean
example {α : Type*} (s : finset α) : s.card = 1 → {a : α // s = finset.singleton a} :=
finset.rec_on s (λ s, @quotient.rec_on_subsingleton _ _
  (λ t : multiset α, Π (nodup : multiset.nodup t),
    finset.card {val := t, nodup := nodup} = 1 → {a // finset.mk t nodup = finset.singleton a}) 
      (λ l, ⟨λ a b, funext (λ x, funext (λ y, subtype.eq $ finset.singleton_inj.1 $ 
        by rw [← (a x y).2, ← (b x y).2]))⟩) s
  (λ l, list.rec_on l (λ _ h, nat.no_confusion h) 
    (λ a l _ _ h, have l.length = 0, from nat.succ_inj h, 
      ⟨a, finset.eq_of_veq $ by dsimp; rw [list.length_eq_zero.1 this]; refl⟩)) )
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 03 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137130013):
Not very pretty

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 03 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137130057):
```lean
import data.finset

lemma list.perm_singleton {α : Type*} {L : list α} {x : α} (H : L ~ [x]) : L = [x] :=
begin
  generalize_hyp hs : [x] = S at H ⊢,
  induction H,
  case list.perm.nil { refl },
  case list.perm.skip : y L₁ L₂ H ih {
    cases hs, cases list.perm_nil.1 H, refl
  },
  case list.perm.swap { injections },
  case list.perm.trans : L₁ L₂ L₃ H12 H23 ih1 ih2 {
    cases hs, cases ih2 rfl, cases ih1 rfl, refl
  }
end

def extract {α : Type*} (s : finset α) (hs : s.card = 1) : α :=
finset.rec_on s
  (λ m, quotient.rec_on m
    (λ L _, show L.length = 1 → α, from list.cases_on L
      (λ H, absurd H dec_trivial)
      (λ hd tl H, hd))
    (λ L₁ L₂ HL, begin
  ext H1 H2, rcases list.length_eq_one.1 H2 with ⟨x₂, rfl⟩,
  cases list.perm_singleton HL, refl
end)) hs
```
my version

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 03 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137130058):
well yours is much shorter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 03 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137130070):
clever use of subsingleton...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 03 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137130125):
```lean
theorem extract_mem {α : Type*} (s : finset α) (hs : s.card = 1) :
  extract s hs ∈ s :=
begin
  induction s with m _,
  rcases m with L,
  cases L with hd tl, { cases hs },
  left, refl
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 03 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137130137):
@**Wojciech Nawrocki** so we have 2 solutions now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 03 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137130139):
(i.e. mine and Chris's solution)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Nov 03 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/137130206):
Oh wow, these are quite complex! I wonder if i should have just used lists instead :P but thanks a lot

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 06 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/146838268):
related: https://github.com/leanprover/mathlib/pull/421

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Nov 09 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147370525):
When a goal contains a reducible definition, how can i expand it to work with the internals? Namely, in here:
```lean
  @[reducible]
  def compose_partial (f₁: α → option β) (f₂: β → option γ)
    : α → option γ :=
  (λ a: α, option.cases_on (f₁ a) none (λ x, f₂ x))

  notation [parsing_only] a `⬝ₚ` b := compose_partial b a

  theorem compose_none (f₁: α → option β) (f₂: β → option γ) (x: α) (h: f₁ x = none)
    : (f₂ ⬝ₚ f₁) x = none :=
  begin
    sorry
  end
```
I would like to expand `compose_partial` to carry through the `none` and get back a `none`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Nov 09 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147370813):
You can use `unfold compose_partial`. `simp [compose_partial]` or `dsimp [compose_partial]` can also be useful.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Nov 09 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147370896):
Ah, `unfold`. Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147375089):
`@[reducible]` means that the typeclass system will automatically unfold it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147375094):
but only the typeclass system

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Nov 17 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147889775):
How can I make an instance of a dependent product `(x, p x)` where `p` is some proposition depending on `x`? Lean complains about impredicativity:
```lean
type mismatch at application
  (n, h)
term
  h
has type
  n = 4 : Prop
but is expected to have type
  ?m_1 : Type ?
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 17 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147889850):
use `subtype`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 17 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147889862):
If you're using `prod`, it won't work because it's non dependent and it doesn't accept Propositions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 17 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147889863):
Parentheses are only for `prod`, yeah

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Nov 17 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147890136):
Oh I see, thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 17 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147890301):
`prod` is non-dependent `sigma`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 17 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147890303):
but if it's proposition then you're better off using `subtype` which is a sort of specialize `sigma`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Nov 18 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147932778):
Given an inductive type with some variants that take arguments, e.g.
```lean
inductive Foo: Type
| A : nat -> Foo
| B: Foo
```
Is there a better way of saying that a particular `x: Foo` was constructed by `A` regardless of what the argument was than `\ex n: nat, x = A n`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 18 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147933315):
I don't think so. "x was constructed by A and I don't know what the argument was" is *exactly* `\ex n: nat, x = A n`, right? What's wrong with this way of saying it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 18 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147933417):
Other approaches
```lean
def p : foo → Prop
| (A n) := true
| B     := false

inductive p : foo → Prop
| bar : p (A n)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 18 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147933471):
That first one is a much better way :-) I don't understand the second one!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Nov 18 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147933521):
Hm, I guess it might just be nice to have a shorthand like `p` in Chris's example for when the constructor is unwieldy, e.g. has lots of arguments. `p` would sound better as e.g. `is_A`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Nov 18 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147933522):
The second one is an inductive proposition. I think you need `inductive` instead of `def`. This seems like the "canonical" way to me, and you can easily prove it equivalent to one using exists.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 18 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147933585):
The inductive one gives you a nice recursor.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 18 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147934065):
Is there another typo in the second one? I'm trying to figure out how to use it and I'm getting `unknown identifier 'n'`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Nov 18 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147934438):
It should look like
```lean
inductive Foo : Type
| A : nat -> Foo
| B: Foo

inductive Foo.is_A : Foo → Prop
| of_A (n) : Foo.is_A (Foo.A n)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Nov 18 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147934446):
The idea being, `Foo.is_A` is a family of propositions. For any `n : nat`, `Foo.is_A.of_A n` is a proof of `Foo.is_A (Foo.A n)`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 18 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question/near/147934510):
Thanks! I'd tried adding `n` after `bar` and I forgot that the parentheses were necessary.


{% endraw %}
