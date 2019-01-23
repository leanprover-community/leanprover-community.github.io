---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/88248Defineafiniteset.html
---

## Stream: [new members](index.html)
### Topic: [Define a finite set](88248Defineafiniteset.html)

---

#### [Abhimanyu Pallavi Sudhir (Oct 15 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135797911):
How do I define a finite set only giving information of its cardinality? I'd like to define something like this:

```lean
definition S' : Type u
| card : fintype.card S' = 2
```

(once again nonsense, but a sketch of what I want to define)

#### [Bryan Gin-ge Chen (Oct 15 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135797918):
`finset.range` ?

#### [Bryan Gin-ge Chen (Oct 15 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135797927):
oh you want a fintype, then try `fin`

#### [Kevin Buzzard (Oct 15 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135799298):
Do you mean a finite type?

#### [Abhimanyu Pallavi Sudhir (Oct 15 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135815346):
You mean `def S' : Type := fin 2`? That does seem to work.

#### [Abhimanyu Pallavi Sudhir (Oct 15 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135815375):
```quote
Do you mean a finite type?
```
Oh, right, set only refers to subsets. I forgot.

#### [Kenny Lau (Oct 15 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135815434):
I don’t think we understood this question

#### [Kevin Buzzard (Oct 15 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135831206):
@**Abhimanyu Pallavi Sudhir** `fin 2` is a type. There are exactly two distinct terms of that type. The terms are rather a mouthful to describe: 

```lean
example : fin 2 := ⟨(0 : ℕ), dec_trivial⟩
example : fin 2 := ⟨(1 : ℕ), dec_trivial⟩
```

There's another type called `bool` which also has exactly two terms. Type `#check bool` and right-click on `bool`and select "go to definition" to see it. The definition is completely different to `fin`. The two terms of type `bool` are `tt` and `ff`. These types `bool` and `fin 2` are not *equal*, but there is a map from `bool` to `fin 2` which is a bijection, and which you can define using the equation compiler (pattern matching).

Exercise 1: `def f : bool → fin 2`. Define a function from `bool` to `fin 2` which you can prove (in maths, not in Lean) is a bijection.

Exercise 2: fill in the sorry.
```lean
import data.equiv.basic

def X : equiv bool $ fin 2 := sorry
```

Exercise 3: find the library function which turns `X` into a proof that `f` is a bijection. Hint: which namespace do you think that function would be in?

```lean
open function

example : bijective f := <FILL IN FUNCTION NAME> X
```

#### [Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135858585):
```quote
@**Abhimanyu Pallavi Sudhir** `fin 2` is a type. There are exactly two distinct terms of that type. The terms are rather a mouthful to describe: 

```lean
example : fin 2 := ⟨(0 : ℕ), dec_trivial⟩
example : fin 2 := ⟨(1 : ℕ), dec_trivial⟩
```

There's another type called `bool` which also has exactly two terms. Type `#check bool` and right-click on `bool`and select "go to definition" to see it. The definition is completely different to `fin`. The two terms of type `bool` are `tt` and `ff`. These types `bool` and `fin 2` are not *equal*, but there is a map from `bool` to `fin 2` which is a bijection, and which you can define using the equation compiler (pattern matching).

Exercise 1: `def f : bool → fin 2`. Define a function from `bool` to `fin 2` which you can prove (in maths, not in Lean) is a bijection.

Exercise 2: fill in the sorry.
```lean
import data.equiv.basic

def X : equiv bool $ fin 2 := sorry
```

Exercise 3: find the library function which turns `X` into a proof that `f` is a bijection. Hint: which namespace do you think that function would be in?

