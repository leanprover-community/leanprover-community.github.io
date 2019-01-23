---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/02913yoneda.html
---

## Stream: [maths](index.html)
### Topic: [yoneda](02913yoneda.html)

---

#### [Johan Commelin (Oct 18 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136033284):
@**Scott Morrison|110524** Is there a reason why `yoneda` takes the category as explicit argument? Now we have to write `yoneda C X` instead of just `yoneda X`.

#### [Scott Morrison (Oct 18 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136047539):
Try it: you still wouldn't be able to write `yoneda X`. The problem is that `yoneda C X` has a coercion, converting it to `(yoneda C).obj X`, and the coercion mechanism isn't clever enough to handle `yoneda X` by filling in `C` as an implicit argument before using the coercion.

#### [Reid Barton (Oct 18 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136047790):
I guess `yoneda.obj X` would work then, if the category argument was implicit?

#### [Reid Barton (Oct 18 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136047957):
This coercion stuff has turned out to be a lot more frustrating than expected--it's lovely when it works but Lean's reluctance to use coercions in the presence of metavariables means that they're often a lot more awkward than just writing `F.obj X`, but then you have the burden of supporting both `F X` and `F.obj X` which are different expressions.

#### [Johan Commelin (Oct 18 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136047972):
*"and the coercion mechanism isn't clever enough"* :sad:

#### [Johan Commelin (Oct 18 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136047999):
I guess this is why Scott didn't use any coercions a couple of months ago...

#### [Reid Barton (Oct 18 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048072):
If `F X` and `F.obj X` were the same expression, one could forgive the elaborator for being picky about where it is willing to insert a coercion

#### [Reid Barton (Oct 18 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048215):
I think this thing with `yoneda C` is the same issue I ran into whenever I had to deal with cylinders in my homotopy theory library. There I had a functor $$I : C \to C$$ which was attached to $$C$$ by a type class, but I think that detail doesn't matter.

#### [Johan Commelin (Oct 18 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048220):
Could we choose a fancy bracket that looks like `(` and `)`, and turn that into notation for `has_apply`?

#### [Reid Barton (Oct 18 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048261):
And then I also had natural transformations $$i_0$$, $$i_1 : \mathrm{id} \to I$$, $$p : I \to \mathrm{id}$$, $$v : I \to I$$, all of which had the same issue...

#### [Johan Commelin (Oct 18 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048366):
I think wouldn't mind write `F(X)` with some fancy `()`. But maybe this is abusing notation and type classes too much.

#### [Johan Commelin (Oct 18 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048387):
I think this could then replace `coe_to_fun`.

#### [Reid Barton (Oct 18 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048509):
It's not clear to me that we would not just end up back in the same situation

#### [Reid Barton (Oct 18 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048567):
We would still have two things, `F.obj X` and `apply F X`. I guess the question is whether we could avoid ever having to write `F.obj X`. But it would be so much simpler if there was just one thing in the first place.

#### [Johan Commelin (Oct 18 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048684):
`apply F X` would be `F.obj X` by definition.

#### [Reid Barton (Oct 18 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048696):
It's possible if I had built my homotopy theory library on top of a category theory version with coercions from the start, I could have found a more convenient way to set things up

#### [Reid Barton (Oct 18 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048781):
But "by definition" is not good enough for `simp`, `rw` etc.

#### [Reid Barton (Oct 18 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048801):
I had a hard time porting a lot of proofs over the transition to use coercions in category theory

#### [Reid Barton (Oct 18 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048815):
because I had to be careful about the difference between `F X` and `F.obj X`

#### [Reid Barton (Oct 18 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048831):
If I could actually write `F X` consistently then that might be okay, but I couldn't because of the issues with coercions and metavariables

#### [Reid Barton (Oct 18 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048875):
In the end I think I wrote some explicit type ascriptions in the statements of the simp lemmas I had defined, so that they could work on the `F X` version

#### [Scott Morrison (Oct 18 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048943):
If we can agree that the coercion mechanism is broken, I would very happily rip them back out of the `category_theory/`.

#### [Reid Barton (Oct 18 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048952):
For example https://github.com/rwbarton/lean-homotopy-theory/commit/e98dd6f51cd46653bf30c610e60573318443466c#diff-6931c0d6d9d8dda133a6b3ed34b290d5L548

#### [Scott Morrison (Oct 18 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048993):
The saving of not having to write `.obj` most of the time is far outweighed by the confusion of sometimes mysteriously having to do so.

#### [Reid Barton (Oct 18 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049015):
https://github.com/rwbarton/lean-homotopy-theory/commit/e98dd6f51cd46653bf30c610e60573318443466c#diff-f49cdebfeaf5ac27e5bea99a12ad4ca9L129 -- sometimes I needed to help Lean out with the types and other times I didn't; it was hard to predict

#### [Scott Morrison (Oct 18 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049175):
There's also the issue of why `category_theory/` requires so much use of `erw` rather than `rw`. This stinks, and I don't have a clear idea of why it happens, but fear that coercions are sometimes to blame.

#### [Reid Barton (Oct 18 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049245):
I changed a bunch of `rw` to `erw` in that commit too, precisely because of the coercion thing. But there are some other situations where you need `erw` as well.

