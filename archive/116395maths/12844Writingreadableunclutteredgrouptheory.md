---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/12844Writingreadableunclutteredgrouptheory.html
---

## Stream: [maths](index.html)
### Topic: [Writing readable uncluttered group theory](12844Writingreadableunclutteredgrouptheory.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808670):
I noticed that the definition of a group in Lean was one more axiom than it could be

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808710):
you can prove `mul_one` from the other axioms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808713):
This may well have been talked about before

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808714):
But I thought I'd write a blog post on this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808715):
and I wanted to talk about the proof of `mul_one` (which goes via `mul_left_cancel`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808719):
for Lean-groups-without-`mul_one`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808721):
But I could not make the arguments look beautiful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808723):
This is kind of OK

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808724):
```lean
lemma gripe.mul_left_cancel {G : Type} [has_mul G] [has_one G] [has_inv G] [gripe G]
: ∀ (a b c : G), a * b = a * c → b = c :=
begin
  intros a b c Habac,
  exact calc b = 1 * b : (one_mul b).symm
           ... = (a⁻¹ * a) * b : by rw [←gripe.mul_left_inv a]
           ... = a⁻¹ * (a * b) : mul_assoc _ _ _
           ... = a⁻¹ * (a * c) : by rw Habac
-- ... = c : by simp only [mul_assoc,one_mul,mul_left_inv] -- fails
           ... = (a⁻¹ * a) * c : (gripe.mul_assoc _ _ _).symm
           ... = 1 * c : by rw [gripe.mul_left_inv a]
           ... = c : one_mul _
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808776):
although all this `has_mul` stuff is both really cluttering things up and not actually telling us the one useful thing about it, which is that it is a map alpha -> alpha -> alpha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808784):
I made a type for that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808785):
```lean
class gripe (G : Type) [has_mul G] [has_one G] [has_inv G] :=
(mul_assoc : ∀ (a b c : G), a * b * c = a * (b * c))
(one_mul : ∀ (a : G), 1 * a = a)
(mul_left_inv : ∀ (a : G), a⁻¹ * a = 1)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808828):
But got a bit sick about still having to say we have a `has_mul`. On the other hand I really want the notation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808836):
can you use `extends` instead of those extra parameters to the class? I've never used it myself but I see it in the algebraic classes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808837):
Other complains about that calc proof is that I need to give too many hint, I seem to have to mention the type's name (gripe) randomly and I can only sometimes get away with `_`s, and why do I even have to put them at all?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808843):
I tried without the structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808845):
```quote
This may well have been talked about before
```
https://gitter.im/leanprover_public/Lobby?at=59fd723d976e63937e268f50

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808888):
```lean
lemma mul_left_cancel' {G : Type} [has_mul G] [has_one G] [has_inv G]
(mul_assoc : ∀ (a b c : G), a * b * c = a * (b * c))
(one_mul : ∀ (a : G), 1 * a = a)
(mul_left_inv : ∀ (a : G), a⁻¹ * a = 1)
: ∀ (a b c : G), a * b = a * c → b = c :=
begin
  intros a b c Habac,
  exact calc b = 1 * b : (one_mul _).symm
           ... = (a⁻¹ * a) * b : by rw [mul_left_inv]
           ... = a⁻¹ * (a * b) : mul_assoc _ _ _ -- why not just mul_assoc?
           ... = a⁻¹ * (a * c) : by rw Habac
-- ... = c : by simp only [mul_assoc,one_mul,mul_left_inv] -- fails
           ... = (a⁻¹ * a) * c : (mul_assoc _ _ _).symm
           ... = 1 * c : by rw [mul_left_inv]
           ... = c : one_mul _ -- why the _ ?
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808938):
and that seemed to go better, but then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808940):
```lean
theorem mul_one' {G : Type} [has_mul G] [has_one G] [has_inv G]
(mul_assoc : ∀ (a b c : G), a * b * c = a * (b * c))
(one_mul : ∀ (a : G), 1 * a = a)
(mul_left_inv : ∀ (a : G), a⁻¹ * a = 1)
: ∀ (a : G), a * 1 = a :=
begin
intro a,
 apply (mul_left_cancel' mul_assoc one_mul mul_left_inv a⁻¹ _ _), -- aargh 
 rw [←mul_assoc,mul_left_inv,one_mul],
end 

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808942):
@**Kevin Buzzard** edit > change title

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808943):
Oh, I guess you are complaining about `has_mul` being opaque to the reader wherever it appears, not that you had to write it twice?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808948):
I couldn't apply the theorem I proved without carrying around all the axioms.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808949):
wrong thread

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808952):
I want to write a blog post which looks good and works in Lean and proves clearly that one of the axioms of a group follows from the others

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808953):
god

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808991):
but I really want the kids to understand that they can also do some of their group theory example sheets in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808995):
whatever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808998):
How do you feel about using `variables` instead?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125808999):
can I move this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125809007):
@**Scott Morrison** sorry, had to move your messages as well; could you move your messages back to "notations in category theory"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125809008):
Sorry

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125809010):
The stupidity of all the has_one has_mul stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125809049):
is that these typeclasses have notation attached to them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125809050):
and you want to use the notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125809051):
```lean
variable {G : Type}
variable (mul : G → G → G)
variable (one : G)
variable (inv : G → G)

local notation a `*` b := mul a b
local notation 1 := one
local notation a `⁻¹` := inv a

variable (mul_assoc : ∀ (a b c : G), a * b * c = a * (b * c))
variable (one_mul : ∀ (a : G), 1 * a = a)
variable (mul_left_inv : ∀ (a : G), a⁻¹ * a = 1)

lemma mul_left_cancel' : ∀ (a b c : G), a * b = a * c → b = c :=
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125809053):
Maybe instead of local notation I can use instances

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125809250):
oh, I forgot `variables` don't get along well with tactics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125823314):
I am just going to bite the bullet and implement it in 5 different ways and see which one is best

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125823316):
`class has_group_notation (G : Type) extends has_mul G, has_one G, has_inv G`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125823322):
Does that class exist @**Mario Carneiro** ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125823328):
It seems to come with free and painless type class inference

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125823374):
I had not appreciated how that barrage of classes in `core.lean` was actually just a barrage of notation. Each typeclass corresponds to precisely one piece of notation. I had not realised this before!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125823419):
I don't really understand notation and don't use any in my schemes work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125823422):
actually I think I suddenly understand it a whole lot better

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125823427):
my class corresponds to a finite set of notations.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125823661):
```lean
class group' (G : Type) extends has_group_notation G :=
(mul_assoc : ∀ (a b c : G), a * b * c = a * (b * c))
(one_mul : ∀ (a : G), 1 * a = a)
(mul_left_inv : ∀ (a : G), a⁻¹ * a = 1)

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125823664):
@**Reid Barton**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125823665):
That's the way to get rid of all that continually carrying around `[has_add]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125823670):
```lean
lemma group'.mul_left_cancel {G : Type} [group' G]
: ∀ (a b c : G), a * b = a * c → b = c := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125823671):
This thread is about making the proof that one of the axioms of a group as defined by Lean follows from all of the others

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125823711):
look as nice and uncluttered as possible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125823727):
The strat is : first prove `mul_left_cancel` (without using `mul_one` of course), and then deduce `mul_one`. I know there are other strategies but that's the strategy I'd like to showcase in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125823728):
so I can show the undergraduates one way of revising for their upcoming group theory exam

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125823743):
I want to show them that using Lean to do abstract basic chase stuff around stuff in group theory is really easy in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125823771):
I'll blog about it but I need to get it as nice looking as possible first

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125824936):
https://gist.github.com/kbuzzard/2adf2b42a9ea23dabc2eb26a1a4b20fb

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125824937):
My efforts using classes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125824938):
I had to keep writing the class name

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125824943):
and the calc proof needed a lot of blanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125824944):
How could this be improved?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125824984):
I am going to try other ways of setting this up to see pros and cons

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125824987):
Change
```lean
(mul_assoc : ∀ (a b c : G), a * b * c = a * (b * c))
```
to
```lean
(mul_assoc : ∀ {a b c : G}, a * b * c = a * (b * c))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825665):
Do you think that's right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825667):
I changed it for the constants example

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825668):
and my tactic proof got worse

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825669):
if you change it then you don't need to put underscores

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825674):
I'll show you you're wrong

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825716):
https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/group_axioms_constants.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825718):
But maybe you can fix it :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825720):
there is a point in tactic mode where I needed underscores :-(

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825723):
where?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825729):
https://github.com/kbuzzard/xena/blob/master/canonical_isomorphism/group_axioms_class.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825730):
not there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825732):
so where am I wrong?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825733):
https://github.com/kbuzzard/xena/blob/48ce83d8bc9782a08ee852d126e784f696086846/canonical_isomorphism/group_axioms_constants.lean#L48

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825734):
there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825775):
In the calc proof, if you just begin every justification with `by rw`, you can make it quite uniform (at least in this case)
```lean
  exact calc b = 1 * b         : by rw group'.one_mul
           ... = (a⁻¹ * a) * b : by rw group'.mul_left_inv
           ... = a⁻¹ * (a * b) : by rw group'.mul_assoc
           ... = a⁻¹ * (a * c) : by rw Habac
           ... = (a⁻¹ * a) * c : by rw group'.mul_assoc
           ... = 1 * c         : by rw group'.mul_left_inv
           ... = c             : by rw group'.one_mul
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825776):
Change
```lean
lemma mul_left_cancel : ∀ {a b c : G}, a * b = a * c → b = c := 
```
to
```lean
lemma mul_left_cancel : ∀ (a) {b c : G}, a * b = a * c → b = c := 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825781):
do you feel that this change is actually justified rather than it being an attempt to sort out a problem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825782):
yes, because `a` could not be infered from the final type `b = c`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825783):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825784):
I wondered if that was a reasonable justification for the change

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 28 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825823):
It can be inferred from the hypothesis though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825824):
exactly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825825):
well if you don't want to change it you can state the hypothesis explicitly using `have`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825826):
> ... = (a⁻¹ * a) * b : by rw [mul_left_inv] -- why does that line even work? I believe it should fail. Is it a bug?

