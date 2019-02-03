---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85476updatingthenthelementofalist.html
---

## Stream: [general](index.html)
### Topic: [updating the nth element of a list](85476updatingthenthelementofalist.html)

---


{% raw %}
#### [ Scott Morrison (Nov 30 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148832961):
<p>Do we have something equivalent to</p>
<div class="codehilite"><pre><span></span>def patch_nth {α : Type} (f : α → α) : ℕ → list α → list α
| _ []           := []
| 0 (h :: t)     := f h :: t
| (n+1) (h :: t) := h :: patch_nth n t
</pre></div>


<p>in mathlib?</p>

#### [ Scott Morrison (Nov 30 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148832974):
<p>I've found a few times that it's really painful for update the nth element, because you have to deal with <code>nth</code> returning an option, even when you know it's there.</p>

#### [ Scott Morrison (Nov 30 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148833022):
<p>A slight variation that is even more useful:</p>
<div class="codehilite"><pre><span></span>def opatch_nth {α : Type} (f : α → option α) : ℕ → list α → list α
| _ []           := []
| 0 (h :: t)     := match f h with
                    | (some e) := e :: t
                    | none     := t
                    end
| (n+1) (h :: t) := h :: opatch_nth n t
</pre></div>

#### [ Kenny Lau (Nov 30 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148833045):
<blockquote>
<p>I've found a few times that it's really painful for update the nth element, because you have to deal with <code>nth</code> returning an option, even when you know it's there.</p>
</blockquote>
<p>... did you say it's painful to <strong><em>update</em></strong> the <strong><em>nth</em></strong> element?</p>

#### [ Scott Morrison (Nov 30 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148833052):
<p>Of course there is <code>update_nth</code></p>

#### [ Kenny Lau (Nov 30 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148833091):
<p>also what is it with your <code>meta</code>?</p>

#### [ Scott Morrison (Nov 30 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148833099):
<p>Oh, yeah, those <code>meta</code>s are completely unnecessary :-) Just habit, as I was in a whole file where most things were meta.</p>

#### [ Scott Morrison (Nov 30 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148833150):
<p>But  to use <code>update_nth</code>, you need to use <code>nth</code> earlier to get out the existing element to modify.</p>

#### [ Scott Morrison (Nov 30 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148833154):
<p>The typical example here is that I have a list of some structure, and I want to modify a single field of the nth element.</p>

#### [ Scott Morrison (Nov 30 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148833205):
<p>In this case the function <code>f</code> can be <code>λ s, { f := x, .. s}</code>.</p>

#### [ Mario Carneiro (Nov 30 2018 at 04:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148837711):
<p>did you say you want to <strong><em>modify</em></strong> the <strong><em>nth</em></strong> element?</p>

#### [ Reid Barton (Nov 30 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148838352):
<p>Did somebody say "lens"?</p>

#### [ Scott Morrison (Nov 30 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/148844167):
<p>Thanks. And yes, let's have more lens. :-)</p>

#### [ Keeley Hoek (Dec 01 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20the%20nth%20element%20of%20a%20list/near/150230501):
<p>Wait, isn't the syntax to declare functions in lean <code>meta def ....</code>? ;)</p>


{% endraw %}