```lean
open function

example : bijective f := <FILL IN FUNCTION NAME> X
```
```
One more question: is there any way to use statements like "x is either the first element of fin 2 or the second element" directly without bijecting to bool?

#### [Kenny Lau (Oct 15 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135858626):
by "use" do you mean "proof"?

#### [Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135858645):
```quote
by "use" do you mean "proof"?
```
Either a proof or an existing lemma.

#### [Kenny Lau (Oct 15 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135858653):
dec_trivial

#### [Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135858776):
```quote
dec_trivial
```
Oh ok -- how would I actually denote "the first element of fin 2" and "the second element of fin 2" in such a statement? Just putting down the explicit form (like `⟨(0 : ℕ), dec_trivial⟩`) gives errors.

#### [Kenny Lau (Oct 15 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135858791):
0 and 1

#### [Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135858861):
```quote
0 and 1
```
Wait, don't I need to do x.val, y.val for that? or do just x and y also take the values 0 and 1? (where `x y : fin 2`). I was under the impression that `.val` indexes the elements as 0 and 1 but the elements themselves are left abstract.

#### [Kenny Lau (Oct 15 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135858962):
```lean
example : ∀ x : fin 2, x = 0 ∨ x = 1 := dec_trivial
```

#### [Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135859021):
Oh ok -- what's the point of `x.val`, then?

#### [Kenny Lau (Oct 15 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135859126):
that 0 is of type `fin 2`

#### [Chris Hughes (Oct 15 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135859183):
for any n, `fin (succ n)` has `0` defined on it in the obvious way, and any other numeral `x` is just `\< x % succ n, proof\>`. `val` is a function `fin n -> nat`, so it's useful whenever you want to turn something of type `fin n` into something of type `nat`.

#### [Kenny Lau (Oct 15 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135859184):
you can also write:
```lean
example : ∀ x : fin 2, x.val = 0 ∨ x.val = 1 := dec_trivial
```

#### [Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135859198):
```quote
for any n, `fin (succ n)` has `0` defined on it in the obvious way, and any other numeral `x` is just `\< x % succ n, proof\>`. `val` is a function `fin n -> nat`, so it's useful whenever you want to turn something of type `fin n` into something of type `nat`.
```
So it's like a coercion?

#### [Chris Hughes (Oct 15 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135859207):
Yes.

#### [Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135859412):
Thanks. I was proving that if there are three elements in fin 2, two of them must be equal -- I was trying some insanely long (relative to the triviality of the statement) proof by contradiction, ordering the elements and showing that the largest of the three will be above fin.last. Now it's easy.

#### [Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135859602):
By the way, does dec_trivial behave differently in term mode and tactic mode? The statement `have H01 : ∀ s : fin 2, s = 0 ∨ s = 1 := dec_trivial` works, but `have H01 : ∀ s : fin 2, s = 0 ∨ s = 1, exact dec_trivial,` doesn't.

#### [Kenny Lau (Oct 15 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135859712):
```lean
example : true :=
have H01 : ∀ s : fin 2, s = 0 ∨ s = 1, from dec_trivial,
trivial

example : true :=
begin
  have H01 : ∀ s : fin 2, s = 0 ∨ s = 1, exact dec_trivial,
  trivial
