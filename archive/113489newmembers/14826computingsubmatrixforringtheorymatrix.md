---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/14826computingsubmatrixforringtheorymatrix.html
---

## Stream: [new members](index.html)
### Topic: [computing submatrix for ring_theory.matrix](14826computingsubmatrixforringtheorymatrix.html)

---


{% raw %}
#### [ Tobias Grosser (Sep 29 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134897036):
On another lean saturday afternoon, I continued looked forther into formalizing another basic lean maths. This time I want to compute sub-matrixes for ring_theory.matrix.

This is what I came up with:
```lean
def rsubmx {m n_left n_right: nat} :
Π (m n_left n_right),
matrix (fin m) (fin (n_right + n_left)) α → matrix (fin m) (fin (n_right)) α 
| x y_l y_r A :=
  λ i j,
  let (offset : fin (y_r + y_l)) := (fin.add_nat j y_l) in
  A i offset
```

It compiles without flaws, but looks very messy. Two things I feel should still be changed are:
1) It would be nice if the function would not require m, n_right, n_left to be passed explicitly, but would instead automatically derive the relevant offsets.
2) I keep getting type errors due to a fin(x + y) being not equal to fin(y + x) when using it. It would be great if one could automatically convert between the two.

#### [ Tobias Grosser (Sep 29 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134897038):
Feedback very much appreciated.

#### [ Kevin Buzzard (Sep 29 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134897446):
I think that I would have been tempted to move away from just adding an offset and would instead consider any increasing maps `fin m' -> fin m` and `fin n' -> fin n`. Isn't that what people usually look at -- all the m' x n' minors or something?

#### [ Tobias Grosser (Sep 30 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134898201):
I am not sure I understand what interface you have in mind.

#### [ Bryan Gin-ge Chen (Sep 30 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134898247):
For example, suppose I have a 5x5 matrix and want to extract the 3x3 matrix consisting of rows 1,2,4 and columns 1,3,4.

#### [ Tobias Grosser (Sep 30 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134898256):
Right.

#### [ Tobias Grosser (Sep 30 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134898258):
I mean, it makes sense to have a more generic interface that computes a minor.

#### [ Tobias Grosser (Sep 30 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134898297):
Such a functionality could even be the basis for this function, I assume.

#### [ Tobias Grosser (Sep 30 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134898355):
Still, I feel that it would not completely replace this function as the interface for the special case I propose could be simpler, as it could just derive the sizes from the types.

#### [ Tobias Grosser (Sep 30 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134898446):
More from a practical perspective, I am not sure how a general minorification interface should look like. Would I ask for two more parameters fin m -> Prop and fin n -> Prop, which evaluate to true if the specific column should be included?

#### [ Tobias Grosser (Sep 30 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134898452):
Computing the necessary offsets seems a little involved. Not sure how this will effect performance.

#### [ Bryan Gin-ge Chen (Sep 30 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134898699):
I think the interface Kevin suggests is the following: to specify a general $$m' \times n'$$ submatrix of an $$m \times n$$ matrix, it is sufficient to provide two increasing maps, one of type `fin m' → fin m` and one of type `fin n' → fin n`. No need to compute any offsets, so far as I can tell; simply pull out the specified matrix entries using the two maps to grab the row and column indices.

#### [ Kevin Buzzard (Sep 30 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134899303):
And then the function you've already implemented could be a special case of this.

#### [ Tobias Grosser (Sep 30 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134910891):
Right.

#### [ Tobias Grosser (Sep 30 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134910897):
Here what I came up with:

```lean
import ring_theory.matrix

variables {α : Type}
variables {m n m' n': Type} [fintype m] [fintype n] [fintype m'] [fintype n']

def minormx : matrix m n α → (m' → m) → (n' → n) → matrix m' n' α :=
λ A trans_col trans_row i j, A (trans_col i) (trans_row j)

def rsubmx {m n_left n_right: nat} :
  matrix (fin m) (fin (n_right + n_left)) α → matrix (fin m) (fin (n_right)) α 
| A := minormx A (λ i, i) (λ j, fin.add_nat j _)

#### [ Tobias Grosser (Sep 30 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134910905):
(deleted)

#### [ Tobias Grosser (Sep 30 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134910948):
(deleted)

#### [ Tobias Grosser (Sep 30 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911004):
I created a bunch of tests:

```lean
def rsubmx_test_join_fail:
matrix (fin 5) (fin 5) α → matrix (fin 5) (fin 3) α :=
λ A, rsubmx A

