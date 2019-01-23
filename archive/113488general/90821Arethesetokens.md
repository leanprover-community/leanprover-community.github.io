---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90821Arethesetokens.html
---

## Stream: [general](index.html)
### Topic: [Are these tokens?](90821Arethesetokens.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499064):
In VS Code, if I type `#check nat.`and then, with the cursor just to the right of the `.` I type Esc then ctrl-space (possibly more than once) then I get, I think, to see a list of things which the Lean VS Code plugin thinks might come next. In this particular case,  the list seems to naturally split into two types of things.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499067):
The first type of thing is the "purple cube" type of thing, which are all the possibilities which are prefixed by a little drawing of a purple hexagon/cube thing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499078):
In this particular case they seem to be every single theorem / definition / constructor etc (perhaps every single `name`?) which starts `nat.X` where `X` begins with a, b, c or d.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499082):
The fact that it stops at d might be a bug in the VS Code Lean plugin.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499123):
But, from `nat.add` to `nat.discriminate` they're all "purple cube" choices.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499126):
And then after the purple cube choices, we have the "about 7 straight lines" choices

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499131):
```quote
The fact that it stops at d might be a bug in the VS Code Lean plugin.
```
or maybe because there are too many possibilities?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499184):
The "7 straight lines" possibilities start `#check #compile #eval #exit #help #print #reduce #unify`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499232):
and then there's a whole bunch more, `add_key_equivalence assume at attribute axiom axioms begin by calc class coinductive...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499238):
there is `def` but no `definition`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499240):
wait, coinductive?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499245):
there is `theorem` though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499247):
wait, I thought we don't have coinductive!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499250):
VS Code says it's there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499252):
but then again I thought we had definitions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499253):
and VS Code says no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499294):
nah, coinductive hasn't been implemented

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499296):
These are strange choices for completions because nat.theorem makes no sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499297):
` vm check failed: is_closure(o) (possibly due to incorrect axioms, or sorry) `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499298):
I think you get an achievement for that error

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499303):
I'll give you an octopus

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499306):
thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499348):
So are these "7 straight lines" almost the complete list of symbols and commands?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499349):
except that they do mention coinductive and don't mention definition...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499400):
As well as "purple cube" and "7 lines" I can get "abc in a box"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499401):
which might mean "string"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499461):
although ctrl-space after `#check "abc"`gives me that `#check` is an abc-in-a-box

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499474):
Maybe purple cube means "identifier"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499732):
Reading through the docs of Lean VS Code extension doesn't seem to mention these purple hexagons. It does say " *   By default, vscode will complete `then` to `has_bind.and_then` when you press enter. To disable this behavior, set `"editor.acceptSuggestionOnEnter": false` " though, which I think is not true: it should be the string "off" rather than the bool `false`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499792):
`coinductive` is a lean command, but it only supports coinductive predicates. It is defined as a user command in `init/meta/coinductive_predicates.lean`


{% endraw %}
