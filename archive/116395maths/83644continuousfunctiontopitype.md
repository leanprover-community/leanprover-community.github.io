---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/83644continuousfunctiontopitype.html
---

## [maths](index.html)
### [continuous function to pi type](83644continuousfunctiontopitype.html)

#### [Johan Commelin (May 23 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969544):
I have no clue how to prove this:
```lean
lemma continuous.pi_mk {X I : Type*} {Y : I → Type*}
[topological_space X] [Πi, topological_space (Y i)] (f : Πi, X → (Y i)) (H : Πi, continuous (f i))
: continuous (λ x i, f i x) := sorry
```

#### [Kevin Buzzard (May 23 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969599):
Can you prove it in maths?

#### [Kevin Buzzard (May 23 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969600):
:-)

#### [Kevin Buzzard (May 23 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969604):
i.e. "is it true"

#### [Johan Commelin (May 23 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969606):
Unless I made a stupid mistake: yes

#### [Mario Carneiro (May 23 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969651):
how is the pi topology defined?

#### [Johan Commelin (May 23 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969652):
It just says that Pi is some sort of categorical product on steroids

#### [Kevin Buzzard (May 23 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969654):
what Mario said

#### [Johan Commelin (May 23 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969657):
If I have continuous maps to all the factors, I get a continuous map to the Pi

#### [Kevin Buzzard (May 23 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969658):
(in Lean)

#### [Johan Commelin (May 23 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969660):
```lean
instance Pi.topological_space {β : α → Type v} [t₂ : Πa, topological_space (β a)]
 : topological_space (Πa, β a) :=
⨆a, topological_space.induced (λf, f a) (t₂ a)
```

#### [Mario Carneiro (May 23 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969668):
so look for theorems about continuity on induced

#### [Johan Commelin (May 23 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969677):
There are loads of those... but how do I deal with the `⨆a,` that is in front?

#### [Mario Carneiro (May 23 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969678):
look for continuity on a Sup

#### [Johan Commelin (May 23 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969728):
there is only continuity for `sup`, not `Sup`

#### [Mario Carneiro (May 23 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969736):
I think it's called that... serach for the bigcup

#### [Johan Commelin (May 23 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969740):
I'm already down 5 rabbit holes, I really hope I don't need to go down this one as well...

#### [Johan Commelin (May 23 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969744):
Search for `⨆` gives `No results` in `continuity.lean`

#### [Mario Carneiro (May 23 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969801):
hm, looks like it is missing from the list at `continuity.lean`

#### [Johan Commelin (May 23 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969827):
Right, there is constructors for products of two topological spaces, and continous maps towards them, etc... but for Pi types this seems missing. And I don't know exactly how to prove this stuff...

#### [Johan Commelin (May 23 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969872):
/me doesn't know anything about `Sup` and friends

#### [Mario Carneiro (May 23 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969877):
okay, so use the existing theorems as guides and write your own version for continuity on supr

#### [Johan Commelin (May 23 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969887):
\me goes down rabbit hole # 6

#### [Mario Carneiro (May 23 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969888):
(or I can, if this is going too far afield)

#### [Mario Carneiro (May 23 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969895):
I'm just showing you what I would do

#### [Johan Commelin (May 23 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969908):
Well, I'm trying to prove that the face map between two standard simplices is continuous...

#### [Johan Commelin (May 23 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126969975):
@**Mario Carneiro** At the moment, I don't even know how to write the statement for `Sup`

#### [Mario Carneiro (May 23 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126970325):
here you go:
```
lemma continuous_Sup_dom {t₁ : set (tspace α)} {t₂ : tspace β}
  {t : tspace α} (h₁ : t ∈ t₁) : cont t t₂ f → cont (Sup t₁) t₂ f :=
continuous_le_dom (le_Sup h₁)

lemma continuous_Sup_rng {t₁ : tspace α} {t₂ : set (tspace β)}
  (h : ∀t∈t₂, cont t₁ t f) : cont t₁ (Sup t₂) f :=
continuous_Inf_rng
  (λ t ht, show t ≤ coinduced f t₁, from h t ht)
  continuous_coinduced_rng

lemma continuous_supr_dom {t₁ : ι → tspace α} {t₂ : tspace β}
  {i : ι} : cont (t₁ i) t₂ f → cont (supr t₁) t₂ f :=
continuous_Sup_dom ⟨i, rfl⟩

lemma continuous_supr_rng {t₁ : tspace α} {t₂ : ι → tspace β}
  (h : ∀i, cont t₁ (t₂ i) f) : cont t₁ (supr t₂) f :=
continuous_Sup_rng $ assume t ⟨i, (t_eq : t = t₂ i)⟩, t_eq.symm ▸ h i
```

#### [Mario Carneiro (May 23 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126970334):
I just copied the Inf stuff and dualized everything