end
```

#### [Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135859931):
Weird, that doesn't work for my theorem. I'll post my code, one second.

#### [Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135860017):
Or maybe it does.

#### [Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135860103):
Ok yeah it does.

#### [Chris Hughes (Oct 15 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135860131):
If you `intro s` it won't work.

#### [Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135860946):
I found my problem -- I have `local attribute [instance] classical.prop_decidable` in my code, which seems to interfere with `dec_trivial`.

#### [Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861021):
How do I define the scope of a local attribute so it applies only to the theorem it is intended for?

#### [Kevin Buzzard (Oct 15 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861033):
```quote
I found my problem -- I have `local attribute [instance] classical.prop_decidable` in my code, which seems to interfere with `dec_trivial`.
```
Remember when I suggested that `local attribute [instance, priority 0] classical.prop_decidable` was better? It's for this sort of reason.

#### [Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861043):
You did? Whoops, I missed it.

#### [Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861114):
Yep, that works. Thanks.

#### [Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861127):
But in a general scenario, is `section` the only way to define the scope of local things?

#### [Kevin Buzzard (Oct 15 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861487):
`example (a b c : bool) : a = b ∨ b = c ∨ c = a := by cases a;cases b;cases c;simp `

#### [Kevin Buzzard (Oct 15 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861551):
This trick wouldn't work with `fin 2` though. Although maybe @**Scott Morrison|110087**  was recently talking about a tactic which enabled you to do cases on `fin n` somehow...

#### [Kevin Buzzard (Oct 15 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861572):
To make the trick work with `fin 2` you would have to define your own recursor.

#### [Kenny Lau (Oct 15 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861604):
```lean
example (a b c : bool) : a = b ∨ b = c ∨ c = a :=
(dec_trivial : ∀ a b c, a = b ∨ b = c ∨ c = a) a b c
```

#### [Kevin Buzzard (Oct 16 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861698):
How do you do it for `fin 2`?

#### [Kevin Buzzard (Oct 16 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861765):
I am surprised your code works -- I would have guessed that `dec_trivial` would have complained that it did not know the type of anything before you fed `a b c` to it

#### [Kenny Lau (Oct 16 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861771):
```lean
example (a b c : bool) : a = b ∨ b = c ∨ c = a :=
match a, b, c with
| ff, ff, _ := or.inl rfl
| tt, tt, _ := or.inl rfl
| ff, _, ff := or.inr (or.inr rfl)
| tt, _, tt := or.inr (or.inr rfl)
| _, ff, ff := or.inr (or.inl rfl)
| _, tt, tt := or.inr (or.inl rfl)
end
```

#### [Kenny Lau (Oct 16 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861778):
```quote
How do you do it for `fin 2`?
```
```lean
example (a b c : fin 2) : a = b ∨ b = c ∨ c = a :=
(dec_trivial : ∀ a b c, a = b ∨ b = c ∨ c = a) a b c
```

#### [Mario Carneiro (Oct 16 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861986):
> I am surprised your code works -- I would have guessed that dec_trivial would have complained that it did not know the type of anything before you fed a b c to it

That's what the type ascription is for

#### [Scott Morrison (Oct 16 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135862313):
The tactic Kevin mentioned above is in the PR #352.

#### [Kevin Buzzard (Oct 16 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135862416):
```quote
> I am surprised your code works -- I would have guessed that dec_trivial would have complained that it did not know the type of anything before you fed a b c to it

That's what the type ascription is for
```
Lean can't work out the types of `a b c` when it has to check that `dec_trivial` is a term of that type, in my model of how it works. It must decide to wait a bit longer and hope it gets lucky.

#### [Kenny Lau (Oct 16 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135862435):
```quote
The tactic Kevin mentioned above is in the PR #352.
```
yeah but it ain't merged

#### [Kevin Buzzard (Oct 16 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135862505):
Interestingly, this fails:
```lean
example : ∀ a b c : bool, a = b ∨ b = c ∨ c = a
| ff, ff, _ := or.inl rfl
| tt, tt, _ := or.inl rfl
| ff, _, ff := or.inr (or.inr rfl)
| tt, _, tt := or.inr (or.inr rfl)
| _, ff, ff := or.inr (or.inl rfl)
| _, tt, tt := or.inr (or.inl rfl)
```

#### [Kevin Buzzard (Oct 16 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135862521):
aah it's the commas I guess

#### [Kevin Buzzard (Oct 16 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135862583):
```lean
example : ∀ a b c : bool, a = b ∨ b = c ∨ c = a
| ff ff _ := or.inl rfl
| tt tt _ := or.inl rfl
| ff _ ff := or.inr (or.inr rfl)
| tt _ tt := or.inr (or.inr rfl)
| _ ff ff := or.inr (or.inl rfl)
| _ tt tt := or.inr (or.inl rfl)
```

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135911890):
```quote
@**Abhimanyu Pallavi Sudhir** `fin 2` is a type. There are exactly two distinct terms of that type. The terms are rather a mouthful to describe: 

```lean
example : fin 2 := ⟨(0 : ℕ), dec_trivial⟩
example : fin 2 := ⟨(1 : ℕ), dec_trivial⟩
```

There's another type called `bool` which also has exactly two terms. Type `#check bool` and right-click on `bool`and select "go to definition" to see it. The definition is completely different to `fin`. The two terms of type `bool` are `tt` and `ff`. These types `bool` and `fin 2` are not *equal*, but there is a map from `bool` to `fin 2` which is a bijection, and which you can define using the equation compiler (pattern matching).

