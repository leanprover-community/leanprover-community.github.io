---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/42445Nantestalkvideo.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Nantes talk video](https://leanprover-community.github.io/archive/113488general/42445Nantestalkvideo.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jan 18 2019 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156362257):
<p>The maths department in Nantes uploaded the video of the Lean talk I gave in November at <a href="http://media.math.sciences.univ-nantes.fr/fr/node/801" target="_blank" title="http://media.math.sciences.univ-nantes.fr/fr/node/801">http://media.math.sciences.univ-nantes.fr/fr/node/801</a> It's in French and the most interesting part was also in my Amsterdam talk, but it could still be useful for people who intend to give talks presenting Lean to mathematicians.</p>

#### [ Kevin Buzzard (Jan 18 2019 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156363763):
<p>Thanks a lot for posting this Patrick. I hope to be finding myself in this sort of position many times in the future.</p>

#### [ Kevin Buzzard (Jan 18 2019 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156386051):
<p>I'm watching this video now. After you typed <code>split</code> in the function proof, how did you get <code>{ sorry}</code> x 2 to appear instantly?</p>

#### [ Patrick Massot (Jan 18 2019 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156386271):
<p>User code snippet</p>

#### [ Patrick Massot (Jan 18 2019 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156386293):
<p>In my <code>~/.config/Code/User/snippets/lean.json</code> I see:</p>

#### [ Patrick Massot (Jan 18 2019 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156386309):
<div class="codehilite"><pre><span></span><span class="s2">&quot;Split&quot;</span><span class="err">:</span> <span class="p">{</span>
        <span class="nt">&quot;prefix&quot;</span><span class="p">:</span> <span class="s2">&quot;split&quot;</span><span class="p">,</span>
        <span class="nt">&quot;body&quot;</span><span class="p">:</span> <span class="p">[</span>
          <span class="s2">&quot;split,&quot;</span><span class="p">,</span>
          <span class="s2">&quot;{ $0&quot;</span><span class="p">,</span>
          <span class="s2">&quot;  sorry },&quot;</span><span class="p">,</span>
          <span class="s2">&quot;{ &quot;</span><span class="p">,</span>
          <span class="s2">&quot;  sorry },&quot;</span>
        <span class="p">],</span>
        <span class="nt">&quot;description&quot;</span><span class="p">:</span> <span class="s2">&quot;Split tactic&quot;</span>
        <span class="p">}</span><span class="err">,</span>
</pre></div>

#### [ Patrick Massot (Jan 18 2019 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156386380):
<p>Do you understand enough French to understand me, or are following only through Lean?</p>

#### [ Johan Commelin (Jan 18 2019 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156386670):
<p>Kevin gave math talks in French!</p>

#### [ Kevin Buzzard (Jan 18 2019 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156387286):
<p>My French is good enough to understand what you're saying. The camera is off now though -- in your group theory proof I can't see the first four or five characters of every line in the VS Code.</p>

#### [ Patrick Massot (Jan 18 2019 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156387316):
<p>I forgot, you can talk about "une groupe"!</p>

#### [ Kevin Buzzard (Jan 18 2019 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156387422):
<p>:-/</p>


{% endraw %}