#### [Johan Commelin (May 23 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126970571):
Ok, thanks!

#### [Johan Commelin (May 23 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126970576):
Let me see if I can continue with rabbit hole # 5 (-;

#### [Johan Commelin (May 23 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126971289):
Hurray!
```lean
lemma continuous.pi_mk {X I : Type*} {Y : I → Type*}
[t₁ : topological_space X] [t₂ : Πi, topological_space (Y i)] (f : Πi, X → (Y i)) (H : Πi, continuous (f i))
: continuous (λ x i, f i x) :=
begin
let YY := (Πi, Y i),
apply continuous_Sup_rng,
intros t ht,
cases ht with i hi,
simp at *,
rw hi,
apply continuous_induced_rng,
unfold function.comp,
exact H i,
end
```

#### [Johan Commelin (May 23 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126972217):
Ok, so now I'm stuck with this MWE:
```lean
lemma continuous_sums {n : ℕ} : continuous (λ x : ((fin n) → ℝ), univ.sum x) := sorry
```

#### [Johan Commelin (May 23 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126972240):
Whatever I try, I'm pulled hard into all sorts of `foldr` stuff. And I'm completely out of my comfort zone.

#### [Mario Carneiro (May 23 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126972265):
that's not a trivial theorem

#### [Johan Commelin (May 23 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126972267):
I would like to mumble some think like... well, addition is continuous... if you repeatedly add, you get continuity by induction

#### [Johan Commelin (May 23 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126972274):
Can I `foldr` the continuity proof off `add`?

#### [Mario Carneiro (May 23 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126972276):
I guess you can prove it by induction on `n`, you will need to show that `fin (succ n) -> R` is homeomorphic to `R x (fin n -> R)`

#### [Johan Commelin (May 23 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126972319):
To link back to the discussion with Kevin, from about an hour ago... do you think this could be made into a trivial theorem?

#### [Mario Carneiro (May 23 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126972322):
no

#### [Mario Carneiro (May 23 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126972365):
okay, maybe that's too strong, you might be able to prove it by induction on the set instead

#### [Johan Commelin (May 23 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126972371):
that sounds closer to what I wanted to mumble

#### [Mario Carneiro (May 23 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126972379):
in that case you want to use `finset.induction_on`

#### [Mario Carneiro (May 23 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126972424):
and the IH says that a sum of continuous functions over set s is continuous

#### [Johan Commelin (May 23 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126972492):
Ok, I'm going to try this. Thanks!

#### [Patrick Massot (May 23 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126974780):
Johan, you may already know, but just in case: there very easy clean up steps you can run on such proofs. `YY` is never used. `unfold` is actually much less useful that one thinks in the beginning, so I always try to remove all `unfold` once a proof work. And then we always try to get rid of `simp` in the middle of proofs. The result is:
```lean
lemma continuous.pi_mk {X I : Type*} {Y : I → Type*}
[t₁ : topological_space X] [t₂ : Πi, topological_space (Y i)] (f : Πi, X → (Y i)) (H : Πi, continuous (f i))
: continuous (λ x i, f i x) :=
begin
    apply continuous_Sup_rng,
    intros t ht,
    cases ht with i hi,
    rw hi,
    apply continuous_induced_rng,
    exact H i,
end
```

#### [Patrick Massot (May 23 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126974828):
Out of curiosity, I also tried to build a term proof, but haven't succeeded because of the mysterious rewrite in the middle (which rewrites implicit arguments, which has the weird effect of not changing the visible goal)

#### [Patrick Massot (May 23 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126974838):
I can't get more obfuscated than:
```lean
lemma continuous.pi_mk {X I : Type*} {Y : I → Type*}
[t₁ : topological_space X] [t₂ : Πi, topological_space (Y i)] (f : Πi, X → (Y i)) (H : Πi, continuous (f i))
: continuous (λ x i, f i x) :=
continuous_Sup_rng $ λ t ht, match ht with ⟨i, hi⟩ := by rw hi ; apply continuous_induced_rng ; exact (H i) end
```

