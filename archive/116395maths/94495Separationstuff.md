---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/94495Separationstuff.html
---

## Stream: [maths](index.html)
### Topic: [Separation stuff](94495Separationstuff.html)

---


{% raw %}
#### [ Patrick Massot (Sep 19 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134237694):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> I'm working on uniform spaces again, and I have a couple of question. </p>
<ul>
<li>First, at <a href="https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_space.lean#L638-L640" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_space.lean#L638-L640">https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_space.lean#L638-L640</a> the comment mentions two possible definitions of T1 spaces. Am I right to think the equivalence of those definitions is not in mathlib?</li>
<li>Bourbaki defines separated uniform spaces as uniform spaces whose underlying topology is T2. You define them in terms of the separation relation, and prove the underlying topological space is T2. But you don't prove the converse implication, do you?</li>
<li>When trying to prove the converse implication on paper, I get that T1 underlying topology is enough. Is this fishy? Or is it only that topologies coming from uniform structures are special and T1 implies T2 (and regular)?</li>
</ul>

#### [ Reid Barton (Sep 19 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134239354):
<p>T1 implies T2 for uniform spaces should be the same epsilon/2 as shows metric spaces are T2</p>

#### [ Reid Barton (Sep 19 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134239449):
<p>Uh, on my phone and apparently can't form complete sentences but I guess you understand what I mean.</p>

#### [ Patrick Massot (Sep 19 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134239563):
<p>Indeed it looks very plausible, but I wanted to check with our local expert before starting to Lean it</p>

#### [ Patrick Massot (Sep 19 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134240553):
<p>I now have a really detailed paper proof of the fact that the group uniform structure on the completion of a group is the same as the completion of the group uniform structure. I have about 15 lemmas to state and prove in Lean. I'm really afraid because lots of them involve different uniform structures on the same type, and I don't know how to fight the type class resolution system here.</p>

#### [ Patrick Massot (Sep 19 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134253310):
<p>Ok, I decided to start with a lemma which is independent of all the group theory stuff and openly involves different uniform structures on the same type. </p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">uniform_space</span>
<span class="kn">open</span> <span class="n">set</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>

<span class="kn">lemma</span> <span class="n">uniform_continuous_id_of_emb</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">u</span> <span class="n">u&#39;</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">top</span> <span class="o">:</span> <span class="n">u</span><span class="bp">.</span><span class="n">to_topological_space</span> <span class="bp">=</span> <span class="n">u&#39;</span><span class="bp">.</span><span class="n">to_topological_space</span><span class="o">)</span>
  <span class="o">{</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">ue</span> <span class="o">:</span> <span class="bp">@</span><span class="n">uniform_embedding</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">u</span> <span class="n">e</span><span class="o">)</span> <span class="o">(</span><span class="n">dense</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">closure</span> <span class="o">(</span><span class="n">range</span> <span class="n">e</span><span class="o">))</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">@</span><span class="n">uniform_continuous</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">u&#39;</span> <span class="n">e</span><span class="o">)</span> <span class="o">:</span>  <span class="n">u</span> <span class="bp">≤</span> <span class="n">u&#39;</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">let</span> <span class="n">e₀</span> <span class="o">:=</span> <span class="o">(</span><span class="n">ue</span><span class="bp">.</span><span class="n">dense_embedding</span> <span class="n">dense</span><span class="o">)</span><span class="bp">.</span><span class="n">extend</span> <span class="n">e</span><span class="o">,</span>

  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p>As expected, lots of @/_ flying around. First surprise: how does Lean accepts the <code>dense</code> hypothesis? Where does it get a topology on beta? I was expecting to need to need @ here, pick at random from <code>u</code> to <code>u'</code> and then use the <code>topo</code> hypothesis in the proof. And then Lean complains when I define <code>e₀</code>: <code>synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized u' inferred u</code>. Here I want to use uniform structure <code>u</code>. How can I proceed?</p>

#### [ Patrick Massot (Sep 19 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259187):
<p>Any hint about this?</p>

#### [ Johannes Hölzl (Sep 19 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259425):
<p>first observation: in <code>dense</code>, the type class instances find somehow <code>u'</code></p>

#### [ Johannes Hölzl (Sep 19 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259461):
<p>For some reasons it also uses non-type class parameters...</p>

#### [ Patrick Massot (Sep 19 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259548):
<p>Yes, this is what confuses me</p>

#### [ Johannes Hölzl (Sep 19 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259575):
<p>the type class inference will use <code>u</code> if you swap <code>u'</code> and <code>u</code>. then <code>u</code> will be used in <code>dense</code>, and <code>e₀</code> works</p>

#### [ Johannes Hölzl (Sep 19 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259585):
<p>but this is surely not reliable.</p>

#### [ Patrick Massot (Sep 19 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259601):
<p>Of course square brackets are meant to indicate how these arguments will be supplied when applying the lemma. But somehow I thought they also indicated what to put in the type class system for immediate use in following arguments</p>

#### [ Patrick Massot (Sep 19 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259626):
<p>I thought about swapping, but I wanted a robust solution</p>

#### [ Patrick Massot (Sep 19 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259705):
<p>And , while you're here, this thread starts with three questions for you...</p>

#### [ Johannes Hölzl (Sep 19 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259709):
<p>to have it robust you need to use the <code>@...</code> notation</p>

#### [ Patrick Massot (Sep 19 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259913):
<p>My son requires me, you have some extra thinking time <span class="emoji emoji-263a" title="smile">:smile:</span></p>

#### [ Johannes Hölzl (Sep 19 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259939):
<p>1) heh, the comment is the wrong way around. All we have specifically for T1 is the three theorem below the <code>class</code>.  So AFAIR: no this equivalence is not in mathlib.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259948):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">uniform_space</span>
<span class="kn">open</span> <span class="n">set</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>

<span class="c1">--set_option trace.class_instances true</span>
<span class="kn">lemma</span> <span class="n">uniform_continuous_id_of_emb</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">β</span><span class="o">)</span>
 <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">u&#39;</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">β</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="o">,</span> <span class="c1">-- works??</span>
<span class="c1">--  have : u = u&#39; := rfl, -- fails??</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Sep 19 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259975):
<p>this is horrible</p>

#### [ Johannes Hölzl (Sep 19 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260041):
<p>2) no the converse is not proved</p>

#### [ Johannes Hölzl (Sep 19 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260187):
<p>3) Reid's comment makes sense to me.</p>

#### [ Chris Hughes (Sep 19 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260195):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> you used have instead of let.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260216):
<p>thank goodness for that</p>

#### [ Kevin Buzzard (Sep 19 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260225):
<p>and not for the first time</p>

#### [ Johannes Hölzl (Sep 19 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260341):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>  do you work with: <strong>I. M. James: Topologies and Uniformities</strong>? This is what I used to formalize most of uniform spaces.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260347):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">uniform_space</span>
<span class="kn">open</span> <span class="n">set</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>

<span class="kn">lemma</span> <span class="n">uniform_continuous_id_of_emb</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">u</span> <span class="n">u&#39;</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">β</span><span class="o">)</span>
 <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">let</span> <span class="n">βtop</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">β</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="o">,</span> <span class="c1">-- ??</span>
  <span class="k">have</span> <span class="o">:</span> <span class="n">βtop</span> <span class="bp">=</span> <span class="bp">@</span><span class="n">uniform_space</span><span class="bp">.</span><span class="n">to_topological_space</span> <span class="n">β</span> <span class="n">u&#39;</span> <span class="o">:=</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Sep 19 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260400):
<p>So as Johannes says, type class inference picks up <code>u'</code> and it's not clear why</p>

#### [ Kevin Buzzard (Sep 19 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260910):
<blockquote>
<p>How can I proceed?</p>
</blockquote>
<p>Well we now see the problem; type class inference succeeds when it shouldn't, so...</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">uniform_space</span>
<span class="kn">open</span> <span class="n">set</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>

<span class="kn">lemma</span> <span class="n">uniform_continuous_id_of_emb</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">u</span> <span class="n">u&#39;</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">top</span> <span class="o">:</span> <span class="n">u</span><span class="bp">.</span><span class="n">to_topological_space</span> <span class="bp">=</span> <span class="n">u&#39;</span><span class="bp">.</span><span class="n">to_topological_space</span><span class="o">)</span>
  <span class="o">{</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">ue</span> <span class="o">:</span> <span class="bp">@</span><span class="n">uniform_embedding</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">u</span> <span class="n">e</span><span class="o">)</span> <span class="o">(</span><span class="n">dense</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="bp">@</span><span class="n">closure</span> <span class="n">β</span> <span class="o">(</span><span class="n">u</span><span class="bp">.</span><span class="n">to_topological_space</span><span class="o">)</span> <span class="o">(</span><span class="n">range</span> <span class="n">e</span><span class="o">))</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">@</span><span class="n">uniform_continuous</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">u&#39;</span> <span class="n">e</span><span class="o">)</span> <span class="o">:</span>  <span class="n">u</span> <span class="bp">≤</span> <span class="n">u&#39;</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">let</span> <span class="n">e₀</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">dense_embedding</span><span class="bp">.</span><span class="n">extend</span> <span class="bp">_</span> <span class="n">β</span> <span class="n">β</span> <span class="bp">_</span> <span class="o">(</span><span class="n">u</span><span class="bp">.</span><span class="n">to_topological_space</span><span class="o">)</span> <span class="n">e</span> <span class="o">(</span><span class="n">u&#39;</span><span class="bp">.</span><span class="n">to_topological_space</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">uniform_embedding</span><span class="bp">.</span><span class="n">dense_embedding</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">u</span> <span class="bp">_</span> <span class="n">ue</span> <span class="n">dense</span><span class="o">)</span> <span class="n">e</span><span class="o">,</span>

  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p>I don't know what you're complaining about :-)</p>

#### [ Johan Commelin (Sep 19 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260981):
<p>Did you steel Scott's monitor?</p>

#### [ Johan Commelin (Sep 19 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260988):
<p>Those lines are way too long. <span class="emoji emoji-1f923" title="rolling on the floor laughing">:rolling_on_the_floor_laughing:</span></p>

#### [ Kevin Buzzard (Sep 19 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260990):
<p>Here is a possible workaround: use beta and gamma with an equiv, let u be the uniform structure on beta and u' on gamma</p>

#### [ Kevin Buzzard (Sep 19 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261001):
<blockquote>
<p>Those lines are way too long. <span class="emoji emoji-1f923" title="rolling on the floor laughing">:rolling_on_the_floor_laughing:</span></p>
</blockquote>
<p>I even halved the longest one!</p>

#### [ Kevin Buzzard (Sep 19 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261022):
<p>and then you won't get the problems</p>

#### [ Kevin Buzzard (Sep 19 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261028):
<p>and you can just push forward and pull back the uniformities.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261100):
<p>This might actually work. But of course the question still remains as to how type class inference is stealing your uniformities. This is very funny. It's <em>exactly</em> the opposite of the complaint most of my student have -- "I can see it in the local context, how come Lean doesn't know why R is a ring?"</p>

