---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/55857Typeequality.html
---

## Stream: [new members](index.html)
### Topic: [Type equality](55857Typeequality.html)

---


{% raw %}
#### [ Keeley Hoek (Nov 11 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147478097):
<p>Is it possible to decide whether two types are equal?</p>

#### [ Kenny Lau (Nov 11 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147478161):
<p>no</p>

#### [ Keeley Hoek (Nov 11 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147478266):
<p>That makes me sad</p>

#### [ Kenny Lau (Nov 11 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147478309):
<p><code>local attribute [instance] classical.dec</code></p>

#### [ Keeley Hoek (Nov 11 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147478315):
<p>Cheers, but I wanted to use it in a program</p>

#### [ Keeley Hoek (Nov 11 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147478323):
<p>Instead I think I'm going to have to concoct some <code>user_notation</code> trickery to get the same syntax</p>

#### [ Kevin Buzzard (Nov 11 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147479490):
<p>I've heard it said here that even <code>nat = int</code> is undecidable</p>

#### [ Kenny Lau (Nov 11 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147479581):
<p>independent, even</p>

#### [ Abhimanyu Pallavi Sudhir (Nov 11 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147482478):
<blockquote>
<p>I've heard it said here that even <code>nat = int</code> is undecidable</p>
</blockquote>
<p>How exactly are we defining equality of types?</p>

#### [ Chris Hughes (Nov 11 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147482996):
<p>As defined in Lean. If you separately define two inductive types of the same size, their equality will be independent.</p>

#### [ Keeley Hoek (Nov 12 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147511856):
<p>I guess the lesson is to stay in <code>expr</code>-land if you're trying to do something programmatically like this (e.g. either its a <code>expr.const `bool []</code> or its not)</p>

#### [ Mario Carneiro (Nov 12 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147511939):
<p>Well, it depends on what you mean. That will not get <code>id bool = bool</code></p>

#### [ Keeley Hoek (Nov 12 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20equality/near/147513299):
<p>sure yep</p>


{% endraw %}
