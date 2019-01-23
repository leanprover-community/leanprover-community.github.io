---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89192targetteddefinitionalreduction.html
---

## Stream: [general](index.html)
### Topic: [targetted definitional reduction](89192targetteddefinitionalreduction.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127246965):
The history of this question is the following: I had a complicated goal which could be reduced using a definitional unfolding which for some reason wasn't happening -- "unfold" wouldn't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127246970):
I wanted to do the unfold manually with a rw so I asked the name of the theorem that `{a := x, b := y}.a = x`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127246972):
and I was told that this theorem had no name

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127246978):
because it was true by refl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127246982):
On the other hand, browsing through the library I see a bunch of things with names whose proof is rfl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247027):
All the other suggestions for what to do were not good for me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247039):
"Change it yourself with show" -- yeah but this is a PITA because my structure is a very complicated structure with a very long name and it is being constructed using very long terms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247045):
and I know *precisely* how I want *this precise term* to unfold and I don't want to do anything else to the goal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247059):
If I change it myself with show then I have to work out what I want the goal to be using pencil and paper! It's 2018!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247065):
I _need_ to change it because rw is really fussy, it won't rw something defeq to what you want sometimes -- it sometimes needs help

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247067):
and the line after my show line was a complicated rw

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247110):
Here's what I want to do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247115):
I want to zoom in to the area I am interested in using conv

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247120):
and I want to run dsimp or some such thing just on that one term

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247121):
Is this possible?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247122):
I don't think so.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247125):
conv offers me exciting commands such as "to_lhs"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247130):
what about "to 3rd input of this function"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247136):
Can conv do that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247142):
Can I do dsimp in conv?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247151):
I use tactic mode precisely because I like the precise control I have over what is going on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247154):
but as I get older and wiser and understand more about what is happening, I want more precise tools

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247202):
I can do dsimp in conv mode :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247203):
so my question becomes how to access the 3rd input to a function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247207):
goal is `f x y = g z`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247212):
and I want to run dsimp on y only

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247213):
how do I do that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247218):
Ok I just thought of a solution which again will work in many cases

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247222):
just define exactly the rewrite I want, call it H, and rw H

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247224):
This gets me back to the original problem though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247226):
I do not want to run dsimp in my head

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247229):
I am too lazy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247271):
I am a big boy now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 29 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247273):
what's wrong with `dsimp`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247277):
simplifies too much

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247279):
that's the wrong question

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 29 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247281):
no, that's the standard solution

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247284):
unless you are genuinely convinced that I really never want to run dsimp on just a subterm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247288):
Let me go back to my usage case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 29 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247296):
you can use `dsimp only` or other such tricks to limit the unnecessary simping

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 29 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127257747):
`unfold structure.a` sometimes works for me in these situations.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266078):
In my usage case, dsimp doesn't do anything at all

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266492):
the goal is (function x y z).F H -> Z`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266501):
and `function x y z` creates a structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266505):
by saying what all the bits and pieces are

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266508):
including F

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266511):
dsimp does nothing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266515):
I can't get conv to get to it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266577):
is it because it's a pi type?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266622):
In the end I copied the context, scrolled to the end of the proof, pasted it, changed `X : y,` to `(X : y)` about ten times and made them all variables, and then used `#reduce` and then cut and pasted the answer back in the proof and wrote "show" in front of it, and then farted around with some pp.proof on to get it to work and I was done

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266624):
That can't be the best way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266676):
that's not even true

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266680):
#reduce didn't do it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266684):
no wait

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266686):
it half did it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266689):
it did enough of it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266699):
it unfolded (function x y z).F into (some function of x y and z)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266711):
Why did this cause me such pain? What did I miss?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127267136):
```lean
import analysis.topology.topological_space scheme

set_option pp.proofs true 

theorem presheaves_iso (X : Type) [H : topological_space X] (F : presheaf_of_types X) : 
are_isomorphic_presheaves_of_types
    (presheaf_of_types_pullback_under_open_immersion F id 
      (topological_space.open_immersion_id _))
    F
:= 
begin 
  constructor,tactic.swap,
  { constructor,tactic.swap,
    { intros U HU,
      have Hid := topological_space.open_immersion_id X, 
      -- goal now
      show (presheaf_of_types_pullback_under_open_immersion F id Hid).F HU → F.F HU,
      --unfold presheaf_of_types_pullback_under_open_immersion, -- fails
      show (F.F ((Hid.fopens U).mp HU)) → F.F HU, -- obtained by "#reduce" calculation below
      show (F.F (_ : is_open (id '' U)) → F.F HU), -- obtained by more out-of-proof unravelling

      sorry
    },sorry,
    
  },
  sorry
end 
variables 
(X : Type)
(H : topological_space X)
(F : presheaf_of_types X)
(U : set X)
(HU : topological_space.is_open H U)
(Hid : topological_space.open_immersion (@id X))

#reduce (presheaf_of_types_pullback_under_open_immersion F id Hid).F
-- λ (U : X → Prop) (HU : topological_space.is_open H U), F.F ((Hid.fopens U).mp HU)
#check (Hid.fopens U).mp -- is_open U → is_open (id '' U)


#exit 

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127267142):
What my code looks like

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 29 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127267540):
It doesn't run for people who don't have my repo because it needs scheme.lean but I hope it explicitly shows the problem. I don't know how to get Lean to unfold `(presheaf_of_types_pullback_under_open_immersion F id Hid).F`, possibily because it's in a lambda, but it is defeq to something much simpler which I work out outside the proof after some copying of context (IRL the context was huge and I just did the unravelling using cut and paste)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 29 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127267590):
You should have a simp lemma for the value of `.F`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 29 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127267671):
alternatively, you can `dsimp [function]` to unfold it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127278172):
```quote
You should have a simp lemma for the value of `.F`
```
Talking through pnat was very instructional. I realise that I have a very poor feeling about what should be a simp lemma. I made that structure though -- these lemmas aren't automatically added when I make the structure? What is added to the simp machine?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127278180):
```quote
alternatively, you can `dsimp [function]` to unfold it
```
This is what I needed to know :-) Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127278221):
Even though my function isn't a simp lemma :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127278222):
`simp`  will reduce terms that look like `<a, b, c>.2`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127278229):
where `<>` is the builtin structure constructor and `.2` is a builtin projection

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127278241):
If there are any definitions shielding the redex from looking like that, simp won't find it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127278246):
like `(f x y z).F`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127278247):
right

