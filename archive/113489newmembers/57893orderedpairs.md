---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/57893orderedpairs.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [ordered pairs](https://leanprover-community.github.io/archive/113489newmembers/57893orderedpairs.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Oct 19 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077221):
<p>I'm defining a subset of the Cartesian product of two types, specifically: </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">graph</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span> <span class="bp">×</span> <span class="n">Y</span> <span class="o">:=</span>
    <span class="o">{(</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="bp">|</span> <span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">}</span>
</pre></div>


<p>(<code>f</code> is a function, <code>x</code> has not been separately defined) What's the right notation for this (the ordered pairs, and also the set builder itself)?</p>

#### [ Kenny Lau (Oct 19 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077285):
<p>what do you mean by "right notation"?</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 19 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077288):
<p>A notation that works in Lean.</p>

#### [ Kenny Lau (Oct 19 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077300):
<p>do you mean <code>set (X × Y)</code>?</p>

#### [ Kenny Lau (Oct 19 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077303):
<p>oh</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 19 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077304):
<p>No, I mean for the ordered pairs.</p>

#### [ Kenny Lau (Oct 19 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077370):
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span>
<span class="n">def</span> <span class="n">graph</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">X</span> <span class="bp">×</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">z</span> <span class="bp">|</span> <span class="n">z</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">z</span><span class="bp">.</span><span class="mi">1</span> <span class="o">}</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Oct 19 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077386):
<p>Ah.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 19 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077387):
<p>Thanks.</p>

#### [ Kevin Buzzard (Oct 19 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077411):
<p>It's kind of annoying that you can't write <code>{⟨x,y⟩ : X × Y | y = f x}</code></p>

#### [ Kenny Lau (Oct 19 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077469):
<p>you can't define that in ZFC either</p>

#### [ Kenny Lau (Oct 19 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077470):
<p>you need to use specification and an existential</p>

#### [ Kevin Buzzard (Oct 19 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077487):
<p>I guess you could use <code>set.image</code> or <code>set.range</code>, whatever it's called</p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077650):
<p><code>def graph' : set (X × Y) := set.range (λ x, ⟨x,f x⟩) </code></p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077661):
<p>(after <code>import data.set.basic</code>)</p>

#### [ Kenny Lau (Oct 19 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077723):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">lattice</span>
<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span>
<span class="n">def</span> <span class="n">graph</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">X</span> <span class="bp">×</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:=</span>
<span class="err">⨆</span> <span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span> <span class="o">{(</span><span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span><span class="o">)}</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077827):
<p>What's <code>⨆</code>?</p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077886):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span>

<span class="n">def</span> <span class="n">graph</span>  <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">X</span> <span class="bp">×</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{</span><span class="n">z</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">×</span> <span class="n">Y</span> <span class="bp">|</span> <span class="n">z</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">z</span><span class="bp">.</span><span class="mi">1</span><span class="o">}</span>

<span class="n">def</span> <span class="n">graph&#39;</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">X</span> <span class="bp">×</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span><span class="n">f</span> <span class="n">x</span><span class="bp">⟩</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">graph</span> <span class="bp">=</span> <span class="n">graph&#39;</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kenny Lau (Oct 19 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077894):
<p><code>set X</code> is a complete lattice</p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077913):
<p>Abhi: <code>⨆</code> is notation so you can start with <code>#print notation ⨆</code></p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077923):
<p>but if you don't want to go down the lattice rabbithole you could try my homework :-)</p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077997):
<p>I'd be able to do the homework myself if I knew how to prove <code>A = B iff B = A</code> :-/</p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136077999):
<p><code>eq.symm</code> only goes one way</p>

#### [ Kenny Lau (Oct 19 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078000):
<p>eq_comm</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078007):
<p>I'm not sure how to interpret the results of #print notation. All I get is <code>'⨆':1024 binders ',':0 (scoped 0) := #0</code> What's a binder?</p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078057):
<p>oh oops</p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078060):
<p>yes that is impossible to interpret</p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078085):
<p>A binder is something like forall or exists or lambda I think</p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078094):
<p>Kenny is using <code>⨆</code> in the same sort of way that one would use those things.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078137):
<p>Yeah, I can tell it's something like forall, but I'm not sure what the difference is.</p>

