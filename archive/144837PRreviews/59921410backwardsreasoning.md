---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/59921410backwardsreasoning.html
---

## Stream: [PR reviews](index.html)
### Topic: [#410 backwards reasoning](59921410backwardsreasoning.html)

---

#### [Scott Morrison (Oct 10 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/135520408):
I've just made a `[WIP]` pull request for the backwards reasoning tactic which has been discussed in <https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proposal.20for.20.60backwards_reasoning.60>.

#### [Scott Morrison (Oct 10 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/135520452):
It still needs some work (possibly not all of it before merging):
1. Verify that this can be used as a replacement for `backwards_reasoning` currently in `lean-tidy`, for applications in `lean-category-theory`.
2. Combine the `back` and `elim` attributes into just `back`, and `back!`, using `!` as a parameter.
3. Indexing, to make it fun fast. (It's not slow on small examples, but...?)
4. Refactor, and cleanup, as it's not the nicest code at the moment.

#### [Scott Morrison (Oct 10 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/135520471):
I am going to get on with 1. If anyone is interested in helping with 2/3/4 (@**Simon Hudon** ? @**Reid Barton** ?) that would be amazing. :-)

#### [Simon Hudon (Oct 10 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/135520517):
Sure, I'll have a look at 3

#### [Johan Commelin (Oct 25 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/136460194):
Currently the example `tests/back.lean` seems to be broken.

#### [Scott Morrison (Nov 26 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148342156):
Here are the constraints:
* We want to do backtracking search using the "finishing" lemmas, but we don't want to backtrack past the application of a "progress" lemma
* Prioritising the application of different lemmas is a bit complicated, and I don't know what is best!

#### [Scott Morrison (Nov 26 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148342157):
You might think we want to apply "progress" lemmas first (because they've been selected as lemmas which "it's always helpful to apply"!). However it's easy to find situations where you really want to apply a local hypothesis with even higher priority. The current hack is to call `solve_by_elim` with all the lemmas, and then if that fails, try applying a progress lemma and restart `back`. This is horribly inefficient (in particular, it can uselessly call `solve_by_elim` over and over again).

#### [Scott Morrison (Nov 26 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148352552):
Okay, mostly talking to myself here, but I think this is the behaviour I want from `back` (and will need to rewrite to actually achieve).

Given lists of lemmas `P` and `F` (for "progress" and "finishing"), I want to produce a maximal tree of applications, possibly still with metavariables (i.e. remaining subgoals), subject to the condition that no metavariable appears inside an application of a lemma from `F`. (It might seem that this means if you use any `F` lemma, you have to discharge the original goal, but that is not the case --- a `P` lemma might produce multiple subgoals, and then we use `F` lemmas to completely discharge some but not all of these.)

Now, in general there are many possible such maximal trees. I want to do a depth first search of the space of possible applications, where at each stage the lemmas as sorted according to their "number of open arguments", where "open arguments" just means an argument that would create a subgoal when the lemma is applied. (This is more or less the same as the number of arguments which could not be made implicit!) This ensures that if it is ever possible to actually close a goal immediately, we will investigate that before applying lemmas that would create a further subgoal. It also means it's possible to use transitivity lemmas (e.g. `category.comp`) in `back`, but as these typically produce at least 3 new subgoals, they will only be explored "as last resorts".

#### [Scott Morrison (Nov 26 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148352634):
@**Keeley Hoek**, do you think computing that "number of open arguments" for a lemma is easy? I was thinking you'd have to inspect each binder in a Pi type, and just check whether the corresponding `var` actually occurs in the result.

#### [Mario Carneiro (Nov 26 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148353043):
there is a function that does this in `expr`

#### [Mario Carneiro (Nov 26 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148353057):
it is used for pretty printing exprs, since nondependent pis look different

#### [Keeley Hoek (Nov 26 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148353836):
Sure
Just to make sure I understand: the number of "open arguments" of each lemma isn't something that can change throughout the iterations, is it?
Seems like an afternoon-doable thing I guess
So with unwinding, what are we meant to do if we never actually fully discharge the goal?
Say I have a list of "terminal" goals in the search, which one do I actually decide the goal state should be?
---perhaps this backtracking could be a pain

#### [Keeley Hoek (Nov 26 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148354826):
By the way, here is another problem I had when writing `#where`; since `data.list.basic` imports `data.nat.basic`, you can't use any code which, say implements sorting lists (as we will want here) which is defined in that file unless you want your tactic to be unusable there.
But, particularly in `data.list.basic`, there are a whole bunch of useful functions which are just algorithms, but the proofs which are listed alongside them carry the burden of knowing facts about nats, for example. Is there any scope for separating what is a program/routine and what is a proof about a program?

#### [Mario Carneiro (Nov 26 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148355649):
yes, this is reasonable. For the most part we have gotten away without it because all the defs are in `init.data.list.basic`, but we should probably have a file for additional functions on lists added in mathlib

#### [Scott Morrison (Nov 26 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148356627):
```quote
So with unwinding, what are we meant to do if we never actually fully discharge the goal?
Say I have a list of "terminal" goals in the search, which one do I actually decide the goal state should be?
---perhaps this backtracking could be a pain
```

#### [Scott Morrison (Nov 26 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148356653):
I'm not really sure what you meant here. (Also, I wasn't trying (too hard) to pressure you into doing any of this, Keeley. I think I will rewrite the main algorithm, but without the "sorting by number of open arguments" part at first.)

