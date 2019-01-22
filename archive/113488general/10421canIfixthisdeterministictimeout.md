---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/10421canIfixthisdeterministictimeout.html
---

## [general](index.html)
### [can I fix this deterministic timeout?](10421canIfixthisdeterministictimeout.html)

#### [Kevin Buzzard (May 09 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334659):
I am in the middle of a long proof and finding it hard to shorten. I have a hypothesis H3 in my local context. I have a killer theorem which I want to apply, which takes 11 inputs (it's one of these obvious-to-a-mathematician statements of the form "if something happens, then when you replace everything by something equiv to it then it still happens). I want one of the inputs to be H3, but if I put H3 into it then I get a deterministic timeout. Instead I write (_ : [type of H3]) as an input and then I get an extra goal, which I can clear with `exact H3`.

#### [Kevin Buzzard (May 09 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334716):
Am I missing a trick here? Am I likely to have made an error? I am not sure I can minimise.

#### [Mario Carneiro (May 09 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334730):
that's a bit vague. does `by exact H3` work?

#### [Kevin Buzzard (May 09 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334745):
I know it's vague, but deterministic timeouts are a big vague too :-/

#### [Mario Carneiro (May 09 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334754):
is the type of H3 exactly the same as the expected type?

#### [Kevin Buzzard (May 09 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334808):
I believe so

#### [Kevin Buzzard (May 09 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334811):
`by exact H3` doesn't work

#### [Kevin Buzzard (May 09 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334814):
in the sense that I still get the timeout

#### [Kevin Buzzard (May 09 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334827):
`  have H3 : (Π (i : γ), loc Rr (powers (f i))) ≃ Π (i : γ), loc R (non_zero_on_U (Ui i)) := equiv.prod H2,`

#### [Kevin Buzzard (May 09 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334848):
[is equiv.prod already there, by the way? If X i equiv Y i for all i then prod_i X i = prod_i Y i]

#### [Mario Carneiro (May 09 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334861):
`Pi_congr_right`

#### [Kevin Buzzard (May 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334873):
and ` (H3 : ((Π (i : γ), loc Rr (powers (f i))) ≃ (Π (i : γ), loc R (non_zero_on_U (Ui i))))) ` as my input gives me a timeout

#### [Mario Carneiro (May 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334919):
`prod` is the binary product

#### [Kevin Buzzard (May 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334923):
thanks

#### [Kevin Buzzard (May 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334927):
that would be why I couldn't find it ;-)

#### [Kevin Buzzard (May 09 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334945):
I should say that one can't determine the type of H3 immediately, type class inference is doing a lot of work here

#### [Mario Carneiro (May 09 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334953):
I'm afraid this is a little too restricted to get the full picture

#### [Kevin Buzzard (May 09 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334954):
I have about 15 implicit inputs as well as about 10 explicit ones

#### [Mario Carneiro (May 09 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335008):
I suggest leaving this for later then, `refine` with a `_` and then insert it after the unification works

#### [Kevin Buzzard (May 09 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335023):
yes this works fine

#### [Kevin Buzzard (May 09 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335029):
Here's the function I'm trying to apply

#### [Kevin Buzzard (May 09 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335030):
`fourexact_from_iso_to_fourexact :
  ∀ {A B C A' B' C' : Type u_1} [_inst_1 : add_comm_group A] [_inst_2 : add_comm_group A']
  [_inst_3 : add_comm_group B] [_inst_4 : add_comm_group B'] [_inst_5 : add_comm_group C] [_inst_6 : add_comm_group C']
  (ab : A → B) [_inst_7 : is_add_group_hom ab] (bc : B → C) [_inst_8 : is_add_group_hom bc],
    (∀ (b : B), bc b = 0 → (∃! (a : A), ab a = b)) →
    ∀ (fa : A ≃ A') [_inst_9 : is_add_group_hom ⇑fa] (fb : B ≃ B') [_inst_10 : is_add_group_hom ⇑fb]
    (fc : C ≃ C') [_inst_11 : is_add_group_hom ⇑fc] (ab' : A' → B') [_inst_12 : is_add_group_hom ab']
    (bc' : B' → C') [_inst_13 : is_add_group_hom bc'],
      (∀ (a : A), ⇑fb (ab a) = ab' (⇑fa a)) →
      (∀ (b : B), ⇑fc (bc b) = bc' (⇑fb b)) → ∀ (b' : B'), bc' b' = 0 → (∃! (a' : A'), ab' a' = b')`

#### [Kevin Buzzard (May 09 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335088):
I have 13 things which need to be inferred by type class inference because someone somewhere decided that `add_comm_group` and `is_add_group_hom` were type classes

#### [Kevin Buzzard (May 09 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335099):
and I have six add_comm_groups

#### [Mario Carneiro (May 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335108):
I assume all those searches are trivial though, right?

#### [Kevin Buzzard (May 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335109):
and I want Lean to infer them from things like `ab` and `fb` etc

#### [Kevin Buzzard (May 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335116):
yes everything should be trivial

#### [Kevin Buzzard (May 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335117):
oh

#### [Kevin Buzzard (May 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335119):
let me rephrase

#### [Kevin Buzzard (May 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335120):
that

#### [Mario Carneiro (May 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335124):
like they are in the context

#### [Kevin Buzzard (May 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335126):
I have no idea whether these searches are trivial

#### [Kevin Buzzard (May 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335129):
I doubt they're in the context

#### [Kevin Buzzard (May 09 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335179):
I could easily put them in with `by apply_instance`

#### [Kevin Buzzard (May 09 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335183):
If I put them in the context, will type class inference pick them up? I thought not

#### [Mario Carneiro (May 09 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335185):
I suggest you have a type for group isos instead of `(fa : A ≃ A') [_inst_9 : is_add_group_hom ⇑fa] `

#### [Kevin Buzzard (May 09 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335190):
I have a type for R-algebra isos ;-)

