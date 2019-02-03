---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/76731holecommands.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [hole commands](https://leanprover-community.github.io/archive/113488general/76731holecommands.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Aug 30 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hole%20commands/near/133076337):
<p>One thing that might be of general interest that got some attention in Orsay: Lean has support for holes, but it isn't up to par to some other theorem provers. Nevertheless, try typing</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">tidy</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">your_favourite_triviality</span> <span class="o">:=</span> <span class="o">{</span><span class="bp">!</span> <span class="bp">_</span> <span class="bp">!</span><span class="o">}</span>
</pre></div>


<p>and hit Ctrl-. (control-dot) while you are on the hole (<code>{! _ !}</code>). You will get a list of hole commands that are available. Three of them are somewhat silly, and one was added in Orsay: the tidy hole command. If your favourite triviality is actually Lean-trivial, then this hole-command will write a complete tactic proof for you.</p>

#### [ Johan Commelin (Aug 30 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hole%20commands/near/133076506):
<p>It might be a good idea to think about other useful hole commands.</p>

#### [ Kenny Lau (Aug 30 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hole%20commands/near/133076735):
<p>could you show us an example?</p>

#### [ Kenny Lau (Aug 30 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hole%20commands/near/133076760):
<p>oh nvm I didn't import <code>tactic.tidy</code></p>


{% endraw %}
