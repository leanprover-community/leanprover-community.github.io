---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/29871Leandoesntfindinstanceofsomethingthatsrightthere.html
---

## [new members](index.html)
### [Lean doesn't find instance of something that's right there](29871Leandoesntfindinstanceofsomethingthatsrightthere.html)

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135863594):
Weird problem -- I have my goal, which is `(x ⋆ y) → (y ⋆ z) → (x ⋆ z)` (for some operation `⋆`) and I have a hypothesis `Hxy : x = y`. But when I try `rw Hxy,` Lean tells me:

```lean
rewrite tactic failed, did not find instance of the pattern in the target expression
  x
```

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135863628):
But... it's right there.

#### [Kevin Buzzard (Oct 16 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135863810):
Post a MWE

#### [Kevin Buzzard (Oct 16 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135863871):
Sometimes it's because you have two variables called `x`, sometimes it's because something needs to be done by type class inference and type class inference fails but the error mesage is that the rewrite failed, there are all sorts of reasons.

#### [Kevin Buzzard (Oct 16 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135864347):
Another reason it fails is that you can't rewrite under a binder. Does `simp only [Hxy]` work? As you can see, it's difficult to diagnose without a MWE.

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135864405):
Ok, I got the problem (it was the "two variables called `x`" thing) -- I had defined a symbol `S` for `fin 2` and mid-way through the proof had done `rw S at z y x`, which caused two sets of variables `x y z` to be defined.

#### [Kevin Buzzard (Oct 16 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135864450):
`rw` is a fickle beast.

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135864454):
(although I'm not sure why that happened -- usually when you do `rw something at something`, it just changes the statement, not create new ones.)

#### [Kevin Buzzard (Oct 16 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135864455):
It takes a while to get to know its foibles

#### [Kevin Buzzard (Oct 16 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135864545):
```lean
example (n x y : ℕ) (h : n > 0 → x = y) : x + 1 = y + 2 :=
begin
  rw h,
  -- one goal became 2 -- we now need a proof of n > 0
  sorry,sorry
end
```

#### [Abhimanyu Pallavi Sudhir (Oct 16 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135864852):
Yeah, I've encountered that before, but that actually makes sense (and is useful!). Treating rewrites differently based on whether they're done on a natural number or a proof is just weird.