#### [Johannes Hölzl (May 23 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126974960):
For the sum proof: its easiest to generalize for finset, and then go from list to multiset to finset. I will add this to mathlib:
```lean

lemma continuous_supr_rng
  {ι : Sort*} {α : Type*} {β : Type*} {t₁ : topological_space α} {t₂ : ι → topological_space β}
  {f : α → β}
  (h : ∀i, @continuous _ _ t₁ (t₂ i) f) :
  @continuous _ _ t₁ (lattice.supr t₂) f :=
continuous_iff_le_coinduced.2 $ lattice.supr_le $ assume i, continuous_iff_le_coinduced.1 (h i)

lemma continuous.pi_mk
  {X I : Type*} {Y : I → Type*} [t₁ : topological_space X] [t₂ : Πi, topological_space (Y i)]
  (f : Πi, X → (Y i)) (H : Πi, continuous (f i)) :
  continuous (λ x i, f i x) :=
continuous_supr_rng $ assume i, continuous_induced_rng $ H i

lemma continuous_list_sum {α : Type*} {β : Type*} {γ : Type*}
  [topological_space α] [topological_space β] [add_comm_monoid β] [topological_add_monoid β]
  {f : γ → α → β} :
  ∀l:list γ, (∀c∈l, continuous (f c)) → continuous (λa, (l.map (λc, f c a)).sum)
| []       _ := by simp [continuous_const]
| (f :: l) h :=
  begin
    simp,
    exact continuous_add
      (h f (list.mem_cons_self _ _))
      (continuous_list_sum l (assume c hc, h c (list.mem_cons_of_mem _ hc)))
  end

lemma continuous_multiset_sum {α : Type*} {β : Type*} {γ : Type*}
  [topological_space α] [topological_space β] [add_comm_monoid β] [topological_add_monoid β]
  {f : γ → α → β} (s : multiset γ) :
  (∀c∈s, continuous (f c)) → continuous (λa, (s.map (λc, f c a)).sum) :=
quot.induction_on s $ by simp; exact continuous_list_sum

lemma continuous_finset_sum {α : Type*} {β : Type*} {γ : Type*}
  [topological_space α] [topological_space β] [add_comm_monoid β] [topological_add_monoid β]
  (f : γ → α → β) (s : finset γ) :
  (∀c∈s, continuous (f c)) → continuous (λa, s.sum (λc, f c a)) :=
continuous_multiset_sum _
```

#### [Johan Commelin (May 23 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126975014):
@**Patrick Massot** Yes, you are completely right. But it seems the work is now already done (-;

#### [Mario Carneiro (May 23 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126975238):
you can see how Johannes built the term proof for `pi_mk`; the key is to use `continuous_supr_rng` not `continuous_Sup_rng` because the definition uses `supr` (the indexed supremum) not `Sup` (the set supremum). In fact `supr` is defined in terms of `Sup`, but if you apply the wrong theorem it unfolds this definition and things get harder.

#### [Johan Commelin (May 23 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126975550):
Yes, I will take a closer look. I think I can learn a lot from how Johannes improved my kludge

#### [Patrick Massot (May 23 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126975794):
Sure. But this is too efficient in a sense. My message was focused on easy local clean up, that you can actually do without any understanding of the proof. Of course this is only the first step. Really efficient proofs like Johannes' require actual thinking

#### [Mario Carneiro (May 23 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126975891):
you can also look at my term proof of `continuous_supr_rng`, which uses the `\t` for rewriting

#### [Patrick Massot (May 23 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126975965):
I'm a bit frustrated by this \t thing. I know it's somehow the term version of `rw` and I see it everywhere in mathlib, but I was almost never able to use it

#### [Mario Carneiro (May 23 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126975978):
I admit it was a bit delicate for me at first

#### [Mario Carneiro (May 23 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126976035):
it is so much weaker than the lean 2 version, it fails whenever the expected type or the thing to rewrite with has metavariables

#### [Johan Commelin (May 23 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126976056):
Anyway, I just proved that the face map between standard simplices is continuous!

#### [Johan Commelin (May 23 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126976057):
The proof is not cleaned up. But it works (-;

#### [Mario Carneiro (May 23 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126976067):
but it's often just the thing when you want to rewrite with an equality in the context

#### [Patrick Massot (May 23 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126976197):
What about my attempt? Can you use \t there? (without switching to `continuous_supr_rng`)

#### [Mario Carneiro (May 23 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126976271):
yes, the proof should be almost identical to the one I pointed at

#### [Johan Commelin (May 23 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126976317):
Ok, like I said, the proofs are still ugly. But here goes nothing: https://github.com/jcommelin/mathlib/commit/fec9db2028bea163352f574055dad44029d04788

#### [Mario Carneiro (May 23 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126976321):
```
lemma continuous.pi_mk
  {X I : Type*} {Y : I → Type*} [t₁ : topological_space X] [t₂ : Πi, topological_space (Y i)]
  (f : Πi, X → (Y i)) (H : Πi, continuous (f i)) :
  continuous (λ x i, f i x) :=
continuous_Sup_rng $ assume t ⟨i, e⟩, e.symm ▸ continuous_induced_rng (H i)
```

#### [Patrick Massot (May 23 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126980416):
Hum, I think I stupidly missed the `eq.symm` when I tried

#### [Johannes Hölzl (May 23 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126981716):
@**Johan Commelin** I forgot that there is already `tendsto_sum`, so you could also derive `continuous_finset_sum` from this.
Anyway, this all is now in mathlib.

#### [Johan Commelin (May 23 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous function to pi type/near/126985262):
Thanks a lot! I will merge into my fork. Once I clean my stuff up, I think I will make a PR

