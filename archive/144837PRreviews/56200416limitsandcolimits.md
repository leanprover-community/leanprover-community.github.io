---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/56200416limitsandcolimits.html
---

## Stream: [PR reviews](index.html)
### Topic: [#416 limits and colimits](56200416limitsandcolimits.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 12 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135665324):
Okay, here is limits and colimits (just for general shapes, not all the useful special cases yet), with no dependency on new-fangled tactics.

https://github.com/leanprover/mathlib/pull/416

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 12 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135665397):
@**Reid Barton**, @**Johan Commelin** hopefully this will give you the parts you need for playing with presheaves.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 12 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135667107):
@**Scott Morrison|110087** Hurray! Thank you so much!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 13 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741575):
I've now added all the special shapes (although equalizers and pullbacks are less developed than everything else).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 13 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741583):
I also added instances for (co)limits in `Type u`, and appropriate simp lemmas.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 13 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741588):
I'm happy for this to be reviewed/merged at this point, I don't have immediate plans to add more.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 13 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741667):
A few missing bits if anyone wants to fill them in:
* lemmas describing how equalizers and pullbacks (and the dual notions) transform, similar to all the `pre`, `post`, and `map` lemmas in the other files
* the final three lemmas describing how colimits behave in `Type u`. (@**Reid Barton**?)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 13 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741727):
One thing that I noticed while working on sheaves was that Lean couldn't figure out that if a category has limits then it also has products.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 13 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741730):
I guess this means we need to add some instances.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 13 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741731):
Other stuff that should be done in other PRs later, and of which I have prototypes (but someone should feel free to do themselves):
* functors into a complete category are complete
* all the gadgets getting between different shapes of limits (equalizers and products imply all limits, etc)
* filtered limits, finite limits, finite products

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 13 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741741):
But maybe "limits implies products" should also be part of other PRs?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 13 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741743):
@**Johan Commelin** , let me see if I have that one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 13 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741853):
Yes, I've got it. It relies on `discrete_category.lean`, which I think never got PR'd yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 13 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135741862):
Ok, well it can of course wait till another PR (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 14 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759817):
I have a notational problem in the (co)limits PR. At first I'd introduced 
```
def sigma {C : Type u} [𝒞 : category.{u v} C][has_coproducts.{u v} C] {β : Type v} (f : β → C) : C
def pi {C : Type u} [𝒞 : category.{u v} C][has_products.{u v} C] {β : Type v} (f : β → C) : C
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 14 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759832):
but then realised `sigma` is a terrible idea, because it overloads the built-in sigma.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759834):
`protected`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 14 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759877):
I thought to change `sigma` to `Sigma` and `pi` to `Pi`, but `Pi` is of course already taken for pi-types.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 14 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759879):
Is `protected` the best solution?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 14 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759880):
I'm a bit unclear on what happens when we use it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759882):
it means you have to prefix the namespace

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 14 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759890):
Hmm. I guess that's okay.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759892):
there are a few examples of things in the library named `sigma` and `pi` and protected

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 14 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759894):
Ok, I'll try that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 14 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759936):
I better sleep, spent a long time on :airplane_departure: today.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 14 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135759953):
In other news, there's a second PR, containing the constructions limits => equalizers, limits => products, products + equalizer => limits, and functors into complete categories form a complete category, ready to go.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135760013):
By the way, in response to an earlier suggestion of inferring has_products from has_limits or something like this, I suggest that all these be regular defs, and you make them instances in particular categories

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 14 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135760020):
that way you get to decide which ones imply which others

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 14 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135788644):
Great, these have just appeared as #420.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 14 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135788813):
Are there any examples of actual limits (in mathlib or in your repo)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135788825):
so how close are we to direct limits?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 14 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135788830):
Direct limits of what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135788833):
rings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 14 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135788883):
This was my question: we have abstract notion of limits and colimits, but I think there is no example yet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 14 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135788884):
Limits in Ring would be an example

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 14 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135788999):
@**Scott Morrison|110087** maybe you could do one example, in order to demonstrate the interface, and then we could try to have another one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 14 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135789055):
The examples so far are just are the (co)limits in `Type u`. https://github.com/leanprover/mathlib/pull/416/files#diff-e57d73facf90a0010edf5b1dcece8ac1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 14 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135789059):
I'm a bit indecisive about how to do rings. We can do it directly, or we can build machinery to do it quickly. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 14 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135789101):
What would be the machinery?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 14 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135789305):
reflective subcategories (to get from Ring to CommRing) and monadic adjunctions (to get from Type to Ring)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 14 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135789312):
But I don't know this stuff well; I'd need to talk to Reid again to get it all straight.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 14 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135789324):
I guess that is an indication that doing things directly on the first pass is a good idea. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 14 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135789364):
Also, my PRs don't include filtered colimits yet, so the direct limits Kenny wants require another intermediate step.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 14 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135789424):
I'd love to get this fancy stuff, but it would probably be better to first do it by hand for rings, and then check we get the same result using fancy stuff (I mean the same usability, hopefully the abstract result should be the same anyway)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 14 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135789431):
Maybe topological spaces are an easier target for beginners

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 14 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135789949):
Ok... I will do products for rings in a moment.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135790430):
As I mentioned in another thread, the perfect closure of F can be constructed as a direct limit of a bunch of copies of F.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135790433):
So I would really like to have direct limit. However it's fine if you don't feel like doing it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 14 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135790486):
No, I would like to do it (the general definition, that is). Next time I see Reid around I'm going to ask him about how to do it without too much duplication.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135790554):
in the meantime, maybe I can revive my [direct limit PR](https://github.com/leanprover/mathlib/pull/118)...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135790703):
@**Scott Morrison|110087** would there be any problem if I do so?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 14 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135791871):
I think it's pointless to try to do topological spaces before you do rings, there are too many definitions and notations to decipher. I started with
```lean
instance : has_products.{u+1 u} Top :=
{ prod := λ β f, 
  { X := {α := Π b, f b, str := by apply_instance},
    π := λ b, ⟨_, continuous_supr_dom continuous_induced_dom⟩ },
  is_product :=
  begin
    tidy,
  end }.
