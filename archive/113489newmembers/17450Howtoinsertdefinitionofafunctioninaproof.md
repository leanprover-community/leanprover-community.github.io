---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/17450Howtoinsertdefinitionofafunctioninaproof.html
---

## Stream: [new members](index.html)
### Topic: [How to insert definition of a function in a proof](17450Howtoinsertdefinitionofafunctioninaproof.html)

---

#### [Tobias Grosser (Oct 20 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136147887):
Hi, I again have a simple beginners questions. The definition of
```lean
def Gaussian_elimination [decidable_eq α] [has_inv α]:
   Π (m n), matrix (fin m) (fin n) α → 
   (matrix (fin m) (fin m) α × matrix (fin n) (fin n) α × nat)
| (x+1) (y+1) A :=
  let optional_ij := pick_encodable (α) (λ el, el ≠ 0) (x+1) (y+1) A in
  match optional_ij with
  | some ij :=
    let i := ij.1 in
    let j := ij.2 in
    let a := A i j in
    let A1 := xrow i 0 (xcol j 0 A) in
    let A1' := fin_swap A1 in 
    let B := A1' in 
    let u := ursubmx A1' in 
    let v := a⁻¹ • dlsubmx A1' in
    let (L, U, r) := Gaussian_elimination (x) (y) (drsubmx A1' - (v *ₘ u)) in 
    (
      xrow i 0 (fin_swap (block_mx 1 0 v L)),
      xcol j 0 (fin_swap (block_mx (λ i1 j1, a) u 0 U)),
      r + 1
    )
  | none :=
     (
      (1 : (matrix (fin (x+1)) (fin (x+1)) α)),
      (1 : (matrix (fin (y+1)) (fin (y+1)) α)),
      0
     )
  end
| x y A :=
     (
      (1 : (matrix (fin (x)) (fin (x)) α)),
      (1 : (matrix (fin (y)) (fin (y)) α)),
      0
```
appears in a proof  state:
```lean
α : Type,
_inst_5 : ordered_ring α,
_inst_8 : decidable_eq α,
_inst_9 : has_inv α,
_inst_10 : has_one α,
m n : ℕ,
M : matrix (fin m) (fin m) α
⊢ (Gaussian_elimination m m M).fst *ₘ ((Gaussian_elimination m m M).snd).fst = M
```

I expected a simple `rw Gaussian_elimination` to inline the definition of Gaussian_eliminatin into the proof. But unfortunately this did not work out. Any ideas what I did wrong?

#### [Tobias Grosser (Oct 20 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136148002):
I unfortunately just get "failed"

#### [Chris Hughes (Oct 20 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136148305):
It will only reduce if it's applied to `m+1` or `0`, not `m`

#### [Tobias Grosser (Oct 20 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136148381):
I see.

#### [Tobias Grosser (Oct 20 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136148383):
Any quick pointer how I introduce m+1 or 0?

#### [Tobias Grosser (Oct 20 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136148439):
Found it. Just need to do 'induction m'.

#### [Tobias Grosser (Oct 20 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136148481):
Thanks a lot, this was easy.

#### [Tobias Grosser (Oct 20 2018 at 03:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136149746):
OK, the basecase is now also proofen. Learned the 'ext' tactic and fin_zero_elim.

