---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/66414groupactingongroup.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [group acting on group](https://leanprover-community.github.io/archive/116395maths/66414groupactingongroup.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Apr 09 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124835829):
<p>Do we have a name for a group acting on another group that is compatible with the group structure?</p>

#### [ jmc (Apr 09 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124836222):
<p>There is this thing called G-module</p>

#### [ jmc (Apr 09 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124836230):
<p>But then you act on abelian groups</p>

#### [ Kenny Lau (Apr 09 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124836231):
<p>but a group is not a module</p>

#### [ Kenny Lau (Apr 09 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124836232):
<p>right</p>

#### [ jmc (Apr 09 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124836300):
<p>Where does this show up?</p>

#### [ Kenny Lau (Apr 09 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124836303):
<p>in my brain</p>

#### [ Kenny Lau (Apr 09 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124836304):
<p>i'm just making this up</p>

#### [ Kenny Lau (Apr 09 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124836308):
<p>oh wait, this does show up in group theory</p>

#### [ Kenny Lau (Apr 09 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124836348):
<p>a group acts on a normal subgroup by conjugation</p>

#### [ jmc (Apr 09 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124836349):
<p>Ok, G-modules show up a lot in group cohomology</p>

#### [ jmc (Apr 09 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124836351):
<p>Aah, ok, sure</p>

#### [ Kenny Lau (Apr 09 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124836352):
<p>right, i'm learning group cohomology right now</p>

#### [ Kenny Lau (Apr 09 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124836355):
<p>and then an action of G on N is just a homomorphism G -&gt; Aut(N)</p>

#### [ jmc (Apr 09 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124836366):
<p>Sure, but if G acts on G', it is also just a homom G -&gt; Aut(G')</p>

#### [ jmc (Apr 09 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124836370):
<p>if the action is compatible with the group structure</p>

#### [ Kevin Buzzard (Apr 09 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124836498):
<p>If the group M you're acting on is abelian, then this is just called a G-module usually (G the group doing the acting)</p>

#### [ Kevin Buzzard (Apr 09 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124836539):
<p>If M is not abelian then this is sometimes called a "non-abelian G-module" and the theory very quickly gets technical</p>

#### [ Kevin Buzzard (Apr 09 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124836549):
<p>H^1 is no longer a group, but just a pointed set</p>

#### [ Kevin Buzzard (Apr 09 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124836557):
<p>and for higher cohomology groups one has to use fancy stuff like gerbes</p>

#### [ Kevin Buzzard (Apr 09 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/group%20acting%20on%20group/near/124836577):
<p>See Serre's book on Galois cohomology (some appendix) for a brief and clear introduction.</p>


{% endraw %}
