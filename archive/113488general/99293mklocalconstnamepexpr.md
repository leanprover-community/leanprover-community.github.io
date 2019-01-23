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
Is there such a function that give a `pexpr` of local constant from the variable name? I can just call `expr.local_const`, but the constructor is kind of complex and not so much documentation, also I don't think it's the way to go.

#### [ Mario Carneiro (Jul 10 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382529):
There is `mk_const`, but one way or another you have to decide what to do about universe variables

#### [ Zesen Qian (Jul 10 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382778):
sorry, what's the difference between `const` and `local_const`? also, I'm trying to work without the tactic monad.

#### [ Mario Carneiro (Jul 10 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382857):
`const` is a global constant, which is declared by a `def` or `theorem` or `axiom`, like `nat` or `nat.succ` or `nat.succ_pos`

#### [ Mario Carneiro (Jul 10 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382906):
`local_const` is a "local constant" which is probably less than helpful but you would usually think of it as a variable. These are the variables that appear in the context during a tactic proof, left of the turnstile

#### [ Zesen Qian (Jul 10 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382910):
ahh I see.

#### [ Zesen Qian (Jul 10 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382918):
yeah, so I guess I'm trying to create a reference to local constant, from a string.

#### [ Mario Carneiro (Jul 10 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382921):
This is in contrast to `var` which is a de bruijn variable, which are variables which are currently bound in a binder in a term

#### [ Zesen Qian (Jul 10 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382928):
I can create `name` by `mk_simple_name`, but from that to `expr` I don't know.

#### [ Mario Carneiro (Jul 10 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382933):
You can't make a local constant from a string without the local context

#### [ Mario Carneiro (Jul 10 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382974):
that is what enables name resolution

#### [ Zesen Qian (Jul 10 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382982):
ok, so I need to be in a tactic.

#### [ Zesen Qian (Jul 10 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382985):
monad.

#### [ Mario Carneiro (Jul 10 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382987):
right

#### [ Mario Carneiro (Jul 10 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382988):
you want `get_local` I think

#### [ Zesen Qian (Jul 10 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129382994):
yes, I saw that.

#### [ Zesen Qian (Jul 10 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383000):
and I was wondering why it's implemented in VM, if it can be implemented natively.

#### [ Zesen Qian (Jul 10 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383002):
and now I know why.

#### [ Mario Carneiro (Jul 10 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383045):
You need that local context information to find out the unique name and type given the pp name

#### [ Mario Carneiro (Jul 10 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383047):
this is what the `tactic_state` provides

#### [ Zesen Qian (Jul 10 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383108):
ok. question: can I make a `elet`, getting a `local_const`, and pass it to the rest of the function, without access tactic state?

#### [ Mario Carneiro (Jul 10 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383124):
Possibly, what are the inputs? You need a variable, a type, a value and a body

#### [ Zesen Qian (Jul 10 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383186):
I want to construct a proof, which start with `let v = ...`, and I hope to get a `expr` refering to this `v`, and pass it to the rest of the proof generation.

#### [ Zesen Qian (Jul 10 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383188):
is that viable?

#### [ Mario Carneiro (Jul 10 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383422):
There are two ways you could proceed: you could construct the body containing `v` as a `local_const`, and then abstract it when you are finished, or you could construct it with `v` already abstracted, meaning you refer to it only as `var 0`

#### [ Mario Carneiro (Jul 10 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383496):
Lean is mostly geared toward constructing terms the first way, particularly if you intend for the expression to be constructed partially using tactics, with a metavariable in the middle etc. Most tactics only work on "closed terms", meaning that `var` is not allowed

#### [ Mario Carneiro (Jul 10 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383500):
But if you can construct the entire expr in one go with no intervention then the second approach is possible

#### [ Zesen Qian (Jul 10 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383627):
thanks, I'll try

#### [ Zesen Qian (Jul 10 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129383632):
very much appreciated.

#### [ Sebastian Ullrich (Jul 10 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129397269):
Please also note https://github.com/leanprover/lean/issues/1921#issuecomment-363028776. This distinction between "pure" and "tactic" local constants will likely vanish in Lean 4. As well as the name "local constant".

#### [ Simon Hudon (Jul 10 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mk_local_const%20%3A%20name%20-%3E%20pexpr%3F/near/129419037):
Do you mean that this kind of type won't leak through into the Lean code?


{% endraw %}
