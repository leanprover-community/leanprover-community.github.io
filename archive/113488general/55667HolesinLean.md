---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55667HolesinLean.html
---

## Stream: [general](index.html)
### Topic: [Holes in Lean](55667HolesinLean.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Stevens (May 29 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Holes%20in%20Lean/near/127223244):
Last noob question of the night from me: "holes" in Lean are not the same thing as holes in Agda, right? Agda lets you use the question mark symbol to create what they call a "hole", which is a subgoal; the prover can take a guess at how to fill if you ask it. I found http://leodemoura.github.io/files/lean_cade25.pdf which suggests that the underscore should do something similar in Lean, but my feeble attempts with the underscore and with curly braces don't seem to replicate what Agda does.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 29 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Holes%20in%20Lean/near/127223257):
in tactic mode you can do `refine`, which makes `_` into subgoals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 29 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Holes%20in%20Lean/near/127223258):
in term mode subgoals don't make sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 29 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Holes%20in%20Lean/near/127223298):
the syntax of `refine` is similar to `exact`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Stevens (May 29 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Holes%20in%20Lean/near/127223309):
Great, thanks - I'll have a play with it now I know what I'm looking for

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 29 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Holes%20in%20Lean/near/127223536):
Holes in Lean are an incomplete alpha feature, the syntax is `{! !}`. They aren't so useful right now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 29 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Holes%20in%20Lean/near/127223577):
@**Andrew Ashworth** is that different from `refine funext _`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 29 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Holes%20in%20Lean/near/127223579):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 29 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Holes%20in%20Lean/near/127223642):
holes are a way to make term mode as easy to use as tactics, in a way. stuff like automatically knowing the type of a hole, and clicking an option to write out a match statement, or calc block, generally any sequence of term mode steps that can be automated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 29 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Holes%20in%20Lean/near/127223704):
but yeah, it's sorta like `_`, but better

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 29 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Holes%20in%20Lean/near/127223709):
I'm not sure why it needs a special syntax, I'm not too familiar with holes. They are big in Agda and Idris

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Holes%20in%20Lean/near/127278347):
I see holes all the time in tactic mode. I try and make my tactic proof run at all times, and fill the holes with sorry, and then sometimes remove one and just look at the output to see what I have to fill. It's so much easier in tactic mode which is why I use tactic mode for anything non-trivial basically


{% endraw %}
