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
<p>is it possible to pattern match structures? I saw on the PDF version of Theorem Proving in Lean (which I am guessing is now outdated based on other syntax differences) it is used, but the HTML version makes no mention of it, and none of my obvious guesses are working</p>

#### [ Simon Hudon (Aug 27 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/structure%20pattern%20matching/near/132868967):
<p>Yes you can. Normally, the constructor is named <code>my_struct.mk</code></p>

#### [ Olli (Aug 27 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/structure%20pattern%20matching/near/132869071):
<p>ah yes that works, I was trying to use the <code>⦃ field, .. ⦄</code> syntax</p>

#### [ Simon Hudon (Aug 27 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/structure%20pattern%20matching/near/132869129):
<p>Those are not the right brackets. You need <code>⟨ field1,  ... ⟩</code></p>

#### [ Olli (Aug 27 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/structure%20pattern%20matching/near/132869410):
<p>yeah the new book doesn't mention <code>⦃ ... ⦄</code>, I think the old one did. I was trying to use it in the same manner as the field updates work, where I don't have to know the order of the fields, and I thought maybe it is possible to use <code>{ field, .. }</code> with the two dots to match only a single field (while handling the other fields in other match arms</p>

#### [ Simon Hudon (Aug 27 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/structure%20pattern%20matching/near/132869925):
<p>I see, I bit like in Haskell. I'm not aware of such a syntax in Lean but <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> or <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> might correct me.</p>

#### [ Sebastian Ullrich (Aug 27 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/structure%20pattern%20matching/near/132870018):
<p><code>{ field := pat, .. }</code> should absolutely work as a pattern</p>

#### [ Simon Hudon (Aug 27 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/structure%20pattern%20matching/near/132870035):
<p>Nice!</p>

#### [ Olli (Aug 27 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/structure%20pattern%20matching/near/132870212):
<p>thanks, I swear I tried that but I must have gotten something unrelated wrong :)</p>


{% endraw %}