#### [ Johannes Hölzl (Sep 19 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261241):
<p>ah yes, when you move the parameters <code>u</code> and <code>u'</code> to the right side of <code>:</code>, then it doesn't work anymore:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">uniform_continuous_id_of_emb</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span>
  <span class="bp">∀</span><span class="o">(</span><span class="n">u</span> <span class="n">u&#39;</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">top</span> <span class="o">:</span> <span class="n">u</span><span class="bp">.</span><span class="n">to_topological_space</span> <span class="bp">=</span> <span class="n">u&#39;</span><span class="bp">.</span><span class="n">to_topological_space</span><span class="o">)</span>
  <span class="o">{</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">ue</span> <span class="o">:</span> <span class="bp">@</span><span class="n">uniform_embedding</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">u</span> <span class="n">e</span><span class="o">)</span>
  <span class="o">(</span><span class="n">dense</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">closure</span> <span class="o">(</span><span class="n">range</span> <span class="n">e</span><span class="o">))</span> <span class="c1">-- fails here</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">@</span><span class="n">uniform_continuous</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">u&#39;</span> <span class="n">e</span><span class="o">),</span> <span class="n">u</span> <span class="bp">≤</span> <span class="n">u&#39;</span> <span class="o">:=</span> <span class="bp">...</span>
</pre></div>

#### [ Kevin Buzzard (Sep 19 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261338):
<p>So when Leo said only stuff to the left of the colon could be used for type class inference, I didn't realise he meant that even stuff which we didn't want to use would get used...</p>

#### [ Kevin Buzzard (Sep 19 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261347):
<p>Is this just for uniform spaces or does everything do this?</p>

#### [ Johannes Hölzl (Sep 19 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261357):
<p>I guess everything?!</p>

#### [ Johannes Hölzl (Sep 19 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261372):
<p>maybe only things which are marked as <code>@[class]</code>?</p>

#### [ Kevin Buzzard (Sep 19 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261392):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">test</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">ring</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">let</span> <span class="n">v</span> <span class="o">:</span> <span class="n">ring</span> <span class="n">α</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="o">,</span>
  <span class="c1">-- who knew that this worked??</span>
  <span class="k">have</span> <span class="o">:</span> <span class="n">u</span> <span class="bp">=</span> <span class="n">v</span> <span class="o">:=</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Sep 19 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261407):
<p>Is this a bug??</p>

#### [ Mario Carneiro (Sep 19 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261471):
<p>I'm confused, why is this a surprise</p>

#### [ Mario Carneiro (Sep 19 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261498):
<p>you asked for an instance, it found one</p>

#### [ Kevin Buzzard (Sep 19 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261505):
<p>Patrick, even though Johannes has pointed out a fix, the more I think about the gamma trick the more I think you should consider it seriously. Then you can just use type class inference for beta with u and gamma with u', and deduce the actual thing you want afterwards with a minimal amount of <code>@</code></p>

#### [ Kevin Buzzard (Sep 19 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261512):
<p>I just had absolutely no idea that it would look there</p>

#### [ Mario Carneiro (Sep 19 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261523):
<p>isn't that where it normally looks?</p>

#### [ Kevin Buzzard (Sep 19 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261535):
<p>I thought there was the square bracket stuff and the round bracket stuff</p>

#### [ Kevin Buzzard (Sep 19 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261541):
<p>and it only looked in the square bracket stuff</p>

#### [ Mario Carneiro (Sep 19 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261591):
<p>Ah, I see. The square bracket only affects users of the theorem, it doesn't matter what you mark it when it's in the context</p>

#### [ Mario Carneiro (Sep 19 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261614):
<p>the only thing that matters inside the theorem is whether the head constant is a <code>@[class]</code></p>

#### [ Kevin Buzzard (Sep 19 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261627):
<p>I see!</p>

#### [ Johannes Hölzl (Sep 19 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261666):
<p>Hm, this is also news to me!</p>

#### [ Kevin Buzzard (Sep 19 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261709):
<p>In which case Patrick I think this is an even bigger indication that you should just work with two different types and maps between them, and in the application make the types the same</p>

#### [ Kevin Buzzard (Sep 19 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261780):
<p>Hopefully this solves some blockages higher up the chain of problems as well. I didn't know things worked like this, and presumably Patrick didn't either -- but I do remember him saying that he could not actually solve some problems with type classes because he could not direct his instances in the right direction. This will hopefully clear a lot of stuff up.</p>

#### [ Johannes Hölzl (Sep 19 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261857):
<p>I also think it is a good idea to use two types and a uniform equivalence between them. The annoying this is: this may force you to prove for a lot of constants, that they are invariant under equivalences</p>

#### [ Kevin Buzzard (Sep 19 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261869):
<p>I guess the reason many users didn't notice this is simply because it is very rare to actually have two terms of type <code>foo X</code> with <code>foo</code> a class, which you actually want to be distinct; usually users are wrestling to prove that they are the equal, not the other way around.</p>

#### [ Johannes Hölzl (Sep 19 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261902):
<p>yes, type classes work so well, exactly for this reason: if you assume two different structures, you usually have two different types</p>

#### [ Kevin Buzzard (Sep 19 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261948):
<blockquote>
<p>I also think it is a good idea to use two types and a uniform equivalence between them. The annoying this is: this may force you to prove for a lot of constants, that they are invariant under equivalences</p>
</blockquote>
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> This is back to transport de structure. Deligne emphasized this concept in his IAS lecture last week.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134262036):
<p>Patrick is about to need the fact that if he has <code>h : equiv X Y</code> and a topological space structure on X, then all topology-like theorems he proves for X should have an analogue for Y obtained by mapping and co-mapping along h.</p>

#### [ Johannes Hölzl (Sep 19 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134262303):
<p>we need to extensions of <code>equiv</code>: <code>continuous_equiv</code> and <code>uniform_equiv</code>. We also assume a topological structure on <code>Y</code> (it may be the one induced by <code>h</code>, but this shouldn't be necessary def-equal)</p>

#### [ Mario Carneiro (Sep 19 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134262810):
<p>isn't <code>continuous_equiv</code> just <code>homeo</code>?</p>

#### [ Johannes Hölzl (Sep 19 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134262868):
<p>yes</p>

#### [ Kevin Buzzard (Sep 19 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134263238):
<p>I feel like we have taken a big step forward here though. My solution with long lines would have been hell and Patrick was complaining some time ago that he could not control his instances. I realised the other reason that this phenomenon was not well known -- if you have a term whose type is a class, 99% of the time you put it in square brackets in the statement of a theorem or definition</p>

#### [ Patrick Massot (Sep 19 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134263651):
<p>I'm back. Thanks everybody for your work on this.</p>

#### [ Patrick Massot (Sep 19 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134263681):
<p>I'm not sure I'm buying the two types solutions. The problem is that I'm not intersted in this lemma in isolation, it's a tiny step in a much bigger proof</p>

#### [ Patrick Massot (Sep 19 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134263692):
<p>So I'll actually need to apply this lemma</p>

#### [ Simon Hudon (Sep 19 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134264311):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>: <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> keeps pointing out that <code>transport</code> overlaps with his <code>transfer</code> machinery. I think it would be worth checking if <code>transfer</code> solves your problems right out of the box.</p>

#### [ Johannes Hölzl (Sep 19 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134264380):
<p>it doesn't solve them right out of the box. It still requires quite some infrastructure. But I think it is less work to extend <code>transfer</code> than to implement a <code>transport</code></p>

#### [ Kevin Buzzard (Sep 19 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134265117):
<p>I would like to hear much more about what is going on here. I don't know what either of these words are. Are they tactics? I remember having a lot of fun working towards <code>transport</code>. Maybe we have an actual use case here. Presumably Johannes in his message above has pinpointed exactly what we need in this situation</p>

#### [ Kevin Buzzard (Sep 19 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134265223):
<p>Patrick if you try and prove the lemma using just one beta then you have an @ nightmare. If you prove it using beta and gamma then you have a different problem which might be easily solvable and furthermore your lemma will be a more general result. You can get the lemma you want by applying the more general one in the case beta = gamma and then you are only in @ hell for a few lines</p>

#### [ Patrick Massot (Sep 19 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134265278):
<p>I think this is a very important topic, so I'll probably try a couple of solutions</p>

#### [ Patrick Massot (Sep 19 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134265294):
<p>I still need to know how I can use my "same topology hypothesis" to deduce that the range of e is dense for for topologies</p>

#### [ Kevin Buzzard (Sep 19 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134265322):
<p>This is very much like how transport de structure works in Galois theory. You first do it with an isomorphism X = Y and then apply it with X=Y but the isomorphism not equal to the identity and you deduce something which might look like a nontrivial computation with no work</p>

#### [ Andrew Ashworth (Sep 19 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134265376):
<p><code>transfer</code> is a tactic, used in core lean to prove various properties of integers</p>

#### [ Patrick Massot (Sep 19 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134265497):
<p>Kevin, you heard about it in Orsay</p>

#### [ Kevin Buzzard (Sep 19 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134265731):
<p>Oh I remember! I hadn't put two and two together.</p>

#### [ Patrick Massot (Sep 19 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134266139):
<p>This fight against @ is epic. Did I tell you I forgot to assume both uniformities on β are complete and separated?</p>

#### [ Patrick Massot (Sep 19 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134266198):
<p>I tried to cut my proof into so many tiny lemmas that I forgot to copy-paste a couple of assumptions</p>

#### [ Patrick Massot (Sep 19 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134266574):
<p><code>set_option pp.all true</code> is my only ally</p>

#### [ Patrick Massot (Sep 19 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134266643):
<p><code>rewrite tactic failed, motive is not type correct nested exception message: check failed, application type mismatch (use 'set_option trace.check true' for additional details)</code> is my enemy</p>

#### [ Kevin Buzzard (Sep 19 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134266705):
<p>Now I am confused about why something which transfers proofs from N x N to Z can help. I think I need to think about how transfer actually works. But with the beta gamma approach there are no @s at all and you can just use type class inference as usual.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134266720):
<p>In fact I would be tempted to see how much you can do with beta not assumed equal to gamma and not ever prove anything with beta = gamma unless you absolutely have to.</p>

#### [ Patrick Massot (Sep 19 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134266778):
<p>You can try to prove the lemma if you want (without forgetting to assume both structures on target are complete and separated)</p>

#### [ Johannes Hölzl (Sep 19 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134266850):
<p><code>transfer</code> doesn't require an equivalence, just a relation and proofs about terms related terms. That's how proofs about <code>Z</code> can be reduced to proofs about <code>N x N</code></p>

#### [ Kevin Buzzard (Sep 19 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267045):
<p>I guess I would need to know the maths statement and proof...</p>

#### [ Patrick Massot (Sep 19 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267138):
<p>Here is the real world story (using A and B instead of greek letters for typing convenience). We have A with a fixed uniform structure, and B with two complete separated uniform structure u and u', which induce the same topology on B. We have e : A to B which is a uniform embedding into (B, u) with dense image. We assume e is uniformly continuous from A to (B, u'). Hence it can be extended by continuity to some uniformly continuous e0 from (B, u) to (B, u'). Since e0 \circ e = e, we learn the e0 is the identity on the image of e. But the later is dense, so by continuity, e0 = Id. So we learned that Id is uniformly continuous from (B, u) to (B, u'), QED.</p>

#### [ Patrick Massot (Sep 19 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267191):
<p>As is often the case, the paper I have in front of me contains only an annotated commutative diagram.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267273):
<p>Can we work on this together at cocalc (possibly at different times)?</p>

#### [ Kevin Buzzard (Sep 19 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267286):
<p>or is it easier just to spam the chat with gists?</p>

#### [ Patrick Massot (Sep 19 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267302):
<p>Here my full Lean so far:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">uniform_space</span>

<span class="kn">open</span> <span class="n">set</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>

<span class="n">def</span> <span class="n">unif_emb</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">u_α</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">u_β</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="n">uniform_embedding</span> <span class="n">f</span>

<span class="n">def</span> <span class="n">unif_cont</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">u_α</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">u_β</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="n">uniform_continuous</span> <span class="n">f</span>

<span class="n">def</span> <span class="n">top</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">):=</span> <span class="n">u</span><span class="bp">.</span><span class="n">to_topological_space</span>

<span class="n">def</span> <span class="n">complete</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">complete_space</span> <span class="n">α</span>

<span class="n">def</span> <span class="n">hausdorff</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">separated</span> <span class="n">α</span>

<span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">all</span> <span class="n">true</span>
<span class="kn">lemma</span> <span class="n">uniform_continuous_id_of_emb</span> <span class="o">[</span><span class="n">uα</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">u&#39;</span> <span class="n">u</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">β</span><span class="o">)</span>
  <span class="o">[</span><span class="n">cu</span> <span class="o">:</span> <span class="n">complete</span> <span class="n">u</span><span class="o">]</span> <span class="o">[</span><span class="n">hu</span> <span class="o">:</span> <span class="n">hausdorff</span> <span class="n">u</span><span class="o">]</span> <span class="o">[</span><span class="n">cu&#39;</span> <span class="o">:</span> <span class="n">complete</span> <span class="n">u&#39;</span><span class="o">]</span> <span class="o">[</span><span class="n">hu&#39;</span> <span class="o">:</span> <span class="n">hausdorff</span> <span class="n">u&#39;</span><span class="o">]</span> <span class="o">(</span><span class="n">htop</span> <span class="o">:</span> <span class="n">top</span> <span class="n">u</span> <span class="bp">=</span> <span class="n">top</span> <span class="n">u&#39;</span><span class="o">)</span>
  <span class="o">{</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">ue</span> <span class="o">:</span> <span class="n">unif_emb</span> <span class="n">uα</span> <span class="n">u</span> <span class="n">e</span><span class="o">)</span> <span class="o">(</span><span class="n">dense</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">closure</span> <span class="o">(</span><span class="n">range</span> <span class="n">e</span><span class="o">))</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">unif_cont</span> <span class="n">uα</span> <span class="n">u&#39;</span> <span class="n">e</span><span class="o">)</span> <span class="o">:</span>  <span class="n">u</span> <span class="bp">≤</span> <span class="n">u&#39;</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">let</span> <span class="n">e₀</span> <span class="o">:=</span> <span class="o">(</span><span class="n">ue</span><span class="bp">.</span><span class="n">dense_embedding</span> <span class="n">dense</span><span class="o">)</span><span class="bp">.</span><span class="n">extend</span> <span class="n">e</span><span class="o">,</span>
  <span class="n">haveI</span> <span class="o">:</span> <span class="n">separated</span> <span class="n">β</span> <span class="o">:=</span> <span class="n">hu</span><span class="o">,</span>
  <span class="k">have</span> <span class="o">:</span> <span class="n">unif_cont</span> <span class="n">u</span> <span class="n">u&#39;</span> <span class="n">e₀</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">dsimp</span> <span class="o">[</span><span class="n">unif_cont</span><span class="o">,</span> <span class="n">e₀</span><span class="o">],</span>
    <span class="k">have</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">uniform_continuous_uniformly_extend</span> <span class="n">β</span> <span class="n">α</span> <span class="n">β</span> <span class="n">u</span> <span class="n">uα</span> <span class="n">u&#39;</span> <span class="n">e</span> <span class="n">ue</span> <span class="n">dense</span> <span class="n">e</span> <span class="n">h</span> <span class="n">cu&#39;</span> <span class="n">hu&#39;</span><span class="o">,</span>
    <span class="n">dsimp</span> <span class="o">[</span><span class="n">top</span><span class="o">]</span> <span class="n">at</span> <span class="n">htop</span><span class="o">,</span>

    <span class="n">sorry</span> <span class="o">},</span>

  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Sep 19 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267307):
<p>I am trying to help my daughter with biology homework, clean the kitchen, eat some dinner and prove a lemma</p>

