---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/27988reasoningaboutemptysetinlean.html
---

## Stream: [new members](index.html)
### Topic: [reasoning about empty set in lean](27988reasoningaboutemptysetinlean.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Marcus Klaas (Dec 02 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729616):
Hi y'all. Sorry to bother again. I'm having trouble working with the empty set. Specifically, I'd like to prove that a set is not empty whenever I can produce a concrete element of it:
```lean
example : { x | x = nat.succ nat.zero } ≠ ∅ := sorry
```
but so far, I haven't been successful. What can I do here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Dec 02 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729661):
`set.ne_empty_of_mem` will probably be helpful!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Dec 02 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729662):
You'll have to import `data.set.basic` from mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Marcus Klaas (Dec 02 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729664):
Thanks! I will try it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 02 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729714):
no import needed :)
```lean
example : { x | x = nat.succ nat.zero } ≠ ∅ :=
λ H, (congr_fun H 1).mp rfl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 02 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729721):
...says the person with over 1 year's Lean experience ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 02 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729723):
```lean
import data.set.basic

example : { x | x = nat.succ nat.zero } ≠ ∅ :=
begin
  rw set.ne_empty_iff_exists_mem,
  use 1,
  exact rfl, -- refl doesn't work!
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 02 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729730):
`refl` is really bad at set membership.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 02 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729783):
`example (a : ℕ) : a ∈ {x : ℕ | x = a} := by refl -- fails `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 02 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729785):
I wonder whether we could fool it into working somehow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Marcus Klaas (Dec 02 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729786):
Hmmm I don't seem to have the mathlib tho.. ~~can I install it using elan?~~ I have found a way to do it ^^

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 02 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729787):
basically by adding what Kevin just wrote as a `relfexivity` lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 02 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729838):
@**Marcus Klaas** mathlib is great. It's not just for mathematicians. It has a bunch of useful tactics in, and a whole host of useful data structures. If you work with Lean projects (as I do -- all my files, even scratch files, are within a Lean project) then you can just make mathlib a dependency for that project and then `leanpkg upgrade` will download mathlib.


{% endraw %}
