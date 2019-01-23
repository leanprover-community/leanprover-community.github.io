---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37598sumrec.html
---

## Stream: [general](index.html)
### Topic: [sum.rec](37598sumrec.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 01 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125949453):
I'm having a surprisingly hard time working with `sum.rec`. Specifically, I'm having trouble convincing Lean to give me an ordinary, non-dependent function as the result. I pasted a transcript here: https://gist.github.com/rwbarton/b6cbf07bd07afd89f8c2b4feef8cec5f

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125949466):
the type of the second term depends on the type of the first term though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125949476):
sorry, I thought you were talking about sigma. ignore what I said.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 01 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125949537):
I'm especially confused that `surjective ((λ a, sum.rec f g a) : α ⊕ β → γ)` produces an error that seems to be complaining that the argument needs to be a non-dependent function, though I can kind of imagine how this might not be considered a bug

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 01 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125949607):
It'd be really convenient for me if there was also a non-dependent eliminator `sum.rec' : (α → γ) → (β → γ) → α ⊕ β → γ`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 01 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125949617):
I noticed someone else came across the same issue, too:
```lean
lemma continuous_sum_rec {f : α → γ} {g : β → γ}
  (hf : continuous f) (hg : continuous g) : @continuous (α ⊕ β) γ _ _ (@sum.rec α β (λ_, γ) f g) :=
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 01 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125949693):
That whole result type should really just be `continuous (sum.rec' f g)`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 01 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125949778):
I assume the same issue arises for any other type with multiple constructors, too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125954356):
I think the problem is that `sum.rec` uses the eliminator strategy, meaning it relies heavily on the expected type to determine the motive, but `surjective` does not give a sufficiently specific expected type `?M1 -> ?M2`. You can fix the issue by annotating the metavariables of `surjective`:
```
@surjective (α ⊕ β) γ (λ a, sum.rec f g a)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125954449):
The eliminator strategy makes `T.rec` more or less unusable when unapplied; apparently superfluous eta expansions here are important to trigger the right strategy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955363):
Could this also be fixed by writing a second recursor?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955364):
i.e. is this a problem that the interface could solve?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955375):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955398):
yes, but that would require changing lean (which generates all the `inductive` theorems)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955402):
I think I'm instead reading "yes but you would need to PR core"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955456):
yes, that's what I mean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955531):
So you can't just write a new recursor, with a different name, which runs on top of unmodded Lean 3.4.1?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955538):
You can, but you would have to do so for every inductive type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955548):
but you could solve his one specific problem with `sum.rec`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955590):
I have to ask these stupid questions because I have no understanding of the status of these elab commands

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955595):
all I know is that if you don't like one, you can sometimes add an `@` and get another one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955604):
Sure, `or.elim` already exists and `sum.elim` could be similar

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955859):
`example (a b c : Prop) : @or.elim a b c = @or.rec_on a b c := rfl`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955868):
so the only way these function differ is by magic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955871):
as far as I am concerned

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955929):
Aah do they have different tags?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955943):
Not only are they the same theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955947):
they are the same proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955959):
but one is tagged `[reducible]`and is protected

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125956008):
`[reducible]` is all about how eagerly the elaborator unfolds the definition, or something...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125956015):
`protected` I have no idea. Something about avoiding overloading?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 01 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125956098):
`protected` means if you wrote `open or` (which you probably wouldn't), then you still wouldn't get the name `rec_on` as a synonym for `or.rec_on`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125956298):
one is a def and one is a theorem. Does this make any difference?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125956533):
`unknown identifier 'rec_on'`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125956543):
so nobody is allowed to have `rec_on`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125956918):
```lean
import set_theory.ordinal_notation
open nonote
#check rec_on
/-
rec_on :
  Π (o : nonote),
    ?M_1 0 →
    (Π (e : nonote) (n : ℕ+) (a : nonote) (h : below a e), ?M_1 e → ?M_1 a → ?M_1 (oadd e n a h)) → ?M_1 o
-/
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125956920):
Do I win five pounds?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 01 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125957006):
then that means that `nonote.rec_on` was not declared as protected

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125957707):
What is the complete list of unprotected `rec_on`s? And are these bugs?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125960643):
```lean
/-- This is a recursor-like theorem for `nonote` suggesting an
  inductive definition, which can't actually be defined this
  way due to conflicting dependencies. -/
@[elab_as_eliminator] def rec_on {C : nonote → Sort*} (o : nonote)
  (H0 : C 0)
  (H1 : ∀ e n a h, C e → C a → C (oadd e n a h)) : C o :=
begin
  cases o with o h, induction o with e n a IHe IHa,
  { exact H0 },
  { exact H1 ⟨e, h.fst⟩ n ⟨a, h.snd⟩ h.snd' (IHe _) (IHa _) }
end
```
(set_theory.ordinal_notation, line 857)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125960644):
it isn't automatically generated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125960649):
but indeed, @**Mario Carneiro** should have made it protected


{% endraw %}
