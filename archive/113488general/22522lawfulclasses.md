---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22522lawfulclasses.html
---

## Stream: [general](index.html)
### Topic: [lawful classes](22522lawfulclasses.html)

---


{% raw %}
#### [ Simon Hudon (Mar 23 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lawful%20classes/near/124114932):
<p>I'm having a look at the new <code>is_lawful_functor</code>. I just realized that it does not extend <code>functor</code>. That makes some signatures pretty verbose. Is there a plan to make shortcuts like <code>lawful_functor</code> that would combine both?</p>

#### [ Mario Carneiro (Mar 23 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lawful%20classes/near/124120584):
<p>I think it used to be bundled and was later unbundled. Of course you should ask Sebastian for the full story</p>

#### [ Sebastian Ullrich (Mar 23 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lawful%20classes/near/124123405):
<p>I'm not convinced of the useful of such shortcut classes. You cannot have class inference convert both to and from the class without risking cycles, which would make their usage quite clunky, I'd imagine.</p>


{% endraw %}
