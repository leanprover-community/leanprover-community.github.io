---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/06032conflictofInstances.html
---

## Stream: [general](index.html)
### Topic: [conflict of Instances](06032conflictofInstances.html)

---

#### [AHan (Dec 04 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150822083):
I wanted to prove the following function, but I've run into problems at the commented line
Seems like lean interprets `≤ ` in `le_of_not_lt h₂` as the `le` defined in `linear_order` instead of `semilattice_sup_bot`, while `lattice.sup_of_le_left ` requires `le` defined by `semilattice_sup_bot`...
How can I fix this?

```lean
import data.finset
namespace finest

section
parameters {α : Type*} [lattice.semilattice_sup_bot α] [decidable_linear_order α]

lemma mem_of_sup_id' : ∀ {a : finset α}, a ≠ ∅ → a.sup id ∈ a
| a := finset.induction_on a (λ a, false.elim (a (refl _)))
    (λ x y notin ih notempty, begin 
        rw [insert_eq, sup_union, mem_union, sup_singleton] at *,
        simp,
        generalize hy : sup y id = y',
        from if h₁ : y = ∅ 
        then begin
            left,
            rw [h₁, sup_empty] at hy,
            rw [←hy, lattice.sup_bot_eq],
        end
        else begin
            from if h₂ : x < y'
            then begin
                right, 
                rw [lattice.sup_of_le_right (le_of_lt h₂), ←hy],
                apply ih h₁,
            end
            else begin
                left,
                --rw [lattice.sup_of_le_left (le_of_not_lt h₂)],
            end
        end
    end
end

end finset
```

#### [Sebastien Gouezel (Dec 04 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150828636):
You are introducing two orders which have nothing to do with each other, as both `semilattice_sup_bot` and `decidable_linear_order` contain an order. Instead, you need to start from one order only, and add some "mixin", i.e., some property of the order but not a new order. For instance, in `data/finset.lean`, you have
```lean
lemma sup_lt [is_total α (≤)] {a : α} : (⊥ < a) → (∀b ∈ s, f b < a) → s.sup f < a
```
Your problem can be solved in the same way.

#### [AHan (Dec 04 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150829193):
So I have to define another class which includes properties of `semilattice_sup_bot` and `decidable_linear_order`?

#### [Johan Commelin (Dec 04 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150829404):
Yes, I think so. So you define a class that `extends (semilattice_sup_bot X) (decidable_linear_order X).` I think you can just put a `.` after that extends statement, and then it will merge those two classes. You don't need any extra conditions, so you don't need a `:= (foo : blah)` part.

#### [Johan Commelin (Dec 04 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150829408):
But this is all from memory, so I might be wrong.

#### [AHan (Dec 04 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150829714):
@**Johan Commelin**  I've tried, but it outputs the error message :
"invalid 'structure' header, field 'le' from 'decidable_linear_order' has already been declared"...

```lean
class decidable_semilattice_sup_bot (α : Type*) extends (lattice.semilattice_sup_bot α), (decidable_linear_order α) .
```

`function expected at  lattice.semilattice_sup_bot α term has type  Type ?`
```lean
class decidable_semilattice_sup_bot (α : Type*) extends (lattice.semilattice_sup_bot α) (decidable_linear_order α) .
```

#### [Johan Commelin (Dec 04 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150829776):
Hmm, then I don't know. Maybe others can help.

#### [AHan (Dec 04 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150829847):
I checked `semilattice_sup_bot` which is extended from `order_bot` and `semilattice_sup`, and both of them are extended from `partial_order`, but it doesn't seems to conflict in this case...

#### [AHan (Dec 04 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150830288):
@**Johan Commelin**  Solved! Have to `set_option` lol
```lean 
set_option old_structure_cmd true
class decidable_semilattice_sup_bot (α : Type*) extends lattice.semilattice_sup_bot α, decidable_linear_order α
```

