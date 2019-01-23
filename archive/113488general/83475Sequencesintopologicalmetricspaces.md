---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83475Sequencesintopologicalmetricspaces.html
---

## Stream: [general](index.html)
### Topic: [Sequences in topological/metric spaces](83475Sequencesintopologicalmetricspaces.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rohan Mitta (Sep 07 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133532026):
Hi, 

I'm trying to prove some propositions about complete metric spaces and need to use sequences for them. I can't seem to find any lemmas in topological_space or metric_space to do with sequences, and was wondering if I should be trying to prove my own basic lemmas about sequences or if I missed something. I also wonder if I'm thinking about sequences properly. 

For example,  below I wanted to prove that if Y is a subset of a metric space, and y is an element of the closure of Y, then there exists a sequence in Y converging to y. Am I approaching this correctly? 

```lean
import analysis.metric_space
import order.filter

theorem lim_sequence_of_mem_closure {α : Type*} [metric_space α] (Y : set α) (a : α) (H : a ∈ closure Y) :
∃ (f : ℕ → α) (H1 : ∀ (n : ℕ), f n ∈ Y), filter.tendsto f filter.cofinite (nhds a)  := begin
  have := mem_closure_iff_nhds.1 H,
  let ball_n := λ (n : ℕ), ball a ((1 : ℝ)/n),
  
  have H1 : ∀ (n : ℕ), nonempty {x : α | x ∈ (ball_n (n+1)) ∩ Y},
    intro n,
    apply @nonempty_of_exists _ (λ _,true),
    have H2 := this (ball_n (n+1)) (ball_mem_nhds _ _),
    have H3 := set.exists_mem_of_ne_empty H2,
    cases H3 with xn Hxn,
    existsi (⟨xn, Hxn⟩ : ↥{x : α | x ∈ ball_n (n+1) ∩ Y}),
    trivial,
    sorry,

  have sequence := λ (n : ℕ), classical.choice (H1 n),
  let sequencevals := λ (n : ℕ), (sequence n).val,
  existsi sequencevals,
  have H1 : ∀ (n : ℕ), sequencevals n ∈ Y,
    show ∀ (n : ℕ), (sequence n).val ∈ Y,
    let sequenceprops := λ (n : ℕ), ((sequence n).property).2,
    exact sequenceprops,
  existsi H1,
  sorry,
  
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 07 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133532531):
I think we would want to state this over first countable spaces instead of metric spaces. What are you using it for?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rohan Mitta (Sep 07 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133533234):
I want to use it to help me show that a complete subspace Y of a metric space X is closed in X

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rohan Mitta (Sep 07 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133533304):
I'm working towards eventually proving Banach's fixed point theorem but am starting with some easier propositions about complete metric spaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 07 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133533540):
I'm pretty sure the first thing is already there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 07 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133533838):
but maybe not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 07 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133534094):
> complete subspace Y of a metric space X is closed in X

This has nothing to do with sequences, it generalizes to uniform spaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 07 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133534290):
It's not the same as your statement, but this lemma writes out the definition of complete so that we can say "a complete subspace Y of X"
```lean
lemma compact_of_totally_bounded_complete {s : set α}
  (ht : totally_bounded s) (hc : ∀{f:filter α}, cauchy f → f ≤ principal s → ∃x∈s, f ≤ nhds x) :
  compact s :=
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 07 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133534555):
This is what I recommend proving:

```lean
variables {α : Type*} [uniform_space α]
lemma is_closed_of_complete {s : set α} 
  (hc : ∀{f:filter α}, cauchy f → f ≤ principal s → ∃x∈s, f ≤ nhds x) :
  is_closed s :=
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rohan Mitta (Sep 07 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133534739):
Okay, I see, I'll try that. Thanks!
I've still got somewhat of a problem  because I can't see a way around using sequences for the proof of Banach's fixed point theorem, so I will need to eventually find a good way of dealing with them in order to do that. That can be a task for later at this point though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 07 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133535426):
The banach fixed point theorem looks pretty tied to metric spaces. I'm not sure how you could state it for uniform spaces. One possibility is some kind of well ordered filtration of the elements of the uniformity such that the contraction mapping forward maps each entourage to one that is strictly greater in the well order. That is, you have a antitone map `o` from entourages to ordinals such that if `S` is an entourage, then `o (map F S) > o S`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 07 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133535501):
Are you trying to help him or scare him?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 07 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133535662):
...that said, I think you should just try to prove the regular BFP on metric spaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 07 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133535712):
Is your definition of a complete subspace of a uniform space equivalent to asking the induced uniformity is complete?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 07 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133535843):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 07 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133535857):
it seems so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 07 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133535859):
we will probably want a proof of equivalence, but I'm not sure how hard the statement is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 07 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133535895):
I guess `complete_space s` is a Prop so that should work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 07 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133536009):
Then again, we have the theorem `complete_space s <-> is_closed s` so I guess the latter is a simpler way to write it :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 07 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133536079):
For Rohan, I would say that relevant lemmas as `cauchy_vmap` in `uniform_space.lean` and `is_closed_iff_nhds` in `topological_space.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 07 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133536083):
What?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 07 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133536086):
Which theorem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 07 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133536120):
I mean once Rohan proves it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 07 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133536128):
ah ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rohan Mitta (Sep 07 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133536676):
Thanks so much both of you! I'm going to sleep now but I'll see what I can do on it over the weekend.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 07 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133537576):
is it actually true if the uniform spaces are not separated?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 07 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133537768):
anyway, my wife calls me, so I'll give you my try. Note that the number of `@` suggests I'm doing it wrong (looks like I'm fighting the interface):
```lean
import analysis.topology.topological_space
import analysis.topology.uniform_space

variables {X : Type*} (Y : set X) [u : uniform_space X]

lemma aux (f : filter X) : filter.vmap (λ  y : Y, y.val) f ≠ ⊥ ↔ f ⊓ filter.principal Y ≠ ⊥ :=
sorry

lemma rohan (h : @complete_space Y (uniform_space.vmap (λ  y : Y, y.val) u)) : is_closed Y :=
begin
  letI : uniform_space Y := (uniform_space.vmap (λ  y : Y, y.val) u),
  rw is_closed_iff_nhds,
  intros x ne_bot,
  have := @cauchy_vmap Y X _ _ (nhds x) (λ  y : Y, y.val) (le_refl _) cauchy_nhds,
  rw aux at this,
  specialize this ne_bot,
  rcases complete_space.complete this with ⟨x', H⟩,
  sorry
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 07 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133537887):
I this the aux lemma sounds plausible. The status in the main proof is:
```lean
x : X,
x' : ↥Y,
H : filter.vmap (λ (y : ↥Y), y.val) (nhds x) ≤ nhds x'
⊢ x ∈ Y
```
which looks promising, except maybe if things are not separated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 07 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133538194):
The book I looked at on uniform spaces had a lot of Hausdorff assumptions which were not always really required, but rather seemed to be used as a device to ward off evil spirits

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 08 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133540912):
So Rohan is a mathematics undergraduate and whilst this filter stuff might be a cool way to do it (and I know he's read my filter blog post), I think there is some merit in seeing a proof which is more what mathematics undergraduates are used to. So here are some dumb questions. Is the epsilon-delta definition of a sequence tending to a limit in Lean? I'm assuming the fact that open balls are open and that x is in the closure of Y iff Y intersects every open set containing x. Given all this, it seems to me to be completely feasible to prove the lemma "the way a mathematician proves it".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 08 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133542300):
There is an epsilon delta definition of continuity in a metric space, but I don't think we've unfolded the definition of a sequence limit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 08 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133542312):
The sequence limit is provided via the `at_top` filter on `nat`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 08 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133563057):
@**Rohan Mitta** why not write down the mathematics proof you want to work in Lean and then see if you can get it to work. You might want to make some auxiliary definitions. I am still a bit unclear about whether the predicate "this sequence (i.e. function nat -> X) tends to this limit in the metric space X" is in Lean. I'm sure there will be some fancy filter version which works for second countable uniform semi-topologies or whatever, but the thing you're thinking about is a common notion in undergraduate mathematics and in my mind that is justifiction enough for it to be its own special predicate. I guess you could define it for topological spaces using open sets, and then prove that for metric spaces it's equivalent to the epsilon delta definition. This all sounds like very reasonable stuff to dump into an M2PM5 directory on the UROP repo (or the topology directory).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 08 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133563487):
I don't think we have the epsilon-N description of convergent sequences. For continuous functions we do have the epsilon-delta description, see `continuous_of_metric` and adjacent theorems.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 08 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133563488):
We should definitely have this. I'll need it for teaching.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 08 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133563493):
But it should be very easy to define

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 08 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133564349):
It's lunch time, so I can't golf the second half:
```lean
variables {α : Type*} [metric_space α]
open filter

example (u : ℕ → α) (a : α) : tendsto u at_top (nhds a) ↔ 
  ∀ ε > 0, ∃ (N : ℕ), ∀ {n}, n ≥ N → dist (u n) a < ε :=
⟨λ H ε εpos, mem_at_top_sets.1 $ mem_map.2 $ H (ball_mem_nhds _ εpos),
 λ H s s_nhd,
  begin
    rw [mem_map, mem_at_top_sets],
    rcases mem_nhds_iff_metric.1 s_nhd with ⟨ε, εpos, sub⟩,
    rcases H ε εpos with ⟨N, H⟩,
    existsi N,
    intros n nN,
    exact sub (mem_ball.2 $ H nN)
  end⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133621575):