#### [ Patrick Massot (Sep 19 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267315):
<p>A CoCalc effort would probably be fun</p>

#### [ Patrick Massot (Sep 19 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267377):
<p>As you can see, I tried to hide a bunch of @ in new definitions which simply change binders</p>

#### [ Patrick Massot (Sep 19 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267413):
<p>The bad side is we need <code>dsimp</code> then</p>

#### [ Mario Carneiro (Sep 19 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267624):
<p>That real world proof looks applicable where the types are different. The only tricky bit is "generating the same topology", but I think this just means that the equiv is a quotient map (in the topological sense)</p>

#### [ Patrick Massot (Sep 19 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267625):
<p>The relevant part of state is then</p>
<div class="codehilite"><pre><span></span><span class="n">this</span> <span class="o">:</span>
  <span class="bp">@</span><span class="n">uniform_continuous</span><span class="bp">.</span><span class="o">{</span><span class="n">u_2</span> <span class="n">u_2</span><span class="o">}</span> <span class="n">β</span> <span class="n">β</span> <span class="n">u</span> <span class="n">u&#39;</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">dense_embedding</span><span class="bp">.</span><span class="n">extend</span><span class="bp">.</span><span class="o">{</span><span class="n">u_1</span> <span class="n">u_2</span> <span class="n">u_2</span><span class="o">}</span> <span class="n">α</span> <span class="n">β</span> <span class="n">β</span> <span class="o">(</span><span class="bp">@</span><span class="n">uniform_space</span><span class="bp">.</span><span class="n">to_topological_space</span><span class="bp">.</span><span class="o">{</span><span class="n">u_1</span><span class="o">}</span> <span class="n">α</span> <span class="n">uα</span><span class="o">)</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">uniform_space</span><span class="bp">.</span><span class="n">to_topological_space</span><span class="bp">.</span><span class="o">{</span><span class="n">u_2</span><span class="o">}</span> <span class="n">β</span> <span class="n">u</span><span class="o">)</span>
       <span class="n">e</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">uniform_space</span><span class="bp">.</span><span class="n">to_topological_space</span><span class="bp">.</span><span class="o">{</span><span class="n">u_2</span><span class="o">}</span> <span class="n">β</span> <span class="n">u&#39;</span><span class="o">)</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">uniform_embedding</span><span class="bp">.</span><span class="n">dense_embedding</span><span class="bp">.</span><span class="o">{</span><span class="n">u_1</span> <span class="n">u_2</span><span class="o">}</span> <span class="n">α</span> <span class="n">β</span> <span class="n">uα</span> <span class="n">u</span> <span class="n">e</span> <span class="n">ue</span> <span class="n">dense</span><span class="o">)</span>
       <span class="n">e</span><span class="o">),</span>
<span class="n">htop</span> <span class="o">:</span>
  <span class="bp">@</span><span class="n">eq</span><span class="bp">.</span><span class="o">{</span><span class="n">u_2</span><span class="bp">+</span><span class="mi">1</span><span class="o">}</span> <span class="o">(</span><span class="n">topological_space</span><span class="bp">.</span><span class="o">{</span><span class="n">u_2</span><span class="o">}</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">uniform_space</span><span class="bp">.</span><span class="n">to_topological_space</span><span class="bp">.</span><span class="o">{</span><span class="n">u_2</span><span class="o">}</span> <span class="n">β</span> <span class="n">u</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">uniform_space</span><span class="bp">.</span><span class="n">to_topological_space</span><span class="bp">.</span><span class="o">{</span><span class="n">u_2</span><span class="o">}</span> <span class="n">β</span> <span class="n">u&#39;</span><span class="o">)</span>
<span class="err">⊢</span> <span class="bp">@</span><span class="n">uniform_continuous</span><span class="bp">.</span><span class="o">{</span><span class="n">u_2</span> <span class="n">u_2</span><span class="o">}</span> <span class="n">β</span> <span class="n">β</span> <span class="n">u</span> <span class="n">u&#39;</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">dense_embedding</span><span class="bp">.</span><span class="n">extend</span><span class="bp">.</span><span class="o">{</span><span class="n">u_1</span> <span class="n">u_2</span> <span class="n">u_2</span><span class="o">}</span> <span class="n">α</span> <span class="n">β</span> <span class="n">β</span> <span class="o">(</span><span class="bp">@</span><span class="n">uniform_space</span><span class="bp">.</span><span class="n">to_topological_space</span><span class="bp">.</span><span class="o">{</span><span class="n">u_1</span><span class="o">}</span> <span class="n">α</span> <span class="n">uα</span><span class="o">)</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">uniform_space</span><span class="bp">.</span><span class="n">to_topological_space</span><span class="bp">.</span><span class="o">{</span><span class="n">u_2</span><span class="o">}</span> <span class="n">β</span> <span class="n">u</span><span class="o">)</span>
       <span class="n">e</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">uniform_space</span><span class="bp">.</span><span class="n">to_topological_space</span><span class="bp">.</span><span class="o">{</span><span class="n">u_2</span><span class="o">}</span> <span class="n">β</span> <span class="n">u</span><span class="o">)</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">uniform_embedding</span><span class="bp">.</span><span class="n">dense_embedding</span><span class="bp">.</span><span class="o">{</span><span class="n">u_1</span> <span class="n">u_2</span><span class="o">}</span> <span class="n">α</span> <span class="n">β</span> <span class="n">uα</span> <span class="n">u</span> <span class="n">e</span> <span class="n">ue</span> <span class="n">dense</span><span class="o">)</span>
       <span class="n">e</span><span class="o">)</span>
</pre></div>


<p>So it looks like <code>rwa htop at this</code> should close the goal, but I get a that nasty error instead</p>

#### [ Patrick Massot (Sep 19 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267727):
<p>(deleted)</p>

#### [ Kevin Buzzard (Sep 19 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267732):
<p>Here is the version which is written in what I believe is the correct generality (using A and B and C instead of greek letters for typing convenience). We have A, B, C uniform spaces, with B and C uniform and complete, and a homeo j : B -&gt; C.  We have e : A to B which is a uniform embedding into B with dense image. We assume j circ e is uniformly continuous from A to C. Hence it can be extended by continuity to some uniformly continuous j' from B to C. Since j = j' on e(A), j = j' and hence j is uniformly continuous from B to C, QED <em>without a single @</em></p>

#### [ Patrick Massot (Sep 19 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267846):
<p>I'll try to prove that tomorrow, but I fear this is only pushing the pain to the moment I will need to apply the lemma</p>

#### [ Mario Carneiro (Sep 19 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267863):
<p>we need the theorem that <code>id</code> is uniformly continuous from <code>u</code> to <code>u'</code> iff <code>u &lt;= u'</code></p>

#### [ Mario Carneiro (Sep 19 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267879):
<p>that is the only part that really needs <code>@</code> work, and the proof is trivial using <code>map_id</code> on filters</p>

#### [ Patrick Massot (Sep 19 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267939):
<p>Sure, we need this id stuff.</p>

#### [ Patrick Massot (Sep 19 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267956):
<p>But I don't understand the next sentence</p>

#### [ Patrick Massot (Sep 19 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268016):
<p>And I don't understand why rewrite doesn't work in my attempt.</p>

#### [ Johannes Hölzl (Sep 19 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268122):
<p>uniform continuity works on pairs of function, i.e. you need to prove <code>(λx:α×α, (x.1, x.2)) = id</code></p>

#### [ Johannes Hölzl (Sep 19 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268196):
<p>and then unfold <code>uniform_continuity</code> and rewrite with this equality</p>

#### [ Patrick Massot (Sep 19 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268304):
<p>Sure, but this is completely orthogonal to my problem, right?</p>

#### [ Patrick Massot (Sep 19 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268321):
<p>I'm far away from having that id is uniformly continuous here</p>

#### [ Kevin Buzzard (Sep 19 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268507):
<p>Do we have homeomorphisms in the strong sense of a continuous equiv with a continuous inverse?</p>

#### [ Johannes Hölzl (Sep 19 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268530):
<p>no :(</p>

#### [ Patrick Massot (Sep 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268631):
<p><a href="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/homeos.lean" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/homeos.lean">https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/homeos.lean</a></p>

#### [ Patrick Massot (Sep 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268639):
<p>Would you like to get this in mathlib?</p>

#### [ Patrick Massot (Sep 19 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268698):
<p>I need to go sleeping, but don't hesitate to unblock this. I hope I could then imitate the solution in many other such lemmas</p>

#### [ Kevin Buzzard (Sep 19 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268794):
<p>Patrick here is the statement with beta ne gamma:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">uniform_continuous_id_of_emb&#39;</span> <span class="o">[</span><span class="n">uα</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">γ</span><span class="o">]</span>
  <span class="o">[</span><span class="n">complete_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">separated</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">complete_space</span> <span class="n">γ</span><span class="o">]</span> <span class="o">[</span><span class="n">separated</span> <span class="n">γ</span><span class="o">]</span> <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">β</span> <span class="n">γ</span><span class="o">)</span> <span class="c1">-- need cts</span>
  <span class="o">{</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">ue</span> <span class="o">:</span> <span class="n">uniform_embedding</span> <span class="n">e</span><span class="o">)</span> <span class="o">(</span><span class="n">dense</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">closure</span> <span class="o">(</span><span class="n">range</span> <span class="n">e</span><span class="o">))</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="o">(</span><span class="n">j</span> <span class="err">∘</span> <span class="n">e</span><span class="o">))</span> <span class="o">:</span>  <span class="n">uniform_continuous</span> <span class="n">j</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>I had to use none of your five binder-changing defs</p>

#### [ Patrick Massot (Sep 19 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134269048):
<p>Weird! My rewrite now works</p>

#### [ Patrick Massot (Sep 19 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134269054):
<p>I wanted to try one more time. I have no idea what changed</p>

#### [ Patrick Massot (Sep 19 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134269137):
<p>Thanks Kevin. I'll definitely try this road tomorrow</p>

#### [ Patrick Massot (Sep 19 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134269145):
<p>But, as I wrote earlier, I think it's important enough that I try several things</p>

#### [ Johannes Hölzl (Sep 19 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134269235):
<p>wait, does the statement hold at all?</p>

#### [ Johannes Hölzl (Sep 19 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134269249):
<p>How do you want to prove it? (ah, reading your previous description)</p>

#### [ Johannes Hölzl (Sep 19 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134269434):
<div class="codehilite"><pre><span></span>  <span class="k">have</span> <span class="o">:</span> <span class="n">unif_cont</span> <span class="n">u</span> <span class="n">u&#39;</span> <span class="n">e₀</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">dsimp</span> <span class="o">[</span><span class="n">unif_cont</span><span class="o">,</span> <span class="n">e₀</span><span class="o">],</span>
    <span class="k">have</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">uniform_continuous_uniformly_extend</span> <span class="n">β</span> <span class="n">α</span> <span class="n">β</span> <span class="n">u</span> <span class="n">uα</span> <span class="n">u&#39;</span> <span class="n">e</span> <span class="n">ue</span> <span class="n">dense</span> <span class="n">e</span> <span class="n">h</span> <span class="n">cu&#39;</span> <span class="n">hu&#39;</span><span class="o">,</span>
    <span class="n">dsimp</span> <span class="o">[</span><span class="n">top</span><span class="o">]</span> <span class="n">at</span> <span class="n">htop</span><span class="o">,</span>
    <span class="n">rwa</span> <span class="o">[</span><span class="n">htop</span><span class="o">]</span> <span class="o">{</span><span class="n">occs</span> <span class="o">:=</span> <span class="n">occurrences</span><span class="bp">.</span><span class="n">pos</span> <span class="o">[</span><span class="mi">2</span><span class="o">]}</span> <span class="o">},</span>
</pre></div>


<p>the have can be proved fixing the occurence. I guess the <code>e₀ = id</code> proof doesn't mention any uniformities?</p>

#### [ Kevin Buzzard (Sep 19 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134269643):
<p>Oh -- I should add that my formalisation is not quite correct because the <code>equiv</code> should be a <code>homeo</code></p>

#### [ Kevin Buzzard (Sep 19 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134269735):
<p>Hmm, we seem to need the theorem that <code>id</code> is uniformly continuous from <code>u</code> to <code>u'</code> iff <code>u &lt;= u'</code>. But I would rather prove a statement that an equiv is uniformly continuous iff some pushforward of a uniformity is <code>&lt;=</code> the other one. Is this already in Lean?</p>

#### [ Johannes Hölzl (Sep 19 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134269997):
<p>this holds by definitional equality. EDIT: no, it doesn't</p>

#### [ Kevin Buzzard (Sep 19 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134270448):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">unif_cont</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">u_α</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">u_β</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="n">uniform_continuous</span> <span class="n">f</span>
</pre></div>


<p>Is this OK if alpha = beta? I'm not so sure. I think type class inference chooses the same uniform structure twice. <span class="user-mention" data-user-id="110031">@Patrick Massot</span> I think there's a bug here. Thoughts anyone?</p>

#### [ Johannes Hölzl (Sep 19 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134270861):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">uniform_continuous_iff</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">}</span> <span class="o">[</span><span class="n">uα</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">uβ</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">):</span>
  <span class="n">uniform_continuous</span> <span class="n">f</span> <span class="bp">↔</span> <span class="n">uβ</span><span class="bp">.</span><span class="n">comap</span> <span class="n">f</span> <span class="bp">≤</span> <span class="n">uα</span> <span class="o">:=</span>