I was puzzled by this too up until quite recently. The reason it works is that `rw` does not rewrite the left hand side to the right hand side as one might think. Rather, it rewrites the desired equality `1 * b = (a⁻¹ * a) * b` to whatever it becomes after the rewrite, and that rewrite might occur on either side.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825827):
so Kenny based on your logic what are the forms of the other axioms that I should be using?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825833):
Then because the rewritten goal is of the form `a = a`, it gets solved by `rfl` automatically

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825834):
@**Kevin Buzzard** maybe don't make `a` explicit afterall, lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825835):
:-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825887):
I don't quite know what I am looking for here. I guess what is going on is that different conventions produce different results which may or may not have slight annoyances

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825888):
Also if you use `by rw` on every line of the calc proof, then it doesn't matter whether you make the arguments of the axioms explicit or not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825980):
Kenny in none of the standard typeclasses do I see variables in axioms being introduced with `{}`. I am imagining there is a good reason for this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825987):
Letting them all be `{}` announces that you're 100 percent convinced that unification will save you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825988):
well they have interface like
```lean
class semigroup (α : Type u) extends has_mul α :=
(mul_assoc : ∀ a b c : α, a * b * c = a * (b * c))

lemma mul_assoc [semigroup α] : ∀ a b c : α, a * b * c = a * (b * c) :=
semigroup.mul_assoc
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825989):
but letting them all be `()` does not mean you're giving up home

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825990):
oh wait

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825991):
because other things might fill in the gaps later

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125825992):
right, you still need `_` for `mul_assoc` lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826031):
so maybe change back to `()` and use Reid's approach

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826032):
Sometimes I did

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826033):
sometimes I didn't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826040):
Oh I make the interface!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826053):
I'm saying, the interface in the library still uses explicit variables

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826096):
`exact calc b = 1 * b         : by rw group'.one_mul` -- that "shouldn't work" either

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826097):
why not?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826100):
the goal is `b = 1 * b`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826105):
Oh I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826106):
of course

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826107):
Kenny do you understand why that bug is not a bug?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826149):
line 33

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826164):
Oh I now understand

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826165):
I should think of what the rw actually does

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826166):
not what I want it to do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826218):
```lean
lemma mul_left_cancel : ∀ {a b c : G}, a * b = a * c → b = c := 
begin
  intros a b c Habac,
  exact calc b = 1 * b         : by rw one_mul
           ... = (a⁻¹ * a) * b : by rw mul_left_inv
           ... = a⁻¹ * (a * b) : by rw mul_assoc
           ... = a⁻¹ * (a * c) : by rw Habac
           ... = (a⁻¹ * a) * c : by rw mul_assoc
           ... = 1 * c         : by rw mul_left_inv
           ... = c : one_mul
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826221):
Yes that's really nice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826224):
That's just how a mathematician would explain it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826228):
"apply this axiom"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826233):
"I don't care which way"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826234):
"the obvious way"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826236):
I'm sure you can have fewer lines lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826237):
of course

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826253):
but this is the raw beauty which you see here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826280):
and then your `begin intros exact` kind of defeat the purpose of entering tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826282):
ha ha you are exactly right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826292):
I wasn't sure whether to comment about the intros line, haha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826294):
comment about them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125826451):
@**Kevin Buzzard** I just finished writing a file without ever entering tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831048):
All the rewrites fail in the below

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831051):
```lean
class has_group_notation (G : Type) extends has_mul G, has_one G, has_inv G

