---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58005Cardinality.html
---

## Stream: [general](index.html)
### Topic: [Cardinality](58005Cardinality.html)

---


{% raw %}
#### [ Huyen Chau Nguyen (Jun 22 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cardinality/near/128461092):
Hey guys, I want to ask about the cardinality of sets. I'm totally newbie to Lean so the questions might be trivial and silly. Still, I need your help.

I would like to ask what is the function in mathlib that returns the number of elements of a set (of type set \N and not finset, but this set surely has a finite number of elements, it's not infinite set like R or N) and also which file i should have to import.

Thank you for your responses.

P.S.: I'm from Vn so please excuse-me for my English too.

#### [ Sean Leather (Jun 22 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cardinality/near/128461286):
I haven't used `set` myself, but I think an answer can be found in `data/set/finite.lean` in mathlib:

```lean
def finite (s : set α) : Prop := nonempty (fintype s)
```

Then, looking at `data/fintype.lean`, we see:

```lean
class fintype (α : Type*) :=
(elems : finset α)
(complete : ∀ x : α, x ∈ elems)
```

#### [ Huyen Chau Nguyen (Jun 22 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cardinality/near/128461714):
My prob is that i have to define my set as a set and not finset and then i need to count its size. 
Thank you very much for your answer.  I dont totally understand it yet but i would explore your hint with those files first and might ask you guys more later ^^.

#### [ Sean Leather (Jun 22 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cardinality/near/128461975):
You might want to think how you would define cardinality yourself. Consider the definition of `set`:

```lean
def set (α : Type u) := α → Prop
```

Without additional information, how do you count the number of elements? How do you even know a given `s : set α` is finite? For example, is `s : set ℕ` (whose type reduces to `ℕ → Prop`)  finite?

#### [ Chris Hughes (Jun 22 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cardinality/near/128462742):
`fintype.card` is the function you want.

#### [ Huyen Chau Nguyen (Jun 22 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cardinality/near/128463888):
@**Sean Leather**  : my set is constructed from an argument n of integer, if n tends to inifinity then the set's number of element could tend to be infinite, but for any given n, the number of elements of that set is guaranteed to be bounded ( Im wondering if i misunderstood the notion of being finite :-? ).  

@**Chris Hughes** okie thank you I'll check that out too .

#### [ Johannes Hölzl (Jun 22 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cardinality/near/128476931):
If you know your set is bound by a natural number `n` you can write `((finset.range n).filter (λi, i < 3)).card`, i.e. you first generate the finite set of all natural numbers up to `n` and then filter on a predicate (in this case`i < 3`). Then using `card` we compute the cardinality.

#### [ Johannes Hölzl (Jun 22 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cardinality/near/128476976):
If you have a proof that a `s : set α` is finite (i.e. `finite s`), then you can use `set.finite.to_finset` to get the `finset` of a `set`.


{% endraw %}