<span class="n">filter</span><span class="bp">.</span><span class="n">map_le_iff_le_comap</span>
</pre></div>

#### [ Johannes Hölzl (Sep 19 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134271113):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> the content of <code>unif_cont</code> is fully elaborated. The elaborator doesn't do a type class search when it is used in <code>uniform_continuous_id_of_emb</code></p>

#### [ Kevin Buzzard (Sep 19 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134271209):
<p>Oh I see. So it's Ok.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134271228):
<p>As you can see, I am still coming to terms with my new knowledge about how typeclass inference works. Patrick -- sorry -- it's Ok.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134271543):
<p>Patrick's version --</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">uniform_continuous_id_of_emb</span> <span class="o">[</span><span class="n">uα</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">u&#39;</span> <span class="n">u</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">β</span><span class="o">)</span>
  <span class="o">[</span><span class="n">cu</span> <span class="o">:</span> <span class="n">complete</span> <span class="n">u</span><span class="o">]</span> <span class="o">[</span><span class="n">hu</span> <span class="o">:</span> <span class="n">hausdorff</span> <span class="n">u</span><span class="o">]</span> <span class="o">[</span><span class="n">cu&#39;</span> <span class="o">:</span> <span class="n">complete</span> <span class="n">u&#39;</span><span class="o">]</span> <span class="o">[</span><span class="n">hu&#39;</span> <span class="o">:</span> <span class="n">hausdorff</span> <span class="n">u&#39;</span><span class="o">]</span> <span class="o">(</span><span class="n">htop</span> <span class="o">:</span> <span class="n">top</span> <span class="n">u</span> <span class="bp">=</span> <span class="n">top</span> <span class="n">u&#39;</span><span class="o">)</span>
  <span class="o">{</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">ue</span> <span class="o">:</span> <span class="n">unif_emb</span> <span class="n">uα</span> <span class="n">u</span> <span class="n">e</span><span class="o">)</span> <span class="o">(</span><span class="n">dense</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">closure</span> <span class="o">(</span><span class="n">range</span> <span class="n">e</span><span class="o">))</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">unif_cont</span> <span class="n">uα</span> <span class="n">u&#39;</span> <span class="n">e</span><span class="o">)</span> <span class="o">:</span>  <span class="n">u</span> <span class="bp">≤</span> <span class="n">u&#39;</span> <span class="o">:=</span>
</pre></div>


<p>Should the conclusion be <code>u' &lt;= u</code>? I'm not an expert in uniform spaces.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134271658):
<p>I ask because Patrick seemed to be saying that the conclusion was that id was continuous from u to u', and Johannes seems to want to conclude from this that <code>u' &lt;= u</code>. But this could easily be some situation where <code>&lt;=</code> is defined as <code>&gt;=</code> for some people (as far as I know)</p>

#### [ Kevin Buzzard (Sep 20 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134272056):
<p>There is no <code>uniform_space.comap_id</code> :-(</p>

#### [ Kevin Buzzard (Sep 20 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134274017):
<p>gaargh there seems to be no <code>ext</code></p>

#### [ Kevin Buzzard (Sep 20 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134274344):
<p><code>⊢ u' = uniform_space.comap id u'</code></p>

#### [ Kevin Buzzard (Sep 20 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134275140):
<blockquote>
<div class="codehilite"><pre><span></span>  <span class="k">have</span> <span class="o">:</span> <span class="n">unif_cont</span> <span class="n">u</span> <span class="n">u&#39;</span> <span class="n">e₀</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">dsimp</span> <span class="o">[</span><span class="n">unif_cont</span><span class="o">,</span> <span class="n">e₀</span><span class="o">],</span>
    <span class="k">have</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">uniform_continuous_uniformly_extend</span> <span class="n">β</span> <span class="n">α</span> <span class="n">β</span> <span class="n">u</span> <span class="n">uα</span> <span class="n">u&#39;</span> <span class="n">e</span> <span class="n">ue</span> <span class="n">dense</span> <span class="n">e</span> <span class="n">h</span> <span class="n">cu&#39;</span> <span class="n">hu&#39;</span><span class="o">,</span>
    <span class="n">dsimp</span> <span class="o">[</span><span class="n">top</span><span class="o">]</span> <span class="n">at</span> <span class="n">htop</span><span class="o">,</span>
    <span class="n">rwa</span> <span class="o">[</span><span class="n">htop</span><span class="o">]</span> <span class="o">{</span><span class="n">occs</span> <span class="o">:=</span> <span class="n">occurrences</span><span class="bp">.</span><span class="n">pos</span> <span class="o">[</span><span class="mi">2</span><span class="o">]}</span> <span class="o">},</span>
</pre></div>


</blockquote>
<p>With the gamma version it's just</p>
<div class="codehilite"><pre><span></span>  <span class="k">let</span> <span class="n">e₀</span> <span class="o">:=</span> <span class="o">(</span><span class="n">ue</span><span class="bp">.</span><span class="n">dense_embedding</span> <span class="n">dense</span><span class="o">)</span><span class="bp">.</span><span class="n">extend</span> <span class="o">(</span><span class="n">j</span> <span class="err">∘</span> <span class="n">e</span><span class="o">),</span>
  <span class="k">have</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">e₀</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">dsimp</span> <span class="o">[</span><span class="n">unif_cont</span><span class="o">,</span> <span class="n">e₀</span><span class="o">],</span>
    <span class="n">exact</span> <span class="n">uniform_continuous_uniformly_extend</span> <span class="n">ue</span> <span class="n">dense</span> <span class="n">h</span><span class="o">,</span>
  <span class="o">},</span>
</pre></div>

#### [ Kevin Buzzard (Sep 20 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134275198):
<p>Everything is easier this way, switching to gamma is a no-brainer</p>

#### [ Kevin Buzzard (Sep 20 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134275275):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">uniform_space</span>

<span class="kn">open</span> <span class="n">set</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>

<span class="kn">lemma</span> <span class="n">uniform_continuous_id_of_emb&#39;</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">γ</span><span class="o">]</span>
  <span class="o">[</span><span class="n">complete_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">separated</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">complete_space</span> <span class="n">γ</span><span class="o">]</span> <span class="o">[</span><span class="n">separated</span> <span class="n">γ</span><span class="o">]</span> <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">β</span> <span class="n">γ</span><span class="o">)</span> <span class="c1">-- need continuity assumption</span>
  <span class="o">{</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">ue</span> <span class="o">:</span> <span class="n">uniform_embedding</span> <span class="n">e</span><span class="o">)</span> <span class="o">(</span><span class="n">dense</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">closure</span> <span class="o">(</span><span class="n">range</span> <span class="n">e</span><span class="o">))</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="o">(</span><span class="n">j</span> <span class="err">∘</span> <span class="n">e</span><span class="o">))</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">j</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">let</span> <span class="n">e₀</span> <span class="o">:=</span> <span class="o">(</span><span class="n">ue</span><span class="bp">.</span><span class="n">dense_embedding</span> <span class="n">dense</span><span class="o">)</span><span class="bp">.</span><span class="n">extend</span> <span class="o">(</span><span class="n">j</span> <span class="err">∘</span> <span class="n">e</span><span class="o">),</span>
  <span class="k">have</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">e₀</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">dsimp</span> <span class="o">[</span><span class="n">e₀</span><span class="o">],</span>
    <span class="n">exact</span> <span class="n">uniform_continuous_uniformly_extend</span> <span class="n">ue</span> <span class="n">dense</span> <span class="n">h</span><span class="o">,</span>
  <span class="o">},</span>
  <span class="n">sorry</span> <span class="c1">-- I need that j is a homeo and this isn&#39;t in the assumptions</span>
<span class="kn">end</span>
</pre></div>


<p>but it's bedtime now</p>

#### [ Kevin Buzzard (Sep 20 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134275281):
<p>and we need to say that <code>j</code> is a homeo not just an equiv.</p>

#### [ Kevin Buzzard (Sep 20 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134275359):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">uniform_continuous_iff</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">}</span> <span class="o">[</span><span class="n">uα</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">uβ</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">):</span>
  <span class="n">uniform_continuous</span> <span class="n">f</span> <span class="bp">↔</span> <span class="n">uβ</span><span class="bp">.</span><span class="n">comap</span> <span class="n">f</span> <span class="bp">≤</span> <span class="n">uα</span> <span class="o">:=</span>
<span class="n">filter</span><span class="bp">.</span><span class="n">map_le_iff_le_comap</span>

<span class="n">def</span> <span class="n">unif_emb</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">u_α</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">u_β</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="n">uniform_embedding</span> <span class="n">f</span>

<span class="n">def</span> <span class="n">unif_cont</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">u_α</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">u_β</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="n">uniform_continuous</span> <span class="n">f</span>

<span class="n">def</span> <span class="n">top</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">):=</span> <span class="n">u</span><span class="bp">.</span><span class="n">to_topological_space</span>

<span class="n">def</span> <span class="n">complete</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">complete_space</span> <span class="n">α</span>

<span class="n">def</span> <span class="n">hausdorff</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">separated</span> <span class="n">α</span>

<span class="kn">lemma</span> <span class="n">uniform_continuous_id_of_emb</span> <span class="o">[</span><span class="n">uα</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">u&#39;</span> <span class="n">u</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">β</span><span class="o">)</span>
  <span class="o">[</span><span class="n">cu</span> <span class="o">:</span> <span class="n">complete</span> <span class="n">u</span><span class="o">]</span> <span class="o">[</span><span class="n">hu</span> <span class="o">:</span> <span class="n">hausdorff</span> <span class="n">u</span><span class="o">]</span> <span class="o">[</span><span class="n">cu&#39;</span> <span class="o">:</span> <span class="n">complete</span> <span class="n">u&#39;</span><span class="o">]</span> <span class="o">[</span><span class="n">hu&#39;</span> <span class="o">:</span> <span class="n">hausdorff</span> <span class="n">u&#39;</span><span class="o">]</span> <span class="o">(</span><span class="n">htop</span> <span class="o">:</span> <span class="n">top</span> <span class="n">u</span> <span class="bp">=</span> <span class="n">top</span> <span class="n">u&#39;</span><span class="o">)</span>
  <span class="o">{</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">ue</span> <span class="o">:</span> <span class="n">unif_emb</span> <span class="n">uα</span> <span class="n">u</span> <span class="n">e</span><span class="o">)</span> <span class="o">(</span><span class="n">dense</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">closure</span> <span class="o">(</span><span class="n">range</span> <span class="n">e</span><span class="o">))</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">unif_cont</span> <span class="n">uα</span> <span class="n">u&#39;</span> <span class="n">e</span><span class="o">)</span> <span class="o">:</span>  <span class="n">u&#39;</span> <span class="bp">≤</span> <span class="n">u</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:</span> <span class="n">unif_cont</span> <span class="n">u</span> <span class="n">u&#39;</span> <span class="n">id</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">uniform_continuous_id_of_emb&#39;</span> <span class="n">α</span> <span class="n">β</span> <span class="n">β</span> <span class="n">uα</span> <span class="n">u</span> <span class="n">u&#39;</span> <span class="n">cu</span> <span class="n">hu</span> <span class="n">cu&#39;</span> <span class="n">hu&#39;</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">refl</span> <span class="n">β</span><span class="o">)</span> <span class="n">e</span> <span class="n">ue</span> <span class="n">dense</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">unif_cont</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">uniform_continuous_iff</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">convert</span> <span class="n">H</span><span class="o">,</span>
  <span class="c1">-- ⊢ u&#39; = uniform_space.comap id u&#39;</span>
  <span class="c1">-- should be trivial?</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Sep 20 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134275590):
<p><code>  have : uniform_continuous e₀ :=
    uniform_continuous_uniformly_extend ue dense h,</code></p>

#### [ Patrick Massot (Sep 20 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291887):
<p>Indeed it seems the following is missing:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">id_prod</span> <span class="o">:</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">α</span><span class="o">),</span> <span class="o">(</span><span class="n">p</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span><span class="o">))</span> <span class="bp">=</span> <span class="n">id</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">ext</span> <span class="bp">;</span> <span class="n">simp</span>

<span class="n">attribute</span> <span class="o">[</span><span class="n">extensionality</span><span class="o">]</span> <span class="n">uniform_space_eq</span>

<span class="kn">lemma</span> <span class="n">uniform_space_comap_id</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">:</span> <span class="n">uniform_space</span><span class="bp">.</span><span class="n">comap</span> <span class="o">(</span><span class="n">id</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="n">id</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">ext</span> <span class="n">u</span><span class="o">,</span>
  <span class="n">dsimp</span> <span class="o">[</span><span class="n">uniform_space</span><span class="bp">.</span><span class="n">comap</span><span class="o">],</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">id_prod</span><span class="o">,</span> <span class="n">filter</span><span class="bp">.</span><span class="n">comap_id</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>


<p>The first one is strange, but I couldn't find it <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> any thought?</p>

#### [ Patrick Massot (Sep 20 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291938):
<p>Should we add this to mathlib? make the first one a simp lemma?</p>

#### [ Johannes Hölzl (Sep 20 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291941):
<p>you mean <code>id_prod</code>? I don't think we have it yet</p>

#### [ Patrick Massot (Sep 20 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291947):
<p>Yes, id_prod</p>

#### [ Kevin Buzzard (Sep 20 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291951):
<p>I feel like a child collecting football cards again</p>

