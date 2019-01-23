---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99350rwfeature.html
---

## Stream: [general](index.html)
### Topic: [rw feature](99350rwfeature.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 23 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20feature/near/132628472):
```lean
example (a b c : ℕ) (H : a = b) (H2 : (a = b) → (a = c)) : c = b :=
begin
  rw (H2 H) at H, -- does nothing
  exact H -- fails
end

example (a b c : ℕ) (H : a = b) (H2 : (a = b) → (a = c)) : c = b :=
begin
  have H' := H,
  rw (H2 H') at H, -- works fine
  exact H
end

example (a b c : ℕ) (H : a = b) (H2 : (a = b) → (a = c)) : c = b :=
begin
  have H' := H,
  rw (H2 H) at H', -- works fine
  exact H'
end
```

Is this a bug, or is it not a good idea to let rewrites affect hypotheses which are used to construct the term being rewritten? (or both?)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 23 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20feature/near/132628548):
```lean
example (a b : ℕ) (H : a = b) : false :=
begin
  rw H at H, -- I would expect H to become b = b...
  sorry
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 23 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20feature/near/132628571):
[PS this is not frivolous -- I just attempted to do a rewrite on a term which I had used to explicitly fill in something which type class inference couldn't infer, and it silently failed]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 23 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20feature/near/132639780):
I think `rw` does not rewrite the assumptions themselves because if you have:

```
h0 : a = b,
h1 : a = c
...
```

`rw h0 at *` would transform `h0` into `b = b` and then `rw` would not be able to rewrite `h1`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 23 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20feature/near/132639895):
I suspect the developers consciously decided to not let `rw` rewrite assumptions using themselves as a rule. If the assumptions eventually get reshuffled, the design of `rw` makes the re-execution of the same proof less surprising. Does `simp` or `dsimp` help in your situation?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 23 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20feature/near/132639964):
I did exactly what I suggested in my original post -- I just introduced a new hypothesis which was by definition the old one :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 23 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20feature/near/132640206):
Ah ok, I thought it might fit in a more complex situation. So it would rank as "annoying", I assume

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 23 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20feature/near/132640291):
Yeah, I'm helping undergraduates to write code and today has been quite an annoying day for some reason, I've had to introduce several workarounds for things.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 23 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20feature/near/132640475):
I think that happens a lot in any programming language: with time, you start instinctively avoiding the pain points and then the newcomers run right into them


{% endraw %}
