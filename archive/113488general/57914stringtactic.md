---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57914stringtactic.html
---

## Stream: [general](index.html)
### Topic: [string -> tactic?](57914stringtactic.html)

---

#### [Scott Morrison (Apr 06 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124695173):
Is there a good way to take a string (e.g. "simp, exact p") and return the tactic that executes it in interactive mode?

#### [Scott Morrison (Apr 06 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124695190):
(I have some "self-describing tactics", which can print as a message "what they did" in terms of built-in tactics, and I would like to automatic verify they are producing correct output.)

#### [Simon Hudon (Apr 06 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124696700):
I think the best I could do is something of type `string -> parser (tactic unit)`

#### [Simon Hudon (Apr 06 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124696748):
I don't know how to run that in a tactic though ... unless we're parsing the parameters to the tactic. Is that good enough?

#### [Scott Morrison (Apr 06 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124696754):
Unfortunately not. I'm deep inside a tactic by now.

#### [Simon Hudon (Apr 06 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124696801):
I think we'd need to plead with the developers to give us a `parser_state.mk` function

#### [Scott Morrison (Apr 06 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124697368):
If I want to parse a `rw_rule`, followed by a `nat` (e.g. so I can write `some_tactic foo 1`, or `some_tactic ← foo 3`), what am I meant to do?

#### [Scott Morrison (Apr 06 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124697374):
I've worked out that ` (q : parse (rw_rule_p (parser.pexpr 0)))` will parse a single `rw_rule`.

#### [Simon Hudon (Apr 06 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124697618):
Is the `rw_rule` fed by the user through a `begin ... end` block?

#### [Scott Morrison (Apr 06 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124697661):
yes

#### [Scott Morrison (Apr 06 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124697669):
I've decided that it's just as good to parse a list of rw_rules, and this seems to work out of the box.

#### [Scott Morrison (Apr 06 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124697683):
`(q : parse rw_rules) (n : ℕ) `

#### [Simon Hudon (Apr 06 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124697689):
Oh good then

#### [Simon Hudon (Apr 06 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124697744):
I don't know if `n : ℕ ` will work but if it doesn't, you can use `n : parse small_nat`

#### [Scott Morrison (Apr 06 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124697755):
Ah, I see, I just found `parse small_nat` in `conv`. Not bothering to use the parser for the nat seems okay.

#### [Simon Hudon (Apr 06 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124697809):
Alright then :)

#### [Mario Carneiro (Apr 06 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124698444):
@**Sebastian Ullrich** knows the answer to this one. My first thought was either a `parser A -> tactic A` lift, or the `with_input` function which is used to implement `format!`, but the first doesn't exist (you can make a parser from a tactic but not vice versa) and the second only works in the parser monad. There is no way to create a `parser_state` in lean that I can see (which corresponds to creating a C++ `parser` object), so I think parsing can only be done at parse time, not at tactic running time. (One *suuper* hacky way to maybe get this to work is to call `lean` using the `io` monad with a file that you create.)

#### [Sebastian Ullrich (Apr 06 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124707373):
What Mario said

