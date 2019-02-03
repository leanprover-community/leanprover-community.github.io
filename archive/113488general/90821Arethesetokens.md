---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90821Arethesetokens.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Are these tokens?](https://leanprover-community.github.io/archive/113488general/90821Arethesetokens.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 01 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499064):
<p>In VS Code, if I type <code>#check nat.</code>and then, with the cursor just to the right of the <code>.</code> I type Esc then ctrl-space (possibly more than once) then I get, I think, to see a list of things which the Lean VS Code plugin thinks might come next. In this particular case,  the list seems to naturally split into two types of things.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499067):
<p>The first type of thing is the "purple cube" type of thing, which are all the possibilities which are prefixed by a little drawing of a purple hexagon/cube thing.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499078):
<p>In this particular case they seem to be every single theorem / definition / constructor etc (perhaps every single <code>name</code>?) which starts <code>nat.X</code> where <code>X</code> begins with a, b, c or d.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499082):
<p>The fact that it stops at d might be a bug in the VS Code Lean plugin.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499123):
<p>But, from <code>nat.add</code> to <code>nat.discriminate</code> they're all "purple cube" choices.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499126):
<p>And then after the purple cube choices, we have the "about 7 straight lines" choices</p>

#### [ Kenny Lau (Apr 01 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499131):
<blockquote>
<p>The fact that it stops at d might be a bug in the VS Code Lean plugin.</p>
</blockquote>
<p>or maybe because there are too many possibilities?</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499184):
<p>The "7 straight lines" possibilities start <code>#check #compile #eval #exit #help #print #reduce #unify</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499232):
<p>and then there's a whole bunch more, <code>add_key_equivalence assume at attribute axiom axioms begin by calc class coinductive...</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499238):
<p>there is <code>def</code> but no <code>definition</code></p>

#### [ Kenny Lau (Apr 01 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499240):
<p>wait, coinductive?</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499245):
<p>there is <code>theorem</code> though.</p>

#### [ Kenny Lau (Apr 01 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499247):
<p>wait, I thought we don't have coinductive!</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499250):
<p>VS Code says it's there</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499252):
<p>but then again I thought we had definitions</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499253):
<p>and VS Code says no</p>

#### [ Kenny Lau (Apr 01 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499294):
<p>nah, coinductive hasn't been implemented</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499296):
<p>These are strange choices for completions because nat.theorem makes no sense</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499297):
<p><code> vm check failed: is_closure(o) (possibly due to incorrect axioms, or sorry) </code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499298):
<p>I think you get an achievement for that error</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499303):
<p>I'll give you an octopus</p>

#### [ Kenny Lau (Apr 01 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499306):
<p>thanks</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499348):
<p>So are these "7 straight lines" almost the complete list of symbols and commands?</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499349):
<p>except that they do mention coinductive and don't mention definition...</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499400):
<p>As well as "purple cube" and "7 lines" I can get "abc in a box"</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499401):
<p>which might mean "string"</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499461):
<p>although ctrl-space after <code>#check "abc"</code>gives me that <code>#check</code> is an abc-in-a-box</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499474):
<p>Maybe purple cube means "identifier"</p>

#### [ Kevin Buzzard (Apr 01 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499732):
<p>Reading through the docs of Lean VS Code extension doesn't seem to mention these purple hexagons. It does say " *   By default, vscode will complete <code>then</code> to <code>has_bind.and_then</code> when you press enter. To disable this behavior, set <code>"editor.acceptSuggestionOnEnter": false</code> " though, which I think is not true: it should be the string "off" rather than the bool <code>false</code></p>

#### [ Mario Carneiro (Apr 01 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20these%20tokens%3F/near/124499792):
<p><code>coinductive</code> is a lean command, but it only supports coinductive predicates. It is defined as a user command in <code>init/meta/coinductive_predicates.lean</code></p>


{% endraw %}