#### [Kevin Buzzard (Dec 04 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150830341):
This whole aspect of the type class inference system is very cumbersome. It would not surprise me if somewhere someone had made exactly the typeclass that you need to give you the structure you want, but finding it is another matter. The type class system is extremely fussy when it comes to this sort of thing. I am not sure how long the old structure command option will be around for...

#### [Kevin Buzzard (Dec 04 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150830498):
Although someone will no doubt come along and suggest a fix for your use case that doesn't involve the old structure command, I don't know how to solve this sort of problem in general. I guess it would be nice to be able to define the structures you wanted and then precisely insert them into the type class system by hand.

#### [Johan Commelin (Dec 04 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150830584):
I thought the entire type class system is going to be redone in :four_leaf_clover:. So by then `old_structure_cmd` will be `ancient_structure_cmd` and our current structures will be `old_structure`...

#### [AHan (Dec 04 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150830640):
Ancient ! LOL

#### [Sebastien Gouezel (Dec 04 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150830741):
As I tried to say, you can prove your lemma without introducing a new class, with
```lean
import data.finset
namespace finest

section
variables {α : Type*} [lattice.semilattice_sup_bot α] [is_total α (≤)]

lemma mem_of_sup_id' : ∀ {a : finset α}, a ≠ ∅ → a.sup id ∈ a
...
```

#### [AHan (Dec 04 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150830975):
@**Sebastien Gouezel**  That's nice! Thanks a lot!

#### [Sebastian Ullrich (Dec 04 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150831357):
(the typeclass inference system and the structure command are really quite orthogonal topics)

#### [Sebastian Ullrich (Dec 04 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150831579):
There are no semantic change planned so far for either of them. Though hopefully you'll be able to "just" copy and modify the structure command in Lean 4, after it's rewritten in Lean.

#### [Kevin Buzzard (Dec 04 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150831588):
```quote
orthogonal topics
```
Well, probably they are to a dev. Maybe the dev's answer to this question is "go and define the right mixins". The problems with this approach are (1) it doesn't seem to scale and (2) it confuses newcomers. It also means that mathematicians constantly make fun of Lean having a theory of distribs :D

#### [Patrick Massot (Dec 04 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150831711):
We have explicitl  promise that Johan will be able to define `ancient_structure` and `fancy_johan_structure` that will reuse parts of the grammar of the built-in command. http://leanprover.github.io/presentations/20181012_MSR/#/1

#### [Patrick Massot (Dec 04 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150831727):
Oh, I was too slow finding back the slides, Sebastian already mentioned it

#### [Kevin Buzzard (Dec 04 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150831755):
Ultimately mathematicians will want to define five new concepts A B C D E, and then 2^5 more concepts of the form "put together this subset of A B C D E" and will want all the obvious compatibiities to hold and will want them all to be typeclasses. Now the two concepts are kind of mixed together. I thought we had the explicit promise that nothing was going to change? In the back of my mind I always figured that if the type class system wasn't up to some complicated collection of maths structures then the answer is simple -- just don't use it.

#### [Kevin Buzzard (Dec 04 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150831836):
Oh but maybe I am beginning to understand the future better. The devs will leave us the structure command and type class system as it is, but will give us the tools to tweak it so that perhaps I can still do these 2^5 things in my own way and add exactly the fields I want to the type class inference system or whatever.

#### [AHan (Dec 04 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832214):
@**Sebastien Gouezel**  Sorry, I forgot to ask, what if I also wanted the decidable instance?
I can't just add `[decidable_rel (≤)]`...

