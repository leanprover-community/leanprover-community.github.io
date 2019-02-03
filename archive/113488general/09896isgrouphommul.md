---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/09896isgrouphommul.html
---

## Stream: [general](index.html)
### Topic: [is_group_hom.mul](09896isgrouphommul.html)

---


{% raw %}
#### [ Kenny Lau (Apr 12 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970058):
<p>This is what <code>is_group_hom.mul</code> looked like on <a href="https://github.com/leanprover/mathlib/blob/22e671c5ed5fd1b891fb73aa10c9425d1c6cfd3d/algebra/group.lean#L493" target="_blank" title="https://github.com/leanprover/mathlib/blob/22e671c5ed5fd1b891fb73aa10c9425d1c6cfd3d/algebra/group.lean#L493">Apr 5</a>:</p>
<div class="codehilite"><pre><span></span>namespace is_group_hom
variables {f : α → β} (H : is_group_hom f)
include H

theorem mul : ∀ a b : α, f (a * b) = f a * f b := H
</pre></div>


<p>Now, the function variable became explicit, which broke some of my files. Are changes like this just going to happen randomly without any notice?</p>

#### [ Mario Carneiro (Apr 12 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970067):
<p>short answer: yes</p>

#### [ Kenny Lau (Apr 12 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970068):
<p>wonderful</p>

#### [ Mario Carneiro (Apr 12 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970106):
<p>mathlib is not stable any more than lean itself is, be prepared for this sort of thing</p>

#### [ Kenny Lau (Apr 12 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970111):
<p><a href="https://github.com/leanprover/mathlib/commit/fa86d349527766c2d0fc3173fcda302cdd5673f3#diff-52b9e281e7667f88f8203fb617843d93L488" target="_blank" title="https://github.com/leanprover/mathlib/commit/fa86d349527766c2d0fc3173fcda302cdd5673f3#diff-52b9e281e7667f88f8203fb617843d93L488">https://github.com/leanprover/mathlib/commit/fa86d349527766c2d0fc3173fcda302cdd5673f3#diff-52b9e281e7667f88f8203fb617843d93L488</a></p>

#### [ Mario Carneiro (Apr 12 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970112):
<p>It's not clear what kind of notice would be appropriate here in any case</p>

#### [ Kenny Lau (Apr 12 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970121):
<p>so if i werent clever enough to know exactly that my files broke because they made this variable explicit, I'm just going to have to sit down for an hour?</p>

#### [ Kenny Lau (Apr 12 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970164):
<p>also, this change broke <code>h.one</code> where <code>h</code> is the proof that some function is a group homomorphism</p>

#### [ Kenny Lau (Apr 12 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970165):
<p>now I have to do <code>is_group_hom.one _ h</code></p>

#### [ Mario Carneiro (Apr 12 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970166):
<p>If you update and your files break, double check what changed in the update, should give you a hint at what to do</p>

#### [ Mario Carneiro (Apr 12 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970167):
<p>or ask here, of coure</p>

#### [ Mario Carneiro (Apr 12 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970169):
<p>Now you do <code>is_group_hom.one f</code> I think</p>

#### [ Kenny Lau (Apr 12 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970224):
<p>right</p>

#### [ Kenny Lau (Apr 12 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970225):
<p>suddenly <code>is_group_hom</code> became a class</p>

#### [ Kenny Lau (Apr 12 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970226):
<p>and guess what</p>

#### [ Kenny Lau (Apr 12 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970227):
<p><a href="https://github.com/leanprover/mathlib/commit/fa86d349527766c2d0fc3173fcda302cdd5673f3#diff-52b9e281e7667f88f8203fb617843d93L515" target="_blank" title="https://github.com/leanprover/mathlib/commit/fa86d349527766c2d0fc3173fcda302cdd5673f3#diff-52b9e281e7667f88f8203fb617843d93L515">https://github.com/leanprover/mathlib/commit/fa86d349527766c2d0fc3173fcda302cdd5673f3#diff-52b9e281e7667f88f8203fb617843d93L515</a></p>

#### [ Mario Carneiro (Apr 12 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970228):
<p>Complain to <span class="user-mention" data-user-id="110524">@Scott Morrison</span> and <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>, I think this change is still in its probationary period</p>

#### [ Kenny Lau (Apr 12 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970232):
<p>before: <code>theorem inv (a : α) : (f a)⁻¹ = f a⁻¹</code><br>
after: <code>theorem inv (a : α) : f a⁻¹ = (f a)⁻¹</code></p>

#### [ Kenny Lau (Apr 12 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970233):
<p>really</p>

#### [ Mario Carneiro (Apr 12 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970240):
<p>I agree with that change, it makes more sense the other way around to match with <code>one</code> and <code>mul</code></p>

#### [ Mario Carneiro (Apr 12 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_group_hom.mul/near/124970294):
<p>but one thing I will not do is avoid small consistency changes because of a worry of breaking things. Once you start doing that, it will only become more crufty as time goes on</p>


{% endraw %}