#### [Tobias Grosser (Oct 20 2018 at 03:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136149747):
I am now in
```lean
case nat.succ
α : Type,
_inst_5 : ordered_ring α,
_inst_8 : decidable_eq α,
_inst_9 : has_inv α,
_inst_10 : has_one α,
n m_n : ℕ,
m_ih :
  ∀ (M : matrix (fin m_n) (fin m_n) α),
    (Gaussian_elimination m_n m_n M).fst *ₘ ((Gaussian_elimination m_n m_n M).snd).fst = M,
M : matrix (fin (nat.succ m_n)) (fin (nat.succ m_n)) α
⊢ (Gaussian_elimination._match_1 m_n m_n M
         (λ (ij : fin (m_n + 1) × fin (m_n + 1)),
            Gaussian_elimination m_n m_n
              (drsubmx (fin_swap (xrow (ij.fst) 0 (xcol (ij.snd) 0 M))) +
                 -((M (ij.fst) (ij.snd))⁻¹ • dlsubmx (fin_swap (xrow (ij.fst) 0 (xcol (ij.snd) 0 M))) *ₘ
                      ursubmx (fin_swap (xrow (ij.fst) 0 (xcol (ij.snd) 0 M))))))
         (pick_encodable α (λ (el : α), ¬el = 0) (m_n + 1) (m_n + 1) M)).fst *ₘ
      ((Gaussian_elimination._match_1 m_n m_n M
          (λ (ij : fin (m_n + 1) × fin (m_n + 1)),
             Gaussian_elimination m_n m_n
               (drsubmx (fin_swap (xrow (ij.fst) 0 (xcol (ij.snd) 0 M))) +
                  -((M (ij.fst) (ij.snd))⁻¹ • dlsubmx (fin_swap (xrow (ij.fst) 0 (xcol (ij.snd) 0 M))) *ₘ
                       ursubmx (fin_swap (xrow (ij.fst) 0 (xcol (ij.snd) 0 M))))))
          (pick_encodable α (λ (el : α), ¬el = 0) (m_n + 1) (m_n + 1) M)).snd).fst =
    M
```

#### [Tobias Grosser (Oct 20 2018 at 03:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136149749):
That seems complicated.

#### [Tobias Grosser (Oct 20 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136149755):
In case anybody wants to drop me a bone, this would be appreciated.

#### [Chris Hughes (Oct 20 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136150894):
`funext` is a start

#### [Tobias Grosser (Oct 20 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136150900):
Thanks.

#### [Chris Hughes (Oct 20 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136150903):
But it looks really complicated.

#### [Tobias Grosser (Oct 20 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136150910):
That's what I feel.

#### [Tobias Grosser (Oct 20 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136150950):
Maybe I approach this from the wrong angle.

#### [Chris Hughes (Oct 20 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136150952):
What is `pick_encodable`?

#### [Tobias Grosser (Oct 20 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136150953):
I basically want to show that " (M : matrix (fin m) (fin m) α) : (getL M) *ₘ (getU M) = M :="

#### [Tobias Grosser (Oct 20 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136150963):
That comes from: `  let optional_ij := pick_encodable (α) (λ el, el ≠ 0) (x+1) (y+1) A in`

#### [Tobias Grosser (Oct 20 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136150969):
It finds a non-zero element in the matrix.

#### [Tobias Grosser (Oct 20 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151009):
And returns an optional.

#### [Chris Hughes (Oct 20 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151011):
What is `getL`?

#### [Tobias Grosser (Oct 20 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151015):
```lean
def getL [decidable_eq α] [has_inv α] {m n : nat}  (M : matrix (fin n) (fin m) α) :=
  let res := Gaussian_elimination n m M in
  res.1

def getU [decidable_eq α] [has_inv α] {m n : nat}  (M : matrix (fin n) (fin m) α) :=
  let res := Gaussian_elimination n m M in
  res.2.1
```

#### [Tobias Grosser (Oct 20 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151022):
That's the full algorithm:
```lean
def Gaussian_elimination [decidable_eq α] [has_inv α]:
   Π (m n), matrix (fin m) (fin n) α → 
   (matrix (fin m) (fin m) α × matrix (fin n) (fin n) α × nat)
| (x+1) (y+1) A :=
  let optional_ij := pick_encodable (α) (λ el, el ≠ 0) (x+1) (y+1) A in
  match optional_ij with
  | some ij :=
    let i := ij.1 in
    let j := ij.2 in
    let a := A i j in
    let A1 := xrow i 0 (xcol j 0 A) in
    let A1' := fin_swap A1 in 
    let B := A1' in 
    let u := ursubmx A1' in 
    let v := a⁻¹ • dlsubmx A1' in
    let (L, U, r) := Gaussian_elimination (x) (y) (drsubmx A1' - (v *ₘ u)) in 
    (
      xrow i 0 (fin_swap (block_mx 1 0 v L)),
      xcol j 0 (fin_swap (block_mx (λ i1 j1, a) u 0 U)),
      r + 1
    )
  | none :=
     (
      (1 : (matrix (fin (x+1)) (fin (x+1)) α)),
      (1 : (matrix (fin (y+1)) (fin (y+1)) α)),
      0
     )
  end
| x y A :=
     (
      (1 : (matrix (fin (x)) (fin (x)) α)),
      (1 : (matrix (fin (y)) (fin (y)) α)),
      0
     )
```

