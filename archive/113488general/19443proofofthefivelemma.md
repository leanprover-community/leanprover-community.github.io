---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/19443proofofthefivelemma.html
---

## Stream: [general](index.html)
### Topic: [proof of the five lemma](19443proofofthefivelemma.html)

---


{% raw %}
#### [ Johan Commelin (Apr 24 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618074):
Yoohoo, I'm done.
https://gist.github.com/jcommelin/9ea76f7a1356ed8dd9499e765f580ef8
It's pretty long and ugly.

#### [ Johan Commelin (Apr 24 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618084):
Feel free to start golfing on this one (-;

#### [ Johan Commelin (Apr 24 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618094):
I feel that a computer should almost be able to find the proof alone

#### [ Johan Commelin (Apr 24 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618132):
But my tactic-fu is small and my tactic-writing-fu is nonexistent

#### [ Sean Leather (Apr 24 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618139):
But how would the computer know how many times to `apply_assumption`? :dizzy_face: :laughing:

#### [ Johan Commelin (Apr 24 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618157):
Yeah, agreed... but still... every line I really just follow my nose...

#### [ Sean Leather (Apr 24 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618160):
The nice thing about your proof is that it is clearly step-by-step.

#### [ Johan Commelin (Apr 24 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618162):
And I guess already with the existing tactics I think it can be reasonably shortened

#### [ Johan Commelin (Apr 24 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618203):
Because using commutativity or computations in a group takes pretty long atm

#### [ Johan Commelin (Apr 24 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618223):
I feel like the lines with `\ex bla : Group, condition` are the only place that Lean should get my help.

#### [ Johan Commelin (Apr 24 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125618224):
The rest it should figure out alone...

#### [ Johan Commelin (Apr 24 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125622862):
/me updated the proof of the five lemma: https://gist.github.com/jcommelin/9ea76f7a1356ed8dd9499e765f580ef8

#### [ Johan Commelin (Apr 24 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125622867):
It is now refactored to first prove two four-lemmas

#### [ Johan Commelin (Apr 24 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125622871):
These then combine to prove the five lemma

#### [ Kenny Lau (Apr 24 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125622956):
```lean
begin
 split,
 apply four_lemma₁ com₁ com₂ com₃ eB₁ eC₁ eB₂ eC₂ hj hk.1 hm.1,
 apply four_lemma₂ com₂ com₃ com₄ eC₁ eD₁ eC₂ eD₂ hk.2 hm.2 hn,
end
```

#### [ Kenny Lau (Apr 24 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125622957):
now I would write this in term mode lol

#### [ Kenny Lau (Apr 24 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125622973):
```lean
⟨four_lemma₁ com₁ com₂ com₃ eB₁ eC₁ eB₂ eC₂ hj hk.1 hm.1, four_lemma₂ com₂ com₃ com₄ eC₁ eD₁ eC₂ eD₂ hk.2 hm.2 hn⟩
```

#### [ Johan Commelin (Apr 24 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125622974):
Aah, yes. I should have done that

#### [ Johan Commelin (Apr 24 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623014):
Also, can I use some `_` business to let it figure out the hypotheses itself?

#### [ Kenny Lau (Apr 24 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623020):
yes

#### [ Johan Commelin (Apr 24 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623026):
I tried... and failed :disappointed:

#### [ Kenny Lau (Apr 24 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623032):
you removed the wrong things :P

#### [ Kenny Lau (Apr 24 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623035):
`_` does not find the value from assumptions

#### [ Kenny Lau (Apr 24 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623036):
`_` only does unification

#### [ Kenny Lau (Apr 24 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623044):
and only first order (and zeroth order) unification

#### [ Johan Commelin (Apr 24 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623109):
Hmm, ok... But it should be able to figure out everything alone

#### [ Johan Commelin (Apr 24 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623111):
I will need to learn at some point how to do that

#### [ Kenny Lau (Apr 24 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623112):
it does **not** find the appropriate proofs from the asumptions

#### [ Johan Commelin (Apr 24 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623116):
No, but I mean the `com₁ com₂ com₃ eB₁ eC₁ eB₂ eC₂ hj hk.1 hm.1` stuff

#### [ Kenny Lau (Apr 24 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623127):
why would it be able to figure them out?

#### [ Kenny Lau (Apr 24 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623130):
the goal is `bijective l`

#### [ Kenny Lau (Apr 24 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623131):
it does not contain any of those things you mentioned

#### [ Kenny Lau (Apr 24 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623137):
they have to be found from the assumption list

#### [ Kenny Lau (Apr 24 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623139):
which `_` does not do

#### [ Kenny Lau (Apr 24 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623142):
`_` only unifies types

#### [ Johan Commelin (Apr 24 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623144):
Yes, and the type of `l` is `C_1 \to C_2`

#### [ Johan Commelin (Apr 24 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623187):
and those are mentioned in the statement, and there are requirements (e.g. a group `B_1` with a map to `C_1`

#### [ Kenny Lau (Apr 24 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623188):
but if you replace `com₁` with `_`, the compiler would have to find `com₁` from the assumptions

#### [ Johan Commelin (Apr 24 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623197):
...), and those are also in the context, etcc...

#### [ Kenny Lau (Apr 24 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623204):
it is not in the type of the goal

#### [ Kenny Lau (Apr 24 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623205):
it is not in the type of any component of the goal

#### [ Kenny Lau (Apr 24 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623209):
`_` does not find things from the local context

#### [ Kenny Lau (Apr 24 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623211):
(that is what I meant by assumption)

#### [ Kenny Lau (Apr 24 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623221):
```lean
H1 : something
H2 : something
|- goal
```

#### [ Kenny Lau (Apr 24 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623222):
`_` does not match against `H1` and `H2`

#### [ Kenny Lau (Apr 24 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623223):
unless the `goal` contains them

#### [ Johan Commelin (Apr 24 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623228):
I see

#### [ Johan Commelin (Apr 24 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623235):
So, maybe I should not have done `apply ...`, but `simp [four_lemma_1]`

#### [ Johan Commelin (Apr 24 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623238):
or something like that?

#### [ Kenny Lau (Apr 24 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623278):
does that work?

#### [ Kenny Lau (Apr 24 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623282):
I doubt that works

#### [ Kenny Lau (Apr 24 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623284):
try `apply four_lemma₁, repeat { assumption }`

#### [ Kenny Lau (Apr 24 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623306):
alternatively `apply four_lemma₁; try { assumption }`

#### [ Johan Commelin (Apr 24 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623366):
hmm, doesn't make it shorter... because it can't figure out `hk.1` on it's own...

#### [ Kenny Lau (Apr 24 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623369):
right

#### [ Johan Commelin (Apr 24 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623373):
never mind, I learned something (-;

#### [ Kenny Lau (Apr 24 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623377):
:)

#### [ Johan Commelin (Apr 24 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623394):
Next up: the snake lemma ???

#### [ Kenny Lau (Apr 24 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623399):
I heard one of them follows from the other

#### [ Johan Commelin (Apr 24 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623443):
I guess the snake lemma is stronger

#### [ Kenny Lau (Apr 24 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623451):
maybe we should have proved the snake lemma first :P

#### [ Johan Commelin (Apr 24 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623455):
lol

#### [ Johan Commelin (Apr 24 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623461):
There is also the salamander lemma

#### [ Johan Commelin (Apr 24 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623470):
And you can apply it 4 times to get the snake lemma

#### [ Kenny Lau (Apr 24 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623475):
then perhaps we should prove that first

#### [ Johan Commelin (Apr 24 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623485):
https://ncatlab.org/nlab/show/salamander+lemma

#### [ Johan Commelin (Apr 24 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623491):
My eyes always glaze over when I read that page

#### [ Kenny Lau (Apr 24 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623536):
:P

#### [ Kenny Lau (Apr 24 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125623572):
really, prove the strongest theorem, and your work will be minimized

#### [ Kevin Buzzard (Apr 27 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762769):
I need the three lemma

#### [ Kevin Buzzard (Apr 27 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762772):
I need that if A,B,C,A',B',C' are abelian groups

#### [ Kevin Buzzard (Apr 27 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762773):
and A -> B -> C is exact

#### [ Kevin Buzzard (Apr 27 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762776):
and A is isomorphic to A'

#### [ Kevin Buzzard (Apr 27 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762777):
and B to B'

#### [ Kevin Buzzard (Apr 27 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762778):
and C to C'

#### [ Kevin Buzzard (Apr 27 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762780):
and we have maps A' -> B' -> C'

#### [ Kevin Buzzard (Apr 27 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762782):
with both squares commuting

#### [ Kevin Buzzard (Apr 27 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762821):
then A' -> B' -> C' is exact

#### [ Kevin Buzzard (Apr 27 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762824):
As a mathematician my instinct is to do surgery on the first sequence

#### [ Kevin Buzzard (Apr 27 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762825):
i.e. simply replace A with A', B with B' and C with C' and then say we're done

#### [ Kevin Buzzard (Apr 27 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762832):
I am trying to work out if there is a general principle here

#### [ Kevin Buzzard (Apr 27 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762873):
but if there is, I don't think I can formulate it well in Lean yet.

#### [ Kevin Buzzard (Apr 27 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762884):
It says something like "if there is a commutative diagram, and you do some computation like image of this over kernel of this"

#### [ Kevin Buzzard (Apr 27 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762891):
"and then you take a term in the commutative diagram and replace it with an isomorphic term such that all the diagrams commute"

#### [ Kevin Buzzard (Apr 27 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762893):
"then the computation changes in the same way"

#### [ Kevin Buzzard (Apr 27 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762899):
but I fear that I am going to have to use three lemmas to prove the three lemma

#### [ Kevin Buzzard (Apr 27 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762900):
one for replacing A

#### [ Kevin Buzzard (Apr 27 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762901):
one for B

#### [ Kevin Buzzard (Apr 27 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762902):
and one for C

#### [ Kevin Buzzard (Apr 27 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762955):
or just prove it by brute force in one go

#### [ Kevin Buzzard (Apr 27 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762956):
and then deal with the fact that I'll need another trivial lemma of this form tomorrow, tomorrow

#### [ Kevin Buzzard (Apr 27 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762958):
I want more of this abstract nonsense in Lean

#### [ Kevin Buzzard (Apr 27 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762959):
either for abelian groups

#### [ Kevin Buzzard (Apr 27 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125762999):
or for abelian categories

#### [ Johan Commelin (Apr 27 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763020):
Hmm, I'm sorry that my five lemma doesn't help :slightly_frowning_face:

#### [ Kevin Buzzard (Apr 27 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763021):
yes, it's too strong :-)

#### [ Kevin Buzzard (Apr 27 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763023):
it proves something non-trivial

#### [ Johan Commelin (Apr 27 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763028):
Haha

#### [ Johan Commelin (Apr 27 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763070):
We need a very good way of substituting isomorphic things

#### [ Kevin Buzzard (Apr 27 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763071):
`rw` :-)

