---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/54532setunionequality.html
---

## Stream: [maths](index.html)
### Topic: [set union equality](54532setunionequality.html)

---


{% raw %}
#### [ Kevin Buzzard (Apr 25 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683378):
`example (X : Type) (R : Type) (D : R → set X) (γ : Type) (f : γ → R) :
  ⋃₀(D '' set.range f) = ⋃ (i : γ), D (f i) := sorry`

#### [ Kevin Buzzard (Apr 25 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683386):
I was rather hoping simp would do this one...

#### [ Kevin Buzzard (Apr 25 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683389):
is there some lemma?

#### [ Kevin Buzzard (Apr 25 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683403):
or do I stick with my 25 line tactic proof :-/

#### [ Mario Carneiro (Apr 25 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683516):
use `D '' range f = range (D o f)` and then hopefully `U range f = U i, f i` is a theorem

#### [ Kenny Lau (Apr 25 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683659):
```lean
import data.set

example (X : Type) (R : Type) (D : R → set X) (γ : Type) (f : γ → R) :
  ⋃₀(D '' set.range f) = ⋃ (i : γ), D (f i) :=
set.ext $ λ z, ⟨λ ⟨x1, ⟨⟨x2, ⟨x3, h1⟩, h2⟩, h3⟩⟩, ⟨x1, ⟨x3, h2 ▸ h1 ▸ rfl⟩, h3⟩,
λ ⟨x1, ⟨x2, h1⟩, h3⟩, ⟨x1, ⟨f x2, ⟨x2, rfl⟩, h1.symm⟩, h3⟩⟩
```

#### [ Kevin Buzzard (Apr 25 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683764):
That's my 25 line tactic proof!

#### [ Kenny Lau (Apr 25 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683768):
interesting

#### [ Kevin Buzzard (Apr 25 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683776):
```lean
begin
  apply set.ext,
  intro x,
  split,
  intro H,
  cases H with V HV,
  cases HV with HV HX,
  cases HV with r HR,
  cases HR.1 with i Hi,
  existsi V,
  existsi _,
  assumption,
  simp,
  existsi i,
  rw Hi,rw HR.2,

  intro H,
  cases H with V HV,
  cases HV with HV Hx,
  cases HV with i Hi,
  existsi V,
  existsi _,
  assumption,
  existsi (f i),
  split,
  simp,
  existsi i,
  refl,
  rw Hi,
end 
```

#### [ Kenny Lau (Apr 25 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683779):
use `rcases` :P

#### [ Kevin Buzzard (Apr 25 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683783):
It must be, because we both start with the same line and then do nothing

#### [ Kevin Buzzard (Apr 25 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683795):
other than following our nose

#### [ Kevin Buzzard (Apr 25 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125685487):
```lean
example (X : Type) (R : Type) (D : R → set X) (γ : Type) (f : γ → R) :
  ⋃₀(D '' set.range f) = ⋃ (i : γ), D (f i) := 
  begin
  rw [←set.image_univ,←set.image_comp],
  show ⋃₀(D ∘ f '' set.univ) = ⋃ (i : γ), (D ∘ f) i,
  simp [set.Union_eq_sUnion_image],
  end 

```

#### [ Kevin Buzzard (Apr 25 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125685555):
don't even need the show

#### [ Kevin Buzzard (Apr 25 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125685585):
Mario's insight is that we reduce the number of functions from 2 to 1 and then simp can handle it

#### [ Kenny Lau (Apr 25 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125685871):
```lean
import data.set

example (X : Type) (R : Type) (D : R → set X) (γ : Type) (f : γ → R) :
  ⋃₀(D '' set.range f) = ⋃ (i : γ), D (f i) :=
by rw [set.Union_eq_sUnion_image, ← set.range_comp]
```

#### [ Kenny Lau (Apr 25 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125685873):
do I win?

#### [ Kevin Buzzard (Apr 25 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125686366):
[IMG_20180425_113712650.jpg](/user_uploads/3121/wqULCViCYbpmWIeiX5WCeQ76/IMG_20180425_113712650.jpg)

#### [ Kevin Buzzard (Apr 25 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125686376):
saw that on the way in today and thought of you