#### [Kevin Buzzard (May 09 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335208):
and instances which give me the equiv and the add_group_hom

#### [Kevin Buzzard (May 09 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335210):
but I'm letting type class inference do all of this

#### [Kevin Buzzard (May 09 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335264):
This whole experience has been extremely hard going, by the way.

#### [Kevin Buzzard (May 09 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335267):
I've had to set that other parameter which causes me trouble up to 100

#### [Mario Carneiro (May 09 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335269):
I suggest you apply this theorem by writing `apply fourexact_from_iso_to_fourexact ... bc'` giving all the function arguments, and then prove the remaining goals

#### [Kevin Buzzard (May 09 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335271):
yes that's exactly what I'm doing

#### [Kevin Buzzard (May 09 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335276):
it avoids the time out

#### [Kevin Buzzard (May 09 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335279):
It does mean that all of a sudden I go from 1 goal to 11

#### [Kevin Buzzard (May 09 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335287):
I have `set_option class.instance_max_depth 100` too

#### [Kevin Buzzard (May 09 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335317):
and all I am doing is proving something which is so trivial that it is not even explicitly mentioned in the stacks project

#### [Mario Carneiro (May 09 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335330):
An alternative is `have := fourexact_from_iso_to_fourexact ... bc' ` then `refine this ...` with the remaining args

#### [Kevin Buzzard (May 09 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335333):
I have a workaround

#### [Kevin Buzzard (May 09 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335336):
I was just wondering what was happening

#### [Kevin Buzzard (May 09 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335342):
I was going to take the 11 goals

#### [Kevin Buzzard (May 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335353):
and then solve them all in squiggly brackets with "show" at the top of each one

#### [Mario Carneiro (May 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335355):
This theorem is more complicated than it needs to be btw

#### [Kevin Buzzard (May 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335359):
I know full well

#### [Mario Carneiro (May 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335360):
you don't need any groups at all

#### [Kevin Buzzard (May 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335362):
because it's all trivial

#### [Kevin Buzzard (May 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335366):
and your silly system doesn't know this

#### [Mario Carneiro (May 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335368):
the statement is just about functions

#### [Mario Carneiro (May 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335369):
so all the TC args can go away

#### [Kevin Buzzard (May 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335370):
TC?

#### [Mario Carneiro (May 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335372):
typeclass

#### [Kevin Buzzard (May 09 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335416):
yes you're right

#### [Kevin Buzzard (May 09 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335419):
It's a statement about pointed sets

#### [Kevin Buzzard (May 09 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335421):
Are there pointed sets in Lean?

#### [Kevin Buzzard (May 09 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335433):
I've been carrying the group homs around because in practice one uses some algebra to prove the diagram commutes -- "both maps are the unique group hom with some property" etc.

#### [Kevin Buzzard (May 09 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335436):
You need a zero though, to define kernel

#### [Mario Carneiro (May 09 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335437):
Floris knows a lot about pointed sets in lean

#### [Kevin Buzzard (May 09 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335438):
But you don't need anything else

#### [Kevin Buzzard (May 09 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335440):
I'll rephrase it in terms of pointed sets

#### [Kevin Buzzard (May 09 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335480):
and then someone will make [is_pointed_set_hom] a typeclass

#### [Kevin Buzzard (May 09 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335482):
and I'll be back to square one ;-)

#### [Kevin Buzzard (May 09 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335483):
So it's not just about functions in fact

#### [Kevin Buzzard (May 09 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335485):
I need that a kernel maps to a kernel

#### [Mario Carneiro (May 09 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335486):
For your purposes I would just take the pointedness assumption as an argument

#### [Kevin Buzzard (May 09 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335488):
so I need that 0 maps to 0

#### [Kevin Buzzard (May 09 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335501):
I need that my equivs are equivs of pointed sets

#### [Mario Carneiro (May 09 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335571):
You should study how the `transfer` tactic works, even if you don't use the tactic the supporting theorems may be of use to you

#### [Kevin Buzzard (May 09 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335843):
I am solving my 11 goals and I think I located the reason for the time-out. If I put `H3` explicitly into the system then type class inference tries to prove it's a group hom and type class inference isn't very good at this sort of thing in my experience.

#### [Kevin Buzzard (May 09 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335852):
Ever since I've been trying to use type class inference to prove things are group homs / ring homs etc, I've been having trouble.

#### [Kevin Buzzard (May 09 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335860):
I've now realised that this is just another one of my type class woes

#### [Kevin Buzzard (May 09 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335920):
```lean
  show is_add_group_hom H3',
    apply_instance,
```

#### [Kevin Buzzard (May 09 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335929):
There's the time-out. So your instinct was right

#### [Kevin Buzzard (May 09 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335931):
Thanks.

#### [Kevin Buzzard (May 09 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335940):
It's a product of group homs

#### [Kevin Buzzard (May 09 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335954):
and maybe there's no instance that if X i -> Y i is a group hom for all i then Pi i, X i -> Pi i, Y i is a group hom

#### [Mario Carneiro (May 09 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126336362):
that one is up to you, I don't think `is_add_group_hom` even exists in mathlib

#### [Mario Carneiro (May 09 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126336409):
but you have to show that `Pi_congr_right` as defined respects the Pi group structure

