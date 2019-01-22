---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/141825kbb/47597heckeoperator.html
---

## [kbb](index.html)
### [hecke operator](47597heckeoperator.html)

#### [Johan Commelin (Sep 14 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/133964447):
The next step would be to define https://en.wikipedia.org/wiki/Hecke_operator#Explicit_formula on the subspace of `Petersson_weight k` functions on the upper half plane.

#### [Johan Commelin (Sep 14 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/133964469):
Afterwards, we need to show that it preserves `holomorphic`, `bounded_at_infinity` and `zero_at_infinity`.

#### [Johan Commelin (Sep 14 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/133964474):
We also need to prove that it is linear.

#### [Johan Commelin (Sep 14 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/133972202):
Ok, this stuff is a mess. I just wanted to plug a matrix with determinant `m` into the Möbius transform action. Of course that doesn't work...

#### [Kenny Lau (Sep 14 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/133972741):
wow this is really a heck of an operator

#### [Johan Commelin (Sep 14 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/133973372):
Ok, I think we should forget about Hecke operators. We can define them if we want. But we won't even get close to formalising the abstract of Kevin's paper.

#### [Johan Commelin (Sep 14 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/133973393):
Until 5 minutes ago, I thought that the only thing missing was the fact that $$S_k$$ is finite-dimensional (which requires Riemann–Roch).

#### [Johan Commelin (Sep 14 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/133973470):
But of course, with the definition of the Hecke operator that we are now going after, we will get a linear operator on a complex vector space. This beast will have a characteristic polynomial defined over `complex`.

#### [Johan Commelin (Sep 14 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/133973490):
Such polynomials do not have very interesting splitting fields.

#### [Patrick Massot (Sep 15 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012391):
How do you prove this polynomial has interesting coefficients in the real world?

#### [Reid Barton (Sep 15 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012447):
are the coefficients actually rational?

#### [Patrick Massot (Sep 15 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012451):
I guess there are integers

#### [Patrick Massot (Sep 15 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012458):
But I know no number theory

#### [Patrick Massot (Sep 15 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012512):
And it probably also requires Fourier series for modular forms

#### [Reid Barton (Sep 15 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012524):
If they are actually integers, then can't we define the splitting field to be the smallest subfield of C which contains the roots?

#### [Johan Commelin (Sep 15 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012563):
The Hecke operator acts on the singular homology of the modular curve. This has Q coeffients

#### [Reid Barton (Sep 15 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012567):
Then we don't need either splitting fields or to prove that the coefficients are integers

#### [Johan Commelin (Sep 15 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012570):
By Hodge theory you recover the cusp forms in the complexification of this cohomology group.

#### [Johan Commelin (Sep 15 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012574):
But maybe I'm using a sledgehammer, there might be a more low-brow proof.

#### [Reid Barton (Sep 15 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012578):
Of course then we wouldn't know that the this field is a finite extension...

#### [Johan Commelin (Sep 15 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012591):
Right...

#### [Johan Commelin (Sep 15 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012594):
Somehow I don't mind sorrying finite-dimensionality of S_k, but sorrying this fact feels like a big cheat.

#### [Patrick Massot (Sep 15 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012653):
I guess Hecke's point of view was less sophisticated

#### [Johan Commelin (Sep 15 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012721):
Probably. I think using Fourier coefficients there is another approach.

#### [Johan Commelin (Sep 15 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012733):
But then, we didn't want to do Fourier coefficients either.

#### [Johan Commelin (Sep 15 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012777):
So maybe we just define the Hecke operator over `complex`, and then wrap up the project.

#### [Johan Commelin (Sep 18 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163084):
Let's put this discussion in the correct thread.

#### [Johan Commelin (Sep 18 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163095):
The following lemma is crucial:
```lean
theorem M_trans_SL2Z_H {m : ℤ} {h : m > 0} {M : SL2Z} {A : Mat m} :
M_trans h (SL2Z_M m M A) = SL2Z_H M ∘ (M_trans h A) :=
begin
  funext z,
  simp [M_trans, SL2Z_M, SL2Z_H, «Möbius_transform»],

-- m : ℤ,
-- h : m > 0,
-- M : SL2Z,
-- A : Mat m,
-- z : ↥ℍ
-- ⊢ (↑(M.a) * ↑(A.b) + (↑(M.b) * ↑(A.d) + (↑(M.a) * ↑(A.a) + ↑(M.b) * ↑(A.c)) * ↑z)) /
--       (↑(M.c) * ↑(A.b) + (↑(M.d) * ↑(A.d) + (↑(M.c) * ↑(A.a) + ↑(M.d) * ↑(A.c)) * ↑z)) =
--     (↑(M.b) + ↑(M.a) * ((↑(A.b) + ↑(A.a) * ↑z) / (↑(A.d) + ↑(A.c) * ↑z))) /
--       (↑(M.d) + ↑(M.c) * ((↑(A.b) + ↑(A.a) * ↑z) / (↑(A.d) + ↑(A.c) * ↑z)))

  -- ring, -- fails
end
```

