---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/63247429finitesubgroupsofintegraldomain.html
---

## Stream: [PR reviews](index.html)
### Topic: [#429 finite subgroups of integral domain](63247429finitesubgroupsofintegraldomain.html)

---


{% raw %}
#### [ Chris Hughes (Oct 20 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23429%20finite%20subgroups%20of%20integral%20domain/near/136142678):
<p>Can anyone think of a good name for a file containing the proof that any finite subgroup of the units of an integral domain is cyclic? It imports <code>data.polynomial</code> and <code>group_theory.order_of_element</code>, so a file name that encompasses all thing depending on that would be great. I hate thinking of names.</p>

#### [ Johan Commelin (Oct 20 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23429%20finite%20subgroups%20of%20integral%20domain/near/136152756):
<p><code>ring_theory/basic.lean</code></p>

#### [ Chris Hughes (Oct 20 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23429%20finite%20subgroups%20of%20integral%20domain/near/136152859):
<p>The bulk of it is actually just a proof about groups, that satisfy the condition that the number of nth roots of one is le n, so I'll put that in group theory.</p>

#### [ Kevin Buzzard (Oct 20 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23429%20finite%20subgroups%20of%20integral%20domain/near/136161594):
<blockquote>
<p><code>ring_theory/basic.lean</code></p>
</blockquote>
<p><code>commutative_algebra/basic.lean</code></p>

#### [ Kevin Buzzard (Oct 20 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23429%20finite%20subgroups%20of%20integral%20domain/near/136161606):
<p>This is specifically a result about commutative rings, and given the make-up of people here there is going to be a lot more commutative ring theory being generated before a big push on stuff like group rings for non-abelian groups etc. It's time we were proud to be commutative.</p>

#### [ Kenny Lau (Oct 20 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23429%20finite%20subgroups%20of%20integral%20domain/near/136161647):
<p>right, but first the modules need to be refactored</p>

#### [ Kevin Buzzard (Oct 20 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23429%20finite%20subgroups%20of%20integral%20domain/near/136161690):
<p>I don't think this stops us making the directory :-)</p>


{% endraw %}