#### [Keeley Hoek (Nov 26 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148356800):
Ok sure that's cool
But yeah if we just count non-implicit arguments working out that number is totally not a big deal

What I was trying to say is if we work out some "tree" with some leaves, none of which actually end up closing all of the goals and giving a proof, we're meant to return control back to the user (and not fail), right? If I understood what the tree was right then wouldn't we have to pick a leaf to leave the goal state in? (if so and I don't misunderstood, I was wondering how to pick this leaf)

#### [Scott Morrison (Nov 26 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148356883):
Oh, I see, you mean what order should the goals be returned in?

#### [Johan Commelin (Nov 26 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148356891):
The safe option is probably just to backtrack, and don't pick a leaf.

#### [Scott Morrison (Nov 26 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148356894):
I guess just the order they pop out of `apply` in.

#### [Johan Commelin (Nov 26 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148356899):
No, that's not what he meant.

#### [Scott Morrison (Nov 26 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148356904):
Ah!

#### [Scott Morrison (Nov 26 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148356906):
Okay :-) Sorry, two different trees going on here.

#### [Scott Morrison (Nov 26 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148356918):
My idea was just to never backtrack back pass the successful application of a `progress` lemma

#### [Scott Morrison (Nov 26 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148356961):
So it matters how they get ordered!

#### [Johan Commelin (Nov 26 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148356976):
What I would like to have in the future is that (if the number of leaves is reasonable), I can just cycle through them interactively, and tell the computer: "Hey, this one looks interesting, let's keep it around." or "Mwahh, this one's going nowhere. We can toss it out."

#### [Scott Morrison (Nov 26 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148356982):
It may be necessary to give the user a way to specify both progress and finishing lemmas directly.

#### [Keeley Hoek (Nov 26 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148356988):
Ok gotcha
I guess the "maximal trees" were psyching me out

#### [Scott Morrison (Nov 26 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148357002):
I was wondering if we can actually write something like: `back [foo!, bar, baz!]`, and use the exclamation marks to distinguish between the two sorts of lemmas.

#### [Keeley Hoek (Nov 26 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148357004):
yep that's a thing

#### [Keeley Hoek (Nov 26 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148357009):
(like an easy thing I mean, supported functionality even!) :D

#### [Scott Morrison (Nov 26 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148357060):
I think actually it might be worth swapping the meaning of `!` and no-`!`, so `!` is for decorating the "progress lemmas". As in "this lemma is a really good idea, apply it whenever you can!"

#### [Keeley Hoek (Nov 26 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148357129):
How about `:commitment:` for `commit`ed xd

#### [Johan Commelin (Nov 26 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148357522):
We don't really care about `commit`s though... only about `push` and `merge`... but I don't know good emoji's for those either...

#### [Scott Morrison (Nov 27 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148407774):
Hi @**Mario Carneiro**, do you recall the name of this function:
> Mario Carneiro: there is a function that does this in expr
> Mario Carneiro: it is used for pretty printing exprs, since nondependent pis look different

I've had a look but can't identify it.

