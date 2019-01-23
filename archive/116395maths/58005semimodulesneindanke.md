---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/58005semimodulesneindanke.html
---

## Stream: [maths](index.html)
### Topic: [semimodules nein danke](58005semimodulesneindanke.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 13 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133914925):
```
tactic.mk_instance failed to generate instance for
  module (polynomial R) (polynomial R)
```

That didn't used to happen.

From `algebra/module.lean`:

```lean
instance semiring.to_semimodule [r : semiring α] : semimodule α α := [stuff]

instance ring.to_module [r : ring α] : module α α :=
{ ..semiring.to_semimodule }
```

Is this definitely OK? My rings are no longer modules over themselves for some reason.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 13 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133914954):
> nein danke

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 13 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133915566):
```lean
import data.polynomial algebra.module

example (R) [nonzero_comm_ring R] (I : set (polynomial R)) [is_submodule I] : 1 = 1 := by simp

/-

failed to synthesize type class instance for
R : Type ?,
_inst_1 : nonzero_comm_ring R,
I : set (polynomial R)
⊢ module ?m_1 (polynomial R)

-/

```

Am I just making a rookie error? I thought this used to work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 13 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133915592):
Oh -- I am -- this is not the problem. I need decidable equality. I'll keep looking for the problem.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 13 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133915650):
FYI I'm currently working on a big rewrite of most of this, so stay tuned.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 13 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133915817):
Oh Ok. I just pulled again and the errors moved to different places, so I guess that's progress.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133916124):
Oh I still have (in the middle of some code)

```lean
      letI : comm_ring (polynomial R) := by apply_instance, -- works fine
      letI : module (polynomial R) (polynomial R) := by apply_instance, -- fails to generate instance
```

but if you're changing stuff then perhaps I will just leave things for now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133939719):
```lean
import data.polynomial algebra.module linear_algebra.submodule

local attribute [instance, priority 1] classical.prop_decidable

open polynomial

#print ring.to_module 
/-

@[instance]
protected def ring.to_module : Π {α : Type u} [r : ring α], module α α := ...

-/

lemma leading_term_bdd_deg_ideal {R} [nonzero_comm_ring R] (I : set (polynomial R)) [is_submodule I] (n : ℕ) :
submodule R R :=
⟨{c : R | ∃ f, f ∈ I ∧ degree f ≤ n ∧ leading_coeff f = c},{
  zero_ := ⟨0,is_submodule.zero,lattice.bot_le,rfl⟩,
  add_ := λ a b ⟨f, Hf⟩ ⟨g, Hg⟩, begin
    letI : ring (polynomial R) := by apply_instance, -- works
    letI : module (polynomial R) (polynomial R) := by apply_instance, -- fails
  sorry, end,
  smul := sorry,
}⟩
```

There's a fairly minimal working example of something which is stopping me from doing anything on Hilbert basis at the minute. Type class inference can find the ring instance, and the ring to module instance is there, but type class inference can't find the module instance.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133939818):
I can't add the instance explictly -- well, I can -- but then I get weird diamond errors later on. I am going to put Hilbert basis on hold for a while until I can understand what is going on here -- currently my understanding is that this is not user error and I should just wait, and of course I'm happy to wait.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133940044):
@**Kevin Buzzard** You could use  the explicit
`letI : module (polynomial R) (polynomial R) := @ring.to_module (polynomial R) _,`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133940048):
It is a bit ugly, but maybe it would unblock you?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133940379):
No because then I get diamond issues with exactly the instances that Mario is currently refactoring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133940459):
I just thought I'd post this example because either it's something which seems to be to be currently broken or I've made a mistake and it doesn't work for a good reason (note that I go from term mode to tactic mode and for all I know this has consequences for type class inference). If I've not made a mistake then it's something that should work after the refactoring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133940518):
Hmmm... that's crazy.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133940963):
```
invalid type ascription, term has type
  @is_submodule R (@polynomial R (@comm_ring.to_comm_semiring R (@nonzero_comm_ring.to_comm_ring R _inst_1)))
    (@comm_ring.to_ring R (@nonzero_comm_ring.to_comm_ring R _inst_1))
    (@polynomial.module R (λ (a b : R), classical.prop_decidable (a = b)) (@nonzero_comm_ring.to_comm_ring R _inst_1))
    I
but is expected to have type
  @is_submodule (@polynomial R (@comm_ring.to_comm_semiring R (@nonzero_comm_ring.to_comm_ring R _inst_1)))
    (@polynomial R (@comm_ring.to_comm_semiring R (@nonzero_comm_ring.to_comm_ring R _inst_1)))
    (@comm_ring.to_ring (@polynomial R (@comm_ring.to_comm_semiring R (@nonzero_comm_ring.to_comm_ring R _inst_1)))
       _inst)
    _inst_3
    I
```

