---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08327darraytypechangingupdate.html
---

## Stream: [general](index.html)
### Topic: [`d_array` type changing update](08327darraytypechangingupdate.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125705649):
In `data.array.basic`, there's an optimized mutation function:

```
def foreach (a : d_array n α) (f : Π i : fin n, α i → α i) : d_array n α :=
...
```

Is it possible to change the element type during the update efficiently? I'd like an operation like:
```
def foreach (a : d_array n α) (f : Π i : fin n, α i → β i) : d_array n β :=
...
```

Ultimately, I'm trying to implement `traversable` for array and I'd like it to not be too slow. If the required functions are not available, should I postpone submitting a traversable instance of array to `mathlib` until it can be done efficiently?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706021):
No, it's an in-place update so the type has to stay fixed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706063):
Because the amount of memory allocated per element?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706064):
It's conceivable that you could use an auxiliary array of sigma types (which would be erased on the vm side)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706075):
It updates like this: [1, 2, 3] -> [f 1, 2, 3] -> [f 1, f 2, 3] -> [f 1, f 2, f 3]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706079):
Each update is performed on the same underlying data structure so that space isn't wasted

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706080):
Right but now, `array` is based on `d_array` where the type of elements depends on indices

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706126):
So the intermediate arrays are well-typed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706138):
The core function doing the in place write is `array.write` and this function doesn't change the type of the argument

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706181):
oh wait, the comment says that `foreach` is also given a builtin impl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706239):
Maybe you can get similar performance with `iterate` to build the new array?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706298):
Actually, maybe I'm better off converting to list, traversing the list and converting back to array: if I'm executing within a monad like list that would mean duplicating the array a lot while the list would share its tail so it wouldn't be so bad.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706300):
Actually I think `array.mk` is the most efficient option

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706344):
that will just evaluate the whole function at once to get the new elements

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706523):
I'm not sure how I could reconcile that with working within an applicative. I would have to store an accumulation of closures which does not sound good

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706533):
```

def d_array.map'
  {n : nat} {α β : fin n → Type*}
  (a : d_array n α) (f : Π i : fin n, α i → β i) : d_array n β :=
⟨λ i, f _ (a.read _)⟩

#eval
  let a := d_array.mk (λ a:fin 1000000, a.1) in
  let a' := timeit "map" (a.map' (λ i j, j+1)) in
  a'
```
Looks like it takes roughly linear time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706583):
That looks good but it doesn't seem to address my comment

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706614):
It is important to realize that (unlike most constructors taking a function) `array.mk` does not store its argument function, it evaluates it and puts the result in an array

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706658):
`array.mk f` is O(n), while `array'.mk f` would be O(1) if you wrote `array'` identically to `array`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706720):
and conversely, `a.read i` does not call the underlying function of `a`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706733):
```
#eval
  let f (a:fin 3) := trace ("calling f " ++ to_string a.1) a.1 in
  let a := d_array.mk f in
  a.read ⟨1, dec_trivial⟩

-- calling f 0
-- calling f 1
-- calling f 2
--
-- (note: "calling f 1" does not appear twice)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125706833):
Right, that make sense but the reason I was talking about accumulating closures is that I'm thinking of  implementing the mutation by recursion because I have to combine applicative values:

```
def traverse (g : α → f β) : Π n (a : array n α), f (fin n → β) 
 | 0 a := -- ...
 | (succ n) a := _ <$> g (a.read ⟨n,_⟩) <*> traverse n a.pop_back
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707001):
So you have a dependency between the different elements of the computation? Like calculating the first element affects the computation of the second

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707019):
It might. `f` is actually a parameter of which I only know that it's an applicative functor

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707043):
Do you have a default value for the array? This will be easier if you do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707057):
Where would be the fun in "easy"? :stuck_out_tongue_closed_eyes:  I have no assumptions about either `α` or `β`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707105):
Except: they're from the same universe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707117):
I think you should just do it semi-imperatively then, just call `read` and `push_back` and make sure you use the array linearly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707160):
Do not do induction over the array size

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707165):
and accumulate an array, not a function to fin n

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707166):
You mean I should do induction on the index `i` and maintain `i < n`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707213):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707214):
The fun thing about knowing next to nothing about `f` is that I can't guarantee that it is a linear computation: if it's a non-deterministic computation, it would screw up that assumption

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707217):
I have no mental model for applicative functors except as monads

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707232):
When I say linearly I mean in the "linear logic" sense, i.e.  use the variable once

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707248):
That's good enough. The only thing they add is asynchronous computations. But just think of the list monad. It's basically an unbounded backtracking device

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707276):
That means that at every branching point, I'd need a copy of the array

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707277):
Lean doesn't currently check this but you can test it by setting some option to hear whether an array write is destructive or not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707285):
How does that work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707289):
Whenever you call `array.write` lean checks the reference counter to determine if it can do an in-place update

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707344):
But can I use that information to select a different algorithm?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707489):
Maybe the best is accept the intermediate list. Maybe in Lean 4 we'll see custom rewrite rules for optimization. Then, maybe I can eliminate that intermediate list when the use is linear (or affine)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707547):
The linear usage thing is a static analysis you can do on your code to try and preserve destructive writes when the use is actually linear, but since the check is done at run time it doesn't matter if you use it in a nonlinear context, it will just make copies and that's the right thing to do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707783):
Does this work?
```
universe u
variables {α β : Type u} {f : Type u → Type u} [applicative f]

def traverse.aux (g : α → f β) (n) (a : array n α) :
  ∀ i ≤ n, f (array i β)
| 0 h := pure array.nil
| (i+1) h :=
  have h' : i ≤ n := nat.le_of_succ_le h,
  array.push_back <$> (traverse.aux _ h') <*> g (a.read ⟨i, h⟩)

def traverse (g : α → f β) (n) (a : array n α) : f (array n β) :=
traverse.aux g n a n (le_refl _)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707829):
Nice! Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125707882):
I believe in backtracking computations, this will be pretty inefficient though. I'm wondering if the rarity of such monads is a good reason to accept that cost or if taking a small hit in the general case would be a worthy price to pay so that backtracking computations wouldn't be too slow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125708080):
For backtracking computations, you will end up using more of the `p` in the `p_array` data type that actually implements lean's `array` in C++. It has optimizations for precisely this use case, it's not just a block of memory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125708125):
I would argue that the lack of an actual C-like array data structure is a current failing of lean, but having a deluxe array type has its advantages

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125708128):
(the `p` stands for [persistent](https://en.wikipedia.org/wiki/Persistent_data_structure) btw)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125708187):
Oh! Interesting!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 26 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125708231):
I assume the kind of optimization you're talking about is to queue up updates until you get a read and only then do you actually perform them?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 26 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60d_array%60%20type%20changing%20update/near/125708292):
Actually I'm not exactly sure, I haven't studied the implementation in detail. I think the updates are in chunks though, there is a "buffer" aspect to it as well which makes repeated `push_back` like I've done here not stupidly inefficient

