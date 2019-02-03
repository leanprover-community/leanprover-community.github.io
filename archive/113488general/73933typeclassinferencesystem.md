---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/73933typeclassinferencesystem.html
---

## Stream: [general](index.html)
### Topic: [type class inference system](73933typeclassinferencesystem.html)

---


{% raw %}
#### [ Johan Commelin (Jun 05 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20system/near/127610700):
<p>Two (classes of) related questions:<br>
1) Is there some reference for the type class inference algorithm that Lean uses? Is it ad hoc, or does it follow some established algorithm? Is it documented in some paper?<br>
2) How will Lean 4 impact the type class system? Is it planned to remain the same, or will it go through a major revision?</p>

#### [ Gabriel Ebner (Jun 05 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20system/near/127610978):
<blockquote>
<p>Is there some reference for the type class inference algorithm that Lean uses? Is it ad hoc, or does it follow some established algorithm? Is it documented in some paper?</p>
</blockquote>
<p>I think the canonical answer is that it's a λProlog interpreter, which synthesizes instances by essentially backchaining.  We typically cite [1].</p>
<p>[1] D. Miller and G. Nadathur. Programming with Higher-Order Logic. Cambridge, 2012.</p>
<p>(Not entirely sure if this is helpful.)</p>

#### [ Johan Commelin (Jun 05 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20system/near/127611007):
<p>Yes, I think it answers 1).</p>

#### [ Gabriel Ebner (Jun 05 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20system/near/127611008):
<blockquote>
<p>How will Lean 4 impact the type class system? Is it planned to remain the same, or will it go through a major revision?</p>
</blockquote>
<p>I don't expect any significant changes, but Sebastian can probably speak more authoritatively on this topic.</p>

#### [ Sebastian Ullrich (Jun 05 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20system/near/127611083):
<p>There are no changes to the type class system planned right now</p>

#### [ Johan Commelin (Jun 05 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20system/near/127611098):
<p>Maybe I have a newbie question 3): Are coercions and type class inferences somehow two avatars of some underlying common principle?</p>

#### [ Johan Commelin (Jun 05 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20system/near/127611427):
<p>/me just realises that the Miller--Nadathur reference is a 300 page book...</p>

#### [ Johan Commelin (Jun 05 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20system/near/127611656):
<p>Once Lean 4 is ready, someone should write "The Leanbook". Alas, I hear that Don Knuth's todo list is non-empty ;-)</p>

#### [ Johan Commelin (Jun 05 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20system/near/127611690):
<p>I would love to understand the inner workings of Lean. But I'm not a very proficient source reader. In that regard I found the TeXbook very enlightening.</p>


{% endraw %}