for what it's worth. Oh! What is this `polynomial.module`?? That's the statement that `R[X]` is a module over `R`. Is that relevant? Anyway, this is not the point -- the point is that either my original thing should work and it doesn't (in which case I should stop, because I am using modules all over the place and will surely see other problems later, even though no module actually occurs in the proofs, only ideals, and part of me wants to define ideals as subsets of rings plus blah because we all know that type classes for modules have problems, whereas type classes for ideals will probably work fine), or I've made a mistake (in which case I need help because I can't see it).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133941521):
@**Kevin Buzzard** So the math strategy would be something like "wlog we have deg(f) ≤ deg(g), now look at `X^(degree g - degree f) * f + g`. Done."

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133941543):
I don't know how to do `wlog` in Lean, so I'll just do cases on `have H := le_or_gt f.degree g.degree,`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133941553):
The next step fails, because Lean doesn't know how to subtract `with_bot ℕ` thingies. Is that intended? Or should we use `nat_degree`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133941852):
Oh I've done all this bit -- you should look at the `kmb_hilbert_basis` branch of community mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133941999):
```quote
why are you making me commit just becuase I want to change branch
```
`git stash`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133942704):
Oh that's what it's for!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133943962):
`unexpected occurrence of recursive function`
Did I unlock something?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133943968):
@**Kevin Buzzard** I tried using `wlog`:
```lean
-- zero ring a special case so let's deal with it separately
theorem hilbert_basis_zero_ring {R} [comm_ring R] (h : (0 : R) = 1) :
is_noetherian_ring (polynomial R) :=
begin
  apply ring.is_noetherian_of_zero_eq_one,
  rw polynomial.ext,
  intro n,
  repeat {rw semiring.zero_of_zero_eq_one h (coeff _ n)}
end

theorem hilbert_basis {R} [comm_ring R] (hR : is_noetherian_ring R) : is_noetherian_ring (polynomial R) :=
begin
  -- deal with zero ring first
  by_cases h01 : (0 : R) = 1,
    exact hilbert_basis_zero_ring h01,
  letI : nonzero_comm_ring R := comm_ring.non_zero_of_zero_ne_one h01,
  let L : set R := set.range leading_coeff,
  have HL : is_ideal L := {
    zero_ := ⟨0,rfl⟩,
    add_ := λ a b ⟨f,Hf⟩ ⟨g,Hg⟩, begin
      by_cases h0 : a + b = 0, rw h0, exact ⟨0, rfl⟩,
      by_cases hf : f = 0, rw [←Hf, ←Hg, hf, leading_coeff_zero, zero_add], exact ⟨g,rfl⟩,
      by_cases hg : g = 0, rw [←Hf, ←Hg, hg, leading_coeff_zero, add_zero], exact ⟨f,rfl⟩,
      wlog hd : nat_degree f ≤ nat_degree g using [f g, g f],
      { exact or.cases_on (le_or_lt (nat_degree f) (nat_degree g)) (assume H, or.inl H) (assume H, or.inr (le_of_lt H)) },
      { let h := f * X ^ (nat_degree g - nat_degree f) + g,
        have Htemp : leading_coeff f * leading_coeff (X ^ (nat_degree g - nat_degree f)) ≠ 0,
          rw [leading_coeff_X_pow,mul_one],
          exact (λ h, hf $ leading_coeff_eq_zero.1 h),
        have Ha : a = leading_coeff (f * X ^ (nat_degree g - nat_degree f)),
          rw [leading_coeff_mul' Htemp,leading_coeff_X_pow,mul_one,Hf],
        exact ⟨h, begin convert leading_coeff_add_of_degree_eq _ _, exact Hg.symm,
                      rw degree_mul_eq' Htemp,
                      rw degree_X_pow,
                      rw degree_eq_nat_degree hf,
                      rw degree_eq_nat_degree hg,
                      rw ←with_bot.coe_add,
                      rw with_bot.coe_eq_coe,
                      exact nat.add_sub_cancel' hd,
                    rwa [←Ha,Hg],
                  end⟩ },
    end,
    smul := sorry
  },
  sorry,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133943976):
I also proved `hilbert_basis_zero_ring`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 14 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133944142):
I wonder whether Hilbert ever proved it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133944224):
Lol...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133944235):
Do you have any idea how I managed to get into this recursive function? Is this a bug in `wlog`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 14 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945017):
Usually when I get that recursive function error it's because I have some `_fun_match` or similar thing among my hypotheses and some tactic tried to apply it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 14 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945027):
Is that the whole error message?
Guessing from previous discussion here I can't run your code that easily

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 14 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945044):
The `add := λ a b ⟨f,Hf⟩ ⟨g,Hg⟩,` looks possibly to blame, if that is the cause

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945203):
There are indeed `_fun_match` hypotheses in the context.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 14 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945257):
see if moving that lambda stuff to an `rintros` tactic helps

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945263):
Ok, I'll try

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945268):
`wlog` is too good to miss out on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 14 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945363):
> Hilbert (1890) proved the theorem (for the special case of polynomial rings over a field)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945386):
And here we are, about 130 years later, proving it for the zero ring!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945454):
Maybe you don't have my most recent commits. I have more than this. I gave up on wlog for exactly the reason you posted

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945517):
Hmmm, too bad.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 14 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945653):
I feel like you could avoid this zero ring stuff if you worked at it. For example, instead of the ideal of all leading coefficients, take the ideal `{ coeff f i | coeff f j = 0 for all j > i }`. Probably not worth it though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945733):
Hmm, I don't know. Doesn't that lead to rather clean proofs?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945741):
I honestly don't think that trying to write proofs that work with the zero ring is worth it. Every third step you need to check that something is non-zero. To prove that if I is an ideal of R[X] then the set of leading terms of polynomials in I is an ideal involves so many edge cases; leading term f non-zero, leading term g non-zero, leading term f + g non-zero, and this is all in the case R non-zero. The proof is edge case after edge case and edge case 1 is very naturally R = 0.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945743):
You need a little lemma saying `coeff f j = 0` for all `j > degree f`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945826):
Loads of the lemmas about how leading coefficients of polynomials behave rely on terms being non-zero, e.g. you use f*X^(deg g - deg f) to get degree of f up to that of g, and to compute the degree of this you need degree of X is 1 and this demands a proof that 1 isn't 0

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945859):
Oh I see -- you mean avoid leading terms completely? But we also need the ideal of leading terms of polys of degree at most n. Maybe you're right and there's some way of doing it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945862):
PS I pushed some more commits

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945921):
the j thing -- you have to be careful because degree is not a nat, it's a with_bot nat, and coeff takes a nat

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 14 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945927):
I think if you avoid ever saying the word "degree", and unravel its definition everywhere, then possibly all the "R is not zero" steps disappear.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 14 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133945951):
(But they may be replaced by having to do more other work, and in any case it's a bit unnatural.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 14 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133946079):
Apparently they proved this in Mizar

> Let $$R$$ be a Noetherian Abelian add-associative right zeroed right complementable associative distributive well unital commutative non empty double loop structure. One can verify that Polynom-Ring $$R$$ is Noetherian.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133949236):
You need to talk about degrees because given an ideal $$I$$ of $$R[X]$$ you need to consider the ideal $$J_k$$ ($$k$$ a natural) comprising of 0 and the leading terms of the polynomials in $$I$$ of degree $$k$$. But I agree there might be tricks. Here's another example of an edge case -- if $$f$$ has degree $$k$$ and leading term $$a$$, and $$c$$ is in $$R$$ then you want to prove that $$a*c$$ is in $$R$$, but $$c*f$$ might not have degree $$k$$ any more and you have to deal with that case separately. It's quite an annoying proof to formalise :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133963161):
Aah! I found my type class problem!

```lean
import data.polynomial algebra.module linear_algebra.submodule

