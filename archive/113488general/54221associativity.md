---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54221associativity.html
---

## Stream: [general](index.html)
### Topic: [associativity](54221associativity.html)

---

#### [Simon Hudon (Jul 30 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130552015):
I'm writing a tactic about associativity and I'm inferring the associativity of the operators that appear in an expression. It turns out that this is the bottleneck of my script: building an instance of `is_associative` takes hundreds of ms. Is there a faster way to do it?

#### [Kevin Buzzard (Jul 30 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130563174):
I hardly ever understand your questions Simon (too CS!), but I'd like to begin to try. Do you mean "type class inference is taking a long time checking that my random operation is associative"? You know better than I do that you can just make your own instance and add it to the type class inference system. It occurs to me that in contrast to `simp`, where I can look at traces, I don't really know how to look at what type class inference is doing. I don't want to derail this thread though.

#### [Patrick Massot (Jul 30 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130564572):
Of course you know it: `set_option trace.class_instances true`

#### [Patrick Massot (Jul 30 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130564575):
But you only think of it when things go wrong

#### [Simon Hudon (Jul 30 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130581550):
@**Kevin Buzzard** That's exactly it. It's not clear to me that adding instances would improve the situation

#### [Reid Barton (Jul 30 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130581859):
Are you trying to infer the associativity of some operations which don't have `is_associative` instances? If so, could you give an example?

#### [Reid Barton (Jul 30 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130581922):
Or is it instance lookup itself that takes a long time?

#### [Simon Hudon (Jul 30 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130583646):
Instance lookup is taking a really long lime. My work around right now is, the first time I need that information, I add it to the local assumptions and I keep looking at assumptions to see if it's there before calling `mk_instance`.

#### [Simon Hudon (Jul 30 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130583738):
The other idea I'm considering is to have an internal table where I cache that kind of information. That could be faster still and less intrusive but I would redo the instance inference at least once per call to the overall tactic (which I call `assoc_rewrite`)

#### [Reid Barton (Jul 30 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130583854):
Whoa, `assoc_rewrite`! I need this more than you can possibly imagine.
How hard do you think it would be to make this work with category-style associativity, where the composition operator is indexed on the source and target types? I haven't looked at the implementation yet. I can probably rig up a representative example at some point if that would be helpful.

#### [Reid Barton (Jul 30 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130583893):
I imagine it could involve internally needing a "thrist" rather than just a list, though maybe you can just ignore the type indices.

#### [Reid Barton (Jul 30 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130584175):
Checking that a diagram in a category commutes usually comes down to these alternately reassociating and then rewriting arguments and when there are more than three morphisms involved it's a real pain to specify the reassociation you want.

#### [Simon Hudon (Jul 30 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130584182):
That is very good to know! I can consider categories. I don't think it would be too hard. Given a categorical composition operator, is there an analogue to `is_associative` to get me the associativity law?

#### [Reid Barton (Jul 30 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130584248):
It's just a constant--a class method of `category` (`category.associativity`)

#### [Simon Hudon (Jul 30 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130584291):
Cool :) can you give me a proof example? I'll see if I can add it to my PR

#### [Reid Barton (Jul 30 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130584408):
That is, my compositions are already written syntactically in terms of the fixed composition operator `category.compose`.

#### [Reid Barton (Jul 30 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130584418):
Well, hmm. It might be a bit tricky, since categories are not in mathlib yet.

#### [Reid Barton (Jul 30 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130584559):
I guess I'll give you a self-contained example, including the `category` class, for starters.

#### [Simon Hudon (Jul 30 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130584560):
Yeah, that's tricky. Are you working on a branch of mathlib? If so I could make a version for that. Alternatively, I could make a `associativity` attribute that you can put on that associativity law.

#### [Simon Hudon (Jul 30 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130584575):
That's a good start.

#### [Reid Barton (Jul 30 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130585073):
Here is a simple, but very common sort of example: https://gist.github.com/rwbarton/b10c0229be25bd6880661afb2f1b32f5

#### [Reid Barton (Jul 30 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130585145):
An `associativity` attribute would be a good solution for me.

