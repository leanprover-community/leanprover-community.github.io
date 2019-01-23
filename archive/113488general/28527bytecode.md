---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28527bytecode.html
---

## Stream: [general](index.html)
### Topic: [bytecode?](28527bytecode.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Oct 17 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bytecode%3F/near/135998701):
In a file with `noncomputable theory`, I get the trace message
```
failed to generate bytecode for 'locally_compact_of_compact'
code generation failed, VM does not have code for 'locally_compact_of_compact_nhds'
```
What does this mean, and should I worry?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 17 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bytecode%3F/near/135999111):
[I got that message before](https://leanprover.zulipchat.com/#narrow/stream/113489-new-members/subject/finsets.2C.20decidable_mem.2C.20and.20filter/near/133708032) when I had accidentally labeled a def as a theorem / lemma. Not sure if that applies in your case or not.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 17 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bytecode%3F/near/135999119):
Usually it means there is a lemma whose type is not a Prop, yes. In this case it is because I forgot to mark `locally_compact_space` as a Prop.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Oct 17 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bytecode%3F/near/135999225):
Indeed, it solves the problem. Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 17 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bytecode%3F/near/136000581):
I have a fix for mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 18 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bytecode%3F/near/136006536):
Thanks :+1:


{% endraw %}