#### [Kevin Buzzard (May 10 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126337259):
I have type class inference issues :-(

#### [Kevin Buzzard (May 10 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126337281):
How do I say "for all i, the proof (e i) of equiv (X i) (Y i) is a ring hom" (say)

#### [Kevin Buzzard (May 10 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126337291):
in the sense that I want that to be the assumption, inferred by type class inference

#### [Kevin Buzzard (May 10 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126337294):
This has nothing to do with equiv.

#### [Kevin Buzzard (May 10 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126337333):
Let me formulate something easier, and in the correct thread.

#### [Mario Carneiro (May 10 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126337602):
It's just `\forall i, is_ring_hom (e i)`

#### [Kevin Buzzard (May 10 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126337667):
It was getting it in the brackets I was worried about

#### [Kevin Buzzard (May 10 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126337670):
But `[∀ (i : γ), ring (F i)]` works fine

#### [Kevin Buzzard (May 10 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126337671):
I've never seen that construction before

#### [Kevin Buzzard (May 10 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126337681):
Thanks as ever. I'm back on track!

#### [Patrick Massot (May 10 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353221):
@**Kevin Buzzard** You should start reading from https://github.com/leanprover/mathlib/blob/master/algebra/pi_instances.lean#L61

#### [Patrick Massot (May 10 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353227):
and add things if needed

#### [Kevin Buzzard (May 10 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353552):
We use this stuff in the schemes work.

#### [Kevin Buzzard (May 10 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353555):
But it's only objects.

#### [Kevin Buzzard (May 10 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353556):
I now realise we need the morphisms too.

#### [Kevin Buzzard (May 10 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353562):
Currently my impression is that the morphisms which are classes are kind of random, and not all are classes.

#### [Kevin Buzzard (May 10 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353613):
For morphisms, I find myself needing both "if $$X \to Y_i$$ are group homs, then $$X \to \Pi_i Y_i$$ is"

#### [Kevin Buzzard (May 10 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353619):
and "if $$X_i\to Y_i$$ are group homs, then $$\Pi_i X_i \to \Pi_i Y_i$$ is too"

#### [Kevin Buzzard (May 10 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353780):
It was these instances that caused the time-out :-)

#### [Kevin Buzzard (May 10 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353781):
It knew that the product of groups was a group and then timed out trying to prove using type class inference only that the product of the morphisms was a morphism

#### [Mario Carneiro (May 10 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353850):
how are those functions being specified?

#### [Mario Carneiro (May 10 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353853):
you wrote the type but not the term there

#### [Patrick Massot (May 10 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353929):
Then I'm confused. How could you write: "`[∀ (i : γ), ring (F i)]` I've never seen that construction before"

#### [Patrick Massot (May 10 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353979):
Anyway, I think having Lean figuring out by itself that composition and products of morphisms are morphisms is a good reason to try to use type class here.  But you need to add instances to that `pi_instance` file, which was written at a time were morphisms were defs

#### [Patrick Massot (May 10 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353984):
That may require improving Simon's `pi_instance` tactic

#### [Patrick Massot (May 10 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353986):
I'm not sure

#### [Kevin Buzzard (May 10 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354452):
```quote
how are those functions being specified?
```
There's only one sensible specification in each case. I just noticed that the Android Zulip app doesn't do maths mode.

#### [Kevin Buzzard (May 10 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354495):
```quote
Then I'm confused. How could you write: "`[∀ (i : γ), ring (F i)]` I've never seen that construction before"
```
I glanced at the Pi file at the time, realised I understood what it did, forgot how it did it, then had to do it myself. Patrick I'm nearly 50. It's completely consistent that I have to write `[∀ (i : γ), ring (F i)]` again in two months' time and again claim that I've never seen it before.

#### [Kevin Buzzard (May 10 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354504):
I mean "...according to my memory banks" :-)

#### [Kevin Buzzard (May 10 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354551):
It's pretty depressing. Sometimes I want to know something about some technical number theory question so I google, find a good mathoverflow answer, read it, learn a lot, and then discover to my surprise that I had written the answer myself 5 years ago. The first time that happened to me was a genuine shock. Now I just consider it normal.

#### [Kevin Buzzard (May 10 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354556):
It's not depressing at all -- it's pretty funny :-)

#### [Mario Carneiro (May 10 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354687):
> There's only one sensible specification in each case.

Not quite: are you giving an explicit lambda term or a definition?

#### [Kevin Buzzard (May 10 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354747):
I don't understand the subtlety you've found, but what I am saying is that I need the following two facts:

#### [Mario Carneiro (May 10 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354750):
I'm just asking what you wrote

#### [Mario Carneiro (May 10 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354769):
the typeclass system is trying to solve `is_add_group_hom ...`; what is in the place of the `...`?

#### [Mario Carneiro (May 10 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354775):
the typeclass system is very sensitive to the way you write things

#### [Kevin Buzzard (May 10 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354778):
(1) If gamma is a type and for all i in gamma I have (f i : X -> Y i), which type class inference knows is a group hom (actually in my case this one was a ring hom) then the induced map from X to Pi i, Y i sending x i to f i (x) is a group hom

#### [Mario Carneiro (May 10 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354787):
> the induced map from X to Pi i, Y i sending x i to f i (x)

and how did you write that

#### [Kevin Buzzard (May 10 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354850):
`\lam x i,f i x` I guess

#### [Mario Carneiro (May 10 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354851):
did you prove that in a lemma?

#### [Kevin Buzzard (May 10 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354854):
I proved it in an instance

#### [Mario Carneiro (May 10 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354856):
show me

#### [Kevin Buzzard (May 10 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354862):
well I didn't yet

#### [Kevin Buzzard (May 10 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354863):
are you saying I'm going to run into trouble?

#### [Kevin Buzzard (May 10 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354864):
I proved the other one

#### [Mario Carneiro (May 10 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354866):
well if the instance isn't there of course it will fail

#### [Mario Carneiro (May 10 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354868):
but yes, that instance is trouble

#### [Mario Carneiro (May 10 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354870):
you want to wrap that function in a definition

#### [Kevin Buzzard (May 10 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354872):
Oh