def rsubmx_test_split_const_ok (x : nat) :
matrix (fin 5) (fin (3 + 2)) α → matrix (fin 5) (fin 3) α :=
λ A, rsubmx A

def rsubmx_test_split_const_fail (x : nat) :
matrix (fin 5) (fin (2 + 3)) α → matrix (fin 5) (fin 3) α :=
λ A, rsubmx A

def rsubmx_test_split_param_ok (x y : nat) :
matrix (fin 5) (fin (x + y)) α → matrix (fin 5) (fin (x)) α :=
λ A, rsubmx A

def rsubmx_test_split_param_fail (x y : nat) :
matrix (fin 5) (fin (y + x)) α → matrix (fin 5) (fin (x)) α :=
λ A, rsubmx A
```

Only if the fine type is split into a clear  "+" with the correct order of operands in the plus (the LHS operand must appear in the result type), this compiles. Automatic splitting or exploiting commutativity does not work.

Here the associated error messages:

```lean
test.lean:16:5: error

type mismatch at application
  rsubmx A
term
  A
has type
  matrix (fin 5) (fin 5) α
but is expected to have type
  matrix (fin 5) (fin (3 + ?m_1)) α

type mismatch at application
  rsubmx A
term
  A
has type
  matrix (fin 5) (fin (2 + 3)) α
but is expected to have type
  matrix (fin 5) (fin (3 + ?m_1)) α
test.lean:24:5: error

type mismatch at application
  rsubmx A
term
  A
has type
  matrix (fin 5) (fin (y + x)) α
but is expected to have type
  matrix (fin 5) (fin (x + ?m_1)) α

```

#### [ Tobias Grosser (Sep 30 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911323):
@**Mario Carneiro** , any idea how to make my tests independent of the order of fin? This seems to require lean foo I am not yet capable of.

#### [ Mario Carneiro (Sep 30 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911423):
Use Kevin's suggestion

#### [ Mario Carneiro (Sep 30 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911425):
You should avoid algebra inside types like the plague

#### [ Tobias Grosser (Sep 30 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911524):
With
```lean
def minormx : matrix m n α → (m' → m) → (n' → n) → matrix m' n' α :=
λ A trans_col trans_row i j, A (trans_col i) (trans_row j)
```

I tried to implement Kevin's suggestion.

#### [ Tobias Grosser (Sep 30 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911533):
I now try to implement ssreflects
```coq
   [l|r]submx A == the left/right submatrices of a row block matrix A.      
                   Note that the type of A, 'M_(m, n1 + n2) indicates how A 
                   should be decomposed.                       
```
on top of it.

#### [ Tobias Grosser (Sep 30 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911571):
It seems a nice feature that they can split just based on the type sizes.

#### [ Tobias Grosser (Sep 30 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911578):
Are you saying the interface they use in coq is not a good interface for lean?

#### [ Mario Carneiro (Sep 30 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911625):
That will only work when `n1` and `n2` are explicitly given, and they also have to be numerals not variables for it to be useful

#### [ Mario Carneiro (Sep 30 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911629):
Do you have any examples of use of this notation in Coq?

#### [ Mario Carneiro (Sep 30 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911682):
> Note that the type of A, 'M_(m, n1 + n2) indicates how A should be decomposed.

This sounds to me like lean's behavior is consistent with coq's: You have to give an input of a matrix `matrix 5 (3 + 2)` rather than `matrix 5 5` to get the function to figure out `n1` and `n2`

#### [ Tobias Grosser (Sep 30 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911732):
Sure, my guaussien elimination code:

```coq
Fixpoint Gaussian_elimination {m n} : 'M_(m, n) → 'M_m × 'M_n × nat :=
  match m, n with
  | _.+1, _.+1 ⇒ fun A : 'M_(1 + _, 1 + _) ⇒
    if [pick ij | A ij.1 ij.2 != 0] is Some (i, j) then
      let a := A i j in let A1 := xrow i 0 (xcol j 0 A) in
      let u := ursubmx A1 in let v := a^-1 *: dlsubmx A1 in
      let: (L, U, r) := Gaussian_elimination (drsubmx A1 - v ×m u) in
      (xrow i 0 (block_mx 1 0 v L), xcol j 0 (block_mx a%:M u 0 U), r.+1)
    else (1%:M, 1%:M, 0%N)
  | _, _ ⇒ fun _ ⇒ (1%:M, 1%:M, 0%N)
  end.
