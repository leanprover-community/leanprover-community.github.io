---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/72652Isthereawaytocomplicatethingswithsimp.html
---

## Stream: [new members](index.html)
### Topic: [Is there a way to complicate things with simp?](72652Isthereawaytocomplicatethingswithsimp.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Nov 25 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Is%20there%20a%20way%20to%20complicate%20things%20with%20simp%3F/near/148315124):
<p>I.e. is there a way to write <code>simp [←lemma, lemma, lemma]</code>?</p>

#### [ Kenny Lau (Nov 25 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Is%20there%20a%20way%20to%20complicate%20things%20with%20simp%3F/near/148315168):
<p><code>simp [(lemma).symm, lemma, lemma]</code></p>

#### [ Abhimanyu Pallavi Sudhir (Nov 25 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Is%20there%20a%20way%20to%20complicate%20things%20with%20simp%3F/near/148315223):
<p>That doesn't always work, though. For instance, I'm trying to do <code>simp [(polynomial.sum_C_mul_X_eq p).symm, finsupp.sum, polynomial.derivative_sum],</code> -- rewrites work, but <code>simp</code> doesn't.</p>

#### [ Kevin Buzzard (Nov 25 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Is%20there%20a%20way%20to%20complicate%20things%20with%20simp%3F/near/148318355):
<p><code>simp</code> might be taking a wrong turn before it tries the rewrites you want. Switch logging on if you want to investigate further -- see the <code>simp</code> docs in mathlib for an explanation of how to do this.</p>


{% endraw %}
