---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79076Mathematicianslearningtactics.html
---

## Stream: [general](index.html)
### Topic: [Mathematicians learning tactics](79076Mathematicianslearningtactics.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318046):
```lean
instance : comm_monoid ℕ+ :=
{ mul       := λ m n, ⟨m.1 * n.1, mul_pos m.2 n.2⟩,
  mul_assoc := λ a b c, subtype.eq (mul_assoc _ _ _),
  one       := succ_pnat 0,
  one_mul   := λ a, subtype.eq (one_mul _),
  mul_one   := λ a, subtype.eq (mul_one _),
mul_comm := λ a b, subtype.eq (mul_comm _ _) }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318057):
https://github.com/leanprover/mathlib/blob/00a2eb4119d27761c8a6ee38eb1eae532cd3ac19/data/pnat.lean#L52

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318061):
All of the proofs of the axioms are the same

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318070):
"it's true for `nat` so done by `subtype.eq`"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318075):
Could I write that sentence as a tactic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318082):
I don't even know if that's possible because I don't know what tactics know about names

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318143):
I'm looking for a proof that defines `mul` and `one` and then says `done by tactic`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318210):
If I can do the above with a tactic then I think I can start to work on the tactic I actually want.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318216):
and maybe other mathematicians might like the same sort of tactics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318230):
Remember when we noticed that proving that if A and B were equiv and A was a ring then B was a ring, was actually quite annoying?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318243):
And Kenny would just knock off a proof and he'd just check all ten axioms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318254):
and every proof would be `funext, simp [name of thing I'm proving]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318296):
I think it's about time Kenny learnt how to write this tactic too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318312):
This is somewhat similar to Simon's pi instance tactic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318314):
Can you give me a link?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318327):
https://github.com/leanprover/mathlib/blob/master/algebra/pi_instances.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318339):
It's just the same underlying question Mario. It's some concept that is natural to us -- you exchange something with something that's equiv and then an algorithm goes off in our heads which just transfers a whole bunch of structure from one thing to the other effortlessly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318345):
but to be perfectly honest, the "Kenny method", which I used also in metamath days, actually gets things done

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318406):
It's only after you find yourself doing exactly the same thing ~20 times that you should start considering the tactic approach

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318420):
That's the point. I wonder if this is what I'm staring at.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318426):
with less than that, the time it takes to figure out how to write a tactic *eclipses* the time it would have taken to just copy paste get it over with

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318428):
I'm running into it again and again, constantly proving trivial things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318437):
and the reason I'm interested

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318439):
That's not the same

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318444):
is that the tactic formalises something which I do naturally in my brain

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318445):
if it's *different* trivial things, the tactic won't help

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318447):
and I like formalizing stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318451):
it will handle one kind of trivial and leave untouched 60 others

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318452):
This is the point at which I stop understanding

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318455):
and the only way I will understand

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318473):
is by trying to do it and failing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318499):
How many other proofs look like the proof of `comm_monoid pnat`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318500):
so I want to finally understand how difficult it is to write schoolkid.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318504):
I don't know Mario. That's what I want to find out.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318514):
Instead of saying "Mario go write schoolkid like I told you, it should be there"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318521):
it should already be in your file staring back at you before you want to consider writing a tactic automating it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318523):
I should just try to write it myself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318592):
Another way to put it: Tactics are a *refactoring technique*. You should already have a repetitive proof, and now you want to get the same thing done but easier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 30 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318616):
I also wonder whether you really need a tactic, or just a lemma/instance "a subtype of a monoid is a monoid if it's closed under multiplication and contains the identity"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318684):
^ this. In this world of automation, lemmas are unsung heroes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 30 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127320354):
that might be true in this case, but i think knowing how to write a tactic is a useful and core lean skill. Even if you don't write tactics, you should understand how they work so you can understand why they fail

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 30 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127320393):
obviously there is chapter 8 in programming in lean. now if you don't want to write anything complicated, the way forward is to browse through how the tactics are written in core lean, starting with the most basic ones like intro.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 30 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127320399):
(this is all on my to-do list as well, haha)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 30 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127320469):
for references there is John Harrison's "Practical Logic and Automated Reasoning", Chlipala's "Certified Programming with Dependent Types", although in Coq, is handy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 30 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127320585):
for some applications I have "Term Rewriting and All That", "Decision Procedures: An Algorithmic Point of View", "Modern Computer Algebra"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 30 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127320794):
All the way at the bottom of my very sad to-do list is: "learn Isabelle and study sledgehammer and nitpick" (some other popular and useful tactics...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 30 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127320822):
since i only make progress with Lean on the weekends, I'll see you guys in a few years :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 30 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321007):
But the `intro` tactic is written in C++, right? At least I found https://github.com/leanprover/lean/tree/dac6eec55661d3a2dab56859ffc05aef1aabb185/src/library/tactic, and it contains a lot of `cpp` files.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 30 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321123):
try `library/init/meta/interactive.lean`
```lean
meta def intro : parse ident_? → tactic unit
| none     := intro1 >> skip
| (some h) := tactic.intro h >> skip
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 30 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321207):
So what is the relation between this `lean`-file and the `cpp`-files that I found?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 30 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321289):
The tactics that you found are declared in Lean as constants:

```
meta constant intro_core    : name → tactic expr
meta constant intron        : nat → tactic unit
```

That is, they do not have Lean definitions and Lean simply executes the C++ implementation when they are called.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321647):
Dumb question:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321708):
what's the quickest way to generate a complete "blank" construction of a `comm_ring`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321712):
I want

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321718):
```
{mul := _,

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321725):
`mul_assoc := _,`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321731):
etc etc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (May 30 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321765):
`{..}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 30 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321819):
You should look into `pexpr.mk_structure_instance`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127322553):
Possibly first stupid question of many

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127322561):
```lean
instance semigroup [∀ i, semigroup $ f i] : semigroup (Π i : I, f i) :=
{ mul := begin intros, sorry end,
mul_assoc := sorry
}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127322575):
I am just trying to play with structures to see how far I can get in tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127322588):
but Lean doesn't like that instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127322628):
```
type mismatch at field 'mul_assoc'
  sorry
has type
  ∀ (a b c : Π (i : I), f i), ?m_1 (?m_1 a b) c = ?m_1 a (?m_1 b c)
but is expected to have type
  ∀ (a b c : Π (i : I), f i), a * b * c = a * (b * c)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127322630):
@**Sebastian Ullrich** thanks -- that comment helped!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127322634):
I'm still stuck though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127322666):
fixed it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127322669):
```lean
instance semigroup [∀ i, semigroup $ f i] : semigroup (Π i : I, f i) :=
{ 
mul_assoc := λ a b c,sorry,
mul := begin intros, sorry end,
}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127322676):
I think Mario once explained to me what was going on there but I still find it confusing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127323292):
I am experimenting with algebra.pi_instances

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127323297):
I kind of suspect that Kenny will know all the answers to my questions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127323332):
@**Kenny Lau** what's your golf proof of `instance comm_ring [∀ i, comm_ring $ f i] : comm_ring (Π i : I, f i)`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127323365):
Product of commutative rings is a ring.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127323385):
Do you have to write as many lines as there are axioms (plus a few more lines on top)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127323397):
Or can you do tricks -- but you can't use Simon's tactic, just stuff like simp

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127323402):
you can write tools

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127323406):
but in tactic mode, not new tactics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 30 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127324580):
```lean
instance pi.comm_ring {I : Type*} {f : I → Type*} [∀ i, comm_ring $ f i] : comm_ring (Π i : I, f i) :=
by refine
{ add := λ x y i, x i + y i,
  zero := λ i, 0,
  neg := λ x i, -x i,
  mul := λ x y i, x i * y i,
  one := λ i, 1,
  .. };
{ intros, funext,
  { apply add_assoc <|> apply add_zero <|> apply zero_add
    <|> apply add_left_neg <|> apply add_comm
    <|> apply mul_assoc <|> apply mul_one <|> apply one_mul
    <|> apply left_distrib <|> apply right_distrib
    <|> apply mul_comm } }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325167):
Kenny I want to play with the add/zero/neg etc part of your code

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325169):
but if I try this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325171):
```lean
instance pi.comm_ring {I : Type*} {f : I → Type*} [∀ i, comm_ring $ f i] : comm_ring (Π i : I, f i) :=
by refine
{ add := begin intros,sorry,end,-- λ x y i, x i + y i,
  zero := λ i, 0,
  neg := λ x i, -x i,
  mul := λ x y i, x i * y i,
  one := λ i, 1,
  .. };
{ intros, funext,
  { apply add_assoc <|> apply add_zero <|> apply zero_add
    <|> apply add_left_neg <|> apply add_comm
    <|> apply mul_assoc <|> apply mul_one <|> apply one_mul
    <|> apply left_distrib <|> apply right_distrib
    <|> apply mul_comm } }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 30 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325176):
