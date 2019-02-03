---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/94743Insight.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Insight](https://leanprover-community.github.io/archive/113488general/94743Insight.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Nov 26 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148393158):
<p>Do we know how much of <a href="https://www.youtube.com/watch?v=bGD_YF64Nwk" target="_blank" title="https://www.youtube.com/watch?v=bGD_YF64Nwk">https://www.youtube.com/watch?v=bGD_YF64Nwk</a> has been formally certified?</p>
<div class="youtube-video message_inline_image"><a data-id="bGD_YF64Nwk" href="https://www.youtube.com/watch?v=bGD_YF64Nwk" target="_blank" title="https://www.youtube.com/watch?v=bGD_YF64Nwk"><img src="https://i.ytimg.com/vi/bGD_YF64Nwk/default.jpg"></a></div>

#### [ Scott Morrison (Nov 26 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148394235):
<p>Interesting question. I was wondering the same earlier today. Looks like it was certified enough. :-)</p>

#### [ Scott Morrison (Nov 26 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148394259):
<p><a href="https://lars-lab.jpl.nasa.gov/" target="_blank" title="https://lars-lab.jpl.nasa.gov/">https://lars-lab.jpl.nasa.gov/</a></p>

#### [ Patrick Massot (Nov 26 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148394845):
<p>Indeed</p>

#### [ Patrick Massot (Nov 26 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148395406):
<p><a href="https://lars-lab.jpl.nasa.gov/JPL_Coding_Standard_C.pdf" target="_blank" title="https://lars-lab.jpl.nasa.gov/JPL_Coding_Standard_C.pdf">https://lars-lab.jpl.nasa.gov/JPL_Coding_Standard_C.pdf</a> is pretty scary reading. It makes me wonder why they still use C</p>

#### [ Patrick Massot (Nov 26 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148395488):
<p>(not that  I know anything about this)</p>

#### [ Andrew Ashworth (Nov 26 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148398421):
<p>Embedded systems are still mainly programmed in C and assembly, since you need to interface directly with hardware</p>

#### [ Andrew Ashworth (Nov 26 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148398437):
<p>C++ is getting some traction though</p>

#### [ Kevin Buzzard (Nov 26 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148400439):
<p>How difficult can it be to formally verify C code? Doesn't C only have about 8 commands?</p>

#### [ Simon Cruanes (Nov 26 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148402018):
<p>C is pretty difficult to verify due to the tons of undefined behaviors, but people have done a lot of work on it. I'm more surprised that they never switched to Ada…</p>

#### [ Chris Hughes (Nov 26 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148402097):
<p><code>nat</code> only has two.</p>

#### [ Kevin Buzzard (Nov 27 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148408016):
<blockquote>
<p><code>nat</code> only has two.</p>
</blockquote>
<p>Yeah, but their behaviour is well-defined :-)</p>

#### [ Kenny Lau (Nov 27 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148408161):
<blockquote>
<p>How difficult can it be to formally verify C code? Doesn't C only have about 8 commands?</p>
</blockquote>
<p>... so... verify brainfuck?</p>

#### [ Keeley Hoek (Nov 27 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148408641):
<p>Most of those rules are more benign than I would have thought<br>
Pretty sensible for any embedded system which wants to be careful I guess<br>
Also, classic:</p>
<div class="codehilite"><pre><span></span>Rule 30 (type conversion)
Conversions shall not be performed between a pointer to a
function and any type other than an integral type.
</pre></div>

#### [ Keeley Hoek (Nov 27 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148408657):
<p>"Sorry team, I cast my function pointer to a double, then added five"</p>


{% endraw %}
