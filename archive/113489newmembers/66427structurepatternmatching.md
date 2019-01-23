---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/66427structurepatternmatching.html
---

## Stream: [new members](index.html)
### Topic: [structure pattern matching](66427structurepatternmatching.html)

---


{% raw %}
#### [ Olli (Aug 27 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/structure%20pattern%20matching/near/132868918):
is it possible to pattern match structures? I saw on the PDF version of Theorem Proving in Lean (which I am guessing is now outdated based on other syntax differences) it is used, but the HTML version makes no mention of it, and none of my obvious guesses are working

#### [ Simon Hudon (Aug 27 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/structure%20pattern%20matching/near/132868967):
Yes you can. Normally, the constructor is named `my_struct.mk`

#### [ Olli (Aug 27 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/structure%20pattern%20matching/near/132869071):
ah yes that works, I was trying to use the `⦃ field, .. ⦄` syntax

#### [ Simon Hudon (Aug 27 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/structure%20pattern%20matching/near/132869129):
Those are not the right brackets. You need `⟨ field1,  ... ⟩`

#### [ Olli (Aug 27 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/structure%20pattern%20matching/near/132869410):
yeah the new book doesn't mention `⦃ ... ⦄`, I think the old one did. I was trying to use it in the same manner as the field updates work, where I don't have to know the order of the fields, and I thought maybe it is possible to use `{ field, .. }` with the two dots to match only a single field (while handling the other fields in other match arms

#### [ Simon Hudon (Aug 27 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/structure%20pattern%20matching/near/132869925):
I see, I bit like in Haskell. I'm not aware of such a syntax in Lean but @**Sebastian Ullrich** or @**Mario Carneiro** might correct me.

#### [ Sebastian Ullrich (Aug 27 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/structure%20pattern%20matching/near/132870018):
`{ field := pat, .. }` should absolutely work as a pattern

#### [ Simon Hudon (Aug 27 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/structure%20pattern%20matching/near/132870035):
Nice!

#### [ Olli (Aug 27 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/structure%20pattern%20matching/near/132870212):
thanks, I swear I tried that but I must have gotten something unrelated wrong :)


{% endraw %}
