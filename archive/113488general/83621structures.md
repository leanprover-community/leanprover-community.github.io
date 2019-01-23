---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83621structures.html
---

## Stream: [general](index.html)
### Topic: [structures](83621structures.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 08 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/123459639):
When I was building the complexes, I think I tried to make them a field all in one go, and there were problems which perhaps were something to do with neg or sub. @**Mario Carneiro** showed me how to fix these problems by showing first that the complexes were an additive group and then only afterwards that they were a field. But I cannot remember what the problems were. Can anyone here guess? Was it something to do with defining sub or neg myself vs letting the system somehow do it for me? I now cannot really imagine how the system would do it for me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 02 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764601):
How am I supposed to finish of this triviality?
```lean
C : Type u,
cat : category C
⊢ {Hom := category.Hom cat,
     identity := 𝟙,
     compose := category.compose cat,
     left_identity := _,
     right_identity := _,
     associativity := _} =
    cat
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 02 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764615):
It is just asking me whether sum structure `cat` is equal to the structure built from the fields of `cat`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 02 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764618):
`congr` or `ext`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 02 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764621):
To which I reply: "Yes! Of course it is."

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 02 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764627):
oh no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 02 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764628):
`cases cat`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 02 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764629):
then `dsimp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 02 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764631):
aha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 02 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764633):
I'm not sure because this is not an MWE

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 02 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764636):
`congr` failed, and `ext` did nothing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 02 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764680):
if `ext` did nothing, then it is because you don't have an extensionality lemma, i.e. the interface

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 02 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764686):
`@[extensionality] lemma category.ext : ...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 02 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764754):
```lean
lemma op_op' : @opposites.Opposite C (@opposites.Opposite C cat) = cat :=
begin
  tactic.unfreeze_local_instances,
  cases cat,
  dsimp [opposites.Opposite],
  congr
end -- We win!
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 02 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764756):
That worked.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 02 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764759):
Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 02 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764760):
nice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 02 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130765215):
My guess is that perhaps you wanted the` add_group` axioms to prove some other the other field axioms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 02 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130765227):
add group?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 02 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130765298):
What's the question?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 02 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130765311):
you're replying to the message from March

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 02 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130765345):
I see.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 02 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130767424):
Johan, I think you shouldn't need to directly call `unfreeze_local_instances`. What are you trying to do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 02 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130767475):
Well, I tried to do the `cases cat` and it complained... it told me to `unfreeze` stuff, and I happily complied.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 02 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130767488):
I am trying to investigate how far the double `op` of a category `C` is from being defeq to `C`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 02 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130767489):
Do you have a MWE I could try?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 02 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130767500):
Hmm, it depends on an old version of Scott's PR...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 02 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130767508):
If you have his PR checked out somewhere, I suppose you could copy paste my latest snippet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 02 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130768912):
@**Patrick Massot** https://github.com/jcommelin/lean-homotopy-theory/blob/playground/src/categories/op_op.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 02 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130768914):
That's a file in a fork of a project by Reid, depending on an old version of Scott's PR.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 02 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130768988):
If you're being asked to unfreeze local instances then it's probably because you're doing cases on some random class -- that's when this happens to me. I think the last time it happened, Chris pointed out that I had access to all the things I wanted, with `cat.foo`, `cat.bar` etc, so I didn't need to unfreeze anything.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 02 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130769080):
Is unfreezing a bad thing to do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 02 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130769237):
`Opposite (Opposite C)` isn't going to be defeq to `C`. It's going to be provably equal, or isomorphic, but since we know those are both evil notions, in the end we probably just want to prove it's equivalent. (My intuition is that even proving the equality is just going to invite trouble later, when you rewrite along the equality.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 02 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130769289):
Right. But it's pretty close to being defeq (whatever that means). As expected, there is nothing going into the proofs I just linked to.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 02 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130769490):
The CS people love stuff being defeq but because categories are one level up in the mathematical hierarchy from sets, it's basically never the right question to ask if they're isomorphic, let alone defeq

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 02 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130769616):
Sure. But `op op` is somewhat special right? And I can imagine it would help a lot, in this special case.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 04 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130879231):
I don't think there is any harm in proving an equality of categories when it happens to be true. Of course there should be theorems saying equality implies isomorphism and isomorphism implies equivalence

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 04 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130879241):
the main point is to not expect that equality is much stronger or easier to work with than these other two notions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 04 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130879244):
I agree. Just don't rewrite the source or target of a functor/natural transformation by an equation of categories and expect to be happy later. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 04 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130879337):
I think one way to handle this is to use a `have` subproof to show that some equality of categories holds (say an embedded op op cancellation), and then use `cast h` as a functor and have theorems about it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 04 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130882057):
```quote
I don't think there is any harm in proving an equality of categories when it happens to be true. Of course there should be theorems saying equality implies isomorphism and isomorphism implies equivalence
```
Maybe the CS experience is different, but it's very rare for categories to be isomorphic in "real life" maths.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 04 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130882101):
I think it's about as common as equality of categories, like in this case