#### [Tobias Grosser (Oct 20 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151024):
It computes a matrix L, a matrix U and the rank of the matrix M.

#### [Tobias Grosser (Oct 20 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151130):
I feel I should proof something simpler.

#### [Tobias Grosser (Oct 20 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151131):
E.g. that the result matrix is in upper triangular form.

#### [Chris Hughes (Oct 20 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151312):
What are `xrow` and `fin_swap` and `block_mx`?

#### [Tobias Grosser (Oct 20 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151515):
https://github.com/tobig/lean-polyhedra/blob/master/src/polyhedra.lean

#### [Tobias Grosser (Oct 20 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151629):
http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.652.3183&rep=rep1&type=pdf

#### [Tobias Grosser (Oct 20 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151630):
Is the relevant paper.

#### [Tobias Grosser (Oct 20 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151670):
I just started playing around with it. See sec 3.1 for the relevant algorithm.

#### [Chris Hughes (Oct 20 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151823):
That is surprising. I was going to say that my instinct would be to do it totally differently, and express each Gaussian elimination operation, as multiplication by a well chosen matrix, and prove the properties of the matrices that correspond to the Gaussian elimination operations. Georges Gonthier probably knows what he's doing though.

#### [Tobias Grosser (Oct 20 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151874):
I am new to lean. Probably this problem is too difficult for now, but I feel I understand matrices so I want to follow a proof that already exists, is interesting and at the same time useful.

#### [Tobias Grosser (Oct 20 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151877):
If you have advices what would be reasonable steps and which parts would be useful for mathlib, that would certainly be helpful.

#### [Tobias Grosser (Oct 20 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151886):
The paper justifies some of the choices they have taken.

#### [Tobias Grosser (Oct 20 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151926):
Now the proof structure itself can likely be changed without affecting everything that uses Gaussian elimination.

#### [Tobias Grosser (Oct 20 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151927):
Would be interesting to see if your proof idea might even be nicer than their original proof idea.

#### [Tobias Grosser (Oct 20 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136151977):
I doubt that the proof structure depends a lot on coq vs. lean, but if your proof is more accessible to people less advanced than Georges, this would be interesting to me.

#### [Mario Carneiro (Oct 20 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152216):
My guess is that translating so strictly from Coq is not going to come out well

#### [Mario Carneiro (Oct 20 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152260):
The thing about translations is that even though the axioms are similar, the *language*, in the informal sense, is different. We use different modes of speech for the same kinds of things

#### [Mario Carneiro (Oct 20 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152265):
and the library is "written in that language", meaning that you will encounter friction if you don't use it

#### [Scott Morrison (Oct 20 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152284):
My student @**Jack Crawford** has also been looking at gaussian elimination. He's been using an inductive type describing individual steps of row operations.

#### [Scott Morrison (Oct 20 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152293):
It acts like a "relation" between two matrices, but carries the data of the elementary matrix to multiply by.

#### [Tobias Grosser (Oct 20 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152330):
Are you talking about Jack?

#### [Tobias Grosser (Oct 20 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152334):
I mean, I obviously have no idea what the right approach is.

#### [Tobias Grosser (Oct 20 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152336):
Just use this to learn stuff.

#### [Mario Carneiro (Oct 20 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152341):
It might help to try to invent your own gaussian elimination

#### [Mario Carneiro (Oct 20 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152343):
rather than porting from coq

#### [Mario Carneiro (Oct 20 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152350):
Use the coq development and wikipedia to help you with the maths, and just focus on the lean encoding part

