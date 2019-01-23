---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/65860quantifierexercises.html
---

## Stream: [new members](index.html)
### Topic: [quantifier exercises](65860quantifierexercises.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 08 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561165):
could I get a hint how to make progress here:

https://gist.github.com/luxbock/853bdcdde0f333502055c6913fc91e9c

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 08 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561182):
You can't make progress without some classical axiom.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 08 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561221):
please provide a minimum *working* example (MWE).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 08 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561226):
Most directly, `classical.by_contradiction`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 08 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561272):
Or, wait. Also what Kenny said. Where did `a` come from?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 08 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561286):
sorry, I'll edit to include the full context and also my attempt with `by_contradiction` where I got stuck

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 08 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561341):
please provide a *minimum* working example (MWE).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 08 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561389):
https://gist.github.com/luxbock/853bdcdde0f333502055c6913fc91e9c updated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 08 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561447):
I don't think that's what you want to prove.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 08 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561512):
This `variable a : α` isn't doing what you want--now you have to prove `p a` for *every* `a`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 08 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561518):
this is one of the exercises from here:
https://leanprover.github.io/theorem_proving_in_lean/quantifiers_and_equality.html

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 08 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561524):
so my attempt is clearly wrong (it does not work after all), but I don't know how to make progress beyond `by_contradiction (λ ha, _)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 08 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561578):
I don't know how to go about getting a `p a` from what I have:
```
nanpx : (∀ (x : α), p x → false) → false,
hnpa : ¬p a
⊢ false
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 08 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561580):
> Notice that the declaration `variable a : α` amounts to the assumption that there is at least one element of type `α`. This assumption is needed in the **second** example, as well as in the **last two**.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 08 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561587):
your example is neither the second nor the last two

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 08 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561594):
You can never get `p a`, because `a` is an arbitrary member of `α`, and it might not be one for which `p` holds.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 08 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561638):
So line 11 `suffices hpa : p a, from ...` is already the wrong way to go.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 08 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561691):
The way to do this is to use `by_contradiction` at the top level--suppose `¬ (∃ x, p x)`, then what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 08 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561703):
thanks, I'll try to see where backtracking to beginning gets me. although now that @**Kenny Lau**  commented about the `variable` declaration, I'm a little bit confused about if I need to change anything outside this example

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 08 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561756):
oh I think I understand what you mean, I don't need the `variable` declaration for this particular example

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 08 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561761):
I just copy/pasted the exercises from the page and I'm filling in the `sorry`'s

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 08 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561824):
actually that can't be the case, so yeah I am confused about what you meant @**Kenny Lau**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 08 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561866):
You don't need `variable a : α`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 08 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561876):
I think I need it, because `p` uses it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 08 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561917):
oh sorry, I now realize what you meant

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 08 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133562068):
got it, thanks for the help

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Sep 09 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133587708):
I'm doing the same exercise atm!
I found some disparities in mathlib's intuitionist and classical namespaces, namely in intuitionist we have this:
```lean
theorem not_forall {p : α → Prop}
    [decidable (∃ x, ¬ p x)] [∀ x, decidable (p x)] :
  (¬ ∀ x, p x) ↔ ∃ x, ¬ p x :=
⟨not.imp_symm $ λ nx x, nx.imp_symm $ λ h, ⟨x, h⟩,
 not_forall_of_exists_not⟩

@[simp] theorem not_forall_not [decidable (∃ x, p x)] :
  (¬ ∀ x, ¬ p x) ↔ ∃ x, p x :=
by haveI := decidable_of_iff (¬ ∃ x, p x) not_exists;
exact not_iff_comm.1 not_exists
```
but in classical only this:
```lean
protected theorem not_forall : (¬ ∀ x, p x) ↔ (∃ x, ¬ p x) := not_forall
```
So from `classical.not_forall.mp h` with `h: ¬ ∀ x, ¬ p x` we get a double negation. Now, I know that `¬¬p ↔ p` is easy to prove from classical axioms, but despite how common its usage seems to be, there is no theorem for it built into the library. Is there some reason why double-negation is redundant, or should I make a PR to add it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133587798):
lean and mathlib are pretty huge, it would surprise me if `¬¬p ↔ p` were not there already.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133587800):
The idea is that you should use the "intuitionist" theorem and use `classical.dec` to fulfill the decidability assumptions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133587811):
(aka `classical.prop_decidable`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Sep 09 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133587813):
@**Kevin Buzzard** `#find` tells me that there are versions for `decidable p`, but not for generic propositions in classical reasoning

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Sep 09 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133587853):
@**Mario Carneiro** oh i see, so i should use all the `decidable` stuff with classical reasoning and then that one axiom to make it work? Ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133587871):
This is why you often see `local attribute [instance] classical.prop_decidable` at the top of files that do classical reasoning

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133587881):
I've taken to using `local attribute [instance, priority 1] classical.prop_decidable`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133587918):
because I ran into situations where this local attribute clobbered some decidability result which type class inference had given me and I ended up with typeclass problems.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133587936):
is `priority 0` problematic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Sep 09 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133588002):
I see, this attribute is indeed used in [`classical.lean`](https://github.com/leanprover/lean/blob/master/library/init/classical.lean#L90)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133588287):
```quote
is `priority 0` problematic?
```
my bad, I just went back to the file where some undergrads were having trouble and indeed I fixed it with `priority 0`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 11 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133703971):
is it possible to solve the barber paradox exercise without using `classical`?https://leanprover.github.io/theorem_proving_in_lean/quantifiers_and_equality.html

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 11 2018 at 04:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133704194):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 11 2018 at 04:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133704251):
can I have a hint? this is what I have so far:

```lean
example (h : ∀ x : α, S x x ↔ ¬ S x x) : false :=
have saa : S a a → ¬S a a, from (h a).mp,
have nsaa : ¬ S a a → S a a, from (h a).mpr, 
sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 11 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133704259):
hint: solve exercise 3.7.2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 11 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133704266):
also your problem statement isn't quite right for the barber paradox

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 11 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133704322):
thanks, looks like I actually overlooked 3.7.2, so I'll go back to that and try to figure it out from there (and also fix what you mentioned)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 11 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133704328):
```
example {α} (b : α) (r : α → α → Prop)
  (H : ∀ x : α, r b x ↔ ¬ r x x) : false := sorry
```


{% endraw %}
