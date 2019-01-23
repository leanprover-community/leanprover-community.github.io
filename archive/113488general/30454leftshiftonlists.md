---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30454leftshiftonlists.html
---

## Stream: [general](index.html)
### Topic: [left shift on lists](30454leftshiftonlists.html)

---

#### [Chris Hughes (Jun 01 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/left%20shift%20on%20lists/near/127424565):
Is there a function on lists that rotates the elements of the list i.e [1, 2, 3, 4] -> [2, 3, 4, 1]?

#### [Simon Hudon (Jun 01 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/left%20shift%20on%20lists/near/127424622):
For list `xs`, you can do it with `drop 1 xs ++ take 1 xs`

#### [Kevin Buzzard (Jun 01 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/left%20shift%20on%20lists/near/127429588):
you'd better remember what you dropped :-)

#### [Simon Hudon (Jun 01 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/left%20shift%20on%20lists/near/127430668):
yep! That's what`take 1 xs` does

