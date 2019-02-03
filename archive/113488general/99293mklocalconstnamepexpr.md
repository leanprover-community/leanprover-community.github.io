---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99293mklocalconstnamepexpr.html
---

## Stream: [general](index.html)
### Topic: [mk_local_const : name -> pexpr?](99293mklocalconstnamepexpr.html)

---


{% raw %}
#### [ Zesen Qian (Jul 09 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129374884):
<p>Is there such a function that give a <code>pexpr</code> of local constant from the variable name? I can just call <code>expr.local_const</code>, but the constructor is kind of complex and not so much documentation, also I don't think it's the way to go.</p>

#### [ Mario Carneiro (Jul 10 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382529):
<p>There is <code>mk_const</code>, but one way or another you have to decide what to do about universe variables</p>

#### [ Zesen Qian (Jul 10 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382778):
<p>sorry, what's the difference between <code>const</code> and <code>local_const</code>? also, I'm trying to work without the tactic monad.</p>

#### [ Mario Carneiro (Jul 10 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382857):
<p><code>const</code> is a global constant, which is declared by a <code>def</code> or <code>theorem</code> or <code>axiom</code>, like <code>nat</code> or <code>nat.succ</code> or <code>nat.succ_pos</code></p>

#### [ Mario Carneiro (Jul 10 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382906):
<p><code>local_const</code> is a "local constant" which is probably less than helpful but you would usually think of it as a variable. These are the variables that appear in the context during a tactic proof, left of the turnstile</p>

#### [ Zesen Qian (Jul 10 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382910):
<p>ahh I see.</p>

#### [ Zesen Qian (Jul 10 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382918):
<p>yeah, so I guess I'm trying to create a reference to local constant, from a string.</p>

#### [ Mario Carneiro (Jul 10 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382921):
<p>This is in contrast to <code>var</code> which is a de bruijn variable, which are variables which are currently bound in a binder in a term</p>

#### [ Zesen Qian (Jul 10 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382928):
<p>I can create <code>name</code> by <code>mk_simple_name</code>, but from that to <code>expr</code> I don't know.</p>

#### [ Mario Carneiro (Jul 10 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382933):
<p>You can't make a local constant from a string without the local context</p>

#### [ Mario Carneiro (Jul 10 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382974):
<p>that is what enables name resolution</p>

#### [ Zesen Qian (Jul 10 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382982):
<p>ok, so I need to be in a tactic.</p>

#### [ Zesen Qian (Jul 10 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382985):
<p>monad.</p>

#### [ Mario Carneiro (Jul 10 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382987):
<p>right</p>

#### [ Mario Carneiro (Jul 10 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382988):
<p>you want <code>get_local</code> I think</p>

#### [ Zesen Qian (Jul 10 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382994):
<p>yes, I saw that.</p>

#### [ Zesen Qian (Jul 10 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383000):
<p>and I was wondering why it's implemented in VM, if it can be implemented natively.</p>

#### [ Zesen Qian (Jul 10 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383002):
<p>and now I know why.</p>

#### [ Mario Carneiro (Jul 10 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383045):
<p>You need that local context information to find out the unique name and type given the pp name</p>

#### [ Mario Carneiro (Jul 10 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383047):
<p>this is what the <code>tactic_state</code> provides</p>

#### [ Zesen Qian (Jul 10 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383108):
<p>ok. question: can I make a <code>elet</code>, getting a <code>local_const</code>, and pass it to the rest of the function, without access tactic state?</p>

#### [ Mario Carneiro (Jul 10 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383124):
<p>Possibly, what are the inputs? You need a variable, a type, a value and a body</p>

#### [ Zesen Qian (Jul 10 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383186):
<p>I want to construct a proof, which start with <code>let v = ...</code>, and I hope to get a <code>expr</code> refering to this <code>v</code>, and pass it to the rest of the proof generation.</p>

#### [ Zesen Qian (Jul 10 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383188):
<p>is that viable?</p>

#### [ Mario Carneiro (Jul 10 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383422):
<p>There are two ways you could proceed: you could construct the body containing <code>v</code> as a <code>local_const</code>, and then abstract it when you are finished, or you could construct it with <code>v</code> already abstracted, meaning you refer to it only as <code>var 0</code></p>

#### [ Mario Carneiro (Jul 10 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383496):
<p>Lean is mostly geared toward constructing terms the first way, particularly if you intend for the expression to be constructed partially using tactics, with a metavariable in the middle etc. Most tactics only work on "closed terms", meaning that <code>var</code> is not allowed</p>

#### [ Mario Carneiro (Jul 10 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383500):
<p>But if you can construct the entire expr in one go with no intervention then the second approach is possible</p>

#### [ Zesen Qian (Jul 10 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383627):
<p>thanks, I'll try</p>

#### [ Zesen Qian (Jul 10 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383632):
<p>very much appreciated.</p>

#### [ Sebastian Ullrich (Jul 10 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129397269):
<p>Please also note <a href="https://github.com/leanprover/lean/issues/1921#issuecomment-363028776" target="_blank" title="https://github.com/leanprover/lean/issues/1921#issuecomment-363028776">https://github.com/leanprover/lean/issues/1921#issuecomment-363028776</a>. This distinction between "pure" and "tactic" local constants will likely vanish in Lean 4. As well as the name "local constant".</p>

#### [ Simon Hudon (Jul 10 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129419037):
<p>Do you mean that this kind of type won't leak through into the Lean code?</p>


{% endraw %}