#### [Scott Morrison (Oct 18 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049299):
Do you think you can explain any of the others? I unfortunately just try `erw` and get on with it, and haven't invested the time in seeing what was going wrong.

#### [Reid Barton (Oct 18 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049412):
I suspect that most of my cases are because I still use the explicit version (`nat_trans.app` in this case) in my definitions: https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/homotopy_theory/formal/cylinder/homotopy.lean#L17
and I frequently want to rewrite using the conditions Hi\0, Hi\1

#### [Reid Barton (Oct 18 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049503):
It was quite unclear to me at first whether the easiest way forward was to use coercions everywhere or to use coercions nowhere or something in between

#### [Reid Barton (Oct 18 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049546):
Oh you mean the other situations, not related to coercions.

#### [Reid Barton (Oct 18 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049640):
I think for me they come from things like: $$i_0$$ is a natural transformation $$\mathrm{id} \to I$$. So the naturality law for $$i_0$$ contains stuff like `(functor.id C) X` in the types and I need it to be `X` to continue with a subsequent rewrite, and that's why I need `erw`.

#### [Reid Barton (Oct 18 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049645):
I don't remember more details off-hand, sorry

#### [Reid Barton (Oct 18 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049665):
But I know that at least some cases had to do with this specific issue of applying the identity functor

#### [Reid Barton (Oct 18 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049757):
Like I might want to rewrite using associativity where I have three maps `A -> B`, `B -> X`, `(functor.id C) X -> (functor.id C) Y`

#### [Reid Barton (Oct 18 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049770):
and then `rw` says "nope"

#### [Reid Barton (Oct 18 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049818):
I guess my suggestion might be to rip out coercions for now and then suggest as a wishlist item for :four_leaf_clover: to replace `has_coe_to_fun` by what I was calling in Orsay "type-indexed notation"

#### [Mario Carneiro (Oct 18 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049869):
what is that?

#### [Reid Barton (Oct 18 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049899):
The idea is if `F X` was actually **notation** for `F.obj X` then coercion and non-coercion syntax could all live happily forever.

#### [Reid Barton (Oct 18 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049909):
Currently, when Lean tries to elaborate `F X` it sees that the type of `F` is not a Pi type and then it maybe inserts a coercion

#### [Reid Barton (Oct 18 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049921):
So I presume this involves reducing the type of `F` to WHNF at least?

#### [Reid Barton (Oct 18 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049969):
Then the idea is, allow the user to specify another interpretation of `F X` as *notation* which depends on the head of the type of `F`, or something like that.

#### [Reid Barton (Oct 18 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136050000):
rather than the rule being "if the type of `F` is a Pi type then produce an application `F X`, otherwise produce `coe_fun_t F X`" or whatever it is today

#### [Reid Barton (Oct 18 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136050010):
give the user the chance to add additional rules "if the type of `F` looks like [...], then produce [...]"

#### [Reid Barton (Oct 18 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136050092):
In this case, `functor.obj F X`

#### [Reid Barton (Oct 18 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136050430):
By the way, the `equiv` coercion to fun is another one which has given me a lot of problems, which again is annoying because there are simp rules written in terms of the coercion like `e.symm (e x) = x`

#### [Reid Barton (Oct 18 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136050577):
I guess the usability of these coercions depends upon the usage patterns. Once the `equiv`s you are working with are not ones which were passed as arguments to your lemma, but things like the equivalence Hom(FX, Y) = Hom(X, GY) induced by an adjunction, then I guess more of these metavariables crop up

#### [Mario Carneiro (Oct 18 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136050684):
I think this can be solved by a simp lemma like `e.to_fun = \u e` and `e.inv_fun = \u e.symm`

#### [Reid Barton (Oct 18 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136050894):
Yes, probably; then the next problem is that I might want to define my own simp lemmas whose statements involve applying equivs as functions

#### [Reid Barton (Oct 18 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136050915):
and then I don't know how to write the statement of the lemma in simp normal form except by writing some bulky type ascriptions

#### [Mario Carneiro (Oct 18 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136050937):
I have found that coercions between different function(like) types is a bad idea for this reason

#### [Reid Barton (Oct 18 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136051838):
By the way, when bumping dependencies of your project across a substantial change, I can highly recommend having a separate checkout of the project built against the old version of the deps so that you can figure out how the heck any of your proofs used to work :smile:

#### [Mario Carneiro (Oct 18 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136052379):
ah, that brings me back to metamath days

#### [Johan Commelin (Oct 19 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136105758):
On the topic of coercions in category theory: would it make sense to use coercions to turn specialised shapes (like `fork` and `square` and `fan`) into the general shape `cone`? Of course we should also prove that have limits means having equalizers, pullbacks, products, etc... Then we might be able to prove a lot of stuff about general limits and use those results on specialised shapes. Or is this wishful thinking?

#### [Johan Commelin (Oct 19 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136106147):
@**Reid Barton** I really like your idea about type indexed notation! Because then we could also have very clean notation for applying a functor to a morphism.