#### [Kevin Buzzard (Dec 04 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832300):
```lean
variable α : Type

structure basic_thing α extends has_mul α :=
(basic : ∀ a : α, a * a * a = a * a)

-- mathematically sensible object
structure extension1 α extends basic_thing α :=
(thing1 : α)
(thing2 : α × α)

-- mathematically sensible object
structure extension2 α extends basic_thing α :=
(thing2 : α × α)
(thing3 : α × α × α)
(axiom1 : thing2.1 = thing3.1)

-- mathematically sensible object
structure extension3 α extends basic_thing α :=
(thing2 : α × α)
(thing7 : α × α × α × α)
(axiom2: thing7.1 = thing2.1)

-- mathematically sensible object
structure extension23 α extends basic_thing α :=...
-- I want to extend extension2 and extension3
-- but now I have to start defining mixins

-- insert 1000 lines of code here

-- object I realise I want later on
structure extension123 α extends basic_thing α :=...
-- oh dear, I now have to go back and refactor
-- everything because I want to extend 1 and 2 and 3 now
-- so maybe I need to remix my mixins
-- but the mixins are artificial objects anyway, I don't
-- really want to make new ones :-/
```

#### [Johannes Hölzl (Dec 04 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832348):
You need to annotate the `(≤)` in `[decidable_rel (≤)]`: `[decidable_rel ((≤) : α -> α -> Prop)]`

#### [Kevin Buzzard (Dec 04 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832432):
@AHan what happens if you just add exactly the extra hypotheses you need and then insert them manually into the type class inference system?

```lean
example ... (H : extra_axiom alpha) ... -- round brackets not square
...
begin
  letI := H, -- manually insert
  letI : decidable_linear_order alpha := { -- manually build },
...
end

#### [Kevin Buzzard (Dec 04 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832451):
You will I guess need to import `tactic.interactive` for this, from mathlib

#### [Kevin Buzzard (Dec 04 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832529):
Aah -- Johannes has a better solution ;-)

#### [AHan (Dec 04 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832535):
Still doesn't work at `(le_of_not_lt h₂)` in this case...
```lean
import data.finset
namespace finset
variables {α : Type*} 
variables [lattice.semilattice_sup_bot α] [decidable_rel ((≤) : α → α → Prop)] [is_total α (≤)]

lemma mem_of_sup_id : ∀ {a : finset α}, a ≠ ∅ → a.sup id ∈ a
| a := finset.induction_on a (λ a, false.elim (a (refl _)))
    (λ x y notin ih notempty, begin 
        rw [finset.insert_eq, finset.sup_union, finset.mem_union, finset.sup_singleton],
        simp,
        from if h₁ : y = ∅ 
        then begin
            left,
            rw [h₁, finset.sup_empty, lattice.sup_bot_eq],
        end
        else begin
            from if h₂ : x < y.sup id
            then begin
                right, 
                rw [lattice.sup_of_le_right (le_of_lt h₂)],
                apply ih h₁,
            end
            else begin
                left,                
                --rw [lattice.sup_of_le_left (le_of_not_lt h₂)],
            end
        end
    end)

end finset
```

#### [Kevin Buzzard (Dec 04 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832627):
@AHan can you post fully working code? I am lost with the imports, sections, parameters etc. I can try and fix it but it would be nice to just be able to cut and paste one thing

#### [Kevin Buzzard (Dec 04 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832639):
Sorry, I don't understand sections, parameters etc as well as most of the others here :-)

#### [Kevin Buzzard (Dec 04 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832652):
@**AHan**

#### [Johannes Hölzl (Dec 04 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832713):
`#check @le_of_not_lt` tells us that it really needs a `linear_order`.

#### [Kevin Buzzard (Dec 04 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832794):
@**AHan** oh it's Ok, I got your code (not) working.

#### [AHan (Dec 04 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832813):
@**Kevin Buzzard**  Sorry, I just edited the code!

#### [AHan (Dec 04 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833026):
@**Johannes Hölzl**  Yeah, so seems like `[is_total α (≤)]` can't work on this case?

#### [Johannes Hölzl (Dec 04 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833041):
Not when you want to use `le_of_not_lt`...

#### [AHan (Dec 04 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833089):
Or is there any better way to prove the function without needing `(≤)` to be a linear_order ...?

#### [Kevin Buzzard (Dec 04 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833091):
```lean
                haveI : linear_order α := by apply_instance, -- fails
                rw [lattice.sup_of_le_left (le_of_not_lt h₂)],
```

