---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/57602withtopdiamonds.html
---

## Stream: [maths](index.html)
### Topic: [with_top "diamonds"](57602withtopdiamonds.html)

---


{% raw %}
#### [ Chris Hughes (Oct 25 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/with_top%20%22diamonds%22/near/136461132):
The following equality isn't `rfl`. I think it should be. I tried redefining the instances, because I thought it might have something to do with the issue that stopped `(0 : with_bot nat) = some 0` being definitional, but I couldn't get it to work 
```lean
example : @with_top.add_monoid ℕ _ = add_comm_monoid.to_add_monoid _ := rfl
```

#### [ Johan Commelin (Oct 27 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/with_top%20%22diamonds%22/near/136592348):
Hmmm, since when is `(0 : with_bot nat) = some 0` no longer defeq? I know that things like that worked for `with_zero` a couple of weeks ago. You are just using a wrapper around `option` and the obvious coercion. This seems a bit surprising.

#### [ Chris Hughes (Oct 27 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/with_top%20%22diamonds%22/near/136598822):
Ages ago it didn't work, but it's now fixed.

#### [ Johan Commelin (Oct 27 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/with_top%20%22diamonds%22/near/136598865):
Ok, good!

#### [ Chris Hughes (Oct 27 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/with_top%20%22diamonds%22/near/136603200):
Found a fix and PRed. #442


{% endraw %}
