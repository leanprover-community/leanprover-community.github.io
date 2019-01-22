---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/81623pfilter.html
---

## [maths](index.html)
### [pfilter](81623pfilter.html)

#### [Johannes Hölzl (Nov 08 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pfilter/near/147287895):
@Mario
```quote
I'm going to sleep now, but I've got something for you guys to puzzle over tomorrow: [leanprover-community/pfilter](https://github.com/leanprover/mathlib/compare/master...leanprover-community:pfilter) is beginning work on generalizing filters to preorders. @**Johannes Hölzl** if you have any ideas for how all your lifting and monad stuff works when separating the two levels of sets out, I'd like to hear it. I have not figured out what the new version of `join` has to do with the old one (which has a different type - `filter (filter A)` becomes `pfilter (set (pfilter A))` which is not obviously related to `pfilter (pfilter A)`, which is something new).
```
I would be surprised if the monads on `filter` and `pfilter` are related. For me the monad of filter is not what is expected (one gets the wrong products), but `applicative` is a nice structure. I don't know about `pfilter`...