#### [ Scott Morrison (Apr 26 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125697140):
@**Kevin Buzzard** your 25 line tactic proof doesn't seem to work (fails at `cases H with V HV,`). I was curious how my tactics cope with this one. :-)

#### [ Mario Carneiro (Apr 26 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125697303):
works for me

#### [ Mario Carneiro (Apr 26 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125697366):
```
import data.set.lattice

example (X : Type) (R : Type) (D : R → set X) (γ : Type) (f : γ → R) :
  ⋃₀(D '' set.range f) = ⋃ (i : γ), D (f i) :=
begin
  apply set.ext,
  ... +25 lines
end
```

#### [ Kevin Buzzard (Apr 26 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712128):
Simon's code in the cases thread didn't work for me without a minor fix

#### [ Kevin Buzzard (Apr 26 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712129):
I wonder whether we are using different versions of Lean

#### [ Mario Carneiro (Apr 26 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712137):
I'm running 04-20 now, along with the latest mathlib. Are you?

#### [ Kevin Buzzard (Apr 26 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712138):
you are no doubt bleeding edge, I am enjoying the stability of 4-06

#### [ Kevin Buzzard (Apr 26 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712140):
Upgrading is such a chore

#### [ Kevin Buzzard (Apr 26 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712141):
I need to do it on three machines

#### [ Kevin Buzzard (Apr 26 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712142):
and make all the olean files

#### [ Kevin Buzzard (Apr 26 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712144):
and I just want to concentrate on getting schemes done

#### [ Kevin Buzzard (Apr 26 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712184):
Everything is taking longer than expected

#### [ Kevin Buzzard (Apr 26 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712188):
because I have a bunch of commutative diagrams / exact sequences

#### [ Kevin Buzzard (Apr 26 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712189):
and I continually want to replace an object with a canonically isomorphic object

#### [ Kevin Buzzard (Apr 26 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712190):
and claim that everything is still commutative / exact

#### [ Kevin Buzzard (Apr 26 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712195):
I hate computers

#### [ Kevin Buzzard (Apr 26 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712206):
In maths you just say it works and nobody even notices

#### [ Mario Carneiro (Apr 26 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712261):
My instinct always says there's a proof architectural solution to such problems

#### [ Mario Carneiro (Apr 26 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712268):
but sometimes you just have to do it the long way a few times before you can see the pattern

#### [ Mario Carneiro (Apr 26 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712269):
but once you identify the pattern, it's a short hop to formalized patterns and then lemmas that save you the boilerplate work

#### [ Kevin Buzzard (Apr 26 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712538):
It is that way of thinking which led me to all this "unique-R-algebra-hom" stuff

#### [ Kevin Buzzard (Apr 26 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712543):
The proofs that the diagrams commute are just "this is a map with a property, so it's the only map with the property, so it's equal to the map we want"

#### [ Kevin Buzzard (Apr 26 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712549):
I think a mathematician would instinctively prove commutativity using a diagram chase

#### [ Kevin Buzzard (Apr 26 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712552):
"where does this element go? This way it goes here, that way it goes there, oh look they're the same"

#### [ Kevin Buzzard (Apr 26 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712555):
but seeing as I have a pathological fear of quotient types I had to find another way

#### [ Mario Carneiro (Apr 26 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712597):
I think that was a good idea on your part

#### [ Kevin Buzzard (Apr 26 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712599):
I don't think my universal property methods are much quicker

#### [ Kevin Buzzard (Apr 26 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712601):
in the sense that if I asked Kenny to prove the diagrams commute he would just do the chase

#### [ Kevin Buzzard (Apr 26 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712602):
and the proof would be about as long, I suspect

#### [ Kevin Buzzard (Apr 26 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712603):
but my methods are easier to explain

#### [ Mario Carneiro (Apr 26 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712608):
I think Kenny is good at getting to the end, but he needs to work on his long game

#### [ Kevin Buzzard (Apr 26 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712609):
they just involve setting type class inference resolution depth to 93 occasionally ;-)

#### [ Mario Carneiro (Apr 26 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712654):
there is a lot more possibility for "golfing" at the large scale, planning out the right lemmas that give you the most bang for the buck

#### [ Mario Carneiro (Apr 26 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712668):
and that's where stuff like `is_unique_R_hom` come in

#### [ Mario Carneiro (Apr 26 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712717):
I think the difference between Kenny's and my answer to your union-image-range question demonstrate this well