#### [Reid Barton (Oct 19 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136108963):
Yes, I was just thinking of that as well--it would be nice to have both `F X` for `F.obj X` and `F f` for `F.map f`. I'm not sure that comes for free with the exact setup I had in mind, where the interpretation of juxtaposition depends only on the type of `F`, but maybe some slightly different design could handle it.

#### [Reid Barton (Oct 19 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136109281):
I think we may indeed want to arrange things so that equalizers and so on are actually defined as special cases of limits, and then wrap that in a nicer interface (which doesn't involve manually constructing a diagram/functor). The body of facts we have about limits is just going to keep increasing, and duplicating the results for each special shape of limit doesn't make sense.

#### [Johan Commelin (Oct 19 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136110360):
You say "actually defined as". Do you mean defeq? I was suggesting a coercion. But maybe that is not good enough.

#### [Johan Commelin (Oct 19 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136110402):
I do think that these are issues that should be sorted out soon. Because otherwise the refactoring will become a big pain if there is already too much code depending on the current setup.

#### [Johan Commelin (Oct 19 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136112654):
@**Reid Barton** I suppose the parser could also look at the "token" just following `F` to see whether it is an object or a hom. (And I assume the parser is smart enough to guess the right "token".)

#### [Reid Barton (Oct 19 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136112698):
I meant defeq but I haven't thought that much about what exact condition we would want.
Here is an example statement: if I have a limit cone in a diagram category then evaluation on any object yields a limit cone. Now we want the same statement for equalizers. If equalizers are defeq to a special case of limits, then we just apply the original statement. If equalizers are only `equiv` to a special shape of limit, then we need to transport across the equiv on both sides.

#### [Johan Commelin (Oct 19 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136112828):
So all the current machinery should be replaced by constructors yielding a nice API?

#### [Johan Commelin (Oct 19 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136112977):
It's really weird that these definitions are so non-trivial. Why are we so good at unifying concepts, and why can't we teach that trick to a computer?

#### [Scott Morrison (Oct 19 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136120823):
I’d love to be able to do something like this, but at the moment I really don’t see a good option. We can work on constructing diagrams (with some help from tactics) more easily. As an example, if `X Y : C`, and `f g : X \hom Y`, there’s no reason why `construct_diagram [f,g]` couldn’t return a `\Sigma (J : Type) [category J], J \func C`, automatically deciding the index category J should be the walking parallel pair.

#### [Scott Morrison (Oct 19 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136120919):
If this becomes easy enough, it becomes plausible to start defining “special” limits in terms of general ones. But without a huge improvement in this direction, it’s way too painful to expect a user to talk about equalizers as (defeq) special cases of limits. Just see the hoops I had to jump through to prove that having limits implies having equalizers...

#### [Scott Morrison (Oct 19 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136121056):
Also, @**Johan Commelin**, I’m not sure if you saw it already, but there’s a second pull request (from the `limits-constructions` branch) that constructs products and equalizers from limits, etc.

#### [Johan Commelin (Oct 19 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136121069):
I haven't yet looked in detail.

#### [Johan Commelin (Oct 19 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136121484):
I really hope that I will be able to write down a definition of `sieve` without `@`s. I must say that my experience with your library has been very positive. Writing things down is really pain-free and automation takes care of a lot of troubles.
Do you have a general guideline for when to add an auto_param in a definition?

#### [Reid Barton (Oct 19 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136122297):
Couldn't we have a function `construct_equalizer_diagram {a b} (f g : a \hom b) : walking_fork \func C`, and then define `equalizer f g := limit (construct_equalizer_diagram f g)`?

#### [Johan Commelin (Oct 19 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136126239):
I like this idea. @**Scott Morrison|110087** , did you try something like this before you settled on the current approach? Do you see problems with it?

#### [Reid Barton (Oct 19 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136126789):
```quote
But without a huge improvement in this direction, it’s way too painful to expect a user to talk about equalizers as (defeq) special cases of limits. Just see the hoops I had to jump through to prove that having limits implies having equalizers...
```
I agree that it is more work starting from scratch to set up the basic definitions of things like equalizers as special cases of limits, but now that *you* have already jumped through those particular hoops, why would a user also need to?

#### [Scott Morrison (Oct 19 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127042):
I guess the problem with `equalizer f g := limit (construct_equalizer_diagram f g)` is that then the user of equalizers has to know the names of the objects and morphisms in the `walking_fork`. (Separately, I think `walking_fork` is the wrong name here; the "handle" of the fork is missing at this point.)

#### [Scott Morrison (Oct 19 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127048):
Maybe this is a small cost.

#### [Scott Morrison (Oct 19 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127083):
What should the objects and morphisms be?

#### [Scott Morrison (Oct 19 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127202):
I guess I'm really not seeing where there would be a simplification of the code, however.

#### [Johan Commelin (Oct 19 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127279):
The simplification would come later, right? For example you have a massive file about deriving products and equalizers from limits. That would simplify.

#### [Johan Commelin (Oct 19 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127290):
And functors preserving limits and such.

#### [Scott Morrison (Oct 19 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127302):
Still for any theorem about limits, you need to restate a special version of it for equalizers/products/etc. None of these things require humans to write the proofs at this point.

#### [Johan Commelin (Oct 19 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127348):
Sorry, maybe I'm dense, but what exactly do you mean?

#### [Scott Morrison (Oct 19 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127349):
Okay, I agree the files that construct equalizers, products, etc from limits would essentially disappear.

#### [Scott Morrison (Oct 19 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127444):
Let's think about the construction 
```def pi.post (f : β → C) (G : C ⥤ D) : G (limits.pi f) ⟶ (limits.pi (G.obj ∘ f)) := ...```

#### [Reid Barton (Oct 19 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127488):
`pi` = product of an arbitrary family?

#### [Scott Morrison (Oct 19 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127490):
if `limits.pi f` is defined as `limit (functor.of_function f)`

#### [Scott Morrison (Oct 19 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127493):
Yes.

#### [Scott Morrison (Oct 19 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127589):
hmm... okay, maybe you guys are right here. :-)

