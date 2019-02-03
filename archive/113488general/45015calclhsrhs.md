---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/45015calclhsrhs.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [calc lhs/rhs](https://leanprover-community.github.io/archive/113488general/45015calclhsrhs.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Nov 20 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20lhs/rhs/near/148043376):
<p>When writing <code>calc</code> blocks, it would be very convenient if we could have some special symbol that refers to the lhs/rhs of the original goal. Because currently I try to copy paste stuff from the goal, and then Lean starts moaning that it can't figure out the type etc...<br>
I guess it might be tricky to use literal <code>lhs</code>, because people might want to use that as variable name. But maybe something can be done?</p>

#### [ Bryan Gin-ge Chen (Nov 20 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20lhs/rhs/near/148043505):
<p>I've been using <code>_</code> to start / end <code>calc</code> blocks with the lhs / rhs.</p>

#### [ Johan Commelin (Nov 20 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20lhs/rhs/near/148043761):
<p>Hmm, I fear that it will then start moaning about <code>X</code> in <code>_ = X</code>... But I'll try.</p>

#### [ Johan Commelin (Nov 20 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20lhs/rhs/near/148044194):
<p>Meeh, it's not really working...</p>

#### [ Bryan Gin-ge Chen (Nov 20 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20lhs/rhs/near/148044384):
<p>MWE?</p>

#### [ Johan Commelin (Nov 20 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20lhs/rhs/near/148044572):
<p>Well... I don't really know how to produce a MWE. I'm not going to trim down my <code>sheaf</code> branch... I guess I could just enable <code>pp.all</code> and copy-paste the lhs into the calc-block. It's just more convenient if there would be a shorthand for it.</p>

#### [ Johan Commelin (Nov 20 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20lhs/rhs/near/148044697):
<p>Fail... <code>pp.all</code> is trimming my output. It is too long <span class="emoji emoji-1f923" title="rolling on the floor laughing">:rolling_on_the_floor_laughing:</span></p>


{% endraw %}
