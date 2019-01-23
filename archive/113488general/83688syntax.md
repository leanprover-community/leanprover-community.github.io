---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83688syntax.html
---

## Stream: [general](index.html)
### Topic: [syntax](83688syntax.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 04 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127544480):
Fun fact: `notation` applies even in `namespace` commands, so if you write ``notation `foo` := bar`` and then `namespace foo` it means `namespace bar`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 04 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127544555):
Cool! :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 04 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127544571):
I don't know if that's a good thing but I was properly surprised when I realized what you meant

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 04 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127544624):
If you don't want this to happen (like I didn't) then you can write `namespace «foo»`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 04 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127544649):
Curiously enough, it also works on binders: `∀ foo, f foo` actually means `∀ bar, f bar` which is inconvenient when the notation is a short hand for an expression, not an identifier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 04 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127544653):
Thanks for the fix

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 04 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127544833):
o.O

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 04 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127544900):
I take it that's unintended behavior?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 04 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127544969):
(I was actually using `local notation`, in case that matters)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 04 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127545111):
I get "identifier expected" in both cases
```
constants foo bar : Type
local notation `foo` := bar
#check ∀ foo, foo
namespace foo
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 04 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127545171):
Oh, I might have jumped to conclusions.
What actually happened was that I was inside `namespace foo` and then I defined `foo` as local notation for something, and then `end foo` stopped working.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 04 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127545183):
with some error like "identifier expected"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 04 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127545332):
Yes, you're right. That's what happens for me too. Sorry about the confusion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 04 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127545397):
I see. This will probably be fixed in Lean 4 automatically since we will be using a parser combinator without a scanner, so we can skip notations where we only want to parse identifiers.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 04 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127545431):
How is that going by the way?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 04 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127545680):
Let's... say that we're transitioning from the planning phase to the implementation phase (parser, compiler, and other refactorings)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 04 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127545899):
Exciting :D I can't wait to see where that will end up!


{% endraw %}