#### [ Johan Commelin (Apr 27 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763072):
I don't know much about HoTT, but I think this is what Voevodsky was after as well

#### [ Kevin Buzzard (Apr 27 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763073):
yes

#### [ Kevin Buzzard (Apr 27 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763074):
I wrote some vague mumblings about that in some other thread a week or so ago

#### [ Kevin Buzzard (Apr 27 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763075):
after reading some of his work

#### [ Kevin Buzzard (Apr 27 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763081):
but he redefined =

#### [ Johan Commelin (Apr 27 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763085):
Well, if you're changing from ZFC to type theory, might as well change '='

#### [ Johan Commelin (Apr 27 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763124):
Anyway, I guess that you are not saved by 5 `rw`s

#### [ Johan Commelin (Apr 27 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763137):
So we need @**Scott Morrison** 's category theory, and then some strong tactics that know about commutative diagrams

#### [ Johan Commelin (Apr 27 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125763339):
Or are you just going for a temporary brute force approach?

#### [ Kenny Lau (Apr 27 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125767661):
```lean
import algebra.group data.set data.equiv

def is_add_group_hom {α : Type*} {β : Type*} [add_group α] [add_group β] (f : α → β) : Prop :=
@is_group_hom (multiplicative α) (multiplicative β) _ _ f

attribute [class] is_add_group_hom

namespace is_add_group_hom

variables {α : Type*} {β : Type*} [add_group α] [add_group β] (f : α → β) [hf : is_add_group_hom f]

theorem mk (H : ∀ x y, f (x + y) = f x + f y) : is_add_group_hom f :=
⟨H⟩

theorem add (x y) : f (x + y) = f x + f y :=
@is_group_hom.mul (multiplicative α) (multiplicative β) _ _ f hf x y

theorem zero : f 0 = 0 :=
@is_group_hom.one (multiplicative α) (multiplicative β) _ _ f hf

theorem neg (x) : f (-x) = -f x :=
@is_group_hom.inv (multiplicative α) (multiplicative β) _ _ f hf x

def ker : set α :=
{ x | f x = 0 }

end is_add_group_hom

theorem three (A B C A' B' C' : Type*)
  [add_comm_group A] [add_comm_group A']
  [add_comm_group B] [add_comm_group B']
  [add_comm_group C] [add_comm_group C']
  (ab : A → B) [is_add_group_hom ab]
  (bc : B → C) [is_add_group_hom bc]
  (Habc : set.range ab = is_add_group_hom.ker bc)
  (fa : A ≃ A') [is_add_group_hom fa]
  (fb : B ≃ B') [is_add_group_hom fb]
  (fc : C ≃ C') [is_add_group_hom fc]

  (ab' : A' → B') [is_add_group_hom ab']
  (bc' : B' → C') [is_add_group_hom bc']
  (H1 : fb ∘ ab = ab' ∘ fa)
  (H2 : fc ∘ bc = bc' ∘ fb) :
  
  set.range ab' = is_add_group_hom.ker bc' :=
begin
  apply set.ext,
  intro b',
  split,
  { intro hb',
    cases hb' with a' ha',
    simp [is_add_group_hom.ker],
    let a := fa.symm a',
    have ha : fa a = a',
    { simp [a] },
    rw [← ha', ← ha],
    change bc' ((ab' ∘ fa) a) = 0,
    rw ← H1,
    change (bc' ∘ fb) (ab a) = 0,
    rw ← H2,
    have H3 : ab a ∈ is_add_group_hom.ker bc,
    { rw ← Habc, existsi a, simp },
    simp [is_add_group_hom.ker] at H3 ⊢,
    rw H3,
    apply is_add_group_hom.zero },
  { intro hb',
    let b := fb.symm b',
    have hb : fb b = b',
    { simp [b] },
    simp [is_add_group_hom.ker] at hb',
    rw ← hb at hb',
    change (bc' ∘ fb) b = 0 at hb',
    rw ← H2 at hb',
    rw ← is_add_group_hom.zero fc at hb',
    replace hb' := congr_arg fc.symm hb',
    simp at hb',
    have H3 : b ∈ set.range ab,
    { rwa Habc },
    cases H3 with a ha,
    existsi fa a,
    change (ab' ∘ fa) a = b',
    rw ← H1,
    simp [ha] }
end
```

