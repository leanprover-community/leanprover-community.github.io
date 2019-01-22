---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/14315431applytoadditiverecursively.html
---

## [PR reviews](index.html)
### [#431 apply `to_additive` recursively](14315431applytoadditiverecursively.html)

#### [Johan Commelin (Nov 30 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#431 apply `to_additive` recursively/near/148869284):
@**Simon Hudon** Somehow I missed this PR, but it looks awesome! Kudos :octopus: :tada: 
Too bad that Travis is saying that there is some error:
```
The command "leanpkg test" exited with 1.
20.65s$ lean --recursive --export=mathlib.txt
/home/travis/build/leanprover/mathlib/data/finsupp.lean:246:0: error: type mismatch at application
  @prod.equations._eqn_1 α β γ (@add_monoid.to_has_zero β _inst_3) _inst_4
term
  _inst_4
has type
  add_comm_monoid γ
but is expected to have type
  comm_monoid γ
<unknown>:1:1: error: type mismatch at application
  finsupp.prod.equations._eqn_1 α β γ (add_monoid.to_has_zero β _inst_3) _inst_4
term
  _inst_4
has type
  add_comm_monoid γ
but is expected to have type
  comm_monoid γ
```

#### [Simon Hudon (Nov 30 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#431 apply `to_additive` recursively/near/148869890):
Thanks :) I have put it on hold for now. There was a strange rabbit hole right in the model. I'll see if I can get back to it next time I need to procrastinate

