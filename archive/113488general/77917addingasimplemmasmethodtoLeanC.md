---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/77917addingasimplemmasmethodtoLeanC.html
---

## Stream: [general](index.html)
### Topic: [adding a simp_lemmas method to Lean C++](77917addingasimplemmasmethodtoLeanC.html)

---

#### [Edward Ayers (Dec 12 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20simp_lemmas%20method%20to%20Lean%20C%2B%2B/near/151537147):
Dear lean developers. I wanted to be able to use `simp_lemmas.rewrite` but instead of just returning the first rewrite that worked, I want all possible rewrites. I couldn't think of a nice way to do that in Lean code so I hacked the C++:

https://github.com/EdAyers/lean/commit/3e97849d03d8f720df9cbe45c2be7e0b1246e3f5

From doing some simple tests the code works.
If any of the Lean developers have a spare moment, I would really appreciate any comments on the above commit, I am especially worried that I have introduced a memory leak by using `buffer`.

