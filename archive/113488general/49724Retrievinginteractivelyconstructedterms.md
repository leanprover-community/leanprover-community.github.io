---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49724Retrievinginteractivelyconstructedterms.html
---

## Stream: [general](index.html)
### Topic: [Retrieving interactively constructed terms](49724Retrievinginteractivelyconstructedterms.html)

---


{% raw %}
#### [ Seul Baek (Jun 15 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Retrieving%20interactively%20constructed%20terms/near/128095723):
Suppose I'd like to construct a term of type `τ` interactively, so I use `e ← assert n '(τ)` and apply some further tactics to close off the goal. Now `e` is bound to a local constant, which is the expr of a term that has type `τ`.

Later in the proof, I need to call a tactic `foo : τ → tactic unit`. I think I should be able to use `e` in some way to extract a term `t : τ ` to be used as an argument for `foo`. But `t ← eval_expr τ e` doesn't work, because `eval_expr` only works on closed expressions. Is there something else I can do to retrieve the constructed term?

It seems that `define` retains more information than `assert`, but I'm not sure whether that helps.

#### [ Sebastian Ullrich (Jun 15 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Retrieving%20interactively%20constructed%20terms/near/128110543):
You should probably use `tactic.solve_aux` in favor of `assert`

#### [ Seul Baek (Jun 15 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Retrieving%20interactively%20constructed%20terms/near/128125818):
@**Sebastian Ullrich** I think this is closer to what I need, but it requires that you provide upfront a specific tactic which will solve the newly created goal. If there is a need to go interactive because it can't be predicted beforehand which tactic will do the job, I wonder if there are alternatives?

I'm currently experimenting with combinations of `assert` and `mk_meta_var`, but it seems that anything I do will only add a local constant to the context, instead of the actual term. Perhaps I'm trying to do something that you're not supposed to do :confused:

#### [ Sebastian Ullrich (Jun 15 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Retrieving%20interactively%20constructed%20terms/near/128125953):
> If there is a need to go interactive because it can't be predicted beforehand which tactic will do the job, I wonder if there are alternatives?

I'm not sure I understand, what does your use case look like that you don't know when the goal will be solved? Anyway, if you copy and adapt `solve_aux`'s implementation, you should be able to do something like that.


{% endraw %}
