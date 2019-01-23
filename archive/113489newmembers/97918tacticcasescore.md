---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/97918tacticcasescore.html
---

## Stream: [new members](index.html)
### Topic: [tactic.cases_core](97918tacticcasescore.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 24 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/tactic.cases_core/near/148270993):
What is the output of `tactic.cases_core`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 24 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/tactic.cases_core/near/148271269):
```lean
/-- Apply `cases_on` recursor, names for the new hypotheses are retrieved from `ns`.
   `h` must be a local constant. It returns for each new goal the name of the constructor, a list of new hypotheses, and a list of
   substitutions for hypotheses depending on `h`. The number of new goals may be smaller than the
   number of constructors. Some goals may be discarded when the indices to not match.
   See `induction` for information on the list of substitutions.

   The `cases` tactic is implemented using this one, and it relaxes the restriction of `h`. -/
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 24 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/tactic.cases_core/near/148286948):
I don't really understand `a list of substitutions for hypotheses` and the fact that sometimes I get duplicates in that particular list


{% endraw %}
