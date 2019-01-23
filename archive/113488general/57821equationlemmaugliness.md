---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57821equationlemmaugliness.html
---

## Stream: [general](index.html)
### Topic: [equation lemma ugliness](57821equationlemmaugliness.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemma%20ugliness/near/127977206):
```lean
def poly := list ℤ

def poly.add : poly → poly → poly 
| [] g := g
| f [] := f 
| (a :: f') (b :: g') := (a + b) :: poly.add f' g' 

-- example (p : poly) : poly.add [] p = p := rfl -- fails

#print prefix poly.add 

/-
...
poly.add.equations._eqn_1 : poly.add list.nil list.nil = list.nil
poly.add.equations._eqn_2 : ∀ (hd : ℤ) (tl : list ℤ), poly.add list.nil (hd :: tl) = hd :: tl
...

-- it did unnecessary cases on g.
-/

example (p : poly) : poly.add [] p = p := by cases p;refl 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemma%20ugliness/near/127977299):
Is this just "one of those things" -- is my proof of poly.add using cases something which I should be OK with, or should I now start tweaking things to try and make the example rfl? I am about to make it a simp lemma -- is that "good enough"? As you can see, I can prove the result, I am just worried about whether my proof is somehow bad style. It's my fancy recursive definition which is to blame of course, but the definition is recursive (I'm representing a polynomial as a list of its coefficients starting with the constant term)


{% endraw %}