#### [Johan Commelin (Oct 19 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127591):
Wouldn't you just prove this by `limit.post`...?

#### [Johan Commelin (Oct 19 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127656):
Oohh, I really don't know. You guys have written orders of magnitude more code then I have. I'm just a user...

#### [Scott Morrison (Oct 19 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127698):
So... for now I agree that this is worth exploring.

#### [Scott Morrison (Oct 19 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127744):
However, I'm hoping to pause for a while on Lean, in not too long, as I have a lot of maths I want to work on.

#### [Scott Morrison (Oct 19 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127754):
So I'm not sure what to do with this PR in the meantime.

#### [Scott Morrison (Oct 19 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127755):
Options:

#### [Scott Morrison (Oct 19 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127764):
1. leave it open for others to modify

#### [Scott Morrison (Oct 19 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127801):
2. close it for now

#### [Reid Barton (Oct 19 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127811):
I'm not sure exactly where that "..." was going, but another example to keep in mind is "if D is a complete category then a cone in D^J is a limit cone iff each the value at each j in J is a limit cone"

#### [Scott Morrison (Oct 19 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127820):
3. strip it down to just limits, not the special cases, and leave those for later

#### [Reid Barton (Oct 19 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127834):
I have been meaning to suggest that 3 is a good idea anyways

#### [Reid Barton (Oct 19 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127923):
Because the PR involves a lot of relatively untested design, and I think it's worth it to go and try to prove loads of things about general limits to "kick the tires" and make sure we settle on a design that we want

#### [Scott Morrison (Oct 19 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127930):
Okay. I will strip it down. Maybe someone else can explore if the special cases defined as suggested above are usable.

#### [Johan Commelin (Oct 19 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136128038):
@**Reid Barton** How hard would it be to test that on your homotopy lib?

#### [Johan Commelin (Oct 19 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136128100):
Or should we try this on a fork of Scott's lib?

#### [Reid Barton (Oct 19 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136129012):
Probably not that easy since I have some setup of my own to prove a bunch of lemmas about pushouts. Though maybe I could sorry all those proofs and just see how usable it is in the actual homotopy theory part.

#### [Johan Commelin (Oct 19 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136129599):
Yeah, I meant that you just create a branch, and maybe break a couple files, but test this idea on the other files.

#### [Johan Commelin (Oct 19 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136129608):
I'm not suggesting you uproot your `master` branch (-;

#### [Scott Morrison (Oct 20 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136142166):
@**Reid Barton**, do you have  ideas about how to define all the "walking" categories for limits of special shapes?

#### [Scott Morrison (Oct 20 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136142173):
I have reduced my PR to just the plain limits.

#### [David Michael Roberts (Oct 20 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146298):
Just as we have finite sets, why not have a collection of finite categories of the usual special shapes?

#### [Scott Morrison (Oct 20 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146369):
Yes. The point is just to decide the names of the objects and morphisms, because these names will then be fixed forever, and part of the API.

#### [Scott Morrison (Oct 20 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146418):
```quote
Wouldn't you just prove this by `limit.post`...?
```
I've just been trying this, and quickly discovered the reason: `limit.post` assumes that you're in a complete category. However `pi.post` only assumes you have all products. Therefore you can't call `limit.post` from `pi.post`, and we're stuck proving it again.

#### [Scott Morrison (Oct 20 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146426):
Maybe this is a sign that `pi.post` is not what we want to provide people anyway.

#### [Scott Morrison (Oct 20 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146470):
Except ... that it is...

#### [Scott Morrison (Oct 20 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146475):
Maybe I will finish off "porting" products to the new setup, and then you guys can have a look to see what can be reduced.

#### [Scott Morrison (Oct 20 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146479):
I'll do products because there no walking categories are required, we just use `functor.of_function`.

#### [Reid Barton (Oct 20 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146551):
We probably need things like `[has_limits_of_shape J]` for other purposes anyways

#### [Reid Barton (Oct 20 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146593):
e.g. $$\kappa$$-accessible categories have all $$\kappa$$-filtered colimits

#### [Reid Barton (Oct 20 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146599):
("We" = "I", perhaps)

#### [Reid Barton (Oct 20 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146608):
Similarly we want to talk about functors which preserve finite products or whatever

