---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48560environmentsandparameters.html
---

## Stream: [general](index.html)
### Topic: [environments and parameters](48560environmentsandparameters.html)

---


{% raw %}
#### [ Jakob von Raumer (Apr 20 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/environments%20and%20parameters/near/125449732):
<p>So I want to emulate inductive types defined in some section with parameters (or variables, I don't care). Can I do that by adding the paramters as local consts to some evironment <code>e</code> and then use <code>e.add_inductive</code>?</p>

#### [ Simon Hudon (Apr 20 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/environments%20and%20parameters/near/125449994):
<p>You would need to make it a proper constant I think. I assume you're writing a user command?</p>

#### [ Sebastian Ullrich (Apr 20 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/environments%20and%20parameters/near/125450242):
<p>There is no list of local consts in an environment, it's all in the parser (unexposed to Lean)</p>

#### [ Jakob von Raumer (Apr 20 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/environments%20and%20parameters/near/125450717):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Yes, I am... I'll just take a look at environments...</p>

#### [ Jakob von Raumer (Apr 20 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/environments%20and%20parameters/near/125450747):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> I don't necessarily need a list of them. So far I get around using parameters by just adding them as parameters to the inductive types I'm constructing and to every function I'm defining.</p>

#### [ Sebastian Ullrich (Apr 20 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/environments%20and%20parameters/near/125450823):
<p>Yes, that's what Lean itself does. It also creates aliases for the applied definitions in the parser, but you can't do that.</p>

#### [ Jakob von Raumer (Apr 20 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/environments%20and%20parameters/near/125450856):
<p>Do you have an idea how to solve that annoyance? Because it really makes my code very messy.</p>

#### [ Jakob von Raumer (Apr 20 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/environments%20and%20parameters/near/125451136):
<p>It sometimes seems a bit arbitrary what's exposed as meta constants and what isn't...</p>


{% endraw %}
