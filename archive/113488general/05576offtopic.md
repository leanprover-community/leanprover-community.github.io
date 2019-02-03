---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/05576offtopic.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [off-topic](https://leanprover-community.github.io/archive/113488general/05576offtopic.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Andrew Ashworth (Feb 26 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123008244):
<p>or you could have an off-topic topic, very meta</p>

#### [ Kevin Buzzard (Feb 26 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123008251):
<p>Now we're flooding the topic list.</p>

#### [ Andrew Ashworth (Feb 26 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123008401):
<p>up and down is j and k, feels very vi-like</p>

#### [ Sean Leather (Feb 26 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123008468):
<p>I'm here. I'm also confused.</p>

#### [ Sean Leather (Feb 26 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123008487):
<p>I'm here. I'm also confused. Doubly confused. Because I didn't know my message was at the bottom!</p>

#### [ Sebastian Ullrich (Feb 26 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123009814):
<p>That's okay, the topic list seems to be a most-recently-used cache</p>

#### [ Andrew Ashworth (Feb 26 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123011839):
<p>is there a way to give a friendly name to a metavariable while inside a proof?</p>

#### [ Simon Hudon (Feb 26 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123011904):
<p>how did you create that meta variable?</p>

#### [ Andrew Ashworth (Feb 26 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012009):
<p>i haven't yet, I'm still in term mode, haha. in tactic mode it'd be from using <code>apply</code>, <code>refine</code>, and friends</p>

#### [ Simon Hudon (Feb 26 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012224):
<p>What you can try is: </p>
<div class="codehilite"><pre><span></span>let my_mvar, tactic.swap,
refine (my_fun my_mvar),
</pre></div>


<p>instead of</p>
<div class="codehilite"><pre><span></span>refine (my_fun _),
</pre></div>

#### [ Andrew Ashworth (Feb 26 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012248):
<p>that looks like what i'd do in term mode with <code>suffices</code>, nice</p>

#### [ Simon Hudon (Feb 26 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012293):
<p><code>suffices</code> works in tactic mode as well</p>

#### [ Chris Hughes (Feb 26 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012589):
<p>How do I view the automatically generated name of an instance?</p>

#### [ Moses Schönfinkel (Feb 26 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012659):
<p>You could <code>#print instances</code> and check that way, I guess?</p>

#### [ Simon Hudon (Feb 26 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012677):
<p>wrong topic</p>

#### [ Patrick Massot (Feb 26 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012744):
<p>That's the real test: will the stream and topic stuff be useful or irritating?</p>

#### [ Moses Schönfinkel (Feb 26 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012749):
<p>I don't think I have the mental fortitude to carefully tag every message I type :(.</p>

#### [ Simon Hudon (Feb 26 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012752):
<p>I think it would be great if you suggest a different topic for a given post</p>

#### [ Simon Hudon (Feb 26 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012820):
<blockquote>
<p>I don't think I have the mental fortitude to carefully tag every message I type :(.</p>
</blockquote>
<p>If you click on the message you want to respond to, you're going to respond in the right topic</p>

#### [ Moses Schönfinkel (Feb 26 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012826):
<p>That would mean I have to touch the rodent.</p>

#### [ Moses Schönfinkel (Feb 26 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012870):
<p>I sit on a fitball and my furry friend is a little bit too far usually.</p>

#### [ Reid Barton (Feb 26 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012871):
<p>You can also press <code>r</code> or Enter to respond</p>

#### [ Moses Schönfinkel (Feb 26 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012877):
<p>Can <code>r</code> read my mind as to which message I am replying to?</p>

#### [ Andrew Ashworth (Feb 26 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012891):
<p>you can use j and k to move up and down, ? displays keyboard shortcuts</p>

#### [ Simon Hudon (Feb 26 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012895):
<p>Great!</p>

#### [ Reid Barton (Feb 26 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012919):
<p>(Or the up and down keys)</p>

#### [ Moses Schönfinkel (Feb 26 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012938):
<p>Nice! Why does j go down o_O?</p>

#### [ Andrew Ashworth (Feb 26 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012949):
<p>j moves the cursor down in vim</p>

#### [ Reid Barton (Feb 26 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123012969):
<p><a href="http://www.catonmat.net/blog/why-vim-uses-hjkl-as-arrow-keys/" target="_blank" title="http://www.catonmat.net/blog/why-vim-uses-hjkl-as-arrow-keys/">http://www.catonmat.net/blog/why-vim-uses-hjkl-as-arrow-keys/</a></p>

#### [ Moses Schönfinkel (Feb 26 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123013037):
<p>It's a little bit fiddle-ey I have to say.</p>

#### [ Patrick Massot (Feb 26 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123013052):
<p>help you keep your fingers on the home row</p>

#### [ Andrew Ashworth (Feb 26 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123013055):
<p>i always end up installing nano whenever i have to work on the terminal</p>

#### [ Moses Schönfinkel (Feb 26 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123013066):
<p>I mean the whole reply-to thing with selecting what exactly it is I am replying to. Might be a bit more work than I would like, perhaps?</p>

#### [ Moses Schönfinkel (Feb 26 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123013072):
<p><em>shrug</em></p>

#### [ Andrew Ashworth (Feb 26 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123013075):
<p>probably just fine to post whatever into general, if something deserves more in depth discussion, someone can always quote and reply to break it off into its own topic</p>

#### [ Simon Hudon (Feb 26 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123013426):
<p>for starting conversations, that's good but in the middle of a conversation, commenting on the wrong topic means that some people will see it and others will not</p>

#### [ Reid Barton (Feb 26 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123013745):
<p>Everyone sees messages to all topics on the streams they're subscribed to (unless they've explicitly muted a particular topic, which isn't the common case).<br>
An analogy that might be helpful is that streams are like mailing lists while topics are like the subjects of threads on a particular list. Streams are relatively static and stream membership determines what you receive. Topics are ephemeral and clarify the context of a message. If there is a conversation about affine schemes and another conversation about mathlib failing to build, then you can reply to one of the conversations with "it didn't work" and it won't be misunderstood as relating to the other conversation.<br>
You can also choose to view one topic at a time or all topics on a stream (or on all streams) mixed together, but the expectation is that you'll eventually see all messages on a stream regardless of their topics.</p>

#### [ Reid Barton (Feb 26 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/off-topic/near/123013910):
<p>For now, there's little enough traffic (here and on the gitter) that it probably doesn't make sense to create additional streams, but if, say, the stacks project grows to the point where not all lean users want to see all the discussion about the project, that's when having a separate stream would be useful.</p>


{% endraw %}
