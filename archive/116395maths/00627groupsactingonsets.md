---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/00627groupsactingonsets.html
---

## Stream: [maths](index.html)
### Topic: [groups acting on sets](00627groupsactingonsets.html)

---


{% raw %}
#### [ Kevin Buzzard (Jan 31 2019 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/groups%20acting%20on%20sets/near/157280679):
<p>Did we ever get groups acting on sets? [or even monoids acting on sets?]. The reason I ask is that I just tried to define groups acting on abelian groups and I realised I can't use <code>*</code> because the action is <code>G -&gt; M -&gt; M</code>. Has a decision been made about notation for groups acting on anything other than themselves?</p>

#### [ Johan Commelin (Jan 31 2019 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/groups%20acting%20on%20sets/near/157280852):
<p>Yes, these are in mathlib, and you want to use <code>smul</code>, I think.</p>

#### [ Johan Commelin (Jan 31 2019 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/groups%20acting%20on%20sets/near/157280856):
<p><code>\bullet</code></p>

#### [ Kevin Buzzard (Jan 31 2019 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/groups%20acting%20on%20sets/near/157281437):
<p>Apparently it's <code>\bu</code> now. And I have to import <code>algebra.module</code> to get the notation :-) It should be some far more primitive thing. Is the fact that the notation is defined in algebra.module evidence that we don't have groups acting on sets yet?</p>

#### [ Kenny Lau (Jan 31 2019 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/groups%20acting%20on%20sets/near/157283231):
<blockquote>
<p>Did we ever get groups acting on sets? [or even monoids acting on sets?]. The reason I ask is that I just tried to define groups acting on abelian groups and I realised I can't use <code>*</code> because the action is <code>G -&gt; M -&gt; M</code>. Has a decision been made about notation for groups acting on anything other than themselves?</p>
</blockquote>
<p><code>is_group_action</code></p>

#### [ Kenny Lau (Jan 31 2019 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/groups%20acting%20on%20sets/near/157283295):
<p>also when I did it myself I used <code>\ci</code></p>


{% endraw %}