Exercise 1: `def f : bool → fin 2`. Define a function from `bool` to `fin 2` which you can prove (in maths, not in Lean) is a bijection.

Exercise 2: fill in the sorry.
```lean
import data.equiv.basic

def X : equiv bool $ fin 2 := sorry
```

Exercise 3: find the library function which turns `X` into a proof that `f` is a bijection. Hint: which namespace do you think that function would be in?

```lean
open function

example : bijective f := <FILL IN FUNCTION NAME> X
```
```
Exercise 1 is easy, it's just 
```lean
def f : bool → fin 2 := begin intro x, cases x, exact 0, exact 1, end
```

But I have no clue as to how to even start exercise 2. Is there a library command that helps you prove the isomorphism?

#### [Kevin Buzzard (Oct 16 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912162):
Do you know how to build terms whose type is a structure using `{` `}`?

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912238):
No, I'm not even sure what a structure is.

#### [Kevin Buzzard (Oct 16 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912269):
A structure is just an inductive type which only has one constructor.

#### [Kevin Buzzard (Oct 16 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912280):
So non-examples are things like `nat` and `bool`.

#### [Kevin Buzzard (Oct 16 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912327):
But an example would be something like `and P Q`.

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912357):
Wait, can't `and P Q` be considered a pi type?

#### [Kenny Lau (Oct 16 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912372):
it's a sigma type

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912377):
Since it's a function of two propositions?

#### [Kenny Lau (Oct 16 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912382):
`and` is a pi type

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912396):
Ok, sure, then how is it an inductive type? ("A structure is just an inductive type...")

#### [Kevin Buzzard (Oct 16 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912411):
There's only one way you can build a term of type `and P Q` -- you have to supply a proof of `P` and a proof of `Q`. So this gives us the possibility of having a second piece of notation for defining terms of type `and P Q` where we say we're making something of type `and P Q` and then just supply the proofs of `P` and `Q`

#### [Kevin Buzzard (Oct 16 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912452):
I said `and P Q` is an inductive type, not `and`

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912474):
Oh ok sure, that makes sense.

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912484):
But I'm still not sure what that has to do with inductive types.

#### [Kevin Buzzard (Oct 16 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912493):
`example (P Q : Prop) : and P Q := {}`

#### [Kevin Buzzard (Oct 16 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912521):
If you type that, you get a red underline under the squiggly bracket -- this can't work currently, because we didn't supply proofs of P and Q. But the `{}` notation is clue to a new way of defining a term of type `and P Q`

#### [Kevin Buzzard (Oct 16 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912580):
And the error is interesting -- Lean complains that some fields are missing.

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912589):
I tried supplying the proofs, still doesn't work.

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912602):
`example (P Q : Prop) (HP : P) (HQ : Q) : and P Q := {HP HQ}`

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912617):
function expected at
  HP
term has type
  P

#### [Kevin Buzzard (Oct 16 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912634):
You have to know how to supply them.

#### [Chris Hughes (Oct 16 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912641):
`example (P Q : Prop) (HP : P) (HQ : Q) : and P Q := { left := HP, right := HQ}` is the syntax I think.

#### [Kevin Buzzard (Oct 16 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912649):
right

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912709):
Oh ok, so it's just standard left and right in term mode.

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912726):
(But I don't know how to do exercise 2 in tactic mode either.)

#### [Reid Barton (Oct 16 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912735):
It doesn't have anything to do with the `left` and `right` tactics if that's what you mean

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912753):
Oh right, that's for `or` goals.

#### [Reid Barton (Oct 16 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912765):
It's just that the fields of the structure `and P Q` happen to also be named `left` and `right` (I guess? I never knew this)

#### [Kevin Buzzard (Oct 16 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912768):
So you can start work on Q2 by doing this:

```lean
def X : equiv bool $ fin 2 := {
  to_fun := f,
  inv_fun := sorry,
  left_inv := begin sorry end,
  right_inv := begin sorry end
}
```

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912786):
Ah, I see.

#### [Kevin Buzzard (Oct 16 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912787):
I figured out the fields by writing `... := {}` and then looking at the errors.

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912841):
I knew the fields from the definition, but I didn't know how to supply them.

#### [Kevin Buzzard (Oct 16 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912862):
If you replace `inv_fun := sorry` with `inv_fun := _` and look at the error, you'll see that `inv_fun` is supposed to be the inverse map from `fin 2` back to `bool`. So you could define that outside, like you did with `f`

#### [Kevin Buzzard (Oct 16 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912885):
The two remaining fields are the proofs that the compositions in both directions are the identity. Of course both proofs are "just unravel everything" but I think it's quite good fun trying to work out how to do this.

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135913696):
Ok, I'm defining `f_inv`, and I've gotten up to having `Hx01 : x = 0 ∨ x = 1`:

```lean
def f_inv : fin 2 → bool :=
    begin
        intro x,
        have H01 : ∀ s : fin 2, s = 0 ∨ s = 1, exact dec_trivial,
        have Hx01 : x = 0 ∨ x = 1, exact H01 x,
        sorry,
    end