#### [ Mario Carneiro (Oct 19 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078141):
<p>I think you can click on the sup to go to definition</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078143):
<p>I get "no definition found"</p>

#### [ Mario Carneiro (Oct 19 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078144):
<p>It's the analogue of <code>\bigcup</code> for lattices</p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078146):
<p>It's in <code>order/complete_lattice.lean</code></p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078149):
<p><code>notation </code>⨆<code> binders </code>, <code> r:(scoped f, supr f) := r</code></p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078169):
<p>I taught Abhi about bigcup today in lectures :-)</p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078211):
<p>Glad to see my lectures are coming in handy in his day to day life</p>

#### [ Mario Carneiro (Oct 19 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078237):
<p>"day to day life"</p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078244):
<p>I don't understand that notation line at all. I think notation in Lean is somehow evil; most of it is fine and then there are some weird hacks which I don't get at all. The key point is <code>supr</code> somehow, and then everything else is some notation mantra I guess</p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078294):
<p><code>def supr [complete_lattice α] (s : ι → α) : α := Sup {a : α | ∃i : ι, a = s i}</code></p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078339):
<p>so <code>supr s</code> is the supremum of the range of <code>s</code></p>

#### [ Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078511):
<p>Btw I'm trying <code>def p1 (g : graph) : X := g.1</code> based on the earlier definition of <code>graph</code>, but it doesn't work:</p>
<div class="codehilite"><pre><span></span><span class="n">invalid</span> <span class="n">field</span> <span class="kn">notation</span><span class="o">,</span> <span class="n">type</span> <span class="n">is</span> <span class="n">not</span> <span class="n">of</span> <span class="n">the</span> <span class="n">form</span> <span class="o">(</span><span class="n">C</span> <span class="bp">...</span><span class="o">)</span> <span class="n">where</span> <span class="n">C</span> <span class="n">is</span> <span class="n">a</span> <span class="kn">constant</span>
  <span class="n">g</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="err">⁇</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="kn">universe</span> <span class="n">u</span>
<span class="kn">variable</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
<span class="kn">variable</span> <span class="o">{</span><span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
<span class="kn">variable</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">}</span>
<span class="n">def</span> <span class="n">graph</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">X</span> <span class="bp">×</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">g</span> <span class="bp">|</span> <span class="n">g</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">g</span><span class="bp">.</span><span class="mi">1</span> <span class="o">}</span>
<span class="n">def</span> <span class="n">p1</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">graph</span><span class="o">)</span> <span class="o">:</span> <span class="n">X</span> <span class="o">:=</span> <span class="n">g</span><span class="bp">.</span><span class="mi">1</span>
</pre></div>


<p>I guess part of the problem is that <code>G</code> is not a type -- I tried coercing it as <code>↑G</code>, but that just produces more errors.</p>

#### [ Reid Barton (Oct 19 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078535):
<p>I think the bigger problem is Lean doesn't know what you want to take the graph of</p>

#### [ Mario Carneiro (Oct 19 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078541):
<p>I can't make sense of that definition</p>

#### [ Reid Barton (Oct 19 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078543):
<p>I would make <code>f</code> an explicit argument and then pass it in <code>p1</code></p>

#### [ Mario Carneiro (Oct 19 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078594):
<p>what does <code>g : graph</code> mean?</p>

#### [ Mario Carneiro (Oct 19 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078596):
<p>it's not a type</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078618):
<blockquote>
<p>what does <code>g : graph</code> mean?</p>
</blockquote>
<p>Yeah, I realise that, but I want to show (separately from the definition) it's a bijection from <code>graph</code> to <code>X</code>.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078677):
<blockquote>
<p>I would make <code>f</code> an explicit argument and then pass it in <code>p1</code></p>
</blockquote>
<p>Indeed that removes the first error. How, though?</p>

#### [ Mario Carneiro (Oct 19 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078690):
<p>Keep in mind that <code>graph f</code>is not a type either, it's a set</p>

#### [ Mario Carneiro (Oct 19 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078699):
<p>lean knows to coerce from a set to a type, but maybe you want the subtype instead?</p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078706):
<p>a set is a term not a Type Abhi. Did you come to my lecture today?</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078759):
<blockquote>
<p>a set is a term not a Type Abhi. Did you come to my lecture today?</p>
</blockquote>
<p>I realise that -- but how else would I later show it to be a bijection from graph to X?</p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078760):
<p>If <code>X</code> is a type and <code>p : X -&gt; Prop</code> then in Lean there are two very different ways to express what in set theory is just "the subset of X consisting of elements <code>a</code> for which <code>p a</code> is true"</p>