#### [Scott Morrison (Nov 27 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148407791):
Recall this is inspecting a lemma, and deciding how many arguments it has that are not fixed by the return type. Hopefully this is the same number as the number of new goals that will be created when we `apply` the lemma.

#### [Keeley Hoek (Nov 27 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148410955):
I think maybe there is a little subtlety with dependence here scott which has to be accounted for because of the following situation:
say a big 2-layer Pi binder has type `var 0` (nice and simple), but the inner pi binder defining `var 0` has type depending itself on `var 0` (which now refers to the outer Pi binder)
Then we should observe that both arguments will have to be accounted for, right?

#### [Scott Morrison (Nov 27 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148411034):
Oof, I'm not sure I follow. Can you give an example?

#### [Scott Morrison (Nov 27 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148411274):
I've just pushed a major revision of `back`. It's more efficient, has better user interface, and entirely subsumes `apply_rules`. (And possibly also `solve_by_elim`, I'd have to think a bit.)

#### [Keeley Hoek (Nov 27 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148412008):
When making an example I realised my original point was just something that you'd make an implicit arg, but here is a variant.
````
def my_type (n : ℕ) := Type

def my_identity {n : ℕ} (t : my_type n) : Type := t
````
Imagine applying `my_identity` to the goal. The nat `n` will be deduced when the goal associated with `t` is cleared, but the var associated to `n` does not appear in the type and will be considered explicit. I guess changing this is just an improvement to the goal-estimator.

#### [Keeley Hoek (Nov 27 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148412018):
Also super sick tactic

#### [Scott Morrison (Nov 27 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148617753):
I think I'm happy for `apply my_identity` to count as creating two goals. Unfortunately I haven't yet worked out how to do this accounting, and I can see playing with examples that it will be really helpful. You'll be able to tag more ambitious lemmas as `[back]` without worrying about them derailing quick and otherwise successful searches.

#### [Johan Commelin (Nov 27 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148617836):
@**Scott Morrison|110087** Just reading the docs for `back` that you wrote. So in the list `hs` there is no distinction between `foo` and `foo!`?

#### [Scott Morrison (Nov 27 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148617841):
There is! (Or there should be... docs aren't finished.)

#### [Scott Morrison (Nov 27 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148617885):
first, in the list you have to write it as `!foo` for now, as I couldn't get the parser to accept trailing punctuation in a list.

#### [Scott Morrison (Nov 27 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148617895):
second, using `!foo` will include `foo` in the list of lemmas whose successful application qualifies as an overall success, even if we don't end up discharging all subgoals.

#### [Scott Morrison (Nov 27 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618030):
@**Simon Hudon**, do you know this one? How do I tell ahead of time how many goals `apply L` will create, if `L` is some expr? I want to count how many Pi binders there are, that aren't determined by the result type.

#### [Johan Commelin (Nov 27 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618035):
@**Scott Morrison|110087** This is really cool! I'm looking forward to having this in my toolkit :hammer:

#### [Scott Morrison (Nov 27 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618045):
Said another way, if you pretty-printed the type, some arguments would be shown as Pi's and some just as function arrows (because nothing later depends on that argument). I want to know the number that will appear as function arrows.

#### [Scott Morrison (Nov 27 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618052):
Mario said that this exists somewhere in `expr`, for the sake of pretty-printing, but I haven't been able to find it.

#### [Simon Hudon (Nov 27 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618121):
`is_arrow` will give you that information for the first pi type. If you want to count the arrows, you can do it like this:

#### [Simon Hudon (Nov 27 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618228):
```lean
meta def count_arrows : expr -> ℕ
| (expr.pi n bi d b) := 
   if b.has_var_idx 0 then count_arrows b
                      else 1 + count_arrows b
| _ := 0
```

#### [Simon Hudon (Nov 27 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618237):
You can modify this code to list their types but you'll need to take better care of bound variables.

#### [Scott Morrison (Nov 27 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618242):
I really just need the count for my application, so this is perfect.

#### [Simon Hudon (Nov 27 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618245):
:+1:

#### [Scott Morrison (Nov 27 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618307):
err... while you're here, do you know how to sort lists by the value of a function in Lean?

#### [Simon Hudon (Nov 27 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618308):
Please let me know if it works. I haven't used `has_var_idx` before and I'd like to make sure I used it properly

#### [Keeley Hoek (Nov 27 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618310):
Does that really work simon? Like what if `b` is another `expr.pi`, so that a `var 0` bound under this other `pi` changes the meaning of `var 0`
Does `has_var_idx` actually account for that? (I guess I should just read its implementation)

#### [Simon Hudon (Nov 27 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618370):
@**Keeley Hoek** I think so. The correct way of implementing it would be that every time you encounter a binder, instead of calling recursively `has_var_idx n` you call `has_var_idx $ n+1` so that when you use the function, you're actually looking for variables bound exactly where the call originated from.

#### [Keeley Hoek (Nov 27 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618378):
Actually, according to line 303 of src/library/vm/vm_expr.cpp is seems that `expr.has_var_idx _ 0` always returns false?

#### [Keeley Hoek (Nov 27 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618389):
sure makes sense

#### [Keeley Hoek (Nov 27 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618504):
From a little test I'm definitely wrong
But I totally don't understand why :D

#### [Keeley Hoek (Nov 27 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618510):
Oh `auto n` is a pointer, all g

#### [Simon Hudon (Nov 27 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618520):
@**Scott Morrison|110087** If you import `data.list.sort`, you can choose your sorting algorithm (say `merge_sort`) and you have to provide a relation. What you can do if you want to sort according to `f` is to use `inv_image (<) f` as the relation you're going to sort with.

#### [Simon Hudon (Nov 27 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618570):
@**Keeley Hoek** Thanks for looking into it. I'm reassured :)

#### [Keeley Hoek (Nov 27 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618638):
Note though that then you can't use `back` in the stuff which `data.list.sort` imports, which includes `tactic.interactive` and `algebra.group`. If anyone more confident could come up with some "official" names for an algorithm file and a proof file, I'll de-splice like mario suggested/claimed non-opposition-in-principle above

#### [Simon Hudon (Nov 27 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618777):
Is the issue that you're putting `back` in `tactic.interactive`?

#### [Keeley Hoek (Nov 27 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618830):
it's not an issue per-se
It's just that if you ever want to prove something with back in any of those files it includes
well
you can't

#### [Scott Morrison (Nov 27 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618831):
Oh, this is beautiful. `count_arrows` does exactly what I wanted (after I remembered to `infer_type` on the lemma .... duh!), and moreover sorting the lemmas by `count_arrows` has exactly the desired effect, and `back` is no longer distracted when you give it dumb lemmas (e.g. transitivity style lemmas).

#### [Keeley Hoek (Nov 27 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618833):
whooooooooooooooooooooooooooooooooooo

#### [Simon Hudon (Nov 27 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148618979):
@**Keeley Hoek** To reduce the size of the dependency, you can use `qsort` which is defined in core

#### [Keeley Hoek (Nov 27 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148619022):
Thanks simon I didn't know about that

#### [Scott Morrison (Nov 27 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148619080):
Oh, it turns out I need one little tweak to `count_arrows`. Since I automatically try applying `iff` statements in both directions, I need to add one if the statement ends with an `iff`.

#### [Mario Carneiro (Nov 27 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148619260):
how about `data.list.defs`?

#### [Simon Hudon (Nov 27 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148619410):
@**Scott Morrison|110087** Try

```lean
| `(%%a <-> %%b) := 2 + count_arrows a + count_arrows b
```

as an additional branch

#### [Scott Morrison (Nov 27 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148619417):
ooh, I'm not sure that's actually the counting I want.

#### [Scott Morrison (Nov 27 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148619466):
I think `1 + min (count_arrows a) (count_arrows b)` is actually what I need.

#### [Scott Morrison (Nov 27 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148619531):
In any case, thanks. I see that handling `iff`s requires a bit more work, but I'll have to pause for now.

#### [Simon Hudon (Nov 27 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148619591):
Good luck :) I've been meaning to look more closely at your project but I've been pretty absorbed by something else ... plus three other projects. In any case, don't hesitate to call on me if you need to.

#### [Johan Commelin (Nov 27 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148622890):
@**Scott Morrison|110087** Is back going to kill this goal for me?
```lean
⊢ X.left ⟶ X.left
```
I currently have
```lean
{ app := λ X, by {tidy, exact 𝟙 _, tidy, exact 𝟙 _, tidy, } },
```

#### [Scott Morrison (Nov 27 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148665760):
@**Johan Commelin**: If you tag `category.id` with `back` then `tidy` will kill this goal.

However this would be a bad idea. Better would be to define an attribute `[fyn]`, and tag `category.id`, `category.comp`, and a few other things with `[fyn]`, and then define ``meta def follow_your_nose : tactic unit := `[back [fyn]]``, and then `local attribute [tidy] follow_your_nose` will result in `tidy` being able to kill goals like this.

#### [Scott Morrison (Nov 28 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148678798):
I've now removed `apply_rules`, moving its test cases into the test cases for `back`.

My todo list is now:

- [ ] Decide if `solve_by_elim` should be subsumed by `back`; they are very close.
- [X] Switch to using `back [lemma] using [attr]` instead of `back [lemma, attr]`.
- [X] Add support for `back using [!attr]`.
- [ ] Can we use postfix `!` for lemmas, e.g. `back [attr!]` instead of the current `back [!attr]`?
- [ ] Add a mechanism to locally include an attribute in all calls to `back`, so we can write something like `local attribute [back] dvd`, where `dvd` is itself an attribute. (Not sure about the best implementation here.)

Any suggestions about the implementation of the last two points appreciated.

#### [Scott Morrison (Nov 28 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148741472):
Okay, `back` is getting more awesome. :-) How about this:
```
theorem infinitude_of_primes'' (N : ℕ) : ∃ p ≥ N, prime p :=
begin
  let M := fact N + 1,
  let p := min_fac M,
  use p,
  have pp : prime p, back,
  -- Goal is `∃ (H : p ≥ N), prime p`
  split; try { assumption },
  -- Goal is `p ≥ N`.
  by_contradiction h, simp at h,
  back,
end
```

#### [Scott Morrison (Nov 28 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148741603):
(That is, `back` successfully, and quickly, runs the whole "`p | fact N`, and `p | M` so `p | 1`, but that's nonsense" argument by itself.)

#### [Mario Carneiro (Nov 28 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148741618):
how is `back` performance looking at this point?

#### [Scott Morrison (Nov 28 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148741653):
And if you write `back?` there, it prints:
```
exact prime.not_dvd_one pp
  ((nat.dvd_add_iff_right (dvd_fact (prime.pos pp) (le_of_lt h)).mpr) 
     (min_fac_dvd M))
```

#### [Mario Carneiro (Nov 28 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148741680):
nice short proof there

#### [Scott Morrison (Nov 28 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148741809):
It seems fast to me. :-)
```
example {a b c d e : nat} (h1 : a ≤ b) (h2 : c ≤ d) (h3 : 0 ≤ e) :
a + c * e + a + c + 0 ≤ b + d * e + b + d + e :=
by back [add_le_add, mul_le_mul_of_nonneg_right]
```
takes 0.259s, producing the proof `add_le_add (add_le_add (add_le_add (add_le_add h1 (mul_le_mul_of_nonneg_right h2 h3)) h1 ) h2) h3`.
The proof above about primes takes 0.189s.

