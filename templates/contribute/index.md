# Contributing to mathlib

We're glad you are interested in contributing to mathlib. This project can use lots of help. On the other hand, it is also quite large: to usefully contribute, you need to follow a few principles.

This page explains what and why to contribute to mathlib, covering:
* what kind of contributions are welcome
* style-only contributions in particular
* responsible usage of AI: only certain AI contributions are accepted to mathlib


## What to contribute to mathlib

Small fixes (for example fixes in docstrings) and single-lemma additions in already-existing theories
are almost always welcome as contributions to mathlib. Longer PRs which extend existing theories are also almost
always welcome. 

But what about adding completely new theories to `mathlib`? Here, things can be more nuanced. The first question 
you will need to consider is whether the material you want to contribute is a good fit for `mathlib`. 
Whilst there is currently no formal description of exactly what mathlib's remit is, here are some questions which you 
can ask about your proposed contribution.

* Is the material typically taught or studied in a mathematics department? Would it naturally be part 
of an undergradute or graduate mathematics course, or research level mathematics study group? If not, then the material 
may not be in scope for `mathlib`.

* Is the topic of the material contained within the 
[mathematical interests of the `mathlib` maintainers](https://github.com/leanprover-community/mathlib4?tab=readme-ov-file#maintainers)? 
If not, then the maintainers might find your code hard to maintain as lean and `mathlib` evolve over time, 
which again may make it not a good fit for `mathlib`.

In particular the remit of mathlib should *not* be thought of as "all of mathematics and related areas". 
As the number of open PRs increases, the maintainers will sometimes need to make some hard decisions.

If you are not sure about whether your proposed topic is a good fit for mathlib, then please feel
free to open a discussion in the [`#mathlib` channel](https://leanprover.zulipchat.com/#narrow/channel/287929-mathlib4/) on the Lean Zulip.

An issue related to the fact that the expertise of the maintainers may not cover all of mathematics: 
you may want to think about *who* is going to review your potential PR. Contributors are encouraged 
to seek out reviewers for their PRs. A PR reviewer does *not* have to be a maintainer! This seems
to be a common misconception by the community. Reviews of PRs, especially from new reviewers, 
are essentially always welcome. 

Please also consider the possibility of creating a standalone repository, and adding `mathlib` as a dependency. 
There are many Lean repositories on github, indexed by [reservoir](https://reservoir.lean-lang.org). 
And [here](https://reservoir.lean-lang.org/@leanprover-community/mathlib/dependents) are those projects
which have `mathlib` has a dependency. The solution of having a new project which depends on
`mathlib` is a particularly good fit for projects in areas which do not align with the 
expertise of the mathlib maintainers. One example of such a repository is the [combinatorial game
theory repository](https://github.com/vihdzp/combinatorial-games). This solution is also a good fit
for projects which would like to move quickly; at the time of writing (mid 2026), mathlib has over 2600 open PRs
and it may take time for mathlib contributions to be reviewed and merged.

### Style changes

`mathlib` has a [style guide](style.html) and PRs fixing
style violations documented in this guide are welcome. Other stylistic PRs that don't have explicit
approval by the authors of the affected files may be closed. We invite authors to instead discuss the proposed
change on Zulip and, when significant consensus among reviewers is reached, to open a PR to the style guide.

## Use of AI

Using artificial intelligence tools to generate code is becoming more and more common. While this can be practical, their use also poses ethical, ecological, legal and social concerns. We recognise that there are strong differences in opinion on this topic. That said, while individual action alone will not address these concerns, we ask you to consider the effects of your AI use. When reviewing PRs, we are particularly concerned that the pedagogical value of the reviewers work is wasted if there is not a human contributor actively learning.

Using an LLM when writing comments on GitHub or Zulip is not allowed: use your own words.

Mathlib intentionally has very high standards (on generality, integration with the remaining library and maintainability, including code style). As of mid-2026, code written by an AI without the supervision of a Lean subject expert fails to meet that bar by a large margin. Members of the review team will summarily close without comment any low quality PR produced using LLMs, especially if the author has made little effort to directly engage in the community in a discussion about its merits before opening the PR.
If we notice that you open several PRs without putting in this learning effort or without adhering to our community ethical standards, we will suspend (or permanently ban) you both from opening new PRs and from the Zulip chat.

Getting code to mathlib's standards requires understanding and writing Lean code by hand. If you just want to help and not put in the learning effort, making a PR to mathlib is counterproductive: the effort required from the mathlib maintainers is larger than the benefit, because the time used to improve the quality of the code will not result in a better quality in future PRs.

If you use artificial intelligence (such as, by using GitHub's copilot mode, asking an LLM like [ChatGPT](https://chatgpt.com/) or using an agent like [Codex](https://openai.com/codex/), [Claude](https://claude.ai/), [Gemini](https://gemini.google.com/app), or even Lean-dedicated agents like [Aristotle](https://aristotle.harmonic.fun/)), you must explain this in the PR description. Explain which tool(s) you used and how you used it.
This provides useful context for reviewers: tools make different mistakes than humans, so knowing this makes it easier to spot common errors. If your PR contains a substantial amount of LLM-generated code, add the `LLM-generated` label by adding the comment `LLM-generated`.

It is essential that you understand all the content written by an AI. This includes understanding any design decisions made for the formalization and being able to justify each decision to reviewers without the use of an AI. If you don't, it is likely that the PR actually has negative value to the community.

## How to contribute

If you have read and understood the contribution guidelines above, you are ready to [learn how to contribute](/contribute/how-to-contribute.html).