```

But for some reason I can't do `cases Hx01`. I get `induction tactic failed, recursor 'or.dcases_on' can only eliminate into Prop` What's going on?

#### [Patrick Massot (Oct 16 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135913805):
```quote
I figured out the fields by writing `... := {}` and then looking at the errors.
```
This is so September 2018...

#### [Patrick Massot (Oct 16 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135913874):
Nowadays we type `{!}` and click on the light bulb (or Ctrl-.) and choose the relevant option from the menu (I don't have Lean to check right now)

#### [Kevin Buzzard (Oct 16 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135915076):
I need to move with the times.

#### [Kevin Buzzard (Oct 16 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135915189):
Abhi -- it's not a good idea to use tactics to define data. You can use tactics for the proof, but for the data you are better off using something like the equation compiler

#### [Kevin Buzzard (Oct 16 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135915333):
But to answer your question about what's going on, the `cases` command runs the recursor for the type, and if you look at the definition of `or.rec` you'll see that it's only set up to spit out proofs, not data

#### [Kevin Buzzard (Oct 16 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135915359):
I think I once knew a good reason for this

#### [Chris Hughes (Oct 16 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135915489):
The iota reduction rule for `or`  would cause contradictions when both sides of the `or` were true if `or` could produce data.

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135916915):
@**Chris Hughes**  Can you give an example?

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917107):
```quote
Abhi -- it's not a good idea to use tactics to define data. You can use tactics for the proof, but for the data you are better off using something like the equation compiler
```
I'm not sure how to. I mean, I tried to use the equation compiler to produce a definition for `f`, but all I could do is:

```lean
def f (b : bool): fin 2 := 
    if b = tt then 0 else 1