#### [Johan Commelin (Sep 18 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163130):
I'm not surprised that `ring` fails, because there are divisions. But boy, I really don't want to prove this stuff by hand.

#### [Patrick Massot (Sep 18 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163207):
I could try since Johannes is working for me right now

#### [Patrick Massot (Sep 18 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163212):
Did you push everything?

#### [Johannes Hölzl (Sep 18 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163237):
Hm, isabelle has `field_simps` for these kind of things. `field_simps` is a collection which applies distributivity, and tries to remove the `x / d`. Sometimes it needs to introduces `if` to check if `d = 0`

#### [Patrick Massot (Sep 18 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163272):
We need this *so* badly

#### [Johan Commelin (Sep 18 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163669):
I pushed some stuff

#### [Johan Commelin (Sep 18 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163689):
I've got `M` out of `f`, so now we need to do the cocycle computation

#### [Johan Commelin (Sep 18 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163742):
Which is just as ugly as the other thing I just posted.

#### [Patrick Massot (Sep 18 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163769):
Did you do the other ugly thing?

#### [Johan Commelin (Sep 18 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134164244):
No, everything I did was pushed.

#### [Johan Commelin (Sep 18 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134164251):
I went to the last sorry: proving that the result again has weight `k`

#### [Johan Commelin (Sep 18 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134164256):
I now have the following goal
```lean
⊢ quotient.lift_on' o
      (λ (A : Mat m), 1 / (↑(A.c) * ↑(SL2Z_H M z) + ↑(A.d)) ^ (k + 1) * f.val (M_trans h A (SL2Z_H M z)))
      _ =
    (↑(M.c) * ↑z + ↑(M.d)) ^ (k + 1) *
      quotient.lift_on' o (λ (A : Mat m), 1 / (↑(A.c) * ↑z + ↑(A.d)) ^ (k + 1) * f.val (M_trans h A z)) _
```

#### [Johan Commelin (Sep 18 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134164263):
How do I get past that `quotient.lift_on'`?

#### [Patrick Massot (Sep 18 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134164264):
I'm working on M_trans_SL2Z_H

#### [Johannes Hölzl (Sep 18 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134164721):
eliminate `o`. Easiest: `rcases o with <x>`.

#### [Johan Commelin (Sep 18 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134164982):
Thanks, that worked!

#### [Johan Commelin (Sep 18 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134164990):
@**Patrick Massot** The name is wrong. The final `_H` should be `_M`.