structure group' (G : Type) extends has_group_notation G :=
(mul_assoc : ∀ (a b c : G), a * b * c = a * (b * c))
(one_mul : ∀ (a : G), 1 * a = a)
(mul_left_inv : ∀ (a : G), a⁻¹ * a = 1)

variables {G : Type} (group'.G : group' G) [has_group_notation G]  
-- variables (H : Type) [has_mul H] [has_one H] [has_inv H]

-- We prove left_mul_cancel for group'

lemma group'.mul_left_cancel : ∀ (a b c : G), a * b = a * c → b = c := 
λ a b c Habac,
 calc b = 1 * b         : by rw one_mul
    ... = (a⁻¹ * a) * b : by rw mul_left_inv
    ... = a⁻¹ * (a * b) : by rw mul_assoc
    ... = a⁻¹ * (a * c) : by rw Habac
    ... = (a⁻¹ * a) * c : by rw mul_assoc
    ... = 1 * c         : by rw mul_left_inv
                ... = c : by rw one_mul
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831052):
I am using a structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831053):
I don't understand the error messages

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831054):
First is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831055):
```
rewrite tactic failed, did not find instance of the pattern in the target expression
  1 * ?m_3
state:
G : Type,
_inst_1 : has_group_notation G,
a b c : G,
Habac : a * b = a * c
⊢ b = 1 * b
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831094):
I am unimpressed with Lean's instance-finding abilities here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831095):
what am i missing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831099):
I wondered how changing a class to astructure changed things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831106):
I think all notation as a notational typeclass works great in these sorts of situations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831107):
Lean only finds classes, not structures

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831109):
it's clear what it's doing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831110):
and it's doing nothing more

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831111):
the structure isnt even in the hypotheses

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831154):
I don't understand

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831158):
I will take notation off

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831160):
and put pp.all on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831161):
am I missing something simple?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831166):
kenny can you fix it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831171):
that might help me understand

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831267):
Look at this beautiful proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831273):
```lean
lemma mul_left_cancel' {G : Type} [has_mul G] [has_one G] [has_inv G]
(mul_assoc : ∀ (a b c : G), a * b * c = a * (b * c))
(one_mul : ∀ (a : G), 1 * a = a)
(mul_left_inv : ∀ (a : G), a⁻¹ * a = 1)
: ∀ (a b c : G), a * b = a * c → b = c :=
λ a b c Habac,
 calc b = 1 * b         : by rw one_mul
    ... = (a⁻¹ * a) * b : by rw mul_left_inv
    ... = a⁻¹ * (a * b) : by rw mul_assoc
    ... = a⁻¹ * (a * c) : by rw Habac
    ... = (a⁻¹ * a) * c : by rw mul_assoc
    ... = 1 * c         : by rw mul_left_inv
    ... = c             : by rw one_mul
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831281):
Can you show me how to make a proof which is just as beautiful, but using a class or structure?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831329):
I am getting sick of carrying the axioms around with me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831368):
I have packaged up all the notation in a typeclass

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831369):
but I want to package all the group axioms up as well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831379):
The typeclass system is perfect for notation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831381):
There is very little risk of a diamond :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831406):
I want to package everything away but keep the proof beautiful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831438):
and once I have managed that, I think I am done.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 28 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831505):
Why aren't you just using the `group` typeclass?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 28 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125831988):
The `has_group_notation` class has been discussed in some of Jeremy's explorations, called `group_struct`, but it's not needed in mathlib as it is now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 28 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125832087):
The standard way to show that an axiom is redundant is to have an auxiliary constructor for `group` that doesn't have the redundant axioms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 28 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125832272):
Is this better?
```lean

class has_group_notation (G : Type) extends has_mul G, has_one G, has_inv G

class group' (G : Type) extends has_group_notation G :=
(mul_assoc' : ∀ (a b c : G), a * b * c = a * (b * c))
(one_mul' : ∀ (a : G), 1 * a = a)
(mul_left_inv' : ∀ (a : G), a⁻¹ * a = 1)

variables {G : Type} [group' G]
open group'
-- variables (H : Type) [has_mul H] [has_one H] [has_inv H]

-- We prove left_mul_cancel for group'

lemma group'.mul_left_cancel : ∀ (a b c : G), a * b = a * c → b = c :=
λ a b c Habac,
 calc b = 1 * b         : by rw one_mul' b
    ... = (a⁻¹ * a) * b : by rw mul_left_inv'
    ... = a⁻¹ * (a * b) : by rw mul_assoc'
    ... = a⁻¹ * (a * c) : by rw Habac
    ... = (a⁻¹ * a) * c : by rw mul_assoc'
    ... = 1 * c         : by rw mul_left_inv'
                ... = c : by rw one_mul'
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 28 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125832280):
You had two `has_group_notation` instances, one from `group'` and another one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125832281):
Just use a namespace and drop the fucking primes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 28 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125832284):
one mul is global

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125832322):
protected

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 28 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125832326):
but it doesn't know which `one_mul` I mean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 28 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125832826):
```
def group.mk' {α : Type*} [semigroup α] [has_one α] [has_inv α]
  (one_mul : ∀ (a : α), 1 * a = a)
  (mul_left_inv : ∀ (a : α), a⁻¹ * a = 1) : group α :=
have ∀ a : α, a * a = a → a = 1, from λ a h,
  calc a = a⁻¹ * a * a : by simp [mul_left_inv, one_mul]
    ... = a⁻¹ * a : by rw [mul_assoc, h]
    ... = 1 : mul_left_inv _,
have ∀ a : α, a * a⁻¹ = 1, from
λ a, this _ $ calc
  a * a⁻¹ * (a * a⁻¹)
      = a * (a⁻¹ * a) * a⁻¹ : by simp [mul_assoc]
  ... = a * a⁻¹ : by rw mul_left_inv; simp [mul_assoc, one_mul],
{ one_mul := one_mul,
  mul_left_inv := mul_left_inv,
  mul_one := λ a, show a * 1 = a,
    by rw [← mul_left_inv a, ← mul_assoc, this, one_mul],
  ..‹semigroup α›, ..‹has_one α›, ..‹has_inv α› }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 29 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125834341):
This is a common problem in making definitions --- do you go for maximal axioms (so that you don't need lots of lemmas later, and the big results follow easily from the definitions), or minimal axioms (so instances are easy to construct)? Often, the right solution in Lean is to go for maximal axioms with alternate constructors that require minimal axioms.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 29 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125836997):
```quote
The standard way to show that an axiom is redundant is to have an auxiliary constructor for `group` that doesn't have the redundant axioms
```
Yes but these are mathematicians with no functional programming background and I think they would prefer to see something which looks like an honest proof (never mention the axiom, then prove it) rather than wrapping anything in a complicated structure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 29 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125837057):
Mario your proof is in some sense canonical, but I prefer mine for pedagogical reasons.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 29 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125839656):
```quote
Just use a namespace and drop the fucking primes
```
Kenny can you do it? Namespaces seem to lead to overloading anyway.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 29 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125839695):
I am reluctant to prime the axioms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 29 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125839696):
but maybe I have to

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 29 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125840944):
> something which looks like an honest proof (never mention the axiom, then prove it)

I'm confused. Isn't that pretty much exactly what my proof does? I start with a semigroup with a one and inv, and the left_inv and one_mul axioms, and derive mul_one. There is no funny business at all, or complicated structures, it's literally just proving one statement from another, and then wrapping it up in a `group`. The proof part could also be factored out like so:
```
section
parameters {α : Type*} [semigroup α] [has_one α] [has_inv α]
  (one_mul : ∀ (a : α), 1 * a = a)
  (mul_left_inv : ∀ (a : α), a⁻¹ * a = 1)
