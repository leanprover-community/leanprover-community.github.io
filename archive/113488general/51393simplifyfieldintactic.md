---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51393simplifyfieldintactic.html
---

## Stream: [general](index.html)
### Topic: [simplify field in tactic](51393simplifyfieldintactic.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 10 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133639356):
Trivial question: I've got an instance `s` of some structure which has a `nat`-valued field `f`. In tactic mode I have as a hypothesis `v : nat := s.f`. What can I do to replace v with with its actual `nat` value? Sorry for the noise

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 10 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133639619):
what do you mean? If you are in tactic mode, you aren't proving anything so it doesn't matter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 10 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133639634):
or do you mean that `v : nat := s.f` is in the local context of the proof state?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 10 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133639640):
You can use `dsimp only [v] {zeta := tt}` to zeta expand `v`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 10 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133639833):
Hi Mario, I think that's what I mean. If I understand you right, are you saying something like this:
````
structure my_struct :=
(f : ℕ)

example : false := begin
  let s : my_struct := ⟨42⟩,
  let v := s.f,
  dsimp only [v] {zeta := tt},
  admit
end
````
should work? Weirdly, the `dsimp` line fails with
````
dsimplify tactic failed to simplify
state:
s : my_struct := {f := 42},
v : ℕ := s.f
⊢ false
````
:'(

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 10 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133639884):
Does `v` occur in the goal?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 10 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640190):
No, well secretly I'm trying to write a function which I can pass an `expr` and get back a "simplified" `expr`; in this case hopefully `s.f` will become `42`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 10 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640248):
Is there anything which does something like this? Maybe even just like `1 + 1` -> `2`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 10 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640374):
from my experience, not many tactics know about definitions (i.e. `:=`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 10 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640378):
which is quite annoying

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 10 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640385):
You can have a look at `tactic.dsimp_target` in `init/meta/simp_tactic.lean` to do that. But if your variable `v` does not occur in the expression, it will fail. You may have to enclose it in `try`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 10 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640455):
oh and you'll never change the definition of `v` using any tactic.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 10 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640463):
just literally no tactic can rewrite definition (things to the right of `:=`) in hypothesis, in my experience

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 10 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640468):
my workaround:
```lean
structure my_struct :=
(f : ℕ)

example : false := begin
  let s : my_struct := ⟨42⟩,
  let v := s.f,
  have hv : v = 42 := rfl,
  admit
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 10 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640484):
No, you can do some manipulation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 10 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640526):
in `tactic.basic`, in `mathlib`, you can use `local_def_value` to get the value of a definition. Then you can rewrite that experience, create a new definition and clear the old one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 10 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640746):
Thanks, yeah I was poking around in `simp_target` and `simplify` before and was wondering why it was failing. I note that
````
structure my_struct :=
(f : ℕ)

def s : my_struct := ⟨42⟩

#reduce s.f
````
(obviously) prints `42`. Is there any way to capture the result like this? I see that in the kernel reduce calls `normalize(...)` which returns an `expr`, is there away to get it to do that and capture the result myself?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 10 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640862):
Are you trying to evaluate the expression? If it's an arithmetic expression, you can use norm_num. Otherwise, whnf should take you part of the way there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 10 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640973):
Also, do you mean `normalize` from `ring.lean`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 10 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133641053):
Thanks I'll dig in and read about `whnf` for a bit. I don't think so, there's this file `src/library/normalize.cpp` which `normalize`s `expr`s you give it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 10 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133641194):
Actually, I think:
````
meta def dme : tactic unit := do
  let no_dflt := ff,
  let attr_names : list name := [],
  let hs : list simp_arg_type := [],
  (s, to_unfold) ← mk_simp_set no_dflt attr_names hs,
  e ← s.dsimplify to_unfold `({ my_struct . f := 42 }.f),
  trace e

#eval dme
````
might do what I want!

