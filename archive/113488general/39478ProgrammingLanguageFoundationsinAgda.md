---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39478ProgrammingLanguageFoundationsinAgda.html
---

## [general](index.html)
### [Programming Language Foundations in Agda](39478ProgrammingLanguageFoundationsinAgda.html)

#### [Sean Leather (Jul 20 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming Language Foundations in Agda/near/129979672):
I got an email that [Phil Wadler](http://homepages.inf.ed.ac.uk/wadler/) is giving a talk at Utrecht University. Here's the introduction:

```quote
The leading textbook for formal methods is Software Foundations (SF), written by Benjamin Pierce in collaboration with others, and based on Coq. After five years using SF in the classroom, I have come to the conclusion that Coq is not the best vehicle for this purpose, as too much of the course needs to focus on learning tactics for proof derivation, to the cost of learning programming language theory. Accordingly, I have written a new textbook, [Programming Language Foundations in Agda (PLFA)](https://plfa.github.io/). PLFA covers much of the same ground as SF, although it is not a slavish imitation.

What did I learn from writing PLFA? First, that it is possible. One might expect that without proof tactics that the proofs become too long, but in fact proofs in PLFA are about the same length as those in SF. Proofs in Coq require an interactive environment to be understood, while proofs in Agda can be read on the page. Second, that constructive proofs of preservation and progress give immediate rise to a prototype evaluator. This fact is obvious in retrospect but it is not exploited in SF (which instead provides a separate normalise tactic) nor can I find it in the literature. Third, that using raw terms with a separate typing relation is far less perspicuous than using inherently-typed terms. SF uses the former presentation, while PLFA presents both; the former uses about 1.6 as many lines of Agda code as the latter, roughly the golden ratio.
```

Considering the interest some people have shown in Software Foundations, I thought people might also find this interesting.

#### [Johan Commelin (Jul 20 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming Language Foundations in Agda/near/129980285):
Too bad I just moved away from Utrecht!

#### [Johannes Hölzl (Jul 20 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming Language Foundations in Agda/near/129985490):
@**Sean Leather**  Do you now where I can find more about his talk in Utrecht?

#### [Sean Leather (Jul 20 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming Language Foundations in Agda/near/129985545):
@**Johannes Hölzl** http://www.cs.uu.nl/docs/vakken/mccs/

#### [Johannes Hölzl (Jul 20 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming Language Foundations in Agda/near/129985553):
Argh, I'm still in Munich then...