#### [Kevin Buzzard (May 10 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354873):
Here's the one I did

#### [Kevin Buzzard (May 10 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354894):
```lean
instance Prod {γ : Type u} {F : γ → Type u} {G : γ → Type u} [∀ i, add_group (F i)]
[∀ i, add_group (G i)] (H : ∀ i : γ, F i → G i) [∀ i, is_add_group_hom (H i)] :
 is_add_group_hom (λ Fi i, H i (Fi i) : (Π i, F i) → Π i, G i) := ⟨λ a b, funext $ λ i,
show H i ((a i) + (b i)) = H i (a i) + H i (b i),
by rw (add (H i))⟩
```

#### [Kevin Buzzard (May 10 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354915):
You don't know the type class I'm using here

#### [Kevin Buzzard (May 10 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354919):
```lean
def is_add_group_hom {α : Type u} {β : Type v} [add_group α] [add_group β] (f : α → β) : Prop :=
@is_group_hom (multiplicative α) (multiplicative β) _ _ f
```

#### [Kevin Buzzard (May 10 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354924):
```lean
theorem add (x y) : f (x + y) = f x + f y :=
@is_group_hom.mul (multiplicative α) (multiplicative β) _ _ f hf x y
```

#### [Kevin Buzzard (May 10 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354926):
Are there problems with this?

#### [Mario Carneiro (May 10 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354934):
this is bad: `is_add_group_hom (λ Fi i, H i (Fi i))`

#### [Kevin Buzzard (May 10 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354935):
Hmm

#### [Kevin Buzzard (May 10 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354936):
Well thanks for spotting this

#### [Mario Carneiro (May 10 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354937):
it's okay as a def but as an instance it requires higher order unification

#### [Kevin Buzzard (May 10 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354938):
On the other hand

#### [Kevin Buzzard (May 10 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354982):
these morphisms between mathematical objects are being defined to be type classes

#### [Kevin Buzzard (May 10 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354990):
so I am being pushed to use the type class inference system

#### [Mario Carneiro (May 10 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354991):
you just need to define `Pi_lift H := λ Fi i, H i (Fi i` and give that the instance

#### [Kevin Buzzard (May 10 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354993):
Oh so I can still use type class inference

#### [Mario Carneiro (May 10 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355001):
the typeclass system needs a constant to key on

#### [Kevin Buzzard (May 10 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355005):
This is of course the problem with me using things I don't understand completely

#### [Kevin Buzzard (May 10 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355008):
It's exactly what I tell my graduate students not to do

#### [Kevin Buzzard (May 10 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355045):
I don't know what "constant" or "key on" mean in your last post

#### [Mario Carneiro (May 10 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355051):
for example if you want to show `is_group_hom (f o g)` it's no problem but `is_group_hom (\lam x, f (g x))` is not likely to work

#### [Kevin Buzzard (May 10 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355055):
*boggle*

#### [Sean Leather (May 10 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355056):
Mario probably means a unique definition name.

#### [Sean Leather (May 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355059):
`function.compose` in that case.

#### [Kevin Buzzard (May 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355062):
I just spent some time changing f circ g's to lam x, f (g x) because Kenny told me that things were better that way

#### [Kevin Buzzard (May 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355069):
in the sense that they were easier to work with

#### [Kenny Lau (May 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355070):
```quote
I just spent some time changing f circ g's to lam x, f (g x) because Kenny told me that things were better that way
```
you see, things have a context

#### [Mario Carneiro (May 10 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355071):
That's true for the most part, but if it shows up as the target of a typeclass problem you want it to be "obviously a morphism"

#### [Kenny Lau (May 10 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355112):
```quote
for example if you want to show `is_group_hom (f o g)` it's no problem but `is_group_hom (\lam x, f (g x))` is not likely to work
```
but aren't they definitionally equivalent?

#### [Mario Carneiro (May 10 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355113):
and that means writing things functorially

#### [Mario Carneiro (May 10 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355116):
they are, but typeclass inference doesn't work up to definitional equivalence

#### [Kevin Buzzard (May 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355122):
I wonder if this has anything to do with the fact that three times now I've had to `set_option class.instance_max_depth 100`

#### [Mario Carneiro (May 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355123):
it's doing a big search through the whole library. It doesn't have time to unify everything properly

#### [Kenny Lau (May 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355124):
what do they work up to?

#### [Mario Carneiro (May 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355136):
unification of metavariables unfolding reducibles only

#### [Kevin Buzzard (May 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355141):
I want to give hints to the system

#### [Kenny Lau (May 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355142):
is that another type of equivalence?

#### [Kevin Buzzard (May 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355145):
because in every case I know exactly what I want it to do

#### [Mario Carneiro (May 10 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355189):
it's almost syntactic equality, except that reducible definitions are eagerly expanded

#### [Kevin Buzzard (May 10 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355191):
In some cases it's even "I want you to use precisely the instance which I just defined in another file precisely so that this next line will work"

#### [Mario Carneiro (May 10 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355201):
the key is to write the typeclass problem so that it's obvious to the system

#### [Mario Carneiro (May 10 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355208):
that basically means that all your typeclass instances should have the form `my_class (my_operation A B C)`

#### [Kevin Buzzard (May 10 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355209):
To put this into some context, the fact that the product of group homs is a group hom is the sort of thing which is explained in an undergraduate maths lecture in the 15 minute period just after the definition of a group hom has been given, and is then never mentioned again and everyone thinks it's obvious

#### [Mario Carneiro (May 10 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355248):
with some assumptions like `my_class A` `my_class2 B`

#### [Mario Carneiro (May 10 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355249):
and your typeclass problems should look like `my_class (my_op (my_other_op A) B)`

#### [Mario Carneiro (May 10 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355250):
no lambdas