#### [Johan Commelin (Sep 18 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134164995):
With `_H` it is another lemma, and I need that one now (-;

#### [Patrick Massot (Sep 18 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134165060):
but do you still want ` {m : ℤ} {h : m > 0} {M : SL2Z} {A : Mat m} : M_trans h (SL2Z_M m M A) = SL2Z_H M ∘ (M_trans h A)`?

#### [Patrick Massot (Sep 18 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134165078):
Or only the other one?

#### [Johan Commelin (Sep 18 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134165198):
No, the one you are working on is used

#### [Johan Commelin (Sep 18 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134165204):
I just realised that I had the wrong name.

#### [Johan Commelin (Sep 18 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134165210):
You can already see it being used

#### [Johan Commelin (Sep 18 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134165214):
In what I last pushed

#### [Johan Commelin (Sep 18 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134166605):
Aaahrg, the final sorry is a real pain. I'm now even confused about the maths again.

#### [Johan Commelin (Sep 18 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134166644):
OTOH, those are the better moments of theorem proving (-; I'm rather confused about the maths than that I'm fight silly `↑`

#### [Patrick Massot (Sep 18 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167046):
I just pushed something

#### [Patrick Massot (Sep 18 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167084):
Things are reduced to many variation on https://github.com/semorrison/kbb/blob/42b4509e2d9ca5beaeb712a17fc0f5754f73854c/src/hecke_operator.lean#L16 which itself is a variation on https://github.com/semorrison/kbb/blob/42b4509e2d9ca5beaeb712a17fc0f5754f73854c/src/upper_half_space.lean#L37

#### [Patrick Massot (Sep 18 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167087):
But I'm tired of fighting this

#### [Patrick Massot (Sep 18 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167137):
After writing https://github.com/semorrison/kbb/blob/42b4509e2d9ca5beaeb712a17fc0f5754f73854c/src/hecke_operator.lean#L32-L49

#### [Patrick Massot (Sep 18 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167150):
One day we will think back and laugh. But right now it's only screaming: Lean is nowhere near ready!

#### [Johan Commelin (Sep 18 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167160):
Right, it's really annoying

#### [Johan Commelin (Sep 18 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167368):
I also pushed. I didn't really get very far.

#### [Patrick Massot (Sep 18 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167442):
Maybe we can switch sides

#### [Johan Commelin (Sep 18 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167477):
So, on my side that maths is confusing.

#### [Johan Commelin (Sep 18 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167510):
If you take an `f` of weight `k`. After you plug it into Hecke, you want to check that the result has weight `k`.

#### [Johan Commelin (Sep 18 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167565):
But this means that you get `f(A • M z)`, where `A : Mat m` and `M : SL2Z`

#### [Johan Commelin (Sep 18 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167575):
Now you can't use the weight property of `f`.

#### [Johan Commelin (Sep 18 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167579):
Because the `M` is not on the left.

#### [Johan Commelin (Sep 18 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167618):
But `A M A¯¹` doesn't have to be in `SL2Z`...

#### [Johan Commelin (Sep 18 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167622):
So now I'm confused.

#### [Patrick Massot (Sep 18 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167681):
M should be on the left

#### [Patrick Massot (Sep 18 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167699):
We are acting from the left

#### [Patrick Massot (Sep 18 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167710):
At least on my piece of paper

#### [Patrick Massot (Sep 18 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167717):
And on Wikipedia

#### [Johan Commelin (Sep 18 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167915):
Yes, but `M` acts before `A` does, right?

#### [Johan Commelin (Sep 18 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167998):
It is `f (A • (M • z))`. So `M` is in fact acting on the left.

#### [Reid Barton (Sep 18 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168094):
Yeah you want to write $$AM = MA'$$ for some other $$A'$$ of det m, I think. The action of M will permute the terms of the sum

#### [Patrick Massot (Sep 18 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168109):
It didn't seem necessary earlier today

#### [Patrick Massot (Sep 18 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168230):
I think using reflexivity of the equivalence relation is enough

#### [Patrick Massot (Sep 18 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168259):
or reflexivity of equality

#### [Johan Commelin (Sep 18 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168287):
Hmmm... Reid, that might be the trick

#### [Johan Commelin (Sep 18 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168312):
I tried writing `AM = M'A`, but then your `M'` is not in SL2Z

#### [Johan Commelin (Sep 18 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168320):
But maybe with your attack it works.

#### [Patrick Massot (Sep 18 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168382):
You need to prove to compute the term in the sum corresponding to AM until you get the one corresponding to M

#### [Johan Commelin (Sep 18 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168396):
Because $$A' = M^{-1}AM$$ and $$M^{-1} \in \mathrm{SL2Z}$$

#### [Johan Commelin (Sep 18 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168457):
@**Patrick Massot** I don't think that will work. You really need to use that `f` has weight `k` at some point. So you need to rewrite things.

#### [Patrick Massot (Sep 18 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168465):
of course you use that!

#### [Johan Commelin (Sep 18 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168470):
Ok, then I'm confused about your plan.

#### [Reid Barton (Sep 18 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168637):
The book I have writes the action of SL(2, Z) (or more generally GL+(2, R)) on functions on the upper half plane as a right action, which I think makes more sense

#### [Reid Barton (Sep 18 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168658):
$$(f|_k \gamma)(z) = \frac{\det \gamma}{(cz + d)^k} f(\gamma z)$$

#### [Johan Commelin (Sep 18 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168754):
True, but it acts on the left on the plane, right?

#### [Reid Barton (Sep 18 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168764):
and also the Hecke operators
$$(f|_k T_p) = p^{k/2-1} \sum_\delta f|_k \delta$$ "where $$\delta$$ runs over a set of representatives for the distinct right cosets of $$\Gamma_1(N)$$ in $$\Delta_p$$"

#### [Reid Barton (Sep 18 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168767):
Yes

#### [Johan Commelin (Sep 18 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168805):
In Lean we only have the action on the plane, so far...

#### [Johan Commelin (Sep 18 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168811):
Well, and the action on other matrices.

#### [Reid Barton (Sep 18 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168877):
Then to check that the Hecke operator preserves modular forms of weight k you need to show that
$$(\sum_\delta f|_k\delta)|_k \gamma = \sum_\delta f|_\delta$$ and the strategy is going to be to move $$\gamma$$ past $$\delta$$ and reindex

#### [Reid Barton (Sep 18 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169028):
Yeah, I'm just trying to show how to isolate the step where you reindex the sum

#### [Reid Barton (Sep 18 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169140):
do we even know yet that the Hecke operator preserves holomorphic functions?

#### [Johan Commelin (Sep 18 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169222):
That statement does not make sense yet (-;

#### [Johan Commelin (Sep 18 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169245):
Hmmm, maybe we could turn it into a sensible statement.

#### [Johan Commelin (Sep 18 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169264):
At the moment the Hecke operators are being defined as operators on functions of weight k

#### [Reid Barton (Sep 18 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169287):
do we know that (az + b)/(cz + d) is itself a holomorphic function?

#### [Johan Commelin (Sep 18 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169290):
Afterwards we want to check that the preserve holomorphic functions and functions bound at infinity.

#### [Reid Barton (Sep 18 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169295):
right

#### [Johan Commelin (Sep 18 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169296):
We do not know that

#### [Reid Barton (Sep 18 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169301):
I see

#### [Johan Commelin (Sep 18 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169311):
It might be a nice example of a holomorphic function (-;

#### [Kenny Lau (Sep 18 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169484):
are there any sorry that I can fill in?

#### [Patrick Massot (Sep 18 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169536):
**YES**

#### [Johan Commelin (Sep 18 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169571):
@**Kenny Lau** It might be good to read the discussion of the last 20 minutes

#### [Johan Commelin (Sep 18 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169605):
There is some non-trivialish math going into this. (Nothing you don't understand in 30 secs) But still...

#### [Kenny Lau (Sep 18 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169681):
where is the sorry?

#### [Johan Commelin (Sep 18 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169717):
Look in the Hecke file

#### [Kenny Lau (Sep 18 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169722):
is it WIP?

#### [Kenny Lau (Sep 18 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169736):
I don't want to cause pull conflict

#### [Patrick Massot (Sep 18 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169829):
I stand by my claim we don't need any reordering

#### [Johan Commelin (Sep 18 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169842):
I'm not working on it right now

#### [Johan Commelin (Sep 18 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169845):
Need to do some emails

#### [Patrick Massot (Sep 18 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169848):
Hold on 10 sec

#### [Patrick Massot (Sep 18 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169981):
Ok, look at https://github.com/semorrison/kbb/blob/master/src/hecke_operator.lean#L76

#### [Patrick Massot (Sep 18 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169986):
I claim there is no problem here

#### [Patrick Massot (Sep 18 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169993):
Except we miss a field tactic

#### [Patrick Massot (Sep 18 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170009):
Kenny: you can fill in all sorries in that file

#### [Kenny Lau (Sep 18 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170053):
well you just pulled

#### [Kenny Lau (Sep 18 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170054):
pushed*

#### [Patrick Massot (Sep 18 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170062):
yes

#### [Patrick Massot (Sep 18 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170066):
Don't forget what I wrote: Things are reduced to many variation on https://github.com/semorrison/kbb/blob/42b4509e2d9ca5beaeb712a17fc0f5754f73854c/src/hecke_operator.lean#L16 which itself is a variation on https://github.com/semorrison/kbb/blob/42b4509e2d9ca5beaeb712a17fc0f5754f73854c/src/upper_half_space.lean#L37

#### [Patrick Massot (Sep 18 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170071):
About the other sorries in that file

#### [Patrick Massot (Sep 18 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170090):
And if you really feel like impressing us, you can get rid of all quadruples of integers and use matrices everywhere

#### [Patrick Massot (Sep 18 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170094):
I'm giving up on this.

#### [Patrick Massot (Sep 18 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170167):
Honestly I think the upshot of this story is that Lean is not yet ready for anything involving divisions

#### [Kenny Lau (Sep 18 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170192):
I don't feel like impressing anyone

#### [Mario Carneiro (Sep 18 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170199):
You could always just apply division cancellation theorems, it's not that hard...

#### [Patrick Massot (Sep 18 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170223):
Mario, did you see https://github.com/semorrison/kbb/blob/master/src/hecke_operator.lean#L32-L49?

#### [Mario Carneiro (Sep 18 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170224):
I'm not too keen on replacing these direct and logical proofs with arcane tactic-generated proofs

#### [Patrick Massot (Sep 18 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170283):
The trouble with division cancellations theorems is that terms must be next to each other

#### [Johan Commelin (Sep 18 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170285):
I am very keen on have a tactic that will write the direct and logical proof for me.

#### [Patrick Massot (Sep 18 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170290):
hence the endless conv

#### [Patrick Massot (Sep 18 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170297):
No, this is stupid

#### [Patrick Massot (Sep 18 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170303):
We don't want to see this proof

#### [Patrick Massot (Sep 18 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170311):
We want Lean to compute, as with ring

#### [Mario Carneiro (Sep 18 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170313):
I think it can be done better than that

#### [Mario Carneiro (Sep 18 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170324):
plus a little `calc` would go a long way in that proof

#### [Mario Carneiro (Sep 18 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170327):
what is all the uparrow stuff?

#### [Johan Commelin (Sep 18 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170367):
ℤ-matrices acting on ℂ

#### [Johan Commelin (Sep 18 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170408):
There is a boatload of stuff in this repo that could be generalised. But some thing's can't... for example this lemma could be about arbitrary matrices in `GL2R+`. But that would shift the arrows somewhere else.

#### [Johan Commelin (Sep 18 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170826):
I'm looking forward to Lean Forward... these things are the basic Lego blocks that Sander Dahmen works with.

#### [Mario Carneiro (Sep 18 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170886):
Okay, I've downloaded and set up kbb. What area needs my attention?

#### [Johan Commelin (Sep 18 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170900):
`hecke_operator.lean`

#### [Johan Commelin (Sep 18 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170907):
You'll get pulled into the other files by `import`

#### [Johan Commelin (Sep 18 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170919):
Beware, there are minor dragons in these files.

#### [Johan Commelin (Sep 18 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170944):
Every 10 lines will give you another opportunity for a major refactor (-;

#### [Patrick Massot (Sep 18 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170952):
The area where you write a field tactic

#### [Johan Commelin (Sep 18 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170967):
@**Kenny Lau** you might want to tell @**Mario Carneiro** which `sorry` you are working on.

#### [Kenny Lau (Sep 18 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134171012):
all of them

#### [Mario Carneiro (Sep 18 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134171030):
lol that's not happening before friday Patrick

#### [Patrick Massot (Sep 18 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134171055):
I'm sure Kevin will understand

#### [Patrick Massot (Sep 18 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134171072):
Do you think you could do it before he turns 60?

#### [Johan Commelin (Sep 18 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134171083):
@**Mario Carneiro** Any improvements of the repo would be appreciated.

#### [Johan Commelin (Sep 18 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134171095):
`matrices` and `determinants` seem to be almost ready to merge. And independent of the other files.

#### [Kenny Lau (Sep 18 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134172685):
@**Patrick Massot** what's the math proof of the thing that Patrick claims to be true?

#### [Kenny Lau (Sep 18 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134172738):
and what is the second thing?

#### [Patrick Massot (Sep 18 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134172751):
The maths proof is to expand everythings and compute

#### [Patrick Massot (Sep 18 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134172759):
But probably there is a better way to setup all this

#### [Kenny Lau (Sep 18 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134172828):
I filled in two of the sorries

#### [Kenny Lau (Sep 18 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134172834):
see if you can learn anything therefrom

#### [Johan Commelin (Sep 19 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134223218):
Reid quoted some formulas containing the Petersson slash operator (of weight `k`). Would it make sense to mimic that notation, somehow? I think we should also wrap `M_trans` and `SL2Z_H` into notation (`has_scalar`). I hope it will make statements more readable. Maybe it will even improve proofs, I don't know.

#### [Johan Commelin (Sep 19 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134225022):
@**Kenny Lau** I agree with Patrick's claim. I made some small rewrites. Maybe now it is easier to math-see why it is true. I still wish `ring` would kill this. But it doesn't... because there are divisions. I hate divisions in Lean.

#### [Johan Commelin (Sep 19 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134225043):
(Oooh, I also pushed those small rewrites.)

