---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/05576offtopic.html
---

## Stream: [general](index.html)
### Topic: [off-topic](05576offtopic.html)

---


{% raw %}
#### [ Andrew Ashworth (Feb 26 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123008244):
or you could have an off-topic topic, very meta

#### [ Kevin Buzzard (Feb 26 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123008251):
Now we're flooding the topic list.

#### [ Andrew Ashworth (Feb 26 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123008401):
up and down is j and k, feels very vi-like

#### [ Sean Leather (Feb 26 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123008468):
I'm here. I'm also confused.

#### [ Sean Leather (Feb 26 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123008487):
I'm here. I'm also confused. Doubly confused. Because I didn't know my message was at the bottom!

#### [ Sebastian Ullrich (Feb 26 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123009814):
That's okay, the topic list seems to be a most-recently-used cache

#### [ Andrew Ashworth (Feb 26 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123011839):
is there a way to give a friendly name to a metavariable while inside a proof?

#### [ Simon Hudon (Feb 26 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123011904):
how did you create that meta variable?

#### [ Andrew Ashworth (Feb 26 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012009):
i haven't yet, I'm still in term mode, haha. in tactic mode it'd be from using `apply`, `refine`, and friends

#### [ Simon Hudon (Feb 26 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012224):
What you can try is: 

```
let my_mvar, tactic.swap,
refine (my_fun my_mvar),
```

instead of

```
refine (my_fun _),
```

#### [ Andrew Ashworth (Feb 26 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012248):
that looks like what i'd do in term mode with `suffices`, nice

#### [ Simon Hudon (Feb 26 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012293):
`suffices` works in tactic mode as well

#### [ Chris Hughes (Feb 26 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012589):
How do I view the automatically generated name of an instance?

#### [ Moses Schönfinkel (Feb 26 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012659):
You could `#print instances` and check that way, I guess?

#### [ Simon Hudon (Feb 26 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012677):
wrong topic

#### [ Patrick Massot (Feb 26 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012744):
That's the real test: will the stream and topic stuff be useful or irritating?

#### [ Moses Schönfinkel (Feb 26 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012749):
I don't think I have the mental fortitude to carefully tag every message I type :(.

#### [ Simon Hudon (Feb 26 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012752):
I think it would be great if you suggest a different topic for a given post

#### [ Simon Hudon (Feb 26 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012820):
```quote
I don't think I have the mental fortitude to carefully tag every message I type :(.
```
If you click on the message you want to respond to, you're going to respond in the right topic

#### [ Moses Schönfinkel (Feb 26 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012826):
That would mean I have to touch the rodent.

#### [ Moses Schönfinkel (Feb 26 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012870):
I sit on a fitball and my furry friend is a little bit too far usually.

#### [ Reid Barton (Feb 26 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012871):
You can also press `r` or Enter to respond

#### [ Moses Schönfinkel (Feb 26 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012877):
Can `r` read my mind as to which message I am replying to?

#### [ Andrew Ashworth (Feb 26 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012891):
you can use j and k to move up and down, ? displays keyboard shortcuts

#### [ Simon Hudon (Feb 26 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012895):
Great!

#### [ Reid Barton (Feb 26 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012919):
(Or the up and down keys)

#### [ Moses Schönfinkel (Feb 26 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012938):
Nice! Why does j go down o_O?

#### [ Andrew Ashworth (Feb 26 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012949):
j moves the cursor down in vim

#### [ Reid Barton (Feb 26 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012969):
http://www.catonmat.net/blog/why-vim-uses-hjkl-as-arrow-keys/

#### [ Moses Schönfinkel (Feb 26 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123013037):
It's a little bit fiddle-ey I have to say.

#### [ Patrick Massot (Feb 26 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123013052):
help you keep your fingers on the home row

#### [ Andrew Ashworth (Feb 26 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123013055):
i always end up installing nano whenever i have to work on the terminal

#### [ Moses Schönfinkel (Feb 26 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123013066):
I mean the whole reply-to thing with selecting what exactly it is I am replying to. Might be a bit more work than I would like, perhaps?

#### [ Moses Schönfinkel (Feb 26 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123013072):
*shrug*

#### [ Andrew Ashworth (Feb 26 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123013075):
probably just fine to post whatever into general, if something deserves more in depth discussion, someone can always quote and reply to break it off into its own topic

#### [ Simon Hudon (Feb 26 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123013426):
for starting conversations, that's good but in the middle of a conversation, commenting on the wrong topic means that some people will see it and others will not

#### [ Reid Barton (Feb 26 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123013745):
Everyone sees messages to all topics on the streams they're subscribed to (unless they've explicitly muted a particular topic, which isn't the common case).
An analogy that might be helpful is that streams are like mailing lists while topics are like the subjects of threads on a particular list. Streams are relatively static and stream membership determines what you receive. Topics are ephemeral and clarify the context of a message. If there is a conversation about affine schemes and another conversation about mathlib failing to build, then you can reply to one of the conversations with "it didn't work" and it won't be misunderstood as relating to the other conversation.
You can also choose to view one topic at a time or all topics on a stream (or on all streams) mixed together, but the expectation is that you'll eventually see all messages on a stream regardless of their topics.

#### [ Reid Barton (Feb 26 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123013910):
For now, there's little enough traffic (here and on the gitter) that it probably doesn't make sense to create additional streams, but if, say, the stacks project grows to the point where not all lean users want to see all the discussion about the project, that's when having a separate stream would be useful.


{% endraw %}
