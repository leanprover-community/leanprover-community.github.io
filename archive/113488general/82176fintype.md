---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/82176fintype.html
---

## Stream: [general](index.html)
### Topic: [fintype](82176fintype.html)

---


{% raw %}
#### [ Chris Hughes (Feb 27 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123059884):
<p>What's the reason fintype isn't marked as Prop?</p>

#### [ Simon Hudon (Feb 27 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123060084):
<p>I think it can't be <code>Prop</code> because its accessor <code>elems</code> has a non-<code>Prop</code> type</p>

#### [ Chris Hughes (Feb 27 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123060323):
<p>Exists is a Prop, so presumably it's possible to define it in a way such that it is a Prop. I thought that since it's a subsingleton, it may as well be a Prop, but there's probably a good reason why not.</p>

#### [ Simon Hudon (Feb 27 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123060387):
<p>That's true. The difference is that <code>Exists</code> is defined using <code>inductive</code> not <code>structure</code>. Inductive doesn't come with accessors (in the case of <code>Exists</code>, the accessors could also be called the axiom of choice).</p>

#### [ Simon Hudon (Feb 27 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123060434):
<p>I think allowing <code>fintype</code> to be <code>Prop</code> would render every constructivist paranoid</p>

#### [ Simon Hudon (Feb 27 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123060441):
<p>(because merely declaring a structure could quietly add the axiom of choice into your development)</p>

#### [ Kevin Buzzard (Feb 27 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123060454):
<blockquote>
<p>I think allowing <code>fintype</code> to be <code>Prop</code> would render every constructivist paranoid</p>
</blockquote>
<p>I think they're already pretty paranoid if they're constructivists...</p>

#### [ Simon Hudon (Feb 27 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123060505):
<p>Should I say "paranoider"?</p>

#### [ Chris Hughes (Feb 27 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123060543):
<p>Mario mentioned that he wanted his proofs of <code>[fintype \a] \r [fintype \b] \r [fintype (\a \r \b)]</code> to be computable. Not sure why, especially since choice is everywhere in mathlib</p>

#### [ Simon Hudon (Feb 27 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123060674):
<p>Even when you assume the axiom of choice, constructive functions are great. They allow you to build programs without efforts</p>

#### [ Kevin Buzzard (Feb 27 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123061184):
<p>Try calculations with integers</p>

#### [ Kevin Buzzard (Feb 27 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123061227):
<p>What do you mean by "forever"?</p>

#### [ Simon Hudon (Feb 27 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123061255):
<p>wrong topic</p>

#### [ Kevin Buzzard (Feb 27 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123061261):
<p>damn topics</p>

#### [ Mario Carneiro (Feb 28 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123067712):
<p><code>fintype</code> and <code>finite</code> exist exactly so that you can decide whether or not you want to work in Prop</p>

#### [ Chris Hughes (Feb 28 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123067953):
<p>Didn't know about finite. I'll have to look at it.</p>


{% endraw %}
