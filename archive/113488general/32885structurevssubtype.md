---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/32885structurevssubtype.html
---

## Stream: [general](index.html)
### Topic: [structure vs. subtype](32885structurevssubtype.html)

---


{% raw %}
#### [ Sean Leather (Jul 04 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129073745):
<p>I was wondering why one would choose a <code>structure</code> over a <code>subtype</code> (or vice versa) for <code>finset</code> or any similar construction. It seems like the two are equivalent, but I might be missing something. I don't see an advantage for using a <code>structure</code>. Using a <code>subtype</code> gives you a few existing simple lemmas that you wouldn't have to write, but that's the only advantage I see, and it's relatively minor.</p>

#### [ Kenny Lau (Jul 04 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129073788):
<p>write the appropriate simp lemmas yourself :)</p>

#### [ Sean Leather (Jul 04 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129073806):
<p>Which simp lemmas?</p>

#### [ Kenny Lau (Jul 04 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129073819):
<p>oh, I thought you meant simp lemma by simple lemma</p>

#### [ Sean Leather (Jul 04 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129073879):
<p>No, I meant <code>init/data/subtype/basic.lean</code>, which is all the support I've found for <code>subtype</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">init</span><span class="bp">.</span><span class="n">logic</span>
<span class="kn">open</span> <span class="n">decidable</span>

<span class="n">universes</span> <span class="n">u</span>

<span class="kn">namespace</span> <span class="n">subtype</span>

<span class="n">def</span> <span class="n">exists_of_subtype</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span> <span class="o">{</span> <span class="n">x</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span> <span class="o">}</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span>

<span class="kn">lemma</span> <span class="n">tag_irrelevant</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h1</span> <span class="n">h2</span> <span class="o">:</span> <span class="n">p</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">mk</span> <span class="n">a</span> <span class="n">h1</span> <span class="bp">=</span> <span class="n">mk</span> <span class="n">a</span> <span class="n">h2</span> <span class="o">:=</span>
<span class="n">rfl</span>

<span class="kn">protected</span> <span class="kn">lemma</span> <span class="n">eq</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a1</span> <span class="n">a2</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span><span class="o">}},</span> <span class="n">val</span> <span class="n">a1</span> <span class="bp">=</span> <span class="n">val</span> <span class="n">a2</span> <span class="bp">→</span> <span class="n">a1</span> <span class="bp">=</span> <span class="n">a2</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">h1</span><span class="bp">⟩</span> <span class="bp">⟨.</span><span class="o">(</span><span class="n">x</span><span class="o">),</span> <span class="n">h2</span><span class="bp">⟩</span> <span class="n">rfl</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">eta</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span><span class="o">})</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">p</span> <span class="o">(</span><span class="n">val</span> <span class="n">a</span><span class="o">))</span> <span class="o">:</span> <span class="n">mk</span> <span class="o">(</span><span class="n">val</span> <span class="n">a</span><span class="o">)</span> <span class="n">h</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:=</span>
<span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="n">rfl</span>

<span class="kn">end</span> <span class="n">subtype</span>

<span class="kn">open</span> <span class="n">subtype</span>

<span class="kn">instance</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">p</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">inhabited</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span><span class="o">}</span> <span class="o">:=</span>
<span class="bp">⟨⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩⟩</span>
</pre></div>

#### [ Kenny Lau (Jul 04 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129073887):
<p>erase "simp" from my advice</p>

#### [ Sean Leather (Jul 04 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129073906):
<p>Sure, you could write these yourself, which is why I said the advantage is relatively minor.</p>

#### [ Sean Leather (Jul 04 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129073921):
<p>So, given that, I'm wondering why choose one or the other.</p>

#### [ Kenny Lau (Jul 04 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129073968):
<p>then don't choose :P</p>

#### [ Sean Leather (Jul 04 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074046):
<p>Oh, there are at least a couple other options, of course, depending on what you want: <code>exists</code> and (<code>p</code>)<code>sigma</code>.</p>

#### [ Sean Leather (Jul 04 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074052):
<p>But, still, you have to make choice, assuming you want to do something and not nothing. <span class="emoji emoji-1f61c" title="stuck out tongue winking eye">:stuck_out_tongue_winking_eye:</span></p>

#### [ Kenny Lau (Jul 04 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074056):
<p>write both</p>

#### [ Kenny Lau (Jul 04 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074058):
<p>don't use choice</p>

#### [ Sean Leather (Jul 04 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074066):
<p>Why, Kenny?</p>

#### [ Kenny Lau (Jul 04 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074072):
<p>choice is non-constructive</p>