#### [Scott Morrison (Nov 28 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148741914):
I think the basic performance point here is: Leo made `apply` incredibly fast, and so if you don't do anything dumb with it, tactics based on it are fast.

#### [Mario Carneiro (Nov 28 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148741926):
I recall you mentioning that there were some known inefficiencies, are those fixed now?

#### [Scott Morrison (Nov 28 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148741964):
(And I should say, of course, `back` is really just tweaks and improvements on the already awesome `solve_by_elim`, by @**Simon Hudon**).

#### [Scott Morrison (Nov 28 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148741980):
Yes, the efficiency problems are gone. It's a complete rewrite.

#### [Scott Morrison (Nov 28 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148742097):
A big todo list item remaining is the decide whether to replace `solve_by_elim` with `back`. There are two reasons I don't want to do this immediately:
1) I'd have to check that `back` really is just as fast in all the applications in mathlib. (I suspect it is.)
2) There's a fair bit of code in `back`, and I'd prefer to get some review of it before going to the effort of making replacements. :-)

#### [Kevin Buzzard (Nov 28 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148742202):
What does `back` do? I know people talk about it but I have no idea what it is supposed to do.

#### [Scott Morrison (Nov 28 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148742207):
That proof of the infinitude of primes makes me wish for a few things:
1) `split` would try `assumption` on each propositional goal it produces (or perhaps even `back`!)

