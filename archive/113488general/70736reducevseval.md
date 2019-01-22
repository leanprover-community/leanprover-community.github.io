---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/70736reducevseval.html
---

## [general](index.html)
### [#reduce vs #eval](70736reducevseval.html)

#### [Simon Hudon (Feb 27 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce vs #eval/near/123060876):
Does it ever happen that #reduce runs forever while #eval terminates immediately?

#### [Kevin Buzzard (Feb 27 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce vs #eval/near/123061271):
Try 1000*1000

#### [Simon Hudon (Feb 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce vs #eval/near/123061346):
it times out

#### [Kevin Buzzard (Feb 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce vs #eval/near/123061357):
Does that not count as "I ran forever but I explained this to you in a different kind of way"

#### [Simon Hudon (Feb 27 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce vs #eval/near/123061395):
It would but my example involves numbers such as 1 and 0

#### [Kevin Buzzard (Feb 27 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce vs #eval/near/123061409):
Try `(1+1)*(1+1)*(1+1)*(1+1)*...*(1+1)`

#### [Simon Hudon (Feb 27 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce vs #eval/near/123061467):
... but it also involves an encoding of an infinite tree ... I wonder if that's what is taking super duper long

#### [Simon Hudon (Feb 27 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce vs #eval/near/123061650):
I'll be more specific. I'm trying:

```lean
#reduce to_bin_tree 3 (mk_tree 0)
```

where `my_tree` creates an infinite tree starting at 0 and incrementing it from time to time and `to_bin_tree` truncates it after 3 steps. It creates the following binary tree:

```
(node 0 (node 1 (node ⊥ ⊥)))
```

#### [Simon Hudon (Feb 27 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce vs #eval/near/123061734):
Anyway, you made your point. Truncating the tree is probably much more expensive now that I changed their representation

#### [Simon Hudon (Feb 27 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/#reduce vs #eval/near/123061736):
Thanks!