include one_mul mul_left_inv

theorem group.mk'_aux1 {a : α} (h : a * a = a) : a = 1 :=
calc a = a⁻¹ * a * a : by simp [mul_left_inv, one_mul]
   ... = a⁻¹ * a : by rw [mul_assoc, h]
   ... = 1 : mul_left_inv _

theorem group.mk'_aux2 (a : α) : a * a⁻¹ = 1 :=
group.mk'_aux1 $ calc
  a * a⁻¹ * (a * a⁻¹)
      = a * (a⁻¹ * a) * a⁻¹ : by simp [mul_assoc]
  ... = a * a⁻¹ : by rw mul_left_inv; simp [mul_assoc, one_mul]

theorem group.mk'_aux3 (a : α) : a * 1 = a :=
by rw [← mul_left_inv a, ← mul_assoc, group.mk'_aux2, one_mul]

def group.mk' : group α :=
{ one_mul := one_mul,
  mul_left_inv := mul_left_inv,
  mul_one := group.mk'_aux3,
  ..‹semigroup α›, ..‹has_one α›, ..‹has_inv α› }

end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 29 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/125841574):
Another way to present a proof like this is via an auxiliary class like your `gripe`, like so:
```
class gripe (α : Type*) extends semigroup α, has_one α, has_inv α :=
(one_mul : ∀ (a : α), 1 * a = a)
(mul_left_inv : ∀ (a : α), a⁻¹ * a = 1)

namespace gripe
variables {α : Type*} [gripe α]

theorem eq_one_of_idem {a : α} (h : a * a = a) : a = 1 :=
calc a = a⁻¹ * a * a : by simp [mul_left_inv, one_mul]
   ... = a⁻¹ * a : by rw [mul_assoc, h]
   ... = 1 : mul_left_inv _

theorem mul_right_inv (a : α) : a * a⁻¹ = 1 :=
eq_one_of_idem $ calc
  a * a⁻¹ * (a * a⁻¹)
      = a * (a⁻¹ * a) * a⁻¹ : by simp [mul_assoc]
  ... = a * a⁻¹ : by rw mul_left_inv; simp [mul_assoc, one_mul]

theorem mul_one (a : α) : a * 1 = a :=
by rw [← mul_left_inv a, ← mul_assoc, mul_right_inv, one_mul]

instance (α) [gripe α] : group α :=
{ one_mul := one_mul,
  mul_left_inv := mul_left_inv,
  mul_one := mul_one,
  ..gripe.to_semigroup α,
  ..gripe.to_has_one α,
  ..gripe.to_has_inv α }

end gripe
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 02 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Writing%20readable%20uncluttered%20group%20theory/near/126004737):
Here's how it ended up. https://xenaproject.wordpress.com/2018/04/30/group-theory-revision/


{% endraw %}
