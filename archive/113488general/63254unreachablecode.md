---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63254unreachablecode.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [unreachable code](https://leanprover-community.github.io/archive/113488general/63254unreachablecode.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Dec 12 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unreachable%20code/near/151491054):
<p>sometimes <code>_</code> causes "unreachable code" error. it is quite clear that they won't fix it, so I'm not here to "feed the fed horse". Rather, I think I've found a temporary fix by just replacing <code>_</code> with <code>by skip</code> or any tactic mode thing at all</p>

#### [ Mario Carneiro (Dec 12 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unreachable%20code/near/151491085):
<p>That's a bit vague. Do you have an example?</p>

#### [ Kenny Lau (Dec 12 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unreachable%20code/near/151491158):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">group</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">×</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="o">(</span><span class="bp">_</span><span class="o">,</span> <span class="bp">_</span><span class="o">)</span> <span class="o">}</span>
</pre></div>

#### [ Mario Carneiro (Dec 12 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unreachable%20code/near/151491168):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> known bug?</p>

#### [ Sebastian Ullrich (Dec 12 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unreachable%20code/near/151509950):
<p>Probably not. Probably not worth fixing, either?</p>

#### [ Sebastian Ullrich (Dec 12 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unreachable%20code/near/151510002):
<p>To be honest, the Lean 4 error messages are so bad right now that I don't see any problem at all with this <span class="emoji emoji-1f606" title="laughing">:laughing:</span></p>

#### [ Simon Hudon (Dec 12 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unreachable%20code/near/151532124):
<p>Oh dear!</p>


{% endraw %}