local attribute [instance, priority 1] classical.prop_decidable

open polynomial

set_option pp.all true

universe u

-- Maths :  "Let I be an ideal of R[X]"

definition ABC (R : Type u) [comm_ring R] (I : set (polynomial R)) [is_submodule I] : false :=
begin

-- ...but I is not an ideal of (polynomial R)!

/-

_inst_2 :
  @is_submodule.{u u} R (@polynomial.{u} R (@comm_ring.to_comm_semiring.{u} R _inst_1))
    (@comm_ring.to_ring.{u} R _inst_1)
    (@polynomial.module.{u} R (λ (a b : R), classical.prop_decidable (@eq.{u+1} R a b)) _inst_1)

-/

-- I is an R-submodule :-/

sorry
end
```

There's an instance making (polynomial R) an R-module, and another instance making it a (polynomial R)-module, and `is_submodule` chooses the one I don't want. @**Chris Hughes** @**Mario Carneiro** is there a coherent strategy to deal with this? Any time a ring is a module over another ring (and this happens all the time in commutative ring theory) we will have instances of `module R M` for fixed `M` and lots of `R`. I propose scrapping stuff like `is_submodule M` and replacing it with `is_submodule R M`. What do you think?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133963705):
It's probably worth saying that it is not uncommon at all to hear mathematicians saying "let N be an A-submodule of B" or "let W be a k-subspace of V".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133975502):
```lean
-- Maths :  "Let I be an ideal of R[X]"