```

it uses ```dlsubmx``` which again is defined as:

```coq
Definition ulsubmx := lsubmx (usubmx A).
Definition ursubmx := rsubmx (usubmx A).
Definition dlsubmx := lsubmx (dsubmx A).
Definition drsubmx := rsubmx (dsubmx A).
```

which again uses
```coq
Fact lsubmx_key : unit. 
Definition lsubmx (A : 'M[R]_(m, n1 + n2)) :=
  \matrix[lsubmx_key]_(i, j) A i (lshift n2 j).

Fact rsubmx_key : unit. 
Definition rsubmx (A : 'M[R]_(m, n1 + n2)) :=
  \matrix[rsubmx_key]_(i, j) A i (rshift n1 j).

Fact usubmx_key : unit. 
Definition usubmx (A : 'M[R]_(m1 + m2, n)) :=
  \matrix[usubmx_key]_(i, j) A (lshift m2 i) j.

Fact dsubmx_key : unit. 
Definition dsubmx (A : 'M[R]_(m1 + m2, n)) :=
  \matrix[dsubmx_key]_(i, j) A (rshift m1 i) j.
```

```coq
Lemma lshift_subproof m n (i : 'I_m) : i < m + n.

Lemma rshift_subproof m n (i : 'I_n) : m + i < m + n.

Definition lshift m n (i : 'I_m) := Ordinal (lshift_subproof n i).
Definition rshift m n (i : 'I_n) := Ordinal (rshift_subproof m i).
```

#### [ Tobias Grosser (Sep 30 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911822):
 
```quote
> Note that the type of A, 'M_(m, n1 + n2) indicates how A should be decomposed.

This sounds to me like lean's behavior is consistent with coq's: You have to give an input of a matrix `matrix 5 (3 + 2)` rather than `matrix 5 5` to get the function to figure out `n1` and `n2`
```
If that's as good as it gets that's fine. I just had hoped lean would be able to figure out that 5 can be split into 3 + 2. If this not the case, I need to do this manually. Is there a function that does this type splitting for me?

#### [ Mario Carneiro (Sep 30 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911829):
what is the type of `A1`?

#### [ Mario Carneiro (Sep 30 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911831):
or `xrow` and `xcol`

#### [ Mario Carneiro (Sep 30 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911835):
Lean can figure out that `5` is `3 + 2`, but it is ambiguous what to split it into

#### [ Tobias Grosser (Sep 30 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911888):
I see.

#### [ Tobias Grosser (Sep 30 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911942):
In my implementation in lean it is ```A1 : matrix (fin (x + 1)) (fin (y + 1)) α```

#### [ Tobias Grosser (Sep 30 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911944):
So what I have today might already be enough.

#### [ Tobias Grosser (Sep 30 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911946):
I learn that generalizing this further is not a good idea.

#### [ Tobias Grosser (Sep 30 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911948):
Thanks! I leave it at this generality.

#### [ Tobias Grosser (Sep 30 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912144):
Now I am only left with the problem of casting. I need the matrix to be of type  matrix (fin (1 + x)) (fin (1 + y)))

#### [ Tobias Grosser (Sep 30 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912154):
I tried to type-cast using:

```lean
    let (A1': matrix (fin (1+x)) (fin (1+y)) α) := A1 in 
```
but this just gives

```lean
type mismatch at application
  _let_match A1'
term
  A1'
has type
  matrix (fin (1 + x)) (fin (1 + y)) α
but is expected to have type
  matrix (fin (x + 1)) (fin (y + 1)) α
```

#### [ Tobias Grosser (Sep 30 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912155):
You said lean should be able to understand this.

#### [ Tobias Grosser (Sep 30 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912158):
This is no ambiguity

#### [ Tobias Grosser (Sep 30 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912207):
I just need to show that these two are equivalent types.

#### [ Mario Carneiro (Sep 30 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912270):
this is not ambiguous, but since `x` is not a numeral these aren't defeq

#### [ Mario Carneiro (Sep 30 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912321):
How do the `xrow i 0 (xcol j 0 A)` functions work?

#### [ Mario Carneiro (Sep 30 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912324):
are you building a new row on `A` or taking a minor?

#### [ Tobias Grosser (Sep 30 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912386):
They just interchange rows. AFAIU they don;t thange the type.

#### [ Mario Carneiro (Sep 30 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912393):
The fact that in coq `1+x = succ x` is definitional makes this translation more complicated, unless you reverse the `+` arguments in the minors function, or work from the bottom rather than the top of the matrix

#### [ Mario Carneiro (Sep 30 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912434):
In lean `x+1 = succ x` is definitional

#### [ Tobias Grosser (Sep 30 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912435):
My lean implementation is:
```lean
def xrow [decidable_eq m] (row1: m) (row2: m) (A: matrix m n α) : matrix m n α :=
λ x y, if x = row1
         then
           A row2 y
         else
           if x = row2
             then 
               A row1 y
             else
               A x y
```

#### [ Mario Carneiro (Sep 30 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912437):
right, I see, that shouldn't be a problem

#### [ Mario Carneiro (Sep 30 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912448):
you are still using the code you posted above for `rsubmx`?

#### [ Mario Carneiro (Sep 30 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912449):
with `n_right + n_left` in the type I mean

#### [ Tobias Grosser (Sep 30 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912451):
Yes.

#### [ Tobias Grosser (Sep 30 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912494):
I could move the zero columns/rows to position x+1 / y +1, then the types would work out.

#### [ Tobias Grosser (Sep 30 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912497):
But then the result matrices are layed out in a non-standard way.

#### [ Mario Carneiro (Sep 30 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912499):
so since `A` has type `(n+1) (n+1)` you can naturally strip off the left/top end

#### [ Tobias Grosser (Sep 30 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912500):
Right.

#### [ Tobias Grosser (Sep 30 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912509):
That's easy. Just that most textbook implementations of gaussian elimination build upper triangular matrices.

#### [ Tobias Grosser (Sep 30 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912510):
So the zeros should be at the lower left corner.

#### [ Mario Carneiro (Sep 30 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912551):
I think you can still build upper triangular if you also transpose the rows and columns

#### [ Tobias Grosser (Sep 30 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912554):
Sure, I could probably hack my way though this.

#### [ Tobias Grosser (Sep 30 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912559):
Just don't feel this is nice.

#### [ Mario Carneiro (Sep 30 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912560):
But I think that having reversed arguments to the minors function is also fine

#### [ Tobias Grosser (Sep 30 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912562):
Why again does this work in coq?

#### [ Mario Carneiro (Sep 30 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912568):
because they defined addition by recursion on the first argument rather than the second

#### [ Mario Carneiro (Sep 30 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912573):
Personally I prefer lean's definition (i.e. `x + succ y = succ (x + y)`)

#### [ Tobias Grosser (Sep 30 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912575):
They do?

#### [ Tobias Grosser (Sep 30 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912607):
I feel they also have this cast in their code.

#### [ Tobias Grosser (Sep 30 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912616):
```coq
 | _.+1, _.+1 ⇒ fun A : 'M_(1 + _, 1 + _) ⇒
```

#### [ Mario Carneiro (Sep 30 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912619):
That's why in the induction you notice the type is `1+_` instead of `_ +1`

#### [ Mario Carneiro (Sep 30 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912630):
The `.+` is suspicious

#### [ Mario Carneiro (Sep 30 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912633):
do you know what it means?

#### [ Tobias Grosser (Sep 30 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912635):
```coq
Notation "n .+1" := (succn n) (at level 2, left associativity,
  format "n .+1") : nat_scope.
```

#### [ Mario Carneiro (Sep 30 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912674):
heh

#### [ Tobias Grosser (Sep 30 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912678):
So they define notation to allow RHS addition of +1?

#### [ Mario Carneiro (Sep 30 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912679):
so `1+n = n .+1`

#### [ Mario Carneiro (Sep 30 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912682):
looks like it

#### [ Tobias Grosser (Sep 30 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912683):
This stuff is all crazy!

#### [ Tobias Grosser (Sep 30 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912686):
Now based on the way nat is defined I cannot write my algorithm the way I want it.

#### [ Tobias Grosser (Sep 30 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912692):
:(

#### [ Mario Carneiro (Sep 30 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912693):
You can also write `fin.add_nat` with an appropriate type

#### [ Mario Carneiro (Sep 30 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912743):
You can also `cast` to get `A1'` the way you were attempting, but this will cause more problems later on

#### [ Tobias Grosser (Sep 30 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912799):
OK, I will try to write add_nat after breakfast.

There is already
```lean
def add_nat {n} (i : fin n) (k) : fin (n + k) :=                                 
⟨i.1 + k, nat.add_lt_add_right i.2 _⟩  
```

#### [ Tobias Grosser (Sep 30 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912800):
Seems trivial to write (assuming one knows what to write)

#### [ Tobias Grosser (Sep 30 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912806):
Now, I am not sure what I actually want here.

#### [ Tobias Grosser (Sep 30 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912807):
In some way I just want to cast from n + 1 to 1 + n.

#### [ Tobias Grosser (Sep 30 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912809):
Or pattern match based on 1 + n.

#### [ Tobias Grosser (Sep 30 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912811):
Would add_nat help me with the pattern matching?

#### [ Mario Carneiro (Sep 30 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912854):
just swap the arguments, like this
```
def nat_add {n} (k) (i : fin n) : fin (k + n) :=
⟨k + i.1, nat.add_lt_add_left i.2 _⟩
```

#### [ Mario Carneiro (Sep 30 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912857):
then use it in your minors function

#### [ Tobias Grosser (Sep 30 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912972):
Are you suggeting to change the signature of my functions.

```lean
def ursubmx {m_bottom m_top n_left n_right: nat} : Π (m_bottom m_top n_left n_right),
  matrix (fin (m_bottom + m_top)) (fin (n_left + n_right)) α → matrix (fin m_top) (fin (n_right)) α 
:= sorry

def ursubmx2 {m_bottom m_top n_left n_right: nat} : Π (m_bottom m_top n_left n_right),
  matrix (fin (m_top + m_bottom)) (fin (n_right + n_left)) α → matrix (fin m_top) (fin (n_right)) α 
:= sorry 
```

#### [ Mario Carneiro (Sep 30 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134913014):
yes... although I think this will make a cast required

#### [ Tobias Grosser (Sep 30 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134913015):
I feel I have enough ideas to make things work. I can then later try to make the code nice.

#### [ Tobias Grosser (Sep 30 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134913018):
This just screems ugly all over the place.

#### [ Tobias Grosser (Sep 30 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134913022):
Need to get used to this more to see a beautiful solution.

#### [ Tobias Grosser (Sep 30 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134913024):
Need to have breakfast now. Thanks a lot for the helpful discussion. I learned a lot!

#### [ Mario Carneiro (Sep 30 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134913071):
Here's a trick: You can use Kevin's minors function as a cast

#### [ Mario Carneiro (Sep 30 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134913073):
the identity function `fin (m+n) -> fin (n+m)` is monotonic :)

#### [ Kevin Buzzard (Sep 30 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134914237):
Is there an argument for not even using `fin n` at all and having a general class indexed over a pair of finite types?

Here's a result I'd like to see in Lean one day: if f(X) is the char poly of the n x n matrix M then the coefficient of X^(n-i) in f(X) is the sum of the (appropriately signed?) determinants of the i x i principal minors.

#### [ Mario Carneiro (Sep 30 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134914299):
We already have that; Tobias is explicitly avoiding that because he wants to do induction on fin n

#### [ Kevin Buzzard (Sep 30 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134914352):
Oh -- I'm behind the times :-)

#### [ Mario Carneiro (Sep 30 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134914394):
If this is to be computationally efficient, it should probably use list representation though (a.k.a `fast_matrix`), and it might be possible to just ignore the dependent types and work with `list (list A)`

#### [ Tobias Grosser (Sep 30 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134915836):
I see.

#### [ Tobias Grosser (Sep 30 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134915876):
I would certainly like this to be computationally efficient, but will take this a step at a time. I feel I am close to sth that could work. I will finish this up and polish it.

#### [ Tobias Grosser (Sep 30 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134915879):
Then we have a first baseline implementation. I am then happy to take feedback on how to improve interface / performance / ...

#### [ Mario Carneiro (Sep 30 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134916119):
I think that's a good idea

#### [ Tobias Grosser (Sep 30 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134921308):
OK, I think I got a first implementation: https://gist.github.com/tobig/376e9a394c674474b8c1f6ecf9555478
It compiles and gives expected results. Still a couple of sorry, but seems to work.

#### [ Tobias Grosser (Sep 30 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134921349):
Need to clean up everything at some point.

#### [ Tobias Grosser (Sep 30 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134921353):
But no today any more.

#### [ Tobias Grosser (Sep 30 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134921355):
Also I learned it is indeed _very_ slow.

#### [ Tobias Grosser (Sep 30 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134921356):
I need to wait 10s of seconds for results on a 3x3 matrix.

#### [ Tobias Grosser (Sep 30 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134921362):
Oh dear, seems there is optimization potential.

#### [ Kevin Buzzard (Sep 30 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134922425):
I think for your test matrix I would have been tempted to send x and y to `C[3*x+y]` with C a vector of the nine entries (`def C := [3,3,3,3,2,3,2,1,1]`)...hmm...one might then have to prove 3*x+y<=8...

#### [ Andrew Ashworth (Sep 30 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134924823):
hmm, are you aiming for speed? I believe `vector` has special support in the VM, so you might try defining matrix using that instead of an arbitrary `fintype`

#### [ Andrew Ashworth (Sep 30 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134924884):
iirc, and you would be more familiar than me on this topic, but doesn't SSReflect also define matrix as a vector of vectors?

#### [ Tobias Grosser (Sep 30 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134926152):
I am not aiming for speed atm. I just want to get things working / defined and improve my lean-knowledge.

#### [ Tobias Grosser (Sep 30 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134926161):
Eventually, I would like this to be fast and maybe even support exporting code to C++.

#### [ Tobias Grosser (Sep 30 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134926164):
However, this is a medium term only.

#### [ Tobias Grosser (Oct 05 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/135234645):
My first pull request: https://github.com/leanprover/mathlib/pull/387

Still very small, but gets things rolling.

#### [ Tobias Grosser (Oct 05 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/135236714):
I got an amazing review from @**Simon Hudon** and @**Sean Leather**. Thanks a lot!

#### [ Simon Hudon (Oct 05 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/135236765):
The PR has my stamp of approval and, I think, that of @**Sean Leather**, now we just need @**Mario Carneiro** or @**Johannes Hölzl** to merge it.

#### [ Sean Leather (Oct 05 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/135236826):
Agreed.

#### [ Mario Carneiro (Oct 05 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/135236830):
yeah okay

#### [ Simon Hudon (Oct 05 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/135236836):
This must be some sort of record :D

#### [ Tobias Grosser (Oct 05 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/135236911):
Impressive!

#### [ Tobias Grosser (Oct 05 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/135242622):
I pushed anther pull request for fin in (https://github.com/leanprover/mathlib/pull/388) as well as the submatrix definitions this thread was originally about in: https://github.com/leanprover/mathlib/pull/389. The last PR uses @**Kevin Buzzard**'s idea of using a general function minormx to implement this functionality.

#### [ Tobias Grosser (Oct 05 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/135242713):
Especially the last one is more a RFC, as I am not sure if limiting these functionality to (fin n) makes sense.

#### [ Tobias Grosser (Oct 05 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/135242722):
My lean time is over for today. Will look at potential feedback later tonight. Thanks everyone again!


{% endraw %}