#### [ Mario Carneiro (Apr 26 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712726):
on the one hand you can use matches and rfl and anonymous instances to just write out the whole thing from first principles, it's not so hard

#### [ Mario Carneiro (Apr 26 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712729):
and on the other you could chain together two lemmas that were written exactly for the purpose

#### [ Mario Carneiro (Apr 26 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712781):
I think it's a bit unfortunate that proofs from lemmas lose a lot relative to proofs using basic dependent type theory simply because they have names (and lean's naming convention averages 20 characters or so)

#### [ Mario Carneiro (Apr 26 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712827):
which is a bit misleading since something like `λ ⟨a, b⟩,` is actually quite a bit more complicated under the hood than it looks

#### [ Kevin Buzzard (Apr 26 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713016):
In practice, my current problem is that I now know enough about the system to be able to prove these things from first principles, I know that ideally this is not what I should be doing, but I do not have an encyclopedic knowledge of the lemmas which are there and to be honest I am unclear about the roadmap for getting this knowledge.

#### [ Kevin Buzzard (Apr 26 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713017):
I am not even sure this qualifies as a "problem"

#### [ Kevin Buzzard (Apr 26 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713020):
but we saw it twice yesterday

#### [ Kevin Buzzard (Apr 26 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713032):
My ability to retain information is not what it was; I can read the source code and think "oh that is cool" but then not remember everything that is there, unlike when I was in my 20s

#### [ Kevin Buzzard (Apr 26 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713034):
I need to develop (as Kenny once pointed out) a good feeling for "what _should_ be there"

#### [ Kevin Buzzard (Apr 26 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713071):
and then simply check that it is

#### [ Kevin Buzzard (Apr 26 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713078):
Having said all that, I would rather be here than where I was 6 months ago

#### [ Kevin Buzzard (Apr 26 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713079):
where I had to ask because I simply had no idea how to prove what I needed

#### [ Mario Carneiro (Apr 26 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713198):
I agree with kenny's quote. I certainly don't remember all the lemmas in mathlib, I just think about the things that should exist and make sure they are actually there. Your question about the union-image-range seems like a step in the right direction, you are getting the sense for what form the lemmas should take, but in that case union-image-range is three things and I like lemmas to talk about two things

#### [ Kevin Buzzard (Apr 26 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713211):
One thing that has helped me terrifically is trying to use Kenny's localization work, because it was written in a completely different style to mathlib. Rather than being written by someone who knew everything and wanted to write an interface, it was written by someone who knew nothing and was learning the material.

#### [ Kevin Buzzard (Apr 26 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713250):
In practice I said to Kenny "can you please give me a function which given a ring R and a multiplicative subset S, returns the ring R[1/S]"

#### [ Mario Carneiro (Apr 26 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713251):
As far as what you should learn by reading printouts, I would say focus on definitions, that's the core around which the lemmas are built

#### [ Kevin Buzzard (Apr 26 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713254):
and he said "sure" and a day or so later I had that ring

#### [ Kevin Buzzard (Apr 26 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713257):
and then I realised I could do nothing with it

#### [ Kevin Buzzard (Apr 26 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713259):
so I kept asking for more and he kept making it (basically by return of post)

#### [ Kevin Buzzard (Apr 26 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713269):
and by the end of it I had a feeling for what it meant to build a mathlib file

#### [ Mario Carneiro (Apr 26 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713313):
writing for others is definitely harder than writing for yourself

#### [ Kevin Buzzard (Apr 26 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713314):
focus on definitions -- thanks for the tip!

#### [ Kevin Buzzard (Apr 26 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713319):
writing for others -- Kenny and I have worked really well as a team, I knew the maths and he did the dirty work

#### [ Mario Carneiro (Apr 26 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713322):
you can look at the lemmas, but your reaction to them should be "oh, well of course"

#### [ Kevin Buzzard (Apr 26 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713381):
and the really cool thing about the localization stuff was once he'd done the really primitive dirty work of proving that some map had some universal property, all the other universal properties which people used in practice could be deduced from Kenny's, and I could write that code myself

#### [ Kevin Buzzard (Apr 26 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713386):
you have probably seen this phenomenon before

