---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40901ringrefactoring.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [ring refactoring](https://leanprover-community.github.io/archive/113488general/40901ringrefactoring.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Nov 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20refactoring/near/147427723):
<p>In the module refactoring, we turned <code>(N : set M) [is_submodule N]</code> into <code>(N: submodule R M)</code>, and we turned <code>(f : M -&gt; N) (hf : is_linear_map f)</code> into <code>(f : linear_map M N)</code>. And I found this very helpful.</p>

#### [ Kenny Lau (Nov 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20refactoring/near/147427733):
<p>Should we also change <code>(S : set R) [is_subring S]</code> into <code>(S : subring R)</code> and turn <code>(f : R -&gt; S) [is_ring_hom f]</code> into <code>(f : ring_hom R S)</code>?</p>

#### [ Kenny Lau (Nov 10 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20refactoring/near/147427736):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> <span class="user-mention" data-user-id="112680">@Johan Commelin</span> <span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Kenny Lau (Nov 10 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20refactoring/near/147427742):
<p>I think this would make defining / using algebras easier</p>

#### [ Kevin Buzzard (Nov 10 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20refactoring/near/147430470):
<p>What do I know about this sort of thing? I tend to just see what the state of stuff is, and then try to write mathematics, and if I get stuck I ask here and then people that understand these infrastructure issues say things like "oh OK looks like we need to entirely refactor modules". Make all the changes you like; I will finish my UG course in 5 weeks' time and then I will start proving a bunch of lemmas about complete rings which we need for <a href="https://github.com/kbuzzard/lean-perfectoid-spaces/issues/25" target="_blank" title="https://github.com/kbuzzard/lean-perfectoid-spaces/issues/25">https://github.com/kbuzzard/lean-perfectoid-spaces/issues/25</a> and will certainly be reporting back here with any problems I find. This is exactly the sort of behaviour I am seeing people like <span class="user-mention" data-user-id="112680">@Johan Commelin</span> and <span class="user-mention" data-user-id="110031">@Patrick Massot</span>  doing too, and which I guess will be a common theme amongst people who have PhDs in mathematics -- they find a project, they try it, and then they report back on the bits where they had to fight Lean and offer partial insights which are then typically instantly understood by the more CS-y people who are much better at seeing to the core of the underlying problem and how to solve it. This is one of the reasons that this is such an amazing community.</p>

#### [ Chris Hughes (Nov 10 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20refactoring/near/147431769):
<p>Same question for subgroups</p>

#### [ Johan Commelin (Nov 10 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20refactoring/near/147435630):
<p>Intuitively, I really like bundling things. But there were good reasons not to bundle <code>group</code> and <code>is_group_hom</code> etc... I don't claim to understand these reasons. But I feel like the way an ITP can handle bundling is an extremely important feature. For mathematicians bundling and unbundling is completely transparent. In Lean I have the feeling we need both versions, and we also need to state lots of lemmas twice. But again, I'm not an expert, and these are mostly feelings...</p>


{% endraw %}