#### [ Kenny Lau (Apr 27 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125767698):
@**Kevin Buzzard**

#### [ Kenny Lau (Apr 27 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125768067):
that's why I don't like stating equality with function composition

#### [ Kenny Lau (Apr 27 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125768238):
```lean
import algebra.group data.set data.equiv

def is_add_group_hom {α : Type*} {β : Type*} [add_group α] [add_group β] (f : α → β) : Prop :=
@is_group_hom (multiplicative α) (multiplicative β) _ _ f

attribute [class] is_add_group_hom

namespace is_add_group_hom

variables {α : Type*} {β : Type*} [add_group α] [add_group β] (f : α → β) [hf : is_add_group_hom f]

theorem mk (H : ∀ x y, f (x + y) = f x + f y) : is_add_group_hom f :=
⟨H⟩

theorem add (x y) : f (x + y) = f x + f y :=
@is_group_hom.mul (multiplicative α) (multiplicative β) _ _ f hf x y

theorem zero : f 0 = 0 :=
@is_group_hom.one (multiplicative α) (multiplicative β) _ _ f hf

theorem neg (x) : f (-x) = -f x :=
@is_group_hom.inv (multiplicative α) (multiplicative β) _ _ f hf x

def ker : set α :=
{ x | f x = 0 }

end is_add_group_hom

theorem three (A B C A' B' C' : Type*)
  [add_comm_group A] [add_comm_group A']
  [add_comm_group B] [add_comm_group B']
  [add_comm_group C] [add_comm_group C']
  (ab : A → B) [is_add_group_hom ab]
  (bc : B → C) [is_add_group_hom bc]
  (Habc : set.range ab = is_add_group_hom.ker bc)
  (fa : A ≃ A') [is_add_group_hom fa]
  (fb : B ≃ B') [is_add_group_hom fb]
  (fc : C ≃ C') [is_add_group_hom fc]

  (ab' : A' → B') [is_add_group_hom ab']
  (bc' : B' → C') [is_add_group_hom bc']
  (H1 : ∀ a, fb (ab a) = ab' (fa a))
  (H2 : ∀ b, fc (bc b) = bc' (fb b)) :
  
  set.range ab' = is_add_group_hom.ker bc' :=
begin
  apply set.ext,
  intro b',
  split,
  { intro hb',
    cases hb' with a' ha',
    simp [is_add_group_hom.ker],
    let a := fa.symm a',
    have ha : fa a = a',
    { simp [a] },
    rw [← ha', ← ha, ← H1, ← H2],
    have H3 : ab a ∈ is_add_group_hom.ker bc,
    { rw ← Habc, existsi a, simp },
    simp [is_add_group_hom.ker] at H3 ⊢,
    rw H3,
    apply is_add_group_hom.zero },
  { intro hb',
    let b := fb.symm b',
    have hb : fb b = b',
    { simp [b] },
    simp [is_add_group_hom.ker] at hb',
    rw [← hb, ← H2, ← is_add_group_hom.zero fc] at hb',
    replace hb' := congr_arg fc.symm hb',
    simp at hb',
    have H3 : b ∈ set.range ab,
    { rwa Habc },
    cases H3 with a ha,
    existsi fa a,
    rw ← H1,
    simp [ha] }
end
```