-- Lean
example {R} [comm_ring R] (I : set (polynomial R)) [@is_submodule (polynomial R) _ _ (ring.to_module) I] 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133975549):
Lean currently has to be told that the ring `polynomial R` is a module over itself.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133976193):
```lean
import data.polynomial algebra.module linear_algebra.submodule

local attribute [instance, priority 1] classical.prop_decidable

open polynomial

universe u

-- Maths :  "Let I be an ideal of R[X]. Then 0 ∈ I. "

definition ABC (R : Type u) [comm_ring R] (I : set (polynomial R)) [is_submodule I] : (0 : polynomial R) ∈ I :=
is_submodule.zero -- fails

/-

function expected at
  is_submodule.zero
term has type
  ?m_1 0
Additional information:
/home/buzzard/lean-projects/mathlib-community/tests/scratch.lean:16:0: context: switched to simple application elaboration procedure because failed to use expected type to elaborate it, error message
  too many arguments

-/
```

Does anyone know what `too many arguments` means in this context and why it happened?

```lean
definition ABC (R : Type u) [comm_ring R] (I : set (polynomial R)) [@is_submodule (polynomial R) _ _ (ring.to_module) I] : (0 : polynomial R) ∈ I :=
is_submodule.zero -- also fails
```


```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133976867):
```lean
definition ABC (R : Type u) [comm_ring R]
  (I : set (polynomial R)) [@is_submodule (polynomial R) _ _ (ring.to_module) I] :
