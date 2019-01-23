---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/55375additivegrouphoms.html
---

## Stream: [maths](index.html)
### Topic: [additive group homs](55375additivegrouphoms.html)

---

#### [Johan Commelin (May 23 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126990085):
This has come up before. I need additive group homs. I can duplicate Patrick's work on group homs, but I also saw `@[to_additive finsupp.sum_map_range_index]` in `data/finsupp.lean`. Can someone explain to me how that magic works? Would it be enough to sprinkle some `@[to_additive ...]`'s into `algebra/group.lean` to have everything work?

#### [Kevin Buzzard (May 23 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126990781):
There are additive group homs in the scheme stuff

#### [Kevin Buzzard (May 23 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126990782):
Kenny wrote them

#### [Kevin Buzzard (May 23 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126990787):
you could cut and paste for some basic stuff

#### [Kevin Buzzard (May 23 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126990789):
if you just want a solution

#### [Johan Commelin (May 23 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126990833):
Sure, but I'm also interested in the long-term approach

#### [Kevin Buzzard (May 23 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126990842):
lines 47 onwards at https://github.com/kbuzzard/lean-stacks-project/blob/master/src/canonical_isomorphism_nonsense.lean

#### [Kevin Buzzard (May 23 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126990862):
already there is a little magic going on

#### [Andrew Ashworth (May 23 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126991426):
the long term approach would be to learn a bit about tactics and understand how to_additive works, which is for automatically moving theorems from multiplicative groups to additive groups... unfortunately, learning tactics in Lean is a bit of a chore right now since Programming in Lean is unfinished

#### [Andrew Ashworth (May 23 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126991559):
well, actually, now that I'm looking at `algebra/group.lean`, you don't need to know much about tactics to understand what's going on there

#### [Johan Commelin (May 23 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126991753):
But then... I know next to nothing...

#### [Andrew Ashworth (May 23 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126992374):
hmm, have you worked through TPIL by chance?

#### [Andrew Ashworth (May 23 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126992434):
The first eleven chapters of Software Foundations is in Coq, but also quite good

#### [Andrew Ashworth (May 23 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126992443):
I am the kind of person who learns by grabbing a textbook and doing the exercises...

#### [Johan Commelin (May 23 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126992799):
Yes, maybe I should do that as well... but trying to define singular homology seems like a lot more fun...

#### [Johan Commelin (May 23 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126992815):
I am the kind of person who learns by cargo cult hacking

#### [Andrew Ashworth (May 23 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126993051):
this is also valid, but unfortunately if you get stuck there is no solutions manual available to unstuck you, whereas such a thing exists for Software Foundations... the solutions manual known as Mario is asleep right now

#### [Johannes Hölzl (May 23 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126993084):
the magic of `to_additive` is a search and replace of all `to_additive` constants in the definition of the constant. Afterwards the additive, multiplicative constant pair is added to the `to_additive` database. By using `attribute [to_additive a_c] m_c` you add a new relation. The requirement is that the additive constants are an exact mirror of the multiplicative ones.

#### [Johan Commelin (May 23 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126993161):
So, if I understand you correctly, it shouldn't be too complicated to sprinkle `@to_additive` in `algebra/group.lean`. Is that right?

#### [Johan Commelin (May 25 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127063451):
Ok, so here is something that I am a bit worried about: in mathematics the notion of an "additive" group is really just notation (though pretty useful!). In Lean we have "groups" and "additive groups" and now we have `is_group_hom` and `is_add_group_hom`. But we also need mixed homomorphisms (from a multiplicative group to an additive group, and vice versa). For example, exp and log are such mixed homomorphisms. So all of a sudden, we have 4 notions of group homomorphisms. And now we want to compose these guys. So we need 8 composition lemmas. And I proved the 5 lemma some time ago: it has 10 groups in its statements. But any of those can be an "additive" group (and this occurs in nature!). Does that mean we need 1024 statements of the Five Lemma?

#### [Mario Carneiro (May 25 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064340):
Use `multiplicative` to do these kind of things

#### [Johan Commelin (May 25 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064381):
But, doesn't that mean we should use `multiplicative` all the time?

#### [Mario Carneiro (May 25 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064392):
The additive / multiplicative group thing has a long history, and we are still debating the best way to do it

#### [Johan Commelin (May 25 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064404):
Ok, I see. I can understand that it might be delicate to pick the correct approach

#### [Mario Carneiro (May 25 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064456):
`multiplicative` is useful for post hoc fitting a multiplicative theorem in an additive or mixed-additive use case

