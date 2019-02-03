---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40789tokens.html
---

## Stream: [general](index.html)
### Topic: [tokens](40789tokens.html)

---


{% raw %}
#### [ Scott Morrison (Oct 08 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382507):
<p>Does anyone know where the list of "registered tokens" is?</p>
<blockquote>
<p>/-- Check that the next token is <code>tk</code> and consume it. <code>tk</code> must be a registered token. -/<br>
meta constant tk (tk : string) : parser unit</p>
</blockquote>

#### [ Simon Hudon (Oct 08 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382549):
<p>You can define one as <code>precedence `my_keyword`:0</code></p>

#### [ Scott Morrison (Oct 08 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382612):
<p>I'd like to modify some of my tactics so they print out a trace message of what they're doing.</p>

#### [ Scott Morrison (Oct 08 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382619):
<p>My idea was to have, e.g. <code>backwards_reasoning</code>, but then be able to write <code>backwards_reasoning?</code> and get trace ouput.</p>

#### [ Scott Morrison (Oct 08 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382620):
<p>However <code>?</code> isn't an allowed token.</p>

#### [ Scott Morrison (Oct 08 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382623):
<p>Do you have a suggestion for good syntax for this?</p>

#### [ Scott Morrison (Oct 08 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382666):
<p>I'm hoping that one day this model might be widespread --- e.g. in Lean 4 we could even imagine your squeeze_simp just be callable by <code>simp?</code>.</p>

#### [ Simon Hudon (Oct 08 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382731):
<p>Are you trying to make <code>backwards_reasoning?</code>the name of the tactic or is <code>?</code> a parameter to <code>backwards_reasoning</code>?</p>

#### [ Scott Morrison (Oct 08 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382740):
<p>? was meant to be a parameter</p>

#### [ Scott Morrison (Oct 08 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382741):
<p>I can make this work with !, just via:</p>

#### [ Scott Morrison (Oct 08 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382742):
<p><code>meta def backwards_reasoning (trace : parse $ optional (tk "!"))  ...</code></p>

#### [ Scott Morrison (Oct 08 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382782):
<p>Hmm, it seems <code>#</code> works fine, maybe that's good enough.</p>

#### [ Mario Carneiro (Oct 08 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382784):
<p>Surely <code>?</code> is a token</p>

#### [ Scott Morrison (Oct 08 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382785):
<p>Somehow <code>!</code> strikes me as a "work harder!" modifier to a tactic,  rather than a "tell me more"</p>

#### [ Mario Carneiro (Oct 08 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382795):
<p>I think <code>rcases</code> and <code>rintro</code> use <code>?</code> in their parsing, for the hint mode</p>

#### [ Scott Morrison (Oct 08 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382802):
<p>Okay, I will look at those.</p>

#### [ Mario Carneiro (Oct 08 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382811):
<p>Actually it would be nice if <code>squeeze_simp</code> was <code>simp?</code></p>

#### [ Scott Morrison (Oct 08 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382817):
<p>Ugh...</p>

#### [ Simon Hudon (Oct 08 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382853):
<p>I get the same error as you but this fixes it:</p>
<div class="codehilite"><pre><span></span><span class="kn">precedence</span> <span class="bp">`</span><span class="err">?</span><span class="bp">`</span><span class="o">:</span><span class="mi">0</span>
</pre></div>

#### [ Scott Morrison (Oct 08 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382864):
<p>Awesome, thanks <span class="user-mention" data-user-id="110026">@Simon Hudon</span>.</p>

#### [ Scott Morrison (Oct 08 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382867):
<p>Presumably this is a bit fragile, but works for now. :-)</p>

#### [ Mario Carneiro (Oct 08 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382870):
<p>I would be careful with that</p>

#### [ Mario Carneiro (Oct 08 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382876):
<p>declaring something as a token makes it unusable as a variable name</p>

#### [ Mario Carneiro (Oct 08 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382884):
<p>maybe that's not a problem here though :)</p>

#### [ Mario Carneiro (Oct 08 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382950):
<p>Does it work if you declare it locally?</p>

#### [ Mario Carneiro (Oct 08 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135382958):
<p>I see that <code>rcases</code> has <code>local postfix `?`:9001 := optional</code>, which may be a factor in why this works</p>

#### [ Simon Hudon (Oct 08 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135383035):
<p>I am also unclear on the interaction between <code>postfix</code> and <code>precedence</code></p>

#### [ Scott Morrison (Oct 08 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135383149):
<p>You can't do anything with <code>local precedence</code></p>

#### [ Simon Hudon (Oct 08 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135383161):
<p>Even if you could that would make your tactic tricky to use</p>

#### [ Scott Morrison (Oct 08 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135383206):
<p>Yeah.</p>

#### [ Reid Barton (Oct 08 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135410263):
<p>Aha interesting. So this explains why I could never get <code>rcases?</code> to work. It only works once I make <code>?</code> some kind of notation.</p>

#### [ Simon Hudon (Oct 08 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135411814):
<p>That sounds like a probable explanation. <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> you may need to add <code>precedence `?`:0</code> in mathlib</p>

#### [ Mario Carneiro (Oct 08 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135413968):
<p>oh! I didn't realize <code>rcases?</code> was broken</p>

#### [ Patrick Massot (Oct 08 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135418076):
<p>This was mentioned several times here, but I guess we need to learn to use GitHub issues instead of only relying on whining here</p>

#### [ Mario Carneiro (Oct 08 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135418181):
<p>was it? I don't recall any error reports for <code>rcases?</code></p>

#### [ Patrick Massot (Oct 08 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135419249):
<p>e.g. <a href="#narrow/stream/113488-general/subject/rcases.3F/near/133503552" title="#narrow/stream/113488-general/subject/rcases.3F/near/133503552">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/rcases.3F/near/133503552</a></p>

#### [ Mario Carneiro (Oct 08 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135419347):
<p>oh, I thought that was resolved from the comments</p>

#### [ Patrick Massot (Oct 08 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tokens/near/135419489):
<p>I was sure it was mentioned a couple more times but I can't find it</p>


{% endraw %}
