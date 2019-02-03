---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30454leftshiftonlists.html
---

## Stream: [general](index.html)
### Topic: [left shift on lists](30454leftshiftonlists.html)

---


{% raw %}
#### [ Chris Hughes (Jun 01 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/left%20shift%20on%20lists/near/127424565):
<p>Is there a function on lists that rotates the elements of the list i.e [1, 2, 3, 4] -&gt; [2, 3, 4, 1]?</p>

#### [ Simon Hudon (Jun 01 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/left%20shift%20on%20lists/near/127424622):
<p>For list <code>xs</code>, you can do it with <code>drop 1 xs ++ take 1 xs</code></p>

#### [ Kevin Buzzard (Jun 01 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/left%20shift%20on%20lists/near/127429588):
<p>you'd better remember what you dropped :-)</p>

#### [ Simon Hudon (Jun 01 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/left%20shift%20on%20lists/near/127430668):
<p>yep! That's what<code>take 1 xs</code> does</p>


{% endraw %}
