---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/60703hasmemdisjoint.html
---

## Stream: [general](index.html)
### Topic: [has_mem disjoint](60703hasmemdisjoint.html)

---


{% raw %}
#### [ Sean Leather (Oct 02 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017185):
Currently, there is this definition in `data/list/basic.lean`:

```lean
def disjoint (l₁ l₂ : list α) : Prop :=
∀ ⦃a⦄, a ∈ l₁ → a ∉ l₂
```

Would there be any interest in replacing it with the following more general version?

```lean
def disjoint {α β₁ β₂} [has_mem α β₁] [has_mem α β₂] (b₁ : β₁) (b₂ : β₂) : Prop :=
∀ ⦃a : α⦄, a ∈ b₁ → a ∉ b₂
```

I'm using the latter quite a lot, and a number of the `list` theorems can be stated about it instead.

#### [ Simon Hudon (Oct 02 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017241):
Can those list theorems be generalized too?

#### [ Sean Leather (Oct 02 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017249):
A number of them could.

#### [ Simon Hudon (Oct 02 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017259):
What assumptions do they need on top of `has_mem`?

#### [ Sean Leather (Oct 02 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017312):
I haven't looked into it, but theorems like this obviously need `list`s:

```lean
theorem disjoint_of_disjoint_cons_left {a : α} {l₁ l₂} : disjoint (a::l₁) l₂ → disjoint l₁ l₂ 
```

#### [ Sean Leather (Oct 02 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017321):
But this...

```lean
theorem disjoint.symm {l₁ l₂ : list α} (d : disjoint l₁ l₂) : disjoint l₂ l₁
| a i₂ i₁ := d i₁ i₂
```

#### [ Kenny Lau (Oct 02 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017383):
you mean `lattice.disjoint`

#### [ Simon Hudon (Oct 02 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017384):
I guess you could also reformulate the first one to use `insert`

#### [ Sean Leather (Oct 02 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017386):
For me, the latter `disjoint` is useful when mixing `list` and `finset`.

#### [ Sean Leather (Oct 02 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017398):
```quote
you mean `lattice.disjoint`
```
I don't think I do. I specifically want `has_mem`.

#### [ Kenny Lau (Oct 02 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017401):
but what structure has mem?

#### [ Sean Leather (Oct 02 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017403):
Also, `β₁` and `β₂` are different.

#### [ Kenny Lau (Oct 02 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017404):
does this make much sense for `option.has_mem`?

#### [ Sean Leather (Oct 02 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017452):
```quote
I guess you could also reformulate the first one to use `insert`
```
I don't think you want to do that. It's a useful theorem by its own right.

#### [ Simon Hudon (Oct 02 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017462):
Right, I would keep both

#### [ Sean Leather (Oct 02 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135017605):
Kenny: I don't understand what you mean. Plenty of things have `has_mem` instances:

```lean
category_theory/examples/topological_spaces.lean:instance : has_mem X.α (open_set X) :=
computability/partrec_code.lean:instance : has_mem (ℕ →. ℕ) code := ⟨λ f c, eval c = f⟩
data/finset.lean:instance : has_mem α (finset α) := ⟨λ a s, a ∈ s.1⟩
data/hash_map.lean:instance : has_mem α (hash_map α β) := ⟨λa m, m.contains a⟩
data/multiset.lean:instance : has_mem α (multiset α) := ⟨mem⟩
data/option.lean:instance has_mem : has_mem α (option α) := ⟨λ a b, b = some a⟩
data/pfun.lean:instance : has_mem α (roption α) := ⟨roption.mem⟩
data/semiquot.lean:instance : has_mem α (semiquot α) := ⟨λ a q, a ∈ q.s⟩
data/seq/computation.lean:instance : has_mem α (computation α) := ⟨computation.mem⟩
data/seq/seq.lean:instance : has_mem α (seq α) :=
data/seq/wseq.lean:instance : has_mem α (wseq α) :=
data/seq/wseq.lean:    unfold cons has_mem.mem wseq.mem seq.mem seq.cons, simp,
linear_algebra/submodule.lean:instance : has_mem β (submodule α β) := ⟨λ x y, x ∈ (y : set β)⟩
logic/basic.lean:theorem ne_of_mem_of_not_mem {α β} [has_mem α β] {s : β} {a b : α}
set_theory/lists.lean:instance {b} : has_mem (lists α) (lists' α b) :=
set_theory/lists.lean:instance : has_mem (lists α) (lists α) := ⟨mem⟩
set_theory/zfc.lean:instance : has_mem pSet.{u} pSet.{u} := ⟨mem⟩
set_theory/zfc.lean:instance : has_mem Set Set := ⟨mem⟩
set_theory/zfc.lean:show @has_mem.mem _ _ Set.has_mem y ⟦⟨α, A⟩⟧ → p y, from
set_theory/zfc.lean:instance : has_mem Class Class := ⟨Class.mem⟩
```