```
but then I see goals like `is_open ((λ (a : ((s.to_shape).X).α) (b : β), (s.π b).val a) ⁻¹' s_1)` which is pretty hard to read

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135797440):
@**Patrick Massot** You will see something very similar if you do products of rings. The `to_shape` and the `s.pi ..).val` etc are all parts of the category theory.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135803776):
@**Patrick Massot**, to parse that for you: `s_1` is presumably an open set. `s` is a cone (in this case called a "fan" because we're doing products, not general limits. It has a field `X`, which is the cone point. Unfortunately this is written as `(s.to_shape).X`; I wish the `to_shape` wasn't necessary; I'll investigate that further. I'd originally called `X` `cone_point`, but people's preference for brevity caused me to change it. In any case, `(s.to_shape).X` is now a `Top`, i.e. a bundled topological space. Then `((s.to_shape).X).α` is the underlying type of points of that topological space. `s.π b` is one of the projection maps of the cone, i.e. the continuous map from `((s.to_shape).X)` to `f b`. So the goal you reach is just saying: the preimage of an open set under the ... [oops, first attempt got this wrong]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135803885):
under the product of all the projection maps (i.e. some subset of `\Pi b, (f b).α`) is open.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135803926):
At this point we're actually going to need to look at the topology we gave on `Π b`, and see that this is true pretty much by definition, using the fact that all the `(s.π b).val` are continuous functions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135803932):
(assuming that's is the definition of the product topology we're using, I haven't looked)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135803936):
If you have advice about renaming fields to make it easier to do that unpacking, please let me know!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135804097):
I would suggest casing a whole bunch on `s`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135804237):
if possible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135804244):
I would prefer to see a theorem that assumes a topological space and some properties

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135805031):
I'll continue this in https://leanprover.zulipchat.com/#narrow/stream/144837-PR-reviews/subject/.23422.20limits.20in.20CommRing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 17 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135963625):
@**Johannes Hölzl** wrote on the PR page:
```quote
Another thing which doesn't work for me: duplication of duality.
What about copying to_additive and adapting it to an duality method?
```
We talked about that in Orsay. I think Mario and Scott came to the conclusion that it is a lot of hassle.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 17 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23416%20limits%20and%20colimits/near/135963653):
For example, a lot of names change.

