---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64025multiplayerlean.html
---

## Stream: [general](index.html)
### Topic: [multiplayer lean](64025multiplayerlean.html)

---

#### [Kevin Buzzard (Nov 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiplayer%20lean/near/148818374):
At Xena today about six people collaborated in CoCalc using mathlib, and they made dihedral groups! @**Amelia Livingston** @**Kenny Lau** @**Jean Lo** @**Chris Hughes** @**Calle Sönne** @**Ken Lee** together wrote the below. It was *really funny* watching it happen, not least at the beginning when people kept changing the definition of multiplication and/or inverse because it wasn't quite right, whilst other people were trying to prove things about these functions at the same time. Once it stabilised things worked quite well. They also implemented https://xenaproject.wordpress.com/2018/04/30/group-theory-revision/ . It's still going, although several of the contributors have left now; they're proving stuff like how dihedral groups aren't abelian etc.

```lean
import data.zmod.basic data.bool tactic.tidy group_theory.subgroup

class has_group_notation (G : Type) extends has_mul G, has_one G, has_inv G

structure group_core (G : Type*) extends has_group_notation G :=
(mul_assoc : ∀ (a b c : G), a * b * c = a * (b * c))
(one_mul : ∀ (g : G), 1 * g = g)
(mul_left_inv : ∀ (g : G), g⁻¹ * g = 1)

private theorem group_core.mul_inv {G : Type*} (hg : group_core G) (g : G) :
  by haveI := hg.to_has_group_notation; exact g * g⁻¹ = 1 :=
by letI := hg.to_has_group_notation; exact
have g⁻¹⁻¹ * g⁻¹ * g * g⁻¹ = 1,
  by rw [hg.mul_assoc, hg.mul_assoc, ← hg.mul_assoc (g⁻¹), hg.mul_left_inv, hg.one_mul, hg.mul_left_inv],
by rwa [hg.mul_left_inv, hg.one_mul] at this

private theorem group_core.mul_one {G : Type*} (hg : group_core G) (g : G) :
  by haveI := hg.to_has_group_notation; exact g * 1 = g :=
by letI := hg.to_has_group_notation; exact
calc  g * 1
    = g * (g⁻¹ * g) : by rw [hg.mul_left_inv g]
... = g : by rw [← hg.mul_assoc, group_core.mul_inv hg g, hg.one_mul]

def group.of_core {G : Type*} (hg : group_core G) : group G :=
by letI := hg.to_has_group_notation; exact
{ mul := (*),
  mul_assoc := hg.mul_assoc,
  one := 1,
  one_mul := hg.one_mul,
  mul_one := group_core.mul_one hg,
  inv := has_inv.inv,
  mul_left_inv := hg.mul_left_inv
}

-- ff,a := ρ^a
-- tt,a := σ * ρ^a
definition dihedral2 (n : ℕ+) := bool × (zmod n)

namespace dihedral2

variable {n : ℕ+}

-- ρ^a * ρ^b = ρ^(a+b)
-- (σ * ρ^a) * ρ^b = σ * ρ^(a+b)
-- (ρ^a) * (σ ρ^b) = σ * ρ^(b-a)
-- (σ ρ^a) * (σ ρ^b) = ρ^(b-a)
instance : has_mul (dihedral2 n) :=
⟨λ x y, ⟨bxor x.1 y.1, cond y.1 (y.2 - x.2) (x.2 + y.2)⟩⟩

@[simp] lemma mul_fst {x y : dihedral2 n} : (x * y).1 = bxor x.1 y.1 := rfl
@[simp] lemma mul_snd {x y : dihedral2 n} : (x * y).2 = cond y.1 (y.2 - x.2) (x.2 + y.2) := rfl

instance : has_one (dihedral2 n) := ⟨⟨ff,0⟩⟩

-- (σ * ρ^a)⁻¹ = σ * ρ^a
-- (ρ^a)⁻¹ = ρ^(-a)
instance : has_inv (dihedral2 n) := ⟨λ x, ⟨x.1, cond x.1 x.2 (-x.2)⟩⟩

protected theorem mul_assoc {n : ℕ+} (g h k : dihedral2 n) : g * h * k = g * (h * k) :=
begin
  apply prod.ext,
  { exact bool.bxor_assoc g.1 h.1 k.1 },
  rcases g with ⟨_,a⟩; rcases h with ⟨_|_,b⟩; rcases k with ⟨_|_,c⟩,
  { exact add_assoc a b c },
  { exact sub_add_eq_sub_sub_swap c a b },
  { exact sub_add_eq_add_sub b a c },
  { change c - (b - a) = a + (c - b), rw [← sub_add, add_comm] }
end

protected theorem one_mul {n : ℕ+} : ∀ g : dihedral2 n, 1 * g = g
| (ff, x) := prod.ext rfl (zero_add x)
| (tt, x) := prod.ext rfl (sub_zero x)

protected theorem mul_left_inv {n: ℕ+} : ∀ g : dihedral2 n, g⁻¹ * g = 1
| (ff, x) := prod.ext rfl (add_left_neg x)
| (tt, x) := prod.ext rfl (add_right_neg x)

instance : group (dihedral2 n) :=
group.of_core
{ mul := (*),
  inv := has_inv.inv,
  one := 1,
  mul_assoc := dihedral2.mul_assoc,
  one_mul := dihedral2.one_mul,
  mul_left_inv := dihedral2.mul_left_inv
}

def ρ : dihedral2 n := ⟨ff, 1⟩
def σ : dihedral2 n := ⟨tt, 0⟩

theorem rho_mul_sigma : (ρ * σ : dihedral2 n) = σ * ρ⁻¹ := rfl

instance {n : ℕ+} : fintype (dihedral2 n) := prod.fintype _ _
instance {n : ℕ+} : decidable_eq (dihedral2 n) := prod.decidable_eq

end dihedral2
```

#### [Kevin Buzzard (Nov 29 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiplayer%20lean/near/148819305):
It was the nerdiest thing I'd seen for quite some time. @**William Stein** we didn't use VS Code, we just worked together using the basic editor. It worked really well. Mathlib was really helpful -- without it we would have had to use `fin n` for a set with n elements, but with it we could use `zmod n` with its group structure.

#### [Kevin Buzzard (Nov 29 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiplayer%20lean/near/148820730):
Looking at the code now, the comments were crucial. People tended not to use the chat, they talked using comments. It became clear very early on that we needed comments to explain the conventions we were using, and I see now that whilst people tidied up the chatty comments they left in the comments explaining the mathematics (more precisely the conventions and basic notation), so in some sense it has created more readable Lean code.

#### [Scott Morrison (Nov 29 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiplayer%20lean/near/148821796):
This sounds fantastic.

#### [William Stein (Nov 30 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiplayer%20lean/near/148844392):
Thanks for explaining how the first serious collaborative use of cocalc lean went!  

>  People tended not to use the chat, they talked using comments.

This is something I've wondered about, since I've experienced this too.  It depends a lot on the sort of document being edited.  I also haven't quite figured out if I should add some extra support for "comments attributed to people".  When collaboratively editing markdown files, we (cocalc devs) often do this sort of thing (to attribute the remark):
```
> [ws] blah blah

> [hsy] blah blah
```

#### [William Stein (Nov 30 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiplayer%20lean/near/148844401):
@**Kevin Buzzard** I also implemented "run a bash command line in every student project" in case that helps you workaround the path issue more easily.