#### [Reid Barton (Oct 20 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146677):
or filtered colimits, etc. This seems to me like more evidence that we need to be able to represent special shapes of (co)limits as special cases of general (co)limits so that we can flexibly mix all these notions, though certainly I have not yet tried to construct a specific design for any of this

#### [Scott Morrison (Oct 20 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146882):
Could we try something like... `has_limits_of {A : Type} (Q : A \to \Sigma (J : Type), J \func C)`

#### [Scott Morrison (Oct 20 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146949):
`has_limits` itself could be defined as `has_limits_of id`

#### [Scott Morrison (Oct 20 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146965):
`has_products` could be defined as `has_limits_of A Q` with `A = \Sigma (b : Type), b \to C`, and `Q = \lambda p, p.1, functor.of_function p.2`.

#### [Reid Barton (Oct 20 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146967):
That's super general but I think even that level of generality could be useful in specific circumstances.

#### [Scott Morrison (Oct 20 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147009):
Maybe there's no need to specify the allowed functors?

#### [Scott Morrison (Oct 20 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147015):
Just the allowed diagrams?

#### [Reid Barton (Oct 20 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147016):
For example cofibration categories or Waldhausen categories have an axiom which says that you can form a pushout if one of the legs is a cofibration (one of the bits of structure)

#### [Scott Morrison (Oct 20 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147021):
I see.

#### [Reid Barton (Oct 20 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147033):
I just hand-crafted this axiom in my project: https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/homotopy_theory/formal/cofibrations/precofibration_category.lean#L41

#### [Reid Barton (Oct 20 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147080):
So I know this example off-hand because I already implemented it in Lean. I think this is a pretty rare scenario, but if doesn't make things too much more complicated...? Certainly the common case would be A = (J \func C), or Sigma of that over all J of some form (e.g., J filtered)

#### [Reid Barton (Oct 20 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147151):
i.e., stick `has_limits_of_shape J` as a specialization of `has_limits_of` and a generalization of `has_products`

#### [Scott Morrison (Oct 20 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147519):
well, maybe even one more step: `has_limits_of`, allowing you to specify arbitrary diagrams and arbitrary functors out of those, then `has_limits_of_shapes` allowing you to specify a class of diagrams, but all functors out of them, then `has_limits_of_shape` for a single diagram, and then `has_binary_products` would be a specialisation of that.

#### [Scott Morrison (Oct 20 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147522):
in any case, I'll give this a go, I guess.

#### [Reid Barton (Oct 20 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147525):
Sounds great!

#### [Reid Barton (Oct 20 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147610):
I should really finish up that Grand Plan for formalizing model categories that I started writing a while ago...

#### [Johan Commelin (Oct 20 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136153288):
While we are at it: Do people have strong opinions on whether the homs of a category live in `Type v` or `Sort v`? I think if we start doing all sorts of diagrams over preorders (or using preorders as categories in other places) it might help in manipulating the homs if they are just in `Prop` instead of the whole `ulift plift` dance.
@**Scott Morrison|110087** Let me stress that I really love what you've done so far :thank_you:. The only reason that I have these questions is because your code is so good :thumbs_up:  that I can't resist using it :stuck_out_tongue_wink:

#### [Scott Morrison (Oct 20 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136155058):
I've tried this before, but it's not possible to use `Sort v`. Unfortunately at the moment I can't remember why... From memory if you just start at the top and switch it over you run into difficulties quite quickly, if you want to try it yourself. :-)

#### [David Michael Roberts (Oct 20 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136157606):
```quote
For example cofibration categories or Waldhausen categories have an axiom which says that you can form a pushout if one of the legs is a cofibration (one of the bits of structure)
```
Dually, there are many cases where one has a class of morphisms of which pullbacks along arbitrary maps exist (eg submersions, in smooth manifolds)

#### [Johan Commelin (Oct 20 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136158656):
Right. At some point we want to formalise this list: https://stacks.math.columbia.edu/tag/02WE

#### [David Michael Roberts (Oct 20 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136159177):
Well, `span` and `cospan` are obvious choices, as is `parallel_pair`. Then also for each finite set one should have the corresponding discrete category, so as to form products/coproduct. The empty category should be there too, to get terminal/initial objects.

#### [Scott Morrison (Oct 20 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173465):
No, I want to know what the _objects_ and _morphisms_ inside, for example `parallel_pair` should be called.

#### [Scott Morrison (Oct 20 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173471):
Should the objects be `source` and `target`, and the morphisms `left` and `right`?

#### [Reid Barton (Oct 20 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173472):
Yeah that's a tough one. `top_arrow`?

#### [Scott Morrison (Oct 20 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173473):
Or should `parallel_pair := bool`??

#### [Mario Carneiro (Oct 20 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173480):
I like 0 and 1 for the objects

#### [Scott Morrison (Oct 20 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173484):
As in `def parallel_pair := fin 2`?

#### [Scott Morrison (Oct 20 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173531):
Or
```
inductive parallel_pair | _0 | _1
```
??

#### [Mario Carneiro (Oct 20 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173532):
probably not literally

#### [Mario Carneiro (Oct 20 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173535):
like the second

#### [Mario Carneiro (Oct 20 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173541):
I just mean as names

#### [Scott Morrison (Oct 20 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173543):
okay, that's what I've done previously. Is there something better that `_0` and `_1` for the names?

