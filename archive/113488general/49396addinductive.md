---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49396addinductive.html
---

## Stream: [general](index.html)
### Topic: [add_inductive](49396addinductive.html)

---


{% raw %}
#### [ Jakob von Raumer (Mar 21 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010223):
<p>Why does</p>
<div class="codehilite"><pre><span></span>tactic.add_inductive `foo [] 0 `(Type) $
[(`mk, expr.pi `mk binder_info.default (expr.app (expr.const `list [level.zero]) (expr.const `foo [])) (expr.const `foo []))],
</pre></div>


<p>fail?</p>

#### [ Sebastian Ullrich (Mar 21 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010398):
<p>That's a nested inductive type, <code>add_inductive</code> only supports basic inductive types</p>

#### [ Jakob von Raumer (Mar 21 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010420):
<p>Too bad, and there's no API for the nested ones, right?</p>

#### [ Sebastian Ullrich (Mar 21 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010467):
<p>Right</p>

#### [ Jakob von Raumer (Mar 21 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010567):
<p>But are they internally reduced to basic inductive types?</p>

#### [ Kevin Buzzard (Mar 21 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010636):
<p>That's what is claimed in section 7.9 of TPIL : <a href="https://leanprover.github.io/theorem_proving_in_lean/inductive_types.html#mutual-and-nested-inductive-types" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/inductive_types.html#mutual-and-nested-inductive-types">https://leanprover.github.io/theorem_proving_in_lean/inductive_types.html#mutual-and-nested-inductive-types</a></p>

#### [ Sebastian Ullrich (Mar 21 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010637):
<p>Yes <a href="https://github.com/leanprover/lean/wiki/Compiling-nested-inductive-types" target="_blank" title="https://github.com/leanprover/lean/wiki/Compiling-nested-inductive-types">https://github.com/leanprover/lean/wiki/Compiling-nested-inductive-types</a></p>

#### [ Jakob von Raumer (Mar 21 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010694):
<p>Nice, thanks!</p>

#### [ Jakob von Raumer (Mar 21 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010830):
<p>This is done in C++ but outside the kernel, right?</p>

#### [ Mario Carneiro (Mar 21 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010832):
<p>yes</p>

#### [ Jakob von Raumer (Mar 21 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010842):
<p>Why isn't it done in Lean?</p>

#### [ Mario Carneiro (Mar 21 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124010976):
<p>It could be...</p>

#### [ Mario Carneiro (Mar 21 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124011034):
<p>I started working on that a while back, but then the ground started shaking and I decided to wait for the dust to settle</p>

#### [ Moses Schönfinkel (Mar 21 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_inductive/near/124011580):
<p>Very poetic!</p>


{% endraw %}
