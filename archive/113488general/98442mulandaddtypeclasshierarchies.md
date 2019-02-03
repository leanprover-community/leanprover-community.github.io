---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98442mulandaddtypeclasshierarchies.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [mul and add type class hierarchies](https://leanprover-community.github.io/archive/113488general/98442mulandaddtypeclasshierarchies.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Oct 04 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mul%20and%20add%20type%20class%20hierarchies/near/135157838):
<p>I'm curious why we have two nearly duplicate type class hierarchies – multiplicative and additive – in Lean. It seems like it would be better to have the type classes be parameterized by the binary operator instead of inheriting the operator. I suppose there are technical/practical problems here which led to the current design.</p>

#### [ Johan Commelin (Oct 04 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mul%20and%20add%20type%20class%20hierarchies/near/135157910):
<p>Yes. You are right. I'll search for the discussion. 1 sec</p>

#### [ Johan Commelin (Oct 04 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mul%20and%20add%20type%20class%20hierarchies/near/135157995):
<p><a href="#narrow/stream/116395-maths/subject/additive.20group.20homs/near/127064577" title="#narrow/stream/116395-maths/subject/additive.20group.20homs/near/127064577">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/additive.20group.20homs/near/127064577</a></p>

#### [ Johan Commelin (Oct 04 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mul%20and%20add%20type%20class%20hierarchies/near/135157999):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span> <span class="emoji emoji-2b06" title="up">:up:</span></p>

#### [ Chris Hughes (Oct 04 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mul%20and%20add%20type%20class%20hierarchies/near/135158019):
<p>Also <a href="https://github.com/leanprover/lean/wiki/Refactoring-structures" target="_blank" title="https://github.com/leanprover/lean/wiki/Refactoring-structures">https://github.com/leanprover/lean/wiki/Refactoring-structures</a></p>

#### [ Sean Leather (Oct 04 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mul%20and%20add%20type%20class%20hierarchies/near/135158491):
<blockquote>
<p>Also <a href="https://github.com/leanprover/lean/wiki/Refactoring-structures" target="_blank" title="https://github.com/leanprover/lean/wiki/Refactoring-structures">https://github.com/leanprover/lean/wiki/Refactoring-structures</a></p>
</blockquote>
<p>I've tried to read that before and my eyes glazed over every time.</p>


{% endraw %}