Your problem is that the type class inference system cannot figure out that alpha is a linear order.

#### [Kevin Buzzard (Dec 04 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833094):
Even though all the data is there.

#### [Kevin Buzzard (Dec 04 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833124):
You probably need to do some `refine_struct` stuff

#### [Kevin Buzzard (Dec 04 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833134):
This is a great example of exactly what the problem is.

#### [Johannes Hölzl (Dec 04 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833174):
Also not `haveI` but `letI` the order contains the relation

#### [Johannes Hölzl (Dec 04 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833181):
`letI : linear_order α := { le_total := _ },`

#### [Kevin Buzzard (Dec 04 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833183):
Oops, I always screw this up.

#### [Johan Commelin (Dec 04 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833209):
I think whenever there is data involved you should use `let` and not `have`.

#### [Kevin Buzzard (Dec 04 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833215):
```
invalid structure value { ... }, field 'le' was not provided
```

#### [Kevin Buzzard (Dec 04 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833222):
```quote
I think whenever there is data involved you should use `let` and not `have`.
```
 Sure -- I just always forget that there is data involved.

#### [Kevin Buzzard (Dec 04 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833285):
```quote
`letI : linear_order α := { le_total := _ },`
```
 I think we need to tell Lean about the partial order somehow. But I can never remember these arcane structure extension tricks.

#### [Kevin Buzzard (Dec 04 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833293):
Do we do refine_struct? extends? `by refine` somehow?

#### [Johannes Hölzl (Dec 04 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833324):
```
  letI : linear_order α :=
    { le_total := is_total.total (≤), .. _inst_1 },
```

#### [Johannes Hölzl (Dec 04 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833334):
`_inst_1` is the name of the semilattice sup bot instance.

#### [AHan (Dec 04 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833401):
Wow! It works!
But... I don't quite get why this work..?

#### [Kevin Buzzard (Dec 04 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833424):
@**AHan** what is happening with Johannes' magic code is that he is explicitly building the term of type `linear_order alpha` from the pieces you already have (`_inst_1` is the partial order etc) and then he is inserting it into the type class inference system with `letI`.

#### [Kevin Buzzard (Dec 04 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833484):
It is absolutely clear to anyone watching that this is a pretty hacky and horrible solution, but as far as I can see it is the only one we have that works in general.

#### [Patrick Massot (Dec 04 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833492):
Having to type `_inst_1` is always a bad omen

#### [Kevin Buzzard (Dec 04 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833508):
No doubt you can get around it with some sort of `by apply_instance` trickery. But ultimately this is not a situation which scales.

#### [Kevin Buzzard (Dec 04 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833560):
Ultimately one does not want `distrib`s because they are useless objects. They serve a purpose which is to give a hacky fix to a problem which deserves a better fix but which I have no ideas about.

#### [Kevin Buzzard (Dec 04 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833600):
```lean
class distrib (α : Type u) extends has_mul α, has_add α :=
(left_distrib : ∀ a b c : α, a * (b + c) = (a * b) + (a * c))
(right_distrib : ∀ a b c : α, (a + b) * c = (a * c) + (b * c))
```

a.k.a. "here are some axioms which make no sense by themselves, but which we need to beef up structure X to structure Y so we have to have an entirely new typeclass"

#### [Johannes Hölzl (Dec 04 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833714):
you can always give your `semilattie...` instance a concrete name, but then you need to mark it a `include` or add it to your theorem statement (the anonymous instances are always added as long as the type in you type class instance is used in the theorem statement)

#### [Mario Carneiro (Dec 04 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150835207):
this is one of my favorite uses of the french quotes for getting a term by its type

#### [Johan Commelin (Dec 04 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150835883):
Hah, now I can golf the `assumption` tactic:
```lean
example {X : Type} (x : X) : X :=
begin
  exact ‹_›
--assumption
end
```

#### [AHan (Dec 04 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150836031):
Oh I got it! Thanks a lot for the explanation!!