#### [Mario Carneiro (Oct 20 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173551):
`0` and `1` are achievable

#### [Scott Morrison (Oct 20 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173555):
Oh, how?

#### [Mario Carneiro (Oct 20 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173557):
add an instance

#### [Reid Barton (Oct 20 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173560):
`has_zero` `has_one`

#### [Scott Morrison (Oct 20 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173613):
ah, I see.

#### [Scott Morrison (Oct 20 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173617):
Isn't it just more confusing to have an inductive type with terms `_0`, `_1`, but then give them second names via instances?

#### [Reid Barton (Oct 20 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173619):
Probably

#### [Mario Carneiro (Oct 20 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173627):
I would call them `zero` and `one`

#### [Mario Carneiro (Oct 20 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173635):
and then use `0` and `1` as notation

#### [Mario Carneiro (Oct 20 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173640):
we do that for `nat`, it's not that confusing

#### [Scott Morrison (Oct 20 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173643):
okay... And using `0` and `1` as notation via `has_zero` and `has_one` will work in pattern matching, etc, just like for nat.

#### [Scott Morrison (Oct 20 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173644):
Sounds reasonable.

#### [Scott Morrison (Oct 20 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173648):
On to the morphisms, then. :-)

#### [Mario Carneiro (Oct 20 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173667):
yeah...

#### [Scott Morrison (Oct 20 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173692):
And the names of objects in pullbacks and pushouts...

#### [Mario Carneiro (Oct 20 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173694):
no bright ideas there. `left` and `right` seem reasonable?

#### [Scott Morrison (Oct 20 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173706):
Except that there's no sense in which the two are actually different...

#### [Reid Barton (Oct 20 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173721):
surely they're `top` and `bottom`?

#### [Mario Carneiro (Oct 20 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173723):
I don't think `left` and `right` imply any other difference

#### [Reid Barton (Oct 20 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173724):
Which way do you draw your equalizers??

#### [Scott Morrison (Oct 20 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173768):
Yeah, there's that too. `top` and `bottom` are probably better.

#### [Reid Barton (Oct 20 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173769):
(but maybe `top` and `bottom` have too many other connotations, with ordering?)

#### [Mario Carneiro (Oct 20 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173772):
I know, it's bugging me that the walking pair is always drawn with the arrows above each other

#### [Scott Morrison (Oct 20 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173788):
oh -- and if `walking_pair` is the diagram for an equalizer, what is the diagram for a binary product?

#### [Mario Carneiro (Oct 20 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173789):
but I think that the analogy to posets is important, that's why 0 and 1 are useful

#### [Reid Barton (Oct 20 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173790):
I was going to bring up binary things next.

#### [Mario Carneiro (Oct 20 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173796):
which one is that?

#### [Mario Carneiro (Oct 20 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173799):
A > B < C?

#### [Scott Morrison (Oct 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173844):
binary product is just the diagram with two objects, no arrows at all

#### [Mario Carneiro (Oct 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173849):
left and right, definitely

#### [Reid Barton (Oct 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173851):
In my homotopy theory library I used the convention of naming things like the inclusions of a coproduct with `\_0` and `\_1`, and eventually I got annoyed that I hadn't chosen `\_1` and `\_2`, but it would be a lot of things to change.

#### [Scott Morrison (Oct 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173852):
... I'd been tempted to call that the `walking_pair`, and the diagram for an equalizer the `walking_parallel_pair`, but that is contrary to usual usage, I think.

#### [Reid Barton (Oct 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173861):
I assume you're going to define it as `discrete` of some type?

#### [Reid Barton (Oct 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173870):
The reason is that `\_1` and `\_2` aligns better with Lean's builtin `p.1` and `p.2`

#### [Scott Morrison (Oct 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173877):
Okay, yeah, I guess that is best, so it's defeq a special case of arbitrarily indexed products.

#### [Reid Barton (Oct 20 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173922):
Yes, and it should also just be less work overall

#### [Scott Morrison (Oct 20 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173923):
So is the indexing category for `binary_product` `discrete (fin 2)`, `discrete bool` or `discrete side`, where `side` is an inductive type with terms `left` and `right`?

#### [Scott Morrison (Oct 20 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173927):
I maybe prefer the last?

#### [Mario Carneiro (Oct 20 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173931):
I think I do too

#### [Scott Morrison (Oct 20 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173937):
or something with terms `fst` and `snd`?

#### [Scott Morrison (Oct 20 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173942):
That fits better with the naming of projection maps in Lean itself.

#### [Mario Carneiro (Oct 20 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173947):
the problem with that is they aren't maps

#### [Mario Carneiro (Oct 20 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173992):
I would get the two confused

#### [Scott Morrison (Oct 20 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173994):
yes, but we'll be able to write things like `c.\pi fst` for the first projection

#### [Reid Barton (Oct 20 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174001):
`left` and `right` are nice for `inl` and `inr` though

#### [Mario Carneiro (Oct 20 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174009):
is it the same category being reused?

#### [Scott Morrison (Oct 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174021):
I don't see why not.

#### [Mario Carneiro (Oct 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174023):
ok, then I agree with Reid

