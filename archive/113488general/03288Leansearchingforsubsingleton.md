---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03288Leansearchingforsubsingleton.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Lean searching for subsingleton?](https://leanprover-community.github.io/archive/113488general/03288Leansearchingforsubsingleton.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Nov 09 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147398515):
<p><a href="https://gist.github.com/kckennylau/2b5890b44f2f66196254a50e9fd6fa96#file-subsingleton-L727" target="_blank" title="https://gist.github.com/kckennylau/2b5890b44f2f66196254a50e9fd6fa96#file-subsingleton-L727">https://gist.github.com/kckennylau/2b5890b44f2f66196254a50e9fd6fa96#file-subsingleton-L727</a><br>
What motivates Lean to use 10 second to search for a subsingleton instance?</p>

#### [ Kenny Lau (Nov 09 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147398535):
<p>The code was</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">monic_X_sub_C&#39;</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">monic</span> <span class="o">(</span><span class="n">X</span> <span class="bp">-</span> <span class="n">C</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">unfold</span> <span class="n">monic</span> <span class="n">leading_coeff</span> <span class="n">nat_degree</span> <span class="n">degree</span> <span class="n">coeff</span>
</pre></div>

#### [ Kenny Lau (Nov 09 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147398546):
<p>but I'm afraid one cannot reproduce this because I modified polynomials in some other ways</p>

#### [ Kenny Lau (Nov 09 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147398611):
<p>So unfortunately my link would have to suffice</p>

#### [ Kenny Lau (Nov 09 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147398794):
<p>Actually the subsingleton thing might not be related at all</p>

#### [ Kenny Lau (Nov 09 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147398798):
<p>I really don't know why Lean uses 10 seconds to elaborate the type</p>

#### [ Kenny Lau (Nov 09 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147398916):
<p>How will it scale when our library gets 2 times bigger?</p>

#### [ Kenny Lau (Nov 09 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147399015):
<p>Would we need a day to compile the mathlib?</p>

#### [ Kenny Lau (Nov 09 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147399022):
<p>We only have ~260 files now</p>

#### [ Kenny Lau (Nov 09 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147399188):
<p>also very strangely, if I go to my sandbox and import data.polynomial and do exactly the same thing, it compiles in a fraction in a second</p>

#### [ Kenny Lau (Nov 09 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147399197):
<p>despite the environment being the same</p>

#### [ Kevin Buzzard (Nov 09 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147400866):
<p>You have been posting some very hard-to-reproduce issues recently</p>

#### [ Mario Carneiro (Nov 09 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147401204):
<p>Usually searches for subsingleton instances are prompted by <code>congr</code> (also used inside <code>simp</code>), which will use subsingleton instances to avoid some subgoals</p>

#### [ Kenny Lau (Nov 09 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20searching%20for%20subsingleton%3F/near/147401342):
<p>ok</p>


{% endraw %}
