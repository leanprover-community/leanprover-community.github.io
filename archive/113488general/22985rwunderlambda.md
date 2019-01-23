---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22985rwunderlambda.html
---

## Stream: [general](index.html)
### Topic: [rw under lambda](22985rwunderlambda.html)

---


{% raw %}
#### [ Reid Barton (May 04 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20lambda/near/126107890):
`rw` refuses to perform rewrites inside a lambda, as far as I can tell. Is there a convenient way to do so?
For example, frequently my goal is of the form `∃ x, P x ∧ Q x` and I would like to rewrite it to `∃ x, P x ∧ Q' x` (where I know `Q x ↔ Q' x`).

#### [ Simon Hudon (May 04 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20lambda/near/126107975):
use `simp` instead of `rw` if you want to rewrite under lambda. If you don't want `simp` to use default `simp` rules, you can do `simp only [my_rule]`

#### [ Reid Barton (May 04 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20lambda/near/126108133):
Oops, I tried `simp only`, but I mixed up `.symm` and `.mpr` so it didn't appear to work. Thanks!

#### [ Patrick Massot (May 04 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20lambda/near/126109753):
See also https://github.com/leanprover/mathlib/blob/master/docs/extras/conv.md

#### [ Reid Barton (May 04 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20lambda/near/126111096):
I couldn't work out how to do this with `conv`:
```lean
example (h : ∃ a b, a + b = 0) : ∃ a b, b + a = 0 :=
begin
  conv begin
    -- use rw add_comm somehow
  end, 
  exact h
end
```

#### [ Reid Barton (May 04 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20lambda/near/126111175):
I tried `congr, funext, congr` but I got an error that I didn't understand on the second `congr`

#### [ Simon Hudon (May 04 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20lambda/near/126111358):
try:

```
example : (∃ a b, a + b = 0) ↔ ∃ a b, b + a = 0 :=
by conv in (_ + _) begin
  rw add_comm,
end
```

#### [ Reid Barton (May 04 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20lambda/near/126111674):
ah, interesting

#### [ Simon Hudon (May 04 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20lambda/near/126112393):
This would also work, btw:

```lean
example (h : (∃ a b, a + b = 0)) : ∃ a b, b + a = 0 :=
begin
  conv in (_ + _) 
  { rw add_comm },
  exact h
end
```

#### [ Patrick Massot (May 04 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20lambda/near/126115523):
`conv in ( _ = _)` would also work, but I would be interested in seeing a solution without pattern matching. It seems we lack some navigation tactic (like `to_lhs`/`to_rhs`,  `congr`). @**Gabriel Ebner**  @**Mario Carneiro** any idea?


{% endraw %}
