---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79810maximumclassinstanceresolutiondepthhasbeenreached.html
---

## Stream: [general](index.html)
### Topic: [maximum class-instance resolution depth has been reached](79810maximumclassinstanceresolutiondepthhasbeenreached.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627176):
I was writing some random universal property code

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627183):
and I got the good old "maximum class-instance resolution depth has been reached" error

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627184):
and we all know what that means

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627185):
so I restarted Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627186):
and I got the error again.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627188):
*sigh*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627192):
so I guess I know what that means

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627194):
and I decided I'd made some sort of error with my types

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627201):
so I carefully wrote down the types of everything in my statement

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627202):
and managed to make sure that everything really had the type I thought it would have

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627203):
and I restarted Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627207):
and I got the error again.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627208):
*sigh*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627212):
The error in its Lean 3.4 form says

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627217):
```
maximum class-instance resolution depth has been reached (the limit can be increased by setting option 'class.instance_max_depth') (the class-instance resolution trace can be visualized by setting option 'trace.class_instances')
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627263):
so I figured that it was about time I read the error properly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627272):
and I realised it was hard for me to increase the max_depth

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627275):
because I didn't know what it currently was

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627285):
so I looked at the trace

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627288):
and it was really long

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627290):
and complicated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627294):
and I spent some time trying to understand it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627301):
and in total spent over half an hour on this issue

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627302):
before it occurred to me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627304):
that actually

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627307):
maybe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627313):
the maximum class-instance resolution depth *had* been reached!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627325):
So I wrote `set_option class.instance_max_depth 100`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627326):
and the error went away!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 24 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627387):
lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627390):
So I came to the conclusion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627397):
that either my code is really really cool and I am using type class resolution like a pro now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627398):
or

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627399):
maybe my code is really really bad

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627428):
and anyone who needs to change the default setting of the max class-instance resolution might want to take a look at what they're doing and how they're doing it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627491):
And one thing that occured to me was that I might be being sloppy with the difference between proofs and data

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627503):
but this might not be relevant, I'm not sure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627506):
Here's a structure:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627513):
```lean
-- Here is the way KMB wants to package all these things together.
structure is_unique_R_alg_hom {R : Type u} {α : Type v} {β : Type w} [comm_ring R] [comm_ring α] [comm_ring β] 
(sα : R → α) (sβ : R → β) (f : α → β) [is_ring_hom sα] [is_ring_hom sβ] [is_ring_hom f] :=
(R_alg_hom : sβ = f ∘ sα)
(is_unique : ∀ (g : α → β) [is_ring_hom g], sβ = g ∘ sα → g = f)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627516):
You make an instance of that structure by giving two proofs.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627567):
But the structure turns out to be a Type.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627576):
I could have rewritten this as `is_unique_R_alg_hom blah := proof1 and proof2`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627579):
and then it would be a Prop.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627604):
Should I change this, or does it not make a difference to anything?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627619):
And is it completely unrelated to the max class-instance resolution?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627672):
Oh I seem to just be able to make the structure a Prop anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627773):
aah, and now I don't need `set_option class.instance_max_depth 52` (for 52 was the min to make it work)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 24 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627776):
Probably best to make it a Prop, to avoid issues with not recognizing that two instances of the same thing are equal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627779):
because I seem to have forgotten things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627801):
Whyever would Lean make a structure whose constructor involved giving two proofs into a type??

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627865):
Probably also best to make it into a Prop, because then I don't need to change a max depth to 52

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627989):
no, the error is back

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627992):
I am still getting used to new lean in VS Code

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628001):
OK so my question remains

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628044):
```lean
set_option class.instance_max_depth 52 -- !!
/-- universal property of inverting one element and then another -/
theorem away_away_universal_property {R : Type u} [comm_ring R] (f : R)
(g : loc R (powers f)) {γ : Type v} [comm_ring γ] (sγ : R → γ) [is_ring_hom sγ] (Hf : is_unit (sγ f))
(Hg : is_unit (away.extend_map_of_im_unit sγ Hf g)) :
is_unique_R_alg_hom 
  ((of_comm_ring (loc R (powers f)) (powers g)) ∘ (of_comm_ring R (powers f))) 
  sγ
  (away.extend_map_of_im_unit (away.extend_map_of_im_unit sγ Hf) Hg)
    := sorry 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628048):
Is that first line evidence that I am doing something wrong?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628155):
If I `set_option trace.class_instances true`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628159):
then I get things like https://gist.github.com/kbuzzard/2a135ef1486fc55c3b4c70ca11cf50b4

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 24 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628161):
How deep do you have to go if you try to do type class inference by hand? Maybe it's just a really hard type class inference problem, that requires that depth?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628162):
I don't think it's hard

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628205):
I compose two ring homomorphisms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628209):
and I want the result to be a ring homomorphism

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628238):
It's difficult to know where the exact problem is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628251):
because when I set trace.class_instances true pretty much everything gets underlined in green

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628255):
and if I let it be 51

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628305):
then the name of the theorem gets underlined in red

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628350):
The biggest number I can find in brackets is (14)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628352):
```
[class_instances] (14) ?x_314 : discrete_linear_ordered_field R := rat.discrete_linear_ordered_field
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628356):
the mind boggles

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628401):
why is Lean wondering if my ring is a discrete linear ordered field?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 24 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631291):
because type class instance search is really dumb,  it's basically searching the graph of all paths that might reach your proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 24 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631353):
the more definitions and lemmas that you use with nested type class arguments, the bigger you'll need to set the search depth to

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631548):
So are you saying that there is a non-zero chance that I might actually have to set the search depth to 52 and this doesn't just mean that my code is crappy?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 24 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631768):
in most cs applications the type class tree search is going to be somewhat shallow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631782):
I am pushing it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631784):
but I didn't realise I was pushing that hard

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 24 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631789):
if you think it's going to be super deep, i wouldn't use type class search

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631794):
I didn't think it was going to be super deep

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631798):
I am surprised that I need 52

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631847):
in the sense that I thought that all I was doing was trying to get Lean to spot that (a) the output of some function is a ring homomorphism and (b) the composite of two ring homomorphisms is a ring homomorphism

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631852):
I don't understand how to find out where the pushing is occurring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 24 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631853):
I wonder whether you actually need 52, or it's going off in some other unsuccessful part of the search that needs depth 52

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631856):
I don't know how to find out

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 24 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631861):
Me neither

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631863):
I put the debugging on and am immediately swimming in output

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 24 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125632444):
Maybe have a look at https://github.com/leanprover/mathlib/blob/master/data/real/basic.lean#L74

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 24 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125632453):
Sometimes you can help the type class resolution algorithm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 24 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125632460):
By precomputing some shortcut

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 24 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125632465):
I have no idea if this applies in your case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125632645):
Do you have something I can test here myself?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125633311):
I have a MWE but it didn't need 52

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125633314):
:P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125633460):
I can point you to a theorem in lean-stacks-project if that's what you mean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125633469):
line 138 of tag01HR.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125633498):
https://github.com/kbuzzard/lean-stacks-project

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125633510):
wait

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125633511):
I need to push

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125633590):
https://github.com/kbuzzard/lean-stacks-project/blob/179ff95b6bd8d4998e1a007b2e8942179d9e24a8/src/tag01HR.lean#L138

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125633753):
Thanks for pointing that out Patrick. I don't know if this applies in my situation because I have no idea what the problem is. I didn't think I was doing anything too weird.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 24 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125633780):
PS @**Mario Carneiro** I commented everything out from line 171 onwards (I mention this because it's not so easy to spot in VS Code)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 24 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125637889):
By the way another way to comment everything out after a certain point is `#exit`, which also causes a notification so it's not so hard to spot

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125643878):
woohoo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125643888):
new record

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125643894):
```lean
noncomputable definition loc_is_loc_loc {R : Type u} [comm_ring R] (f g : R) :
R_alg_equiv 
  ((of_comm_ring (loc R (powers f)) (powers (of_comm_ring R (powers f) g)))
  ∘ (of_comm_ring R (powers f)))
  (of_comm_ring R (powers (f * g))) :=
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125643897):
proof that `R[1/f][1/g] = R[1/fg]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125643904):
`set_option class.instance_max_depth 93`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125643905):
:-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125643910):
I don't like the way this is going...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125644005):
Here's the proof:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125644007):
```lean
R_alg_equiv_of_unique_homs
  (away_away_universal_property' f g (of_comm_ring R (powers (f * g)))
    (unit_of_loc_more_left f g) -- proof that f is aunit in R[1/fg]
    (unit_of_loc_more_right f g) -- proof that g is a unit in R[1/fg]
  )
  (away_universal_property (f*g) 
    ((of_comm_ring (loc R (powers f)) (powers (of_comm_ring R (powers f) g))) 
      ∘ (of_comm_ring R (powers f)))
    (tag01HR.unitfg f g) -- proof that fg is a unit in R[1/f][1/g]
  )
  (away_away_universal_property' f g ((of_comm_ring (loc R (powers f)) (powers (of_comm_ring R (powers f) g))) ∘ (of_comm_ring R (powers f)))
    (tag01HR.unitf f g) -- proof that f is a unit in R[1/f][1/g]
    (tag01HR.unitg f g) -- proof that g is a unit in R[1/f][1/g]
  )
  (id_unique_R_alg_from_loc _)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125644009):
All universal properties


{% endraw %}
