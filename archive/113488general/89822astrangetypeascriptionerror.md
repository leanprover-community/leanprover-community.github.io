---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89822astrangetypeascriptionerror.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [a strange type ascription error](https://leanprover-community.github.io/archive/113488general/89822astrangetypeascriptionerror.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Jun 22 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20strange%20type%20ascription%20error/near/128464038):
<p>I am getting an error of the form </p>
<div class="codehilite"><pre><span></span>invalid type ascription, term has type
  @eq X a b
but is expected to have type
  @eq Y a b
</pre></div>


<p>where here <code>X</code> and (especially) <code>Y</code> are quite large expressions.</p>

#### [ Scott Morrison (Jun 22 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20strange%20type%20ascription%20error/near/128464065):
<p>But <code>a</code> and <code>b</code> are just names of hypotheses. Any advice on dealing with this sort of thing?</p>

#### [ Scott Morrison (Jun 22 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20strange%20type%20ascription%20error/near/128464118):
<p>It seems like merely from the fact that the two terms separately typecheck I should have a proof that <code>X = Y</code>...</p>

#### [ Scott Morrison (Jun 22 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20strange%20type%20ascription%20error/near/128464203):
<p>Curiously here, even though the goal prints as <code>a = b</code>, writing <code>show a = b</code> results in <code>show tactic failed</code>.</p>

#### [ Scott Morrison (Jun 22 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20strange%20type%20ascription%20error/near/128465208):
<p>... immediate problem solved, (remove a few unnecessary <code>@[reducible]</code> attributes), although I don't really understand what was going wrong.</p>

#### [ Reid Barton (Jun 22 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20strange%20type%20ascription%20error/near/128474905):
<p>I have seen a tactic produce a goal which was not well-typed before, and it was very confusing. Sounds like the same sort of issue?</p>

#### [ Reid Barton (Jun 22 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20strange%20type%20ascription%20error/near/128475258):
<p>In my case the offending tactic was <code>induction using quotient.ind</code>; from your resolution, it sounds unrelated</p>

#### [ Reid Barton (Jun 22 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20strange%20type%20ascription%20error/near/128475337):
<p>I guess the main point is that "the goal in tactic mode is well-typed" is not a 100% iron-clad guarantee, although it surely indicates a bug somewhere if it is violated.</p>


{% endraw %}
