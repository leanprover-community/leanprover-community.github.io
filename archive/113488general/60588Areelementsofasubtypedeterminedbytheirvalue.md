---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/60588Areelementsofasubtypedeterminedbytheirvalue.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Are elements of a subtype determined by their value?](https://leanprover-community.github.io/archive/113488general/60588Areelementsofasubtypedeterminedbytheirvalue.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (May 22 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915156):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">order</span><span class="bp">.</span><span class="n">bounds</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">ordered_group</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">real</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">infinite_sum</span>
<span class="n">noncomputable</span> <span class="n">theory</span>

<span class="kn">definition</span> <span class="n">nnreal</span> <span class="o">:=</span> <span class="o">{</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">//</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">r</span><span class="o">}</span>
<span class="kn">notation</span> <span class="bp">`</span> <span class="n">ℝ</span><span class="bp">≥</span><span class="mi">0</span> <span class="bp">`</span> <span class="o">:=</span> <span class="n">nnreal</span>

<span class="kn">lemma</span> <span class="n">val_eq_val</span> <span class="o">(</span><span class="n">r₁</span> <span class="n">r₂</span> <span class="o">:</span> <span class="n">ℝ</span><span class="bp">≥</span><span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="n">r₁</span> <span class="bp">=</span> <span class="n">r₂</span> <span class="bp">↔</span> <span class="n">r₁</span><span class="bp">.</span><span class="n">val</span> <span class="bp">=</span> <span class="n">r₂</span><span class="bp">.</span><span class="n">val</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>I want to mutter something about proof-irrelevance... and of course I'm working classical</p>

#### [ Kenny Lau (May 22 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915217):
<p>yes. <code>subtype.eq</code></p>

#### [ Johan Commelin (May 22 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915243):
<p>Ok, thanks!</p>

#### [ Johan Commelin (May 22 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915244):
<p>That is helpful</p>

#### [ Johan Commelin (May 22 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915299):
<p>I expected that to be right after the definition of a subtype, but I should have thought of looking for a separate file</p>

#### [ Kenny Lau (May 22 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915302):
<p>mathlib vs core :)</p>

#### [ Johan Commelin (May 22 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915312):
<p>I see</p>

#### [ Kevin Buzzard (May 22 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915354):
<p>All methods have advantages and disadvantages but the reason I'm mentioning this is that it's important to get into the right mindset.</p>

#### [ Kevin Buzzard (May 22 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915355):
<p>The logic is "it's important, so it's probably there already, so I could either plough through subtype.lean, or guess what the theorem might be called and try and find it with the ctrl-space dance, or just ask here"</p>

#### [ Kevin Buzzard (May 22 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915364):
<p>my posts are appearing in random orders</p>

#### [ Kevin Buzzard (May 22 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915428):
<p>I asked here too much in the early days and it took me a while to figure out the other algorithms, it's a sort of "give a man a fish" thing, and of course asking here is a super-helpful resource, but somehow I understand the other possibilities better now and once you understand them you become more powerful.</p>

#### [ Kevin Buzzard (May 22 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915432):
<p>And of course from where you're sitting you have no idea about what will be in core and what will be in mathlib, so sometimes it's just less frustrating to ask</p>

#### [ Kevin Buzzard (May 22 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126915441):
<p>What it took me a long time to understand was "if it's natural, it's already there, and is almost certainly named well"</p>

#### [ Johan Commelin (May 22 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916503):
<p>Ok, so I applied your strategy, and expected there to be a <code>subtype.neq</code>. But it's not there...</p>

#### [ Kenny Lau (May 22 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916508):
<p>someone is being too classical</p>

#### [ Kenny Lau (May 22 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916512):
<p>it's just a <code>rw</code> for the other direction</p>

#### [ Kevin Buzzard (May 22 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916574):
<p>You should add it :-)</p>

#### [ Kevin Buzzard (May 22 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916577):
<p>subtype.eq is an iff</p>

#### [ Johan Commelin (May 22 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916584):
<p>Hmm, so I should <code>rw</code>, instead of <code>apply</code>...?</p>

#### [ Mario Carneiro (May 22 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916595):
<p>There aren't a lot of negated theorems like that, since <code>mt</code> is literally two characters and turns any A -&gt; B into \not B -&gt; \not A</p>

#### [ Kenny Lau (May 22 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916596):
<p><code>congr_arg subtype.val</code>, whatever</p>

#### [ Kevin Buzzard (May 22 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916652):
<p>If H is A &lt;-&gt; B then H.1 is A -&gt; B and H.2 is B -&gt; A, if this helps</p>

#### [ Kevin Buzzard (May 22 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916657):
<p>(this is because the _definition_ of &lt;-&gt; is what you think it is)</p>

#### [ Johan Commelin (May 22 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916672):
<p>Wait, how do I use <code>mt</code>?</p>

#### [ Kevin Buzzard (May 22 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916716):
<p><code>#print mt</code></p>

#### [ Johan Commelin (May 22 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916718):
<p>Hmmz, I see</p>

#### [ Kevin Buzzard (May 22 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916720):
<p>or <code>#check mt</code> if you just want to see the type</p>

#### [ Kevin Buzzard (May 22 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916727):
<p>Some questions of the form "how do I use X" are really "what is its type?" and some are "what is its definition?"</p>

#### [ Johan Commelin (May 22 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916728):
<p>Stuff isn't typechecking over here... I'll have to work a bit</p>

#### [ Kevin Buzzard (May 22 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916729):
<p>so you use <code>#check</code> or <code>#print</code></p>

#### [ Kevin Buzzard (May 22 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916730):
<p>That's another thing I learnt -- when I get errors now I read them carefully</p>

#### [ Kevin Buzzard (May 22 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916733):
<p>because they tell you exactly what you have got wrong</p>

#### [ Johan Commelin (May 22 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126916842):
<p>Ok, so my subtype.eq is not an iff, it's something from core saying</p>
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="kn">lemma</span> <span class="n">eq</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a1</span> <span class="n">a2</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span><span class="o">}},</span> <span class="n">val</span> <span class="n">a1</span> <span class="bp">=</span> <span class="n">val</span> <span class="n">a2</span> <span class="bp">→</span> <span class="n">a1</span> <span class="bp">=</span> <span class="n">a2</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">h1</span><span class="bp">⟩</span> <span class="bp">⟨.</span><span class="o">(</span><span class="n">x</span><span class="o">),</span> <span class="n">h2</span><span class="bp">⟩</span> <span class="n">rfl</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Kevin Buzzard (May 22 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126921269):
<p>OK great -- I just assumed it was an iff from something someone said earlier</p>

#### [ Kevin Buzzard (May 22 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Are%20elements%20of%20a%20subtype%20determined%20by%20their%20value%3F/near/126921310):
<p>I guess it's protected because if you open subtype then all of a sudden you have clobbered the definition of eq</p>


{% endraw %}