#### [ Kevin Buzzard (Apr 26 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713388):
technical code full of [[ ]] and quot.sound or whatever to get stuff off the ground

#### [ Kevin Buzzard (Apr 26 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713389):
but then the proofs get more conceptual after a while

#### [ Mario Carneiro (Apr 26 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713390):
oh yes

#### [ Mario Carneiro (Apr 26 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713430):
I expect that outside the free_group file we will never see `list (A x bool)`

#### [ Kevin Buzzard (Apr 26 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713434):
it's been a fascinating learning experience.

#### [ Scott Morrison (Apr 26 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125718755):
````lean
example (X : Type) (R : Type) (D : R → set X) (γ : Type) (f : γ → R) :
  ⋃₀(D '' set.range f) = ⋃ (i : γ), D (f i) := by obviously
````

#### [ Kevin Buzzard (Apr 26 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732464):
Well it does look obvious to me.

#### [ Kevin Buzzard (Apr 26 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732467):
I think we are probably a long way from a tactic which will be able to prove everything which looks obvious to me

#### [ Kevin Buzzard (Apr 26 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732471):
but I want to start along down that road.

#### [ Patrick Massot (Apr 26 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732521):
Kevin,  you may have missed the point

#### [ Patrick Massot (Apr 26 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732527):
Scott *does* have a tactic called `obviously` which does the job here

#### [ Patrick Massot (Apr 26 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732559):
https://github.com/semorrison/lean-tidy/blob/f2303e5376c3520d4432fd073fdb1fd0dfb1f8a8/examples/20180426-kbuzzard.lean

#### [ Patrick Massot (Apr 26 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732580):
https://github.com/semorrison/lean-tidy/blob/b8c6661d4ea74d5e8b5df25b2225f4353e5c6bf5/src/tidy/tidy.lean#L136

#### [ Kevin Buzzard (Apr 26 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732772):
right

#### [ Kevin Buzzard (Apr 26 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732776):
but unfortunately I suspect that it will not prove _everything_ which is obvious

#### [ Patrick Massot (Apr 26 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732826):
He's working on it

#### [ Kevin Buzzard (Apr 26 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732858):
In particular I bet it won't prove that if there exists a,b,c,d nats with `a^2+b^2+c^2+d^2 = 2n` then there exists `w x y z` nats with `w^2+x^2+y^2+z^2=2n` and `w^2+x^2` even

#### [ Scott Morrison (Apr 27 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125750337):
It would be nice to have a better name than `obviously`. Suggestions welcome. `follow_your_nose` is a a possibility :-)

#### [ Scott Morrison (Apr 27 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125750401):
I think your `a^2+b^2+c^2+d^2 = 2n` is far from "obvious" in this sense. I mean, it's easy, but I don't think "let's think about the parity of the numbers, and the multiplicities of the parities, and solve the problem merely by permuting" counts as "following your nose".

#### [ Simon Hudon (Apr 27 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125750639):
`left_as_an_exercise_to_the_reader`

#### [ Simon Hudon (Apr 27 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125750695):
Or `beside_the_point`

#### [ Simon Hudon (Apr 27 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125750703):
or `omitted`

#### [ Mario Carneiro (Apr 27 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125751085):
I think `by beside_the_point` is a hilarious substitute for `sorry`

#### [ Mario Carneiro (Apr 27 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125751140):
but none of those suggest that the proof is actually done automatically

#### [ Simon Hudon (Apr 27 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125751148):
How about `magic` or `automagic`? :D

#### [ Simon Hudon (Apr 27 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125751215):
I think I might like `chocolate` even better, since Uncyclopedia mentions it's a respectable proof technique:

http://uncyclopedia.wikia.com/wiki/Proof

#### [ Mario Carneiro (Apr 27 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125752084):
Here's a nice proof of that statement: Given any three numbers `a b c`, I claim that the sum of two of them is even. If `a+b` is odd, and `a+c` is odd, and `b+c` is odd, then `(a+b)+(a+c)+(b+c)=2*(a+b+c)` is odd, a contradiction.

#### [ Mario Carneiro (Apr 27 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125752135):
To do this formally you only need to know that every number is even or odd and apply it three times, and then do some simple algebra at the end

#### [ Mario Carneiro (Apr 27 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125752144):
also you have to know parity rules for adding even and odd


{% endraw %}