I'm returning to this thread because I think this should go into mathlib:
```lean
lemma seq_tendsto_iff (u : ℕ → α) (a : α) : tendsto u at_top (nhds a) ↔ 
  ∀ ε > 0, ∃ (N : ℕ), ∀ {n}, n ≥ N → dist (u n) a < ε :=
⟨λ H ε εpos, mem_at_top_sets.1 $ mem_map.2 $ H (ball_mem_nhds _ εpos),
 λ H s s_nhd, let ⟨ε, εpos, sub⟩ := mem_nhds_iff_metric.1 s_nhd in
   let ⟨N, H'⟩ := H ε εpos in mem_at_top_sets.2 ⟨N, λ n nN, 
   sub $ mem_ball.2 $ H' nN⟩⟩
```
Mario, what do you think?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133621588):
For teaching purposes, we could even define a new abbreviation like `seq_tendsto u a` for `tendsto u at_top (nhds a)` but maybe this kind of things does not belong to mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133621628):
You can split that into two parts; first state it for an arbitrary filter and then reduce to the `nhds` filter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133621635):
Too late: I turned it into term mode, so now it's read-only

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133621640):
It cannot be modified anymore

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133623215):
```lean
lemma tendsto_nhds_iff (u : β → α) (f : filter β) (a : α) : tendsto u f (nhds a) ↔ 
  ∀ ε > 0, ∃ s ∈ f.sets, ∀ {n}, n ∈ s → dist (u n) a < ε :=
⟨λ H ε εpos, ⟨u ⁻¹' ball a ε, ⟨H $ ball_mem_nhds a εpos, λ n h, h⟩⟩,
 λ H s s_nhd, let ⟨ε, εpos, sub⟩ := mem_nhds_iff_metric.1 s_nhd in
   let ⟨N, ⟨N_in, H'⟩⟩ := H ε εpos in f.sets_of_superset N_in (λ b b_in, sub $ H' b_in)⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133623218):
Obfuscating is so fun

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133623220):
I understand how one could get addicted to it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133623281):
you missed a spot - `⟨N, ⟨N_in, H'⟩⟩` could be `⟨N, N_in, H'⟩`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133623299):
Oh you're right, the reader could infer from my version that N_in and H' go together

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133623339):
By the way, if this proof was replaced with `by finish` I would argue it is even more obfuscatory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 09 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133623681):
```quote
∀ ε > 0, ∃ (N : ℕ), ∀ {n}, n ≥ N → dist (u n) a < ε
```
Aah, it's just like the old days

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133623752):
The things we do for our students...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624326):
Mario, how would you call
```lean
lemma t [inhabited α] [semilattice_sup α] {p : α → Prop} :
(∃ (s : set α) (H : s ∈ (at_top : filter α).sets), ∀ n, n ∈ s → p n) ↔ 
(∃ N : α, ∀ n, n ≥ N → p n) :=
```
And do you have a one line long proof? It's meant to be a variation on `mem_at_top_sets` but deducing it is surprisingly painful here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624432):
My proof is
```lean
begin
  simp only [mem_at_top_sets, exists_prop],
  split ; intro h,
  { rcases h with ⟨s, ⟨⟨b, h⟩, h'⟩⟩,
    existsi b,
    intros n nb,
    exact h' _ (h n nb) },
  { rcases h with  ⟨N, h'⟩,
    existsi {a : α | a ≥ N }, 
    exact ⟨⟨N, λ _ x, x⟩, h'⟩ }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624586):
I don't think there is a one line proof, although both conditions are equivalent to `{n | p n} ∈ at_top.sets`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624645):
wait, isn't the proof `rfl`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624657):
No

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624661):
I mean
```
lemma t [inhabited α] [semilattice_sup α] {p : α → Prop} :
  {n | p n} ∈ at_top.sets ↔ (∃ N : α, ∀ n, n ≥ N → p n) := iff.rfl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624704):
I need to go sleeping but @**Rohan Mitta** you can use https://gist.github.com/PatrickMassot/1b2d39011855ba43f3bf00c08051ad9e if you want to play with sequences in metric spaces. The lemma at bottom bridges the gap between what you see in lectures and mathlib context

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624711):
oh, this is just `mem_at_top_sets`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624715):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624758):
the last bit you wrote is mem_at_top_sets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624763):
The question is: how to deduce my `t` lemma from this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624764):
The fact `(∃ (s : set α) (H : s ∈ F.sets), ∀ n, n ∈ s → p n) ↔ {n | p n} ∈ F.sets` is true in any filter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624769):
it's just saying that a filter is upward closed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624790):
frankly I'd avoid it simply because the lhs is needlessly verbose

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624832):
just use `upward_sets` if it looks like the hypotheses of the lhs are about to appear

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624839):
See the link above: the goal of this lemma is to allow the last proof to be so short

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624891):
I would state the previous theorem differently:
```
lemma tendsto_nhds_iff (u : β → α) (f : filter β) (a : α) : tendsto u f (nhds a) ↔ 
  ∀ ε > 0, {n | dist (u n) a < ε} ∈ f.sets := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133624907):
this would be even nicer if we had a quantifier-like notation for `{n | p n} ∈ f`, but I can live with this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rohan Mitta (Sep 13 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133882373):
Is this true? I can see how to go from an arbitrary sequence in a metric space to a filter, but don't see how it is possible in general to get from an arbitrary filter to a sequence. 

```lean
import analysis.metric_space
import order.filter
noncomputable theory

lemma complete_iff_seq_complete {α : Type*} [metric_space α] :
  complete_space α ↔ ( ∀ (f : ℕ → α), cauchy (filter.map f at_top) → (∃ (a : α), tendsto f at_top (nhds a)) :=
begin 
  split, intros H f Hf,
    exact (@complete_space.complete _ _ H _ Hf),
  sorry,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 13 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133884917):
You can get a sequence by for each n taking ε = 1/n and then applying the Cauchy property to the entourage of points at distance less than ε, and picking a point from the set you get out. `cauchy_of_metric` does some of this work for you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 13 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sequences%20in%20topological/metric%20spaces/near/133885019):
I haven't checked but I expect this this defines a Cauchy sequence which you can then use to show the original filter converges.


{% endraw %}