#### [Simon Hudon (Jul 30 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130585592):
Cool! Thanks! With the associativity attribute, it would probably be enough to put it on the associativity law from `semigroup` and `add_semigroup` and `semi_lattice`, what do you think?

#### [Simon Hudon (Jul 30 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130585718):
From an aesthetic perspective, if you use `x*y = a*b` to rewrite `p * x * y * q`, do you prefer the tactic to leave the expression flat (i.e. `p * a * b * q`) or manipulated only minimally after rewrite (i.e. `p * (a * b) * q`)?

#### [Reid Barton (Jul 30 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130585914):
If using an attribute is faster than instance lookup then that sounds like a good approach, since users can mark their own operations with the attribute anyways. I doubt we need the Prolog-style search power here. (I'm also wondering why instance synthesis is so slow, though.)

#### [Reid Barton (Jul 30 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130585956):
Good question. Probably I can answer it better after trying it out in a few dozen proofs :slight_smile:

#### [Simon Hudon (Jul 30 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586040):
What I'm suspecting that there are some dead alleys in the set of instances. Maybe I should start tracing the instance search process

#### [Reid Barton (Jul 30 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586042):
I think it usually won't matter for me, since I'd probably follow it with either more `assoc_rw`s or `simp`, which applies `associativity` everywhere anyways.

#### [Simon Hudon (Jul 30 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586094):
If you follow with `simp`, it might be more effective to flatten the expression so that `simp` doesn't waste time flattening it one associativity at a time.

#### [Reid Barton (Jul 30 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586197):
BTW, when do I get `assoc_simp`? :)

#### [Simon Hudon (Jul 30 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586278):
On Christmas if you've been a good boy ;-)

#### [Simon Hudon (Jul 30 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586328):
Actually, I'd like to tackle `simp` as well but it seems like a bigger project.

#### [Simon Hudon (Jul 30 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586349):
I'll keep you posted

#### [Reid Barton (Jul 30 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586357):
I have a way to deal with associativity in `simp` to some degree already, so it's not so bad. Actually it's stolen from @**Scott Morrison**'s idea here: https://github.com/semorrison/lean-category-theory-pr/blob/lean-3.4.1/src/categories/isomorphism.lean#L34

#### [Reid Barton (Jul 30 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586402):
The general form is: if you have a `@[simp]` lemma which states that `a * b = c * d * e`, first generalize it to the form `z * (a * b) = z * (c * d * e)`, and then reassociate the parentheses on the left side (there can be more than two original factors).

#### [Reid Barton (Jul 30 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586465):
Make that another simp lemma. Then you have a left-hand side of the form `(z * a) * b = ...` where `z` can be anything. So it will match any left-nested tree in which `a` and `b` appear "consecutively".

