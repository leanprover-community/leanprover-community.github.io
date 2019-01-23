---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04817Problemswithprovingaddrightcancel.html
---

## Stream: [general](index.html)
### Topic: [Problems with proving add_right_cancel](04817Problemswithprovingaddrightcancel.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Nov 28 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148741055):
Hi folks, I'm a beginner at lean and I was trying my hand at proving one of the arithmetic identities, `add_right_cancel`. Here's my attempt (please note this is done within a hidden namespace so it does not conflict with the usual definition):

```lean
theorem add_right_cancel (n m k : nat) : n + k = m + k → n = m :=
nat.rec_on k
    (assume h : n + 0 = m + 0,
        show n = m, from calc
            n = n + 0 : by rw add_zero
          ... = m + 0 : by rw h
          ... = m     : by rw add_zero)
    (assume k,
        assume ih : n + k = m + k → n = m,
        assume h : n + succ k = m + succ k,
        have s1 : (n + succ k = m + succ k) = (n + k = m + k), from calc
            (n + succ k = m + succ k) = (succ (n + k) = succ (m + k)) : by rw [add_succ, add_succ]
                                  ... = (n + k = m + k) : by simp,
        show n = m, from ih (s1 ▸ h))
```

There are a few problems here. One is that it doesn't type check. I get the following error:

```
[Lean]
"eliminator" elaborator type mismatch, term
  λ (h : n + 0 = m + 0),
    show n = m, from
      eq.trans
        (eq.trans (eq.mpr (id (eq.rec (eq.refl (n = n + 0)) (add_zero n))) (eq.refl n))
           (eq.mpr (id (eq.rec (eq.refl (n + 0 = m + 0)) h)) (eq.refl (m + 0))))
        (eq.mpr (id (eq.rec (eq.refl (m + 0 = m)) (add_zero m))) (eq.refl m))
has type
  n + 0 = m + 0 → n = m
but is expected to have type
  (?m_3 * ?m_4 = ?m_5 * ?m_4 → ?m_3 = ?m_5) → n + 0 = m + 0 → n = m
Additional information:
/Users/lyle/Sync/devel/lean/logic_and_proof/ch18-exercises.lean:95:0: context: the inferred motive for the eliminator-like application is
  λ (_x : ℕ), (?m_3 * ?m_4 = ?m_5 * ?m_4 → ?m_3 = ?m_5) → n + _x = m + _x → n = m
nat.rec_on : ∀ {C : ℕ → Prop} (n : ℕ), C 0 → (∀ (n : ℕ), C n → C (succ n)) → C n
```

Clearly this relates to the base case of the induction. I'm not sure what it's missing, though. 

As for the inductive step, it seemed a bit awkward that I had to have nested equalities in the calc mode, but perhaps that's normal? I suppose I can prove a hypothesis and then apply an equivalence using `▸`, e.g. `from add_succ ▸ h1`?

Then, I didn't like the fact that I had to use the `simp` strategy. Perhaps that's fine normally but for this exercise I wanted to be more explicit. It seems that `succ.inj` ought to apply, but I can't figure out how to apply it. I can't use that as a rewrite rule because it's an implication, not an equivalence.

Finally, it bugged me that I had to have that last line to make the `s1` substitution within `h`. Because in the calc mode I've only proven `(n + succ k = m + succ k) = (n + k = m + k)`, so I have to take an extra step outside of calc mode to get `n = m`. I feel that perhaps I'm going about this the wrong way.

Any tips? Thanks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 28 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148741455):
It typechecks for me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 28 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148741515):
Do you maybe have a `mul_right_cancel` on the line following this theorem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 28 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148741587):
I don't like how you use `calc` for equality of propositions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 28 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148741644):
```lean
theorem add_right_cancel (n m k : nat) : n + k = m + k → n = m :=
nat.rec_on k id $ λ k ih h, ih $ succ_inj h
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 28 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148741673):
You can probably replace all the equalities between equations with `\iff`s

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 28 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148741739):
and the weird triangle with `s1.mp h`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 28 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148742052):
```quote
Do you maybe have a `mul_right_cancel` on the line following this theorem?
```
 Top Lean tip : stick `#exit` directly after the code you're writing, and make sure there are no red errors earlier in the file -- any random stuff before or after your code can interfere with your code.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Nov 28 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148744233):
@**Kenny Lau** , @**Mario Carneiro**: Ah yes, you're right it does type check. When I copy-pasted it, I noticed it had an extra `mul_right_cancel` at the end and thought I had just made a mistake in copying it. But the mistake was there in the source file, and when I got rid of that, it type checked.