#### [Kevin Buzzard (May 10 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355259):
Well this is very helpful. Whereabouts is all this documented? ;-)

#### [Sean Leather (May 10 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355260):
Look up. :arrow_up: :wink:

#### [Kevin Buzzard (May 10 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355303):
I don't know why I'm bothering writing docs, I could just refer people to https://leanprover.zulipchat.com/

#### [Sean Leather (May 10 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355314):
TBD: The [type class reference section](https://leanprover.github.io/reference/declarations.html#type-classes) is currently empty.

#### [Kevin Buzzard (May 10 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355316):
Oh, on a related topic, why `Pi_congr_right`?

#### [Kevin Buzzard (May 10 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355356):
I mean, why the name?

#### [Kevin Buzzard (May 10 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355357):
`equiv.Pi_congr_right :
  Π {α : Sort u_3} {β₁ : α → Sort u_4} {β₂ : α → Sort u_5},
    (Π (a : α), β₁ a ≃ β₂ a) → ((Π (a : α), β₁ a) ≃ Π (a : α), β₂ a)`

#### [Kevin Buzzard (May 10 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355359):
That looks like `equiv.Pi` to me

#### [Kevin Buzzard (May 10 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355360):
modulo the fact that that name is probably illegal

#### [Kevin Buzzard (May 10 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355407):
but I don't see anything `right` about it, other than the fact that it's right

#### [Kevin Buzzard (May 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355562):
Are these fundamental constructions already in Lean:

#### [Kevin Buzzard (May 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355566):
```lean
definition Pi_lift₁ {γ : Type u} {F : γ → Type u} {G : γ → Type u} 
  (H : ∀ i : γ, F i → G i) : (Π i, F i) → Π i, G i := λ Fi i, H i (Fi i)

definition Pi_lift₂ {γ : Type u} {X : Type u} {G : γ → Type u} 
  (H : ∀ i : γ, X → G i) : X → Π i, G i := λ x i, H i x
```

#### [Mario Carneiro (May 10 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355579):
Pi takes two arguments

#### [Mario Carneiro (May 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355606):
a domain and a family

#### [Mario Carneiro (May 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355620):
Pi_congr_left is likely to be much messier though so I left it out

#### [Kevin Buzzard (May 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355632):
So is the following now OK:

#### [Kevin Buzzard (May 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355671):
```lean
instance is_add_group_hom.Pi_lift {γ : Type u} {F : γ → Type u} {G : γ → Type u} [∀ i, add_group (F i)]
[∀ i, add_group (G i)] (H : ∀ i : γ, F i → G i) [∀ i, is_add_group_hom (H i)] :
 is_add_group_hom (Pi_lift_map₁ H) := ⟨λ a b, funext $ λ i,
show H i ((a i) + (b i)) = H i (a i) + H i (b i),
by rw (add (H i))⟩
```

#### [Mario Carneiro (May 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355673):
yep that's ok

#### [Kevin Buzzard (May 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355683):
Can you appreciate that this is a subtlety that people are unlikely to guess, and it's up to the very few people who appreciate the subtlety to somehow get the news around? :-/

#### [Mario Carneiro (May 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355684):
certainly

#### [Kevin Buzzard (May 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355685):
I don't recall this being mentioned in TPIL

#### [Kevin Buzzard (May 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355686):
although as we've seen earlier in this thread, that's not saying much

#### [Kevin Buzzard (May 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355727):
I guess I felt the same way about `simp` earlier on.

#### [Mario Carneiro (May 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355728):
In a way, it's "your fault" in generalizing from "typeclasses can do X" to "typeclasses can do Y"

#### [Kevin Buzzard (May 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355729):
I would tag arbitrary things with simp and then had to be rolled back by people that actually knew what simp did

#### [Kevin Buzzard (May 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355730):
I mean, by people who knew _how simp actually worked_

#### [Kevin Buzzard (May 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355731):
and I guess the same is happening here.

#### [Mario Carneiro (May 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355734):
everything has limitations, and most of the existing documentation is vague about where the limitations are

#### [Kevin Buzzard (May 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355738):
In maths, generalizing like that is a _really_ important skill

#### [Kevin Buzzard (May 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355739):
It's not so clear that such limitations exist in maths

#### [Kevin Buzzard (May 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355741):
If you understand the idea behind a proof

#### [Kevin Buzzard (May 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355742):
then you can see the same idea working in many other situations

#### [Mario Carneiro (May 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355743):
on the one hand, you can assume Leo is magic and made everything work (which is not an unreasonable rule of thumb)

#### [Kevin Buzzard (May 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355786):
I feel like I need you a huge amount less than I needed you last October

#### [Kevin Buzzard (May 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355787):
but I still need you from time to time :-)

#### [Kevin Buzzard (May 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355788):
Many thanks as ever

#### [Mario Carneiro (May 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355789):
but sometimes if you don't know you should stick to areas that you know how to use already... it's a balancing act

#### [Mario Carneiro (May 10 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355800):
I don't use `finish` or `cc` because I don't understand them well

#### [Kevin Buzzard (May 10 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355804):
Don't say that in front of your advisor

#### [Kevin Buzzard (May 10 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355805):
didn't he write at least one of them?

#### [Mario Carneiro (May 10 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355808):
yes, Jeremy wrote `finish`

#### [Mario Carneiro (May 10 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355855):
I'm not sure he understands it either, since it's a complicated set of heuristics calling in to less understood things like e-matching

#### [Kevin Buzzard (May 10 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355863):
My impression is that computer scientists are much better at generating work that they "don't understand"

#### [Kevin Buzzard (May 10 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355865):
much better than mathematicians, I mean

#### [Kevin Buzzard (May 10 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355869):
If I use theorem X whose proof I've not read, in my proof, then I can just argue that I have a complete understanding of "theorem X implies the result I proved"