#### [ Kevin Buzzard (Sep 20 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291955):
<p>great excitement when we discover a new basic lemma we don't have</p>

#### [ Patrick Massot (Sep 20 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291967):
<p>simp or not simp?</p>

#### [ Johannes Hölzl (Sep 20 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291968):
<p>I guess we will never run out of basic lemmas</p>

#### [ Johannes Hölzl (Sep 20 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291971):
<p>currently I'm in favor of not simp</p>

#### [ Kevin Buzzard (Sep 20 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291975):
<p>I ran out of football cards once; I remember the joy of getting the last one. Bryan Flynn, Leeds United.</p>

#### [ Johannes Hölzl (Sep 20 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291976):
<p>I don't think we have a lot of eta-rule like these in the simp-set. And it might get confusing. But then this rule is quiet nice...</p>

#### [ Kevin Buzzard (Sep 20 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134292015):
<p>But I thought we would ultimately find that every basic lemma is either easy or has a tactic-free and simple proof</p>

#### [ Patrick Massot (Sep 20 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134292016):
<p>What about tagging uniform_space_eq?</p>

#### [ Johannes Hölzl (Sep 20 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134292107):
<p>yes, <code>uniform_space_eq</code> should be tagged with <code>@[extensionality]</code>.</p>

#### [ Patrick Massot (Sep 20 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134292424):
<p>Ok, I first PR'ed id_prod, then I'll do the other two</p>

#### [ Johannes Hölzl (Sep 20 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134292533):
<p>just waiting for Travis</p>

#### [ Patrick Massot (Sep 20 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316246):
<p>Quick update on this topic: mathlib got <a href="https://github.com/leanprover/mathlib/commit/d0f1b21a9df64f48a8d28203bf292eb80e05a6da" target="_blank" title="https://github.com/leanprover/mathlib/commit/d0f1b21a9df64f48a8d28203bf292eb80e05a6da">https://github.com/leanprover/mathlib/commit/d0f1b21a9df64f48a8d28203bf292eb80e05a6da</a> and <a href="https://github.com/leanprover/mathlib/commit/1da8cc51854c2e75f456878b195b162dc8dbb130" target="_blank" title="https://github.com/leanprover/mathlib/commit/1da8cc51854c2e75f456878b195b162dc8dbb130">https://github.com/leanprover/mathlib/commit/1da8cc51854c2e75f456878b195b162dc8dbb130</a> then I added <a href="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/homeos.lean" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/homeos.lean">https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/homeos.lean</a> to the perfectoid project (I think I still don't whether mathlib wants it). We can then write the two versions of the lemma (following my real life sketch and Kevin's Lean  start) as:</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">set</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>

<span class="kn">lemma</span> <span class="n">uniform_continuous_id_of_emb&#39;</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">γ</span><span class="o">]</span>
  <span class="o">[</span><span class="n">complete_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">separated</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">complete_space</span> <span class="n">γ</span><span class="o">]</span> <span class="o">[</span><span class="n">separated</span> <span class="n">γ</span><span class="o">]</span> <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">homeo</span> <span class="n">β</span> <span class="n">γ</span><span class="o">)</span>
  <span class="o">{</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">ue</span> <span class="o">:</span> <span class="n">uniform_embedding</span> <span class="n">e</span><span class="o">)</span> <span class="o">(</span><span class="n">dense</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">closure</span> <span class="o">(</span><span class="n">range</span> <span class="n">e</span><span class="o">))</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="o">(</span><span class="n">j</span> <span class="err">∘</span> <span class="n">e</span><span class="o">))</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">j</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">let</span> <span class="n">e₀</span> <span class="o">:=</span> <span class="o">(</span><span class="n">ue</span><span class="bp">.</span><span class="n">dense_embedding</span> <span class="n">dense</span><span class="o">)</span><span class="bp">.</span><span class="n">extend</span> <span class="o">(</span><span class="n">j</span> <span class="err">∘</span> <span class="n">e</span><span class="o">),</span>
  <span class="k">have</span> <span class="n">uc_e₀</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">e₀</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">dsimp</span> <span class="o">[</span><span class="n">e₀</span><span class="o">],</span>
    <span class="n">exact</span> <span class="n">uniform_continuous_uniformly_extend</span> <span class="n">ue</span> <span class="n">dense</span> <span class="n">h</span> <span class="o">},</span>
  <span class="n">convert</span> <span class="n">uc_e₀</span><span class="o">,</span>
  <span class="n">ext</span> <span class="n">b</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">closed</span> <span class="o">:</span> <span class="n">is_closed</span> <span class="o">{</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">|</span> <span class="n">j</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">e₀</span> <span class="n">b</span><span class="o">}</span> <span class="o">:=</span> <span class="o">(</span><span class="n">is_closed_eq</span> <span class="n">j</span><span class="bp">.</span><span class="n">fun_con</span> <span class="n">uc_e₀</span><span class="bp">.</span><span class="n">continuous</span><span class="o">),</span>
  <span class="k">have</span> <span class="n">dense&#39;</span> <span class="o">:</span> <span class="n">closure</span> <span class="o">(</span><span class="n">range</span> <span class="n">e</span><span class="o">)</span> <span class="bp">=</span> <span class="n">univ</span><span class="o">,</span> <span class="k">by</span> <span class="n">rwa</span> <span class="n">eq_univ_iff_forall</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">is_closed_property</span> <span class="n">dense&#39;</span> <span class="n">closed</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="err">$</span> <span class="n">uniformly_extend_of_emb</span> <span class="n">ue</span> <span class="n">dense</span> <span class="n">h</span><span class="o">)</span>
<span class="kn">end</span>

<span class="n">def</span> <span class="n">unif_emb</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">u_α</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">u_β</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="n">uniform_embedding</span> <span class="n">f</span>

<span class="n">def</span> <span class="n">unif_cont</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">u_α</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">u_β</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="n">uniform_continuous</span> <span class="n">f</span>

<span class="n">def</span> <span class="n">top</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">):=</span> <span class="n">u</span><span class="bp">.</span><span class="n">to_topological_space</span>

<span class="n">def</span> <span class="n">complete</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">complete_space</span> <span class="n">α</span>

<span class="n">def</span> <span class="n">hausdorff</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">separated</span> <span class="n">α</span>

<span class="kn">lemma</span> <span class="n">uniform_continuous_id_of_emb</span> <span class="o">[</span><span class="n">uα</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">u&#39;</span> <span class="n">u</span> <span class="o">:</span> <span class="n">uniform_space</span> <span class="n">β</span><span class="o">)</span>
  <span class="o">[</span><span class="n">cu</span> <span class="o">:</span> <span class="n">complete</span> <span class="n">u</span><span class="o">]</span> <span class="o">[</span><span class="n">hu</span> <span class="o">:</span> <span class="n">hausdorff</span> <span class="n">u</span><span class="o">]</span> <span class="o">[</span><span class="n">cu&#39;</span> <span class="o">:</span> <span class="n">complete</span> <span class="n">u&#39;</span><span class="o">]</span> <span class="o">[</span><span class="n">hu&#39;</span> <span class="o">:</span> <span class="n">hausdorff</span> <span class="n">u&#39;</span><span class="o">]</span> <span class="o">(</span><span class="n">htop</span> <span class="o">:</span> <span class="n">top</span> <span class="n">u</span> <span class="bp">=</span> <span class="n">top</span> <span class="n">u&#39;</span><span class="o">)</span>
  <span class="o">{</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">ue</span> <span class="o">:</span> <span class="n">unif_emb</span> <span class="n">uα</span> <span class="n">u</span> <span class="n">e</span><span class="o">)</span> <span class="o">(</span><span class="n">dense</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">closure</span> <span class="o">(</span><span class="n">range</span> <span class="n">e</span><span class="o">))</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">unif_cont</span> <span class="n">uα</span> <span class="n">u&#39;</span> <span class="n">e</span><span class="o">)</span> <span class="o">:</span>  <span class="n">u&#39;</span> <span class="bp">≤</span> <span class="n">u</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">let</span> <span class="n">iduu&#39;</span> <span class="o">:</span> <span class="bp">@</span><span class="n">homeo</span> <span class="n">β</span> <span class="n">β</span> <span class="o">(</span><span class="n">top</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">top</span> <span class="n">u&#39;</span><span class="o">)</span> <span class="o">:=</span>
  <span class="o">{</span> <span class="n">to_fun</span> <span class="o">:=</span> <span class="n">id</span><span class="o">,</span>
    <span class="n">inv_fun</span> <span class="o">:=</span> <span class="n">id</span><span class="o">,</span>
    <span class="n">left_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
    <span class="n">right_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
    <span class="n">fun_con</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="err">←</span><span class="n">htop</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">continuous_id</span><span class="o">,</span>
    <span class="n">inv_con</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="err">←</span><span class="n">htop</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">continuous_id</span> <span class="o">},</span>

  <span class="n">rw</span> <span class="k">show</span> <span class="n">e</span> <span class="bp">=</span> <span class="n">iduu&#39;</span> <span class="err">∘</span> <span class="n">e</span><span class="o">,</span> <span class="k">by</span> <span class="n">refl</span> <span class="n">at</span> <span class="n">h</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">uniform_continuous_id_of_emb&#39;</span> <span class="n">α</span> <span class="n">β</span> <span class="n">β</span> <span class="n">uα</span> <span class="n">u</span> <span class="n">u&#39;</span> <span class="n">cu</span> <span class="n">hu</span> <span class="n">cu&#39;</span> <span class="n">hu&#39;</span> <span class="n">iduu&#39;</span> <span class="n">e</span> <span class="n">ue</span> <span class="n">dense</span> <span class="n">h</span><span class="o">,</span>

  <span class="n">rw</span> <span class="n">uniform_continuous_iff</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">convert</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">rw</span> <span class="k">show</span> <span class="o">(</span><span class="n">iduu&#39;</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="bp">=</span> <span class="n">id</span><span class="o">,</span> <span class="k">by</span> <span class="n">refl</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">uniform_space_comap_id</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Sep 20 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316471):
<p>Of course the first proof has no @, we are not fighting mathlib here. The second one is not too bad in my opinion. The statement is clean, because of the "rebinded" definitions, which cost nothing in the proof.</p>

#### [ Patrick Massot (Sep 20 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316535):
<p>The main @ thing is the definition of the identity seen as a homeo between different topologies, which costs two slightly awkwards <code>rw show ..., by refl</code>.</p>

#### [ Patrick Massot (Sep 20 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316601):
<p>What do you guys think about all this?</p>

#### [ Mario Carneiro (Sep 20 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316684):
<p>I think the identity homeo should be a theorem</p>

#### [ Patrick Massot (Sep 20 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316753):
<p>Stating what?</p>

#### [ Mario Carneiro (Sep 20 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316771):
<p>just like the theorem that identity is continuous iff the topologies are le, the identity is a homeo iff the topologies are eq</p>

#### [ Patrick Massot (Sep 20 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316811):
<p>This bundled definition of a homeo doesn't seem so nice when it comes to stating that some map is a homeo</p>

#### [ Mario Carneiro (Sep 20 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316836):
<p>this is true. Maybe settle for one direction, the one you proved</p>

#### [ Mario Carneiro (Sep 20 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316920):
<p>The reverse direction says that if <code>f : homeo A A T1 T2</code> and <code>f x = x</code> for all <code>x</code>, then <code>T1 = T2</code></p>

#### [ Patrick Massot (Sep 20 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316930):
<p>So it would be a <code>def</code>, not a <code>lemma</code>, right?</p>

#### [ Mario Carneiro (Sep 20 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316939):
<p>yes</p>

#### [ Mario Carneiro (Sep 20 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317018):
<p>After all this refactoring, I would ask whether you really need <code>uniform_continuous_id_of_emb</code> though</p>

#### [ Mario Carneiro (Sep 20 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317045):
<p>we treated it as the endgame but maybe you can avoid le on uniformities to begin with</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317110):
<p>I was wondering the same</p>

#### [ Patrick Massot (Sep 20 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317111):
<p>Of course this is also a legitimate question. But this thread is also used as an exercise in type class hell survival.</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317153):
<p>Patrick's original question was whether the completion of a top group "equalled" (in a mathematician-like way) the completion of the underlying uniform space. But these two completions are just two different types so you could instead ask if they are uniform-equiv, not that this exists.</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317201):
<p>On the other hand Johannes, if I recall correctly, put a bunch of stuff in <code>topological_space.lean</code> about different topologies on the same space...</p>

#### [ Patrick Massot (Sep 20 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317202):
<p>What do you mean "different types"?</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317249):
<p>Isn't there one "complete-a-group" function which completes a group and spits out one type, and one "complete-a-uniform-space" function which completes a uniform space and spits out a second type? And we think of them as "equal" but they're two different types. That's all I mean, and you know all this already.</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317315):
<p>I was wondering if you ever needed to compare two uniformities on the same type, but I don't know the full story</p>

#### [ Patrick Massot (Sep 20 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317340):
<p>No, there is a complete a uniform space structure, an instance saying that the result has a uniform structure, and there are instances saying that abelian top groups are uniform spaces, and that the completion of a group is a top group</p>

#### [ Patrick Massot (Sep 20 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317355):
<p>The full story is still at <a href="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean#L124" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean#L124">https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean#L124</a></p>

#### [ Patrick Massot (Sep 20 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317382):
<p>and <a href="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/group_completion.lean#L118" target="_blank" title="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/group_completion.lean#L118">https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/group_completion.lean#L118</a> of course (maybe with tiny differences)</p>

#### [ Patrick Massot (Sep 20 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317454):
<p>So we really have two uniform space structures on the same type. But of course I wonder whether I could cook up more functions to hide things to the type class system</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317655):
<p>So should that line 124 even make sense?</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317662):
<p>That's what I'm thinking</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317668):
<p>Given some top group H</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317670):
<p>there is an associated uniform space which is also H</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317685):
<p>but then isn't there <code>topological_add_group.completion H</code> (one type) and <code>uniform_space.completion H</code> (a different type)?</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317756):
<p>And then maybe you prove a theorem saying that two uniform structures are the same</p>