(0 : polynomial R) ∈ I := @is_submodule.zero _ (polynomial R) _ (ring.to_module) I _
```
Zero is in an ideal of a polynomial ring! Why am I so bad at this? Is it broken or am I just overlooking something simple?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133976930):
@**Kenny Lau** how do you prove zero is in an ideal of the ring $$R[X]$$?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133976938):
I don't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133976946):
Why not?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133977036):
You want algebraic closure to finish your rigorous formulation of the statement of the local Langlands conjectures for all abelian algebraic groups, a theorem of Langlands. More mathematicians will be interested in Lean if you do that. Tom Hales has already mentioned it in a talk of his -- did you see?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133977043):
and for algebraic closure you're going to have to use ideals in polynomial rings quite a lot.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133977058):
What is the current status of your formulation project?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133977216):
I mean, aren't we waiting for the refactoring?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133977241):
The Langlands philosophy is notorious for being a "philosophy", a vague web of general ideas that it's hard to make rigorous, which occasionally specialise down to very explicit conjectures but sometimes are not actually rigorous mathematical statements. If you get stuck formulating them in general then you can start asking experts in number theory how they actually formulate their grand conjectures. I think it would be really cool. Toby Gee and I spent several years of our lives trying to formulate an actual rigorous conjecture which could rightly be given the name of "Langlands' Reciprocity Conjecture for a general connected reductive group" and we still do not have a general conjecture which encompasses everything.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133977297):
https://arxiv.org/abs/1009.0785

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133977302):
```quote
You want algebraic closure to finish your rigorous formulation of the statement of the local Langlands conjectures for all abelian algebraic groups, a theorem of Langlands. More mathematicians will be interested in Lean if you do that. Tom Hales has already mentioned it in a talk of his -- did you see?
```
in fact I saw it recently while searching for myself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133977411):
I believe that our conjecture can be formalised in Lean and I am not sure that Langlands' philosophy can, not in a way that everyone would find satisfactory at least. What if someone claimed it was the existence of some Global Langlands Group with some properties and then someone like Reid Barton or you just observed that such a group with these properties trivially exists because it's just some pullback. The "ultimate conjecture" is extremely vague. It says that the global Langlands group should be constructed in some way using some generalisation of Galois theory that we don't actually have.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133977541):
If you just say that it's some "Galoisish" group whose representation theory looks like the set of automorphic representations in some vague way, and then you try to formalise what you mean, then you're in danger of someone just building a group whose representation theory has this property for trivial reasons.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133977788):
Jim Arthur wrote a paper about this many years ago and I wish I understood that paper better. http://www.claymath.org/library/cw/arthur/pdf/automorphic-langlands-group.pdf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133981310):
@**Reid Barton**  I thought a bit more about your suggestion and of course you're right. One wants a new subtype `deg_le n` of polynomials of degree at most n, we want to prove that this is an R-module, and we want to define these increasing ideals as the projection map given by the n'th coefficient. That way we should still to the construction of the finite generating set for the ideal. There's then an induction to go but it looks really easy in this optic.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133981394):
No need to assume R is non zero

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133981491):
We just need deg (f + g) <= max(deg f,deg g) and deg r*f <= deg f, both of which are true unconditionally

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133981512):
@**Chris Hughes** these are the nice statements about degrees of polynomials.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 14 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133981618):
In some sense I'm back to square 1 with my proof but this time it's going to be far more mathlib-ready!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133983245):
Dumb question: if R is a ring considered as a semiring and M is a semimodule over the semiring R, is then M a module over the ring R?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 15 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133984088):
Yes because $$m \mapsto -m$$ is provided by multiplication by $$-1 \in R$$ and it satisfies the expected equation by distributivity $$0 = (1 + (-1)) m = m - m$$.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 15 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133985287):
I've been too busy to respond today but I see you have converged on the same solution as I have for the ideal of degree <= n polynomials :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133985565):
it's not an ideal :-/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133985586):
this is exactly the difference between an ideal and a submodule :-) It's a submodule for one module structure but not for the other.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/133986217):
```lean
def coeff_zero_iff_deg_le {R} [comm_semiring R] (f : polynomial R) (n : with_bot ℕ) :
degree f ≤ n ↔ ∀ m : ℕ, n < m → coeff f m = 0 :=
begin
  split,
  { intros H m Hm,
    unfold degree at H,
    have : m ∉ f.support,
      intro H2,
      rw finset.sup_le_iff at H,
      have H3 := H m H2,
      revert Hm,
      show ¬ (n < m),
      apply not_lt_of_ge,
      exact H3,
      rw ←decidable.not_not_iff (coeff f m = 0),
      intro H4,
      apply this,
      rw finsupp.mem_support_to_fun,
      exact H4},
  { intro H,
--    have H2 := H (with_bot_succ n) (with_bot_lt_succ n),
    unfold degree,
    refine finset.sup_le _,
    intros b Hb,
    rw finsupp.mem_support_to_fun at Hb,
    change coeff f b ≠ 0 at Hb,
    apply decidable.of_not_not _, apply_instance,
    intro Hn,
    replace Hn := lt_of_not_ge Hn,
    apply Hb,
    apply H,
    exact Hn,
  }