#### [Scott Morrison (Nov 28 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148742229):
2) `by_contradiction h` would automatically try `simp at h` afterwards?

#### [Kenny Lau (Nov 28 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148742296):
```quote
That proof of the infinitude of primes makes me wish for a few things:
1) `split` would try `assumption` on each propositional goal it produces (or perhaps even `back`!)
```
you can write a `split'` tactic that does that! :D

#### [Scott Morrison (Nov 28 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148742307):
3) For a tactic `have' p : Q`, which is just `have p : Q, back`, for some better name for `have'`. :-)

#### [Kenny Lau (Nov 28 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148742339):
```quote
2) `by_contradiction h` would automatically try `simp at h` afterwards?
```
 you can write `by_contradiction'`! :D

#### [Reid Barton (Nov 28 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148742351):
in the limit, our proofs will be entirely `'`s

#### [Scott Morrison (Nov 28 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148742606):
@**Kevin Buzzard**, to a first approximation, `back` is just `solve_by_elim`. It repeatedly `apply's hypotheses against the goal, succeeding if it discharges the goal.

#### [Scott Morrison (Nov 28 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148742718):
You can also pass it extra lemmas to use. You can also pass it attributes to use (so all lemmas with that attribute are applied). You can (soon) give it "hints", saying, for the rest of this file, always use all the lemmas marked with this attribute.

#### [Scott Morrison (Nov 28 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148742774):
You can also mark a lemma or hypothesis with `!` (as in `back [!foo]`, or `attribute [back!] foo`), and then `back` will act as an "interactive tactic" --- if it manages to apply a `!` lemma, it will return successfully even if it didn't complete every resulting subgoal.

#### [Kenny Lau (Nov 28 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148742850):
```lean
import tactic.interactive