#### [ Mario Carneiro (Sep 20 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317768):
<p>I guess there is a single (uniform) completion operation which additionally has the property that it lifts topological group structure</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317774):
<p>right, but should it be like that?</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317777):
<p>should the theorem be that there's a uniform space equiv?</p>

#### [ Mario Carneiro (Sep 20 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317778):
<p>Obviously <code>topological_group</code> should have a uniform component so that this can be by defeq</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317847):
<blockquote>
<p>Obviously <code>topological_group</code> should have a uniform component</p>
</blockquote>
<p>This is when it gets silly.</p>

#### [ Patrick Massot (Sep 20 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317853):
<p>The theorem that is sorried there has mathematical content, it won't become trivial</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317857):
<p>right</p>

#### [ Patrick Massot (Sep 20 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317866):
<p>So I don't know what Mario wants to see defeq</p>

#### [ Mario Carneiro (Sep 20 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317867):
<p>of course, the content is shifted to the definition of the topological group</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317879):
<p>Is there no way of making all this sensible?</p>

#### [ Mario Carneiro (Sep 20 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317884):
<p>There are zero cases where you want a topological group with a uniform structure that doesn't agree with it</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317890):
<p>It's like the product of metric spaces example, but it's even better, because we don't even have to take a product.</p>

#### [ Patrick Massot (Sep 20 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317894):
<p>Except for non-commutative groups where there are two choices</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317895):
<p>rofl</p>

#### [ Patrick Massot (Sep 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317944):
<p>Left uniformity and right uniformity</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317945):
<p>two different uniformities giving the same topology, right?</p>

#### [ Patrick Massot (Sep 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317950):
<p>sure</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317959):
<p>Let's cross that bridge when we come to it</p>

#### [ Patrick Massot (Sep 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317960):
<p>I assumed everything was commutative because I aimed for addition in rings</p>

#### [ Patrick Massot (Sep 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317964):
<p>and it was complicated enough</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317967):
<p>I want to end up in a situation where there are no diamonds. Is this possible?</p>

#### [ Mario Carneiro (Sep 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317977):
<p>yes</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317978):
<p>Given a uniform space I want to be able to complete it</p>

#### [ Patrick Massot (Sep 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317982):
<p>I don't mind seeing the uniform structure as part of the abelian top group</p>

#### [ Mario Carneiro (Sep 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317985):
<p>I assume you mean the diamonds commute by defeq</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317987):
<p>yes</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318005):
<p>What I was thinking is that the group completion should have a different name.</p>

#### [ Patrick Massot (Sep 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318006):
<p>But I don't see how this will help when proving the actual theorem, even if this proof is now part of the construction of the top group instance</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318053):
<p>this is not supposed to help proving the theorem</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318059):
<p>yes I was just wondering about how to make the theorem part of the infrastructure. Is this just clear to both of you?</p>

#### [ Patrick Massot (Sep 20 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318060):
<p>I mean help in the Lean sense, not maths sense</p>

#### [ Patrick Massot (Sep 20 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318076):
<p>Nothing is clear to me here (except the proof I see on paper in front of me)</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318084):
<p>I want to give the top group completion a different name, make it a different type to the uniform space completion</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318110):
<p>hmm but it still has to be a top group</p>

#### [ Mario Carneiro (Sep 20 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318113):
<p>It will make that <code>same_uniformity</code> theorem true by defeq, so you won't have to muck about with rewriting instance arguments</p>

#### [ Mario Carneiro (Sep 20 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318165):
<p>But it's true that the theorem still has to be proved, and it is an equality of uniformities</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318169):
<p>top groups and uniform spaces -- they are going to be classes, right? Let's make that assumption</p>

#### [ Mario Carneiro (Sep 20 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318172):
<p>yes, are they not already?</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318173):
<p>And there's always going to be an instance from top group to uniform space, right?</p>

#### [ Mario Carneiro (Sep 20 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318174):
<p>right</p>

#### [ Patrick Massot (Sep 20 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318184):
<p>but it may be generated by <code>extends</code></p>

#### [ Mario Carneiro (Sep 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318198):
<p>?</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318208):
<p>and will a top group definitely have a uniformity component?</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318215):
<p>so the instance is a forgetful functor?</p>

#### [ Patrick Massot (Sep 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318219):
<p>If <code>class top_group extends uniform_space</code></p>

#### [ Mario Carneiro (Sep 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318222):
<p>right</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318225):
<p>But with the completion construction</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318230):
<p>you can insert the theorem into the construction, can you not?</p>

#### [ Mario Carneiro (Sep 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318236):
<p>yes, that's the idea</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318239):
<p>right</p>

#### [ Kevin Buzzard (Sep 20 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318313):
<p>so the top group completion <em>must</em> have the "uniform space generated by the top group structure" uniform space</p>

#### [ Patrick Massot (Sep 20 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318321):
<p>So the gain would be when I wanted to use the <code>same_uniformity</code> theorem, in <a href="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean#L161" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean#L161">https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean#L161</a> not when I want to prove it</p>

#### [ Mario Carneiro (Sep 20 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318401):
<p>yes</p>

#### [ Patrick Massot (Sep 20 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318406):
<p>sounds very good</p>

#### [ Kevin Buzzard (Sep 20 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318411):
<p>I think I'm there</p>

#### [ Patrick Massot (Sep 20 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318434):
<p>Kevin, do you want to know why we need this theorem? It's easy to explain</p>

#### [ Patrick Massot (Sep 20 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318451):
<p>Mario, the trouble is I tried to do this "top_group extends uniform space" trick after the Orsay meeting but couldn't handle everything that broke when I started</p>

#### [ Kevin Buzzard (Sep 20 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318512):
<p>I can see for maths reasons why we want to prove the two uniformities are equal.</p>

#### [ Kevin Buzzard (Sep 20 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318529):
<p>What I was thinking about was how all this could play well with the type class system.</p>

#### [ Kevin Buzzard (Sep 20 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318544):
<p>That is exactly why I changed your beta,beta to beta,gamma, because then the theorem you were struggling on suddenly seemed much easier</p>

#### [ Patrick Massot (Sep 20 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318545):
<p>ok, we're on the same page</p>

