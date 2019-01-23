---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/70558TypeDrivenProgramSynthesis.html
---

## Stream: [general](index.html)
### Topic: ["Type-Driven Program Synthesis"](70558TypeDrivenProgramSynthesis.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 22 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136245038):
I just watched and enjoyed this talk: ["Type-Driven Program Synthesis" by Nadia Polikarpova](https://www.youtube.com/watch?v=HnOix9TFy1A). To a newbie like me, this kind of automation seems quite cool and mindblowing. Also, the way she described synthesizing programs as a search problem made me think of @**Scott Morrison|110087** 's `rewrite_search` demo.

How much of this is useful / within reach for theorem proving? Presumably there are some restrictions (e.g. decidability?) on what this can be used on, but I haven't looked too hard at [the paper](https://cseweb.ucsd.edu/~npolikarpova/publications/pldi16.pdf). How different are "refinement types" from subtypes in lean? Here's [the "Synquid" repository](https://bitbucket.org/nadiapolikarpova/synquid) and [live demo](http://comcom.csail.mit.edu/comcom/#Synquid). I guess the work is from 2016, so maybe it's already been discussed pre-zulip?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 22 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136246221):
I don't see why we couldn't do it in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 22 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136246651):
Refinement types are another way to express the same idea as subtypes, but the execution is different

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 22 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136246700):
in particular, a refinement type is a subtype, in the sense that if `x : {v : T | stuff}` then `x : T`. Lean does not have subtyping in this sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 22 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136246710):
Do we have coercion between a subtype and its carrier type?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 22 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136246722):
In lean, this means you have to insert functions going back and forth, but since the VM erases proofs these functions disappear from generated code

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 22 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136246728):
yes, there is a coe instance for subtype

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 22 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136246787):
If you have `xs : list { v : T | stuff }`, I don't suppose `xs.map subtype.val` will reduce to `id`, will it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 22 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136246832):
unfortunately no. This is one place where I want compiler support for marking functions as "VM identity functions"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 22 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136246834):
same for `list.attach`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 22 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136246843):
Haskell has the same trouble


{% endraw %}
