---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52580howtousetransfer.html
---

## Stream: [general](index.html)
### Topic: [how to use transfer](52580howtousetransfer.html)

---

#### [Mario Carneiro (Oct 06 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299504):
Okay, here is a mockup use of `transfer`:
```lean
import tactic.interactive

inductive xnat : Type
| zero : xnat
| succ : xnat → xnat

instance : has_zero xnat := ⟨xnat.zero⟩
instance : has_one xnat := ⟨xnat.succ 0⟩

def to_xnat : ℕ → xnat
| 0 := 0
| (nat.succ n) := (to_xnat n).succ

def of_xnat : xnat → ℕ
| 0 := 0
| (xnat.succ n) := (of_xnat n).succ

theorem to_of_xnat : ∀ n, (to_xnat (of_xnat n)) = n
| 0 := rfl
| (xnat.succ n) := congr_arg xnat.succ (to_of_xnat n)

theorem of_to_xnat : ∀ n, (of_xnat (to_xnat n)) = n
| 0 := rfl
| (nat.succ n) := congr_arg nat.succ (of_to_xnat n)

def rel (x : xnat) (n : ℕ) : Prop := to_xnat n = x

lemma rel_zero : rel 0 0 := eq.refl _
lemma rel_succ : (rel ⇒ rel) xnat.succ nat.succ :=
by rintro m _ ⟨⟩; exact rfl
lemma rel_one : rel 1 1 := eq.refl _

instance : has_add xnat :=
⟨λ m n, by induction n; [exact m, exact n_ih.succ]⟩

theorem to_xnat_add (m) : ∀ n, to_xnat (m + n) = to_xnat m + to_xnat n
| 0 := rfl
| (nat.succ n) := congr_arg xnat.succ (to_xnat_add n)

lemma rel_add : (rel ⇒ rel ⇒ rel) (+) (+) :=
by rintro m _ ⟨⟩ n _ ⟨⟩; apply to_xnat_add

lemma rel_eq : (rel ⇒ rel ⇒ iff) (=) (=) :=
by rintro m _ ⟨⟩ n _ ⟨⟩; exact
⟨λ e, by simpa [of_to_xnat] using congr_arg of_xnat e, congr_arg _⟩

instance : relator.bi_total rel :=
⟨λ a, ⟨_, to_of_xnat _⟩, λ a, ⟨_, rfl⟩⟩

example : ∀ x y : xnat, x + y = y + x :=
begin
  transfer.transfer [``relator.rel_forall_of_total, ``rel_eq, ``rel_add],
  simp [add_comm]
end
```

#### [Scott Olson (Oct 06 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299649):
Coincidentally I was playing with some proofs recently where I wished I had automatic transport. I'm playing with (regular) languages, and I've manually proven language equivalences like `L₁ ≃ L₃ → L₂ ≃ L₄ → L₁ ∪ L₂ ≃ L₃ ∪ L₄` which feel a lot like the `A ≃ B → P A ≃ P B` univalent transport

#### [Johan Commelin (Oct 06 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299658):
@**Mario Carneiro** Thanks a lot for this mock-up! Do you mind if I post my thoughts about it?

#### [Mario Carneiro (Oct 06 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299697):
of course, that's the idea

#### [Scott Olson (Oct 06 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299698):
I wonder if `transfer` would apply here? It might run intro trouble because these is an equivalence of functions, and `funext`-as-a-theorem would still be something cubical types have and Lean doesn't, but I haven't thought this through

#### [Johan Commelin (Oct 06 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299700):
Should we take it to a different thread?