And I don't like how I use `calc` for equality of propositions, either. Wondering how I can reformulate that.

@**Reid Barton** : I will try using `\iff`s, thanks. Weird triangle? It's `\t` and is used for substituting via equivalences. I learned that from *Logic & Proof*. E.g. if you have `h1 : s = t` and `h2: s * x  = 4` you can derive `have t * x = 4, from h1 ▸ h2`. Haven't heard of `.mp`, I'll try that, thanks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 28 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148744246):
@**Lyle Kopnicky** did you see my one-liner?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Nov 28 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148744336):
@**Kenny Lau** Ah I missed that, it was so short. Thanks. I'll try that out. I may want to expand a bit because for pedagogical reasons I want to be able to see the steps.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 28 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148744872):
I think tactic mode is much better for seeing the steps. Here's my effort:

```lean
import tactic.interactive -- to get simpa

namespace random

open nat

theorem add_right_cancel (n m k : nat) : n + k = m + k → n = m :=
begin
  induction k with k ih,
  { -- base case
    exact id, -- n = n + 0 is true by definition
  },
  { -- inductive step
    show succ (n + k) = succ (m + k) → _, -- again true by definition
    intro H,
    apply ih,
    simpa using H
  }
end

end random
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 28 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148744972):
```lean
namespace random

open nat

meta def add_right_cancel (n m k : nat) : n + k = m + k → n = m :=
add_right_cancel

end random
```
lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Nov 28 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148746236):
Thanks, folks. I guess there are some steps in there that seem a little too magic to me.

E.g., `succ_inj` is being applied to `n + succ k = m + succ k` but it's supposed to be applied to something of the form `succ a = succ b`. So how does it get from `n + succ k = m + succ k` to `succ (n + k) = succ (m + k)`? This is where I was trying to apply `succ_add` twice to make that transformation. But I guess since that's part of the definition of `succ`, it's considered definitionally equivalent and doesn't need a proof step. For a beginner it's a little hard to follow when multiple steps are happening at the same time.

Similarly with the leap from `n + 0 = m + 0` to `n + m`. I guess there's no proof step because it's just a definitional equivalence.

What about when you really *do* need to make substitutions (`eq.subst`) on both sides of the equation?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 28 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148746273):
it's not definiton of `succ`, it's definition of `+`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Nov 28 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148746289):
Ah, right.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 28 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148746387):
what's your background?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 28 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148746555):
```lean
namespace random

open nat

theorem add_right_cancel (n m k : nat) : n + k = m + k → n = m :=
nat.rec_on k
  (assume h : n + 0 = m + 0, calc
      n = n + 0 : by rw add_zero
    ... = m + 0 : h
    ... = m     : by rw add_zero)
  (assume k : ℕ,
    assume ih : n + k = m + k → n = m,
    assume h : n + succ k = m + succ k,
    have succ (n + k) = succ (m + k), from calc
          succ (n + k)
        = n + succ k   : by rw add_succ
    ... = m + succ k   : h
    ... = succ (m + k) : by rw add_succ,
    show n = m, from ih (succ_inj this))

end random
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 28 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148746594):
Kevin, using `simpa` in this situation is cheating, it probably uses `simp` lemmas of the same level as what we try to prove by hand

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Nov 28 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148746600):
BS and MS in computer science, have done a lot of Haskell programming, have done quite a few proofs by hand but have been working through *Logic & Proof* and learning how to do proofs with a proof assistant.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 28 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148746758):
Lyle, if you want to see more explicitly where definitional equality is used, you can try to follow that version:
```lean
theorem add_right_cancel (n m k : nat) : n + k = m + k → n = m :=
begin
  induction k with k ih ; intro h,
  { -- base case
    exact h -- n = n + 0 is true by definition
  },
  { -- inductive step
    change succ (n + k) = succ (m + k) at h, -- again true by definition
    apply ih,
    exact succ_inj h
  }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 28 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148746839):
When you call `exact` and see what `h` looks like in the info view, you see what defintional reduction occurred. Same with the `change` tactic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 28 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148746853):
I also used `;` to do `intro h` in both cases

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 28 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148746880):
Definitional equality vs usual equality is clearly the single most confusing point of type theory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 28 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148746889):
you'll need time to get used to it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Nov 28 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747036):
@**Kenny Lau** , I see, nice trick, using `h` in the middle of the `calc`. Thanks.

@**Patrick Massot** : I haven't really gotten into tactic mode yet. Trying to do proofs without tactics at first because that's closer to how they are proven by hand. Once I get comfortable with that I will move on to tactics. I know, I'm using them a bit with `by rw`.

I'll load your example up in the editor though and hover the cursor over things and see what happens. I'm using VS Code. Thanks for the pointers.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 28 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747145):
```quote
 Trying to do proofs without tactics at first because that's closer to how they are proven by hand.