#### [ Kenny Lau (Oct 19 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078763):
<p>it did took me some time to figure out that Kevin wants us to prove that the two big big functions <code>graph</code> and <code>graph'</code> are equal</p>

#### [ Kenny Lau (Oct 19 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078770):
<p>so you should start with <code>ext X Y f</code></p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078772):
<p>One is the set <code>{x : X | p x}</code> and one is the subtype <code>{x : X // p x}</code></p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078800):
<p>I am in the middle of showing my <code>graph</code> is Kenny's <code>supr</code> thing</p>

#### [ Kenny Lau (Oct 19 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078861):
<p>I bet <code>example : graph = graph' :=</code> isn't what Kevin wanted us to prove</p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078867):
<p>I proved that using <code>eq.comm</code></p>

#### [ Kenny Lau (Oct 19 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136078880):
<p><code>example : graph X Y f = graph' X Y f :=</code></p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079017):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">lattice</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span>

<span class="n">def</span> <span class="n">graph</span>  <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">X</span> <span class="bp">×</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{</span><span class="n">z</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">×</span> <span class="n">Y</span> <span class="bp">|</span> <span class="n">z</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">z</span><span class="bp">.</span><span class="mi">1</span><span class="o">}</span>

<span class="n">def</span> <span class="n">graph&#39;</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">X</span> <span class="bp">×</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span><span class="n">f</span> <span class="n">x</span><span class="bp">⟩</span><span class="o">)</span>

<span class="n">def</span> <span class="n">graph&#39;&#39;</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">X</span> <span class="bp">×</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:=</span> <span class="err">⨆</span> <span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span> <span class="o">{(</span><span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span><span class="o">)}</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">graph</span> <span class="bp">=</span> <span class="n">graph&#39;</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">graph</span> <span class="bp">=</span> <span class="n">graph&#39;&#39;</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>I did them both :-)</p>

#### [ Kevin Buzzard (Oct 19 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079020):
<p>I am not proud of the second one though.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079102):
<p>Re:the bijection, I <em>can</em> write <code>def p1 (g : graph f) := g.1</code>(still defining <code>graph</code> as a set because subtype gives me even more errors), but then <code>p1</code> for some reason has the wrong type. Apparently <code>g.1</code> isn't processed correctly (it still has type <code>X × Y</code> and not <code>X</code>).</p>

#### [ Mario Carneiro (Oct 19 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079129):
<p>that has to do with the fact that it is a subtype</p>

#### [ Mario Carneiro (Oct 19 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079183):
<p><code>g</code> is a pair of an element of <code>X x Y</code> and a proof that this element satisfies <code>z.2 = f z.1</code></p>

#### [ Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079184):
<p>Is the notation for ordered pairs different for subtypes?</p>

#### [ Mario Carneiro (Oct 19 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079190):
<p>so the X value is <code>g.1.1</code></p>

#### [ Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079202):
<p>That works, but I don't get why.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079207):
<p>(deleted)</p>

#### [ Reid Barton (Oct 19 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079216):
<p>or <code>g.val.fst</code></p>

#### [ Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079275):
<p>Ok, I get the argument, but I'm not sure why it's defined that way (to include a proof).</p>

#### [ Reid Barton (Oct 19 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079360):
<p>If you didn't have to provide a proof when constructing a value of the subtype, then it would just be the same as the entire original type.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 19 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079477):
<p>Why does the same convention not apply to sets?</p>

#### [ Reid Barton (Oct 19 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/ordered%20pairs/near/136079571):
<p>I don't really understand the question. A set is not a type; perhaps that's the answer</p>


{% endraw %}
