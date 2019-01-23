---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/29201zeroring.html
---

## Stream: [maths](index.html)
### Topic: [zero ring](29201zeroring.html)

---


{% raw %}
#### [ Kevin Buzzard (Sep 09 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133613106):
I'm working with polynomials and the zero ring is constantly a special case. There is a class `nonzero_comm_ring` extending comm_ring with the proposition that `0 \ne 1`, and several of Chris' results on polynomials need this as a hypothesis (for example the fact that degree of `X` is 1, and every corollary of this). Of course everything is true (and trivial) for the zero ring, but often the proofs need to be separate because of this. Because of the constructor for `nonzero_comm_ring` I am coming around to the idea to be splitting on `(0 : R) = 1` for lemmas which are true in the case R=0 but where the proof in the non-zero case is far from working for the zero ring.

So I now find myself wanting to prove things such as "if R is a ring and 0 = 1 then R is a fintype". I don't really know how to make that an instance, and I am not sure whether it should be an instance. On the other hand if I made a new class `zero_ring` then in some sense my life would be easier. Having said that, making a class for such a silly edge case seems a bit ridiculous. Should I just stick to proving lemmas rather than making this a class? I am slightly concerned that really I should be working with `zero_semiring` or something.

Another issue is that if I put `0 = 1 -> fintype R` into `ring.lean` then I have to add an import to `ring.lean` and I have this vague worry that I don't really know "which comes first" out of rings and fintypes.

#### [ Reid Barton (Sep 09 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133613814):
> "if R is a ring and 0 = 1 then R is a fintype"

Is this a real example, including the `fintype` part?

#### [ Reid Barton (Sep 09 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133613889):
Your `zero_ring` could be "lifted" all the way up to `is_singleton`, except we don't have it.

#### [ Chris Hughes (Sep 09 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133613892):
Rings definitely come before `fintype`. A more useful instance would perhaps be `0 = 1 -> subsingleton R`

#### [ Reid Barton (Sep 09 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133613899):
You can also use `subsingleton` in this case, yeah

#### [ Kevin Buzzard (Sep 09 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133613915):
```lean

lemma ring.zero_of_zero_eq_one {α} [ring α] (h01 : (0 : α) = 1) (a : α) : a = 0 :=
by rw [←one_mul a,←h01,zero_mul]

noncomputable definition ring.fintype_of_zero_eq_one {α} [ring α] (h01 : (0 : α) = 1) : fintype α := {
  elems := {0},
  complete := λ x, begin
    suffices: x = 0, by simpa,
    exact ring.zero_of_zero_eq_one h01 x,
  end
}

theorem ring.is_noetherian_of_zero_eq_one {R} [ring R] (h01 : (0 : R) = 1) : is_noetherian_ring R :=
@ring.is_noetherian_of_fintype R R _ _ $ ring.fintype_of_zero_eq_one h01
```

#### [ Reid Barton (Sep 09 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133613971):
Aha I see. I was wondering how you were using the `fintype`, but this makes sense.

#### [ Kevin Buzzard (Sep 09 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133613973):
I am trying to prove the Hilbert basis theorem for the zero ring :-)

#### [ Kevin Buzzard (Sep 09 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133614007):
I've proved that if a module is a fintype then it's Noetherian so I figured I'd use that.

#### [ Reid Barton (Sep 09 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133614049):
So you could use case analysis on whether R is a subsingleton, and show that if it isn't then $$0 \ne 1$$.
Then also make an instance that says that if R is a subsingleton then so is R[X].

#### [ Reid Barton (Sep 09 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133614079):
Or write a lemma `∀ R, subsingleton R ∨ ((0 : R) ≠ 1)`

#### [ Kevin Buzzard (Sep 09 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133614109):
I see. You're suggesting that I use what we currently have in the type class system by using a different class to convey what I'm trying to say, rather than making a new class. Thanks!

#### [ Reid Barton (Sep 09 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133614126):
Well, I would actually prefer that you make a new class but that it should be called `is_singleton` :)

#### [ Kevin Buzzard (Sep 09 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133614395):
Hmm. `subsingleton` is a Prop. Does this mean that type class inference won't get me from it to `fintype`?

#### [ Chris Hughes (Sep 09 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133614443):
Not computably.

#### [ Chris Hughes (Sep 09 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133614459):
It will for rings though

#### [ Kevin Buzzard (Sep 09 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133615195):
Proof now looks like

```lean
theorem ring.is_noetherian_of_zero_eq_one {R} [ring R] (h01 : (0 : R) = 1) : is_noetherian_ring R :=
by haveI := ring.subsingleton_of_zero_eq_one h01; exact ring.is_noetherian_of_fintype R R
```

#### [ Patrick Massot (Sep 12 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133793917):
I read that Kevin fights the zero ring. But what's the point of allowing this ring? Why don't we defined a ring with the assumption that 0 and 1 are different? Is it a trick in order to totalize certain constructions? Or is it needed from a categorical point of view (I guess it's a terminal object)?

#### [ Johan Commelin (Sep 12 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133793951):
I've never thought this through carefully, but I think it is indeed useful from a categorical point of view.

#### [ Kevin Buzzard (Sep 12 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133794730):
Funnily enough in my undergraduate ring theory course the lecturer made 0 not= 1 an axiom, and it caused them all sorts of problems. Whenever they formed a quotient ring R / I I would put my hand up and point out that they needed to assume that I was not R (which was not a natural thing to do on many occasions). On the other hand I was only an undergraduate and just assumed that this was an axiom of rings. It was only when I learnt algebraic geometry that I found out that it wasn't. Assuming 0 isn't 1 is a disastrous idea. In a separated scheme, the intersection of two affines is affine -- this sort of thing is used all the time. It would not be true if the empty scheme were not affine.

#### [ Patrick Massot (Sep 12 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133794785):
The quotient case is one of the examples I had in mind when I wrote "totalizing construction". The same probably happens with localization

#### [ Patrick Massot (Sep 12 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133794890):
> and i̶t̶  Kevin caused them all sorts of problems

#### [ Mario Carneiro (Sep 12 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133812772):
of course, Kevin's behavior there is exactly what lean would do to you if you tried to formalize it


{% endraw %}