#### [ Kenny Lau (Apr 27 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125768242):
this is much better

#### [ Reid Barton (Apr 27 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125785178):
How about proving some lemmas like this one, and combining them into what you want.
```lean
import data.equiv

open set

lemma equiv_range {α β : Type*} (f : α → β) {α' β' : Type*} (f' : α' → β')
  (eα : α ≃ α') (eβ : β ≃ β') (h : f' ∘ eα = eβ ∘ f) :
  range f' = eβ '' range f :=
calc range f' = f' '' univ         : by rw image_univ
     ...      = f' '' (range eα)   : by rw range_iff_surjective.mpr eα.bijective.2
     ...      = f' '' (eα '' univ) : by rw image_univ
     ...      = (f' ∘ eα) '' univ  : by rw ←image_comp
     ...      = (eβ ∘ f) '' univ   : by rw h
     ...      = eβ '' (f '' univ)  : by rw image_comp
     ...      = eβ '' range f      : by rw image_univ
```

#### [ Reid Barton (Apr 27 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125786306):
(Now I see that Patrick said much the same thing about a half hour earlier.)

#### [ Johan Commelin (Apr 27 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125788582):
I should have used `calc` in my proof of the five lemma...

#### [ Kevin Buzzard (Apr 27 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125791112):
You live and learn in this game

#### [ Kevin Buzzard (Apr 27 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125791117):
Your levels were really helpful for me today. Do you know some abstract type theory?

#### [ Kevin Buzzard (Apr 27 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20of%20the%20five%20lemma/near/125791127):
You understood what Scott was saying


{% endraw %}