#### [ Kevin Buzzard (Sep 20 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318717):
<p>but if topological_group extends uniform_space (I don't know if it does or if it should) then we have to be careful, but it sounds like it's OK. I guess it doesn't matter whether it extends or not -- you probably still want an instance. Eew. Is top group -&gt; uniform space -&gt; top space defeq to top group -&gt; top space?</p>

#### [ Patrick Massot (Sep 20 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318744):
<p>Yes, I made sure this is true back in June</p>

#### [ Kevin Buzzard (Sep 20 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318765):
<p>It's ridiculous that this sort of thing is important. I think the system is not quite fit for purpose.</p>

#### [ Patrick Massot (Sep 20 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318790):
<p><a href="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L353" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L353">https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L353</a></p>

#### [ Kevin Buzzard (Sep 20 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318805):
<p>I'm with Chris. He had trouble with two instances which were provably equivalent but not defeq. There should be a way to make this work by brandishing a theorem at the type class inference system and saying "use this if stuck"</p>

#### [ Patrick Massot (Sep 20 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318890):
<blockquote>
<p>just like the theorem that identity is continuous iff the topologies are le</p>
</blockquote>
<p>Do we actually have this theorem in mathlib? I can't find it</p>

#### [ Kevin Buzzard (Sep 20 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318891):
<p>It would be wonderful if the default setting was "if it's a class, then you will have one instance and that's the end of it. If there are two instances, then you had better supply the proof that they're the same"</p>

#### [ Kevin Buzzard (Sep 20 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318900):
<p>and you had to explicitly switch this off.</p>

#### [ Patrick Massot (Sep 20 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134319419):
<p>Let's try to use the existing Lean. <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what do you suggest I should do? Should I try to refactor everything about commutative additive top groups? Should I start with <code>class topological_abelian_group (α : Type u) extends uniform_space α, add_comm_group α</code>?</p>

#### [ Patrick Massot (Sep 20 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134319450):
<p>and then prove an instance converting this to the existing topological group classes?</p>

#### [ Kevin Buzzard (Sep 20 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134320701):
<p>he'll make you call it <code>topological_add_comm_group</code></p>

#### [ Mario Carneiro (Sep 20 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134321783):
<p>I'm okay with saying <code>top</code> instead of <code>topological</code></p>

#### [ Mario Carneiro (Sep 20 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134321834):
<p>exactly because you want to stack adjectives like this</p>

#### [ Patrick Massot (Sep 20 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134324250):
<p>What about my question?</p>

#### [ Mario Carneiro (Sep 20 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134325399):
<p>I hate to answer a question like that with yes, but yes</p>

#### [ Mario Carneiro (Sep 20 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134325445):
<p>then again, I think <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> had a part in the original formulation so maybe he should say something here</p>

#### [ Patrick Massot (Sep 20 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134325826):
<blockquote>
<p>I hate to answer a question like that with yes, but yes</p>
</blockquote>
<p>What would you prefer?</p>

#### [ Mario Carneiro (Sep 20 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134326342):
<p>what you said: a class <code>top_add_comm_group</code> that extends <code>uniform_space</code> and <code>add_comm_group</code></p>

#### [ Patrick Massot (Sep 21 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134377971):
<p>I tried various things today, but clearly I'm not doing it right. Recall I defined the Hausdorff completion functor in <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/master/src/for_mathlib/completion.lean" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/master/src/for_mathlib/completion.lean">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/master/src/for_mathlib/completion.lean</a> I also defined a uniform structure on commutative topological groups in <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/master/src/for_mathlib/topological_structures.lean#L109" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/master/src/for_mathlib/topological_structures.lean#L109">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/master/src/for_mathlib/topological_structures.lean#L109</a>, and wanted to get a group completion functor. For this it seems we need closer integration of topological groups and uniform structures. I made a first attempt at <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/e44b49e7bd9f77f59246f725cc38bf879c2af50f/src/for_mathlib/top_groups.lean" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/e44b49e7bd9f77f59246f725cc38bf879c2af50f/src/for_mathlib/top_groups.lean">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/e44b49e7bd9f77f59246f725cc38bf879c2af50f/src/for_mathlib/top_groups.lean</a> There I have an axiom relating a uniform structure and a group structure, but the uniform structure is a parameter. There are only two sorries in that file, and the completion stuff is available right from the beginning, seemingly without diamond issue. However I'd like a way to produce a <code>top_add_comm_group</code> from a topological space structure and a group structure, building the uniform space structure automatically using a version of my previous unbundled work. I don't see how to do that. Then I tried <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/master/src/for_mathlib/top_groups.lean" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/master/src/for_mathlib/top_groups.lean">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/master/src/for_mathlib/top_groups.lean</a> where the only parameter of <code>top_add_comm_group</code> is the carrier type. But then I had to setup much more wrapping around my completion stuff, and <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/master/src/for_mathlib/top_groups.lean#L45" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/master/src/for_mathlib/top_groups.lean#L45">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/master/src/for_mathlib/top_groups.lean#L45</a> completely fails. I really need help from <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>  or <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> in order to now which attempt (if any) goes in the right direction.</p>

#### [ Johannes Hölzl (Sep 21 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134391084):
<p>I'm taking a look at it</p>

#### [ Johannes Hölzl (Sep 22 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134432236):
<p>Do you need <code>topological_add_group</code> in your definition of <code>top_add_comm_group</code>? Shouldn't <code>topological_add_group</code> be derived from <code>unif_group</code>?</p>

#### [ Patrick Massot (Sep 22 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134434646):
<p>You're probably right</p>

#### [ Johannes Hölzl (Sep 22 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134434933):
<p>I forked your repo: <a href="https://github.com/johoelzl/lean-perfectoid-spaces" target="_blank" title="https://github.com/johoelzl/lean-perfectoid-spaces">https://github.com/johoelzl/lean-perfectoid-spaces</a></p>

#### [ Johannes Hölzl (Sep 22 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134434980):
<p>So in <code>top_groups</code> you need to prove that the group is a group, and then that the uniformity fits</p>

#### [ Johannes Hölzl (Sep 22 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134435010):
<p>first we need to show that <code>-</code> and <code>+</code> are (uniform) continuous, and reduce to <code>-</code>, <code>+</code> on <code>G</code> under <code>to_completion</code>. Then we can proof the group properties by the embedding along <code>to_completion</code>.</p>

#### [ Johannes Hölzl (Sep 22 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134435042):
<p>is this what you expected or do you want something different?</p>

#### [ Patrick Massot (Sep 22 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134435676):
<p>I want to be able to manipulate topological groups and their completions. The mathematical story is extremely clear, and I already formalized large parts of it, but they don't want to fit together. Have you seen my two recent attempts? There are successive commits. The older attempts are in neighboring files. Would you like me to LaTeX the math story?</p>

#### [ Johannes Hölzl (Sep 22 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134435734):
<p>I think LaTeX is not yet necessary. But what kind of manipulations do you want to make?</p>

#### [ Patrick Massot (Sep 22 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134435834):
<p>The same thing we want from the beginning: a completion functor, left adjoint to the inclusion of complete hausdorff group into all topological groups. That's all!</p>

#### [ Patrick Massot (Sep 22 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134435843):
<p>We do have it for uniform space, in my <code>completion.lean</code></p>

#### [ Johannes Hölzl (Sep 22 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134435897):
<p>hm, this is a little bit too far for me. but you are currently stuck in proving that the completion of a topological group (with the induced uniformity) is again a group. This is what I see in <code>top_groups</code>. is this correct?</p>

#### [ Johannes Hölzl (Sep 22 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134435910):
<p>or did you just <code>sorry</code> this part, because you wanted to see how this way works for later proofs?</p>

#### [ Patrick Massot (Sep 22 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134436031):
<p>The key fact is we start with a completion which is a universal solution to the problem of factoring maps into complete hausdorff spaces:</p>
<ul>
<li><a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L51" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L51">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L51</a></li>
<li><a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L132" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L132">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L132</a></li>
<li><a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L157" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L157">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L157</a></li>
<li><a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L171" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L171">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L171</a><br>
Then the action of the completion functor on maps comes for free: <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L144" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L144">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L144</a></li>
</ul>
<p>When moving to topological groups, we want all those maps to be group morphisms. It looks like extending operation by continuity and running the same abstract non-sense will do it without any work. But when you think about how to prove that <code>completion.map f</code> is a group morphisms you see you need commutation of the two constructions (from top group to uniform space and from uniform space to completion)</p>

#### [ Johannes Hölzl (Sep 22 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134436032):
<p>so what I propose is:</p>
<ul>
<li>we get obviously that <code>group_completion G</code> is a complete, separated uniformity (and everything we know about them). This is a couple of instances.</li>
<li>then we proof that it is a <code>group</code>. This requires some work, we need to lift the group operations and show that they are uniform and invariant under coerion</li>
</ul>

#### [ Patrick Massot (Sep 22 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134436086):
<p>I did all that in my first attempt in <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/topological_structures.lean" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/topological_structures.lean">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/topological_structures.lean</a></p>

#### [ Patrick Massot (Sep 22 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134436096):
<p>But then the last instance fail completely because of the diamond issue, and even sorrying an equality of uniform structures didn't help because I couldn't manage rewriting instances</p>

#### [ Patrick Massot (Sep 22 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134436140):
<p>I'm sorry I need to take care of my family. But in any case I don't think this problem can be solved without investing some time into reading my various attempts</p>

#### [ Patrick Massot (Sep 22 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134436141):
<p>Thank you very much for trying to help me</p>

#### [ Kevin Buzzard (Sep 22 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134436154):
<p>I am of course actively interested in making all this work so let me know if I can help somehow.</p>

#### [ Johannes Hölzl (Sep 22 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134446757):
<p>So it turns out that <code>top_add_comm_group</code> is equivalent to <code>uniform_add_group</code>. From <code>uniform_add_group</code> we can derive <code>uniformity = comap (λx:α×α, x.2 - x.1) (nhds (0:α))</code>.</p>
<p>so the only complicated lift is the group structure itself</p>

#### [ Patrick Massot (Sep 24 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134515389):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> I see you made some progress in your fork. Are you still working on this? Or do you think I should try to copy your work and try to proceed?</p>

#### [ Johannes Hölzl (Sep 24 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134515432):
<p>I didn't continue on this yet. But I want to continue today</p>

#### [ Patrick Massot (Sep 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134515457):
<p>In particular, does it mean you think that the definition of <code>top_add_comm_group</code> is the correct starting point, and wrapping the completion stuff in <code>group_completion</code> is the right thing to do?</p>

#### [ Patrick Massot (Sep 24 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134515513):
<p>Ok, great. I'll wait and see then</p>

#### [ Johannes Hölzl (Sep 24 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134515522):
<p>But I think I will take a look again at your <code>completion</code> branch in <code>leanprover-community</code>.</p>

#### [ Johannes Hölzl (Sep 24 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134515619):
<p>I think <code>top_add_comm_group</code> is not necessary. I think <code>uniform_add_group</code> can also be used instead of it.</p>

#### [ Johannes Hölzl (Sep 24 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134515669):
<p>But if you want you can finish the proofs in <code>top_groups.lean</code>. In the meantime I look at your <code>completion</code> branch and try to bring it up to current <code>mathlib</code> and see how I want to merge it. What do you think about this?</p>

#### [ Patrick Massot (Sep 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134515861):
<p>I still don't understand what is <code>uniform_add_group</code> This notion doesn't exist in real world maths, and it seems equivalent to topological groups, at least in the communtative case. What's the point?</p>

#### [ Johannes Hölzl (Sep 24 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134516035):
<p>The difference is just that <code>topological_add_group</code> doesn't know about its uniformity. So I called the type class which requires the uniformity <code>uniform_add_group</code>. We can change <code>topological_add_group</code> to require an uniform space, and change the axiom to assume that <code>-</code> is uniformly continuous.</p>

#### [ Johannes Hölzl (Sep 24 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134516077):
<p>The difference to <code>top_add_comm_group</code> will be that <code>topological_add_group</code> is still unbundled.</p>

#### [ Patrick Massot (Sep 24 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134516170):
<p>I don't understand. What is unbundled?</p>

#### [ Johannes Hölzl (Sep 24 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134516284):
<p>Okay, <strong>bundled</strong> is not the right word in this context. What I mean is that <code>topological_add_group</code> has the topology and the group structure as <strong>parameter</strong>. <code>top_add_group</code> has it as the uniformity and its group as fields in its structure.</p>

#### [ Patrick Massot (Sep 24 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134516888):
<p>I'm sorry this conversation is not smoother, but my youngest daughter is sick, and I have to take care of her</p>

#### [ Patrick Massot (Sep 24 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134516966):
<p>The point of the "bundled" version was to try to make sure the work of proving the uniform structure compatibility in group completions would be hidden in the instance building, and would never be an issue afterwards</p>

#### [ Patrick Massot (Sep 24 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134517026):
<p>But of course this version needs a constructor which only takes group law axioms, a topology and a bunch of continuity proofs, in the same way as a metric space can be constructed from a distance without providing a uniformity</p>

#### [ Johannes Hölzl (Sep 24 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134517460):
<p>I will see how much of the actual construction can be hidden. Also, note that I will rebase your <code>completions</code> branch in <code>leanprover-community</code> after lunch. I hope you don't have any local changes</p>

#### [ Patrick Massot (Sep 24 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134517551):
<p>It's a bit of a mess that this work is somewhat split between this mathlib branch and the prefectoid repository, but I think the only substantial difference is the new <code>top_groups.lean</code> in the perfectoid repository, so you can work on the community mathlib branch</p>

#### [ Patrick Massot (Sep 24 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134522077):
<p>I worked a bit, see <a href="https://github.com/johoelzl/lean-perfectoid-spaces/compare/master...PatrickMassot:master" target="_blank" title="https://github.com/johoelzl/lean-perfectoid-spaces/compare/master...PatrickMassot:master">https://github.com/johoelzl/lean-perfectoid-spaces/compare/master...PatrickMassot:master</a> I unsorried the <code>add_comm_group</code> structure by porting my previous work. Hopefully this could save you some time. This required adding a couple of lemmas first. I tried to follow the mathlib convention in naming <code>group_completion.continuous_add</code> and <code>group_completion.continuous_add'</code> but I noticed you didn't. Also, I shortened the name since it's all in the <code>group_completion</code> namespace, but since the purely topological <code>continuous_add</code> is in root namespace, it's a but of a mess. Hopefully all this will be much simpler in the end</p>

#### [ Johannes Hölzl (Sep 24 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134522483):
<p>Thanks! I'm currently reorganizing <code>uniform_space.lean</code> and move the separated quotient type and <code>Cauchy</code> to <code>completions.lean</code>.</p>

#### [ Patrick Massot (Sep 24 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134522579):
<p>Great!</p>

#### [ Patrick Massot (Sep 24 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134522595):
<p>I'm very excited and grateful to get some help here</p>

#### [ Patrick Massot (Sep 24 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134524646):
<p>Also note that the proofs in <a href="https://github.com/johoelzl/lean-perfectoid-spaces/blob/fa721c6aa863c79b22ce463358c2b616c413e38c/src/for_mathlib/top_groups.lean#L194" target="_blank" title="https://github.com/johoelzl/lean-perfectoid-spaces/blob/fa721c6aa863c79b22ce463358c2b616c413e38c/src/for_mathlib/top_groups.lean#L194">https://github.com/johoelzl/lean-perfectoid-spaces/blob/fa721c6aa863c79b22ce463358c2b616c413e38c/src/for_mathlib/top_groups.lean#L194</a> are not as abstract as we'd like them to be. Ideally they would all follow from things like <a href="https://github.com/leanprover-community/mathlib/blob/a5da4d5acccc9910d921cfadb2c8e4cce59e1d80/analysis/topology/completion.lean#L726" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/a5da4d5acccc9910d921cfadb2c8e4cce59e1d80/analysis/topology/completion.lean#L726">https://github.com/leanprover-community/mathlib/blob/a5da4d5acccc9910d921cfadb2c8e4cce59e1d80/analysis/topology/completion.lean#L726</a>. So all topological argument would ultimately be in <a href="https://github.com/leanprover-community/mathlib/blob/a5da4d5acccc9910d921cfadb2c8e4cce59e1d80/analysis/topology/completion.lean#L552" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/a5da4d5acccc9910d921cfadb2c8e4cce59e1d80/analysis/topology/completion.lean#L552">https://github.com/leanprover-community/mathlib/blob/a5da4d5acccc9910d921cfadb2c8e4cce59e1d80/analysis/topology/completion.lean#L552</a>, as they should be. But the trouble is that group axioms in mathlib are stated as equalities between elements, instead of functions. So a lot of packing and unpacking would be required. I hesitated to setup all this, with a new group structure constructor inspired by <a href="https://en.wikipedia.org/wiki/Universal_algebra" target="_blank" title="https://en.wikipedia.org/wiki/Universal_algebra">universal algebra</a> but I preferred to move on.</p>

#### [ Johannes Hölzl (Sep 25 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134615079):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> I moved now most of the completion stiff to its own lean theory <code>analysis.topology.completion</code>. I added the group completion instances to the <code>completion</code> type itself. I guess this makes sense.<br>
the only thing missing is a nice setup for topological groups, where one only needs to define the zero nighbourhood and get a topological group, or where one proofs that we have a topological group and get the uniformity. This is currently in <code>analysis/topology/topological_groups</code> but needs to be restructured.</p>

#### [ Patrick Massot (Sep 25 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134619925):
<p>Thanks <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> It all looks nice, except that I still don't know what we are talking about. What is this theory of <code>uniform_add_group</code>? Is this meant to be only an intermediate definition? Is the missing piece the piece were you make connection with topological groups as they are defined in math books?</p>

#### [ Patrick Massot (Sep 25 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134620301):
<p>Also, I'm confused about when the diamond problem will return to hit us. The fact that the group uniform structure on the completion of a group is the completion of the group uniform structure is a non-empty mathematical content. In my approach it seemed necessary in order to get a functorial group completion. Where will this be needed in your way of building the theory?</p>

#### [ Johannes Hölzl (Sep 25 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134620397):
<p><code>uniform_add_group</code> is a technical device. I don't want to force each appearance of a topological group to be a uniform space. That's why it is split into a <code>topological_add_group</code> (topology + group) and <code>uniform_add_group</code> (uniformity + group). We know also that we can derive a canonical uniform space for a topological group, but this is not setup as a type class instance.</p>

#### [ Johannes Hölzl (Sep 25 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134620466):
<p>What is exactly the diamond? We have <code>add_group (completion A)</code> and <code>uniform_space (completion A)</code>. Both have currently only one way to construct them. What are the alternatives?</p>

#### [ Patrick Massot (Sep 25 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134620573):
<p><code>topological_add_group.to_uniform_space (completion A) = completion (topological_add_group.to_uniform_space A)</code></p>

#### [ Patrick Massot (Sep 25 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134620584):
<p>That's a non-empty mathematical result</p>

#### [ Johannes Hölzl (Sep 25 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134620608):
<p>but <code>topological_add_group.to_uniform_space</code> is currently not in our type class hierarchy</p>

#### [ Patrick Massot (Sep 25 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134620712):
<p>I don't understand why this theorem can be avoided while constructing the completion functor for commutative topological groups</p>

#### [ Patrick Massot (Sep 25 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134620730):
<p>It's independent of the discussion of have instances or def</p>

#### [ Johannes Hölzl (Sep 25 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134621075):
<p>With <code>uniformity_eq_comap_nhds_zero</code> (<a href="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L276" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L276">https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L276</a>) it should be easy to prove this. In the one direction this is how we define the uniformity, in the other direction we have a <code>uniform_add_group</code> and can use <code>uniformity_eq_comap_nhds_zero</code>.</p>
<p>But maybe I misunderstand the problem. I will try to prove this diamond tomorrow.</p>

#### [ Patrick Massot (Sep 25 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134621323):
<p>Ok, thank you very much. I would really love to see the finished thing (including the link with topological groups). I hope I'll be able to learn something from this, since I spend quite a lot of time thinking about more naive (ie. straight from maths books) approaches</p>

#### [ Patrick Massot (Sep 25 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134625736):
<p>Indeed <code>uniformity_eq_comap_nhds_zero</code> looks like a characterization of the uniform structure that could be very important. The first step of the proof looks like it has nothing to do with groups:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">johannes_lemma</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">α</span><span class="bp">×</span><span class="n">α</span><span class="o">)}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span><span class="o">},</span>
  <span class="n">uniform_continuous</span> <span class="o">(</span><span class="bp">λ</span><span class="n">p</span><span class="o">:</span><span class="n">α</span><span class="bp">×</span><span class="n">α</span><span class="o">,</span> <span class="n">f</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span> <span class="bp">→</span> <span class="n">s</span> <span class="err">∈</span> <span class="o">(</span><span class="bp">@</span><span class="n">uniformity</span> <span class="n">α</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">sets</span> <span class="bp">→</span>
  <span class="bp">∃</span> <span class="n">u</span> <span class="err">∈</span> <span class="o">(</span><span class="bp">@</span><span class="n">uniformity</span> <span class="n">α</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">sets</span><span class="o">,</span> <span class="bp">∀</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">,</span> <span class="o">(</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="err">∈</span> <span class="n">u</span> <span class="bp">→</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span> <span class="n">c</span><span class="o">,</span> <span class="n">f</span> <span class="n">b</span> <span class="n">c</span><span class="o">)</span> <span class="err">∈</span> <span class="n">s</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">assume</span> <span class="n">s</span> <span class="n">f</span> <span class="n">hf</span> <span class="n">hs</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">uniform_continuous</span><span class="o">,</span> <span class="n">uniformity_prod_eq_prod</span><span class="o">,</span> <span class="n">tendsto_map&#39;_iff</span><span class="o">,</span> <span class="o">(</span><span class="err">∘</span><span class="o">)]</span> <span class="n">at</span> <span class="n">hf</span><span class="o">,</span>
  <span class="n">rcases</span> <span class="n">mem_map_sets_iff</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">hf</span> <span class="n">hs</span><span class="o">)</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">t</span><span class="o">,</span> <span class="n">ht</span><span class="o">,</span> <span class="n">hts</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">clear</span> <span class="n">hf</span><span class="o">,</span>
  <span class="n">rcases</span> <span class="n">mem_prod_iff</span><span class="bp">.</span><span class="mi">1</span> <span class="n">ht</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">u</span><span class="o">,</span> <span class="n">hu</span><span class="o">,</span> <span class="n">v</span><span class="o">,</span> <span class="n">hv</span><span class="o">,</span> <span class="n">huvt</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">clear</span> <span class="n">ht</span><span class="o">,</span>
  <span class="n">refine</span> <span class="bp">⟨</span><span class="n">u</span><span class="o">,</span> <span class="n">hu</span><span class="o">,</span> <span class="k">assume</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">hab</span><span class="o">,</span> <span class="n">hts</span> <span class="err">$</span> <span class="o">(</span><span class="n">mem_image</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨⟨⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">c</span><span class="o">,</span> <span class="n">c</span><span class="bp">⟩⟩</span><span class="o">,</span> <span class="n">huvt</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="bp">_⟩</span><span class="o">,</span> <span class="bp">_⟩⟩</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">hab</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">refl_mem_uniformity</span> <span class="n">hv</span><span class="o">,</span>
  <span class="n">refl</span>
<span class="kn">end</span>
</pre></div>


<p>I don't know what would be a better mathlib name.</p>

#### [ Patrick Massot (Sep 25 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134625920):
<p>Better statement:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">johannes_lemma</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">β</span><span class="o">]</span>
<span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">β</span> <span class="bp">×</span> <span class="n">β</span><span class="o">)}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">},</span>
  <span class="n">uniform_continuous</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">α</span><span class="o">,</span> <span class="n">f</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span> <span class="bp">→</span> <span class="n">s</span> <span class="err">∈</span> <span class="o">(</span><span class="bp">@</span><span class="n">uniformity</span> <span class="n">β</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">sets</span> <span class="bp">→</span>
  <span class="bp">∃</span> <span class="n">u</span> <span class="err">∈</span> <span class="o">(</span><span class="bp">@</span><span class="n">uniformity</span> <span class="n">α</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">sets</span><span class="o">,</span> <span class="bp">∀</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">,</span> <span class="o">(</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="err">∈</span> <span class="n">u</span> <span class="bp">→</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span> <span class="n">c</span><span class="o">,</span> <span class="n">f</span> <span class="n">b</span> <span class="n">c</span><span class="o">)</span> <span class="err">∈</span> <span class="n">s</span> <span class="o">:=</span>
</pre></div>

#### [ Patrick Massot (Sep 25 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134625951):
<p>And I don't change any character from the proof! I love that. Usually when we wrote in real world math: "the same proof shows that..." it's a polite lie</p>

#### [ Patrick Massot (Sep 25 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134626147):
<p>Of course we can also write this as:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">johannes_lemma</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span>
<span class="o">:</span> <span class="n">uniform_continuous</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">α</span><span class="o">,</span> <span class="n">f</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">β</span> <span class="bp">×</span> <span class="n">β</span><span class="o">)},</span> <span class="n">s</span> <span class="err">∈</span> <span class="o">(</span><span class="bp">@</span><span class="n">uniformity</span> <span class="n">β</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">sets</span> <span class="bp">→</span>
  <span class="bp">∃</span> <span class="n">u</span> <span class="err">∈</span> <span class="o">(</span><span class="bp">@</span><span class="n">uniformity</span> <span class="n">α</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">sets</span><span class="o">,</span> <span class="bp">∀</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">,</span> <span class="o">(</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="err">∈</span> <span class="n">u</span> <span class="bp">→</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span> <span class="n">c</span><span class="o">,</span> <span class="n">f</span> <span class="n">b</span> <span class="n">c</span><span class="o">)</span> <span class="err">∈</span> <span class="n">s</span>
</pre></div>


<p>Isn't it an <code>iff</code> then?</p>

#### [ Reid Barton (Sep 25 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134626187):
<p>I'm trying to process the "better statement". Is it essentially saying that if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>:</mo><mi>A</mi><mo>×</mo><mi>A</mi><mo>→</mo><mi>B</mi></mrow><annotation encoding="application/x-tex">f : A \times A \to B</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mrel">:</span><span class="mord mathit">A</span><span class="mbin">×</span><span class="mord mathit">A</span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span> is uniformly continuous, then so is <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>(</mo><mo>−</mo><mo separator="true">,</mo><mi>c</mi><mo>)</mo><mo>:</mo><mi>A</mi><mo>→</mo><mi>B</mi></mrow><annotation encoding="application/x-tex">f(-, c) : A \to B</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord">−</span><span class="mpunct">,</span><span class="mord mathit">c</span><span class="mclose">)</span><span class="mrel">:</span><span class="mord mathit">A</span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span> for any <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>c</mi><mo>∈</mo><mi>A</mi></mrow><annotation encoding="application/x-tex">c \in A</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.72243em;vertical-align:-0.0391em;"></span><span class="base"><span class="mord mathit">c</span><span class="mrel">∈</span><span class="mord mathit">A</span></span></span></span>?</p>

#### [ Patrick Massot (Sep 25 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134626239):
<p>I'm also trying to process it</p>

#### [ Patrick Massot (Sep 25 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134626262):
<p>But I don't think it means what you wrote</p>

#### [ Patrick Massot (Sep 25 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134626280):
<p>but you may be right</p>

#### [ Reid Barton (Sep 25 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134626303):
<p>Oh no I am not right.</p>

#### [ Reid Barton (Sep 25 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134626314):
<p>I see. I had the quantifier involving <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>c</mi></mrow><annotation encoding="application/x-tex">c</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">c</span></span></span></span> in the wrong place.</p>

#### [ Patrick Massot (Sep 25 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134626333):
<p>Yeah, it's a tricky statement</p>

#### [ Patrick Massot (Sep 25 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134626410):
<p>Still there is an asymmetry between the two A factors, so it's probably not an iff</p>

#### [ Patrick Massot (Sep 25 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134627274):
<p>Anyway, this lemma, in its latest version allows to reduce the crucial proof to:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">uniformity_eq_comap_nhds_zero</span> <span class="o">:</span> <span class="n">uniformity</span> <span class="bp">=</span> <span class="n">comap</span> <span class="o">(</span><span class="bp">λ</span><span class="n">x</span><span class="o">:</span><span class="n">α</span><span class="bp">×</span><span class="n">α</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">-</span> <span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">nhds</span> <span class="o">(</span><span class="mi">0</span><span class="o">:</span><span class="n">α</span><span class="o">))</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">nhds_eq_comap_uniformity</span><span class="o">,</span> <span class="n">filter</span><span class="bp">.</span><span class="n">comap_comap_comp</span><span class="o">],</span>
  <span class="n">refine</span> <span class="n">le_antisymm</span> <span class="o">(</span><span class="n">filter</span><span class="bp">.</span><span class="n">map_le_iff_le_comap</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">;</span> <span class="n">intros</span> <span class="n">s</span> <span class="n">hs</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">rcases</span> <span class="n">johannes_lemma</span> <span class="n">uniform_continuous_sub&#39;</span> <span class="n">hs</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">t</span><span class="o">,</span> <span class="n">ht</span><span class="o">,</span> <span class="n">hts</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">refine</span> <span class="n">mem_map</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">mem_sets_of_superset</span> <span class="n">ht</span> <span class="bp">_</span><span class="o">),</span>
    <span class="n">rintros</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">simpa</span> <span class="o">[</span><span class="n">subset_def</span><span class="o">]</span> <span class="kn">using</span> <span class="n">hts</span> <span class="n">a</span> <span class="n">b</span> <span class="n">a</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">rcases</span> <span class="n">johannes_lemma</span> <span class="n">uniform_continuous_add&#39;</span> <span class="n">hs</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">t</span><span class="o">,</span> <span class="n">ht</span><span class="o">,</span> <span class="n">hts</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">refine</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">ht</span><span class="o">,</span> <span class="bp">_⟩</span><span class="o">,</span>
    <span class="n">rintros</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">subset_def</span><span class="o">]</span> <span class="kn">using</span> <span class="n">hts</span> <span class="mi">0</span> <span class="o">(</span><span class="n">b</span> <span class="bp">-</span> <span class="n">a</span><span class="o">)</span> <span class="n">a</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Sep 25 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134627304):
<p>And I still don't understand the magic trick that seems to have removed the diamond issue (I mean removed from the maths discussion, I'm not even talking about Lean). I guess I'll see it when everything will be in place.</p>

#### [ Patrick Massot (Sep 25 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134627409):
<p>I also don't understand at all <a href="https://github.com/leanprover-community/mathlib/commit/85b19e23d45f14a210d0b7491c66477d0c560c9a" target="_blank" title="https://github.com/leanprover-community/mathlib/commit/85b19e23d45f14a210d0b7491c66477d0c560c9a">https://github.com/leanprover-community/mathlib/commit/85b19e23d45f14a210d0b7491c66477d0c560c9a</a> Why did you remove all this? It contains a lot of maths that don't appear anywhere else</p>

#### [ Johannes Hölzl (Sep 26 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134652519):
<p>Urgs, I removed the wrong file.</p>

#### [ Patrick Massot (Sep 26 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134697940):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> Did you try to go from <code>topological_add_group</code> to the completion and still get everything?</p>

#### [ Mario Carneiro (Sep 26 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134698069):
<p>(deleted)</p>

#### [ Reid Barton (Sep 26 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134698176):
<p>Mario did you just respond to a question asked on the wrong topic with an answer posted on the wrong stream</p>

#### [ Mario Carneiro (Sep 26 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134698232):
<p>yes. yes I did.</p>

#### [ Patrick Massot (Sep 26 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134698240):
<p>This topic was only distantly related to separation stuff anyway</p>

#### [ Patrick Massot (Sep 26 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134698271):
<p>Somehow, deep down, I guess we miss Gitter's mess</p>

#### [ Patrick Massot (Sep 26 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134698719):
<p>The stuff about group topologies generated from a neighborhood filter around zero will probably be very convenient for the perfectoid project, which  uses adic topology</p>

#### [ Johannes Hölzl (Sep 26 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134699310):
<p>I didn't work yet on the diamond, I got side tracked by the topological space construction</p>

#### [ Patrick Massot (Sep 26 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134699347):
<p>Ok, I understand.</p>

#### [ Johannes Hölzl (Sep 27 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134731658):
<p>I added now <code>topological_add_comm_group.to_uniform_space_eq</code>. It doesn't look to be directly a diamond. The reason is the following:<br>
For <code>completion α</code> to be a group, we already need to know that <code>α</code> has a uniform space, and that the group structure is compatible with this uniformity (i.e. <code>uniform_add_group</code>).</p>
<p>A diamond would mean we have <code>group_to_uniform ∘ completion = completion ∘group_to_uniform</code>. But <code>completion</code> doesn't work on groups without the uniformity. So we actually have <code>group_to_uniform ∘ completion ∘group_to_uniform = completion ∘group_to_uniform</code>. Now it is enough to prove <code>group_to_uniform ∘ G = G</code>, where <code>G</code> is already a group with compatible uniformity.</p>


{% endraw %}
