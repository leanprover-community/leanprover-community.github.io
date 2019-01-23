---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/85801computabledivisionbynonzeroreal.html
---

## Stream: [maths](index.html)
### Topic: [computable division by non-zero real](85801computabledivisionbynonzeroreal.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188580):
If I have a proof that `r : ℝ` is non-zero, can I make `def f : ℝ → ℝ := λ x, x / r` computable?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188609):
if you have `r^-1`, then it's just multiplication

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188681):
I ask because Luca has a bunch of these, and he's ended up making his entire file `noncomputable theory` to shut Lean up, with the result that we're going to end up with a noncomputable fundamental group. Is that inevitable though?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188692):
but a proof that r is nonzero is not sufficient to compute a Cauchy sequence, you need a rational lower bound

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188698):
His definition of the topology on [0,1] was noncomputable -- that didn't look like a good start

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188755):
topologies are trivially computable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188789):
I feel like we could fix all this because he wrote a bunch of stuff for general closed intervals `[r,s]`with only the hypothesis `s>r`, however his applications tend to be `[0,1/2]` or `[0,1/4]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188820):
if you give me a noncomputable definition of a topology, I can define a computable topology that is defeq

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188832):
because topologies have no data

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188933):
Why is the fundamental group noncomputable?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188944):
what are the steps of construction that are problematic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189025):
```lean
import analysis.topology.topological_space
import analysis.real
import data.real.basic

def I01 := {x : ℝ | 0 ≤ x ∧ x ≤ 1}

instance : topological_space I01 := by unfold I01; apply_instance
-- definition 'I01.topological_space' is noncomputable, it depends on 'real.metric_space'

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189051):
real.metric_space is noncomputable?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189069):
oh of course, the distance function is a max

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189070):
anyway it doesn't matter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 09 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189074):
why is Kevin worrying about computability?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189124):
let the instance be noncomputable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189134):
it won't cause any problems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189144):
The fundamental group is noncomputable currently because if you want a map from [0,1/2] to [0,1] you can either define it as lam x, 2 * x, or you can define a general map from [r,s] to [0,1] as lam x, (x-r)/(s-r), and use that function everywhere in your file, and fix all the noncomputable errors by writing `noncomputable theory` at the top, and nobody noticing until the file is 1000 lines long.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189160):
none of that matters

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189166):
oh great :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189177):
The definition of the multiplication on paths is noncomputable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189186):
that checks out

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189191):
So that's OK?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189237):
you have to define it by cases on whether you are greater or less than 1/2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189238):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189246):
but Luca's implementation uses the map from [r,s] to [0,1] defined using division

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189249):
with r=0 and s=1/2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189253):
and then with r=1/2 and s=1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189256):
I often claim that when the function being defined is continuous you can do it without noncomputability, but in a general top space I'm not sure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189282):
division by 2?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189332):
I thought you meant real division - division by 2 is easy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189333):
```quote
why is Kevin worrying about computability?
```
I don't worry about it in general, I was just surprised to see it here. Were you virtually at my lecture a week last Monday? The example of G(3) made it clear to me what computability was.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189345):
we're dividing by s-r

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189354):
using a general function which divides by s-r

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189359):
in the special case where s-r=1/2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189391):
and when doing associativity s-r will be 1/4

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189448):
those could all be rationals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189460):
just do your s-r trick where s and r are rationals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189462):
rofl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189501):
But path multiplication will still be noncomputable because of the pasting you have to do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189571):
if you have f g : [0,1] -> X and you want to concatenate them, you define `(f * g) x = if x < 1/2 then f(2*x) else g(2*x-1)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189662):
aie you're right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189663):
I think if you wanted to do that computably, you could define it by that equation on rationals, then take the limit as the sequence of rationals approaches some real

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189679):
but then you have to have a computable limit operation on the target topological space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189691):
I think this is all too much for Luca's project, I think we might stick to noncomputable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189697):
I'm glad I mentioned this now, I can go back to thinking computable maths is all a bit silly for a while.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189716):
What I'm trying to do nowadays is to get some sort of feeling for when I am actually being noncomputable. Like when I was a PhD student and I got some sort of a feeling for when I was actually using the axiom of choice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189759):
or when I was a post-doc and I got some sort of a feeling for when I was actually using universes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189768):
rule of thumb: if you use anything descendent from `topological_space.lean` or `analysis/real.lean`, just put `noncomputable theory` and don't attempt to get away from it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189772):
[answer: probably never, although it was difficult to find a reference sometimes]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189788):
If all your imports are in `data` you should try to be computable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189817):
Well Luca's file uses lots of stuff from both of those files, so we'll have to be noncomputable for now. Kenny can fix it all up when he's finished

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189824):
topology is 100% classical maths

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189888):
I'm surprised. I didn't realise that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189893):
and metric spaces and uniform spaces...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189914):
Metric spaces I can understand because they mention reals.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189922):
it could conceivably be different but it would require a major rewrite of the library

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189937):
`data.real.basic` is computable, `analysis.real` is not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189960):
Metric spaces also often use countable dependent choice, because the two definitions of closure only coincide when you are able to choose a sequence of points in your space tending to a point in the closure, which involves choosing `x_n` at distance at most `1/n` from the boundary point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131190030):
well, that's just first countable spaces in general

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131190053):
but there I'm not so worried because all the claims are propositional anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131190069):
we make no attempt to avoid the axiom of choice in theorems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 09 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131190413):
```lean
import data.real.basic

def computable_inv (x : ℝ) : x ≠ 0 → ℝ :=
quotient.hrec_on x 
(λ x (hx : real.mk x ≠ 0), real.mk 
  (cau_seq.inv x (mt real.mk_eq_zero.2 hx))) 
  (λ a b h, begin
    have : real.mk a = real.mk b := quotient.sound h,
    refine function.hfunext (by rw this) 
      (λ h₁ h₂ _, heq_of_eq _),
    refine (domain.mul_right_inj h₁).1 _,
    conv {to_rhs, congr, skip, rw this},
    refine quotient.sound _,
    refine setoid.trans (cau_seq.inv_mul_cancel (mt real.mk_eq_zero.2 h₁)) 
      (setoid.symm (cau_seq.inv_mul_cancel (mt real.mk_eq_zero.2 h₂))) 
  end)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131190434):
Yeah, I double checked the proof in data.real.basic and it can definitely be defined... I'm not sure why I didn't try

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 09 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131190547):
```lean
lemma computable_inv_mul_cancel (x : ℝ) : Π hx : x ≠ 0,
  computable_inv x hx * x = 1 :=
quotient.induction_on x (λ x hx, quotient.sound (cau_seq.inv_mul_cancel _))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 09 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131190657):
@**Kevin Buzzard** you still haven't explained why you care about computable reals?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 09 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131190733):
Oh, I found a counterexample for the computability claim. Let $$X$$ be a quotient of $$\Bbb R$$ identifying all points in $$[1,2]$$. Let $$f(x)=x$$ and $$g(x)=x+2$$; these are continuous functions on $$[0,1]$$ such that $$f(1)=[1]=[2]=g(0)$$, and both functions are computable. The path concatenation $$f\ast g$$ is discontinuous at $$1/2$$ (in the real topology), so it is not computably definable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131190754):
Because Luca was dividing by a positive real which I could prove was greater than 1/10 and so I realised that probably I could make some of his noncomputable code computable. I hence wondered whether it would be an easy fix to make his fundamental group computable. But as Mario pointed out, there are other problems with computability, and I've now decided not to worry about it.


{% endraw %}