#### [Reid Barton (Jul 30 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586492):
(You can reassociate the parentheses on the right-hand side too, so that `simp` doesn't have to do it every time you apply the lemma.)

#### [Reid Barton (Jul 30 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586662):
This is like a Knuth-Bendix completion step: we could simplify `z * (a * b)` to either `z * (c * d * e)` or `(z * a) * b`, so add another rewrite rule to make those confluent.

#### [Reid Barton (Jul 30 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586765):
So one wishlist item is an tactic/attribute to put on a simp lemma which will apply this transformation and make a new simp lemma.

#### [Reid Barton (Jul 30 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586779):
I've done this by hand in a few cases, and it simplified some proofs.

#### [Reid Barton (Jul 30 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586917):
But this is not by itself sufficient to deal with situations where we want to use hypotheses, rather than simp lemmas, like the equation `e` in my example earlier. That's why I still want `assoc_rw` for this situation. (Maybe an alternative is to generate a transformed version of the hypotheses, but I might also want to rewrite using equations tucked away inside fields of structures and things like that.)

#### [Simon Hudon (Jul 30 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130586920):
Ah I see! So `assoc_simp` would be better still I assume because then you wouldn't need to duplicate so many lemmas

#### [Reid Barton (Jul 30 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130587032):
Right, I mean in general `rw` and `simp` are distinct, but overlapping in their uses, so both `assoc_rw` and `assoc_simp` ought to be useful as well.

#### [Reid Barton (Jul 30 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130587101):
Maybe `assoc_simp` with arguments could apply this transformation to those arguments, as well as all simp lemmas

#### [Simon Hudon (Jul 30 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130587366):
I was thinking of rewriting the `simp` tactic and changing the rewriting function so that it matches modulo associativity.

#### [Reid Barton (Jul 30 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130587508):
Ah, I see. Sounds more ambitious, but probably more powerful as well.
Is `simp` in Lean? Maybe worth waiting for Lean 4?

#### [Simon Hudon (Jul 30 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130587539):
Where it gets tricky I find is when you have a lemma `forall x, x * y = foo`, you may instantiate `x` with `a * b` which is harder for my current matching to consider.

#### [Simon Hudon (Jul 30 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130587627):
```quote
Ah, I see. Sounds more ambitious, but probably more powerful as well.
Is `simp` in Lean? Maybe worth waiting for Lean 4?
```
It might be. In any case, maybe I should first roll out `assoc_rw` and wait for feedback before getting started on `assoc_simp`

#### [Simon Hudon (Jul 30 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130589220):
I think the category theory development looks beautiful, by the way. I wish I understood more of it

#### [Scott Morrison (Jul 31 2018 at 04:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130616056):
On the subject of associativity, there is something I would like to work on soon, but that I think it still orthogonal to `rw_assoc` and `simp_assoc`.

#### [Scott Morrison (Jul 31 2018 at 04:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130616067):
When working with monoidal categories, very often one has to insert associators (which are isomorphisms, not equations!) in order to be able to compose.

#### [Scott Morrison (Jul 31 2018 at 04:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130616356):
For example, if I have `f : A -> (B ⊗ C) ⊗ D` and `g : B ⊗ (C ⊗ D) -> E`, of course `f  ≫ g` doesn't typecheck.

#### [Scott Morrison (Jul 31 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130616450):
I would like to define some extra notation, e.g. `f ⊗≫ g`, which would invoke a tactic that inspects the target of `f` and the source of `g`, and decides if they are isomorphic via associator isomorphisms (probably also via identity isomorphisms, absorbing the monoidal unit on either side), and if so contructs that isomorphism `α` and returns `f ≫ α ≫ g `.

#### [Scott Morrison (Jul 31 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130616499):
(By the axioms for monoidal categories, it doesn't matter _which_ associator isomorphism we use, as they are all equal.)

#### [Simon Hudon (Jul 31 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130619435):
should there be an arrow in the type of `g`?

#### [Simon Hudon (Jul 31 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130619565):
I think I see where you're going for. Similar logic to my `assoc_rw` tactic can be used to construct `α`

#### [Simon Hudon (Jul 31 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620191):
@**Reid Barton** applying `assoc_rw` to categories is more complicated than I thought. It might be that I should just write a `cat_rw` specifically for categories. Is there any other context in which such a tactic would be useful or would it make sense to just refer to composition from `category`?

#### [Mario Carneiro (Jul 31 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620280):
a semigroupoid? :D

#### [Simon Hudon (Jul 31 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620518):
:) Shouldn't that be an ancestor of category?

#### [Simon Hudon (Jul 31 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620524):
I could hard-code semigroupoid composition instead of category composition, no?

#### [Scott Morrison (Jul 31 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620591):
I've heard the word `semicategory`, and there's actually some natural reasons to study them.

#### [Scott Morrison (Jul 31 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620598):
(Idempotent completion takes semicategories to categories, and in a certain sense is adjoint to the functor which forgets identities)

#### [Simon Hudon (Jul 31 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620696):
Would it be worth introducing a `has_comp` type class?

#### [Simon Hudon (Jul 31 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620815):
(I assume semicategories have an associative composition)

#### [Mario Carneiro (Jul 31 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620826):
I'm joking. I prefer to introduce concepts when they become useful and not before

#### [Mario Carneiro (Jul 31 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620866):
it's not hard to retrofit them if some time in the future we see a genuine semigroupoid which is not a category

#### [Simon Hudon (Jul 31 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620877):
Fair enough :) my sense of usefulness for category theory still needs sharpening