namespace tactic.interactive
open lean.parser tactic interactive
meta def split' : tactic unit :=
`[split; try {assumption}]
end tactic.interactive

example {p q : Prop} {hp : p} : p ∧ q := by split'
example {p q : Prop} {hp : q} : p ∧ q := by split'
```

#### [Scott Morrison (Nov 28 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148742856):
It's also clever enough to accept `iff` lemmas. (Although the current implementation says: if you apply an iff lemma, never apply it again.)

#### [Kevin Buzzard (Nov 28 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148742863):
```quote
in the limit, our proofs will be entirely `'`s
```
 https://en.wikipedia.org/wiki/Iota_and_Jot

#### [Mario Carneiro (Nov 28 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148743562):
I vote `then` for `have, back`

#### [Reid Barton (Nov 28 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148743606):
can't wait for `thus`, `hence` and `therefore`

#### [Reid Barton (Nov 28 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148743728):
Actually I don't think you can use `then`

#### [Mario Carneiro (Nov 28 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148743738):
oh, if then?

#### [Reid Barton (Nov 28 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148743760):
Yeah, it's complaining about "invalid expression"

#### [Kevin Buzzard (Nov 28 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148743841):
`thither`

#### [Mario Carneiro (Nov 28 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148743895):
nope, it's fine

#### [Mario Carneiro (Nov 28 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148743904):
```lean
namespace tactic.interactive
meta def «then» := «have»
end tactic.interactive

example : true :=
begin
  then a : true := trivial,
end
```

#### [Mario Carneiro (Nov 28 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148743969):
you have to quote it since it's keywordish

#### [Mario Carneiro (Nov 28 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148743979):
`have` is also defined like this

#### [Mario Carneiro (Nov 28 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148744041):
although it's a bit weird that it shows up purple in the highlighting

#### [Kenny Lau (Nov 28 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148744085):
@**Mario Carneiro** how would you convert my `split; try {assumption}` to tactic notation?

#### [Mario Carneiro (Nov 28 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148744093):
?

#### [Kenny Lau (Nov 28 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148744104):
I wrote this:
```lean
meta def split' : tactic unit :=
`[split; try {assumption}]
```

#### [Kenny Lau (Nov 28 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148744123):
and I wonder how to write it using ... how do you call it

#### [Kenny Lau (Nov 28 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148744128):
monads and what not

