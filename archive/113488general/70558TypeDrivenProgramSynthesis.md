---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/70558TypeDrivenProgramSynthesis.html
---

## Stream: [general](index.html)
### Topic: ["Type-Driven Program Synthesis"](70558TypeDrivenProgramSynthesis.html)

---


{% raw %}
#### [ Bryan Gin-ge Chen (Oct 22 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136245038):
<p>I just watched and enjoyed this talk: <a href="https://www.youtube.com/watch?v=HnOix9TFy1A" target="_blank" title="https://www.youtube.com/watch?v=HnOix9TFy1A">"Type-Driven Program Synthesis" by Nadia Polikarpova</a>. To a newbie like me, this kind of automation seems quite cool and mindblowing. Also, the way she described synthesizing programs as a search problem made me think of <span class="user-mention" data-user-id="110087">@Scott Morrison</span> 's <code>rewrite_search</code> demo.</p>
<p>How much of this is useful / within reach for theorem proving? Presumably there are some restrictions (e.g. decidability?) on what this can be used on, but I haven't looked too hard at <a href="https://cseweb.ucsd.edu/~npolikarpova/publications/pldi16.pdf" target="_blank" title="https://cseweb.ucsd.edu/~npolikarpova/publications/pldi16.pdf">the paper</a>. How different are "refinement types" from subtypes in lean? Here's <a href="https://bitbucket.org/nadiapolikarpova/synquid" target="_blank" title="https://bitbucket.org/nadiapolikarpova/synquid">the "Synquid" repository</a> and <a href="http://comcom.csail.mit.edu/comcom/#Synquid" target="_blank" title="http://comcom.csail.mit.edu/comcom/#Synquid">live demo</a>. I guess the work is from 2016, so maybe it's already been discussed pre-zulip?</p>
<div class="youtube-video message_inline_image"><a data-id="HnOix9TFy1A" href="https://www.youtube.com/watch?v=HnOix9TFy1A" target="_blank" title="https://www.youtube.com/watch?v=HnOix9TFy1A"><img src="https://i.ytimg.com/vi/HnOix9TFy1A/default.jpg"></a></div>

#### [ Simon Hudon (Oct 22 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136246221):
<p>I don't see why we couldn't do it in Lean</p>

#### [ Mario Carneiro (Oct 22 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136246651):
<p>Refinement types are another way to express the same idea as subtypes, but the execution is different</p>

#### [ Mario Carneiro (Oct 22 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136246700):
<p>in particular, a refinement type is a subtype, in the sense that if <code>x : {v : T | stuff}</code> then <code>x : T</code>. Lean does not have subtyping in this sense</p>

#### [ Simon Hudon (Oct 22 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136246710):
<p>Do we have coercion between a subtype and its carrier type?</p>

#### [ Mario Carneiro (Oct 22 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136246722):
<p>In lean, this means you have to insert functions going back and forth, but since the VM erases proofs these functions disappear from generated code</p>

#### [ Mario Carneiro (Oct 22 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136246728):
<p>yes, there is a coe instance for subtype</p>

#### [ Simon Hudon (Oct 22 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136246787):
<p>If you have <code>xs : list { v : T | stuff }</code>, I don't suppose <code>xs.map subtype.val</code> will reduce to <code>id</code>, will it?</p>

#### [ Mario Carneiro (Oct 22 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136246832):
<p>unfortunately no. This is one place where I want compiler support for marking functions as "VM identity functions"</p>

#### [ Mario Carneiro (Oct 22 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136246834):
<p>same for <code>list.attach</code></p>

#### [ Simon Hudon (Oct 22 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22Type-Driven%20Program%20Synthesis%22/near/136246843):
<p>Haskell has the same trouble</p>


{% endraw %}
