---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/62811listfromafinset.html
---

## Stream: [maths](index.html)
### Topic: [list from a finset](62811listfromafinset.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 13 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032331):
Is there a way to get a `list` from a `finset` without using `finset.sort` or writing my own recursive function on `finset`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 13 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032374):
but `finset` is a subquotient of `list`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 13 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032377):
and quotients can't be reversed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 13 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032390):
That's right, so I couldn't use a recursive function anyway.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 13 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032522):
Well, I suppose I could follow the `sort` example:

```lean
def finset.sort (s : finset α) : list α := multiset.sort r s.1

def multiset.sort (s : multiset α) : list α :=
quot.lift_on s (merge_sort r) $ λ a b h,
eq_of_sorted_of_perm tr.trans an.antisymm
  ((perm_merge_sort _ _).trans $ h.trans (perm_merge_sort _ _).symm)
  (sorted_merge_sort r to.total tr.trans _)
  (sorted_merge_sort r to.total tr.trans _)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 13 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032728):
Ah, `fold`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 13 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032788):
Why do you not want to sort it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 13 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032790):
Because I don't need a particular order.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 13 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032791):
then it's uncomputable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 13 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032857):
Right but them being in a particular order can't be harmful, is it? Is it that you care about the performances?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 13 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032874):
It requires adding an ordering constraint to the elements that I don't need or want.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 13 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032878):
What you could do is compute on the list before taking it out of the quotient and proving that the result is independent of order

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 13 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125032951):
```lean
def multiset.foldr (f : α → β → β) (H : left_commutative f) (b : β) (s : multiset α) : β :=
quot.lift_on s (λ l, foldr f b l) (λ l₁ l₂ p, foldr_eq_of_perm H p b)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 13 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033001):
```quote
It requires adding an ordering constraint to the elements that I don't need or want.
```
otherwise it won't be a well-defined function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 13 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033199):
```quote
```lean
def multiset.foldr (f : α → β → β) (H : left_commutative f) (b : β) (s : multiset α) : β :=
quot.lift_on s (λ l, foldr f b l) (λ l₁ l₂ p, foldr_eq_of_perm H p b)
```
```
Exactly. What are you trying to compute?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 13 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033557):
So, `finset.fold` doesn't work because it requires the append operator to be commutative, which it is not:

```lean
def to_list : finset α → list α :=
  fold (++) [] (λ a, [a])

⊢ is_commutative (list α) append
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 13 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033566):
right, because the function you're trying to define isn't well-defined

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 13 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033577):
Since `finset` is a quotient on list permutations, is it not possible to choose an arbitrary permutation?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 13 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033582):
no, that's what quotient is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 13 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033583):
it needs to work for any permutation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 13 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033643):
your functions need to be well-defined

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 13 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033652):
if {2,1,3} gives [2,1,3] and {1,2,3} gives [1,2,3], then it isn't a well-defined function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 13 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033654):
`quotient.out` works, but that's noncomputable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 13 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033665):
`quot.unquot` also works, but you can't use that in a proof, because it implies false.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 13 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033708):
in fact, if your function did that, then I can prove false

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 13 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033714):
because {2,1,3} and {1,2,3} are equal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 13 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125033803):
@**Kenny Lau** Right, so your point is that the function has to produce the same permutation for any set, and that's why sorting is necessary.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 13 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125034441):
Right. But the other idea is: what are you going to do with that list? If the function that uses the list works the same for all permutation, you don't need to care about sorting the list. You just need to make sure that when you use the list, you produce the same results regardless of order

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 13 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125034446):
In the end, I want a list with certain properties. I thought using a finset to construct it would be simpler (since that function is easier), but it appears that I should just construct the list directly. I'm going to try using `list.to_finset` to simplify the property testing during construction in an auxiliary function and then extract the list-specific properties from the finset properties in a wrapper.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 13 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125034447):
Instead of going inside the `quot` to extract a list, go inside to do more of your computations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 13 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125034894):
Sean -- you want your function to be computable?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 19 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125291437):
To catch up on this thread, I was trying to figure out how to use

```lean
def fresh_finset (s₁ : finset α) : ∀ n, Σ' (s₂ : finset α), card s₂ = n ∧ s₂ ∩ s₁ = ∅
```

in the definition of

```lean
def fresh_list (s : finset α) : ∀ n, Σ' (l : list α), l.length = n ∧ l.nodup ∧ l.to_finset ∩ s = ∅
```

but, as has been pointed out to me, this is not possible without adding an additional constraint on `α`. In the end, I wrote `fresh_list` from scratch. It wasn't as difficult as I thought, and it shares a proof structure with `fresh_finset`.

See the [source](https://github.com/spl/tts/blob/010faf776c4fda5a376994a06cd76dd0784f3faf/src/data/finset/fresh.lean#L19-L50) for the definitions.

Kevin: Yes, I want a computable definition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125291609):
I agree that it is best to write the list definition directly in this case. I think it would be better to have the fresh list separate from the properties though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 19 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125291625):
How so?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125291630):
It makes the code path a bit more obvious

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125291682):
I always worry that the match and such will add extra overhead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125291688):
it's not clear to me whether it is in fact optimized away

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 19 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125291689):
What type signature would you want?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125291854):
```

