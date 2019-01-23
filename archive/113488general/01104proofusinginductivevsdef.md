---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01104proofusinginductivevsdef.html
---

## Stream: [general](index.html)
### Topic: [proof using inductive vs def](01104proofusinginductivevsdef.html)

---

#### [Sean Leather (Sep 14 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133936109):
This is quite an esoteric problem, so I'm not sure if anybody would be interested in looking into it. Nonetheless, I thought I'd try to see if anybody had any ideas.

So I thought I would change a inductive `Prop` to a definition. The original inductive:

```lean
inductive lc : exp V → Prop
  | varf : Π (x : V),                                                                          lc (varf x)
  | app  : Π                {ef ea : exp V}, lc ef → lc ea →                                   lc (app ef ea)
  | lam  : Π {L : finset V} {eb : exp V},            (∀ {x : V}, x ∉ L → lc (open_var x eb)) → lc (lam eb)
  | let_ : Π {L : finset V} {ed eb : exp V}, lc ed → (∀ {x : V}, x ∉ L → lc (open_var x eb)) → lc (let_ ed eb)
```

The new def:

```lean
def lc' : exp V → Prop
  | (varb _)     := false
  | (varf _)     := true
  | (app ef ea)  := lc' ef ∧ lc' ea
  | (lam eb)     := ∃ (L : finset V), ∀ {x}, x ∉ L → lc' (open_var x eb)
  | (let_ ed eb) := lc' ed ∧ ∃ (L : finset V), ∀ {x}, x ∉ L → lc' (open_var x eb)
  using_well_founded {
    dec_tac := `[simp [measure, inv_image, nat.pos_iff_ne_zero']],
    rel_tac := λ_ _, `[exact ⟨_, measure_wf depth⟩] }
```

But then I ran into a problem proving a theorem that did induction on `lc`. Since I can't do induction on `lc'`, I changed the proof to do induction on the parameter to `lc'`. In the old proof, I have this at one stage:

```lean
V : Type,
_inst_1 : finset.has_fresh V,
e₁ e₂ : exp V,
k : ℕ,
L : finset V,
eb : exp V,
Fb : ∀ {x : V}, x ∉ L → lc (open_var x eb),
rb : ∀ {x : V}, x ∉ L → ∀ {e₂ : exp V} {k : ℕ}, open.rec e₂ k (open_var x eb) = open_var x eb
⊢ open.rec e₂ (k + 1) eb = eb
```

In the new proof, I have this at the same stage:

```lean
V : Type,
_inst_1 : finset.has_fresh V,
e₂ : exp V,
k : ℕ,
eb : exp V,
L : finset V,
Fb : ∀ {x : V}, x ∉ L → lc' (open_var x eb)
rb : lc' eb → ∀ {e₂ : exp V} {k : ℕ}, open.rec e₂ k eb = eb,
⊢ open.rec e₂ (k + 1) eb = eb
```

Notice the difference in `rb`. In the old proof, I have an auxiliary proof that works for `open.rec e₂ k (open_var x eb)`, but in the new proof, I'm stuck. Since the new `lc'` doesn't provide the same evidence at `rb`, I don't know what to do. I think I should somehow reproduce the old `rb` in the new proof, perhaps using some knowledge of `lc'` that is lost since I'm not doing induction on `lc`, but I don't know how.

The full thing is at https://github.com/spl/tts/tree/lc-def .

#### [Kenny Lau (Sep 14 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133936608):
does `rec_on` solve the problem?

#### [Sean Leather (Sep 14 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133936659):
`rec_on` what?

#### [Kenny Lau (Sep 14 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133936828):
exp

#### [Sean Leather (Sep 14 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133936836):
Do you mean use `rec_on` instead of `induction`? I'm not sure, but I don't see how it could.

#### [Mario Carneiro (Sep 14 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937291):
which case are you in? what is the induction proof?

#### [Mario Carneiro (Sep 14 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937349):
none of the variables in the state match things in the inductive definitions you gave

#### [Sean Leather (Sep 14 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937489):
The `lam` case. See https://github.com/spl/tts/commit/04e4229c0fccec935b7f615a4aefe18d14982f2b#diff-94a57c5df4a0ba5ba897bada2c897d1aR73

#### [Sean Leather (Sep 14 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937510):
Just above that is the old proof (line 49).

#### [Mario Carneiro (Sep 14 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937539):
you are doing induction on `k`?

#### [Sean Leather (Sep 14 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937593):
In the old proof, induction was on `l : lc e₁`. In the new proof, induction is on `e₁ : exp V`.

#### [Sean Leather (Sep 14 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937630):
The focus is here: https://github.com/spl/tts/blob/04e4229c0fccec935b7f615a4aefe18d14982f2b/src/exp/open.lean#L41-L77 (if that helps).

#### [Mario Carneiro (Sep 14 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937634):
induction on `e1` isn't good enough

#### [Mario Carneiro (Sep 14 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937674):
you have to do induction on the same well founded measure you used to define `lc'` in the first place

#### [Sean Leather (Sep 14 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937678):
You mean induction on `depth`?

#### [Mario Carneiro (Sep 14 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937679):
yes

#### [Sean Leather (Sep 14 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937683):
Oh....

#### [Mario Carneiro (Sep 14 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937690):
because presumably these `open_var` things don't increase depth

#### [Sean Leather (Sep 14 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937696):
Correct.

#### [Mario Carneiro (Sep 14 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937708):
it's a general rule that you have to prove properties about a recursive definition using the same recursion strategy as the definition

#### [Sean Leather (Sep 14 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937791):
Ah, okay. The well-founded stuff still confuses me.

#### [Sean Leather (Sep 14 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937807):
So, it seems that the `inductive` is already doing a lot for me that I would otherwise have to do with more work.

#### [Sean Leather (Sep 14 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937849):
Would it be better just to keep using it instead of the definition version?

#### [Sean Leather (Sep 14 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937854):
I thought a definition would make things easier, but it's not.

#### [Kenny Lau (Sep 14 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937859):
I mean, you can always use `well_founded.fix`

#### [Sean Leather (Sep 14 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937920):
I've never used `well_founded.fix`.

#### [Mario Carneiro (Sep 14 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937952):
it is not easier

#### [Mario Carneiro (Sep 14 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937961):
it is used behind the scenes by `using_well_founded`

#### [Sean Leather (Sep 14 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133938025):
Okay. So I'll stick with the inductive. Lesson learned!

#### [Simon Hudon (Sep 15 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133995045):
Inductive propositions are quite handy in those situations. You can do induction on them when they are in your assumptions and it will automatically unify the variables that should be equal and you want have to handle cases where your definition would say `false`

