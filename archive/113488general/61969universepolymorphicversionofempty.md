---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/61969universepolymorphicversionofempty.html
---

## [general](index.html)
### [universe polymorphic version of empty?](61969universepolymorphicversionofempty.html)

#### [Zesen Qian (Jul 05 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe polymorphic version of empty?/near/129158168):
RT? The current empty is at Type 0

#### [Zesen Qian (Jul 05 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe polymorphic version of empty?/near/129158198):
just don't want to reinvent the wheel.
Also wondering why empty is not universe polymorphic

#### [Chris Hughes (Jul 05 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe polymorphic version of empty?/near/129158379):
What situation would it be an advantage for empty to be polymorphic?

#### [Zesen Qian (Jul 05 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe polymorphic version of empty?/near/129158418):
oh wait, is lean's universe cumulative?

#### [Simon Hudon (Jul 05 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe polymorphic version of empty?/near/129158419):
If you need `empty` in universe `u`, you can use `ulift.up.{u} empty`. `ulift` is a tool to fit objects of different universes together.

#### [Simon Hudon (Jul 05 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe polymorphic version of empty?/near/129158425):
No, it's not

#### [Zesen Qian (Jul 05 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe polymorphic version of empty?/near/129158429):
very nice, thank you.

#### [Simon Hudon (Jul 05 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe polymorphic version of empty?/near/129158469):
we use `ulift` when we would need cumulativeness

#### [Simon Hudon (Jul 05 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe polymorphic version of empty?/near/129158575):
In general, you should use universe variables as rarely as possible and use `ulift`. When you build definitions like `list`, you have no choice to make it universe polymorphic so that it can be used in various universes: `list : Type u -> Type u`. That's because if `list : Type -> Type`, there's no way of using lift on `a : Type 3` in order to have a `list a`

#### [Zesen Qian (Jul 05 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe polymorphic version of empty?/near/129159229):
ahh, can't understand the error
ulift Type 
not match 
Type u

#### [Simon Hudon (Jul 05 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe polymorphic version of empty?/near/129159286):
Can you show the code?

#### [Zesen Qian (Jul 05 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe polymorphic version of empty?/near/129159295):
```
def clause : list (Type u) → Type u
| ([]) := ulift.up.{u+1} empty
| (x :: xs) := sum x $ clause xs
```

#### [Simon Hudon (Jul 05 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe polymorphic version of empty?/near/129159557):
Use `ulift empty` instead of `ulift.up empty`. `ulift.up` is something you use on a term. On a type, you use simply `ulift`

