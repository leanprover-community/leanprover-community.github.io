---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/74151Problem210TheoremProvinginLean.html
---

## Stream: [new members](index.html)
### Topic: [Problem 2.10 "Theorem Proving in Lean"](74151Problem210TheoremProvinginLean.html)

---


{% raw %}
#### [ Christopher Sumnicht (Jan 19 2019 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Problem%202.10%20%22Theorem%20Proving%20in%20Lean%22/near/156414053):
Hello, I hope this is the correct place to ask this. I was looking at the [Theorem Proving in Lean book exercises in Chap 2](https://leanprover.github.io/theorem_proving_in_lean/dependent_type_theory.html#exercises) which asks to both add two vectors together and reverse a vector. I have the following questions: 

1. Why does it want to make a constant instead of a definition?
 2. Normally, I would pattern match in Haskell on the head and tail of a list to solve both problems, but I don't know how to do this without recursion (as recursion isn't mentioned until later in chap 8). Any hints as to how to do this without recursion would be appreciated.

#### [ Mario Carneiro (Jan 19 2019 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Problem%202.10%20%22Theorem%20Proving%20in%20Lean%22/near/156414478):
Normally we would define that as a function, but this is early in the book and the question is only about getting the type right. For the exercise you aren't even trying to make the definition itself, just the type of the hypothetical definition


{% endraw %}