```

Which is only the value of `f`, not a function itself.

#### [Johan Commelin (Oct 16 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917243):
That did define a function `f`.

#### [Johan Commelin (Oct 16 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917292):
It is the same as
```lean
def f : bool → fin 2 :=
\lam b, if b = tt then 0 else 1
```

#### [Chris Hughes (Oct 16 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917376):
`def f (h : 1 = 1 ∨ 0 = 0) : ℕ := or.cases_on h (λ h, 0) (λ h, 1)`. The iota reduction rule says `f (or.inl rfl) = 0` and that `f (or.inr rfl) = 1)`, but since by proof irrelevance `or.inl rfl = or.inr rfl`, this would imply `0 = 1`, hence `or` cannot eliminate into data.

#### [Chris Hughes (Oct 16 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917466):
Here's your function defined using the equation compiler
```lean
def f : bool → fin 2
| tt := 0
| ff := 1
```

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917644):
```quote
`def f (h : 1 = 1 ∨ 0 = 0) : ℕ := or.cases_on h (λ h, 0) (λ h, 1)`. The iota reduction rule says `f (or.inl rfl) = 0` and that `f (or.inr rfl) = 1)`, but since by proof irrelevance `or.inl rfl = or.inr rfl`, this would imply `0 = 1`, hence `or` cannot eliminate into data.
```
Huh -- I thought `0 = 0` and `1 = 1` would just be treated as propositions (and indeed they are equivalent).

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917806):
```quote
It is the same as
```lean
def f : bool → fin 2 :=
\lam b, if b = tt then 0 else 1
```
```
Thanks -- why doesn't `∀ b : bool` work in place of `λ b`?

#### [Kenny Lau (Oct 16 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917850):
`(λ b,  proof) : (∀ b : bool, p b)`

#### [Chris Hughes (Oct 16 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917919):
They are treated as propositions. That's why it's not possible to eliminate into data. If both sides of the `or` are true it breaks proof irrelevance, but without this iota reduction rule you can't compute with it.

#### [Johan Commelin (Oct 16 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917928):
`\forall` is only for propositions.

#### [Chris Hughes (Oct 16 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917973):
It's only for types.

#### [Kevin Buzzard (Oct 16 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135921897):
@**Abhimanyu Pallavi Sudhir** here are some comments on things you said whilst I was going home. 

If `X` is an inductive type then it could well have been defined in something like the following way:

```lean
inductive X
| c1 : X
| c2 : X
```

and then you can define functions `X->Y` using the equation compiler like this (I `open X` because `c1` is really called `X.c1` etc)

```lean
open X

def f : X → ℕ
| c1 := 4
| c2 := 6
```

Note that the `|` symbols are being used in two different ways here -- first to define an inductive type, and secondly to define a function from the type. The equation compiler is quite powerful. It's trickier to get it to define the map from `fin 2`, but it's possible. The equation compiler is very smart.

You asked about `\forall b` instead of `lam b` -- one is the type, and one is the term. You use Pi to make Pi types (and forall is a special case of Pi, as are function types), and lam to make terms of type Pi. This is what Kenny's post was demonstrating. It took me some time to get my head around all this but it's easy really -- somehow I never read anything which explained it all in simple terms (which was what I needed this time last year). There are propositions called things like `P` and proofs called things like `H` or `HP`. Similarly there are function types (Pi types) called things like `X -> Y` and then there are actual functions (the terms) called things like `lam x, x + 1`.

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925018):
Thanks. This works for exercise 2 (`left_inv` only -- presumably the same thing works for `right_inv`) :

```lean
import data.equiv.basic
import tactic.norm_num
--set_option pp.notation false

def f : bool → fin 2
    | tt := 1
    | ff := 0

def f_inv : fin 2 → bool :=
    λ k, if k = 1 then tt else ff

def X : equiv bool (fin 2) := {
  to_fun := f,
  inv_fun := f_inv,
  left_inv := begin
                rw function.left_inverse,
                intro x, cases x,
                have Hfff : f ff = 0, rw f,
                rw Hfff, rw f_inv, exact dec_trivial,
                have Hftt : f tt = 1, rw f,
                rw Hftt, rw f_inv, exact dec_trivial,
              end,
  right_inv := begin sorry end
}

example : function.bijective f := sorry --<FILL IN FUNCTION NAME> X

#check function.bijective_iff_has_inverse
```

Although `dec_trivial` did the job for me, I'm curious to know what exactly is the algorithm being tried by Lean at that point (in Lean notation, it's obvious mathematically), i.e. what could I replace `dec_trivial` with?

#### [Kevin Buzzard (Oct 16 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925157):
`right_inv` might be harder, the way you've set it up.

#### [Kevin Buzzard (Oct 16 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925232):
```lean
  left_inv := begin
                intro x, cases x,
                have Hfff : f ff = 0, rw f,
                rw Hfff, rw f_inv,refl,
                have Hftt : f tt = 1, rw f,
                rw Hftt, rw f_inv, refl,
              end,
