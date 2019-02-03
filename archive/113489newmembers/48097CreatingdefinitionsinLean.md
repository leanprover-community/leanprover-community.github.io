---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/48097CreatingdefinitionsinLean.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Creating definitions in Lean](https://leanprover-community.github.io/archive/113489newmembers/48097CreatingdefinitionsinLean.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Creating%20definitions%20in%20Lean/near/135772739):
<p>I am trying to define an equivalence class in Lean, where I already have a binary relation, defined as a variable <code>variable (r : S → S → Prop)</code> -- how would I insert the requirement of <code>binary_relation</code> satisfying <code>equivalence</code> while defining an equivalence class?</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Creating%20definitions%20in%20Lean/near/135772781):
<p>I.e. surely just def <code>class (a : S) : set S := { x | r x a }</code> is not enough. Do I need some squiggly brackets here to impose the requirement <code>equivalence binary_relation</code>?</p>

#### [ Kenny Lau (Oct 14 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Creating%20definitions%20in%20Lean/near/135772896):
<p>the philosophy is that we create the definition as general as possible, and only insert the hypothesis in the proofs</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Creating%20definitions%20in%20Lean/near/135772964):
<p>Perhaps, but I just want to learn how definitions work. Can we make them specific in this way?</p>

#### [ Kenny Lau (Oct 14 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Creating%20definitions%20in%20Lean/near/135772975):
<p><code>def equivalence_class (h : is_equivalence r) (a : S) : set S := { x | r x a }</code></p>

#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Creating%20definitions%20in%20Lean/near/135773069):
<p>Right, and then when using the definition we'd need to provide a proof of is_equivalence r as a parameter, right?</p>

#### [ Kenny Lau (Oct 14 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Creating%20definitions%20in%20Lean/near/135773077):
<p>yes</p>

#### [ Bryan Gin-ge Chen (Oct 14 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Creating%20definitions%20in%20Lean/near/135773243):
<p>Note that if you use that definition, the variable <code>r</code> becomes something lean can very easily infer. Thus it's convenient to make it implicit (by writing <code>variable {r}</code> immediately beforehand), so that when you use <code>equivalence_class</code>, you won't need to write <code>equivalence_class r h a</code> but only <code>equivalence_class h a</code>.</p>

#### [ Kevin Buzzard (Oct 14 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Creating%20definitions%20in%20Lean/near/135777737):
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> just to note that <code>class</code> is already a keyword in Lean so you might want to stick to Kenny's suggestion of <code>equivalence_class</code> in any experiments you try.</p>


{% endraw %}
