---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88074castwoes.html
---

## Stream: [general](index.html)
### Topic: [cast woes](88074castwoes.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 25 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127073963):
```lean
import data.int.basic data.nat.cast 

#check int.mod_add_mod -- ∀ (m n k : ℤ), (m % n + k) % n = (m + k) % n
-- #check nat.mod_add_mod -- unknown identifier
-- so let's create it

-- note:
#check int.of_nat_mod -- ∀ (m n : ℕ), ↑m % ↑n = int.of_nat (m % n)

theorem nat.mod_add_mod : ∀ (m n k : ℕ), (m % n + k) % n = (m + k) % n :=
begin 
  intros m n k,
  apply int.of_nat_inj,
  rw ←int.of_nat_mod,
  rw ←int.of_nat_mod,
  rw nat.cast_add -- fails
  /-
  rewrite tactic failed, did not find instance of the pattern in the target expression
  ↑(?m_4 + ?m_5)
state:
m n k : ℕ
⊢ ↑(m % n + k) % ↑n = ↑(m + k) % ↑n
  -/
  sorry
end 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 25 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127073966):
What am I doing wrong?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 25 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127073972):
I found a "hole" in mathlib -- but am failing to fix it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 25 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127074019):
I tried to be really precise:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 25 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127074021):
```lean
have H1 := @nat.cast_add ℤ _ _ (m % n) k,
  /-
  H1 : ↑(m % n + k) = ↑(m % n) + ↑k
  ⊢ ↑(m % n + k) % ↑n = ↑(m + k) % ↑n
  -/

  -- rw H1, -- fails
  /-
  rewrite tactic failed, did not find instance of the pattern in the target expression
  ↑(m % n + k)
state:
m n k : ℕ,
H1 : ↑(m % n + k) = ↑(m % n) + ↑k
⊢ ↑(m % n + k) % ↑n = ↑(m + k) % ↑n
  -/
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 25 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127074028):
I switched notation off and the rewrite still looked like it should work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 25 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127074031):
I switched pp.all off and got swamped.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 25 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127074035):
`int.coe_nat_add` is the correct lemma, rather than `nat.cast_add` I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 25 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127074043):
You're right Chris.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 25 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127074045):
Do you know why what I tried is failing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 25 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127074121):
Because `cast` is a coercion into a general ring, whereas there's a seperately defined coercion from`nat` to `int`, probably because it's in core, but cast is is in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 25 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127074193):
Also, `of_nat` is a more natural function to use as the coercion than `cast` which just does 1 + 1 + 1 ...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 25 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127074721):
You can probably use `nat.modeq` to prove this one, there are more modeq theorems than there are theorems about mod

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122090):
```quote
You can probably use `nat.modeq` to prove this one, there are more modeq theorems than there are theorems about mod
```
My eyes are opened!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122131):
I had somehow ruled out this MOD stuff as "another way of setting up the theory, which I didn't use".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122133):
I've always thought that MOD notation was horrible, by the way.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122177):
pmod is standard LaTeX notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 26 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122216):
there were technical reasons I couldn't use parens and lowercase

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122217):
I think using LaTeX as a guide is a good idea. I'm really familiar with LaTeX notation and it still occasionally confuses me that `\equiv` is not `equiv`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122218):
Oh --

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122219):
this was forced upon you somehow?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122220):
I had no idea! I just thought it was a wacky design decision

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122223):
the MOD stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 26 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122226):
I'm not even sure the notation is worth it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122227):
This wasn't the fault of some labour-saving tactic was it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122264):
The notation is what mathematicians want

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 26 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122267):
it's a parsing thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122268):
We are sticklers for notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122269):
That's why I mentioned it -- it looks funny to mathematicians because there is already standard notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 26 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122310):
It's probably better than no notation, but even as it is it's a bit problematic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122315):
it enables you to write uncluttered calc proofs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122316):
so it's definitely better than no notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122317):
but it still looks funny

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122318):
To be honest I've never used it -- I assume it can be used in calc proofs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122319):
I'm giving a talk on this stuff in about 10 hours

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 26 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122324):
I never tried it, but I think chris did

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122325):
Maybe it's about time I learnt how it worked.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122327):
@**Chris Hughes** how did you learn that funny `MOD` stuff?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 26 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122380):
What funny MOD stuff?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 23 2019 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/156678741):
I have generally got the hang of how to handle casts now. The point of view which I want to push amongst the UGs is that even though yes it's annoying that natural numbers aren't actually real numbers, `simp` should do all the translating for you. But here's an example where I couldn't make it work:

```lean
import data.real.basic

example (M : ℕ) (H : 0 < M + 1) : (0 : ℝ) < M + 1 :=
begin
  simp [H],
  -- ⊢ 0 < 1 + ↑M
  -- gaargh
  -- simp at H, -- won't change it to 0 < 1 + M
  sorry
end
```

Applying `simp` to nat `M + 1` doesn't change it, but applying `simp` to real `M + 1` changes it to `1 + M` and this somehow means Lean loses track.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 23 2019 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/156678755):
I know I can use some cast_lt or whatever, but this is exactly what I am trying to avoid. `simp` is usually good at these.


{% endraw %}
