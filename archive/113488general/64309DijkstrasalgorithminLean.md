---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64309DijkstrasalgorithminLean.html
---

## Stream: [general](index.html)
### Topic: [Dijkstra's algorithm in Lean](64309DijkstrasalgorithminLean.html)

---


{% raw %}
#### [ Kevin Buzzard (Dec 08 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dijkstra%27s%20algorithm%20in%20Lean/near/151183263):
One of my children was explaining Dijkstra's algorithm to me -- they are far more computer-sciency than I am. After some conversation I decided that they might be saying this:

```lean
-- Dijkstra's algorithm in Lean

import data.fintype

structure finite_directed_graph :=
-- finite type of vertices
(V : Type*) [HVfin: fintype V]
-- finite type of directed edges
(E : Type*) [HE : fintype E] (Esrc : E → V) (Etrg : E → V)


definition Dijkstra (G : finite_directed_graph)
-- I need an algorithm which spits out an element of V from a non-empty subset
[HVord : decidable_linear_order G.V]
-- I'd rather have a decidable linear ordered monoid for my weights
(W : Type*) [HW : decidable_linear_ordered_comm_group W] 
-- Weight of an edge
(Ewt : G.E → W)
-- start and finish vertex
(start : G.V) (finish : G.V)
: with_top W := sorry

variables {G : finite_directed_graph} [HVord : decidable_linear_order G.V]
{W : Type*} [HW : decidable_linear_ordered_comm_group W] (Ewt : G.E → W)
(start : G.V) (finish : G.V)

def is_path_from_start_to_finish : G.V → G.V → list G.E → Prop
| start finish [] := (start = finish)
| start finish (l :: ls) := G.Esrc l = start ∧ is_path_from_start_to_finish (G.Etrg l) (finish) ls

include HW
def path_length (Ewt : G.E → W) : list G.E → W
| [] := 0
| (l :: ls) := Ewt l + path_length ls

include HVord
-- do we want an existence result or should the algorithm return an actual minimal path?
theorem Dijkstra_attained : Dijkstra G W Ewt start finish ≠ none → ∃ Es : list G.E, is_path_from_start_to_finish start finish Es 
∧ Dijkstra G W Ewt start finish = some (path_length Ewt Es) := sorry

theorem Dijkstra_best : ∀ Es : list G.E,
(∀ w : W, w ∈ set.range Ewt → w ≥ 0) →
is_path_from_start_to_finish start finish Es → 
Dijkstra G W Ewt start finish ≤ some (path_length Ewt Es) := sorry

```

What happens next? I (or he) need(s) to implement the algorithm (the first sorry) and then prove that it has the properties I claim (the other sorries). Does this algorithm get written in Lean or meta Lean? It can be written in Lean, right? Then I can prove things about it. Have I got this straight? My sons are learning a bunch of algorithms and I'm trying to figure out what I can say about them in Lean.

#### [ Johan Commelin (Dec 08 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dijkstra%27s%20algorithm%20in%20Lean/near/151184026):
Right. I would implement it in Lean. My guess/hope is that it shouldn't be too hard.

#### [ Johan Commelin (Dec 08 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dijkstra%27s%20algorithm%20in%20Lean/near/151184072):
But I think one of the reasons that graph theory hasn't been fleshed out much is that it's hard to get the data structures right. You want to be both general enough and usable. But for a one-off push for Dijkstra, I guess this should work.

#### [ Kevin Buzzard (Dec 08 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dijkstra%27s%20algorithm%20in%20Lean/near/151184218):
This is exactly the sort of thing I don't understand, and which my children were telling me about. So now we have to think about issues involving exactly how to implement the data structures which show up in the implementation of the algorithm?

#### [ Johan Commelin (Dec 08 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dijkstra%27s%20algorithm%20in%20Lean/near/151184617):
Well, I'm certainly not an expert in graph theory. So I would probably just go for it, and see where I get stuck.

#### [ Johan Commelin (Dec 08 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dijkstra%27s%20algorithm%20in%20Lean/near/151184621):
But probably Mario, Sean or Simon can share a lot more wisdom here.

#### [ Johan Commelin (Dec 08 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dijkstra%27s%20algorithm%20in%20Lean/near/151184664):
Dijkstra is just a form of BFS, and Simon already implemented a BFS algorithm in meta Lean for the `tfae` tactic.

#### [ Kevin Buzzard (Dec 08 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dijkstra%27s%20algorithm%20in%20Lean/near/151184794):
Is implementing it in Lean and implementing it in meta Lean two completely different problems? I tried to put in enough hypotheses to guarantee that the algorithm terminates in finite type. My son and I were desperate to get some kinds of infinite graphs in but we pretty soon found some weird examples where the algorithm was poorly behaved, so we decided to stick to finite types for vertex and edge types.

#### [ Johan Commelin (Dec 08 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dijkstra%27s%20algorithm%20in%20Lean/near/151184909):
It probably is a different game whether you use `meta` or not.

#### [ Andrew Ashworth (Dec 08 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dijkstra%27s%20algorithm%20in%20Lean/near/151194004):
There's a bit on graphs in Coq here: https://softwarefoundations.cis.upenn.edu/vfa-current/Color.html, if this has caught your interest.


{% endraw %}
