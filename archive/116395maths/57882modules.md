---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/57882modules.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [modules](https://leanprover-community.github.io/archive/116395maths/57882modules.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Jan 30 2019 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modules/near/157169541):
<p>Can someone (<span class="user-mention" data-user-id="110049">@Mario Carneiro</span>, <span class="user-mention" data-user-id="110064">@Kenny Lau</span>) explain why exactly one needs <code>[add_comm_group M]</code> before being able to speak about <code>[module M]</code>?</p>

#### [ Mario Carneiro (Jan 30 2019 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modules/near/157169605):
<p>because it's not <code>[module M]</code> anymore, it's <code>[module R M]</code></p>

#### [ Kenny Lau (Jan 30 2019 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modules/near/157169610):
<blockquote>
<p>Because the parent coercion <code>module R M =&gt; add_comm_group M</code> was causing much of the module typeclass issues</p>
</blockquote>
<p><a href="#narrow/stream/113488-general/topic/module.20refactoring/near/146796108" title="#narrow/stream/113488-general/topic/module.20refactoring/near/146796108">Mario Carneiro, 13:48 (UTC), 2018 Nov 05</a></p>

#### [ Mario Carneiro (Jan 30 2019 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modules/near/157169631):
<p>after Kenny's refactoring, we definitely need <code>add_comm_group</code> separate</p>

#### [ Johan Commelin (Jan 30 2019 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modules/near/157169632):
<p>Ok</p>

#### [ Mario Carneiro (Jan 30 2019 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modules/near/157169646):
<p>in short, it's the part of the module structure that doesn't depend on <code>R</code></p>

#### [ Johan Commelin (Jan 30 2019 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modules/near/157169660):
<p>Sure</p>


{% endraw %}
