---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/39790Parser.html
---

## Stream: [new members](index.html)
### Topic: [Parser](39790Parser.html)

---


{% raw %}
#### [ Pablo Le Hénaff (Aug 08 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131100158):
<p>Hello !</p>

#### [ Kenny Lau (Aug 08 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131100172):
<p>bienvenu</p>

#### [ Pablo Le Hénaff (Aug 08 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131100173):
<p>Can one use lean.parser to actually parse strings? If so, how do I run a parser on a string? That's what I want to do.</p>

#### [ Pablo Le Hénaff (Aug 08 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131102457):
<p>Should I ask this on the other <a class="stream" data-stream-id="113488" href="/#narrow/stream/113488-general">#general</a>  stream?</p>

#### [ Sean Leather (Aug 08 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131102527):
<p>You could try pinging <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> and <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span>. (Actually, I just did that. <span class="emoji emoji-263a" title="smile">:smile:</span>)</p>

#### [ Rob Lewis (Aug 08 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131102655):
<p><span class="user-mention" data-user-id="114221">@Pablo Le Hénaff</span> You can. Here's an example: <a href="https://github.com/robertylewis/mathematica/blob/master/mathematica_parser.lean" target="_blank" title="https://github.com/robertylewis/mathematica/blob/master/mathematica_parser.lean">https://github.com/robertylewis/mathematica/blob/master/mathematica_parser.lean</a></p>

#### [ Scott Morrison (Aug 08 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131102723):
<p><span class="user-mention" data-user-id="110596">@Rob Lewis</span> cool! Last time I asked about this, I got the impression it couldn't be done.</p>

#### [ Rob Lewis (Aug 08 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131102733):
<p>Er, wait a sec. <code>lean.parser</code> is different from <code>data.buffer.parser</code>.</p>

#### [ Pablo Le Hénaff (Aug 08 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131102760):
<p>I didn't know about <code>data.buffer.parser</code></p>

#### [ Rob Lewis (Aug 08 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131102828):
<p><code>data.buffer.parser</code> is a parser monad. <code>lean.parser</code> exposes a bit of the built-in parser, I think.</p>

#### [ Rob Lewis (Aug 08 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131102840):
<p>So you can use the former to write your own string parser. But you don't get access to any of the built in stuff.</p>

#### [ Pablo Le Hénaff (Aug 08 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131102853):
<p>I think <code>data.buffer.parser</code> is what I need, thanks!</p>

#### [ Rob Lewis (Aug 08 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131102949):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> What can't be done (easily, anyway) is parsing a string into an expr.</p>

#### [ Scott Morrison (Aug 08 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131103152):
<p>ah, okay. The thing I really wanted to do was parse a string into a tactic.</p>

#### [ Scott Morrison (Aug 08 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131103215):
<p>(I have some "self-describing" tactics, which you can ask to output a string, which is meant to be a tactic block that achieves whatever the invoked tactic just did (probably only using lower-level tactics). I really want to verify the output by parsing it and replaying it on the original goal, but never worked out how to do the parsing step.)</p>

#### [ Rob Lewis (Aug 08 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131103543):
<p>Yeah, you'd need to access the Lean parser to do that.</p>

#### [ Rob Lewis (Aug 08 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131103549):
<p>Can you make them output an expr instead of a string?</p>

#### [ Johan Commelin (Aug 08 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131103550):
<p>Hmm, can't you save the tactics from just before you generate the strings</p>

#### [ Scott Morrison (Aug 08 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131103754):
<p>Sure, certainly I can save the tactics: the point is to double-check that the copy-and-pasteable text you're about to present to the human really does what you promise.</p>


{% endraw %}