```

#### [Kenny Lau (Oct 16 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925250):
we should all wait until `fin_cases` is merged

#### [Kevin Buzzard (Oct 16 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925295):
Your `rw` doesn't seem to do anything. Because your goal is definitionally equal to what the rw changed it into, you can just skip it. And both of your algorithms are `rfl` -- the left hand side equals the right hand side by definition.

#### [Kevin Buzzard (Oct 16 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925376):
@**Kenny Lau** I just dealt with `n>=2` using contradiction. Abhi is yet to run into this issue I think.

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925548):
Does `fin_cases` actually allow just doing cases on `fin n`? Does it break it up into the full `n` cases even if `n` is a thousand?

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925570):
```quote
@**Kenny Lau** I just dealt with `n>=2` using contradiction. Abhi is yet to run into this issue I think.
```
Wait, which issue?

#### [Kevin Buzzard (Oct 16 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925651):
His definition of `f_inv` is "k=1" and "all other cases" so he'll have to deal with k>=2 at some point.

#### [Kevin Buzzard (Oct 16 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925662):
```lean
  left_inv := begin
                intro x, cases x;refl
              end,
```

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925812):
I guess `refl` is more powerful than I thought.

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925884):
```quote
His definition of `f_inv` is "k=1" and "all other cases" so he'll have to deal with k>=2 at some point.
```
I can just use exfalso and prove a contradiction using `2 > fin.last`.

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925975):
In fact it seems just doing `cases x` gives a statement that says `x.val < 2`.

#### [Kenny Lau (Oct 16 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925992):
```lean
import data.fintype

noncomputable def X : equiv bool (fin 2) :=
trunc.out (fintype.equiv_fin bool)
```

#### [Kenny Lau (Oct 16 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925998):
:P

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926050):
What??

#### [Kevin Buzzard (Oct 16 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926067):
rofl what happened there?

#### [Mario Carneiro (Oct 16 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926096):
`fintype.card bool = 2`

#### [Mario Carneiro (Oct 16 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926103):
so `bool ~= fin 2`

#### [Kenny Lau (Oct 16 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926145):
trunc

#### [Kevin Buzzard (Oct 16 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926148):
Oh, that's exactly what Abhi was asking if he could do earlier. `fintype.equiv_fin` is the general proof that a type which is known to have finitely many elements (say `n`) `equiv`s with `fin n`

#### [Kenny Lau (Oct 16 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926152):
still trunc

#### [Kevin Buzzard (Oct 16 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926170):
Aah, but Kenny's proof is noncomputable :O

#### [Mario Carneiro (Oct 16 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926191):
the funny part is it's not really, if you evaluate the proof you can eliminate the trunc

#### [Kenny Lau (Oct 16 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926198):
how?

#### [Kenny Lau (Oct 16 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926204):
wait, proof is irrelevant and can't be evaluated

#### [Mario Carneiro (Oct 16 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926215):
false on both counts

#### [Mario Carneiro (Oct 16 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926232):
it's not a proof, it's a trunc

#### [Mario Carneiro (Oct 16 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926236):
and it can be evaluated

#### [Mario Carneiro (Oct 16 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926239):
even if it was a proof

#### [Kenny Lau (Oct 16 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926242):
how can I do it then

#### [Mario Carneiro (Oct 16 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926244):
via `#reduce`

#### [Kenny Lau (Oct 16 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926289):
oh well then you can't make it a definition

#### [Kenny Lau (Oct 16 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926300):
could you show us the code?

#### [Mario Carneiro (Oct 16 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926331):
If you `#reduce` the proof that `trunc (bool ~= fin 2)` you will get something that starts `trunc.mk`... then you throw that away and keep the rest

#### [Kevin Buzzard (Oct 16 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926448):
...or get a deterministic timeout

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926489):
```lean
def X : equiv bool (fin 2) := {
  to_fun := f,
  inv_fun := f_inv,
  left_inv :=  begin
                 --rw function.left_inverse,
                 intro x, cases x,
                 have Hfff : f ff = 0, rw f,
                 rw Hfff, rw f_inv, refl,
                 have Hftt : f tt = 1, rw f,
                 rw Hftt, rw f_inv, refl,
               end,
  right_inv := begin
                 intro x,
                 have H01 : ∀ s : fin 2, s = 0 ∨ s = 1, exact dec_trivial,
                 have x01 : x = 0 ∨ x = 1, exact H01 x,
                 cases x01 with x0 x1,
                 --case x0
                    rw x0,
                    have Hfarc0 : f_inv 0 = ff, refl,
                    rw Hfarc0, refl,
                 --case x1
                    rw x1,
                    exact dec_trivial,
               end
}
```

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926558):
What's `trunc.out`? Someone catch me up.

