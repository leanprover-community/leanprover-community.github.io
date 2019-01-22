---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/91335Commutativityofmultiplicationininductivetype.html
---

## [new members](index.html)
### [Commutativity of multiplication in inductive type](91335Commutativityofmultiplicationininductivetype.html)

#### [Carlesso Diego (Jan 05 2019 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Commutativity%20of%20multiplication%20in%20inductive%20type/near/154475123):
Hi! As it is suggested in exercise n1 chapter 7 of "theorem Proving in Lean" I'm trying to define some operations(such as multiplication, predecessor etc.) with the inductive type and then prove some theorem about them as they did with addition. I'm struggling at the moment with trying to prove commutativity of multiplication, in the following code my problems start at the proper comment "HERE".

```lean
namespace hidden


inductive nat : Type
| zero : nat
| succ : nat → nat
namespace nat

instance : has_zero nat := has_zero.mk zero
instance : has_one nat := has_one.mk (succ zero)

-- addition
def add (m n : nat) : nat :=
nat.rec_on n m (λ (n add_m_n: nat ), succ add_m_n)

instance : has_add nat := has_add.mk add

-- properties add
theorem add_zero (m : nat) : m + 0  = m := rfl

theorem add_succ (m n : nat) : m + succ n = succ (m + n) := rfl

theorem zero_add (n : nat) : 0 + n = n :=
nat.rec_on n
  (show 0 + zero = 0, from rfl)
  (assume n,
    assume ih : 0 + n = n,
    show 0 + succ n = succ n, from
      calc
        0 + succ n = succ (0 + n) : rfl
          ... = succ n : by rw ih)

theorem add_assoc (m n k : nat) : m + n + k = m + (n + k) :=
nat.rec_on k
  (show m + n + 0 = m + (n + 0), from rfl)
  (assume k,
    assume ih : m + n + k = m + (n + k),
    show m + n + succ k = m + (n + succ k), from
      calc
        m + n + succ k = succ (m + n + k) : rfl
          ... = succ (m + (n + k)) : by rw ih
          ... = m + succ (n + k) : rfl
          ... = m + (n + succ k) : rfl)

theorem succ_add (m n : nat) : succ m + n = succ (m + n) :=
nat.rec_on n
  (show succ m + 0 = succ (m + 0), from rfl)
  (assume n,
    assume ih : succ m + n = succ (m + n),
    show succ m + succ n = succ (m + succ n), from
      calc
        succ m + succ n = succ (succ m + n) : rfl
          ... = succ (succ (m + n)) : by rw ih
          ... = succ (m + succ n) : rfl)

theorem add_comm (m n : nat) : m + n = n + m :=
nat.rec_on n
  (show m + 0 = 0 + m, by rw [nat.zero_add, nat.add_zero])
  (assume n,
    assume ih : m + n = n + m,
    calc
        m + succ n = succ (m + n) : rfl
        ... = succ (n + m) : by rw ih
        ... = succ n + m :  by rw succ_add )

-- multiplication
def mult (m n: nat) : nat := 
nat.rec_on n zero (λ n mult_m_n, add mult_m_n m )

instance : has_mul nat := has_mul.mk mult 

-- properties mult

theorem mul_zero (m: nat) : mult m 0 = 0 := rfl  -- m * 0 = 0

theorem zero_mul (m : nat) : mult 0 m = 0 :=     -- 0 * m = 0
nat.rec_on m 
    (show  0 * zero = 0, from rfl)
    (assume m, 
     assume ih: 0 * m = 0,
     show  0 * (succ m) = 0, from 
        calc 
             0 * (succ m) =    0 * m + 0: rfl  
            ... = 0 * 0 : ih
            ... = 0: rfl
    )

theorem succ_mul (n m : nat) : ( n + 1 ) * m = ( n * m ) + m :=  -- ( n + 1 ) * m = ( n * m ) + m
    nat.rec_on m 
        (show (n + 1) * 0 = (n * 0) + 0, from rfl)
        (assume m,
         assume ih: (n + 1) * m = ( n * m ) + m,
         show (n + 1) * (m + 1) = ( n *(m + 1) ) + (m + 1), from 
         calc 
            (n + 1) * (m + 1) = ((n + 1) * m) + (n + 1) : rfl
            ... = (n * m) + m + (n + 1) : by rw ih
            ... = (n * m) + (m + (n + 1)) : by rw add_assoc
            ... = (n * m) + ((n + 1) + m) : by rw add_comm -- HERE
            ... = n * m + (n + (m + 1)) : nat.succ_add_eq_succ_add -- ((n + 1) + m) = ( n + (m + 1))
            ... = n * m + n + (m + 1) : add_assoc
            ... = n * (m + 1) + (m + 1): rfl

        )


theorem mul_comm (m n : nat) :  m * n = n * m :=        -- m * n = n * m
nat.rec_on n
    (show  m * 0 =  0 * m , from  eq.symm (zero_mul m) )
    (assume n ,
     assume ih : m * n = n * m,
     show m * n + 1 = ( n + 1) * m, from
        calc m * (n + 1) =  m * n + m : by rw mul_add, 
            ... =  (n * m) + m : by rw ih, 
            ... =  ( n + 1) * m : by rw succ_mul 

            )

end nat 
end hidden
```
I think that the proof is correct, or at least I can't see the error, maybe I'm using  ```rw ``` in```calc``` in a wrong way.
The errors I got are in ```succ_mul``` and in ```mul_comm```.
(the ```instance``` command I use is something I shouldn't know from the tutorial but as they use it once I adapt it to my needs, maybe I did it in a wrong way, but I don't think that that is the main problem. From what I understand is just a way, for example, to let me use ```m * n```instead of ```mult m n```  ).

