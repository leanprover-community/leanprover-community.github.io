---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/56347HowexactlydoIdoselfreferentialdefinitions.html
---

## Stream: [new members](index.html)
### Topic: [How exactly do I do self-referential definitions?](56347HowexactlydoIdoselfreferentialdefinitions.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792425):
<p>I'm trying to define a relation R such that <code>for all x, x R (x + 1)</code> and <code>transitive R</code>. Now I know I could probably do this inductively, but I don't want to (because I want the method to apply even if I had, e.g. <code>symmetric R</code>). My instinct was to use a non-constructive definition, like this (I know this is nonsense,  but it's just a sketch of what I want to do):</p>
<div class="codehilite"><pre><span></span><span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span>
<span class="n">noncomputable</span> <span class="n">def</span> <span class="n">double_cosets</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">):</span> <span class="bp">ℤ</span> <span class="bp">→</span> <span class="bp">ℤ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span>
    <span class="k">if</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span> <span class="k">then</span> <span class="n">true</span>
    <span class="n">transitivity</span> <span class="n">double_cosets</span>
</pre></div>


<p>But that doesn't work because </p>
<p>1. <code>true</code> becomes the value of a relation, when I really want that to be the <em>proposition it maps to</em>.<br>
 2. Lean doesn't understand the self-reference.</p>
<p>How do I define it?</p>

#### [ Kenny Lau (Oct 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792448):
<p><code>trans_gen</code></p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792451):
<p>Take the transitive closure of your original relation</p>

#### [ Mario Carneiro (Oct 14 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792454):
<p>isn't this just <code>&lt;</code>?</p>

#### [ Kenny Lau (Oct 14 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792499):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">logic</span><span class="bp">.</span><span class="n">relation</span>

<span class="kn">inductive</span> <span class="n">original</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">r</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">original</span> <span class="n">n</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span>

<span class="n">def</span> <span class="n">R</span> <span class="o">:=</span> <span class="n">relation</span><span class="bp">.</span><span class="n">trans_gen</span> <span class="n">original</span>
</pre></div>

#### [ Kenny Lau (Oct 14 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792504):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I think he wants to experiment instead of creating new things</p>

#### [ Kenny Lau (Oct 14 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792508):
<p>alternatively:</p>

#### [ Kenny Lau (Oct 14 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792509):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">R</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">basic</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">R</span> <span class="n">n</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">trans</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">,</span> <span class="n">R</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">R</span> <span class="n">b</span> <span class="n">c</span> <span class="bp">→</span> <span class="n">R</span> <span class="n">a</span> <span class="n">c</span>
</pre></div>

#### [ Kevin Buzzard (Oct 14 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792548):
<p>Now you can prove things about <code>R</code> by induction</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792549):
<p>It might be interesting to look at the definition of <code>&lt;</code> on the natural numbers at this point</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792556):
<p>Huh, that makes sense. So induction can be used for <em>anything</em> self-referential?</p>

#### [ Kenny Lau (Oct 14 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792557):
<p>not anything.</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792558):
<p>and to tie this up with an earlier conversation, you could even look at the proof that <code>&lt;</code> on <code>nat</code> is decidable, which is an algorithm which, given two nats, spits out which is the smallest.</p>

#### [ Kenny Lau (Oct 14 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792600):
<p>and I would define a function N -&gt; N -&gt; bool instead</p>

#### [ Kenny Lau (Oct 14 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792603):
<p>to emphasize that it is decidable</p>

#### [ Mario Carneiro (Oct 14 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792614):
<p>Whenever you want the "least relation satisfying some properties" that's an inductive predicate</p>

#### [ Kenny Lau (Oct 14 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792618):
<p>and "smallest type closed under some operations" is an inductive type</p>

#### [ Mario Carneiro (Oct 14 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792619):
<p>the relation doesn't have to be decidable, and the proof that it is usually goes by rather different methods than the original</p>

#### [ Mario Carneiro (Oct 14 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792668):
<p>There are interesting examples of nondecidable predicates like "in the span of s" in a group</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792682):
<p>So what is the <code>noncomputable</code> kind of definition for? Isn't my definition non-constructive?</p>

#### [ Kenny Lau (Oct 14 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792728):
<p><code>inductive</code> things are always computable, it's <code>definition</code> that is noncomputable</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792729):
<p>I think it's fine.</p>

#### [ Kenny Lau (Oct 14 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792733):
<p><code>Prop</code> is a strange thing</p>

#### [ Kenny Lau (Oct 14 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792736):
<p>you can have non-decidable propositions</p>

#### [ Kenny Lau (Oct 14 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792738):
<p>that doesn't make it noncomputable</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792740):
<p>No, I get that -- my point is that the definition is non-constructive, isn't it?</p>

#### [ Kenny Lau (Oct 14 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792757):
<p>it isn't</p>

#### [ Kenny Lau (Oct 14 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792760):
<p>you're just defining a proposition</p>

#### [ Mario Carneiro (Oct 14 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792762):
<p>it is not nonconstructive because you aren't actually constructing anything</p>

#### [ Kenny Lau (Oct 14 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792764):
<p>it's like you can write down what it means for a program to halt</p>

#### [ Kenny Lau (Oct 14 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792765):
<p>you just can't evaluate that statement</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20exactly%20do%20I%20do%20self-referential%20definitions%3F/near/135792837):
<p>Yeah, you're right, I got confused.</p>


{% endraw %}