#### [Kenny Lau (Nov 28 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148744152):
because once I `tactic.split` it's hard to keep track of the newly added goals

#### [Kenny Lau (Nov 28 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148744160):
I could get the goals before and after and just compare the length

#### [Kenny Lau (Nov 28 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148744175):
but I don't think that's very safe nor the best way to do it

#### [Mario Carneiro (Nov 28 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148744244):
a straight translation:
```lean
namespace tactic
meta def split' : tactic unit :=
(split >> return ()); try assumption
end tactic
```

#### [Kenny Lau (Nov 28 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148744267):
I have much to learn

#### [Mario Carneiro (Nov 28 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148744325):
the semicolon operator is `tactic.seq_focus`

#### [Mario Carneiro (Nov 28 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148744333):
you can see what it does for goal management

#### [Kenny Lau (Nov 28 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148744378):
I see that the unsafe option (actually it's safe, it just seems weird) is used

#### [Kenny Lau (Nov 28 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148744384):
well technically it is different

#### [Kenny Lau (Nov 28 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148744388):
I've learnt, thanks

#### [Mario Carneiro (Nov 28 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148744393):
unsafe?

#### [Kenny Lau (Nov 28 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148744406):
I don't feel very comfortable messing with the goals

#### [Mario Carneiro (Nov 28 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148744440):
you can often just get away with using the built in tactic combinators like `and_then` if it suffices

#### [Johan Commelin (Nov 29 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148767152):
@**Scott Morrison|110087** So we can now also do the following?
```lean
theorem infinitude_of_primes'' (N : ℕ) : ∃ p ≥ N, prime p :=
by use min_fac (fact N + 1); tidy
```
Or will `tidy` not (yet) try the proof by contradiction? If we want to golf this proof, I suggest we introduce `N!` notation for factorials :rolling_on_the_floor_laughing:

#### [Scott Morrison (Nov 29 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148767171):
One thing to remember is that part of the philosophy of `tidy` is that it does no backtracking. So if we wanted to add `by_contradiction` to tidy, it would be because we're committing to "when all else fails, actually go ahead and try contradiction (returning to the user the goals produced by `by_contradiction`", which I don't think is a good idea.

#### [Johan Commelin (Nov 29 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148767280):
Right... so we need a bigger hammer (-;
Is it possible to write something like `tidy [by_contradiction]` so that `tidy` knows it can use that tactic for this proof?

#### [Scott Morrison (Nov 29 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148767291):
It's a reasonable idea. So far `tidy` doesn't take many configuration arguments.

#### [Keeley Hoek (Nov 29 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148767651):
Wouldn't `tidy { tactics := [by_contradiction >> return "by_contradiction"] }` work

#### [Scott Morrison (Nov 29 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148767905):
Oh, hmm, yeah :-)

#### [Johan Commelin (Nov 29 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148773132):
```quote
Wouldn't `tidy { tactics := [by_contradiction >> return "by_contradiction"] }` work
```
 Cool! So the functionality is there. Now we only need to make it a bit more user-friendly. I guess the `>> return "by_contradiction"` is needed for the trace output, right? How hard is it to write a function that takes a `tactic` and stringifies its name?

#### [Keeley Hoek (Nov 29 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148777157):
Well, Scott, if we use the fancy configurator then we could parse `tactic unit`s and `tactic strings` at the same time ;)
But there is the dreaded `{}` requirement.
Maybe an extra character? `tidy` or `tidy@{ my_config }`? I suspect this won't be approved :P

Unfortunately, Johan, the only way to obtain the name of a tactic you are passing is to use a `parser`, which is some work to set up the most convenient way.

#### [Mario Carneiro (Nov 29 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148777208):
what about `tidy with [stuff]`?

#### [Mario Carneiro (Nov 29 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/148777280):
Rather than trying to guess the tactic script, you should just have some additional tidy tactics that are enabled explicitly via some tags

#### [Johan Commelin (Dec 05 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150909827):
@**Scott Morrison|110087** What is the status of this PR? I got the impression you made quite some nice improvements. Do you have more up your sleeve?

#### [Scott Morrison (Dec 05 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150910787):
It's a bit rough, but could be made usable with not much effort. However, I'd also like to put in a larger amount of effort, to make it better. :-)

