---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/61969universepolymorphicversionofempty.html
---

## Stream: [general](index.html)
### Topic: [universe polymorphic version of empty?](61969universepolymorphicversionofempty.html)

---


{% raw %}
#### [ Zesen Qian (Jul 05 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20polymorphic%20version%20of%20empty%3F/near/129158168):
<p>RT? The current empty is at Type 0</p>

#### [ Zesen Qian (Jul 05 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20polymorphic%20version%20of%20empty%3F/near/129158198):
<p>just don't want to reinvent the wheel.<br>
Also wondering why empty is not universe polymorphic</p>

#### [ Chris Hughes (Jul 05 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20polymorphic%20version%20of%20empty%3F/near/129158379):
<p>What situation would it be an advantage for empty to be polymorphic?</p>

#### [ Zesen Qian (Jul 05 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20polymorphic%20version%20of%20empty%3F/near/129158418):
<p>oh wait, is lean's universe cumulative?</p>

#### [ Simon Hudon (Jul 05 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20polymorphic%20version%20of%20empty%3F/near/129158419):
<p>If you need <code>empty</code> in universe <code>u</code>, you can use <code>ulift.up.{u} empty</code>. <code>ulift</code> is a tool to fit objects of different universes together.</p>

#### [ Simon Hudon (Jul 05 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20polymorphic%20version%20of%20empty%3F/near/129158425):
<p>No, it's not</p>

#### [ Zesen Qian (Jul 05 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20polymorphic%20version%20of%20empty%3F/near/129158429):
<p>very nice, thank you.</p>

#### [ Simon Hudon (Jul 05 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20polymorphic%20version%20of%20empty%3F/near/129158469):
<p>we use <code>ulift</code> when we would need cumulativeness</p>

#### [ Simon Hudon (Jul 05 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20polymorphic%20version%20of%20empty%3F/near/129158575):
<p>In general, you should use universe variables as rarely as possible and use <code>ulift</code>. When you build definitions like <code>list</code>, you have no choice to make it universe polymorphic so that it can be used in various universes: <code>list : Type u -&gt; Type u</code>. That's because if <code>list : Type -&gt; Type</code>, there's no way of using lift on <code>a : Type 3</code> in order to have a <code>list a</code></p>

#### [ Zesen Qian (Jul 05 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20polymorphic%20version%20of%20empty%3F/near/129159229):
<p>ahh, can't understand the error<br>
ulift Type <br>
not match <br>
Type u</p>

#### [ Simon Hudon (Jul 05 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20polymorphic%20version%20of%20empty%3F/near/129159286):
<p>Can you show the code?</p>

#### [ Zesen Qian (Jul 05 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20polymorphic%20version%20of%20empty%3F/near/129159295):
<div class="codehilite"><pre><span></span>def clause : list (Type u) → Type u
| ([]) := ulift.up.{u+1} empty
| (x :: xs) := sum x $ clause xs
</pre></div>

#### [ Simon Hudon (Jul 05 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20polymorphic%20version%20of%20empty%3F/near/129159557):
<p>Use <code>ulift empty</code> instead of <code>ulift.up empty</code>. <code>ulift.up</code> is something you use on a term. On a type, you use simply <code>ulift</code></p>


{% endraw %}
