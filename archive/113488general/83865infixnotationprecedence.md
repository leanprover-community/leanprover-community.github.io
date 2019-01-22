---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83865infixnotationprecedence.html
---

## [general](index.html)
### [infix notation precedence](83865infixnotationprecedence.html)

#### [Sean Leather (Jun 07 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/infix notation precedence/near/127717979):
I want something that is effectively equivalent to this:

```lean
reserve infix ` d∉ `:51
local notation a d∉ l := blah l a
```

However, I'm guessing it's not a good idea to use `reserve` here. I've tried several `notation` declarations (e.g. ``notation a ` d∉ `:51 l`` and ``notation a ` d∉ `:51 l:0``), but I can't seem to get the precedence right. What's the correct way to specify the above without using `reserve`?

#### [Sebastian Ullrich (Jun 07 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/infix notation precedence/near/127718532):
Why are you not using `local infix`?

#### [Sean Leather (Jun 07 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/infix notation precedence/near/127718663):
Because then I would have to write:

```lean
local infix ` d∉ `:51 := λ a l, blah l a
```

#### [Sebastian Ullrich (Jun 07 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/infix notation precedence/near/127718782):
I see. The equivalent to `infix` should be 
```
a ` d∉ `:51 l:51
```

#### [Sean Leather (Jun 07 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/infix notation precedence/near/127718930):
Ah ha! Can you help me understand that?

#### [Sebastian Ullrich (Jun 07 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/infix notation precedence/near/127719540):
The first `:51` sets the token's binding power, whereas the second one sets the right-binding power (rbp) the Pratt parser will use while parsing that expression. The parser will try to parse an expression until it encounters a token with bp <= its rbp. The rbp used initially is 0.
For example, on the input `a d∉ b d∉ c` (not that it makes much sense in your case), the parser will start with rbp 0, read the leading term `a`, read the token with bp > 0, then recurse for the notation RHS using rbp 51. This recursive call will read the leading `b`, then stop at the token since 51 <= 51, and return. The original parser call will accept it, since it uses rbp 0, and complete parsing the input. Thus the output is `(a d∉ b) d∉ c` because the parser for the first notation's RHS stopped after `b`.

#### [Sebastian Ullrich (Jun 07 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/infix notation precedence/near/127719638):
If you use `infixr` instead and do `#print d∉`, you'll see that the RHS now has rbp 50 so that it will consume the `d∉` token

#### [Sean Leather (Jun 08 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/infix notation precedence/near/127757084):
Thanks, @**Sebastian Ullrich**!

