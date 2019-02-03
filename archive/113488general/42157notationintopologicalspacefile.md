---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/42157notationintopologicalspacefile.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [notation in topological space file](https://leanprover-community.github.io/archive/113488general/42157notationintopologicalspacefile.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Mar 12 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20in%20topological%20space%20file/near/123620935):
<p>In <code>analysis/topology/topological_space.lean</code> we have s and t being used for more than one thing. Even in the definition of a topological space we have</p>
<div class="codehilite"><pre><span></span>(is_open_inter  : ∀s t, is_open s → is_open t → is_open (s ∩ t))
(is_open_sUnion : ∀s, (∀t∈s, is_open t) → is_open (⋃₀ s))
</pre></div>


<p>Here s is an open set on one line, and a set of open sets on the next. Is this sort of thing regarded as OK? We're doing Xena tonight (it's usually Thursdays but I'm busy this Thurs) and a 2nd year undergraduate who has just learnt what a topological space is, is trying to read this mathlib file and this sort of notational trickery is not helping. Would <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> be interested in a PR which only contained changes of the form</p>
<div class="codehilite"><pre><span></span>(is_open_inter  : ∀s₁ s₂, is_open s₁ → is_open s₂ → is_open (s₁ ∩ s₂))
(is_open_sUnion : ∀I, (∀s∈I, is_open s) → is_open (⋃₀ I))
</pre></div>


<p>? For me, that is more readable, but might not conform to some sort of mathlib style (I'm not sure about this). Later on in <code>is_open_sUnion</code> we have a <code>t</code> in the statement and a different <code>t</code> in the proof. Of course none of this is logically wrong, but it does strike me as a strange design decision in some sense. Maybe mathematicians don't label their theorems as well as computer scientists might want them to, but I think they label their objects in a more consistent manner than this (e.g it would be considered bad writing to have s representing more than one thing, particularly two different types in consecutive sentences -- although of course I've seen it happen!)</p>

#### [ Mario Carneiro (Mar 12 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20in%20topological%20space%20file/near/123621019):
<p>I often use capital letters for higher order sets. So <code>is_open_sUnion</code> would become <code>∀S, (∀s∈S, is_open s) → is_open (⋃₀ S)</code></p>

#### [ Mario Carneiro (Mar 12 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20in%20topological%20space%20file/near/123621034):
<p>I believe there is a similar convention of changing font registers in standard math</p>

#### [ Mario Carneiro (Mar 12 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20in%20topological%20space%20file/near/123621093):
<p>I usually reserve <code>I</code> or <code>ι</code> for the index set of a type/set family, say if I was discussing the indexed union instead of the set union</p>


{% endraw %}
