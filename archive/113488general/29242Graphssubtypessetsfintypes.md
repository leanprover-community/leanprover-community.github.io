---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29242Graphssubtypessetsfintypes.html
---

## Stream: [general](index.html)
### Topic: [Graphs, subtypes, sets, fintypes](29242Graphssubtypessetsfintypes.html)

---

#### [Pablo Le Hénaff (Jun 15 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Graphs%2C%20subtypes%2C%20sets%2C%20fintypes/near/128121007):
Hello hello
I would like to formalize some theorems of graph theory, but before going any further I would like to get the basis of the implementation right.
I did do some work representing the edges as a set, but I didn't feel it was the most natural ways to do it. I tried another approach using the binary edge relation between vertices and lots of coercions from sets to subtypes, but it had me write lots of instances which I don't find particularily aesthetic. Here is a piece of code which is right but doesn't seem to carry the best design choices that could be made. What do you think ? :)
```lean
import data.set
open set

-- so my goal is to define graphs
-- I find the best way to implement them is as a structure with a set of vertices and a binary relation on those vertices
-- I like the coercion from sets to subtypes, but it looks like it makes things a little complicated with the little experience I have (see below)
constants {V : Type} (vertices : set V) (edge : vertices → vertices → Prop)

-- this is an extra convenient definition to allow the creation of "set edges" below
def edges : set (vertices × vertices) := λ⟨v₁,v₂⟩, edge v₁ v₂

-- I would like to reason on the edge binary relation rather than on the set of edges, that's why I suppose edge is a decidable rel
instance [H : decidable_rel edge] : decidable_pred edges := λ⟨v₁,v₂⟩, H v₁ v₂

-- set of edges whose tip is v ∈ vertices
-- used to define the "in-degree" of vertex v
-- in_edges has type "set edges" because I find it convenient, maybe it's not the best to do (too many coercions ?)
def in_edges (v : vertices) : set edges := let ⟨v,hv⟩ := v in λ⟨⟨_,⟨b,hb⟩⟩, _⟩, b = v

-- I need to use noncomputable because in_edges is a set whose base type is a subtype and
-- I only assume decidable_eq on V
-- but there exists subtype.decidable_eq...
#check subtype.decidable_eq

noncomputable instance [H : decidable_eq V] {v : vertices} : decidable_pred (in_edges v) := let ⟨v,hv⟩ := v in λ⟨⟨⟨a, ha⟩,⟨b,hb⟩⟩, _⟩, H b v
noncomputable instance {v : vertices} [fintype vertices] [decidable_rel edge] [decidable_eq V] : fintype (in_edges v) := @set_fintype _ (set_fintype _) _ _

variables [fintype vertices] [decidable_eq V] [decidable_rel edge]

-- now I want to define some stuff on finite graphs and prove some lemmas
-- for instance, the sum of the in_degrees of all the vertices is equal to fintype.card edges
-- which I did prove, but with another unpleasant setup
noncomputable def in_degree (v : vertices) := finset.card (in_edges v).to_finset
-- this doesn't work without the extra instances above
-- I would like instances to be inferred out-of-the-box but I didn't succeed
```

#### [Mario Carneiro (Jun 15 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Graphs%2C%20subtypes%2C%20sets%2C%20fintypes/near/128121155):
I think you are misusing `constants` here - this is equivalent to `axiom` in lean, while I think you mean something more like `variables` or `parameters`

#### [Pablo Le Hénaff (Jun 15 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Graphs%2C%20subtypes%2C%20sets%2C%20fintypes/near/128121326):
Probably ! My initial script involved the definition of a graph structure and then a graph as a variable. The "constants" part was just to make it shorter, should be "variables" then.

#### [Mario Carneiro (Jun 15 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Graphs%2C%20subtypes%2C%20sets%2C%20fintypes/near/128121338):
For the theory of possibly infinite graphs, I recommend using a type alpha of vertices and a binary relation E for the edges. In this context it does not differ substantially with order theory

#### [Pablo Le Hénaff (Jun 15 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Graphs%2C%20subtypes%2C%20sets%2C%20fintypes/near/128121400):
But then, how would you describe a subset of the vertices, for instance a clique ?

#### [Mario Carneiro (Jun 15 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Graphs%2C%20subtypes%2C%20sets%2C%20fintypes/near/128121450):
the subset itself can just be a `set A`

#### [Mario Carneiro (Jun 15 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Graphs%2C%20subtypes%2C%20sets%2C%20fintypes/near/128121456):
but if you want to talk about the induced subgraph you can use `subtype`