#### [Chris Hughes (Jan 05 2019 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Commutativity%20of%20multiplication%20in%20inductive%20type/near/154475186):
`rw add_comm m` works at `HERE`. There are two places where it's possible to `rw add_comm` so you have to give the correct one.

#### [Chris Hughes (Jan 05 2019 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Commutativity%20of%20multiplication%20in%20inductive%20type/near/154475231):
On the next line you use a lemma about `nat` in the core library, which doesn't apply to the `nat` that you defined.

#### [Carlesso Diego (Jan 06 2019 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Commutativity%20of%20multiplication%20in%20inductive%20type/near/154510669):
```quote
`rw add_comm m` works at `HERE`. There are two places where it's possible to `rw add_comm` so you have to give the correct one.
```
 thank you, you are right! I wasn't considering it. Solved, even the next line I succeeded with an ```add_assoc``` and another  ```add_comm m ```  in order to avoid the problem with the lemma about ```nat``` in the core library  , it was easier than I thought .
 Now I have solved everything simply adding :
```lean
theorem mul_succ (n m : nat) : m * ( n + 1 ) = ( m * n ) + m := 
    nat.rec_on m 
        (show 0 * (n + 1) = (0 * n) + 0, from rfl)
        (assume m,
         assume ih: m * (n + 1) = ( m * n ) + m,
         show (m + 1) * ( n+ 1) = ( (m + 1) * n ) + (m + 1), from 
         calc 
            (m + 1) * (n + 1) = ((m + 1) * n) + (m + 1) : rfl
            ... = (m * n) + n + (m + 1) : by rw succ_mul
            ... = ( (m + 1) * n) + (m + 1) : by rw ←succ_mul  
```
and with ```mul_comm``` becoming:
```lean
theorem mul_comm (m n : nat) :  m * n = n * m :=        -- m * n = n * m
nat.rec_on n
    (show  m * 0 =  0 * m , from  eq.symm (zero_mul m) )
    (assume n,
     assume ih : m * n = n * m,
     show m * (n + 1) = ( n + 1 ) * m, from
        calc m * (n + 1) =  (m * n) + m : by rw mul_succ   
            ... =  (n * m) + m : by rw ih 
            ... =  ( n + 1) * m : by rw succ_mul 

            )
```
Thanks again!