class has_fresh (α : Type*) :=
(fresh : finset α → α)
(fresh_not_mem : ∀ s, fresh s ∉ s)

def fresh_list (s : finset α) : nat → list α
| 0 := []
| (n+1) := let l := fresh_list n in fresh (l.to_finset ∪ s) :: l

theorem fresh_list_length (s : finset α) : ∀ n, (fresh_list s n).length = n

theorem fresh_list_nodup_disjoint (s : finset α) :
  ∀ n, (fresh_list s n).nodup ∧ (fresh_list s n).to_finset ∩ s = ∅
```
I conjoin the last two only because I think the proof is by mutual recursion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 19 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125291994):
Ah, I see what you mean. You're talking about splitting the methods of the `class`. Yeah, that seems fine, assuming it works.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125292003):
By the way, it is conceivable that `fresh` in the typeclass will be difficult to define, since it enforces that the fresh element not depend on the order of the input list

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 19 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125293488):
```quote
By the way, it is conceivable that `fresh` in the typeclass will be difficult to define, since it enforces that the fresh element not depend on the order of the input list
```
@**Mario Carneiro** I don't follow. I'm guessing you mean it's difficult to define `fresh` for instances of `has_fresh`. But what “input list”? `has_fresh` only depends on the element of the `finset`.

You could, of course, define different functions to produce a fresh element from a `list` or a fresh element from a `finset` with a required ordering to the element. Nonetheless, it is possible to define a `has_fresh` instance for `nat` and other infinite types for which it is possible to find an extreme, and `has_fresh` does not impose an ordering constraint that is not always needed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125293581):
I mean that to implement `fresh` on a type `A`, you need to define a function `list A -> A`, and then lift it to a function `finset A -> A`, meaning that the original function must map `[a, b]` and `[b, a]` to the same fresh value `c`. Depending on `A`, that may not be convenient to do, for example if you hash the list or something to generate a disambiguator

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 19 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125301276):
```quote
I think it would be better to have the fresh list separate from the properties though
```

@**Mario Carneiro** This was a good suggestion. The [result](https://github.com/spl/tts/blob/84267eb8dac118884ffb8de2f77fa3cfb3c397cd/src/data/finset/fresh.lean) is much cleaner now.

```quote
I mean that to implement `fresh` on a type `A`, you need to define a function `list A -> A`, and then lift it to a function `finset A -> A` [...]
```

This is the part I don't follow. Why does one need to define a function `list A -> A`? For [`nat`](https://github.com/spl/tts/blob/84267eb8dac118884ffb8de2f77fa3cfb3c397cd/src/data/finset/fresh.lean#L89-L142), this isn't necessary. I conjecture that the same is true for other types.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125301322):
every function on `finset` is ultimately the `lift` of a function on `list`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125301327):
I assume you used `finset.fold` or something to define the nat function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 19 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20from%20a%20finset/near/125301330):
True, but that doesn't mean I have to write the `list` function itself.