#### [Johan Commelin (Oct 06 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299706):
@**Mario Carneiro** wrote a mockup use of `transfer`:
```lean
import tactic.interactive

inductive xnat : Type
| zero : xnat
| succ : xnat → xnat

instance : has_zero xnat := ⟨xnat.zero⟩
instance : has_one xnat := ⟨xnat.succ 0⟩

def to_xnat : ℕ → xnat
| 0 := 0
| (nat.succ n) := (to_xnat n).succ

def of_xnat : xnat → ℕ
| 0 := 0
| (xnat.succ n) := (of_xnat n).succ

theorem to_of_xnat : ∀ n, (to_xnat (of_xnat n)) = n
| 0 := rfl
| (xnat.succ n) := congr_arg xnat.succ (to_of_xnat n)

theorem of_to_xnat : ∀ n, (of_xnat (to_xnat n)) = n
| 0 := rfl
| (nat.succ n) := congr_arg nat.succ (of_to_xnat n)

def rel (x : xnat) (n : ℕ) : Prop := to_xnat n = x

lemma rel_zero : rel 0 0 := eq.refl _
lemma rel_succ : (rel ⇒ rel) xnat.succ nat.succ :=
by rintro m _ ⟨⟩; exact rfl
lemma rel_one : rel 1 1 := eq.refl _

instance : has_add xnat :=
⟨λ m n, by induction n; [exact m, exact n_ih.succ]⟩

theorem to_xnat_add (m) : ∀ n, to_xnat (m + n) = to_xnat m + to_xnat n
| 0 := rfl
| (nat.succ n) := congr_arg xnat.succ (to_xnat_add n)

lemma rel_add : (rel ⇒ rel ⇒ rel) (+) (+) :=
by rintro m _ ⟨⟩ n _ ⟨⟩; apply to_xnat_add

lemma rel_eq : (rel ⇒ rel ⇒ iff) (=) (=) :=
by rintro m _ ⟨⟩ n _ ⟨⟩; exact
⟨λ e, by simpa [of_to_xnat] using congr_arg of_xnat e, congr_arg _⟩

instance : relator.bi_total rel :=
⟨λ a, ⟨_, to_of_xnat _⟩, λ a, ⟨_, rfl⟩⟩

example : ∀ x y : xnat, x + y = y + x :=
begin
  transfer.transfer [``relator.rel_forall_of_total, ``rel_eq, ``rel_add],
  simp [add_comm]
end
```

#### [Johan Commelin (Oct 06 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299754):
First of all: I think for general applicability I think we need a quick way to construct `rel` from an `equiv.

#### [Johan Commelin (Oct 06 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299803):
And then I have several conflicting thoughts...

#### [Johan Commelin (Oct 06 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299809):
One is, given `nat` and the definition of `xnat` I would like to just immediately transfer `comm_semiring` to `xnat`.

#### [Johan Commelin (Oct 06 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299810):
All the structure and proofs should be transferable using automation.

#### [Johan Commelin (Oct 06 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299853):
On the other hand, one might find oneself in the situation where both sides are already equipped with some structure. In this case both already have a `0` and a `+`.

#### [Mario Carneiro (Oct 06 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299854):
It is easy to define `equiv.rel : A ~= B -> A -> B -> Prop`

#### [Johan Commelin (Oct 06 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299861):
Right, I'm collecting things that you find easy to define (-;

#### [Mario Carneiro (Oct 06 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299868):
immediately transferring structures is both more difficult and not necessarily what we want

#### [Johan Commelin (Oct 06 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299870):
So, suppose that both have a `0` and `+` like in your example.

#### [Mario Carneiro (Oct 06 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299910):
I would prefer an expedited method for showing that pre-existing structures are compatible with an equiv

#### [Mario Carneiro (Oct 06 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299911):
..oh wait, that's group_iso etc

#### [Johan Commelin (Oct 06 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299912):
Exactly

#### [Mario Carneiro (Oct 06 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299913):
so problem solved?

#### [Johan Commelin (Oct 06 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299917):
So we show that `to_xnat` is an `add_monoid` iso. And then?

#### [Johan Commelin (Oct 06 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299921):
Then there should be an easy way to extract those `rel`-lemmas

#### [Mario Carneiro (Oct 06 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299926):
oh yes, that's a one liner

#### [Mario Carneiro (Oct 06 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299927):
rel for add is literally map_add with some dressing

#### [Johan Commelin (Oct 06 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299928):
After that, proving that `xnat` is a `comm_monoid` should be `by transfer`.

#### [Johan Commelin (Oct 06 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299930):
Or something like that.

#### [Mario Carneiro (Oct 06 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299931):
we could put that in the theorems for group_iso

#### [Mario Carneiro (Oct 06 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299972):
But I am wary about *constructing* structure using `transfer`

#### [Mario Carneiro (Oct 06 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299975):
you might use `transfer` to prove that the addition is commutative, like I showed, but the definitions themselves should stand on their own

#### [Johan Commelin (Oct 06 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299981):
```lean
lemma rel_zero : rel 0 0 := eq.refl _
lemma rel_succ : (rel ⇒ rel) xnat.succ nat.succ :=
by rintro m _ ⟨⟩; exact rfl
lemma rel_one : rel 1 1 := eq.refl _
lemma rel_add : (rel ⇒ rel ⇒ rel) (+) (+) :=
by rintro m _ ⟨⟩ n _ ⟨⟩; apply to_xnat_add

