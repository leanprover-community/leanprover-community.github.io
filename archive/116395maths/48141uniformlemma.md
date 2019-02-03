---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/48141uniformlemma.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [uniform lemma](https://leanprover-community.github.io/archive/116395maths/48141uniformlemma.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jul 14 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform%20lemma/near/129677243):
<p>Is the following lemma already hidden somewhere in mathlib? Or is it too trivial to be stated? What would be his canonical name?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">uniform_space</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">separation_setoid</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">β</span><span class="o">]</span>

<span class="kn">lemma</span> <span class="n">separation_rel_of_uniform_continuous</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">f</span><span class="o">)</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span>
<span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≈</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≈</span> <span class="n">f</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">assume</span> <span class="bp">_</span> <span class="n">h&#39;</span><span class="o">,</span> <span class="n">h</span> <span class="bp">_</span> <span class="o">(</span><span class="n">H</span> <span class="n">h&#39;</span><span class="o">)</span>
</pre></div>

#### [ Patrick Massot (Jul 14 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform%20lemma/near/129677487):
<p>Same question for the obvious corollary</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">image_eq_of_uniform_continuous_of_separated</span> <span class="o">[</span><span class="n">separated</span> <span class="n">β</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">f</span><span class="o">)</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span>
<span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≈</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">y</span> <span class="o">:=</span>
<span class="n">separated_def</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="k">by</span> <span class="n">apply_instance</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="n">separation_rel_of_uniform_continuous</span> <span class="n">H</span> <span class="n">h</span>
</pre></div>

#### [ Patrick Massot (Jul 14 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform%20lemma/near/129677492):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I know this is Johannes domain, but I'd be interested in your opinion about naming here</p>

#### [ Mario Carneiro (Jul 15 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform%20lemma/near/129684119):
<p>That's a tough one. I don't like the use of the word <code>image</code> in the second one, that connotes <code>''</code> but it doesn't appear in the statement</p>

#### [ Mario Carneiro (Jul 15 2018 at 04:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform%20lemma/near/129684167):
<p>Maybe <code>apply_eq_of_separated</code> for the second?</p>

#### [ Patrick Massot (Jul 15 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform%20lemma/near/129696241):
<p>Ok. It leaves out most of the statement but I don't see how to avoid that when there are so many hypotheses.</p>

#### [ Johannes Hölzl (Jul 15 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform%20lemma/near/129699884):
<p>I think <code>separated_of_uniform_continuous</code> and <code>eq_of_separated_of_uniform_continuous</code> would be also okay.</p>

#### [ Patrick Massot (Jul 15 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform%20lemma/near/129700368):
<p>Thanks. I now use these names since you will have to review a PR containing all this at some point.</p>

#### [ Patrick Massot (Jul 15 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform%20lemma/near/129701065):
<p>Now, for something really weird, I'll try to go read Bourbaki GT in a bar, hoping this will secure me some place to watch the game. It may be too late already.</p>

#### [ Patrick Massot (Jul 15 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform%20lemma/near/129701130):
<p>Maybe  I should point out that my wife and kids are in vacations, so I'm alone at home. Otherwise I wouldn't do that :-)</p>

#### [ Kenny Lau (Jul 15 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform%20lemma/near/129701134):
<p>I think every mathematician should read Bourbaki in a bar</p>

#### [ Patrick Massot (Jul 15 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform%20lemma/near/129710662):
<p>It worked out pretty nicely. Now I know what are the supporting lemmas that I need to prove about completions.</p>

#### [ Patrick Massot (Jul 15 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform%20lemma/near/129710670):
<p>Kenny, reading and doing math in bar is very standard, what was slightly weird was the atmosphere around me. But I was able to mostly work until about 15 minutes before the beginning.</p>


{% endraw %}
