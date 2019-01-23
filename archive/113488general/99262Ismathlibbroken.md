---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99262Ismathlibbroken.html
---

## Stream: [general](index.html)
### Topic: [Is mathlib broken?](99262Ismathlibbroken.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 05 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123292498):
I do not expect mathlib to be working 24/7 but I am wondering if it currently broken for everyone or just me. I have problems in prod.lean with `prod.mk.eta` on line 21 -- `invalid definition, a declaration named 'prod.mk.eta' has already been declared`

#### [ Kevin Buzzard (Mar 05 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123292504):
The reason I ask is that I have a file which reaches unreachable code

#### [ Kevin Buzzard (Mar 05 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123292507):
and it probably it would be better if this were the only error rather than all the sorrys which currently come with it

#### [ Kevin Buzzard (Mar 05 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123292510):
which may or may not be part of the problem

#### [ Kevin Buzzard (Mar 05 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123292573):
current version is here : https://gist.github.com/kbuzzard/50a650e6df7e712138456facb5a81f22 but I also have 4 sorrys from mathlib so I'll try to remove mathlib

#### [ Moses Schönfinkel (Mar 05 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123292628):
Broken for me as well.

#### [ Johannes Hölzl (Mar 05 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123305123):
It should work again.

#### [ Johannes Hölzl (Mar 05 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123305506):
@**Sebastian Ullrich** the generalization of the `do`-notation resulted in the following work around:  https://github.com/leanprover/mathlib/commit/ec9dac3ada9aa2107d5f3fceb3d28eee113278b8#diff-d49a7b7cdfea7e016e137ab7be5dc597L65
I don't know what exactly is happening, it claims to expect a `name`, but gets a `tactic _`. Is there a way to see what overloaded `bind` is used in the error message? `pp.full_names` etc didn't work for me.

#### [ Sebastian Ullrich (Mar 05 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123305570):
Urgh, pretty sure it's trying to do a recursive call

#### [ Sebastian Ullrich (Mar 05 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123305576):
Could you post the error?

#### [ Johannes Hölzl (Mar 05 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123305709):
Ah yes, looks like this (now I also added `pp.locals_full_name`:
```
type mismatch at application
  <bind.0._fresh.31.20685> (<c₁.0._fresh.31.20672> <r.0._fresh.31.20695> <e.0._fresh.31.20699>)
term
  <c₁.0._fresh.31.20672> <r.0._fresh.31.20695> <e.0._fresh.31.20699>
has type
  tactic (old_conv_result <α.0._fresh.31.20670>)
but is expected to have type
  name
```

#### [ Johannes Hölzl (Mar 05 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123305785):
Would it make sense to force the namespace of `bind`, like the `begin [m]` notation does? But it gets a ambiguous with `do [c] <- l, ...`

#### [ Sebastian Ullrich (Mar 05 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123305831):
The real issue is that the local for recursive calls ignores the `protected` specifier, imo

#### [ Johannes Hölzl (Mar 05 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123305899):
Or this!


{% endraw %}