how do you want to play with them?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325185):
then there's no definition of add so your tactic doesn't finish the job and the errors from this for some reason stop Lean from processing `add`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 30 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325192):
what do you want to change it to?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325201):
I want to change it into a begin end tactic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325248):
of the form "intros,funext,apply has_add.add end"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 30 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325254):
trust the force, Luke

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325285):
Can you write a tactic which does add,zero,neg,mul and one?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 30 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325301):
not really

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325306):
In every case it's "deduce it from the factors"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127327884):
I'm not clear on why we're rehashing this. You are rediscovering Simon's tactic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328137):
```lean
namespace pi
variable {I : Type}     -- The indexing type
variable {f : I → Type} -- The family of types already equiped with instances

class notation_crazy_structure_that_someone_else_wrote (α : Type) extends has_add α,
has_mul α, has_zero α, has_one α, has_neg α, has_le α :=
(a : α)
(H : a + a * 0 ≤ -1)

instance can_a_tactic_prove_me [∀ i, notation_crazy_structure_that_someone_else_wrote $ f i] :
notation_crazy_structure_that_someone_else_wrote (Π i : I, f i) := sorry 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328145):
I'm trying to learn it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328238):
I can't prove that with pi_instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328254):
I am hoping I can just have a proof of the form "by canonical"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328266):
I have to learn it because I can't keep pestering Simon every time I want it to do a bit more

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328440):
no extra inputs or anything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328458):
because isn't it true that all that structure just transfers over completely canonically?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328540):
@**Simon Hudon** can `pi_instance` do this without being fed any extra information whatsoever?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328563):
Lean needs to get better at doing stuff which mathematicians find trivial

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 30 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328635):
Do what specifically?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 30 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328636):
(deleted)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328683):
construct the instance above called `can_a_tactic_prove_me`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328725):
Is it possible to write a tactic which proves a goal like that without any extra prodding?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 30 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328730):
I think so.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328740):
By generalising your pi_instance tactic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 30 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328857):
I'm working on a set of tactics to replace `pi_instance`. It would be the dual of `cases` / `case` which I call `refine_struct`/ `field` / `apply_field`. Basically, you write `refine_struct { .. } ; intro ; apply_field`. Maybe you'd need a bit more but you would have a generic way of referring to the field that you're looking into

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328918):
oh wow!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 30 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328953):
I've been procrastinating with writing my dissertation and working but I should get back to it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328962):
Yes that's exactly the sort of conclusion I was coming to (that's why I was asking about `..`). I wanted to do `begin refine { .. },...` but was having trouble with it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328969):
Well can I write these tactics somehow?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328976):
Or Kenny when he's finished doing my project?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 30 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127329067):
It is actually some pretty tricky stuff so it would be easier for me to just do it than to explain how to do it. Although, I'd like to also write a tutorial about it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127329164):
Darn it I need a route into this stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 30 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127329194):
In the mean time, I have a goodie coming up: a tactic that asserts that subtractions have non-negative results (they don't hit the floor of natural numbers) and a tactic that assert that all divisors are non-null

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127329201):
I need to find a tactic which I can write and is somehow distantly related to what I want to be able to do with tactics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127329253):
subtractions -- Patrick will be over the moon!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 30 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127329342):
If you want, I can show you my subtraction tactic and let you figure out the version for division

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127329369):
I could have a look!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127329374):
Somehow it's the canonical stuff that I'm interested in though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 30 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127329426):
What do you mean by canonical?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 30 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127330210):
Feel free to try your hand on https://gist.github.com/cipher1024/72af1694ce395d7162bab1a72c1f9c56

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 31 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127349075):
Thanks Simon! I'll have a very close look at that (but probably not today :disappointed: )