#### [Johan Commelin (May 25 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064464):
I feel like I would rather just remove `add_group` entirely. But I don't see through all the ramifications

#### [Mario Carneiro (May 25 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064467):
`to_additive` is useful for preparing theorems up front *with new names* and statements

#### [Mario Carneiro (May 25 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064508):
It's very confusing to apply `mul_one` when you want to simplify `x + 0 = x`

#### [Johan Commelin (May 25 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064513):
Yes, but I think that that `to_additive` magic will replace *all* occurences of mul with add

#### [Mario Carneiro (May 25 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064515):
yes, that's the idea

#### [Johan Commelin (May 25 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064516):
Or can you also use it to create mixed statements?

#### [Mario Carneiro (May 25 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064522):
it's not very smart, it usually fails on mixed statements

#### [Mario Carneiro (May 25 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064551):
like `gpow`, which has an interplay between the additive semiring N and the group in question

#### [Mario Carneiro (May 25 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064565):
those translations had to be done manually, and in that case usually `multiplicative` is easier

#### [Johan Commelin (May 25 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064577):
So, if we didn't have all the "multiplicative" connotations with our groups... but just `op_neu` instead of `mul_one`. Would that be helpful?

#### [Mario Carneiro (May 25 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064621):
Jeremy likes this idea. I think it's the worst of both worlds

#### [Johan Commelin (May 25 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064630):
If you could somehow have some magic that infers whether you use `*` or `+` notation, I feel like it would give a very nice fusion.

#### [Mario Carneiro (May 25 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064633):
(Jeremy Avigad has been testing out a bunch of solutions in this space the past few months)

#### [Johan Commelin (May 25 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064635):
But why do you think it is worse?

#### [Mario Carneiro (May 25 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064638):
It's less mnemonic than either add_zero or mul_one

#### [Mario Carneiro (May 25 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064679):
some of that magic goes beyond what lean will currently do on its own

#### [Johan Commelin (May 25 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064681):
Yes, but having a lot of `gsmul` sprinkled through your goal is also not very helpful

#### [Mario Carneiro (May 25 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064683):
but then it gets into extending lean, which gets messy

#### [Mario Carneiro (May 25 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064691):
What do you mean?

#### [Johan Commelin (May 25 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064696):
Well, I was playing around with `multiplicative` a bit. And I think it gave me those `gsmul`'s

#### [Johan Commelin (May 25 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064735):
But maybe I just used it wrong

#### [Johan Commelin (May 25 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064768):
I think I will just wait to see what you and Jeremy work out.

#### [Mario Carneiro (May 25 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064811):
What are you trying to do exactly?

#### [Johan Commelin (May 25 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064812):
If I understand you correctly, you say that a class `is_add_group_hom` is fine. But we shouldn't have classes for mixed homomorphisms. If one of those pops up, just turn it into an `is_group_hom`with `multiplicative`. Is that correct?

#### [Mario Carneiro (May 25 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064852):
yes

#### [Johan Commelin (May 25 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064853):
Because if we also have classes for the mixed homomorphisms, then you do need 8 composition rules. And I feel like you run head first into some cambrian explosion.

#### [Mario Carneiro (May 25 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064855):
we don't

#### [Johan Commelin (May 25 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064865):
So, shouldn't I just get rid of `is_add_group_hom` as well? And just use `multiplicative` immediately?

#### [Mario Carneiro (May 25 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064914):
I should hope there isn't too much theory on `is_add_group_hom`

#### [Mario Carneiro (May 25 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064917):
seeing as it can usually be rephrased in terms of `is_group_hom`

#### [Johan Commelin (May 25 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064929):
But still, I don't see why you draw the line there...

#### [Mario Carneiro (May 25 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064933):
two is manageable, 2^n isn't?

#### [Johan Commelin (May 25 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064969):
Anyway, what I am trying to do, is to prove that the boundary operator on the simplicial complex satisfies `d \circ d = 0`