lemma rel_eq : (rel ⇒ rel ⇒ iff) (=) (=) :=
by rintro m _ ⟨⟩ n _ ⟨⟩; exact
⟨λ e, by simpa [of_to_xnat] using congr_arg of_xnat e, congr_arg _⟩

instance : relator.bi_total rel :=
⟨λ a, ⟨_, to_of_xnat _⟩, λ a, ⟨_, rfl⟩⟩

example : ∀ x y : xnat, x + y = y + x :=
begin
  transfer.transfer [``relator.rel_forall_of_total, ``rel_eq, ``rel_add],
  simp [add_comm]
end
```
I would wish that this could all be compressed into 2 or 3 lines.

#### [Mario Carneiro (Oct 06 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135299983):
I don't think it needs to, it can be done in generality

#### [Mario Carneiro (Oct 06 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300030):
the stuff about applying `transfer.transfer` is not nice though, it should be easier than that

#### [Johan Commelin (Oct 06 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300039):
@**Mario Carneiro** Why are you cautious about `transfer`ing structure?

#### [Mario Carneiro (Oct 06 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300041):
because it leads to bad definitional reduction

#### [Mario Carneiro (Oct 06 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300044):
there are very few cases when it is the right thing to do

#### [Johan Commelin (Oct 06 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300094):
Hmmm, maybe I'm sad about that. I would have to see how it turns out in practice...

#### [Johan Commelin (Oct 06 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300134):
I would wish that if someone inadvertently defined `xnat`, then we could just say: "Aaah, that's `equiv` to `nat`. Bam!!! from now one it is a `comm_semiring` and you can use all theorems about `nat` for your `xnat`."

#### [Johan Commelin (Oct 06 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300144):
Hmm, I want to use more.

#### [Johan Commelin (Oct 06 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300182):
I want to use that it is not just some random `equiv`. I want to use that they are structurally equivalent. Is that a thing?

#### [Johan Commelin (Oct 06 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300186):
They are the *same* inductive type.

#### [Johan Commelin (Oct 06 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300187):
But I'm getting distracted, I think.

#### [Scott Olson (Oct 06 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300193):
So you're interested in duplicated definitions, not e.g. `nat` vs. `binnat`?

#### [Johan Commelin (Oct 06 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300234):
Well, not really. Like I said, I was getting distracted.

#### [Johan Commelin (Oct 06 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300239):
@**Mario Carneiro** Ok, I think I know what I want. I want you to remove every mention of `rel` in your example.

#### [Mario Carneiro (Oct 06 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300240):
That's the key part that makes transfer work

#### [Johan Commelin (Oct 06 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300241):
In the proof that addition is commutative, I want to invoke `big_transfer`

#### [Mario Carneiro (Oct 06 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300242):
you could remove everything else

#### [Johan Commelin (Oct 06 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300243):
And it will ask me for a `rel`

#### [Johan Commelin (Oct 06 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300279):
And I will answer: use this `equiv`

#### [Mario Carneiro (Oct 06 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300283):
but it is a logical relations proof, not a rewrite proof

#### [Mario Carneiro (Oct 06 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300287):
That's fine, I think

#### [Johan Commelin (Oct 06 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300288):
And then it says: Good. But then you need to prove these goals: `rel_zero`, `rel_add`.

#### [Mario Carneiro (Oct 06 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300289):
the user layer can handle that

#### [Johan Commelin (Oct 06 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300290):
And it generates those two goals. And I prove them with `tidy`.

#### [Mario Carneiro (Oct 06 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300291):
But the user layer here *really* needs work

#### [Mario Carneiro (Oct 06 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300297):
there is nothing, it's not even an interactive tactic

#### [Johan Commelin (Oct 06 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300298):
And there you have a 4 line tactic proof of commutativity. And all the other stuff above is gone.

#### [Johan Commelin (Oct 06 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300301):
Aaah...!

#### [Johan Commelin (Oct 06 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300303):
When I asked whether there was a tactic for `transfer`, you said "Yes". And I immediately assumed it was interactive.

#### [Johan Commelin (Oct 06 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300304):
Lol

#### [Johan Commelin (Oct 06 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300343):
For me tactic implies interactive. Silly me.

#### [Mario Carneiro (Oct 06 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300344):
In the int.basic example, there is a local redefinition of `transfer` to get the big list of relevant rel theorems for this particular relation

#### [Mario Carneiro (Oct 06 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300345):
because it is often the case that you will want to use the same relation, or pair of structures, in multiple nearby proofs

#### [Mario Carneiro (Oct 06 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300350):
in `int.basic` it is of course used for each of the axioms of the ring structure

#### [Johan Commelin (Oct 06 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300351):
But, can a tactic automatically infer what it needs to know about a relation, given a certain goal?

#### [Mario Carneiro (Oct 06 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300352):
no, it doesn't even know the target

#### [Mario Carneiro (Oct 06 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300391):
For example in my mockup I have a goal on `xnat` and I said `transfer` with no info

#### [Mario Carneiro (Oct 06 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300393):
how would it know that I am transferring to `nat` instead of something else? and why that relation instead of something else?

#### [Johan Commelin (Oct 06 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300401):
```lean
begin
  interactive.transfer my_equiv.to_rel,
  { -- prove rel_zero },
  { -- prove rel_add }