#### [Kevin Buzzard (May 10 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355870):
and all proofs are irrelevant

#### [Mario Carneiro (May 10 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355910):
says the man who is rediscovering his own proofs every five years :)

#### [Kevin Buzzard (May 10 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355911):
:-)

#### [Kevin Buzzard (May 10 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355913):
That's how irrelevant they are :-)

#### [Kevin Buzzard (May 10 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355915):
I don't rediscover the proofs I created in my 20s and 30s, those are pretty much hard wired

#### [Kevin Buzzard (May 10 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355920):
It's the stuff I do in my 40s that I occasionally do again

#### [Kevin Buzzard (May 10 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355923):
This schemes code is getting quite unwieldy, and occasionally I prove some lemma and in the middle of the proof I think "I ran into this issue before, I think I already proved this lemma"

#### [Kevin Buzzard (May 10 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355925):
With the tag system I can really control well this sort of thing, most of the time

#### [Kevin Buzzard (May 10 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355969):
but when I go "off piste" because the tag says "this is now clear, as every mathematican knows" and Lean is saying "but the diagrams! You have to check they commute!" and I end up with 1000 lines of code checking a triviality, that's when I duplicate

#### [Kevin Buzzard (May 10 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126356137):
My esteemed co-author writes

#### [Kevin Buzzard (May 10 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126356138):
```lean
instance deus : comm_ring (α [1/S] /ᵣ (S⁻¹ I)) := by apply_instance
instance salva : module (α [1/S] /ᵣ (S⁻¹ I)) (α [1/S] /ᵣ (S⁻¹ I)) := ring.to_module
instance me : is_submodule (is_ring_hom.ker (to_be_named_aux3 S I)) := is_ring_hom.ker.is_submodule (to_be_named_aux3 S I)

```

#### [Kevin Buzzard (May 10 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126356147):
Are these OK (modulo the names)

#### [Kenny Lau (May 10 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126356199):
```quote
My esteemed co-author writes
```
right

#### [Mario Carneiro (May 10 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357426):
I would hope that `is_submodule (is_ring_hom.ker f)` always works

#### [Kevin Buzzard (May 10 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357465):
Kenny look how stupid type class inference is:

#### [Kevin Buzzard (May 10 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357470):
```lean
universe u
definition Pi_lift_map₁ {γ : Type u} {F : γ → Type u} {G : γ → Type u} 
  (H : ∀ i : γ, F i → G i) : (Π i, F i) → Π i, G i := λ Fi i, H i (Fi i)
  
class foomap {α β : Type u} (f : α → β) :=
(preserves_structure : ∀ a : α, f a = f a)

instance Pi_foomap_is_foomap {γ : Type u} {F : γ → Type u} {G : γ → Type u} 
(H : ∀ i : γ, F i → G i) [∀ i, foomap (H i)] : foomap (Pi_lift_map₁ H) := sorry

example {γ : Type u} {F : γ → Type u} {G : γ → Type u} 
(H : ∀ i : γ, F i → G i) [∀ i, foomap (H i)] : foomap (Pi_lift_map₁ H) := by apply_instance

example {γ : Type u} {F : γ → Type u} {G : γ → Type u} 
(H : ∀ i : γ, F i → G i) [∀ i, foomap (H i)] : foomap (λ Fi i, H i (Fi i) : (Π i, F i) → Π i, G i) := by apply_instance

```

#### [Mario Carneiro (May 10 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357471):
the `salva` instance is trouble

#### [Kevin Buzzard (May 10 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357473):
even though they're defeq

#### [Kevin Buzzard (May 10 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357481):
the last example fails

#### [Mario Carneiro (May 10 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357486):
It can be a local instance, but you don't necessarily want to always have that ring be a module over itself

#### [Kevin Buzzard (May 10 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357493):
I think this is because type class inference doesn't have a constant to key on

#### [Kevin Buzzard (May 10 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357497):
```quote
It can be a local instance, but you don't necessarily want to always have that ring be a module over itself
```
That ring _is_ always a module over itself, so what do you actually mean?

#### [Kevin Buzzard (May 10 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357615):
```lean

example {γ : Type u} {F : γ → Type u} {G : γ → Type u} 
(H : ∀ i : γ, F i → G i) [∀ i, foomap (H i)] : foomap (Pi_lift_map₁ H) := by apply_instance

example {γ : Type u} {F : γ → Type u} {G : γ → Type u} 
(H : ∀ i : γ, F i → G i) [∀ i, foomap (H i)] : (Pi_lift_map₁ H) = (λ Fi i, H i (Fi i) : (Π i, F i) → Π i, G i) := rfl

example {γ : Type u} {F : γ → Type u} {G : γ → Type u} 
(H : ∀ i : γ, F i → G i) [∀ i, foomap (H i)] : foomap (λ Fi i, H i (Fi i) : (Π i, F i) → Π i, G i) := by apply_instance -- fails


```

#### [Kevin Buzzard (May 10 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357617):
well I've learnt something today

#### [Mario Carneiro (May 10 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357680):
I mean that when you make it an instance you are saying "this is the only ring I want to consider this as a module over"

#### [Mario Carneiro (May 10 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357686):
because modules infer their ring argument from typeclass inference

#### [Mario Carneiro (May 10 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357727):
Any ring is a module over itself, but that doesn't mean that's the only ring you want to consider, for example R as a Q-module

#### [Johan Commelin (May 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357733):
But if you consider R as an R-module, and later you need it as Q-module, then this could be inferred by some statement about forgetting scalars, right?

#### [Johan Commelin (May 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357734):
Except that we might get a diamond...

#### [Mario Carneiro (May 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357735):
forgetting scalars?

#### [Johan Commelin (May 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357736):
From R to Q