end
```
This is with the `poly_coeffs` branch of community mathlib, with Kenny's coeff commands. I think that it might be possible to golf that a bit.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134000891):
```lean
def coeff_zero_iff_deg_le {R} [comm_semiring R] (f : polynomial R) (n : with_bot ℕ) :
degree f ≤ n ↔ ∀ m : ℕ, n < m → coeff f m = 0 :=
⟨λ (H : finset.sup (f.support) some ≤ n) m (Hm : n < (m : with_bot ℕ)), decidable.of_not_not $ λ H4,
  have H1 : m ∉ f.support,
    from λ H2, not_lt_of_ge ((finset.sup_le_iff.1 H) m H2 : ((m : with_bot ℕ) ≤ n)) Hm,
  H1 $ (finsupp.mem_support_to_fun f m).2 H4,
λ H, finset.sup_le $ λ b Hb, decidable.of_not_not $ λ Hn, 
  (finsupp.mem_support_to_fun f b).1 Hb $ H b $ lt_of_not_ge Hn⟩
```

That'a a bit better

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134006427):
This code seems to demonstrate various things which are currently not optimal:

```lean
lemma leading_term_bdd_deg_ideal {R} [decidable_eq R] [nonzero_comm_ring R]
  (I : set (polynomial R)) [@is_submodule R _ _ _ I] (n : ℕ) :
submodule R R :=
submodule.map (λ f : polynomial R, coeff f n) (@coeff_is_linear R _ _ n)
  (⟨I,by apply_instance⟩ ⊓ ⟨deg_le R n,by apply_instance⟩)