#### [Simon Hudon (Jul 31 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130620944):
While we wait for the category theory stuff to be merged, would it be worth it to add `has_comp` to mathlib if I can use it in `assoc_rw`? That might facilitate the development of the category theory proofs.

#### [Mario Carneiro (Jul 31 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130621378):
that sounds like it would be tied to a notation, but probably `assoc_rw` will need to be usable with at least a few notations, in particular `+`, `*`, and `o`

#### [Simon Hudon (Jul 31 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130621439):
What I'm thinking is for operators with simpler types (e.g. `+`, `*`) I can rely on `is_associative` and then make a special case for categorical composition. The matching is a bit different anyway

#### [Mario Carneiro (Jul 31 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130622261):
that sounds reasonable. I doubt categorical composition will use any other notation than whatever Scott is setting up

#### [Patrick Massot (Jul 31 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130633467):
I also have something like Scott's associators everywhere in my group completion work. For every uniform space `a`, I have a complete Hausdorff `completion a` and a map from `a` to `completion a`, and every uniformly continuous map from `a` to `b` lifts to a map between completions. This is all fun. The trouble comes when product spaces are involved. I have an isomorphism from `completion (a × b)` to`completion a × completion  b`, but I need to insert it and its inverse at a lot of places.

#### [Reid Barton (Jul 31 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130654032):
```quote
Would it be worth introducing a `has_comp` type class?
```
Hmm, I wonder if moving `∘` to notation for a `has_comp` class would be viable, with an instance for `function.comp`... though I guess that is all in core Lean, so not viable at the moment.

#### [Kevin Buzzard (Jul 31 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130654630):
Although this is even less under our control, is the correct long-term solution really to try and rethink how the actual type class system works? Or is the type class system some sort of standard machine which clearly will never change and we have to figure out how to work around it?

#### [Johannes Hölzl (Jul 31 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130662971):
The mechanism will not change, at least there are no public plans for Lean 4 to change the type class mechanism. What will change, is the type class hierarchy. One thing is to move properties like commutativity, or `zero_ne_one` to be type class *mixins*, i.e. predicates over other type classes. `[comm_ring A]` will become `[ring A] [is_commutative A (*)]` (or similar). Also the lower type classes in the hierarcht like semigroups, monoid, etc, will be parameterized in their operators. This could eliminate parts of the additive / multiplicative split of the type class hierarchy.

#### [Johan Commelin (Aug 01 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130704179):
Concerning Lean 4: in what time scales should I think about the release? 3 weeks, 3 months, 3 years, 3 decades? Is there any hope/expectation/statement about this?

#### [Kevin Buzzard (Aug 01 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130704197):
"Not before the end of 2018" said Leo in Oxford IIRC

#### [Kevin Buzzard (Aug 01 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130704200):
Maybe some of my students with better memories than me can confirm this

#### [Johan Commelin (Aug 01 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130704286):
Ok. I didn't know anything at all. So if people said we would have to wait till at least 2025, I wouldn't have been surprised either.

#### [Reid Barton (Aug 01 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130731512):
@**Simon Hudon** was there a question here left over from yesterday?
There isn't currently anything which generalizes `category.compose` nor any concrete plans to add such a thing.
I assume it would be easy to change `assoc_rw` later if this changes, anyways.

#### [Reid Barton (Aug 01 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130731684):
By the way how do you feel about the name `rw_assoc` (and potentially `simp_assoc`) instead? Potentially more discoverable by autocompletion, for one

#### [Simon Hudon (Aug 01 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130733107):
Yes you're right. The other thing that such a generalization helps with is separating the category code  from the code of `assoc_rw`

#### [Simon Hudon (Aug 01 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/associativity/near/130733213):
I chose `assoc_rw` to conform with `ac_refl`. I think I could be convinced in favor of `rw_assoc`