```
 This may be the weirdest thing I read on this chat. I guess it's the background difference (CS vs pure maths training)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Nov 28 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747191):
Hmm, I can hover over the tactic names and get nice detailed description of what the tactic means. But I don't have an "info view".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 28 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747204):
Ctrl-Shift-Enter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Nov 28 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747210):
One reason I'm studying Lean instead of Coq is because all the training materials for Coq seem to use tactics right away. I can't follow what's going on in the proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 28 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747222):
And suddenly you'll discover why tactic mode is *way easier* than term mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 28 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747246):
Tactic mode proofs can be hard to read without the view you just unlocked with Ctrl-Shift-Enter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 28 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747306):
But with this view they are infinitely easier to read

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Nov 28 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747366):
Yeah, I want to be able to read them off a piece of paper or a text file, without having to use a special viewer.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Nov 28 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747379):
But I'll give it a try

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Nov 28 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747442):
I'm used to reading proofs out of textbooks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 28 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747485):
It's very difficult to write proofs in Lean that are readable on paper and, unfortunately, this is not at all a goal of mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 28 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747507):
It's doable, but pretty verbose

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Nov 28 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747616):
I have taken a lot of math classes but we always did proofs on paper too.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 28 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747627):
> I'm used to reading proofs out of textbooks.

Proofs in textbooks explain the steps (just like a tactic proof). The idea that there is a "proof term" is pretty alien to most mathematicians. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 28 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747691):
Mathematicians' paper proofs do use `show` a lot ("Next, we need..."), and this makes a big improvement in readability.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Nov 28 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747735):
By "proof term" you mean the goal that we are trying to prove? My understanding is that the tactic proofs work backwards from the goal. I'm used to working forwards from the hypotheses.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 28 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747738):
The thing which could be readable would be a sequence of `have` and `suffices` stating all steps that would be mentioned on paper, with automation crushing the proof of each step. But automation is not ready yet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 28 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747755):
No, you don't have to go backward in tactic mode, both directions are allowed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Nov 28 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747794):
OK, interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 28 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747816):
And I think you use backward reasoning on paper more than you are aware

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 28 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747837):
Working backwards means using the `apply` tactic, but there are other tactics!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 28 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747840):
Especially when you write "We can now apply the ... theorem because ..." (first naming the theorem and then explaining why assumptions are satisfied)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 28 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148747845):
And indeed this is the `apply` tactic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Nov 28 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148749147):
I would think you could still write that in forward mode by writing:

`the_theorem h1 h2 h3 h4`

But maybe I am still too stuck in that mode of thinking.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Nov 28 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148749232):
Anyway, thanks for the help, folks. I run a meetup where we are going through *Logic & Proof*, so we're all on the same page and I can't just say "let's use tactics for all the proofs from now on" when the examples in the book don't use tactic mode. If it were just me I could diverge and study tactics. I will show the example code you folks created in the meeting tonight.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Nov 28 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148749268):
*Logic & Proof* being what's linked to at the bottom of https://leanprover.github.io/publications/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Lyle Kopnicky (Nov 28 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148749310):
It's a goal of our study to learn mathematical logic, but also to learn to use a proof assistant. Which makes the book perfect.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Nov 29 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148762910):
FWIW, I like proof terms for readability too. You do you! That's why we have both options.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Nov 29 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148762983):
Although, it is possible to write incomprehensible code in either mode pretty easily

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Nov 29 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148763035):
The most important thing for comprehension is using lots of show, have, and suffices

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Nov 29 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148763037):
As Patrick mentioned

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 29 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148772700):
Proof terms are highly unreadable to me. One can't inspect them without having to do some work. @**Lyle Kopnicky** I just want to check you've understood Patrick's comment. When I am looking through my tactic proof in VS Code after ctrl-shift-enter, my session looks like the attached pic. [vscode.png](/user_uploads/3121/-ce0o2nYwcGCB9e_XvSMqgjI/vscode.png) . Clicking on different lines in the tactic proof shows me the exact state that Lean is in on every line. When I was a beginner I found this *completely indispensable*. One can attempt to mimic this in term mode, to try and understand someone else's term mode proof, but it involves actually deleting terms and replacing them with `_` which is much more of a pain.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 29 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20proving%20add_right_cancel/near/148773031):
Exactly!
I've somewhat gotten the hang of writing term mode proofs by keeping a sufficient number of `_` to the right of my cursor. But inspecting a term-mode proof is a nightmare.


{% endraw %}
