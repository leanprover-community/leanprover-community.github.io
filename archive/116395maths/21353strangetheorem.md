---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/21353strangetheorem.html
---

## Stream: [maths](index.html)
### Topic: [strange theorem](21353strangetheorem.html)

---


{% raw %}
#### [ Kenny Lau (Apr 28 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strange%20theorem/near/125808366):
<div class="codehilite"><pre><span></span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="n">A</span> <span class="n">B</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">,</span>
<span class="n">t</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">set</span> <span class="n">α</span><span class="o">),</span>

<span class="n">ht1</span> <span class="o">:</span> <span class="n">t</span> <span class="err">⊆</span> <span class="o">{</span><span class="n">A</span><span class="o">},</span>
<span class="n">ht2</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">finite</span> <span class="n">t</span><span class="o">,</span>
<span class="n">ht3</span> <span class="o">:</span> <span class="err">⋂₀</span> <span class="n">t</span> <span class="err">⊆</span> <span class="n">B</span>
<span class="err">⊢</span> <span class="n">A</span> <span class="err">⊆</span> <span class="n">B</span>
</pre></div>

#### [ Kenny Lau (Apr 28 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strange%20theorem/near/125808368):
<p>claim: you can't prove it without using ht2</p>

#### [ Kenny Lau (Apr 28 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strange%20theorem/near/125808416):
<p>I mean, constructively, of course</p>

#### [ Reid Barton (Apr 28 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strange%20theorem/near/125808417):
<p>I was going to say, I'm pretty sure <em>I</em> can prove it, since I can use LEM <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Kenny Lau (Apr 28 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strange%20theorem/near/125808418):
<p>:D</p>


{% endraw %}
