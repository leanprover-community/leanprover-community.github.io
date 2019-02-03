---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39072orelsenontermination.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [orelse nontermination](https://leanprover-community.github.io/archive/113488general/39072orelsenontermination.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Seul Baek (Dec 26 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/orelse%20nontermination/near/152538868):
<div class="codehilite"><pre><span></span>meta def foo : tactic unit :=
triv &lt;|&gt; foo

example : true := by foo
</pre></div>


<p>In this example I expected <code>foo</code> to behave just like <code>triv</code> since the right branch would never be used, but it times out. Is there a way to avoid this?</p>

#### [ Mario Carneiro (Dec 26 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/orelse%20nontermination/near/152540454):
<p>you can eta expand <code>foo</code> on the right</p>

#### [ Gabriel Ebner (Dec 26 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/orelse%20nontermination/near/152542912):
<p>Another nice option is to use <code>local attribute [inline] interaction_monad_orelse</code>.</p>

#### [ Seul Baek (Dec 26 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/orelse%20nontermination/near/152550157):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>  I thought you meant changing the body of <code>foo</code> to <code>triv &lt;|&gt; (λ s, foo s)</code>, but this still times out. Am I doing something wrong here?</p>

#### [ Seul Baek (Dec 26 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/orelse%20nontermination/near/152550222):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span>  That works. Thanks!</p>

#### [ Mario Carneiro (Dec 26 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/orelse%20nontermination/near/152569135):
<p>actually I think you have to eta expand the definition of foo itself, i.e. <code>def foo | s := (triv &lt;|&gt; foo) s</code></p>


{% endraw %}