#### [Reid Barton (Oct 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174025):
Probably it should be... so that we can relate coproducts in C to products in C^op eventually

#### [Mario Carneiro (Oct 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174029):
although I guess technically one is the op of the other

#### [Reid Barton (Oct 20 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174069):
Yes, technically it should be the op

#### [Scott Morrison (Oct 20 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174072):
Great, I will use `side` with `left` and `right`.

#### [Reid Barton (Oct 20 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174074):
but we're already writing the category as `discrete T` where `T` is the type of its objects

#### [Scott Morrison (Oct 20 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174075):
Finally, pullbacks and pushouts

#### [Mario Carneiro (Oct 20 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174087):
Can we steal the same names?

#### [Scott Morrison (Oct 20 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174088):
it would be nice here if everything is consistent...

#### [Reid Barton (Oct 20 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174092):
`middle`??

#### [Reid Barton (Oct 20 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174095):
Is anyone going to actually see these names?

#### [Mario Carneiro (Oct 20 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174152):
`left - inl > 1 < inr - right`

#### [Mario Carneiro (Oct 20 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174158):
`left < fst - 0 - snd > right`

#### [Scott Morrison (Oct 20 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174262):
okay, sounds good to me

#### [Scott Morrison (Oct 20 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174278):
except...

#### [Reid Barton (Oct 20 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174281):
I guess those names are technically accurate in some sense, though I find them really confusing

#### [Reid Barton (Oct 20 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174289):
like, you have `fst` and `snd` involved in the diagram for pushouts and vice versa

#### [Scott Morrison (Oct 20 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174292):
remember the morphisms there are terms of one-element types

#### [Scott Morrison (Oct 20 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174303):
maybe we should just make all those morphisms types `punit`.

#### [Scott Morrison (Oct 20 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174308):
and not have names at all

#### [Scott Morrison (Oct 20 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174365):
we just have to name the objects here, so we'd have `inductive walking_pullback | left | right | one`

#### [Mario Carneiro (Oct 20 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174368):
I don't think so... the type is a inductive family with two elements

#### [Reid Barton (Oct 20 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174370):
As they say, no names is good names

#### [Scott Morrison (Oct 20 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174396):
why? we need to have a type of morphisms from `left` to `one`, and it contains only `inl`.

#### [Scott Morrison (Oct 20 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174400):
etc

#### [Reid Barton (Oct 20 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174403):
It depends on whether you want to define `hom` as a single inductive family, or a type defined by case analysis

#### [Mario Carneiro (Oct 20 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174418):
I think types by case analysis is a bad idea

#### [Scott Morrison (Oct 20 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174462):
remember `hom : obj -> obj -> Type`

#### [Reid Barton (Oct 20 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174474):
I agree it probably makes the finite amount of work it takes to set up these categories and describe functors from them larger

#### [Scott Morrison (Oct 20 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174475):
maybe I'm confused here

#### [Reid Barton (Oct 20 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174478):
I don't know if it has any longer term consequences though

#### [Mario Carneiro (Oct 20 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174484):
`inductive hom | inl : hom left 1 | inr : hom right 1`

#### [Scott Morrison (Oct 20 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174486):
I see

#### [Scott Morrison (Oct 20 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174487):
okay, that does sound good

#### [Scott Morrison (Oct 20 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174489):
but makes it harder to name things. :-)

#### [Reid Barton (Oct 20 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174527):
what about identities though? I think the truly correct way to do this is to go through the free graph construction

#### [Reid Barton (Oct 20 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174531):
Er, free category on a graph construction

#### [Mario Carneiro (Oct 20 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174533):
I was just about to say the same

#### [Mario Carneiro (Oct 20 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174534):
this is a graph, not a cat

#### [Reid Barton (Oct 20 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174536):
which I do have written down somewhere

#### [Scott Morrison (Oct 20 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174539):
yes... I have this as well. It is extraordinarily painful to use, and this is why I hadn't previously pursued this approach.

#### [Reid Barton (Oct 20 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174542):
but I'm still not sure whether it makes any difference once we're done defining all these little categories

#### [Mario Carneiro (Oct 20 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174547):
really? I wouldn't have expected that

#### [Scott Morrison (Oct 20 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174549):
but Reid, isn't your point that "all these little categories" is not a fixed set?

#### [Reid Barton (Oct 20 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174552):
Specifically, it should be easy enough to change our mind about the definitions of these categories later, right?
As long as we have a usable interface for building functors out of them

#### [Reid Barton (Oct 20 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174619):
for example: there is some category called `parallel_pair`, and to define a functor `parallel_pair \func C` I have to give you two objects (a b : C) and two maps (f g : a \hom b)

#### [Scott Morrison (Oct 20 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174627):
yes

#### [Scott Morrison (Oct 20 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174633):
my preference would be on the first cut to define the slightly larger  indexed inductive types for morphisms that include identity morphisms.

#### [Reid Barton (Oct 20 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174634):
and then... there is some extensionality rule or something... and then it doesn't matter what goes inside. Right?
And nobody really needs to care about the choices of names, since I just renamed everything `a b f g` anyways