#### [Johan Commelin (May 25 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064975):
Yes, but one is even more manageable... (-;

#### [Mario Carneiro (May 25 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064979):
so use `is_group_hom` and call it a day

#### [Johan Commelin (May 25 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064980):
And this complex consists of an additive group for each `n : nat`. And an additive hom between succesive groups.

#### [Mario Carneiro (May 25 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064989):
what makes them additive?

#### [Johan Commelin (May 25 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064991):
Those groups are all `finsupp (X n) int`

#### [Johan Commelin (May 25 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064992):
where `X n` is a Type; depending on `n` (duh)

#### [Mario Carneiro (May 25 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065036):
okay, so where is the mixed group hom?

#### [Johan Commelin (May 25 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065048):
And the homomorphisms between them are somehow a bit involved... You take an alternating sum of (n+1) maps from `X (n+1)` to `X n`, and those induce maps between those additive groups.

#### [Johan Commelin (May 25 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065051):
Aah, there is no mixed group hom in this picture yet.

#### [Johan Commelin (May 25 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065052):
But I was thinking about other stuff in maths, where they do pop up.

#### [Johan Commelin (May 25 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065055):
In all sorts of exponential sequences

#### [Mario Carneiro (May 25 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065098):
So you can use `is_group_hom` + `multiplicative` to define `is_add_group_hom`, and then most of the theorems will defeq carry over (although they may need to be restated)

#### [Johan Commelin (May 25 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065121):
Ok, but I think I will try to just use `multiplicative` directly.

#### [Johan Commelin (May 25 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065163):
So instead of proving `is_add_group_hom d` I prove `@is_group_hom (multiplicate _) (multiplicative _) d`

#### [Johan Commelin (May 25 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065164):
Or something like that.

#### [Mario Carneiro (May 25 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065222):
they should be the same, but yes unfold if necessary

#### [Johan Commelin (May 25 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065227):
Ok, thanks for this discussion! I learned something (-;

#### [Johan Commelin (May 25 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065234):
Ooh, and if I locally make every instance of `add_group` into an instance of `group`, I think I run into the same trouble with ugly notation and names, right?

#### [Mario Carneiro (May 25 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065235):
Oh don't do that

#### [Mario Carneiro (May 25 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065275):
that's a recipe for disaster because the notations get all mixed up

#### [Johan Commelin (May 25 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065277):
ok

#### [Mario Carneiro (May 25 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065281):
next you know it you write `1 + 1 : nat` and get `0` :/

#### [Johan Commelin (May 25 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065286):
got it

#### [Johan Commelin (May 25 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067503):
Ok, so here is another ignorant question:
The reason we have infix notation `*` for every `group` is because they are instances of `has_mul`, right?

#### [Johan Commelin (May 25 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067516):
So what if we made abstract groups, with `op` and `neu` etc...

#### [Johan Commelin (May 25 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067520):
And we don't have infix notation for those

#### [Johan Commelin (May 25 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067526):
And then we have concrete groups (like the units in `rat`, or `int`) and we make those instances of `has_mul` resp. `has_add`

#### [Johan Commelin (May 25 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067527):
Then we still have our beloved infix notation.

#### [Johan Commelin (May 25 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067568):
And then we can have some `to_multiplicate` resp. `to_additive` magic, that will turn `op_neu` into `mul_one` resp. `add_zero`

#### [Johan Commelin (May 25 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067569):
So the proofs remain readable and intuitive

#### [Johan Commelin (May 25 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067616):
If you want to prove something about an abstract group, and you would like to use infix `*` notation, then inside the proof you can make the group into an instance of `has_mul` (I hope) and voila, you have your `*`. But the statement that you proved is all of a sudden also valid in the context of additive notation.

#### [Johan Commelin (May 25 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067619):
Does this idea make any sense at all?

#### [Mario Carneiro (May 25 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067625):
If you use `has_mul` then it gets involved in the statements of the theorems you prove, so there is some unfolding to apply it in a given context

#### [Johan Commelin (May 25 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067629):
Well, I hope to keep it out of the statements.

#### [Mario Carneiro (May 25 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067631):
then you can't use notation with abstract group theory

#### [Mario Carneiro (May 25 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067669):
which is a thing people want

#### [Johan Commelin (May 25 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067672):
So you would have some statement `theorem {G : Type} [group G] : blabla := begin ... end`

#### [Johan Commelin (May 25 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067677):
and between the `begin` and `end` you do some sort of `have_instance : has_mul G := { mul := op }`

#### [Johan Commelin (May 25 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067683):
and then you can use multiplicative notation in the rest of the proof.

#### [Johan Commelin (May 25 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067685):
But it does not affect the statement

#### [Mario Carneiro (May 25 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067690):
so `blabla` there has no notation?

#### [Johan Commelin (May 25 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067733):
Yes, that is correct

#### [Johan Commelin (May 25 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067734):
Unless we can somehow sugar that in... but I guess then we run into trouble again (which was your point)

#### [Mario Carneiro (May 25 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067735):
right

#### [Mario Carneiro (May 25 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067742):
Also, without `mul` constants in that statement `simp`  gets lost in higher order unification

#### [Johan Commelin (May 25 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067743):
I think there is quite a lot of interesting `blabla` that does not have very much notation

#### [Mario Carneiro (May 25 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067745):
for example if you have the theorem `op x id = x` where `op` and `id` are variables, `simp` can't use it

#### [Mario Carneiro (May 25 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067748):
but if the theorem is `x + 0 = x` then it can

#### [Johan Commelin (May 25 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067788):
You could wrap the statement with `local notation x' \bullet 'y := op x y`

#### [Johan Commelin (May 25 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067789):
If you really want infix notation in the statement

#### [Mario Carneiro (May 25 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067790):
that doesn't solve the problem I just mentioned though

#### [Johan Commelin (May 25 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067797):
Hmmm, so why can't `simp` use the former? (Newbie alert!)

#### [Mario Carneiro (May 25 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067800):
the expression `?M1 x ?M2` matches almost anything

#### [Mario Carneiro (May 25 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067835):
because you can have some lambda term for `?M1`

#### [Mario Carneiro (May 25 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067842):
unification up to beta reduction is called higher order unification and it's undecidable

#### [Mario Carneiro (May 25 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067843):
and lean only does a very limited subset of it

#### [Johan Commelin (May 25 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067849):
Ok, so then we don't have `simp` for abstract groups.

#### [Mario Carneiro (May 25 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067850):
sad face

#### [Johan Commelin (May 25 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067851):
But as soon as you are in a multiplicate of additive setting, you have it back

#### [Mario Carneiro (May 25 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067854):
then I always want to be in a multiplicative or additive setting

#### [Johan Commelin (May 25 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067855):
and if inside the proof you do the `have instance` thing that I suggested above, then you also have it back (I hope)

#### [Johan Commelin (May 25 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067895):
So (I hope, once again) inside proofs you can always assume that you are inside the multiplicative setting

#### [Johan Commelin (May 25 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067898):
even if you prove something for an abstract group

#### [Mario Carneiro (May 25 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067908):
no, you still have that `simp` can only *use* groups with notation regardless of whether the goal uses notation

#### [Johan Commelin (May 25 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067918):
Yes, but you will *have* a group with notation. Because the first thing you prove inside your proof is that you have notation. And then you continue with the actual proof.

#### [Johan Commelin (May 25 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067957):
I really hope something like that is possible

#### [Mario Carneiro (May 25 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067959):
I mean, if you have a theorem whose statement is neutral but whose proof uses notation, it can't be used with simp

#### [Johan Commelin (May 25 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067961):
Hmmz, that is very sad

#### [Mario Carneiro (May 25 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067962):
because only the statement matters for simp

#### [Johan Commelin (May 25 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067971):
But you can change the statement inside the proof, right? By some `apply to_multiplicative`, or something

#### [Mario Carneiro (May 25 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067975):
So I just use multiplicative notation for "generic" group theory, and use `multiplicative` for transferring to additive

#### [Mario Carneiro (May 25 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068019):
I don't see any reason to avoid some kind of primacy between the notations

#### [Johan Commelin (May 25 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068020):
Ok, maybe I just need to get used to that (-;

#### [Johan Commelin (May 25 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068042):
But let me try to understand Lean better: if I have a "generic" statement, and I start my proof with `apply multiplicative`. Would I be able to use `simp` after that?

#### [Mario Carneiro (May 25 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068094):
`simp` can be used on any statement, but it can only use simp lemmas that are stated with notation

#### [Mario Carneiro (May 25 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068133):
I guess if you want to use `simp` on a generic statement you will need to change your goal to one that uses notation for the lemmas to match though

#### [Johan Commelin (May 25 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068143):
Right, and I think a tactic could do that change for me

#### [Mario Carneiro (May 25 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068145):
yes

#### [Mario Carneiro (May 25 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068152):
no such tactic exists, but it could be done

#### [Johan Commelin (May 25 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068154):
Great. Then I prefer that approach to group theory. But I respect your choice.

#### [Johan Commelin (May 25 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068160):
It would solve all the `group_hom` hassle

#### [Johan Commelin (May 25 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068161):
I think in the end, the code would be shorter, less duplication, and less `multiplicative` for end users.

#### [Mario Carneiro (May 25 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068162):
but it would still have the problem of not being registerable with simp, as a lemma on its own right

#### [Johan Commelin (May 25 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068202):
True, but I believe that the bulk of generic group theory is not simp lemmas

#### [Johan Commelin (May 25 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068205):
So we would need to state a couple of simp lemmas for groups with notation.

#### [Johan Commelin (May 25 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068212):
We don't want the five lemma to be a simp lemma, right?

#### [Mario Carneiro (May 25 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068214):
more complicated theorems, proving existence of things or what not, can often be opened up to defeq anyway so it doesn't matter

#### [Johan Commelin (May 25 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068216):
But I wouldn't mind if end users could use it, without figuring out to which of the 10 groups they first need to apply `multiplicative`

#### [Mario Carneiro (May 25 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068266):
Why don't you just state a version where everything is group, and another where everything is add_group, and let users deal with it themselves if they have mixed groups

#### [Johan Commelin (May 25 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068274):
Because I really think that means I won't have many users...

#### [Johan Commelin (May 25 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068287):
The conversion between `group` and `add_group` should be completely transparent

#### [Johan Commelin (May 25 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068299):
Otherwise we won't convert much mathematicians to formalisation

#### [Mario Carneiro (May 25 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068346):
Not completely transparent, if it's too transparent then `*` and `+` become the same and that's bad

#### [Mario Carneiro (May 25 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068348):
it's really not an easy problem

#### [Mario Carneiro (May 25 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068356):
I think `multiplicative` strikes the right balance, you have to explicitly state what you want but otherwise lean does the proof for free

#### [Johan Commelin (May 25 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068370):
Hmmm, would still like to have groups without notation

#### [Mario Carneiro (May 25 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068371):
why?

#### [Mario Carneiro (May 25 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068397):
it's not easier to read

#### [Mario Carneiro (May 25 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068412):
it's not easier to use

#### [Mario Carneiro (May 25 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068415):
the names are less obvious

#### [Johan Commelin (May 25 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068416):
For the generic theorems. Because those can be applied transparently to both settings

#### [Mario Carneiro (May 25 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068418):
I see no advantages

#### [Mario Carneiro (May 25 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068425):
it can't be applied transparently though

#### [Johan Commelin (May 25 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068426):
I think they are just as easy to use (or easier, in the mixed setting).

#### [Mario Carneiro (May 25 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068433):
it is as easy to apply a neutral theorem to an additive setting as it is to apply a multiplicative theorem in an additive setting

#### [Johan Commelin (May 25 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068434):
If every `add_group` is an instance of `generic_group`, and I prove the five lemma for generic groups, then I can just apply it to additive groups, right?

#### [Johan Commelin (May 25 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068435):
Without any `multiplicative` stuff

#### [Johan Commelin (May 25 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068479):
You see, when I have my mathematician hat on I never think about whether my group is additive or multiplicative. I just use it. And I just use theorems. And it works.

#### [Mario Carneiro (May 25 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068491):
I never had to deal with this in metamath either

#### [Johan Commelin (May 25 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068492):
So I don't want end users to have to figure out themselves where they need to use `multiplicative` to make some generic theorem work

#### [Kenny Lau (May 25 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068493):
```quote
You see, when I have my mathematician hat on I never think about whether my group is additive or multiplicative. I just use it. And I just use theorems. And it works.
```
hear hear

#### [Mario Carneiro (May 25 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068496):
it was all local notation

#### [Kenny Lau (May 25 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068497):
we do have an algebra hierarchy that mario doesn't use though

#### [Kenny Lau (May 25 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068498):
in that hierarchy this problem is avoided, I think

#### [Mario Carneiro (May 25 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068537):
Leo has his own ideas about generic groups. Like I said, this issue has a long history

#### [Mario Carneiro (May 25 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068539):
The core lean impl is unfinished though, maybe lean 4 will have something workable

#### [Mario Carneiro (May 25 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068588):
Honestly I have had more conversations on this topic than I would like, and things have not changed as a result

#### [Mario Carneiro (May 25 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068601):
I just want to prove theorems and use what's there

#### [Johan Commelin (May 25 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068613):
Ok. Got that.

#### [Johan Commelin (May 25 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068617):
I really don't want to start any fights of course. I really love what you have done so far.

#### [Mario Carneiro (May 25 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068660):
I don't mean to be short with you, but everyone has an idea and every solution has pros and cons

#### [Mario Carneiro (May 25 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068669):
I would suggest not entering the ring unless you have a large amount of testing to support your claims

#### [Johan Commelin (May 25 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068765):
Yeah, that's good advice.

#### [Kevin Buzzard (May 26 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127104639):
```quote
I don't see any reason to avoid some kind of primacy between the notations
```
This is a concept alien to mathematicians, that's why Johan is talking about it. But, like division by zero, it's just something we have to learn.

#### [Kevin Buzzard (May 26 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127104713):
They have different customs here.

#### [Patrick Massot (Jul 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/129399170):
Did we get anywhere with this additive group homs thread? @**Mario Carneiro** what is the definition you recommend in the end?