```

I has type `set S` for `S` a ring which is hence an $$S$$-module and an $$R$$-module. I want to prove a relatively straightforward theorem about a sub-$$R$$-module of $$S$$. I could have proved it for sub-$$S$$-modules but it's true for sub-$$R$$-modules so I have written it in the correct generality. Of course I now want to immediately apply it to a sub-$$S$$-module and type class inference is going to struggle with that because there is some content there (the lemma that the $$R$$-module structure on $$S$$ is induced by a ring map $$R\to S$$ and hence any $$S$$-module is naturally an $$R$$-module, and that all these $$R$$-module structures are the same). I also have a problem with intersections of submodules. I carry around the *sets*, because the proofs that they are submodules are known to type class inference. However when I want to construct their intersection using the lattice structure I find myself having to explicitly magic up the instances to turn the sets into modules. @**Mario Carneiro** this is real-world module usage -- in general I want to know that if $$A\to B$$ is a map of rings then a $$B$$-module "is" an $$A$$-module. It does not sound to me like this is appropriate for type class inference. Is it? If I have to make the instances explicitly then is this an indication that modules shouldn't be typeclasses at all, or that some other sort of rethink is needed?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 15 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134026366):
I will not start on this until I've finished the current refactoring, but I think it is the right time to bring this up. I think that we should drop the out_param on the scalar field of a module. Downsides:

1. `linear_map`, `submodule`, `module` and other such types will require an explicit ring argument
2. `a • x` will not typecheck if the type of `a` is not specified
3. `add_comm_group B` cannot be a parent of `module A B`

I think (1) is mainly a problem for notation, i.e. something like `M1 ->l M2` won't work since you have to shove `R` in the notation somewhere. (2) is possibly a problem if we are leaving off the type in pis or such but I can't see it having a big effect. (3) is the biggest problem, since it will add to the things you have to say about modules in proofs, but I'm already testing this change with the current refactoring. Upsides:

1. no more mysterious module typeclass timeout problems
2. no more questions about what to have implicit and what to have typeclass implicit
3. you can freely use modules over different rings, even in the same proof or statement
4. we can fill out the module typeclass hierarchy, rather than hiding some instances that have bad behavior like the endomorphism ring

I think that on the whole the benefits outweigh the downsides. The contract of an out_param is that you should only have one instance for `module ? B` for fixed B. This is just not true in advanced math. Indeed it's false even in the most trivial case, since you can always restrict the ring to a subring. @**Johannes Hölzl** @**Kevin Buzzard** Thoughts?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 15 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134026520):
will it be finally possible to tell Lean that every abelian group is a Z-module? :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 15 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134026534):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 15 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134026535):
yay

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 15 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134026575):
it is very similar to the removal of out_param for `^`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 15 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134026583):
now we can have has_pow instances for `monoid, nat`, `group, int`, and `cardinal, cardinal` all at the same time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134027008):
I don't think I am competent enough to understand the ramifications of what you are suggesting, but I am all for changing things if you think it's a good idea, and will report back if I find any problems -- when things have settled down I will simply just go back to Hilbert and see what happens.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134027015):
All I can say is that I have now seen with my own eyes that I want subsets of M to be either A-submodules or B-submodules and I am happy to say which.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 15 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134027060):
are you comfortable saying which in all circumstances, even when there is only one reasonable choice?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134027170):
I am going to say yes I'm happy doing this. It doesn't feel unnatural to say "R-submodule" everywhere even if there is only one ring R -- after all, the axioms for a submodule really do depend on R.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 15 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134027183):
and now `ideal` actually has some work to do - `ideal of R` means `R-submodule of R`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134027185):
Of course others might not be so happy but I think that even when I teach students about vector spaces over k I might even say "k-subspace" a lot.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134027225):
Oh but actually this is now better, because for ideals I would get annoyed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134027226):
For ideals there's only one choice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 15 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134027229):
Although `subspace` is still being useless

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134027238):
but that's Ok I think. I like the sound of this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 16 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134028228):
I don't understand why `module A B` cannot have `add_comm_group` as parent? What is the problem?
For me Point 3 (a type often has multiple different modules for different rings) is the main reason. I think everything else could be worked around eventually (maybe in Lean 4). And it looks we were already running into problems with the field instance for vector spaces. So I think this is a very good change!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 16 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134038660):
If `module A B` requires both `A` and `B` before being synthesized, as would happen if `A` was no longer marked an out_param, but it had a parent coercion to `add_comm_group B`, then you could not resolve a goal like `has_zero B`. It would climb the hierarchy to `add_comm_group B`, but then the parent coercion `\all A B [ring A] [module A B], add_comm_group B` would not be triggered since `A` is not yet known. Indeed this is a classic example of an unusable instance, since it has dependencies that don't appear in the target type.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Sep 16 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134045911):
Is there a place where I can find all the classes (like linear_order or module)? I think my distances are a semi module, but I don't know where they are, and they might even be something stronger.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134045961):
`git grep` says there are about 200 classes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134045966):
but probably there's a bunch of false positives. What do you want to do with them now? Just look at them?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Sep 16 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134046014):
I don't think I could sift through 200

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134046015):
If you're now assuming the parallel postulate then you can divide by a positive integer, so your distances are now probably a semi vector space over the semi field Q_{>=0}. But I am not sure that these concepts exist or are useful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134046021):
Hmm, I guess $$\mathbb{Q}$$ is a semi-module over $$\mathbb{Q}^+$$ with no basis, so there will be no theorem of the form that every semimodule over $$\mathbb{Q}^+$$ has a basis (in contrast to the theory of fields, where every vector space has a basi).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Sep 16 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134046058):
I have a linear_order, with a 0. My angles have a maximum in addition to that, but I plan to turn them into mod 360 (or 2*pi).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134046061):
Your angles currently are [0,180] basically, right? Or (0,180) or something.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Sep 16 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134046067):
inclusive, but I don't need to make those at the moment. But I would like to have a linear order and a minimum (which is 0).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134046108):
The point of this thread was for me to whinge about modules and ideals and things, but mathlib is currently undergoing a bit of a transition in the way it handles this stuff. So introducing semimodules into your work might mean that you have to rewrite later. As you might have seen from yesterday, there seems to be still some discussion about exactly how the semiring will be mentioned (or perhaps decisions have been made but not implemented yet).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Sep 16 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134046156):
Ok, I guess I'll just have a linear_order, and a theorem that says everything is bigger than 0.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/134046163):
well you can certainly have a linear order. I don't think looking through all of Lean trying to spot classes is the way to see what's there. I think you should look through mathlib, spot a directory or a file which looks relevant to you like `order/basic.lean` and then take a look at the types and typeclasses being used in that file. Right click on something like `preorder` to find where it's defined (a preorder is another example of something which is used a lot in Lean but which is hardly ever defined or used in a maths UG degree, we see partial orders but this is even weaker) and then just poke around. I just tried this and ending up finding my way to core Lean's `init/algebra/order.lean` very quickly. I think doing stuff like this can be pretty instructive.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 08 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semimodules%20nein%20danke/near/147286411):
```quote
will it be finally possible to tell Lean that every abelian group is a Z-module? :D
```
@**Mario Carneiro** do you think we're ready to teach Lean this fact?


{% endraw %}