#### [ Kenny Lau (Oct 02 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135018358):
how did you search that?

#### [ Kenny Lau (Oct 02 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135018400):
oh, it's a grep right

#### [ Sean Leather (Oct 02 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135018684):
```quote
how did you search that?
```
`git grep has_mem`

#### [ Simon Hudon (Oct 02 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135018757):
Why not `#print instances has_mem`?

#### [ Sean Leather (Oct 02 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135018826):
Why not? You could use that, too. `git grep` is faster and, in this case, useful enough.

#### [ Simon Hudon (Oct 02 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135018878):
I accept your answer.

#### [ Johannes Hölzl (Oct 02 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135019217):
I don't think a `has_mem` version of `disjoint` makes sense. You get surely some basic facts from the implication. But otherwise we don't have any structure behind `mem`. Its better to use the `lattice` version.

#### [ Sean Leather (Oct 02 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135019292):
In my case (which may be strange), I can't use the `lattice` version. It requires the types to be the same.

#### [ Mario Carneiro (Oct 02 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135019293):
Note that anything that satisfies that definition also fits the lattice definition (at least mathematically), since it can be expressed on the lattice of sets `{x | x \in s}`

#### [ Sean Leather (Oct 02 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135019353):
In particular, I want to show that a `list` and a `finset` are disjoint.

#### [ Mario Carneiro (Oct 02 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135019355):
oh, I see you've made the types different

#### [ Mario Carneiro (Oct 02 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135019367):
just say `l1.to_finset.disjoint s2`

#### [ Sean Leather (Oct 02 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135019376):
```quote
just say `l1.to_finset.disjoint s2`
```
That adds the extra baggage of `to_finset`, which I don't need.

#### [ Sean Leather (Oct 02 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135019388):
I really just want `∀ ⦃a : α⦄, a ∈ b₁ → a ∉ b₂`.

#### [ Mario Carneiro (Oct 02 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135019443):
then define it for yourself

#### [ Mario Carneiro (Oct 02 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135019452):
I don't see strong evidence that this is a common case

#### [ Sean Leather (Oct 02 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020502):
```quote
I don't think a `has_mem` version of `disjoint` makes sense. You get surely some basic facts from the implication. But otherwise we don't have any structure behind `mem`.
```

Just to make my final case for the `has_mem`-based `disjoint` above before I go away. :slight_smile:

Advantages:

1. It provides a nice generalization of the `list`-based `disjoint`. So, you can define the basic implication facts such that they work for other types beside `list`. And, yet, you can also define the `list` `disjoint` facts just as they are, so you don't lose anything.
2. It works with two different types, while the `lattice` `disjoint` doesn't.
3. Useful simplification theorems can be defined for different combinations of types.

Disadvantages:

1. It adds too much generality?

(I'm having trouble thinking of disadvantages.)

#### [ Mario Carneiro (Oct 02 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020550):
can you do the lattice disjoint using has_mem disjoint?

#### [ Sean Leather (Oct 02 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020615):
```quote
can you do the lattice disjoint using has_mem disjoint?
```
What do you mean?

#### [ Mario Carneiro (Oct 02 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020625):
you say it's more general, but it doesn't capture the generality of lattices

#### [ Mario Carneiro (Oct 02 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020638):
so it's really just a generalization in a different direction

#### [ Sean Leather (Oct 02 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020647):
More general in the sense that the “sets” are different even though the element type is the same.

#### [ Sean Leather (Oct 02 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020651):
```quote
so it's really just a generalization in a different direction
```
Yes.

#### [ Mario Carneiro (Oct 02 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020656):
In particular, I like that the bottom element need not be the empty set / "false"

#### [ Mario Carneiro (Oct 02 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020700):
i.e. when I am talking about disjoint subgroups

#### [ Mario Carneiro (Oct 02 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020721):
This kind of generality gets use in several places in mathlib. Multiple type disjointness does not

#### [ Mario Carneiro (Oct 02 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020732):
If it comes up, I'm prepared to consider a definition but we have zero theorems that need this right now

#### [ Sean Leather (Oct 02 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020734):
Yeah, so this is not a very mathematically elegant generality, more of a practical one. :slight_smile:

#### [ Mario Carneiro (Oct 02 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020778):
if all the theorems are in your project, then so should this definition

#### [ Mario Carneiro (Oct 02 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020820):
I'm not saying it's a bad definition, but it is certainly "premature optimization" for mathlib

#### [ Sean Leather (Oct 02 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135020883):
That may be.

#### [ Simon Hudon (Oct 02 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20disjoint/near/135057773):
You could have a function `to_set [has_mem a b] : b -> set a` for which @**Sean Leather**' version of `disjoint` is consistent with `to_set a ∩ to_set b = ∅` even if `a` and `b` have different types.


{% endraw %}