#### [Scott Morrison (Dec 05 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150910852):
Essentially, at the moment it does a depth-first search of possible uses of `apply` (with a simple heuristic to order the branches, and one or two rules for cutting off the search). I'd really like to restructure the core code a bit, to make the type of search configurable, as once you make "too many" rules available to `back` the depth first search starts being too dumb.

#### [Scott Morrison (Dec 05 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150910861):
I'd really like to have it more robust to having "too many" rules, so that it's possible to just set and forget large groups of rules, and still have `back` performant enough.

#### [Scott Morrison (Dec 05 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150910916):
Given `back?` produces proof terms that you can copy and paste, it's potentially a good hammer.

#### [Patrick Massot (Dec 05 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150913149):
I have a question about this PR. How is it related to the core library [back_chaining tactic](https://github.com/leanprover/lean/blob/master/library/init/meta/backward.lean)?

#### [Patrick Massot (Dec 05 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150913185):
And, since @**Sebastian Ullrich** is here: what is the status of this tactic? What is only a tech demo, or is it meant to be ready for use? I discovered it while reading demo slides (POPL 2017)

#### [Sebastian Ullrich (Dec 05 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150913344):
I suppose it's just as ready to use as `rcases`. Which you people probably have more experience with and opinions about than me.

#### [Patrick Massot (Dec 05 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150913352):
Is it possible to use custom tags, or does it have to be `intro`?

#### [Patrick Massot (Dec 05 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150913402):
It looks like only two things are tagged with `intro` in core+mathlib

#### [Patrick Massot (Dec 05 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150913412):
but still we could want several sets of lemmas depending on the kind of statement we'd like to prove

#### [Scott Morrison (Dec 05 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150913533):
That's a great question, Patrick. It looks closely related (and both to solve_by_elim). This one is implemented in C, and does two extra things --- allows you to specify a "simp" tactic to apply at each step, and allows you to specify a "leaf" tactic to apply once you run out of lemmas but haven't closed the goal.

#### [Scott Morrison (Dec 05 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150913577):
It doesn't seem to give you that much control over which lemmas to use (i.e. just the one attribute [intro])

#### [Scott Morrison (Dec 05 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150913604):
and `back` additionally gives you the idea of "progress" lemmas, i.e. lemmas whose successful application will result in the tactic being considered a success, even if it doesn't finish the proof. I've found this very useful in practice (and as part of `tidy`).

#### [Scott Morrison (Dec 05 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150913611):
(I had no idea this one existed!)

#### [Patrick Massot (Dec 05 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150913948):
I found it yesterday!

#### [Patrick Massot (Dec 05 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150917059):
I have a riddle now. Download https://github.com/leanprover/lean/blob/master/library/init/meta/backward.lean It works. Now add `import data.multiset` on top. It doesn't work anymore.

#### [Johannes Hölzl (Dec 05 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150917106):
`backward.lean` is in `init` so it will be loaded automatically. `data.multiset` will import it.

#### [Johannes Hölzl (Dec 05 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150917161):
`prelude` means to _not_ load `init`

#### [Patrick Massot (Dec 05 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150918133):
Oops, I copied the wrong link. I meant https://github.com/leanprover/presentations/blob/master/20170116_POPL/backchain/builtin.lean

#### [Patrick Massot (Dec 05 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150918141):
I'm sorry about this confusion

#### [Patrick Massot (Dec 05 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150927154):
Mario, did you try this little puzzle? Were you aware of `back_chaining`?

#### [Mario Carneiro (Dec 05 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150927485):
as I thought, it's a notation ambiguity problem

#### [Mario Carneiro (Dec 05 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150927577):
`in_tail` and `in_head` break because the `::` is overloaded notation that means `multiset.cons` and `list.cons`

#### [Mario Carneiro (Dec 05 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150927611):
In this case you can fix it by putting a type ascription around `a::l`

#### [Patrick Massot (Dec 05 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150927729):
Thanks. Are you sure this notation overloading was a good idea?

#### [Mario Carneiro (Dec 05 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150928365):
no, it's avoided almost everywhere because lean is flaky about it

#### [Mario Carneiro (Dec 05 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150928445):
but in this case `::` is already overloaded in core so there isn't much we can do about it

#### [Patrick Massot (Dec 05 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23410%20backwards%20reasoning/near/150928495):
Sorry, I didn't realize this was in core