#### [ Sean Leather (Jul 04 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074115):
<p>It's a decidable choice.</p>

#### [ Sean Leather (Jul 04 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074137):
<p>Note that I'm talking about constructing something. <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Sean Leather (Jul 04 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074146):
<blockquote>
<p>I was wondering why one would choose a <code>structure</code> over a <code>subtype</code> (or vice versa) for <code>finset</code> or <strong>any similar construction</strong>.</p>
</blockquote>

#### [ Kenny Lau (Jul 04 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074207):
<p>never use choice</p>

#### [ Kenny Lau (Jul 04 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074209):
<p>even when it's decidable</p>

#### [ Kenny Lau (Jul 04 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074213):
<p>it's evil</p>

#### [ Johan Commelin (Jul 04 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074217):
<p>Kenny, why did you choose to enroll at Imperial?</p>

#### [ Kenny Lau (Jul 04 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074227):
<p>I didn't choose</p>

#### [ Kenny Lau (Jul 04 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074272):
<p>it just happened</p>

#### [ Johan Commelin (Jul 04 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074283):
<p>Just like you trolling this thread <em>just happens</em></p>

#### [ Kenny Lau (Jul 04 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074288):
<p>lol</p>

#### [ Kevin Buzzard (Jul 04 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074308):
<p>In CS they choose things all the time -- even to the point of breaking symmetry. For example they chose <code>lt</code> to be the important one and define <code>gt</code> through it. Here it doesn't matter which one to choose, but they had to choose one.</p>

#### [ Kevin Buzzard (Jul 04 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074375):
<p>For making more complex structures, it is dawning on me more and more that you do have to make a design decision -- what the "fundamental" way of doing it is -- and then you build other things on top. But I guess you only prove the lemmas for one implementation and then deduce for the others.</p>

#### [ Johan Commelin (Jul 04 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074387):
<p>Kenny, I suggest that it <em>just happens</em> that you read the following article in the Journal of the American Philosophical Association: <a href="https://www.cambridge.org/core/journals/journal-of-the-american-philosophical-association/article/aristotle-on-trolling/540BB557C82186C33BFFB61E35A0B5B6" target="_blank" title="https://www.cambridge.org/core/journals/journal-of-the-american-philosophical-association/article/aristotle-on-trolling/540BB557C82186C33BFFB61E35A0B5B6">https://www.cambridge.org/core/journals/journal-of-the-american-philosophical-association/article/aristotle-on-trolling/540BB557C82186C33BFFB61E35A0B5B6</a></p>

#### [ Johan Commelin (Jul 04 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074435):
<p>Kevin, yes, and then write a solid API.</p>

#### [ Kevin Buzzard (Jul 04 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074441):
<p>So the question is that in any specific case, e.g. fintype, topological spaces, valuations, whatever -- which construction do you make "fundamental"? And this seems to me to be a very delicate question.</p>

#### [ Johan Commelin (Jul 04 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074449):
<p>I am currently trying to grasp the math-API to mixed Hodge modules. There really is a lot of API there. A huge black box behind it, but a solid API.</p>

#### [ Johan Commelin (Jul 04 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074495):
<p>Kevin, if the API is good, the question becomes a bit less delicate, I hope.</p>

#### [ Johan Commelin (Jul 04 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074505):
<p>But lots of parts in mathlib are lacking good API's. (And I myself am very bad at writing good API's.)</p>

#### [ Sean Leather (Jul 04 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074509):
<blockquote>
<p>So the question is that in any specific case, e.g. fintype, topological spaces, valuations, whatever -- which construction do you make "fundamental"? And this seems to me to be a very delicate question.</p>
</blockquote>
<p>For my question, I can only see a slight <em>practical</em> advantage to choosing <code>subtype</code> over <code>structure</code>. I was wondering if there was anything deeper.</p>

#### [ Sean Leather (Jul 04 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074523):
<p>By the way, this <span class="emoji emoji-2b06" title="arrow up">:arrow_up:</span> is me trying to stay on the topic of the thread. <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Sean Leather (Jul 04 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129074585):
<p>Though I'm happy to see other threads branch off on related topics.</p>

#### [ Sean Leather (Jul 09 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs.%20subtype/near/129344097):
<p>The results of my <code>finset</code> <code>structure</code> → <code>subtype</code> experiment: <a href="https://github.com/leanprover/mathlib/pull/183" target="_blank" title="https://github.com/leanprover/mathlib/pull/183">https://github.com/leanprover/mathlib/pull/183</a></p>


{% endraw %}
