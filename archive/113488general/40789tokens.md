---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40789tokens.html
---

## Stream: [general](index.html)
### Topic: [tokens](40789tokens.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 08 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382507):
Does anyone know where the list of "registered tokens" is?
> /-- Check that the next token is `tk` and consume it. `tk` must be a registered token. -/
> meta constant tk (tk : string) : parser unit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 08 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382549):
You can define one as ``precedence `my_keyword`:0``

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 08 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382612):
I'd like to modify some of my tactics so they print out a trace message of what they're doing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 08 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382619):
My idea was to have, e.g. `backwards_reasoning`, but then be able to write `backwards_reasoning?` and get trace ouput.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 08 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382620):
However `?` isn't an allowed token.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 08 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382623):
Do you have a suggestion for good syntax for this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 08 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382666):
I'm hoping that one day this model might be widespread --- e.g. in Lean 4 we could even imagine your squeeze_simp just be callable by `simp?`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 08 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382731):
Are you trying to make `backwards_reasoning?`the name of the tactic or is `?` a parameter to `backwards_reasoning`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 08 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382740):
? was meant to be a parameter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 08 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382741):
I can make this work with !, just via:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 08 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382742):
`meta def backwards_reasoning (trace : parse $ optional (tk "!"))  ...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 08 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382782):
Hmm, it seems `#` works fine, maybe that's good enough.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382784):
Surely `?` is a token

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 08 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382785):
Somehow `!` strikes me as a "work harder!" modifier to a tactic,  rather than a "tell me more"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382795):
I think `rcases` and `rintro` use `?` in their parsing, for the hint mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 08 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382802):
Okay, I will look at those.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382811):
Actually it would be nice if `squeeze_simp` was `simp?`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 08 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382817):
Ugh...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 08 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382853):
I get the same error as you but this fixes it:

```lean
precedence `?`:0
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 08 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382864):
Awesome, thanks @**Simon Hudon**.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 08 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382867):
Presumably this is a bit fragile, but works for now. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382870):
I would be careful with that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382876):
declaring something as a token makes it unusable as a variable name

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382884):
maybe that's not a problem here though :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382950):
Does it work if you declare it locally?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382958):
I see that `rcases` has ``local postfix `?`:9001 := optional``, which may be a factor in why this works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 08 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135383035):
I am also unclear on the interaction between `postfix` and `precedence`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 08 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135383149):
You can't do anything with `local precedence`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 08 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135383161):
Even if you could that would make your tactic tricky to use

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 08 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135383206):
Yeah.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 08 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135410263):
Aha interesting. So this explains why I could never get `rcases?` to work. It only works once I make `?` some kind of notation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 08 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135411814):
That sounds like a probable explanation. @**Mario Carneiro** you may need to add ``precedence `?`:0`` in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135413968):
oh! I didn't realize `rcases?` was broken

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 08 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135418076):
This was mentioned several times here, but I guess we need to learn to use GitHub issues instead of only relying on whining here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135418181):
was it? I don't recall any error reports for `rcases?`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 08 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135419249):
e.g. https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/rcases.3F/near/133503552

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135419347):
oh, I thought that was resolved from the comments

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 08 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135419489):
I was sure it was mentioned a couple more times but I can't find it

