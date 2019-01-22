---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01949minimumoffiniteset.html
---

## [general](index.html)
### [minimum of finite set](01949minimumoffiniteset.html)

#### [Reid Barton (May 06 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126161321):
I have a `finset` of rationals which I know is nonempty. How do I find its minimum element?

#### [Mario Carneiro (May 06 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126163639):
I forget if there is a `max` operation on finsets, but you can `fold` with `max`

#### [Sean Leather (May 06 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126170875):
```quote
I have a `finset` of rationals which I know is nonempty. How do I find its minimum element?
```
@**Reid Barton** See https://github.com/spl/tts/blob/master/src/data/finset/fresh.lean#L121-L154

I'd like to see something like this with `max` and `min` in mathlib. I haven't proposed it because I wasn't sure it was worth it, but, since you are also looking for it, perhaps it is.

#### [Sean Leather (May 07 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126212361):
@**Reid Barton** Is this something (after replacing `max` with `min`) that would be useful to you? I can work on it next.

```lean
import data.finset

namespace finset
variables {α : Type*} [decidable_linear_order α]

def max (a : α) : finset α → α :=
  fold _root_.max a id

@[simp]
theorem max_empty {a : α} : max a (∅ : finset α) = a :=
  by simp [max]

@[simp]
theorem max_insert {a b : α} {s : finset α} (h : a ∉ s)
: max b (insert a s) = _root_.max a (max b s) :=
  by simp [max, fold_insert h]

@[simp]
theorem max_singleton {a b : α} : max b {a} = _root_.max a b :=
  by simp [max]

theorem le_max_left (a : α) (s : finset α) : a ≤ max a s :=
  finset.induction_on s
    (by rw max_empty)
    (λ b s (hnm : b ∉ s) (ih : a ≤ max a s),
     by rw max_insert hnm; exact le_trans ih (le_max_right b (max a s)))

theorem le_max_of_mem {a b : α} {s : finset α} (h : a ≤ b) : a ∈ s → a ≤ max b s :=
  finset.induction_on s
    (λ _, by simp only [max_empty, h])
    (λ c s (hnm : c ∉ s) (ih : a ∈ s → a ≤ max b s) (hins : a ∈ insert c s),
     begin
       rw max_insert hnm,
       cases mem_insert.mp hins,
       case or.inl : p { simp only [p, _root_.le_max_left] },
       case or.inr : p { exact le_trans (ih p) (le_max_right c (max b s)) }
     end)

end finset
```

#### [Patrick Massot (May 07 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126212689):
What's this `{a}` syntax in `max b {a}`?

#### [Sean Leather (May 07 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126212753):
It's notation for a singleton.

#### [Sean Leather (May 07 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126212815):
Actually, to correct myself, `{a}` is a singleton, but the notation comes from `init/core.lean`, I think:

```lean
/- Type class used to implement the notation { a ∈ c | p a } -/
class has_sep (α : out_param $ Type u) (γ : Type v) :=
(sep : (α → Prop) → γ → γ)
```

#### [Patrick Massot (May 07 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126212817):
Oh

#### [Patrick Massot (May 07 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126212857):
I was confused, I thought it was an implicit parameter right of colon

#### [Patrick Massot (May 07 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126212858):
The theorem even has "singleton" in its name...

#### [Sean Leather (May 07 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126212913):
Hmm, maybe it's not from `has_sep`. I thought I knew, but I don't know anymore.

#### [Sean Leather (May 07 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126212976):
Ah, right, it's this one:

```lean
/- Type classes has_emptyc and has_insert are
   used to implement polymorphic notation for collections.
   Example: {a, b, c}. -/
class has_emptyc   (α : Type u) := (emptyc : α)
class has_insert   (α : out_param $ Type u) (γ : Type v) := (insert : α → γ → γ)
```

#### [Sean Leather (May 07 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126212990):
So, if your type has `has_emptyc` and `has_insert` instances, you can use the `{..., ...}` notation.

#### [Sean Leather (May 07 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126213048):
I agree that it can be confusing.

#### [Patrick Massot (May 07 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126213133):
It's my fault, I wasn't paying enough attention. I shouldn't be watching Zulip while grading Sage notebooks (@**William Stein** when will we get auto-grading Sage notebooks so that we can focus on understanding Lean code?).

#### [Sean Leather (May 07 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126213255):
I don't think it's a great idea to overload `{...}` in this way, even if it isn't ambiguous to the parser. But it is notationally short, which makes it convenient.

#### [Patrick Massot (May 07 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126213294):
And it's the maths notations, so it should win over any other interpretation

#### [Sean Leather (May 07 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126213343):
True, but it doesn't see as much usage as implicit parameters, and it would be better to reserve short notation for things you type/read a lot.

#### [Sean Leather (May 07 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126213355):
You pretty much only use this notation for singletons or examples.

#### [Sean Leather (May 07 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126214292):
PR for `finset.max` and `finset.min`: https://github.com/leanprover/mathlib/pull/133