#### [Kevin Buzzard (Oct 16 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926607):
it noncomputably removes the trunc.

#### [Kenny Lau (Oct 16 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926655):
For a type `\a`, `trunc \a` is the type `\a` quotient by the equivalence relation that relates everything

#### [Kevin Buzzard (Oct 16 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926721):
You can see the docstring for `trunc` by hovering over it. It's some weird CS thing.

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926919):
Ok, I'll need to read up a bit on that.

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926937):
By the way, exercise 3 is just `equiv.bijective X` (or at least this works).

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135927027):
Wait, could we also have used `finset.card_eq_of_bijective` to prove bijectivity then prove `equiv` from `equiv.of_bijective`?

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135927044):
Oh wait that's for `finset`s.

#### [Kevin Buzzard (Oct 16 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135927279):
```quote
By the way, exercise 3 is just `equiv.bijective X` (or at least this works).
```
Great! How did you find it? I found it by writing `bijective` and hitting ctrl-space and escape a few times.

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135927496):
```quote
Great! How did you find it? I found it by writing `bijective` and hitting ctrl-space and escape a few times.
```
Yep, same.

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135927538):
Although I didn't hit escape, just scrolled.

#### [Kevin Buzzard (Oct 16 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135927565):
Sometimes in VS Code the first time I try ctrl-space I don't get all the options, so I instinctively cancel and try again before I start scrolling.

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135927649):
Yeah, I think sometimes it limits itself to a specific namespace or something.

#### [Kevin Buzzard (Oct 16 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135927702):
Oh this `trunc` thing -- Lean is not keen on choosing a bijection between `bool` and `fin 2`but if you put an equivalence relation on the type of all choices, and the relation was "it's always true", then Lean will give you an element of the quotient type and this is well-defined! So Kenny's construction only shows that the type of `equiv`s is non-empty without producing an explicit element.

#### [Chris Hughes (Oct 16 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135929371):
It's stronger than nonempty.

#### [Kevin Buzzard (Oct 16 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135929688):
because it's data. But I am very hazy about what difference this makes, and even hazier about whether I care.

#### [Chris Hughes (Oct 16 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135930657):
The definition of `equiv.fintype`, the thing that says `A` is finite implies `equiv A B` is finite uses `equiv_fin` and the lift condition is met because `fintype` is a `subsingleton`. This in turn means that determinant is computable.

#### [Kevin Buzzard (Oct 16 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135931288):
They'll be pleased in M1M1 :-) I still have not got my head around how important computability is in my world.

#### [Chris Hughes (Oct 16 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135931427):
I get the impression that it's nice to be able to easily prove `1+1=2` etc., but I never use computability on naturals on numbers bigger than about 4, and the same with most other computable objects.

#### [Chris Hughes (Oct 16 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135931731):
Also Lean computable rarely means efficiently computable, so it's kind of useless.

#### [Kenny Lau (Oct 16 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135931843):
David Helm once said that one of the reasons he likes modular forms is that this is one of the unique opportunities in pure maths where you get to see numbers bigger than 4

#### [Kevin Buzzard (Oct 16 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135931969):
I once wrote an entire paper and then looked through it to find the biggest number in it, and it was 2

#### [Kevin Buzzard (Oct 16 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135931985):
Maybe I'm less concerned about computability than I think

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135932585):
```quote
I once wrote an entire paper and then looked through it to find the biggest number in it, and it was 2
```
I'm guessing reference and equation numbering don't count.

#### [Kevin Buzzard (Oct 17 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135933569):
I'm not sure I numbered any equations but I almost certainly numbered theorems (did you notice that here they name them instead?) and no I didn't count those numbers :-)