#### [Mario Carneiro (May 10 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357778):
as in you want to compose with a ring hom?

#### [Johan Commelin (May 10 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357781):
Every R-module is a Q-module

#### [Johan Commelin (May 10 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357783):
That is what I mean

#### [Kevin Buzzard (May 10 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357785):
I can envisage your implied assertion that each abelian group can only be a module over one ring as being problematic

#### [Johan Commelin (May 10 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357786):
And somehow *newbie me* would wish that typeclass inference can do that for me

#### [Kevin Buzzard (May 10 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357787):
I just found something else problematic too

#### [Kevin Buzzard (May 10 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357792):
```lean
def Pi_congr_right {α} {β₁ β₂ : α → Sort*} (F : ∀ a, β₁ a ≃ β₂ a) : (Π a, β₁ a) ≃ (Π a, β₂ a) :=
⟨λ H a, F a (H a), λ H a, (F a).symm (H a),
 λ H, funext $ by simp, λ H, funext $ by simp⟩
```

#### [Kevin Buzzard (May 10 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357793):
That's your(?) definition of Pi_congr_right

#### [Kevin Buzzard (May 10 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357802):
but you did not use `definition Pi_lift_map₁ {γ : Type u} {F : γ → Type u} {G : γ → Type u} 
  (H : ∀ i : γ, F i → G i) : (Π i, F i) → Π i, G i := λ Fi i, H i (Fi i)`

#### [Johan Commelin (May 10 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357804):
Ok, I guess I don't understand typeclass inference... and what I mean is that I would like every R-module to automatically coerce to a Q-module when that's necessary

#### [Mario Carneiro (May 10 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357808):
of course not, you just wrote it

#### [Kevin Buzzard (May 10 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357853):
but I am using `Pi_congr_right` to construct my product instances

#### [Kevin Buzzard (May 10 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357855):
so now I can't use type class inference on them

#### [Mario Carneiro (May 10 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357858):
You will need a theorem saying that `\u Pi_congr_right ` is a group hom

#### [Mario Carneiro (May 10 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357860):
it's defeq to your other one about Pi_lift

#### [Kevin Buzzard (May 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357865):
I see, so I don't try and get you to rewrite Pi_congr_right

#### [Mario Carneiro (May 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357871):
right, that's too much for TC inference

#### [Mario Carneiro (May 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357879):
even if it was rewritten it wouldn't help

#### [Kevin Buzzard (May 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357881):
But am I safe making this an instance?

#### [Mario Carneiro (May 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357883):
yes

#### [Kevin Buzzard (May 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357887):
I mean the proof that \u= Pi_congr_right is a group

#### [Kevin Buzzard (May 10 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357927):
hom

#### [Kevin Buzzard (May 10 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357934):
OK I see.

#### [Kevin Buzzard (May 10 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357942):
@**Johan Commelin** I didn't think too hard about the module ring thing yet

#### [Kevin Buzzard (May 10 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357952):
but one funny thing about type classes is that if the devs deem a structure to be worthy of being called a class

#### [Kevin Buzzard (May 10 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357956):
then you are only supposed to ever have one instance of that class

#### [Kevin Buzzard (May 10 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357957):
I am not being very precise

#### [Kevin Buzzard (May 10 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357997):
I mean that if `group` is a class, and `G` is a type, then `H1 : group G` and `H2 : group G` are supposed to be equal

#### [Kevin Buzzard (May 10 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357998):
because otherwise how can type class inference decide whether you want to use `H1` or `H2`

#### [Kevin Buzzard (May 10 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358003):
So if you want more than one group structure on your type `G`, you have to jettison type classes

#### [Kevin Buzzard (May 10 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358006):
This happens in the topological space stuff in Lean -- a topological space is a structure

#### [Kevin Buzzard (May 10 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358009):
because Johannes wanted to put more than one topological space on a set so he could partially order them for some reason

#### [Kevin Buzzard (May 10 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358049):
But you can't edit the source, so a group is a class, so if there's more than one group structure on G then you have to go it alone

#### [Johan Commelin (May 10 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358050):
But there is only one instance of `module R R` right? So that shouldn't be the problem that Mario was talking about...

#### [Johan Commelin (May 10 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358055):
At the same time there could be an instance of `module Q R`

#### [Johan Commelin (May 10 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358056):
Or is that giving a conflict somewhere?

#### [Kevin Buzzard (May 10 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358057):
In semilinear algebra I've seen plenty of other ways of making R an R-module, but that's not the point right now ;-)