#### [Patrick Massot (May 07 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126215835):
Nice. I will probably use it to build new normed spaces out of finitely many old ones.

#### [Reid Barton (May 07 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126223645):
@**Sean Leather** I think this approach with a starting element (`a`) would be fine for my current application, since I have a particular element which I know belongs to the set. From a general math perspective, though, it's odd not to be able to talk about the minimum of a nonempty set, without first choosing an element of the set.

#### [Reid Barton (May 07 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126223715):
I've been considering an approach that starts from `fold1`of an associative, commutative operation on a nonempty multiset, though this `fold1` was quite a challenge to define.

#### [Reid Barton (May 07 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126223856):
But `fold1` seems like something one ought to have anyways.

#### [Reid Barton (May 07 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126223869):
A friend suggested that I could just sort the list (`finset.sort`) and take the first element

#### [Sean Leather (May 08 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126251600):
My thinking is that you can write different variations using `max [decidable_linear_order α] : α → finset α → α`. I believe this definition of `max` is the most general and least prescriptive since only `[decidable_linear_order α]` is required.

#### [Sean Leather (May 08 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126251644):
@**Johannes Hölzl** [suggested](https://github.com/leanprover/mathlib/pull/133#issuecomment-387110828) `max [decidable_linear_order α] [inhabited α] : finset α → α`, but I'm not sure if that's better ([my response](https://github.com/leanprover/mathlib/pull/133#issuecomment-387300724)).

#### [Mario Carneiro (May 08 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126251859):
It is not true that `max` as suggested by Johannes is the same as `max_inhabited` that you wrote. If `s` is nonempty, then `max (default A) s` is the max of `default A` and the elements of `s`, while Johannes's `max` is the max of the elements of `s` only. It is closer to Reid's suggested max operation, except that the nonempty constraint is replaced by a default value.

#### [Sean Leather (May 08 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126251868):
Right. See the bottom of my response.

#### [Mario Carneiro (May 08 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126251909):
Given johannes's `max` function, you could recover your `max` function as `sean_max a s := @johannes_max A _ <a> (insert a s)`

#### [Sean Leather (May 08 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126251917):
So they are equivalent?

#### [Mario Carneiro (May 08 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126251924):
Johannes's definition is more complicated since it requires casing on whether the list is empty

#### [Sean Leather (May 08 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126251929):
What is the definition?

#### [Mario Carneiro (May 08 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126251966):
there is not an easy expression for `johannes_max` using `sean_max`, you would need another quot.lift

#### [Mario Carneiro (May 08 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126251969):
You have to start from list, define `foldl1` and work your way up

#### [Sean Leather (May 08 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126251977):
Ah, something like that.

#### [Mario Carneiro (May 08 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126251983):
Alternatively, you could `sean_max` over `option A`

#### [Mario Carneiro (May 08 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126251987):
where `none` has the appropriate interpretation as a neutral element for max

#### [Sean Leather (May 08 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126252030):
You mean map/image `some` over the `finset`?

#### [Mario Carneiro (May 08 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126252034):
and that would give you both the partial `max` function and the inhabited max function (Johannes's max)

#### [Mario Carneiro (May 08 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126252047):
Any semigroup operation extends to a monoid if you add a neutral element

#### [Mario Carneiro (May 08 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126252058):
That means that you can take a semigroup operation like `max` and extend it to `option_max : option A -> option A -> option A` that is a monoid operation

#### [Mario Carneiro (May 08 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126252096):
and then you can `finset.prod` over this

#### [Mario Carneiro (May 08 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126252112):
This is essentially the same as adjoining a `-inf` element to the set

#### [Sean Leather (May 08 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126252114):
Can you not `finset.image some`?

#### [Mario Carneiro (May 08 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126252120):
That would be the input to the fold, yes

#### [Sean Leather (May 08 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126252124):
Right, okay.

#### [Mario Carneiro (May 08 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126252178):
The nice thing about this approach is that it naturally handles partiality, you don't need the `inhabited` thing; but it's easy to implement the inhabited version using `option.iget`

#### [Sean Leather (May 08 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126252244):
Personally, I'm not a big fan of `inhabited`. I haven't found a need for it in anything I've done, and I feel like, if you need an `inhabited` type, why not use `option` in the first place?

#### [Sean Leather (May 08 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126252258):
But I'm happy to see *some* version of `finset.max` and `finset.min` go into mathlib, so I don't feel that strongly about which one... as long as it works with `nat`. :simple_smile:

#### [Mario Carneiro (May 08 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126252472):
I have a similar antipathy to `inhabited`, it's a somewhat lazy way to totalize functions like division on nonempty domains.

#### [Mario Carneiro (May 08 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126252480):
Arguments in favor would say that composing them is a lot cleaner than the monad stuff

#### [Mario Carneiro (May 08 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126252500):
i.e. `(x + 2) / (y + 2 / z)` is easier to read than `do a <- 2 / z, (x + 2) / (y + a)` or some such

#### [Mario Carneiro (May 08 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126252566):
The best situation is if you are literally working in a sup_bot semilattice, in which case you don't have to cheat and get a proper function

#### [Johannes Hölzl (May 08 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126253973):
Working on `sup_bot_semilattice` is indeed very nice, e.g.  https://github.com/johoelzl/mason-stother/blob/master/Sup_fin.lean But we don't have a lot of ordered types having this structure, I guess `nat`, `fin`, and `ennreal`.

#### [Johannes Hölzl (May 08 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126254143):
I prefer the `inhabited` version over `option`. With `inhabited` you get not only a nicer syntax, but a lot of cases etc can be easily done in the proofs, while for `option` we are often forced to do it on the term itself.

#### [Sean Leather (May 08 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126265296):
Just thinking about it a little more... It seems like there are two goals here: one for a `max` with no requirements other than `decidable_linear_order` (me) and one for a `max` that does not need the extra `a : α` (Johannes and Reid). In the latter case, which is more useful: an `inhabited α` predicate or a non-empty predicate (e.g. `s ≠ ∅` or `∃ a : α, a ∈ s`)? I'm guessing the non-empty predicate is more useful because `inhabited α` doesn't tell you anything about the `finset` itself, and if you use the `inhabited α` version and want to know that you are not getting the `inhabited.default`, you need to know if the `finset` is empty anyway.

#### [Johannes Hölzl (May 08 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126265564):
It is the other way round, the `inhabited α` is more useful from a user perspective. We don't need to give `max` more information than necessary. For `max` it is enough to show that `α` is inhabited, it is **not** necessary to show that `s` is inhabited (from which at least `nonempty α` follows). It is very annoying when the user always needs to provide a prove that `s` is not empty, this is exactly what I want to avoid.
After all, we are in a theorem prover! Carrying around this information explicitly is not necessary, as usually we can show it in a proof.

#### [Reid Barton (May 08 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126273572):
My only worry about `inhabited` is that as, on the one hand, it is not a `Prop`, and on the other hand, we may not always have a canonical `inhabited` instance at hand and need to construct one from the knowledge that `s` is nonempty, we might end up in a situation where Lean thinks `max s` depends on the choice of `inhabited` instance, even though we know it doesn't really.

#### [Reid Barton (May 08 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126273648):
On the other hand, taking a `nonempty α` instance would make `max` noncomputable, which is maybe sort of okay for a theorem prover but not very attractive for programming use.

#### [Reid Barton (May 08 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126273684):
(As it turns out, the theorem I really need has the conclusion `∃x ∈ s, ∀y ∈ s, f y ≤ f x`, and for this, we need `s` to be nonempty anyways.)

#### [Reid Barton (May 08 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126273773):
The advantage of `s ≠ ∅` here is that it is a `Prop`, but also sufficient to define `max` computably

#### [Reid Barton (May 08 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126274645):
I'm kind of tempted to make `s ≠ ∅` into a type class argument, actually, but maybe that is going too far?

#### [Johannes Hölzl (May 08 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126274905):
Of course a theorem like `s ≠ ∅ -> ∃x ∈ s, ∀y ∈ s, f y ≤ f x` is a nice fit for `max` with such an assumption. I'm worried about complicated constructions, where you have an elaborate proof that `s` is not empty. Putting `s ≠ ∅` in a type class argument makes also some constructions very unpleasent, like using `finset.filter`

#### [Reid Barton (May 09 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126322044):
Maybe the version returning `option` is most flexible then. If you want the version that uses `inhabited`, you can apply `option.iget`.

#### [Sean Leather (May 09 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126330803):
@**Reid Barton** Are you referring to `max [decidable_linear_order α] : finset α → option α`. that returns `none` for an empty `finset` and `some a` for a non-empty `finset`? That would be fine with me.

#### [Reid Barton (May 09 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126332611):
Yes. Or more generally, `fold1 f : finset α → option α` for an associative and commutative operation `f`.

#### [Sean Leather (May 22 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126920643):
For those not following along on GitHub, [leanprove/mathlib#133](https://github.com/leanprover/mathlib/pull/133) has been updated with new versions of the definitions under discussion:
```lean
finset.max [decidable_linear_order α] : finset α → option α
finset.min [decidable_linear_order α] : finset α → option α
```
I think this proposal is better than the original. Thanks to everyone for the discussion and collaboration. Feedback welcome.

#### [Patrick Massot (May 23 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126981683):
So, how do we use this new toy? Say I want to talk about the function "max of coordinates on ℝ^n", assuming n is a British natural number, so I get a well defined function from ℝ^n to ℝ

#### [Patrick Massot (May 23 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126982922):
I can't even find the lemma saying the image of `finset` is a `finset`

#### [Johannes Hölzl (May 23 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum of finite set/near/126984645):
Its already in the type of `finset.image`.
To do what you want: `λx, (univ.image (λn, x n)).max.iget`

