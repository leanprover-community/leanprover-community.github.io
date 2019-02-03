---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/49995quiversanddiagrams.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [quivers and diagrams](https://leanprover-community.github.io/archive/116395maths/49995quiversanddiagrams.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (May 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937757):
<p>I've got the following snippet</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span> <span class="n">w</span>

<span class="kn">structure</span> <span class="n">quiver</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span>
<span class="o">(</span><span class="n">E</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span>
<span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">E</span> <span class="bp">→</span> <span class="n">V</span><span class="o">)</span>
<span class="o">(</span><span class="n">t</span> <span class="o">:</span> <span class="n">E</span> <span class="bp">→</span> <span class="n">V</span><span class="o">)</span>

<span class="kn">variable</span> <span class="o">{</span><span class="n">Q</span> <span class="o">:</span> <span class="n">quiver</span><span class="o">}</span>

<span class="kn">definition</span> <span class="n">is_a_path</span> <span class="o">:</span> <span class="o">(</span><span class="n">list</span> <span class="n">Q</span><span class="bp">.</span><span class="n">E</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="o">:=</span> <span class="n">true</span>
<span class="bp">|</span> <span class="o">[</span><span class="n">e</span><span class="o">]</span> <span class="o">:=</span> <span class="n">true</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">e₁</span> <span class="bp">::</span> <span class="n">e₂</span> <span class="bp">::</span> <span class="n">es</span><span class="o">)</span> <span class="o">:=</span> <span class="n">Q</span><span class="bp">.</span><span class="n">s</span> <span class="n">e₁</span> <span class="bp">=</span> <span class="n">Q</span><span class="bp">.</span><span class="n">t</span> <span class="n">e₂</span> <span class="bp">∧</span> <span class="n">is_a_path</span> <span class="o">(</span><span class="n">e₂</span> <span class="bp">::</span> <span class="n">es</span><span class="o">)</span>

<span class="kn">structure</span> <span class="n">diagram</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">D</span> <span class="o">:</span> <span class="n">Q</span><span class="bp">.</span><span class="n">V</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">)</span>
<span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">Q</span><span class="bp">.</span><span class="n">E</span><span class="o">),</span> <span class="n">D</span> <span class="o">(</span><span class="n">Q</span><span class="bp">.</span><span class="n">s</span> <span class="n">e</span><span class="o">)</span> <span class="bp">→</span> <span class="n">D</span> <span class="o">(</span><span class="n">Q</span><span class="bp">.</span><span class="n">t</span> <span class="n">e</span><span class="o">))</span>
</pre></div>

#### [ Johan Commelin (May 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937763):
<p>But now I realise that I actually only want to consider finite lists</p>

#### [ Kenny Lau (May 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937765):
<p>why don't you use chain lol</p>

#### [ Kenny Lau (May 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937766):
<p>aha</p>

#### [ Johan Commelin (May 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937771):
<p>How would I best go about that</p>

#### [ Kenny Lau (May 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937772):
<p>but lists are all finite</p>

#### [ Johan Commelin (May 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937774):
<p>Why?</p>

#### [ Kenny Lau (May 01 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937778):
<p>because they're defined inductively</p>

#### [ Kenny Lau (May 01 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937785):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">list</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span>
<span class="n">constructors</span><span class="o">:</span>
<span class="n">list</span><span class="bp">.</span><span class="n">nil</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">T</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">},</span> <span class="n">list</span> <span class="n">T</span>
<span class="n">list</span><span class="bp">.</span><span class="n">cons</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">T</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">},</span> <span class="n">T</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">T</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">T</span>
</pre></div>

#### [ Kenny Lau (May 01 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937788):
<p>and I can inductively prove that they are finite :P</p>

#### [ Johan Commelin (May 01 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937790):
<p>I see</p>

#### [ Johan Commelin (May 01 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937797):
<p>Crazy...</p>

#### [ Kenny Lau (May 01 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937835):
<p>you want lazy lists?</p>

#### [ Kenny Lau (May 01 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937838):
<p>I see you want everything to be lazy</p>

#### [ Kenny Lau (May 01 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937839):
<p>maybe that's why you think they're crazy</p>

#### [ Johan Commelin (May 01 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937844):
<p>Hmm, maybe now I'm happy that they aren't lazy (-;</p>

#### [ Kenny Lau (May 01 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937846):
<p>maybe your ideas are a bit hazy</p>

#### [ Johan Commelin (May 01 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937849):
<p>That.</p>

#### [ Kenny Lau (May 01 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937853):
<p><a href="http://www.rhymezone.com/r/rhyme.cgi?Word=lazy&amp;typeofrhyme=perfect" target="_blank" title="http://www.rhymezone.com/r/rhyme.cgi?Word=lazy&amp;typeofrhyme=perfect">http://www.rhymezone.com/r/rhyme.cgi?Word=lazy&amp;typeofrhyme=perfect</a></p>

#### [ Johan Commelin (May 01 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937857):
<p>That is definitely true. It's one of my defining properties</p>

#### [ Kenny Lau (May 01 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937859):
<p>not many words rhyme with lazy though</p>

#### [ Kenny Lau (May 01 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937861):
<p>so I'm done coz I can't use daisy</p>

#### [ Mario Carneiro (May 01 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937865):
<p>I guess you just did</p>

#### [ Johan Commelin (May 01 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937867):
<p>And you don't wanna look like jay z</p>

#### [ Johan Commelin (May 01 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937919):
<p>Anyway... I am going to try and define the set of all paths, and then try to figure out how to define commutative diagrams</p>

#### [ Kenny Lau (May 01 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937924):
<p>hmm... I would rather use categories to define diagrams</p>

#### [ Kenny Lau (May 01 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937968):
<p><a href="https://github.com/kckennylau/category-theory/blob/master/src/natural_transformation.lean" target="_blank" title="https://github.com/kckennylau/category-theory/blob/master/src/natural_transformation.lean">https://github.com/kckennylau/category-theory/blob/master/src/natural_transformation.lean</a></p>

#### [ Kenny Lau (May 01 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937970):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="n">def</span> <span class="n">product</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">ι</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">ι</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">limit</span> <span class="o">(</span><span class="n">discrete</span> <span class="n">ι</span><span class="o">)</span> <span class="n">C</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_discrete</span> <span class="n">C</span> <span class="n">f</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (May 01 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937973):
<p>product is the limit of the discrete diagram</p>

#### [ Johan Commelin (May 01 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937978):
<p>But that is not how we use them, I think</p>

#### [ Kenny Lau (May 01 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quivers%20and%20diagrams/near/125937981):
<p>is it not?</p>


{% endraw %}