#### [Johan Commelin (May 10 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358064):
Right (-;

#### [Kevin Buzzard (May 10 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358065):
Let's have a look at `module`

#### [Johan Commelin (May 10 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358068):
Those shouldn't be instances... for a reason

#### [Kevin Buzzard (May 10 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358073):
I can't find it :-)

#### [Kevin Buzzard (May 10 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358109):
got it

#### [Kevin Buzzard (May 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358123):
yes module takes both the ring and the module as parameters

#### [Kevin Buzzard (May 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358124):
so I don't understand Mario's comment

#### [Kevin Buzzard (May 10 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358165):
```quote
because modules infer their ring argument from typeclass inference
```
It's this though

#### [Johan Commelin (May 10 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358176):
I'm still confused...

#### [Kevin Buzzard (May 10 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358179):
In the definition of `module` do you see `out_param`?

#### [Johan Commelin (May 10 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358217):
Yes

#### [Kevin Buzzard (May 10 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358227):
`out_param` is a great function, it is the identity function

#### [Kevin Buzzard (May 10 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358230):
but behind the scenes in the C++ code, type class inference is affected by `out_param`

#### [Johan Commelin (May 10 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358234):
Ouch... I'm being cheated again

#### [Kevin Buzzard (May 10 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358250):
That `out_param` mean in practice "if you give me a module, I'm going to try and guess the ring"

#### [Kevin Buzzard (May 10 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358294):
My guess is that this was written by people with some specific usage in mind, who did not talk to a professional ring theorist beforehand

#### [Johan Commelin (May 10 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358304):
So we might get rid of the `out_param` and hopefully stuff would be better?

#### [Johan Commelin (May 10 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358307):
Or will mathlib break?

#### [Kevin Buzzard (May 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358315):
As you know from the docs

#### [Kevin Buzzard (May 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358318):
(i.e the chat)

#### [Johan Commelin (May 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358320):
Haha: `docs = logs` is now an `axiom`?

#### [Kevin Buzzard (May 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358322):
there was some discussion about this at some point

#### [Kevin Buzzard (May 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358326):
Jan 19th on gitter between Mario and Sebastian

#### [Kevin Buzzard (May 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358328):
according to my logs

#### [Johan Commelin (May 10 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358370):
Ok, gitter is from before my time

#### [Kevin Buzzard (May 10 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358372):
I'll quote it

#### [Kevin Buzzard (May 10 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358377):
```
To review, the problem is that the definition:

class module (α : out_param $ Type u) (β : Type v) [out_param $ ring α]
  extends has_scalar α β, add_comm_group β :=
...

leads to a search problem in which ring ?M1 is solved before module ?M1 β, which leads to a loop when there is an instance like [ring A] [ring B] : ring (A x B)
I would like to make lean search for module ?M1 β only, obtaining α and the ring instance by unification
Johannes suggested using {out_param $ ring α} instead of [out_param $ ring α], but then it doesn't work as a typeclass, and all the multiplications etc in the theorem statements break
A possible solution is to skip out_param typeclass search problems until after all the others are solved

***

So the real issue is: You want the elaborator to handle applying a function {A B} [ring A] [module A B] (x : B) : ..., yes...?
Mario Carneiro
@digama0
Jan 19 10:10
yes
Sebastian Ullrich
@Kha
Jan 19 10:10
Where you want it to solve the second instance first, which fixes A and the first instance
```

#### [Kevin Buzzard (May 10 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358390):
Every now and again stuff like this happens and I become convinced that type class inference is too stupid to handle non-trivial maths stuff

#### [Kevin Buzzard (May 10 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358436):
There is this diamond catastrophe, today we learn that it doesn't work for things defeq to stuff that works etc etc

#### [Kevin Buzzard (May 10 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358441):
It is extremely delicate to get right

#### [Johan Commelin (May 10 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358442):
Yeah, I see that (-;

#### [Johan Commelin (May 10 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358445):
Anyway, lunch time over here... see you later!

#### [Kevin Buzzard (May 10 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358446):
but on the plus side, every time I run into an explicit problem Mario has some workaround

#### [Kevin Buzzard (May 10 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358605):
One instance for maps, one for equivs:

#### [Kevin Buzzard (May 10 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358606):
```lean
instance Pi_lift {γ : Type u} {F : γ → Type u} {G : γ → Type u} [∀ i, add_group (F i)]
[∀ i, add_group (G i)] (H : ∀ i : γ, F i → G i) [∀ i, is_add_group_hom (H i)] :
 is_add_group_hom (Pi_lift_map₁ H) := ⟨λ a b, funext $ λ i,
show H i ((a i) + (b i)) = H i (a i) + H i (b i),
by rw (add (H i))⟩

instance equiv.Pi_congr_right {γ : Type u} {F : γ → Type u} {G : γ → Type u} [∀ i, add_group (F i)]
[∀ i, add_group (G i)] (H : ∀ i : γ, F i ≃ G i) [∀ i, is_add_group_hom (H i)] :
 is_add_group_hom (equiv.Pi_congr_right H) := ⟨λ a b, funext $ λ i, 
 show H i ((a i) + (b i)) = H i (a i) + H i (b i),
by rw (add (H i))⟩
```

#### [Kevin Buzzard (May 10 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358607):
same proof

#### [Kevin Buzzard (May 10 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358608):
unsurprising because equivs are maps

#### [Kevin Buzzard (May 10 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358658):
[I'm in namespace is_add_group_hom]

#### [Kevin Buzzard (May 10 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358672):
but apparently I need both instances

#### [Kevin Buzzard (May 10 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358778):
I guess one thing I am unclear about is what is wrong with the following fix : I create a mathlib PR which adds the function `Pi_lift_map₁ H` which sends a product of maps to a map on the product and rewrites `equiv.Pi_congr_right` to use this function. I then delete my second instance and observe that type class inference should spot it. But Mario, I think, suggested that this would not work either.

#### [Kevin Buzzard (May 10 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358886):
and oh wow I now have my type class inference working, my time-out was indeed caused by type class inference failing, it now doesn't fail, and I can feed my parameters into my functions :-) So finally my initial problem is solved in the best possible way!

#### [Kevin Buzzard (May 10 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358942):
I want to argue that this is all about transport of structure. I'm switching to the canonical thread.

#### [Mario Carneiro (May 10 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126359245):
You don't need to reprove the theorem

#### [Kenny Lau (May 10 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126359246):
why is everyone using "reprove" to mean "prove again" lol

#### [Mario Carneiro (May 10 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126359259):
just define the `equiv.Pi_congr_right` instance to equal `Pi_lift`

#### [Johan Commelin (May 10 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126359452):
```quote
and oh wow I now have my type class inference working, my time-out was indeed caused by type class inference failing, it now doesn't fail, and I can feed my parameters into my functions :-) So finally my initial problem is solved in the best possible way!
```
Does it also solve your `max_depth` problem?

#### [Kevin Buzzard (May 10 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126365201):
unfortunately not, but I don't know what other terrible type class sins I have committed.

