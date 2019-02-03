---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/62843leanstacksproject.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [lean-stacks-project](https://leanprover-community.github.io/archive/116395maths/62843leanstacksproject.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Bryan Gin-ge Chen (Aug 30 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lean-stacks-project/near/133081672):
<p>I noticed some updates to lean-stacks-project today. In case this helps, I wanted to share a fork I played with a few weeks ago where I also tried to update it to work with more recent mathlib commits. See the testing branch <a href="https://github.com/bryangingechen/lean-stacks-project/tree/testing" target="_blank" title="https://github.com/bryangingechen/lean-stacks-project/tree/testing">here</a> which builds successfullly with mathlib at commit <code>b267edc</code> (from July 16-17).  Here's the relevant page of the mathlib <a href="https://github.com/leanprover/mathlib/commits/master?after=86c955eb424b70b493aa5b9594a91a0a14ba462d+139" target="_blank" title="https://github.com/leanprover/mathlib/commits/master?after=86c955eb424b70b493aa5b9594a91a0a14ba462d+139">commit history</a> for reference.</p>
<p>I tried bumping the mathlib commit to <code>a0dd286</code> (since that seems to be the next one in the history with a green Travis CI checkmark) but I couldn't figure out how to fix the resulting issues in tensor_product. The same issues seem to be present in the master branch of lean-stacks-project as well. So I think whatever's going on there was caused by <a href="https://github.com/leanprover/mathlib/compare/b267edc...a0dd286" target="_blank" title="https://github.com/leanprover/mathlib/compare/b267edc...a0dd286">one of these changes between those two commits</a>. </p>
<p>Anyways, I'm curious to understand better what happened there and what the eventual fix will be.</p>

#### [ Kevin Buzzard (Aug 30 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lean-stacks-project/near/133082064):
<p>Hi. I'm the maintainer. I tried today to get the project to compile with the latest mathlib, I'm something like one sorry away. I'm trying to put together a paper about this stuff. I seem to have two options: try publishing in a CS place, which would involve tidying the code up, or in a maths place, which might well not. I might try a maths journal, I am far keener to tell mathematicians that schemes can be formalised than to tell computer scientists that something they don't care about can be formalised, because they know that already.</p>


{% endraw %}
