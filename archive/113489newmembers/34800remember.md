---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/34800remember.html
---

## Stream: [new members](index.html)
### Topic: [remember](34800remember.html)

---


{% raw %}
#### [ petercommand (Nov 01 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/remember/near/136927744):
<p>Is there something similar to coq's remember tactic in lean?</p>

#### [ petercommand (Nov 01 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/remember/near/136927833):
<p>I can't find it in lean's documents</p>

#### [ Chris Hughes (Nov 01 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/remember/near/136927846):
<p>What does coq's remember tactic do?</p>

#### [ petercommand (Nov 01 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/remember/near/136927899):
<p>It's basically a way to remember a term so that after pattern matching on a non-trivial term, no information is lost</p>

#### [ Chris Hughes (Nov 01 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/remember/near/136928040):
<p>Possibly <code>generalize</code>. But I don't fully understand the explanation in the coq docs</p>

#### [ Reid Barton (Nov 01 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/remember/near/136928066):
<p>I think <code>cases</code> and/or <code>induction</code> accepts a syntax which lets you name a hypothesis that the thing you pattern matched is equal to the result of the pattern match--is that the sort of thing you mean?</p>

#### [ petercommand (Nov 01 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/remember/near/136928149):
<p>yes</p>

#### [ petercommand (Nov 01 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/remember/near/136928230):
<p>that's what I want</p>

#### [ Reid Barton (Nov 01 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/remember/near/136928271):
<p>Yes, they both have it: the syntax is <code>cases (id :)? expr (with id*)?</code>--check the docstring for full details</p>

#### [ petercommand (Nov 01 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/remember/near/136928315):
<p>Thanks!</p>


{% endraw %}