end
```

#### [Johan Commelin (Oct 06 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300403):
Would that be possible?

#### [Mario Carneiro (Oct 06 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300408):
I think we will need to rewrite transfer anyway, I very much doubt the one in core works well enough for our purposes

#### [Mario Carneiro (Oct 06 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300449):
(at least we should copy it to mathlib and give it a nice front end)

#### [Mario Carneiro (Oct 06 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300452):
That would be possible, but like I said you want more reuse than that

#### [Johan Commelin (Oct 06 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300454):
Cool

#### [Mario Carneiro (Oct 06 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300470):
that might prove your theorem now, but in the very next theorem you will probably want this relation again and you would have to prove `rel_zero` again

#### [Johan Commelin (Oct 06 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300471):
Yes, the VScode "Turn this goal into lemma" keyboard-shortcut will take care of the reuse.

#### [Mario Carneiro (Oct 06 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300515):
I don't think we have to worry about proof obligations much here

#### [Johan Commelin (Oct 06 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300516):
It will take everything between a pair of `{ .. }` and turn it into a proof of the subgoal. It will suggest a name for the lemma. And it will apply that lemma where previously the `{ .. }` were written.

#### [Johan Commelin (Oct 06 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300517):
But I'm getting distracted again :lol:

#### [Mario Carneiro (Oct 06 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300518):
it will usually already have all the info it needs to prove these obligations

#### [Johan Commelin (Oct 06 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300526):
Right.

#### [Mario Carneiro (Oct 06 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300529):
e.g. if you are proving rel_zero and rel_add that means you have a group iso and so you probably assumed it was a group iso, and so these theorems will already be proven

#### [Mario Carneiro (Oct 06 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300570):
The main point behind the `rel` stuff is to build up relations on bigger things, i.e. kernels and short exact sequences

#### [Johan Commelin (Oct 06 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300572):
But then `interactive.transfer` needs to remember that the `rel` came from an `equiv`. Then it could use type class search to find those results.

#### [Johan Commelin (Oct 06 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300573):
```quote
The main point behind the `rel` stuff is to build up relations on bigger things, i.e. kernels and short exact sequences
```
This could all be `equiv.to_rel`, right?

#### [Mario Carneiro (Oct 06 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300581):
there is nothing to remember, the relation is explicitly `equiv.rel e`

#### [Mario Carneiro (Oct 06 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300585):
not sure what you mean by that last bit

#### [Johan Commelin (Oct 06 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300586):
But then transfer will have a hard time finding theorems about `e`, not?

#### [Johan Commelin (Oct 06 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300627):
I meant that to me `equiv` seems a lot more natural than `rel`. And usually we will have an `equiv` floating around. Even for kernels and s.e.s's

#### [Mario Carneiro (Oct 06 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300628):
We will have to think about how to discover/supply rel theorems to transfer. Currently it just accepts a big ugly list of names

#### [Johan Commelin (Oct 06 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300630):
Or some `Isom` in a category. So we will need `Isom.rel`

#### [Mario Carneiro (Oct 06 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300635):
Note that rel is a *lot* more general

#### [Mario Carneiro (Oct 06 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300637):
The relation need not be an equiv

#### [Johan Commelin (Oct 06 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300638):
Yes, I know. I'm not sure if I care

#### [Mario Carneiro (Oct 06 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300639):
Almost all of these theorems hold with much weaker assumptions

#### [Johan Commelin (Oct 06 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300679):
I suggest that the interactive transfer generates a list of goals.
Then we can prove `by transfer my_rel; tidy`.

#### [Mario Carneiro (Oct 06 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300684):
I think it will discharge all its goals

#### [Mario Carneiro (Oct 06 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300691):
except the main goal

#### [Mario Carneiro (Oct 06 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135300695):
I wonder whether it should deliver its iff statement instead of changing the goal... that way it can apply on hyps too

#### [Andrew Ashworth (Oct 06 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301646):
I was reading https://www21.in.tum.de/~kuncar/documents/huffman-kuncar-cpp2013.pdf again and I saw that Isabelle's transfer can do `The transfer proof method can replace a universal with an equivalent bounded quantifier:
e.g., (∀n::nat. n < n + 1) is transferred to (∀x::int ∈ {0..}. x < x + 1).`

#### [Andrew Ashworth (Oct 06 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301653):
This sounds suspiciously like the number casting tactic mentioned in this chat earlier

#### [Mario Carneiro (Oct 06 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301695):
Of course our `transfer` is based on isabelle's `transfer`

#### [Mario Carneiro (Oct 06 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301696):
The number casting tactic uses rewrites instead of logical relations

#### [Mario Carneiro (Oct 06 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301698):
Maybe it would be better to use transfer for this ...?

#### [Andrew Ashworth (Oct 06 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301754):
I think `transfer` in Lean will want this anyway at some point, so the same machinery may as well do double duty...? I'm unsure of what the implications are

#### [Andrew Ashworth (Oct 06 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301795):
I do like that relations are stronger than rewrites

#### [Andrew Ashworth (Oct 06 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301800):
I'm reading some of the follow-on papers and there are some tactics that automatically generate refinement theorems for converting algorithms over finsets to concrete algorithms over data structures like rb-trees etc

#### [Andrew Ashworth (Oct 06 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301801):
using transfer or derivatives of

#### [Andrew Ashworth (Oct 06 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301860):
it appears someone in Coq wanted to port `transfer` too: https://arxiv.org/pdf/1505.05028.pdf

#### [Andrew Ashworth (Oct 06 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301861):
example 2 in the coq paper is exactly xnat and nat...

#### [Johan Commelin (Oct 06 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135301901):
The number casting tactic would be transferring data as well, right? Not only proofs...

#### [Kevin Buzzard (Oct 06 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135306619):
```quote
They are the *same* inductive type.
```
I remember when I used to go on about this sort of thing. For computer scientists there is a very precise notion of *the same* and it's asking a lot more than what we have -- it means they are literally the same object -- structurally equal. Two inductive types with canonically isomorphic definitions are just canonically isomorphic, which is a much weaker notion. For each notion of "the same" (these groups are "the same", these topological spaces are "the same") we have to formalise our notion of sameness (e.g. with an equiv or a beefed-up equiv structure with extra proof such as "...and the maps are also group homomorphisms") and then understand exactly which constructions descend to equivalence classes. "The same" is a fluid concept in mathematics, it is really a bunch of equivalence relations. I discovered in the schemes project that it was very costly to think of the open set `U` and the open set `id'' U` (the image of U under the identity map) as "the same", because they really were not *the same*. They were "equal because of a theorem" and this is a much weaker statement. Stuff like `congr_arg` and `congr_fun` work because `eq` (which is a random inductive type remember, not at all related to whether things are *the same*) has a good recursor.

#### [Kevin Buzzard (Oct 06 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135306664):
There was a thread a while ago now, possibly on gitter, where I got extremely frustrated about how `U` and `id'' U` could even *possibly* not be *the same* and it took a lot of talking from Mario and Kenny to peel me off the ceiling. Once I realised that the correct map from $$\mathcal{F}(U)$$ to $$\mathcal{F}(id(U))$$ was not `id` but `res` all my problems went away.

#### [Kevin Buzzard (Oct 06 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135306746):
$$U$$ and $$id(U)$$ are canonically isomorphic in the computer-scientist's version of the category of open sets on a topological space, but the moment you start treating them as *the same* you get a whole bunch of errors about motives not being type correct which Reid did show me how to fight against if necessary. However these techniques turned out not to be needed once I understood that the canonical isomorphisms were not `id` but `res`.

#### [Kevin Buzzard (Oct 06 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20transfer/near/135306755):
In the mathematician's model of this category, these sets are *the same*.