#### [Tobias Grosser (Oct 20 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152391):
So you feel my translation from coq is not very ideomatic in lean?

#### [Mario Carneiro (Oct 20 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152394):
that's right

#### [Tobias Grosser (Oct 20 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152397):
It seems to do what I want, so I am reasonably happy with it.

#### [Mario Carneiro (Oct 20 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152401):
in particular, I would work more with fintypes and less with fin n

#### [Tobias Grosser (Oct 20 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152402):
As I don't really know lean, I have zero feeling what would be more ideomatic

#### [Tobias Grosser (Oct 20 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152410):
OK, I can change this. Not sure though if this would change the overall algorithm a lot.

#### [Mario Carneiro (Oct 20 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152415):
I would be curious to hear how Jack is doing things differently

#### [Tobias Grosser (Oct 20 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152416):
It might be interesting to look into the code from @**Jack Crawford**

#### [Tobias Grosser (Oct 20 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152456):
Yes.

#### [Tobias Grosser (Oct 20 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152467):
He promised to share the code, but his now on exam leave.

#### [Tobias Grosser (Oct 20 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152478):
It seems Scott gave already quite some input on @**Jack Crawford** 's code, so I assume it is more ideomatic.

#### [Tobias Grosser (Oct 20 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152479):
@**Scott Morrison|110087** , what is your goal with GE?

#### [Jack Crawford (Oct 20 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152480):
I really need to clean a few things up first and am currently on mobile so don’t have my code with me, but as Scott said, I’m just using inductive types to break row equivalence down into steps

#### [Jack Crawford (Oct 20 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152483):
I’ll share the code as soon as I have it neater and a little more complete

#### [Tobias Grosser (Oct 20 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152523):
Would it make sense to build up a matrix theory similar to http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.652.3183&rep=rep1&type=pdf

#### [Tobias Grosser (Oct 20 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152525):
mathcomp.mxalgebra?

#### [Tobias Grosser (Oct 20 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152526):
Or is this not even useful in the context of lean?

#### [Tobias Grosser (Oct 20 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152530):
@**Jack Crawford** , no need to rush.

#### [Tobias Grosser (Oct 20 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152535):
I would be glad to look over your code to learn from it.

#### [Jack Crawford (Oct 20 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152577):
I have an inductive type that represents a single “step” of a row equivalence, with a constructor for scaling, swapping, and linear addition of matrices, and then I have another inductive type that gives me the transitive closure of this.

#### [Jack Crawford (Oct 20 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152640):
Then I have a few functions that perform individual steps of the GE algorithm (putting the pivot in the right place, scaling the pivot, eliminating down the column). Then I show that the result of each of these steps are row-equivalent (by my previous inductive definition of row-equivalence) with the original matrix, and then I make a new function that just combines these steps of the Gaussian elimination in the obvious way, and show that it is also row-equivalent by carrying through my proofs that each of the individual steps that it is composed of is row-equivalent

#### [Tobias Grosser (Oct 20 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152643):
I see.

#### [Jack Crawford (Oct 20 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152684):
and from my row-equivalence I can get the proof that the invertible matrix which represents all of the steps of the row reduction, times the original matrix, is in fact the row-reduced version of the matrix

#### [Tobias Grosser (Oct 20 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152685):
I see,

#### [Tobias Grosser (Oct 20 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152691):
Do you also compute an extended gaussian elimination similar to what 'Georges Gonthier' does?

#### [Tobias Grosser (Oct 20 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152695):
Meaning, do you e.g. have proofs about the rank of the matrix?

#### [Jack Crawford (Oct 20 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136152907):
Not yet, I haven’t actually gotten to proving much at all yet because I’ve had to re-write substantial parts of my code a few times over now. Hopefully this will be the final iteration! Haven’t really given much of a thought to matrix rank yet

#### [Tobias Grosser (Oct 20 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136153002):
OK. Please ping me when it's time to look at your code.

#### [Tobias Grosser (Oct 20 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20to%20insert%20definition%20of%20a%20function%20in%20a%20proof/near/136153003):
Also, feedback on the Georges paper would be interesting.

