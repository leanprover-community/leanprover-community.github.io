---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31387typeclassinferences.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [typeclass inferences](https://leanprover-community.github.io/archive/113488general/31387typeclassinferences.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Apr 06 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695237):
<p><a href="https://github.com/kckennylau/Lean/blob/master/enough_injectives.lean#L72" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/enough_injectives.lean#L72">https://github.com/kckennylau/Lean/blob/master/enough_injectives.lean#L72</a><br>
In L72 of this, I needed to type <code>@linear_map R M (Hom_R_Q_div_Z R) _ _ (Hom_R_Q_div_Z.module R)</code>, i.e. I needed to manually provide the proof term <code>Hom_R_Q_div_Z.module R</code> that <code>Hom_R_Q_div_Z R</code> is a module, despite it being attributed as <code>instance</code>. Why is this the case?</p>

#### [ Scott Morrison (Apr 06 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695367):
<p>When faced with this problem, I often try to write an example beforehand, which hopefully should summon the instance via <code>by apply_instance</code>, and see if I can get that working.</p>

#### [ Scott Morrison (Apr 06 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695372):
<p>If I can't I start worrying about universe levels, which in my experience is a very common cause of typeclass inference failing.</p>

#### [ Scott Morrison (Apr 06 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695410):
<p>(I haven't actually looked at your example.)</p>

#### [ Scott Morrison (Apr 06 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695678):
<p>Having quickly looked at your example, I'd suggest trying to restrict to the case where the ring and the module live in the same universe.</p>

#### [ Kenny Lau (Apr 06 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695682):
<p>hmm, would that break generality?</p>

#### [ Kenny Lau (Apr 06 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695722):
<p><code>linear_map</code> accepts three universes</p>

#### [ Scott Morrison (Apr 06 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695723):
<p>Yeah... but that's maybe dangerous as well.</p>

#### [ Kenny Lau (Apr 06 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695729):
<p>so other universes don't have enough injectives lol</p>

#### [ Scott Morrison (Apr 06 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695730):
<p>at least check if this solves the inference problem</p>

#### [ Scott Morrison (Apr 06 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695735):
<p>If it doesn't then it's irrelevant. If it does, it's probably time to consult Mario for advice.</p>

#### [ Scott Morrison (Apr 06 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695736):
<p>(One can always <code>ulift</code> when you don't have enough universe polymorphism, and sometimes this is the better option.)</p>

#### [ Kenny Lau (Apr 06 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695738):
<p>it doesn't</p>

#### [ Scott Morrison (Apr 06 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695782):
<p>Oh well!</p>

#### [ Scott Morrison (Apr 06 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695794):
<p>try replacing the points where you explicitly provide the instances with <code>by apply_instance</code>, and then set <code>pp.all</code></p>

#### [ Kenny Lau (Apr 06 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695869):
<p>wait what</p>

#### [ Kenny Lau (Apr 06 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695981):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> once I removed L67-69, everything worked</p>

#### [ Kenny Lau (Apr 06 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124695982):
<p>except the fact that i of course need those lines</p>

#### [ Kenny Lau (Apr 06 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124697691):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> any idea? In <a href="https://github.com/kckennylau/Lean/blob/master/enough_injectives.lean#L72" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/enough_injectives.lean#L72">here</a>, I need <code> Hom_R_Q_div_Z.module R </code> to tell Lean that <code> Hom_R_Q_div_Z R </code> is a module, but once I remove L67-69, it is no longer necessary</p>

#### [ Kenny Lau (Apr 06 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124697743):
<p>I suspect it is because of the <code> injective.to_module </code></p>

#### [ Kenny Lau (Apr 06 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20inferences/near/124697747):
<p>interfering with the typeclass resolutions</p>


{% endraw %}