#### [Scott Morrison (Oct 20 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174676):
and only later to pursue defining these as path categories on graphs (because I don't know how to do this well)

#### [Reid Barton (Oct 20 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174678):
As long as we can maintain this interface, it shouldn't matter whether we use the free category on a graph, or define hom as an indexed inductive type, or define hom by case analysis

#### [Reid Barton (Oct 20 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174683):
or define the category as a poset if it happens to be one

#### [Scott Morrison (Oct 20 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174688):
I can't see to find my previous attempt to construct equalizers, based on a free category, out of limits, which was so unpleasant...

#### [Reid Barton (Oct 20 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174736):
I admit I never actually used my free category construction to do anything. I was going to use it to prove that Cat has coequalizers... but I didn't.

#### [Mario Carneiro (Oct 20 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174758):
Oh hey, are graphs an example of `has_hom`?

#### [Reid Barton (Oct 20 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174780):
That depends on what `has_hom` means exactly--this example was in the back of my mind when commenting on that aspect of Simon's PR

#### [Mario Carneiro (Oct 20 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174823):
assuming categories extend it, it must mean the notation, with hom and objects

#### [Reid Barton (Oct 20 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174824):
I think Scott convinced me at one point that it was better to not build `category` on top of `graph`, but I don't remember why exactly... maybe if we rename `graph` to `has_hom` it is more palatable, haha

#### [Mario Carneiro (Oct 20 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174883):
I kind of want to reserve the name `graph` for *small* `has_hom`s

#### [Reid Barton (Oct 20 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174893):
Mario I'm glad you agree--there's this discussion about what to rename `has_hom` to in Simon's PR, which is really "the data of a category without the laws"

#### [Reid Barton (Oct 20 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174900):
That would just be specializing the universe parameters of `has_hom` to be equal right?

#### [Mario Carneiro (Oct 20 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174949):
I think so? I'm not sure that's small enough. Maybe it doesn't make sense

#### [Mario Carneiro (Oct 20 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174956):
I want `graph A : Type u` when `A : Type u`

#### [Mario Carneiro (Oct 20 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174960):
but there's no way I'm going to get that

#### [Reid Barton (Oct 20 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174961):
A graph is a set of vertices, together with a set of edges from a to b for each a and b

#### [Reid Barton (Oct 20 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174964):
Well, if graph isn't allowed to have multiple edges...

#### [Mario Carneiro (Oct 20 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136175003):
yeah, simple graphs solve the problem

#### [Reid Barton (Oct 20 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136175008):
I guess actual graph theorists would call this a multigraph

#### [Reid Barton (Oct 20 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136175074):
Anyways `graph`s would also be examples of `has_hom` in any case

#### [Reid Barton (Oct 20 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136175113):
Anyways anyways, my overall claim is that these names don't really matter either, because people should only be using the interface like `parallel_pair_functor f g`.

#### [Reid Barton (Oct 20 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136175312):
Maybe that means the things to do is to pick the variable names which appear in the interface (like `f` and `g`?) and then choose the names of generating morphisms based on them in some systematic way (like `F` and `G`?)

#### [Reid Barton (Oct 20 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136175325):
or whatever naming convention seems least likely to collide with other relevant things, maybe `F` is a bad name

#### [Kevin Buzzard (Oct 20 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136178333):
```quote
The reason is that `\_1` and `\_2` aligns better with Lean's builtin `p.1` and `p.2`
```
I was surprised once when I realised that the builtin notation was not `p.0` and `p.1` but presumably could have been, given that Lean was written by CS people.

#### [Scott Morrison (Oct 21 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136199413):
@**Reid Barton**, @**Johan Commelin**, I experimented with a new design for "special" shape limits. Now they are all defined as special cases of limits. If you want to have a quick look, see https://github.com/leanprover-community/mathlib/tree/limits-others-new/category_theory/limits.

#### [Scott Morrison (Oct 21 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136199421):
I think it looks reasonable. I would like to try proving some things about limits in functor categories, and make sure they immediately imply the corresponding results about pullbacks/products/etc.

#### [Scott Morrison (Oct 23 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136302717):
I'm going to make other fundamental changes, I think.

#### [Scott Morrison (Oct 23 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136302755):
(deleted)

#### [Scott Morrison (Oct 23 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136302808):
I'm going to change `cone F` at least so that it is an object, bundled with a natural transformation from the constant functor (with value that object) to `F`. I may go all the way and just define `cone F` as a special case of a comma category. That had, long ago, been my initial version of limits, but I was having too much trouble with it. Having learnt a few things, I think it's viable again, so will try again. :-)

#### [Reid Barton (Oct 23 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136303069):
I wanted exactly this description in order to prove that right adjoints preserve limits

#### [Johan Commelin (Oct 23 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136319006):
@**Scott Morrison|110087** Cool! That sounds like a good generalisation.
Concretely, you had a definition of sheaves, and I have almost generalised it to arbitrary sites. The real test case is probably going to be sheafification, and more generally pushforward and pullbacks of sheaves (and the fact that those are adjoint).

#### [Johan Commelin (Oct 23 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136324809):
@**Scott Morrison|110087** How general are you planning to set up comma categories? Only slices over an object, or the general thing where you start with two functors?

